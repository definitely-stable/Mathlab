"""HYP-105 C13: exact *joint* GQ/physical double-sided orbit reductions.

The mathematical symmetry holds for ALL symplectic W(3,2**h) and legal
left/right physical pair-label injections. Explicit group enumeration and
canonicalization are ONLY for actual finite W(3,2) (q=2, V=15).

Three transformations MUST act together: an original incidence
automorphism sigma on original point/line IDs, and an independent
physical-coordinate graph automorphism on EACH physical half. This
neither changes the GQ incidence graph nor separately remaps motifs.
"""
from collections import Counter
from itertools import combinations
from math import factorial

from hyp105_b1_symplectic import symplectic_gq, symplectic
from hyp105_g5e2b3e1a_fixed_leading import validated_small_model
from hyp105_g5e2b3e1c12_physical_orbits import physical_coordinate_actions


def _xor4(a, b):
    return tuple(x ^ y for x,y in zip(a,b))


def w32_original_sp4_automorphisms():
    """Independently exhaust 15*8*3*2 = 720 classical Sp(4,2) bases.

    An ordered symplectic basis (A,B,C,D) has:
      <A,C>=1, <B,D>=1; all other basis pairings 0.
    Columns replace standard e0,e1,e2,e3, respectively.
    Over GF(2), every invertible projective transform equals a linear
    transform, hence q=2 has no nontrivial field automorphisms.
    The routine CHECKS all 45 original GQ incidence edges exactly.
    """
    field,points,lines,incidence=symplectic_gq(1)
    V=len(points)
    if V!=15 or len(lines)!=15 or len(incidence)!=45:
        raise AssertionError("expected canonical W(3,2) doily")
    pidx={x:i for i,x in enumerate(points)}
    lidx={frozenset(line):i for i,line in enumerate(lines)}
    incidences=frozenset(incidence)
    actions=set()
    zeros=(0,0,0,0)
    nonzero=tuple(x for x in points if x!=zeros)
    for A in nonzero:
        for C in nonzero:
            if symplectic(A,C,field)!=1:
                continue
            for B in nonzero:
                if symplectic(A,B,field) or symplectic(C,B,field):
                    continue
                for D in nonzero:
                    if (symplectic(B,D,field)!=1
                            or symplectic(A,D,field)
                            or symplectic(C,D,field)):
                        continue
                    def image(x):
                        out=zeros
                        for bit,col in zip(x,(A,B,C,D)):
                            if bit:
                                out=_xor4(out,col)
                        return out
                    pts=tuple(pidx[image(x)] for x in points)
                    if len(set(pts))!=V:
                        raise AssertionError("symplectic basis map not bijective")
                    mapped=[]
                    for line in lines:
                        key=frozenset(pts[i] for i in line)
                        if key not in lidx:
                            raise AssertionError("symplectic transform lost original line")
                        mapped.append(lidx[key])
                    lns=tuple(mapped)
                    if (len(set(lns))!=V or
                        {(pts[p],lns[l]) for p,l in incidence}!=incidences):
                        raise AssertionError("SP4 mapping does not preserve GQ incidence")
                    actions.add((pts,lns))
    actions=tuple(sorted(actions))
    if len(actions)!=720 or (tuple(range(V)),tuple(range(V))) not in actions:
        raise AssertionError("incorrect SP(4,2) order or identity")
    return actions


def original_incidence_pair_orbits(original_actions):
    """Exact W32 original point-line ordered-pair incidence orbit census.

    This is ORIGINAL incidence p~l, not physical K_a edge adjacency.
    Under the full 720 original symplectic transformations all 225
    ordered point-line pairs must split into 45 flags + 180 antiflags.
    """
    _,points,lines,inc=symplectic_gq(1)
    V=len(points)
    if not original_actions or any(len(p)!=V or len(l)!=V
                                   for p,l in original_actions):
        raise ValueError("invalid original W32 collineation group")
    unvisited={(i,j) for i in range(V) for j in range(V)}
    orbits=[]
    while unvisited:
        seed=min(unvisited)
        orbit={(p[seed[0]],l[seed[1]]) for p,l in original_actions}
        if not orbit<=unvisited:
            raise AssertionError("original incidence orbit overlap")
        count=len(orbit)
        if len(original_actions)%count:
            raise AssertionError("invalid incidence orbit stabilizer")
        orbits.append((seed,count,len(original_actions)//count))
        unvisited-=orbit
    incset=set(inc)
    if sorted(x[1] for x in orbits)!=[45,180]:
        raise AssertionError("doily point-line flag/antiflag orbit changed")
    if not {len({v for v in
                {(p[seed[0]],l[seed[1]]) for p,l in original_actions}
                if v in incset}) for seed,_,_ in orbits}=={0,45}:
        raise AssertionError("original incidence vs nonincidence not preserved")
    return {
        "original_points":V,
        "original_lines":V,
        "original_incidence_flags":len(incset),
        "original_nonincident_antiflags":V*V-len(incset),
        "point_line_pair_orbits":tuple(orbits),
        "orbit_cardinalities":tuple(sorted(x[1] for x in orbits)),
        "full_point_line_pairs_exhausted":V*V,
    }


def W32_joint_one_left_one_right_pin_orbits():
    """True 4-tuple prefix quotient: (original p, original l, f(p),g(l)).

    Each physical full-K6 S6 action is edge-transitive on 15 pair edges,
    and the original Sp4 group has exactly TWO distinct orbits on
    original point×line pairs: 45 flags and 180 antiflags.
    Their direct product therefore has EXACTLY two orbits on all
    15*15*15*15 = 50,625 one-left/one-right pinned assignments.

    This is NOT a quotient of all full f,g mapping pairs.
    """
    A=w32_original_sp4_automorphisms()
    orbit=original_incidence_pair_orbits(A)
    F=tuple(combinations(range(6),2))
    physical=physical_coordinate_actions(6,F)
    H=physical["distinct_occupied_edge_actions"]
    V=len(F)
    if any({h[i] for h in H}!=set(range(V)) for i in range(V)):
        raise AssertionError("K6 physical edge action is not transitive")
    if orbit["orbit_cardinalities"]!=(45,180):
        raise AssertionError("original GQ flag-antiflag split changed")
    flags=45*V**2
    antiflags=180*V**2
    total=V**4
    if flags+antiflags!=total:
        raise AssertionError("combined named pin orbit partition invalid")
    if 720**3 % flags or 720**3 % antiflags:
        raise AssertionError("combined named pin orbit stabilizers noninteger")
    return {
        "original_point_line_named_pair_count":V*V,
        "physical_left_and_right_label_choices":V**2,
        "all_joint_one_eachd_side_pin_assignments":total,
        "joint_flag_prefix_orbit_size":flags,
        "joint_antiflag_prefix_orbit_size":antiflags,
        "joint_one_eachd_side_physical_and_GQ_orbit_count":2,
        "joint_flag_prefix_stabilizer":720**3//flags,
        "joint_antiflag_prefix_stabilizer":720**3//antiflags,
        "full_f_g_mapping_pair_orbits_computed":False,
    }


def W32_joint_global_orbit_count_lower():
    """Exact counting NO-GO for exhaustive quotient enumeration.

    The complete physical left/right K6 factor maps are independent
    bijections of 15 ORIGINAL points/lines onto 15 K6 pair edges.
    There are (15!)**2 actual legal mapping PAIRS. Every joint orbit
    has AT MOST |Sp4(2)|*|S6_L|*|S6_R| = 720**3 maps, with equality
    only when its stabilizer is trivial. Therefore number of JOINT
    ORBITS >= ceil((15!)**2/720**3), without assuming a free action.
    """
    total=factorial(15)**2
    G=720**3
    floor=(total+G-1)//G
    if floor!=4581437148288000:
        raise AssertionError("W32 global orbit lower integer drift")
    return {
        "full_W32_joint_left_right_mapping_pairs":total,
        "largest_possible_joint_orbit":G,
        "rigorous_number_joint_orbits_at_least":floor,
        "all_joint_orbits_exhaustively_enumerated":False,
        "symmetry_quotient_alone_is_not_feasible_exhaustive_search":True,
    }


def _physical_bijections(model):
    left,right,edges,_=validated_small_model(model)
    a=model["a"]
    palette=tuple(combinations(range(a),2))
    if len(left)!=len(palette) or len(right)!=len(palette):
        raise ValueError("finite C13 requires two COMPLETE K6 physical alphabets")
    index={e:i for i,e in enumerate(palette)}
    return tuple(index[e] for e in left),tuple(index[e] for e in right),palette


def joint_transport_W32(model, geometry_action, left_physical_action,
                        right_physical_action):
    """ONE simultaneous exact GQ original reindex plus BOTH physical maps.

    Input source incidence IDs stay the same finite canonical W(3,2)
    original factor graph; f'(sigma_P(i))=hL(f(i)),
    g'(sigma_L(j))=hR(g(j)).
    Reconstruct the actual column supports from the new f',g' (never
    retain stale model['supports'] after changing physical labels).
    """
    fp,fg,palette=_physical_bijections(model)
    V=len(fp)
    sigma_p,sigma_l=geometry_action
    hL,hR=tuple(left_physical_action),tuple(right_physical_action)
    if (any(len(t)!=V or set(t)!=set(range(V))
            for t in (sigma_p,sigma_l,hL,hR))):
        raise ValueError("geometry and physical actions must be complete bijections")
    # A random permutation of 15 physical PAIR-EDGE labels is a legal
    # new assignment but NOT a physical-coordinate automorphism.
    # Only genuine S6 coordinate actions preserve the 2factor targets.
    full_H=set(physical_coordinate_actions(
        model["a"],palette)["distinct_occupied_edge_actions"])
    if hL not in full_H or hR not in full_H:
        raise ValueError("claimed physical action is not induced by a coordinate automorphism")
    from hyp105_b1_symplectic import symplectic_gq
    _,_,_,original_edges=symplectic_gq(1)
    if {(sigma_p[i],sigma_l[j]) for i,j in original_edges}!=set(original_edges):
        raise ValueError("original action does not preserve true GQ incidence")
    transformed_f=[None]*V
    transformed_g=[None]*V
    for i in range(V):
        transformed_f[sigma_p[i]]=palette[hL[fp[i]]]
        transformed_g[sigma_l[i]]=palette[hR[fg[i]]]
    model_new=dict(model)
    model_new["left_labels"]=tuple(transformed_f)
    model_new["right_labels"]=tuple(transformed_g)
    a=model["a"]
    model_new["supports"]=tuple(
        tuple(sorted(model_new["left_labels"][i]
                     +tuple(a+x for x in model_new["right_labels"][j])))
        for i,j in model["incidences"])
    validated_small_model(model_new)
    return model_new


def joint_fixed_pair_stabilizer_W32(model, original_actions,
                                    physical_left_actions,
                                    physical_right_actions):
    """Count exact stabilizers in H_L x H_R x Sp4 by ONLY 720 sigma.

    For fixed complete bijective f and g and a chosen geometry action
    sigma, at most ONE induced physical edge action hL makes
      hL(f(i))=f(sigma_P(i))
    simultaneously for all i. Analogously hR for right lines.
    So testing membership in the physical groups gives the exact
    combined stabilizer WITHOUT 720^3 triple enumeration.
    """
    left,right,_=_physical_bijections(model)
    V=len(left)
    HL=set(physical_left_actions)
    HR=set(physical_right_actions)
    if not original_actions or not HL or not HR:
        raise ValueError("all three input groups must be nonempty")
    stabilizer=[]
    for pts,lns in original_actions:
        reqL=[-1]*V
        reqR=[-1]*V
        for i in range(V):
            reqL[left[i]]=left[pts[i]]
            reqR[right[i]]=right[lns[i]]
        if tuple(reqL) in HL and tuple(reqR) in HR:
            stabilizer.append((pts,lns))
    S=len(stabilizer)
    full_group_order=len(original_actions)*len(HL)*len(HR)
    if not S or full_group_order%S:
        raise AssertionError("joint orbit/stabilizer formula invalid")
    return {
        "original_incidence_automorphism_group_order":len(original_actions),
        "left_physical_edge_action_order":len(HL),
        "right_physical_edge_action_order":len(HR),
        "full_joint_group_order":full_group_order,
        "stabilizer_size_of_actual_pair_f_g":S,
        "joint_orbit_cardinality":full_group_order//S,
        "stabilizer_original_collineations":
            tuple(stabilizer),
        "all_orbit_members_are_true_correlated_f_g":True,
        "all_f_g_orbits_enumerated":False,
    }


def _best_physical_normal_form(bijection,actions):
    return min(tuple(h[x] for x in bijection) for h in actions)


def canonical_joint_pair_key_W32(model, original_actions, physical_actions,
                                 *, max_physical_normalizations=1200000):
    """Exact joint double-sided canonical key, not an approximate hash.

    For EACH original sigma, transport f/g back into the SAME canonical
    original IDs. Normalize f under ALL left-physical actions and g
    independently under ALL right-physical actions. Take the lex-min
    PAIR across ALL 720 simultaneous sigma choices. Two genuine
    W32 pairs have the same key IFF they belong to one joint orbit.
    """
    fp,fg,_=_physical_bijections(model)
    H=tuple(physical_actions)
    valid=set(physical_coordinate_actions(
        model["a"],tuple(combinations(range(model["a"]),2))
    )["distinct_occupied_edge_actions"])
    if set(H)!=valid or len(H)!=len(valid):
        raise ValueError("canonical normal form requires the EXACT full physical group")
    n=len(original_actions)*(2*len(H))
    if (type(max_physical_normalizations) is not int or
        max_physical_normalizations<1 or n>max_physical_normalizations):
        raise ValueError("full canonical search budget exceeded, no partial key")
    if not H:
        raise ValueError("empty physical group")
    V=len(fp)
    best=None
    for pts,lns in original_actions:
        left_reindexed=[None]*V
        right_reindexed=[None]*V
        for i in range(V):
            left_reindexed[pts[i]]=fp[i]
            right_reindexed[lns[i]]=fg[i]
        lkey=_best_physical_normal_form(left_reindexed,H)
        rkey=_best_physical_normal_form(right_reindexed,H)
        key=(lkey,rkey)
        if best is None or key<best:
            best=key
    if best is None:
        raise AssertionError("no canonical joint representative")
    return {
        "canonical_pair_key":best,
        "original_collineations_exhausted":len(original_actions),
        "physical_normalizations_exhausted":n,
        "all_three_actions_coupled_correctly":True,
        "no_all_f_g_minimum_claim":True,
    }


def W32_joint_orbit_report():
    """Real GQ W32 and *independent* exact seven-original-motif recount."""
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
    from hyp105_g5e2b3e1b0_seven_signature import seven_census
    from hyp105_g5e2b3e1c12_physical_orbits import genuine_W32_orbit_report

    A=w32_original_sp4_automorphisms()
    model=pair_labeled_symplectic(1,"reverse-line")
    group=physical_coordinate_actions(6,tuple(combinations(range(6),2)))
    H=group["distinct_occupied_edge_actions"]
    original_orbits=original_incidence_pair_orbits(A)
    one_each=W32_joint_one_left_one_right_pin_orbits()
    global_count=W32_joint_global_orbit_count_lower()
    cert=joint_fixed_pair_stabilizer_W32(model,A,H,H)
    key=canonical_joint_pair_key_W32(model,A,H)
    identity=tuple(range(15))
    # Both physical relabelings and a genuine NONIDENTITY geometry map:
    first=next(x for x in A if x!=(identity,identity))
    hL=next(x for x in H if x!=identity)
    hR=next(x for x in reversed(H) if x!=identity)
    transported=joint_transport_W32(model,first,hL,hR)
    normalized=canonical_joint_pair_key_W32(transported,A,H)
    if normalized["canonical_pair_key"]!=key["canonical_pair_key"]:
        raise AssertionError("joint triple action changed complete canonical key")
    census0=seven_census(model,independent_checks=False)
    census1=seven_census(transported,independent_checks=False)
    for field in ("seven_class_motif_counts","S_seven","GF5_seven_lower_numerator"):
        if census0[field]!=census1[field]:
            raise AssertionError("joint-original-incidence physical action changed "+field)
    # Independent reference C12 verifies true right physical action and
    # W32 C11 original four-right-line simultaneous completion.
    reference=genuine_W32_orbit_report()
    if (reference["real_W32_original_S_seven"]!=169 or
        reference["real_W32_BA_minimizer_S_seven"]!=141):
        raise AssertionError("true W32 seven-original-class baseline drift")
    return {
        "scope":"GENUINE_W32_BOTH_LEFT_AND_RIGHT_COMPLETE_PHYSICAL_K6",
        "original_sp4_order":len(A),
        "physical_left_S6_order":len(H),
        "physical_right_S6_order":len(H),
        "joint_group_order":cert["full_joint_group_order"],
        "named_one_left_one_right_pin_orbits":
            one_each["joint_one_eachd_side_physical_and_GQ_orbit_count"],
        "joint_flag_named_pin_orbit_size":one_each["joint_flag_prefix_orbit_size"],
        "joint_antiflag_named_pin_orbit_size":
            one_each["joint_antiflag_prefix_orbit_size"],
        "full_joint_left_right_mapping_pairs":
            global_count["full_W32_joint_left_right_mapping_pairs"],
        "rigorous_joint_mapping_pair_orbits_at_least":
            global_count["rigorous_number_joint_orbits_at_least"],
        "actual_original_pair_stabilizer":cert["stabilizer_size_of_actual_pair_f_g"],
        "actual_joint_f_g_orbit_size":cert["joint_orbit_cardinality"],
        "canonical_joint_pair_key_invariant_under_nontrivial_triple":True,
        "canonical_normalizations_per_model":
            key["physical_normalizations_exhausted"],
        "original_point_line_orbits":
            original_orbits["orbit_cardinalities"],
        "original_incidence_flags":original_orbits["original_incidence_flags"],
        "original_nonincident_antiflags":
            original_orbits["original_nonincident_antiflags"],
        "same_map_seven_original_S":census0["S_seven"],
        "same_map_transformed_S":census1["S_seven"],
        "same_map_all_seven_class_counts_preserved":True,
        "same_map_GF5_necessary_floor_numerator":
            census0["GF5_seven_lower_numerator"],
        "C12_real_original_S":reference["real_W32_original_S_seven"],
        "C12_BA_minimizing_right_map_seven_S":
            reference["real_W32_BA_minimizer_S_seven"],
        "joint_orbit_all_f_g_exhausted":False,
        "all_h_uniform_seven_class_lower_proved":False,
        "full_GF5_R3_evaluated":False,
    }


if __name__=="__main__":
    import json
    print(json.dumps(W32_joint_orbit_report(),indent=2,sort_keys=True))
