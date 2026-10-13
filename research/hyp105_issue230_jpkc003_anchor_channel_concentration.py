"""JPKC-003: exact ORIGINAL GQ anchor/diagonal blocker concentration.

All equalities J6 and finite cuts J7 are definition-level. The ALL-h
asymptotic conditional alternative J8 is proved in companion note;
NO root A/B theorem or unconditional positive GF5 S is claimed.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb
import argparse
import json

from hyp105_issue230_projection import ProjectionClosure, fixture
from hyp105_issue230_jpkc002_path_collision_taxonomy import (
    _path_fibers, BLOCKED, collision_certificate,
)


def _original_collinear_intersections(ctx):
    """Original physical point/line adjacent-label pairs on GQ neighborhoods."""
    Mf=Mg=0
    for points_on_line in ctx.lines:
        for p,q in combinations(sorted(points_on_line),2):
            Mf+=bool(set(ctx.f[p]) & set(ctx.f[q]))
    for lines_on_point in ctx.point_lines:
        for l,r in combinations(sorted(lines_on_point),2):
            Mg+=bool(set(ctx.g[l]) & set(ctx.g[r]))
    return Mf,Mg


def _occupied_image_cut(labels,a):
    """Classical near-complete Ahlswede-Katona image adjacency bound; D6-Y."""
    V=len(labels)
    K=comb(a,2)
    missing=K-V
    if missing<0 or missing>a-2:
        raise ValueError("minimal physical alphabet / near-complete occupancy required")
    deg=[0]*a
    for x,y in labels:
        deg[x]+=1
        deg[y]+=1
    observed=sum(comb(d,2) for d in deg)
    upper=a*comb(a-1,2)-2*missing*(a-2)+comb(missing,2)
    if observed>upper:
        raise AssertionError("sharp occupied-edge adjacency cut violated")
    return {"observed":observed, "sharp_Ahlswede_Katona_upper":upper,
            "missing_physical_edges":missing, "slack":upper-observed,
            "min_coordinate_occupancy":min(deg),
            "max_coordinate_occupancy":max(deg)}


def _anchors(ctx,fibers):
    """Each nonincident ORIGINAL (q,r) gives two graph diagonal channels."""
    Mf,Mg=_original_collinear_intersections(ctx)
    s,a=ctx.s,ctx.a
    badleft=badright=badboth=0
    records=[]
    for (q,r),(p,l) in ctx.projection.items():
        left=bool(set(ctx.f[q]) & set(ctx.f[p]))
        right=bool(set(ctx.g[r]) & set(ctx.g[l]))
        badleft+=left
        badright+=right
        badboth+=left and right
        x,xp=ctx.f[q]
        y,yp=ctx.g[r]
        diagonals=((x*a+y,xp*a+yp),(x*a+yp,xp*a+y))
        channel=[]
        for u,v in diagonals:
            n=sum(tag in BLOCKED for _,_,tag,_ in fibers.get((u,v),()))
            n_reverse=sum(tag in BLOCKED for _,_,tag,_ in fibers.get((v,u),()))
            if n!=n_reverse:
                raise AssertionError("physical path reversal loses blocker class")
            if left or right:
                # For bad ORIGINAL endpoint anchor, EVERY coordinate-proper
                # simple graph 3-path with these endpoints is blocked.
                if any(tag not in BLOCKED for _,_,tag,_ in fibers.get((u,v),())
                       if tag!="coordinate_repeat"):
                    raise AssertionError("endpoint-blocked GQ anchor admits an unblocked good path")
            channel.append(n)
        b0,b1=channel
        mass=2*(b0+b1)
        falling=2*(b0*(b0-1)+b1*(b1-1))
        if falling!=(mass*mass)//4-mass+(b0-b1)**2:
            raise AssertionError("two-diagonal ORIGINAL anchor identity J6 failed")
        records.append((q,r, bool(left or right),left,right,b0,b1,mass,falling))
    if badleft!=2*s*Mf or badright!=2*s*Mg:
        raise AssertionError("exact ORIGINAL 2s*M collinearity/ concurrency anchor identity failed")
    A=badleft+badright-badboth
    if A!=sum(rec[2] for rec in records):
        raise AssertionError("inclusion-exclusion of original bad anchors failed")
    return records,{
        "M_f_original_collinear":Mf,
        "M_g_original_concurrent":Mg,
        "endpoint_bad_left_original_anchors":badleft,
        "endpoint_bad_right_original_anchors":badright,
        "endpoint_bad_both_original_anchors":badboth,
        "endpoint_bad_union_original_anchors":A,
    }


def _cut(total, capacity):
    if capacity==0:
        if total:
            raise AssertionError("nonzero path count on an empty original anchor region")
        return Fraction(0)
    return Fraction(total*total,capacity)-total


def anchor_concentration_certificate(model,*,max_paths=2_000_000,
                                     compare_pair_ledger=False,
                                     include_anchor_rows=False):
    ctx=ProjectionClosure(model)
    _,fibers,labels=_path_fibers(ctx,max_paths)
    records,original=_anchors(ctx,fibers)
    V,s,a=ctx.v,ctx.s,ctx.a
    N=len(ctx.edges)
    M=V*V-N
    if len(records)!=M:
        raise AssertionError("original nonincident GQ anchor family incomplete")
    Cs=(s-1)*V+(s*s+1)*(a-1)
    if original["M_f_original_collinear"]>Cs or original["M_g_original_concurrent"]>Cs:
        raise AssertionError("PR394 all-h spectral GQ physical collinearity cap violated")

    B=sum(rec[7] for rec in records)
    K=sum(rec[8] for rec in records)
    E=sum(rec[7] for rec in records if rec[2])
    I=B-E
    KE=sum(rec[8] for rec in records if rec[2])
    KI=K-KE
    if B!=sum(labels[t] for t in BLOCKED):
        raise AssertionError("original anchored paths do not exhaust all blocked physical P3")
    delta2=sum((rec[5]-rec[6])**2 for rec in records)
    Ksq=sum(rec[7]**2//4 for rec in records)
    if K!=Ksq-B+delta2:
        raise AssertionError("global all-h J6 diagonal imbalance identity failed")
    anchor_var=Fraction(Ksq)-Fraction(B*B,4*M)
    if anchor_var<0 or K!=Fraction(B*B,4*M)-B+anchor_var+delta2:
        raise AssertionError("two-scale ORIGINAL anchor-variance identity J6 failed")

    A=original["endpoint_bad_union_original_anchors"]
    if A>2*s*(original["M_f_original_collinear"]+
              original["M_g_original_concurrent"]) or A>4*s*Cs:
        raise AssertionError("uniform source endpoint capacity J7 violated")
    if KE<_cut(E,4*A) or KI<_cut(I,4*(M-A)):
        raise AssertionError("region-separated exact-original J7 Cauchy bound violated")
    if K<(_cut(E,4*A)+_cut(I,4*(M-A))):
        raise AssertionError("combined endpoint/internal J7 source bound violated")
    if not all(rec[7]%2==0 and rec[8]%2==0 for rec in records):
        raise AssertionError("ORIGINAL channel reversal implies even mass")
    max_masses=sorted((rec[7] for rec in records),reverse=True)
    out={
        "s":s, "a":a, "V":V, "original_incidences":N,
        "original_nonincident_anchors":M,
        "global_maps_verified":True,
        **original,
        "PR394_uniform_M_f_M_g_cap":Cs,
        "J6_total_blocked_paths":B,
        "J6_total_ordered_blocked_collisions":K,
        "J6_anchor_variance_exact":str(anchor_var),
        "J6_diagonal_imbalance_energy":delta2,
        "J6_base_Cauchy_floor_exact":str(_cut(B,4*M)),
        "J6_anchor_mass_squared_quarter":Ksq,
        "J6_max_anchor_blocked_mass":max(max_masses,default=0),
        "J6_original_anchors_with_nonzero_B":sum(rec[7]>0 for rec in records),
        "J6_exact_identity_verified":True,
        "J7_endpoint_E":E,"J7_internal_only_I":I,
        "J7_endpoint_region_collisions":KE,
        "J7_internal_region_collisions":KI,
        "J7_region_separation_no_mixed_anchor_pairs":True,
        "J7_endpoint_anchor_CS_lower_exact":str(_cut(E,4*A)),
        "J7_internal_anchor_CS_lower_exact":str(_cut(I,4*(M-A))),
        "J7_combined_anchor_CS_lower_exact":
            str(_cut(E,4*A)+_cut(I,4*(M-A))),
        "occupied_point_image":_occupied_image_cut(ctx.f,a),
        "occupied_line_image":_occupied_image_cut(ctx.g,a),
        "new_ASET_exponent":False,
        "root_A_proved":False,
        "root_B_constructed":False,
    }
    if compare_pair_ledger:
        old=collision_certificate(model,max_paths=max_paths)
        if old["J4_blocked_original_P3"]!=B or old["J4_blocked_only_falling2"]!=K:
            raise AssertionError("independent JPKC-002 ordered-pair ledger mismatch")
        if old["J5_original_nonincident_qr_anchors"]!=M:
            raise AssertionError("independent original anchor capacity mismatch")
        if old["J5_anchored_CS_floor_exact"]!=str(_cut(B,4*M)):
            raise AssertionError("J5 and J6 exact endpoint Cauchy floors disagree")
        out["independent_JPKC002_fully_reconciled"]=True
    if include_anchor_rows:
        out["original_anchor_channels"]=[
            {"q":q,"r":r,"endpoint_bad":bad,
             "bad_left":left,"bad_right":right,
             "diagonal_0_paths":b0,"diagonal_1_paths":b1,
             "blocked_paths":mass,"blocked_collisions":falling}
            for q,r,bad,left,right,b0,b1,mass,falling in records
        ]
    return out


def report(*,spread=False):
    records=[]
    for scheme in ("lex","reverse","S68","S72"):
        records.append({"scheme":scheme,**anchor_concentration_certificate(
            fixture(1,scheme),compare_pair_ledger=True)})
    for scheme in ("lex","random"):
        records.append({"scheme":scheme,**anchor_concentration_certificate(
            fixture(2,scheme),compare_pair_ledger=True)})
    if spread:
        from hyp105_issue230_jpkc_spread_adversary import spread_adversary_model
        model,cert=spread_adversary_model(2)
        records.append({"scheme":"D4-true-symplectic-spread",
                        "original_Mf_witness":cert["M_f_original_exact"],
                        **anchor_concentration_certificate(model,compare_pair_ledger=True)})
    return {"scope":"exact ORIGINAL shared-anchor two-channel and source endpoint/internal split",
            "all_h_J6_J7_exact":True,
            "all_h_J8_conditional_necessary_in_docs":True,
            "root_universal_S_omega_s6_PROVED_A":False,
            "records":records}


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--spread",action="store_true")
    args=parser.parse_args()
    print(json.dumps(report(spread=args.spread),indent=2,sort_keys=True))
