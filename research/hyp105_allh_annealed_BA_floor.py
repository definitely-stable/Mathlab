"""AA4-ANNBA: all-h uniform conditional *annealed* original B/A GF5 floor.

For ANY legal injective full f on true W(3,s), ANY b frozen source
lines J and ANY legal fixed injective labels g_J, let the other original
line factor labels be assigned uniformly without replacement from unused
physical pair edges of K_a. Then the exact bound below holds on
E_g U_{B-left/A-right}(f,g) using solely original incidence IDs.

It is POSITIVE for all dyadic s>=8 when J is empty; for b=12 it becomes
positive for s>=32. For arbitrary b_s=o(s), the all-h uniform annealed
liminf lower constant is >=140 in s^6 units. This is NOT a bound
for every g, nor a root Branch A/B/C proof, nor total GF5 R3.
"""
from fractions import Fraction
from itertools import combinations
from math import comb, prod

from hyp105_physical_degree_energy import minimal_alphabet


def falling(n, k):
    """Exact integer falling factorial, zero when fewer than k slots."""
    if type(n) is not int or type(k) is not int or k < 0:
        raise ValueError("nonnegative integer factors required")
    return prod(range(n-k+1, n+1)) if n >= k else 0


def validate_typed_pairs(s, labels, *, partial=False):
    """Validate actual original typed injection (without pretending a proxy GQ)."""
    if type(s) is not int or s < 2 or s & (s-1):
        raise ValueError("s must equal 2^h, h>=1")
    V = (s+1)*(s*s+1)
    a = minimal_alphabet(V)
    labels = tuple(tuple(e) for e in labels)
    if not partial and len(labels) != V:
        raise ValueError("a complete original point map requires V pair labels")
    if len(labels) > V or len(set(labels)) != len(labels) or any(
            len(e) != 2 or type(e[0]) is not int or type(e[1]) is not int or
            not 0 <= e[0] < e[1] < a for e in labels):
        raise ValueError("typed original pair labels must be distinct legal K_a edges")
    return labels


def exact_twofactor_count(a, forbidden=()):
    """Independent tiny-alphabet oracle: count physical 2-factors, not labels.

    Exhaust all C(a,6)*70 labelled six-edge 2-factors; for a=6,7 only.
    C6 or two disjoint triangles are accepted for right A on left B.
    """
    if type(a) is not int or not 6 <= a <= 7:
        raise ValueError("independent oracle supports a=6,7 only")
    F = set(tuple(x) for x in forbidden)
    if len(F) != len(tuple(forbidden)):
        raise ValueError("repeated forbidden pair edge")
    out = 0
    containing = {}
    for six in combinations(range(a), 6):
        six_edges = tuple(combinations(six,2))
        for candidate in combinations(six_edges, 6):
            degrees = {x:0 for x in six}
            for u,v in candidate:
                degrees[u] += 1
                degrees[v] += 1
            if any(z != 2 for z in degrees.values()):
                continue
            if not any(z in F for z in candidate):
                out += 1
            for pair in candidate:
                containing[pair] = containing.get(pair,0)+1
    return {"allowed_2factor_edge_sets":out,
            "2factor_count_unrestricted":70*comb(a,6),
            "per_edge_2factor_counts":containing}


def annealed_original_BA_floor(s, *, frozen_count=0,
                               point_labels=None, frozen_labels=None):
    """Exact guaranteed conditional expectation of accepted ORIGINAL B/A.

    Let V=(s+1)(s^2+1), d=s+1, M=binom(a,2), m=M-V,
    a=min{a:M>=V}; J has b fixed true ORIGINAL source-line factors,
    each already given a distinct legal physical K_a pair label.
    Uniformly inject the other V-b source line factors into M-b
    available pairs, independently of the arbitrary *fixed* f.

    For EVERY allowed f, J, g_J:
       E_g U_B-left/A-right >=
       V * [3*C(a-2,4)-2*m*C(a-4,2)]_+
         * C((d-b)_+,2) * prod_{j=2}^5 (d-b-j)_+
         * 6! * [70*C(a,6)-28*b*C(a-2,4)]_+ / (M-b)_6.

    If fewer than six unfrozen source-line labels can be used, the RHS
    is ZERO. This bound uses a single valid B original source point p,
    four distinct other source points owning an available physical C4,
    two genuine ORIGINAL incidence flags at p and one at each other
    point, with all six ORIGINAL line factors mutually different and
    OUTSIDE J. By the true (s+1)-regular original point pencils,
    the corresponding greedy choices satisfy the lower factor.

    Each such left B source sixset is generated ONCE. Under globally
    uniform remaining right-label injection its six distinct g-images
    are a uniform ordered six-tuple of physical pair edges from the
    available palette, WITHOUT replacement. The numerator lower bounds
    2-factor configurations after deleting b arbitrary frozen edges.
    Accepted historical GF5 label is B-left/A-right, irrespective of
    whether the right physical 2factor is C6 or 2C3.

    For b_s=o(s), liminf_s inf_{f,J,g_J} E U_BA / s^6 >=140.
    Here h increases along dyadic s=2^h. It says NOTHING about the
    adversarial minimum over *complete* g and cannot prove root A/B/C.
    """
    if type(s) is not int or s < 2 or s & (s-1):
        raise ValueError("dyadic s>=2 required")
    V=(s+1)*(s*s+1)
    d=s+1
    a=minimal_alphabet(V)
    M=comb(a,2)
    missing=M-V
    if type(frozen_count) is not int or not 0 <= frozen_count <= V:
        raise ValueError("frozen true source-line factor count outside 0..V")
    b=frozen_count
    if point_labels is not None:
        validate_typed_pairs(s,point_labels,partial=False)
    if frozen_labels is not None:
        if len(frozen_labels)!=b:
            raise ValueError("frozen physical labels disagree with |J|")
        validate_typed_pairs(s,frozen_labels,partial=True)

    # For each repeated original source factor with physical edge {u,v},
    # 3*C(a-2,4) candidate 4cycles on other coordinate symbols exist.
    # A missing f-edge blocks at most 2*C(a-4,2) of these.
    c4_total=3*comb(a-2,4)
    c4_blocked_cap=2*missing*comb(a-4,2)
    c4_min=max(0,c4_total-c4_blocked_cap)

    # Choose two original flags on the repeated point and four singleton
    # flags on distinct cycle-factor points, all from lines OUTSIDE J;
    # reject previously chosen source-line factors greedily.
    t=max(0,d-b)
    original_source_choices=(
        comb(t,2)*prod(t-j for j in range(2,6)) if t >= 6 else 0
    )
    source_B_sixsets_floor=V*c4_min*original_source_choices

    # In a complete physical K_a exactly 70*C(a,6) 2-factors.
    # A fixed forbidden edge lies in 28*C(a-2,4) such 2-factors.
    # Remove b arbitrary occupied frozen pair edges by the union bound.
    physical_A_total=70*comb(a,6)
    physical_A_blocked_cap=28*b*comb(a-2,4)
    physical_A_remaining_floor=max(
        0,physical_A_total-physical_A_blocked_cap
    )
    denom=falling(M-b,6)
    # 6 ordered distinct source lines map to 6 ordered distinct pair
    # edges; each 2factor edge set has exactly 6! orders.
    physical_A_probability_floor=(
        Fraction(720*physical_A_remaining_floor,denom)
        if denom else Fraction(0)
    )
    if not 0 <= physical_A_probability_floor <= 1:
        raise AssertionError("invalid injection-without-replacement probability")
    expectation_floor=source_B_sixsets_floor*physical_A_probability_floor
    return {
        "s":s,
        "V":V,
        "a":a,
        "physical_pair_palette":M,
        "missing_point_pairs":missing,
        "source_degree":d,
        "frozen_true_source_lines":b,
        "canonical_C4_count_floor_per_source_point":c4_min,
        "source_distinct_line_B_sixsets_floor":source_B_sixsets_floor,
        "right_A_physical_2factors_floor":physical_A_remaining_floor,
        "right_A_injection_probability_floor":physical_A_probability_floor,
        "conditional_expected_original_B_left_A_right_floor":expectation_floor,
        "scaled_floor_over_s6":expectation_floor/Fraction(s**6),
        "for_all_correlated_complete_g":False,
        "uniform_in_fixed_f_and_frozen_gJ":True,
        "all_h_asymptotic_liminf_constant_for_b_little_o_s":140,
        "root_BRANCH_A_or_B_or_C_proved":False,
    }


def exact_W32_original_B_source_distinct_line_count(model,
                                                 frozen_source_line_ids=()):
    """INDEPENDENT existing exhaustive 62,370 original W32 sixset oracle.

    This counts exact left B-source 6sets with six DISTINCT ORIGINAL
    source-line IDs outside J. The conditional B/A expectation of these
    sixsets is EXACTLY count*720*N_2factor(remaining physical pairs)/
    (M-|J|)_6. It is not the all-h guaranteed LOWER bound.
    """
    from hyp105_g5e2b3e1a_fixed_leading import selected_left_six
    from hyp105_g5e2a_pair_embeddings import pair_alphabet_size
    if model.get("h") != 1:
        raise ValueError("finite exhaustive independent oracle supports true W32")
    flags=model["incidences"]
    forbidden=set(frozen_source_line_ids)
    if not all(type(l) is int and 0 <= l < model["v"] for l in forbidden):
        raise ValueError("bad true original source line J")
    count=0
    for ids,kind in selected_left_six(model):
        if kind != "B":
            continue
        lines=tuple(flags[i][1] for i in ids)
        if len(set(lines)) == 6 and not any(l in forbidden for l in lines):
            count+=1
    a=pair_alphabet_size(model["v"])
    return {
        "original_B_source_sixsets_all_distinct_unfrozen_lines":count,
        "a":a,
        "all_sixsets_are_original_incidence_IDs":True,
    }
