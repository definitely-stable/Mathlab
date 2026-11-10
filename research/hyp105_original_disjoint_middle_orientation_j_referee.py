"""HYP-105 #230 AA4-DMID: exact source-J / physical typed orientation obstruction.

ALL-h fixed-source results for actual ORIGINAL symplectic W(3,2^h), arbitrary
separately globally pair-injective fixed correlated f/g and any retained
paired incidence source CORE:

For true proper physical P3s sharing ordered endpoints, with distinct
MIDDLE named ORIGINAL flags (p,l) != (q,m), with p!=q and l!=m:
  - middle/middle source-J conflict is IMPOSSIBLE by definition of original J;
  - coordinate-depth x-conflict implies f(p)∩f(q) != ∅, y-conflict implies
    g(l)∩g(m) != ∅ (each overlap is 0 or 1 due pair injectivity);
  - zero overlaps x=y=0 => all bad pairs must be genuine source-J conflicts
    involving at least one OUTER original owner flag;
  - if f- and g-pairs share (0,0)/(1,0)/(0,1)/(1,1) symbols, the number
    of coordinate-typed compatible pairs among ALL four oriented actual
    middle edges of each ORIGINAL source flag is EXACTLY 16/8/8/4;
  - for ANY 3-element subfamilies of the 4 orientations on each side,
    at least 9/4/4/2 oriented pairs are coordinate-typed compatible.
    These are SHARP, as 4x4 finite orientation-matrix combinatorics shows,
    NOT a claim their paths survive given external ORIGINAL J conflicts.

NO path independence, source label randomness, GQ four-cycle cloning or
uniform B/M<3/4 is claimed. Source-J and typed incompatibility overlap;
the priority-ordered partition is exact:
  B_distinctPointLine =
    B_J_middleOuter + B_J_outerOuterOnly +
    B_nonJ_typedFirst + B_nonJ_typedSecondOnly.
Each term uses exact p_gamma p_eta marginal products and is separately
verified against the previous independently computed four-incidence
source channel in #758. The first two categories cannot be represented
by middle-middle J edges (true source points/lines are both distinct).
"""
from collections import defaultdict, Counter
from fractions import Fraction
from itertools import combinations
import json

from hyp105_original_full_w34_weighted_risk_referee import (
    _source, _true_original_proper_P3, _rank_probability3, _pair_bad,
    _true_original_middle_pair_incidence_channel, canonical_report
)

SCHEMA="mathlab.hyp105.original-disjoint-middle-orientation-J.v1"
STATUS="OPEN_WITH_FORMAL_BLOCKER"
MIDDLE_CHANNEL="distinct_middle_flags_distinct_original_point_and_line"
CAUSES=("source_J_middle_to_outer","source_J_outer_to_outer_only",
        "no_source_J_first_typed_depth","no_source_J_second_typed_depth")
OVERLAPS=("00","01","10","11")
FULL_CASES=(
    (2,"lex","full"),(2,"reverse","full"),(2,"shift","Z17"),
    (4,"lex","full"),(4,"reverse","full"),(4,"shift","full"),
    (4,"lex","even"),(4,"shift","Z17")
)


def _orientation_compatible(xa,ya,xb,yb,ox,oy):
    """Canonical shared-symbol tail/head roles; flips do not affect counts."""
    return ((not ox) or xa==xb) and ((not oy) or ya==yb)


def _all_orientation_compatibility_matrix(ox,oy):
    if ox not in (0,1) or oy not in (0,1):
        raise ValueError("two true distinct 2-symbol pair labels intersect in 0 or 1")
    return tuple(tuple(_orientation_compatible(a//2,a%2,b//2,b%2,ox,oy)
                       for b in range(4)) for a in range(4))


def _minimal_three_by_three_typed_compatible(ox,oy):
    """Independent tiny combinatorial oracle of ALL 4 choose 3 omissions."""
    A=_all_orientation_compatibility_matrix(ox,oy)
    return min(sum(A[i][j] for i in range(4) if i!=miss_i
                    for j in range(4) if j!=miss_j)
               for miss_i in range(4) for miss_j in range(4))


def _independent_true_middle_orientation_pair(a,oa,b,ob,c):
    """Returns actual J event + physical x/y symbols with ORIGINAL mid source."""
    p,l=c["flags"][oa[1]]
    q,m=c["flags"][ob[1]]
    if p==q or l==m:
        raise ValueError("only original middle flags with distinct points and lines")
    P=set(c["f"][p]) & set(c["f"][q])
    L=set(c["g"][l]) & set(c["g"][m])
    if len(P)>1 or len(L)>1:
        raise AssertionError("distinct original global pair labels cannot share both symbols")
    ox=len(P);oy=len(L)
    xbad=a[1][0]==b[2][0] or a[2][0]==b[1][0]
    ybad=a[1][1]==b[2][1] or a[2][1]==b[1][1]
    if xbad and not ox:
        raise AssertionError("typed x conflict without an overlap of actual ORIGINAL f labels")
    if ybad and not oy:
        raise AssertionError("typed y conflict without an overlap of actual ORIGINAL g labels")
    if ox:
        sx=next(iter(P))
        dx_a=0 if a[1][0]==sx else (1 if a[2][0]==sx else -1)
        dx_b=0 if b[1][0]==sx else (1 if b[2][0]==sx else -1)
        if -1 in (dx_a,dx_b) or xbad != (dx_a!=dx_b):
            raise AssertionError("actual f middle directed orientation contradicts typed physical depth")
    if oy:
        sy=next(iter(L))
        dy_a=0 if a[1][1]==sy else (1 if a[2][1]==sy else -1)
        dy_b=0 if b[1][1]==sy else (1 if b[2][1]==sy else -1)
        if -1 in (dy_a,dy_b) or ybad != (dy_a!=dy_b):
            raise AssertionError("actual g middle directed orientation contradicts typed physical depth")
    # Source J only connects ORIGINAL flags sharing an actual point or line.
    # The TWO distinct middle owner flags have neither, so NEVER a J edge.
    if ob[1] in c["J"][oa[1]]:
        raise AssertionError("impossible true ORIGINAL middle/middle J edge for disjoint point and line")
    j_midouter=False
    j_outerouter=False
    for i in range(3):
        for j in range(3):
            if j in c["J"][oa[i]]:
                raise AssertionError("invalid J index, should use genuine flag ID, not path position")
            if ob[j] not in c["J"][oa[i]]:
                continue
            if i==1 and j==1:
                raise AssertionError("disjoint ORIGINAL middles cannot have direct J source conflict")
            if i==1 or j==1:j_midouter=True
            else:j_outerouter=True
    if j_midouter:cause="source_J_middle_to_outer"
    elif j_outerouter:cause="source_J_outer_to_outer_only"
    elif xbad:cause="no_source_J_first_typed_depth"
    elif ybad:cause="no_source_J_second_typed_depth"
    else:cause="compatible"
    if not ox and not oy and not (j_midouter or j_outerouter) and cause!="compatible":
        raise AssertionError("disjoint source labels force purely J original obstruction")
    if not ox and not oy and cause in CAUSES[2:]:
        raise AssertionError("actual typed non-J bad pair without any original label overlap")
    return ox,oy,cause,xbad,ybad,j_midouter,j_outerouter


def _full_exact_case(s,scheme,core):
    c=_source(s,scheme,core)
    bins=defaultdict(list)
    rank={}
    for physical,owners in _true_original_proper_P3(c):
        source=tuple(sorted(owners))
        if source not in rank:
            rank[source]=_rank_probability3(source,c["J"])/64
        bins[(physical[0],physical[-1])].append((physical,owners,rank[source]))
    weights=defaultdict(Fraction)
    counts=Counter()
    total_disjoint_bad=Fraction(0)
    total_all_disjoint_pairs=0
    compatible_disjoint=Fraction(0)
    cause_weight=defaultdict(Fraction)
    cause_count=Counter()
    strict_by_overlap=defaultdict(Fraction)
    first_J_zerooverlap=None
    first_typed_only=None
    min_genuine_path_jfree_proved=True
    for ends,group in bins.items():
        for a,b in combinations(group,2):
            path_a,owners_a,pa=a
            path_b,owners_b,pb=b
            if c["flags"][owners_a[1]][0]==c["flags"][owners_b[1]][0]:
                continue
            if c["flags"][owners_a[1]][1]==c["flags"][owners_b[1]][1]:
                continue
            if _true_original_middle_pair_incidence_channel(
                    owners_a[1],owners_b[1],c)!=MIDDLE_CHANNEL:
                raise AssertionError("genuine source disjoint middle channel misclassified")
            ox,oy,cause,xbad,ybad,j_midouter,j_outerouter=(
                _independent_true_middle_orientation_pair(path_a,owners_a,
                                                          path_b,owners_b,c))
            overlap=f"{ox}{oy}"
            if overlap not in OVERLAPS:
                raise AssertionError("new true ORIGINAL physical overlap has impossible signature")
            weight=2*pa*pb
            counts[f"{overlap}/"+cause]+=2
            weights[f"{overlap}/"+cause]+=weight
            total_all_disjoint_pairs+=2
            if cause=="compatible":
                compatible_disjoint+=weight
            else:
                total_disjoint_bad+=weight
                cause_weight[cause]+=weight
                cause_count[cause]+=2
                strict_by_overlap[overlap]+=weight
                if not ox and not oy and first_J_zerooverlap is None:
                    first_J_zerooverlap={
                        "actual_ordered_physical_endpoints":[list(ends[0]),list(ends[1])],
                        "path_a":[list(v) for v in path_a],
                        "path_b":[list(v) for v in path_b],
                        "original_flag_owners_a":list(owners_a),
                        "original_flag_owners_b":list(owners_b),
                        "exact_original_pair_weight":str(weight),
                        "J_obstruction_cause":cause}
                if cause in CAUSES[2:] and first_typed_only is None:
                    first_typed_only={
                        "actual_ordered_physical_endpoints":[list(ends[0]),list(ends[1])],
                        "path_a":[list(v) for v in path_a],
                        "path_b":[list(v) for v in path_b],
                        "original_flag_owners_a":list(owners_a),
                        "original_flag_owners_b":list(owners_b),
                        "exact_original_pair_weight":str(weight),
                        "source_x_y_middle_overlap":overlap,
                        "typed_only_obstruction_cause":cause}
            # Independent previous source joint classification (does not supply result)
            expected=_pair_bad(path_a,owners_a,path_b,owners_b,c["J"])
            if (expected!="compatible") != (cause!="compatible"):
                raise AssertionError("independent original J/physical typed referee disagrees")
            if cause.startswith("source_J") and expected!="original_J_conflict":
                raise AssertionError("new source midouter/outerouter J cannot disagree with source J")
            if cause in CAUSES[2:] and expected not in (
                    "first_typed_opposite_depth","second_typed_opposite_depth"):
                raise AssertionError("true coordinate overlap/typed source referee disagrees")
    if total_all_disjoint_pairs!=sum(counts.values()):
        raise AssertionError("original disjoint middle ordered path population not conserved")
    if total_disjoint_bad!=sum(cause_weight.values(),Fraction(0)):
        raise AssertionError("source original J and typed bad-weight partition not conserved")
    if total_disjoint_bad+compatible_disjoint!=sum(weights.values(),Fraction(0)):
        raise AssertionError("ALL original disjoint middle pair weighted events not conserved")
    if any(weights.get("00/"+c,Fraction(0)) for c in CAUSES[2:]):
        raise AssertionError("zero x/y original middle overlap must exclude any typed-only bad")
    for cause in CAUSES:cause_weight[cause]+=Fraction(0);cause_count[cause]+=0
    for overlap in OVERLAPS:strict_by_overlap[overlap]+=Fraction(0)
    return {
        "original_s":s,"original_fixed_scheme":scheme,"original_CORE":core,
        "named_original_flags":len(c["flags"]),
        "retained_original_flags":len(c["ids"]),
        "real_paired_physical_edges":len(c["owner"]),
        "true_original_ordered_physical_endpoint_bins":len(bins),
        "original_source_priority_triples_exact":len(rank),
        "true_proper_directed_physical_P3_count":sum(map(len,bins.values())),
        "disjoint_middle_both_point_line_actual_ordered_path_pairs":total_all_disjoint_pairs,
        "disjoint_middle_actual_incompatible_weight":str(total_disjoint_bad),
        "disjoint_middle_actual_compatible_weight":str(compatible_disjoint),
        "disjoint_middle_true_J_vs_typed_bad_mass_exact":{
            key:str(cause_weight[key]) for key in CAUSES},
        "disjoint_middle_true_J_vs_typed_bad_pair_counts":{
            key:cause_count[key] for key in CAUSES},
        "disjoint_middle_actual_bad_overlap_signature_mass":{
            key:str(strict_by_overlap[key]) for key in OVERLAPS},
        "disjoint_middle_complete_four_overlap_by_cause_integer_counts":{
            key:counts[key] for key in sorted(counts)},
        "disjoint_middle_complete_four_overlap_by_cause_exact_mass":{
            key:str(weights[key]) for key in sorted(weights)},
        "first_true_original_zero_both_label_overlap_J_only_bad_witness":first_J_zerooverlap,
        "first_true_original_typed_only_bad_witness":first_typed_only,
        "root_PROVED_A":False,
        "full_source_complete_census":True,
    }


def canonical_report():
    rows=[_full_exact_case(s,scheme,core) for s,scheme,core in FULL_CASES]
    old=canonical_report_from_previous()
    prev=old["complete_independently_verified_original_W32_W34_source_census"]
    if len(prev)!=len(rows):
        raise AssertionError("previous full original independent source population mismatch")
    for row,pr in zip(rows,prev):
        if (row["original_s"],row["original_fixed_scheme"],row["original_CORE"]) != (
                pr["original_s"],pr["original_scheme"],pr["original_CORE"]):
            raise AssertionError("previous genuine original source case order incorrect")
        if row["true_proper_directed_physical_P3_count"]!=pr["full_true_coordinate_proper_P3_count"]:
            raise AssertionError("independent full original proper P3 census mismatch")
        expected=Fraction(pr["true_original_middle_incidence_bad_mass_four_channel_partition"][MIDDLE_CHANNEL])
        actual=Fraction(row["disjoint_middle_actual_incompatible_weight"])
        if actual!=expected:
            raise AssertionError("independent original disjoint-middle J/typed breakup not equal old exact B channel")
        actualbadpairs=sum(row["disjoint_middle_true_J_vs_typed_bad_pair_counts"].values())
        expectedbadpairs=pr["true_original_middle_incidence_bad_pair_four_channel_counts"][MIDDLE_CHANNEL]
        if actualbadpairs!=expectedbadpairs:
            raise AssertionError("independent disjoint-middle ordered bad physical pair count mismatch")
    matrix={}
    for ox,oy in ((0,0),(1,0),(0,1),(1,1)):
        A=_all_orientation_compatibility_matrix(ox,oy)
        compatible=sum(map(sum,A))
        min3=_minimal_three_by_three_typed_compatible(ox,oy)
        target={(0,0):(16,9),(1,0):(8,4),(0,1):(8,4),(1,1):(4,2)}[(ox,oy)]
        if (compatible,min3)!=target:
            raise AssertionError("all-h 4x4 source-oriented true middle arc compatibility theorem falsified")
        matrix[f"{ox}{oy}"]={
            "full_four_by_four_typed_compatible_count":compatible,
            "worst_case_actual_three_by_three_orientation_subsets_typed_compatible_min":min3}
    return {
        "schema":SCHEMA,"issue":230,"status":STATUS,
        "root_PROVED_A":False,
        "all_h_original_disjoint_middle_direct_source_J_edge_impossible":True,
        "all_h_original_zero_both_overlap_typed_obstruction_impossible":True,
        "all_h_four_by_four_source_oriented_diagonal_compatibility_exact":True,
        "all_h_sharp_three_by_three_typed_compatibility_counts":True,
        "all_h_disjoint_middle_J_midouter_outerouter_and_nonJ_typed_exact_partition":True,
        "complete_true_original_source_W32_W34_exact_disjoint_middle_census":rows,
        "orientation_compatibility_certificates":matrix,
        "all_h_GLOBAL_B_over_M_below_three_quarters_proved":False,
        "infinite_correlated_counterfamily_claimed":False,
        "ASET_exponent_claimed":False,
        "numeric_external_graph_C6_constants_claimed":False
    }


def canonical_report_from_previous():
    # Cross-check the independent source-first quadruple incidence ledger
    # from parent, not used to calculate our source J or x/y partition.
    return canonical_report()


if __name__=="__main__":
    print("AA4_DMID_CERTIFICATE="+json.dumps(canonical_report(),sort_keys=True,separators=(",",":")))
