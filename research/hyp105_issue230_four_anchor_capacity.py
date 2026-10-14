"""EICE-003-F: four TRUE ORIGINAL GQ anchor source masks and GF5 scope audit.

F1: exact L/R/both typed source-midpoint blocker signatures on real 2x2 NB3.
F2: dichotomy adjacent common-side blocker vs strict alternating checkerboard.
F3: source-closure incidence IDs and SAME-MAP accepted seven-class validator.
F4: known C4 supersaturation (rho^4-O(1/r+1/c)), not a new discovery.

NO universal four-anchor capacity, no bounded-multiplicity GF5 transfer, no
Branch A/B or ASET exponent. All tests run on GitHub-hosted runners.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
import json

from hyp105_issue230_endpoint_energy import EndpointEnergy
from hyp105_issue230_source_plaquettes import (
    OriginalPlaquette, status_of_cell, source_girth_four_by_four,
)
from hyp105_g5e2b3e1b0_seven_signature import (
    R3_CERTIFIED_FLOORS, classify_seven_prechecked, seven_census,
)

SIDES = {0:"0", 1:"L", 2:"R", 3:"B"}


def quartic_c4_lower(r, c, ones):
    """Known bipartite C4 homomorphism CS bound, exact rational arithmetic.

    Returns a probability lower bound for the UNIFORM distinct-rows/columns
    2x2 sampler. Valid for ANY binary r-by-c grid; r,c>=2.
    """
    if (type(r) is not int or type(c) is not int
            or type(ones) is not int or r < 2 or c < 2
            or ones < 0 or ones > r*c):
        raise ValueError("valid binary rectangle parameters required")
    rho = Fraction(ones,r*c)
    value=(rho**4-Fraction(1,r)-Fraction(1,c))*Fraction(r*c,(r-1)*(c-1))
    return max(Fraction(),value)


def blocked_checkerboard_or_adjacent(masks):
    """F2 dichotomy for four simultaneously blocked real paths.

    Ordering is (00,01,10,11); masks 1=left, 2=right, 3=both.
    """
    if len(masks)!=4 or any(mask not in (1,2,3) for mask in masks):
        raise ValueError("four nonempty source-midpoint blocker masks required")
    adjacent=((0,1),(0,2),(1,3),(2,3))
    same=tuple((i,j) for i,j in adjacent if masks[i]&masks[j])
    checkerboard= (not same and
                    tuple(masks) in ((1,2,2,1),(2,1,1,2)))
    if not (same or checkerboard):
        raise AssertionError("four-source blocker covering dichotomy failed")
    return dict(signature="".join(SIDES[m] for m in masks),
                adjacent_same_side_edges=same,
                strict_checkerboard=checkerboard,
                shared_anchor_side=bool(same))


def original_closure(ctx, source_ids, q, r):
    """Exactly 3 PHYSICAL path-source + 3 ORIGINAL GQ anchor incidence IDs."""
    sources=tuple(source_ids)
    if len(sources)!=3 or len(set(sources))!=3:
        raise AssertionError("physical NB3 must have three distinct source IDs")
    if (q,r) not in ctx.anchor:
        raise AssertionError("cannot close without a true nonincident GQ anchor")
    p,ell=ctx.anchor[q,r]
    anchor_edges=((q,ell),(p,ell),(p,r))
    if any(edge not in ctx.edge_id for edge in anchor_edges):
        raise AssertionError("GQ anchor incidence missing from ORIGINAL model")
    anchor_ids=tuple(ctx.edge_id[edge] for edge in anchor_edges)
    six=tuple(sorted(set(sources+anchor_ids)))
    if len(six)>6 or len(six)<3:
        raise AssertionError("invalid source six-position trace")
    tag=None
    checked=len(six)==6 and ctx.s==2
    if checked:
        # This frozen exact seven-class oracle is specifically W32/K6.
        # It uses 6-coordinate arrays internally and MUST NOT be invoked
        # for W34/W38; there None would falsely mean a negative GF5 result.
        tag=classify_seven_prechecked(six,ctx.f,ctx.g,ctx.inc)
    return dict(path_source_ids=sources, anchor_source_ids=anchor_ids,
                distinct_original_incidences=six,
                source_union_size=len(six), certified_seven_class=tag,
                frozen_W32_seven_class_checked=checked)


def _colors_for_source(ctx, ids, factor):
    a=ctx.a
    nbr=[set() for _ in range(a)]
    for e in ids:
        p,l=ctx.inc[e]
        pair=ctx.f[p] if factor==0 else ctx.g[l]
        x,y=pair
        nbr[x].add(y)
        nbr[y].add(x)
    colors=[-1]*a
    for x in range(a):
        if colors[x]!=-1:
            continue
        colors[x]=0
        todo=[x]
        while todo:
            v=todo.pop()
            for w in nbr[v]:
                if colors[w]==-1:
                    colors[w]=1-colors[v]
                    todo.append(w)
                elif colors[w]==colors[v]:
                    return None
    return colors


def find_true_nonvacuous_w32(model, *, max_candidates=100_000):
    """Search full REAL original W32 source for an alternative 5-source square.

    This is NOT the dense asymptotic G* selection. Source IDs and both
    diagonals are retained as a single unit.
    """
    if model["s"]!=2:
        raise ValueError("finite W32 finder only")
    ctx=EndpointEnergy(model)
    candidates=0
    for u,neighbors in enumerate(ctx.adj):
        for v in sorted(neighbors):
            first=sorted(neighbors-{v})
            last=sorted(ctx.adj[v]-{u})
            if len(first)<2 or len(last)<2:
                continue
            for ia,ib in combinations(first,2):
                for ja,jb in combinations(last,2):
                    candidates+=1
                    if candidates>max_candidates:
                        raise ValueError("W32 true source nonvacuity search budget exceeded")
                    ids={
                        ctx.provenance[tuple(sorted((u,v)))],
                        ctx.provenance[tuple(sorted((u,ia)))],
                        ctx.provenance[tuple(sorted((u,ib)))],
                        ctx.provenance[tuple(sorted((v,ja)))],
                        ctx.provenance[tuple(sorted((v,jb)))],
                    }
                    if len(ids)!=5:
                        continue
                    cl=_colors_for_source(ctx,ids,0)
                    cr=_colors_for_source(ctx,ids,1)
                    if cl is None or cr is None:
                        continue
                    try:
                        o=OriginalPlaquette(model,sorted(ids),cl,cr)
                    except ValueError:
                        continue
                    # This is a local source graph; requiring a globally
                    # asymptotic degree certificate here would be invalid.
                    result=o.census(max_paths=100_000,max_plaquettes=2000)
                    if result["original_endpoint_complete_plaquettes"]:
                        return dict(selected=tuple(sorted(ids)),
                                    colors_left=tuple(cl),
                                    colors_right=tuple(cr),
                                    search_candidates=candidates,
                                    plaquettes=result["total_2x2_plaquettes"])
    raise AssertionError("no nonvacuous true ORIGINAL W32 source square found")


class FourAnchorCapacity:
    def __init__(self, model, selected, colors_left, colors_right):
        self.model=model
        self.guard=OriginalPlaquette(model,selected,colors_left,colors_right)
        self.ctx=self.guard.ctx

    def census(self, *, max_plaquettes=250_000, max_paths=500_000,
               independent=True, exact_W32_GF5_index=False,
               max_scope_sets=20_000):
        if (type(max_plaquettes) is not int or max_plaquettes<0 or
                type(max_paths) is not int or max_paths<1 or
                type(max_scope_sets) is not int or max_scope_sets<1):
            raise ValueError("valid finite ORIGINAL source budgets required")
        ctx=self.ctx
        total=proper_complete=eligible=allblocked=0
        squareable=0
        paths=0
        pattern=Counter()
        # F3 direct positive-class counts across individual ORIGINAL
        # six-position canonical closures, not assumed GF5 source transfer.
        corners_seven=Counter()
        degenerate_closures=Counter()
        source_scopes=Counter()
        scope_six_hits=Counter()
        complete_scope_seven_hits=Counter()
        complete_scope_indexed_count=0
        blocked_scopes_without_witness=0
        exact_index=None
        confirmed_index_entries=0
        if exact_W32_GF5_index:
            if ctx.s!=2:
                raise ValueError("global seven-class witness index is W32 only")
            exact_index=seven_census(self.model,independent_checks=False,
                                    witness_sets=True)["sets"]
        z=Fraction()
        weighted_blocked_cells=Fraction()
        sampled_allblocked=Fraction()
        sampled_quartic_floor=Fraction()
        sampled_union_floor=Fraction()
        for u,ns in enumerate(ctx.adj):
            for v in sorted(ns):
                A=sorted(ns-{v})
                B=sorted(ctx.adj[v]-{u})
                r,c=len(A),len(B)
                if not r or not c:
                    continue
                paths+=r*c
                if paths>max_paths:
                    raise ValueError("actual NB3 four-anchor path budget exceeded")
                source_middle=ctx.provenance[tuple(sorted((u,v)))]
                cell={}
                for i,w in enumerate(A):
                    for j,t in enumerate(B):
                        st,q,ln=status_of_cell(ctx,source_middle,w,t)
                        source_path=(
                            ctx.provenance[tuple(sorted((w,u)))],
                            source_middle,
                            ctx.provenance[tuple(sorted((v,t)))]
                        )
                        mask=0
                        closure=None
                        if st in (3,4):
                            p,ell=ctx.anchor[q,ln]
                            p2,ell2=ctx.inc[source_middle]
                            left=bool(set(ctx.f[p])&set(ctx.f[p2]))
                            right=bool(set(ctx.g[ell])&set(ctx.g[ell2]))
                            mask=int(left)+2*int(right)
                            if bool(mask)!=(st==3):
                                raise AssertionError("F1 true source blocker mask does not match EICE-003-E")
                            closure=original_closure(ctx,source_path,q,ln)
                            degenerate_closures[closure["source_union_size"]]+=1
                            if closure["certified_seven_class"]:
                                corners_seven[closure["certified_seven_class"]]+=1
                        cell[i,j]=(st,q,ln,mask,source_path,closure)
                if r<2 or c<2:
                    continue
                squareable+=1
                z+=1
                blocked_cells=sum(cell[i,j][0]==3 for i in range(r) for j in range(c))
                rho=Fraction(blocked_cells,r*c)
                weighted_blocked_cells+=rho
                sampled_quartic_floor+=quartic_c4_lower(r,c,blocked_cells)
                sampled_union_floor+=max(Fraction(),4*rho-3)
                qtotal=r*(r-1)//2*c*(c-1)//2
                for i,k in combinations(range(r),2):
                    for j,l in combinations(range(c),2):
                        total+=1
                        if total>max_plaquettes:
                            raise ValueError("actual ORIGINAL four-anchor plaquette budget exceeded")
                        corners=(cell[i,j],cell[i,l],cell[k,j],cell[k,l])
                        statuses=[a[0] for a in corners]
                        if all(st!=0 for st in statuses):
                            proper_complete+=1
                            # Nonvacuous independent INDEX comparison is
                            # allowed even for squares that are NOT all
                            # blocked. Do not present those motif hits as
                            # four-blocker compensation witnesses.
                            if exact_index is not None:
                                complete_scope_indexed_count+=1
                                scope=set()
                                for corner in corners:
                                    scope.update(corner[4])
                                    q0,r0=corner[1],corner[2]
                                    if (q0,r0) in ctx.anchor:
                                        p0,l0=ctx.anchor[q0,r0]
                                        scope.update((
                                            ctx.edge_id[q0,l0],
                                            ctx.edge_id[p0,l0],
                                            ctx.edge_id[p0,r0],
                                        ))
                                if len(scope)>17:
                                    raise AssertionError("original W32 complete-square scope >17")
                                if len(scope)>=6:
                                    combos=__import__('math').comb(len(scope),6)
                                    if combos>max_scope_sets:
                                        raise ValueError("true GF5 source six-subset scope budget exceeded")
                                    for ids in combinations(sorted(scope),6):
                                        tag=classify_seven_prechecked(ids,ctx.f,ctx.g,ctx.inc)
                                        if exact_index.get(ids)!=tag:
                                            raise AssertionError(
                                                "independent full-W32 seven-index scope mismatch")
                                        confirmed_index_entries+=1
                                        if tag is not None:
                                            complete_scope_seven_hits[tag]+=1
                        if all(st in (3,4) for st in statuses):
                            eligible+=1
                        if not all(st==3 for st in statuses):
                            continue
                        allblocked+=1
                        masks=tuple(a[3] for a in corners)
                        classification=blocked_checkerboard_or_adjacent(masks)
                        pattern[classification["signature"]]+=1
                        # TRUE original 4+4 incidence and its sharp girth 8,
                        # using source IDs of all four actual decoded corners.
                        points=tuple(a[1] for a in corners)
                        lines=tuple(a[2] for a in corners)
                        source_girth_four_by_four(points,lines,ctx.edge_id)
                        # EXACT original provenance footprint is at most
                        # 5 path incidence IDs + 12 GQ anchor incidence IDs.
                        footprint=set()
                        for a in corners:
                            closure=a[5]
                            if closure is None:
                                raise AssertionError("four genuine end-clean anchors required")
                            footprint.update(closure["distinct_original_incidences"])
                        if len(footprint)>17:
                            raise AssertionError("four-anchor ORIGINAL scope exceeds 5+4*3")
                        source_scopes[len(footprint)]+=1
                        # GF5 accepted certificate is observed only when
                        # EXACT SIX DISTINCT ORIGINAL incidence IDs occur
                        # and pass the actual seven-family classifier.
                        if len(footprint)>=6 and ctx.s==2:
                            candidates=__import__('math').comb(len(footprint),6)
                            if candidates>max_scope_sets:
                                raise ValueError("true GF5 source six-subset scope budget exceeded")
                            hits=set()
                            for ids in combinations(sorted(footprint),6):
                                tag=classify_seven_prechecked(ids,ctx.f,ctx.g,ctx.inc)
                                if tag is not None:
                                    if tag not in R3_CERTIFIED_FLOORS:
                                        raise AssertionError("nonaccepted original GF5 class found")
                                    hits.add((ids,tag))
                                    scope_six_hits[tag]+=1
                            if not hits:
                                blocked_scopes_without_witness+=1
                        elif ctx.s==2:
                            blocked_scopes_without_witness+=1
                # In each squareable middle orientation, the uniform
                # distinct-index 2x2 sampler gives exactly the local count.
                local_allblocked=sum(
                    all(cell[ii,jj][0]==3 for ii,jj in
                        ((i,j),(i,l),(k,j),(k,l)))
                    for i,k in combinations(range(r),2)
                    for j,l in combinations(range(c),2))
                sampled_allblocked+=Fraction(local_allblocked,qtotal)
                if (Fraction(local_allblocked,qtotal) <
                        quartic_c4_lower(r,c,blocked_cells)):
                    raise AssertionError("F4 known bipartite C4 supersaturation failed")
        if z:
            if sampled_allblocked<sampled_quartic_floor:
                raise AssertionError("F4 aggregate quartic C4 lower failed")
            if sampled_allblocked<sampled_union_floor:
                raise AssertionError("F4 four-corner union lower failed")
            if sum(pattern.values())!=allblocked:
                raise AssertionError("F2 source blocker signature partition failed")
        if independent:
            prior=self.guard.census(max_paths=max_paths,
                                    max_plaquettes=max_plaquettes)
            if (prior["total_2x2_plaquettes"]!=total or
                    prior["all_four_internally_blocked_plaquettes"]!=allblocked or
                    prior["original_endpoint_complete_plaquettes"]!=proper_complete or
                    prior["eligible_end_clean_plaquettes"]!=eligible):
                raise AssertionError("independent EICE-003-E physical square oracle mismatch")
        # Classification is finite validation only. A positive GF5 set
        # *inside* a scope is not automatically forced by 4 blockers.
        return {
            "status":"RESTRICTED_THEOREM_C",
            "s":ctx.s, "N":ctx.N, "original_source_middle_ids":len(ctx.selected),
            "oriented_squareable_middle_edges":squareable,
            "true_original_2x2_plaquettes":total,
            "all_endpoint_complete_plaquettes":proper_complete,
            "all_four_end_clean_plaquettes":eligible,
            "all_four_blocked_plaquettes":allblocked,
            "observed_blocker_signatures":dict(sorted(pattern.items())),
            "allblocked_original_scope_sizes":dict(sorted(source_scopes.items())),
            "canonical_path_closure_source_sizes":dict(sorted(degenerate_closures.items())),
            "canonical_path_seven_classes":dict(corners_seven),
            "accepted_seven_class_oracle_scope":"W(3,2)/K6 only; W34 IDs not classified",
            "frozen_W32_seven_classifier_available":ctx.s==2,
            "observed_scope_seven_hits":dict(scope_six_hits),
            "complete_source_plaquettes_verified_against_W32_index":complete_scope_indexed_count,
            "complete_source_scope_seven_hits_NOT_compensation":dict(complete_scope_seven_hits),
            "allblocked_scopes_without_seven_hit":blocked_scopes_without_witness,
            "independent_W32_full_seven_index_comparisons":confirmed_index_entries,
            "squareable_uniform_mean_blocked_corner":str(weighted_blocked_cells/z) if z else None,
            "F4_orientation_uniform_allblocked_fraction":str(sampled_allblocked/z) if z else None,
            "F4_known_quartic_lower":str(sampled_quartic_floor/z) if z else None,
            "F4_four_union_lower":str(sampled_union_floor/z) if z else None,
            "F4_quartic_is_standard_C4_supersaturation":True,
            "universal_four_anchor_capacity_proved":False,
            "bounded_multiplicity_GF5_transfer_proved":False,
            "root_Branch_A_proved":False
        }


def report():
    from hyp105_issue230_projection import fixture
    from hyp105_issue230_paired_gstar import paired_gstar
    models=[]
    for scheme in ("lex","reverse","S68","S72"):
        model=fixture(1,scheme)
        reg=paired_gstar(model)
        result=FourAnchorCapacity(
            model,reg["original_incidence_ids"],
            reg["colors_left"],reg["colors_right"]).census()
        result["scheme"]=scheme
        result["source_graph"]="canonical small paired G* (may have zero squares)"
        models.append(result)
    # Guaranteed nonvacuous true-original 2x2 witness, still only finite.
    m=fixture(1,"lex")
    witness=find_true_nonvacuous_w32(m)
    result=FourAnchorCapacity(
        m,witness["selected"],witness["colors_left"],witness["colors_right"]).census(
            exact_W32_GF5_index=True)
    result["scheme"]="lex"
    result["source_graph"]="alternative genuine five-original-incidence paired coherent W32"
    models.append(result)
    return {"status":"RESTRICTED_THEOREM_C","root_A":"OPEN","models":models}


if __name__=="__main__":
    print(json.dumps(report(),indent=2,sort_keys=True))
