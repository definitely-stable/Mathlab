"""AA4-CU: TRUE ORIGINAL W(3,2^h) 3-matching exterior-cube energy.

An original GQ's incidence graph has girth eight. Every 3x3
incidence submatrix has at most ONE perfect matching, hence
per(B) = det(B)**2 exactly over Z. Consequently a fixed ORIGINAL
B/B-overlap source P3 anchor's accepted historical GF(5) count
is a coordinate-compressed squared Frobenius norm of exterior^3(M).

The unrestricted exterior energy is determined exactly by the
GQ parameters; the physical C4 projections are NOT forced to
intersect that energy at every anchor or globally. No root A/B/C.
"""
from itertools import combinations
from math import comb

from hyp105_issue230_d6aa4cq_original_macro_path_cut_gate import _validated_original
from hyp105_issue230_d6aa4cr_exact_BBo_three_matching_transfer import (
    original_nonincident_threepath,
    c4_completions_from_single_and_doubled,
)


def incidence_minor3_det(points, lines, point_lines):
    """Signed 3x3 determinant of TRUE original source flag incidence matrix."""
    if len(points) != 3 or len(lines) != 3 or len(set(points)) != 3 or len(set(lines)) != 3:
        raise ValueError("three different ORIGINAL point and line factors required")
    a = tuple(tuple(int(l in point_lines[p]) for l in lines) for p in points)
    return (a[0][0]*(a[1][1]*a[2][2] - a[1][2]*a[2][1])
            - a[0][1]*(a[1][0]*a[2][2] - a[1][2]*a[2][0])
            + a[0][2]*(a[1][0]*a[2][1] - a[1][1]*a[2][0]))


def true_original_exterior_energy_parameters(s):
    """All-h exact unrestricted norm ||exterior^3 M||_F^2 in two ways.

    r=s(s+1)^2/2. The squared singular values of the point-line
    incidence matrix M are (s+1)^2 (once), 2s (r times), 0 otherwise.
    Their third elementary symmetric polynomial is the global
    number of three-edge matchings, since girth8 => minors 0,+/-1.

    Independent direct ordered-edge matching count:
    m*(m-2d+1)*(m-4d+2) + 2*m*(d-1)^2 all divided by 6,
    where m=V*d and d=s+1.
    """
    if type(s) is not int or s < 2:
        raise ValueError("original GQ integer order >=2 required")
    V = (s+1)*(s*s+1)
    d = s+1
    m = V*d
    r = s*(s+1)**2//2
    if r*2 != s*(s+1)**2:
        raise AssertionError("nonintegral GQ point-collinearity multiplicity")
    spectral = comb(r,3)*(2*s)**3 + comb(r,2)*(s+1)**2*(2*s)**2
    numerator = m*(m-2*d+1)*(m-4*d+2)+2*m*(d-1)**2
    if numerator%6:
        raise AssertionError("ordered original 3-matching count not divisible by 6")
    combinatorial = numerator//6
    if spectral != combinatorial:
        raise AssertionError("independent GQ spectrum and edge matchings disagree")
    return {"s":s,"V":V,"original_incidence_flags":m,"source_degree":d,
            "incidence_matrix_rank":r+1,
            "nontrivial_squared_singular_value":2*s,
            "nontrivial_multiplicity":r,
            "global_exterior3_frobenius_squared":spectral,
            "independent_ordered_edges_matching_count":combinatorial,
            "source_permanent_to_signed_minor_square_is_exact":True,
            "uniform_physical_local_matching_lower_UNPROVED":True,
            "root_230":"OPEN_WITH_FORMAL_BLOCKER"}


def original_source_anchor_exterior_energy(model, anchor_pairs, collect_zero=False):
    """Actual original source P3 anchors, one fixed COMPLETE correlated f,g.

    Left and right physical C4 images use genuine source factor IDs,
    not simulated independent random completion edges. Squares of
    original 3x3 incidence minors count actual accepted GF5 BBo
    Q exactly by AA4-CR's unique source path and GQ girth8.
    """
    s, V, a, f, g, pl, lp = _validated_original(model)
    pairs = tuple(tuple(x) for x in anchor_pairs)
    if not pairs or len(pairs) != len(set(pairs)):
        raise ValueError("one or more distinct genuine original nonincident anchors")
    inv_f = {tuple(sorted(e)):j for j,e in enumerate(f)}
    inv_g = {tuple(sorted(e)):j for j,e in enumerate(g)}
    details = []
    total_squared = total_abs = total_pos = total_neg = total_candidate = 0
    for p,l in pairs:
        if (type(p) is not int or type(l) is not int
                or not 0 <= p < V or not 0 <= l < V or l in pl[p]):
            raise ValueError("genuine original nonincident point-line anchor required")
        path=original_nonincident_threepath(p,l,pl,lp)
        q, l0=path[1][0],path[0][1]
        if frozenset(f[p]) & frozenset(f[q]) or frozenset(g[l]) & frozenset(g[l0]):
            left=right=()
        else:
            left=c4_completions_from_single_and_doubled(f[p],f[q],inv_f,a)
            right=c4_completions_from_single_and_doubled(g[l],g[l0],inv_g,a)
        pos=neg=zero=0
        first_zero=None
        for P in left:
            for L in right:
                det=incidence_minor3_det(P,L,pl)
                if det not in (-1,0,1):
                    raise AssertionError("TRUE original W3 cannot have two perfect 3x3 matchings")
                if det>0:pos+=1
                elif det<0:neg+=1
                else:
                    zero+=1
                    if collect_zero and first_zero is None:
                        first_zero=(P,L)
        pair_count=len(left)*len(right)
        if pos+neg+zero!=pair_count:
            raise AssertionError("exterior-3 compression partition incomplete")
        total_candidate+=pair_count
        total_squared+=pos+neg
        total_abs+=pos+neg
        total_pos+=pos
        total_neg+=neg
        details.append({
            "original_anchor":(p,l), "original_3flag_path":path,
            "left_occupied_C4_source_triples":len(left),
            "right_occupied_C4_source_triples":len(right),
            "both_physical_C4_candidate_pairs":pair_count,
            "signed_original_det_plus_one":pos,
            "signed_original_det_minus_one":neg,
            "original_det_zero":zero,
            "exterior3_compressed_squared_Frobenius":pos+neg,
            "historical_original_BBo_sixflag_count":pos+neg,
            "one_original_zero_witness":first_zero
        })
    return {
        "s":s,"V":V,"a":a,
        "true_original_distinct_source_3path_anchors":len(pairs),
        "all_anchored_occupied_physical_C4_pairs":total_candidate,
        "compressed_exterior3_original_squared_energy":total_squared,
        "historical_original_BBo_sixflag_count":total_squared,
        "determinant_abs_sum_check":total_abs,
        "positive_signed_det_count":total_pos,
        "negative_signed_det_count":total_neg,
        "anchor_details":tuple(details),
        "zero_compressed_energy_does_NOT_imply_zero_global_source_energy":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER"
    }
