"""HYP-105 B3.2-E1-B0: exact same-label seven-family GF5 obstruction.

For complete W(3,2)/K6 bijections this joins all accepted strictly
positive six-coordinate leading motif floors on the SAME factor incidence
set and physical pair labels. D6 is the aligned C6/C6 ORIGINAL matching
family, U_B-left/right are nonmatching one-factor-cherry families,
and four new classes are accepted #224 / #227. This is a rigorously
scoped finite diagnostic. The polynomial identity below is all-h exact,
but no universal S=Omega(s^6) lower, strict R3 upper or ASET power follows.
"""
from collections import Counter
from fractions import Fraction
import json

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_g5e2b3e1a_fixed_leading import (
    GF5_DENOM, CASES, MIN_GF5,
    validated_small_model, selected_left_six,
    _half_projection_kind, _classify_six_prechecked,
)
from hyp105_g5e2b3b2_coincident_cycles import exact_coincident_c6
from hyp105_g5e2b3d_joint_risk import (
    exact_coincident_c4, closed_form_c4_GF5_flow_weight,
)

R3_CERTIFIED_FLOORS = {
    "D6": 5643,
    "B-left/A-right": 45600,
    "A-left/B-right": 45600,
    "C/A": 10*MIN_GF5["C/A"],
    "C/B": 10*MIN_GF5["C/B"],
    "B/B-overlap": 10*MIN_GF5["B/B-overlap"],
    "B/B-disjoint": 10*MIN_GF5["B/B-disjoint"],
}
assert set(R3_CERTIFIED_FLOORS) == {
    "D6", "B-left/A-right", "A-left/B-right",
    "C/A", "C/B", "B/B-overlap", "B/B-disjoint",
}

# Every unranked selected original six-subset has a coefficient of exactly
# one in P(t,x,y) = prod_{(p,l) original incidence}
#   (1 + t * x_{f(p),0}*x_{f(p),1} * y_{g(l),0}*y_{g(l),1}).
# The coefficient [t^6 x_i^2 for i in S (others 0)
#                    y_j^2 for j in T (others 0)], |S|=|T|=6,
# is precisely the six-coordinate leafless count on both halves,
# for ANY finite simple original incidence host. Tags z_p,w_l in each
# factor recover original endpoint multiplicity partitions A/B/C.
#
# This is an identity (one formal monomial per selected original edge);
# it does not provide a fast all-h coefficient extraction by itself.


def physical_column_dual(edges, labels, endpoints):
    """Return six named-column dual edges; inputs have a 6+6 leafless projection."""
    coordinate_to_cols={}
    for local_id, e in enumerate(endpoints):
        u,v=labels[e]
        coordinate_to_cols.setdefault(u,[]).append(local_id)
        coordinate_to_cols.setdefault(v,[]).append(local_id)
    if len(coordinate_to_cols)!=6 or any(len(x)!=2 for x in coordinate_to_cols.values()):
        return None
    return tuple(sorted(tuple(sorted(x)) for x in coordinate_to_cols.values()))


def is_connected_column_cycle(dual):
    """One single 6-cycle on six column positions, not two triangles."""
    if dual is None or len(dual)!=6 or len(set(dual))!=6:
        return False
    adj=[set() for _ in range(6)]
    for u,v in dual:
        if u==v:
            return False
        adj[u].add(v)
        adj[v].add(u)
    if any(len(x)!=2 for x in adj):
        return False
    reached={0}
    todo=[0]
    while todo:
        for v in adj[todo.pop()]:
            if v not in reached:
                reached.add(v)
                todo.append(v)
    return len(reached)==6


def classify_seven_prechecked(ids,left,right,edges):
    """Complete seven accepted leading classes; one value or None."""
    ids=tuple(sorted(ids))
    if len(ids)!=6 or len(set(ids))!=6 or ids[0]<0 or ids[-1]>=len(edges):
        raise ValueError("exactly six different original incidence IDs")
    p=tuple(edges[i][0] for i in ids)
    l=tuple(edges[i][1] for i in ids)
    left_type=_half_projection_kind(p,left)
    right_type=_half_projection_kind(l,right)
    if left_type is None or right_type is None:
        return None
    if left_type=="B" and right_type=="A":
        return "B-left/A-right"
    if left_type=="A" and right_type=="B":
        return "A-left/B-right"
    if left_type=="A" and right_type=="A":
        ld=physical_column_dual(edges,left,p)
        rd=physical_column_dual(edges,right,l)
        if ld==rd and is_connected_column_cycle(ld):
            return "D6"
        return None
    return _classify_six_prechecked(ids,left,right,edges)


def seven_census(model, *, independent_checks=True, witness_sets=False):
    """Full finite W32 seven-class original-six-set count and both R2/R3 floors.

    One exhaustive LEFT candidate enumerator (accepted E1A), no
    binom(45,6) six-subset scan, no physical-sign template overcount.
    """
    left,right,edges,_=validated_small_model(model)
    counts=Counter()
    seen=set()
    witnesses={}
    collected={} if witness_sets else None
    for ids,kind in selected_left_six(model):
        if ids in seen:
            raise AssertionError("original six-set repeated")
        seen.add(ids)
        tag=classify_seven_prechecked(ids,left,right,edges)
        if tag is not None:
            counts[tag]+=1
            witnesses.setdefault(tag,ids)
            if collected is not None:
                collected[ids]=tag
    if len(seen)!=62370:
        raise AssertionError("complete W32 left 6-coordinate count changed")
    if independent_checks:
        d=exact_coincident_c6(model,witness_limit=0)
        if counts["D6"]!=d["exact_coincident_C6_factor_matchings_D"]:
            raise AssertionError("independent C6 DFS+join count disagrees")
        q=exact_coincident_c4(model,witness_limit=0)
        four=q["Q4"]
        if q["GF5_C4_flow_weight"]!=531 or closed_form_c4_GF5_flow_weight()!=531:
            raise AssertionError("full GF5 four-column coefficient changed")
    else:
        four=None
    r3numerator=sum(counts[k]*w for k,w in R3_CERTIFIED_FLOORS.items())
    result={
        "scope":"complete W(3,2) K6 fixed physical pair bijections",
        "new_classes":{k:counts[k] for k in CASES},
        "seven_class_motif_counts":{k:counts[k] for k in R3_CERTIFIED_FLOORS},
        "S_seven":sum(counts.values()),
        "left_6coordinate_candidates":len(seen),
        "GF5_seven_lower_numerator":r3numerator,
        "GF5_seven_lower":Fraction(r3numerator,GF5_DENOM),
        "GF5_r3_denominator":GF5_DENOM,
        "Q4":four,
        "GF5_Q4_R2_lower":(
            Fraction(531*four,51**4) if four is not None else None
        ),
        "witnesses":witnesses,
        "sets":collected,
        "all_h_polynomial_coefficient_identity":True,
        "all_h_universal_S_lower_proved":False,
        "all_h_strict_risk_upper_proved":False,
        "full_GF5_R2_or_R3_computed":False,
        "new_ASET_exponent":False,
    }
    if set(counts)-set(R3_CERTIFIED_FLOORS):
        raise AssertionError("some motif category unaccounted")
    return result


def exact_seven_weighted_GF5(model, *, max_signed_events=5000):
    """EXACT selected seven-family GF5 R3 contribution, NOT total R3.

    Collect every actual qualifying ORIGINAL six-incidence set ONCE.
    Count all 10 unordered balanced 3-vs-3 sign events with the accepted
    independent integer GF5 dual Fourier oracle (all 51 full nonzero
    checksum-4 per-column patterns). For D6 this counts nine additional
    possible signs beyond the ONE alternating event used in the floor.
    A budget breach raises, never returns a partially computed statistic.
    """
    from hyp105_g5e2b3b1_critical_flows import SIGNS
    from hyp105_g5e2b3b1b_five_six_flows import exact_dual_GF5_six_flow
    census=seven_census(model,independent_checks=False,witness_sets=True)
    sets=census["sets"]
    if (not isinstance(max_signed_events,int) or max_signed_events<1
            or 10*len(sets)>max_signed_events):
        raise ValueError("exact full-palette GF5 event budget exceeded")
    if len(SIGNS)!=10:
        raise AssertionError("global-sign-unordered 3v3 partition changed")
    subtotal=Counter()
    min_event_by_class={}
    max_event_by_class={}
    positive_by_class=Counter()
    all_event_count=0
    for ids,tag in sorted(sets.items()):
        supports=tuple(model["supports"][j] for j in ids)
        if len(supports)!=6 or any(len(s)!=4 for s in supports):
            raise ValueError("physical GF5 support map missing six support-four columns")
        for mask in SIGNS:
            signs=tuple(1 if (mask>>i)&1 else -1 for i in range(6))
            val=exact_dual_GF5_six_flow(supports,signs,dimension=model["m"])
            if not isinstance(val,int) or val<0:
                raise AssertionError("negative/nonintegral exact GF5 flow")
            all_event_count+=1
            positive_by_class[tag]+=bool(val)
            subtotal[tag]+=val
            if tag not in min_event_by_class:
                min_event_by_class[tag]=val
                max_event_by_class[tag]=val
            else:
                min_event_by_class[tag]=min(min_event_by_class[tag],val)
                max_event_by_class[tag]=max(max_event_by_class[tag],val)
    if all_event_count != 10*census["S_seven"]:
        raise AssertionError("full 3v3 signed GF5 event mass lost")
    exact_num=sum(subtotal.values())
    if exact_num<census["GF5_seven_lower_numerator"]:
        raise AssertionError("exact selected GF5 seven-class risk below accepted floor")
    for tag in R3_CERTIFIED_FLOORS:
        if tag!="D6" and tag in min_event_by_class:
            expected_per_signed=R3_CERTIFIED_FLOORS[tag]//10
            if min_event_by_class[tag]<expected_per_signed:
                raise AssertionError("new/one-cherry GF5 class minimum violated")
    return {
        "seven_class_original_sixsets":census["S_seven"],
        "selected_exact_GF5_signed_events":all_event_count,
        "selected_positive_signed_events_by_class":dict(positive_by_class),
        "selected_GF5_sum_by_class":dict(subtotal),
        "selected_min_signed_GF5_by_class":min_event_by_class,
        "selected_max_signed_GF5_by_class":max_event_by_class,
        "exact_selected_GF5_R3_numerator":exact_num,
        "exact_selected_GF5_R3":Fraction(exact_num,GF5_DENOM),
        "prior_certified_seven_GF5_R3_floor":
            census["GF5_seven_lower"],
        "total_GF5_R3_all_motifs":False,
        "all_h_general_GF5_bound":False,
    }


def report():
    out=[]
    for scheme in ("lex","reverse-line"):
        m=pair_labeled_symplectic(1,scheme)
        a=seven_census(m)
        weighted=exact_seven_weighted_GF5(m)
        out.append({
            "scheme":scheme,
            "S_seven":a["S_seven"],
            "seven_counts":a["seven_class_motif_counts"],
            "Q4":a["Q4"],
            "R2_necessary_GF5":str(a["GF5_Q4_R2_lower"]),
            "R3_necessary_GF5":str(a["GF5_seven_lower"]),
            "R3_necessary_numerator":a["GF5_seven_lower_numerator"],
            "exact_selected_seven_GF5_R3":
                str(weighted["exact_selected_GF5_R3"]),
            "exact_selected_seven_GF5_R3_numerator":
                weighted["exact_selected_GF5_R3_numerator"],
            "exact_selected_seven_GF5_sign_events":
                weighted["selected_exact_GF5_signed_events"],
            "exact_selected_by_class":weighted["selected_GF5_sum_by_class"],
        })
    return {
        "finite_joint_obstruction":out,
        "all_h_formal_coefficient_identity":True,
        "all_h_universal_motif_lower":False,
        "all_h_strict_R3_upper":False,
        "actual_full_R3_computed":False,
    }


if __name__=="__main__":
    print(json.dumps(report(),indent=2,sort_keys=True))
