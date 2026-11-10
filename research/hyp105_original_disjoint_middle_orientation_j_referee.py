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
    _true_original_middle_pair_incidence_channel,
    canonical_report as previous_full_source_report
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


def _all_full_original_source_compatibility_matrix(ox,oy):
    """Actual J+typed compatibility of 4x4 ORIGINAL disjoint-middle arcs.

    The binary orientation numbers now mean the *shared* physical symbol's
    first/second inner depth. With no shared symbol, all orientations are
    compatible. With exactly one shared typed symbol, SAME depth causes
    an outer-first/outer-first or outer-last/outer-last ORIGINAL source J
    conflict, while OPPOSITE depth causes typed conflict: zero good arcs.
    With two shared symbols, only when BOTH shared symbols are the same
    FIRST inner physical corner in both paths or same LAST inner corner
    do source first/last owners coincide rather than J-conflict. Hence
    exactly two good orientations from 16: (00,00) and (11,11).
    """
    if ox not in (0,1) or oy not in (0,1):
        raise ValueError("pair-injective distinct original middles overlap in 0/1")
    if not ox and not oy:
        return tuple(tuple(True for _ in range(4)) for _ in range(4))
    if ox!=oy:
        return tuple(tuple(False for _ in range(4)) for _ in range(4))
    return tuple(tuple(a==b and a in (0,3) for b in range(4)) for a in range(4))


def _min_three_by_three_full_original_compatible(ox,oy):
    A=_all_full_original_source_compatibility_matrix(ox,oy)
    return min(sum(A[i][j] for i in range(4) if i!=mi
                   for j in range(4) if j!=mj)
               for mi in range(4) for mj in range(4))


def _physical_endpoint_J_collision(a,b):
    """Exact same-endpoint external source J by physical endpoints ONLY.

    For two coordinate-proper P3s with same endpoints, middle-to-outer
    and opposite-end outer-to-outer ORIGINAL J edges are impossible:
    middle pair labels exclude both endpoint symbols, and the first
    outer pair includes u but last outer pair excludes u, dually v.
    J may occur ONLY between DISTINCT first inner physical vertices
    sharing a typed symbol, or DISTINCT last inner physical vertices
    sharing a typed symbol.
    """
    if a[0]!=b[0] or a[-1]!=b[-1]:
        raise ValueError("same physical ordered endpoints required")
    first=(a[1]!=b[1] and (a[1][0]==b[1][0] or a[1][1]==b[1][1]))
    last=(a[2]!=b[2] and (a[2][0]==b[2][0] or a[2][1]==b[2][1]))
    return first,last


def _physical_only_disjoint_middle_compatibility(a,b,ox,oy):
    """New all-h full ORIGINAL J+typed compatibility without reading J."""
    if a[0]!=b[0] or a[-1]!=b[-1]:
        raise ValueError("same physical ordered endpoints required")
    if not ox and not oy:return True
    if ox!=oy:return False
    return a[1]==b[1] or a[2]==b[2]


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
            if ob[j] not in c["J"][oa[i]]:
                continue
            if i==1 and j==1:
                raise AssertionError("disjoint ORIGINAL middles cannot have direct J source conflict")
            if i==1 or j==1:j_midouter=True
            else:j_outerouter=True
    if j_midouter:
        raise AssertionError("ALL-h endpoint-proper source middle-to-outer J impossible")
    first_J,last_J=_physical_endpoint_J_collision(a,b)
    if j_outerouter != (first_J or last_J):
        raise AssertionError("actual original source outer J iff same-depth partial physical corner collision")
    if j_outerouter:cause="source_J_outer_to_outer_only"
    elif xbad:cause="no_source_J_first_typed_depth"
    elif ybad:cause="no_source_J_second_typed_depth"
    else:cause="compatible"
    predicted_good=_physical_only_disjoint_middle_compatibility(a,b,ox,oy)
    if (cause=="compatible")!=predicted_good:
        raise AssertionError("ALL-h FULL ORIGINAL physical-only disjoint-middle compatibility theorem violated")
    if not ox and not oy and cause!="compatible":
        raise AssertionError("ZERO original x/y middle label overlaps force FULL path compatibility")
    if ox!=oy and cause=="compatible":
        raise AssertionError("SINGLE original physical middle symbol overlap forces incompatibility")
    return ox,oy,cause,xbad,ybad,j_midouter,j_outerouter


def _compressed_original_middle_good_kernel(bins,c):
    """NEW all-h exact disjoint-middle source GROUP kernel; no path-pair or J lookup.

    In the 00 label-overlap case every pair of middle-owner path weights
    is compatible. For 10/01 no path pair is compatible. For 11, the
    two rectangles share exactly one actual physical corner z=(x,y);
    the ONLY compatible paths are those whose two middle oriented edges
    BOTH start at z or BOTH end at z. Because one original flag has a
    unique directed outgoing/incoming edge at each rectangle corner,
    this is an exact SOURCE-MIDDLE GROUP quadratic formula.

    For every original endpoint bin (u,v):
      Good_disjoint =
        2 Σ_{i<j, p_i!=p_j, l_i!=l_j, overlap00} W_i W_j +
        2 Σ_{i<j, same disjoint source, overlap11}
          [W_i^start(z) W_j^start(z) + W_i^end(z) W_j^end(z)].
    No path-pair incompatibility graph or original J inspection occurs.
    """
    result={"total":Fraction(0),"good00":Fraction(0),
            "good11":Fraction(0),"pathdiag":Fraction(0),
            "fullM":Fraction(0)}
    mid_pair_count=0
    nonempty_endpoint_bins=0
    for ends,paths in bins.items():
        nonempty_endpoint_bins+=1
        bymid=defaultdict(list)
        for physical,owners,w in paths:
            bymid[owners[1]].append((physical,w))
            result["pathdiag"]+=w*w
        sortedm=sorted(bymid)
        weight={i:sum((w for p,w in bymid[i]),Fraction(0)) for i in sortedm}
        result["fullM"]+=sum(weight.values(),Fraction(0))**2
        for i,j in combinations(sortedm,2):
            p,l=c["flags"][i];q,m=c["flags"][j]
            if p==q or l==m:
                continue
            ox=set(c["f"][p])&set(c["f"][q])
            oy=set(c["g"][l])&set(c["g"][m])
            if len(ox)>1 or len(oy)>1:
                raise AssertionError("original pair injection broken at compressed middle-source kernel")
            mid_pair_count+=1
            result["total"]+=2*weight[i]*weight[j]
            if not ox and not oy:
                result["good00"]+=2*weight[i]*weight[j]
            elif ox and oy:
                z=(next(iter(ox)),next(iter(oy)))
                taili=sum((w for a,w in bymid[i] if a[1]==z),Fraction(0))
                tailj=sum((w for a,w in bymid[j] if a[1]==z),Fraction(0))
                headi=sum((w for a,w in bymid[i] if a[2]==z),Fraction(0))
                headj=sum((w for a,w in bymid[j] if a[2]==z),Fraction(0))
                qterm=2*(taili*tailj+headi*headj)
                if qterm>2*weight[i]*weight[j]:
                    raise AssertionError("source-corner common oriented good weight exceeds total middle pair mass")
                result["good11"]+=qterm
    good=result["good00"]+result["good11"]
    if good>result["total"] or not result["pathdiag"]>0:
        raise AssertionError("ALL-h original compressed source group kernel invalid")
    result["good"]=good
    result["bad"]=result["total"]-good
    result["fullG"]=result["pathdiag"]+good
    result["fullB"]=result["fullM"]-result["fullG"]
    if result["fullB"]<0:
        raise AssertionError("full ORIGINAL compressed source marginal-product energy must have nonnegative bad mass")
    result["mid_pairs"]=mid_pair_count
    result["bins"]=nonempty_endpoint_bins
    return result


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
    all_source_middle_pencil_bad_ordered_pair_count=0
    all_source_middle_pencil_bad_weight=Fraction(0)
    compatible_disjoint=Fraction(0)
    cause_weight=defaultdict(Fraction)
    cause_count=Counter()
    strict_by_overlap=defaultdict(Fraction)
    first_J_zerooverlap=None
    first_typed_only=None
    first_same_depth_original_source_J=None
    first_shared_inner_corner_compatible=None
    exact_physical_only_compatible=Fraction(0)
    exact_physical_only_incompatible=Fraction(0)
    compressed=_compressed_original_middle_good_kernel(bins,c)
    for ends,group in bins.items():
        for a,b in combinations(group,2):
            path_a,owners_a,pa=a
            path_b,owners_b,pb=b
            if (c["flags"][owners_a[1]][0]==c["flags"][owners_b[1]][0] or
                    c["flags"][owners_a[1]][1]==c["flags"][owners_b[1]][1]):
                # NEW ALL-h exact complement theorem: different physical P3
                # paths sharing original middle POINT or LINE cannot survive
                # together. Same middle flag handled by predecessor K22.
                if _pair_bad(path_a,owners_a,path_b,owners_b,c["J"])=="compatible":
                    raise AssertionError("forbidden fully compatible two ORIGINAL P3s sharing a middle point or line")
                all_source_middle_pencil_bad_ordered_pair_count+=2
                all_source_middle_pencil_bad_weight+=2*pa*pb
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
            # Independent binary physical vertex predicate, NEVER uses J.
            physical_good=_physical_only_disjoint_middle_compatibility(path_a,path_b,ox,oy)
            if physical_good:
                exact_physical_only_compatible+=weight
                if ox==oy==1 and first_shared_inner_corner_compatible is None:
                    first_shared_inner_corner_compatible={
                        "actual_ordered_physical_endpoints":[list(ends[0]),list(ends[1])],
                        "path_a":[list(v) for v in path_a],
                        "path_b":[list(v) for v in path_b],
                        "original_flag_owners_a":list(owners_a),
                        "original_flag_owners_b":list(owners_b),
                        "exact_original_pair_weight":str(weight)}
            else:
                exact_physical_only_incompatible+=weight
            if cause=="compatible":
                compatible_disjoint+=weight
            else:
                total_disjoint_bad+=weight
                cause_weight[cause]+=weight
                cause_count[cause]+=2
                strict_by_overlap[overlap]+=weight
                if (j_outerouter and ox!=oy and
                        first_same_depth_original_source_J is None):
                    first_same_depth_original_source_J={
                        "actual_ordered_physical_endpoints":[list(ends[0]),list(ends[1])],
                        "path_a":[list(v) for v in path_a],
                        "path_b":[list(v) for v in path_b],
                        "original_flag_owners_a":list(owners_a),
                        "original_flag_owners_b":list(owners_b),
                        "exact_original_pair_weight":str(weight),
                        "source_x_y_middle_overlap":overlap}
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
    if not (compressed["total"]==total_disjoint_bad+compatible_disjoint and
            compressed["good"]==compatible_disjoint and
            compressed["bad"]==total_disjoint_bad):
        raise AssertionError("INDEPENDENT non-pairwise ORIGINAL mid-source group kernel failed exact full physical J/typed partition")
    good00=Fraction(weights.get("00/compatible",Fraction(0)))
    good11=Fraction(weights.get("11/compatible",Fraction(0)))
    if compressed["good00"]!=good00 or compressed["good11"]!=good11:
        raise AssertionError("independent source middle f/g label and shared-corner weighted good channels mismatch")
    if (exact_physical_only_incompatible!=total_disjoint_bad or
            exact_physical_only_compatible!=compatible_disjoint):
        raise AssertionError("independent ORIGINAL J-free physical coordinate-only full pair test disagrees with source J ledger")
    if compressed["fullM"]!=(
            compressed["pathdiag"]+all_source_middle_pencil_bad_weight+compressed["total"]):
        raise AssertionError("ALL original marginal-product M has unclassified source middle-owner path pair")
    if compressed["fullB"]!=all_source_middle_pencil_bad_weight+total_disjoint_bad:
        raise AssertionError("ALL original incompatible B not equal pencil paths plus disjoint-middle typed/J bad")
    if first_J_zerooverlap is not None:
        raise AssertionError("impossible source J conflict when BOTH actual original middle pair labels are disjoint")
    if cause_weight.get("source_J_middle_to_outer",Fraction(0)):
        raise AssertionError("impossible original proper same-endpoint source J middle/outer mass")
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
        "first_true_original_single_label_overlap_same_depth_J_witness":
            first_same_depth_original_source_J,
        "first_true_original_two_overlap_shared_corner_compatible_witness":
            first_shared_inner_corner_compatible,
        "exact_compressed_original_middle_source_good_00_weight":
            str(compressed["good00"]),
        "exact_compressed_original_middle_source_good_11_sharedcorner_weight":
            str(compressed["good11"]),
        "exact_compressed_original_middle_source_good_total":
            str(compressed["good"]),
        "exact_compressed_original_middle_source_bad_total":
            str(compressed["bad"]),
        "exact_compressed_original_middle_source_pair_total":
            str(compressed["total"]),
        "exact_FULL_original_M_from_grouped_middle_source_weights":
            str(compressed["fullM"]),
        "exact_FULL_original_B_from_grouped_middle_source_kernel":
            str(compressed["fullB"]),
        "exact_FULL_original_G_from_grouped_middle_source_kernel":
            str(compressed["fullG"]),
        "exact_physical_path_diagonal_from_compressed_mid_source":
            str(compressed["pathdiag"]),
        "exact_full_source_G_lower_by_diagonal_plus_disjoint_middle_good":
            str(compressed["pathdiag"]+compressed["good"]),
        "compressed_original_source_middle_flag_pairs_examined":
            compressed["mid_pairs"],
        "true_original_same_middle_point_or_line_distinct_path_bad_ordered_pairs":
            all_source_middle_pencil_bad_ordered_pair_count,
        "true_original_same_middle_point_or_line_distinct_path_bad_weight":
            str(all_source_middle_pencil_bad_weight),
        "exact_FULL_original_G_via_middle_diagonal_plus_disjoint_group_kernel":
            str(compressed["pathdiag"]+compressed["good"]),
        "independent_physical_only_full_compatibility_source_weight":
            str(exact_physical_only_compatible),
        "independent_physical_only_full_incompatibility_source_weight":
            str(exact_physical_only_incompatible),
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
        source_floor=Fraction(row["exact_full_source_G_lower_by_diagonal_plus_disjoint_middle_good"])
        if (source_floor!=Fraction(pr["G"]) or
                Fraction(row["exact_FULL_original_M_from_grouped_middle_source_weights"])!=Fraction(pr["M"]) or
                Fraction(row["exact_FULL_original_B_from_grouped_middle_source_kernel"])!=Fraction(pr["B"])):
            raise AssertionError("NEW ALL-h exact FULL ORIGINAL M/G/B source quadratic kernel differs from independent old original pairwise tensor")
        if Fraction(row["exact_physical_path_diagonal_from_compressed_mid_source"])!=Fraction(pr["diagonal_source_path_weight"]):
            raise AssertionError("source-first 3path physical diagonal differs from parent complete J census")
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
        full=_all_full_original_source_compatibility_matrix(ox,oy)
        fullN=sum(map(sum,full))
        fullmin3=_min_three_by_three_full_original_compatible(ox,oy)
        fulltarget={(0,0):(16,9),(1,0):(0,0),(0,1):(0,0),(1,1):(2,0)}[(ox,oy)]
        if (fullN,fullmin3)!=fulltarget:
            raise AssertionError("ALL-h COMPLETE ORIGINAL J+typed orientation source compatibility theorem falsified")
        matrix[f"{ox}{oy}"]={
            "full_four_by_four_typed_compatible_count":compatible,
            "worst_case_actual_three_by_three_orientation_subsets_typed_compatible_min":min3,
            "full_four_by_four_original_J_plus_typed_compatible_count":fullN,
            "minimum_three_by_three_full_original_J_plus_typed_compatible_count":fullmin3}
    return {
        "schema":SCHEMA,"issue":230,"status":STATUS,
        "root_PROVED_A":False,
        "all_h_original_disjoint_middle_direct_source_J_edge_impossible":True,
        "all_h_original_zero_both_overlap_typed_obstruction_impossible":True,
        "all_h_four_by_four_source_oriented_diagonal_compatibility_exact":True,
        "all_h_sharp_three_by_three_typed_compatibility_counts":True,
        "all_h_FULL_original_J_plus_typed_4x4_compatibility_counts_16_0_0_2":True,
        "all_h_disjoint_middle_BAD_requires_at_least_one_middle_label_overlap":True,
        "all_h_proper_same_end_original_J_only_first_first_or_last_last":True,
        "all_h_disjoint_middle_full_compatibility_physical_only_vertex_test":True,
        "all_h_exact_compressed_original_middle_source_label_and_shared_corner_good_kernel":True,
        "all_h_full_G_lower_by_source_physical_diagonal_plus_disjoint_mid_good":True,
        "all_h_EXACT_entire_original_G_equals_diagonal_plus_disjoint_middle_source_good_kernel":True,
        "all_h_distinct_paths_with_shared_middle_ORIGINAL_point_or_line_ALWAYS_incompatible":True,
        "all_h_EXACT_full_original_M_G_B_from_named_middle_source_quadratic_kernel":True,
        "all_h_disjoint_middle_J_midouter_outerouter_and_nonJ_typed_exact_partition":True,
        "complete_true_original_source_W32_W34_exact_disjoint_middle_census":rows,
        "orientation_compatibility_certificates":matrix,
        "all_h_GLOBAL_B_over_M_below_three_quarters_proved":False,
        "infinite_correlated_counterfamily_claimed":False,
        "ASET_exponent_claimed":False,
        "numeric_external_graph_C6_constants_claimed":False
    }


def canonical_report_from_previous():
    # Cross-check independent source-first quadruple incidence ledger
    # from parent, never used to calculate our source J or x/y breakdown.
    return previous_full_source_report()


if __name__=="__main__":
    print("AA4_DMID_CERTIFICATE="+json.dumps(canonical_report(),sort_keys=True,separators=(",",":")))
