"""AA4-PC3: ALL-h exact ORIGINAL accepted D6 via triple PAIR-codegree witnesses.

Earlier AA4-TCN uses only physically complete K3,3 as a positive
D6 subfamily. Here ANY rainbow physical C6 is enumerated directly by
three physically separated hub corners h0<h1<h2 and three coordinate
transverse witnesses:
 z01 in N(h0)&N(h1),
 z12 in N(h1)&N(h2),
 z20 in N(h2)&N(h0).
Six first and six second coordinates must be pairwise distinct.

Every accepted original six-source-flag GF5 D6 physical six-cycle
has EXACTLY TWO representations (its two alternating hub triples).
Consequently EXACTLY, for all h and every legal correlated map:
  2*D6 = sum_{h0<h1<h2: hub coordinates injective}
    sum_{z01 in CN01,z12 in CN12,z20 in CN20}
       1[all 6 first coordinates and all 6 second coordinates distinct].

The triple-COMMON-neighbor/K3,3 sector of #657 corresponds to triples
z01,z12,z20 all in N(h0)&N(h1)&N(h2); other D6 motifs can occur when
no such K3,3 exists. All physical arcs derive from genuine ORIGINAL
W(3,s) point-line incidence flags, not synthetic physical graphs.
"""
from collections import Counter, defaultdict
from itertools import combinations

from hyp105_b1_symplectic import symplectic_gq
from hyp105_physical_rainbow_c6 import (
    build_original_physical_graph, exact_rainbow_c6_finite,
)


def exact_pair_codegree_triangle_d6(power, f, g, *,
                                     verify_historical_gf5=True,
                                     verify_existing_C6_oracle=True):
    """Finite GF2/GF4 ORIGINAL point-line incidence preserving D6 oracle.

    Independently indexed by PAIR common-neighbor posting lists, not
    physical simple-C6 path DFS nor K3,3 triple-common-neighbor code.
    """
    if type(power) is not int or power not in (1,2):
        raise ValueError("source exact finite pair-codegree oracle h=1,2 only")
    s=1<<power
    _,points,lines,flags=symplectic_gq(power)
    V=(s+1)*(s*s+1)
    if len(points)!=V or len(lines)!=V:
        raise AssertionError("non-genuine original symplectic W(3,s)")
    f,g=tuple(map(tuple,f)),tuple(map(tuple,g))
    adj,original_arc_ids=build_original_physical_graph(s,f,g,flags)
    if verify_historical_gf5:
        from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked

    # Invert the two-edge physical wedge relation. Each pair of physical
    # hubs is posted ONCE per genuine physical common neighbor.
    common_pairs=defaultdict(set)
    for z,neighbors in adj.items():
        for h0,h1 in combinations(sorted(neighbors),2):
            common_pairs[h0,h1].add(z)
    neighborhood_of_hubs=defaultdict(set)
    for h0,h1 in common_pairs:
        neighborhood_of_hubs[h0].add(h1)
        neighborhood_of_hubs[h1].add(h0)

    source_six_multiplicity=Counter()
    total_oriented=0
    from_complete_K33=0
    inspected_triangle_hub_triples=0
    for h0 in sorted(neighborhood_of_hubs):
        for h1 in sorted(z for z in neighborhood_of_hubs[h0] if z>h0):
            pair0=common_pairs[h0,h1]
            for h2 in sorted(z for z in (
                    neighborhood_of_hubs[h0] &
                    neighborhood_of_hubs[h1]) if z>h1):
                hub_x={h0[0],h1[0],h2[0]}
                hub_y={h0[1],h1[1],h2[1]}
                if len(hub_x)!=3 or len(hub_y)!=3:
                    continue
                q01=tuple(sorted(z for z in pair0
                                 if z[0] not in hub_x and z[1] not in hub_y))
                q12=tuple(sorted(z for z in common_pairs[h1,h2]
                                 if z[0] not in hub_x and z[1] not in hub_y))
                q20=tuple(sorted(z for z in common_pairs[h0,h2]
                                 if z[0] not in hub_x and z[1] not in hub_y))
                if not q01 or not q12 or not q20:
                    continue
                inspected_triangle_hub_triples+=1
                common3=adj[h0] & adj[h1] & adj[h2]
                for z01 in q01:
                    for z12 in q12:
                        if z01[0]==z12[0] or z01[1]==z12[1]:
                            continue
                        for z20 in q20:
                            if (z20[0] in (z01[0],z12[0]) or
                                    z20[1] in (z01[1],z12[1])):
                                continue
                            cyc=(h0,z01,h1,z12,h2,z20)
                            if (len({v[0] for v in cyc})!=6 or
                                    len({v[1] for v in cyc})!=6):
                                raise AssertionError("not a rainbow source cycle")
                            ids=tuple(sorted(
                                original_arc_ids[cyc[i],cyc[(i+1)%6]]
                                for i in range(6)))
                            if len(set(ids))!=6 or (
                                len({flags[k][0] for k in ids})!=6 or
                                len({flags[k][1] for k in ids})!=6
                            ):
                                raise AssertionError("D6 source ORIGINAL factor collision")
                            if verify_historical_gf5 and (
                                classify_seven_prechecked(ids,f,g,flags)!="D6"
                            ):
                                raise AssertionError("pair witness not accepted historical GF5 D6")
                            source_six_multiplicity[ids]+=1
                            total_oriented+=1
                            if (z01 in common3 and z12 in common3 and
                                    z20 in common3):
                                from_complete_K33+=1
    if any(v!=2 for v in source_six_multiplicity.values()):
        raise AssertionError("every ORIGINAL D6 sixset needs exactly TWO alternating hub triples")
    if total_oriented!=2*len(source_six_multiplicity):
        raise AssertionError("source D6 pair-witness double cover malformed")
    if from_complete_K33%2:
        raise AssertionError("physical K3,3 witness part not doubled")
    if verify_existing_C6_oracle:
        separate=exact_rainbow_c6_finite(
            power,f,g,verify_GF5=verify_historical_gf5)
        if len(source_six_multiplicity)!=separate["D6_original_sixsets"]:
            raise AssertionError("independent true-source physical D6 C6 oracle disagrees")
    return {
        "s":s,"V":V,
        "physical_hub_pairs_with_nonempty_codegree":len(common_pairs),
        "candidate_hub_triangles":inspected_triangle_hub_triples,
        "oriented_pair_codegree_witness_triples":total_oriented,
        "accepted_original_D6":len(source_six_multiplicity),
        "oriented_complete_K33_witnesses":from_complete_K33,
        "accepted_original_D6_from_complete_K33":from_complete_K33//2,
        "non_K33_accepted_original_D6":
            len(source_six_multiplicity)-from_complete_K33//2,
        "all_h_exact_pair_codegree_D6_identity_proved":True,
        "all_h_seven_accepted_classes_proved":False,
        "root_Omega_s6_proved":False,
    }
