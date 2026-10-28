"""AA4-FIXD6: same-f, same-frozen-g true W34 D6 displacement census.

Original-source sixsets are counted, not signed GF(5) events.
One independent *rainbow physical C6 / original-ID DFS* is compared
with the existing pair-codegree triangle oracle (#657).  Counts are
stratified by the number of ORIGINAL source-line IDs outside the
frozen J, never by artificial physical edges.  Zero local radius-2
K3,2 extension mass is NOT equated with zero global accepted D6.

Universal conservation lemma (all dyadic s, any complete f and two
complete g maps agreeing on J): every accepted original seven-class
sixset using exclusively source lines J has the same acceptance/tag
under both completions.  Only the D6 stratum is enumerated here.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
import json

from hyp105_full_physical_degree_tail import genuine_source
from hyp105_physical_degree_energy import minimal_alphabet
from hyp105_physical_rainbow_c6 import build_original_physical_graph
from hyp105_g5e2b3e1b0_seven_signature import (
    R3_CERTIFIED_FLOORS, classify_seven_prechecked,
)
from hyp105_pair_codegree_triangle_d6 import exact_pair_codegree_triangle_d6
from hyp105_k32_saturated_unit_multiplicity import (
    genuine_source_saturated_unit_transfer,
    real_W34_two_disjoint_saturated_blocks,
)
from hyp105_saturated_fresh_extension_zero_w34 import (
    ZERO_OTHER_LINE_PAIR_PERMUTATION,
)


def true_source_D6_stratified_by_frozen_lines(
        power, f, g, frozen_line_ids, selected_original_flag_ids=()):
    """Exact original GF5 D6 histogram by count of *unfrozen* source lines.

    Enumerate only rainbow simple C6, using the independent physical
    path DFS rather than the pair-codegree inversion.  Prove every
    counted sixset has six different actual original flags, points and
    lines; require acceptance from the historical seven-class GF5
    classifier.  The return strata are an exact partition of all D6.
    """
    s, V, flags = genuine_source(power)
    f = tuple(map(tuple, f))
    g = tuple(map(tuple, g))
    J = frozenset(frozen_line_ids)
    I = frozenset(selected_original_flag_ids)
    if any(type(l) is not int or not 0 <= l < V for l in J):
        raise ValueError("frozen source lines outside original geometry")
    if any(type(i) is not int or not 0 <= i < len(flags) for i in I):
        raise ValueError("selected source incidence IDs outside original geometry")
    a = minimal_alphabet(V)
    adj, arcs = build_original_physical_graph(s, f, g, flags)
    seen = set()
    strata = Counter()
    selected_strata = Counter()
    frozen_only = set()
    path = []
    used = set()
    used_x, used_y = set(), set()

    def visit(root, last):
        if len(path) == 6:
            if root not in adj[last] or path[1] >= last:
                return
            ids = tuple(sorted(arcs[path[k],path[(k+1) % 6]]
                               for k in range(6)))
            if (len(set(ids)) != 6 or
                    len({flags[i][0] for i in ids}) != 6 or
                    len({flags[i][1] for i in ids}) != 6):
                raise AssertionError("rainbow physical C6 reused real source factor")
            if ids in seen:
                raise AssertionError("different physical C6 share an original sixset")
            if classify_seven_prechecked(ids, f, g, flags) != "D6":
                raise AssertionError("six actual original flags failed historical D6")
            seen.add(ids)
            outside = sum(flags[i][1] not in J for i in ids)
            strata[outside] += 1
            selected_strata[len(I.intersection(ids))] += 1
            if outside == 0:
                frozen_only.add(ids)
            return
        for v in sorted(adj[last]):
            if v <= root or v in used or v[0] in used_x or v[1] in used_y:
                continue
            path.append(v)
            used.add(v)
            used_x.add(v[0])
            used_y.add(v[1])
            visit(root, v)
            used_y.remove(v[1])
            used_x.remove(v[0])
            used.remove(v)
            path.pop()

    for root in sorted(adj):
        path.append(root)
        used.add(root)
        used_x.add(root[0])
        used_y.add(root[1])
        visit(root, root)
        used_y.remove(root[1])
        used_x.remove(root[0])
        used.remove(root)
        path.pop()

    if sum(strata.values()) != len(seen):
        raise AssertionError("original source D6 stratum partition malformed")
    return {
        "s": s, "V": V, "alphabet": a,
        "true_original_source_flags": len(flags),
        "full_physical_undirected_edges": len(arcs)//2,
        "frozen_source_lines": len(J),
        "selected_original_incidence_IDs": len(I),
        "exact_original_GF5_D6": len(seen),
        "D6_by_unfrozen_source_lines": {k: strata[k] for k in range(7)},
        "D6_by_selected_original_incidence_IDs":
            {k: selected_strata[k] for k in range(7)},
        "frozen_only_original_D6_sixsets": frozenset(frozen_only),
        "all_seven_class_total_computed": False,
        "root_all_h_universal_Omega_s6_proved": False,
    }


def true_W34_fixed_f_frozen_g_D6_displacement():
    """Full original D6 census for POS/ZERO #665 TRUE W(3,4) completions.

    Both legal maps freeze identical f and g_J; only 73 unselected
    source-line assignments can differ.  True original source flags are
    unchanged, both full physical diagonals retained.
    """
    _, f, g_pos, flags, selected = (
        real_W34_two_disjoint_saturated_blocks(return_inputs=True)
    )
    s, V, original = genuine_source(2)
    if (s, V, tuple(flags)) != (4, 85, original):
        raise AssertionError("not the same genuine symplectic W34 source")
    frozen_lines = frozenset(flags[i][1] for i in selected)
    if len(frozen_lines) != 12 or len(selected) != 12:
        raise AssertionError("expected 12 original frozen selected lines")
    a = minimal_alphabet(V)
    free_labels = tuple(z for z in combinations(range(a), 2)
                        if z not in {g_pos[l] for l in frozen_lines})
    unselected_lines = tuple(l for l in range(V) if l not in frozen_lines)
    if (len(free_labels), len(unselected_lines),
            len(ZERO_OTHER_LINE_PAIR_PERMUTATION)) != (79, 73, 79):
        raise AssertionError("missing unused full-injection pair slots")
    if set(ZERO_OTHER_LINE_PAIR_PERMUTATION) != set(range(79)):
        raise AssertionError("fixed ZERO line permutation is not a bijection")
    g_zero = list(g_pos)
    for l, j in zip(unselected_lines, ZERO_OTHER_LINE_PAIR_PERMUTATION):
        g_zero[l] = free_labels[j]
    g_zero = tuple(g_zero)
    if any(g_pos[l] != g_zero[l] for l in frozen_lines):
        raise AssertionError("a selected original source line label was altered")

    result = {}
    profiles = {}
    for tag, g in (("positive", g_pos), ("zero", g_zero)):
        profile = true_source_D6_stratified_by_frozen_lines(
            2, f, g, frozen_lines, selected
        )
        # Independent algorithm: all three pair-codegree witnesses from
        # ACTUAL original physical arc provenance, exactly double-count.
        pc3 = exact_pair_codegree_triangle_d6(
            2, f, g, verify_historical_gf5=True,
            verify_existing_C6_oracle=False
        )
        if (profile["exact_original_GF5_D6"] != pc3["accepted_original_D6"]
                or pc3["oriented_pair_codegree_witness_triples"] !=
                2*profile["exact_original_GF5_D6"]):
            raise AssertionError("source-ID DFS and pair-codegree disagree")
        local = genuine_source_saturated_unit_transfer(2, f, g, selected)
        if local["saturated_original_source_K32_blocks"] != 2:
            raise AssertionError("same selected original saturated blocks lost")
        if local["two_swap_D6_extension_memberships"] > (
                profile["exact_original_GF5_D6"]):
            raise AssertionError("certified radius-two original D6 exceeds global D6")
        d6 = profile["exact_original_GF5_D6"]
        profiles[tag] = profile
        result[tag] = {
            "global_accepted_original_GF5_D6": d6,
            "D6_by_unfrozen_source_lines": profile[
                "D6_by_unfrozen_source_lines"],
            "D6_by_selected_source_flags": profile[
                "D6_by_selected_original_incidence_IDs"],
            "global_K33_sector_D6": pc3[
                "accepted_original_D6_from_complete_K33"],
            "global_non_K33_sector_D6": pc3[
                "non_K33_accepted_original_D6"],
            "selected_saturated_K32_blocks": local[
                "saturated_original_source_K32_blocks"],
            "actual_local_full_H_fresh_hub_pair_mass": local[
                "full_H_fresh_common_neighbor_mass"],
            "accepted_original_D6_two_flag_extension_lower": local[
                "two_swap_D6_extension_memberships"],
            "rigorous_seven_class_S_lower_from_D6_only": d6,
            "rigorous_GF5_R3_floor_from_D6_only": str(Fraction(
                R3_CERTIFIED_FLOORS["D6"]*d6, 51**6)),
            "source_ID_DFS_pair_codegree_agree": True,
        }

    if (profiles["positive"]["frozen_only_original_D6_sixsets"] !=
            profiles["zero"]["frozen_only_original_D6_sixsets"]):
        raise AssertionError("unchanged source g_J illegally changed fixed-only D6")
    if (result["positive"]["actual_local_full_H_fresh_hub_pair_mass"],
            result["zero"]["actual_local_full_H_fresh_hub_pair_mass"]) != (4, 0):
        raise AssertionError("parent #665 local positive/zero contrast lost")
    return {
        "scope": "TRUE W(3,4), same full f and selected 12-line g_J",
        "s": 4, "V": 85, "a": 14, "original_source_flags": 425,
        "source_lines_frozen": 12, "source_lines_unfrozen": 73,
        "full_source_incidence_IDs_selected": 12,
        "same_full_f_and_frozen_g_J": True,
        "frozen_only_D6_original_sixsets_identical": True,
        "frozen_only_original_D6_count": len(
            profiles["positive"]["frozen_only_original_D6_sixsets"]),
        "positive": result["positive"],
        "zero": result["zero"],
        "global_D6_zero_minus_positive": (
            result["zero"]["global_accepted_original_GF5_D6"] -
            result["positive"]["global_accepted_original_GF5_D6"]),
        "complete_original_seven_class_census": False,
        "universal_all_h_S_s_omega_s6_proved": False,
        "infinite_counterexample_to_root": False,
    }


if __name__ == "__main__":
    print(json.dumps(true_W34_fixed_f_frozen_g_D6_displacement(),
                     indent=2, sort_keys=True))
