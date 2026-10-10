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


def orbit_quotiented_shared_minimum_interval(
        source, a, occupied, original_pins, *,
        max_prefixes=50000,
        max_relevant_source_cells=10000,
        explicit_right_witnesses=()):
    """FULL right-S_V global interval for ONE fixed genuine f,F, via H-orbits.

    Every complete common g has a D-prefix p belonging to EXACTLY
    one physical Aut(F) orbit. An h maps g to a full completion of the
    canonical representative without changing U. Thus min over all g
    is >=min over orbit representatives of ANY valid C11/C8 conditional
    completion lower, and <=min over orbit reps of floor conditional
    completion mean (existential upper). This does not optimize f or F.

    Exact independent tower identities also audit the physical quotient:
      (sum_{prefix-orbits} orbit_size * E[U|representative]) / (V)_k
        == unconditional one-right-bijection mean,
    and identically for E[U^2]. No independent motif or anchor maps.
    """
    from hyp105_g5e2b3e1c11_coupled_four import common_prefix_joint_moments
    from hyp105_g5e2b3e1c8_fiber_rearrangement import frozen_fiber_rearrangement
    from hyp105_g5e2b3e1c5_common_bijection import common_bijection_moments

    F=tuple(occupied)
    group=physical_prefix_orbits(
        a,F,original_pins,max_prefixes=max_prefixes)
    V=len(F)
    src=validate_weighted_sixsets(source,V)
    target=physical_occupied_target(a,F)
    D=group["original_pins"]
    rows=[]
    total_mu=Fraction(0)
    total_second=Fraction(0)
    for orb in group["orbits"]:
        images=orb["canonical_images"]
        p=dict(zip(D,images))
        moments=common_prefix_joint_moments(
            src,target,V,p,
            max_relevant_source_cells=max_relevant_source_cells)
        loose=frozen_fiber_rearrangement(src,target,V,D,images)
        lower=max(
            loose,moments["worst_completion_lower_from_second_moment"])
        upper=moments["existential_completion_upper_from_mean"]
        if lower>upper:
            raise AssertionError("invalid globally certified orbit interval")
        weight=orb["orbit_size"]
        total_mu+=weight*moments["mean_one_shared_completion"]
        total_second+=weight*moments["second_moment_one_shared_completion"]
        rows.append({
            "canonical_physical_prefix_images":images,
            "orbit_size":weight,
            "C8_fiber_lower":loose,
            "C11_joint_variance_lower":
                moments["worst_completion_lower_from_second_moment"],
            "certified_all_completions_lower":lower,
            "existential_some_completion_upper":upper,
            "exact_conditional_mean":moments["mean_one_shared_completion"],
            "exact_conditional_second_moment":
                moments["second_moment_one_shared_completion"],
        })
    if not rows:
        raise AssertionError("empty exact physical prefix partition")
    global_lower=min(row["certified_all_completions_lower"] for row in rows)
    moment_only_upper=min(row["existential_some_completion_upper"] for row in rows)
    global_upper=moment_only_upper

    # Explicit FULL original->physical right-map witnesses can sharpen the
    # existential bound, but NEVER the universal deterministic lower.
    # Each is independently validated and recounted against the very same
    # source and occupied physical 2-factor target.
    try:
        witness_sequence=tuple(explicit_right_witnesses)
    except TypeError as exc:
        raise ValueError("witnesses must be explicit full right maps") from exc
    witness_values=[]
    best_witness=None
    for candidate in witness_sequence:
        try:
            pi=tuple(candidate)
        except TypeError as exc:
            raise ValueError("witness must be a complete right bijection") from exc
        if (len(pi)!=V or any(type(x) is not int or not 0<=x<V for x in pi)
                or len(set(pi))!=V):
            raise ValueError("witness must biject ALL original right IDs")
        actual=fixed_map_overlap(src,target,pi)
        witness_values.append(actual)
        if best_witness is None or actual<best_witness[0]:
            best_witness=(actual,pi)
        global_upper=min(global_upper,actual)
    if global_lower>global_upper:
        raise AssertionError("invalid certified right-map witness or lower bound")
    reference=common_bijection_moments(src,target,V)
    count=group["all_injective_prefixes"]
    weighted_mean=total_mu/count
    weighted_second=total_second/count
    if weighted_mean!=reference["one_common_right_bijection_mean"]:
        raise AssertionError("physical-prefix tower violated C5 exact mean")
    if weighted_second!=reference["one_common_right_bijection_second_moment"]:
        raise AssertionError("physical-prefix tower violated C5 exact second moment")
    return {
        "fixed_original_left_embedding_and_occupied_F":True,
        "V":V,"original_pins":D,
        "physical_prefix_orbits":len(rows),
        "physical_prefix_assignments_exhausted":count,
        "certified_global_BA_minimum_lower":global_lower,
        "moment_only_existential_global_BA_upper":moment_only_upper,
        "existential_global_BA_minimum_upper":global_upper,
        "explicit_full_right_witness_values":tuple(witness_values),
        "best_recounted_explicit_right_witness":
            best_witness[1] if best_witness else None,
        "exact_global_BA_minimum_if_equal":
            global_lower if global_lower==global_upper else None,
        "unconditional_mean_recovered_by_exact_orbit_tower":weighted_mean,
        "unconditional_second_recovered_by_exact_orbit_tower":weighted_second,
        "all_prefix_orbit_certificates":tuple(rows),
        "all_right_completions_same_global_map":True,
        "all_f_F_GQ_or_seven_family_lower_proved":False,
    }


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
    # All 210 physical assignments of two NAMED original right lines are
    # covered by just TWO exact common-completion conditional moment gates.
    c11=genuine_W32_coupled_four_report()
    k2_global=orbit_quotiented_shared_minimum_interval(
        src,6,F,(0,1),max_prefixes=210,
        explicit_right_witnesses=(c11["minimizing_full_right_permutation"],))
    if (k2_global["physical_prefix_orbits"]!=2
            or k2_global["physical_prefix_assignments_exhausted"]!=210):
        raise AssertionError("GQ W32 global two-pin orbit certificate incomplete")
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
        "W32_all_right_g_two_pin_orbit_global_lower":
            k2_global["certified_global_BA_minimum_lower"],
        "W32_all_right_g_two_pin_orbit_existential_upper":
            k2_global["existential_global_BA_minimum_upper"],
        "W32_all_right_g_two_pin_orbit_moment_only_upper":
            k2_global["moment_only_existential_global_BA_upper"],
        "W32_global_explicit_right_witness_BA":
            k2_global["explicit_full_right_witness_values"][0],
        "W32_two_pin_orbit_global_exact_if_meet":
            k2_global["exact_global_BA_minimum_if_equal"],
        "W32_two_pin_orbit_conditional_mean_tower":
            str(k2_global["unconditional_mean_recovered_by_exact_orbit_tower"]),
        "W32_two_pin_orbit_conditional_second_tower":
            str(k2_global["unconditional_second_recovered_by_exact_orbit_tower"]),
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
