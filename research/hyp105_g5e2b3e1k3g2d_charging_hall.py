"""K3-G2-D: exact finite Hall obstruction to charging repeated C6 into proper D6.

This is a FINITE FALSIFICATION of unit-capacity local charging, not a
uniform negative result for seven-family S and not an ASET theorem.
Each off-diagonal original source-pair witness gives one C6 with exactly
one repeated original incidence column. Candidate proper D6 must share
the exact original anchor column, so a bipartite capacity matching is a
necessary-and-sufficient finite local charging criterion.

Theorem (all finite bipartite graphs): maxflow=mincut, and a full
capacity-k assignment exists iff |X|<=k|N(X)| for every witness subset X.
An isolated witness forbids ALL finite k under the anchor-overlap rule.
The Hall deficiency set is extracted from residual reachability.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations
import json

from hyp105_g5e2b3e1k1_kikuchi_c6 import (
    gq_pair_model, kikuchi_graph, proper_six_cycles_pruned,
)
from hyp105_g5e2b3e1k3g2b_origin_pair_kernel import inc_tables
from hyp105_g5e2b3e1k3g2c_projection_fibers import (
    anchored_projection, class_of_pair, projection_pair_certificate,
)

HEAVY="off_differentfoot_noncollinear"

def edge_source_index(model, graph):
    a=model["a"]
    lookup={}
    for p,l in model["incidences"]:
        x,x2=model["left_labels"][p]
        y,y2=model["right_labels"][l]
        for v,w in ((x*a+y,x2*a+y2),(x*a+y2,x2*a+y)):
            e=tuple(sorted((v,w)))
            if e in lookup or v not in graph[w] or w not in graph[v]:
                raise AssertionError("original edge-to-incidence injection failed")
            lookup[e]=(p,l)
    if len(lookup)!=2*len(model["incidences"]):
        raise AssertionError("Kikuchi edge cardinality mismatch")
    return lookup

def proper_d6_supports(model, *, max_cycles=100000):
    """Proper simple six-cycles, distinct original columns, counted once."""
    if type(max_cycles) is not int or max_cycles<0:
        raise ValueError("cycle budget must be a nonnegative integer")
    graph=kikuchi_graph(model)
    edge_source=edge_source_index(model,graph)
    a=model["a"]
    supports=[]
    for start in range(len(graph)):
        x,y=divmod(start,a)
        def visit(path,xs,ys):
            last=path[-1]
            if len(path)==6:
                if start in graph[last] and path[1]<last:
                    cols=frozenset(edge_source[tuple(sorted((u,v)))]
                        for u,v in zip(path,path[1:]+[start]))
                    if len(cols)!=6:
                        raise AssertionError("proper six-cycle repeated original column")
                    supports.append(cols)
                    if len(supports)>max_cycles:
                        raise RuntimeError("proper D6 cycle budget exceeded")
                return
            for w in sorted(graph[last]):
                if w<=start:
                    continue
                xx,yy=divmod(w,a)
                if xx in xs or yy in ys:
                    continue
                visit(path+[w],xs|{xx},ys|{yy})
        visit([start],{x},{y})
    if len(supports)!=proper_six_cycles_pruned(graph,a):
        raise AssertionError("K1 independent proper C6 reference discrepancy")
    return supports

def cross_witnesses(model, *,max_witnesses=200000):
    """Witness-by-witness original-source provenance and foot projection."""
    if type(max_witnesses) is not int or max_witnesses<0:
        raise ValueError("witness budget must be a nonnegative integer")
    graph=kikuchi_graph(model)
    source=edge_source_index(model,graph)
    P,L=inc_tables(model)
    a=model["a"]
    foot_cache={}
    rows=[]
    for p,l in model["incidences"]:
        x,xx=model["left_labels"][p]
        y,yy=model["right_labels"][l]
        A=x*a+y;B=xx*a+yy;C=x*a+yy;D=xx*a+y
        for u,v,w,z,which,source_idx,anchor,pencils,anchor_on in (
            (A,C,B,D,"line",0,l,P,L[l]),
            (A,D,B,C,"point",1,p,L,P[p]),
        ):
            key=(which,anchor)
            if key not in foot_cache:
                foot_cache[key]=anchored_projection(pencils,anchor_on)[0]
            feet=foot_cache[key]
            for middle in sorted(graph[u]&graph[v]):
                e1=source[tuple(sorted((u,middle)))]
                e2=source[tuple(sorted((v,middle)))]
                if e1[source_idx]!=e2[source_idx]:
                    raise AssertionError("origin provenance differs along two-path")
                q=e1[source_idx]
                for other in sorted(graph[w]&graph[z]):
                    if other==middle:
                        raise AssertionError("GQ prohibits equal antipodal middle")
                    e3=source[tuple(sorted((w,other)))]
                    e4=source[tuple(sorted((z,other)))]
                    if e3[source_idx]!=e4[source_idx]:
                        raise AssertionError("opposite two-path provenance differs")
                    r=e3[source_idx]
                    if q==r:
                        continue
                    category=class_of_pair(q,r,feet,anchor_on,pencils)
                    rows.append({"anchor":(p,l),"side":which,
                                 "origin_pair":tuple(sorted((q,r))),
                                 "middle_pair":(middle,other),"class":category})
                    if len(rows)>max_witnesses:
                        raise RuntimeError("source witness budget exceeded")
    return rows

def _maxflow_with_cut(adjacency,right_count,capacity):
    if type(capacity) is not int or capacity<=0:
        raise ValueError("positive integral per-motif charging capacity needed")
    if type(right_count) is not int or right_count<0:
        raise ValueError("nonnegative right vertex count needed")
    if any(any(j<0 or j>=right_count for j in row) for row in adjacency):
        raise ValueError("unknown proper D6 charge candidate")
    L=len(adjacency);R=right_count
    src=L+R;snk=src+1;node_count=snk+1
    net=[[] for _ in range(node_count)]
    def add(u,v,c):
        net[u].append([v,c,len(net[v])])
        net[v].append([u,0,len(net[u])-1])
    for i in range(L):
        add(src,i,1)
        for j in sorted(set(adjacency[i])):
            add(i,L+j,1)
    for j in range(R):
        add(L+j,snk,capacity)
    flow=0
    while True:
        dist=[-1]*node_count
        dist[src]=0
        queue=deque([src])
        while queue:
            u=queue.popleft()
            for v,c,_ in net[u]:
                if c and dist[v]<0:
                    dist[v]=dist[u]+1
                    queue.append(v)
        if dist[snk]<0:
            break
        cur=[0]*node_count
        def dfs(u,available):
            if u==snk:
                return available
            while cur[u]<len(net[u]):
                edge=net[u][cur[u]]
                v,c,rev=edge
                if c and dist[v]==dist[u]+1:
                    sent=dfs(v,min(available,c))
                    if sent:
                        edge[1]-=sent
                        net[v][rev][1]+=sent
                        return sent
                cur[u]+=1
            return 0
        while True:
            pushed=dfs(src,L-flow)
            if not pushed:
                break
            flow+=pushed
    # Canonical source-side minimum cut, with exact capacity certificate.
    reachable={src}
    queue=deque([src])
    while queue:
        u=queue.popleft()
        for v,c,_ in net[u]:
            if c and v not in reachable:
                reachable.add(v)
                queue.append(v)
    left_reach={i for i in range(L) if i in reachable}
    right_reach={j for j in range(R) if L+j in reachable}
    cut=(L-len(left_reach))+capacity*len(right_reach)
    # All L-to-R edges from reached left nodes must remain in the cut
    # only if saturated; for this integral network an optimal cut can
    # have those arcs, so include their 1-capacities explicitly.
    cross_arcs=sum(1 for i in left_reach for j in set(adjacency[i])
                   if j not in right_reach)
    cut+=cross_arcs
    if cut!=flow:
        raise AssertionError("maxflow/mincut residual certificate mismatched")
    return {"matched":flow,"left_nodes":L,"right_nodes":R,
            "capacity":capacity,"min_cut_capacity":cut,
            "witness_subset_size":len(left_reach),
            "witness_neighbor_count":len(set(j for i in left_reach
                                                  for j in adjacency[i])),
            "residual_right_reachable":len(right_reach),
            "unmatched":L-flow,
            "all_witnesses_charged":flow==L,
            "isolated":sum(not row for row in adjacency)}

def finite_charging_certificate(model, *,max_witnesses=200000,
                                max_proper_cycles=100000):
    witnesses=cross_witnesses(model,max_witnesses=max_witnesses)
    proper=proper_d6_supports(model,max_cycles=max_proper_cycles)
    baseline=projection_pair_certificate(model)
    by_class=Counter(w["class"] for w in witnesses)
    for cls in by_class:
        expected=(baseline["line"]["seven_class_weighted"].get(cls,0)+
                  baseline["point"]["seven_class_weighted"].get(cls,0))
        if by_class[cls]!=expected:
            raise AssertionError("K3-G2-C weighted original source witness mismatch")
    if len(witnesses)!=baseline["J_cross_exact"]:
        raise AssertionError("Jcross proper charging cardinality is wrong")
    anchor_index=defaultdict(list)
    for j,cols in enumerate(proper):
        for column in cols:
            anchor_index[column].append(j)
    def subset_certificate(rows,with_capacity_search=True):
        adj=[tuple(anchor_index[w["anchor"]]) for w in rows]
        stats=_maxflow_with_cut(adj,len(proper),1)
        if with_capacity_search and rows and not stats["isolated"]:
            # Monotone exact minimum feasible integer multiplicity k.
            low=max(1,(len(rows)+max(1,len(proper))-1)//max(1,len(proper)))
            high=len(rows)
            while low<high:
                mid=(low+high)//2
                if _maxflow_with_cut(adj,len(proper),mid)["all_witnesses_charged"]:
                    high=mid
                else:
                    low=mid+1
            stats["minimum_capacity_to_charge_all"]=low
            if not _maxflow_with_cut(adj,len(proper),low)["all_witnesses_charged"]:
                raise AssertionError("finite Hall threshold failed")
            if low>1 and _maxflow_with_cut(adj,len(proper),low-1)["all_witnesses_charged"]:
                raise AssertionError("nonminimal charging capacity")
        else:
            stats["minimum_capacity_to_charge_all"]=(
                None if stats["isolated"] else (0 if not rows else None))
        stats["global_counting_floor"]=(
            (len(rows)+len(proper)-1)//len(proper) if proper else None)
        return stats
    heavy=[w for w in witnesses if w["class"]==HEAVY]
    result={
        "s":model["s"],"a":model["a"],
        "scheme":model["scheme"],"seed":model.get("seed"),
        "J_cross_exact":len(witnesses),
        "proper_D6_exact":len(proper),
        "class_witness_counts":dict(sorted(by_class.items())),
        "unit_injection_global_no_go":len(witnesses)>len(proper),
        "all_cross_anchor_local_charge":subset_certificate(witnesses),
        "heavy_class":HEAVY,"heavy_witness_count":len(heavy),
        "heavy_anchor_local_charge":subset_certificate(heavy),
        "seven_family_S_all_h_proved":False,
        "finite_labeling_counterexample_to_abstract_S":False,
    }
    return result

def report():
    models=((1,"lex",None),(1,"reverse-line",None),
            (1,"random",20261012))
    result={"slice":"HYP-105-E1-K3-G2-D",
            "status":"FINITE_HALL_CHARGING_FALSIFIER_NOT_S_THEOREM","models":{}}
    for h,scheme,seed in models:
        m=gq_pair_model(h,scheme,seed)
        name=f"s{m['s']}-{scheme}-{seed}"
        result["models"][name]=finite_charging_certificate(m)
    return result

if __name__=="__main__":
    print(json.dumps(report(),indent=2,sort_keys=True))
