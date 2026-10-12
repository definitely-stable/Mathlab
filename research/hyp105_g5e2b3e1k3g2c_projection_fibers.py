"""HYP-105 E1-K3-G2-C: GQ projection-fiber refinement of J_cross.

For any anchor line l (dually, point p), every original source off
the anchor has a UNIQUE projection onto one of s+1 anchor sources.
All sources are partitioned into fibers, each with s^2 off-anchor
origins and one anchor origin. Exact seven-class geometry formula
refines K3-G2-B's four classes, with tested cardinalities independent
of arbitrary coherent global physical f,g labellings.

These are exact finite/all-h GQ incidence statements, NOT a uniform
o(s^6) cross-source bound or original seven-family S obstruction.
"""
from collections import Counter
from itertools import combinations
import json

from hyp105_g5e2b3e1k1_kikuchi_c6 import gq_pair_model
from hyp105_g5e2b3e1k3g2b_origin_pair_kernel import (
    CLASSES, inc_tables, closure_tensor, cross_origin_certificate,
)

CLASSES7=(
    "both_on_anchor",
    "one_on_projected",
    "one_on_other",
    "off_samefoot_collinear",
    "off_samefoot_noncollinear",
    "off_differentfoot_collinear",
    "off_differentfoot_noncollinear",
)
COARSE={
    "both_on_anchor":"both_on_anchor",
    "one_on_projected":"one_on_anchor",
    "one_on_other":"one_on_anchor",
    "off_samefoot_collinear":"off_anchor_collinear",
    "off_samefoot_noncollinear":"off_anchor_noncollinear",
    "off_differentfoot_collinear":"off_anchor_collinear",
    "off_differentfoot_noncollinear":"off_anchor_noncollinear",
}

def theoretical_pair_capacities(s):
    """Exact number of ALL unordered original source pairs per anchor."""
    if type(s) is not int or s<2:
        raise ValueError("s must be >=2")
    m=s+1
    return {
        "both_on_anchor":m*s//2,
        "one_on_projected":m*s*s,
        "one_on_other":m*s**3,
        "off_samefoot_collinear":m*s*s*(s-1)//2,
        "off_samefoot_noncollinear":m*s*s*(s*s-s)//2,
        "off_differentfoot_collinear":m*s**4//2,
        "off_differentfoot_noncollinear":m*(s-1)*s**4//2,
    }

def anchored_projection(pencils, on_anchor):
    """Find unique GQ projection using actual ORIGINAL incidence."""
    all_origins=len(pencils)
    on=set(on_anchor)
    foot={}
    fiber=Counter()
    for q in range(all_origins):
        if q in on:
            foot[q]=q
        else:
            near=[t for t in on if pencils[q]&pencils[t]]
            if len(near)!=1:
                raise AssertionError("unique GQ point/line projection failed")
            foot[q]=near[0]
        fiber[foot[q]]+=1
    return foot,fiber

def class_of_pair(q,r,foot,on,pencils):
    """Seven disjoint original GQ source-pair types."""
    on_q=q in on
    on_r=r in on
    if on_q and on_r:
        return "both_on_anchor"
    if on_q!=on_r:
        p=q if on_q else r
        other=r if on_q else q
        return "one_on_projected" if foot[other]==p else "one_on_other"
    same=foot[q]==foot[r]
    coll=bool(pencils[q]&pencils[r])
    if same:
        return "off_samefoot_collinear" if coll else "off_samefoot_noncollinear"
    return ("off_differentfoot_collinear" if coll
            else "off_differentfoot_noncollinear")

def _bridge(left,right,anchor_edges):
    pairs={tuple(sorted((x,y))) for x in left for y in right if x!=y}
    return len(pairs&anchor_edges)

def projection_pair_certificate(model, *, max_pairs=2_000_000,
                                max_wedges=2_000_000,
                                verify_all_geometry=True,
                                max_geometry_pairs=1_000_000):
    """All-source GQ projection theorem and exact K3-G2-B cross contraction."""
    for name,value in (("max_pairs",max_pairs),("max_wedges",max_wedges),
                       ("max_geometry_pairs",max_geometry_pairs)):
        if type(value) is not int or value<0:
            raise ValueError(name+" must be a nonnegative integer")
    P,L=inc_tables(model)
    V=len(P)
    s=model["s"]
    target=theoretical_pair_capacities(s)
    if sum(target.values())!=V*(V-1)//2:
        raise AssertionError("GQ projection class cardinality formula")
    by_side={}
    geometry_pairs_total=0
    for side in ("line","point"):
        # line: point origins projected onto the original anchor line.
        # point: dual line origins projected onto the original anchor point.
        pencils=P if side=="line" else L
        anchors=L if side=="line" else P
        physical=model["left_labels"] if side=="line" else model["right_labels"]
        closure=closure_tensor(model,side,max_wedges=max_wedges)
        weighted=Counter()
        raw=Counter()
        active=Counter()
        all_geometry=Counter()
        crossed=0
        same=0
        repeated=0
        different_foot_mass=0
        same_foot_mass=0
        source_fiber_sizes=set()
        for anchor,T in enumerate(closure["T"]):
            on=anchors[anchor]
            foot,fiber=anchored_projection(pencils,on)
            if len(fiber)!=s+1 or any(val!=s*s+1 for val in fiber.values()):
                raise AssertionError("each complete GQ projection fiber has s²+1 sources")
            source_fiber_sizes.update(fiber.values())
            if verify_all_geometry:
                geometry_pairs_total+=V*(V-1)//2
                if geometry_pairs_total>max_geometry_pairs:
                    raise RuntimeError("full GQ geometry pair budget exceeded")
                for q,r in combinations(range(V),2):
                    all_geometry[class_of_pair(q,r,foot,on,pencils)]+=1
            edge_set={tuple(physical[p]) for p in on}
            total=sum(T.values())
            foot_mass=Counter()
            for q,t in T.items():
                foot_mass[foot[q]]+=t
                if q in on:
                    same+=t*t
            different_foot_mass+=(total*total-
                                  sum(t*t for t in foot_mass.values()))//2
            same_foot_mass+=sum(
                (t*t-sum(n*n for q,n in T.items() if foot[q]==f))//2
                for f,t in foot_mass.items()
            )
            for (q,tq),(r,tr) in combinations(sorted(T.items()),2):
                repeated+=1
                if repeated>max_pairs:
                    raise RuntimeError("active source pair budget exceeded")
                cat=class_of_pair(q,r,foot,on,pencils)
                mul=tq*tr
                raw[cat]+=mul
                active[cat]+=1
                k=_bridge(physical[q],physical[r],edge_set)
                if k:
                    if k>min(4,s+1):
                        raise AssertionError("physical bridge multiplicity exceeds capacity")
                    weighted[cat]+=mul*k
                    crossed+=mul*k
        if verify_all_geometry:
            for cls,count in target.items():
                if all_geometry[cls]!=V*count:
                    raise AssertionError("universal seven-class GQ population mismatch")
        if sum(weighted.values())!=crossed:
            raise AssertionError("seven-class weighted partition incorrect")
        diff=sum(raw[c] for c in CLASSES7 if c.startswith("off_differentfoot"))
        diff+=raw["one_on_other"]
        # one_on_other always has different feet, but both_on_anchor
        # can also have different feet; separate geometry test below.
        if not sum(raw.values())==different_foot_mass+same_foot_mass:
            raise AssertionError("projection-fiber weighted pair split failed")
        if sum(weighted.values())>4*sum(raw.values()):
            raise AssertionError("bridge kernel upper failed")
        by_side[side]={
            "seven_class_weighted":{k:weighted[k] for k in CLASSES7},
            "seven_class_source_pair_products":{k:raw[k] for k in CLASSES7},
            "active_source_pairs":{k:active[k] for k in CLASSES7},
            "total_cross":crossed,"total_same":same,
            "same_foot_source_pair_products":same_foot_mass,
            "different_foot_source_pair_products":different_foot_mass,
            "complete_geometry_counts":(
                {k:all_geometry[k] for k in CLASSES7}
                if verify_all_geometry else None),
            "complete_projection_fiber_size":next(iter(source_fiber_sizes)),
            "source_closure_mass":closure["closed"],
        }
    previous=cross_origin_certificate(model,max_wedges=max_wedges,
                                      max_pairs=max_pairs)
    for side in ("line","point"):
        ours=by_side[side]
        parent=previous[side]
        if ours["total_cross"]!=parent["J_cross"]:
            raise AssertionError("original G2-B source pair kernel not reproduced")
        if ours["total_same"]!=parent["J_same"]:
            raise AssertionError("G2-A source-local diagonal not reproduced")
        for cls in CLASSES:
            actual=sum(ours["seven_class_weighted"][c]
                       for c in CLASSES7 if COARSE[c]==cls)
            if actual!=parent["geometry"][cls]:
                raise AssertionError("projection classes do not refine G2-B")
    if (sum(by_side[x]["total_cross"] for x in by_side)!=previous["J_cross"]
        or sum(by_side[x]["total_same"] for x in by_side)!=previous["J_same"]):
        raise AssertionError("whole-source exact ledger mismatch")
    return {
        "s":s,"V":V,"a":model["a"],
        "all_source_pair_capacities_per_anchor":target,
        "line":by_side["line"],"point":by_side["point"],
        "J_cross_exact":previous["J_cross"],
        "J_same_exact":previous["J_same"],
        "all_h_seven_class_population_theorem":True,
        "all_h_Jcross_o_s6_proved":False,
        "seven_family_S_omega_s6_proved":False,
    }

def report():
    output={"slice":"HYP-105-E1-K3-G2-C",
            "status":"RESTRICTED_THEOREM_C_EXACT_GQ_PROJECTION_FIBERS",
            "models":{}}
    for h,scheme,seed in ((1,"lex",None),(1,"reverse-line",None),
                          (2,"lex",None),(2,"random",20261011)):
        m=gq_pair_model(h,scheme,seed)
        key="s%s-%s%s"%(m["s"],scheme,
                        "-"+str(seed) if seed is not None else "")
        output["models"][key]=projection_pair_certificate(m)
    return output

if __name__=="__main__":
    print(json.dumps(report(),sort_keys=True,indent=2))
