#!/usr/bin/env python3
"""UCT-005 D1-C3: exact conditional GF(2) causal-observation rank.

Scope: public, fixed SET-coordinate schedule, named nonadaptive historical
range queries, two reader labels, independently variable initial bits and SET
payloads. This is a CLASSICAL answer-tuple count, NOT a Byzantine F1 lower.
"""
from __future__ import annotations

from itertools import product
from functools import reduce
from operator import or_
import json

from uct005_d1b0_f1_reference import validate_contract

CLASSIFICATION = "EXACT_CLASSICAL_CAUSAL_RANK_AND_ADDITIVE_CUT_STOP"
MAX_EXHAUSTIVE_SYMBOLS = 10


def _valid(n: int, updates: tuple[int, ...],
           queries: tuple[tuple[int, int, int, int], ...],
           known: tuple[tuple[int, int], ...]) -> None:
    if type(n) is not int or n < 1 or type(updates) is not tuple:
        raise ValueError("n positive and updates a tuple")
    if any(type(i) is not int or i < 0 or i >= n for i in updates):
        raise ValueError("invalid publicly scheduled SET coordinates")
    if type(queries) is not tuple:
        raise ValueError("queries must be a tuple")
    H = len(updates)
    for query in queries:
        if (type(query) is not tuple or len(query) != 4 or
                any(type(a) is not int for a in query)):
            raise ValueError("queries are (reader,epoch,left,right)")
        reader, epoch, left, right = query
        if reader not in (0, 1) or not (0 <= epoch <= H) or not (0 <= left < right <= n):
            raise ValueError("invalid reader, historical epoch or half-open range")
    if type(known) is not tuple:
        raise ValueError("known SET values must be a tuple")
    seen = set()
    for item in known:
        if (type(item) is not tuple or len(item) != 2 or
                any(type(a) is not int for a in item)):
            raise ValueError("known update entry must be (zero_based_step,bit)")
        step, bit = item
        if step < 0 or step >= H or bit not in (0, 1) or step in seen:
            raise ValueError("invalid/duplicate charged public SET value")
        seen.add(step)


def rank_gf2(rows: tuple[int, ...]) -> int:
    """Incremental elimination on arbitrary nonnegative Python-int row masks."""
    basis: dict[int, int] = {}
    for value in rows:
        if type(value) is not int or value < 0:
            raise ValueError("GF2 row must be an unsigned integer")
        x = value
        while x:
            pivot = x.bit_length() - 1
            if pivot in basis:
                x ^= basis[pivot]
            else:
                basis[pivot] = x
                break
    return len(basis)


def last_writer_row(n: int, updates: tuple[int, ...],
                    epoch: int, left: int, right: int) -> int:
    """Independent author symbols: n initial bits, then H SET payload bits."""
    if (type(n) is not int or n < 1 or type(updates) is not tuple or
            any(type(i) is not int or i < 0 or i >= n for i in updates) or
            type(epoch) is not int or not 0 <= epoch <= len(updates) or
            type(left) is not int or type(right) is not int or
            not 0 <= left < right <= n):
        raise ValueError("invalid causal row parameters")
    last = list(range(n))
    for step, coord in enumerate(updates[:epoch]):
        last[coord] = n + step
    row = 0
    for coord in range(left, right):
        row ^= 1 << last[coord]
    return row


def causal_rank(n: int, updates: tuple[int, ...],
                queries: tuple[tuple[int, int, int, int], ...],
                known: tuple[tuple[int, int], ...] = ()) -> dict:
    """Rank conditions on billed PUBLIC b_t; reader label is not entropy."""
    _valid(n, updates, queries, known)
    known_mask = sum(1 << (n + step) for step, _ in known)
    known_one_mask = sum(1 << (n + step) for step, bit in known if bit)
    rows = tuple(last_writer_row(n, updates, t, l, r)
                 for _, t, l, r in queries)
    hidden = tuple(row & ~known_mask for row in rows)
    offsets = tuple((row & known_one_mask).bit_count() & 1 for row in rows)
    joint = rank_gf2(hidden)
    readers = tuple(rank_gf2(tuple(row for row, query in zip(hidden, queries)
                                   if query[0] == reader)) for reader in (0, 1))
    epochs = tuple(rank_gf2(tuple(row for row, query in zip(hidden, queries)
                                  if query[1] == t))
                   for t in range(len(updates) + 1))
    shared = reduce(or_, hidden, 0).bit_count()
    return {
        "model": "FIXED_PUBLIC_COORDINATE_SCHEDULE_CONDITIONAL_ANSWER_ONLY",
        "n": n, "H": len(updates), "queries": len(queries),
        "input_symbols": n + len(updates),
        "hidden_symbols": n + len(updates) - len(known),
        "known_author_payload_values": len(known),
        "rows": list(rows), "hidden_rows": list(hidden),
        "public_offsets": list(offsets),
        "joint_rank": joint, "answer_tuple_count": 1 << joint,
        "sum_individual_reader_ranks": sum(readers),
        "reader_ranks": list(readers),
        "sum_individual_epoch_ranks": sum(epochs),
        "epoch_ranks": list(epochs),
        "distinct_hidden_provenance_variables_used": shared,
        "no_double_counted_information_rank": joint,
        "full_F1_joint_lower_proved": False,
        "novelty": "STOP_NOVELTY_CLASSICAL"
    }


def independent_answer_signatures(n: int, updates: tuple[int, ...],
                                  queries: tuple[tuple[int, int, int, int], ...],
                                  known: tuple[tuple[int, int], ...] = ()) -> set[tuple[int, ...]]:
    """Brute-force literal SET execution; DOES NOT use row/elimination routines.

    Independently enumerate hidden inputs, copy the actual evolving bit array,
    and compute all named parities from epoch snapshots.
    """
    _valid(n, updates, queries, known)
    H = len(updates)
    if n + H > MAX_EXHAUSTIVE_SYMBOLS:
        raise ValueError("finite oracle only; no free exponential theorem")
    public = dict(known)
    unknown_steps = tuple(step for step in range(H) if step not in public)
    outcomes: set[tuple[int, ...]] = set()
    for bits in product((0, 1), repeat=n):
        for hidden_values in product((0, 1), repeat=len(unknown_steps)):
            assignments = dict(zip(unknown_steps, hidden_values))
            assignments.update(public)
            state = list(bits)
            snapshots = [tuple(state)]
            for step, coord in enumerate(updates):
                state[coord] = assignments[step]  # includes intentional no-ops
                snapshots.append(tuple(state))
            signature = tuple(sum(snapshots[t][l:r]) & 1
                              for _reader, t, l, r in queries)
            outcomes.add(signature)
    return outcomes


def examples() -> dict:
    # Identical current PIN observations by two independent readers:
    # ranks add to 6 but one common n=3 image suffices for the answer quotient.
    dup = tuple((reader, 0, i, i + 1)
                for reader in (0, 1) for i in range(3))
    duplicate = causal_rank(3, (), dup)

    # Four PIN epochs read unchanged x0, while the author only overwrites x1.
    repeating = causal_rank(2, (1, 1, 1),
                            tuple((t & 1, t, 0, 1) for t in range(4)))

    # n=1, 3 independently chosen SET values: all four epochs really independent.
    four = tuple((t & 1, t, 0, 1) for t in range(4))
    hidden_history = causal_rank(1, (0, 0, 0), four)
    known_history = causal_rank(1, (0, 0, 0), four,
                                ((0, 0), (1, 1), (2, 0)))

    # Late single-epoch query cannot resurrect initial/old overwritten payload.
    erased = causal_rank(1, (0, 0, 0), ((0, 3, 0, 1),))

    for n, updates, queries, known, z in (
            (3, (), dup, (), duplicate),
            (2, (1, 1, 1), tuple((t & 1, t, 0, 1) for t in range(4)), (), repeating),
            (1, (0, 0, 0), four, (), hidden_history),
            (1, (0, 0, 0), four, ((0, 0), (1, 1), (2, 0)), known_history),
            (1, (0, 0, 0), ((0, 3, 0, 1),), (), erased)):
        if len(independent_answer_signatures(n, updates, queries, known)) != z["answer_tuple_count"]:
            raise AssertionError("independent executable histories refute matrix rank")
    if not (duplicate["joint_rank"] == 3 and
            duplicate["sum_individual_reader_ranks"] == 6 and
            repeating["joint_rank"] == 1 and
            repeating["sum_individual_epoch_ranks"] == 4 and
            hidden_history["joint_rank"] == 4 and
            known_history["joint_rank"] == 1 and
            erased["joint_rank"] == 1):
        raise AssertionError("frozen reuse/overwrite falsifiers changed")
    return {
        "duplicate_reader_PIN_same_epoch": duplicate,
        "unchanged_coordinate_across_many_epochs": repeating,
        "independently_hidden_historical_SET_payloads": hidden_history,
        "charged_public_SET_payloads": known_history,
        "last_writer_erases_prior_answer_dependency": erased,
    }


def report() -> dict:
    f1 = validate_contract()
    if f1["root_novelty"] != "OPEN_UNPROVED":
        raise AssertionError("F1 contract unexpectedly promoted")
    return {
        "classification": CLASSIFICATION,
        "root_novelty": "OPEN_UNPROVED",
        "same_F1_nonfactorizing_theorem": None,
        "joint_F1_page_write_or_query_lower": None,
        "charged_F1_resource_axes_not_derived": {
            axis: None for axis in f1["coordinates"]
            if axis not in ("n", "H", "lambda", "epsilon", "P")
        },
        "hard_adaptive_distribution": None,
        "full_primary_theorem_model_transfer": False,
        "finite_restricted_witnesses": examples(),
        "classical_rank_counting_not_original": True,
    }


if __name__ == "__main__":
    print(json.dumps(report(), indent=2, sort_keys=True))
