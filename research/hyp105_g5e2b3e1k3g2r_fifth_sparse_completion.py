"""HYP-105 E1-K3-G2-R: sparse fifth Johnson harmonic and TRUE GQ-dual source.

ALL physical a>=6: a five-edge physical subset has a target six-edge
2-factor completion iff it is a simple P6 or disjoint C3+P3 on six
coordinates, with EXACTLY ONE completion. Together with prior exact
H0,H2,H3,H4 down-harmonics, this gives the unique H5(F), with
rank-five target squared energy evaluated using only TWO representatives:

    E5(a)=C(a,6)*(360*h5(P6)+60*h5(C3+P3)).

E6 is the exact Parseval residue. All seven target rank energies on
J(C(a,2),6) can thus be computed WITHOUT enumerating its 6-subsets.

Finite W32 independently cross-checks the complete 5005-element J15,6
rank5/6 target projections and the genuine ORIGINAL and DUAL GQ
anchor/permanent-1 and permanent-2 sixth-order weighted source splits.

This is not an all-label P2/P7 theorem or a universal charging proof.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import comb
import json

from hyp105_g5e2b3e1c0_weighted_overlap import simple_six_2factor_targets
from hyp105_g5e2b3e1k3g2n_johnson_harmonics import (
    target_low_harmonics,target_H2_value,physical_pair_indices,
    exact_target_johnson_decomposition,_frozen_target_W32,
    six_image_index,gq_pair_model,rat,
)
from hyp105_g5e2b3e1k3g2o_gq_third_coupling import (
    physical_triple_shape,target_rank3_orbits,
    target_H3_on_six,
)
from hyp105_g5e2b3e1k3g2p_fourth_geometry import (
    physical_four_shape,target_rank4_orbits,
    _target_rank4_on_six,
)
from hyp105_g5e2b3e1k3g2q_gq_anchor_permanents import (
    true_original_sixsource_permanents,
)
from hyp105_g5e2b3e1k3g2m_twofamily_falsifier import (
    dual_model,exact_two_family_point,_anchors,
)
from hyp105_g5e2b3e1k3g2h_exact_swap_shell import swapped_labeling


SIX_CYCLE=((0,1),(1,2),(2,3),(3,4),(4,5),(0,5))
TWO_TRIANGLES=((0,1),(0,2),(1,2),(3,4),(3,5),(4,5))
PATH_FIVE=tuple(e for e in SIX_CYCLE if e!=(0,5))
TRIANGLE_PATH=tuple(e for e in TWO_TRIANGLES if e!=(4,5))


def five_edge_completion(edges):
    """Independent physical 2-factor extension test on 5 canonical edges.

    Every accepted physical 2-factor has exactly six edges and exactly six
    nonisolated coordinates. Removing one edge from C6 or C3+C3 yields
    either P6 or C3+P3. A 5-edge set has at most one such completion.
    """
    E=tuple(tuple(e) for e in edges)
    if (len(E)!=5 or len(set(E))!=5 or any(
            len(e)!=2 or type(e[0]) is not int or
            type(e[1]) is not int or not 0<=e[0]<e[1] for e in E)):
        raise ValueError("five distinct canonical simple physical edges")
    vertices={u for e in E for u in e}
    if len(vertices)!=6:
        return ()
    deg={v:0 for v in vertices}
    neighbor={v:set() for v in vertices}
    for u,v in E:
        deg[u]+=1
        deg[v]+=1
        neighbor[u].add(v)
        neighbor[v].add(u)
    endpoints=tuple(v for v in sorted(vertices) if deg[v]==1)
    if len(endpoints)!=2 or sorted(deg.values())!=[1,1,2,2,2,2]:
        return ()
    u,v=endpoints
    missing=(u,v)
    if missing in E or (v,u) in E:
        return ()
    candidate=tuple(sorted(E+(missing,)))
    if all(deg[x]+int(x in (u,v))==2 for x in vertices):
        # Four internal degree-two vertices cannot have hidden loops; the
        # only possible resulting simple 2-regular graph has cycles >=3.
        return candidate
    raise AssertionError("physical target completion degree invariant")


def physical_five_harmonic(F, *, low,third,fourth):
    """All-a exact H5 coefficient of one physical five-edge subset."""
    E=tuple(tuple(e) for e in F)
    extension=five_edge_completion(E)
    K=low["K"]
    c5=int(bool(extension))
    H2=sum((
        low["h2_adj"] if set(x)&set(y) else low["h2_dis"]
        for x,y in combinations(E,2)),Fraction(0))
    H3=sum((third["h3"][physical_triple_shape(B)]
            for B in combinations(E,3)),Fraction(0))
    H4=sum((fourth["shapes"][str(physical_four_shape(B))]["h4"]
            for B in combinations(E,4)),Fraction(0))
    return Fraction(
        c5-low["density"]*(K-5)-(K-7)*H2-(K-8)*H3-(K-9)*H4,
        K-10)


@lru_cache(maxsize=12)
def target_rank5_and_rank6_energies(a):
    """ALL physical integer a>=6; only TWO 5-edge prototypes needed."""
    low=target_low_harmonics(a)
    third=target_rank3_orbits(a)
    fourth=target_rank4_orbits(a)
    path=physical_five_harmonic(PATH_FIVE,low=low,third=third,fourth=fourth)
    tri=physical_five_harmonic(TRIANGLE_PATH,low=low,third=third,fourth=fourth)
    if (five_edge_completion(PATH_FIVE)!=tuple(sorted(SIX_CYCLE)) or
            five_edge_completion(TRIANGLE_PATH)!=tuple(sorted(TWO_TRIANGLES))):
        raise AssertionError("two sparse physical target extensions mismatch")
    E5=comb(a,6)*(360*path+60*tri)
    E6=fourth["E_ge5"]-E5
    if E5<0 or E6<0:
        raise AssertionError("fifth/sixth Johnson target energy negative")
    full=(low["E0"],low["E1"],low["E2"],third["E3"],
          fourth["E4"],E5,E6)
    if sum(full,Fraction(0))!=low["target_count"]:
        raise AssertionError("exact ALL-a seven-level Parseval mismatch")
    return {
        "a":a,"K":low["K"],"E0_to_E6":full,
        "h5_path_P6":path,"h5_C3_plus_P3":tri,
        "physical_five_nonzero_completion_types":2,
        "physical_target_ranks_zero_to_six_closed_all_a":True,
    }


def rank5_lift_on_six(S, physical_edges,*,low,third,fourth):
    if len(S)!=6 or len(set(S))!=6 or any(
            type(i) is not int or not 0<=i<len(physical_edges) for i in S):
        raise ValueError("six distinct valid physical pair edges")
    return sum((physical_five_harmonic(
        tuple(physical_edges[i] for i in F),
        low=low,third=third,fourth=fourth)
        for F in combinations(S,5)),Fraction(0))


def direct_target_rank6_residual(S, physical_edges,*,low,third,fourth,targets):
    """Rank6 target from *independent* ORIGINAL 2-factor membership and H0..5."""
    labelset=frozenset(physical_edges[i] for i in S)
    known=(
        low["density"]+
        target_H2_value(S,physical_edges,low)+
        target_H3_on_six(S,physical_edges,third["h3"])+
        _target_rank4_on_six(S,physical_edges,fourth)+
        rank5_lift_on_six(S,physical_edges,
                          low=low,third=third,fourth=fourth))
    return Fraction(int(labelset in targets))-known


@lru_cache(maxsize=1)
def _W32_rank56():
    low=target_low_harmonics(6)
    third=target_rank3_orbits(6)
    fourth=target_rank4_orbits(6)
    physical=tuple(combinations(range(6),2))
    targets=simple_six_2factor_targets(6)
    indices,components,energies=_frozen_target_W32()
    ranks5=[]
    ranks6=[]
    for S in indices:
        h5=rank5_lift_on_six(S,physical,
                   low=low,third=third,fourth=fourth)
        h6=direct_target_rank6_residual(S,physical,
                   low=low,third=third,fourth=fourth,targets=targets)
        idx=indices[S]
        if h5!=components[5][idx] or h6!=components[6][idx]:
            raise AssertionError("H5/H6 independent physical rank mismatch")
        ranks5.append(h5)
        ranks6.append(h6)
    expected=target_rank5_and_rank6_energies(6)["E0_to_E6"]
    if expected!=energies:
        raise AssertionError("entire ALL-a rank energies differ from N K6")
    return indices,tuple(ranks5),tuple(ranks6)


def permanent_witness_fifth_sixth_split(model,ledger):
    """W32 2x2 signed rank 5/6 by genuine ORIGINAL perm 1/2 witnesses."""
    weights=ledger["weights"]
    one=ledger["permanent_one_counts"]
    two=ledger["permanent_two_counts"]
    indices,h5,h6=_W32_rank56()
    palette=physical_pair_indices(6)
    slots=[[Fraction(0),Fraction(0)],[Fraction(0),Fraction(0)]]
    mass=[0,0]
    for R,w in weights.items():
        idx=indices[six_image_index(R,model["right_labels"],palette)]
        n1,n2=one[R],two[R]
        if w!=n1+2*n2:
            raise AssertionError("true original anchor witness multiplicity changed")
        vals=(h5[idx],h6[idx])
        for rank,value in enumerate(vals):
            slots[0][rank]+=n1*value
            slots[1][rank]+=2*n2*value
        mass[0]+=n1
        mass[1]+=2*n2
    if sum(mass)!=sum(weights.values()):
        raise AssertionError("original W32 source mass was not conserved")
    # Independent exact J15,6 target projections with ALL original C0 weights.
    _,components,_=_frozen_target_W32()
    signed=[Fraction(0),Fraction(0)]
    for R,w in weights.items():
        idx=indices[six_image_index(R,model["right_labels"],palette)]
        signed[0]+=w*components[5][idx]
        signed[1]+=w*components[6][idx]
    if [sum(row[j] for row in slots) for j in range(2)]!=signed:
        raise AssertionError("true source rank5/6 independent spectrum mismatch")
    return {
        "permanent_one_two_source_masses":mass,
        "rows_permanent_one_two_columns_rank5_rank6":[
            [rat(x) for x in row] for row in slots],
        "signed_C5":rat(signed[0]),"signed_C6":rat(signed[1]),
        "signed_C56":rat(sum(signed)),
        "source_mass":sum(weights.values()),
    }


def report():
    all_a={str(a):{
        "a":a,
        "h5_path_P6":rat(target_rank5_and_rank6_energies(a)["h5_path_P6"]),
        "h5_C3_plus_P3":rat(target_rank5_and_rank6_energies(a)["h5_C3_plus_P3"]),
        "E0_to_E6":[rat(x) for x in
            target_rank5_and_rank6_energies(a)["E0_to_E6"]],
    } for a in (6,9,14)}
    models=[]
    for name,model in (
        ("lex",gq_pair_model(1,"lex")),
        ("hardest-M",swapped_labeling(_anchors()[0][1],"left",13,14)),
    ):
        point=exact_two_family_point(model)
        BA=true_original_sixsource_permanents(model)
        dual=dual_model(model)
        AB=true_original_sixsource_permanents(dual)
        left=permanent_witness_fifth_sixth_split(model,BA)
        right=permanent_witness_fifth_sixth_split(dual,AB)
        if (point["U_BA"],point["U_AB"]) != (
            sum(BA["weights"][R] for R in BA["weights"]
                if frozenset(model["right_labels"][v] for v in R) in
                    simple_six_2factor_targets(6)),
            sum(AB["weights"][R] for R in AB["weights"]
                if frozenset(dual["right_labels"][v] for v in R) in
                    simple_six_2factor_targets(6))):
            raise AssertionError("independent original/dual physical target discrepancy")
        models.append({
            "name":name,"U_BA":point["U_BA"],"U_AB":point["U_AB"],
            "S_seven":point["S_seven"],"P2_margin":point["two_family_minus_mu"],
            "original_BA":left,"genuine_original_dual_AB":right,
            "joint_C5":rat(Fraction(*left["signed_C5"])+Fraction(*right["signed_C5"])),
            "joint_C6":rat(Fraction(*left["signed_C6"])+Fraction(*right["signed_C6"])),
        })
    return {
        "slice":"HYP-105-E1-K3-G2-R",
        "physical_complete_all_a_rank0_to6":all_a,
        "genuine_original_and_dual_GQ_models":models,
        "all_a_sparse_unique_fifth_completion_theorem":True,
        "all_h_two_family_P2_proved":False,
        "all_h_seven_family_P7_proved":False,
        "branch_A_B":"OPEN",
    }


if __name__=="__main__":
    print(json.dumps(report(),sort_keys=True,indent=2))
