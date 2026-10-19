"""HYP-105 #230 AA4-CO: EXACT global original all-seven W32 96-map audit.

Unlike #612-#614's TWO restricted source POINT-A sixflag fibers,
enumerate ALL 62,370 true original left-2factor six-DISTINCT incidence
Q under EACH of the SAME 96 globally injected original POINT f maps,
one fully injected original LINE g kept unchanged.

For every genuine original W(3,2^h) and every fixed complete
correlated f,g, physical left 2-regular/6coordinate Q necessarily
has TRUE original source POINT multiplicity pattern A=(1^6),
B=(2,1^4), C=(2^3), by the physical degree-deficit argument and
injectivity of source-factor physical pair images. The accepted
SEVEN historical GF5 positive classes therefore partition disjointly:
two selected POINT-A sixpoint-source fibers A/B, other POINT-A,
all source POINT-B, all source POINT-C.
The partition and covariance of sum are tautologically EXACT all-h,
but there is NO all-h lower from this decomposition.

The full ORIGINAL selected weighted seven-GF5 score and the ROOT #230
UNWEIGHTED seven-motif S are measured for all 96 actual complete f
maps. Two separately verified true original historical fiber scores
from #612/614 are subtracted EXACTLY once, and all complement source
patterns independently accounted. Any local negative/positive
covariance MUST be evaluated against this full root diagnostic before
a false global compensation or asymptotic claim.
"""
from collections import Counter
from fractions import Fraction

from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4cl_shared_four_point_fibers_covariance import (
    ORBIT, FAMILIES, _cov, complete_overlapping_global_f,
    genuine_original_two_fiber_fixture, original_two_fiber_same_global_96_orbit,
)
from hyp105_g5e2b3e1a_fixed_leading import selected_left_six
from hyp105_g5e2b3e1b0_seven_signature import (
    R3_CERTIFIED_FLOORS, classify_seven_prechecked, seven_census,
)
from hyp105_issue230_projection import fixture

GROUPS=("A_fiber","B_fiber","A_other","POINT_B","POINT_C")
SEVEN=tuple(R3_CERTIFIED_FLOORS)
EXPECTED_LEFT_COUNT=62370


def source_original_POINT_multiplicity(Q,original_inc):
    """Check actual six distinct original flag IDs and typed source multiplicity."""
    Q=tuple(Q)
    if len(Q)!=6 or len(set(Q))!=6 or any(
            type(j) is not int or j<0 or j>=len(original_inc) for j in Q):
        raise ValueError("SIX DISTINCT genuine original incidence IDs are mandatory")
    freq=Counter(original_inc[j][0] for j in Q)
    signature=tuple(sorted(freq.values()))
    if signature==(1,)*6:return "A"
    if signature==(1,1,1,1,2):return "B"
    if signature==(2,2,2):return "C"
    return "OTHER"


def _actual_source_bucket(Q,kind,inc,PA,PB):
    if kind=="A":
        members=frozenset(inc[j][0] for j in Q)
        if members==PA:return "A_fiber"
        if members==PB:return "B_fiber"
        return "A_other"
    if kind=="B":return "POINT_B"
    if kind=="C":return "POINT_C"
    raise AssertionError("physical original sixcoordinate left Q cannot have another source multiplicity")


def original_W32_global_96_allseven_census(model,points):
    """Whole true original W32 7-class S and accepted GF5 floor, every f state.

    This independently enumerates ALL original Q, not the union of TWO
    source-POINT-A fibers, nor samples of Q, nor a single selected
    historical D6 signature.
    """
    s,V,a,inc,f,g,_,_=_original_source(model)
    if (s,V,a)!=(2,15,6):
        raise ValueError("EXHAUSTIVE GLOBAL original sevenclass bridge W32/K6 ONLY")
    pts=tuple(points)
    if (len(pts)!=8 or len(set(pts))!=8 or any(
            type(p) is not int or p<0 or p>=V for p in pts)):
        raise ValueError("eight genuinely distinct original POINT source IDs required")
    PA=frozenset(pts[i] for i in FAMILIES["A"])
    PB=frozenset(pts[i] for i in FAMILIES["B"])
    if len(PA& PB)!=4 or len(PA)!=6 or len(PB)!=6:
        raise ValueError("two different original source 6point sets with four shared")
    # Global f orbit legality and double-fiber physical support guard
    dual=original_two_fiber_same_global_96_orbit(model,pts)
    scores={k:[] for k in GROUPS}
    counts={k:[] for k in GROUPS}
    class_counts=[]
    physical_counts=[]
    full_weight=[];full_unweighted=[]
    original_Q_accepted=[]
    for state in ORBIT:
        actual_f=complete_overlapping_global_f(f,pts,state)
        current=dict(model,left_labels=actual_f)
        group_counts=Counter()
        hist=Counter()
        physically_left=0
        positive_original_Qs=0
        for Q,kind in selected_left_six(current):
            physically_left+=1
            tag=classify_seven_prechecked(Q,actual_f,g,inc)
            if tag is None:continue
            source_kind=source_original_POINT_multiplicity(Q,inc)
            if source_kind!=kind:
                raise AssertionError("actual true ORIGINAL source factor pattern != real physical left generator")
            group=_actual_source_bucket(Q,kind,inc,PA,PB)
            hist[tag]+=1
            group_counts[group,tag]+=1
            positive_original_Qs+=1
        if physically_left!=EXPECTED_LEFT_COUNT:
            raise AssertionError("complete true original W32 left-Q count must be 62,370")
        curr_weight=sum(R3_CERTIFIED_FLOORS[k]*n for k,n in hist.items())
        curr_count=sum(hist.values())
        if sum(group_counts.values())!=curr_count:
            raise AssertionError("some accepted true original Q was double-counted or lost")
        for group in GROUPS:
            gs=sum(n*R3_CERTIFIED_FLOORS[tag] for (gname,tag),n in group_counts.items()
                   if gname==group)
            gc=sum(n for (gname,_),n in group_counts.items() if gname==group)
            scores[group].append(gs)
            counts[group].append(gc)
        if sum(scores[group][-1] for group in GROUPS)!=curr_weight:
            raise AssertionError("GLOBAL seven-GF5 weighted source partition is not exhaustive")
        if sum(counts[group][-1] for group in GROUPS)!=curr_count:
            raise AssertionError("GLOBAL UNWEIGHTED root seven-motif S source partition is not exhaustive")
        for family in ("A","B"):
            if scores[family+"_fiber"][-1]!=dual["global_state_scores"][family][state]:
                raise AssertionError("independent ALL-ORIGINAL-Q original W32 GF5 tag census differs from fixed original twofiber historical score")
        full_weight.append(curr_weight)
        full_unweighted.append(curr_count)
        physical_counts.append(physically_left)
        class_counts.append(dict(hist))
        original_Q_accepted.append(positive_original_Qs)
    if len(full_weight)!=96:
        raise AssertionError("all true original global f 96 source action states required")
    A=tuple(scores["A_fiber"]);B=tuple(scores["B_fiber"])
    R=tuple(sum(scores[x][i] for x in ("A_other","POINT_B","POINT_C"))
            for i in range(96))
    T=tuple(full_weight)
    if _cov(A,B)!=dual["historical_score_covariance_A_B"]:
        raise AssertionError("true entire original W32 selected Q twofiber covariance mismatched prior")
    # Variance/covariance of entire GLOBAL original seven-class count
    # (not just the two source fibers) as a raw algebraic check.
    relation=(_cov(A,A)+_cov(B,B)+_cov(R,R)
              +2*_cov(A,B)+2*_cov(A,R)+2*_cov(B,R))
    if relation!=_cov(T,T):
        raise AssertionError("entire actual original sevenGF5 score does not satisfy exact coupled variance ledger")
    count_vectors={k:tuple(v) for k,v in counts.items()}
    unweighted=tuple(full_unweighted)
    if sum(R3_CERTIFIED_FLOORS[tag]*class_counts[0].get(tag,0) for tag in SEVEN)!=T[0]:
        raise AssertionError("historical seven classes do not reconstruct first complete map")
    return {
        "scope":"entire original W32/K6 root selected sevenfamily S, all 96 GLOBAL complete f maps",
        "s":s,"V":V,"a":a,
        "original_eight_source_POINT_factors":pts,
        "six_distinct_original_incidence_IDs_required":True,
        "all_96_full_original_f_and_one_g":True,
        "physically_left_original_six_Q_each":tuple(physical_counts),
        "all_seven_original_historical_class_counts_by_complete_f":tuple(class_counts),
        "full_root_UNWEIGHTED_seven_motif_S":unweighted,
        "full_original_hist_GF5_weighted_seven_numerator":T,
        "all_original_Q_counts_by_SOURCE_group":count_vectors,
        "all_original_GF5_weight_by_SOURCE_group":{
             k:tuple(v) for k,v in scores.items()},
        "source_fiber_A_B_GF5_covariance":_cov(A,B),
        "complement_GF5_variance":_cov(R,R),
        "full_original_GF5_weighted_variance":_cov(T,T),
        "full_original_UNWEIGHTED_seven_variance":_cov(unweighted,unweighted),
        "global_variance_ledger_components":{
           "Var_A":_cov(A,A),"Var_B":_cov(B,B),"Var_rest":_cov(R,R),
           "Cov_A_B":_cov(A,B),"Cov_A_rest":_cov(A,R),
           "Cov_B_rest":_cov(B,R)},
        "weighted_min":min(T),"weighted_max":max(T),
        "unweighted_min":min(unweighted),"unweighted_max":max(unweighted),
        "root_A_B_C_status":"OPEN_WITH_FORMAL_BLOCKER",
        "all_h_universal_fixed_label_lower_NOT_PROVED":True,
        "W34_W38_full_sixset_census_NOT_CLAIMED":True,
    }


def original_W32_S72_reversible_TWO_family_fixture():
    """One real original W32 S72 fixture, eight true original POINT IDs."""
    model=fixture(1,"S72")
    s,V,a,inc,f,g,_,_=_original_source(model)
    shared,ea,eb=(
        ((0,1),(1,2),(3,4),(4,5)),
        ((0,5),(2,3)),
        ((0,3),(2,5)))
    inv={tuple(edge):i for i,edge in enumerate(f)}
    pts=tuple(inv[tuple(edge)] for edge in shared+ea+eb)
    if len(pts)!=8 or len(set(pts))!=8:
        raise AssertionError("real W32 S72 full f has no genuine K6 twofiber four-shared")
    return model,pts


def original_W32_global_reference_single_state(model,points,state):
    """INDEPENDENT legacy W32 full original seven_census (no source bucketing)."""
    s,V,a,inc,f,g,_,_=_original_source(model)
    if (s,V,a)!=(2,15,6):
        raise ValueError("only true original W32 for independent full Q reference")
    full=dict(model,left_labels=complete_overlapping_global_f(f,points,state))
    census=seven_census(full,independent_checks=False)
    return {"weighted":census["GF5_seven_lower_numerator"],
            "unweighted":census["S_seven"],
            "historical_seven_classes":census["seven_class_motif_counts"],
            "original_complete_left_Q":census["left_6coordinate_candidates"]}
