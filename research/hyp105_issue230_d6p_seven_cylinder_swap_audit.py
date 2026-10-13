"""HYP-105 #230 D6-P: deterministic ORIGINAL seven-family right-label cylinders.

ALL-FINITE-H MATHEMATICAL IDENTITY (finite W32 implementation only):
Fix a complete globally injective left physical-pair map f on ORIGINAL
GQ points. Select DISTINCT ORIGINAL six-incidence subsets with left
physical type A/B/C. A right cylinder contains:
  * six ORIGINAL right line IDs in original incidence-column order
    (repetitions intentionally retained);
  * left physical type A/B/C;
  * the left physical column-dual pairing when A is a 6-cycle;
  * repeated original left point incidence positions when B.
Original sixsets with identical cylinder signature have the same
accepted seven-GF5 class under EVERY complete right injection g.
Let m_f(t) count ORIGINAL sixsets with cylinder t and let chi_t(g)
be its accepted seven-class indicator (0 or one of seven classes).
Then exactly S_seven(f,g)=sum_t m_f(t)1{chi_t(g)!=0},
and 51**6 R3_selected_lower=sum_t m_f(t) GF5_WEIGHT[chi_t(g)].

A/A aligned D6 is NOT a function of the unordered right six-line
support: its column-dual pairing depends on WHICH incidence positions
carry the right physical edges. B/B-overlap similarly depends on
repeated-point vs repeated-line incidence positions. Discarding column
positions is therefore invalid for the full seven-family count.

For a transposition of two ORIGINAL right-line physical pair labels u,v,
chi_t(g) can change ONLY when cylinder t uses u or v. Therefore exact
seven-family swap increments can be recomputed using only those cylinders.
For B-left/A-right and C-left/A-right, if BOTH u and v occur among the
SIX DISTINCT original right lines, swapping physical labels preserves
the unordered physical right A-edge set, hence the indicator is unchanged.
This latter sharpening is NOT valid for full D6 or the other families.

This is a model-equivalent deterministic support/cylinder reduction, not
an all-h Omega(s**6) lower, an infinite Branch B witness, or full R3 upper.
"""
from collections import Counter, defaultdict
from itertools import combinations
from math import comb
import json

from hyp105_g5e2b3e1a_fixed_leading import (
    selected_left_six, validated_small_model,
)
from hyp105_g5e2b3e1b0_seven_signature import (
    R3_CERTIFIED_FLOORS, seven_census,
)
from hyp105_issue230_projection import fixture


SEVEN_CLASSES=tuple(R3_CERTIFIED_FLOORS)
LEFT_TYPES=("A","B","C")
RIGHT_TYPES=("A","B","C")
PHYSICAL_PROFILES={
    (1,1,1,1,1,1):"A",
    (2,1,1,1,1):"B",
    (2,2,2):"C",
}


def _physical_dual(indices, pair_labels):
    """Six pairs of original column positions induced by six coordinates."""
    col=defaultdict(list)
    for pos, original_factor in enumerate(indices):
        u,v=pair_labels[original_factor]
        col[u].append(pos)
        col[v].append(pos)
    if len(col)!=6 or any(len(values)!=2 for values in col.values()):
        return ()
    return tuple(sorted(tuple(sorted(values)) for values in col.values()))


def _is_six_cycle(dual):
    if len(dual)!=6 or len(set(dual))!=6:
        return False
    adj=[set() for _ in range(6)]
    for u,v in dual:
        if u==v:
            return False
        adj[u].add(v)
        adj[v].add(u)
    if any(len(x)!=2 for x in adj):
        return False
    visited={0}
    stack=[0]
    while stack:
        for v in adj[stack.pop()]:
            if v not in visited:
                visited.add(v)
                stack.append(v)
    return len(visited)==6


def _right_kind(lines, right_labels):
    """Genuine right physical 2-regularity, retaining ORIGINAL repeats."""
    prof=tuple(sorted(Counter(lines).values(),reverse=True))
    kind=PHYSICAL_PROFILES.get(prof)
    if kind is None:
        return None
    physical=Counter(c for r in lines for c in right_labels[r])
    if len(physical)!=6 or set(physical.values())!={2}:
        return None
    return kind


def _signature_for_original_sixset(ids, kind, edges, left_labels):
    """One canonical, incidence-position-aware right cylinder."""
    if kind not in LEFT_TYPES or len(ids)!=6 or len(set(ids))!=6:
        raise ValueError("requires original six distinct incidence IDs and A/B/C")
    pts=tuple(edges[i][0] for i in ids)
    lines=tuple(edges[i][1] for i in ids)
    left_dual=()
    repeated_left=()
    if kind=="A":
        if len(set(pts))!=6:
            raise AssertionError("left A must use six distinct original points")
        dual=_physical_dual(pts,left_labels)
        left_dual=dual if _is_six_cycle(dual) else ()
    elif kind=="B":
        repeated=[p for p,count in Counter(pts).items() if count==2]
        if len(repeated)!=1:
            raise AssertionError("left B must have one doubled original point")
        repeated_left=tuple(i for i,p in enumerate(pts) if p==repeated[0])
        if len(repeated_left)!=2:
            raise AssertionError("invalid doubled left point positions")
    else:
        if tuple(sorted(Counter(pts).values()))!=(2,2,2):
            raise AssertionError("left C needs three doubled original points")
    return kind,lines,left_dual,repeated_left


def cylinder_seven_class(signature, right_labels):
    """Independent accepted seven GF5 class classifier for one cylinder."""
    left_type,lines,left_dual,left_repeat=signature
    right_type=_right_kind(lines,right_labels)
    if right_type is None:
        return None
    if (left_type,right_type)==("B","A"):
        return "B-left/A-right"
    if (left_type,right_type)==("A","B"):
        return "A-left/B-right"
    if {left_type,right_type}=={"A","C"}:
        return "C/A"
    if {left_type,right_type}=={"B","C"}:
        return "C/B"
    if (left_type,right_type)==("B","B"):
        repeated=[r for r,c in Counter(lines).items() if c==2]
        if len(repeated)!=1:
            raise AssertionError("right B repeated original line invariant")
        right_repeat={i for i,r in enumerate(lines) if r==repeated[0]}
        overlap=len(right_repeat.intersection(left_repeat))
        if overlap not in (0,1):
            raise AssertionError("original GQ simple incidences forbid BB double overlap")
        return "B/B-overlap" if overlap else "B/B-disjoint"
    if (left_type,right_type)==("A","A"):
        right_dual=_physical_dual(lines,right_labels)
        if left_dual and right_dual==left_dual:
            return "D6"
    return None


def compile_original_W32_cylinders(model):
    """Finite W32 canonical ALL-left-A/B/C ORIGINAL sixset compression."""
    left,right,edges,_=validated_small_model(model)
    compiled=Counter()
    all_left=Counter()
    for ids,kind in selected_left_six(model):
        if kind not in LEFT_TYPES:
            raise AssertionError("unexpected original left physical type")
        all_left[kind]+=1
        sig=_signature_for_original_sixset(ids,kind,edges,left)
        compiled[sig]+=1
    if all_left!={"A":51030,"B":10935,"C":405}:
        raise AssertionError("complete original W32 left candidate count changed")
    if sum(compiled.values())!=62370:
        raise AssertionError("lost ORIGINAL incidence sixsets during compression")
    by_original_line=defaultdict(list)
    for sig in compiled:
        for line in set(sig[1]):
            by_original_line[line].append(sig)
    return {
        "a":model["a"],
        "original_lines":len(right),
        "cylinders":compiled,
        "by_original_line":dict(by_original_line),
        "left_original_sixset_counts":dict(all_left),
        "original_left_sixsets":sum(compiled.values()),
        "unique_position_aware_right_cylinders":len(compiled),
    }


def cylinder_census(compiled,right_labels):
    """No original sixset enumeration after one compilation of f."""
    counts=Counter()
    for sig,m in compiled["cylinders"].items():
        tag=cylinder_seven_class(sig,right_labels)
        if tag is not None:
            counts[tag]+=m
    seven={k:counts[k] for k in SEVEN_CLASSES}
    return {
        "seven_class_motif_counts":seven,
        "S_seven":sum(seven.values()),
        "GF5_seven_lower_numerator":sum(
            R3_CERTIFIED_FLOORS[tag]*v for tag,v in seven.items()),
        "uses_independent_right_physical_classifier":True,
        "number_original_left_candidates":compiled["original_left_sixsets"],
    }


def swapped_labels(right_labels,u,v):
    result=list(right_labels)
    if (type(u) is not int or type(v) is not int or
            not 0<=u<len(result) or not 0<=v<len(result) or u==v):
        raise ValueError("swap two distinct original right line IDs")
    result[u],result[v]=result[v],result[u]
    return tuple(result)


def exact_seven_cylinder_swap(compiled,right_labels,u,v):
    """Only cylinders whose ORIGINAL right support intersects {u,v}."""
    changed=set(compiled["by_original_line"].get(u,()))
    changed.update(compiled["by_original_line"].get(v,()))
    new=swapped_labels(right_labels,u,v)
    before=Counter()
    after=Counter()
    stable_two_factor_classes=0
    both_present=0
    for sig in changed:
        w=compiled["cylinders"][sig]
        old=cylinder_seven_class(sig,right_labels)
        updated=cylinder_seven_class(sig,new)
        if old:
            before[old]+=w
        if updated:
            after[updated]+=w
        if u in sig[1] and v in sig[1]:
            both_present+=w
            if sig[0] in ("B","C") and len(set(sig[1]))==6:
                # For left B/C + 6 distinct right ORIGINAL lines,
                # same unordered set of right physical PAIR edges.
                # The acceptance of right A cannot change.
                if (old=="B-left/A-right") != (updated=="B-left/A-right"):
                    raise AssertionError("B-left/A-right two-present swap invariant")
                if (old=="C/A" and sig[0]=="C") != (
                        updated=="C/A" and sig[0]=="C"):
                    raise AssertionError("C-left/A-right two-present swap invariant")
                stable_two_factor_classes+=w
    diff={kind:after[kind]-before[kind] for kind in SEVEN_CLASSES}
    total_delta=sum(diff.values())
    weighted_delta=sum(R3_CERTIFIED_FLOORS[k]*v for k,v in diff.items())
    return {
        "swap_original_lines":[u,v],
        "touched_unique_cylinders":len(changed),
        "touched_original_sixsets":sum(compiled["cylinders"][sig]
                                     for sig in changed),
        "both_original_lines_in_cylinder_sixsets":both_present,
        "both_lines_right_A_stable_BC_original_sixsets":stable_two_factor_classes,
        "delta_by_seven_class":diff,
        "delta_S_seven":total_delta,
        "delta_GF5_selected_lower_numerator":weighted_delta,
        "exact_swapped_right_labels_are_globally_injective":True,
    }


def original_W32_seven_cylinder_report():
    records=[]
    for scheme in ("lex","reverse","S68","S72"):
        model=fixture(1,scheme)
        compiled=compile_original_W32_cylinders(model)
        right=model["right_labels"]
        row=cylinder_census(compiled,right)
        source=seven_census(model,independent_checks=False)
        if (row["seven_class_motif_counts"]!=source["seven_class_motif_counts"]
                or row["S_seven"]!=source["S_seven"]
                or row["GF5_seven_lower_numerator"]!=source[
                    "GF5_seven_lower_numerator"]):
            raise AssertionError("independent ORIGINAL seven-GF5 census mismatch")
        swaps=[exact_seven_cylinder_swap(compiled,right,u,v)
               for u,v in combinations(range(len(right)),2)]
        if len(swaps)!=105:
            raise AssertionError("must check ALL 105 original W32 right-label swaps")
        deltas=[z["delta_S_seven"] for z in swaps]
        weighted_deltas=[z["delta_GF5_selected_lower_numerator"]
                         for z in swaps]
        records.append({
            "scheme":scheme,
            "base":row,
            "compressed_original_cylinders":compiled[
                "unique_position_aware_right_cylinders"],
            "original_left_sixset_counts":compiled["left_original_sixset_counts"],
            "all_105_original_right_pair_label_transpositions_checked":True,
            "number_improving_one_swaps":sum(x<0 for x in deltas),
            "number_worsening_one_swaps":sum(x>0 for x in deltas),
            "number_stable_one_swaps":sum(x==0 for x in deltas),
            "min_delta_S_seven":min(deltas),
            "max_delta_S_seven":max(deltas),
            "min_delta_GF5_lower_numerator":min(weighted_deltas),
            "max_delta_GF5_lower_numerator":max(weighted_deltas),
            "minimum_delta_swap":swaps[deltas.index(min(deltas))][
                "swap_original_lines"],
            "strict_right_one_swap_local_minimum":min(deltas)>0,
            "right_one_swap_local_minimum":min(deltas)>=0,
            "strict_right_one_swap_local_maximum":max(deltas)<0,
            "all_swaps_local_only":True,
        })
    return {
        "slice":"HYP105-ISSUE230-D6P-ORIGINAL-SEVEN-CYLINDER-SWAP",
        "all_finite_h_exact_seven_cylinder_identity":True,
        "all_g_same_two_global_injections":"REQUIRED",
        "D6_original_column_position_information":"REQUIRED",
        "finite_W32_independent_original_seven_GF5_classifier":"MATCHED",
        "finite_W32_all_105_right_line_swaps_each":"EXACT-LOCAL-CYLINDER-DELTAS",
        "complete_W34_W38_seven_S":"UNKNOWN-NOT-CLAIMED",
        "deterministic_all_h_lower_bound_proved":False,
        "infinite_correlated_Branch_B_proved":False,
        "Branch_A":"OPEN","Branch_B":"OPEN",
        "records":records
    }


if __name__=="__main__":
    print(json.dumps(original_W32_seven_cylinder_report(),indent=2,sort_keys=True))
