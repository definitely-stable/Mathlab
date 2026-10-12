"""HYP-105 E1-K3-G2-F: rigorous bounded two-column completion of accepted S motifs.

For W(3,2) or W(3,4) with ONE globally coherent pair-label f,g,
classify any ACTUAL six distinct ORIGINAL incidence columns by seven
accepted positive GF5 leading families (A/B/C original factor profiles,
exact six physical degree-two coordinates on EACH half).
Search completes a pair of fixed ORIGINAL columns to accepted six-sets
via a constrained lexicographic DFS, without C(N,6) enumeration.

Every found target is independently verifiable and has a prior all-h
positive class GF5 floor; truncated/budgeted searches are NOT proof of
absence, exhaustive target sets, failed Hall, or all-h S=Omega(s^6).
"""
from collections import Counter
from itertools import combinations
import json

from hyp105_g5e2b3e1k1_kikuchi_c6 import gq_pair_model,kikuchi_graph
from hyp105_g5e2b3e1b0_seven_signature import (
    R3_CERTIFIED_FLOORS,is_connected_column_cycle
)
from hyp105_g5e2b3e1k3g2d_charging_hall import (
    HEAVY,cross_witnesses,edge_source_index,_maxflow_with_cut
)
from hyp105_g5e2b3e1k3g2e_seven_family_hall import (
    witness_original_five_support,explicit_injective_assignment
)

KINDS={(1,1,1,1,1,1):"A",(2,1,1,1,1):"B",(2,2,2):"C"}

def generic_seven_family(model,ids):
    """Exact B0 accepted seven-class predicate valid for ANY physical a.

    Input IDs are ORIGINAL incidence IDs. The validated seven-family
    target set is NOT the complete full GF5 R3: reject all other classes.
    """
    ids=tuple(sorted(ids))
    if (len(ids)!=6 or len(set(ids))!=6 or
            any(type(i) is not int or not 0<=i<len(model["incidences"])
                for i in ids)):
        raise ValueError("six distinct original incidence column IDs required")
    P=model["left_labels"];L=model["right_labels"]
    E=model["incidences"]
    halves=[]
    endpoints=[]
    for color,labels in ((0,P),(1,L)):
        origins=tuple(E[i][color] for i in ids)
        frequency=Counter(origins)
        kind=KINDS.get(tuple(sorted(frequency.values(),reverse=True)))
        if kind is None:
            return None
        physical=Counter(x for q in origins for x in labels[q])
        if len(physical)!=6 or any(d!=2 for d in physical.values()):
            return None
        halves.append(kind)
        endpoints.append(origins)
    l,r=halves
    if (l,r)==("B","A"):
        return "B-left/A-right"
    if (l,r)==("A","B"):
        return "A-left/B-right"
    if l==r=="A":
        dual=[]
        for origins,labels in ((endpoints[0],P),(endpoints[1],L)):
            pairs=tuple(sorted(
                tuple(j for j,origin in enumerate(origins)
                      if coordinate in labels[origin])
                for coordinate in sorted(set(x for q in origins for x in labels[q]))
            ))
            if len(pairs)!=6 or any(len(pair)!=2 for pair in pairs):
                raise AssertionError("six physical coordinate degrees must be two")
            dual.append(pairs)
        return "D6" if dual[0]==dual[1] and is_connected_column_cycle(dual[0]) else None
    if (l=="C" and r=="A") or (l=="A" and r=="C"):
        return "C/A"
    if (l=="C" and r=="B") or (l=="B" and r=="C"):
        return "C/B"
    if l==r=="B":
        q=next(x for x,n in Counter(endpoints[0]).items() if n==2)
        t=next(x for x,n in Counter(endpoints[1]).items() if n==2)
        a={j for j,x in enumerate(endpoints[0]) if x==q}
        b={j for j,x in enumerate(endpoints[1]) if x==t}
        if len(a&b)>1:
            raise AssertionError("two repeated ORIGINAL incidences would contradict simple GQ")
        return "B/B-overlap" if a&b else "B/B-disjoint"
    return None


def _profiles_ok(deg1,deg2,remaining):
    """Necessary degree-budget constraints for a six-coordinate 2-factor."""
    for deg in (deg1,deg2):
        touched=sum(d>0 for d in deg)
        unmatched=sum(d==1 for d in deg)
        if (touched>6 or touched+2*remaining<6 or
                unmatched>2*remaining or any(d>2 for d in deg)):
            return False
        if remaining==0 and (touched!=6 or unmatched):
            return False
    return True


def seed_pair_completion(model,first,second,*,max_nodes=20000,
                         max_targets=20):
    """Sound positive target search, complete only if NO cutoff occurred.

    Lexicographic completion of original source columns {first,second};
    ALL four additional IDs are strictly increasing (can be below seeds).
    Attempts counted on every candidate considered, including invalids.
    """
    if type(max_nodes) is not int or max_nodes<0 or (
            type(max_targets) is not int or max_targets<1):
        raise ValueError("invalid nonnegative work or positive target budget")
    N=len(model["incidences"])
    if (type(first) is not int or type(second) is not int or first==second
            or not 0<=first<N or not 0<=second<N):
        raise ValueError("two distinct actual original incidence IDs required")
    a=model["a"];V=len(model["left_labels"])
    incidences=model["incidences"]
    lx=model["left_labels"];ry=model["right_labels"]
    profiles=[(p,l,lx[p],ry[l]) for p,l in incidences]
    point_used=[0]*V
    line_used=[0]*V
    degx=[0]*a
    degy=[0]*a
    ids=[first,second]
    for col in ids:
        p,l,x,y=profiles[col]
        point_used[p]+=1
        line_used[l]+=1
        for v in x:degx[v]+=1
        for v in y:degy[v]+=1
    if (any(v>2 for v in point_used+line_used) or
            not _profiles_ok(degx,degy,4)):
        return {"seed":tuple(sorted(ids)),"targets":(),
                "nodes":0,"complete":True,"reason":"incompatible_seed"}
    # Closure-first is an ORDERING of all candidate column IDs, never
    # a filter: lexicographic traversal in this fixed order still
    # enumerates each four-element completion exactly once if uncut.
    # Prefer edges connecting already touched coordinates in BOTH halves.
    seed_x={v for col in ids for v in profiles[col][2]}
    seed_y={v for col in ids for v in profiles[col][3]}
    def relevance(col):
        _,_,x,y=profiles[col]
        share=sum(v in seed_x for v in x)+sum(v in seed_y for v in y)
        return (-share,col)
    others=tuple(sorted((i for i in range(N) if i not in ids),
                        key=relevance))
    targets=[]
    nodes=0
    truncated=False
    reason="exhaustive"
    def walk(start):
        nonlocal nodes,truncated,reason
        if truncated:
            return
        missing=6-len(ids)
        if missing==0:
            if _profiles_ok(degx,degy,0):
                family=generic_seven_family(model,ids)
                if family is not None:
                    targets.append((tuple(sorted(ids)),family))
                    if len(targets)>=max_targets:
                        truncated=True
                        reason="target_limit"
            return
        if len(others)-start<missing:
            return
        for pos in range(start,len(others)-missing+1):
            if truncated:
                break
            if nodes>=max_nodes:
                truncated=True
                reason="node_budget"
                break
            nodes+=1
            column=others[pos]
            p,l,x,y=profiles[column]
            if point_used[p]>=2 or line_used[l]>=2 or (
                    any(degx[v]>=2 for v in x) or
                    any(degy[v]>=2 for v in y)):
                continue
            ids.append(column)
            point_used[p]+=1
            line_used[l]+=1
            for v in x:degx[v]+=1
            for v in y:degy[v]+=1
            if _profiles_ok(degx,degy,missing-1):
                walk(pos+1)
            for v in y:degy[v]-=1
            for v in x:degx[v]-=1
            line_used[l]-=1
            point_used[p]-=1
            ids.pop()
    walk(0)
    if len({z[0] for z in targets})!=len(targets):
        raise AssertionError("source-seed search repeated an accepted six-set")
    if any(generic_seven_family(model,ids)!=tag for ids,tag in targets):
        raise AssertionError("invalid target escaped source-seed DFS")
    return {"seed":tuple(sorted((first,second))),
            "targets":tuple(targets),"nodes":nodes,
            "complete":not truncated,"reason":reason}


def _seed_order(model,original_five):
    """Prefer source-column pairs with larger existing physical support."""
    cols=sorted(original_five)
    pairs=list(combinations(cols,2))
    def score(pair):
        phys_x=set()
        phys_y=set()
        for col in pair:
            p,l=model["incidences"][col]
            phys_x.update(model["left_labels"][p])
            phys_y.update(model["right_labels"][l])
        return (-len(phys_x)-len(phys_y),pair)
    return tuple(sorted(pairs,key=score))


def targeted_seven_hall_probe(model,*,witness_limit=8,
                               seed_pairs_per_witness=2,
                               max_nodes_per_seed=20000,
                               max_targets_per_seed=20):
    """Finite positive-target lower certificate, not negative Hall proof.

    A FULL finite injection from selected actual Jcross witnesses into
    independently verified actual accepted sixsets is PROOF of such
    assignment for the selected subset. Incomplete search or failure to
    match does not prove lack of a charging relation.
    """
    if (type(witness_limit) is not int or witness_limit<1 or
            type(seed_pairs_per_witness) is not int or
            not 1<=seed_pairs_per_witness<=10):
        raise ValueError("finite positive sample and 1..10 seeds required")
    graph=kikuchi_graph(model)
    provenance=edge_source_index(model,graph)
    all_witnesses=cross_witnesses(model,max_witnesses=50000)
    # Deterministic, explicitly selected SUBSET: heavy class first, then
    # non-heavy. Never claim all-Jcross coverage when sampling.
    ordered=sorted(enumerate(all_witnesses),
                   key=lambda item:(item[1]["class"]!=HEAVY,item[0]))
    chosen=ordered[:witness_limit]
    targets={}
    sampled=[]
    attempts=0
    nodes=0
    completed_seeds=0
    incomplete_seeds=0
    for global_id,w in chosen:
        original=witness_original_five_support(model,w,provenance,graph)
        mapped=frozenset(model["incidences"].index(x) for x in original)
        seeds=_seed_order(model,mapped)[:seed_pairs_per_witness]
        candidate=set()
        for i,j in seeds:
            attempt=seed_pair_completion(model,i,j,
                                         max_nodes=max_nodes_per_seed,
                                         max_targets=max_targets_per_seed)
            attempts+=1
            nodes+=attempt["nodes"]
            completed_seeds+=attempt["complete"]
            incomplete_seeds+=not attempt["complete"]
            for six,tag in attempt["targets"]:
                old=targets.setdefault(six,tag)
                if old!=tag:
                    raise AssertionError("inconsistent true seven-family classification")
                if len(mapped & set(six))<2:
                    raise AssertionError("target fails required two-column original overlap")
                candidate.add(six)
        sampled.append({"original_witness_id":global_id,
                        "source_class":w["class"],
                        "original_five_column_ids":tuple(sorted(mapped)),
                        "pairs_tested":seeds,
                        "candidates":tuple(sorted(candidate))})
    all_targets=sorted(targets)
    right={six:j for j,six in enumerate(all_targets)}
    adj=[tuple(right[six] for six in w["candidates"]) for w in sampled]
    flow=_maxflow_with_cut(adj,len(all_targets),1)
    injection=explicit_injective_assignment(adj,len(all_targets))
    if flow["matched"]!=injection["assigned"]:
        raise AssertionError("positive-source construction vs Hall mismatch")
    check_assignment=[]
    for i,j in enumerate(injection["assignment"]):
        if j is not None:
            six=all_targets[j]
            if len(set(six)&set(sampled[i]["original_five_column_ids"]))<2:
                raise AssertionError("constructed mapping violates two-column overlap")
            tag=generic_seven_family(model,six)
            if tag!=targets[six] or R3_CERTIFIED_FLOORS[tag]<=0:
                raise AssertionError("assigned positive target not accepted")
            check_assignment.append((sampled[i]["original_witness_id"],six,tag))
    return {
        "s":model["s"],"a":model["a"],"scheme":model["scheme"],
        "seed":model.get("seed"),"all_Jcross_witnesses":len(all_witnesses),
        "tested_witnesses":len(sampled),
        "tested_heavy_witnesses":sum(w["source_class"]==HEAVY for w in sampled),
        "source_seed_pair_attempts":attempts,
        "explored_candidate_nodes":nodes,
        "exhausted_seed_searches":completed_seeds,
        "truncated_seed_searches":incomplete_seeds,
        "discovered_true_positive_sixsets":len(all_targets),
        "discovered_target_families":dict(Counter(targets.values())),
        "positive_targets_sample":tuple((six,targets[six])
                                         for six in all_targets[:12]),
        "unit_capacity_maximum_injection":flow["matched"],
        "unmatched_selected_witnesses":flow["unmatched"],
        "selected_witnesses_without_found_candidates":flow["isolated"],
        "constructed_assignment_sample":tuple(check_assignment[:12]),
        "constructive_assignment_sha256":
            injection["sha256_of_witness_to_target_indices"],
        "complete_selected_injection_proved":
            injection["complete"],
        "search_complete_for_all_seed_pairs_tested":incomplete_seeds==0,
        "search_complete_for_all_possible_seed_pairs":(
            incomplete_seeds==0 and seed_pairs_per_witness==10),
        "all_Jcross_covered_proved":(
            len(sampled)==len(all_witnesses) and injection["complete"]),
        "failure_of_universal_overlap_rule_proved":False,
        "all_h_S_omega_s6_proved":False,
    }

def report():
    out={"slice":"HYP-105-E1-K3-G2-F",
         "status":"FINITE_POSITIVE_W34_SEEDED_TARGET_LOWER_CERTIFICATE",
         "models":{}}
    for h,scheme,seed in ((1,"lex",None),(2,"lex",None),
                          (2,"random",20261012)):
        m=gq_pair_model(h,scheme,seed)
        # Explicitly budgeted broader W34 exploration, not exhaustive:
        # ten two-column seeds per sampled witness, a deterministic
        # coordinate-closure-first completion order for each seed.
        if h==2:
            args=dict(witness_limit=8,seed_pairs_per_witness=10,
                      max_nodes_per_seed=40000,max_targets_per_seed=12)
        else:
            args=dict(witness_limit=6,seed_pairs_per_witness=2,
                      max_nodes_per_seed=20000,max_targets_per_seed=12)
        out["models"]["s%s-%s"%(m["s"],scheme)]=targeted_seven_hall_probe(
            m,**args)
    return out

if __name__=="__main__":
    print(json.dumps(report(),sort_keys=True,indent=2))
