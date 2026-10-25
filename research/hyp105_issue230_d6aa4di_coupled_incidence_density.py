"""AA4-DI: GQ incidence density barrier for minimal 2-external A-bridges.

Study genuine original Generalized Quadrangle W(3,s) bipartite incidence
couplings between A-side 6-point physical cycle configurations P_A and
opposite 5-line local reservoirs L_5 (or 6-line templates L_A) under
arbitrary complete globally injected typed maps f,g into K_a.

Mathematical results:
1. Necessary Point-Coverage Condition:
   For P_A x L_5 to admit ANY accepted A-left / B-right or C/A sixflag,
   every point p in P_A must have degree >= 1 into L_5:
       P_A <= \\bigcup_{m \\in L_5} m.
   In particular, the five points P_A \\ {q} (the 3 C4 completion points
   and 2 external bridge points) must all lie in the line support.

2. GQ Point-Line Incidence Density Bound (all dyadic h >= 1, s = 2^h):
   In W(3,s), V = (s+1)(s^2+1). Five lines L_5 meet at q (at most 2
   intersecting lines l, l0) and contain at most 5s + 4 distinct points.
   The point-coverage fraction is:
       rho(s) = (5s + 4) / ((s + 1)(s^2 + 1)) <= 5 / s^2.
   For uncorrelated maps, the joint 5-point coverage probability is:
       P(Full 5-point Coverage) <= rho(s)^5 <= 3125 / s^10.
   Specifically:
       s = 2: rho = 14/15 = 0.9333, rho^5 = 0.708 (70.8%)
       s = 4: rho = 24/85 = 0.2824, rho^5 = 1.79e-3 (0.18%)
       s = 8: rho = 44/585 = 0.0752, rho^5 = 2.41e-6 (0.00024%)
       s = 16: rho = 84/4369 = 0.0192, rho^5 = 2.63e-9.

3. D6 1-Factor Matching Bound (P_A x L_A):
   A D6 candidate requires a 6-edge matching between P_A (6 points) and
   L_A (6 lines). Since each point has degree s+1 in W(3,s), the expected
   number of 6-matchings under uncorrelated maps is at most:
       6! * ((s+1)/V)^6 = 720 * (s^2 + 1)^(-6) <= 720 / s^12.

4. Adversarial Anti-Incidence No-Go:
   For s >= 4, the uncovered point set V \\ \\bigcup_{m \\in L_5} m has
   size V - (5s + 4) = s^3 + s^2 - 4s - 3 > 0 (61 points at s=4,
   541 points at s=8, >90% of all points). Correlated global maps f,g
   can force external bridge factors to land in the uncovered majority,
   yielding M_A(f, g) = 0 for all minimal 2-external templates.
   Hence NO uniform lower bound M_A >= Omega(s^6) holds across all
   arbitrary correlated legal maps for this minimal mechanism.

Root #230 remains OPEN_WITH_FORMAL_BLOCKER.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb

from hyp105_issue230_d6aa4cq_original_macro_path_cut_gate import _validated_original
from hyp105_issue230_d6aa4cr_exact_BBo_three_matching_transfer import (
    c4_completions_from_single_and_doubled,
    original_nonincident_threepath,
)
from hyp105_issue230_d6aa4cg_four_shared_edge_two_completion import (
    classify_seven_all_a_original_Q,
    physical_column_dual,
    is_connected_column_cycle,
)
from hyp105_issue230_d6aa4dg_two_external_A_bridge import (
    original_two_external_A_completion_catalogue,
    A_SIDE_POSITIVE_CLASSES,
)


def gq_point_coverage_density(s):
    """Exact rational point coverage density of 5 lines in W(3, s)."""
    if not isinstance(s, int) or s < 2 or (s & (s - 1)) != 0:
        raise ValueError("s must be a power of 2 >= 2")
    V = (s + 1) * (s**2 + 1)
    max_covered_points = 5 * s + 4
    rho = Fraction(max_covered_points, V)
    uncorrelated_5point_prob = rho**5
    d6_expected_matchings = Fraction(720, (s**2 + 1) ** 6)
    uncovered_points = V - max_covered_points
    uncovered_fraction = Fraction(uncovered_points, V)
    return {
        "s": s,
        "V": V,
        "max_covered_points": max_covered_points,
        "uncovered_points": uncovered_points,
        "uncovered_fraction": uncovered_fraction,
        "point_coverage_density_rho": rho,
        "uncorrelated_5point_coverage_bound": uncorrelated_5point_prob,
        "d6_uncorrelated_matching_bound": d6_expected_matchings,
        "asymptotic_rho_order": "O(s^-2)",
        "asymptotic_5point_prob_order": "O(s^-10)",
        "asymptotic_d6_matching_order": "O(s^-12)",
    }


def analyze_point_coverage_and_incidence_deficit(PA, L5, point_lines):
    """Analyze point coverage, line degrees, and incidence deficit for PA x L5.

    PA: tuple of 6 distinct original POINT IDs.
    L5: tuple of 5 distinct original LINE IDs.
    point_lines: list/tuple mapping point ID -> collection of incident lines.
    """
    PA = tuple(sorted(PA))
    L5 = tuple(sorted(L5))
    if len(PA) != 6 or len(set(PA)) != 6:
        raise ValueError("six distinct original point IDs required")
    if len(L5) != 5 or len(set(L5)) != 5:
        raise ValueError("five distinct original line IDs required")

    pt_degrees = {}
    for p in PA:
        lines_of_p = set(point_lines[p])
        pt_degrees[p] = sum(1 for ln in L5 if ln in lines_of_p)

    line_degrees = {}
    for ln in L5:
        line_degrees[ln] = sum(1 for p in PA if ln in point_lines[p])

    total_incidences = sum(pt_degrees.values())
    uncovered_points = tuple(sorted(p for p, deg in pt_degrees.items() if deg == 0))
    covered_count = 6 - len(uncovered_points)

    # Deficit: shortfall from 6 incidences + number of uncovered points
    shortfall = max(0, 6 - total_incidences)
    deficit = shortfall + len(uncovered_points)

    is_fully_covered = (len(uncovered_points) == 0)
    admit_A_left_B_right_necessary = (
        is_fully_covered and total_incidences >= 6 and all(deg >= 1 for deg in line_degrees.values())
    )

    return {
        "PA": PA,
        "L5": L5,
        "total_incidences": total_incidences,
        "point_degrees": pt_degrees,
        "line_degrees": line_degrees,
        "covered_points_count": covered_count,
        "uncovered_points": uncovered_points,
        "is_fully_covered": is_fully_covered,
        "deficit": deficit,
        "admit_A_left_B_right_necessary": admit_A_left_B_right_necessary,
    }


def analyze_both_A_bipartite_matchings(PA, LA, point_lines, left_labels, right_labels, incidences):
    """Analyze bipartite incidences and D6 cycle conditions for PA x LA.

    PA: tuple of 6 distinct original POINT IDs.
    LA: tuple of 6 distinct original LINE IDs.
    """
    PA = tuple(sorted(PA))
    LA = tuple(sorted(LA))
    if len(PA) != 6 or len(set(PA)) != 6:
        raise ValueError("six distinct original point IDs required")
    if len(LA) != 6 or len(set(LA)) != 6:
        raise ValueError("six distinct original line IDs required")

    flag_map = {(i, j): z for z, (i, j) in enumerate(incidences)}
    inc_edges = tuple((p, ln) for p in PA for ln in LA if ln in point_lines[p])
    total_inc = len(inc_edges)

    # Find all 6-edge matchings (1-factors) between PA and LA
    matchings = []
    if total_inc >= 6:
        # Check permutations or search
        pts = list(PA)
        def find_match(pt_idx, used_lines, current_flags):
            if pt_idx == 6:
                matchings.append(tuple(sorted(current_flags)))
                return
            p = pts[pt_idx]
            for ln in LA:
                if ln not in used_lines and ln in point_lines[p]:
                    flag_id = flag_map.get((p, ln))
                    if flag_id is not None:
                        find_match(pt_idx + 1, used_lines | {ln}, current_flags + (flag_id,))
        find_match(0, frozenset(), ())

    # Filter D6 candidates: classify Q and check column dual connected cycle
    d6_flags = []
    for Q in matchings:
        kind = classify_seven_all_a_original_Q(Q, left_labels, right_labels, incidences)
        if kind == "D6":
            d6_flags.append(Q)

    return {
        "PA": PA,
        "LA": LA,
        "total_bipartite_incidences": total_inc,
        "has_perfect_matching": len(matchings) > 0,
        "perfect_matching_count": len(matchings),
        "d6_candidate_count": len(d6_flags),
        "d6_flags": tuple(d6_flags),
    }


def audit_reservoir_incidence_coupling(model, limit_reservoirs=12):
    """Audit incidence coupling and point coverage on genuine original reservoirs.

    Iterates through actual occupied P3 x C4 pairs, evaluates point coverage,
    deficit, and validates that NO accepted A-positive Q exists when deficit > 0.
    """
    s, V, a, f, g, pl, lp = _validated_original(model)
    inc = tuple(model["incidences"])
    source_flag = {(i, j): z for z, (i, j) in enumerate(inc)}
    pi = {e: i for i, e in enumerate(f)}
    li = {e: i for i, e in enumerate(g)}

    pairs_examined = 0
    total_PA_L5_evaluated = 0
    fully_covered_count = 0
    deficit_zero_count = 0
    positive_Q_found = set()
    incidence_distribution = Counter()
    covered_distribution = Counter()

    for p in range(V):
        for l in range(V):
            if l in pl[p]:
                continue
            path = original_nonincident_threepath(p, l, pl, lp)
            q, l0 = path[1][0], path[0][1]
            if set(f[p]) & set(f[q]) or set(g[l]) & set(g[l0]):
                continue
            PT = c4_completions_from_single_and_doubled(f[p], f[q], pi, a)
            LT = c4_completions_from_single_and_doubled(g[l], g[l0], li, a)
            for pc in PT:
                for lc in LT:
                    if pairs_examined >= limit_reservoirs:
                        break
                    pairs_examined += 1
                    P5 = tuple(sorted((p, q, *pc)))
                    L5 = tuple(sorted((l, l0, *lc)))
                    PA_catalogue = original_two_external_A_completion_catalogue(f, p, q, pc)
                    LA_catalogue = original_two_external_A_completion_catalogue(g, l, l0, lc)

                    # Check each PA with L5
                    for PA in PA_catalogue:
                        total_PA_L5_evaluated += 1
                        spec = analyze_point_coverage_and_incidence_deficit(PA, L5, pl)
                        incidence_distribution[spec["total_incidences"]] += 1
                        covered_distribution[spec["covered_points_count"]] += 1
                        if spec["is_fully_covered"]:
                            fully_covered_count += 1
                        if spec["deficit"] == 0:
                            deficit_zero_count += 1

                        # Forward Q search
                        flags = tuple(source_flag[i, j] for i in PA for j in L5 if (i, j) in source_flag)
                        if len(flags) >= 6:
                            for six in combinations(flags, 6):
                                kind = classify_seven_all_a_original_Q(six, f, g, inc)
                                if kind in A_SIDE_POSITIVE_CLASSES:
                                    positive_Q_found.add(tuple(sorted(six)))
                                    # Verification: if a positive Q was found, deficit MUST be 0!
                                    if spec["deficit"] != 0:
                                        raise AssertionError(
                                            "Positive Q discovered in a reservoir with non-zero deficit!"
                                        )

                if pairs_examined >= limit_reservoirs:
                    break
            if pairs_examined >= limit_reservoirs:
                break
        if pairs_examined >= limit_reservoirs:
            break

    full_coverage_rate = (
        float(Fraction(fully_covered_count, total_PA_L5_evaluated))
        if total_PA_L5_evaluated > 0
        else 0.0
    )

    return {
        "s": s,
        "V": V,
        "pairs_examined": pairs_examined,
        "total_PA_L5_evaluated": total_PA_L5_evaluated,
        "fully_covered_count": fully_covered_count,
        "full_coverage_rate": full_coverage_rate,
        "deficit_zero_count": deficit_zero_count,
        "positive_Q_found_count": len(positive_Q_found),
        "incidence_distribution": dict(sorted(incidence_distribution.items())),
        "covered_distribution": dict(sorted(covered_distribution.items())),
    }
