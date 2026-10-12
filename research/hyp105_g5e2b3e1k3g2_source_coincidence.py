"""HYP-105 K3-G2: original-source coincidence partition of repeated C6.

All legal globally injective pair labellings of W(3,s), s=2^h.
For each original incidence the two antipodal two-path matchings
contributing to J are split by whether BOTH originating original
points (respectively lines) coincide. Exact identities:

  J = J_same + J_cross
  J_same = sum_{p,l incident} [tau_{g(l)}(G_p)^2
                              + tau_{f(p)}(F_l)^2]
  J_same = 3*C6_rep3 + C6_rep1_local
  C6_rep1 = C6_rep1_local + J_cross
  C6_repeated = J_cross + C6_rep1_local + C6_rep3.
  0 <= J_same <= 4*V*(s+1)^2 = O(s^5) = o(s^6).

G_p and F_l have s+1 physical edges each. τ_e is the number of
triangles containing edge e. Proof of bound: τ_uv^2 <= deg(u)deg(v),
and sum_{uv in E}deg(u)deg(v) <= 1/2(2m)^2 = 2m^2.
These results DO NOT imply J_cross=o(s^6) or seven-family S floor.
"""
from collections import defaultdict
from math import comb
import json

from hyp105_g5e2b3e1k1_kikuchi_c6 import gq_pair_model
from hyp105_g5e2b3e1k3g_repeat_loss import (
    antipodal_repeat_certificate, aligned_repeat_packing_certificate,
)


def pencil_triangle_edge_profile(edges, *, max_edges=64):
    """Exact triangle count at every EDGE of a simple physical pencil."""
    if type(max_edges) is not int or max_edges<0:
        raise ValueError("max_edges must be nonnegative integer")
    if len(edges)>max_edges:
        raise RuntimeError("pencil source-edge budget exceeded")
    neighborhoods=defaultdict(set)
    seen=set()
    for x,y in edges:
        if type(x) is not int or type(y) is not int or x==y:
            raise ValueError("malformed simple pencil edge")
        e=tuple(sorted((x,y)))
        if e in seen:
            raise ValueError("repeated pencil source edge")
        seen.add(e)
        neighborhoods[x].add(y)
        neighborhoods[y].add(x)
    tau={e:len(neighborhoods[e[0]]&neighborhoods[e[1]])
         for e in seen}
    T_num=sum(tau.values())
    if T_num%3:
        raise AssertionError("every triangle has exactly three edges")
    square_sum=sum(v*v for v in tau.values())
    m=len(seen)
    # Independent two-bound proof via d(u)*d(v) weighted over edges.
    weighted_degree_sum=sum(len(neighborhoods[u])*len(neighborhoods[v])
                            for u,v in seen)
    if square_sum>weighted_degree_sum or weighted_degree_sum>2*m*m:
        raise AssertionError("triangle-edge square mass bound violated")
    return {"triangle_count":T_num//3, "tau":tau,
            "sum_triangle_edge_squares":square_sum,
            "sum_triangle_edge_pair_products":weighted_degree_sum,
            "all_graph_upper":2*m*m}


def source_coincidence_certificate(model, *, max_incidence_columns=10000,
                                   max_pencil_edges=64):
    """Exact local vs cross-origin repeated-column ledger, all integer."""
    if type(max_incidence_columns) is not int or max_incidence_columns<0:
        raise ValueError("max_incidence_columns must be nonnegative integer")
    if len(model["incidences"])>max_incidence_columns:
        raise RuntimeError("source incidence-column budget exceeded")
    s,a=model["s"],model["a"]
    V=len(model["left_labels"])
    if len(model["right_labels"])!=V or V!=(s+1)*(s*s+1):
        raise ValueError("balanced W(3,s) required")
    m=s+1
    point_inc=[[] for _ in range(V)]
    line_inc=[[] for _ in range(V)]
    for p,l in model["incidences"]:
        point_inc[p].append(l)
        line_inc[l].append(p)
    if any(len(row)!=m for row in point_inc+line_inc):
        raise ValueError("every source pencil needs exactly s+1 incidences")
    point_profiles=[
        pencil_triangle_edge_profile([model["right_labels"][l]
                                      for l in ls],max_edges=max_pencil_edges)
        for ls in point_inc]
    line_profiles=[
        pencil_triangle_edge_profile([model["left_labels"][p]
                                      for p in ps],max_edges=max_pencil_edges)
        for ps in line_inc]
    J_same=0
    local_single=0
    for p,l in model["incidences"]:
        yedge=tuple(model["right_labels"][l])
        xedge=tuple(model["left_labels"][p])
        ty=point_profiles[p]["tau"][tuple(sorted(yedge))]
        tx=line_profiles[l]["tau"][tuple(sorted(xedge))]
        J_same+=ty*ty+tx*tx
        local_single+=ty*(ty-1)+tx*(tx-1)
    rep3=sum(p["triangle_count"] for p in point_profiles)+sum(
        l["triangle_count"] for l in line_profiles)
    if J_same!=local_single+3*rep3:
        raise AssertionError("self-source triple and local-single partition")
    universal_local_upper=4*V*m*m
    if J_same>universal_local_upper:
        raise AssertionError("all-h O(s^5) self-source bound failed")
    g1=antipodal_repeat_certificate(
        model,max_incidence_columns=max_incidence_columns,
        max_pencil_edges=max_pencil_edges)
    packing=aligned_repeat_packing_certificate(model)
    J=g1["J_repeat_column_antipodal_path_incidence"]
    if rep3!=g1["C6_rep3"] or J_same>J:
        raise AssertionError("source-pencils incompatible with G1 J")
    cross=J-J_same
    if cross+local_single!=g1["C6_rep1"]:
        raise AssertionError("single-repeat source coincidence decomposition")
    if cross+local_single+rep3!=g1["C6_repeat_exact"]:
        raise AssertionError("entire repeated C6 source split")
    if J>packing["J_refined_source_marginal_upper"]:
        raise AssertionError("K3-G1 shared-source marginal upper mismatch")
    return {"s":s,"a":a,"V":V,"J_total":J,
            "J_source_same":J_same,"J_cross_source":cross,
            "C6_rep1_local_pencil_triangle_pairs":local_single,
            "C6_rep1_cross_source":cross,
            "C6_rep3_pencil_triangles":rep3,
            "C6_repeat_total":g1["C6_repeat_exact"],
            "source_same_upper_all_h":universal_local_upper,
            "source_same_uniform_o_s6":True,
            "cross_source_uniform_o_s6_proved":False,
            "J_G1_refined_marginal_upper":packing["J_refined_source_marginal_upper"],
            "J_G1_universal_O_s6_upper":packing["J_all_h_upper"],
            "point_triangle_edge_square_mass":
                sum(p["sum_triangle_edge_squares"] for p in point_profiles),
            "line_triangle_edge_square_mass":
                sum(l["sum_triangle_edge_squares"] for l in line_profiles),
            "all_h_seven_family_S_proved":False}


def report():
    out={"slice":"HYP-105-B3.2-E1-K3-G2-A",
         "status":"RESTRICTED_THEOREM_C_SOURCE_COINCIDENCE_SPLIT",
         "models":{}}
    for h,scheme,seed in ((1,"lex",None),
                          (1,"reverse-line",None),
                          (2,"lex",None),
                          (2,"random",20261011)):
        m=gq_pair_model(h,scheme,seed)
        label="s%s-%s%s"%(m["s"],scheme,
                           "-"+str(seed) if seed is not None else "")
        out["models"][label]=source_coincidence_certificate(m)
    return out


if __name__=="__main__":
    print(json.dumps(report(),sort_keys=True,indent=2))
