"""EICE-003-G: exact five-ORIGINAL-source localization and finite adversarial search.

G1 (all h): any true 4-blocked coherent paired-diagonal 2x2 NB3
plaquette survives restriction to its five genuine source incidence IDs.
G2: a global source map with no such locally coherent five-source
configuration cannot have ANY all-blocked plaquettes in a valid G*.
G3: on a high-degree G*, absence forces theta_I^4 <= 2/(d_*-1)
by the earlier standard C4+Jensen bound. Does not prove universal G1
absence, Branch A, or seven-GF5 positive sixset transfer.

Finite exhaustive search is ALWAYS scoped to specific actual original
global maps W32/W34; budgets fail closed and no finite extrapolation.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
import json
import random

from hyp105_issue230_endpoint_energy import EndpointEnergy
from hyp105_issue230_source_plaquettes import (
    OriginalPlaquette, status_of_cell, source_girth_four_by_four
)
from hyp105_issue230_four_anchor_capacity import (
    FourAnchorCapacity, blocked_checkerboard_or_adjacent,
    _colors_for_source
)


def five_source_ids(ctx, u, v, first, last):
    """Exact middle + two on u + two on v true ORIGINAL incidence IDs."""
    if (len(first)!=2 or len(last)!=2 or
            len(set(first))!=2 or len(set(last))!=2 or
            u==v or u in last or v in first):
        raise ValueError("genuine distinct physical 2x2 exterior neighbors required")
    arms=(tuple(sorted((u,v))),
          tuple(sorted((u,first[0]))),
          tuple(sorted((u,first[1]))),
          tuple(sorted((v,last[0]))),
          tuple(sorted((v,last[1]))))
    if any(edge not in ctx.provenance for edge in arms):
        raise ValueError("every physical edge must have TRUE source provenance")
    return tuple(sorted(set(ctx.provenance[edge] for edge in arms)))


def exact_five_source_coherence(model, source_ids, *, ctx=None):
    """Both diagonals + full valid bichromatic/coherent graph on 5 sources.

    Never assert coherence merely from an abstract original GQ projection.
    """
    if ctx is None:
        ctx=EndpointEnergy(model)
    ids=tuple(sorted(source_ids))
    if len(ids)!=5 or len(set(ids))!=5:
        return None
    left=_colors_for_source(ctx,ids,0)
    right=_colors_for_source(ctx,ids,1)
    if left is None or right is None:
        return None
    try:
        original=OriginalPlaquette(model,ids,left,right)
    except (ValueError,AssertionError):
        return None
    return (original,tuple(left),tuple(right))


def conditional_no_local_square_theta_bound(min_active_degree,
                                            count_allblocked_plaquettes):
    """Analytic G3: ONLY when certified complete absence is given.

    The input is a bool (NOT a count to extrapolate from finite tests);
    user must separately prove that no allblocked square exists in the
    SAME actual coherent G* for the full original source assignment.
    """
    if (type(min_active_degree) is not int or min_active_degree<3
            or type(count_allblocked_plaquettes) is not bool):
        raise ValueError("active degree>=3 and exact absence certificate required")
    if count_allblocked_plaquettes:
        raise ValueError("cannot assert no-local-square bound when a witness exists")
    # Previous F6 gives 0 >= theta^4 - 2/(d*-1);
    # store fourth-power upper EXACTLY, avoid floating approximation.
    return dict(theta_I_fourth_power_upper=str(Fraction(2,min_active_degree-1)),
                theta_I_bound_exponent="1/4",
                theorem_scope="IF zero all-blocked true original squares in SAME stationary G*",
                universal_exclusion_of_allblocked_plaquettes_proved=False,
                branch_A_proved=False)


class FiveSourceSearch:
    """Complete true ORIGINAL source physical-middle enumeration with budgets."""

    def __init__(self, model):
        self.model=model
        self.ctx=EndpointEnergy(model)  # complete original source, NOT G*.
        self._coherence_cache={}

    def _coherent(self, ids):
        if ids not in self._coherence_cache:
            self._coherence_cache[ids]=exact_five_source_coherence(
                self.model,ids,ctx=self.ctx)
        return self._coherence_cache[ids]

    def census(self, *, max_middle_orientations=4000,
               max_physical_nb3_cells=3_000_000,
               max_allblocked_candidates=150_000,
               witness_limit=1,
               independent_witness_oracle=True):
        if any(type(x) is not int or x<0 for x in (
                max_middle_orientations,max_physical_nb3_cells,
                max_allblocked_candidates,witness_limit)):
            raise ValueError("nonnegative integer exhaustive source budgets required")
        ctx=self.ctx
        processed_middle=processed_path_cells=0
        raw_blocked_cells=0
        raw_allblocked=0
        distinct_five_source=0
        with_two_cuts=0
        fully_coherent=0
        masks=Counter()
        classifications=Counter()
        witness_rows=[]
        allblocked_by_mid=Counter()
        raw_by_mid=Counter()
        no_block_mid=0
        # Complete ORIGINAL physical graph, all true SOURCE edge IDs retained.
        # Enumerate every oriented physical middle edge. A five-source
        # coherent witness is locally sufficient in ANY larger valid G*.
        for u,nb in enumerate(ctx.adj):
            for v in sorted(nb):
                processed_middle+=1
                if processed_middle>max_middle_orientations:
                    raise ValueError("complete W32/W34 middle-orientation budget exceeded")
                A=sorted(nb-{v})
                B=sorted(ctx.adj[v]-{u})
                nr,nc=len(A),len(B)
                if not nr or not nc:
                    continue
                processed_path_cells+=nr*nc
                if processed_path_cells>max_physical_nb3_cells:
                    raise ValueError("complete original physical NB3 cell budget exceeded")
                e=ctx.provenance[tuple(sorted((u,v)))]
                blocked=[]
                for w in A:
                    flags=[]
                    for z in B:
                        # Full G is NOT coherent; many NB3 are improper.
                        coords=(divmod(w,ctx.a),divmod(u,ctx.a),
                                divmod(v,ctx.a),divmod(z,ctx.a))
                        if (len({x for x,y in coords})!=4 or
                                len({y for x,y in coords})!=4):
                            flags.append(0)
                            continue
                        st,q,r=status_of_cell(ctx,e,w,z)
                        if st!=3:
                            flags.append(0)
                            continue
                        p,ell=ctx.anchor[q,r]
                        p2,ell2=ctx.inc[e]
                        mask=int(bool(set(ctx.f[p]) & set(ctx.f[p2]))) + (
                            2*int(bool(set(ctx.g[ell]) & set(ctx.g[ell2]))))
                        if mask not in (1,2,3):
                            raise AssertionError("genuine source blocked mask absent")
                        raw_blocked_cells+=1
                        flags.append(mask)
                    blocked.append(flags)
                if nr<2 or nc<2:
                    continue
                local_candidate=0
                for i,k in combinations(range(nr),2):
                    common=[j for j in range(nc) if blocked[i][j] and blocked[k][j]]
                    for j,l in combinations(common,2):
                        local_candidate+=1
                        raw_allblocked+=1
                        if raw_allblocked>max_allblocked_candidates:
                            raise ValueError("complete original four-blocker budget exceeded")
                        source_ids=five_source_ids(ctx,u,v,(A[i],A[k]),(B[j],B[l]))
                        if len(source_ids)!=5:
                            continue
                        distinct_five_source+=1
                        coherent=self._coherent(source_ids)
                        if coherent is None:
                            continue
                        with_two_cuts+=1
                        o,cl,cr=coherent
                        # Independent positive witness recheck on restricted
                        # original source graph, including TRUE q,r/anchors.
                        corner_masks=tuple(blocked[ii][jj] for ii,jj in
                                           ((i,j),(i,l),(k,j),(k,l)))
                        cls=blocked_checkerboard_or_adjacent(corner_masks)
                        masks[cls["signature"]]+=1
                        classifications["checkerboard" if cls["strict_checkerboard"]
                                        else "adjacent_common_side"]+=1
                        fully_coherent+=1
                        allblocked_by_mid[e]+=1
                        if len(witness_rows)<witness_limit:
                            corner_sources=[]
                            original_points=[]
                            original_lines=[]
                            for ii,jj in ((i,j),(i,l),(k,j),(k,l)):
                                w,z=A[ii],B[jj]
                                _,q,r=status_of_cell(ctx,e,w,z)
                                p,ell=ctx.anchor[q,r]
                                original_points.append(q)
                                original_lines.append(r)
                                corner_sources.append({
                                    "point":q,"line":r,"anchor_point":p,
                                    "anchor_line":ell,
                                    "left_right_mask":blocked[ii][jj],
                                    "original_path_source_incidence_ids":(
                                        ctx.provenance[tuple(sorted((w,u)))], e,
                                        ctx.provenance[tuple(sorted((v,z)))])
                                })
                            source_girth_four_by_four(
                                original_points,original_lines,ctx.edge_id)
                            if independent_witness_oracle:
                                # The exact five-ID graph must itself
                                # contain the real 4-blocked 2x2 square.
                                independent=FourAnchorCapacity(
                                    self.model,source_ids,cl,cr).census(
                                        max_paths=10_000,max_plaquettes=10_000)
                                if independent["all_four_blocked_plaquettes"]<1:
                                    raise AssertionError(
                                        "independent restricted ORIGINAL source oracle false positive")
                            witness_rows.append({
                                "oriented_middle_vertices":(u,v),
                                "true_middle_source_incidence_id":e,
                                "original_source_incidence_ids":source_ids,
                                "colors_left":cl,"colors_right":cr,
                                "outer_first_vertices":(A[i],A[k]),
                                "outer_last_vertices":(B[j],B[l]),
                                "typed_blocker_class":cls,
                                "four_true_original_anchors":corner_sources,
                                "same_five_source_pair_diagonals":True,
                                "independent_restricted_F_oracle_verified":
                                    independent_witness_oracle,
                            })
                raw_by_mid[e]+=local_candidate
                if not local_candidate:
                    no_block_mid+=1
        return {
            "status":"RESTRICTED_THEOREM_G",
            "scope":"finite EXACT full original W(3,s) global map; exhaustive oriented middle source search under strict budgets",
            "s":ctx.s,"a":ctx.a,
            "original_incidences":ctx.N,
            "physical_edges_full_original":ctx.m,
            "oriented_middle_edges_examined":processed_middle,
            "original_nb3_cells_examined":processed_path_cells,
            "coordinate_proper_internal_blocked_cells":raw_blocked_cells,
            "raw_allfour_blocked_plaquettes_before_coherence":raw_allblocked,
            "raw_allfour_with_five_distinct_original_source_ids":distinct_five_source,
            "locally_coherent_allfour_original_plaquettes":fully_coherent,
            "source_five_subset_cache_size":len(self._coherence_cache),
            "locally_coherent_mask_signatures":dict(sorted(masks.items())),
            "locally_coherent_blocking_channels":dict(classifications),
            "physical_middle_edges_with_no_raw_allfour":no_block_mid,
            "witnesses":witness_rows,
            "finite_map_no_coherent_allblocked_square":fully_coherent==0,
            "universal_all_h_forbidden_five_source_theorem_proved":False,
            "bounded_multiplicity_GF5_transfer_proved":False,
            "branch_A_proved":False,
        }


def report():
    from hyp105_issue230_projection import fixture
    rows=[]
    for scheme in ("lex","reverse","S68","S72"):
        data=FiveSourceSearch(fixture(1,scheme)).census()
        data["scheme"]=scheme
        rows.append(data)
    for scheme in ("lex","random"):
        data=FiveSourceSearch(fixture(2,scheme)).census()
        data["scheme"]=scheme
        rows.append(data)
    return {"status":"RESTRICTED_THEOREM_G","root_A":"OPEN","finite":rows}


if __name__=="__main__":
    print(json.dumps(report(),indent=2,sort_keys=True))
