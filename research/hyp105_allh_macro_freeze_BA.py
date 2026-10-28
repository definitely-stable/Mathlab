"""HYP-105 #230 AA4-MFREEZE: ALL-h ANNEALED B/A bound with b=o(V).

Strengthen AA4-ANNBA from b=o(s) to b=o(V), V~s^3, and even
b=floor(rho*V), constant rho<1/6. The improvement is an ORIGINAL GQ
source-pencil average: sum_p |J intersect pencil(p)| = |J|*(s+1),
regardless of adversarial original source-line set J. Keep point
factors with at most k fixed source lines; their pair-edge labels
occupy an almost-full physical K_a, so all five source pencils of
a surviving physical B structure have at least s+1-k free source
line factors. The remaining right labels are ONE uniform injection.

The exact lower bound is for E_g U_(B-left/A-right) CONDITIONED on
any complete f and legal frozen g_J, not for every completed g.
No root A/B/C proof, no total R3 claim or ASET exponent.
"""
from fractions import Fraction
from math import comb, isqrt, prod

from hyp105_allh_annealed_BA_floor import (
    falling, validate_typed_pairs,
)
from hyp105_physical_degree_energy import minimal_alphabet


def robust_annealed_BA_floor(s, frozen_count, pencil_threshold, *,
                            point_labels=None, frozen_labels=None):
    """Exact all-h uniform-in-(f,J,g_J) conditional expectation floor.

    Original true-source identity: for J of b *ORIGINAL* line-factor IDs,
    sum_(original points p) |J intersection L(p)| = b*d where d=s+1.
    Let k be a nonnegative integer. At most floor(b*d/(k+1)) ORIGINAL
    point factors have >k frozen incident original source line IDs,
    since each such point contributes >=k+1 to the identity.
    Therefore G=max(0,V-floor(b*d/(k+1))) original point factors
    each have >=q=d-k free original incident source flags.

    Every complete f is globally injective into M=binom(a,2) K_a pairs.
    Therefore GOOD original points' f images omit at most M-G
    physical edges, so every GOOD repeated point p lies in at least
    Q=[3*C(a-2,4)-2*(M-G)*C(a-4,2)]_+
    unique coordinate-disjoint GOOD physical C4s. The four C4 edges
    belong to four other distinct GOOD original source points.

    Select two distinct original non-J line factors at repeated p and
    one non-J original source line at each C4 point, avoiding ALL
    previously used original source line IDs. At least
    C(q,2)*(q-2)*(q-3)*(q-4)*(q-5) six-ID selections per shape.
    This is one canonical ORIGINAL B-side sixset with six DISTINCT
    original source line factors, hence under one uniform remaining
    g injection its right A physical six-edge 2factor probability
    is at least 720*[70*C(a,6)-28*b*C(a-2,4)]_+/(M-b)_6.

    All source/physical configuration counting is injective, no
    omitted within-pencil collisions or independence assumption.
    """
    if type(s) is not int or s < 2 or s & (s - 1):
        raise ValueError("s must equal 2^h for integer h>=1")
    d = s+1
    V = d*(s*s+1)
    if type(frozen_count) is not int or not 0 <= frozen_count <= V:
        raise ValueError("b must be number of true original frozen line factors")
    b=frozen_count
    if type(pencil_threshold) is not int or not 0 <= pencil_threshold <= d:
        raise ValueError("source pencil freeze threshold k must be 0..d")
    k=pencil_threshold
    if point_labels is not None:
        validate_typed_pairs(s, point_labels, partial=False)
    if frozen_labels is not None:
        if len(frozen_labels) != b:
            raise ValueError("frozen physical line images inconsistent with b")
        validate_typed_pairs(s, frozen_labels, partial=True)
    a = minimal_alphabet(V)
    M = comb(a,2)
    max_bad = min(V,(b*d)//(k+1))
    G = V-max_bad
    missing_good = M-G
    free_source_degree = d-k
    c4_total = 3*comb(a-2,4)
    c4_blocked_bound = 2*missing_good*comb(a-4,2)
    good_c4_floor = max(0,c4_total-c4_blocked_bound)
    six_original_choices_floor = (
        comb(free_source_degree,2) *
        prod(free_source_degree-j for j in range(2,6))
        if free_source_degree >= 6 else 0
    )
    source_sixsets_floor = G*good_c4_floor*six_original_choices_floor
    right_2factor_floor = max(0,
        70*comb(a,6)-28*b*comb(a-2,4))
    denominator = falling(M-b,6)
    right_probability = (
        Fraction(720*right_2factor_floor,denominator)
        if denominator else Fraction(0)
    )
    if not Fraction(0)<=right_probability<=Fraction(1):
        raise AssertionError("invalid six-source-line injection probability")
    certified_expectation_floor = source_sixsets_floor*right_probability
    return {
        "s":s,"V":V,"a":a,"M":M,
        "frozen_original_source_lines":b,
        "pencil_freeze_threshold_k":k,
        "source_degree":d,
        "upper_bound_bad_original_source_points":max_bad,
        "guaranteed_good_original_source_points":G,
        "good_source_minimum_unfrozen_pencil":free_source_degree,
        "missing_good_f_pair_edges_upper_bound":missing_good,
        "good_point_physical_C4_floor":good_c4_floor,
        "canonical_good_original_B_sixsets_floor":source_sixsets_floor,
        "available_right_A_physical_2factors_floor":right_2factor_floor,
        "right_A_probability_lower_bound":right_probability,
        "conditional_expected_original_BA_lower_bound":
            certified_expectation_floor,
        "floor_of_expected_original_BA":(
            certified_expectation_floor.numerator //
            certified_expectation_floor.denominator
        ),
        "scaled_expected_BA_floor_over_s6":
            certified_expectation_floor/Fraction(s**6),
        "all_h_annealed_not_all_completed_g":True,
        "root_A_B_C_proved":False,
    }


def best_robust_annealed_BA_floor(s, frozen_count):
    """Best available integer threshold, finite exact optimization over k.

    Optimization is only of a rigorously valid lower bound on expectation,
    not an optimizer over actual correlated complete line mappings.
    """
    if type(s) is not int or s < 2 or s & (s-1):
        raise ValueError("dyadic s>=2 required")
    V=(s+1)*(s*s+1)
    if type(frozen_count) is not int or not 0<=frozen_count<=V:
        raise ValueError("b must be an integer between zero and V")
    d=s+1
    candidates=(
        robust_annealed_BA_floor(s,frozen_count,k)
        for k in range(max(1,d-5))
    )
    return max(candidates,
               key=lambda r:r["conditional_expected_original_BA_lower_bound"])


def macroscopic_freeze_rational_example(s, rho_numerator=1,
                                        rho_denominator=16):
    """Prove finite conservative bound with frozen b=floor(rho V).

    For rho<1/6 and k/d->alpha with 4rho<alpha<1,
    normalized all-h lower limit is at least
       140*(1-rho/alpha)*(1-4rho/alpha)*(1-alpha)^6*(1-6rho).
    The closed-form test case rho=1/16, alpha=1/2 gives 1225/2048.
    """
    if (type(rho_numerator) is not int or
            type(rho_denominator) is not int or
            not 0<=rho_numerator<rho_denominator):
        raise ValueError("rho must be a rational fraction in [0,1)")
    V=(s+1)*(s*s+1)
    b=(V*rho_numerator)//rho_denominator
    d=s+1
    k=d//2
    return robust_annealed_BA_floor(s,b,k)


def synthetic_regular_source_good_point_oracle(s, frozen_original_lines, k):
    """Finite independent pencil double-count check on an ABSTRACT host.

    This is a combinatorial test helper, NOT a model substitution:
    actual true W(3,s) has exactly the same d-regular first-moment
    identity. Synthetic circulant incidence is used only to falsify
    the algebra of the Markov count, never as W(3,s) evidence.
    """
    if type(s) is not int or s<2 or s&(s-1):
        raise ValueError("dyadic s required")
    d=s+1;V=d*(s*s+1)
    J=set(frozen_original_lines)
    if len(J)!=len(tuple(frozen_original_lines)) or (
            any(type(ell) is not int or not 0<=ell<V for ell in J)):
        raise ValueError("source line selection invalid")
    if type(k) is not int or not 0<=k<=d:
        raise ValueError("invalid original pencil threshold")
    # Abstract finite regular bipartite source: cyclic shifts.
    counts=[
        sum((p+j)%V in J for j in range(d))
        for p in range(V)
    ]
    bad=sum(t>k for t in counts)
    assert sum(counts)==len(J)*d
    assert bad<=len(J)*d//(k+1)
    return {
        "abstract_regular_host_not_W3":True,
        "V":V,"d":d,"frozen_b":len(J),
        "exact_sum_original_pencil_incidence":sum(counts),
        "exact_bad_pencils":bad,
        "max_bad_by_Markov":len(J)*d//(k+1),
        "actual_good_pencils":V-bad,
    }
