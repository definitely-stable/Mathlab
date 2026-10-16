"""AA4-BE: partially pinned TRUE ORIGINAL accepted GF(5) D6 sixflag extension.

Not another 3-flag GOOD result.  Every dyadic h>=5, genuine W(3,s),
ALL fixed globally injected original POINT maps f, ALL adversarial V-edge
right physical occupied sets E, ANY set of <=floor(V/16) genuine original
LINE source IDs pinned injectively to E admits a globally consistent
full g extending the pins with genuine ORIGINAL six-distinct-incidence
positive historically accepted D6 count >= s**6.

Proof: delete pinned ORIGINAL six-line incidence sets from genuine point
physical C6 candidate pool, separately delete pinned occupied physical
edges from right sixcycles, then ONE conditional GLOBAL line permutation
of the remaining line factors. No per-Q redraw; no assertion for ALL
completely fixed g or historical other GF5 classes.
"""
from fractions import Fraction
from itertools import combinations, permutations, product
from math import comb

from hyp105_issue230_d6aa4ay_quenched_allD_opposite_mean import _params


def falling(n, length):
    if type(n) is not int or type(length) is not int or length < 0 or n < length:
        raise ValueError("need distinct original source labels and physical images")
    result=1
    for v in range(n-length+1,n+1):
        result*=v
    return result


def original_D6_sixflag_pinned_envelope(s,k):
    """Exact Fraction all-h universally quantified six-ID D6 expectation."""
    if type(s) is not int or s<32 or s & (s-1):
        raise ValueError("genuine dyadic s>=32")
    V,a,K,m=_params(s)
    if type(k) is not int or not 0<=k<=V//16:
        raise ValueError("up to floor(V/16) distinct ORIGINAL LINE factor pins")
    d=s+1
    full_Ka_C6=Fraction(falling(a,6),12)
    one_edge_C6=falling(a-2,4)
    full_support_C6_floor=full_Ka_C6-m*one_edge_C6
    six_distinct_lines_per_point_C6_floor=d**4*(d*d-15)
    original_point_source_Q_floor=full_support_C6_floor*six_distinct_lines_per_point_C6_floor
    source_one_actual_line_influence_upper=d**6*one_edge_C6
    source_unpinned_Q_floor=original_point_source_Q_floor-k*source_one_actual_line_influence_upper
    right_unpinned_physical_C6_floor=full_support_C6_floor-k*one_edge_C6
    n=V-k
    if full_support_C6_floor < Fraction(19,20)*full_Ka_C6:
        raise AssertionError("minimal full K_a support C6 floor")
    if source_unpinned_Q_floor < full_Ka_C6*d**6/2:
        raise AssertionError("true GQ source six-flag Q mass with arbitrary pins")
    if right_unpinned_physical_C6_floor < full_Ka_C6/2:
        raise AssertionError("target physical sixcycle mass after arbitrary pins")
    p_right=Fraction(12*right_unpinned_physical_C6_floor,falling(n,6))
    mean_floor=source_unpinned_Q_floor*p_right
    if mean_floor<s**6:
        raise AssertionError("all-h accepted genuine ORIGINAL GF5 D6 existence")
    if full_Ka_C6*12*10 < 9*a**6:
        raise AssertionError("all-h (a)_6 >= 9a^6/10; algebra miscalibrated")
    if mean_floor < Fraction(27,25)*d**6:
        raise AssertionError("sharp simple all-h mean >=27/25 d^6")
    M=full_Ka_C6*d**6
    if M<mean_floor:
        raise AssertionError("full original sixflag maximum smaller than expectation")
    success_density_floor=Fraction(s**6,2)/M
    if not 0<success_density_floor<=1:
        raise AssertionError("rigorous counting density threshold invalid")
    return {
        "s":s,"h":s.bit_length()-1,"V":V,"a":a,"m":m,
        "allowed_arbitrary_original_LINE_pin_count":V//16,
        "actual_original_LINE_pins":k,"unpinned_original_line_count":n,
        "K_a_full_physical_C6":full_Ka_C6,
        "single_occupied_physical_pair_edge_C6_upper":one_edge_C6,
        "physical_complete_support_C6_floor":full_support_C6_floor,
        "original_genuine_six_distinct_line_choices_per_point_C6_floor":
            six_distinct_lines_per_point_C6_floor,
        "original_point_C6_sixflag_candidates_avoiding_all_pinned_line_IDs_floor":
            source_unpinned_Q_floor,
        "right_physical_C6_avoiding_all_pinned_pair_edge_images_floor":
            right_unpinned_physical_C6_floor,
        "one_global_conditional_D6_target_probability_lower":p_right,
        "one_global_conditional_original_sixID_D6_expected_count_lower":mean_floor,
        "some_complete_legal_extension_selected_original_D6_ge_s6":True,
        "fraction_of_completed_global_g_with_original_D6_at_least_s6_over2_lower":
            success_density_floor,
        "every_given_full_original_g_has_positive_D6_NOT_PROVED":True,
        "seven_GF5_sum_for_EACH_complete_f_g_NOT_PROVED":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


def original_W32_true_source_candidate_and_physical_cycle_census(model,pins):
    """Finite independent genuine W32 literal original source flags.

    Exhaust original 6-point physical C6 and source six *distinct* LINE IDs.
    Compare against exact one GLOBAL conditional right permutation expectation.
    W32 h=1 is a finite oracle ONLY; not h>=5 theorem.
    """
    s=model["s"]
    if s !=2:
        raise ValueError("independent exhaustive original sixflag census only W32")
    V,a,_,_=_params(s)
    left=tuple(tuple(sorted(x)) for x in model["left_labels"])
    right=tuple(tuple(sorted(x)) for x in model["right_labels"])
    incidence=set(map(tuple,model["incidences"]))
    if len(incidence)!=V*(s+1) or len(left)!=V or len(right)!=V:
        raise ValueError("complete genuine W32 typed original f/g source needed")
    if len(set(left))!=V or len(set(right))!=V:
        raise ValueError("global physical pair assignments must be injective")
    if not isinstance(pins,dict) or any(type(x) is not int or x<0 or x>=V
                                       for x in pins):
        raise ValueError("pin actual LINE IDs")
    lockedges=set()
    for j,e in pins.items():
        e=tuple(sorted(e))
        if e not in right or e in lockedges:
            raise ValueError("pins must target globally different occupied right edges")
        lockedges.add(e)
    nbr=[[] for _ in range(V)]
    for p,l in incidence:
        nbr[p].append(l)
    original_point={edge:p for p,edge in enumerate(left)}
    supportright=set(right)
    pinids=set(pins)

    def physical_cycles(support):
        """Independent physical vertex permutation / 12 canon quotient."""
        cycles=set()
        for vertices in permutations(range(a),6):
            edges=tuple(tuple(sorted((vertices[i],vertices[(i+1)%6])))
                        for i in range(6))
            if all(e in support for e in edges):
                cycles.add(frozenset(edges))
        return tuple(cycles)

    src_cycles=physical_cycles(set(left))
    right_free_cycles=physical_cycles(supportright-lockedges)
    n=V-len(pins)
    original_Q=0
    raw_Q=0
    full_lineIDsets=set()
    for edges in src_cycles:
        pts=tuple(original_point[e] for e in sorted(edges))
        for lines in product(*(nbr[p] for p in pts)):
            if len(set(lines)) !=6:
                continue
            raw_Q+=1
            full_lineIDsets.add(tuple(sorted(lines)))
            if not any(j in pinids for j in lines):
                original_Q+=1
    exact_conditional_mean=Fraction(
        12*len(right_free_cycles)*original_Q,falling(n,6))
    return {
        "s":s,"V":V,"k":len(pins),"point_C6_count":len(src_cycles),
        "original_pointC6_six_distinct_lineID_source_Q_count":raw_Q,
        "original_sixflag_candidates_avoiding_pinned_lines":original_Q,
        "right_C6_cycles_avoiding_pinned_physical_edges":len(right_free_cycles),
        "exact_ONE_complete_original_LINE_permutation_conditional_D6_mean":
            exact_conditional_mean,
        "same_six_original_incidence_IDs_and_one_global_g":True,
        "W32_DOES_NOT_PROVE_all_h_floor":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }
