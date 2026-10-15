"""HYP-105 #230 AA4-AK: final adjacent-pin connected-C6 genuine Hall sector.

For every true W(3,2^h) and ONE fixed fully injected physical map on each
original source type, classify adjacent pinned C6 exactly by a length-four
physical path and anchor its middle edge to an ACTUAL original neighbor.
Contains an independent brute physical-2factor / 24-permutation oracle.

Separate all-map disjoint-pin INTERNAL-LINK candidate occupancy theorem
strengthens source-indexed pre-Hall mass but does not prove genuine Hall.
"""
from itertools import combinations, permutations
from math import comb, isqrt
from fractions import Fraction

from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import (
    _source_cohort, classify_physical_A_twofactor,
)
from hyp105_issue230_d6aa4ad_opposite_a_hall_transfer import pinned_twofactor_completions

PERM4 = tuple(permutations(range(4)))


def edge(a, b):
    if a == b:
        raise ValueError("physical pair endpoints must differ")
    return (a, b) if a < b else (b, a)


def adjacent_pin_endpoints(e0, e1):
    shared = set(e0) & set(e1)
    if len(shared) != 1:
        return None
    common = next(iter(shared))
    u = next(x for x in e0 if x != common)
    w = next(x for x in e1 if x != common)
    return u, common, w


def adjacent_path_physical_count(a, pins, occupied):
    """Independent direct O(a^3) physical-path oracle (NOT source matching)."""
    if type(a) is not int or a < 6:
        raise ValueError("physical a>=6 required")
    ends = adjacent_pin_endpoints(*pins)
    if ends is None:
        return 0
    u, v, w = ends
    E = set(occupied)
    O = sorted(set(range(a)) - {u, v, w})
    count = 0
    for y in O:
        if edge(w, y) not in E:
            continue
        for z in O:
            if z == y or edge(y, z) not in E:
                continue
            for t in O:
                if t in (y, z):
                    continue
                if edge(z, t) in E and edge(t, u) in E:
                    count += 1
    return count


def exact_original_adjacent_C6_transfer(model, *, side, root, pair_offset, four,
                                        independent=True):
    """Exact ORIGINAL six-distinct incidence-ID B/A (or dual A/B) count.

    A physical connected C6 containing adjacent physical pinned images is
    uniquely u-v-w-y-z-t-u, with y,z,t distinct and outside u,v,w.
    Each accepted original 4-rook matching uniquely chooses the source
    row k matched to the middle physical edge y-z; its opposite source
    factor is in N_GQ(q_k), of size d=s+1. For any other source row j,
    outer edge w-y is matched to q_j. The remaining two source rows
    are matched to z-t and t-u via their (0/1) true original GQ 2x2
    permanent; this is counted without physical-H enumeration.
    """
    a, inc, neighbors, pinned, inv, pins, four = _source_cohort(
        model, side=side, root=root, pair_offset=pair_offset, src_four=four)
    ends = adjacent_pin_endpoints(*pins)
    if ends is None:
        return dict(s=model["s"], side=side, root=root,
                    pinned_physical_adjacent=False,
                    occupied_adjacent_connected_C6_H=0,
                    accepted_original_adjacent_connected_C6_Q=0,
                    original_Hall_lower_NOT_PROVED=True)
    u, v, w = ends
    outside = set(range(a)) - {u, v, w}
    opposite = tuple(tuple(x) for x in model[
        "right_labels" if side == 0 else "left_labels"])
    accepted = 0
    details = []
    for k, row in enumerate(four):
        for middle_source in neighbors[row]:
            yz = opposite[middle_source]
            if not set(yz) <= outside:
                continue
            for y, z in (yz, yz[::-1]):
                first = edge(w, y)
                if first not in inv:
                    continue
                first_source = inv[first]
                for j in range(4):
                    if j == k or first_source not in neighbors[four[j]]:
                        continue
                    R = tuple(i for i in range(4) if i not in (k, j))
                    sites = 0
                    for t in outside - {y, z}:
                        last0, last1 = edge(z, t), edge(t, u)
                        if last0 not in inv or last1 not in inv:
                            continue
                        f0, f1 = inv[last0], inv[last1]
                        ways = int(f0 in neighbors[four[R[0]]] and
                                   f1 in neighbors[four[R[1]]])
                        ways += int(f1 in neighbors[four[R[0]]] and
                                    f0 in neighbors[four[R[1]]])
                        if ways > 1:
                            raise AssertionError("true GQ source girth >=8 violated")
                        sites += ways
                    accepted += sites
                    if sites:
                        details.append((k, middle_source, y, z, j, sites))
    occupied = adjacent_path_physical_count(a, pins, inv)
    # 4 rows for middle edge, each has d ORIGINAL opposite neighbors;
    # two ordered yz orientations, three options for first outer row,
    # remaining 2x2 site injection caps sites <= d per fixed anchor.
    cap = 24 * (model["s"] + 1)**2
    assert accepted <= cap
    if independent:
        brute = independent_adjacent_C6_original_oracle(
            model, side=side, root=root, pair_offset=pair_offset, four=four)
        if accepted != brute["accepted_Q"] or occupied != brute["occupied_H"]:
            raise AssertionError("independent original 24-permutation C6 oracle mismatch")
    return dict(s=model["s"], side=side, root=root,
                pinned_physical_adjacent=True,
                pinned_actual_original_incidence_other_factors=pinned,
                four_original_source_factors=four,
                occupied_adjacent_connected_C6_H=occupied,
                accepted_original_adjacent_connected_C6_Q=accepted,
                original_degree_s_plus_one=model["s"]+1,
                accepted_original_per_cohort_upper=cap,
                source_middle_edge_anchored_channels=tuple(details),
                original_Hall_lower_NOT_PROVED=True)


def independent_adjacent_C6_original_oracle(model, *, side, root, pair_offset, four):
    """Literal physical twofactor enumeration + all 24 real source bijections."""
    a, _, neighbors, _, inv, pins, four = _source_cohort(
        model, side=side, root=root, pair_offset=pair_offset, src_four=four)
    if adjacent_pin_endpoints(*pins) is None:
        return {"occupied_H": 0, "accepted_Q": 0}
    occupied = 0
    accepted = 0
    for H in pinned_twofactor_completions(*pins, a):
        if classify_physical_A_twofactor(H, pins) != "connected_C6":
            continue
        free = sorted(set(H) - set(pins))
        if any(e not in inv for e in free):
            continue
        occupied += 1
        cols = tuple(inv[e] for e in free)
        accepted += sum(
            all(cols[p[i]] in neighbors[four[i]] for i in range(4))
            for p in PERM4)
    return {"occupied_H": occupied, "accepted_Q": accepted}


def adjacent_complete_capacity(a):
    """Exact physical adjacent pinned C6 paths in fully occupied K_a."""
    if type(a) is not int or a < 6:
        raise ValueError("physical a>=6 required")
    return (a-3)*(a-4)*(a-5)


def original_connected_full_join(model, *, side, root, pair_offset, four,
                                 independent=True):
    """Exact all-pin connected C6 = sibling AJ disjoint + new AK adjacent."""
    from hyp105_issue230_d6aa4aj_connected_c6_original_transfer import (
        exact_original_connected_C6_transfer)
    from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import (
        single_original_A_sector_permanent)
    left = exact_original_connected_C6_transfer(
        model, side=side, root=root, pair_offset=pair_offset, four=four)
    right = exact_original_adjacent_C6_transfer(
        model, side=side, root=root, pair_offset=pair_offset, four=four,
        independent=independent)
    count = (left["accepted_original_connected_C6_Q"] +
             right["accepted_original_adjacent_connected_C6_Q"])
    occupied = (left["occupied_physical_connected_C6_H"] +
                right["occupied_adjacent_connected_C6_H"])
    if independent:
        full = single_original_A_sector_permanent(
            model, side=side, root=root, pair_offset=pair_offset, four=four)
        assert count == full["accepted"]["connected_C6"]
        assert occupied == full["occupied_physical_H"]["connected_C6"]
    return dict(accepted_original_full_C6_Q=count,
                occupied_physical_full_C6_H=occupied,
                disjoint_original=left["accepted_original_connected_C6_Q"],
                adjacent_original=right["accepted_original_adjacent_connected_C6_Q"],
                all_pin_relations_genuine_original_C6_EXACT=True,
                all_global_maps_Hall_lower_NOT_PROVED=True)


def original_internal_link_prehall_floor(s):
    """All-global-f,g genuinely rooted 1+3 disjoint pin physical candidates.

    Uses independent sharp original GQ line-pencil theorem in sibling
    #518 and the new absent-cross physical edge incidence double count.
    Produces a deterministic PRE-HALL physical lower >=s^14/384
    for all s=2^h>=16. All accepted original Hall positives may vanish.
    """
    if type(s) is not int or s < 2 or (s & (s-1)):
        raise ValueError("genuine W(3,2^h) power required")
    V = (s+1)*(s*s+1)
    a = (1+isqrt(1+8*V))//2
    if comb(a,2) < V:
        a += 1
    m = comb(a,2)-V
    d = s+1
    N = V*comb(d,2)
    H = (32*m)//a
    safe = max(0, N - a*comb(a-1,2) - H*(a-1)*d*(d-1))
    # Every disjoint physical pin-pair with all FOUR cross-links missing
    # contributes four to the missing physical cross-edge incidence count.
    # Any missing physical edge joins endpoints of at most (a-2)(a-3)
    # disjoint unordered physical pin-pairs, and true GQ line pairs have
    # a unique original root. Hence at most floor(m*(a-2)*(a-3)/4)
    # actual safe rooted pairs can have all four cross links missing.
    dead = m*(a-2)*(a-3)//4
    active = max(0, safe-dead)
    C4 = max(0, 3*comb(a-2,4)-m*(a-4)*(a-5))
    per_direct = (a*a+3)//4 if a>=32 else 0
    physical = active*C4*per_direct
    if s>=16:
        assert 384*physical >= s**14
    # Parent AJ #521 supplies accepted genuine original internal-link
    # Q <= 192*d per fixed root/pins/B-C4. Every active safe cohort has
    # occupied internal-link physical H >= ceil(a^2/4), so its fraction
    # of Hall-positive physical patterns is at most 192*d/ceil(a^2/4).
    # Since a^2>=2(s+1)(s^2+1), this is <=384/(s^2+1).
    source_cap = 192*d
    source_success_fraction = Fraction(source_cap, per_direct) if per_direct else None
    source_success_s_bound = Fraction(384, s*s+1)
    Hall_failed_lower = (
        Fraction(physical)*(1-source_success_s_bound) if s>=32 else Fraction(0))
    if s>=32:
        assert source_success_fraction <= source_success_s_bound < 1
        assert Hall_failed_lower >= Fraction(s**14,384)*(1-source_success_s_bound)
    return dict(s=s, a=a, V=V, missing_global_opposite_pairs=m,
                original_rootpairs_total=N, source_pencil_safe_lower=safe,
                missing_four_cross_bad_upper=dead,
                safe_with_at_least_one_occupied_cross_lower=active,
                occupied_physical_C4_per_original_root_lower=C4,
                occupied_internal_link_C6_per_safe_active_pair_lower=per_direct,
                all_map_indexed_internal_link_preHall_lower=physical,
                original_internal_link_preHall_s14_over384_PROVED=s>=16,
                original_source_internal_link_accepted_Q_per_cohort_UPPER=source_cap,
                original_Hall_positive_fraction_UPPER=source_success_fraction,
                original_success_fraction_s_only_UPPER=source_success_s_bound,
                all_map_true_original_Hall_FAILED_indexed_physical_lower=Hall_failed_lower,
                all_map_true_original_Hall_FAILED_Omega_s14_PROVED=s>=32,
                accepted_original_Hall_positive_lower_NOT_PROVED=True)
