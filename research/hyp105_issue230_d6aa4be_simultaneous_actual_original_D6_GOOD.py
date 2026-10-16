"""HYP-105 #230 AA4-BE: ONE ORIGINAL global g with D6 and GOOD simultaneously.

PREDECESSORS (credit; not new):
* #564: any k<=floor(V/1024) injected pinned original LINE images
  admit global GOOD >=s^6/512 after completion (s=2^h,h>=5).
* #566: exact conditional-expectation greedy constructs such a single
  WHOLE ORIGINAL global line mapping under any original source order.
* #548 sibling: any eligible true original sixflag Q can individually be
  D6 repaired <=5 whole-source-line swaps (we DO NOT import #548).

NEW COMPOSITION + independent polynomial source/physical witnesses:
(a) ANY minimal globally occupied V pair-edge support at h>=5 has
    a K6 physical vertex clique. Greedy min-missing-degree selects it:
    at each of first 6 stages min-degree<=floor(2(a-2)/remaining)<3,
    removes <=3 vertices, since a>=261.
(b) ANY six distinct actual original GQ source points have six distinct
    incident ORIGINAL LINE sources: d-regular bipartite incidence Hall.
    Therefore arbitrary global point f admits an eligible original
    six-incidence Q whose six physical point pair edges are a C6.
(c) Given ANY specified eligible original Q and ANY occupied right
    physical support E, choose six right physical C6 edges in E,
    assign them to Q's SIX distinct ORIGINAL line IDs in SAME sixflag
    cyclic order; these SIX whole-original-line-image PINs FORCE
    historical selected seven GF5 D6 on Q under EVERY legal completion.
(d) Since s>=32 implies V>=33825, SIX pins<=floor(V/1024).
    Parent #564 mean and #566 exact greedy create ONE single legal
    complete GLOBAL original line map with D6(Q) and simultaneous
    >=s^6/512 TRUE ORIGINAL physically opposite CLEAN GOOD threeflag
    wedges. No per-Q redraw, no original incidence ID modifications.

ONLY existence/construction of some g; NOT a lower on selected seven GF5
six-Q population for EVERY preexisting fully adversarial f,g, and not
even a claim of >=s^6 selected six-Q on the constructed g.
Finite genuine W32/W34 examples are tests, not all-h h<5 floors.
"""
from itertools import combinations
from fractions import Fraction
from math import isqrt

from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked
from hyp105_issue230_d6aa4bd_exact_adaptive_good_derandomization import (
    constructive_true_original_GOOD_partial_line_completion,
)
from hyp105_issue230_d6aa4bc_robust_pins import (
    certified_robust_pins_envelope,
)


def _valid_image_map(images,physical_alphabet):
    items=tuple(tuple(sorted(e)) for e in images)
    a=physical_alphabet
    if (type(a) is not int or a<6 or
            len(set(items))!=len(items) or
            any(len(x)!=2 or x[0]==x[1] or
                any(type(v) is not int or v<0 or v>=a for v in x)
                for x in items)):
        raise ValueError("full original typed globally injective physical source pair images")
    return items


def six_clique_in_minimal_occupied_original_support(occupied,a):
    """ACTUAL full occupied V-edge original source physical K_a support.

    h>=5 proof: a>=261,m=C(a,2)-V<=a-2.
    During first 6 min-degree picks remaining n>=a-3j;
    2m/n<=2(a-2)/(a-15)<3, so 0,1,2 missing-neighbors
    removed with chosen vertex at every stage. Hence six vertices
    pairwise adjacent in E. No binary-search/random graph heuristic.

    Small true W32/W34 cases are executed and checked, but proof is
    specifically asserted only when a>=261.
    """
    E=_valid_image_map(occupied,a)
    full=set(combinations(range(a),2))
    mset=full-set(E)
    if len(mset)>a-2:
        raise ValueError("original physical V support not minimally near complete")
    missing=[set() for _ in range(a)]
    for u,v in mset:
        missing[u].add(v);missing[v].add(u)
    live=set(range(a));selected=[]
    for j in range(6):
        if not live:raise ValueError("physical support no six-vertex clique")
        v=min(live,key=lambda x:(len(missing[x]&live),x))
        neighbors=missing[v]&live
        if a>=261 and len(neighbors)>2:
            raise AssertionError("all-h original near-complete K_a min-missing-degree lemma")
        selected.append(v)
        live-=neighbors|{v}
    out=tuple(selected)
    if len(set(out))!=6 or any(tuple(sorted(x)) not in set(E)
                               for x in combinations(out,2)):
        raise AssertionError("physical six vertices are NOT a globally occupied K6")
    return out


def actual_true_original_sixflag_left_cycle_order(model,Q):
    """Strict six ACTUAL source incidence IDs, SIX distinct genuine
    original points and six distinct original lines, with physical
    POINT edge-images forming one simple connected C6.

    Return source original Q flag IDs in cyclic point-edge order,
    independently of historical GF5 seven-family classifier.
    """
    s=model["s"];V=(s+1)*(s*s+1);a=model["a"]
    f=_valid_image_map(model["left_labels"],a)
    inc=tuple(tuple(x) for x in model["incidences"])
    if len(f)!=V or len(inc)!=V*(s+1) or len(set(inc))!=len(inc):
        raise ValueError("genuine complete original symplectic source flag model required")
    ids=tuple(Q)
    if (len(ids)!=6 or len(set(ids))!=6 or
            any(type(i) is not int or i<0 or i>=len(inc) for i in ids)):
        raise ValueError("exactly six distinct ORIGINAL incidence flag IDs required")
    pts=[inc[i][0] for i in ids]
    lines=[inc[i][1] for i in ids]
    if len(set(pts))!=6 or len(set(lines))!=6:
        raise ValueError("six distinct original source point AND line factor IDs required")
    if any(not (0<=p<V and 0<=l<V) for p,l in zip(pts,lines)):
        raise ValueError("true original source factor IDs out of bounds")
    edges={i:f[inc[i][0]] for i in ids}
    physical_vertices={v for e in edges.values() for v in e}
    if len(physical_vertices)!=6:
        raise ValueError("true original point physical six edges not on exactly six vertices")
    deg={v:sum(v in e for e in edges.values()) for v in physical_vertices}
    if any(z!=2 for z in deg.values()):
        raise ValueError("original point physical six edges not 2-regular")
    adj={i:tuple(sorted(j for j in ids if j!=i and
                       len(set(edges[i])&set(edges[j]))==1)) for i in ids}
    if any(len(js)!=2 for js in adj.values()):
        raise ValueError("source sixflag physical point cycle not simple C6")
    start=min(ids);order=[start,min(adj[start])]
    while len(order)<6:
        nxt=next((j for j in adj[order[-1]] if j!=order[-2]),None)
        if nxt is None or nxt in order:
            raise ValueError("true original point-side 2factor is disjoint two triangles")
        order.append(nxt)
    if start not in adj[order[-1]]:
        raise ValueError("original physical point C6 not connected")
    return tuple(order)


def all_alphabet_original_sixflag_D6_positional_pattern(model,Q,right_images):
    """Source-true, physical alphabet GENERIC, same six original flag
    positions. Both typed pair-edge images must each form a simple
    connected C6 with six physical coordinates, six distinct physical
    edges, and IDENTICAL 2-regular position adjacency graphs.

    Historical K6 GF5 classification is checked separately only for
    s=2; legacy _half_projection_kind has a hardcoded six-coordinate
    degree vector and MUST NOT be called for K14/higher. This physical
    definition is the D6 channel in the all-h seven GF5 framework.
    """
    inc=tuple(tuple(e) for e in model["incidences"])
    f=tuple(tuple(e) for e in model["left_labels"])
    g=tuple(tuple(e) for e in right_images)
    if len(g)!=len(f) or len(set(g))!=len(g):
        raise ValueError("one globally injected original right factor mapping required")
    ordered=actual_true_original_sixflag_left_cycle_order(model,Q)
    duals=[]
    for image,slot in ((f,0),(g,1)):
        edges=tuple(tuple(sorted(image[inc[i][slot]])) for i in ordered)
        if len(set(edges))!=6:
            return False
        vertices={v for edge in edges for v in edge}
        if len(vertices)!=6:
            return False
        graph={tuple(sorted((i,j))) for i,j in combinations(range(6),2)
               if len(set(edges[i])&set(edges[j]))==1}
        if len(graph)!=6 or any(sum(i in e for e in graph)!=2
                                 for i in range(6)):
            return False
        seen={0};todo=[0]
        while todo:
            i=todo.pop()
            for x,y in graph:
                j=y if x==i else x if y==i else None
                if j is not None and j not in seen:
                    seen.add(j);todo.append(j)
        if len(seen)!=6:
            return False
        duals.append(graph)
    return duals[0]==duals[1]


def choose_genuine_original_Q_from_any_complete_point_f(model):
    """Deterministic actual original Q construction from ANY f:
    choose physical K6 clique, orient connected point C6, and use
    d-regular original incidence Hall (matching of six distinct lines).

    Finite real original W32/W34 source IDs only as executor. For all
    h>=5 the algorithm is mathematical over actual source incidence
    input, not a synthetic high-h GQ.
    """
    s=model["s"];V=(s+1)*(s*s+1);a=model["a"]
    f=_valid_image_map(model["left_labels"],a)
    if len(f)!=V:raise ValueError("point source labels incomplete")
    verts=six_clique_in_minimal_occupied_original_support(f,a)
    left={e:p for p,e in enumerate(f)}
    source_pts=tuple(left[tuple(sorted((verts[j],verts[(j+1)%6])))]
                     for j in range(6))
    inc=tuple(tuple(z) for z in model["incidences"])
    if len(inc)!=V*(s+1) or len(set(inc))!=len(inc):
        raise ValueError("actual original source incidence host incomplete")
    incident=[[] for _ in range(V)]
    idx={}
    for i,(p,l) in enumerate(inc):
        if not (0<=p<V and 0<=l<V):raise ValueError("invalid true original factor")
        incident[p].append(l);idx[(p,l)]=i
    if any(len(v)!=s+1 for v in incident):
        raise ValueError("not genuine original point valency")
    assign={}
    def match(p,seen):
        for l in sorted(incident[p]):
            if l in seen:continue
            seen.add(l)
            if l not in assign or match(assign[l],seen):
                assign[l]=p
                return True
        return False
    for p in source_pts:
        if not match(p,set()):
            raise AssertionError("d-regular original source point-line Hall matching failed")
    inverse={p:l for l,p in assign.items()}
    Q=tuple(idx[(p,inverse[p])] for p in source_pts)
    actual_true_original_sixflag_left_cycle_order(model,Q)
    return Q


def pin_original_D6_and_construct_global_good(model,Q=None, *,
                                               max_steps=None,
                                               source_order=None,
                                               verify_universal_guarantee=True):
    """Materialize SAME one true original original-GQ global g, with an
    actual selected GF5 D6 six-ID Q and GOOD source threeflag wedges.

    High-h >=5 rigorous parent floor applies to six pins; if model
    realistically instantiated, check exact conditional mean too.
    True small W32 complete; W34 optionally only first few steps.
    """
    s=model["s"];V=(s+1)*(s*s+1);a=model["a"]
    f=_valid_image_map(model["left_labels"],a)
    E=_valid_image_map(model["right_labels"],a)
    if len(f)!=V or len(E)!=V:
        raise ValueError("both genuine original typed physical supports must be full V")
    if Q is None:
        Q=choose_genuine_original_Q_from_any_complete_point_f(model)
    ordered=actual_true_original_sixflag_left_cycle_order(model,Q)
    v=six_clique_in_minimal_occupied_original_support(E,a)
    target=tuple(tuple(sorted((v[j],v[(j+1)%6]))) for j in range(6))
    inc=tuple(tuple(x) for x in model["incidences"])
    pins={inc[i][1]:edge for i,edge in zip(ordered,target)}
    if len(pins)!=6 or len(set(pins.values()))!=6:
        raise AssertionError("real ORIGINAL Q six distinct LINE source factor physical images")
    # Any globally complete g extending these pins accepts SAME
    # original six-ID incidence Q as the HISTORICAL GF5 D6 class.
    rest=iter(e for e in E if e not in set(target))
    provisional=tuple(pins[l] if l in pins else next(rest) for l in range(V))
    if set(provisional)!=set(E) or not all_alphabet_original_sixflag_D6_positional_pattern(
            model,Q,provisional):
        raise AssertionError("source sixflag point/line C6 alignment not all-h D6 pattern")
    if s==2 and classify_seven_prechecked(Q,f,provisional,inc)!="D6":
        raise AssertionError("original all-alphabet D6 inconsistent with historical true W32 GF5")
    parent=None
    if verify_universal_guarantee and s>=32:
        if V//1024<6:raise AssertionError("all-h six original LINE pin budget insufficient")
        parent=certified_robust_pins_envelope(s,6)
        if parent["conditional_mean_of_unpinned_GOOD_wedges_lower"]<Fraction(s**6,512):
            raise AssertionError("prior genuine original robust-six-pin GOOD mean lower violated")
    z=constructive_true_original_GOOD_partial_line_completion(
        model,pins,source_order=source_order,max_steps=max_steps,
        verify_all_h_floor=verify_universal_guarantee)
    g=z["completed_GLOBAL_original_line_source_factor_images"]
    selected=None
    if g is not None:
        if not all_alphabet_original_sixflag_D6_positional_pattern(model,Q,g):
            raise AssertionError("six pinned true-original global LINE images lost all-h D6")
        selected="D6"
        if s==2 and classify_seven_prechecked(Q,f,g,inc)!="D6":
            raise AssertionError("historical original K6 GF5 D6 classifier rejects constructed global g")
        if z["completed_true_original_ALL_good_opposite_threeflag_charge"]<z[
                "completed_true_original_FREE_good_opposite_threeflag_charge"]:
            raise AssertionError("true original same global GOOD contribution lost")
        if verify_universal_guarantee and s>=32 and (
            z["completed_true_original_FREE_good_opposite_threeflag_charge"] <
            Fraction(s**6,512)):
            raise AssertionError("parent six-pin GOOD theorem failed")
    return {
        "s":s,"V":V,"source_original_six_distinct_incidence_IDs_Q":tuple(Q),
        "source_original_Q_order_in_point_physical_C6":ordered,
        "real_original_point_f_globally_fixed":True,
        "right_global_occupied_physical_edge_support_preserved":True,
        "six_original_LINE_images_always_pinned_to_ONE_D6_C6":pins,
        "independent_PROVISIONAL_full_original_D6_witness":True,
        "complete_original_line_g_realized":g is not None,
        "historical_seven_GF5_original_six_incidence_Q_class":
            selected if s==2 else None,
        "all_alphabet_original_D6_sixflag_pattern_prechecked":True,
        "all_alphabet_original_D6_sixflag_pattern_completed":
            bool(g is not None and selected=="D6"),
        "all_h_s_greater_2_legacy_K6_classifier_NOT_called":s>2,
        "initial_PINNED_original_GOOD_conditional_mean":
            z["conditional_good_wedge_source_3flag_initial_mean"],
        "complete_GLOBAL_original_GOOD_charge":
            z["completed_true_original_ALL_good_opposite_threeflag_charge"],
        "complete_GLOBAL_unpinned_original_GOOD_charge":
            z["completed_true_original_FREE_good_opposite_threeflag_charge"],
        "actual_global_LINE_factor_images":g,
        "math_parent_s_ge32_six_pin_good_guarantee_exact":parent,
        "all_h_s_ge32_one_GLOBAL_g_supports_D6_and_GOOD_s6_over512":
            bool(g is not None and verify_universal_guarantee and s>=32),
        "NOT_every_adversarial_fully_FIXED_global_g":True,
        "NOT_s6_count_of_historical_GF5_six_Q":True,
        "root_230_A_B_C_OPEN":True,
    }


def all_h_original_sixpin_D6_GOOD_math_certificate(s):
    """All-h parameter-only theorem gate. No huge fake GQ created."""
    if type(s) is not int or s<32 or s&(s-1):
        raise ValueError("all-h simultaneously constructive six-pin theorem requires dyadic s>=32")
    V=(s+1)*(s*s+1);d=s+1
    a=(1+isqrt(1+8*V))//2
    if a*(a-1)//2<V:
        a+=1
    m=a*(a-1)//2-V
    if a<261 or m>a-2 or V//1024<6:
        raise AssertionError("all-h source matching / physical K6 / pin eligibility")
    # At j=0..5, when greedy physical missing-graph min-degree
    # elimination has removed <=3j vertices, min missing-degree
    # <= 2m/(a-3j) < 3. This is a rigorous structural induction.
    if any(2*m>=3*(a-3*j) for j in range(6)):
        raise AssertionError("all-h each original physical source K6 greedy clique step unsupported")
    p=certified_robust_pins_envelope(s,6)
    if p["conditional_mean_of_unpinned_GOOD_wedges_lower"]<Fraction(s**6,512):
        raise AssertionError("parent robust GOOD source guarantee altered")
    return {
        "s":s,"h":s.bit_length()-1,"V":V,"a":a,"missing_E_Ka_edges":m,
        "original_source_d_regular_incidence_Hall_for_six_points":d>=6,
        "any_original_point_f_support_greedy_physical_K6":True,
        "any_original_right_E_support_greedy_physical_K6":True,
        "six_distinct_REAL_original_incidence_ID_matching_exists":True,
        "six_ORIGINAL_LINE_image_pins_satisfy_parent_budget":6<=V//1024,
        "one_GLOBAL_completed_original_g_constructive_D6_Q_and_GOOD":
            True,
        "source_original_GOOD_3flag_lower":
            p["conditional_mean_of_unpinned_GOOD_wedges_lower"],
        "historic_GF5_D6_positive_six_ID_count_at_least_ONE_only":1,
        "source_good_3flag_to_seven_GF5_count_s6_NOT_proved":True,
        "ALL_preexisting_fully_FIXED_g_NOT_proved":True,
        "root_230_A_B_C_OPEN":True,
    }
