"""Exact nonincident ORIGINAL GQ anchor-blocking ledger (HYP-105 issue #230).

All paths are in the physical diagonal graph of ONE SAME coherent global
f,g, never independently permuted labelings. The four bit mask types:
  1 = f(projection point) meets FIRST/LAST physical first-coordinate,
  2 = f(projection point) meets one of two INTERNAL first-coordinates,
  4 = g(projection line) meets FIRST/LAST physical second-coordinate,
  8 = g(projection line) meets one of two INTERNAL second-coordinates.

The sixteen mask atoms partition all *nonincident endpoint-complete* proper
oriented 3-paths. The zero atom is precisely the successfully completed
synchronized BB-overlap subclass; all nonzero atoms are anchor-blocked.

No universal upper on blocking, no lower bound on all seven families, and
no proof of either issue #230 Branch A or Branch B is asserted.
"""
from collections import Counter
from itertools import combinations
import json

from hyp105_issue230_projection import ProjectionClosure, fixture


def _bits(label_left, label_right, f_anchor, g_anchor):
    """Independent of path orientation; input endpoint/internal slots explicit."""
    x0,x1,x2,x3=label_left
    y0,y1,y2,y3=label_right
    lf=set(f_anchor)
    lg=set(g_anchor)
    return (
        (1 if lf.intersection((x0,x3)) else 0) |
        (2 if lf.intersection((x1,x2)) else 0) |
        (4 if lg.intersection((y0,y3)) else 0) |
        (8 if lg.intersection((y1,y2)) else 0)
    )


def _original_endpoint_pair_census(core):
    """TRUE original GQ projection and exact all-h s*sum r(r-1) identities."""
    left_bad=set()
    right_bad=set()
    for (q,r),(p,l) in core.projection.items():
        if set(core.f[q]).intersection(core.f[p]):
            left_bad.add((q,r))
        if set(core.g[r]).intersection(core.g[l]):
            right_bad.add((q,r))
    # For left bad: ordered original points q,p on line l, with physical
    # f(q),f(p) sharing one coordinate; choose r thru p other than l.
    l_formula=0
    for points in core.lines:
        degrees=Counter(x for q in points for x in core.f[q])
        l_formula+=core.s*sum(v*(v-1) for v in degrees.values())
    # For right bad: ordered original lines r,l thru point p, choose q
    # on l other than p.  Original dual, not a guessed GQ symmetry.
    r_formula=0
    for lines in core.point_lines:
        degrees=Counter(x for l in lines for x in core.g[l])
        r_formula+=core.s*sum(v*(v-1) for v in degrees.values())
    if (l_formula,r_formula)!=(len(left_bad),len(right_bad)):
        raise AssertionError("actual ORIGINAL endpoints differ from exact s*sum r(r-1)")
    if len(core.projection)!=core.v*(core.v-core.delta):
        raise AssertionError("not complete genuine GQ nonincidence projection")
    return {
        "actual_original_nonincident_endpoint_pairs":len(core.projection),
        "left_endpoint_bad_pair_count":len(left_bad),
        "right_endpoint_bad_pair_count":len(right_bad),
        "union_endpoint_bad_pair_count":len(left_bad|right_bad),
        "joint_endpoint_bad_pair_count":len(left_bad&right_bad),
        "left_original_GQ_ordered_pencil_pair_formula":l_formula,
        "right_true_dual_GQ_ordered_pencil_pair_formula":r_formula,
    },left_bad,right_bad


def anchor_ledger(model, *, max_paths=70_000_000, verify_middle_edges=False):
    core=ProjectionClosure(model)
    a=core.a
    deg=list(map(len,core.adj))
    walk_budget=sum((deg[u]-1)*(deg[v]-1)
                    for u,neighbors in enumerate(core.adj) for v,_ in neighbors)
    if type(max_paths) is not int or max_paths<0 or walk_budget>max_paths:
        raise ValueError("complete and explicitly bounded physical path census required")
    endpoints,left_bad,right_bad=_original_endpoint_pair_census(core)
    masks=[0]*16
    by_pair=Counter()
    per_pair_atoms={}
    totals=Counter()
    # Independently classify every REAL physical path; never import
    # parent census, parent accepted seven-family target, or random mean.
    for v0,neighbors in enumerate(core.adj):
        x0,y0=divmod(v0,a)
        for v1,_ in neighbors:
            x1,y1=divmod(v1,a)
            for v2,_ in core.adj[v1]:
                x2,y2=divmod(v2,a)
                if x2 in (x0,x1) or y2 in (y0,y1):
                    continue
                for v3,_ in core.adj[v2]:
                    x3,y3=divmod(v3,a)
                    if x3 in (x0,x1,x2) or y3 in (y0,y1,y2):
                        continue
                    totals["proper"]+=1
                    q=core.fi.get(tuple(sorted((x0,x3))))
                    r=core.gi.get(tuple(sorted((y0,y3))))
                    if q is None or r is None:
                        totals["missing"]+=1
                        continue
                    if (q,r) in core.edge_id:
                        totals["incident"]+=1
                        continue
                    p,l=core.projection[q,r]
                    mask=_bits((x0,x1,x2,x3),(y0,y1,y2,y3),
                               core.f[p],core.g[l])
                    if bool(mask&1)!=((q,r) in left_bad):
                        raise AssertionError("left endpoint blocking must be PATH-INDEPENDENT")
                    if bool(mask&4)!=((q,r) in right_bad):
                        raise AssertionError("right endpoint blocking must be PATH-INDEPENDENT")
                    masks[mask]+=1
                    by_pair[q,r]+=1
                    if (q,r) not in per_pair_atoms:
                        per_pair_atoms[q,r]=[0]*16
                    per_pair_atoms[q,r][mask]+=1
    nonincident=sum(masks)
    blocked=sum(masks[1:])
    endpoint_only=sum(v for k,v in enumerate(masks) if k and (k&5) and not (k&10))
    internal_only=sum(v for k,v in enumerate(masks) if k and (k&10) and not (k&5))
    endpoint_and_internal=sum(v for k,v in enumerate(masks) if (k&5) and (k&10))
    if endpoint_only+internal_only+endpoint_and_internal!=blocked:
        raise AssertionError("blocked paths not exactly partitioned by 16 mask atoms")
    if totals["proper"]!=totals["missing"]+totals["incident"]+nonincident:
        raise AssertionError("every complete physical path needs exactly one status")
    if any(v%2 for v in masks):
        raise AssertionError("physical path reversal must preserve each four-bit blocking mask")
    weights_bad={pair:v for pair,v in by_pair.items()
                 if pair in left_bad or pair in right_bad}
    weights_good={pair:v for pair,v in by_pair.items()
                  if pair not in left_bad and pair not in right_bad}
    endpoint_bad_weight=sum(weights_bad.values())
    if endpoint_bad_weight!=endpoint_only+endpoint_and_internal:
        raise AssertionError("endpoint bad-pair weighted sum != blocked path mask sum")
    if sum(weights_good.values())!=masks[0]+internal_only:
        raise AssertionError("good endpoint pairs must be zero/internal-only masks")
    # Maximum LOCAL congestion from ONE original (q,r) projection fiber.
    ranked=sorted(by_pair.items(),key=lambda x:(-x[1],x[0]))
    bad_ranked=sorted(weights_bad.items(),key=lambda x:(-x[1],x[0]))
    cross_counts={
        "left_endpoint_paths":sum(v for k,v in enumerate(masks) if k&1),
        "left_internal_paths":sum(v for k,v in enumerate(masks) if k&2),
        "right_endpoint_paths":sum(v for k,v in enumerate(masks) if k&4),
        "right_internal_paths":sum(v for k,v in enumerate(masks) if k&8),
        "exactly_one_block_type":sum(v for k,v in enumerate(masks) if k.bit_count()==1),
        "two_or_more_block_types":sum(v for k,v in enumerate(masks) if k.bit_count()>=2),
        "endpoint_bad_pair_weight":endpoint_bad_weight,
        "left_endpoint_bad_pair_weight":sum(v for pair,v in by_pair.items()
                                             if pair in left_bad),
        "right_endpoint_bad_pair_weight":sum(v for pair,v in by_pair.items()
                                              if pair in right_bad),
        "internal_only_weight":internal_only,
        "endpoint_only_weight":endpoint_only,
        "mixed_endpoint_internal_weight":endpoint_and_internal,
    }
    result={
        "s":core.s,"a":core.a,
        "coherent_global_injections":True,
        "proper_P3":totals["proper"],
        "missing":totals["missing"],
        "incident":totals["incident"],
        "nonincident_endpoint_complete":nonincident,
        "blocked":blocked,
        "unblocked":masks[0],
        "synchronized_BB_overlap_sixsets":masks[0]//2,
        "blocking_bit_names":["left_endpoint","left_internal",
                              "right_endpoint","right_internal"],
        "exact_sixteen_mask_histogram":masks,
        **cross_counts,**endpoints,
        "active_nonincident_endpoint_pairs":len(by_pair),
        "active_endpoint_bad_pairs":len(weights_bad),
        "max_original_endpoint_pair_path_multiplicity":max(by_pair.values(),default=0),
        "max_bad_original_endpoint_pair_path_multiplicity":max(weights_bad.values(),default=0),
        "top_original_pair_path_weights":[{"original_point":q,"original_line":r,
                                          "original_projection_point":core.projection[q,r][0],
                                          "original_projection_line":core.projection[q,r][1],
                                          "endpoint_bad_left":(q,r) in left_bad,
                                          "endpoint_bad_right":(q,r) in right_bad,
                                          "oriented_paths":v,
                                          "sixteen_mask_breakdown":per_pair_atoms[q,r]}
                                         for (q,r),v in ranked[:5]],
        "top_bad_original_pair_path_weights":[{"original_point":q,"original_line":r,
                                              "original_projection_point":core.projection[q,r][0],
                                              "original_projection_line":core.projection[q,r][1],
                                              "endpoint_bad_left":(q,r) in left_bad,
                                              "endpoint_bad_right":(q,r) in right_bad,
                                              "oriented_paths":v,
                                              "sixteen_mask_breakdown":per_pair_atoms[q,r]}
                                             for (q,r),v in bad_ranked[:5]],
        "all_inclusion_exclusion_atoms_exact":True,
        "all_h_blocking_upper_proved":False,
        "universal_S_lower_proved":False,
        "infinite_small_S_construction_proved":False,
    }
    if verify_middle_edges:
        # An algorithmically DIFFERENT enumeration: for each ORIGINAL
        # nonincidence (q,r), pin the four physical endpoint combinations,
        # choose independent H-neighbors from both ends, and test the
        # connecting central H edge. Never traverse the path from v0.
        adjacency=[set(w for w,_ in row) for row in core.adj]
        independent=[0]*16
        for (q,r),(p,l) in core.projection.items():
            u,v=core.f[q]
            x,y=core.g[r]
            for first,last in (((u,x),(v,y)),((u,y),(v,x)),
                               ((v,x),(u,y)),((v,y),(u,x))):
                x0,y0=first
                x3,y3=last
                v0=x0*a+y0
                v3=x3*a+y3
                for v1 in adjacency[v0]:
                    x1,y1=divmod(v1,a)
                    if x1 in (x0,x3) or y1 in (y0,y3):
                        continue
                    for v2 in adjacency[v3]:
                        x2,y2=divmod(v2,a)
                        if (x2 in (x0,x1,x3) or
                                y2 in (y0,y1,y3) or v2 not in adjacency[v1]):
                            continue
                        independent[_bits((x0,x1,x2,x3),(y0,y1,y2,y3),
                                          core.f[p],core.g[l])]+=1
        if independent!=masks:
            raise AssertionError("independent anchored middle-edge oracle disagrees on 16 atoms")
        result["independent_original_endpair_middle_edge_oracle"]=True
    else:
        result["independent_original_endpair_middle_edge_oracle"]=False
    return result


def report():
    records=[]
    for power,schemes in ((1,("lex","reverse","S68","S72")),
                          (2,("lex","random")),
                          (3,("random",))):
        for scheme in schemes:
            row=anchor_ledger(fixture(power,scheme),
                              verify_middle_edges=power<=2)
            reference=ProjectionClosure(fixture(power,scheme)).census()
            for a,b in (("proper_P3","proper_P3"),
                        ("missing","missing"),("incident","incident"),
                        ("blocked","blocked"),("unblocked","unblocked")):
                if row[a]!=reference[b]:
                    raise AssertionError("full independent ORIGINAL projection census mismatch")
            if row["synchronized_BB_overlap_sixsets"]!=reference["synchronized_BBo"]:
                raise AssertionError("true original BB-overlap multiplicity two changed")
            row["scheme"]=scheme
            records.append(row)
    return {"slice":"ISSUE230-PROJECTION-BLOCKING-D1",
            "all_sixteen_masks_physical_coherent":True,
            "exact_endpoint_pair_GQ_identity_both_sides":True,
            "independent_middle_edge_checker_for_W32_W34":True,
            "root_230_Branch_A":"OPEN",
            "root_230_Branch_B":"OPEN",
            "weighted_or_uniform_blocking_theorem":"OPEN",
            "records":records}


if __name__=="__main__":
    print(json.dumps(report(),sort_keys=True,indent=2))
