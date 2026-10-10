#!/usr/bin/env python3
"""D1-C0: exact classical multi-version observation entropy; ROOT OPEN.

Counts only exact RANGE_PARITY-observable BITMAP TUPLES at named epochs, not
authenticated F1 proofs, malicious-server messages, physical pages or GC.
An online SET may be a no-op or flip exactly one coordinate per epoch.
"""
from __future__ import annotations

from functools import lru_cache
from itertools import combinations, product
from math import comb
import json


CLASSIFICATION = "CLASSICAL_EXACT_PIN_OBSERVATION_ENTROPY_STOP_NOVELTY"


def ball_volume(n: int, steps: int) -> int:
    if type(n) is not int or n < 1 or type(steps) is not int or steps < 0:
        raise ValueError("positive n and nonnegative number of SET steps")
    return sum(comb(n, j) for j in range(min(n, steps) + 1))


def checked_epochs(times: tuple[int, ...]) -> tuple[int, ...]:
    if (type(times) is not tuple or not times
            or any(type(x) is not int or x < 0 for x in times)
            or any(a >= b for a,b in zip(times,times[1:]))):
        raise ValueError("public observed epochs must be sorted, unique, nonnegative")
    return times


def distinguishable_tuples(n: int, times: tuple[int, ...]) -> int:
    checked_epochs(times)
    if type(n) is not int or n < 1:
        raise ValueError("positive number of binary state bits")
    result = 1 << n
    for a,b in zip(times,times[1:]):
        result *= ball_volume(n,b-a)
    return result


def exact_minimum_fixed_bits(count: int) -> int:
    if type(count) is not int or count < 1:
        raise ValueError("positive number of distinct messages")
    return (count-1).bit_length()


@lru_cache(maxsize=256)
def _ball_masks(n: int, steps: int) -> tuple[int, ...]:
    if type(n) is not int or not 1 <= n <= 12:
        raise ValueError("finite enumerative reference supports n=1..12")
    ball_volume(n,steps)
    return tuple(mask for mask in range(1<<n)
                 if mask.bit_count() <= steps)


def rank_observations(n: int, times: tuple[int, ...],
                      bitmaps: tuple[int, ...]) -> int:
    checked_epochs(times)
    if (type(bitmaps) is not tuple or len(bitmaps)!=len(times)
            or any(type(v) is not int or not 0<=v<(1<<n) for v in bitmaps)):
        raise ValueError("one valid exact binary bitmap per observed epoch")
    value=bitmaps[0]
    for t0,t1,x,y in zip(times,times[1:],bitmaps,bitmaps[1:]):
        masks=_ball_masks(n,t1-t0)
        diff=x^y
        if diff.bit_count()>t1-t0:
            raise ValueError("unreachable named snapshot tuple")
        value=value*len(masks)+masks.index(diff)
    return value


def unrank_observations(n: int, times: tuple[int, ...],
                        code: int) -> tuple[int, ...]:
    checked_epochs(times)
    count=distinguishable_tuples(n,times)
    if (type(code) is not int or not 0<=code<count or n>12):
        raise ValueError("rank outside finite supported observation space")
    digits=[]
    for t0,t1 in reversed(tuple(zip(times,times[1:]))):
        masks=_ball_masks(n,t1-t0)
        code,digit=divmod(code,len(masks))
        digits.append(masks[digit])
    if code >= 1<<n:
        raise AssertionError("invalid mixed-radix initial bitmap")
    bitmaps=[code]
    for mask in reversed(digits):
        bitmaps.append(bitmaps[-1]^mask)
    return tuple(bitmaps)


def finite_canonical_paths(n: int, H: int):
    """Independent update-by-update enumerator; never calls product formula.

    For each initial word and each of H steps, symbol 0 is *a no-op*,
    symbol i+1 flips bit i. Every legal SET(i,b) snapshot path appears;
    multiple no-op labels produce the same path and are rightly deduplicated
    because this oracle observes only snapshot answers, not update receipts.
    """
    if type(n) is not int or not 1<=n<=6 or type(H) is not int or not 0<=H<=4:
        raise ValueError("finite exhaustive oracle limited to n<=6,H<=4")
    for initial in range(1<<n):
        for steps in product(range(n+1),repeat=H):
            state=initial
            path=[state]
            for step in steps:
                if step:
                    state^=1<<(step-1)
                path.append(state)
            yield tuple(path)


def independent_observation_oracle(n: int, H: int,
                                   times: tuple[int, ...]) -> dict:
    checked_epochs(times)
    if times[-1]>H:
        raise ValueError("observer cannot query future epoch")
    observed=set()
    for path in finite_canonical_paths(n,H):
        observed.add(tuple(path[t] for t in times))
    closed_form=distinguishable_tuples(n,times)
    if len(observed)!=closed_form:
        raise AssertionError("independent online transition oracle contradicts formula")
    ranks=set()
    for snapshots in observed:
        r=rank_observations(n,times,snapshots)
        if unrank_observations(n,times,r)!=snapshots:
            raise AssertionError("exact finite enumerative coding roundtrip broken")
        ranks.add(r)
    if ranks!=set(range(closed_form)):
        raise AssertionError("mixed radix encoding is not onto all valid histories")
    return {
        "classification":CLASSIFICATION,
        "n":n,"H":H,"observed_epochs":list(times),
        "distinct_answer_tuples":len(observed),
        "exact_minimum_fixed_code_bits":exact_minimum_fixed_bits(closed_form),
        "independent_snapshot_bits_upper_naive":n*len(times),
        "rank_unrank_bijection":True,
        "counting_only_not_physical_F1_storage_or_verified_cost":True,
        "root_novelty":"OPEN_UNPROVED",
    }


def labeled_SET_transcript_count(n: int, H: int) -> int:
    """Count labeled SET(i,b) receipts together with initial epoch0 bitmap.

    A legal SET has 2n labels at each epoch, including differently labeled
    no-op writes. This is NOT a byte cost for signed receipts or fresh roots.
    """
    if type(n) is not int or n < 1 or type(H) is not int or H < 0:
        raise ValueError("positive n and nonnegative horizon required")
    return (1 << n) * (2*n)**H


def independent_labeled_receipt_oracle(n: int, H: int) -> dict:
    """Independent SET(i,b) enumeration vs bitmap-only projection."""
    if type(n) is not int or not 1 <= n <= 4 or type(H) is not int or not 0 <= H <= 3:
        raise ValueError("finite receipt census supports n<=4, H<=3")
    observed_joint=set()
    observed_bitmap_paths=set()
    for initial in range(1<<n):
        for labels in product(range(2*n), repeat=H):
            state=initial
            path=[state]
            for label in labels:
                coordinate,bit=divmod(label,2)
                state=(state|(1<<coordinate)) if bit else (state&~(1<<coordinate))
                path.append(state)
            observed_joint.add((initial,labels))
            observed_bitmap_paths.add(tuple(path))
    if (len(observed_joint)!=labeled_SET_transcript_count(n,H)
            or len(observed_bitmap_paths)!=distinguishable_tuples(
                n,tuple(range(H+1)))):
        raise AssertionError("labeled receipts vs bitmap-only entropy census failed")
    return {
        "n":n, "H":H,
        "distinct_initial_plus_labeled_SET_transcripts":len(observed_joint),
        "distinct_bitmap_answer_paths_only":len(observed_bitmap_paths),
        "update_labels_must_be_accounted_not_treated_as_free":True,
        "authenticated_receipt_and_wire_bytes_priced":False,
        "root_novelty":"OPEN_UNPROVED",
    }


def report():
    # The n=5,H=3 examples deliberately compare observing ALL historical
    # epochs against just two independently PINned epochs + latest.
    all_time=(0,1,2,3)
    two_pins_latest=(0,2,3)
    return {
        "classification": CLASSIFICATION,
        "count_formula": "2^n * product_j(sum_{i=0}^{min(n,Delta_j)} binom(n,i))",
        "full_history_formula": "2^n*(n+1)^H",
        "exact_bit_count_uses_integer_bit_length_not_float_log":True,
        "all_epochs":independent_observation_oracle(5,3,all_time),
        "author_labeled_SET_scope_comparator":independent_labeled_receipt_oracle(4,3),
        "two_pins_plus_latest":independent_observation_oracle(5,3,two_pins_latest),
        "source_security_and_page_costs":None,
        "asserted_new_joint_lower_bound":False,
        "root_novelty":"OPEN_UNPROVED",
    }


if __name__=="__main__":
    print(json.dumps(report(),indent=2,sort_keys=True))
