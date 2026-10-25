"""HYP-105 #230 / D6-AA4-AC: genuine-root B/A tensor gap and TWO-anchor orbit sectors.

All-h (h>=1) restricted deterministic mathematics, no adversarial
Omega(s**6) claim:
 (1) independently normalize TWO distinct point-source pair labels and
     TWO distinct line-source pair labels, preserving each historical GF5
     tag, the same-Q connected D6 and fixed weighted GF5 numerator;
 (2) the second anchor has exactly TWO physical adjacency orbits;
     four independently anchored two-side sectors exhaust all maps;
 (3) on each actual ORIGINAL B/A (resp A/B) six-incidence forest and
     each ORIGINAL repeated point (resp line) root, the exact accepted
     positive GF5 count equals (left_size+right_size-Hamming_gap)/2.

The h=1 oracle produces TRUE full global per-root sparse incidence
vectors, not independently sampled Q maps or an abstract matching
relaxation. True all-h GQ source counts are separate closed inputs.
"""
from collections import Counter
from itertools import combinations
from math import prod

from hyp105_issue230_d6aa4ab_minimax_orbit_normalform import (
    _valid_original_model, transform_model, local_original_seven_tag,
)
from hyp105_issue230_d6aa4q_two_sided_seven_join import (
    exact_ONE_side_original_projection_index,
    exact_two_sided_original_seven_join,
)
from hyp105_issue230_d6aa4u_source_forest_frechet import (
    original_sixset_source_cell,
)
from hyp105_issue230_d6aa4aa_original_full_forest_closure import (
    exact_all_h_nine_source_forest_universes,
)
from hyp105_g5e2b3e1b0_seven_signature import R3_CERTIFIED_FLOORS


def _pair(edge,a):
    value=tuple(edge)
    if value not in set(combinations(range(a),2)):
        raise ValueError("requires canonical unordered physical edge")
    return value


def two_edge_physical_orbit(first,second,a):
    e0,e1=_pair(first,a),_pair(second,a)
    if e0==e1:
        raise ValueError("global physical injectivity prohibits duplicate edge images")
    common=set(e0)&set(e1)
    if len(common)==1:
        return "adjacent"
    if not common:
        return "disjoint"
    raise AssertionError("two different simple physical edges only meet in 0 or 1 coordinate")


def normalize_two_physical_edges(first,second,a):
    """Explicit permutation of [a] mapping an ordered edge pair into
    (01,02) (adjacent) or (01,23) (disjoint). This is a joint
    permutation of ALL source physical labels on ONE typed side.
    """
    e0,e1=_pair(first,a),_pair(second,a)
    relation=two_edge_physical_orbit(e0,e1,a)
    mapping=[None]*a
    if relation=="adjacent":
        shared=next(iter(set(e0)&set(e1)))
        other0=next(x for x in e0 if x!=shared)
        other1=next(x for x in e1 if x!=shared)
        roots=((shared,0),(other0,1),(other1,2))
    else:
        roots=((e0[0],0),(e0[1],1),(e1[0],2),(e1[1],3))
    for old,new in roots:
        mapping[old]=new
    occupied=set(mapping)-{None}
    missing_old=(x for x in range(a) if mapping[x] is None)
    missing_new=(x for x in range(a) if x not in occupied)
    for old,new in zip(missing_old,missing_new):
        mapping[old]=new
    if set(mapping)!=set(range(a)):
        raise AssertionError("two-edge physical normal-form relabel must be bijective")
    canonical=tuple(sorted((mapping[e1[0]],mapping[e1[1]])))
    assert tuple(sorted((mapping[e0[0]],mapping[e0[1]])))==(0,1)
    assert canonical==(0,2) if relation=="adjacent" else canonical==(2,3)
    return {"relation":relation, "permutation":tuple(mapping),
            "first_canonical":(0,1),"second_canonical":canonical}


def normalize_two_anchors(model,point_sources=(0,1),line_sources=(0,1)):
    """No loss of ANY minimizer; four two-side canonical edge-orbit sectors."""
    v,a,_=_valid_original_model(model)
    if any(len(x)!=2 or len(set(x))!=2 or
           any(type(i) is not int or not 0<=i<v for i in x)
           for x in (point_sources,line_sources)):
        raise ValueError("two distinct ORIGINAL source factors per typed side required")
    P=normalize_two_physical_edges(
        model["left_labels"][point_sources[0]],
        model["left_labels"][point_sources[1]],a)
    L=normalize_two_physical_edges(
        model["right_labels"][line_sources[0]],
        model["right_labels"][line_sources[1]],a)
    candidate=transform_model(model,point_coordinates=P["permutation"],
                             line_coordinates=L["permutation"])
    for key,sources,reference in (("left_labels",point_sources,P),
                                  ("right_labels",line_sources,L)):
        assert candidate[key][sources[0]]==(0,1)
        assert candidate[key][sources[1]]==reference["second_canonical"]
    return {"model":candidate,"point_orbit":P["relation"],
            "line_orbit":L["relation"],"point_source_anchors":tuple(point_sources),
            "line_source_anchors":tuple(line_sources),
            "root_230_all_h_lower_PROVED":False}


def _falling(n,k):
    if k<0 or n<k:
        raise ValueError("invalid falling factorial")
    return prod(range(n-k+1,n+1))


def all_h_second_anchor_sectors(s):
    """EXACT count of canonical assignments, not quotient by stabilizer."""
    from hyp105_issue230_proof_audit import parameters
    par=parameters(s)
    a,K,V=par["a"],par["K"],par["V"]
    A,D=2*(a-2),(a-2)*(a-3)//2
    if 1+A+D != K:
        raise AssertionError("ordered-edge orbit two adjacency counts must exhaust K-1")
    per=_falling(K-2,V-2)
    individual=per**2
    unanchored=_falling(K,V)**2
    if unanchored!=(K*(K-1))**2*individual:
        raise AssertionError("four-sector exact original assignment count drift")
    sectors={"point_"+p+"__line_"+q:individual
             for p in ("adjacent","disjoint") for q in ("adjacent","disjoint")}
    return {
        "s":s,"V":V,"a":a,"K":K,
        "possible_ordered_second_physical_edges_adjacent":A,
        "possible_ordered_second_physical_edges_disjoint":D,
        "unanchored_global_two_map_assignments":unanchored,
        "per_canonical_orbit_sector_assignments":individual,
        "four_canonical_sector_assignments_total":4*individual,
        "exact_search_assignment_reduction_factor":(K*(K-1))**2//4,
        "reduction_factor_exact_fraction":
            f"{(K*(K-1))**2}/4",
        "sector_cardinalities":sectors,
        "not_a_full_automorphism_stabilizer_quotient":True,
        "all_h_universal_adversarial_lower_PROVED":False,
    }


def all_h_repeated_source_root_universe(s):
    """Source-only true GQ capacities, NOT physical motif memberships."""
    src=exact_all_h_nine_source_forest_universes(s)
    V=src["V"]
    n=src["all_nine_original_source_forest_cell_populations"]
    if n["A/B"]!=n["B/A"] or n["B/A"]%V:
        raise AssertionError("true-GQ dual root transitivity/cell count invalid")
    return {
        "s":s,"V":V,
        "original_source_B/A_Q_per_repeated_point_root":n["B/A"]//V,
        "original_source_A/B_Q_per_repeated_line_root":n["A/B"]//V,
        "source_B/A_total":n["B/A"],
        "source_A/B_total":n["A/B"],
        "no_physical_f_g_conditions_in_SOURCE_reservoir":True,
    }


def _root_of(Q,inc,side):
    c=Counter(inc[i][side] for i in Q)
    roots=[k for k,n in c.items() if n==2]
    if len(roots)!=1:
        raise AssertionError("B/A source requires one uniquely repeated ORIGINAL root")
    return roots[0]


def true_W32_root_gap_certificate(model, *, independent_join=True):
    """Full ORIGINAL W32 root-resolved same-six-ID deterministic tensor.

    On original U_p^{BA}, define x_{p,Q}=1 when point half physical B,
    y_{p,Q}=1 when line half physical A, using ONE global pair map each.
    b_p=|x|, a_p=|y|, d_p=|x symmetric_difference y|;
    2|x intersect y|=b_p+a_p-d_p. Dual for A/B line roots.
    """
    inc,point,line=None,None,None
    v,a,_=_valid_original_model(model)
    if v!=15 or a!=6:
        raise ValueError("complete true original W32 root oracle only")
    inc=tuple(model["incidences"])
    point_half=exact_ONE_side_original_projection_index(model,0)[
        "candidate_sixset_map"]
    line_half=exact_ONE_side_original_projection_index(model,1)[
        "candidate_sixset_map"]
    # Each original source-cell root index is unique. Keep half supports
    # independently assembled rather than joining first and hiding mismatch.
    point_BA=[set() for _ in range(v)]
    line_BA=[set() for _ in range(v)]
    point_AB=[set() for _ in range(v)]
    line_AB=[set() for _ in range(v)]
    for Q,kind in point_half.items():
        cell=original_sixset_source_cell(Q,inc)
        if cell=="B/A":
            if kind!="B":raise AssertionError("point B physical profile drift")
            point_BA[_root_of(Q,inc,0)].add(Q)
        elif cell=="A/B":
            if kind!="A":raise AssertionError("point A physical profile drift")
            point_AB[_root_of(Q,inc,1)].add(Q)
    for Q,kind in line_half.items():
        cell=original_sixset_source_cell(Q,inc)
        if cell=="B/A":
            if kind!="A":raise AssertionError("line A physical profile drift")
            line_BA[_root_of(Q,inc,0)].add(Q)
        elif cell=="A/B":
            if kind!="B":raise AssertionError("line B physical profile drift")
            line_AB[_root_of(Q,inc,1)].add(Q)
    reservoir=all_h_repeated_source_root_universe(2)
    U=reservoir["original_source_B/A_Q_per_repeated_point_root"]
    if U!=111132:
        raise AssertionError("true original W32 B/A source root reservoir drift")
    root_rows={}
    for tag,X,Y in (("B-left/A-right",point_BA,line_BA),
                    ("A-left/B-right",point_AB,line_AB)):
        rooted=[]
        for i in range(v):
            b=len(X[i]);a=len(Y[i]);joint=len(X[i]&Y[i])
            gap=len(X[i]^Y[i])
            if not (0<=joint<=min(a,b)<=U):
                raise AssertionError("root physical acceptance outside true source reservoir")
            if b+a-gap!=2*joint:
                raise AssertionError("exact SAME original Q rooted Hamming identity failed")
            frechet=max(0,b+a-U)
            if joint<frechet:
                raise AssertionError("exact original rooted Fréchet lower violated")
            rooted.append({
                "source_root_id":i,"first_side_half_support":b,
                "second_side_half_support":a,
                "joint_original_SIX_Q_positive":joint,
                "symmetric_difference_gap":gap,
                "source_only_root_reservoir":U,
                "root_Frechet_lower":frechet,
                "root_coupled_overlap_excess_above_Frechet":joint-frechet,
            })
        root_rows[tag]=rooted
    jointBA=sum(q["joint_original_SIX_Q_positive"]
                for q in root_rows["B-left/A-right"])
    jointAB=sum(q["joint_original_SIX_Q_positive"]
                for q in root_rows["A-left/B-right"])
    weighted=R3_CERTIFIED_FLOORS["B-left/A-right"]*jointBA+R3_CERTIFIED_FLOORS["A-left/B-right"]*jointAB
    if independent_join:
        other=exact_two_sided_original_seven_join(
            model,independent_history=True)
        if jointBA!=other["accepted_seven_GF5_original_Q_by_tag"]["B-left/A-right"]:
            raise AssertionError("full historical independent B/A original join disagreement")
        if jointAB!=other["accepted_seven_GF5_original_Q_by_tag"]["A-left/B-right"]:
            raise AssertionError("full historical independent A/B original join disagreement")
        if weighted>other["selected_GF5_51palette_certified_numerator"]:
            raise AssertionError("positive historical B/A-only weighted lower exceeded full")
    return {
        "s":2,"V":v,"actual_original_incidence_ids":len(inc),
        "global_point_and_line_complete_injections":True,
        "all_62370_physical_six_Q_candidates_enumerated_per_typed_side":True,
        "true_original_root_source_universe":U,
        "root_rows_by_GF5_tag":root_rows,
        "accepted_original_B_left_A_right":jointBA,
        "accepted_original_A_left_B_right":jointAB,
        "accepted_two_BA_AB_classes":jointBA+jointAB,
        "B/A_A/B_selected_51palette_certified_numerator":weighted,
        "root_stratified_full_original_Q_Hamming_polarization_exact":True,
        "rank_only_or_marginal_only_positive_lower_PROVED":False,
        "universal_BA_AB_Omega_s6_PROVED":False,
    }


def root_gap_hamming_theorem(s):
    """Proof metadata; universal formula itself holds for every admissible h.

    All original repeated roots partition source B/A or A/B universes
    disjointly, so sum of exact per-root symmetric differences gives
    an IF AND ONLY IF condition on the BA+AB positive motif count.
    """
    from hyp105_issue230_proof_audit import parameters
    p=parameters(s)
    return {
        "s":s,"V":p["V"],"original_source_W3s_required":True,
        "for_each_complete_global_pair_map_f_g":True,
        "B/A_per_root_identity":"2J_p=b_p+a_p-|B_p(f) symmetric_difference A_p(g)|",
        "A/B_dual_root_identity":"2J_l=a_l+b_l-|A_l(f) symmetric_difference B_l(g)|",
        "BA_plus_AB_exact_root_global_identity":True,
        "omega_s6_equivalent_to_uniform_rooted_Hamming_deficit_bound_FOR_BA_AB_ONLY":True,
        "full_seven_positive_S_lower_NOT_PROVED":True,
    }


if __name__=="__main__":
    import json
    from hyp105_issue230_projection import fixture
    a=all_h_second_anchor_sectors(2)
    b=true_W32_root_gap_certificate(fixture(1,"S68"))
    print(json.dumps({"sector":a,
                      "B/A":b["accepted_original_B_left_A_right"],
                      "A/B":b["accepted_original_A_left_B_right"],
                      "sum":b["accepted_two_BA_AB_classes"]},
                     indent=2,sort_keys=True))
