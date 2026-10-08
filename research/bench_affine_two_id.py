#!/usr/bin/env python3
"""HYP-002-C diagnostic Python microbenchmark, no performance acceptance gate.

Timing is workload/hardware/interpreter dependent; strictly descriptive.
A sparse arithmetic *count of changed coordinates* is not a runtime metric:
our immutable Python tuples are copied at O(m) cost per raw update.
"""
from __future__ import annotations

import json
from statistics import median
from time import perf_counter_ns

from affine_two_id import (
    canonical_line, checked_transition, decode, encode, size,
    storage_report, trusted_raw_update,
)


def median_ns(op, *, warmup: int = 40, rounds: int = 5, repeats: int = 400) -> int:
    for _ in range(warmup):
        op()
    samples: list[float] = []
    for _ in range(rounds):
        start = perf_counter_ns()
        for _ in range(repeats):
            op()
        samples.append((perf_counter_ns() - start) / repeats)
    return round(median(samples))


def run_benchmarks() -> None:
    results: list[dict[str, int | float]] = []
    for rank in (2, 3, 4, 5):
        m = size(rank)
        first = canonical_line(0, 1, rank)
        second = canonical_line(3, 4, rank)
        direct = tuple(sorted((first, second)))
        state = encode(direct, rank)
        assert decode(state, rank) == direct
        assert checked_transition(state, rank, first, add=False) == encode(
            (second,), rank
        )
        direct_del = lambda: tuple(x for x in direct if x != first)
        assert direct_del() == (second,)

        result = storage_report(rank)
        result.update({
            "decode_dense_ns": median_ns(lambda: decode(state, rank)),
            "direct_read_ns": median_ns(lambda: tuple(direct)),
            "checked_delete_dense_ns": median_ns(
                lambda: checked_transition(state, rank, first, False)
            ),
            "trusted_raw_delta_python_ns": median_ns(
                lambda: trusted_raw_update(state, rank, first, -1)
            ),
            "direct_delete_ns": median_ns(direct_del),
        })
        results.append(result)
    print("HYP002C_DIAGNOSTIC_BENCHMARK", json.dumps(results, sort_keys=True))
    print("HYP002C_BENCHMARK_COMPLETED_NO_PERF_GATE")


if __name__ == "__main__":
    run_benchmarks()
