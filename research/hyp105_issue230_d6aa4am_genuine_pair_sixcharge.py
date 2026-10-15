"""HYP-105 #230 AA4-AM: actual-original TWO-FLAG-to-SEVEN-GF5 sixset charge.

For every genuine original W(3,2^h), every full globally injective
typed f,g and every accepted ORIGINAL distinct six-incidence-ID Q from
the seven selected positive GF5 classes, let k(Q) count unordered pairs
of its genuine flags (p,l),(q,m) with p!=q, l!=m and BOTH physical
source pair labels f(p),f(q) and g(l),g(m) sharing a coordinate. These
are the ACTUAL D pairs proven plentiful in AA4-AL.

All-h exact structural channel bounds:
  physical source projection A => at most 6 eligible pairs
  physical source projection B => at most 4 eligible pairs
  physical source projection C => exactly 0 eligible pairs.
Hence selected tag:
  D6: k=6 (the two physical 6-cycles on the SIX Q flags align);
  B/A, A/B, B/B: 0<=k<=4;
  C/A, C/B: k=0.
No per-Q physical mapping resampling or fake source forest.

For any fixed globally injected f,g, define
  E = sum_{selected Q} k(Q) = sum_{D-pairs e} deg_seven(e);
  U = #{selected Q: k(Q)=0};
  S = total #selected seven-class genuine six-Q.
Then U+E/6<=S<=U+E, and S=Omega(s^6) iff U+E=Omega(s^6)
(up to factor SIX, for ALL global maps). The equivalence by itself
is only a rigorous EXTENSION/CHARGING REFORMULATION, NOT a proof of
either lower and not a claim that U=0. In fact the C/* GF5 classes
always contribute to U, and actual D pairs can be uncovered.

Only true finite ORIGINAL W32 exhaustive septuple oracle is run here
for the numerical profile. No all-h finite GQ materialization.
"""
from collections import Counter,defaultdict
from fractions import Fraction
from itertools import combinations

from hyp105_issue230_d6aa4al_global_original_coordinate_transport import (
    _actual_strict_original_transport,exact_original_global_transport)
from hyp105_g5e2b3e1b0_seven_signature import R3_CERTIFIED_FLOORS,seven_census


_CAP={"D6":6,"B-left/A-right":4,"A-left/B-right":4,
      "C/A":0,"C/B":0,"B/B-overlap":4,"B/B-disjoint":4}
_KIND_COUNTS={"A":(1,1,1,1,1,1),"B":(1,1,1,1,2),"C":(2,2,2)}


def _different_true_flag_physically_bilateral(e0,e1,inc,left,right):
    p,l=inc[e0]
    q,m=inc[e1]
    return (p!=q and l!=m and
            bool(set(left[p])&set(left[q])) and
            bool(set(right[l])&set(right[m])))


def original_D_pair_index(model):
    """Every genuine source-flag compatible pair, no transport tensor."""
    s,V,d,a,left,right,inc,np,nl=_actual_strict_original_transport(model)
    D=set()
    for i in range(len(inc)):
        for j in range(i+1,len(inc)):
            if _different_true_flag_physically_bilateral(i,j,inc,left,right):
                D.add((i,j))
    return frozenset(D)


def six_Q_anchored_D_pairs(Q,inc,left,right):
    """Genuine original 6-ID Q -> compatible unordered D pairs."""
    Q=tuple(sorted(Q))
    if len(Q)!=6 or len(set(Q))!=6 or any(i<0 or i>=len(inc) for i in Q):
        raise ValueError("six DIFFERENT actual original incidence IDs required")
    return frozenset((i,j) for i,j in combinations(Q,2)
                     if _different_true_flag_physically_bilateral(
                         i,j,inc,left,right))


def _projection_source_type(Q,inc,side):
    # Source factor multiplicities ALONE, independent of physical
    # source A/B/C under already selected complete GF5 6-coordinate Q.
    counts=tuple(sorted(Counter(inc[i][side] for i in Q).values()))
    for kind,expected in _KIND_COUNTS.items():
        if counts==expected:
            return kind
    raise AssertionError("selected six original source flags have invalid source partition")


def all_h_seven_class_anchor_capacity():
    """Universal sharp STRUCTURAL upper, no finite model or GF5 lower."""
    return {
        "accepted_true_original_seven_GF5_tag_max_D_two_flag_anchors":dict(_CAP),
        "physical_A_source_projection_distinct_pair_capacity":6,
        "physical_B_source_projection_distinct_pair_capacity":4,
        "physical_C_source_projection_distinct_pair_capacity":0,
        "true_original_D6_Q_anchors_EXACT":6,
        "true_original_C_A_C_B_selected_Q_anchors_EXACT":0,
        "double_counted_original_extension_E_upper_per_Q":6,
        "all_complete_global_label_maps_all_h_structural_theorem":True,
        "seven_class_S_omega_s6_NOT_PROVED":True
    }


def exact_W32_original_seven_pair_extension_certificate(model,
                                                        *,independent_oracle=False):
    """Complete 7-class original sixset × actual ORIGINAL D-pair incidence.

    W32 finite ONLY. One fully fixed globally complete source f,g pair.
    Exact E, U, coverage / uncovered, pair degrees and per-tag channels.
    Independent historical 62,370-six-Q and separate half-join oracles
    optionally enforce identical selected actual ORIGINAL six-ID Q.
    """
    s,V,d,a,left,right,inc,np,nl=_actual_strict_original_transport(model)
    if (s,V,a,len(inc))!=(2,15,6,45):
        raise ValueError("true original W(3,2) K6 ONLY for finite exhaustive join")
    selected=seven_census(model,independent_checks=False,witness_sets=True)
    tags=selected["sets"]
    if not tags or len(tags)!=selected["S_seven"]:
        raise AssertionError("historical genuine original selected Q tags invalid")
    if independent_oracle:
        from hyp105_issue230_d6aa4q_two_sided_seven_join import (
            exact_two_sided_original_seven_join)
        other=exact_two_sided_original_seven_join(
            model,independent_history=True,collect=True)
        if tags!=other["selected_ORIGINAL_Q_tags"]:
            raise AssertionError("two independent original seven-Q joins disagree")
    D=original_D_pair_index(model)
    al=exact_original_global_transport(model)
    if len(D)!=al[
        "exact_UNORDERED_DISTINCT_source_flag_pair_bilateral_physical_collision"]:
        raise AssertionError("source-first genuine pair oracle mismatches AL transport")
    anchor_degree=Counter()
    Q_k=Counter()
    tag_s=Counter()
    tag_e=Counter()
    tag_anchored=Counter()
    tag_unanchored=Counter()
    witness_unanchored={}
    witness_positive={}
    for Q,tag in tags.items():
        if tag not in _CAP:
            raise AssertionError("unrecognized genuine seven-GF5 Q class")
        kset=six_Q_anchored_D_pairs(Q,inc,left,right)
        k=len(kset)
        Q_k[k]+=1
        tag_s[tag]+=1
        tag_e[tag]+=k
        if k:
            tag_anchored[tag]+=1
            witness_positive.setdefault(tag,tuple(sorted(Q)))
        else:
            tag_unanchored[tag]+=1
            witness_unanchored.setdefault(tag,tuple(sorted(Q)))
        if k>_CAP[tag]:
            raise AssertionError("all-h pair capacity structural theorem violated")
        L=_projection_source_type(Q,inc,0)
        R=_projection_source_type(Q,inc,1)
        if (L=="C" or R=="C") and k:
            raise AssertionError("C physical source projection cannot anchor D pair")
        if tag=="D6" and (k!=6 or L!="A" or R!="A"):
            raise AssertionError("aligned original D6 six-cycle has six D anchors")
        for e in kset:
            if e not in D:
                raise AssertionError("false pair original source/physical indexing")
            anchor_degree[e]+=1
    E=sum(tag_e.values())
    S=selected["S_seven"]
    U=sum(tag_unanchored.values())
    covered=len(anchor_degree)
    uncovered=len(D)-covered
    if (sum(Q_k.values())!=S or
        E!=sum(anchor_degree.values()) or
        S!=U+sum(tag_anchored.values()) or
        E>6*(S-U) or
        E<S-U or
        E>6*S or
        not Fraction(E,6)+U<=S<=E+U or
        uncovered<0):
        raise AssertionError("exact original D-pair to seven-GF5 double counting identity")
    for tag in _CAP:
        if tag_s[tag]!=tag_anchored[tag]+tag_unanchored[tag]:
            raise AssertionError("tag decomposition")
    return {
        "s":s,"V":V,"a":a,
        "D_unordered_actual_original_bilateral_two_flag_pairs":len(D),
        "S_selected_original_seven_GF5_sixsets":S,
        "E_original_extension_incidences":E,
        "U_selected_sixsets_with_ZERO_original_D_pair_anchors":U,
        "S_with_positive_D_anchor":S-U,
        "D_covered_by_at_least_one_selected_original_six_Q":covered,
        "D_UNCOVERED_by_ALL_SEVEN_selected_six_Q":uncovered,
        "D_coverage_fraction":Fraction(covered,len(D)),
        "mean_D_pair_selected_six_Q_extension_multiplicity":Fraction(E,len(D)),
        "mean_selected_six_Q_D_anchor_multiplicity":Fraction(E,S),
        "positive_extension_degree_histogram":dict(sorted(Counter(anchor_degree.values()).items())),
        "selected_six_Q_anchored_D_pair_histogram":dict(sorted(Q_k.items())),
        "seven_original_S_by_tag":dict((t,tag_s[t]) for t in _CAP),
        "seven_original_D_extension_E_by_tag":dict((t,tag_e[t]) for t in _CAP),
        "seven_original_zero_D_anchor_U_by_tag":dict((t,tag_unanchored[t]) for t in _CAP),
        "seven_original_positive_D_anchor_count_by_tag":dict((t,tag_anchored[t]) for t in _CAP),
        "sample_original_zero_D_anchor_six_Q_by_tag":witness_unanchored,
        "sample_original_positive_D_anchor_six_Q_by_tag":witness_positive,
        "sharp_all_h_E_over_S_upper":6,
        "exact_energy_anchor_sandwich_lower":Fraction(E,6)+U,
        "exact_energy_anchor_sandwich_upper":E+U,
        "E_plus_U_equivalent_to_S_with_factor_at_most_6":True,
        "D_pair_positive_fraction_not_assumed":True,
        "model_equivalent_charge_frontier_not_Branch_A_B":True,
        "independent_historical_and_two_sided_Q_oracle":
            "PASS" if independent_oracle else "NOT_RUN",
    }


def independent_W32_pair_anchor_referee(model,selected_seven):
    """Second finite algorithm: D-first original 45-flag pairs -> actual Q."""
    s,V,d,a,left,right,inc,np,nl=_actual_strict_original_transport(model)
    if s!=2 or V!=15 or a!=6:
        raise ValueError("finite true ORIGINAL W32 only")
    D=original_D_pair_index(model)
    E=0
    covered=0
    degrees={}
    for p in D:
        n=sum(int(p[0] in Q and p[1] in Q) for Q in selected_seven)
        degrees[p]=n
        E+=n
        covered+=int(n>0)
    return {"E_from_D_major_oracle":E,"covered_from_D_major_oracle":covered,
            "uncovered_from_D_major_oracle":len(D)-covered,
            "degree_histogram_from_D_major_oracle":
                dict(Counter(n for n in degrees.values() if n>0)),
            "all_global_original_incidence_flags_not_abstract_vertices":True}
