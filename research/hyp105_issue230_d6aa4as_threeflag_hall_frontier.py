"""HYP-105 #230 AA4-AS: EXACT REAL ORIGINAL three-flag wedge -> six-GF5 funnel.

True W(3,2^h), all globally fixed complete injected typed physical maps
f,g; no synthetic source factor or per-Q relabeling.

Given REAL original three flags (i,j,k) with centered two AA4-AL
D-compatibility edges j-i and j-k, whose two point physical shared
colors differ AND two line physical shared colors differ, each physical
typed triple consists of THREE distinct original factors:
 (T) physical C3 triangle on 3 coordinates, or
 (P) physical length-three P4 path on 4 coordinates.

To complete six physical degree-two coordinates with THREE additional
genuine ORIGINAL incidence IDs:
 T: unique disjoint triangle on 3 NEW physical coordinates;
    C(a-3,3) formal residual edge multisets.
 P: on 2 NEW coordinates z,w, two path completions
    u-z-w-v and u-w-z-v; OR direct port u-v plus
    doubled physical edge z-w; 3*C(a-4,2) formal residuals.
In a full global physical K6 injection T has ONE physical template
and P has THREE. Both side patterns therefore at most N=9 per wedge,
compared with AA4-AN 100 per genuine original D PAIR.

Use SAME original f and g image inverse to map the remaining 3
physical factor slots into true original source point/line factor
slots; match them via at most 3! original W3s INCIDENCES, check SIX
DISTINCT genuine source incidence-flag IDs. Exact accepted sevenclass
GF5 source Q by historical independent AA4-Q classifier; reject all
unaligned physical original A/A sets, including triangle/triangle.

All-h structural permitted accepted classes from ANY such wedge:
D6, B-left/A-right, A-left/B-right, B/B-overlap ONLY.
C/A,C/B,B/B-disjoint can contain NO centered two-D-edge wedge.

The NEW strong unconditional structural obstruction:
if physical source point-side AND line-side pinned wedge triple are
BOTH triangles T/T, then they extend to ZERO selected positive seven-
GF5 six-Q for ANY complete correlated f,g ALL h: the resulting
two physical 2-factors are both C3+C3, never accepted aligned
connected original D6, independent of source Hall.

No original six-Q acceptance fraction or s^6 lower is assumed.
"""
from collections import Counter
from itertools import combinations,permutations
from math import comb

from hyp105_issue230_d6aa4al_global_original_coordinate_transport import (
    _actual_strict_original_transport,_parameters)
from hyp105_issue230_d6aa4aq_colored_original_D_cycle import (
    original_bicolored_D_flag_graph)
from hyp105_issue230_d6aa4ar_good_wedges_port_balance import (
    _good_D_edge_graph)
from hyp105_issue230_d6aa4an_port_completion_hall_funnel import (
    physical_edge)
from hyp105_issue230_d6aa4am_genuine_pair_sixcharge import (
    _projection_source_type)
from hyp105_issue230_d6aa4q_two_sided_seven_join import (
    independent_joint_classify)


def all_h_threeflag_physical_completion_formula(s):
    """All-h all-global typed capacity (FORMAL, NOT original Hall)."""
    V,d,a=_parameters(s)
    T=comb(a-3,3)
    P=3*comb(a-4,2)
    return dict(s=s,V=V,a=a,
        pinned_three_original_distinct_incidence_flags=True,
        triangle_T_three_new_coordinate_templates=T,
        path_P_two_new_coordinate_templates=P,
        path_P_A_sixcycle_templates=2*comb(a-4,2),
        path_P_B_doubled_source_factor_templates=comb(a-4,2),
        two_typed_max_formal_patterns=max(T,P)**2,
        triangle_triangle_ALL_h_no_positive_original_GF5=True,
        physical_completion_not_actual_original_source_Hall_lower=True)


def _wedge_actual_ports(inc,labels,wedge,side):
    """Classify the exactly THREE pinned globally mapped source factor edges.

    Wedge input (center,outer_low,outer_high), with original bilateral
    D compatibility and complementary physical shared colors already
    established in prepare_original_opposite_wedge.
    """
    c,i,k=wedge
    e0=tuple(labels[inc[c][side]])
    e1=tuple(labels[inc[i][side]])
    e2=tuple(labels[inc[k][side]])
    share1=tuple(set(e0)&set(e1))
    share2=tuple(set(e0)&set(e2))
    if len(share1)!=1 or len(share2)!=1 or share1==share2:
        raise ValueError("original wedge must use opposite distinct typed physical ports")
    port1=next(v for v in e1 if v!=share1[0])
    port2=next(v for v in e2 if v!=share2[0])
    used=frozenset(e0)|frozenset((port1,port2))
    kind="T" if port1==port2 else "P"
    if len(used)!=(3 if kind=="T" else 4):
        raise AssertionError("true global original point/line source image physical triple")
    return dict(kind=kind,
        physical_original_threefactor_edges=(e0,e1,e2),
        pinned_physical_coordinates=tuple(sorted(used)),
        opposite_shared_colors=(share1[0],share2[0]),
        free_ports=(port1,port2),
        originally_distinct_typed_source_factors=True)


def original_opposite_wedge_context(model):
    """Reuse expensive whole genuine-original global D graph for many wedges."""
    s,V,d,a,left,right,inc,np,nl=_actual_strict_original_transport(model)
    G,good,neighbors,badP,badL=_good_D_edge_graph(model)
    if G["inc"]!=inc:
        raise AssertionError("original source flag mismatch")
    return dict(s=s,V=V,d=d,a=a,inc=inc,left=left,right=right,
        G=G,GOOD=good,good_neighbors=neighbors,
        inverses=tuple({tuple(edge):i for i,edge in enumerate(labels)}
                       for labels in (left,right)))


def prepare_original_opposite_wedge(context,wedge,*,require_good=False):
    """Single actual source triple with both typed physical port reversal."""
    inc=context["inc"]
    w=tuple(wedge)
    if (len(w)!=3 or any(type(i)!=int or i<0 or i>=len(inc) for i in w)
            or len(set(w))!=3 or w[1]>=w[2]):
        raise ValueError("real ORIGINAL wedge needs (center,outer_lower,outer_higher)")
    c,i,k=w
    D=context["G"]["D_edges"]
    if tuple(sorted((c,i))) not in D or tuple(sorted((c,k))) not in D:
        raise ValueError("two genuinely original bilateral D edges required")
    if require_good and (tuple(sorted((c,i))) not in context["GOOD"]
                         or tuple(sorted((c,k))) not in context["GOOD"]):
        raise ValueError("both original D edges must have good physical ports")
    ports=tuple(_wedge_actual_ports(inc,labels,w,side)
                for side,labels in enumerate((context["left"],context["right"])))
    if (len({inc[t][0] for t in w})!=3 or
        len({inc[t][1] for t in w})!=3):
        raise AssertionError("true opposite-typed wedge outer source factors repeat")
    return ports


def _threeflag_residuals(ports,a):
    """All 1*T or 3*P formal 3-factor physical multisets, ALL h."""
    kind=ports["kind"]
    used=frozenset(ports["pinned_physical_coordinates"])
    other=tuple(v for v in range(a) if v not in used)
    if kind=="T":
        for x,y,z in combinations(other,3):
            yield "T_A_two_triangles",tuple(sorted((
                physical_edge(x,y),physical_edge(y,z),physical_edge(x,z))))
    elif kind=="P":
        u,v=ports["free_ports"]
        for z,w in combinations(other,2):
            yield "P_A_sixcycle",tuple(sorted((
                physical_edge(u,z),physical_edge(z,w),physical_edge(w,v))))
            yield "P_A_sixcycle",tuple(sorted((
                physical_edge(u,w),physical_edge(w,z),physical_edge(z,v))))
            double=physical_edge(z,w)
            yield "P_B_C4_plus_double",tuple(sorted((
                physical_edge(u,v),double,double)))
    else:
        raise ValueError("unknown genuine opposite wedge typed pattern")


def occupied_original_threeflag_half(ports,a,inv):
    """Globally occupied true typed source factor residual multisets."""
    formal=Counter()
    occupied=Counter()
    residual=[]
    seen=set()
    for kind,edges in _threeflag_residuals(ports,a):
        formal[kind]+=1
        if edges in seen:raise AssertionError("duplicate residual 3-source-factor physical multiset")
        seen.add(edges)
        if any(e not in inv for e in edges):
            continue
        factors=tuple(inv[e] for e in edges)
        residual.append((kind,factors,edges))
        occupied[kind]+=1
    want=(comb(a-3,3) if ports["kind"]=="T"
          else 3*comb(a-4,2))
    if len(seen)!=want or sum(formal.values())!=want:
        raise AssertionError("all-h exactly one T / three P per new physical coordinate choice")
    return tuple(residual),dict(formal),dict(occupied)


def _original_threeflag_Hall_completions(inc_index,wedge,left_factors,right_factors):
    """Three ACTUAL ORIGINAL source-incidence IDs added by 3×3 Hall match."""
    left=left_factors[1]
    right=right_factors[1]
    pinned=set(wedge)
    source_Q=set()
    for perm in set(permutations(right)):
        flags=[]
        for p,l in zip(left,perm):
            q=inc_index.get((p,l))
            if q is None or q in pinned:
                break
            flags.append(q)
        else:
            Q=tuple(sorted(tuple(wedge)+tuple(flags)))
            if len(set(Q))==6:
                source_Q.add(Q)
    return source_Q


def exact_original_opposite_threeflag_six_Q_funnel(
        model,wedge,*,context=None,require_good=False,retain_selected=True):
    """True original T/P per-typed physical → 3x3 source Hall → GF5.

    This is ALL-h exact for ONE specified true opposite wedge, with
    enumeration time proportional to occupied physical template pairs.
    FULL all-wedge scan is practical only for genuine W32.

    For T/T it structurally returns zero selected original six-Q,
    but still executes genuine source Hall to validate rejected A/A.
    """
    ctx=context if context is not None else original_opposite_wedge_context(model)
    w=tuple(wedge)
    ports=prepare_original_opposite_wedge(ctx,w,require_good=require_good)
    assert ctx["s"]==model["s"]
    halves=[occupied_original_threeflag_half(
                ports[side],ctx["a"],ctx["inverses"][side])
            for side in (0,1)]
    typed_patterns=tuple((ports[side]["kind"]) for side in (0,1))
    original_index={edge:i for i,edge in enumerate(ctx["inc"])}
    hall=set()
    selected={}
    rejected=set()
    for f in halves[0][0]:
        for g in halves[1][0]:
            for Q in _original_threeflag_Hall_completions(
                    original_index,w,f,g):
                if Q in hall:continue
                hall.add(Q)
                lk=_projection_source_type(Q,ctx["inc"],0)
                rk=_projection_source_type(Q,ctx["inc"],1)
                tag=independent_joint_classify(
                    Q,lk,rk,ctx["inc"],ctx["left"],ctx["right"])
                if tag is None:
                    if (lk,rk)!=("A","A"):
                        raise AssertionError("non-AA genuine original leafless source Q must be accepted")
                    rejected.add(Q)
                else:
                    if tag not in (
                        "D6","B-left/A-right","A-left/B-right",
                        "B/B-overlap"):
                        raise AssertionError("genuine opposite wedge cannot meet another selected class")
                    selected[Q]=tag
    if len(hall)!=len(rejected)+len(selected):
        raise AssertionError("true source Hall positive seven GF5 and rejected A/A partition")
    if typed_patterns==("T","T") and selected:
        raise AssertionError("triangle/triangle positive GF5 impossible for all-h true original source")
    if typed_patterns[0]=="T" and any(
            tag not in ("A-left/B-right",) for tag in selected.values()):
        raise AssertionError("typed triangle original LEFT allows only A-left/B-right positive")
    if typed_patterns[1]=="T" and any(
            tag not in ("B-left/A-right",) for tag in selected.values()):
        raise AssertionError("typed triangle original RIGHT allows only B-left/A-right positive")
    result=dict(
        s=ctx["s"],actual_original_centered_wedge=w,
        genuine_original_pinned_three_distinct_point_and_line_source_factors=True,
        point_physical_wedge_kind=typed_patterns[0],
        line_physical_wedge_kind=typed_patterns[1],
        physical_triangle_triangle_structurally_positive_GF5_impossible=(
            typed_patterns==("T","T")),
        point_formal_threefactor_patterns=halves[0][1],
        line_formal_threefactor_patterns=halves[1][1],
        point_globally_occupied_threefactor_patterns=halves[0][2],
        line_globally_occupied_threefactor_patterns=halves[1][2],
        physical_two_side_occupied_pattern_pairs=len(halves[0][0])*len(halves[1][0]),
        genuine_original_both_leafless_three_additional_flag_Hall_Q_count=len(hall),
        genuine_original_unaligned_AA_rejected_Q_count=len(rejected),
        genuine_original_positive_selected_seven_GF5_six_Q_count=len(selected),
        genuine_original_seven_tag_histogram=dict(Counter(selected.values())),
        selected_true_original_six_incidence_ID_Q_tags=(
            selected if retain_selected else None),
        original_unaligned_AA_Q=(
            rejected if retain_selected else None),
        all_h_true_source_source_six_ID_GF5_exact_one_wedge_transfer=True,
        all_map_positive_coverage_fraction_NOT_PROVED=True,
    )
    return result


def independent_physical_threeflag_degree_oracle(a,ports):
    """Independent exhaustive multigraph verifier for small physical K_a.

    Enumerates ALL triple-with-repetition physical edge multisets
    with required remaining degrees and EXACT six physical vertices,
    without calling the T/P constructive helper.
    Practical a<=8 only.
    """
    from itertools import combinations_with_replacement
    if a>8 or type(a)!=int:
        raise ValueError("small abstract physical K6-8 only")
    old=tuple(ports["pinned_physical_coordinates"])
    base=Counter(v for e in ports["physical_original_threefactor_edges"]
                 for v in e)
    edges=tuple(combinations(range(a),2))
    out=set()
    for three in combinations_with_replacement(edges,3):
        all_deg=base.copy()
        for e in three:all_deg.update(e)
        if len(all_deg)==6 and all(x==2 for x in all_deg.values()):
            out.add(tuple(three))
    return out
