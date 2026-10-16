"""HYP-105 #230 AA4-AT: UNIQUE genuine-original three-flag Hall via forest.

Actual symplectic generalized quadrangle W(3,s), s=2^h; all source
incidence flag IDs and both globally fixed typed physical injections
from AA4-AS are retained unchanged.

NEW all-h SOURCE theorem: for fixed occupied point/line 3-factor
physical residual multisets, at most ONE three-distinct-original-flag
completion is possible. The induced bipartite original incidence graph
on <=3 distinct residual points and <=3 distinct residual lines has
NO 4- or 6-cycle by the ORIGINAL W(3,s) girth-eight property.
Hence it is a FOREST, including source repetitions B (prescribed
vertex degrees 1 or 2). A fixed degree vector on a forest admits at
most one set of genuine original incidence edges; peel leaves.

This proves a sharp exact BOOL 0/1 source-Hall transfer per globally
occupied two-sided physical residual template pair, NOT a positive
all-map Hall lower. Original accepted GF5 all-seven S=Omega(s^6)
remains OPEN. Synthetic cyclic input is explicitly rejected.
"""
from collections import Counter
from itertools import combinations
from math import comb

from hyp105_issue230_d6aa4as_threeflag_hall_frontier import (
    original_opposite_wedge_context,prepare_original_opposite_wedge,
    occupied_original_threeflag_half,
    _original_threeflag_Hall_completions)
from hyp105_issue230_d6aa4al_global_original_coordinate_transport import (
    _parameters)


def all_h_original_threeflag_forest_unique_certificate(s):
    """Algebraic worst-case ALL-h template & TRUE source Hall capacity.

    Does NOT promise the presence of any original source Hall matching.
    """
    V,d,a=_parameters(s)
    t=comb(a-3,3)
    p=3*comb(a-4,2)
    return dict(
        s=s,V=V,d=d,a=a,
        T_formal_one_typed_residual_templates=t,
        P_formal_one_typed_residual_templates=p,
        TT_formal_two_typed_capacity=t*t,
        TP_formal_two_typed_capacity=t*p,
        PT_formal_two_typed_capacity=p*t,
        PP_formal_two_typed_capacity=p*p,
        max_original_three_new_flag_Hall_Q_PER_OCCUPIED_PAIR=1,
        original_induced_six_source_factor_graph_is_forest=True,
        forest_uniqueness_holds_with_doubled_source_factors=True,
        no_uniform_positive_original_Hall_density_proved=True,
        no_uniform_positive_seven_GF5_coverage_proved=True)


def _genuine_source_forest_degree_problem(
        source_incidence_index,wedge,left_residual,right_residual):
    """Strict six-factor potential source-edge FOREST with prescribed degrees.

    source_incidence_index {(p,l): genuine original flag-ID}, no loops,
    at most 3 distinct original point and line factors each. Exclude
    already pinned real source flags before degree-constrained matching.
    """
    try:
        left=tuple(left_residual[1]);right=tuple(right_residual[1])
    except (IndexError,TypeError,KeyError) as exc:
        raise ValueError("AA4-AS (kind, three original source factor slots,...) required") from exc
    if (len(left)!=3 or len(right)!=3
            or any(type(z)!=int or z<0 for z in left+right)
            or len(tuple(wedge))!=3 or len(set(wedge))!=3):
        raise ValueError("three original typed residual slots and three different pinned source flag IDs required")
    pneed=Counter(left)
    lneed=Counter(right)
    vertices=frozenset((0,p) for p in pneed)|frozenset((1,l) for l in lneed)
    needed={(0,p):k for p,k in pneed.items()}
    needed.update({(1,l):k for l,k in lneed.items()})
    pinned=frozenset(wedge)
    edges={(p,l):source_incidence_index[(p,l)]
           for p in pneed for l in lneed
           if (p,l) in source_incidence_index
           and source_incidence_index[(p,l)] not in pinned}
    if len(set(edges.values()))!=len(edges):
        raise ValueError("genuine source incidence flag IDs must be unique")

    # A genuine GQ has incidence girth 8; an induced bipartite
    # <=3-point+3-line subgraph cannot contain ANY cycle. Check the
    # hypothesis instead of silently accepting a fabricated source graph.
    parent={v:v for v in vertices}
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]
            x=parent[x]
        return x
    for p,l in sorted(edges):
        u,v=(0,p),(1,l)
        ru,rv=find(u),find(v)
        if ru==rv:
            raise ValueError("not a genuine GQ residual forest: original 4- or 6-cycle")
        parent[ru]=rv

    return needed,edges


def unique_original_threeflag_forest_Hall(
        source_incidence_index,wedge,left_residual,right_residual,
        *,with_certificate=False):
    """LEAF-PEEL exact 0/1 ORIGINAL three-new-flag Hall.

    Output canonical genuine six-incidence-ID Q, or None. Works with
    source factor multiplicities (B) and pinned-flag forbidden edges.
    At most THREE original source incidences are required; never
    permutes six physical or original factor slots.
    """
    needed,edges=_genuine_source_forest_degree_problem(
        source_incidence_index,wedge,left_residual,right_residual)
    original_allowed=len(edges)
    selected=[]
    steps=0
    while needed:
        degree=Counter()
        one_edge={}
        for p,l in edges:
            u,v=(0,p),(1,l)
            degree[u]+=1
            degree[v]+=1
            one_edge[u]=(p,l)
            one_edge[v]=(p,l)
        leaves=sorted(v for v in needed if degree[v]<=1)
        if not leaves:
            raise AssertionError("a true source forest must have a leaf")
        v=leaves[0]
        k=degree[v]
        demand=needed[v]
        if demand<0 or demand>k:
            outcome=None
            break
        if k==0:
            del needed[v]
            steps+=1
            continue
        edge=one_edge[v]
        other=(1,edge[1]) if v[0]==0 else (0,edge[0])
        if demand==1:
            if other not in needed:
                raise AssertionError("dangling original source forest edge")
            needed[other]-=1
            selected.append(edges[edge])
        elif demand!=0:
            raise AssertionError("leaf residual degree must be zero or one")
        del edges[edge]
        del needed[v]
        steps+=1
    else:
        outcome=None
        if len(selected)==3 and len(set(selected))==3:
            allflags=tuple(sorted(tuple(wedge)+tuple(selected)))
            if len(set(allflags))==6:
                outcome=allflags
    if with_certificate:
        return dict(
            unique_genuine_original_six_incidence_Q=outcome,
            original_potential_unpinned_source_incidence_forest_edges=original_allowed,
            original_3x3_forest_leaf_elimination_steps=steps,
            original_three_new_source_flag_Hall_unique_0_or_1=True,
            true_source_four_and_six_cycle_absence_REQUIRED=True,
            accepted_original_seven_GF5_NOT_INFERRED=True,
        )
    return outcome


def exact_original_wedge_forest_Hall_audit(
        model,wedge,*,context=None,require_good=True,
        crosscheck_permutation=True):
    """Every SAME-GLOBAL map real original local threeflag occupied template.

    Compare a second, OLD independent 3! permutation source oracle
    when requested. Compute exact per-wedge 0/1 Hall density, but do
    NOT replace current AA4-AS classifier or re-label source factors.
    """
    ctx=context if context is not None else original_opposite_wedge_context(model)
    w=tuple(wedge)
    ports=prepare_original_opposite_wedge(ctx,w,require_good=require_good)
    halves=tuple(occupied_original_threeflag_half(
        ports[side],ctx["a"],ctx["inverses"][side])[0]
        for side in (0,1))
    genuine_index={edge:i for i,edge in enumerate(ctx["inc"])}
    source_Q_to_template={}
    hits=Counter()
    for f in halves[0]:
        for g in halves[1]:
            Q=unique_original_threeflag_forest_Hall(genuine_index,w,f,g)
            if crosscheck_permutation:
                old=_original_threeflag_Hall_completions(genuine_index,w,f,g)
                if old!=(set() if Q is None else {Q}):
                    raise AssertionError("original forest 0/1 leaf-Hall differs from independently existing original 3! slot matching")
            if Q is not None:
                if Q in source_Q_to_template:
                    raise AssertionError("genuine six ORIGINAL flags have two distinct globally mapped residual physical template pairs")
                source_Q_to_template[Q]=(f[0],g[0])
                hits[(f[0],g[0])]+=1
    n=len(halves[0])*len(halves[1])
    if sum(hits.values())>n:
        raise AssertionError("source forest unique Hall exceeds occupied physical pair capacity")
    return dict(
        s=ctx["s"],original_threeflag_wedge=w,
        source_point_threeflag_shape=ports[0]["kind"],
        source_line_threeflag_shape=ports[1]["kind"],
        globally_occupied_two_typed_residual_template_pairs=n,
        original_forest_Hall_positive_occupied_template_pairs=sum(hits.values()),
        original_forest_Hall_zero_occupied_template_pairs=n-sum(hits.values()),
        unique_genuine_original_six_ID_Q_count=len(source_Q_to_template),
        original_Hall_per_two_typed_template_is_ZERO_or_ONE=True,
        original_Hall_Q_to_physical_template_kind=source_Q_to_template,
        original_positive_seven_GF5_count_NOT_INFERRED=True,
    )
