"""HYP-105 / issue #230 / D6-AA4-W-CYC

NEW genuine ORIGINAL GQ uniform-in-arbitrary-fixed-f all-h second moment
UPPER bound for the true accepted D6 seven-GF5 class under ONE complete
uniform global original source-LINE injection g.

For s=2^h>=8 and the MINIMAL physical edge-pair alphabet a with
K=binom(a,2)>=V=(s+1)(s*s+1):

    forall complete point f,
       E_g[D6(f,g)^2] <= B_s <= 30_000_000_000*s**12.

Together with the already independent AA4-R-CYC original-source
theorem E_g[D6(f,g)] >= s**6/8, this proves the dimension-free
CONDITIONAL existential success probability

    forall complete point f,
       P_g(D6(f,g)>0) >= (s**6/8)^2 / B_s
                      >= 1 / 1_920_000_000_000.

True source original W(3,s) incidence degree d=s+1, six ACTUAL
different original source incidence IDs, one globally injected point
f and ONE shared random globally injected line g. Not independent
per-original-Q physical label assignments, not physical pseudo-P3,
not an all-f,g deterministic positive or full R3 exponent.

ALL upper bounds are strict finite combinatorial inequalities; the
Python EXACT rational certificates check powers of two but are NOT
substituted for the general all-h proof in the accompanying md.
"""
from fractions import Fraction
from math import comb,perm

from hyp105_issue230_d6aa4r_quenched_original_d6 import (
    _params,quenched_original_D6_theorem)

UNIFORM_E2_S12_CONSTANT=30_000_000_000
PROVED_EXPLICIT_E2_S12_COEFFICIENT=25_793_703_936
UNIFORM_SUCCESS_DENOMINATOR=64*UNIFORM_E2_S12_CONSTANT


def source_line_overlap_pair_capacity(s,r,a):
    """For r FIXED DISTINCT ACTUAL ORIGINAL LINE source factors L0:
       # true original six-incidence Q left-connected C6, containing all
       L0 and having 6 DISTINCT source points AND source lines, is <=
       6!*(s+1)^6*a^max(5-r,0) for r=1..6.

    Proof: choose a true ORIGINAL incident source point for each fixed
    source line (at most d^r). Reject point collisions. The r distinct
    occupied physical f(point) edges of one physical simple C6 span at
    least r+1 physical vertices for r<=5; for r=6 they span all six.
    Complete up to six physical coordinate vertices and arrange them
    into a simple C6 in at most 6!*a^max(5-r,0) choices. For the 6-r
    remaining source points choose one of d actual incident lines.
    These may collide with fixed lines, but ignoring this restriction
    only raises the bound. No synthetic source incidence graph used.
    """
    if type(r) is not int or not 1<=r<=6:
        raise ValueError("original shared source line count r in 1..6 required")
    if type(s) is not int or s<2 or s&(s-1):
        raise ValueError("genuine original W(3,2^h) only")
    _,minimal_a,_,_=_params(s)
    if a!=minimal_a:
        raise ValueError("genuine minimal physical alphabet only")
    return 720*(s+1)**6*a**max(5-r,0)


def same_global_g_second_D6_conditional_bound(s,r,a,K):
    """Upper bound on P_g(second Q D6 | first Q D6, fixed complete f),
    for ANY two eligible genuine source Q with EXACTLY r common SOURCE
    LINE factor IDs and arbitrary SOURCE POINT overlaps.

    Given first D6, the r shared source-line physical PAIR labels are
    fixed; the second connected six-column line cycle sees r fixed
    vertex-pairs. Each fixed pair admits <=2 orientations of its two
    incident coordinate colors. If 1<=r<=5, those r vertices cover >=
    r+1 of the six distinct coordinate symbols, leaving <=5-r free
    coordinate choices; when r=6 all six are fixed. Thus at most
    2^r*a^max(5-r,0) possible right color assignments, each yielding
    distinct physical edge labels if eligible. Remaining 6-r original
    lines sample WITHOUT REPLACEMENT from K-6 labels with denominator
    (K-6)_(6-r). Cap bound at 1.

    r=0 is the (a)_6/(K-6)_6 without-replacement bound, keeping the
    complete original global g, never a product of independent halves.
    """
    _,am,Km,_=_params(s)
    if a!=am or K!=Km:
        raise ValueError("same true W(3,s) MINIMAL K_a alphabet required")
    if type(r) is not int or not 0<=r<=6:
        raise ValueError("shared original source line count r must be in 0..6")
    if r==0:
        return min(Fraction(1),Fraction(perm(a,6),perm(K-6,6)))
    return min(Fraction(1),Fraction(2**r*a**max(5-r,0),
                                    perm(K-6,6-r)))


def exact_uniform_original_D6_E2_upper(s):
    """Every fixed complete ORIGINAL point map f, no enumeration of f.

    N=max number of eligible true original left C6 candidate Q:
        N <= ((a)_6/12)*d^6.
    p=P(one actual eligible original six-ID Q D6)= (a)_6/(K)_6.

    Partition ordered true candidate Q×Q by r actual common source
    LINE factors. For r=0, pairs <=N^2 and joint event <=p*q0.

    For r>=1: fix Q0, select r of its six original line IDs (<=C6r).
    Each specified r-source-line set belongs to <=Delta_r distinct
    actual second Q by true ORIGINAL incidence/physical C6 packing.
    Therefore #ordered pairs with exact r shared line IDs <=
         N*C(6,r)*Delta_r.
    Joint probability <=p*q_r. Summing over r0..r6 gives B_s.

    Important: the upper may count artificial physically possible
    choices that do NOT belong to the true GQ. That only increases an
    honest upper; all actual Q are counted, with one shared global g.
    """
    if type(s) is not int or s<8 or s&(s-1):
        raise ValueError("all-h theorem only for genuine s=2^h >=8")
    V,a,K,m=_params(s)
    d=s+1
    C6_all=perm(a,6)//12
    N_upper=C6_all*d**6
    p=Fraction(perm(a,6),perm(K,6))
    sectors={}
    q0=same_global_g_second_D6_conditional_bound(s,0,a,K)
    B=Fraction(N_upper**2)*p*q0
    sectors["r0_no_shared_source_lines"]=str(B)
    for r in range(1,7):
        cap=source_line_overlap_pair_capacity(s,r,a)
        q=same_global_g_second_D6_conditional_bound(s,r,a,K)
        term=N_upper*comb(6,r)*cap*p*q
        sectors[f"r{r}_actual_original_line_overlap_upper"]=str(term)
        B+=term
    if B<=0 or B>UNIFORM_E2_S12_CONSTANT*s**12:
        raise AssertionError("claimed uniform all-h E2 constant violated by exact rational evaluator")

    earlier=quenched_original_D6_theorem(s)
    mu_lower=Fraction(earlier[
        "conditional_E_g_true_original_seven_GF5_D6_lower_for_EVERY_f"])
    if mu_lower<Fraction(s**6,8):
        raise AssertionError("previous AA4-R-CYC true original fixed-f D6 E lower violated")
    PZ_exact_combinatorial_lower=mu_lower**2/B
    PZ_uniform_lower=Fraction(1,UNIFORM_SUCCESS_DENOMINATOR)
    if not 0<PZ_uniform_lower<=PZ_exact_combinatorial_lower<=1:
        raise AssertionError("invalid genuine original Cauchy conditional success lower")
    return {
        "slice":"HYP105-ISSUE230-D6-AA4-W-CYC-UNIFORM-GQ-SECOND-MOMENT",
        "s":s,"V":V,"a":a,"K":K,"source_degree_d":d,
        "physical_C6_upper_count_all_Ka":C6_all,
        "original_left_connected_six_original_ID_Q_upper":N_upper,
        "fixed_true_original_source_Q_one_D6_probability":str(p),
        "full_g_shared_source_LINE_overlap_E2_sector_upper_bounds":sectors,
        "exact_genuine_original_E_g_D6_squared_upper_Bs":str(B),
        "exact_Bs_over_s12":str(B/s**12),
        "PROVED_ALL_h_uniform_E2_s12_clean_coefficient":UNIFORM_E2_S12_CONSTANT,
        "PROVED_all_h_explicit_coarse_E2_s12_coefficient":
            PROVED_EXPLICIT_E2_S12_COEFFICIENT,
        "previous_all_h_fixed_point_map_E_g_D6_lower":str(mu_lower),
        "true_original_PZ_improved_specific_s_lower":str(PZ_exact_combinatorial_lower),
        "new_ALL_h_every_fixed_f_one_uniform_GLOBAL_g_D6_positive_probability_lower":
            str(PZ_uniform_lower),
        "min_original_physical_alphabet_required":True,
        "original_six_distinct_true_point_line_incidence_IDs":True,
        "one_complete_injective_point_map_f_arbitrary_and_fixed":True,
        "one_complete_uniform_injective_global_LINE_map_g_shared_by_ALL_Q":True,
        "all_h_E2_bound_uniform_in_f_PROVED":True,
        "all_h_true_original_stochastic_positive_D6_lower_uniform_in_f_PROVED":True,
        "all_h_for_every_f_g_seven_GF5_S_omega_s6_PROVED":False,
        "all_h_full_GF5_R3_PROVED":False,
        "root_A":"OPEN","root_B":"OPEN",
    }


def elementary_ALL_h_constant_certificate():
    """SYMBOLIC coefficient proof, not an empirical finite-s fit.

    For s>=8, a minimal implies a<=2*s^(3/2) and K-11>=s^3/2;
    d<=9s/8. Thus:
       N < 11s^15,
       p < 4096s^-9, q0 <4096s^-9,
       Delta_r < 1460*2^(5-r)*s^(13.5-1.5r) for 1<=r<=5,
       q_r <=2^(11-r)*s^(-10.5+1.5r) for 1<=r<=5,
       Delta_6 < 1460s^6, q6<=1.
    Thus B_s/s^12 is bounded by the exact integer sum below.
    """
    r0=11**2*4096**2
    r1to5={}
    for r in range(1,6):
        # Product bound is C_r*s^9, and s>=8 gives s^9<=s^12/512.
        coefficient=11*1460*4096*comb(6,r)*2**(16-2*r)
        if coefficient%512:
            raise AssertionError("elementary ALL-h proof coefficient not integer divisible")
        r1to5[r]=coefficient//512
    r6=11*1460*4096
    exact_sum=r0+sum(r1to5.values())+r6
    if exact_sum!=PROVED_EXPLICIT_E2_S12_COEFFICIENT or \
       exact_sum>=UNIFORM_E2_S12_CONSTANT:
        raise AssertionError("ALL-h coarse E2 constant proof arithmetic invalid")
    if not Fraction(64,12)*Fraction(9,8)**6<11:
        raise AssertionError("analytic N upper coefficient false")
    if not 720*Fraction(9,8)**6<1460:
        raise AssertionError("analytic source-LINE cap coefficient false")
    return {
        "exact_constant_from_all_seven_TRUE_original_source_LINE_overlap_sectors":
            exact_sum,
        "r0_disjoint_original_LINES_s12_coefficient":r0,
        "r1_to_r5_original_LINE_overlap_s12_coefficients":r1to5,
        "r6_same_original_LINE_factor_set_s12_coefficient":r6,
        "source_s_ge_8_exact_integer_coefficient_proof":"PASS",
        "physical_alphabet_a_le_2s3over2_minimal_analytic_argument":"PROVED_IN_MD",
        "K_minus_11_ge_s3_over_2_analytic_argument":"PROVED_IN_MD",
        "uniform_original_E2_upper_30b_s12_proof":True,
        "uniform_original_P_D6_positive_at_least_1_over_1920000000000":True,
        "all_f_g_D6_positive_NOT_proved":True,
    }


def report():
    return {
        "slice":"HYP105-ISSUE230-D6-AA4-W-CYC-UNIFORM-GQ-SECOND-MOMENT",
        "elementary_ALL_h_certificate":elementary_ALL_h_constant_certificate(),
        "finite_exact_rational_original_GQ_order_regressions":
            [exact_uniform_original_D6_E2_upper(2**h) for h in range(3,15)],
        "all_h_original_fixed_f_uniform_injected_g_D6_E2_at_most_30b_s12":True,
        "all_h_fixed_f_P_g_D6_positive_lower":"1/1920000000000",
        "root_A":"OPEN","root_B":"OPEN",
        "all_h_every_f_g_S_omega_s6_PROVED":False,
    }


if __name__=="__main__":
    import json
    print(json.dumps(report(),indent=2,sort_keys=True))
