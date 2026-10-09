"""INDEX-001 G2-B4-A: exact canonical binary RLE and variable checkpoint oracle.

Research-only one-writer clean-restart model. Byte counters model serialized files;
not SSD NAND, real atomicity, cache effects, or general dynamization lower bounds.
"""
from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from math import ceil
import json
import struct
import zlib

from index001_checkpoint_policy import Weights

SNAP_MAGIC = b"IXR1"
WAL_MAGIC = b"RW"
CRC = struct.Struct("<I")
MAX_INT = (1 << 63) - 1


def uvarint(n):
    if type(n) is not int or not 0 <= n <= MAX_INT:
        raise ValueError("unsigned 63-bit integer expected")
    encoded = bytearray()
    while n >= 128:
        encoded.append((n & 127) | 128)
        n >>= 7
    encoded.append(n)
    return bytes(encoded)


def parse_uvarint(data, offset):
    start = offset
    n = 0
    for shift in range(0, 70, 7):
        if offset >= len(data):
            raise ValueError("truncated varint")
        b = data[offset]
        offset += 1
        n |= (b & 127) << shift
        if not b & 128:
            if n > MAX_INT or data[start:offset] != uvarint(n):
                raise ValueError("noncanonical varint")
            return n, offset
    raise ValueError("varint exceeds 63 bits")


def _runs(values):
    values = tuple(values)
    if not values or any(type(v) is not int or v not in (0, 1) for v in values):
        raise ValueError("nonempty binary state required")
    out = []
    value = values[0]
    count = 0
    for v in values:
        if v != value:
            out.append((count, value))
            value, count = v, 0
        count += 1
    out.append((count, value))
    return tuple(out)


def _pack_crc(payload):
    return payload + CRC.pack(zlib.crc32(payload) & 0xffffffff)


def _verified_payload(data, magic):
    if not isinstance(data, bytes) or len(data) < len(magic) + 4:
        raise ValueError("truncated frame")
    if not data.startswith(magic):
        raise ValueError("wrong frame magic")
    payload = data[:-4]
    if CRC.unpack(data[-4:])[0] != (zlib.crc32(payload) & 0xffffffff):
        raise ValueError("bad frame CRC")
    return payload


def encode_snapshot(values):
    runs = _runs(values)
    payload = bytearray(SNAP_MAGIC)
    payload += uvarint(len(values))
    payload += uvarint(len(runs))
    for length, value in runs:
        payload += uvarint(length)
        payload.append(value)
    return _pack_crc(bytes(payload))


def decode_snapshot(data):
    payload = _verified_payload(data, SNAP_MAGIC)
    pos = len(SNAP_MAGIC)
    n, pos = parse_uvarint(payload, pos)
    k, pos = parse_uvarint(payload, pos)
    if not 1 <= k <= n:
        raise ValueError("invalid run count")
    out = []
    previous = None
    for _ in range(k):
        length, pos = parse_uvarint(payload, pos)
        if length < 1 or pos >= len(payload):
            raise ValueError("invalid run length or truncated symbol")
        symbol = payload[pos]
        pos += 1
        if symbol not in (0, 1) or symbol == previous or len(out) + length > n:
            raise ValueError("noncanonical run")
        out.extend([symbol] * length)
        previous = symbol
    if pos != len(payload) or len(out) != n:
        raise ValueError("trailing bytes or incorrect total length")
    return tuple(out)


def encode_wal(n, lo, hi, symbol):
    if (type(n) is not int or n < 1 or n > MAX_INT
            or type(lo) is not int or type(hi) is not int
            or not 0 <= lo < hi <= n or type(symbol) is not int
            or symbol not in (0, 1)):
        raise ValueError("invalid nonempty binary assignment")
    return _pack_crc(WAL_MAGIC + uvarint(lo) + uvarint(hi) + bytes([symbol]))


def decode_wal(n, data):
    payload = _verified_payload(data, WAL_MAGIC)
    pos = len(WAL_MAGIC)
    lo, pos = parse_uvarint(payload, pos)
    hi, pos = parse_uvarint(payload, pos)
    if pos + 1 != len(payload):
        raise ValueError("incorrect WAL frame length")
    symbol = payload[pos]
    if not 0 <= lo < hi <= n or symbol not in (0, 1):
        raise ValueError("invalid WAL range or symbol")
    return lo, hi, symbol


def trace_sizes(n, operations):
    """Independent dense state transitions; S indexed 0..U, E indexed 1..U."""
    if type(n) is not int or not 1 <= n <= MAX_INT:
        raise ValueError("invalid universe")
    dense = [0] * n
    snapshots = [len(encode_snapshot(dense))]
    frames = [0]
    states = [tuple(dense)]
    for operation in operations:
        if not isinstance(operation, (tuple, list)) or len(operation) != 3:
            raise ValueError("malformed assignment")
        lo, hi, symbol = operation
        frame = encode_wal(n, lo, hi, symbol)
        frames.append(len(frame))
        dense[lo:hi] = [symbol] * (hi - lo)
        states.append(tuple(dense))
        snapshots.append(len(encode_snapshot(dense)))
    return tuple(snapshots), tuple(frames), tuple(states)


def _inputs(n, operations, restarts, checkpoints, weights):
    operations, restarts, checkpoints = tuple(operations), tuple(restarts), tuple(checkpoints)
    if len(operations) != len(restarts):
        raise ValueError("restart counts must align with updates")
    if any(type(v) is not int or v < 0 for v in restarts):
        raise ValueError("negative or noninteger restart count")
    if (tuple(sorted(set(checkpoints))) != checkpoints
            or any(type(t) is not int or not 1 <= t <= len(operations) for t in checkpoints)):
        raise ValueError("invalid checkpoint indices")
    if not isinstance(weights, Weights):
        raise ValueError("expected explicit nonnegative resource weights")
    return operations, restarts, checkpoints, trace_sizes(n, operations)


def _score_sizes(sizes, frames, restarts, checkpoints, weights):
    last, suffix = 0, 0
    written = sizes[0]
    read = footprint = 0
    peak = sizes[0]
    ages = []
    cp = set(checkpoints)
    for t, r in enumerate(restarts, 1):
        suffix += frames[t]
        written += frames[t]
        if t in cp:
            peak = max(peak, sizes[last] + suffix + sizes[t])
            written += sizes[t]
            last, suffix = t, 0
        steady = sizes[last] + suffix
        peak = max(peak, steady)
        read += r * steady
        footprint += steady
        ages.append(steady)
    return {
        "checkpoints": list(checkpoints),
        "written_bytes": written,
        "recovery_read_bytes": read,
        "steady_footprint_byte_steps": footprint,
        "peak_path_bytes": peak,
        "steady_file_bytes": ages,
        "weighted_cost": (weights.write * written + weights.recovery * read
                          + weights.footprint * footprint),
    }


def score(n, operations, restarts, checkpoints=(), weights=Weights(1, 6, 0)):
    ops, r, cp, (sizes, frames, _) = _inputs(
        n, operations, restarts, checkpoints, weights)
    return _score_sizes(sizes, frames, r, cp, weights)


def online_threshold(n, operations):
    """Decision uses current snapshot size and accumulated WAL; NO restart lookahead."""
    sizes, frames, _ = trace_sizes(n, operations)
    suffix = 0
    cp = []
    for t in range(1, len(sizes)):
        suffix += frames[t]
        if suffix >= sizes[t]:
            cp.append(t)
            suffix = 0
    return tuple(cp)


def offline_dp(n, operations, restarts, weights=Weights(1, 6, 0)):
    """Exact O(U^2) clairvoyant optimizer, key = last checkpoint index."""
    ops, r, _, (sizes, frames, _) = _inputs(n, operations, restarts, (), weights)
    prefix = [0]
    for frame in frames[1:]:
        prefix.append(prefix[-1] + frame)
    dp = {0: (weights.write * sizes[0], ())}
    for t, count in enumerate(r, 1):
        next_dp = {}
        for last, (cost, checkpoints) in dp.items():
            for new_last in (last, t):
                checkpoint = new_last == t
                suffix = 0 if checkpoint else prefix[t] - prefix[last]
                steady = sizes[new_last] + suffix
                candidate = (
                    cost + weights.write * (frames[t] + (sizes[t] if checkpoint else 0))
                    + (weights.recovery * count + weights.footprint) * steady,
                    checkpoints + ((t,) if checkpoint else ()),
                )
                if new_last not in next_dp or candidate < next_dp[new_last]:
                    next_dp[new_last] = candidate
        dp = next_dp
    path = min(dp.values())[1]
    return _score_sizes(sizes, frames, r, path, weights)


def offline_bruteforce(n, operations, restarts, weights=Weights(1, 6, 0)):
    """Independent enumeration of checkpoint subsets; MAX U=10."""
    ops, r, _, (sizes, frames, _) = _inputs(n, operations, restarts, (), weights)
    if len(ops) > 10:
        raise ValueError("exhaustive oracle accepts at most 10 updates")
    best = None
    for decisions in product((False, True), repeat=len(ops)):
        checkpoints = tuple(t for t, use in enumerate(decisions, 1) if use)
        value = _score_sizes(sizes, frames, r, checkpoints, weights)
        key = value["weighted_cost"], checkpoints
        if best is None or key < best[0]:
            best = (key, value)
    return best[1]


def compare(n, operations, restarts, weights=Weights(1, 6, 0)):
    online_path = online_threshold(n, operations)
    online = score(n, operations, restarts, online_path, weights)
    offline = offline_dp(n, operations, restarts, weights)
    if offline["weighted_cost"] == 0:
        if online["weighted_cost"] != 0:
            raise AssertionError("zero offline with positive online")
        ratio = Fraction(1)
    else:
        ratio = Fraction(online["weighted_cost"], offline["weighted_cost"])
    sizes, frames, _ = trace_sizes(n, operations)
    kappa = Fraction(max(sizes), min(sizes))
    # Elementary instance-dependent bound: W_on <= 2 W_off; each
    # read/footprint byte-step on <= 2*Smax and off >= Smin.
    if ratio > 2 * kappa:
        raise AssertionError("violates elementary 2*kappa certificate")
    return {
        "online": online, "offline": offline,
        "ratio": [ratio.numerator, ratio.denominator],
        "kappa": [kappa.numerator, kappa.denominator],
        "sizes": list(sizes), "wal_frames": list(frames[1:]),
    }


def scaling_bad_family(n):
    """For every odd N>=3: force checkpoint of alternating data, then collapse.

    Padding uses acknowledged nonempty range assignments that preserve data.
    Exposes an unbounded lower-bound ratio for THIS threshold policy, not all
    online algorithms. The construction is deterministic and finite.
    """
    if type(n) is not int or n < 3 or n % 2 != 1:
        raise ValueError("odd universe >=3 required")
    operations = [(i, i + 1, 1) for i in range(1, n, 2)]
    while True:
        checkpoints = online_threshold(n, operations)
        if checkpoints and checkpoints[-1] == len(operations):
            break
        operations.append((0, 1, 0))  # semantic no-op, nonempty WAL
    high_checkpoint = len(operations)
    operations.append((0, n, 0))
    return tuple(operations), high_checkpoint


def scaling_bound_instance(n):
    operations, high_checkpoint = scaling_bad_family(n)
    r = (0,) * (len(operations) - 1) + (1,)
    row = compare(n, operations, r, Weights(0, 1, 0))
    width = len(uvarint(n))
    large = 8 + 2 * width + 2 * n
    small = 10 + 2 * width
    collapse_frame = 8 + width
    expected = Fraction(large + collapse_frame, small)
    actual = Fraction(*row["ratio"])
    if (actual != expected or row["online"]["checkpoints"][-1] != high_checkpoint
            or row["offline"]["checkpoints"][-1] != len(operations)
            or row["offline"]["recovery_read_bytes"] != small):
        # With free writes, earlier checkpoints may also appear in the
        # lexicographic tie-break; the final checkpoint is what matters.
        raise AssertionError("variable-size scaling family oracle mismatch")
    return {
        "n": n,
        "padding_updates": high_checkpoint - (n - 1) // 2,
        "high_snapshot_bytes": large,
        "small_snapshot_bytes": small,
        "final_wal_frame_bytes": collapse_frame,
        "ratio": [actual.numerator, actual.denominator],
    }


WITNESS = ((1, 2, 1), (3, 4, 1), (5, 6, 1), (0, 6, 0))


def build_report():
    result = compare(6, WITNESS, (0, 0, 0, 1), Weights(0, 1, 0))
    oracle = offline_bruteforce(6, WITNESS, (0, 0, 0, 1), Weights(0, 1, 0))
    if oracle != result["offline"]:
        raise AssertionError("DP and independent subset oracle disagree")
    if Fraction(*result["ratio"]) <= 2:
        raise AssertionError("missing counterexample")
    return {
        "schema": "mathlab.index001.g2b4a.variable-rle.v1",
        "classification": "VARIABLE_SIZE_NAIVE_THRESHOLD_2_BOUND_FALSIFIED",
        "scope": "CLEAN_RESTART_SINGLE_WRITER_EXACT_SERIALIZED_BYTES_ONLY",
        "naive_threshold_witness": {
            "n": 6, "operations": [list(op) for op in WITNESS],
            "restarts": [0, 0, 0, 1], **result,
        },
        "safe_coarse_upper_bound": "J_online <= 2*(Smax/Smin)*J_offline",
        "scaling_lower_bound_family": [scaling_bound_instance(n) for n in (3, 31, 129)],
        "novel_general_theorem": "NOT_ESTABLISHED",
        "nand_bytes": "NOT_MEASURED",
    }


if __name__ == "__main__":
    report = build_report()
    print(json.dumps(report, sort_keys=True, indent=2))
    print("INDEX001_G2B4A_VARIABLE_RLE_MODEL_AND_WITNESS_PASS")
