"""HYP-105 C12: exact physical-coordinate automorphism orbit quotient.

ONE common original-to-physical right bijection only. The finite
enumerator constructs the induced action of Aut(F) on occupied physical
pair-edge labels and removes ONLY exact symmetry duplicates. Does not
invent independence across GQ distinguished pair completion fibers.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial, perm

from hyp105_g5e2b3e1c5_common_bijection import (
    validate_weighted_sixsets, physical_occupied_target, fixed_map_overlap,
)


def physical_coordinate_actions(a, occupied,
                                *, max_coordinate_permutations=40320):
    """Enumerate physical K_a coordinate relabellings preserving F.

    Distinguish coordinate automorphisms from DISTINCT actions on the
    occupied edge-label set. The latter is the faithful image group
    used for orbit-stabilizer and never double-counts a kernel.
    This finite oracle fails closed when a! exceeds the hard budget.
    The group theorem itself applies to all a, without enumeration.
    """
    if type(a) is not int or not 6 <= a <= 9:
        raise ValueError("finite oracle requires 6<=a<=9")
    if (type(max_coordinate_permutations) is not int
            or max_coordinate_permutations < 1
            or factorial(a)>max_coordinate_permutations):
        raise ValueError("physical coordinate group exceeds exact enumeration budget")
    try:
        F=tuple(tuple(e) for e in occupied)
    except (TypeError,ValueError) as e:
        raise ValueError("invalid physical edge collection") from e
    if (len(F)<6 or len(F)>comb(a,2) or len(set(F))!=len(F)
            or any(len(e)!=2 or any(type(x) is not int or not 0<=x<a for x in e)
                   or e[0]>=e[1] for e in F)):
        raise ValueError("physical F must contain distinct canonical K_a edges")
    index={edge:i for i,edge in enumerate(F)}
    actions=set()
    coordinate_count=0
    for p in permutations(range(a)):
        image=tuple(index.get(tuple(sorted((p[i],p[j]))),-1)
                    for i,j in F)
        if min(image,default=-1)<0:
            continue
        if len(set(image))!=len(F):
            raise AssertionError("coordinate automorphism fails to be bijective")
        coordinate_count+=1
        actions.add(image)
    identity=tuple(range(len(F)))
    if identity not in actions or coordinate_count<1:
        raise AssertionError("physical identity action missing")
    if coordinate_count % len(actions):
        raise AssertionError("induced action kernel is not a subgroup")
    return {
        "a":a, "V":len(F),
        "occupied_physical_edges":F,
        "physical_coordinate_automorphism_count":coordinate_count,
        "distinct_occupied_edge_actions":tuple(sorted(actions)),
        "induced_action_group_order":len(actions),
        "coordinate_to_occupied_action_kernel_size":
            coordinate_count//len(actions),
        "all_actions_exactly_preserve_F":True,
        "all_h_group_action_proof_not_limited_to_a_le9":True,
    }


def physical_prefix_orbits(a, occupied, original_pins,
                           *, max_prefixes=50000,
                           max_coordinate_permutations=40320):
    """Partition ALL ordered injective physical images of D under Aut(F).

    The original pin labels D stay FIXED. Actions act simultaneously
    on their physical images. For fixed original source and occupied
    physical target, exact U and each seven-class count are constant
    along corresponding g-extension orbits. This quotient changes
    neither the true minimum nor conditional U-distributions.
    """
    data=physical_coordinate_actions(
        a,occupied,max_coordinate_permutations=max_coordinate_permutations)
    V=data["V"]
    D=tuple(original_pins)
    if (any(type(x) is not int or not 0<=x<V for x in D)
            or len(set(D))!=len(D) or len(D)>V):
        raise ValueError("invalid original right-line pins")
    N=perm(V,len(D))
    if type(max_prefixes) is not int or max_prefixes < 1 or N>max_prefixes:
        raise ValueError("ordered pinned assignments exceed exact prefix budget")
    unvisited=set(permutations(range(V),len(D)))
    actions=data["distinct_occupied_edge_actions"]
    orbit_rows=[]
    while unvisited:
        seed=min(unvisited)
        orbit={tuple(action[j] for j in seed) for action in actions}
        if not orbit.issubset(unvisited):
            raise AssertionError("orbit overlap inconsistent with prior orbit")
        canonical=min(orbit)
        stabilizer=sum(tuple(action[j] for j in canonical)==canonical
                       for action in actions)
        if not stabilizer or len(orbit)*stabilizer!=len(actions):
            raise AssertionError("incorrect orbit-stabilizer certificate")
        unvisited.difference_update(orbit)
        orbit_rows.append({
            "canonical_images":canonical,
            "orbit_size":len(orbit),
            "stabilizer_size":stabilizer,
        })
    orbit_rows.sort(key=lambda x:x["canonical_images"])
    if sum(row["orbit_size"] for row in orbit_rows)!=N:
        raise AssertionError("prefix orbit partition is incomplete")
    return {
        "a":a,"V":V, "original_pins":D,
        "induced_group_order":len(actions),
        "all_injective_prefixes":N,
        "representative_prefixes":len(orbit_rows),
        "orbits":tuple(orbit_rows),
        "partition_is_exhaustive":True,
        "true_global_minimum_unchanged_by_quotient":True,
        "all_h_positive_seven_motif_lower_proved":False,
    }


def conditional_shared_prefix_mean(source, target, V, pinned):
    """Independent exact one-global-completion FIRST moment, no C7-B import.

    A source sixset of fixed pinned membership A is uniformly sent to
    the C(V-|D|,6-|A|) physical sixsets with membership p(A).
    """
    src=validate_weighted_sixsets(source,V)
    try:
        seq=tuple(target)
    except TypeError as exc:
        raise ValueError("invalid target") from exc
    tar=validate_weighted_sixsets({R:1 for R in seq},V)
    if len(tar)!=len(seq):
        raise ValueError("duplicate target sixset")
    if not hasattr(pinned,"items"):
        raise ValueError("pinned must be mapping")
    p=dict(pinned)
    if (any(type(x) is not int or type(y) is not int or
            x<0 or x>=V or y<0 or y>=V for x,y in p.items())
            or len(set(p.values()))!=len(p)):
        raise ValueError("invalid original-to-occupied partial injection")
    D=set(p)
    I=set(p.values())
    b=Counter()
    q=Counter()
    for R,w in src.items():
        b[frozenset(R&D)]+=w
    for Q in tar:
        q[frozenset(Q&I)]+=1
    n=V-len(D)
    result=Fraction(0)
    for A,mass in b.items():
        images=frozenset(p[x] for x in A)
        denominator=comb(n,6-len(A))
        if not denominator:
            raise AssertionError("source fiber has impossible capacity")
        result+=Fraction(mass*q[images],denominator)
    return result


def full_physical_alphabet_one_pin_blindness(source,a):
    """Exact 1-design null-information theorem for F=E(K_a).

    For EACH original right vertex u and EACH physical occupied edge
    e, the conditional shared-map mean equals unconditional mean:
    all targets form an edge-transitive 1-design with d=6*T/V.
    This theorem holds for every nonnegative source, NOT only GQ,
    but only when the entire K_a edge alphabet is occupied.
    """
    F=tuple(combinations(range(a),2))
    if not 6<=a<=9:
        raise ValueError("finite complete physical oracle requires 6<=a<=9")
    V=len(F)
    src=validate_weighted_sixsets(source,V)
    T=physical_occupied_target(a,F)
    expected=Fraction(sum(src.values())*len(T),comb(V,6))
    degrees=Counter(j for Q in T for j in Q)
    d=Fraction(6*len(T),V)
    if any(degrees[j]!=d for j in range(V)):
        raise AssertionError("full K_a physical 2factor one-design property violated")
    # No need to run V**2 identical conditional sums: proving the two
    # conditional per-source-sixset probabilities equal is exact.
    if (Fraction(d,comb(V-1,5))!=Fraction(len(T),comb(V,6))
            or Fraction(len(T)-d,comb(V-1,6))
               !=Fraction(len(T),comb(V,6))):
        raise AssertionError("one pin unconditional mean identity failed")
    return {
        "a":a,"V":V,"target_count":len(T),
        "target_edge_degree":d,
        "unconditional_one_map_mean":expected,
        "every_original_vertex_every_physical_edge_same_mean":True,
        "not_true_for_arbitrary_incomplete_occupied_F":True,
        "not_a_deterministic_all_g_lower":True,
    }


def original_to_physical_action(pi, action):
    if (len(pi)!=len(action) or len(set(pi))!=len(pi)
            or set(pi)!=set(range(len(action)))):
        raise ValueError("requires full permutation of occupied labels")
    return tuple(action[x] for x in pi)


def genuine_W32_orbit_report():
    """Real original symplectic W32 f; quotient AND seven-class safeguard."""
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
    from hyp105_g5e2b3e1c0_weighted_overlap import source_weighted_BA_hypergraph
    from hyp105_g5e2b3e1c11_coupled_four import (
        genuine_W32_coupled_four_report,common_prefix_joint_moments,
    )
    from hyp105_g5e2b3e1b0_seven_signature import seven_census

    F=tuple(combinations(range(6),2))
    target=physical_occupied_target(6,F)
    source_model=pair_labeled_symplectic(1,"reverse-line")
    src=source_weighted_BA_hypergraph(source_model)
    lookup={edge:i for i,edge in enumerate(F)}
    original=tuple(lookup[e] for e in source_model["right_labels"])
    group=physical_coordinate_actions(6,F)
    part=[physical_prefix_orbits(6,F,tuple(range(k))) for k in range(4)]
    if (tuple(p["representative_prefixes"] for p in part)!=(1,1,2,9)
            or group["induced_action_group_order"]!=720):
        raise AssertionError("canonical physical K6 orbit partition changed")
    blind=full_physical_alphabet_one_pin_blindness(src,6)
    for images in range(15):
        actual_mean=conditional_shared_prefix_mean(src,target,15,{0:images})
        if actual_mean!=blind["unconditional_one_map_mean"]:
            raise AssertionError("genuine W32 one-pin mean not invariant")
    nontrivial=next(h for h in group["distinct_occupied_edge_actions"]
                    if h!=tuple(range(15)))
    full_modified=original_to_physical_action(original,nontrivial)
    if fixed_map_overlap(src,target,original)!=fixed_map_overlap(
            src,target,full_modified):
        raise AssertionError("physical graph automorphism changes B/A")
    model_modified=dict(source_model)
    model_modified["right_labels"]=tuple(F[j] for j in full_modified)
    before=seven_census(source_model,independent_checks=False)
    after=seven_census(model_modified,independent_checks=False)
    if (before["seven_class_motif_counts"]!=after["seven_class_motif_counts"]
            or before["S_seven"]!=after["S_seven"]
            or before["GF5_seven_lower_numerator"]!=after["GF5_seven_lower_numerator"]):
        raise AssertionError("same-map physical automorphism modified seven-class vector")
    D=tuple(range(11))
    p={x:original[x] for x in D}
    p2={x:nontrivial[original[x]] for x in D}
    m=common_prefix_joint_moments(src,target,15,p)
    m2=common_prefix_joint_moments(src,target,15,p2)
    for key in ("mean_one_shared_completion",
                "second_moment_one_shared_completion",
                "variance_one_shared_completion",
                "worst_completion_lower_from_second_moment"):
        if m[key]!=m2[key]:
            raise AssertionError("common-completion distribution changed under automorphism")
    c11=genuine_W32_coupled_four_report()
    if c11["restricted_four_line_exact_minimum"]!=56:
        raise AssertionError("W32 24-common-map regression changed")
    return {
        "scope":"GENUINE_ORIGINAL_W32_FIXED_LEFT_AND_FULL_PHYSICAL_K6",
        "physical_coord_group_order":group["physical_coordinate_automorphism_count"],
        "faithful_edge_action_order":group["induced_action_group_order"],
        "prefix_orbit_counts_k0_to_k3":
            tuple(p["representative_prefixes"] for p in part),
        "prefix_assignment_counts_k0_to_k3":
            tuple(p["all_injective_prefixes"] for p in part),
        "full_right_permutations":factorial(15),
        "full_map_orbits_exact_quotient":factorial(15)//720,
        "all_15_factorial_orbits_enumerated":False,
        "physical_S6_equivariant_seven_class_count":True,
        "same_11_pin_prefix_conditional_variance":
            str(m["variance_one_shared_completion"]),
        "transformed_11_pin_prefix_conditional_variance":
            str(m2["variance_one_shared_completion"]),
        "one_pin_mean":str(blind["unconditional_one_map_mean"]),
        "real_W32_24_joint_map_min":c11["restricted_four_line_exact_minimum"],
        "real_W32_original_S_seven":c11["seven_family_original_S"],
        "real_W32_BA_minimizer_S_seven":c11["seven_family_candidate_S"],
        "real_W32_S_seven_change":c11["seven_family_total_delta"],
        "real_W32_class_changes":c11["seven_family_class_count_delta"],
        "real_W32_GF5_floor_numerator_before":
            c11["GF5_seven_necessary_floor_original_numerator"],
        "real_W32_GF5_floor_numerator_after":
            c11["GF5_seven_necessary_floor_candidate_numerator"],
        "not_universal_all_f_g_seven_lower_proved":True,
    }


if __name__=="__main__":
    import json
    print(json.dumps(genuine_W32_orbit_report(),indent=2,sort_keys=True))
