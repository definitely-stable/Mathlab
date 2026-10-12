"""HYP-105 E1-K3-E: exact C4-weighted mixed-codegree regularity ledger.

For one COHERENT original GQ point/line pair-labeling, the mixed book
term B=3 sum_mixed choose(codeg,3) has exact representation
  B=sum_mixed (codeg-2)*choose(codeg,2).
This is an all-h combinatorial identity, NOT an all-h small-book theorem.

New pointwise source-star upper:
  B <= sum_mixed max(min(Cmax,d_u,d_v)-2,0)*choose(codeg,2).
Its degrees are reconstructed directly from ORIGINAL source incidences.
Layer-cake codegree-tail and source-star-tail certificates permit
future GQ-specific joint packing lemmas, but none is claimed here.
"""
from collections import Counter
from fractions import Fraction
from math import comb
import json

from hyp105_g5e2b3e1k1_kikuchi_c6 import gq_pair_model, kikuchi_graph
from hyp105_g5e2b3e1k2_cycle_pattern_weights import four_cycles
from hyp105_g5e2b3e1k3_local_collisions import star_degree_tensor
from hyp105_g5e2b3e1k3c_book_packing import book_moments
from hyp105_g5e2b3e1k3d_mixed_girth8 import (
    c4_free_edge_cap, girth8_moore_edge_cap,
)


def choose2(x):
    return x*(x-1)//2 if x >= 2 else 0


def choose3(x):
    return x*(x-1)*(x-2)//6 if x >= 3 else 0


def mixed_weighted_profile(model, *, max_pairs=40_000,
                           max_c4=40_000, include_histogram=True):
    """A finite exact oracle and all-h conditional source-star certificate.

    The codegree histogram has ONE key per codegree value; weighted
    mass for codegree c is choose(c,2) times number of mixed pairs.
    This is also the total count of C4 diagonal incidences attributed
    to mixed opposite vertex pairs. Each C4 has exactly TWO diagonals.

    A star-degree cap uses only source-incidence reconstructed degrees,
    not a presumed regular/independent physical map. This upper is
    generally too large to close the global HYP-105 issue.
    """
    if type(max_pairs) is not int or max_pairs < 0:
        raise ValueError("max_pairs must be nonnegative integer")
    if type(max_c4) is not int or max_c4 < 0:
        raise ValueError("max_c4 must be nonnegative integer")
    graph = kikuchi_graph(model)
    a, s = model["a"], model["s"]
    n = len(graph)
    if n*(n-1)//2 > max_pairs:
        raise RuntimeError("all vertex-pairs budget exceeded (fail closed)")
    source_deg = star_degree_tensor(model)
    if source_deg != tuple(map(len,graph)):
        raise AssertionError("original source incidence star degrees mismatch")
    r = a-2
    cmax = min(c4_free_edge_cap(r),girth8_moore_edge_cap(r),r*(s+1))
    hist=Counter()
    aligned_m2=aligned_m3=0
    mixed_m1=mixed_m2=mixed_m3=0
    max_observed=0
    max_source_star=0
    source_star_upper=0
    # Exact tail mass indexed by c>=k; star-tail mass indexed by
    # min(deg_u,deg_v,Cmax)>=k. The latter dominates the former.
    exact_tail_diff=Counter()
    star_tail_diff=Counter()
    degree_tail_max=0
    for u in range(n):
        for v in range(u+1,n):
            c=len(graph[u]&graph[v])
            w=choose2(c)
            if u//a==v//a or u%a==v%a:
                aligned_m2+=w
                aligned_m3+=choose3(c)
                continue
            mixed_m1+=c
            mixed_m2+=w
            mixed_m3+=choose3(c)
            if c:
                hist[c]+=1
            max_observed=max(max_observed,c)
            if c>cmax:
                raise AssertionError("mixed girth-eight GQ cap failed")
            starcap=min(cmax,source_deg[u],source_deg[v])
            max_source_star=max(max_source_star,starcap)
            if starcap<c:
                raise AssertionError("source degree cap below actual codegree")
            source_star_upper+=max(0,starcap-2)*w
            if w:
                # Each weighted unit is active at every integer k in
                # [3,c] (for actual book count), or [3,starcap] for
                # the degree-only source-star upper.
                if c>=3:
                    exact_tail_diff[3]+=w
                    exact_tail_diff[c+1]-=w
                if starcap>=3:
                    star_tail_diff[3]+=w
                    star_tail_diff[starcap+1]-=w
                degree_tail_max=max(degree_tail_max,starcap)
    all_c4=(mixed_m2+aligned_m2)//2
    if 2*all_c4 != mixed_m2+aligned_m2:
        raise AssertionError("each C4 has exactly two diagonals")
    if all_c4>max_c4:
        raise RuntimeError("C4 edge-set oracle budget exceeded (fail closed)")
    if all_c4!=len(four_cycles(graph)):
        raise AssertionError("independent C4 census disagrees with codegree")
    if book_moments(graph,a)["book_mixed"]!=3*mixed_m3:
        raise AssertionError("independent K3-C book-moment mismatch")
    exact=star=0
    tail={}
    source_tail={}
    for k in range(3,max(cmax,degree_tail_max)+1):
        exact+=exact_tail_diff[k]
        star+=star_tail_diff[k]
        tail[k]=exact
        source_tail[k]=star
        if exact>star:
            raise AssertionError("C4-weighted source degree tail bound fails")
    layer_exact=sum(tail.values())
    layer_source=sum(source_tail.values())
    actual_book=3*mixed_m3
    if layer_exact!=actual_book or layer_source!=source_star_upper:
        raise AssertionError("tail integral identities fail")
    global_upper=max(0,cmax-2)*mixed_m2
    if actual_book>source_star_upper or source_star_upper>global_upper:
        raise AssertionError("book bound hierarchy fails")
    if mixed_m2:
        kappa=Fraction(2* mixed_m2+actual_book,mixed_m2)
        excess=Fraction(actual_book,mixed_m2)
    else:
        kappa=excess=None
    report={
        "s":s,"a":a,"r":r,"C4":all_c4,
        "source_aligned_M2":aligned_m2,"mixed_M1":mixed_m1,
        "mixed_M2":mixed_m2,"mixed_M3":mixed_m3,
        "B_mixed":actual_book,"B_aligned":3*aligned_m3,
        "Cmax_girth8":cmax,"max_observed_mixed_codegree":max_observed,
        "max_source_star_cap":max_source_star,
        "kappa_mixed_exact":str(kappa) if kappa is not None else None,
        "kappa_excess_exact":str(excess) if excess is not None else None,
        "B_upper_global_girth8":global_upper,
        "B_upper_source_star":source_star_upper,
        "source_star_saving":global_upper-source_star_upper,
        "source_star_upper_is_uniform_o_s6":False,
        "branch_A_or_B_proved":False,
        "C4_weighted_tail":{str(k):v for k,v in tail.items() if v},
        "source_star_upper_tail":{str(k):v for k,v in source_tail.items() if v},
    }
    if include_histogram:
        report["mixed_codegree_pair_histogram"]={str(k):v for k,v in sorted(hist.items())}
        report["mixed_C4_weight_by_codegree"]={
            str(k):v*choose2(k) for k,v in sorted(hist.items()) if k>=2}
    return report


def report():
    out={
        "slice":"HYP-105-B3.2-E1-K3-E",
        "status":"RESTRICTED_THEOREM_C_WEIGHTED_CODEGREE_IDENTITY",
        "universal_Omega_s6_proved":False,
        "models":{},
    }
    for h,scheme,seed in ((1,"lex",None),(1,"reverse-line",None),
                          (1,"random",230),(2,"lex",None),
                          (2,"random",20261011),(2,"random",230)):
        model=gq_pair_model(h,scheme,seed)
        key="s%s-%s%s"%(model["s"],scheme,("-"+str(seed)) if seed is not None else "")
        out["models"][key]=mixed_weighted_profile(model)
    return out


if __name__=="__main__":
    print(json.dumps(report(),indent=2,sort_keys=True))
