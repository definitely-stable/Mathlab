"""HYP-105 #230 D6-C: W32 ORIGINAL blocked-path-to-seven-sixset local Hall audit.

Rigorous ALL-h observation (proved in companion doc): a blocked proper P3's
UNIQUE original q-l-p-r six-incidence closure is NEVER an accepted leafless
sixset. If it has fewer than six distinct original incidences it fails by
cardinality; if distinct, the offending original anchor is used TWICE,
creating a physical coordinate of degree >=4 instead of degree 2.
For W32 only, finite exact incidence-support local repair gates r=3/2/1
are tested against ALL SEVEN truly accepted original positive classes.
No finite flow statement is extrapolated to the PR394 large-h H or ROOT A/B.
"""
from collections import Counter, deque
from math import ceil
from itertools import combinations
import json

from hyp105_issue230_projection import ProjectionClosure, fixture
from hyp105_issue230_d6b_coherent_pruning import (
    _edge, _bits_from_original_endpoints, original_diagonals,
    full_retention, prune_original_incidences, coherent_selected_first,
    retained_path_census,
)
from hyp105_g5e2b3e1b0_seven_signature import (
    seven_census, classify_seven_prechecked,
)


class _Dinic:
    """Exact integer maxflow. Forward/reverse edges share no mutable values."""
    def __init__(self,n):
        self.graph=[[] for _ in range(n)]

    def edge(self,u,v,cap):
        if cap<0:
            raise ValueError("negative capacity")
        a=[v,cap,len(self.graph[v])]
        b=[u,0,len(self.graph[u])]
        self.graph[u].append(a)
        self.graph[v].append(b)

    def maxflow(self,source,sink):
        graph=self.graph
        total=0
        while True:
            level=[-1]*len(graph)
            level[source]=0
            queue=deque([source])
            while queue:
                u=queue.popleft()
                for v,cap,_ in graph[u]:
                    if cap and level[v]<0:
                        level[v]=level[u]+1
                        queue.append(v)
            if level[sink]<0:
                break
            indices=[0]*len(graph)
            def dfs(u,amount):
                if u==sink:
                    return amount
                while indices[u]<len(graph[u]):
                    e=graph[u][indices[u]]
                    v,cap,reverse=e
                    if cap and level[v]==level[u]+1:
                        f=dfs(v,min(amount,cap))
                        if f:
                            e[1]-=f
                            graph[v][reverse][1]+=f
                            return f
                    indices[u]+=1
                return 0
            while True:
                delta=dfs(source,10**20)
                if not delta:
                    break
                total+=delta
        return total

    def reachable(self,source):
        seen={source}
        todo=[source]
        while todo:
            u=todo.pop()
            for v,cap,_ in self.graph[u]:
                if cap and v not in seen:
                    seen.add(v)
                    todo.append(v)
        return seen


def _half_degree(core,ids,side):
    deg=Counter()
    labels=core.f if side=="left" else core.g
    for eid in ids:
        p,l=core.edges[eid]
        deg.update(labels[p if side=="left" else l])
    return deg


def _closure_proof(core,ids,completion,mask,seven_sets):
    # A true ORIGINAL projected completion (not the arbitrarily chosen repair).
    six=tuple(sorted(set(ids)|set(completion)))
    if len(six)!=6:
        if mask==0:
            raise AssertionError("unblocked true GQ closure must have SIX distinct incidences")
        return "REPEATED_ORIGINAL_INCIDENCE",six
    ld=_half_degree(core,six,"left")
    rd=_half_degree(core,six,"right")
    left_ok=len(ld)==6 and all(d==2 for d in ld.values())
    right_ok=len(rd)==6 and all(d==2 for d in rd.values())
    leafless=left_ok and right_ok
    if (mask==0)!=leafless:
        raise AssertionError("all-h original doubled anchor collision iff leafless failure")
    if mask and (max(ld.values(),default=0)<4 and max(rd.values(),default=0)<4):
        raise AssertionError("blocked original projected GQ closure must have degree>=4")
    # For zero-mask, original closure is genuinely BB-overlap, not merely
    # another unspecified degree-two six-incidence set.
    if seven_sets is not None:
        tag=seven_sets.get(six)
        if mask==0 and tag!="B/B-overlap":
            raise AssertionError("true original unblocked closure not accepted BB-overlap")
        if mask and tag is not None:
            raise AssertionError("blocked original GQ projection unexpectedly accepted")
    return ("ACCEPTED_BB" if not mask else
            "BAD_LEFT" if not left_ok and right_ok else
            "BAD_RIGHT" if left_ok and not right_ok else "BAD_BOTH"),six


def blocked_sources(core,retention,seven_sets,*,max_walks=2000000):
    """Independently recover ORIGINAL source triple and 16 masks from H paths."""
    a=core.a
    H=retention["adj"]
    diag,owners=original_diagonals(core)
    walk_budget=sum((len(H[u])-1)*(len(H[v])-1) for u,row in enumerate(H) for v in row)
    if type(max_walks) is not int or max_walks<0 or walk_budget>max_walks:
        raise ValueError("complete original physical P3 budget exceeded")
    by_triple=Counter()
    by_mask=Counter()
    closure_outcomes=Counter()
    first_by_triple={}
    good=0
    for v0,row in enumerate(H):
        x0,y0=divmod(v0,a)
        for v1 in row:
            x1,y1=divmod(v1,a)
            for v2 in H[v1]:
                x2,y2=divmod(v2,a)
                if x2 in (x0,x1) or y2 in (y0,y1):
                    continue
                for v3 in H[v2]:
                    x3,y3=divmod(v3,a)
                    if x3 in (x0,x1,x2) or y3 in (y0,y1,y2):
                        continue
                    q=core.fi.get(_edge(x0,x3))
                    r=core.gi.get(_edge(y0,y3))
                    if q is None or r is None or (q,r) in core.edge_id:
                        continue
                    mask=_bits_from_original_endpoints(
                        core,q,r,((x0,x1,x2,x3),(y0,y1,y2,y3)))
                    triple=tuple(sorted((
                        owners[_edge(v0,v1)],owners[_edge(v1,v2)],
                        owners[_edge(v2,v3)]
                    )))
                    if len(set(triple))!=3:
                        raise AssertionError("proper original physical P3 repeats source incidence")
                    p,l=core.projection[q,r]
                    completion=(
                        core.edge_id[q,l],core.edge_id[p,l],core.edge_id[p,r]
                    )
                    outcome,_=_closure_proof(core,triple,completion,mask,seven_sets)
                    closure_outcomes[outcome]+=1
                    if not mask:
                        good+=1
                        continue
                    by_triple[triple]+=1
                    by_mask[mask]+=1
                    first_by_triple.setdefault(triple,{
                        "source_three_original_incidences":list(triple),
                        "original_endpoint_point":q,
                        "original_endpoint_line":r,
                        "original_projection_point":p,
                        "original_projection_line":l,
                        "mask":mask,
                        "four_original_grid_vertices":[v0,v1,v2,v3],
                    })
    independent=retained_path_census(core,retention,independent_endpoints=True)
    if sum(by_triple.values())!=independent["C_joint_blocked_proper_P3"]:
        raise AssertionError("full ORIGINAL source-triple blocked count != independent D6B")
    if good!=2*independent["BB_sync_accepted_sixsets"]:
        raise AssertionError("D6-C good projected sixset multiplicity differs from D6B")
    if sum(by_mask.values())!=sum(independent["exact_sixteen_mask_histogram"][1:]):
        raise AssertionError("D6-C 16 source masks differ from D6B")
    for i in range(1,16):
        if by_mask[i]!=independent["exact_sixteen_mask_histogram"][i]:
            raise AssertionError("D6-C independent exact original mask differs")
    return {
        "sources":by_triple,"mask_counts":by_mask,
        "closure_outcomes":closure_outcomes,
        "first":first_by_triple,
        "good":good,"independent":independent
    }


def _repair_graph(source_counts,targets,required):
    """TRUE original incidence triple T can charge sixset R iff |T∩R|>=required."""
    if type(required) is not int or required not in (1,2,3):
        raise ValueError("number of preserved original incidences must be 1,2,3")
    triples=sorted(source_counts)
    recipients=sorted(targets)
    if any(len(t)!=3 or len(set(t))!=3 or source_counts[t]<1 for t in triples):
        raise ValueError("source must be positive multiplicity of three ORIGINAL incidences")
    if any(len(t)!=6 or len(set(t))!=6 for t in recipients):
        raise ValueError("target must be six distinct ORIGINAL incidences")
    recipient_sets=[set(t) for t in recipients]
    neighbors=[]
    for triple in triples:
        s=set(triple)
        neighbors.append(tuple(i for i,r in enumerate(recipient_sets)
                               if len(s&r)>=required))
    return triples,recipients,neighbors


def _flow(triples,recipients,neighbors,demands,capacity):
    nleft=len(triples); nright=len(recipients)
    source=0; leftstart=1; rightstart=leftstart+nleft; sink=rightstart+nright
    d=_Dinic(sink+1)
    total=sum(demands)
    for i,mass in enumerate(demands):
        d.edge(source,leftstart+i,mass)
        for target in neighbors[i]:
            d.edge(leftstart+i,rightstart+target,total+1)
    for j in range(nright):
        d.edge(rightstart+j,sink,capacity)
    value=d.maxflow(source,sink)
    if value==total:
        # Original-target integer assignment with load <= capacity is
        # equivalent to integral feasible flow, from integer capacities.
        return value,None
    reachable=d.reachable(source)
    A=[i for i in range(nleft) if leftstart+i in reachable]
    N=set(j for i in A for j in neighbors[i])
    mass=sum(demands[i] for i in A)
    deficit=mass-capacity*len(N)
    if deficit<=0 or total-value!=deficit:
        raise AssertionError("exact maxflow/mincut Hall obstruction not certified")
    return value,{
        "source_three_incidence_triples":[list(triples[i]) for i in A[:6]],
        "reachable_source_triples":len(A),
        "original_path_demand_on_subset":mass,
        "neighbor_positive_sixsets":len(N),
        "capacity":capacity,
        "exact_hall_deficit":deficit,
        "maxflow_shortfall":total-value,
    }


def capacity_frontier(source_counts,seven_sets,required,*,solve=True):
    triples,targets,neighbors=_repair_graph(source_counts,seven_sets,required)
    demand=sum(source_counts.values())
    if not demand:
        return {"required_original_source_incidence_overlap":required,
                "source_oriented_paths":0,"status":"EMPTY-SOURCE-NO-INFERENCE",
                "min_max_congestion":None}
    uncovered=[i for i,neighbor in enumerate(neighbors) if not neighbor]
    covered=demand-sum(source_counts[triples[i]] for i in uncovered)
    result={
        "required_original_source_incidence_overlap":required,
        "source_oriented_paths":demand,
        "distinct_source_incidence_triples":len(triples),
        "accepted_target_original_sixsets":len(targets),
        "covered_oriented_source_paths":covered,
        "uncovered_oriented_source_paths":demand-covered,
        "uncovered_source_triples":len(uncovered),
        "source_triples_with_any_repair":len(triples)-len(uncovered),
        "unconstrained_global_congestion_floor":ceil(demand/len(targets)) if targets else None,
        "uncovered_witness_source_original_incidence_triple":(
            list(triples[uncovered[0]]) if uncovered else None),
    }
    if uncovered or not targets:
        result.update({"status":"NO-GO-UNSUPPORTED-ORIGINAL-SOURCE",
                       "min_max_congestion":None})
        return result
    if not solve:
        result.update({"status":"COVERED-EXACT-CAPACITY-NOT-SOLVED",
                       "min_max_congestion":None})
        return result
    masses=[source_counts[t] for t in triples]
    low=max(1,ceil(demand/len(targets)))
    high=demand
    while low<high:
        mid=(low+high)//2
        value,_=_flow(triples,targets,neighbors,masses,mid)
        if value==demand:
            high=mid
        else:
            low=mid+1
    value,_=_flow(triples,targets,neighbors,masses,low)
    if value!=demand:
        raise AssertionError("optimal capacity must be feasible")
    witness=None
    if low>0:
        inferior,cut=_flow(triples,targets,neighbors,masses,low-1)
        if inferior==demand or cut is None:
            raise AssertionError("one-less-than-optimal capacity not ruled out")
        witness=cut
    result.update({
        "status":"EXACT-FINITE-INTEGRAL-HALL-OPTIMUM",
        "min_max_congestion":low,
        "optimal_capacity_lower_hall_cut":witness,
        "sixset_class_counts":dict(Counter(seven_sets.values())),
    })
    return result


def one_model(model,scheme,*,solve_flows=True):
    core=ProjectionClosure(model)
    if core.s!=2:
        raise ValueError("exact entire seven-family positive motif census is W32 ONLY")
    accepted=seven_census(model,independent_checks=True,witness_sets=True)
    targets=accepted["sets"]
    if not targets or len(targets)!=accepted["S_seven"]:
        raise AssertionError("full genuine original seven-family sixsets required")
    policies=(
        full_retention(core),
        prune_original_incidences(core,"finite-calibration"),
        coherent_selected_first(core,period=19),
        prune_original_incidences(core,"literal-pr394"),
    )
    records=[]
    for H in policies:
        source=blocked_sources(core,H,targets)
        t=source["sources"]
        full=len(targets)
        if source["good"] and source["closure_outcomes"]["ACCEPTED_BB"]!=source["good"]:
            raise AssertionError("all unblocked projections must enter seven family")
        if sum(source["closure_outcomes"].values())!=(
            sum(t.values())+source["good"]
        ):
            raise AssertionError("all original projected sixsets must be accounted for")
        frontiers=[capacity_frontier(t,targets,r,
                   solve=solve_flows and H["policy"]=="FULL-TRUE-ORIGINAL-G")
                   for r in (3,2,1)]
        row={
            "s":core.s,"scheme":scheme,
            "policy":H["policy"],
            "same_complete_globally_injective_original_f_g":True,
            "retained_true_original_incidences":H["retained_original_incidences"],
            "retained_paired_physical_edges":H["retained_physical_edges"],
            "total_true_original_oriented_blocked_paths":sum(t.values()),
            "total_true_original_unblocked_proper_paths":source["good"],
            "sixteen_original_mask_histogram":[source["mask_counts"][b]
                                               for b in range(16)],
            "unique_original_source_incidence_triples":len(t),
            "canonical_original_closure_outcomes":dict(source["closure_outcomes"]),
            "complete_original_seven_positive_S":full,
            "actual_seven_positive_classes":dict(accepted["seven_class_motif_counts"]),
            "source_overlap_frontiers":frontiers,
            "original_root_S_Omega_s6_proved":False,
            "asymptotic_bounded_congestion_charging_proved":False,
            "all_h_small_S_counterfamily_proved":False,
        }
        for f in frontiers:
            triple=f.get("uncovered_witness_source_original_incidence_triple")
            if triple is not None:
                row[f"r{f['required_original_source_incidence_overlap']}_unsupported_TRUE_original_source"] = source["first"][tuple(triple)]
        records.append(row)
    return records


def report():
    records=[]
    for scheme in ("lex","S68"):
        records.extend(one_model(fixture(1,scheme),scheme))
    return {
        "slice":"HYP105-ISSUE230-D6C-ORIGINAL-SEVEN-LOCAL-HALL",
        "all_h_direct_unique_projection_closure_for_blocked_paths":"NO-GO-PROVED",
        "finite_exact_all_seven_positive_recipients_ONLY_W32":True,
        "finite_empty_pr394_retention_is_vacuous":True,
        "original_root_A_and_B":"OPEN",
        "bounded_congestion_all_h":"OPEN",
        "records":records,
    }


if __name__=="__main__":
    print(json.dumps(report(),indent=2,sort_keys=True))
