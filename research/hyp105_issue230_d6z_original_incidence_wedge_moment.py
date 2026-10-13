"""HYP-105 #230 D6-Z: ORIGINAL-incidence wedge transport and GF5 proxy barrier.

ALL-h exact identities for any complete, globally injective ORIGINAL
point/line maps on W(3,s), s=2^h, Delta=s+1, V=(s+1)(s²+1), N=V*Delta:
 for a distinct ORIGINAL six-incidence subset Q and typed side X,
 tau_X(Q)=sum_c C(deg_{Q,X}(c),2)
         =sum_{i<j in Q}|label_X(original_factor_i) INTERSECT
                          label_X(original_factor_j)|,
 including original factor repetitions in incidence positions.
 Across ALL C(N,6) distinct ORIGINAL incidence sixsets,
 sum_Q tau_X(Q)=C(N-2,4)*[2V*C(Delta,2)+Delta²*A_X],
 A_X=#physically overlapping pairs among globally injective ORIGINAL
 same-type factor labels. Thus D6-Y's SHARP all-h image bound translates
 to a SHARP two-sided GLOBAL six-incidence wedge-moment envelope.

All seven GF5-positive ORIGINAL sixset types require SIX DISTINCT
physical coordinates of degree TWO on BOTH sides (therefore tau=6).
The coarse wedge moment and its 2-regular proxy do not determine the
positive seven-GF5 count: exact true ORIGINAL W(3,2) seven-census
shows S68!=S72 despite IDENTICAL image physical graphs on both sides.

Also exact all-h geometry-aware second-order incidence transport:
 collinear source point pairs C_src=V*C(Delta,2) (GQ partial linearity),
 random permutation of ANY fixed globally injective physical IMAGE E
 gives E[sum_{collinear source p<q}1[f(p) intersects f(q)]]
   = C_src * A(E)/C(V,2).
This is a FINITE-IMAGE expectation identity, NOT an all-label GF5 lower.

These are double counting identities and graph capacity specializations,
not asserted as novel standalone combinatorics. Branch A/B OPEN.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb
import json

from hyp105_issue230_proof_audit import parameters
from hyp105_issue230_d6y_capacity_adjacency_cut import (
    graph_adjacency_count, sharp_adjacency_image_bound, edge_adjacent,
)
from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1a_fixed_leading import (
    validated_small_model, selected_left_six, _half_projection_kind,
)
from hyp105_g5e2b3e1b0_seven_signature import (
    classify_seven_prechecked,seven_census,R3_CERTIFIED_FLOORS,
)


def _canonical_pair(a,e):
    if (not isinstance(e,(tuple,list)) or len(e)!=2
            or any(type(t) is not int for t in e)
            or not 0<=e[0]<e[1]<a):
        raise ValueError("physical canonical unordered edge required")
    return tuple(e)


def validated_original_regular_model(model):
    """Original SOURCE regular bipartite multitype scope, no fake incidences."""
    if not isinstance(model,dict) or type(model.get("s")) is not int:
        raise ValueError("real ORIGINAL finite model required")
    p=parameters(model["s"])
    V,D,a=p["V"],p["Delta"],p["a"]
    if type(model.get("a")) is not int or model["a"]!=a:
        raise ValueError("minimal ORIGINAL physical alphabet required")
    try:
        L=tuple(_canonical_pair(a,e) for e in model["left_labels"])
        R=tuple(_canonical_pair(a,e) for e in model["right_labels"])
        E=tuple(tuple(edge) for edge in model["incidences"])
    except (KeyError,TypeError) as exc:
        raise ValueError("complete ORIGINAL typed maps/incidences required") from exc
    if (len(L)!=V or len(R)!=V or len(set(L))!=V or len(set(R))!=V
            or len(E)!=V*D or len(set(E))!=len(E)
            or any(len(e)!=2 or any(type(t) is not int or not 0<=t<V for t in e)
                   for e in E)):
        raise ValueError("complete typed ORIGINAL injection and simple incidences required")
    degL=Counter(x for x,y in E)
    degR=Counter(y for x,y in E)
    if (len(degL)!=V or len(degR)!=V or any(degL[i]!=D or degR[i]!=D
                                          for i in range(V))):
        raise ValueError("original point/line source regularity false")
    return p,L,R,E


def physical_wedge_sixset(original_six_incidences,left_labels,right_labels):
    """Exact original incidence-position physical wedge, preserves repeats."""
    E=tuple(tuple(e) for e in original_six_incidences)
    if (len(E)!=6 or len(set(E))!=6 or
            any(len(e)!=2 or any(type(t) is not int or t<0 for t in e)
                for e in E)):
        raise ValueError("exactly six DISTINCT ORIGINAL incidence IDs required")
    result={}
    for side,labels in (("left",left_labels),("right",right_labels)):
        indices=tuple(e[0 if side=="left" else 1] for e in E)
        if any(i>=len(labels) for i in indices):
            raise ValueError("ORIGINAL typed factor ID out of range")
        deg=Counter(z for i in indices for z in labels[i])
        wedge=sum(comb(n,2) for n in deg.values())
        direct=sum(len(set(labels[indices[i]])&set(labels[indices[j]]))
                   for i in range(6) for j in range(i+1,6))
        if wedge!=direct:
            raise AssertionError("physical wedge double-count identity false")
        result[side]={
            "wedge":wedge,
            "distinct_physical_coordinates":len(deg),
            "exact_six_coordinate_two_regular":
                len(deg)==6 and all(n==2 for n in deg.values()),
            "original_distinct_typed_factors":len(set(indices)),
        }
    result["two_sided_regular_proxy"]=(
        result["left"]["exact_six_coordinate_two_regular"] and
        result["right"]["exact_six_coordinate_two_regular"])
    return result


def source_collinearity_adjacency(model):
    """Original GQ incidence-conditioned pair statistics on both sides."""
    p,L,R,E=validated_original_regular_model(model)
    D,V=p["Delta"],p["V"]
    byline=defaultdict(set)
    bypoint=defaultdict(set)
    for point,line in E:
        byline[line].add(point)
        bypoint[point].add(line)
    out={}
    for side,sections,labels in (
        ("left",byline,L),("right",bypoint,R)):
        pairs=Counter()
        for scope in sections.values():
            for x,y in combinations(sorted(scope),2):
                pairs[x,y]+=1
        if len(pairs)!=V*comb(D,2) or any(n!=1 for n in pairs.values()):
            raise ValueError("ORIGINAL GQ partial linearity (no 4-cycle) required")
        observed=sum(edge_adjacent(labels[i],labels[j]) for i,j in pairs)
        image=graph_adjacency_count(labels,p["a"])
        mean=Fraction(len(pairs)*image,comb(V,2))
        out[side]={
            "original_collinear_factor_pairs":len(pairs),
            "physical_adjacent_original_collinear_pairs":observed,
            "physical_adjacent_all_original_factor_pairs":image,
            "exact_image_conditioned_uniform_permutation_expected":str(mean),
            "geometry_aware_but_not_seven_GF5_positive_count":True,
        }
    return out


def _minimal_missing_wedges(a,m):
    # m missing simple edges, min adjacent missing pairs by convexity.
    return max(0,2*m-a)


def sharp_two_sided_wedge_moment_envelope(s):
    """Exact sharp image-only bound -> ORIGINAL 6-incidence wedge moment."""
    p=parameters(s)
    V,D,a=p["V"],p["Delta"],p["a"]
    N=V*D
    cap=sharp_adjacency_image_bound(s)
    m=cap["missing_physical_edges"]
    full=a*comb(a-1,2)
    base=full-2*m*(a-2)
    low=base+_minimal_missing_wedges(a,m)
    high=cap["sharp_max_occupied_adjacent_unordered_pairs"]
    if low>high:
        raise AssertionError("minimum physical adjacency exceeds maximum")
    factor=comb(N-2,4)
    fixed=2*V*comb(D,2)
    lower=factor*(fixed+D*D*low)
    upper=factor*(fixed+D*D*high)
    return {
        **p,"original_total_incidences":N,
        "six_incidence_subsets_count":comb(N,6),
        "pair_incidence_to_sixset_multiplicity":factor,
        "same_original_typed_factor_pair_wedge":fixed,
        "physical_image_adjacency_min_sharp":low,
        "physical_image_adjacency_max_sharp":high,
        "global_original_sixset_wedge_sum_min_sharp":lower,
        "global_original_sixset_wedge_sum_max_sharp":upper,
        "holds_for_both_independent_ORIGINAL_typed_sides":True,
        "not_GF5_positive_seven_count_lower":True,
    }


def _minimal_missing_graph(a,m):
    """Explicit matching or a collection of disjoint paths; m<=a-2."""
    if not 0<=m<=a-2:
        raise ValueError("only minimal K_a physical palette missing edges")
    if 2*m<=a:
        removed=tuple((2*i,2*i+1) for i in range(m))
    else:
        components=a-m
        short=tuple((2*i,2*i+1) for i in range(components-1))
        start=2*(components-1)
        long=tuple((i,i+1) for i in range(start,a-1))
        removed=short+long
    if len(removed)!=m or len(set(removed))!=m:
        raise AssertionError("minimum missing graph has incorrect edge count")
    return removed


def explicit_wedge_moment_extremizers(s, *, max_V=10000):
    """Construct actual complete injective both-typed maps at both sharp ends."""
    z=sharp_two_sided_wedge_moment_envelope(s)
    a,V,m=z["a"],z["V"],z["K"]-z["V"]
    if V>max_V:
        raise ValueError("full physical image output exceeds explicit budget")
    palette=tuple(combinations(range(a),2))
    removed_min=set(_minimal_missing_graph(a,m))
    removed_max={(0,i) for i in range(1,m+1)}
    E_min=tuple(e for e in palette if e not in removed_min)
    E_max=tuple(e for e in palette if e not in removed_max)
    if len(E_min)!=V or len(E_max)!=V:
        raise AssertionError("physical image not complete")
    if graph_adjacency_count(E_min,a)!=z["physical_image_adjacency_min_sharp"]:
        raise AssertionError("minimum missing-degree construction not sharp")
    if graph_adjacency_count(E_max,a)!=z["physical_image_adjacency_max_sharp"]:
        raise AssertionError("maximum missing-star construction not sharp")
    return {
        "s":s,"V":V,
        "min_original_point_image_labels":E_min,
        "max_original_point_image_labels":E_max,
        "min_original_line_image_labels":tuple(reversed(E_min)),
        "max_original_line_image_labels":tuple(reversed(E_max)),
        "extremal_wedges_attainable_on_each_ORIGINAL_type":True,
    }


def actual_original_W32_seven_proxy_report():
    """True source 62,370 ORIGINAL incidence candidate census, no surrogate."""
    rows=[]
    for scheme in ("S68","S72"):
        model=fixture(1,scheme)
        p,L,R,E=validated_original_regular_model(model)
        if len(E)!=45:
            raise AssertionError("original W32 must have exactly 45 incidences")
        actual=seven_census(model,independent_checks=False)
        regular_two_sided=0
        positive=Counter()
        rejected=Counter()
        accepted_witness=None
        rejected_witness=None
        for ids,ltype in selected_left_six(model):
            Q=tuple(E[i] for i in ids)
            indices=tuple(line for point,line in Q)
            rtype=_half_projection_kind(indices,R)
            tagged=classify_seven_prechecked(ids,L,R,E)
            if tagged is not None:
                positive[tagged]+=1
                if accepted_witness is None:
                    accepted_witness=Q
            if rtype is not None:
                regular_two_sided+=1
                if tagged is None:
                    rejected[ltype+"/"+rtype]+=1
                    if rejected_witness is None:
                        rejected_witness=Q
            if tagged is not None and rtype is None:
                raise AssertionError("accepted seven class missing right two regular")
        if sum(positive.values())!=actual["S_seven"]:
            raise AssertionError("true ORIGINAL W32 seven-class census drift")
        if regular_two_sided<actual["S_seven"]:
            raise AssertionError("two-sided degree necessity violated")
        if accepted_witness is None or rejected_witness is None:
            raise AssertionError("positive and false-positive 2-regular witnesses required")
        accepted_check=physical_wedge_sixset(accepted_witness,L,R)
        rejected_check=physical_wedge_sixset(rejected_witness,L,R)
        if (not accepted_check["two_sided_regular_proxy"] or
                not rejected_check["two_sided_regular_proxy"]):
            raise AssertionError("two-sided GF5 necessary proxy false")
        col=source_collinearity_adjacency(model)
        rows.append({
            "scheme":scheme,"original_sixsets_left_candidate_census":62370,
            "two_sided_physical_degree_two_proxy":regular_two_sided,
            "true_original_seven_GF5_positive_count":actual["S_seven"],
            "proxy_false_positives":regular_two_sided-actual["S_seven"],
            "false_positive_types":dict(rejected),
            "seven_positive_by_exact_class":dict(positive),
            "seven_GF5_selected_lower_numerator":
                actual["GF5_seven_lower_numerator"],
            "true_positive_original_sixset_witness":accepted_witness,
            "false_positive_original_sixset_witness":rejected_witness,
            "left_right_global_image_adjacency":
                [graph_adjacency_count(L,6),graph_adjacency_count(R,6)],
            "source_incidence_collinearity":col,
            "all_left_original_incidences_preserved":True,
            "full_R3_or_universal_omega_proved":False,
        })
    if not (rows[0]["true_original_seven_GF5_positive_count"]==68 and
            rows[1]["true_original_seven_GF5_positive_count"]==72):
        raise AssertionError("canonical S68/S72 original seven GF5 count changed")
    if (rows[0]["left_right_global_image_adjacency"] != [60,60] or
            rows[1]["left_right_global_image_adjacency"] != [60,60]):
        raise AssertionError("W32 complete K6 physical image adjacency drift")
    if (rows[0]["proxy_false_positives"]<=0 or
            rows[1]["proxy_false_positives"]<=0):
        raise AssertionError("GF5 seven-class strict proxy separation absent")
    return rows


def report():
    rows=actual_original_W32_seven_proxy_report()
    return {
        "slice":"HYP105-ISSUE230-D6Z-ORIGINAL-INCIDENCE-WEDGE-MOMENT",
        "theorem":"ALL-H-EXACT-ORIGINAL-SIXSET-WEDGE-TRANSPORT",
        "original_point_and_line_typed_images":"BOTH-EXACT-ALL-H",
        "all_h_wedge_moment_envelope":"TWO-SIDED-SHARP",
        "global_image_only_determines_original_seven_GF5_S":False,
        "two_sided_physical_regular_proxy_sufficient_for_GF5_seven":False,
        "not_new_graph_extremal_theory":True,
        "not_universal_positive_GF5_bound":True,
        "Branch_A":"OPEN","Branch_B":"OPEN",
        "all_h_envelopes":[sharp_two_sided_wedge_moment_envelope(2**h)
                           for h in range(1,7)],
        "true_original_W32":rows,
    }


if __name__=="__main__":
    print(json.dumps(report(),sort_keys=True,default=list))
