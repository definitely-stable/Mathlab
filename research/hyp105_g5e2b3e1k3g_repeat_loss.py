"""K3-G1: exact antipodal source-column repeat loss for Kikuchi C6.

Every original incidence contributes two disjoint edges. A six-cycle
using both must put them opposite: an intermediate edge across the
same physical rectangle is forbidden. Define J by two aligned
codegree-product matchings, subtracting shared middle vertices.
Then J=C6_rep1+3*C6_rep3 (no C6_rep2 by finite all-pattern lemma).
The triple-repeat cycles are exactly physical label triangles in
original point and line pencils and are uniformly O(s^(9/2)).

No seven-family S lower bound and no uniform C6_rep1 upper is claimed.
"""
from collections import defaultdict
from itertools import combinations
from math import isqrt
import json

from hyp105_g5e2b3e1k1_kikuchi_c6 import gq_pair_model, kikuchi_graph


def triangles_of_edges(edges, *, max_edges=64):
    """Count triangles of an injectively edge-labelled source pencil."""
    if type(max_edges) is not int or max_edges < 0:
        raise ValueError("max_edges must be nonnegative integer")
    if len(edges)>max_edges:
        raise RuntimeError("source pencil edge budget exceeded")
    graph=defaultdict(set)
    seen=set()
    for i,j in edges:
        if i==j or (min(i,j),max(i,j)) in seen:
            raise ValueError("source pencil must be a simple graph")
        seen.add((min(i,j),max(i,j)))
        graph[i].add(j)
        graph[j].add(i)
    return sum(len(graph[x]&graph[y]) for x,y in seen)//3


def source_pencil_repeat_three(model, *, max_edges=64):
    """All-h bijection: triple-repeated C6 <-> one source-pencil triangle."""
    left=model["left_labels"]
    right=model["right_labels"]
    by_point=[[] for _ in left]
    by_line=[[] for _ in right]
    for p,l in model["incidences"]:
        by_point[p].append(right[l])
        by_line[l].append(left[p])
    point_tris=sum(triangles_of_edges(p,max_edges=max_edges) for p in by_point)
    line_tris=sum(triangles_of_edges(l,max_edges=max_edges) for l in by_line)
    s=model["s"]
    V=len(left)
    if len(right)!=V or V!=(s+1)*(s*s+1):
        raise ValueError("balanced W(3,s) source parameters required")
    if any(len(p)!=s+1 for p in by_point+by_line):
        raise ValueError("regular W(3,s) pencils required")
    per_pencil_cap=isqrt((2*(s+1))**3)//6
    total_cap=2*V*per_pencil_cap
    total=point_tris+line_tris
    if total>total_cap:
        raise AssertionError("all-h pencil triangle upper failed")
    return {"C6_rep3":total,"point_pencil_triangles":point_tris,
            "line_pencil_triangles":line_tris,
            "all_h_rep3_upper":total_cap,
            "uniform_rep3_o_s6":True}


def _aligned_path_pair_count(graph, ab, cd, ef, gh):
    """Disjoint internal-vertex choices for two aligned length-2 paths."""
    first=graph[ab]&graph[cd]
    second=graph[ef]&graph[gh]
    return len(first)*len(second)-len(first&second)


def antipodal_repeat_certificate(model, *, max_incidence_columns=10000,
                                 max_pencil_edges=64):
    """Exact source-repeat incidence J without enumerating six-cycles.

    J counts each cycle once PER repeated original incidence column.
    Exhaustive two-coordinate six-walk classification proves that
    a simple Kikuchi six-cycle has either 0, 1, or 3 repeats, never 2.
    Hence J=C6_rep1+3*C6_rep3 and C6_rep=J-2*C6_rep3.
    """
    if type(max_incidence_columns) is not int or max_incidence_columns<0:
        raise ValueError("max_incidence_columns must be nonnegative integer")
    if len(model["incidences"])>max_incidence_columns:
        raise RuntimeError("source incidence-column budget exceeded")
    graph=kikuchi_graph(model)
    a=model["a"]
    J=0
    for p,l in model["incidences"]:
        x,xx=model["left_labels"][p]
        y,yy=model["right_labels"][l]
        A=x*a+y
        B=xx*a+yy
        C=x*a+yy
        D=xx*a+y
        # Original incidence is ACROSS A-B and C-D.
        # The two remaining perfect matchings of {A,B,C,D} pair aligned
        # corners, where common-neighbor 2-paths can close the C6.
        J+=_aligned_path_pair_count(graph,A,C,B,D)
        J+=_aligned_path_pair_count(graph,A,D,B,C)
    triple=source_pencil_repeat_three(model,max_edges=max_pencil_edges)
    n3=triple["C6_rep3"]
    if J<3*n3:
        raise AssertionError("three-repeat column incidence deficit")
    single=J-3*n3
    return {"s":model["s"],"a":a,
            "J_repeat_column_antipodal_path_incidence":J,
            "C6_repeat_exact":single+n3,
            "C6_rep1":single,"C6_rep3":n3,
            "C6_rep2_forbidden_by_pattern_theorem":True,
            "rep3_point_pencil_triangles":triple["point_pencil_triangles"],
            "rep3_line_pencil_triangles":triple["line_pencil_triangles"],
            "rep3_all_h_upper":triple["all_h_rep3_upper"],
            "rep3_uniform_o_s6":True,
            "rep1_uniform_o_s6_proved":False,
            "seven_family_S_omega_s6_proved":False}



def aligned_repeat_packing_certificate(model):
    """All-h J<=4V(a-2)^2 via aligned codegree marginal transport.

    For y!=y', sum_x codeg((x,y),(x,y')) <= 2(a-2):
    for each third t, the two ORIGINAL lines labeled {y,t},{y',t}
    meet at most once, and the unique source point label has two
    physical x endpoints. Dual bound fixes x,x' and sums over y.
    Per source line/point, sums of endpoint-products are bounded by
    all unordered physical endpoint pairs, with no independence.
    """
    graph=kikuchi_graph(model)
    a=model["a"]
    V=len(model["left_labels"])
    if len(model["right_labels"])!=V:
        raise ValueError("balanced original point/line sources required")
    by_line=[[] for _ in range(V)]
    by_point=[[] for _ in range(V)]
    for p,l in model["incidences"]:
        by_line[l].append(p)
        by_point[p].append(l)
    r=a-2
    actual_raw=refined_cap=0
    max_marginal=0
    for l,(y,yy) in enumerate(model["right_labels"]):
        c=[len(graph[x*a+y]&graph[x*a+yy]) for x in range(a)]
        total=sum(c)
        if total>2*r or total%2:
            raise AssertionError("original GQ dual-line intersection marginal")
        max_marginal=max(max_marginal,total)
        actual_raw+=sum(c[x]*c[xx] for p in by_line[l]
                        for x,xx in (model["left_labels"][p],))
        refined_cap+=(total*total-sum(v*v for v in c))//2
    for p,(x,xx) in enumerate(model["left_labels"]):
        c=[len(graph[x*a+y]&graph[xx*a+y]) for y in range(a)]
        total=sum(c)
        if total>2*r or total%2:
            raise AssertionError("original GQ point intersection marginal")
        max_marginal=max(max_marginal,total)
        actual_raw+=sum(c[y]*c[yy] for l in by_point[p]
                        for y,yy in (model["right_labels"][l],))
        refined_cap+=(total*total-sum(v*v for v in c))//2
    all_h_cap=4*V*r*r
    if actual_raw>refined_cap or refined_cap>all_h_cap:
        raise AssertionError("all-h aligned source-pencil packing failed")
    return {"aligned_source_raw_products":actual_raw,
            "aligned_marginal_max":max_marginal,
            "J_refined_source_marginal_upper":refined_cap,
            "J_all_h_upper":all_h_cap,
            "J_uniform_O_s6":True}

def report():
    out={"slice":"HYP-105-B3.2-E1-K3-G1",
         "status":"RESTRICTED_THEOREM_C_ANTIPODAL_SOURCE_REPEAT",
         "models":{}}
    for h,scheme,seed in ((1,"lex",None),
                          (1,"reverse-line",None),
                          (2,"random",20261011)):
        model=gq_pair_model(h,scheme,seed)
        key="s%s-%s%s"%(model["s"],scheme,
                        "-"+str(seed) if seed is not None else "")
        out["models"][key]={**antipodal_repeat_certificate(model),
                            **aligned_repeat_packing_certificate(model)}
    return out


if __name__=="__main__":
    print(json.dumps(report(),sort_keys=True,indent=2))
