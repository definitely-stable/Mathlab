"""HYP-105 E1-K3-G2-G: adaptive complete-Jcross FINITE charging certificate.

All discovered targets are genuine positive accepted six-family originals.
Local pair search is budgeted and may be incomplete; a found injection is
valid even when target enumeration is not exhaustive, while an unmatched
source is NOT a proof of impossible charging.

Separately derives two rigorous model-specific lower certificates:
S >= number of distinct accepted source sixsets found;
51^6 R3 >= sum certified GF5 minimum weights of those distinct sixsets.
"""
from collections import Counter
from itertools import combinations
from hashlib import sha256
import json

from hyp105_g5e2b3e1k1_kikuchi_c6 import gq_pair_model, kikuchi_graph
from hyp105_g5e2b3e1b0_seven_signature import R3_CERTIFIED_FLOORS
from hyp105_g5e2b3e1k3g2d_charging_hall import (
    HEAVY, cross_witnesses, edge_source_index, _maxflow_with_cut
)
from hyp105_g5e2b3e1k3g2e_seven_family_hall import (
    witness_original_five_support, explicit_injective_assignment,
)
from hyp105_g5e2b3e1k3g2f_w34_seeded_targets import (
    _seed_order, seed_pair_completion, generic_seven_family,
)


def _source_supports(model, sample_limit=None):
    if sample_limit is not None and (
            type(sample_limit) is not int or sample_limit<1):
        raise ValueError("positive or absent witness sample limit needed")
    neighbors=kikuchi_graph(model)
    original=edge_source_index(model,neighbors)
    witnesses=cross_witnesses(model,max_witnesses=50000)
    column_idx={col:i for i,col in enumerate(model["incidences"])}
    if len(column_idx)!=len(model["incidences"]):
        raise AssertionError("original incidence IDs must be unique")
    # Heavy first only when using an explicitly documented sample. If
    # all witnesses are included, order is only a deterministic gauge.
    ordered=sorted(enumerate(witnesses),
                   key=lambda z:(z[1]["class"]!=HEAVY,z[0]))
    chosen=ordered[:sample_limit] if sample_limit else ordered
    output=[]
    for original_id,w in chosen:
        source=witness_original_five_support(model,w,original,neighbors)
        indices=frozenset(column_idx[e] for e in source)
        if len(indices)!=5:
            raise AssertionError("source support is not five original columns")
        output.append({
            "witness_id":original_id,
            "class":w["class"],
            "source_original_ids":indices,
            "pair_candidates":_seed_order(model,indices),
        })
    return len(witnesses),output


def _positive_target_graph(sources,target_map):
    target_ids=tuple(sorted(target_map))
    # A complete scan of the CURRENT found target index. There is no
    # inference of nonexistence when future targets may still be undiscovered.
    adj=[]
    for row in sources:
        support=row["source_original_ids"]
        adj.append(tuple(j for j,t in enumerate(target_ids)
                         if len(set(t)&support)>=2))
    return target_ids,adj


def _assert_valid_certificate(model,sources,target_map,target_ids,adj,assignment):
    if len(assignment)!=len(sources):
        raise AssertionError("assignment size wrong")
    used=set()
    for i,j in enumerate(assignment):
        if j is None:
            continue
        if not 0<=j<len(target_ids) or j in used or j not in adj[i]:
            raise AssertionError("not an injective source-to-target matching")
        used.add(j)
        ids=target_ids[j]
        tag=generic_seven_family(model,ids)
        if tag!=target_map[ids] or R3_CERTIFIED_FLOORS.get(tag,0)<=0:
            raise AssertionError("assigned original target GF5 positivity invalid")


def adaptive_complete_cross_probe(model,*,sample_limit=None,
                                  first_pass_seed_count=1,
                                  max_seeds_per_unmatched=4,
                                  max_nodes_per_seed=12000,
                                  max_targets_per_seed=12,
                                  max_unique_targets=15000):
    """Search across ALL Jcross witnesses unless sample_limit is explicit.

    Cached seed pair completions and dynamically shared true-S targets.
    The Hall graph of discovered targets uses EVERY source witness
    regardless of which witness discovered each target. Recovery only
    searches seed pairs of currently unmatched sources; all matchings
    are exact and independently constructed.
    """
    for name,val in (
        ("first_pass_seed_count",first_pass_seed_count),
        ("max_seeds_per_unmatched",max_seeds_per_unmatched),
        ("max_nodes_per_seed",max_nodes_per_seed),
        ("max_targets_per_seed",max_targets_per_seed),
        ("max_unique_targets",max_unique_targets)
    ):
        if type(val) is not int or val<0:
            raise ValueError(name+" must be a nonnegative integer")
    if (not 1<=first_pass_seed_count<=10 or
            not first_pass_seed_count<=max_seeds_per_unmatched<=10 or
            max_targets_per_seed<1 or max_unique_targets<1):
        raise ValueError("invalid positive seed/target limits")
    all_count,sources=_source_supports(model,sample_limit)
    pair_cache={}
    target_map={}
    workload=Counter()
    truncated=Counter()
    seeded=[set() for _ in sources]
    positive_example_by_class={}

    def discover(i,pair_idx):
        row=sources[i]
        pair=row["pair_candidates"][pair_idx]
        seeded[i].add(pair_idx)
        workload["requests"]+=1
        if pair in pair_cache:
            result=pair_cache[pair]
            workload["cache_hits"]+=1
        else:
            result=seed_pair_completion(
                model,*pair,max_nodes=max_nodes_per_seed,
                max_targets=max_targets_per_seed)
            pair_cache[pair]=result
            workload["unique_seed_searches"]+=1
            workload["nodes"]+=result["nodes"]
            truncated[result["reason"]]+=not result["complete"]
        for ids,tag in result["targets"]:
            if len(row["source_original_ids"] & set(ids))<2:
                raise AssertionError("source-target ORIGINAL overlap failed")
            if target_map.setdefault(ids,tag)!=tag:
                raise AssertionError("conflicting accepted seven-family type")
            positive_example_by_class.setdefault(tag,ids)
        if len(target_map)>max_unique_targets:
            raise RuntimeError("positive target storage budget exceeded")

    # First pass: limited search for EVERY witness, including cross-origin
    # witnesses which are not in the heavy projection class.
    for i in range(len(sources)):
        for pair_idx in range(first_pass_seed_count):
            discover(i,pair_idx)

    def current_matching():
        target_ids,adj=_positive_target_graph(sources,target_map)
        flow=_maxflow_with_cut(adj,len(target_ids),1)
        direct=explicit_injective_assignment(adj,len(target_ids))
        if direct["assigned"]!=flow["matched"]:
            raise AssertionError("independent Hall and augmenting path discrepancy")
        _assert_valid_certificate(model,sources,target_map,target_ids,
                                  adj,direct["assignment"])
        return target_ids,adj,flow,direct

    targets,adj,flow,assign=current_matching()
    after_first=flow["matched"]
    # Adaptive recovery. Re-evaluate MATCHING after each round rather
    # than working from the original orphan subset forever.
    rounds=0
    while flow["matched"]<len(sources):
        unmatched=[i for i,j in enumerate(assign["assignment"]) if j is None]
        available=[i for i in unmatched if len(seeded[i])<max_seeds_per_unmatched]
        if not available:
            break
        for i in available:
            next_idx=next(k for k in range(max_seeds_per_unmatched)
                          if k not in seeded[i])
            discover(i,next_idx)
        rounds+=1
        targets,adj,flow,assign=current_matching()
        if rounds>=max_seeds_per_unmatched:
            raise AssertionError("recovery loop unexpectedly exceeded seed cap")
    counts=Counter(target_map.values())
    positive_risk_numerator=sum(
        n*R3_CERTIFIED_FLOORS[tag] for tag,n in counts.items())
    if (len(targets)!=sum(counts.values()) or
            any(tag not in R3_CERTIFIED_FLOORS for tag in counts)):
        raise AssertionError("source target count or risk classes invalid")
    assignments=[
        (sources[i]["witness_id"],targets[j],target_map[targets[j]])
        for i,j in enumerate(assign["assignment"]) if j is not None
    ]
    witness_digest=sha256(";".join(
        str(x[0])+":"+(",".join(map(str,x[1])))+":"+x[2]
        for x in assignments).encode("ascii")).hexdigest()
    all_covered=(
        len(sources)==all_count and flow["matched"]==all_count)
    return {
        "s":model["s"],"scheme":model["scheme"],"seed":model.get("seed"),
        "global_Jcross_exact":all_count,
        "source_witnesses_considered":len(sources),
        "heavy_source_witnesses_considered":
            sum(row["class"]==HEAVY for row in sources),
        "source_sample_limit":sample_limit,
        "positive_targets_distinct":len(targets),
        "positive_seven_family_counts":dict(sorted(counts.items())),
        "positive_seven_sixset_samples":{
            tag:list(ids) for tag,ids in sorted(positive_example_by_class.items())
        },
        "positive_seven_S_lower":len(targets),
        "positive_risk_numerator_lower_51_pow_6":positive_risk_numerator,
        "positive_risk_denominator":51**6,
        "matched_after_first_pass":after_first,
        "matched_after_adaptive_recovery":flow["matched"],
        "unmatched_after_recovery":flow["unmatched"],
        "isolated_under_DISCOVERED_targets":flow["isolated"],
        "recovery_rounds":rounds,
        "seed_pair_requests":workload["requests"],
        "unique_seed_pair_searches":workload["unique_seed_searches"],
        "reused_seed_pair_results":workload["cache_hits"],
        "candidate_nodes_visited":workload["nodes"],
        "seed_truncation_reasons":dict(sorted(truncated.items())),
        "actual_constructed_assignment_sha256":witness_digest,
        "actual_assignment_samples":assignments[:12],
        "full_finite_Jcross_charge_into_true_S_proved":all_covered,
        "unit_capacity_S_charge_for_considered_witnesses_proved":
            flow["matched"]==len(sources),
        "all_h_Jcross_leq_S_proved":False,
        "all_h_S_omega_s6_proved":False,
        "failure_when_budgeted_unmatched_proved":False,
    }


def report():
    output={"slice":"HYP-105-E1-K3-G2-G",
            "status":"GLOBAL_FINITE_W34_ADAPTIVE_CHARGING_AND_POSITIVE_S_LOWER",
            "models":{}}
    for h,scheme,seed in (
        (1,"lex",None),(2,"lex",None),(2,"random",20261012)):
        model=gq_pair_model(h,scheme,seed)
        output["models"]["s%s-%s%s"%(model["s"],scheme,
                                      "-"+str(seed) if seed is not None else "")
                         ]=adaptive_complete_cross_probe(
            model,
            max_nodes_per_seed=30000,
            max_targets_per_seed=12,
            first_pass_seed_count=1,
            max_seeds_per_unmatched=10)
    return output

if __name__=="__main__":
    print(json.dumps(report(),sort_keys=True,indent=2))
