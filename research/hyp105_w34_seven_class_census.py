"""AA4-SEVEN34: exact finite seven original GF5 classes on true W32/W34.

Native kernel enumerates canonical B/C original-source endpoint partitions
without enumerating choose(425,6), and the independent verified #667 D6
physical C6 source bijection supplies the disjoint A/A accepted sector.

For fixed f,g every ORIGINAL sixflag is counted once in exactly one of
the seven historically accepted strictly positive classes or rejected.
This only certifies the necessary GF5 floor, not exact full R3/ASET or
an all-h extremal theorem. Source ID provenance is never randomized.
"""
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from tempfile import TemporaryDirectory
import json
import os
import shutil
import subprocess

from hyp105_b1_symplectic import symplectic_gq
from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_g5e2b3e1b0_seven_signature import (
    R3_CERTIFIED_FLOORS, classify_seven_prechecked, seven_census,
)
from hyp105_k32_saturated_unit_multiplicity import (
    real_W34_two_disjoint_saturated_blocks,
)
from hyp105_saturated_fresh_extension_zero_w34 import (
    ZERO_OTHER_LINE_PAIR_PERMUTATION,
)
from hyp105_w34_fixed_map_d6_stratified import (
    true_source_D6_stratified_by_frozen_lines,
)

CLASS_NAMES = (
    "B-left/A-right", "A-left/B-right", "C/A", "C/B",
    "B/B-overlap", "B/B-disjoint",
)
SOURCE = Path(__file__).with_name("hyp105_w34_seven_class_census.cpp")


def _model_text(power, point_pairs, line_pairs, flags):
    s = 1 << power
    V = (s + 1)*(s*s + 1)
    a = min(x for x in range(2, 100) if x*(x-1)//2 >= V)
    f = tuple(tuple(z) for z in point_pairs)
    g = tuple(tuple(z) for z in line_pairs)
    if len(f) != V or len(g) != V or len(flags) != V*(s+1):
        raise ValueError("requires complete genuine original GQ factor model")
    for labels in (f, g):
        if len(set(labels)) != V or any(
                len(z) != 2 or type(z[0]) is not int or
                type(z[1]) is not int or not 0 <= z[0] < z[1] < a
                for z in labels):
            raise ValueError("invalid full typed original pair injection")
    if len(set(flags)) != len(flags):
        raise ValueError("repeated original incidence flag")
    lines = [f"{V} {a} {len(flags)}"]
    lines.extend(f"{x} {y}" for x, y in f)
    lines.extend(f"{x} {y}" for x, y in g)
    lines.extend(f"{p} {l}" for p, l in flags)
    return "\n".join(lines) + "\n"


def compiled_sixset_BC_counts(binary, power, f, g, flags, *,
                             timeout_seconds=1200):
    """Run exhaustive B/C-only count and independently referee witnesses."""
    raw = subprocess.run(
        [str(binary)], input=_model_text(power, f, g, flags),
        text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        timeout=timeout_seconds, check=True,
    )
    lines = raw.stdout.splitlines()
    if len(lines) < 2 or not lines[0].startswith("COUNTS ") or (
            not lines[1].startswith("STATS ")):
        raise AssertionError("native exact source census output corrupted")
    integers = [int(z) for z in lines[0].split()[1:]]
    if len(integers) != len(CLASS_NAMES) or any(z < 0 for z in integers):
        raise AssertionError("missing six historically accepted non-D6 classes")
    stats = tuple(int(z) for z in lines[1].split()[1:])
    if len(stats) != 4:
        raise AssertionError("missing exhaustive canonical source candidate sizes")
    counts = dict(zip(CLASS_NAMES, integers))
    witnesses = {}
    for line in lines[2:]:
        fields = line.split()
        if len(fields) != 8 or fields[0] != "WITNESS":
            raise AssertionError("native original six-ID witness malformed")
        index = int(fields[1])
        ids = tuple(sorted(int(z) for z in fields[2:]))
        if index not in range(6) or len(ids) != 6 or (
                len(set(ids)) != 6 or
                index in witnesses or
                not all(0 <= i < len(flags) for i in ids)):
            raise AssertionError("bad original six-incidence certificate")
        label = CLASS_NAMES[index]
        if classify_seven_prechecked(ids, f, g, flags) != label:
            raise AssertionError("historical independent GF5 class refuted")
        witnesses[index] = ids
    if set(witnesses) != {i for i, z in enumerate(integers) if z}:
        raise AssertionError("missing independent accepted GF5 witness")
    return {
        "non_D6_original_GF5_counts": counts,
        "distinct_original_source_sixset_witnesses": {
            CLASS_NAMES[k]: witnesses[k] for k in sorted(witnesses)
        },
        "canonical_B_shapes_both_axes": stats[0],
        "canonical_C_shapes_both_axes": stats[1],
        "exhaustive_B_original_sixset_candidates_both_axes": stats[2],
        "exhaustive_C_original_sixset_candidates_both_axes": stats[3],
        "native_historical_GF5_witnesses_verified": True,
    }


def build_census_binary(destination):
    """Build a local, noncommitted executable from source. No system writes."""
    compiler = shutil.which("g++")
    if compiler is None:
        raise RuntimeError("g++ is required for exact hosted B/C original census")
    proc = subprocess.run(
        [compiler, "-O3", "-std=c++20", "-DNDEBUG",
         "-Wall", "-Wextra", "-Werror", str(SOURCE), "-o", str(destination)],
        text=True, capture_output=True, timeout=120, check=True,
    )
    return destination


def certified_model_seven_counts(binary, power, f, g, flags, J=()):
    """Strict six original-class census plus independent D6 source DFS."""
    native = compiled_sixset_BC_counts(binary, power, f, g, flags)
    d6_profile = true_source_D6_stratified_by_frozen_lines(
        power, f, g, frozenset(J))
    counts = {"D6": d6_profile["exact_original_GF5_D6"]}
    counts.update(native["non_D6_original_GF5_counts"])
    if set(counts) != set(R3_CERTIFIED_FLOORS):
        raise AssertionError("not the seven accepted historical GF5 classes")
    if any(x < 0 for x in counts.values()):
        raise AssertionError("negative original source motif count")
    numerator = sum(counts[name]*weight
                    for name, weight in R3_CERTIFIED_FLOORS.items())
    return {
        "s": 1 << power,
        "V": len(f),
        "original_source_flags": len(flags),
        "all_seven_original_GF5_classes": counts,
        "global_S_seven": sum(counts.values()),
        "GF5_seven_necessary_R3_floor_numerator": numerator,
        "GF5_seven_necessary_R3_floor_denominator": 51**6,
        "GF5_seven_necessary_R3_floor": str(Fraction(numerator, 51**6)),
        "original_D6_by_unfrozen_source_lines":
            d6_profile["D6_by_unfrozen_source_lines"],
        "native_original_BC": native,
        "full_GF5_R3_computed": False,
        "root_universal_Omega_s6_proved": False,
    }


def true_W34_positive_zero_all_seven_census():
    """Exact certified whole-seven comparison; source original flags fixed."""
    _, f, g_pos, flags, selected = (
        real_W34_two_disjoint_saturated_blocks(return_inputs=True))
    s, V, original = (
        (4, 85, tuple(symplectic_gq(2)[3]))
    )
    if len(f) != V or tuple(flags) != original or len(flags) != 425:
        raise AssertionError("not true original symplectic W34")
    J = frozenset(flags[i][1] for i in selected)
    if len(selected) != len(J) != 12:
        raise AssertionError("wrong original frozen selected source")
    free = tuple(z for z in combinations(range(14), 2)
                 if z not in {g_pos[l] for l in J})
    other = tuple(l for l in range(V) if l not in J)
    if (len(free), len(other)) != (79, 73):
        raise AssertionError("missing true source unselected line labels")
    g_zero = list(g_pos)
    for l, offset in zip(other, ZERO_OTHER_LINE_PAIR_PERMUTATION):
        g_zero[l] = free[offset]
    g_zero = tuple(g_zero)
    if len(set(g_zero)) != V or (
            any(g_pos[l] != g_zero[l] for l in J)):
        raise AssertionError("not the immutable #665 W34 counterfactual")
    with TemporaryDirectory(prefix="hyp105-seven-gf5-") as tmp:
        binary = build_census_binary(Path(tmp)/"exact-original-seven")
        positive = certified_model_seven_counts(
            binary, 2, f, g_pos, flags, J)
        zero = certified_model_seven_counts(
            binary, 2, f, g_zero, flags, J)
    if (positive["all_seven_original_GF5_classes"]["D6"],
            zero["all_seven_original_GF5_classes"]["D6"]) != (7567, 8110):
        raise AssertionError("existing independently certified W34 D6 drift")
    difference = {
        name: zero["all_seven_original_GF5_classes"][name] -
        positive["all_seven_original_GF5_classes"][name]
        for name in R3_CERTIFIED_FLOORS
    }
    return {
        "scope": "same original W34 complete f, same 12 frozen original g_J",
        "identical_complete_point_pair_labels": True,
        "identical_selected_original_incidence_flags_and_line_labels": True,
        "positive": positive, "zero": zero,
        "zero_minus_positive_by_historical_GF5_class": difference,
        "global_S_seven_zero_minus_positive":
            zero["global_S_seven"]-positive["global_S_seven"],
        "certified_GF5_R3_floor_numerator_zero_minus_positive":
            zero["GF5_seven_necessary_R3_floor_numerator"] -
            positive["GF5_seven_necessary_R3_floor_numerator"],
        "all_seven_classes_finite_W34_exhaustive": True,
        "no_all_h_root_A_or_B_claim": True,
    }


if __name__ == "__main__":
    print("HYP105_AA4_SEVEN34_CERTIFICATE=" +
          json.dumps(true_W34_positive_zero_all_seven_census(),
                     sort_keys=True))
