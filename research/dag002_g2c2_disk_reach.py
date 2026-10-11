"""DAG-002 C2-B1: genuinely file-backed lazy and bitmap reachability baselines.

Both use the SAME on-disk source parent records and manifest protocol.
All predecessor and query reads pass through the charged FilePageStore,
including its linear on-disk directory and bounded user-space page LRU.
No dictionary of old graph records, ancestor sets, or index pages persists
in the updater. This is a reference, not a crash-safe authenticated system.
"""
from __future__ import annotations

from pathlib import Path
import struct

from dag002_g2c2_file_store import FilePageStore
def encode_parents(parents: tuple[int, ...]) -> bytes:
    if len(parents) > 65535:
        raise ValueError("too many parents")
    return struct.pack("<H", len(parents)) + b"".join(
        struct.pack("<I", p) for p in parents)


def decode_parents(payload: bytes) -> tuple[int, ...]:
    if len(payload) < 2:
        raise ValueError("truncated parent header")
    count, = struct.unpack_from("<H", payload)
    if len(payload) != 2 + count*4:
        raise ValueError("parent list length mismatch")
    return tuple(struct.unpack_from("<I", payload, 2+4*i)[0]
                 for i in range(count))

_MAGIC = b"DAGIDX02"
_HEADER = struct.Struct("<8sIIII")
_VERSION = 1
_TYPES = {"lazy": 1, "bitmap": 2}


class FileReachIndex:
    def __init__(self, root: str | Path, mode: str, horizon: int,
                 page_bytes: int = 64, cache_pages: int = 0):
        if mode not in _TYPES or not 1 <= horizon <= 4096:
            raise ValueError("invalid mode or horizon")
        self.mode, self.horizon = mode, horizon
        self.store = FilePageStore(root, page_bytes, cache_pages)
        self.bitmap_size = (horizon + 7) // 8

    def _count(self) -> int:
        try:
            image = self.store.read("manifest")
        except KeyError:
            return 0
        if len(image) != _HEADER.size:
            raise ValueError("invalid DAG index manifest length")
        magic, ver, typ, horizon, count = _HEADER.unpack(image)
        if (magic, ver, typ, horizon) != (
                _MAGIC, _VERSION, _TYPES[self.mode], self.horizon):
            raise ValueError("DAG index mode/horizon/format mismatch")
        if count > self.horizon:
            raise ValueError("invalid DAG index generation")
        return count

    def append(self, parents: tuple[int, ...]) -> dict:
        before_requests = self.store.read_requests
        before_dir = self.store.directory_page_reads
        before_data = self.store.data_page_reads
        before_dir_writes = self.store.directory_page_writes
        before_data_writes = self.store.data_page_writes
        n = self._count()
        if n >= self.horizon:
            raise ValueError("horizon exceeded")
        if parents != tuple(sorted(set(parents))) or any(
                not 0 <= p < n for p in parents):
            raise ValueError("APPEND_SINK requires sorted unique old parents")
        bitmap = (1 << n)
        if self.mode == "bitmap":
            for p in parents:
                saved = self.store.read(f"bitmap:{p}")
                if len(saved) != self.bitmap_size:
                    raise ValueError("bad ancestor bitmap extent")
                bitmap |= int.from_bytes(saved, "little")
        self.store.write(f"parents:{n}", encode_parents(parents),
                         immutable=True)
        if self.mode == "bitmap":
            self.store.write(f"bitmap:{n}",
                             bitmap.to_bytes(self.bitmap_size, "little"),
                             immutable=True)
        # Publication last in the LOGICAL model only: not durable/atomic.
        self.store.write("manifest", _HEADER.pack(
            _MAGIC, _VERSION, _TYPES[self.mode], self.horizon, n+1),
            immutable=False)
        return {
            "vertex": n,
            "parents_input_bits": n,
            "page_requests": self.store.read_requests - before_requests,
            "directory_os_reads": (self.store.directory_page_reads-before_dir),
            "payload_os_reads": self.store.data_page_reads-before_data,
            "directory_os_writes": (
                self.store.directory_page_writes-before_dir_writes),
            "payload_os_writes": self.store.data_page_writes-before_data_writes,
        }

    def query(self, source: int, target: int) -> tuple[bool, int]:
        start = self.store.read_requests
        n = self._count()
        if not (0 <= source < n and 0 <= target < n):
            raise ValueError("query vertex outside published prefix")
        if source == target:
            return True, self.store.read_requests-start
        if source > target:
            return False, self.store.read_requests-start
        if self.mode == "bitmap":
            saved = self.store.read(f"bitmap:{target}")
            if len(saved) != self.bitmap_size:
                raise ValueError("bad ancestor bitmap extent")
            result = bool(int.from_bytes(saved, "little") & (1 << source))
        else:
            pending, seen = [target], set()
            result = False
            while pending:
                v = pending.pop()
                if v == source:
                    result = True
                    break
                if v not in seen:
                    seen.add(v)
                    pending.extend(decode_parents(
                        self.store.read(f"parents:{v}")))
        return result, self.store.read_requests-start

    def report(self) -> dict:
        n = self._count()
        return {
            "mode": self.mode,
            "vertices": n,
            "source_parent_incidence_bits": n*(n-1)//2,
            "on_disk_immutable_source": True,
            "charged_key_directory": True,
            "resident_cache_cap_pages": self.store.cache_pages,
            "user_cache_high_water_pages":
                self.store.max_cached_observed,
            "crash_atomic": False,
            "bounded_actual_rss": False,
            "device_io_measured": False,
            **self.store.report(),
        }

    def close(self) -> None:
        self.store.close()

    def __enter__(self) -> "FileReachIndex":
        return self

    def __exit__(self, *_args) -> None:
        self.close()
