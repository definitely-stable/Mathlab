"""HYP-105 #230 AA4-SYMMOM: exact ALL-h ORIGINAL M/G/B symbol moments.

Main theorem: for ANY true ORIGINAL symplectic W(3,2^h) retained paired
source, separately globally pair-injective fixed f/g (arbitrarily
correlated), and true positive proper physical P3 selector marginal
weights, the ENTIRE compatible and incompatible weighted endpoint P3
pair tensors can be computed by O(number-of-paths + source IDs) sparse
second moments. No pairwise P3-pair J inspection and no pairwise middle
flag traversal is used in this NEW algorithm.

The all-h original proof is in
 docs/research/HYP-105-AA4-ORIGINAL-SYMBOL-SECOND-MOMENTS.md

A separate all-order minimal alphabet original source flag-pair
potential-overlap degree O(s^(5/2)) vs total source flags Θ(s^4) is
proved. This UNWEIGHTED source sparsity does not by itself imply
a uniform bound on weighted same-physical-endpoint B/M.

Scientific root status OPEN_WITH_FORMAL_BLOCKER. No all-h global
B/M<3/4, no full Branch A proof or GF5 ASET exponent promoted.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb, isqrt
import json

from hyp105_original_full_w34_weighted_risk_referee import (
    _source, _true_original_proper_P3, _rank_probability3
)

SCHEMA="mathlab.hyp105.original-middle-symbol-squared-moments.v1"
ROOT_STATUS="OPEN_WITH_FORMAL_BLOCKER"
CASES=(
    (2,"lex","full"),(2,"reverse","full"),(2,"shift","Z17"),
    (4,"lex","full"),(4,"reverse","full"),(4,"shift","full"),
    (4,"lex","even"),(4,"shift","Z17")
)
THRESHOLD=Fraction(3,4)


def _sum_square(d):
    return sum((x*x for x in d.values()),Fraction(0))


def _minimal_pair_alphabet(V):
    if type(V)!=int or V<1:
        raise ValueError("source positive point/line count integer required")
    a=max(2,(1+isqrt(1+8*V))//2)
    while comb(a,2)<V:
        a+=1
    if a>2 and comb(a-1,2)>=V:
        raise AssertionError("original minimal pair alphabet not minimal")
    return a


def _potential_original_middle_label_overlap_degree_bound(s,a):
    """UNWEIGHTED capacity: all h and separately pair-injective f/g.

    Given a source flag i=(p,l), each x-pair f(p) intersects at most
    2(a-2) DISTINCT x-pair labels from other ORIGINAL source points.
    Including p itself, at most 2a-3 original point labels. Each has
    s+1 incident ORIGINAL flags. One self-flag is excluded. Ditto
    on the line side; union bound on neighbors in the potential
    f/g-middle-symbol-overlap graph gives <=
    2 * ((2a-3)*(s+1)-1).
    """
    if type(s)!=int or s<2 or type(a)!=int or a<2:
        raise ValueError("true source order and alphabet required")
    V=(s+1)*(s*s+1)
    if comb(a,2)<V:
        raise ValueError("pair-injective f/g not feasible at this alphabet")
    I=(s+1)*V
    raw=2*((2*a-3)*(s+1)-1)
    return {
        "s":s,"original_points_and_lines_each":V,"original_flags":I,
        "minimal_pair_alphabet":_minimal_pair_alphabet(V),
        "actual_alphabet":a,
        "unweighted_source_middle_pair_overlap_max_degree_cap":min(I-1,raw),
        "raw_union_degree_cap":raw,
        "fraction_bound_for_distinct_original_flag_pairs":
            str(Fraction(min(I-1,raw),I-1)),
        "absolute_cap_derived_only_from_separate_global_pair_injection":True,
        "all_h_asymptotic_finite_source_degree_over_flags_O_s_minus_three_halves_if_minimal_alphabet":a==_minimal_pair_alphabet(V),
        "this_does_NOT_control_same_endpoint_weighted_B_over_M":True,
    }


def _observed_full_original_flag_label_overlap_degree(c):
    """Independent FULL original flag-label-pair capacity census (O(|I|²))."""
    I=c["ids"]
    f=c["f"];g=c["g"];flags=c["flags"]
    deg={i:0 for i in I}
    typed_overlap_pairs=0
    two_overlap_pairs=0
    same_original_pencil_pairs=0
    for i,j in combinations(I,2):
        p,l=flags[i];q,m=flags[j]
        ox=bool(set(f[p])&set(f[q]))
        oy=bool(set(g[l])&set(g[m]))
        if ox or oy:
            deg[i]+=1;deg[j]+=1
            typed_overlap_pairs+=1
            if ox and oy:
                two_overlap_pairs+=1
            if p==q or l==m:
                same_original_pencil_pairs+=1
    if c["a"]!=_minimal_pair_alphabet(c["V"]):
        raise AssertionError("full ORIGINAL source fixture must use MINIMAL alphabet")
    envelope=_potential_original_middle_label_overlap_degree_bound(c["s"],c["a"])
    maxdeg=max(deg.values(),default=0)
    if maxdeg>envelope["unweighted_source_middle_pair_overlap_max_degree_cap"]:
        raise AssertionError("original global pair-injective degree capacity false")
    if 2*typed_overlap_pairs!=sum(deg.values()):
        raise AssertionError("unweighted source label-overlap pair degree handshake false")
    return {
        "original_source_flags_in_CORE":len(I),
        "exact_unweighted_original_middle_label_pair_overlap_pairs":typed_overlap_pairs,
        "exact_unweighted_original_middle_both_typed_pair_overlap_pairs":two_overlap_pairs,
        "exact_unweighted_original_source_same_point_or_line_pairs":same_original_pencil_pairs,
        "max_original_middle_label_overlap_degree_in_CORE":maxdeg,
        "full_source_alphabet_minimal_capacity_envelope":envelope,
        "all_original_flag_pair_overlaps_scanned_without_endpoint_condition":True,
    }


def _full_exact_symbol_moments_one_bin(group,c):
    """ALL-h exact TRUE ORIGINAL P3 source-compatible mass, O(paths + owners).

    Important: only source-middle owner ID, ORIGINAL f/g pair labels, first
    and last inner physical corners, and independently exact p_gamma are
    consulted. NO source J graph and NO pairs of paths or middle flags are
    enumerated. Thus this is a structurally independent referee for the
    physical pairwise J/collision census in inherited #759.
    """
    if not group:
        raise ValueError("positive-size physical endpoint family required")
    flags=c["flags"];f=c["f"];g=c["g"]
    W=Fraction(0);D=Fraction(0)
    middle=defaultdict(Fraction)
    tail=defaultdict(Fraction);head=defaultdict(Fraction)
    tail_p=defaultdict(Fraction);tail_l=defaultdict(Fraction)
    head_p=defaultdict(Fraction);head_l=defaultdict(Fraction)
    tail_i=defaultdict(Fraction);head_i=defaultdict(Fraction)
    for path,owners,w in group:
        if len(path)!=4 or len(owners)!=3 or w<=0 or not isinstance(w,Fraction):
            raise AssertionError("not genuine positive original three-owner path marginal")
        i=owners[1]
        p,l=flags[i]
        a,b=path[1],path[2]
        if tuple(sorted((a[0],b[0])))!=f[p] or tuple(sorted((a[1],b[1])))!=g[l]:
            raise AssertionError("original middle physical diagonal source pair inversion failed")
        W+=w;D+=w*w
        middle[i]+=w
        tail[a]+=w;head[b]+=w
        tail_p[(p,a)]+=w;tail_l[(l,a)]+=w;tail_i[(i,a)]+=w
        head_p[(p,b)]+=w;head_l[(l,b)]+=w;head_i[(i,b)]+=w
    # Original named flag i weight is the sum across its <=3 true physical
    # oriented middle edges per fixed real endpoints, not their independent
    # event probability. Exact paths may have unequal marginal weights.
    point=defaultdict(Fraction);line=defaultdict(Fraction)
    X=defaultdict(Fraction);Y=defaultdict(Fraction)
    XY=defaultdict(Fraction);PY=defaultdict(Fraction);LX=defaultdict(Fraction)
    for i,w in middle.items():
        p,l=flags[i]
        point[p]+=w;line[l]+=w
        for x in f[p]:
            X[x]+=w
            LX[(l,x)]+=w
        for y in g[l]:
            Y[y]+=w
            PY[(p,y)]+=w
        for x in f[p]:
            for y in g[l]:
                XY[(x,y)]+=w
    if sum(X.values(),Fraction(0))!=2*W or sum(Y.values(),Fraction(0))!=2*W:
        raise AssertionError("each real original middle point/line pair owns exactly two symbols")
    if sum(XY.values(),Fraction(0))!=4*W:
        raise AssertionError("each original middle flag owns four physical rectangle corners")
    if sum(point.values(),Fraction(0))!=W or sum(line.values(),Fraction(0))!=W:
        raise AssertionError("source first/second moment marginal conservation false")

    # For two different f-pair labels the intersection size is 0 or 1;
    # for same ORIGINAL point, size 2. Thus 1[nonempty intersection]
    # = number-of-shared-symbols - 1[same ORIGINAL point].
    Ox=_sum_square(X)-_sum_square(point)
    Oy=_sum_square(Y)-_sum_square(line)
    Q=_sum_square(middle)
    Oxy=(_sum_square(XY)-_sum_square(PY)-_sum_square(LX)+Q)
    M=W*W
    # Ordered quadratic source-middle flag weights with NO overlaps on
    # x AND y. There are NO self-flag terms because f(i),g(i) each
    # overlap itself. Requires ONLY moment squares, no pairwise checks.
    G00=M-Ox-Oy+Oxy
    # Actual source incompatible "same p" or "same l" first/last corner
    # duplicates are removed by exact inclusion-exclusion; the matching
    # (p,l) original flag is added back as double-subtracted, leaving
    # EXACT ordered weight of distinct-middle-point-and-line pairs
    # with common first/last inner physical corner.
    G11_tail=(_sum_square(tail)-_sum_square(tail_p)-
              _sum_square(tail_l)+_sum_square(tail_i))
    G11_head=(_sum_square(head)-_sum_square(head_p)-
              _sum_square(head_l)+_sum_square(head_i))
    G11=G11_tail+G11_head
    G=D+G00+G11
    B=M-G
    if not all(z>=0 for z in (Ox,Oy,Oxy,G00,G11_tail,G11_head,G11,B)):
        raise AssertionError("negative exact true ORIGINAL label overlap/source good second moment")
    if not (D>0 and D<=G<=M and G00+G11<=M-D):
        raise AssertionError("full ORIGINAL good/bad moment energy nonconservation")
    if Oxy>Ox or Oxy>Oy:
        raise AssertionError("two-typed original label overlap exceeds one-typed source overlap")
    if B < 0 or G+B!=M:
        raise AssertionError("full source M/G/B moments do not conserve")
    if G != D+M-Ox-Oy+Oxy+G11:
        raise AssertionError("original exact second moment kernel algebra failed")
    maxX=max(X.values());maxY=max(Y.values())
    cap_sum=(maxX+maxY)/W
    # Σ_x X_x² <= (max_x X_x) Σ_x X_x = 2W*maxX,
    # similarly Y. All α/β overlap weights are nonnegative.
    symbol_bound=D+M-2*W*(maxX+maxY)
    if G<symbol_bound:
        raise AssertionError("genuine original max-symbol concentration lower G bound failed")
    threshold=Fraction(3,8)+D/(2*M)
    if B/M>THRESHOLD and not cap_sum>threshold:
        raise AssertionError("strict local B/M>3/4 lacks necessary original heavy symbol")
    if cap_sum<threshold and not G>M/4:
        raise AssertionError("source heavy-symbol strict-safe sufficient condition violated")
    strict_safe_diagonal=D>M/4
    strict_safe_diagonal_plus_nooverlap=D+G00>M/4
    strict_safe_exact_G=G>M/4
    if strict_safe_diagonal and not strict_safe_diagonal_plus_nooverlap:
        raise AssertionError("original monotone positive G00 cannot lose diagonal safe case")
    if strict_safe_diagonal_plus_nooverlap and not strict_safe_exact_G:
        raise AssertionError("original monotone positive G11 cannot lose prior safe case")
    if G<M/4 and (strict_safe_diagonal or strict_safe_diagonal_plus_nooverlap or strict_safe_exact_G):
        raise AssertionError("strict local bad source incorrectly certified safe by actual positive moments")
    return {
        "M":M,"G":G,"B":B,"D":D,
        "Ox":Ox,"Oy":Oy,"Oxy":Oxy,
        "G00":G00,"G11_tail":G11_tail,"G11_head":G11_head,
        "G11":G11,"W":W,
        "max_x_symbol_middle_weight":maxX,"max_y_symbol_middle_weight":maxY,
        "sum_relative_largest_x_and_y_symbol_weight":cap_sum,
        "strict_local_B75_safe_from_original_diagonal_only":
            strict_safe_diagonal,
        "strict_local_B75_safe_from_original_diagonal_plus_nooverlap_00":
            strict_safe_diagonal_plus_nooverlap,
        "strict_local_B75_safe_from_FULL_exact_original_symbol_moments":
            strict_safe_exact_G,
        "source_local_bad_requires_heavy_symbol_fraction":
            cap_sum>=threshold,
        "source_strict_safe_from_symbol_stars":cap_sum<threshold,
        "source_B_over_M_strict_three_quarters_exceeded":B/M>THRESHOLD,
        "source_G_symbol_max_mass_lower_bound":symbol_bound,
        "source_original_midflag_count":len(middle),
        "number_distinct_f_source_points":len(point),
        "number_distinct_g_source_lines":len(line),
        "active_x_symbols":len(X),"active_y_symbols":len(Y),
        "true_original_real_middle_owner_group_quadratic":Q,
        "true_source_moment_signature_count":
            sum(map(len,(point,line,X,Y,XY,PY,LX,tail,head,
                         tail_p,tail_l,tail_i,head_p,head_l,head_i))),
    }


def _full_moment_case(s,scheme,core):
    c=_source(s,scheme,core)
    rank={}
    bins=defaultdict(list)
    for path,owners in _true_original_proper_P3(c):
        key=tuple(sorted(owners))
        if key not in rank:
            rank[key]=_rank_probability3(key,c["J"])/64
        bins[(path[0],path[-1])].append((path,owners,rank[key]))
    if not bins:
        raise AssertionError("empty original true-source physical P3 population")
    sums=defaultdict(Fraction)
    counts=defaultdict(int)
    M_heavy=Fraction(0);M_actualbad=Fraction(0)
    M_strictsafe=Fraction(0)
    M_safe_diag=Fraction(0)
    M_safe_diag00=Fraction(0)
    M_safe_all=Fraction(0)
    worst=None
    for ends,group in bins.items():
        t=_full_exact_symbol_moments_one_bin(group,c)
        for k in ("M","G","B","D","Ox","Oy","Oxy",
                  "G00","G11_tail","G11_head","G11","W",
                  "source_G_symbol_max_mass_lower_bound"):
            sums[k]+=t[k]
        counts["number_nonempty_original_endpoint_bins"]+=1
        counts["total_full_original_coordinate_proper_P3_paths"]+=len(group)
        counts["original_middle_source_symbol_sparse_second_moment_terms"]+=t["true_source_moment_signature_count"]
        counts["max_true_original_middle_flags_per_endpoint_bin"]=max(
            counts["max_true_original_middle_flags_per_endpoint_bin"],
            t["source_original_midflag_count"])
        if t["strict_local_B75_safe_from_original_diagonal_only"]:
            M_safe_diag+=t["M"]
            counts["strictly_safe_endpoint_bins_from_diagonal_D_only"]+=1
        if t["strict_local_B75_safe_from_original_diagonal_plus_nooverlap_00"]:
            M_safe_diag00+=t["M"]
            counts["strictly_safe_endpoint_bins_from_D_plus_G00"]+=1
        if t["strict_local_B75_safe_from_FULL_exact_original_symbol_moments"]:
            M_safe_all+=t["M"]
            counts["strictly_safe_endpoint_bins_from_complete_exact_G"]+=1
        if t["source_local_bad_requires_heavy_symbol_fraction"]:
            M_heavy+=t["M"]
            counts["heavy_symbol_candidate_endpoint_bins"]+=1
        if t["source_strict_safe_from_symbol_stars"]:
            M_strictsafe+=t["M"]
            counts["strictly_safe_endpoint_bins_proven_without_J_or_path_pairs"]+=1
        if t["source_B_over_M_strict_three_quarters_exceeded"]:
            M_actualbad+=t["M"]
            counts["actual_LOCAL_source_bad_B_over_M_above_three_quarters"]+=1
        if worst is None or t["B"]/t["M"]>Fraction(
                worst["actual_local_B_over_M"]):
            worst={
                "physical_ordered_endpoints":[list(ends[0]),list(ends[1])],
                "actual_local_B_over_M":str(t["B"]/t["M"]),
                "number_real_proper_original_P3_paths":len(group),
                "middle_owner_source_flag_groups":t["source_original_midflag_count"],
                "x_y_largest_symbol_middle_source_mass_fraction_sum":
                    str(t["sum_relative_largest_x_and_y_symbol_weight"]),
                "actual_original_pair_label_overlap_x_weight":
                    str(t["Ox"]),
                "actual_original_pair_label_overlap_y_weight":
                    str(t["Oy"]),
                "actual_original_both_label_overlap_weight":
                    str(t["Oxy"]),
            }
    M=sums["M"];G=sums["G"];B=sums["B"];D=sums["D"]
    if not M>0 or not G>0 or G+B!=M:
        raise AssertionError("full ORIGINAL all-h symbol sum not positive or conservative")
    if G != D+sums["G00"]+sums["G11"]:
        raise AssertionError("full ORIGINAL GOOD mass not decomposed into diagonal/no-overlap/shared-corner")
    if not G>=sums["source_G_symbol_max_mass_lower_bound"]:
        raise AssertionError("all-h source symbol max concentration global G lower false")
    if not 0<=M_actualbad<=M_heavy<=M or not 0<=M_strictsafe<=M:
        raise AssertionError("true ORIGINAL heavy-symbol source M mass accounting failed")
    if M_actualbad+M_strictsafe>M:
        raise AssertionError("actual bad and certified strict-safe original bins overlap")
    if not 0<=M_safe_diag<=M_safe_diag00<=M_safe_all<=M:
        raise AssertionError("all-h ORIGINAL D / D+G00 / D+G00+G11 safety gates must improve monotonically")
    if M_actualbad+M_safe_all>M:
        raise AssertionError("actual strict bad B75 bins overlap full exact G strict safe bins")
    observed=_observed_full_original_flag_label_overlap_degree(c)
    rows={k:str(v) for k,v in sums.items()}
    return {
        "original_s":s,"original_scheme":scheme,"original_CORE":core,
        "source_GQ_points_and_lines_each":c["V"],
        "source_original_named_flag_count":len(c["flags"]),
        "source_original_retained_CORE_flag_count":len(c["ids"]),
        "source_actual_physical_pair_alphabet_size":c["a"],
        "source_real_physical_owned_edges":len(c["owner"]),
        "exact_original_priority_threeowner_source_sets":len(rank),
        "full_source_real_physical_path_census":True,
        "moments":rows,
        "total_original_M":str(M),"total_original_G":str(G),
        "total_original_B":str(B),
        "exact_original_B_over_M":str(B/M),
        "original_symbol_G00_weighted_fraction_of_M":str(sums["G00"]/M),
        "original_symbol_G11_weighted_fraction_of_M":str(sums["G11"]/M),
        "original_diagonal_D_fraction_of_M":str(D/M),
        "source_symbol_actual_cross_middle_pair_overlap_x_fraction_M":str(sums["Ox"]/M),
        "source_symbol_actual_cross_middle_pair_overlap_y_fraction_M":str(sums["Oy"]/M),
        "source_symbol_actual_both_middle_pair_overlap_fraction_M":str(sums["Oxy"]/M),
        "source_symbol_heavy_weighted_M_share":str(M_heavy/M),
        "strict_local_B75_diagonal_only_certified_safe_M_share":
            str(M_safe_diag/M),
        "strict_local_B75_diagonal_plus_nooverlap_certified_safe_M_share":
            str(M_safe_diag00/M),
        "strict_local_B75_diagonal_plus_nooverlap_incremental_safe_M_share":
            str((M_safe_diag00-M_safe_diag)/M),
        "strict_local_B75_sharedcorner_11_incremental_safe_M_share":
            str((M_safe_all-M_safe_diag00)/M),
        "strict_local_B75_full_exact_moments_certified_safe_M_share":
            str(M_safe_all/M),
        "full_original_source_global_B75_sufficient_from_D_plus_G00_alone":
            sums["D"]+sums["G00"]>M/4,
        "full_original_source_global_B75_sufficient_from_D_plus_G00_G11":
            G>M/4,
        "source_symbol_actual_strict_local_bad_M_share":str(M_actualbad/M),
        "source_symbol_certified_strict_safe_M_share":str(M_strictsafe/M),
        "worst_true_original_local_source_endpoint":worst,
        "unweighted_original_middle_flag_label_capacity":observed,
        "counts":dict(sorted(counts.items())),
        "root_PROVED_A":False,
        "all_h_global_B_over_M_below_three_quarters_PROVED":False,
    }


def canonical_report():
    cases=[_full_moment_case(s,sch,core) for s,sch,core in CASES]
    expect=[1346,1154,838,83892,82846,79404,9966,66418]
    if [r["counts"]["total_full_original_coordinate_proper_P3_paths"]
            for r in cases]!=expect:
        raise AssertionError("independent source full W32 W34 P3 population does not match previous baseline")
    capacity=[_potential_original_middle_label_overlap_degree_bound(s,
               _minimal_pair_alphabet((s+1)*(s*s+1)))
              for s in (2,4,8,16,32,64)]
    for i,z in enumerate(capacity):
        if i>0 and z["fraction_bound_for_distinct_original_flag_pairs"]=="1" and z["s"]>16:
            raise AssertionError("asymptotic minimal-alphabet source capacity unexpectedly vacuous")
    return {
        "schema":SCHEMA,"issue":230,"status":ROOT_STATUS,
        "all_h_complete_original_M_G_B_exact_linear_sparse_symbol_second_moment_formulas":True,
        "all_h_exact_original_x_y_and_both_pair_overlap_inclusion_exclusion":True,
        "all_h_exact_good_disjoint_middle_00_11_physical_corner_square_moments":True,
        "all_h_heavy_original_physical_symbol_necessary_for_local_B_above_three_quarters":True,
        "all_h_strict_B75_monotone_diagonal_to_nooverlap_to_sharedcorner_safe_mass_gates":True,
        "all_h_minimal_pair_alphabet_source_label_overlap_degree_O_s_5_over_2":True,
        "all_h_unweighted_flag_label_overlap_fraction_O_s_minus_3_over_2":True,
        "this_does_NOT_claim_weighted_same_endpoint_overlap_sparsity":True,
        "root_PROVED_A":False,
        "all_h_global_B_over_M_below_three_quarters_PROVED":False,
        "infinite_original_correlated_counterexample_family_claimed":False,
        "external_numeric_C6_graph_constants_claimed":False,
        "ASET_exponent_claimed":False,
        "true_genuine_original_W32_W34_complete_full_moment_censuses":cases,
        "independent_all_h_minimal_alphabet_degree_capacity_examples":capacity
    }


if __name__=="__main__":
    print("AA4_SYMMOM_CERTIFICATE="+json.dumps(canonical_report(),sort_keys=True,separators=(",",":")))
