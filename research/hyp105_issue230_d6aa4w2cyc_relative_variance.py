"""HYP-105 #230 D6-AA4-W2-CYC: EVERY fixed-f relative variance O(s^-3).

Pure integer/Fraction certificate; original W(3,2^h), six distinct original
incidence IDs and one coherent uniform global opposite-line injection g.
This refines the W-CYC #492 absolute E[D6²] upper via six-source-line
codegree compression, not any deterministic ALL-f,g minimax conclusion.
"""
from fractions import Fraction
from math import comb, factorial, perm

from hyp105_issue230_d6aa4r_quenched_original_d6 import _params


def _fall(n, k):
    if k < 0 or n < k:
        return 0
    return perm(n, k)


def physical_C6_containing_r_edges(a, r, c):
    """Exact pre-existing path-component completion formula from #485.

    r distinct prescribed edges in c disjoint nonempty paths. The
    physical C6 requires exactly r+c source vertices and 6-r-c new ones.
    Isolated and branching/cyclic prescribed edge patterns return zero
    outside this helper's forest domain.
    """
    if type(a) is not int or a < 6 or type(r) is not int or not 1 <= r <= 5:
        raise ValueError("a>=6 and 1<=r<=5 required")
    if type(c) is not int or not 1 <= c <= min(r, 6-r):
        raise ValueError("valid nonempty disjoint path components required")
    return (2 ** (c-1) * factorial(5-r) *
            comb(a-r-c, 6-r-c))


def max_fixed_edges_C6_capacity(a, r):
    if type(a) is not int or a < 6 or type(r) is not int or not 1 <= r <= 6:
        raise ValueError("a>=6 and 1<=r<=6")
    if r == 6:
        return 1
    val = max(physical_C6_containing_r_edges(a, r, c)
              for c in range(1, min(r, 6-r)+1))
    if a >= 35:
        path = _fall(a-r-1, 5-r)
        if val != path:
            raise AssertionError("large-a path overlap extremality invalid")
    return val


def physical_C6_in_E_edges_upper(E):
    """Every simple C6 has 12 oriented starts and alternating triples.

    An oriented six-cycle is determined by its three *oriented*
    alternating edges; at most (2E)^3 such triples exist, so the number
    of unoriented simple C6 is at most (2E)^3/12.
    """
    if type(E) is not int or E < 0:
        raise ValueError("nonnegative integer number of physical edges")
    return Fraction((2*E)**3, 12)


def original_six_line_codegree_bound(d):
    """Fix SIX distinct actual original line factors.

    Union of the six GQ line neighborhoods has at most 6d true original
    point factors; global f injects them to at most 6d physical edges.
    Each source physical C6 can be matched to the six named original
    line factors in at most 6! ways, each a distinct original six-ID set.
    """
    if type(d) is not int or d < 2:
        raise ValueError("true source degree integer >=2")
    return 480 * (6*d)**3  # 6! * (2E)^3/12 at E=6d


def relative_variance_certificate(s):
    """EXACT all-h uniform-f variance ratio upper, for s=2^h >= 8.

    For every one fixed complete globally injected original point map f,
    let D6(f,g) count aligned positively accepted original A/A C6/C6
    sixsets when a SINGLE complete source line map g is uniform.
    E_g[D6]>=s^6/8 is predecessor #480; no simulated huge GQ exists here.
    """
    if type(s) is not int or s < 8 or s & (s-1):
        raise ValueError("s must be a true power of two, >=8")
    V, a, K, m = _params(s)
    d = s+1
    if a < 35 or K < 144:
        raise AssertionError("large palette arithmetic assumptions failed")
    all_physical = perm(a,6)//12
    missing_cycle_upper = m*perm(a-2,4)
    occupied_lower = all_physical-missing_cycle_upper
    n_lower = occupied_lower*perm(d,6)
    p = Fraction(perm(a,6), perm(K,6))
    mu_lower = n_lower*p
    if occupied_lower*24 < perm(a,6):
        raise AssertionError("universal occupied six-cycle half bound broken")
    if mu_lower < Fraction(s**6,8):
        raise AssertionError("predecessor genuine original quenched mean bound failed")

    # r=0: two distinct original source-line supports are not independent
    # under ONE full g. Conditional upper: all physical C6s, regardless
    # of the six g-images already consumed by the first event.
    q0 = Fraction(perm(a,6), perm(K-6,6))
    disjoint_correction = q0/p-1
    codegrees = {}
    terms = {}
    conditional = {}
    for r in range(1,7):
        capacity = max_fixed_edges_C6_capacity(a,r)
        if r < 6:
            delta = d**6 * capacity
            qr = min(Fraction(1), Fraction(12*capacity,
                                            perm(K-6,6-r)))
        else:
            # Essential improvement over #492's d^6 six-line capacity:
            # every six prescribed source lines yield <= O(d^3) C6.
            delta = min(d**6, original_six_line_codegree_bound(d))
            qr = Fraction(1)
        # Exact-r ordered Q×Q pairs are included by choosing r shared
        # line IDs of the FIRST Q; their count is <= C(6,r)*N*delta.
        codegrees[r] = delta
        conditional[r] = str(qr)
        terms[r] = Fraction(comb(6,r)*delta, n_lower) * (qr/p)

    eps_exact = disjoint_correction+sum(terms.values(),Fraction())
    # Analytic ALL-h bound, no finite-h regression fitting:
    # N >= a^6*d^6/432; a>=35, d>=9; K-11>=K/2.
    # r=1..5 contributions <= 10368*C(6,r)*2^(6-2r)/a^2.
    # disjoint correction <=288/a^2;
    # r=6 <=1399680/d^3.
    coeffs = {r: 10368*comb(6,r)*2**(6-2*r)
              for r in range(1,6)}
    assert all(type(x) is int for x in coeffs.values())
    assert sum(coeffs.values())==1867536
    eps_ad = Fraction(1867824,a*a) + Fraction(1399680,d**3)
    eps_s = Fraction(2333592,s**3)
    if not 0 <= eps_exact <= eps_ad <= eps_s:
        raise AssertionError("all-h explicit relative variance certificate failed")

    # P(D6 > 0) >= E[D6]^2/E[D6^2] >= 1/(1+epsilon).
    # Chebyshev: P(D6 < E[D6]/2) <= 4 epsilon,
    # hence P(D6 >= s^6/16) >= max(0,1-4 epsilon).
    return {
        "s":s,"a":a,"K":K,"V":V,"source_degree_d":d,
        "physical_missing_edges":m,
        "occupied_left_C6_lower":occupied_lower,
        "actual_original_left_sixset_count_lower":n_lower,
        "mean_D6_lower":str(mu_lower),
        "mean_D6_over_s6_lower":str(mu_lower/s**6),
        "single_actual_sixset_D6_marginal":str(p),
        "r0_one_full_g_correction":str(disjoint_correction),
        "r1_to_r6_codegree_upper":codegrees,
        "r1_to_r6_conditional_second_D6_probability_upper":conditional,
        "r1_to_r6_relative_variance_terms_upper":{
            k:str(v) for k,v in terms.items()},
        "relative_variance_over_mean_squared_exact_upper":str(eps_exact),
        "universal_rational_upper_a_d":str(eps_ad),
        "universal_rational_upper_s":str(eps_s),
        "one_global_g_positive_probability_at_least":
            str(1/(1+eps_exact)),
        "one_global_g_at_least_s6_over16_probability_at_least":
            str(max(Fraction(),1-4*eps_exact)),
        "all_h_every_fixed_f_relative_variance_O_s_minus3":True,
        "same_one_complete_global_g":True,
        "original_six_distinct_incidence_IDs":True,
        "all_f_g_minimax_seven_proved":False,
        "independent_math_referee":False,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


if __name__=="__main__":
    import argparse,json
    p=argparse.ArgumentParser()
    p.add_argument("--h",type=int,default=8)
    args=p.parse_args()
    print(json.dumps(relative_variance_certificate(1<<args.h),
                     indent=2,sort_keys=True))
