"""INDEX-001 G2-B0/B1 POSIX-only, one-writer *reference* durable range map.

No concurrent writers, storage adversary, fsync hardware warranty, SSD byte
measurement, production safety, Rust API, or original mathematical theorem.
Protocol: docs/research/INDEX-001-G2-B0-DURABILITY-PROTOCOL.md.
"""
import os
from pathlib import Path
import struct
import zlib
from dataclasses import dataclass

SNAP_HEAD = struct.Struct("<4sQII")
WAL_ENTRY = struct.Struct("<4sQIIII")
U32 = struct.Struct("<I")
MAX_U32 = (1 << 32) - 1
MAX_U64 = (1 << 64) - 1


class CorruptStore(ValueError):
    """Complete stored bytes violate the frozen grammar or sequence rules."""


class InjectedCrash(RuntimeError):
    """Stop immediately; the test must reopen, never reuse this instance."""


@dataclass
class IoLedger:
    wal_written: int = 0
    snapshot_written: int = 0
    snapshot_read: int = 0
    wal_read: int = 0
    application_write_calls: int = 0
    application_read_calls: int = 0
    fsync_files: int = 0
    fsync_dirs: int = 0
    wal_truncates: int = 0
    acknowledged_blocks: int = 0

    @property
    def total_application_written(self):
        return self.wal_written + self.snapshot_written

    @property
    def total_application_read(self):
        return self.snapshot_read + self.wal_read


def _u32(x, desc):
    if not isinstance(x, int) or not 0 <= x <= MAX_U32:
        raise ValueError(desc + " must be uint32")
    return x


def _range(size, lo, hi):
    if (not isinstance(lo, int) or not isinstance(hi, int)
            or not 0 <= lo <= hi <= size):
        raise ValueError("invalid half-open address range")


def _crc(frame):
    return U32.pack(zlib.crc32(frame) & MAX_U32)


def encode_snapshot(seq, cells):
    if not isinstance(seq, int) or not 0 <= seq <= MAX_U64:
        raise ValueError("sequence out of bounds")
    n = _u32(len(cells), "universe size")
    if n == 0:
        raise ValueError("empty universe")
    payload = bytearray(SNAP_HEAD.pack(b"IXS1", seq, n, 0))
    for x in cells:
        payload.extend(U32.pack(_u32(x, "cell value")))
    return bytes(payload) + _crc(payload)


def decode_snapshot(raw, expected_size):
    if len(raw) < SNAP_HEAD.size + U32.size:
        raise CorruptStore("short snapshot")
    magic, seq, n, reserved = SNAP_HEAD.unpack_from(raw)
    if magic != b"IXS1" or reserved != 0 or n != expected_size:
        raise CorruptStore("snapshot header/universe mismatch")
    if len(raw) != SNAP_HEAD.size + 4 * n + U32.size:
        raise CorruptStore("snapshot exact byte length mismatch")
    if raw[-4:] != _crc(raw[:-4]):
        raise CorruptStore("snapshot CRC mismatch")
    cells = [x[0] for x in struct.iter_unpack("<I", raw[SNAP_HEAD.size:-4])]
    return seq, cells


def encode_wal(seq, lo, hi, value):
    if not isinstance(seq, int) or not 1 <= seq <= MAX_U64:
        raise ValueError("WAL sequence out of bounds")
    header = struct.pack("<4sQIII", b"IXW1", seq, _u32(lo, "lo"),
                         _u32(hi, "hi"), _u32(value, "value"))
    return header + _crc(header)


def decode_wal(raw, size):
    if len(raw) != WAL_ENTRY.size:
        raise CorruptStore("short WAL record")
    magic, seq, lo, hi, value, checksum = WAL_ENTRY.unpack(raw)
    if magic != b"IXW1" or checksum != zlib.crc32(raw[:-4]) & MAX_U32:
        raise CorruptStore("WAL magic/CRC mismatch")
    if seq == 0 or not 0 <= lo < hi <= size:
        raise CorruptStore("WAL sequence/range invalid")
    return seq, lo, hi, value


def _read(path, ledger, which):
    payload = path.read_bytes()
    setattr(ledger, which, getattr(ledger, which) + len(payload))
    ledger.application_read_calls += 1
    return payload


def _write_all(fd, content, ledger, which):
    offset = 0
    while offset < len(content):
        count = os.write(fd, content[offset:])
        if count <= 0:
            raise OSError("os.write returned no progress")
        offset += count
        setattr(ledger, which, getattr(ledger, which) + count)
        ledger.application_write_calls += 1


def _file_sync(fd, ledger):
    os.fsync(fd)
    ledger.fsync_files += 1


def _directory_sync(folder, ledger):
    if os.name != "posix":
        raise NotImplementedError("G2-B reference requires POSIX directory fsync")
    fd = os.open(folder, os.O_RDONLY | os.O_DIRECTORY)
    try:
        os.fsync(fd)
        ledger.fsync_dirs += 1
    finally:
        os.close(fd)


def _gate(name, failure):
    if failure == name:
        raise InjectedCrash(name)


def _snapshot_install(folder, cells, seq, ledger, failure=None):
    """Write all bytes, sync, replace, sync directory. Caller owns WAL ordering."""
    blob = encode_snapshot(seq, cells)
    temp = folder / "snapshot.tmp"
    fd = os.open(temp, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    try:
        split = max(1, len(blob) // 2)
        _write_all(fd, blob[:split], ledger, "snapshot_written")
        _gate("after_checkpoint_partial", failure)
        _write_all(fd, blob[split:], ledger, "snapshot_written")
        _file_sync(fd, ledger)
        _gate("after_checkpoint_sync", failure)
    finally:
        os.close(fd)
    os.replace(temp, folder / "snapshot.bin")
    _gate("after_checkpoint_replace", failure)
    _directory_sync(folder, ledger)
    _gate("after_checkpoint_dirsync", failure)


def _dense_scan(cells, lo, hi):
    _range(len(cells), lo, hi)
    if lo == hi:
        return ()
    out = []
    first = lo
    for i in range(lo + 1, hi + 1):
        if i == hi or cells[i] != cells[first]:
            out.append((first, i, cells[first]))
            first = i
    return tuple(out)


class DurableRangeStore:
    """One-writer append-only WAL with a full-image checkpoint and recovery."""

    def __init__(self, folder, size, initial=0):
        if not isinstance(size, int) or not 1 <= size <= MAX_U32:
            raise ValueError("universe size must fit uint32")
        _u32(initial, "initial value")
        self.folder = Path(folder)
        self.folder.mkdir(parents=True, exist_ok=True)
        self.snapshot_path = self.folder / "snapshot.bin"
        self.wal_path = self.folder / "wal.bin"
        self.size = size
        self.ledger = IoLedger()
        if not self.snapshot_path.exists():
            if self.wal_path.exists():
                raise CorruptStore("WAL without committed snapshot")
            _snapshot_install(self.folder, [initial] * size, 0, self.ledger)
        blob = _read(self.snapshot_path, self.ledger, "snapshot_read")
        self.checkpoint_seq, self.cells = decode_snapshot(blob, size)
        if not self.wal_path.exists():
            fd = os.open(self.wal_path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
            try:
                _file_sync(fd, self.ledger)
            finally:
                os.close(fd)
            _directory_sync(self.folder, self.ledger)
        self._replay_wal()

    def _replay_wal(self):
        raw = _read(self.wal_path, self.ledger, "wal_read")
        count = len(raw) // WAL_ENTRY.size
        last_record = 0
        self.seq = self.checkpoint_seq
        for i in range(count):
            record = raw[i * WAL_ENTRY.size:(i + 1) * WAL_ENTRY.size]
            seq, lo, hi, value = decode_wal(record, self.size)
            if seq <= last_record:
                raise CorruptStore("WAL sequence duplicate or unordered")
            last_record = seq
            if seq <= self.checkpoint_seq:
                continue
            if seq != self.seq + 1:
                raise CorruptStore("WAL gap after snapshot sequence")
            self.cells[lo:hi] = [value] * (hi - lo)
            self.seq = seq
        if len(raw) % WAL_ENTRY.size:
            # Only a torn/incomplete terminal record is discarded. Full invalid
            # records always fail closed; a partial unacknowledged tail is not data.
            self._truncate_wal(count * WAL_ENTRY.size)

    def _truncate_wal(self, new_length):
        fd = os.open(self.wal_path, os.O_WRONLY)
        try:
            os.ftruncate(fd, new_length)
            self.ledger.wal_truncates += 1
            _file_sync(fd, self.ledger)
        finally:
            os.close(fd)

    def assign(self, lo, hi, value, *, failure=None):
        _range(self.size, lo, hi)
        _u32(value, "value")
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
        _snapshot_install(self.folder, self.cells, self.seq, self.ledger, failure)
        self._truncate_wal(0)
        _gate("after_wal_truncate", failure)
        self.checkpoint_seq = self.seq

    def lookup(self, pos):
        _range(self.size, pos, pos + 1)
        return self.cells[pos]

    def scan(self, lo, hi):
        return _dense_scan(self.cells, lo, hi)

    @property
    def application_written_bytes(self):
        return self.ledger.total_application_written


class SnapshotReference:
    """Independent no-WAL full snapshot rewrite, not a transactional database."""

    def __init__(self, folder, size, initial=0):
        if not isinstance(size, int) or not 1 <= size <= MAX_U32:
            raise ValueError("invalid universe size")
        _u32(initial, "initial")
        self.folder = Path(folder)
        self.folder.mkdir(parents=True, exist_ok=True)
        self.path = self.folder / "snapshot.bin"
        self.size = size
        self.ledger = IoLedger()
        if not self.path.exists():
            _snapshot_install(self.folder, [initial] * size, 0, self.ledger)
        self.seq, self.cells = decode_snapshot(
            _read(self.path, self.ledger, "snapshot_read"), size)

    def assign(self, lo, hi, value, *, failure=None):
        _range(self.size, lo, hi)
        _u32(value, "value")
        if lo == hi:
            return
        if self.seq == MAX_U64:
            raise OverflowError("snapshot sequence exhausted")
        tmp = list(self.cells)
        tmp[lo:hi] = [value] * (hi - lo)
        _snapshot_install(self.folder, tmp, self.seq + 1, self.ledger, failure)
        self.cells = tmp
        self.seq += 1
        self.ledger.acknowledged_blocks += hi - lo

    def lookup(self, pos):
        _range(self.size, pos, pos + 1)
        return self.cells[pos]

    def scan(self, lo, hi):
        return _dense_scan(self.cells, lo, hi)
