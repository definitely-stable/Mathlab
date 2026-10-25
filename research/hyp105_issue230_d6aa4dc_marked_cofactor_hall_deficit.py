"""AA4-DC: exact ORIGINAL three-matching marked-C4 cofactor/Hall deficit.

A completed physical C4 point triple and C4 line triple have exactly
TWO source spoke factors on each side, and ONE physical center factor
each. Count only genuine ORIGINAL spoke-to-spoke SOURCE incidence flags.
For each marked flag (i,j), permanent of complementary actual-original
2x2 incidence matrix is 0 or 1 (no source GQ C4).
Every genuine original 3x3 perfect matching uses 1 OR 2 marks.
Thus EXACT T_mark = D_Hall + E_extend, U_BBo <= E_extend <=2 U_BBo,
hence D_Hall+2 U_BBo>=T_mark>=T_AA4DB>=s^7/2^15 for h>=96,
every globally complete correlated typed original maps and every halfcut.

This is a dichotomy, NOT an unqualified positive U_BBo bound:
either U_BBo>=s^7/2^17 OR D_Hall>=s^7/2^16.
The second alternative is an OPEN REAL ORIGINAL incidence obstruction.
Neither an accepted all-seven A/B/C result nor an independent referee.
"""
from collections import Counter
from itertools import combinations
from math import comb

from hyp105_issue230_d6aa4cq_original_macro_path_cut_gate import _validated_original
from hyp105_issue230_d6aa4cr_exact_BBo_three_matching_transfer import (
    c4_completions_from_single_and_doubled,
    exact_three_by_three_incidence_matching,
    original_nonincident_threepath,
)
from hyp105_issue230_d6aa4db_occupied_c4_spoke_flag_mass import (
    allh_original_occupied_c4_arithmetic,
)


def original_three_by_three_cofactor_certificate(rows):
    """Exact 3x3 0/1 matrix, two source physical SPOKES = indices 0,1.

    Row2 and col2 are source C4 CENTER factors. DOES NOT infer SOURCE
    incidence from physical occupancy; caller supplies actual source M.
    """
    B=tuple(tuple(v for v in row) for row in rows)
    if len(B)!=3 or any(len(r)!=3 for r in B) or any(
        type(v) is not int or v not in (0,1) for r in B for v in r
    ):
        raise ValueError("exact genuine 3x3 binary SOURCE incidence rows required")
    # A REAL GQ source 3x3 subgraph has no C4 (girth eight).
    if any(sum(B[i][j]*B[ii][j] for j in range(3))>=2
           for i,ii in combinations(range(3),2)):
        raise ValueError("original GQ source girth8 forbids a 3x3 C4 submatrix")
    def per2(i,j):
        rr=[p for p in range(3) if p!=i]
        cc=[l for l in range(3) if l!=j]
        return B[rr[0]][cc[0]]*B[rr[1]][cc[1]]+B[rr[0]][cc[1]]*B[rr[1]][cc[0]]
    def per3():
        return sum(B[0][a]*B[1][b]*B[2][c]
                   for a,b,c in ((0,1,2),(0,2,1),(1,0,2),(1,2,0),(2,0,1),(2,1,0)))
    permanent=per3()
    if permanent>1:
        raise ValueError("source 3x3 has multiple perfect matchings (not original GQ girth8)")
    for i in range(3):
        for j in range(3):
            if B[i][j] and per2(i,j)>1:
                raise ValueError("source GQ girth8 forbids 2x2 source C4 minor")
    marked=sum(B[i][j] for i in (0,1) for j in (0,1))
    extended=sum(B[i][j]*per2(i,j) for i in (0,1) for j in (0,1))
    deficit=marked-extended
    if deficit<0 or (permanent==1 and not 1<=extended<=2) or (
        permanent==0 and extended!=0
    ):
        raise AssertionError("original source matching marked-cofactor theorem violated")
    hall=None
    if permanent==0:
        for n in (1,2,3):
            for subset in combinations(range(3),n):
                neigh=tuple(j for j in range(3) if any(B[i][j] for i in subset))
                if len(neigh)<n:
                    hall={"original_source_point_row_subset":subset,
                          "original_source_line_neighbor_columns":neigh}
                    break
            if hall:break
        if hall is None:
            raise AssertionError("zero 3x3 permanent missing an actual Hall witness")
    return {
        "true_original_3x3_binary_rows":B,
        "true_original_3x3_permanent":permanent,
        "original_C4_pair_spoke_spoke_marked_flags":marked,
        "true_original_2x2_cofactor_extendible_spoke_flags":extended,
        "original_source_Hall_rejected_spoke_cross_flags":deficit,
        "minimal_true_original_Hall_deficiency":hall,
        "does_NOT_infer_match_from_one_source_spoke_incidence":True,
    }


def exact_original_C4_marked_cofactor_energy(
        model, *, anchor_pairs=None, point_cut=None, line_cut=None,
        max_triples_per_side=None, independent_matching_referee=True):
    """Exact anchor-indexed true-original 3x3 forest/mark energy census.

    Optional max_triples_per_side is an EXPLICIT partial sampling cap;
    no all-C4 or global accepted U equivalence is claimed if set.
    """
    s,V,a,f,g,pl,lp=_validated_original(model)
    inverse_point={tuple(sorted(edge)):i for i,edge in enumerate(f)}
    inverse_line={tuple(sorted(edge)):i for i,edge in enumerate(g)}
    if len(inverse_point)!=V or len(inverse_line)!=V:
        raise AssertionError("complete injective typed original maps required")
    def cut(t):
        if t is None:return None
        t=tuple(t)
        if (len(set(t))!=len(t) or any(type(v) is not int or not 0<=v<a for v in t)):
            raise ValueError("valid original physical coordinate cut with unique ints required")
        return frozenset(t)
    X=cut(point_cut);Y=cut(line_cut)
    if max_triples_per_side is not None and (
        type(max_triples_per_side) is not int or max_triples_per_side<1
    ):
        raise ValueError("positive partial original C4 triple cap required")
    if anchor_pairs is None:
        anchors=tuple((p,l) for p in range(V) for l in range(V)
                      if l not in pl[p] and (X is None or set(f[p])<=X)
                      and (Y is None or set(g[l])<=Y))
    else:
        anchors=tuple(tuple(x) for x in anchor_pairs)
        if len(anchors)!=len(set(anchors)):
            raise ValueError("duplicate genuine original source anchor")
        for p,l in anchors:
            if (type(p) is not int or type(l) is not int
                or not 0<=p<V or not 0<=l<V or l in pl[p]
                or (X is not None and not set(f[p])<=X)
                or (Y is not None and not set(g[l])<=Y)):
                raise ValueError("source anchors must be distinct genuine nonincident and lie in cut")
    counts=Counter()
    classifications=Counter()
    mark_support=set()
    hall_witness=None
    positive_mark_no_source_matching=None
    matched_witness=None
    eligible_anchors=0
    for p,l in anchors:
        path=original_nonincident_threepath(p,l,pl,lp)
        q,l0=path[1][0],path[0][1]
        if set(f[p])&set(f[q]) or set(g[l])&set(g[l0]):
            continue
        eligible_anchors+=1
        P=c4_completions_from_single_and_doubled(f[p],f[q],inverse_point,a)
        L=c4_completions_from_single_and_doubled(g[l],g[l0],inverse_line,a)
        if max_triples_per_side is not None:
            P=P[:max_triples_per_side];L=L[:max_triples_per_side]
        def order_triple(ids,labels,base):
            spokes=[i for i in ids if len(set(labels[i])&set(base))==1]
            center=[i for i in ids if not set(labels[i])&set(base)]
            if len(spokes)!=2 or len(center)!=1:
                raise AssertionError("actual original physical C4 has 2 spokes and 1 center")
            return tuple(sorted(spokes))+tuple(center)
        for ps in P:
            pp=order_triple(ps,f,f[p])
            for ls in L:
                ll=order_triple(ls,g,g[l])
                B=tuple(tuple(int(j in pl[i]) for j in ll) for i in pp)
                c=original_three_by_three_cofactor_certificate(B)
                if independent_matching_referee:
                    match=exact_three_by_three_incidence_matching(pp,ll,pl)
                    if bool(match)!=bool(c["true_original_3x3_permanent"]):
                        raise AssertionError("3x3 TRUE ORIGINAL cofactor and independent canonical matching disagree")
                    matching_spoke_flags=sum(i in pp[:2] and j in ll[:2] for i,j in match)
                    if matching_spoke_flags!=c["true_original_2x2_cofactor_extendible_spoke_flags"]:
                        raise AssertionError("genuine original matched source spoke flags disagreed")
                marked=c["original_C4_pair_spoke_spoke_marked_flags"]
                extension=c["true_original_2x2_cofactor_extendible_spoke_flags"]
                deficit=c["original_source_Hall_rejected_spoke_cross_flags"]
                counts["C4_pair_count"]+=1
                counts["marked_original_spoke_spoke_cross_source_flag_mass"]+=marked
                counts["true_original_complement_2x2_extendible_mark_mass"]+=extension
                counts["original_Hall_defective_marked_source_flag_mass"]+=deficit
                counts["genuine_source_3x3_perfect_matchings"]+=c["true_original_3x3_permanent"]
                if c["true_original_3x3_permanent"]:
                    counts["cofactor_rejected_marks_on_matching_C4_pairs"]+=deficit
                else:
                    counts["cofactor_rejected_marks_on_zero_matching_C4_pairs"]+=marked
                classifications["matching" if c["true_original_3x3_permanent"] else
                                "Hall_no_matching"]+=1
                if c["minimal_true_original_Hall_deficiency"]:
                    n=len(c["minimal_true_original_Hall_deficiency"]["original_source_point_row_subset"])
                    classifications[f"first_row_Hall_defect_subset_{n}"]+=1
                    if hall_witness is None and marked:
                        hall_witness=(p,l,pp,ll,B,c["minimal_true_original_Hall_deficiency"])
                for ri in (0,1):
                    for cj in (0,1):
                        if B[ri][cj]:
                            mark_support.add((p,l,pp[ri],ll[cj]))
                if marked and not c["true_original_3x3_permanent"] and positive_mark_no_source_matching is None:
                    positive_mark_no_source_matching=(p,l,pp,ll,B)
                if c["true_original_3x3_permanent"] and matched_witness is None:
                    matched_witness=(p,l,pp,ll,B)
    T=counts["marked_original_spoke_spoke_cross_source_flag_mass"]
    D=counts["original_Hall_defective_marked_source_flag_mass"]
    E=counts["true_original_complement_2x2_extendible_mark_mass"]
    U=counts["genuine_source_3x3_perfect_matchings"]
    if (D!=counts["cofactor_rejected_marks_on_zero_matching_C4_pairs"]+
            counts["cofactor_rejected_marks_on_matching_C4_pairs"]):
        raise AssertionError("original cofactor-deficit zero/positive C4 decomposition failed")
    if T!=D+E or not U<=E<=2*U:
        raise AssertionError("genuine original ALL anchored C4 marked-deficit identities failed")
    if T<len(mark_support):
        raise AssertionError("genuine marked-source flag physical C4 multiplicity undercounted")
    return {
        "s":s,"V":V,"a":a,
        "source_nonincident_anchors_requested":len(anchors),
        "source_physically_double_disjoint_anchors":eligible_anchors,
        "C4_pairs_examined":counts["C4_pair_count"],
        "source_occupied_C4_source_cross_flag_mark_mass_T":T,
        "source_2x2_cofactor_extendible_flag_mass_E":E,
        "source_Hall_defective_C4_spoke_flag_mass_D":D,
        "source_cofactor_rejected_marks_on_zero_matching_pairs":
            counts["cofactor_rejected_marks_on_zero_matching_C4_pairs"],
        "source_cofactor_rejected_marks_on_matching_pairs":
            counts["cofactor_rejected_marks_on_matching_C4_pairs"],
        "source_original_3x3_perfect_matching_BBo_U":U,
        "distinct_original_spoke_cross_source_flags_with_two_actual_C4_witnesses":len(mark_support),
        "source_true_Hall_failure_class_counts":dict(classifications),
        "first_actual_original_marked_C4_Hall_failure":hall_witness,
        "first_actual_original_spoke_flag_no_3matching":positive_mark_no_source_matching,
        "first_actual_original_3x3_matching":matched_witness,
        "mathematical_exact_identity_T_equals_D_plus_E":True,
        "mathematical_exact_original_BBo_le_E_le_2BBo":True,
        "PR_scope_partial_source_C4_sampling":max_triples_per_side is not None,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


def allh_original_marked_cofactor_dichotomy_arithmetic(h):
    """Transfer DB universal positive C4-mass into EXACT scoped dichotomy."""
    z=allh_original_occupied_c4_arithmetic(h)
    s,V,a,k=(z[x] for x in ("s","V","a","k"))
    if h>=96 and not (z["allh_gate_h_ge_96"] and
                     z["allh_both_occupied_c4_original_flag_mass_lower_denominator"]==(1<<15)):
        raise AssertionError("source parent original occupied-C4 theorem not accepted as prerequisite")
    return {
        "h":h,"s":s,"V":V,"a":a,"k":k,
        "original_minimum_marked_source_flag_mass_numerator":s**7,
        "original_minimum_marked_source_flag_mass_denominator":1<<15,
        "either_true_original_BBo_U_lower_numerator":s**7,
        "either_true_original_BBo_U_lower_denominator":1<<17,
        "or_original_marked_Hall_deficit_D_lower_numerator":s**7,
        "or_original_marked_Hall_deficit_D_lower_denominator":1<<16,
        "uniform_positive_BBo_not_proven":True,
        "uniform_positive_sevenclass_S_not_proven":True,
        "allh_gate_h_ge_96":h>=96,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }
