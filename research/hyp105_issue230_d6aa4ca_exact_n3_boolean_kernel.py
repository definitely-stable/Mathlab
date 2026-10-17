"""AA4-CA: exact abstract N3-independent sixcube highpass norm.

For EVERY true-original sixth-packet six-incidence indicator in the
symplectic W(3,2^h) source model, previous AA4-BY/BZ imply:
(1) no adjacent 1s, and (2) <=3 neighbors 1 of any vertex.
An exhaustive, finite, proof-by-enumeration 6-vertex set-system lemma
gives the SHARP norm 60/64 = 15/16 over this BOOLEAN constraint class.
Sharpness here is NOT a physical/GF5/W3 realization claim.
All source statements are uniform over complete correlated original f,g.
"""
from array import array
from itertools import combinations, permutations
from fractions import Fraction

from hyp105_issue230_d6aa4bz_original_neighbor_three_kernel import (
    CUBE6_NEIGHBOR_THREE_HIGH_PASS,
    original_W32_f_only_all_seven_neighbor_three_envelope,
    original_W32_all64_true_center_neighbor_three,
)
from hyp105_issue230_d6aa4bx_all_seven_center_kernel import high_degree_boolean_kernel

AA4CA_EXACT_ABSTRACT_N3_ETA6 = Fraction(15, 16)
AA4CA_BZ_TO_CA_SAVING = CUBE6_NEIGHBOR_THREE_HIGH_PASS - AA4CA_EXACT_ABSTRACT_N3_ETA6
K6 = (22, -10, 2, 2, -2, -2, 10)
PAIRS = tuple(combinations(range(6), 2))
TRIPLES = tuple(combinations(range(6), 3))
QUADS = tuple(combinations(range(6), 4))
PAIR_ID = {e: i for i, e in enumerate(PAIRS)}
TRIPLE_ID = {e: i for i, e in enumerate(TRIPLES)}
FULL_PAIRS = (1 << len(PAIRS)) - 1


def _triple_incidence():
    pair_triples = tuple(
        sum(1 << j for j, t in enumerate(TRIPLES) if set(p) <= set(t))
        for p in PAIRS
    )
    quad_triples = tuple(
        sum(1 << TRIPLE_ID[t] for t in combinations(q, 3))
        for q in QUADS
    )
    triple_pairs = tuple(
        sum(1 << PAIR_ID[p] for p in combinations(t, 2))
        for t in TRIPLES
    )
    return pair_triples, quad_triples, triple_pairs


def exhaustive_pair_triple_lemma():
    """Exact finite universal certificate, no optimization libraries.

    E are selected Hamming-layer-2 pairs, H layer-3 triples.
    Necessary N3+independence constraints:
      every vertex belongs to <=3 E;
      every 2-set belongs to <=3 H;
      every 4-set contains <=3 H;
      no E is contained in any H.
    Prove max |E|+|H|=14. Enumerate all 2^20 H masks, then
    maximize E over the allowed 2^15 graph masks using subset-zeta DP.
    All indices are fixed lexicographic 6-element subsets; no random data.
    """
    pt, qt, tp = _triple_incidence()
    best_edges = array("b", [-100]) * (1 << 15)
    for m in range(1 << 15):
        if all(sum((m >> i) & 1 for i, p in enumerate(PAIRS) if v in p) <= 3
               for v in range(6)):
            best_edges[m] = m.bit_count()
    for i in range(15):
        bit = 1 << i
        for m in range(1 << 15):
            if m & bit and best_edges[m ^ bit] > best_edges[m]:
                best_edges[m] = best_edges[m ^ bit]
    forbidden = array("H", [0]) * (1 << 20)
    best = -1
    witness = None
    admissible_h = 0
    for h in range(1 << 20):
        if h:
            bit = h & -h
            forbidden[h] = forbidden[h ^ bit] | tp[bit.bit_length() - 1]
        if any((h & p).bit_count() > 3 for p in pt):
            continue
        if any((h & q).bit_count() > 3 for q in qt):
            continue
        admissible_h += 1
        allowable_e = FULL_PAIRS ^ forbidden[h]
        score = h.bit_count() + best_edges[allowable_e]
        if score > best:
            best = score
            witness = (h, best_edges[allowable_e])
    return {
        "max_layer2_plus_layer3": best,
        "valid_triple_families": admissible_h,
        "triple_family_domain_size": 1 << 20,
        "pair_graph_domain_size": 1 << 15,
        "lex_first_maximizer_triple_mask": witness[0],
        "lex_first_maximizer_number_pairs": witness[1],
    }


def independent_pair_graph_orbit_lemma():
    """Independent exact verifier: enumerate E first and quotient by S6.

    This DOES NOT share subset-zeta DP or forbidden-pair mask recurrence
    with exhaustive_pair_triple_lemma. It enumerates all 2^15 graphs,
    retains degree <=3, canonically reduces under all 720 relabelings,
    and enumerates ALL allowed 3-set subfamilies per representative.
    Returns the same exact global upper bound.
    """
    relabels = tuple(
        tuple(PAIR_ID[tuple(sorted((sigma[a], sigma[b])))]
              for a, b in PAIRS) for sigma in permutations(range(6))
    )
    orbit_reps = {}
    for graph in range(1 << 15):
        if any(sum((graph >> i) & 1 for i, p in enumerate(PAIRS) if v in p) > 3
               for v in range(6)):
            continue
        canonical = min(
            sum(1 << tr[i] for i in range(15) if graph >> i & 1)
            for tr in relabels
        )
        orbit_reps.setdefault(canonical, graph)
    max_score = -1
    for graph in orbit_reps:
        allowed = tuple(
            t for t in TRIPLES
            if all(not (graph >> PAIR_ID[p] & 1) for p in combinations(t, 2))
        )
        pair_masks = tuple(
            sum(1 << j for j, t in enumerate(allowed) if set(p) <= set(t))
            for p in PAIRS
        )
        quad_masks = tuple(
            sum(1 << j for j, t in enumerate(allowed) if set(t) <= set(q))
            for q in QUADS
        )
        for h in range(1 << len(allowed)):
            if any((h & p).bit_count() > 3 for p in pair_masks):
                continue
            if any((h & q).bit_count() > 3 for q in quad_masks):
                continue
            max_score = max(max_score, graph.bit_count() + h.bit_count())
    return {"max_layer2_plus_layer3": max_score,
            "nonisomorphic_degree3_pair_graphs": len(orbit_reps),
            "all_pair_graphs_checked": 1 << 15,
            "symmetric_group_size": len(relabels)}


def assert_n3_independent_cube(bits):
    """Independent direct 64-state falsifier with no source-GQ oracle."""
    b = tuple(int(v) for v in bits)
    if len(b) != 64 or any(v not in (0, 1) for v in b):
        raise ValueError("expected exactly 64 Boolean cube states")
    if any(b[x] and b[x ^ (1 << i)] for x in range(64)
           for i in range(6)):
        raise ValueError("adjacent accepted states")
    if any(sum(b[x ^ (1 << i)] for i in range(6)) > 3
           for x in range(64)):
        raise ValueError("more than three accepted neighbors")
    return True


def signed_kernel_numerator(bits, center=0):
    assert_n3_independent_cube(bits)
    if not isinstance(center, int) or not 0 <= center < 64:
        raise ValueError("center must be a cube vertex 0..63")
    return sum(int(v) * K6[(center ^ i).bit_count()]
               for i, v in enumerate(bits))


def sharp_abstract_witnesses():
    """Two explicit extremizers for the ABSTRACT constraints only."""
    missing = {(0, 1, 4), (0, 1, 5), (0, 2, 3),
               (1, 2, 3), (2, 4, 5), (3, 4, 5)}
    positive_triples = set(TRIPLES) - missing
    pos = tuple(int(x in (0, 63) or
                    (x.bit_count() == 3 and
                     tuple(i for i in range(6) if x >> i & 1)
                     in positive_triples)) for x in range(64))
    negative_4sets = {
        tuple(i for i in range(6) if i not in (a, b))
        for a in range(3) for b in range(3, 6)
    }
    neg = tuple(int((x in (1, 2, 4)) or
                    (x.bit_count() == 4 and
                     tuple(i for i in range(6) if x >> i & 1)
                     in negative_4sets)) for x in range(64))
    assert_n3_independent_cube(pos)
    assert_n3_independent_cube(neg)
    if signed_kernel_numerator(pos) != 60 or signed_kernel_numerator(neg) != -48:
        raise AssertionError("abstract exact witnesses drifted")
    return pos, neg


def exact_n3_boolean_sixcube_certificate():
    a = exhaustive_pair_triple_lemma()
    b = independent_pair_graph_orbit_lemma()
    if a["max_layer2_plus_layer3"] != 14 or b["max_layer2_plus_layer3"] != 14:
        raise AssertionError("finite six-vertex packing lemma is false")
    pos, neg = sharp_abstract_witnesses()
    kernel = high_degree_boolean_kernel(6)
    if tuple(kernel[x] for x in range(64)) != tuple(
        K6[x.bit_count()] for x in range(64)):
        raise AssertionError("historical Walsh degree-4+ kernel drift")
    if AA4CA_EXACT_ABSTRACT_N3_ETA6 != Fraction(60, 64):
        raise AssertionError("incorrect highpass bound")
    if AA4CA_BZ_TO_CA_SAVING != Fraction(19, 128):
        raise AssertionError("incorrect strict BZ saving")
    return {
        "subset_dp": a, "orbit_independent_oracle": b,
        "signed_upper": 60, "signed_lower": -48,
        "positive_witness": tuple(i for i, v in enumerate(pos) if v),
        "negative_witness": tuple(i for i, v in enumerate(neg) if v),
        "exact_abstract_boolean_eta6": AA4CA_EXACT_ABSTRACT_N3_ETA6,
        "strict_saving_from_BZ": AA4CA_BZ_TO_CA_SAVING,
        "sharp_for_actual_physical_GF5": False,
        "root_230": "OPEN_WITH_FORMAL_BLOCKER",
    }


def original_W32_f_only_all_seven_exact_n3_envelope(model, packets):
    """Refine historical genuine original f-only W32 seven-GF5 E, not R3."""
    old = original_W32_f_only_all_seven_neighbor_three_envelope(model, packets)
    mass = old["weighted_six_source_packet_original_Q_mass"]
    new = old["new_original_f_only_ALL_SEVEN_error_upper"] - AA4CA_BZ_TO_CA_SAVING * mass
    if new < 0:
        raise AssertionError("negative full original-GF5 error bound")
    return {
        "parent_BZ_E": old["new_original_f_only_ALL_SEVEN_error_upper"],
        "new_AA4CA_E": new,
        "original_source_Q_weight": mass,
        "strict_saving": AA4CA_BZ_TO_CA_SAVING * mass,
        "new_sixcube_eta6": AA4CA_EXACT_ABSTRACT_N3_ETA6,
        "root_230": "OPEN_WITH_FORMAL_BLOCKER",
    }


def original_W32_all64_true_center_exact_n3(model, packets):
    parent = original_W32_all64_true_center_neighbor_three(model, packets)
    env = original_W32_f_only_all_seven_exact_n3_envelope(model, packets)
    high = parent["original_center_actual_degree4_through6_signed"]
    low = parent["original_zero_through_third_Walsh_at_unchanged_center"]
    actual = parent["original_seven_GF5_unchanged_center"]
    if abs(high) > env["new_AA4CA_E"] or low - env["new_AA4CA_E"] > actual:
        raise AssertionError("new error envelope violated by true original W32 GF5")
    return {
        "original_weighted_center": actual,
        "original_low_order": low,
        "original_high_order": high,
        "new_error_bound": env["new_AA4CA_E"],
        "certified_center_lower": max(Fraction(0), low - env["new_AA4CA_E"]),
        "root_230": "OPEN_WITH_FORMAL_BLOCKER",
    }
