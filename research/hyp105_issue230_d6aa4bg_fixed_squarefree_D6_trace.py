"""AA4-BG: EXACT squarefree bicolored matrix trace for FULLY FIXED genuine W(3,s) f,g.

Work in R=Z[x_0..x_(a-1),y_0..y_(a-1)]/(x_i^2,y_j^2).
A_ij=x_(point overlap coordinate)*y_(line overlap coordinate) for
TRUE original bilateral D-compatible distinct original source flags.
Then Tr(A^6)=12*sum_(|I|=|J|=6) D6_(I,J) x_I*y_J.

This identity is for EVERY ALREADY FIXED (f,g), not a random
relabeling, and is the algebraic refinement of EXISTING PR #539
colored-rainbow D-cycle equivalence. It is NOT an original seven-GF5
all-classes theorem nor a solution of #230 A/B/C.
"""
from collections import defaultdict
from itertools import combinations

from hyp105_issue230_d6aa4aq_colored_original_D_cycle import (
    original_bicolored_D_flag_graph,
)


def _graph(model):
    g=original_bicolored_D_flag_graph(model)
    if len(g["inc"])<6:
        raise ValueError("requires actual original six-incidence source flag IDs")
    for i,row in enumerate(g["neighbors"]):
        for j,cp,cl in row:
            if i==j or cp<0 or cl<0 or cp>=g["a"] or cl>=g["a"]:
                raise AssertionError("D edge must join distinct original flags with valid typed pair colors")
            p,l=g["inc"][i]
            q,m=g["inc"][j]
            if p==q or l==m:
                raise AssertionError("D edges require distinct genuine source POINT and LINE factor IDs")
            if cp not in g["left"][p] or cp not in g["left"][q] or (
                cl not in g["right"][l] or cl not in g["right"][m]
            ):
                raise AssertionError("true physical point and line coordinate colors do not match")
    return g


def squarefree_trace_six_dp(model, roots=None):
    """Matrix-power in the commutative square-zero ring by exact sparse DP.

    No simple-cycle check or distinct-source-factor check inside the
    recurrence: both FOLLOW from six squarefree physical colors plus
    the original globally injected physical pair edges (proof in MD).
    Each DP state is (last ORIGINAL flag ID, used physical point color
    mask, used physical line color mask). Multiplicity counts walks.
    """
    g=_graph(model)
    N=len(g["inc"])
    if roots is None:
        selected=tuple(range(N))
        complete=True
    else:
        selected=tuple(roots)
        if len(set(selected))!=len(selected) or any(
            type(i) is not int or i<0 or i>=N for i in selected
        ):
            raise ValueError("choose distinct TRUE source incidence flag root IDs")
        complete=len(selected)==N
    a=g["a"]
    final_coeff=defaultdict(int)
    rooted_closed_walks=0
    state_expansions=0
    # The DAG is over six matrix products, not graph vertices:
    # repeated vertices are deliberately NOT forbidden here.
    for root in selected:
        states={(root,0,0):1}
        for step in range(6):
            nxt=defaultdict(int)
            for (vertex,px,ly),weight in states.items():
                for j,c,e in g["neighbors"][vertex]:
                    pc=1<<c
                    lc=1<<e
                    if (px&pc) or (ly&lc):
                        continue
                    if step==5 and j!=root:
                        continue
                    if step<5 and j==root:
                        # Such an early return cannot yield a 6-edge
                        # squarefree completion with distinct source
                        # factor colors: it uses the root twice,
                        # needing >=4 different incident point/line
                        # colors but each root has exactly two.
                        # Omit for performance; result exact.
                        continue
                    nxt[(j,px|pc,ly|lc)]+=weight
                    state_expansions+=1
            states=nxt
        for (vertex,px,ly),count in states.items():
            if vertex!=root or px.bit_count()!=6 or ly.bit_count()!=6:
                raise AssertionError("squarefree typed closed walk count invalid")
            final_coeff[px,ly]+=count
            rooted_closed_walks+=count
    if complete:
        if rooted_closed_walks%12 or any(x%12 for x in final_coeff.values()):
            raise AssertionError("12 oriented-rooted true-original D6 walks per accepted motif failed")
    return {
        "s":g["s"],"a":a,"true_original_source_flag_vertex_count":N,
        "actual_original_D_undirected_edges":len(g["D_edges"]),
        "sixfold_squarefree_trace_monomials":
            {key:value for key,value in sorted(final_coeff.items())},
        "Tr_A6_squarefree_sum_over_all_typed_degree6_coefficients":
            rooted_closed_walks,
        "accepted_original_six_ID_D6":
            rooted_closed_walks//12 if complete else None,
        "roots_exhaustive":complete,
        "rooted_walks_enumerated_without_explicit_source_simplicity_filter":True,
        "all_original_point_and_LINE_source_factors_in_rainbow_walk_distinct":True,
        "dp_state_expansions":state_expansions,
        "ordinary_sixth_spectral_moment_is_NOT_enough":True,
        "seven_historical_GF5_classes_total_NOT_PROVED":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


def squarefree_trace_six_literal_walks(model, roots=None):
    """INDEPENDENT DFS multiplying square-zero color monomials directly.

    No 6-ID distinct source-factor restrictions. We check each successful
    walk AFTER traversal as an adversarial falsifier of the algebraic
    automatic-distinctness lemma.
    """
    g=_graph(model)
    N=len(g["inc"])
    if roots is None:
        chosen=tuple(range(N))
    else:
        chosen=tuple(roots)
        if any(type(i) is not int or i<0 or i>=N for i in chosen) or len(set(chosen))!=len(chosen):
            raise ValueError("original source flag roots must be distinct")
    hist=defaultdict(int)
    for root in chosen:
        def recurse(last, flags, seen_point_colors, seen_line_colors):
            if len(flags)==7:
                if last!=root:
                    return
                pids=[g["inc"][j][0] for j in flags[:-1]]
                lids=[g["inc"][j][1] for j in flags[:-1]]
                assert len(set(flags[:-1]))==len(set(pids))==len(set(lids))==6, (
                    "algebraic nilpotence failed to force six distinct genuine factor IDs")
                hist[sum(1<<c for c in seen_point_colors),
                     sum(1<<e for e in seen_line_colors)]+=1
                return
            for j,c,e in g["neighbors"][last]:
                if c in seen_point_colors or e in seen_line_colors:
                    continue
                if len(flags)==6 and j!=root:
                    continue
                recurse(j,flags+(j,),seen_point_colors+(c,),seen_line_colors+(e,))
        recurse(root,(root,),(),())
    return dict(hist)


def typed_squarefree_coefficient_witnesses(trace_certificate):
    """Unpack exact (point physical sixcoords, line sixcoords) coefficient counts."""
    a=trace_certificate["a"]
    return tuple(
        (tuple(j for j in range(a) if point_mask & (1<<j)),
         tuple(j for j in range(a) if line_mask & (1<<j)),
         count)
        for (point_mask,line_mask),count in
        trace_certificate["sixfold_squarefree_trace_monomials"].items()
    )


def abstract_squarefree_six_cycle_polynomial():
    """Only a generic ring oracle: abstract uncolored C6 by itself no D6.

    Assign six distinct point colors and six distinct line colors to
    an abstract oriented six-cycle: 12 closed rooted walks survive.
    Collapse just TWO edge point colors: ALL degree-six squarefree
    monomials vanish despite an ordinary uncolored simple C6.
    Not an asserted genuine W(3,s) physical embedding.
    """
    def calc(point, line):
        adjacency=[[] for _ in range(6)]
        for i in range(6):
            j=(i+1)%6
            adjacency[i].append((j,point[i],line[i]))
            adjacency[j].append((i,point[i],line[i]))
        survivors=0
        for root in range(6):
            todo=[(root,0,0,0)]
            while todo:
                u,steps,px,ly=todo.pop()
                if steps==6:
                    survivors+=int(u==root)
                    continue
                for v,c,e in adjacency[u]:
                    if (px>>c)&1 or (ly>>e)&1:continue
                    todo.append((v,steps+1,px|(1<<c),ly|(1<<e)))
        return survivors
    return {"fully_rainbow_trace":calc(tuple(range(6)),tuple(range(6))),
            "point_color_collision_trace":calc((0,1,2,3,4,0),tuple(range(6))),
            "ordinary_uncolored_has_a_simple_C6":True,
            "not_a_genuine_original_W3_model":True}


if __name__=="__main__":
    from hyp105_issue230_projection import fixture
    for scheme in ("lex","reverse","S68","S72"):
        z=squarefree_trace_six_dp(fixture(1,scheme))
        print("AA4BG",scheme,"D6",z["accepted_original_six_ID_D6"],
              "trace",z["Tr_A6_squarefree_sum_over_all_typed_degree6_coefficients"],
              "states",z["dp_state_expansions"])
