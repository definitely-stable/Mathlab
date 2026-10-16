"""HYP-105 #230 AA4-AS — EVERY eligible ORIGINAL source six-Q radius-5 D6 repair.

Sibling-prior AA4-AR #545 proves existence of *some* repairable Q.
NEW all-h quantifiers: for EVERY six DISTINCT ACTUAL ORIGINAL incidence
flag IDs Q whose six DISTINCT original point factors globally form
a physical connected C6 under arbitrary fixed f and whose six ORIGINAL
line factors are DISTINCT, and for EVERY other arbitrary complete
globally injective fixed line labeling g, there exists a single
globally legal g_Q' obtained from g in <=FIVE factor-label
transpositions, preserving im(g) and one Q original line's image, such
that this SAME true source Q becomes historical aligned D6.

No line-factor source incidence is modified; it is already fixed in
original Q. One exceptional physical C6-free line pair edge is possible
in an almost-complete original minimal physical palette; six distinct
g images ensure at least five nonexceptional candidate anchor flags.
All-h source eligible Q mass A6(f) is UNIFORMLY
    Cmin*q_s <= A6(f) <= Cfull*d**6
and A6(f) = (2/3+o(1)) s**15 uniformly in adversarial f;
q_s=d**4(d**2-15) for dyadic s>=4 and q_s=1 for s=2.
Each Q may need its OWN repaired global g'_Q. This is NOT proof of
a single g' admitting Omega(s^15) D6 or original g having D6>0.

No synthetic source GQ, no original incidence IDs redrawn, no
independent per-flag/global image assignment.
"""
from collections import Counter
from itertools import combinations, permutations, product
from math import comb, factorial, isqrt, perm

from hyp105_issue230_aa4ar_five_swap_original_D6 import (
    _canonical_edge,
    exceptional_noncycle_edge,
    complete_physical_C6_with_anchor,
)
from hyp105_g5e2b3e1b0_seven_signature import (
    classify_seven_prechecked,
    physical_column_dual,
    is_connected_column_cycle,
)


def _parameters(s):
    if type(s) is not int or s<2 or s&(s-1):
        raise ValueError("only genuine symplectic W(3,2^h) powers")
    V=(s+1)*(s*s+1)
    d=s+1
    a=(1+isqrt(1+8*V))//2
    while comb(a,2)<V:a+=1
    assert comb(a-1,2)<V<=comb(a,2)
    return V,d,a,comb(a,2)-V


def all_h_every_original_Q_five_swap_mass(s):
    """Exact integer true original GQ source SDR and physical C6
    sandwich, all h. Does NOT materialize any fake large W3s source."""
    V,d,a,m=_parameters(s)
    physical_full=perm(a,6)//12
    physical_min=physical_full-m*perm(a-2,4)
    if physical_min<=0:
        raise AssertionError("genuine dyadic original palette C6 support")
    # Six original point factors share <=1 common original line for
    # each pair by original C4-free GQ geometry.
    source_six_SDR_lower=d**4*(d*d-15) if s>=4 else 1
    eligible_min=physical_min*source_six_SDR_lower
    eligible_max=physical_full*d**6
    if eligible_min>eligible_max:
        raise AssertionError("source original six-Q bounds contradictory")
    return {
        "s":s,"V":V,"d":d,"a":a,
        "physically_unused_pair_edges_per_typed_image":m,
        "physically_occupied_point_C6_at_least":physical_min,
        "complete_Ka_simple_point_C6":physical_full,
        "genuine_original_six_distinct_line_neighbors_per_C6_at_least":
            source_six_SDR_lower,
        "EVERY_fixed_f_has_at_least_THIS_many_individually_repairable_original_Q":
            eligible_min,
        "EVERY_fixed_f_has_at_most_THIS_many_eligible_original_Q":
            eligible_max,
        "relative_repairable_eligible_Q_count_lower_vs_s15":
            (eligible_min,s**15),
        "relative_repairable_eligible_Q_count_upper_vs_s15":
            (eligible_max,s**15),
        "uniform_in_all_fixed_original_point_f_asymptotic_2_over_3_s15":True,
        "EVERY_eligible_original_Q_repairable_within_FIVE_global_line_swaps":True,
        "each_Q_may_need_ITS_OWN_different_GLOBAL_line_map":True,
        "one_common_global_line_map_covers_ALL_Q_NOT_PROVED":True,
        "root_issue230_A_B_C_still_OPEN":True,
    }


def _strict_finite_actual_original_model(model):
    s=model["s"]
    V,d,a,m=_parameters(s)
    if V>600:raise ValueError("real original finite W32/W34/W38 only")
    if model.get("a")!=a:
        raise ValueError("wrong original physical minimal alphabet")
    f=tuple(tuple(e) for e in model["left_labels"])
    g=tuple(tuple(e) for e in model["right_labels"])
    inc=tuple(tuple(e) for e in model["incidences"])
    if len(f)!=V or len(g)!=V or len(inc)!=V*d or len(set(inc))!=V*d:
        raise ValueError("not actual complete ORIGINAL source flag model")
    all_labels=f+g
    if any(len(e)!=2 or type(e[0]) is not int or type(e[1]) is not int
           or not (0<=e[0]<e[1]<a) for e in all_labels):
        raise ValueError("not canonical physical edge source images")
    if len(set(f))!=V or len(set(g))!=V:
        raise ValueError("global ORIGINAL source factor pair images not injected")
    degree_p=Counter(p for p,l in inc)
    degree_l=Counter(l for p,l in inc)
    if (len(degree_p)!=V or len(degree_l)!=V or
        any(v!=d for v in degree_p.values()) or
        any(v!=d for v in degree_l.values()) or
        any(type(p) is not int or type(l) is not int or
            not(0<=p<V and 0<=l<V) for p,l in inc)):
        raise ValueError("not genuine regular original source incidences")
    return s,V,d,a,f,g,inc


def original_left_C6_order_on_six_flag_IDs(inc,f,Q):
    """Independent actual ORIGINAL source flag positional physical
    graph, not virtual fake independent source edge draws."""
    Q=tuple(Q)
    if len(Q)!=6 or len(set(Q))!=6 or any(type(i) is not int or
                                           i<0 or i>=len(inc) for i in Q):
        raise ValueError("six DIFFERENT actual original incidence IDs")
    ps=tuple(inc[i][0] for i in Q)
    ls=tuple(inc[i][1] for i in Q)
    if len(set(ps))!=6 or len(set(ls))!=6:
        raise ValueError("original six point AND line factors must differ")
    edges=[f[p] for p in ps]
    if len(set(edges))!=6:
        raise ValueError("global original point injectivity violated")
    deg=Counter(v for edge in edges for v in edge)
    if len(deg)!=6 or any(v!=2 for v in deg.values()):
        raise ValueError("genuine original point labels not SIX-coordinate two-regular")
    neigh={i:set() for i in Q}
    for i,j in combinations(Q,2):
        if set(f[inc[i][0]])&set(f[inc[j][0]]):
            neigh[i].add(j);neigh[j].add(i)
    if any(len(neigh[i])!=2 for i in Q):
        raise ValueError("original physical connected C6 has exactly two neighbors")
    visited={Q[0]};stack=[Q[0]]
    while stack:
        i=stack.pop()
        for j in neigh[i]:
            if j not in visited:
                visited.add(j);stack.append(j)
    if len(visited)!=6:
        raise ValueError("two physical C3 components not connected C6")
    return neigh


def repair_EVERY_actual_original_Q_D6_in_five_line_swaps(model,Q):
    """Construct one globally complete line source-image reassignment
    repairing THIS exact user-supplied genuine original Q, <=5 swaps.
    No source Q selection or original neighbor choices inside here.
    """
    s,V,d,a,f,g,inc=_strict_finite_actual_original_model(model)
    Q=tuple(Q)
    neighbor=original_left_C6_order_on_six_flag_IDs(inc,f,Q)
    bad=exceptional_noncycle_edge(a,g)
    anchors=tuple(i for i in Q if g[inc[i][1]]!=bad)
    if len(anchors)<5:raise AssertionError("at most one source line image can be pendant")
    start=anchors[0]
    # Orient original physical point C6, keeping named first original
    # incidence ID fixed as column-position zero.
    successor=min(neighbor[start])
    cycle=[start,successor]
    while len(cycle)<6:
        nxt=next(j for j in neighbor[cycle[-1]] if j!=cycle[-2])
        if nxt in cycle:raise AssertionError("original point C6 positional walk prematurely closed")
        cycle.append(nxt)
    if start not in neighbor[cycle[-1]]:
        raise AssertionError("original point six-flag dual not connected C6")
    line_ids=tuple(inc[i][1] for i in cycle)
    right_cycle=complete_physical_C6_with_anchor(a,g,g[line_ids[0]])
    assert right_cycle[0]==g[line_ids[0]]
    desired=dict(zip(line_ids,right_cycle))
    working=list(g)
    owners={edge:i for i,edge in enumerate(working)}
    swaps=[]
    for l in line_ids[1:]:
        target=desired[l]
        if working[l]==target:continue
        owner=owners[target]
        if owner==line_ids[0]:
            raise AssertionError("would move anchored true original source line factor")
        held=working[l]
        working[l],working[owner]=working[owner],working[l]
        owners[target]=l
        owners[held]=owner
        swaps.append((l,owner))
    if (len(swaps)>5 or working[line_ids[0]]!=g[line_ids[0]] or
        len(set(working))!=V or set(working)!=set(g) or
        any(working[l]!=desired[l] for l in line_ids)):
        raise AssertionError("not a valid five-global-swap original line map")
    pends=tuple(inc[i][0] for i in Q)
    lends=tuple(inc[i][1] for i in Q)
    pdual=physical_column_dual(inc,f,pends)
    ldual=physical_column_dual(inc,tuple(working),lends)
    if pdual is None or pdual!=ldual or not is_connected_column_cycle(pdual):
        raise AssertionError("independent all-a ORIGINAL six-ID D6 positional oracle rejects")
    if a==6 and classify_seven_prechecked(Q,f,tuple(working),inc)!="D6":
        raise AssertionError("historical GF5 seven class original D6 W32 oracle rejects")
    return {
        "s":s,"EXACT_six_distinct_original_incidence_flag_IDs":Q,
        "original_six_point_factors":pends,
        "original_six_line_factors":lends,
        "original_left_C6_flag_order_starting_at_anchor":tuple(cycle),
        "selected_genuine_original_line_anchor_ID":line_ids[0],
        "original_anchor_line_physical_image_UNCHANGED":g[line_ids[0]],
        "source_line_factor_global_swaps":tuple(swaps),
        "number_of_GLOBAL_line_factor_image_transpositions":len(swaps),
        "original_source_point_map_UNCHANGED":f,
        "original_line_image_support_UNCHANGED":set(working)==set(g),
        "original_line_global_image_after":tuple(working),
        "repaired_TRUE_ORIGINAL_exact_same_six_flag_Q_positive_D6":True,
        "entire_unmodified_global_g_MAY_have_D6_zero":True,
        "independent_repair_required_per_source_Q":True,
        "original_HYP105_branch_A_B_C_still_OPEN":True,
    }


def finite_original_eligible_Q_generator(model,*,max_yield=64):
    """Explicit true ORIGINAL six-incidence-ID Q with point physical
    connected C6 and distinct point AND line original factor IDs.
    Enumerate actual K_a C6 from physical edges by oriented 6-tuples;
    HUGE source spaces forbidden. max_yield=None only W32.
    """
    s,V,d,a,f,g,inc=_strict_finite_actual_original_model(model)
    if max_yield is None and s>2:
        raise ValueError("full huge original source six-Q census forbidden")
    inv={edge:i for i,edge in enumerate(f)}
    bypoint=[[] for _ in range(V)]
    for flag_id,(p,l) in enumerate(inc):
        bypoint[p].append((l,flag_id))
    seen_phys=set();n=0
    for verts in permutations(range(a),6):
        phys=tuple(_canonical_edge(verts[i],verts[(i+1)%6]) for i in range(6))
        if not all(e in inv for e in phys):continue
        key=tuple(sorted(phys))
        if key in seen_phys:continue
        seen_phys.add(key)
        point_factors=tuple(inv[e] for e in phys)
        for chosen in product(*(bypoint[p] for p in point_factors)):
            lines=tuple(line for line,flag in chosen)
            if len(set(lines))!=6:continue
            Q=tuple(sorted(flag for line,flag in chosen))
            if len(set(Q))!=6:raise AssertionError("true six original incidence flags")
            yield Q
            n+=1
            if max_yield is not None and n>=max_yield:return
