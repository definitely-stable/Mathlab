"""HYP-105 K3-G2-S: exact finite ORIGINAL/DUAL GQ incidence Hall charging.

For W(3,2) and a legal coherent global pair of injections (f,g), each
B/A six-incidence support has a unique repeated ORIGINAL point p.
The dual A/B support has a unique repeated ORIGINAL line l.

Demand: E[one B/A target hit] = rho * count(B/A supports at p).
Credit: each actual B/A target support at the SAME p has budget one;
each actual A/B dual target support at original line l has budget one.
B/A demand p may use A/B credit at l ONLY when p I l in ORIGINAL GQ.

This restricted transport is stronger than scalar P2. We independently
solve exact integer max-flow and enumerate ALL 2^15 Hall cuts. An
infeasible result refutes only this chosen incidence-local charging model.

No independence assumption, randomized labels, or all-h positive claim.
"""
from collections import deque
from fractions import Fraction
from itertools import combinations
from math import comb
import json

from hyp105_g5e2b3e1c0_weighted_overlap import simple_six_2factor_targets
from hyp105_g5e2b3e1k3g2n_johnson_harmonics import (
    _frozen_target_W32, physical_pair_indices, six_image_index,
    target_low_harmonics, gq_pair_model, rat,
)
from hyp105_g5e2b3e1k3g2q_gq_anchor_permanents import (
    true_original_sixsource_permanents, original_GQ_tables,
    physical_squares, _line_rows, permanent4,
)
from hyp105_g5e2b3e1k3g2m_twofamily_falsifier import (
    dual_model, exact_two_family_point, _anchors,
)
from hyp105_g5e2b3e1k3g2h_exact_swap_shell import swapped_labeling


def anchor_ledger(model, sixsource):
    """Recount genuine ORIGINAL permanents by their unique GQ repeated point.

    Uses true lines, points, physical squares, and 4x4 perfect matchings,
    independently of the source's aggregate anchor attribution.
    """
    if (model["s"],model["a"],model["v_left"],model["v_right"]) != (2,6,15,15):
        raise ValueError("this exact complete finite Hall gate is W32/K6 only")
    points, lines, anchors = original_GQ_tables(
        2, tuple(model["incidences"]))
    squares = physical_squares(model)
    indices, components, _ = _frozen_target_W32()
    palette = physical_pair_indices(6)
    targets = simple_six_2factor_targets(6)
    mass = [0]*15
    hits = [0]*15
    matching_one = [0]*15
    matching_two = [0]*15
    signed = [[Fraction(0) for _ in range(7)] for _ in range(15)]
    cache = {}
    for R, expected in sixsource["weights"].items():
        original = tuple(sorted(R))
        n1 = n2 = 0
        S = six_image_index(R, model["right_labels"], palette)
        index = indices[S]
        is_target = frozenset(model["right_labels"][l] for l in R) in targets
        for B in combinations(original,2):
            p = anchors.get(B)
            if p is None:
                continue
            others = tuple(l for l in original if l not in B)
            for Q in squares[p]:
                key = (others,Q)
                value = cache.get(key)
                if value is None:
                    value = permanent4(_line_rows(others,Q,lines))
                    cache[key] = value
                if value == 0:
                    continue
                n1 += int(value == 1)
                n2 += int(value == 2)
                matching_one[p] += int(value == 1)
                matching_two[p] += int(value == 2)
                mass[p] += value
                if is_target:
                    hits[p] += value
                for j in range(7):
                    signed[p][j] += value*components[j][index]
        if (n1, n2) != (
                sixsource["permanent_one_counts"][R],
                sixsource["permanent_two_counts"][R]):
            raise AssertionError("original anchor attribution disagrees with Q")
        if n1 + 2*n2 != expected:
            raise AssertionError("original distinct six-incidence support lost")
    total = sum(sixsource["weights"].values())
    if (sum(mass)!=total or
            sum(matching_one)+2*sum(matching_two)!=total):
        raise AssertionError("original anchor/permanent source mass not conserved")
    for p in range(15):
        if mass[p] != matching_one[p]+2*matching_two[p]:
            raise AssertionError("local original anchor conservation failed")
        if not 0<=hits[p]<=mass[p]:
            raise AssertionError("invalid original anchor physical target credit")
    if sum(sum(row[j] for row in signed) for j in range(7)) != sum(hits):
        raise AssertionError("complete seven-rank exact target/source overlap failed")
    return {
        "mass":mass,
        "hits":hits,
        "permanent_one":matching_one,
        "permanent_two":matching_two,
        "signed_by_anchor":signed,
        "original_point_lines":points,
        "source_mass":total,
        "target_hits":sum(hits),
    }


def exact_integer_maxflow(demand, own_credit, dual_credit, incidence):
    """Entirely integer capacity flow, with a residual minimum-cut witness."""
    if (len(demand)!=15 or len(own_credit)!=15 or
            len(dual_credit)!=15 or len(incidence)!=15 or
            any(type(x) is not int or x<0 for x in
                list(demand)+list(own_credit)+list(dual_credit))):
        raise ValueError("nonnegative integer W32 anchor capacities required")
    if any((not isinstance(row,(set,frozenset,tuple)) or
            any(type(l) is not int or not 0<=l<15 for l in row))
           for row in incidence):
        raise ValueError("actual 15x15 GQ incidence neighborhoods required")
    # 0=source, 1..15=demand points, 16..30=own B/A credits,
    # 31..45=original-dual A/B line credits, 46=sink.
    graph=[[] for _ in range(47)]
    def add(u,v,c):
        graph[u].append([v,len(graph[v]),c])
        graph[v].append([u,len(graph[u])-1,0])
    total=sum(demand)
    for p in range(15):
        add(0,1+p,demand[p])
        add(1+p,16+p,total)
        add(16+p,46,own_credit[p])
        for l in sorted(incidence[p]):
            add(1+p,31+l,total)
    for l in range(15):
        add(31+l,46,dual_credit[l])
    flow=0
    while True:
        prev=[None]*47
        prev[0]=(-1,-1)
        q=deque([0])
        while q and prev[46] is None:
            u=q.popleft()
            for i,(v,_,cap) in enumerate(graph[u]):
                if cap>0 and prev[v] is None:
                    prev[v]=(u,i)
                    q.append(v)
        if prev[46] is None:
            break
        aug=total-flow
        v=46
        while v:
            u,i=prev[v]
            aug=min(aug,graph[u][i][2])
            v=u
        v=46
        while v:
            u,i=prev[v]
            e=graph[u][i]
            e[2]-=aug
            graph[v][e[1]][2]+=aug
            v=u
        flow+=aug
    reachable={0}
    q=deque([0])
    while q:
        u=q.popleft()
        for v,_,cap in graph[u]:
            if cap>0 and v not in reachable:
                reachable.add(v)
                q.append(v)
    cut_points=tuple(p for p in range(15) if 1+p in reachable)
    neighbors=set().union(*(set(incidence[p]) for p in cut_points))
    cut_gap=(sum(demand[p] for p in cut_points)-
             sum(own_credit[p] for p in cut_points)-
             sum(dual_credit[l] for l in neighbors))
    if cut_gap!=total-flow:
        raise AssertionError("residual min cut does not equal exact deficit")
    return flow,cut_points,cut_gap


def exhaustive_hall_deficit(demand, own_credit, dual_credit, incidence):
    """Independent complete 32768-subset Hall inequality falsifier."""
    if any(len(x)!=15 for x in (demand,own_credit,dual_credit,incidence)):
        raise ValueError("complete W32 Hall enumeration requires 15 anchors")
    N=1<<15
    neighbors=[sum(1<<l for l in row) for row in incidence]
    dsum=[0]*N
    ownsum=[0]*N
    nbr=[0]*N
    max_deficit=0
    worst=0
    for mask in range(1,N):
        bit=mask & -mask
        p=bit.bit_length()-1
        rest=mask^bit
        dsum[mask]=dsum[rest]+demand[p]
        ownsum[mask]=ownsum[rest]+own_credit[p]
        nbr[mask]=nbr[rest]|neighbors[p]
        dualsum=sum(dual_credit[l] for l in range(15)
                    if nbr[mask] & (1<<l))
        gap=dsum[mask]-ownsum[mask]-dualsum
        if gap>max_deficit:
            max_deficit=gap
            worst=mask
    return max_deficit,tuple(p for p in range(15) if worst & (1<<p))


def incidence_charging_gate(original, dual, incidence, *, density):
    """Finite transport is a sufficient certificate for P2, not equivalent.

    Integer scaling by density.denominator makes every ORIGINAL source
    support's demand rho, every original/dual target's credit exactly one.
    A/B credits connect only to original B/A points on TRUE GQ incidences.
    """
    if not isinstance(density,Fraction) or not 0<density<1:
        raise ValueError("exact nontrivial physical target density required")
    numerator,denominator=density.numerator,density.denominator
    demand=[v*numerator for v in original["mass"]]
    own=[v*denominator for v in original["hits"]]
    other=[v*denominator for v in dual["hits"]]
    flow,cut,cut_gap=exact_integer_maxflow(demand,own,other,incidence)
    independently,other_cut=exhaustive_hall_deficit(demand,own,other,incidence)
    if cut_gap!=independently:
        raise AssertionError("exact max-flow/min-cut differs from full Hall census")
    scalar=sum(own)+sum(other)-sum(demand)
    if scalar != denominator*(original["target_hits"]+
                             dual["target_hits"]-
                             Fraction(original["source_mass"])*density):
        raise AssertionError("scalar P2 margin does not match flow capacity")
    if flow==sum(demand) and scalar<0:
        raise AssertionError("feasible nonnegative charging contradicts P2")
    return {
        "scaled_denominator":denominator,
        "density":rat(density),
        "actual_original_BA_anchor_demand":demand,
        "actual_original_BA_own_target_capacity":own,
        "actual_original_dual_AB_target_capacity":other,
        "original_GQ_incidence_edges":sum(len(x) for x in incidence),
        "exact_integer_maxflow":flow,
        "total_demand":sum(demand),
        "hall_shortfall":sum(demand)-flow,
        "full_hall_subsets_checked":1<<15,
        "independent_exhaustive_hall_max_deficit":independently,
        "min_cut_original_point_ids":list(cut),
        "independent_max_deficit_point_ids":list(other_cut),
        "scalar_P2_margin":rat(Fraction(scalar,denominator)),
        "finite_model_feasible":flow==sum(demand),
        "model":("own-original-target-credit + incidence-neighbor "
                 "original-dual-target-credit; both capacities unit per "
                 "TRUE original six-incidence support"),
        "all_h_P2_proved":False,
        "finite_all_label_W32_proved":False,
    }


def report():
    density=target_low_harmonics(6)["density"]
    results=[]
    for name,model in (
        ("lex",gq_pair_model(1,"lex")),
        ("hardest-M",swapped_labeling(_anchors()[0][1],"left",13,14)),
    ):
        original_lines,_,_=original_GQ_tables(
            2,tuple(model["incidences"]))
        # Reconstruct ORIGINAL and TRUE transposed ORIGINAL source weights.
        orig_source=true_original_sixsource_permanents(model)
        dual_state=dual_model(model)
        dual_source=true_original_sixsource_permanents(dual_state)
        BA=anchor_ledger(model,orig_source)
        AB=anchor_ledger(dual_state,dual_source)
        frozen=exact_two_family_point(model)
        if (BA["target_hits"],AB["target_hits"],
                BA["source_mass"])!=(
                frozen["U_BA"],frozen["U_AB"],
                sum(orig_source["weights"].values())):
            raise AssertionError("independent B0/C0 original seven-family census differs")
        result=incidence_charging_gate(
            BA,AB,original_lines,density=density)
        if result["scalar_P2_margin"]!=frozen["two_family_minus_mu"]:
            raise AssertionError("original fixed-left mean or dual counts changed")
        results.append({
            "name":name, "original_BA_source_mass":BA["source_mass"],
            "original_BA_target_hits":BA["target_hits"],
            "true_original_dual_AB_target_hits":AB["target_hits"],
            "original_GQ_point_anchor_permanent_one":BA["permanent_one"],
            "original_GQ_point_anchor_permanent_two":BA["permanent_two"],
            "joint_signed_rank5":rat(sum(
                (row[5] for row in BA["signed_by_anchor"]+
                               AB["signed_by_anchor"]),Fraction(0))),
            "joint_signed_rank6":rat(sum(
                (row[6] for row in BA["signed_by_anchor"]+
                               AB["signed_by_anchor"]),Fraction(0))),
            **result,
        })
    return {
        "slice":"HYP-105-E1-K3-G2-S",
        "original_and_true_dual_complete_W32_cases":results,
        "independent_integer_flow_and_all_32768_hall_cuts":True,
        "universal_hypothesis_P2":"OPEN",
        "universal_hypothesis_P7":"OPEN",
        "branch_A_B":"OPEN",
    }


if __name__=="__main__":
    print(json.dumps(report(),sort_keys=True,indent=2))
