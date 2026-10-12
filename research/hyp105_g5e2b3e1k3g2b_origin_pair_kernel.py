"""K3-G2-B: exact original GQ closure tensor, off-diagonal source-pair kernel.

For side=line, T[anchor_line][origin_point] counts physical wedges
on two source lines through that original point, closed by g(anchor_line).
Dual side=point interchanges points/lines. All f/g globally injective.
Jcross is the off-diagonal quadratic source-pair contraction.
"""
from collections import Counter
from itertools import combinations
from math import comb
import json

from hyp105_g5e2b3e1k1_kikuchi_c6 import gq_pair_model
from hyp105_g5e2b3e1k3g2_source_coincidence import source_coincidence_certificate

CLASSES=("both_on_anchor","one_on_anchor",
         "off_anchor_collinear","off_anchor_noncollinear")

def inc_tables(model):
    V=len(model["left_labels"])
    s=model["s"]
    if len(model["right_labels"])!=V or V!=(s+1)*(s*s+1):
        raise ValueError("balanced W(3,s) size needed")
    P=[set() for _ in range(V)]
    L=[set() for _ in range(V)]
    for p,l in model["incidences"]:
        if not(0<=p<V and 0<=l<V) or l in P[p]:
            raise ValueError("invalid original incidence")
        P[p].add(l)
        L[l].add(p)
    if any(len(row)!=s+1 for row in P+L):
        raise ValueError("invalid original GQ degree")
    return P,L

def closure_tensor(model,side="line",max_wedges=2000000):
    if side not in ("line","point"):
        raise ValueError("unknown source side")
    if type(max_wedges) is not int or max_wedges<0:
        raise ValueError("invalid wedge budget")
    P,L=inc_tables(model)
    labels=model["right_labels"] if side=="line" else model["left_labels"]
    pencils=P if side=="line" else L
    V=len(labels)
    a=model["a"]
    inverse={}
    degrees=[0]*a
    for i,(x,y) in enumerate(labels):
        if not(type(x) is int and type(y) is int and 0<=x<y<a):
            raise ValueError("invalid physical source pair")
        if (x,y) in inverse:
            raise ValueError("noninjective original source labels")
        inverse[(x,y)]=i
        degrees[x]+=1
        degrees[y]+=1
    T=[Counter() for _ in range(V)]
    source_wedges=closed=0
    for q,pencil in enumerate(pencils):
        for i,j in combinations(sorted(pencil),2):
            shared=set(labels[i])&set(labels[j])
            if len(shared)!=1:
                continue
            source_wedges+=1
            if source_wedges>max_wedges:
                raise RuntimeError("source wedge budget exceeded")
            u=next(x for x in labels[i] if x not in shared)
            v=next(x for x in labels[j] if x not in shared)
            anchor=inverse.get(tuple(sorted((u,v))))
            if anchor is not None:
                T[anchor][q]+=1
                closed+=1
    host_wedges=sum(comb(d,2) for d in degrees)
    host_upper=a*comb(a-1,2)
    if not closed<=source_wedges<=host_wedges<=host_upper:
        raise AssertionError("shared original wedge capacity violated")
    if any(sum(bucket.values())>a-2 for bucket in T):
        raise AssertionError("source closure physical third-coordinate cap")
    return {"T":T,"closed":closed,"source_wedges":source_wedges,
            "host_wedges":host_wedges,"host_upper":host_upper}

def _bridge(edge_q,edge_r,anchor_labels):
    choices={tuple(sorted((x,y))) for x in edge_q for y in edge_r if x!=y}
    return len(choices & anchor_labels)

def pair_kernel_one_side(model,side,T,P,L,max_pairs):
    original_labels=model["left_labels"] if side=="line" else model["right_labels"]
    pencils=P if side=="line" else L
    anchors=L if side=="line" else P
    groups={k:0 for k in CLASSES}
    exact=same=origin_pair_mass=eligible=number_pairs=0
    kernel_hist=Counter()
    for anchor,bucket in enumerate(T):
        on_anchor=anchors[anchor]
        anchor_edges={tuple(original_labels[z]) for z in on_anchor}
        same+=sum(v*v for q,v in bucket.items() if q in on_anchor)
        for (q,tq),(r,tr) in combinations(sorted(bucket.items()),2):
            number_pairs+=1
            if number_pairs>max_pairs:
                raise RuntimeError("pair kernel budget exceeded")
            weight=tq*tr
            origin_pair_mass+=weight
            k=_bridge(original_labels[q],original_labels[r],anchor_edges)
            if not k:
                continue
            if k>min(4,len(on_anchor)):
                raise AssertionError("four bridge edges maximum")
            contribution=k*weight
            n_on=int(q in on_anchor)+int(r in on_anchor)
            if n_on==2:
                kind="both_on_anchor"
            elif n_on==1:
                kind="one_on_anchor"
            elif pencils[q]&pencils[r]:
                kind="off_anchor_collinear"
            else:
                kind="off_anchor_noncollinear"
            exact+=contribution
            groups[kind]+=contribution
            kernel_hist[k]+=contribution
            eligible+=weight
    cap=min(4,model["s"]+1)*origin_pair_mass
    if exact!=sum(groups.values()) or exact>cap:
        raise AssertionError("off-diagonal source kernel identity failed")
    return {"J_cross":exact,"J_same":same,"geometry":groups,
            "K_weight_histogram":dict(kernel_hist),
            "active_source_pairs":number_pairs,
            "origin_pair_product":origin_pair_mass,
            "candidate_bound":cap,"eligible_pair_product":eligible}

def cross_origin_certificate(model,max_wedges=2000000,max_pairs=2000000):
    if type(max_pairs) is not int or max_pairs<0:
        raise ValueError("invalid pair budget")
    P,L=inc_tables(model)
    right=closure_tensor(model,"line",max_wedges)
    left=closure_tensor(model,"point",max_wedges)
    h=pair_kernel_one_side(model,"line",right["T"],P,L,max_pairs)
    v=pair_kernel_one_side(model,"point",left["T"],P,L,max_pairs)
    prev=source_coincidence_certificate(model)
    cross=h["J_cross"]+v["J_cross"]
    same=h["J_same"]+v["J_same"]
    if cross!=prev["J_cross_source"] or same!=prev["J_source_same"]:
        raise AssertionError("original source-pair vs G2-A oracle discrepancy")
    return {"s":model["s"],"a":model["a"],"V":len(P),
            "J_cross":cross,"J_same":same,
            "cross_origin_candidate_upper":h["candidate_bound"]+v["candidate_bound"],
            "line":{"closure":right["closed"],"source_wedges":right["source_wedges"],
                    "host_wedges":right["host_wedges"],"host_upper":right["host_upper"],**h},
            "point":{"closure":left["closed"],"source_wedges":left["source_wedges"],
                     "host_wedges":left["host_wedges"],"host_upper":left["host_upper"],**v},
            "universal_wedge_O_s9over2":True,
            "universal_cross_o_s6_proved":False,
            "seven_family_S_proved":False}

def report():
    out={"slice":"HYP-105-E1-K3-G2-B","models":{}}
    for h,scheme,seed in ((1,"lex",None),(1,"reverse-line",None),
                          (2,"lex",None),(2,"random",20261011)):
        m=gq_pair_model(h,scheme,seed)
        name="s%s-%s%s"%(m["s"],scheme,str(seed) if seed is not None else "")
        out["models"][name]=cross_origin_certificate(m)
    return out

if __name__=="__main__":
    print(json.dumps(report(),indent=2,sort_keys=True))
