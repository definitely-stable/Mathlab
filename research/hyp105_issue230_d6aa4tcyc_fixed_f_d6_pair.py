"""HYP-105 #230 / D6-AA4-T-CYC: conditional TWO genuine D6 kernel for fixed f.

For ANY genuine original W(3,s), full typed physical globally injected
f is held FIXED, and ONE uniformly random complete original-line
physical injection g is SHARED by all original six-incidence Q.

For two distinct actual ORIGINAL six-incidence Q0,Q1 with:
  - six different original points & six different original lines each;
  - physical-left connected 6-cycle on six ORIGINAL column positions;
  - DISJOINT sets of ORIGINAL LINE factors across Q0 and Q1;
  - original POINT factors are permitted to overlap (new vs
    source-disjoint both-map JPKC-016);

P_g(D6(Q0) and D6(Q1) | fixed f)
  = [(a)_6/(K)_6] * [12*H_a/(K-6)_6],
H_a = #undirected physical C6 avoiding all six edges of any fixed C6.

The SECOND probability is NOT the marginal p_D6 and is NOT independent,
because g is a GLOBAL without-replacement injection; relative
covariance may be positive or negative depending on a.

Exact 64-subset inclusion-exclusion for H_a and independently
enumerated ORIGINAL W32 anchored right-line-overlap rows + genuine
complete physical right map realizing TWO D6 positive original Q.

This is an exact pair kernel and a computable, strictly PARTIAL
conditional second-moment sector, NOT a full variance/lower tail or
universal all-f,g positive S lower.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations,permutations,product
from math import comb,factorial,perm

from hyp105_issue230_d6aa4r_quenched_original_d6 import (
    _params,_physical_six_cycle)
from hyp105_issue230_projection import fixture


def physical_C6_complement_inclusion_exclusion(a):
    """Exact H_a via ALL 64 subsets of a fixed six-physical-edge C6.

    For 0<k<6 selected F edges, their components are c disjoint
    nonempty paths covering v=k+c fixed physical vertices. Contract
    the paths: 6-k cyclic units. Number of undirected six-cycles in
    K_a containing all selected k prescribed edges is
      2^(c-1)*(5-k)!*C(a-k-c,6-k-c).
    For all six selected edges the only cycle is F itself (one).
    Empty subset count (a)_6/12.
    """
    if type(a) is not int or a<6:
        raise ValueError("at least six physical coordinate symbols required")
    total=perm(a,6)//12
    banned=tuple((i,(i+1)%6) for i in range(6))
    if len(banned)!=6:
        raise AssertionError("fixed edge template not a physical C6")
    signs=Counter()
    H=0
    for mask in range(64):
        k=mask.bit_count()
        if k==0:
            ways=total
        elif k==6:
            ways=1
        else:
            c=sum(bool(mask&(1<<i)) and not bool(mask&(1<<((i-1)%6)))
                  for i in range(6))
            if not 1<=c<=3:
                raise AssertionError("fixed C6 selected path component count wrong")
            v=k+c
            if v>6 or a<v:
                ways=0
            else:
                ways=(1<<(c-1))*factorial(5-k)*comb(a-v,6-v)
        H+=(-1 if k%2 else 1)*ways
        signs[k]+=ways
    if H<0 or H>total:
        raise AssertionError("valid physical C6 complement count outside range")
    return {
        "a":a,
        "all_physical_Ka_undirected_C6":total,
        "fixed_forbidden_physical_edge_cycle_length":6,
        "number_of_exact_64_inclusion_exclusion_subsets":64,
        "physical_Ka_C6_avoiding_fixed_C6_H":H,
        "included_subsets_by_cardinality_weighted_sums":dict(sorted(signs.items())),
        "original_source_geometry_NOT_assumed_by_physical_kernel":True,
    }


def exact_one_sided_fixed_f_disjoint_LINE_D6_kernel(s):
    """ALL-h honest conditional covariance, original POINT overlap allowed."""
    V,a,K,m=_params(s)
    x=physical_C6_complement_inclusion_exclusion(a)
    if K<12:
        raise AssertionError("need two disjoint six-line source supports")
    p=Fraction(perm(a,6),perm(K,6))
    cond=Fraction(12*x["physical_Ka_C6_avoiding_fixed_C6_H"],perm(K-6,6))
    joint=p*cond
    covariance=joint-p*p
    return {
        "s":s,"V":V,"a":a,"K":K,"physical_missing_original_factor_pair_labels":m,
        "physical_C6_complement_count_H":x["physical_Ka_C6_avoiding_fixed_C6_H"],
        "exact_single_Q_D6_probability_fixed_f_uniform_complete_g":str(p),
        "exact_second_Q_D6_given_first_AND_disjoint_original_line_factors":str(cond),
        "exact_two_Q_D6_joint_probability_disjoint_original_LINE_factors":str(joint),
        "exact_conditional_covariance":str(covariance),
        "joint_over_independent_product":str(joint/(p*p)),
        "covariance_sign":"positive" if covariance>0 else "negative" if covariance<0 else "zero",
        "true_original_POINT_factors_between_Q_may_overlap":True,
        "both_Q_original_six_column_duals_must_be_CONNECTED_C6":True,
        "one_GLOBAL_complete_g_for_both_original_Q":True,
        "full_conditional_variance_PROVED":False,
        "all_h_root_minimax_seven_positive_PROVED":False,
    }


# Polynomial governing the sign of exact conditional right-injection
# two-D6 covariance. From the 64-term physical H_a inclusion-exclusion,
# with K=a(a-1)/2, q=12H_a/(K-6)_6, p=(a)_6/(K)_6,
#
# q-p = 768*P(a) / [(a-5)(a-4)(a+1)(a+2)(a+3)(a+4)
#                  *product(a*a-a-j for j in (22,18,16,14,10,8,4))].
#
# The denominator is positive for a>=6. P(a) has a manifestly positive
# coefficient expansion about a=12. For actual minimal ORIGINAL GQ
# physical alphabets a=6 for s=2, and a>=14 for every s>=4. Thus the
# fixed-f right-source-disjoint ORIGINAL two-D6 covariance is strictly
# POSITIVE for EVERY s=2^h>=2. For synthetic a=8/9 it is NEGATIVE, so
# this is not a generic physical-alphabet universal sign law.
_SHIFTED_P_AT_12_DESC=(
    6,618,28242,754027,13029162,152397500,1224585146,
    6705318203,24194129492,53456486932,61643554832,23663646720,
)
_P_COEFF_DESC=(
    6,-174,1602,-2189,-42102,157748,403706,-2294941,
    -1674364,14501476,2327792,-35537280,
)


def _integer_horner(coefficients,n):
    value=0
    for coefficient in coefficients:
        value=value*n+coefficient
    return value


def certified_all_original_orders_fixed_f_disjoint_LINE_D6_positive_covariance(s):
    """ALL genuine original GQ powers, *rigorous* positive covariance.

    Denominator sign, polynomial algebra, and positive shifted
    coefficients verified in exact integer/rational arithmetic.
    For s>=4 minimal a>=14. For s=2 minimal a=6 and P(6)>0.
    """
    original=exact_one_sided_fixed_f_disjoint_LINE_D6_kernel(s)
    a=original["a"]
    P=_integer_horner(_P_COEFF_DESC,a)
    shifted=_integer_horner(_SHIFTED_P_AT_12_DESC,a-12)
    if shifted!=P:
        raise AssertionError("exact shifted covariance sign polynomial mismatch")
    factors=(a-5,a-4,a+1,a+2,a+3,a+4)
    denominator=1
    for q in factors:
        denominator*=q
    for j in (22,18,16,14,10,8,4):
        denominator*=a*a-a-j
    if denominator<=0:
        raise AssertionError("covariance difference denominator must be positive")
    algebraic_difference=Fraction(768*P,denominator)
    k=original["K"]
    h=original["physical_C6_complement_count_H"]
    direct_difference=Fraction(12*h,perm(k-6,6))-Fraction(perm(a,6),perm(k,6))
    if algebraic_difference!=direct_difference:
        raise AssertionError("64-term C6 IE does not match polynomial covariance identity")
    if a>=12:
        if not (all(c>0 for c in _SHIFTED_P_AT_12_DESC) and a-12>=0):
            raise AssertionError("shifted positive coefficient proof cannot be applied")
    elif a!=6:
        raise AssertionError("unexpected ORIGINAL GQ minimal physical alphabet below 12")
    if P<=0 or algebraic_difference<=0:
        raise AssertionError("genuine original s=2^h conditional D6 covariance positivity proof failed")
    return {
        "s":s,"a":a,
        "exact_P_a_integer":P,
        "P_a_shifted_at_12_all_coefficients_strictly_positive":True,
        "exact_q_minus_p_rational":str(algebraic_difference),
        "exact_joint_minus_independent_product_covariance":
            original["exact_conditional_covariance"],
        "for_every_genuine_s_2power_original_minimal_a_positive_covariance_PROVED":True,
        "synthetic_a_8_or_9_negative_covariance_DOES_NOT_CONTRADICT_original_GQ":True,
        "all_h_full_conditional_variance_PROVED":False,
        "not_all_maps_seven_S_lower":True,
    }


def brute_physical_Ka_cycle_complement(a):
    """Oracle independent of 64-subset IE; use only a=6..9."""
    if type(a) is not int or a<6 or a>9:
        raise ValueError("physical graph brute exact verification only a=6..9")
    F={tuple(sorted((i,(i+1)%6))) for i in range(6)}
    total=avoiding=0
    for vs in combinations(range(a),6):
        root=vs[0]
        for rest in permutations(vs[1:]):
            if rest[0]>rest[-1]:
                continue
            cyclic=(root,)+rest
            edges={tuple(sorted((cyclic[i],cyclic[(i+1)%6])))
                   for i in range(6)}
            if len(edges)!=6:
                raise AssertionError("invalid physical simple C6")
            total+=1
            if not (F&edges):
                avoiding+=1
    target=physical_C6_complement_inclusion_exclusion(a)
    if (target["all_physical_Ka_undirected_C6"],
        target["physical_Ka_C6_avoiding_fixed_C6_H"])!=(total,avoiding):
        raise AssertionError("independent physical C6 complement brute disagrees")
    return {"a":a,"brute_physical_C6_total":total,
            "brute_disjoint_from_fixed_C6":avoiding,
            "independent_64_subset_inclusion_exclusion":"PASS"}


def genuine_W32_fixed_f_original_connected_left_Q(scheme):
    """All true original 45-incidence six-ID Q with left COLUMN C6 and
    six source point factors and six source line factors DISTINCT.
    Reconstruct using physical connected C6 and ACTUAL source incidences.
    """
    model=fixture(1,scheme)
    f=tuple(tuple(e) for e in model["left_labels"])
    original=tuple(tuple(x) for x in model["incidences"])
    edges=tuple(combinations(range(6),2))
    if model["s"]!=2 or len(original)!=45 or len(set(original))!=45:
        raise AssertionError("real W32 original 45-incidence source required")
    if len(f)!=15 or set(f)!=set(edges):
        raise AssertionError("complete original source point K6 edge injection required")
    inverse={edge:i for i,edge in enumerate(f)}
    bypoint=[[] for _ in range(15)]
    for i,(p,l) in enumerate(original):
        bypoint[p].append((i,l))
    cycles=tuple(six for six in combinations(edges,6) if _physical_six_cycle(six))
    if len(cycles)!=60:
        raise AssertionError("physical K6 connected sixcycles not exactly60")
    rows={}
    for six in cycles:
        ps=tuple(inverse[e] for e in six)
        for flags in product(*(bypoint[p] for p in ps)):
            ls=tuple(l for i,l in flags)
            if len(set(ls))!=6:
                continue
            Q=tuple(sorted(i for i,l in flags))
            if Q in rows:
                raise AssertionError("same true ORIGINAL six-ID Q double counted")
            line_mask=sum(1<<l for l in ls)
            point_mask=sum(1<<p for p in ps)
            rows[Q]=(point_mask,line_mask)
    if len(rows)!=21186:
        raise AssertionError("true W32 fixture left-connected C6 original AA count drift")
    return model,rows


def genuine_W32_fixed_f_anchored_line_overlap(scheme):
    """One complete-original anchored row, NOT all Q×Q pair histogram."""
    model,rows=genuine_W32_fixed_f_original_connected_left_Q(scheme)
    anchor=next(iter(rows))
    p0,l0=rows[anchor]
    histogram=Counter()
    disjoint=point_shared_but_line_disjoint=0
    other=None
    for Q,(p,l) in rows.items():
        r=(l&l0).bit_count()
        histogram[r]+=1
        if r==0:
            disjoint+=1
            if (p&p0) and other is None:
                other=Q
                point_shared_but_line_disjoint+=1
    if sum(histogram.values())!=len(rows) or disjoint!=histogram[0]:
        raise AssertionError("actual original left C6 right-source line overlap count failed")
    if other is None:
        raise AssertionError("no actual W32 two-C6 Q with disjoint original lines and overlapping point factors")
    kernel=exact_one_sided_fixed_f_disjoint_LINE_D6_kernel(2)
    joint=Fraction(kernel["exact_two_Q_D6_joint_probability_disjoint_original_LINE_factors"])
    return {
        "scheme":scheme,
        "true_original_W32_left_C6_six_incidence_Q_count":len(rows),
        "anchor_TRUE_original_six_incidence_IDs":anchor,
        "anchor_original_line_support_overlap_histogram":dict(sorted(histogram.items())),
        "actual_other_TRUE_original_six_incidence_IDs":other,
        "anchor_and_other_LINE_factors_disjoint":True,
        "anchor_and_other_POINT_factors_overlap":True,
        "number_of_LINE_disjoint_Q_in_one_anchored_row":disjoint,
        "exact_frozen_f_first_second_D6_probability":str(joint),
        "anchored_row_DISJOINT_sector_partial_E_D6_squared_contribution":str(disjoint*joint),
        "anchored_row_is_NOT_full_conditional_variance":True,
        "one_fixed_complete_global_f":True,
        "root_A":"OPEN","root_B":"OPEN",
    }


def independent_real_W32_two_Q_one_complete_g(scheme):
    """Find TWO actual original left C6 source Q with disjoint line
    factors and shared original points, then realize BOTH positive D6
    at once using ONE globally injected right g; historical verifier.
    """
    from hyp105_g5e2b3e1b0_seven_signature import (
        classify_seven_prechecked,physical_column_dual)
    model,rows=genuine_W32_fixed_f_original_connected_left_Q(scheme)
    z=genuine_W32_fixed_f_anchored_line_overlap(scheme)
    A=z["anchor_TRUE_original_six_incidence_IDs"]
    B=z["actual_other_TRUE_original_six_incidence_IDs"]
    inc=tuple(tuple(q) for q in model["incidences"])
    f=tuple(tuple(q) for q in model["left_labels"])
    all_edges=tuple(combinations(range(6),2))
    def align(Q):
        # The left-dual graph is on Q-column POSITION IDs 0..5; its six
        # edges correspond to physical left coordinate incidences.
        dual=physical_column_dual(inc,f,tuple(inc[j][0] for j in Q))
        ls=tuple(inc[j][1] for j in Q)
        if dual is None or len(dual)!=6 or len(set(ls))!=6:
            raise AssertionError("not a genuine ORIGINAL left connected C6 AA Q")
        choices=[]
        for color in permutations(range(6)):
            image=[[] for _ in range(6)]
            for c,(u,v) in zip(color,dual):
                image[u].append(c)
                image[v].append(c)
            out=tuple(tuple(sorted(row)) for row in image)
            if any(len(q)!=2 for q in out) or len(set(out))!=6:
                raise AssertionError("not genuine D6 physical right injection")
            choices.append((ls,out))
        if len(choices)!=720:
            raise AssertionError("not 720 globally completable right alignments")
        return choices
    first=align(A)[0]
    F=set(first[1])
    second=next((x for x in align(B) if not (F&set(x[1]))),None)
    if second is None:
        raise AssertionError("no physically edge-disjoint second C6 completing first actual original Q")
    right=[None]*15
    for l,e in (list(zip(first[0],first[1]))+
                list(zip(second[0],second[1]))):
        if right[l] is not None and right[l]!=e:
            raise AssertionError("two original line supports should be disjoint")
        right[l]=e
    leftover=iter(e for e in all_edges if e not in set(e for e in right if e is not None))
    for l in range(15):
        if right[l] is None:
            right[l]=next(leftover)
    g=tuple(right)
    if set(g)!=set(all_edges) or len(set(g))!=15:
        raise AssertionError("TWO true D6 Q not simultaneously globally extendable")
    tags=(classify_seven_prechecked(A,f,g,inc),
          classify_seven_prechecked(B,f,g,inc))
    if tags!=("D6","D6"):
        raise AssertionError("historical GF5 classifier rejects genuine simultaneous original two-D6")
    targetF=set(first[1])
    check=0
    for llabels in align(B):
        if not (targetF&set(llabels[1])):
            check+=1
    if check!=36:
        raise AssertionError("conditional physical K6 aligned D6 right images avoiding fixed 6-cycle !=36")
    return {
        "scheme":scheme,
        "real_original_Q0":A,"real_original_Q1":B,
        "real_original_point_supports_overlap":True,
        "real_original_LINE_supports_are_disjoint":True,
        "same_global_complete_right_physical_edge_labels":g,
        "historical_original_seven_GF5_tags":tags,
        "number_second_right_alignment_tuples_without_first_six_edges":check,
        "conditional_probability_second_D6_given_first_and_disjoint_lines":"1/1680",
        "one_COMPLETE_right_mapping_accepts_BOTH_true_original_D6_Q":True,
        "not_every_original_Q_simultaneously_accepted":True,
    }


def report(scheme=None):
    data={
        "slice":"HYP105-ISSUE230-D6-AA4-T-CYC-FIXED-F-D6-PAIR-KERNEL",
        "all_h_exact_fixed_point_map_disjoint_original_LINE_D6_pair_kernel":True,
        "independent_real_physical_64_IE_checks":
            [brute_physical_Ka_cycle_complement(a) for a in (6,7,8,9)],
        "all_h_fixed_side_one_global_g_kernel_rows":
            [exact_one_sided_fixed_f_disjoint_LINE_D6_kernel(1<<h)
             for h in range(1,12)],
        "full_conditional_second_moment_and_variance_PROVED":False,
        "universal_all_labels_S_omega_s6_PROVED":False,
        "root_A":"OPEN","root_B":"OPEN",
    }
    if scheme:
        data["true_original_W32_anchored_source_line_overlap"]=genuine_W32_fixed_f_anchored_line_overlap(scheme)
        data["true_original_W32_simultaneous_two_D6_global_completion"]=independent_real_W32_two_Q_one_complete_g(scheme)
    return data


if __name__=="__main__":
    import json,argparse
    p=argparse.ArgumentParser()
    p.add_argument("--scheme",choices=("S68","S72"))
    args=p.parse_args()
    print(json.dumps(report(args.scheme),indent=2,sort_keys=True))
