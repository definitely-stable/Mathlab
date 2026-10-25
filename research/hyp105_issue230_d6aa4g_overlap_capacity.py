"""HYP-105 #230 D6-AA4-G: overlapping ORIGINAL triads and global capacity gates.

All-h theorem is a CONDITIONAL frozen-outside separator lower bound, not
a map-independent seven-GF5 positivity result. W32 full 24-state exact
ORIGINAL source-label audit; X/Y are separately proved capacity falsifiers.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product
from math import comb, factorial

from hyp105_issue230_d6aa4e_global_assignment_dual import alphabet_capacity


def complete_fixed_image_states(types, baseline):
    """ONE shared typed injective assignment across ALL source motifs."""
    types, baseline = tuple(types), tuple(baseline)
    if len(types) != 4 or len(baseline) != 4 or any(t not in ("P", "L") for t in types):
        raise ValueError("four true typed ORIGINAL source factors required")
    groups = {t: tuple(i for i in range(4) if types[i] == t) for t in ("P", "L")}
    if any(len({baseline[i] for i in ix}) != len(ix) for ix in groups.values()):
        raise ValueError("non-injective same-type baseline")
    states = []
    for pt, ln in product(permutations([baseline[i] for i in groups["P"]]),
                          permutations([baseline[i] for i in groups["L"]])):
        state = list(baseline)
        for ix, values in ((groups["P"], pt), (groups["L"], ln)):
            for i, v in zip(ix, values):
                state[i] = v
        states.append(tuple(state))
    count = factorial(len(groups["P"]))*factorial(len(groups["L"]))
    if len(states) != count or len(set(states)) != count or states[0] != baseline:
        raise AssertionError("incomplete all-legal ORIGINAL typed completion fiber")
    return tuple(states)


def overlapping_triad_certificate(types, states, motifs):
    """Exact 4-source scope-checking separator relaxation.

    Each ORIGINAL Q occurs in EXACTLY one of two overlapping 3-factor
    clusters, or in independent residual. Group minima conditioned on
    overlap values are sound even when omitted factors are incompatible.
    Maximizing over all 12 ordered overlap-triad covers is sound.
    """
    types, states = tuple(types), tuple(tuple(x) for x in states)
    if len(types) != 4 or not states or states != complete_fixed_image_states(types, states[0]):
        raise ValueError("expected ALL globally injective fixed-image source states")
    motifs = tuple((tuple(scope), tuple(costs)) for scope,costs in motifs)
    n = len(states)
    independent = 0
    actual = [0]*n
    scopes = Counter()
    for scope, costs in motifs:
        if len(scope)!=len(set(scope)) or any(type(i) is not int or not 0<=i<4 for i in scope):
            raise ValueError("true ORIGINAL source scope IDs must be distinct")
        if len(costs)!=n or any(type(c) is not int or c<0 for c in costs):
            raise ValueError("complete nonnegative integral ORIGINAL sixset costs required")
        witness = {}
        for st,c in zip(states,costs):
            key = tuple(st[i] for i in scope)
            if key in witness and witness[key]!=c:
                raise AssertionError("Q cost depends on factor NOT in claimed ORIGINAL support")
            witness[key] = c
        independent+=min(costs)
        scopes[len(scope)]+=1
        for j,c in enumerate(costs):
            actual[j]+=c
    optimum = min(actual) if actual else 0
    results = []
    for middle in combinations(range(4),2):
        outer = tuple(i for i in range(4) if i not in middle)
        for swap in (False, True):
            left_outer,right_outer = outer[::-1] if swap else outer
            a = tuple(sorted((*middle,left_outer)))
            b = tuple(sorted((*middle,right_outer)))
            ga,gb,rest = [],[],[]
            for scope,costs in motifs:
                if set(scope).issubset(a):
                    ga.append(costs)
                elif set(scope).issubset(b):
                    gb.append(costs)
                else:
                    rest.append(costs)
            rest_min = sum(min(x) for x in rest)
            minima_a = min((sum(x[i] for x in ga) for i in range(n)),default=0)
            minima_b = min((sum(x[i] for x in gb) for i in range(n)),default=0)
            pair_unlinked = minima_a+minima_b+rest_min
            sep_keys = {tuple(s[i] for i in middle) for s in states}
            sep_best = None
            for sep in sep_keys:
                indices = [i for i,st in enumerate(states) if tuple(st[j] for j in middle)==sep]
                if not indices:
                    raise AssertionError("unrealizable separator signature")
                best_a=min(sum(x[i] for x in ga) for i in indices)
                best_b=min(sum(x[i] for x in gb) for i in indices)
                candidate=best_a+best_b+rest_min
                sep_best = candidate if sep_best is None else min(sep_best,candidate)
            if not 0<=independent<=pair_unlinked<=sep_best<=optimum:
                raise AssertionError("source-overlap conditional hierarchy false")
            results.append({
                "shared_original_factor_indices":middle,
                "first_triad":a,"second_triad":b,
                "first_triad_motifs":len(ga),"second_triad_motifs":len(gb),
                "uncovered_original_Q_motifs":len(rest),
                "separate_triad_lower":pair_unlinked,
                "shared_pair_separator_lower":sep_best,
                "number_realizable_overlap_signatures":len(sep_keys),
            })
    if len(results)!=12:
        raise AssertionError("12 ordered two-triad separators not exhausted")
    winner = max(results,key=lambda x:(x["shared_pair_separator_lower"],
                                          x["separate_triad_lower"]))
    return {
        "independent_Q_lower": independent,
        "best_separate_triad_lower": max(x["separate_triad_lower"] for x in results),
        "best_shared_pair_separator_lower": winner["shared_pair_separator_lower"],
        "true_joint_four_factor_minimum": optimum,
        "improvement_from_independent": winner["shared_pair_separator_lower"]-independent,
        "unresolved_shared_pair_to_full_gap": optimum-winner["shared_pair_separator_lower"],
        "complete_globally_injective_states":n,
        "scope_histogram":dict(sorted(scopes.items())),
        "winning_cover":winner,
        "all_twelve_covers":results,
        "all_full_state_costs":tuple(actual),
    }


def analytical_X_Y_capacity_checks(s):
    """Independent exact all-h regression against D6-X / D6-Y pseudo models.

    Not claimed to be new results, a GF5-motif cut, or an SA/SOS claim.
    """
    from math import comb
    z=alphabet_capacity(s)
    a,v,k,m=z["a"],z["V"],z["K"],z["m"]
    full=a*comb(a-1,2)
    sharp=full-2*m*(a-2)+comb(m,2)
    missing_star_achieves=sharp
    fake_adj=v*(a-2)
    gap=fake_adj-sharp
    if gap!=m*(a-2)-comb(m,2) or gap<0:
        raise AssertionError("D6-Y exact sharp physical-image gap changed")
    star_lift = None
    if a>=14:
        # D6-X: for distinct adjacent labels e,e', q!=p, local star model
        # E[x_pe]=1/K, E[x_pe*x_qe']=1/[a(a-1)(a-2)].
        star_lift=Fraction(1,k)-(v-1)*Fraction(1,a*(a-1)*(a-2))
        if star_lift>=0:
            raise AssertionError("D6-X local-star pseudo must FAIL lifted global column cut")
    return {
        "s":s,"a":a,"V":v,"K":k,"m":m,
        "all_real_images_max_adjacent_pairs":sharp,
        "missing_star_constructive_achiever":missing_star_achieves,
        "D6Y_selected_two_site_pseudo_adjacent_pairs":fake_adj,
        "D6Y_selected_two_site_gap":gap,
        "D6Y_pseudo_passes_selected_column_lifts_but_not_global_quad_cut":m>0,
        "D6X_star_pseudo_column_lift_slack":str(star_lift) if star_lift is not None else None,
        "D6X_star_pseudo_fails_column_lift":bool(star_lift is not None and star_lift<0),
        "not_a_GF5_seven_family_lower_bound":True,
    }


def original_W32_four_source_fiber(scheme):
    """Complete actual ORIGINAL W32 4-factor fibers: one coherent map per state.

    Four-factor pure-type transversals chosen deterministically from AA4-D;
    every state re-evaluated through original historical 62,370 candidates.
    """
    from hyp105_issue230_projection import fixture
    from hyp105_g5e2b3e1b0_seven_signature import (
        R3_CERTIFIED_FLOORS,seven_census)
    from hyp105_issue230_d6aa4c_edit_transversal import (
        genuine_original_positive_hypergraph,incidence_cover_bits)
    from hyp105_issue230_d6aa4d_mixed_transversal_fibers import finite_source_support_partition
    if scheme not in ("S68","S72"):
        raise ValueError("only TRUE original S68/S72 W32 mappings")
    model=fixture(1,scheme)
    source=genuine_original_positive_hypergraph(model)
    bits,weights,allmask=incidence_cover_bits(source["records"])
    partition=finite_source_support_partition(bits,weights,allmask)
    if partition["number_transversal_blocks"]!={"S68":53,"S72":119}[scheme]:
        raise AssertionError("original source transversal count drift")
    incidences=tuple(tuple(x) for x in model["incidences"])
    if len(incidences)!=45:
        raise AssertionError("invalid ORIGINAL W32 incidence graph")
    left=tuple(tuple(x) for x in model["left_labels"])
    right=tuple(tuple(x) for x in model["right_labels"])
    result={}
    for typ in ("P","L"):
        block=next((b for b in partition["transversal_original_factor_blocks"]
                    if all((x<15)==(typ=="P") for x in b)),None)
        if block is None or len(block)!=4:
            raise AssertionError("no original pure-type size-four hitting set")
        factor_ids=tuple((typ,i if typ=="P" else i-15) for i in block)
        baseline=tuple((left if typ=="P" else right)[i] for _,i in factor_ids)
        states=complete_fixed_image_states((typ,)*4,baseline)
        if len(states)!=24:
            raise AssertionError("not all four-factor global bijections")
        all_positive=set()
        per_state=[]
        for values in states:
            lp,rp=list(left),list(right)
            for (_,i),e in zip(factor_ids,values):
                (lp if typ=="P" else rp)[i]=e
            census=seven_census({**model,"left_labels":tuple(lp),
                                 "right_labels":tuple(rp)},
                                independent_checks=False,witness_sets=True)
            if census["S_seven"]!=len(census["sets"]) or (
               census["GF5_seven_lower_numerator"]!=sum(
                   R3_CERTIFIED_FLOORS[t] for t in census["sets"].values())):
                raise AssertionError("original positional GF5 conservation failure")
            per_state.append(census)
            all_positive.update(census["sets"])
        motifs=[]
        weighted=[]
        for Q in sorted(all_positive):
            originals={("P",p) for j in Q for p,l in (incidences[j],)}
            originals.update(("L",l) for j in Q for p,l in (incidences[j],))
            scope=tuple(i for i,f in enumerate(factor_ids) if f in originals)
            unit=tuple(int(Q in c["sets"]) for c in per_state)
            cost=tuple(R3_CERTIFIED_FLOORS.get(c["sets"].get(Q),0)
                       for c in per_state)
            motifs.append((scope,unit))
            weighted.append((scope,cost))
        seven=overlapping_triad_certificate((typ,)*4,states,motifs)
        GF5=overlapping_triad_certificate((typ,)*4,states,weighted)
        if seven["all_full_state_costs"]!=tuple(c["S_seven"] for c in per_state):
            raise AssertionError("ALL ORIGINAL positive sixsets not recomposed")
        if GF5["all_full_state_costs"]!=tuple(
             c["GF5_seven_lower_numerator"] for c in per_state):
            raise AssertionError("ALL ORIGINAL certified GF5 weights not recomposed")
        from hyp105_issue230_d6aa4c_edit_transversal import survivor_certificate
        retained,retained_y,_=survivor_certificate(bits,weights,allmask,block)
        if retained!=0 or retained_y!=0:
            raise AssertionError("chosen four-factor ORIGINAL support not a hitting set")
        if seven["true_joint_four_factor_minimum"]!={"S68":68,"S72":(
            69 if typ=="P" else 68)}[scheme]:
            # S72 AA4D minima are over ALL 4-factor hitting blocks, and
            # a specific chosen pure block need not attain that minimum.
            if scheme=="S68" or seven["true_joint_four_factor_minimum"]<(
              69 if typ=="P" else 68):
                raise AssertionError("AA4-D critical-fiber lower regression")
        result[typ]={
            "original_source_block":block,
            "complete_maps":24,"original_candidate_Q_per_map":62370,
            "original_Q_positive_in_any_state":len(all_positive),
            "seven":seven,"selected_GF5_numerator":GF5,
            "no_all_label_lower_claim":True,
        }
    return {"scheme":scheme,"geometry":"genuine ORIGINAL W(3,2) with 45 source incidences",
            "by_type":result,"Branch_A":"OPEN","Branch_B":"OPEN"}


def report(scheme=None):
    out={"slice":"HYP105-ISSUE230-D6-AA4-G-OVERLAPPING-TRIADS-CAPACITY",
         "theorem":"ALL_H_CONDITIONAL_FROZEN_OUTSIDE",
         "universal_positive_seven_GF5":False,
         "physical_capacity_regressions":[analytical_X_Y_capacity_checks(2**h)
                                           for h in range(1,8)],
         "Branch_A":"OPEN","Branch_B":"OPEN","full_R3":False,"ASET_exponent":False}
    if scheme is not None:
        out["W32"]=original_W32_four_source_fiber(scheme)
    return out


if __name__=="__main__":
    import argparse,json
    p=argparse.ArgumentParser()
    p.add_argument("--scheme",choices=("S68","S72"))
    a=p.parse_args()
    print(json.dumps(report(a.scheme),indent=2,sort_keys=True))
