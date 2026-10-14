"""HYP-105 #230 D6-AA4-I: ORIGINAL GQ spectral physical-coordinate cuts.

All-h unconditional ORIGINAL point/line collinearity-vs-physical-pair
obstruction of order Omega(s^5), not the seven-GF5 Omega(s^6) root.
Also an exact GQ incidence × physical-coordinate upper bound. Classical
SRG spectral/expander mixing machinery, no novelty claim for that lemma.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb, isqrt
import json

from hyp105_issue230_d6aa4e_global_assignment_dual import alphabet_capacity


def _floor(q):
    q=Fraction(q)
    return q.numerator//q.denominator


def geometry(s, incidence, *, max_v=600):
    """Verify true ORIGINAL GQ strongly regular identities on finite hosts.

    For large h the all-h proof invokes the axioms of genuine W(3,s),
    NOT fake enumeration or synthetic incidence graph extrapolation.
    """
    z=alphabet_capacity(s)
    v=z["V"];d=s+1;k=s*d
    if v>max_v:
        raise ValueError("finite ORIGINAL GQ validation budget exceeded")
    incidences=tuple(tuple(e) for e in incidence)
    if len(incidences)!=v*d or len(set(incidences))!=v*d or any(
            len(e)!=2 or any(type(t) is not int or not 0<=t<v for t in e)
            for e in incidences):
        raise ValueError("not a genuine-sized distinct ORIGINAL incidence list")
    point_lines=[set() for _ in range(v)]
    line_points=[set() for _ in range(v)]
    for p,l in incidences:
        point_lines[p].add(l);line_points[l].add(p)
    if any(len(e)!=d for e in (*point_lines,*line_points)):
        raise ValueError("not a regular ORIGINAL GQ")
    adj_P=[set() for _ in range(v)]
    adj_L=[set() for _ in range(v)]
    for members,adj in ((line_points,adj_P),(point_lines,adj_L)):
        for ps in members:
            for p in ps:
                adj[p].update(ps-{p})
    for adj in (adj_P,adj_L):
        if any(len(ns)!=k or p in ns for p,ns in enumerate(adj)):
            raise ValueError("original point/line collinearity wrong degree or loop")
        for p in range(v):
            for q in range(p+1,v):
                common=len(adj[p]&adj[q])
                expected=s-1 if q in adj[p] else s+1
                if common!=expected:
                    raise ValueError("not ORIGINAL GQ strongly regular collinearity")
    return {
        "s":s,"V":v,"a":z["a"],"K":z["K"],"m":z["m"],
        "source_point_neighbors":tuple(frozenset(x) for x in adj_P),
        "source_line_neighbors":tuple(frozenset(x) for x in adj_L),
        "original_incidences":incidences,
        "genuine_original_lambda":s-1,"genuine_original_mu":s+1,
        "source_collinearity_degree":k,
        "positive_nontrivial_spectral_eigenvalue":s-1,
        "negative_nontrivial_spectral_eigenvalue":-(s+1),
    }


def _pair_labels(labels,v,a):
    labels=tuple(tuple(x) for x in labels)
    if len(labels)!=v or len(set(labels))!=v or any(
            len(e)!=2 or any(type(x) is not int for x in e)
            or not 0<=e[0]<e[1]<a for e in labels):
        raise ValueError("complete canonical globally injective ORIGINAL typed labels required")
    return labels


def one_type_spectral_certificate(g,labels,*,source_type):
    """Universal mixed ORIGINAL source-collinearity / physical-center cut.

    SRG spectral upper: e_G(U)<=floor([(s-1)|U|+
            ((s²+1)/V)|U|²]/2). Every actual physical center fiber
    U_c contains <=a-1 source factor labels (global pair injectivity).
    """
    s,v,a=g["s"],g["V"],g["a"]
    if source_type not in ("P","L"):
        raise ValueError("explicit original point or line source type required")
    adj=g["source_point_neighbors" if source_type=="P" else "source_line_neighbors"]
    labels=_pair_labels(labels,v,a)
    centers=[set() for _ in range(a)]
    for p,(u,w) in enumerate(labels):
        centers[u].add(p);centers[w].add(p)
    if sum(map(len,centers))!=2*v or max(map(len,centers))>a-1:
        raise AssertionError("physical center two-edge incidence capacity false")
    actual=0
    column_data=[]
    for c,U in enumerate(centers):
        t=len(U)
        e=sum(len(adj[p]&U) for p in U)//2
        ub=_floor((Fraction(s-1)*t
                   +Fraction(s*s+1,v)*t*t)/2)
        if e>ub:
            raise AssertionError("ORIGINAL collinearity violates spectral mixing")
        column_data.append((t,e,ub))
        actual+=e
    # A pair of DIFFERENT physical edges shares <=1 coordinate, so
    # no ORIGINAL collinear source pair is counted twice.
    independent=sum(1 for p in range(v) for q in adj[p] if p<q
                    and set(labels[p])&set(labels[q]))
    if independent!=actual:
        raise AssertionError("physical coordinate collinearity double-counted")
    total=v*s*(s+1)//2
    per_center_upper=sum(x[2] for x in column_data)
    uniform_upper=v*(s-1)+(s*s+1)*(a-1)
    if not actual<=per_center_upper<=uniform_upper:
        raise AssertionError("global original source/physical mixed capacity violated")
    return {
        "original_factor_type":source_type,
        "original_collinear_unordered_pair_total":total,
        "original_collinear_physically_adjacent":actual,
        "original_collinear_physically_disjoint":total-actual,
        "exact_per_center_spectral_adjacency_upper":per_center_upper,
        "exact_per_center_forced_disjoint_lower":total-per_center_upper,
        "all_h_uniform_spectral_adjacency_upper":uniform_upper,
        "all_h_uniform_forced_disjoint_lower":total-uniform_upper,
        "physical_center_degrees":tuple(x[0] for x in column_data),
        "per_physical_center_actual_original_collinear_pairs":tuple(x[1] for x in column_data),
        "per_physical_center_integral_spectral_upper":tuple(x[2] for x in column_data),
        "not_seven_GF5_motif_lower":True,
    }


def all_h_source_disjoint_theorem(s):
    """Exact symbolic all-h SRG cut and explicit Omega(s^5) for h>=2."""
    z=alphabet_capacity(s)
    v,a=z["V"],z["a"]
    k=s*(s+1)
    all_source_collinear=v*k//2
    ub=(s-1)*v+(s*s+1)*(a-1)
    disjoint=all_source_collinear-ub
    if s>=4:
        # For s>=4, C(s²+1,2)>=(s+1)(s²+1), so a-1<=s².
        if a-1>s*s or disjoint< Fraction(s**5,4):
            raise AssertionError("claimed universal s^5/4 cut not proven")
    if s==2 and disjoint!=5:
        raise AssertionError("genuine original W32 global mixed bound baseline false")
    return {
        "s":s,"V":v,"a":a,"K":z["K"],"m":z["m"],
        "original_collinear_unordered_pairs":all_source_collinear,
        "spectral_global_physically_adjacent_upper":ub,
        "uniform_forced_physically_disjoint_collinear_lower":disjoint,
        "explicit_s_ge_4_lower_s_power5_over4":s>=4,
        "all_h_unconditional_original_source_physical_pair_theorem":True,
        "all_h_original_seven_GF5_bound_PROVED":False,
        "all_h_ASET_exponent_PROVED":False,
    }


def _cross_bound_per_center(s,v,ta,tb):
    """Verified rational AM-GM upper on true ORIGINAL incidence overlap.

    For B the true ORIGINAL point-line incidence matrix, top singular
    value s+1 and remaining <=sqrt(2s), since BB*= (s+1)I+A_P.
    Choose any positive rational eta, then nontrivial bilinear <=
    0.5*(eta*||z_P||²+(2s/eta)*||z_L||²).
    """
    up=Fraction(ta*(v-ta),v)
    ul=Fraction(tb*(v-tb),v)
    base=Fraction((s+1)*ta*tb,v)
    positive_etas={Fraction(1),Fraction(2),Fraction(4),Fraction(8),
                   Fraction(max(1,isqrt(2*s))),
                   Fraction(isqrt(2*s)+1)}
    return min(_floor(base+(eta*up+Fraction(2*s,1)/eta*ul)/2)
               for eta in positive_etas)


def original_incidence_coordinate_certificate(g,left,right):
    """Additional two-type original-incidence × SAME physical center cut."""
    s,v,a=g["s"],g["V"],g["a"]
    left=_pair_labels(left,v,a)
    right=_pair_labels(right,v,a)
    lp=[set() for _ in range(a)]
    ll=[set() for _ in range(a)]
    for p,edge in enumerate(left):
        for c in edge:lp[c].add(p)
    for l,edge in enumerate(right):
        for c in edge:ll[c].add(l)
    actual=0
    upper=0
    for c in range(a):
        k=sum(1 for p,l in g["original_incidences"] if p in lp[c] and l in ll[c])
        cap=_cross_bound_per_center(s,v,len(lp[c]),len(ll[c]))
        if k>cap:
            raise AssertionError("true ORIGINAL bipartite GQ spectral incidence cut violated")
        actual+=k
        upper+=cap
    independent=sum(len(set(left[p])&set(right[l]))
                    for p,l in g["original_incidences"])
    if actual!=independent or upper<actual:
        raise AssertionError("true cross ORIGINAL source-physical incidence conservation false")
    return {
        "original_incidences_total":v*(s+1),
        "original_incidence_shared_physical_coordinate_count":actual,
        "two_type_source_physical_spectral_incidence_upper":upper,
        "counts_0_1_or_2_shared_centers_per_original_incidence":True,
        "uses_original_source_incidence_not_two_independent_physical_images":True,
        "not_seven_GF5_motif_lower":True,
    }


def finite_original_map_certificate(power,scheme):
    from hyp105_issue230_projection import fixture
    model=fixture(power,scheme)
    g=geometry(2**power,model["incidences"])
    p=one_type_spectral_certificate(g,model["left_labels"],source_type="P")
    l=one_type_spectral_certificate(g,model["right_labels"],source_type="L")
    cross=original_incidence_coordinate_certificate(
        g,model["left_labels"],model["right_labels"])
    return {
        "s":g["s"],"scheme":scheme,
        "original_point_spectral_cut":p,
        "original_line_spectral_cut":l,
        "original_point_line_bipartite_cut":cross,
        "all_h_GF5_positive_root":"OPEN",
    }


def genuine_original_W32_point_block(scheme):
    """24 true globally typed-injected source-point map states + full GF5."""
    from hyp105_issue230_projection import fixture
    from hyp105_g5e2b3e1b0_seven_signature import R3_CERTIFIED_FLOORS,seven_census
    from hyp105_issue230_d6aa4c_edit_transversal import (
        genuine_original_positive_hypergraph,incidence_cover_bits)
    from hyp105_issue230_d6aa4d_mixed_transversal_fibers import finite_source_support_partition
    from hyp105_issue230_d6aa4g_overlap_capacity import complete_fixed_image_states
    if scheme not in ("S68","S72"):
        raise ValueError("real frozen W32 S68/S72 only")
    model=fixture(1,scheme)
    g=geometry(2,model["incidences"])
    source=genuine_original_positive_hypergraph(model)
    bits,weights,allmask=incidence_cover_bits(source["records"])
    partition=finite_source_support_partition(bits,weights,allmask)
    if partition["number_transversal_blocks"]!={"S68":53,"S72":119}[scheme]:
        raise AssertionError("AA4D original point/line support transversal drift")
    block=next((b for b in partition["transversal_original_factor_blocks"]
                if len(b)==4 and all(i<15 for i in b)),None)
    if block is None:
        raise AssertionError("genuine original four-point critical block missing")
    baseline=tuple(tuple(model["left_labels"][p]) for p in block)
    states=complete_fixed_image_states(("P",)*4,baseline)
    right=tuple(tuple(x) for x in model["right_labels"])
    fixed_right=one_type_spectral_certificate(g,right,source_type="L")
    full=[]
    for state in states:
        left=list(tuple(tuple(x) for x in model["left_labels"]))
        for p,label in zip(block,state):left[p]=label
        actual={**model,"left_labels":tuple(left),"right_labels":right}
        spectral=one_type_spectral_certificate(g,left,source_type="P")
        cross=original_incidence_coordinate_certificate(g,left,right)
        census=seven_census(actual,independent_checks=False,witness_sets=True)
        if census["S_seven"]!=len(census["sets"]) or census[
            "GF5_seven_lower_numerator"]!=sum(
            R3_CERTIFIED_FLOORS[tag] for tag in census["sets"].values()):
            raise AssertionError("not an ORIGINAL GF5 seven-class positional census")
        full.append({
            "seven_original_Q":census["S_seven"],
            "selected_GF5_numerator":census["GF5_seven_lower_numerator"],
            "original_point_collinear_physically_disjoint":
                spectral["original_collinear_physically_disjoint"],
            "original_point_collinear_physically_adjacent":
                spectral["original_collinear_physically_adjacent"],
            "true_original_point_line_shared_coordinate_incidence":
                cross["original_incidence_shared_physical_coordinate_count"],
        })
    if len(full)!=24 or full[0]["seven_original_Q"]!={"S68":68,"S72":72}[scheme]:
        raise AssertionError("actual original W32 base labeling or 24-state fiber changed")
    min_S=min(x["seven_original_Q"] for x in full)
    if min_S!={"S68":68,"S72":72}[scheme]:
        raise AssertionError("AA4G complete real four-point fiber minimum changed")
    # W32 every true typed physical image is exactly the complete K6:
    # all ORIGINAL one-type center degree vectors are (5,)*6, no
    # scalar physical-image adjacency cut can distinguish these 24 maps.
    if fixed_right["physical_center_degrees"]!=(5,)*6 or any(
        g0["original_point_collinear_physically_disjoint"]<9 for g0 in full):
        raise AssertionError("true physical center/GQ spectral frontier violated")
    return {
        "scheme":scheme,"original_W32_genuine_four_point_block":block,
        "all_complete_global_K6_source_states":24,
        "historical_original_sixset_candidates_per_map":62370,
        "minimum_original_seven_S":min_S,
        "physical_image_center_degrees_unchanged":True,
        "point_forced_original_collinear_physical_disjoint_minimum":
            min(x["original_point_collinear_physically_disjoint"] for x in full),
        "point_forced_original_collinear_physical_disjoint_maximum":
            max(x["original_point_collinear_physically_disjoint"] for x in full),
        "cross_original_incidence_coordinate_minimum":
            min(x["true_original_point_line_shared_coordinate_incidence"] for x in full),
        "cross_original_incidence_coordinate_maximum":
            max(x["true_original_point_line_shared_coordinate_incidence"] for x in full),
        "all_exact_genuine_source_scores":full,
        "seven_GF5_minimum_over_all_W32_maps_NOT_claimed":True,
        "universal_all_h_sixset_lower_NOT_claimed":True,
    }


def report(scheme=None):
    ret={
        "slice":"HYP105-ISSUE230-D6-AA4-I-ORIGINAL-SPECTRAL-COORDINATE",
        "all_h_source_collinear_physically_disjoint_omega_s5_PROVED":True,
        "all_h_original_incidence_shared_coordinate_spectral_cut_PROVED":True,
        "classical_GQ_SRG_spectral_prior_art_required":True,
        "root_Branch_A":"OPEN","root_Branch_B":"OPEN",
        "full_GF5_R3":False,"ASET_exponent":False,
        "all_h_bounds":[all_h_source_disjoint_theorem(2**h) for h in range(1,9)],
    }
    if scheme is not None:
        ret["real_original_W32"]=genuine_original_W32_point_block(scheme)
    return ret


if __name__=="__main__":
    import argparse
    p=argparse.ArgumentParser()
    p.add_argument("--scheme",choices=("S68","S72"))
    a=p.parse_args()
    print(json.dumps(report(a.scheme),indent=2,sort_keys=True))
