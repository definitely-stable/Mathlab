"""DAG-002 G2-B2-C2-A: actual file-backed, directory-priced page-image store.

Reference implementation, not a production crash-safe index:
- data.bin and directory.bin are real page-aligned files (os.pread/pwrite);
- every key lookup reverse-scans the on-disk directory, counting its pages;
- bounded page-count LRU covers *both* directory and payload pages;
- immutable keys are enforced across restarts, mutable keys append versions;
- SHA-256 validates each loaded payload and rejects corrupt page contents.

Counters count os.pread/os.pwrite calls, NOT media read/write events.
Disk writes are NOT fsync'd; header/fstat/filesystem metadata syscall cost,
allocation, crash atomicity and true process RSS remain outside the model.
"""
from __future__ import annotations

from collections import OrderedDict
from dataclasses import dataclass
from hashlib import sha256
import os
import struct
from pathlib import Path

_MAGIC = b"D2FILE01"
_ENTRY = struct.Struct("<4sHHQQ32s64s")
_HEAD = struct.Struct("<8sII")
_VERSION = 1


@dataclass(frozen=True)
class Entry:
    key: str
    immutable: bool
    first_page: int
    payload_size: int
    digest: bytes


class FilePageStore:
    """Paid linear directory, real page I/O, LRU cap. No free name→page map."""
    def __init__(self, root: str | Path, page_bytes: int = 64,
                 cache_pages: int = 0):
        if page_bytes < 16 or cache_pages < 0:
            raise ValueError("invalid page size or cache")
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)
        self.page_bytes = page_bytes
        self.cache_pages = cache_pages
        self.slot_bytes = (( _ENTRY.size + page_bytes - 1) // page_bytes) * page_bytes
        self.cache: OrderedDict[tuple[str, int], bytes] = OrderedDict()
        self.max_cached_observed = 0
        self.read_requests = 0
        self.cache_hits = 0
        self.data_page_reads = 0
        self.directory_page_reads = 0
        self.data_page_writes = 0
        self.directory_page_writes = 0
        self.cache_evictions = 0
        self.os_metadata_calls = 0
        self.lookup_entries_examined = 0
        self._closed = False
        self._fds = {
            "data": os.open(self.root / "data.bin", os.O_CREAT | os.O_RDWR, 0o600),
            "directory": os.open(self.root / "directory.bin",
                                 os.O_CREAT | os.O_RDWR, 0o600),
        }
        try:
            length = self._size("directory")
            if length == 0:
                self._write_pages("directory", 0,
                    _HEAD.pack(_MAGIC, _VERSION, page_bytes)
                    .ljust(page_bytes, b"\0"))
            else:
                if length < page_bytes or (length-page_bytes) % self.slot_bytes:
                    raise ValueError("misaligned directory")
                head = self._read_page("directory", 0)
                magic, version, page = _HEAD.unpack_from(head)
                if (magic, version, page) != (_MAGIC, _VERSION, page_bytes):
                    raise ValueError("directory header mismatch")
            if self._size("data") % page_bytes:
                raise ValueError("misaligned data store")
        except Exception:
            self.close()
            raise

    def _size(self, kind: str) -> int:
        self.os_metadata_calls += 1
        return os.fstat(self._fds[kind]).st_size

    def _read_page(self, kind: str, page_number: int) -> bytes:
        identity = (kind, page_number)
        self.read_requests += 1
        if identity in self.cache:
            self.cache_hits += 1
            self.cache.move_to_end(identity)
            return self.cache[identity]
        image = os.pread(self._fds[kind], self.page_bytes,
                         page_number * self.page_bytes)
        if len(image) != self.page_bytes:
            raise IOError("truncated on-disk page")
        if kind == "data":
            self.data_page_reads += 1
        else:
            self.directory_page_reads += 1
        if self.cache_pages:
            self.cache[identity] = image
            if len(self.cache) > self.cache_pages:
                self.cache.popitem(last=False)
                self.cache_evictions += 1
            self.max_cached_observed = max(self.max_cached_observed,
                                           len(self.cache))
        return image

    def _read_pages(self, kind: str, offset: int, count: int) -> bytes:
        if offset % self.page_bytes or count < 1:
            raise ValueError("invalid aligned read")
        return b"".join(self._read_page(kind, offset // self.page_bytes + i)
                        for i in range(count))

    def _write_pages(self, kind: str, offset: int, payload: bytes) -> None:
        if offset % self.page_bytes or not payload or (
                len(payload) % self.page_bytes):
            raise ValueError("writes must be full aligned pages")
        fd = self._fds[kind]
        for i in range(0, len(payload), self.page_bytes):
            pos = offset + i
            chunk = payload[i:i+self.page_bytes]
            count = os.pwrite(fd, chunk, pos)
            if count != self.page_bytes:
                raise IOError("short page write")
            self.cache.pop((kind, pos // self.page_bytes), None)
            if kind == "data":
                self.data_page_writes += 1
            else:
                self.directory_page_writes += 1

    def _entry_count(self) -> int:
        length = self._size("directory")
        if length < self.page_bytes or (
                length-self.page_bytes) % self.slot_bytes:
            raise ValueError("invalid directory length")
        return (length - self.page_bytes) // self.slot_bytes

    def _lookup(self, key: str) -> Entry | None:
        if not isinstance(key, str) or not key or len(key.encode("utf-8")) > 64:
            raise ValueError("key must be 1..64 UTF-8 bytes")
        for i in range(self._entry_count()-1, -1, -1):
            offset = self.page_bytes + i * self.slot_bytes
            raw = self._read_pages("directory", offset,
                                   self.slot_bytes // self.page_bytes)
            self.lookup_entries_examined += 1
            magic, count, flags, first, size, digest, name = _ENTRY.unpack_from(raw)
            if magic != b"D2EN" or count > 64 or flags not in (0, 1):
                raise ValueError("corrupt directory entry")
            if any(name[count:]):
                raise ValueError("noncanonical directory name")
            label = name[:count].decode("utf-8")
            if label == key:
                return Entry(label, bool(flags), first, size, digest)
        return None

    def write(self, key: str, payload: bytes, immutable: bool = True) -> int:
        if not isinstance(payload, bytes):
            raise TypeError("payload must be bytes")
        previous = self._lookup(key)
        if previous is not None and previous.immutable:
            raise ValueError("cannot rewrite an immutable key")
        first_page = self._size("data") // self.page_bytes
        pages = max(1, (len(payload)+self.page_bytes-1)//self.page_bytes)
        self._write_pages("data", first_page * self.page_bytes,
                          payload.ljust(pages*self.page_bytes, b"\0"))
        name = key.encode("utf-8")
        entry = _ENTRY.pack(b"D2EN", len(name), int(immutable),
                            first_page, len(payload), sha256(payload).digest(),
                            name.ljust(64, b"\0"))
        self._write_pages("directory", self._size("directory"),
                          entry.ljust(self.slot_bytes, b"\0"))
        return pages

    def read(self, key: str) -> bytes:
        entry = self._lookup(key)
        if entry is None:
            raise KeyError(key)
        pages = max(1, (entry.payload_size+self.page_bytes-1)//self.page_bytes)
        if (entry.first_page+pages)*self.page_bytes > self._size("data"):
            raise IOError("directory refers beyond data file")
        raw = self._read_pages("data", entry.first_page*self.page_bytes, pages)
        payload = raw[:entry.payload_size]
        if sha256(payload).digest() != entry.digest:
            raise IOError("data checksum mismatch")
        return payload

    def exists(self, key: str) -> bool:
        return self._lookup(key) is not None

    def report(self) -> dict:
        return {
            "page_bytes": self.page_bytes,
            "cache_capacity_pages": self.cache_pages,
            "cache_current_pages": len(self.cache),
            "cache_max_observed_pages": self.max_cached_observed,
            "cache_hits": self.cache_hits,
            "cache_evictions": self.cache_evictions,
            "logical_page_requests": self.read_requests,
            "directory_entry_probes": self.lookup_entries_examined,
            "os_pread_directory_pages": self.directory_page_reads,
            "os_pread_payload_pages": self.data_page_reads,
            "os_pwrite_directory_pages": self.directory_page_writes,
            "os_pwrite_payload_pages": self.data_page_writes,
            "read_page_bytes": self.page_bytes * (
                self.directory_page_reads + self.data_page_reads),
            "written_page_bytes": self.page_bytes * (
                self.directory_page_writes + self.data_page_writes),
            "request_address_bytes_model": 8*self.read_requests,
            "file_directory_bytes": self._size("directory"),
            "file_data_bytes": self._size("data"),
            "os_metadata_syscalls_counted_not_priced": self.os_metadata_calls,
            "durable_on_crash": False,
            "actual_process_rss_bounded": False,
            "filesystem_syscall_cost_model_complete": False,
            "directory_lookup_paid": True,
            "backing_store_real_files": True,
            "novel_lower_bound_proved": False,
        }

    def close(self) -> None:
        if not self._closed:
            self._closed = True
            self.cache.clear()
            for fd in self._fds.values():
                os.close(fd)

    def __enter__(self) -> "FilePageStore":
        return self

    def __exit__(self, *_args) -> None:
        self.close()
