"""HYP-105 K3-G2-E: true accepted seven-family GF5-target Hall charging gate.

FINITE W(3,2) ONLY. Every target is a DISTINCT ORIGINAL six-incidence
set passing the accepted seven-family classifier with a positive
class-specific GF(5) minimum. Each left witness is a 6-cycle with five
distinct ORIGINAL incidence columns, one repeated twice.

The rule R_t charges witness w to accepted target T iff |S(w) ∩ T|>=t.
A stronger anchor rule also demands w's repeated original column in T.
For every rule, exact max-flow/min-cut + binary-search minimum feasible
per-target integer capacity, or an orphan witness disproving this rule
for ALL capacities. This does not prove any all-h S_s lower bound.
"""
from collections import Counter,defaultdict
from math import ceil
from hashlib import sha256
import json

from hyp105_g5e2b3e1k1_kikuchi_c6 import gq_pair_model,kikuchi_graph
from hyp105_g5e2b3e1k3g2d_charging_hall import (
    HEAVY,cross_witnesses,edge_source_index,proper_d6_supports,_maxflow_with_cut
)
from hyp105_g5e2b3e1b0_seven_signature import (
    seven_census,R3_CERTIFIED_FLOORS
)

RULES=("same_anchor","overlap_ge_1","overlap_ge_2",
       "overlap_ge_3","overlap_ge_4","overlap_ge_5",
       "anchor_and_overlap_ge_2","anchor_and_overlap_ge_3")


def witness_original_five_support(model, witness, edge_source, graph):
    """Independently rebuild six physical edges of Jcross cycle.

    Never infer incidence support merely from source q/r: follow every
    physical Kikuchi edge and its globally unique ORIGINAL incidence.
    """
    a=model["a"]
    p,l=witness["anchor"]
    x,xx=model["left_labels"][p]
    y,yy=model["right_labels"][l]
    A=x*a+y; B=xx*a+yy; C=x*a+yy; D=xx*a+y
    if witness["side"]=="line":
        u,v,w,z=A,C,B,D
    elif witness["side"]=="point":
        u,v,w,z=A,D,B,C
    else:
        raise ValueError("unknown original-source witness side")
    middle,other=witness["middle_pair"]
    vertices=(u,middle,v,z,other,w)
    if len(set(vertices))!=6:
        raise AssertionError("Jcross witness not a simple physical six-cycle")
    if not all(vertices[(i+1)%6] in graph[vertices[i]] for i in range(6)):
        raise AssertionError("Jcross witness does not form a Kikuchi cycle")
    source_cols=[
        edge_source[tuple(sorted((vertices[i],vertices[(i+1)%6])))]
        for i in range(6)
    ]
    count=Counter(source_cols)
    if len(count)!=5 or count[witness["anchor"]]!=2 or (
            any(mult!=1 for col,mult in count.items()
                if col!=witness["anchor"])):
        raise AssertionError("Jcross has wrong ORIGINAL repeated-column pattern")
    return frozenset(count)


def _rules_for(witness_support,target_support,anchor):
    intersection=len(witness_support & target_support)
    repeated_present=anchor in target_support
    return {
        "same_anchor":repeated_present,
        "overlap_ge_1":intersection>=1,
        "overlap_ge_2":intersection>=2,
        "overlap_ge_3":intersection>=3,
        "overlap_ge_4":intersection>=4,
        "overlap_ge_5":intersection>=5,
        "anchor_and_overlap_ge_2":repeated_present and intersection>=2,
        "anchor_and_overlap_ge_3":repeated_present and intersection>=3,
    }




def explicit_injective_assignment(adjacency,number_targets):
    """Deterministic explicit injective witness->accepted-target map, if any.

    A matching construction INDEPENDENT of the Dinic/Hall max-flow
    checker, with a deterministic SHA256 of its integer source-target pairs.
    This certificate is finite-model-specific, NEVER all-h proof.
    """
    if type(number_targets) is not int or number_targets<0:
        raise ValueError("valid number of target vertices required")
    for row in adjacency:
        if any(type(j) is not int or not 0<=j<number_targets for j in row):
            raise ValueError("edge to nonexistent target")
    owner=[None]*number_targets
    def try_augment(i,seen):
        for j in sorted(set(adjacency[i])):
            if j in seen:
                continue
            seen.add(j)
            prior=owner[j]
            if prior is None or try_augment(prior,seen):
                owner[j]=i
                return True
        return False
    matched=sum(bool(try_augment(i,set())) for i in range(len(adjacency)))
    assignment=[None]*len(adjacency)
    for j,i in enumerate(owner):
        if i is not None:
            if assignment[i] is not None:
                raise AssertionError("left witness charged more than once")
            assignment[i]=j
    if matched!=sum(v is not None for v in assignment):
        raise AssertionError("constructive injection size mismatch")
    if any(j is not None and j not in adjacency[i]
           for i,j in enumerate(assignment)):
        raise AssertionError("claimed charge edge absent")
    digest=sha256(";".join(
        str(i)+":"+str(j) for i,j in enumerate(assignment)
        if j is not None).encode("ascii")).hexdigest()
    return {"assigned":matched,
            "complete":matched==len(adjacency),
            "assignment":tuple(assignment),
            "sha256_of_witness_to_target_indices":digest}


def hall_capacity_certificate(adjacency,number_targets,*,search_capacity=True):
    if type(number_targets) is not int or number_targets<0:
        raise ValueError("target count must be nonnegative")
    one=_maxflow_with_cut(adjacency,number_targets,1)
    any_isolated=one["isolated"]>0
    if not adjacency:
        minimum=0
    elif any_isolated:
        minimum=None
    elif search_capacity:
        lo=max(1,ceil(len(adjacency)/number_targets))
        hi=len(adjacency)
        if not _maxflow_with_cut(adjacency,number_targets,hi)["all_witnesses_charged"]:
            raise AssertionError("without orphan Hall-k must succeed at n")
        while lo<hi:
            mid=(lo+hi)//2
            if _maxflow_with_cut(adjacency,number_targets,mid)["all_witnesses_charged"]:
                hi=mid
            else:
                lo=mid+1
        minimum=lo
        if minimum>1 and _maxflow_with_cut(
                adjacency,number_targets,minimum-1)["all_witnesses_charged"]:
            raise AssertionError("minimum accepted target capacity not minimal")
    else:
        minimum=None
    one["minimum_capacity_to_charge_all"]=minimum
    one["all_capacity_impossible_due_to_orphans"]=any_isolated
    one["min_positive_candidate_degree"]=min(
        (len(set(row)) for row in adjacency if row),default=0)
    one["max_candidate_degree"]=max((len(set(row)) for row in adjacency),default=0)
    one["targets_with_any_candidate"]=len(set(
        j for row in adjacency for j in row))
    return one


def seven_family_hall_certificate(model,*,max_witnesses=5000,
                                   max_seven_targets=5000):
    """Full finite structural W(3,2) census, not a W(3,4) extrapolation."""
    if type(max_witnesses) is not int or max_witnesses<0:
        raise ValueError("nonnegative finite witness budget")
    if type(max_seven_targets) is not int or max_seven_targets<0:
        raise ValueError("nonnegative accepted target budget")
    if model["s"]!=2 or model["a"]!=6:
        raise ValueError("only exact complete W(3,2) K6 seven-family oracle supported")
    seven=seven_census(model,independent_checks=False,witness_sets=True)
    by_set=seven["sets"]
    if len(by_set)>max_seven_targets:
        raise RuntimeError("seven-family target budget exceeded")
    if any(floor<=0 for floor in R3_CERTIFIED_FLOORS.values()):
        raise AssertionError("nonpositive accepted GF5 floor")
    original_to_column={e:i for i,e in enumerate(model["incidences"])}
    if len(original_to_column)!=model["N"]:
        raise AssertionError("original incidence index missing")
    # Accepted targets are sets of original incidence IDs rather than
    # physical Kikuchi cycle IDs. One motif target per original six-set.
    targets=[
        (frozenset(model["incidences"][i] for i in ids),kind)
        for ids,kind in sorted(by_set.items())
    ]
    if any(len(S)!=6 or kind not in R3_CERTIFIED_FLOORS for S,kind in targets):
        raise AssertionError("invalid distinct accepted 6-column GF5 target")
    graph=kikuchi_graph(model)
    provenance=edge_source_index(model,graph)
    witnesses=cross_witnesses(model,max_witnesses=max_witnesses)
    source_supports=[
        witness_original_five_support(model,w,provenance,graph)
        for w in witnesses
    ]
    if any(len(S)!=5 for S in source_supports):
        raise AssertionError("invalid original five-column witness support")
    target_set=[S for S,_ in targets]
    seven_counts=Counter(kind for _,kind in targets)
    if dict(seven_counts)!=dict((k,v) for k,v
                               in seven["seven_class_motif_counts"].items() if v):
        raise AssertionError("seven-family target histogram disagrees")
    proper_only=proper_d6_supports(model,max_cycles=200000)
    if seven_counts["D6"]!=len(proper_only):
        raise AssertionError("seven-family accepted proper D6 target count mismatch")
    # Charge edges depend on ACTUAL original support overlap; never on
    # artificial subset inclusion or dynamically created S motifs.
    all_adj={k:[] for k in RULES}
    by_kind={k:Counter() for k in RULES}
    for w,S in zip(witnesses,source_supports):
        memberships={k:[] for k in RULES}
        for i,T in enumerate(target_set):
            flags=_rules_for(S,T,w["anchor"])
            for rule,ok in flags.items():
                if ok:
                    memberships[rule].append(i)
                    by_kind[rule][targets[i][1]]+=1
        for rule in RULES:
            all_adj[rule].append(tuple(memberships[rule]))
    heavy_indexes=[i for i,w in enumerate(witnesses) if w["class"]==HEAVY]
    stats={}
    for rule,adj in all_adj.items():
        all_stat=hall_capacity_certificate(adj,len(targets))
        heavy_stat=hall_capacity_certificate(
            [adj[i] for i in heavy_indexes],len(targets))
        constructed=explicit_injective_assignment(adj,len(targets))
        constructed_heavy=explicit_injective_assignment(
            [adj[i] for i in heavy_indexes],len(targets))
        if constructed["assigned"]!=all_stat["matched"] or (
                constructed_heavy["assigned"]!=heavy_stat["matched"]):
            raise AssertionError("constructive matching disagrees with exact Hall flow")
        stats[rule]={
            "all":all_stat,
            "heavy":heavy_stat,
            "constructive_matching":{
                "complete":constructed["complete"],
                "assigned":constructed["assigned"],
                "sha256":constructed["sha256_of_witness_to_target_indices"],
            },
            "heavy_constructive_matching":{
                "complete":constructed_heavy["complete"],
                "assigned":constructed_heavy["assigned"],
                "sha256":constructed_heavy["sha256_of_witness_to_target_indices"],
            },
            "charge_edges_by_accepted_family":dict(by_kind[rule]),
        }
    # Restriction of seven-family "same anchor" candidates to D6
    # must exactly equal previous K3-G2-D anchor-local matching network.
    d6idx=[j for j,(_,kind) in enumerate(targets) if kind=="D6"]
    d6_old_to_new={j:i for i,j in enumerate(d6idx)}
    d6_anchor_adj=[
        tuple(d6_old_to_new[j] for j in row if j in d6_old_to_new)
        for row in all_adj["same_anchor"]
    ]
    direct_d6=hall_capacity_certificate(d6_anchor_adj,len(d6idx))
    return {
        "s":model["s"],"scheme":model["scheme"],"seed":model.get("seed"),
        "accepted_seven_sixset_targets":len(targets),
        "accepted_seven_counts":dict(seven_counts),
        "accepted_full_GF5_risk_floor_numerator":
            seven["GF5_seven_lower_numerator"],
        "all_target_types_have_proved_positive_GF5_floor":True,
        "J_cross_five_column_witnesses":len(witnesses),
        "heavy_class":HEAVY,
        "heavy_class_witnesses":len(heavy_indexes),
        "witness_support_cardinality":5,
        "accepted_target_original_column_cardinality":6,
        "same_anchor_D6_only_reconciliation":direct_d6,
        "rules":stats,
        "all_h_uniform_bounded_charging_proved":False,
        "all_h_seven_family_S_omega_s6_proved":False,
    }


def report():
    result={"slice":"HYP-105-B3.2-E1-K3-G2-E",
            "status":"FINITE_TRUE_SEVEN_GF5_HALL_CAPACITY_AND_SUPPORT_GATE",
            "models":{}}
    for scheme,seed in (("lex",None),("reverse-line",None),
                        ("random",20261012)):
        model=gq_pair_model(1,scheme,seed)
        result["models"][scheme+("-"+str(seed) if seed else "")]=(
            seven_family_hall_certificate(model))
    return result


if __name__=="__main__":
    print(json.dumps(report(),sort_keys=True,indent=2))
