"""INDEX-001 G2-B3-A: two-slot manifest pivot for exact range overwrites.

Reference-only on one-writer POSIX. Failpoints simulate process stop at
operation boundaries, NOT power loss, sector atomicity or SSD/NAND I/O.
The inactive snapshot is NOT an automatic rollback after WAL truncation.
"""
from dataclasses import dataclass
import os
from pathlib import Path
import struct
import zlib

from index001_durable import (
    IoLedger, CorruptStore, InjectedCrash, MAX_U32, MAX_U64,
    WAL_ENTRY, _crc, _read, _write_all, _file_sync, _directory_sync,
    _gate, _range, _u32, _dense_scan, encode_snapshot, decode_snapshot,
    encode_wal, decode_wal,
)

MANIFEST_HEAD = struct.Struct("<4sB3xQ")
MANIFEST_LENGTH = MANIFEST_HEAD.size + 4
assert MANIFEST_LENGTH == 20


@dataclass
class GenerationLedger(IoLedger):
    manifest_written: int = 0
    manifest_read: int = 0
    snapshot_replaces: int = 0
    manifest_replaces: int = 0
    inactive_gc_unlinks: int = 0

    @property
    def total_application_written(self):
        return self.snapshot_written + self.wal_written + self.manifest_written

    @property
    def total_application_read(self):
        return self.snapshot_read + self.wal_read + self.manifest_read


def encode_manifest(slot, seq):
    if not isinstance(slot, int) or slot not in (0, 1):
        raise ValueError("manifest slot must be 0 or 1")
    if not isinstance(seq, int) or not 0 <= seq <= MAX_U64:
        raise ValueError("manifest seq must fit uint64")
    raw = MANIFEST_HEAD.pack(b"IXM1", slot, seq)
    return raw + _crc(raw)


def decode_manifest(raw):
    if len(raw) != MANIFEST_LENGTH:
        raise CorruptStore("manifest exact byte length mismatch")
    if raw[:4] != b"IXM1" or raw[5:8] != b"\x00\x00\x00":
        raise CorruptStore("manifest magic/reserved bytes invalid")
    if raw[-4:] != _crc(raw[:-4]):
        raise CorruptStore("manifest CRC mismatch")
    magic, slot, seq = MANIFEST_HEAD.unpack_from(raw)
    if slot not in (0, 1):
        raise CorruptStore("manifest slot invalid")
    return slot, seq


def _write_temp(folder, name, content, ledger, bucket,
                *, halfway=None, synced=None):
    fd = os.open(folder / name, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    try:
        split = max(1, len(content) // 2)
        _write_all(fd, content[:split], ledger, bucket)
        if halfway:
            _gate(halfway[0], halfway[1])
        _write_all(fd, content[split:], ledger, bucket)
        _file_sync(fd, ledger)
        if synced:
            _gate(synced[0], synced[1])
    finally:
        os.close(fd)


def _replace_and_sync(folder, old, new, ledger, *, replaced=None, dirsynced=None):
    os.replace(folder / old, folder / new)
    if new == "manifest.bin":
        ledger.manifest_replaces += 1
    else:
        ledger.snapshot_replaces += 1
    if replaced:
        _gate(replaced[0], replaced[1])
    _directory_sync(folder, ledger)
    if dirsynced:
        _gate(dirsynced[0], dirsynced[1])


class GenerationRangeStore:
    """Reference durability protocol, NOT a transactional multiwriter store."""

    def __init__(self, folder, size, initial=0):
        if not isinstance(size, int) or not 1 <= size <= MAX_U32:
            raise ValueError("invalid uint32 domain")
        _u32(initial, "initial")
        self.folder = Path(folder)
        self.folder.mkdir(parents=True, exist_ok=True)
        self.size = size
        self.manifest_path = self.folder / "manifest.bin"
        self.wal_path = self.folder / "wal.bin"
        self.ledger = GenerationLedger()
        if not self.manifest_path.exists():
            if any(self.folder.iterdir()):
                raise CorruptStore("incomplete creation: nonempty dir lacks manifest")
            self._initialize(initial)
        raw = _read(self.manifest_path, self.ledger, "manifest_read")
        self.active_slot, self.checkpoint_seq = decode_manifest(raw)
        snap_name = self._snapshot_name(self.active_slot)
        path = self.folder / snap_name
        if not path.is_file():
            raise CorruptStore("manifest points to missing active snapshot")
        seq, cells = decode_snapshot(
            _read(path, self.ledger, "snapshot_read"), self.size)
        if seq != self.checkpoint_seq:
            raise CorruptStore("manifest LSN differs from active snapshot LSN")
        self.cells = cells
        if not self.wal_path.is_file():
            raise CorruptStore("WAL missing; no implicit journal recreation")
        self._replay_wal()

    @staticmethod
    def _snapshot_name(slot):
        return f"snapshot.{slot}.bin"

    def _initialize(self, initial):
        _write_temp(self.folder, "snapshot.0.tmp",
                    encode_snapshot(0, [initial] * self.size),
                    self.ledger, "snapshot_written")
        _replace_and_sync(self.folder, "snapshot.0.tmp", "snapshot.0.bin",
                          self.ledger)
        fd = os.open(self.wal_path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        try:
            _file_sync(fd, self.ledger)
        finally:
            os.close(fd)
        _directory_sync(self.folder, self.ledger)
        _write_temp(self.folder, "manifest.tmp",
                    encode_manifest(0, 0), self.ledger, "manifest_written")
        _replace_and_sync(self.folder, "manifest.tmp", "manifest.bin", self.ledger)

    def _truncate_wal(self, amount):
        fd = os.open(self.wal_path, os.O_WRONLY)
        try:
            os.ftruncate(fd, amount)
            self.ledger.wal_truncates += 1
            _file_sync(fd, self.ledger)
        finally:
            os.close(fd)

    def _replay_wal(self):
        data = _read(self.wal_path, self.ledger, "wal_read")
        full = len(data) // WAL_ENTRY.size
        previous = 0
        self.seq = self.checkpoint_seq
        for index in range(full):
            start = index * WAL_ENTRY.size
            number, left, right, value = decode_wal(
                data[start:start + WAL_ENTRY.size], self.size)
            if number <= previous:
                raise CorruptStore("WAL repeated/decreasing sequence")
            previous = number
            if number <= self.checkpoint_seq:
                continue
            if number != self.seq + 1:
                raise CorruptStore("WAL sequence gap beyond checkpoint")
            self.cells[left:right] = [value] * (right - left)
            self.seq = number
        if len(data) % WAL_ENTRY.size:
            self._truncate_wal(full * WAL_ENTRY.size)

    def assign(self, lo, hi, value, *, failure=None):
        _range(self.size, lo, hi)
        _u32(value, "range value")
        if lo == hi:
            return
        if self.seq == MAX_U64:
            raise OverflowError("WAL sequence exhausted")
        _gate("before_wal", failure)
        record = encode_wal(self.seq + 1, lo, hi, value)
        fd = os.open(self.wal_path, os.O_WRONLY | os.O_APPEND)
        try:
            split = len(record) // 2
            _write_all(fd, record[:split], self.ledger, "wal_written")
            _gate("after_wal_partial", failure)
            _write_all(fd, record[split:], self.ledger, "wal_written")
            _gate("after_wal_write", failure)
            _file_sync(fd, self.ledger)
            _gate("after_wal_sync", failure)
        finally:
            os.close(fd)
        self.cells[lo:hi] = [value] * (hi - lo)
        self.seq += 1
        self.ledger.acknowledged_blocks += hi - lo

    def checkpoint(self, *, failure=None):
        if self.seq == self.checkpoint_seq:
            return
        target = 1 - self.active_slot
        path = self._snapshot_name(target)
        temporary = f"snapshot.{target}.tmp"
        _write_temp(self.folder, temporary, encode_snapshot(self.seq, self.cells),
                    self.ledger, "snapshot_written",
                    halfway=("after_snapshot_partial", failure),
                    synced=("after_snapshot_sync", failure))
        _replace_and_sync(self.folder, temporary, path, self.ledger,
                          replaced=("after_snapshot_replace", failure),
                          dirsynced=("after_snapshot_dirsync", failure))
        _write_temp(self.folder, "manifest.tmp",
                    encode_manifest(target, self.seq),
                    self.ledger, "manifest_written",
                    halfway=("after_manifest_partial", failure),
                    synced=("after_manifest_sync", failure))
        _replace_and_sync(self.folder, "manifest.tmp", "manifest.bin", self.ledger,
                          replaced=("after_manifest_replace", failure),
                          dirsynced=("after_manifest_dirsync", failure))
        self.active_slot = target
        self.checkpoint_seq = self.seq
        self._truncate_wal(0)
        _gate("after_wal_truncate", failure)

    def gc_inactive(self, *, failure=None):
        """Remove only nonselected generation, never an automatic recovery fallback."""
        inactive = self.folder / self._snapshot_name(1 - self.active_slot)
        if not inactive.exists():
            return False
        _gate("before_gc", failure)
        inactive.unlink()
        self.ledger.inactive_gc_unlinks += 1
        _gate("after_gc_unlink", failure)
        _directory_sync(self.folder, self.ledger)
        _gate("after_gc_dirsync", failure)
        return True

    def file_lengths(self):
        names = ["snapshot.0.bin", "snapshot.1.bin", "snapshot.0.tmp",
                 "snapshot.1.tmp", "manifest.bin", "manifest.tmp", "wal.bin"]
        return {n: (self.folder / n).stat().st_size if
                (self.folder / n).exists() else None for n in names}

    def lookup(self, pos):
        _range(self.size, pos, pos + 1)
        return self.cells[pos]

    def scan(self, lo, hi):
        return _dense_scan(self.cells, lo, hi)
