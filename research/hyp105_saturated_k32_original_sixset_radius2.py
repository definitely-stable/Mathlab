"""HYP-105 #230 AA4-K32R2: sharp two-original-flag distance exclusion.

In a source-ID coherent physical graph after BOTH coordinate cuts of
#659, every K3,2 with three hubs and two right vertices, all physically
coordinate-distinct on each axis, uses SIX distinct genuine ORIGINAL
source incidence flags (because each flag contributes one of its two
diagonals to each opposite parity physical component). The six point
pair labels and six line pair labels form separate coordinate K3,2
graphs: five physical symbols of degrees (3,3,2,2,2).

Every historical accepted GF5 six-source-ID class requires SIX
physical symbols with degree exactly 2 on BOTH halves. Consequently
the six original flags defining a saturated K3,2 are rejected. In
fact NO accepted original sixset shares FIVE of those six IDs: one
replacement removes at most ONE edge incident with the two degree-3
coordinate symbols, leaving at least one degree-3 vertex.

The exclusion distance >=2 is SHARP on the TRUE original W(3,4):
a full separately globally injected f,g with eight source-factor-
disjoint ACTUAL incidence flags realizes a protected K3,2 + matching
companion, and two source-ID replacements complete a physical C6,
accepted in the historical GF5 D6 class. This is a scoped NO-GO for
zero/one-flag local compensation, not root sevenclass Omega(s^6).
"""
from collections import Counter
from itertools import combinations

from hyp105_full_physical_degree_tail import (
    genuine_source,physical,verify_selected,conflict_graph
)
from hyp105_physical_degree_energy import (
    minimal_alphabet,_verify_typed_injections
)
from hyp105_codegree_triangle_hall_stability import (
    exact_double_codegree_triangle_stability
)
from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked


def original_sixset_coordinate_degree_signature(ids, flags, f, g):
    """Unconditional actual ORIGINAL source 6-flag x/y label-degree census."""
    ids=tuple(ids)
    if len(ids)!=6 or len(set(ids))!=6:
        raise ValueError("require six different ORIGINAL incidence IDs")
    if any(i<0 or i>=len(flags) for i in ids):
        raise ValueError("source flag ID outside actual source")
    degx=Counter()
    degy=Counter()
    for i in ids:
        p,l=flags[i]
        degx.update(f[p])
        degy.update(g[l])
    return {
        "point_label_coordinate_degrees":tuple(sorted(degx.values())),
        "line_label_coordinate_degrees":tuple(sorted(degy.values())),
        "point_label_coordinate_symbols":len(degx),
        "line_label_coordinate_symbols":len(degy),
        "GF5_six_coordinate_two_regular_necessary":
            len(degx)==len(degy)==6 and
            set(degx.values())==set(degy.values())=={2},
    }


def genuine_W34_protected_k32_radius_two():
    """TRUE W34 fully injected 8-flag source matching; sharp original D6 r=2.

    Six ORIGINAL source flags are arranged on hub/free physical
    coordinate edges K3,2, two further ORIGINAL source flags join
    the same two hubs to a new sixth physical corner. Each retains
    its separate paired physical companion diagonal. The two source
    maps are completed globally injectively to ALL 85 original IDs.
    """
    s,V,flags=genuine_source(2)
    a=minimal_alphabet(V)
    if (s,V,a)!=(4,85,14):
        raise AssertionError("unexpected true original W34 parameters")
    bypoint=[[] for _ in range(V)]
    for p,l in flags:
        bypoint[p].append(l)
    owner={}
    def augment(p,visited):
        for l in bypoint[p]:
            if l in visited:
                continue
            visited.add(l)
            if l not in owner or augment(owner[l],visited):
                owner[l]=p
                return True
        return False
    for p in range(8):
        if not augment(p,set()):
            raise AssertionError("cannot find eight genuine disjoint original flags")
    matched=sorted((p,l) for l,p in owner.items())
    if len(matched)!=8 or len({p for p,l in matched})!=8 or (
        len({l for p,l in matched})!=8):
        raise AssertionError("not eight distinct source point/line factors")
    # K3,2 in the primary parity block, then two edges to NEW free 5:
    primary_pairs=(
        (0,3),(0,4),(1,3),(1,4),(2,3),(2,4),(0,5),(1,5)
    )
    f=[None]*V
    g=[None]*V
    for (x,y),(p,l) in zip(primary_pairs,matched):
        f[p]=(x,y)
        g[l]=(x+6,y+6)
    for labels in (f,g):
        used={z for z in labels if z is not None}
        remaining=iter(pair for pair in combinations(range(a),2)
                       if pair not in used)
        for i in range(V):
            if labels[i] is None:
                labels[i]=next(remaining)
    _verify_typed_injections(a,V,f,g)
    source_lookup={z:i for i,z in enumerate(flags)}
    ids=tuple(source_lookup[z] for z in matched)
    old=ids[:6]
    extended=ids
    # All TRUE source IDs have disjoint original point/line factors,
    # so the #659 source conflict graph is empty for selected flags.
    for subset in (old,extended):
        cg,mf,mg=conflict_graph(subset,flags,f,g)
        if mf or mg or any(cg.values()):
            raise AssertionError("genuine source matching became conflictful")
    # The two global typed physical coordinate color-cuts.
    lc=[0]*a
    rc=[0]*a
    for x in (3,4,5):
        lc[x]=1
    for y in (9,10,11):
        rc[y]=1
    for subset in (old,extended):
        graph,prov,checked=verify_selected(subset,flags,f,g,lc,rc)
        if len(prov)!=2*len(subset) or checked[
            "ordinary_C6"]!=checked["accepted_original_D6"]:
            raise AssertionError("paired genuine source-ID transfer failed")
    old_graph,old_prov,old_checked=verify_selected(
        old,flags,f,g,lc,rc)
    new_graph,new_prov,new_checked=verify_selected(
        extended,flags,f,g,lc,rc)
    old_H=exact_double_codegree_triangle_stability(old_graph)
    new_H=exact_double_codegree_triangle_stability(new_graph)
    if old_H["saturated_identical_two_right_witness_triangles"]!=1 or (
         old_H["total_C6_independent_right_collision_trace"]!=0):
        raise AssertionError("original physical K3,2 not saturated")
    if new_checked["accepted_original_D6"]!=2 or (
         new_H["total_C6_independent_right_collision_trace"]!=2):
        raise AssertionError("two genuine source flags fail to complete two D6")
    signature=original_sixset_coordinate_degree_signature(
        old,flags,f,g)
    expected_degrees=(2,2,2,3,3)
    if signature["point_label_coordinate_degrees"]!=expected_degrees or (
       signature["line_label_coordinate_degrees"]!=expected_degrees):
        raise AssertionError("protected genuine K3,2 source label degree pattern wrong")
    if classify_seven_prechecked(old,f,g,flags) is not None:
        raise AssertionError("saturated K3,2 falsely GF5 accepted")

    # Exhaustively check ALL one-flag substitutions with TRUE original
    # W34 incidence flags, not just the two planted positive flags.
    one_swap_accepted=0
    one_swap_examined=0
    for removed in old:
        for replacement in range(len(flags)):
            if replacement in old:
                continue
            candidate=tuple(sorted((set(old)-{removed})|{replacement}))
            one_swap_examined+=1
            if classify_seven_prechecked(candidate,f,g,flags) is not None:
                one_swap_accepted+=1
    if one_swap_accepted:
        raise AssertionError("distance-one GF5 compensation contradicts degree obstruction")

    # Two distinct sharp two-flag substitutions produce accepted D6.
    # Each removes one of the K3,2 edges adjacent to DIFFERENT 3-valent
    # free vertices and restores the two deficient hubs through new 5.
    positive_two_swaps=(
        tuple(sorted((set(old)-{old[0],old[3]})|{ids[6],ids[7]})),
        tuple(sorted((set(old)-{old[1],old[2]})|{ids[6],ids[7]})),
    )
    if len(set(positive_two_swaps))!=2 or any(
        classify_seven_prechecked(q,f,g,flags)!="D6"
        for q in positive_two_swaps):
        raise AssertionError("radius-two sharp true ORIGINAL GF5 D6 witness missing")
    if len({flags[i][0] for i in extended})!=8 or (
        len({flags[i][1] for i in extended})!=8):
        raise AssertionError("original source factor provenance broken")

    hubs=tuple((i,6+i) for i in range(3))
    frees=tuple((3+j,9+j) for j in range(2))
    primary_edges={
        tuple(sorted((h,z))) for h in hubs for z in frees
    }
    if not primary_edges.issubset(old_prov):
        raise AssertionError("not actual original physical K3,2")
    companion=set(old_prov)-primary_edges
    if len(companion)!=6 or len({v for edge in companion for v in edge})!=12:
        raise AssertionError("six real paired diagonals not a physical matching")
    if set(old_prov)&primary_edges!=primary_edges:
        raise AssertionError("lost whole source physical edge")
    if len(old_prov)!=12 or len(new_prov)!=16:
        raise AssertionError("each TRUE original incidence supplies two physical edges")

    return {
        "s":s,"V":V,"a":a,
        "true_original_protected_ids":old,
        "true_original_two_additional_ids":ids[6:],
        "all_eight_source_flags":tuple(matched),
        "all_distinct_original_point_and_line_factors":True,
        "old_primary_K32_edges":6,
        "old_opposite_parity_companion_matching_edges":6,
        "old_saturated_K32_triangles":
            old_H["saturated_identical_two_right_witness_triangles"],
        "old_original_GF5_seven_tag":
            classify_seven_prechecked(old,f,g,flags),
        "old_original_sixset_coordinate_signature":signature,
        "one_flag_substitution_candidates_checked":one_swap_examined,
        "one_flag_substitution_accepted":one_swap_accepted,
        "sharp_accepted_original_D6_two_replacements":positive_two_swaps,
        "old_ordinary_C6":old_checked["ordinary_C6"],
        "new_ordinary_C6":new_checked["ordinary_C6"],
        "new_accepted_original_D6":new_checked["accepted_original_D6"],
        "paired_source_original_diagonals_checked":True,
        "all_h_one_flag_accepted_GF5_compensation_excluded":True,
        "all_h_root_sevenclass_Omega_s6_proved":False,
    }
