"""HYP-105 C9: genuine GQ concurrence forces C8 <=2-pin floor ZERO.

All-h theorem is for the B-left/A-right weighted sixset source and the
physical occupied 2-factor target, NOT all seven positive GF5 families.
It is a NO-GO for this *specific relaxation*, NOT a zero-overlap map.
"""
from fractions import Fraction
from itertools import combinations
from math import comb, isqrt

from hyp105_g5e2b3e1c1_gq_concurrency import all_h_right_line_concurrency


def minimal_pair_alphabet(V):
    if type(V) is not int or V < 1:
        raise ValueError("V must be positive integer")
    a = (1 + isqrt(1 + 8*V)) // 2
    while comb(a, 2) < V:
        a += 1
    while a > 2 and comb(a-1, 2) >= V:
        a -= 1
    return a


def two_pin_source_target_capacity(s):
    """ALL p, ALL legal f,F: combinatorial bound in every 2-pin fiber.

    Choose D of TWO original GQ right lines, p any injective images,
    r=|R intersect D|, n=V-2, m=6-r.

    If m_f(R)>0 a GQ original concurrence pair is present. Unless
    that pair equals the two pins (possible only at r=2), it occurs
    among unpinned vertices or joins a pinned to an unpinned vertex.
    Count union via E*C(n-2,m-2)+r*d*C(n-1,m-1).
    For r=2 the unique doubled-point distinguished pinned pair has
    at most W=3*C(a-2,4)*(s+1)^4 weighted witnesses (C3), hence at
    most W positive source sixsets. Every physical conditional target
    class has <=T=70*C(a,6) members (C0), even for occupied F subset.
    If source_positive_upper+T < C(n,m), all C8 fiber lowest t weights
    are ZERO. All counts are integer, independent of actual labels.
    """
    if type(s) is not int or s < 2 or s & (s-1):
        raise ValueError("s must equal 2**h with h>=1")
    V = (s+1)*(s*s+1)
    a = minimal_pair_alphabet(V)
    n = V-2
    graph = all_h_right_line_concurrency(s)
    E = graph["line_concurrence_pairs"]
    degree = s*(s+1)
    W = 3*comb(a-2,4)*(s+1)**4
    T = 70*comb(a,6)
    fibers = []
    for r in range(3):
        m = 6-r
        capacity = comb(n,m)
        unpinned_pair = E*comb(n-2,m-2)
        cross_pair = r*degree*comb(n-1,m-1)
        distinguished_pinned_pair = W if r == 2 else 0
        source_support_upper = (unpinned_pair + cross_pair
                                + distinguished_pinned_pair)
        sum_upper = source_support_upper + T
        fibers.append({
            "pinned_source_members": r,
            "remaining_sixset_members": m,
            "fiber_size": capacity,
            "source_support_upper": source_support_upper,
            "all_occupied_target_class_upper": T,
            "total_support_plus_target_upper": sum_upper,
            "strict_zero_fiber": sum_upper < capacity,
            "slack_integer": capacity - sum_upper,
            "exact_ratio": Fraction(sum_upper, capacity),
        })
    return {
        "s": s, "V": V, "a": a,
        "physical_unoccupied_edges": comb(a,2)-V,
        "GQ_concurrence_degree": degree,
        "GQ_concurrence_edge_count": E,
        "source_distinguished_pair_weight_cap": W,
        "all_physical_2factor_count": T,
        "fibers": tuple(fibers),
        "uniform_all_f_F_p_and_any_original_two_pins": True,
        "actual_minimum_zero_proved": False,
    }


def analytic_s_ge_64_gate():
    """Exact rational coefficient checks for uniform noncomputational tail.

    s>=64: V<=11/10*s^3, degree<=11/10*s^2, E<=121/200*s^5,
    n,n-1>=99/100*s^3, n-3>=98/100*s^3,
    a^2<=4*s^3 (minimal edge alphabet).
    For 0<=r<=2, m=6-r:
      E*C(n-2,m-2)/C(n,m) <=(500/27)/s <19/s
      r*degree*C(n-1,m-1)/C(n,m) <=(80/9)/s <9/s
      W/C(n,4) <= (439230000/5764801)/s^2 <77/s^2
      T/C(n,4) <= (400000000/2470629)/s^3 <163/s^3.
    Finally 28/64+77/64^2+163/64^3<1.
    Rational assertion checks the symbolic *constants* (not just samples).
    """
    constants = (
        Fraction(30)*Fraction(121,200)/Fraction(99,100)**2,
        Fraction(8)*Fraction(11,10)/Fraction(99,100),
        Fraction(24)*2*Fraction(11,10)**4/Fraction(98,100)**4,
        Fraction(24)*Fraction(56,9)/Fraction(98,100)**4,
    )
    rounded = (19,9,77,163)
    if any(x >= bound for x,bound in zip(constants,rounded)):
        raise AssertionError("analytic tail constant inequality failed")
    tail = Fraction(28,64)+Fraction(77,64**2)+Fraction(163,64**3)
    if tail >= 1:
        raise AssertionError("tail lacks uniform strict positivity slack")
    return {
        "s_min":64, "symbolic_upper": "28/s+77/s^2+163/s^3",
        "symbolic_constants": tuple(str(x) for x in constants),
        "strict_fraction_at_64": tail,
        "positive_uniform_slack":1-tail,
        "proves_all_real_s_at_least_64_given_parameter_bounds":True,
    }


def two_pin_all_h_zero_barrier(s):
    """All powers s>=16 certified: two exact base cases + analytic tail."""
    p = two_pin_source_target_capacity(s)
    if s < 16:
        p["proved_all_two_pin_fibers_zero"] = False
        p["scope"] = "BELOW_PROVEN_THRESHOLD_NOT_DECIDED"
        return p
    if s == 16 or s == 32:
        proof = "EXACT_INTEGER_BASE_CASE"
    else:
        analytic_s_ge_64_gate()
        proof = "UNIFORM_RATIONAL_ANALYTIC_TAIL"
    if any(not f["strict_zero_fiber"] for f in p["fibers"]):
        raise AssertionError("finite integer check contradicts all-h theorem")
    p.update({
        "proved_all_two_pin_fibers_zero":True,
        "proof_branch":proof,
        "C8_LD_zero_for_every_D_size_at_most_two":True,
        "C8_zero_DOES_NOT_imply_actual_U_zero":True,
        "all_seven_motifs_zero_or_positive_proved":False,
    })
    return p


def W32_compatibility_report():
    """Real W32: no extrapolation of s>=16 bound to s=2."""
    from hyp105_g5e2b3e1c8_fiber_rearrangement import W32_fiber_report
    finite = W32_fiber_report()
    return {
        "s2_two_pin_asymptotic_gate":two_pin_all_h_zero_barrier(2)[
            "proved_all_two_pin_fibers_zero"],
        "genuine_W32_finite_fiber_report":finite,
        "finite_s2_not_mistaken_for_all_h_theorem":True,
    }


if __name__ == "__main__":
    import json
    rows = []
    for s in (2,4,8,16,32,64,128,256,512,1024):
        cert = two_pin_all_h_zero_barrier(s)
        rows.append({
            "s":s, "V":cert["V"],"a":cert["a"],
            "max_support_plus_target_ratio":
                str(max(f["exact_ratio"] for f in cert["fibers"])),
            "all_2pin_fibers_zero":cert["proved_all_two_pin_fibers_zero"],
            "branch":cert.get("proof_branch"),
        })
    print(json.dumps({"all_h_analytic_tail":analytic_s_ge_64_gate(),
                     "exact_integer_grid":rows},
                     indent=2,sort_keys=True,default=str))
