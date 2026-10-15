"""HYP-105 #230 — D6-AA4-O: exact fixed-g ORIGINAL B/A quintic energy.

All-h deterministic identity:
I_L^{BA,int}(f,g) = sum_(p,A) w_g(p,A) *
   1{f(A) consists of a C4 on four physical coordinates,
     disjoint from f(p)}.
Here A consists of FOUR distinct genuine ORIGINAL source point IDs,
w_g is the integer number of genuine ORIGINAL six-incidence B/A sets
having this five-point support, fixed right A projection under ONE
complete globally injected g, and physically disjoint right root edges.
No independent per-Q maps and no proxy physical P3.

Exact transposition gradient is supported only on quintic monomials
whose five source point factors meet the swapped pair. Validate with
historical 62370-sixset ORIGINAL GF5 census on real W32 and an
adversarial complete-globally-injective point-label swap descent.
No all-h positive minimax result is asserted.
"""
from collections import Counter,defaultdict
from fractions import Fraction
from itertools import combinations,product
import json
import random

from hyp105_issue230_d6aa4n_quenched_right_transfer import (
    original_W32_fixed_g_right_A_counter,
)
from hyp105_issue230_d6aa4m_random_injection_charge import (
    exact_random_projection_probabilities,
)


def _physical_masks(labels,a):
    labels=tuple(tuple(e) for e in labels)
    if len(set(labels))!=len(labels):
        raise ValueError("true source factor map must be globally injective")
    masks=[]
    for e in labels:
        if len(e)!=2 or any(type(c) is not int for c in e) or not 0<=e[0]<e[1]<a:
            raise ValueError("canonical source physical-edge label invalid")
        masks.append((1<<e[0])|(1<<e[1]))
    return tuple(masks)


def true_original_W32_fixed_g_weighted_tensor(model):
    """Exact nonnegative five-source-factor coefficient tensor w_g.

    Count each ORIGINAL six-distinct-incidence right-A point-B Q exactly
    once, after fixing genuine complete right map g. A term's point
    support consists of unique root p plus four fresh original points;
    source line factors are reconstructed via ONE actual fixed g.
    """
    if model.get("s")!=2 or model.get("a")!=6:
        raise ValueError("genuine full ORIGINAL W32 fixed-right case required")
    original=tuple(tuple(i) for i in model["incidences"])
    if len(original)!=45 or len(set(original))!=45:
        raise ValueError("45 distinct genuine original incidence IDs required")
    right=tuple(tuple(x) for x in model["right_labels"])
    if len(right)!=15 or set(right)!=set(combinations(range(6),2)):
        raise ValueError("complete true original W32 line-edge K6 bijection required")
    phys_line={e:i for i,e in enumerate(right)}
    bypoint=[set() for _ in range(15)]
    byline=[set() for _ in range(15)]
    for p,l in original:
        if not 0<=p<15 or not 0<=l<15:
            raise ValueError("original point or line ID not in true W32 source")
        bypoint[p].add(l)
        byline[l].add(p)
    if any(len(q)!=3 for q in (*bypoint,*byline)):
        raise ValueError("not a 3-regular true ORIGINAL W32 point-line incidence host")
    edge_labels=tuple(combinations(range(6),2))
    Asets=tuple(frozenset(phys_line[e] for e in six)
                for six in combinations(edge_labels,6)
                if all(sum(c in e for e in six)==2 for c in range(6)))
    if len(Asets)!=70:
        raise AssertionError("real right K6 six-coordinate A projection 2-factor count changed")
    counts=Counter()
    uncompressed=0
    for p in range(15):
        for l0,l1 in combinations(sorted(bypoint[p]),2):
            # The root source original lines must physically NOT share
            # a coordinate, independently of the eventual random f.
            if set(right[l0])&set(right[l1]):
                continue
            root=frozenset((l0,l1))
            for lines6 in Asets:
                if not root<=lines6:
                    continue
                rest=tuple(sorted(lines6-root))
                if len(rest)!=4:
                    raise AssertionError("right A line-set has wrong source root support")
                for q4 in product(*(tuple(sorted(byline[l]-{p})) for l in rest)):
                    if len(set(q4))!=4:
                        continue
                    key=(p,)+tuple(sorted(q4))
                    if p in q4 or len(set(key))!=5:
                        raise AssertionError("not a five-distinct-original-point support")
                    counts[key]+=1
                    uncompressed+=1
    baseline=original_W32_fixed_g_right_A_counter(model)
    if uncompressed!=baseline[
        "right_A_internal_concurrent_disjoint_original_line_pair_Q_T_g"]:
        raise AssertionError("independent AA4-N original right source count disagrees")
    keys=tuple(sorted(counts))
    terms=tuple((key,counts[key]) for key in keys)
    incident=[set() for _ in range(15)]
    for j,(ids,mult) in enumerate(terms):
        if mult<=0:
            raise AssertionError("nonpositive original right fixed coefficient")
        for p in ids:
            incident[p].add(j)
    return {
        "source":"one fixed complete original W32 right g",
        "terms":terms,
        "incident_term_indices":tuple(frozenset(q) for q in incident),
        "five_point_support_count":len(terms),
        "total_original_BA_true_right_A_internal_Q_T_g":uncompressed,
        "max_original_Q_multiplicity_per_five_point_support":max(counts.values()),
        "all_45_original_incidence_IDs_verified":True,
        "independent_original_W32_right_A_oracle":"PASS",
        "positive_probability_full_left_B":str(
            exact_random_projection_probabilities(2)["pB_exact"]),
    }


def _term_positive(masks,ids):
    """Point B projection iff four DISTINCT physical edges form C4 and
    root p is an edge disjoint from all four C4 coordinates.
    All five source labels are globally DISTINCT edges.
    """
    p,*q=ids
    e=(masks[q[0]],masks[q[1]],masks[q[2]],masks[q[3]])
    allbits=e[0]|e[1]|e[2]|e[3]
    return int(
        allbits.bit_count()==4 and (e[0]^e[1]^e[2]^e[3])==0
        and (masks[p]&allbits)==0
    )


def exact_original_BA_energy(tensor,labels,a=6):
    masks=_physical_masks(labels,a)
    if len(masks)!=15:
        raise ValueError("exact original W32 full fifteen-point source injection required")
    return sum(weight*_term_positive(masks,ids)
               for ids,weight in tensor["terms"])


def exact_swap_gradient(tensor,labels,u,v,a=6):
    """One EXACT transposition of two whole source-point physical labels.

    Terms avoiding both source point IDs cancel algebraically.
    """
    if type(u) is not int or type(v) is not int or not 0<=u<15 or not 0<=v<15 or u==v:
        raise ValueError("two DIFFERENT original source point IDs 0..14 required")
    before=_physical_masks(labels,a)
    if len(before)!=15:
        raise ValueError("complete true original fifteen-point mapping required")
    after=list(before)
    after[u],after[v]=after[v],after[u]
    touched=tensor["incident_term_indices"][u] | tensor[
        "incident_term_indices"][v]
    return sum(
        tensor["terms"][j][1]*
        (_term_positive(after,tensor["terms"][j][0])-
         _term_positive(before,tensor["terms"][j][0]))
        for j in touched
    )


def exhaustive_one_swap_frontier(tensor,labels,a=6):
    """All C(15,2)=105 valid complete-global-injection transpositions."""
    labels=tuple(tuple(x) for x in labels)
    deltas={(u,v):exact_swap_gradient(tensor,labels,u,v,a)
            for u,v in combinations(range(15),2)}
    if len(deltas)!=105:
        raise AssertionError("not all true K6 globally bijective swaps enumerated")
    min_delta=min(deltas.values())
    best=min((d,u,v) for (u,v),d in deltas.items())
    nonincreasing=sum(d<=0 for d in deltas.values())
    return {
        "all_original_complete_map_pair_swaps":105,
        "minimum_exact_swap_delta":min_delta,
        "best_swap":(best[1],best[2]),
        "nonincreasing_swap_count":nonincreasing,
        "exact_swaps_preserve_global_source_injectivity":True,
    }


def descend_true_original_W32(tensor,labels,*,max_steps=150):
    """Deterministic steepest transposition descent, no fake global optimum."""
    if type(max_steps) is not int or max_steps<=0:
        raise ValueError("positive finite swap budget required")
    cur=tuple(tuple(x) for x in labels)
    score=exact_original_BA_energy(tensor,cur)
    start=score
    trace=[score]
    for _ in range(max_steps):
        best=exhaustive_one_swap_frontier(tensor,cur)
        if best["minimum_exact_swap_delta"]>=0:
            break
        u,v=best["best_swap"]
        nxt=list(cur)
        nxt[u],nxt[v]=nxt[v],nxt[u]
        nxt=tuple(nxt)
        new=exact_original_BA_energy(tensor,nxt)
        if new-score!=best["minimum_exact_swap_delta"] or new>=score:
            raise AssertionError("exact original five-factor swap gradient wrong")
        cur=nxt
        score=new
        trace.append(score)
    frontier=exhaustive_one_swap_frontier(tensor,cur)
    if frontier["minimum_exact_swap_delta"]<0:
        raise AssertionError("swap descent truncated before one-swap stationarity")
    if any(a<=b for a,b in zip(trace[1:],trace[:-1])):
        raise AssertionError("nonmonotone true ORIGINAL GF5 source B/A energy descent")
    if len(set(cur))!=15:
        raise AssertionError("optimized original point map ceased to be injective")
    return {
        "source":"ONE complete globally type-injective ORIGINAL point map",
        "initial_real_BA_charge":start,
        "final_real_BA_charge":score,
        "strictly_decreasing_steps":len(trace)-1,
        "score_trace":trace,
        "all_105_original_point_pair_label_swap_gradient_nonnegative":True,
        "certified_final_minimum_exact_swap_delta":
            frontier["minimum_exact_swap_delta"],
        "final_globally_injective_point_labels":cur,
        "not_claimed_globally_optimal":True,
        "not_claimed_all_h_charge_zero":True,
    }


def true_W32_quintic_swap_report(scheme,random_starts=2):
    """Cross check historical original 7-GF5 census before/after descent."""
    from hyp105_issue230_projection import fixture
    from hyp105_g5e2b3e1b0_seven_signature import seven_census
    model=fixture(1,scheme)
    tensor=true_original_W32_fixed_g_weighted_tensor(model)
    right=tuple(tuple(x) for x in model["right_labels"])
    original=tuple(tuple(x) for x in model["incidences"])
    starts=[tuple(tuple(x) for x in model["left_labels"])]
    rng=random.Random(2300470+{"lex":0,"reverse":1,"S68":2,"S72":3}[scheme])
    all_physical=list(combinations(range(6),2))
    for _ in range(random_starts):
        rng.shuffle(all_physical)
        starts.append(tuple(all_physical))
    results=[]
    for start in starts:
        f0={**model,"left_labels":start}
        historical=seven_census(f0,independent_checks=False,witness_sets=True)
        # Independently classify every positive accepted TRUE six-incidence
        # B-left/A-right Q and its two real source-concurrent line labels.
        expected=0
        for Q,tag in historical["sets"].items():
            if tag!="B-left/A-right":continue
            ends=tuple(original[i] for i in Q)
            roots=Counter(p for p,l in ends)
            p=next((p for p,n in roots.items() if n==2),None)
            if p is None:raise AssertionError("historical GF5 point-B tag source mismatch")
            lines=[l for q,l in ends if q==p]
            if len(lines)!=2:raise AssertionError("not actual original two-line point pencil")
            expected+=not(set(right[lines[0]])&set(right[lines[1]]))
        energy=exact_original_BA_energy(tensor,start)
        if expected!=energy:
            raise AssertionError("NEW quintic tensor disagrees with historical genuine ORIGINAL GF5 seven-census")
        result=descend_true_original_W32(tensor,start)
        if result["initial_real_BA_charge"]!=energy:
            raise AssertionError("descent original initial charge disagrees")
        f1={**model,"left_labels":tuple(result[
            "final_globally_injective_point_labels"])}
        full=seven_census(f1,independent_checks=False,witness_sets=True)
        final_internal=0
        for Q,tag in full["sets"].items():
            if tag!="B-left/A-right":continue
            ends=tuple(original[i] for i in Q)
            counted=Counter(p for p,l in ends)
            roots=[p for p,n in counted.items() if n==2]
            if len(roots)!=1:raise AssertionError("not original source B/A")
            lines=[l for p,l in ends if p==roots[0]]
            final_internal+=not(set(right[lines[0]])&set(right[lines[1]]))
        if final_internal!=result["final_real_BA_charge"]:
            raise AssertionError("optimized complete map disagrees with ORIGINAL all-seven GF5 census")
        results.append({
            **result,
            "independent_historical_full_original_GF5_initial_internal_charge":expected,
            "independent_historical_full_original_GF5_final_internal_charge":final_internal,
            "full_historical_final_original_positive_seven_Q":full["S_seven"],
            "independent_62370_original_sixsets_before_after":"PASS",
        })
    charges=[r["final_real_BA_charge"] for r in results]
    if any(r["not_claimed_globally_optimal"] is not True for r in results):
        raise AssertionError("unearned global minimum claim")
    return {
        "scheme":scheme,
        "one_true_complete_fixed_original_line_mapping":True,
        "all_45_original_incidence_IDs":True,
        "all_70_physical_right_A_2factors":True,
        "genuine_original_right_T_g":tensor[
            "total_original_BA_true_right_A_internal_Q_T_g"],
        "nonnegative_genuine_original_five_source_tensor_monomials":
            tensor["five_point_support_count"],
        "source_weighted_right_Q_multiplicity_max":
            tensor["max_original_Q_multiplicity_per_five_point_support"],
        "full_uniform_complete_left_charge_expectation_given_g":
            str(Fraction(tensor["total_original_BA_true_right_A_internal_Q_T_g"])*
                Fraction(tensor["positive_probability_full_left_B"])),
        "all_15_global_source_point_labels_are_distinct":True,
        "search_results":results,
        "min_found_after_valid_complete_injection_swaps":min(charges),
        "not_a_global_minimum_certificate":True,
        "root_A":"OPEN","root_B":"OPEN",
    }


def report(schemes=("S68","S72")):
    return {
        "slice":"HYP105-ISSUE230-D6-AA4-O-QUINTIC-ADVERSARIAL-SWAP",
        "all_h_exact_nonnegative_five_source_factor_BA_tensor_identity":True,
        "all_h_exact_transposition_support_local_gradient_identity":True,
        "all_h_global_injective_minimum_GF5_s6_PROVED":False,
        "root_A":"OPEN","root_B":"OPEN",
        "schemes":{x:true_W32_quintic_swap_report(x) for x in schemes},
    }


if __name__=="__main__":
    import argparse
    p=argparse.ArgumentParser()
    p.add_argument("--scheme",choices=("S68","S72","lex","reverse"))
    p.add_argument("--random-starts",type=int,default=2)
    x=p.parse_args()
    if x.scheme:
        result=true_W32_quintic_swap_report(x.scheme,x.random_starts)
    else:
        result={"slice":"HYP105-ISSUE230-D6-AA4-O-QUINTIC-ADVERSARIAL-SWAP",
                "all_h_exact_nonnegative_five_source_factor_BA_tensor_identity":True,
                "all_h_global_injective_minimum_GF5_s6_PROVED":False,
                "root_A":"OPEN","root_B":"OPEN"}
    print(json.dumps(result,indent=2,sort_keys=True))
