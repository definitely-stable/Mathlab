"""HYP-105 #230 AA4-CB: original sixpacket physical parity-code sieve.

The SIX switched original line-image pairs determine a binary incidence
difference matrix D. Physical right 2-regularity implies a zero parity
syndrome, so every positive GF(5) original Q indicator has support in
ONE affine coset of ker D. Global physical edge injection + one feasible
six-edge 2-factor imply rank(D)>=2. An exact 16-profile four-syndrome
finite certificate yields high-pass eta_6 <=54/64 =27/32. This improves
AA4-CA's abstract Boolean N3 eta=60/64=15/16.

The constant 54/64 is sharp for the relaxed rank-two parity-code SUPPORT
class, NOT asserted sharp for realizable original W(3,s) physical pairs
or historically GF5 positive motifs. No root #230 Branch A/B/C.
"""
from collections import Counter
from fractions import Fraction

from hyp105_issue230_d6aa4ca_exact_n3_boolean_kernel import (
    AA4CA_EXACT_ABSTRACT_N3_ETA6,
    original_W32_f_only_all_seven_exact_n3_envelope,
    original_W32_all64_true_center_exact_n3,
    assert_n3_independent_cube,
)
from hyp105_issue230_d6aa4by_original_independent_2factor_kernel import (
    original_six_packet_source_line_A,
)
from hyp105_issue230_d6aa4bq_all_seven_reverse_switching import (
    validate_disjoint_factor_swaps,
)
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source

K6 = (22, -10, 2, 2, -2, -2, 10)
GLOBAL_PARITY_CODE_ETA = Fraction(27, 32)
GLOBAL_CA_TO_CB_SAVING = AA4CA_EXACT_ABSTRACT_N3_ETA6 - GLOBAL_PARITY_CODE_ETA
RANK2_MAX_SIGNED_NUMERATOR = 54


def _edge(edge):
    try:
        a, b = tuple(edge)
    except (TypeError, ValueError):
        raise ValueError("physical edge must contain two endpoints") from None
    if (type(a) is not int or type(b) is not int
            or min(a, b) < 0 or a == b):
        raise ValueError("physical coordinates are distinct nonnegative integers")
    return tuple(sorted((a, b)))


def parity_columns_from_12_images(packet_edges):
    """Six pairs of globally DISTINCT actual physical unordered edge images.

    Each D_i = (1_{e_i^0}+1_{e_i^1}) mod 2 as coordinate bit mask.
    """
    packets = tuple(packet_edges)
    if len(packets) != 6:
        raise ValueError("six disjoint image packets required")
    seen = set()
    result = []
    for pair in packets:
        try:
            e, a = tuple(pair)
        except (TypeError, ValueError):
            raise ValueError("one pair of alternative edges per packet") from None
        e, a = _edge(e), _edge(a)
        if e in seen or a in seen or e == a:
            raise ValueError("12 distinct original physical pair images required")
        seen.add(e)
        seen.add(a)
        d = ((1 << e[0]) ^ (1 << e[1])
             ^ (1 << a[0]) ^ (1 << a[1]))
        if d.bit_count() not in (2, 4):
            raise AssertionError("distinct unordered pair edges differ on 2/4 endpoints")
        result.append(d)
    return tuple(result)


def gf2_rank(columns):
    """RREF-free exact GF(2) row-independent column rank (big integers)."""
    basis = {}
    for column in columns:
        if type(column) is not int or column < 0:
            raise ValueError("GF2 columns are nonnegative integer bit vectors")
        c = column
        while c:
            leading = c.bit_length() - 1
            if leading not in basis:
                basis[leading] = c
                break
            c ^= basis[leading]
    return len(basis)


def syndrome(columns, cube_vertex):
    if len(columns) != 6 or type(cube_vertex) is not int or not 0 <= cube_vertex < 64:
        raise ValueError("six columns and one cube vertex 0..63 required")
    out = 0
    for i, c in enumerate(columns):
        if cube_vertex >> i & 1:
            out ^= c
    return out


def affine_kernel_bound(columns):
    """Exact global-state coset K6 bound for the GIVEN physical packets.

    All actual original accepted states lie in one parity syndrome coset
    (necessarily syndrome of the original baseline physical edge degrees).
    For every possible center (XOR translation), that coset is one of the
    syndrome buckets of all 64 states; optimize positive/negative kernel
    weights over buckets, with no independence or physical realizability
    asserted for the chosen subset.
    """
    columns = tuple(columns)
    if len(columns) != 6 or any(type(c) is not int or c <= 0 for c in columns):
        raise ValueError("six nonzero binary columns required")
    rank = gf2_rank(columns)
    if rank == 1:
        # Rank-1 columns from 12 globally distinct physical edge images
        # cannot have ANY 2-regular selected six-edge state (all-h lemma).
        return {"rank": 1, "eta": Fraction(0), "numerator": 0,
                "rank_one_no_real_2factor": True}
    if rank < 2:
        raise ValueError("six different original physical edge images forbid rank 0")
    cells = {}
    for x in range(64):
        cells.setdefault(syndrome(columns, x), []).append(x)
    if len(cells) != (1 << rank):
        raise AssertionError("GF2 rank/syndrome cardinality mismatch")
    signed_positive = max(sum(max(K6[x.bit_count()], 0) for x in coset)
                          for coset in cells.values())
    signed_negative = max(sum(max(-K6[x.bit_count()], 0) for x in coset)
                          for coset in cells.values())
    bound = max(signed_positive, signed_negative)
    if bound > RANK2_MAX_SIGNED_NUMERATOR:
        raise AssertionError("rank>=2 code violated exhaustive rank2 upper bound")
    return {"rank": rank, "eta": Fraction(bound, 64),
            "numerator": bound, "signed_positive_max": signed_positive,
            "signed_negative_magnitude_max": signed_negative,
            "coset_count": len(cells), "coset_size": 1 << (6-rank),
            "rank_one_no_real_2factor": False}


def profile_scores(n0, n1, n2, n3):
    """Independent syndrome-generating-polynomial exact multiplication.

    Coefficients are six-bit weight and F2^2 syndrome:
    (1+z)^n0 (1+z U_1)^n1 (1+z U_2)^n2 (1+z U_3)^n3,
    where U_s U_t = U_(s xor t). No LP or floating point.
    """
    counts = tuple((n0, n1, n2, n3))
    if any(type(v) is not int or v < 0 for v in counts) or sum(counts) != 6:
        raise ValueError("nonnegative four-color coordinate counts summing to six")
    state = {(0, 0): 1}
    for typ, mult in enumerate(counts):
        for _ in range(mult):
            new = dict(state)
            for (weight, synd), v in state.items():
                key = (weight+1, synd ^ typ)
                new[key] = new.get(key, 0) + v
            state = new
    assert sum(state.values()) == 64
    return tuple((
        sum(n * max(0, K6[j]) for (j, t), n in state.items() if t == s),
        sum(n * max(0, -K6[j]) for (j, t), n in state.items() if t == s),
    ) for s in range(4))


def exact_rank2_profile_certificate():
    """All 16 unordered GL2-color count profiles, finite complete proof.

    Every rank-two map GF2^6 -> GF2^2 has columns of type
    0,1,2,3. GL(2,2) permutes the THREE nonzero types, so represent
    n1>=n2>=n3, with n2>=1 (rank exactly two), n0+n1+n2+n3=6.
    The 16 listed profiles exhaust EVERY rank-two parity-check matrix,
    even those with zero columns. Their exact max equals 54.
    """
    result = {}
    for n0 in range(7):
        for n1 in range(7-n0):
            for n2 in range(n1+1):
                n3 = 6-n0-n1-n2
                if 0 <= n3 <= n2 and n2 >= 1:
                    score = profile_scores(n0, n1, n2, n3)
                    result[(n0,n1,n2,n3)] = max(max(v) for v in score)
    if len(result) != 16 or max(result.values()) != 54:
        raise AssertionError("complete 16-profile finite rank2 theorem failed")
    return result


def independent_rank2_dual_mask_oracle():
    """Independent direct enumeration of all 651 2-D dual row spaces.

    Each nonzero 2-D subspace {0,u,v,u^v} has one sorted triple of
    nonzero masks; consider all four cosets by syndrome and every one
    of 64 cube vertices, no use of profile DP or GL2 reduction.
    """
    seen = set()
    hist = Counter()
    max_score = -1
    witness = None
    for u in range(1, 64):
        for v in range(u+1, 64):
            key = tuple(sorted((u, v, u ^ v)))
            if key in seen:
                continue
            seen.add(key)
            groups = [[], [], [], []]
            for x in range(64):
                groups[((u & x).bit_count() & 1) |
                       (((v & x).bit_count() & 1) << 1)].append(x)
            this_max = max(max(
                sum(max(0, K6[x.bit_count()]) for x in group),
                sum(max(0, -K6[x.bit_count()]) for x in group)
            ) for group in groups)
            hist[this_max] += 1
            if this_max > max_score:
                max_score, witness = this_max, (u, v)
    if len(seen) != 651 or max_score != 54:
        raise AssertionError("independent 651-space dual oracle mismatch")
    return {"dual_spaces": len(seen), "max_abs_numerator": max_score,
            "score_histogram": dict(sorted(hist.items())),
            "one_witness_row_masks": witness}


def original_packet_parity_columns(model, packets):
    """One complete original LINE map, no independently redrawn Q."""
    s,V,a,inc,f,g,_,_ = _original_source(model)
    packets = validate_disjoint_factor_swaps(V, packets)
    if len(packets) != 6:
        raise ValueError("six genuine original source LINE packets required")
    cols = parity_columns_from_12_images(tuple((g[u],g[v]) for u,v in packets))
    return cols


def original_Q_parity_sieve(model, Q, packets):
    """Physical 64-state exact oracle on SIX SAME ORIGINAL flag IDs.

    Compare with independent full-global-g^x oracle in the test file.
    """
    s,V,a,inc,f,g,_,_ = _original_source(model)
    packets = validate_disjoint_factor_swaps(V,packets)
    if not original_six_packet_source_line_A(Q, inc, packets, V):
        raise ValueError("Q must touch all six genuine original LINE packets")
    source_lines = frozenset(inc[j][1] for j in Q)
    actual_edges = tuple(
        (g[u],g[v]) if u in source_lines else (g[v],g[u])
        for u,v in packets)
    cols = parity_columns_from_12_images(actual_edges)
    info = affine_kernel_bound(cols)
    valid = []
    for x in range(64):
        edges = tuple(packet[x >> i & 1] for i,packet in enumerate(actual_edges))
        d = Counter(vertex for edge in edges for vertex in edge)
        ok = int(len(d)==6 and all(count==2 for count in d.values()))
        valid.append(ok)
        if ok and syndrome(cols, x) != syndrome(cols, 0):
            raise AssertionError("original physical 2factor violates parity syndrome")
    if info["rank"] == 1 and any(valid):
        raise AssertionError("rank one cannot produce physical original 2factor")
    for origin in range(64):
        signed = sum(valid[x]*K6[(origin ^ x).bit_count()]
                     for x in range(64))
        if abs(signed)>info["numerator"]:
            raise AssertionError("real original Q exceeds exact code kernel norm")
    return {"physical_indicator":tuple(valid), "parity_rank":info["rank"],
            "physical_active_states":sum(valid),
            "physical_code_eta":info["eta"],
            "columns":cols, "original_source_Q":tuple(Q),
            "same_g_global_physical_support":True}


def original_W32_f_only_all_seven_parity_envelope(model, packets):
    """Universal new f-only E and stronger actual-(f,g)-aware E."""
    prev=original_W32_f_only_all_seven_exact_n3_envelope(model,packets)
    H=prev["original_source_Q_weight"]
    rank_code=affine_kernel_bound(original_packet_parity_columns(model,packets))
    eta=rank_code["eta"]
    universal=prev["new_AA4CA_E"]-GLOBAL_CA_TO_CB_SAVING*H
    adaptive=prev["new_AA4CA_E"]-(AA4CA_EXACT_ABSTRACT_N3_ETA6-eta)*H
    if adaptive>universal or min(adaptive,universal)<0:
        raise AssertionError("original seven-class new envelope invariant broken")
    return {
        "original_f_only_six_source_Q_weight":H,
        "parent_CA_f_only_E":prev["new_AA4CA_E"],
        "new_CB_universal_f_only_E":universal,
        "new_CB_actual_f_g_rank_adaptive_E":adaptive,
        "strict_universal_saving":GLOBAL_CA_TO_CB_SAVING*H,
        "physical_packet_rank":rank_code["rank"],
        "physical_packet_coset_eta":eta,
        "all_seven_original_selected_GF5_not_full_R3":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


def original_W32_all64_true_center_parity_envelope(model,packets):
    parent=original_W32_all64_true_center_exact_n3(model,packets)
    env=original_W32_f_only_all_seven_parity_envelope(model,packets)
    E=env["new_CB_actual_f_g_rank_adaptive_E"]
    low=parent["original_low_order"]
    W=parent["original_weighted_center"]
    if abs(parent["original_high_order"])>E or low-E>W:
        raise AssertionError("genuine seven-GF5 highpass violates new parity envelope")
    return {"actual_weighted_original_GF5_center":W,
            "new_rank_adaptive_E":E,
            "certified_center_lower":max(Fraction(0),low-E),
            "rank":env["physical_packet_rank"],
            "root_230":"OPEN_WITH_FORMAL_BLOCKER"}
