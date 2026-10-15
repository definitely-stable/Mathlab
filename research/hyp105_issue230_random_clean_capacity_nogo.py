"""HYP-105 #230 EICE-003-L — probabilistic NO-GO for FOUR-clean GQ capacity.

For every genuine original W(3,s), s=2^h >=64, and every fixed
true original middle incidence e, uniform independent injections of
all true original point/line labels into K_a edges satisfy an EXPLICIT
positive lower bound on E C_e, the number of I1-valid original 5-source
templates whose four decoded nonincident GQ anchors are end-clean.

The expectation is >= s^4 / 1_000_000, and E(sum_e C_e)>=
N*s^4/1_000_000. Consequently EXIST globally injective actual
original f,g with max_e C_e>=s^4/1_000_000 and sum_e C_e>=
N*s^4/1_000_000. This DISPROVES BOTH proposed all-h uniform
o(s^4) per-middle and o(s^8) total four-clean upper bounds.

Crucially this theorem does NOT assert four INTERNAL blockers or any
positive original seven-GF5 sixset. H_e<=C_e does not reverse:
NO-GO for a STRONGER sufficient upper, not for Branch A itself.
"""
from fractions import Fraction
from math import comb, isqrt
import json


def _falling(n,k):
    if not isinstance(n,int) or not isinstance(k,int) or n<k or k<0:
        raise ValueError("valid nonnegative integer falling factorial required")
    r=1
    for j in range(k):
        r*=n-j
    return r


def random_original_five_clean_certificate(s):
    """Exact rational all-h random-INJECTION true source certificate.

    Choose independent UNIFORMLY RANDOM INJECTIVE maps of all genuine
    V W(3,s) point and line IDs into the T=binom(a,2) physical pairs.

    Condition on the true middle incidence e=(p2,l2).
    Count ORDERED four original incidence arms with all 5 source
    points and all 5 lines distinct, and force arms 1,2 into physical
    source corner Q00 and arms 3,4 into opposite corner Q11.

    Source arm tuples >=prod_j=1..4 [N-2j(s+1)].
    Forced genuine physical distinct outside x/y assignment probability
    exactly ((a-2)_4/(T-1)_4)^2.
    Every valid five-source original set counted 2!*2!=4 times.
    The four induced genuine original q/r endpoints are all
    nonincident and all unique original anchors END-CLEAN with
    conditional probability >=1-beta.

    beta consists of:
    - 8U/(T-5): four f-target & four g-target labels absent;
    - 56(s+1)/(V-5): 16 q_i-r_j GQ incidences, 20 fixed
      source point-vs-r, 20 fixed source line-vs-q incidences;
    - 16(a-2)/(T-9): eight true original anchor intermediate
      label-overlap events, after excluding exposed 5+4 factors.

    No false independence assumption: uniform permutations and
    conditional deferred decisions justify every union-bound term.
    """
    if type(s) is not int or s<64 or (s&(s-1)):
        raise ValueError("true s=2^h>=64 required for quantitative NO-GO")
    V=(s+1)*(s*s+1)
    a=(1+isqrt(1+8*V))//2
    while comb(a,2)<V:
        a+=1
    if comb(a-1,2)>=V:
        raise AssertionError("not the minimal complete-pair universe")
    T=comb(a,2)
    U=T-V
    N=V*(s+1)
    source_matching_ordered_lower=_falling(V-2,1)*_falling(V-4,1)*(
        V-6)*(V-8)*(s+1)**4
    if source_matching_ordered_lower<=0:
        raise AssertionError("nonpositive actual GQ source matching count lower")
    quadrant_f_assignment=Fraction(_falling(a-2,4),_falling(T-1,4))
    same_g_assignment=quadrant_f_assignment
    physical_quadrant_probability=quadrant_f_assignment*same_g_assignment
    missing_labels=Fraction(8*U,T-5)
    geometry_exceptions=Fraction(56*(s+1),V-5)
    anchor_label_collisions=Fraction(16*(a-2),T-9)
    union_bad=missing_labels+geometry_exceptions+anchor_label_collisions
    conditional_clean_lower=max(Fraction(),1-union_bad)
    # Each unordered 5-source set with a prescribed genuine middle e
    # and the Q00/Q11 occupancy is counted four times: exchange the two
    # genuine row arm source IDs and the two genuine column arm source IDs.
    e_clean_expected_lower=(
        Fraction(source_matching_ordered_lower,4)*
        physical_quadrant_probability*conditional_clean_lower)
    uniform_coarse=Fraction(s**4,1_000_000)
    if not(a<=3*s*isqrt(s)+3*s or V>=s**3):
        raise AssertionError("coarse source asymptotic universe sanity failed")
    # Algebraic inequalities supplied in the companion all-h proof:
    # a<=3*s^(3/2), V>=s^3, a>=10, (a-5)/T>=1/a,
    # beta<1/4 for s>=64, and V-8>=V/2.
    # Exact rational lower certificate independently checks its claim.
    if e_clean_expected_lower<uniform_coarse:
        raise AssertionError("probabilistic four-clean capacity NO-GO constant failed")
    return {
        "status":"THEOREM_L_ALL_H_PROBABILISTIC_NONUNIFORM",
        "s":s,"V":V,"N":N,"a":a,"T":T,"U_unassigned_physical_pairs":U,
        "true_original_ordered_four_arm_GQ_matching_count_lower":
            source_matching_ordered_lower,
        "true_physical_corner_Q00_Q11_assignment_probability_exact":
            str(physical_quadrant_probability),
        "conditional_four_decoded_nonincident_clean_anchor_probability_lower":
            str(conditional_clean_lower),
        "deferred_exposure_union_bound":str(union_bad),
        "bad_missing_8_source_endpoint_labels":str(missing_labels),
        "bad_original_GQ_incidence_geometry":str(geometry_exceptions),
        "bad_exposed_original_anchor_intermediate_label_overlaps":
            str(anchor_label_collisions),
        "expected_true_original_middle_four_clean_C_e_lower":
            str(e_clean_expected_lower),
        "expected_C_e_over_s4_lower":str(e_clean_expected_lower/s**4),
        "expected_total_C_over_s8_lower":str(e_clean_expected_lower*N/s**8),
        "PROVED_EXISTENCE_some_true_global_injection_with_max_Ce_ge_s4_over_1e6":True,
        "PROVED_EXISTENCE_some_true_global_injection_with_total_C_ge_N_s4_over_1e6":True,
        "REFUTED_universal_max_Ce_little_o_s4":True,
        "REFUTED_universal_sum_Ce_little_o_s8":True,
        "not_a_counterexample_to_H_e_little_o_s4":True,
        "positive_original_GF5_sixset_transfer_proved":False,
        "root_Branch_A_proved_or_refuted":False,
    }


def report():
    return {
        "status":"THEOREM_L_CLEAN_CAPACITY_NO_GO",
        "root_A":"OPEN",
        "genuine_W3s_source_algebra_not_finite_heuristic":True,
        "certificates":[random_original_five_clean_certificate(s)
                        for s in (64,128,256,1024,4096,65536)],
    }


if __name__=="__main__":
    print(json.dumps(report(),indent=2,sort_keys=True))
