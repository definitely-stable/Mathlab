"""HYP-105 #230 AA4-K32LIFT: exact fixed-f partial-g line-lift expectation.

All-h, genuine W(3,s) with V original points and V original lines.
Fix a COMPLETE globally injective original point-pair map f and a
PARTIAL injective line-pair map g_J on a chosen set J of original
lines. Complete g_J by a uniformly random injection from the
remaining V-|J| source lines into the Q=binom(a,2)-|J| unused typed
line-pair labels. Original incidence flags are NEVER randomized.

For each pair of selected saturated K3,2 hubs hi,hj and each physical
fresh corner (x,y), use the fixed f inverse to determine actual
source points p_i=f^-1({hi.x,x}), p_j=f^-1({hj.x,x}); if either missing
the candidate is impossible. Let pair labels
t_i={hi.y,y}, t_j={hj.y,y}, distinct by transverse hubs. The expected
indicator that both REAL source incidences (p_i,l_i),(p_j,l_j) occur:
  * both t slots fixed: exact 0/1 from source incidences.
  * one fixed: indicator(fixed source incidence) * d_U(p_other)/Q.
  * neither fixed:
    [d_U(p_i)*d_U(p_j)-c_U(p_i,p_j)]/[Q*(Q-1)]
where U is set of currently unfixed source lines and c_U is the number
of their common incident lines. For distinct source points of a true
generalized quadrangle, c_U<=1 (there is at most one joining line).

Summing all candidate physical corners gives an EXACT Fraction
E_g[sum_F sum_hubpairs |W_ij^(FULL H)(F)|]. By #664 unit
multiplicity of accepted source D6 from saturated parents, for EVERY
completion independently:
   D6(f,g) >= 2*sum_F sum_pairs |W_ij(F,g)|.
Therefore E_g[D6]>=2*E_g[W] and at least ONE admissible complete g
has D6>=ceil(2*E_g[W]). This is EXISTENTIAL / annealed, not a
pointwise uniform lower, and DOES NOT prove HYP-105 root.

The finite actual-source W32/W34 runner checks selected source-ID
conflict-freeness, both typed coordinate cuts, all paired diagonals
and exact saturation, while only frozen labels enter the expectation.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations

from hyp105_full_physical_degree_tail import (
    genuine_source, physical, verify_selected, conflict_graph,
)
from hyp105_physical_degree_energy import (
    minimal_alphabet, _verify_typed_injections,
)
from hyp105_k32_saturated_unit_multiplicity import (
    coherent_coordinate_colors, saturated_bipartite_k32_list,
)


def _canonical_pair(pair,a):
    if len(pair)!=2:
        raise ValueError("pair labels must have exactly two coordinates")
    x,y=pair
    if (type(x)is not int or type(y)is not int or
            not(0<=x<y<a)):
        raise ValueError("pair labels must be canonical pairs in K_a")
    return (x,y)


def conditional_line_slot_probability(
        p1,p2,t1,t2,fixed_inverse,unfixed_point_degrees,
        unfixed_common_line_counts,unused_coordinate_pairs,
        source_incidences):
    """Exact probability both original incidence source flags occur.

    frozen label inversion maps pair->ACTUAL original source line ID;
    free labels sample without replacement from unused original lines.
    No assumptions about random f or random original geometry.
    """
    if t1==t2:
        raise ValueError("two hub-pair line labels must be distinct")
    Q=unused_coordinate_pairs
    a=t1 in fixed_inverse
    b=t2 in fixed_inverse
    if a and b:
        return Fraction(int((p1,fixed_inverse[t1]) in source_incidences
                            and (p2,fixed_inverse[t2]) in source_incidences))
    if a:
        ok=(p1,fixed_inverse[t1]) in source_incidences
        return Fraction(int(ok)*unfixed_point_degrees[p2],Q)
    if b:
        ok=(p2,fixed_inverse[t2]) in source_incidences
        return Fraction(int(ok)*unfixed_point_degrees[p1],Q)
    if Q<2:
        return Fraction(0)
    joined=unfixed_common_line_counts.get(
        (min(p1,p2),max(p1,p2)),0)
    numerator=(unfixed_point_degrees[p1]*unfixed_point_degrees[p2]
               -(unfixed_point_degrees[p1] if p1==p2 else joined))
    if not 0<=numerator<=Q*(Q-1):
        raise AssertionError("exact finite line injection probability out of range")
    return Fraction(numerator,Q*(Q-1))


def expected_fresh_mass_for_fixed_saturated_blocks(
        a,source_flags,full_point_pairs,frozen_line_pairs,blocks,
        *,source_point_count=None,source_line_count=None):
    """Pure exact-rational all-h oracle on ACTUAL incidence lists.

    blocks: (hubs,frees) from ONE fixed selected physical coherent G;
    this routine does not magically manufacture or certify saturation;
    the genuine-source wrapper below does so.
    """
    f=tuple(_canonical_pair(z,a) for z in full_point_pairs)
    V=len(f)
    if V!=len(set(f)):
        raise ValueError("point labels not globally injective")
    if source_point_count is not None and source_point_count!=V:
        raise ValueError("true-source point count does not match f")
    if source_line_count is None:
        source_line_count=V
    k=len(frozen_line_pairs)
    if type(source_line_count)is not int or source_line_count<k:
        raise ValueError("invalid number of original source lines")
    if len(source_flags)!=len(set(source_flags)):
        raise ValueError("duplicate original incidence flags")
    inc=set(source_flags)
    if any(not (0<=p<V and 0<=l<source_line_count)
           for p,l in source_flags):
        raise ValueError("incidence outside genuine source factors")
    frozen={}
    seen_pairs=set()
    for line,pair in frozen_line_pairs.items():
        if type(line)is not int or not(0<=line<source_line_count):
            raise ValueError("frozen source line out of range")
        pair=_canonical_pair(pair,a)
        if pair in seen_pairs:
            raise ValueError("frozen line labels are not injected")
        frozen[line]=pair
        seen_pairs.add(pair)
    Q=a*(a-1)//2-k
    m=source_line_count-k
    if Q<m:
        raise ValueError("partial labels cannot be completed injectively")
    frozen_inv={pair:line for line,pair in frozen.items()}
    f_inv={pair:p for p,pair in enumerate(f)}
    free_lines=set(range(source_line_count))-set(frozen)
    unfixed_deg=[0]*V
    line_to_points=defaultdict(set)
    for p,l in source_flags:
        if l in free_lines:
            unfixed_deg[p]+=1
            line_to_points[l].add(p)
    common=defaultdict(int)
    for ps in line_to_points.values():
        for p1,p2 in combinations(sorted(ps),2):
            common[p1,p2]+=1
    component=defaultdict(Fraction)
    blocks_detail=[]
    total=Fraction()
    for hubs,frees in blocks:
        hubs=tuple(hubs)
        frees=tuple(frees)
        if len(hubs)!=3 or len(frees)!=2 or len(set(hubs+frees))!=5:
            raise ValueError("selected saturated K3,2 block needs 3+2 physical corners")
        old_x={u for u,v in hubs+frees}
        old_y={v for u,v in hubs+frees}
        if len(old_x)!=5 or len(old_y)!=5:
            raise ValueError("selected block must be coordinate-transverse")
        block_count=Fraction()
        pair_data={}
        for i,j in combinations(range(3),2):
            hi,hj=hubs[i],hubs[j]
            pair_count=Fraction()
            for x in range(a):
                if x in old_x:
                    continue
                p1=f_inv.get(tuple(sorted((hi[0],x))))
                p2=f_inv.get(tuple(sorted((hj[0],x))))
                if p1 is None or p2 is None:
                    continue
                if p1==p2:
                    raise AssertionError("distinct typed point-label pairs share actual source point")
                for y in range(a):
                    if y in old_y:
                        continue
                    t1=tuple(sorted((hi[1],y)))
                    t2=tuple(sorted((hj[1],y)))
                    if t1==t2:
                        raise AssertionError("hub line coordinate labels unexpectedly coincide")
                    pr=conditional_line_slot_probability(
                        p1,p2,t1,t2,frozen_inv,unfixed_deg,common,Q,inc)
                    if pr:
                        component[
                            ("frozen" if t1 in frozen_inv else "free")+
                            "-"+
                            ("frozen" if t2 in frozen_inv else "free")
                        ]+=pr
                    pair_count+=pr
            pair_data[i,j]=pair_count
            block_count+=pair_count
        blocks_detail.append(tuple(sorted(pair_data.items())))
        total+=block_count
    expected_D6_lower=2*total
    return {
        "source_points":V,
        "source_lines":source_line_count,
        "source_flags":len(source_flags),
        "alphabet":a,
        "frozen_original_line_labels":k,
        "unfixed_original_source_lines":m,
        "available_unused_pair_labels":Q,
        "source_saturated_blocks":len(blocks),
        "block_pair_expected_fresh_mass":tuple(blocks_detail),
        "expected_total_fresh_common_neighbor_mass":total,
        "expected_saturated_parent_original_D6_sector":expected_D6_lower,
        "at_least_one_complete_line_injection_original_D6_lower":
            -(-expected_D6_lower.numerator//expected_D6_lower.denominator),
        "probability_components":dict(component),
        "all_h_conditional_expectation_identity_proved":True,
        "pointwise_for_every_completion_positive_proved":False,
        "root_sevenclass_Omega_s6_proved":False,
    }


def genuine_source_conditional_saturated_line_lift(
        power,f,reference_complete_g,selected_source_IDs):
    """Finite exact true W32/W34 selected-graph source-safe wrapper."""
    s,V,flags=genuine_source(power)
    a=minimal_alphabet(V)
    f=tuple(map(tuple,f))
    g=tuple(map(tuple,reference_complete_g))
    _verify_typed_injections(a,V,f,g)
    ids=tuple(sorted(selected_source_IDs))
    if len(ids)!=len(set(ids)) or any(type(i)is not int or
            not(0<=i<len(flags)) for i in ids):
        raise ValueError("selected source IDs must be true and distinct")
    conflicts,mf,mg=conflict_graph(ids,flags,f,g)
    if mf or mg or any(conflicts.values()):
        raise ValueError("selected true-source flags not conflict-free")
    left_colors=coherent_coordinate_colors(ids,flags,f,g,0)
    right_colors=coherent_coordinate_colors(ids,flags,f,g,1)
    left_colors=left_colors+(0,)*(a-len(left_colors))
    right_colors=right_colors+(0,)*(a-len(right_colors))
    selected,provenance,source_stats=verify_selected(
        ids,flags,f,g,left_colors,right_colors)
    if len(provenance)!=2*len(ids) or (
            source_stats["accepted_original_D6"]!=
            source_stats["ordinary_C6"]):
        raise AssertionError("selected original paired physical diagonals/GF5 invalid")
    blocks=saturated_bipartite_k32_list(selected)
    frozen={flags[i][1]:g[flags[i][1]] for i in ids}
    if len(frozen)!=len(ids):
        raise ValueError("selected line factors not distinct; bad frozen partition")
    result=expected_fresh_mass_for_fixed_saturated_blocks(
        a,flags,f,frozen,blocks,source_point_count=V,
        source_line_count=V)
    result["s"]=s
    result["selected_original_source_IDs"]=ids
    result["selected_source_ordinary_C6"]=source_stats["ordinary_C6"]
    result["selected_source_original_D6"]=source_stats["accepted_original_D6"]
    result["selected_original_diagonal_edges"]=len(provenance)
    result["all_genuine_source_incidence_flags"]=len(flags)
    return result


def deterministically_complete_line_labels_by_conditional_expectation(
        power,full_point_pairs,reference_complete_line_pairs,
        selected_original_source_IDs):
    """Produce a FULL genuine source g with M(g) >= exact E[M|selected].

    Classical method of conditional expectations applied to the NEW
    exact original-incidence rectangle oracle. Original source IDs,
    complete f and the selected old source g line pairs remain fixed.

    At each step choose the lexicographically first remaining source
    line and try EVERY available physical K_a pair slot. Uniform
    injections make the conditional mean of all child expectations
    EXACTLY the current expectation; choose the maximizer. After all
    source lines have been frozen, expected M equals actual integer M.
    This is deterministic and exact, not a randomized sample; no
    pointwise all-map HYP-105 root claim is made.
    """
    from hyp105_k32_saturated_unit_multiplicity import (
        genuine_source_saturated_unit_transfer,
    )
    s,V,flags=genuine_source(power)
    a=minimal_alphabet(V)
    f=tuple(map(tuple,full_point_pairs))
    g0=tuple(map(tuple,reference_complete_line_pairs))
    _verify_typed_injections(a,V,f,g0)
    original=genuine_source_conditional_saturated_line_lift(
        power,f,g0,selected_original_source_IDs)
    ids=original["selected_original_source_IDs"]
    selected,_=physical(ids,flags,f,g0)
    blocks=saturated_bipartite_k32_list(selected)
    fixed={flags[i][1]:g0[flags[i][1]] for i in ids}
    initial=original["expected_total_fresh_common_neighbor_mass"]
    current=initial
    steps=0
    for line in range(V):
        if line in fixed:
            continue
        used=set(fixed.values())
        available=(z for z in combinations(range(a),2) if z not in used)
        candidates=[]
        for pair in available:
            candidate=dict(fixed)
            candidate[line]=pair
            q=expected_fresh_mass_for_fixed_saturated_blocks(
                a,flags,f,candidate,blocks,source_point_count=V,
                source_line_count=V)
            candidates.append((q["expected_total_fresh_common_neighbor_mass"],pair))
        if not candidates:
            raise AssertionError("no legal global source line-label injection left")
        if sum((v for v,_ in candidates),Fraction())!=(
                len(candidates)*current):
            raise AssertionError("conditional tower law failed for true source injections")
        best,pair=max(candidates,key=lambda p:(p[0],tuple(-z for z in p[1])))
        if best<current:
            raise AssertionError("conditional-expectation monotonicity failed")
        fixed[line]=pair
        current=best
        steps+=1
    if len(fixed)!=V or len(set(fixed.values()))!=V or (
            current.denominator!=1):
        raise AssertionError("deterministic completed source g is not valid")
    g=tuple(fixed[l] for l in range(V))
    _verify_typed_injections(a,V,f,g)
    if any(g[flags[i][1]]!=g0[flags[i][1]] for i in ids):
        raise AssertionError("selected original source labels were changed")
    actual=genuine_source_saturated_unit_transfer(
        power,f,g,ids)
    if actual["full_H_fresh_common_neighbor_mass"]!=int(current):
        raise AssertionError("last exact conditional expectation differs from full original source M")
    if actual["two_swap_D6_extension_memberships"]<2*current or (
            current<initial):
        raise AssertionError("greedy real-source accepted GF5 D6 guarantee failed")
    return {
        "s":s,"V":V,
        "source_IDs_selected":ids,
        "frozen_old_original_line_pairs":len(ids),
        "line_assignments_chosen_deterministically":steps,
        "initial_exact_expected_fresh_mass":initial,
        "final_actual_fresh_mass":int(current),
        "final_two_swap_original_GF5_accepted_D6":
            actual["two_swap_D6_extension_memberships"],
        "fully_injective_completed_original_line_pairs":g,
        "all_source_incidence_flags":len(flags),
        "source_selected_saturated_blocks":
            actual["saturated_original_source_K32_blocks"],
        "method_of_conditional_expectations_verified":True,
        "pointwise_all_completions_lower_proved":False,
        "root_sevenclass_Omega_s6_proved":False,
    }
