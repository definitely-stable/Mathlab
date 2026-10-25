"""HYP-105 #230 D6-AA4-M: exact ALL-h randomized GLOBAL source-charge expectation.

A genuine all-h stochastic (NOT deterministic all-label) positive charge
theorem from B-left/A-right source-incidence forests. Independent uniform
complete typed physical-edge injections, no independent sixset choices.

E[S_B/A] = N_B/A * p_B(a,K) * p_A(a,K)
E[I_L_internal,B/A] = (3/5)*N_B/A*p_B*p_A.
N_B/A >= V*C(s+1,2)*prod_{j=0..3}[(s+1)(V-3-2j)]/4!.
The exact lower asymptotically equals (140+o(1))s^6 for S_B/A and
(84+o(1))s^6 for I_L. This proves existence of at least one
HIGH-charge real full map, not a positive lower for EVERY f,g.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb, factorial, perm, prod

from hyp105_issue230_d6aa4e_global_assignment_dual import alphabet_capacity
from hyp105_issue230_d6aa4g_overlap_capacity import complete_fixed_image_states


def exact_random_projection_probabilities(s):
    """Uniform injection assigns ordered distinct original factor edges from K_a."""
    if type(s) is not int or s<2 or s&(s-1):
        raise ValueError("s must be an original 2^h >=2")
    par=alphabet_capacity(s)
    a,K,V=par["a"],par["K"],par["V"]
    if a<6 or K<6:
        raise AssertionError("true original alphabet cannot host six physical coordinates")
    pA=Fraction(comb(a,6)*70*factorial(6),perm(K,6))
    pB=Fraction(K*comb(a-2,4)*3*factorial(4),perm(K,5))
    if not 0<pA<=1 or not 0<pB<=1:
        raise AssertionError("physical degree-two exact half-projection counts invalid")
    return {
        "s":s,"V":V,"a":a,"K":K,
        "pA_exact":pA,"pB_exact":pB,
        "A_ordered_injective_good_images":comb(a,6)*70*factorial(6),
        "A_ordered_injective_total_images":perm(K,6),
        "B_ordered_injective_good_images":K*comb(a-2,4)*3*factorial(4),
        "B_ordered_injective_total_images":perm(K,5),
        "A_has_C6_or_two_triangles_60_plus_10":True,
        "B_has_one_double_edge_plus_C4":True,
        "independent_full_typed_global_injections_not_per_Q_assignments":True,
    }


def original_BA_source_lower(s):
    """All-h true original GQ 6-flag count lower with B(point)/A(line).

    Select repeated true ORIGINAL point p and TWO actual incident lines,
    then four true ORIGINAL incidences with fresh source points (none p)
    and fresh ORIGINAL lines (none of the two lines), one new p & l per
    selection. The simple union bound forbids <=(3+2j)(s+1) flags after
    j additional flags; divide by 4! to unorder the four extra flags.
    This counts six distinct true ORIGINAL incidence IDs and has
    exactly one degree-two original point, six distinct original lines.
    """
    z=exact_random_projection_probabilities(s)
    V=s0=z["V"]
    d=s+1
    next_flags=tuple(d*(V-3-2*j) for j in range(4))
    if min(next_flags)<=0:
        raise AssertionError("all-h greedy four independent genuine flags failed")
    lower=Fraction(V*comb(d,2)*prod(next_flags),factorial(4))
    if lower<=0:
        raise AssertionError("true original B/A source candidate lower nonpositive")
    return {
        "s":s,"V":V,"original_point_line_incidence_degree":d,
        "repeated_original_point_has_two_distinct_source_lines":True,
        "four_additional_true_original_flags_point_line_fresh":True,
        "ordered_four_additional_true_source_flags_lower":prod(next_flags),
        "four_sequential_flag_choice_lower_bounds":next_flags,
        "guaranteed_original_B_point_A_line_sixsets_lower":lower,
        "true_original_point_repetition_type":"B",
        "true_original_line_multiplicity_type":"A",
        "not_GF5_accepted_without_physical_projection":True,
    }


def exact_random_global_charge_theorem(s):
    """Rigorous exact expectation lower and genuine all-h Omega(s^6) IN MEAN."""
    px=exact_random_projection_probabilities(s)
    sc=original_BA_source_lower(s)
    M=sc["guaranteed_original_B_point_A_line_sixsets_lower"]
    pA,pB=px["pA_exact"],px["pB_exact"]
    lower_S=M*pA*pB
    lower_internal=lower_S*Fraction(3,5)
    if not lower_internal>0:
        raise AssertionError("expected source-charge lower must be strictly positive")
    return {
        "s":s,"V":px["V"],"a":px["a"],"K":px["K"],
        "complete_GLOBAL_uniform_typed_injections_symmetric":True,
        "all_h_original_source_B_point_A_line_candidate_lower":str(M),
        "exact_physical_B_probability":str(pB),
        "exact_physical_A_probability":str(pA),
        "same_original_point_two_lines_conditioned_A_disjoint_probability":"3/5",
        "expected_true_B_left_A_right_seven_GF5_count_lower":str(lower_S),
        "expected_internal_ORIGINAL_line_pair_GF5_charge_lower":str(lower_internal),
        "rational_BA_expectation_lower_over_s6":str(lower_S/s**6),
        "rational_internal_charge_lower_over_s6":str(lower_internal/s**6),
        "asymptotic_BA_expected_count_lower_coefficient":"140",
        "asymptotic_internal_expected_charge_lower_coefficient":"84",
        "there_exists_a_real_complete_map_with_high_total_I":True,
        "universal_all_maps_charge_lower_PROVED":False,
        "universal_S_s6_lower_PROVED":False,
        "full_GF5_R3_PROVED":False,
        "stochastic_positivity_is_not_deterministic_minimax":True,
    }


def genuine_original_W32_exact_BA_source_count():
    """Independent literal true 45-original-incidence source B/A enumeration.

    Explicitly enumerate the 2-star root and FOUR additional matching
    flags for every choice of the repeated original point and pair of
    incident lines. Compare to source-greedy all-h lower, and independently
    check each six-flag true original endpoint multiplicity.
    """
    from hyp105_issue230_projection import fixture
    model=fixture(1,"lex")
    inc=tuple(tuple(x) for x in model["incidences"])
    v=15
    if len(inc)!=45 or model["s"]!=2:
        raise AssertionError("not a genuine W32 original incidence host")
    by_point=[[] for _ in range(v)]
    for p,l in inc:by_point[p].append(l)
    if any(len(x)!=3 for x in by_point):
        raise AssertionError("not real regular W32 source incidence geometry")
    total=0
    min_choices=10**30
    max_choices=0
    for p in range(v):
        for chosen_lines in combinations(by_point[p],2):
            bad_lines=frozenset(chosen_lines)
            edges=[(q,l) for q,l in inc if q!=p and l not in bad_lines]
            subtotal=0
            for four in combinations(edges,4):
                if len({q for q,l in four})==4 and len({l for q,l in four})==4:
                    subtotal+=1
            total+=subtotal
            min_choices=min(min_choices,subtotal)
            max_choices=max(max_choices,subtotal)
    floor=original_BA_source_lower(2)[
        "guaranteed_original_B_point_A_line_sixsets_lower"]
    if total<floor:
        raise AssertionError("genuine ORIGINAL 6-set source candidate counting under floor")
    return {
        "s":2,
        "all_true_original_incidence_ID_count":len(inc),
        "independently_enumerated_original_B_point_A_line_Q_exact":total,
        "all_h_greedy_source_lower":str(floor),
        "source_two_star_roots":v*comb(3,2),
        "minimum_completion_count_per_two_star_root":min_choices,
        "maximum_completion_count_per_two_star_root":max_choices,
        "no_physical_GF5_classification_in_original_source_count":True,
    }


def original_W32_BA_internal_charge_fiber(scheme):
    """Exact 24 coherent maps / 62,370 candidates: true class & internal charge."""
    from hyp105_issue230_projection import fixture
    from hyp105_g5e2b3e1b0_seven_signature import seven_census
    from hyp105_issue230_d6aa4c_edit_transversal import (
        genuine_original_positive_hypergraph,incidence_cover_bits)
    from hyp105_issue230_d6aa4d_mixed_transversal_fibers import (
        finite_source_support_partition)
    from hyp105_issue230_d6aa4k_projection_aware_charge import (
        true_original_projection_charge)
    model=fixture(1,scheme)
    original=tuple(tuple(e) for e in model["incidences"])
    if scheme not in ("S68","S72") or len(original)!=45:
        raise ValueError("genuine pinned original W32 schemes S68/S72 only")
    from hyp105_issue230_d6aa4i_original_spectral_coordinate import geometry
    g=geometry(2,original)
    r=genuine_original_positive_hypergraph(model)
    bits,weights,mask=incidence_cover_bits(r["records"])
    partition=finite_source_support_partition(bits,weights,mask)
    if partition["number_transversal_blocks"]!={"S68":53,"S72":119}[scheme]:
        raise AssertionError("original AA4D four-source transversal drift")
    block=next((tuple(b) for b in partition["transversal_original_factor_blocks"]
                if len(b)==4 and all(0<=i<15 for i in b)),None)
    if block is None:
        raise AssertionError("no true ORIGINAL all-point four-factor hitting block")
    baseline=tuple(tuple(model["left_labels"][p]) for p in block)
    states=complete_fixed_image_states(("P",)*4,baseline)
    right=tuple(tuple(x) for x in model["right_labels"])
    observations=[]
    for st in states:
        left=list(tuple(tuple(x) for x in model["left_labels"]))
        for p,lab in zip(block,st):left[p]=lab
        current={**model,"left_labels":tuple(left),"right_labels":right}
        full=seven_census(current,independent_checks=False,witness_sets=True)
        cls=full["sets"]
        # One B(left)/A(right) ORIGINAL Q has exactly one doubled original
        # source point factor and hence exactly ONE source-concurrent pair
        # of actual right LINE factor IDs. It is eligible precisely if
        # those two right physical labels share NO coordinate.
        B=0;internal=0;with_right_line_pencil=0
        for Q,tag in cls.items():
            if tag!="B-left/A-right":
                continue
            six=tuple(original[i] for i in Q)
            freq=Counter(p for p,l in six)
            roots=[p for p,n in freq.items() if n==2]
            if len(roots)!=1 or len({l for p,l in six})!=6:
                raise AssertionError("actual ORIGINAL B/A source graph pattern wrong")
            lines=tuple(l for p,l in six if p==roots[0])
            if len(lines)!=2 or lines[0]==lines[1]:
                raise AssertionError("not exactly one actual source-line concurrent pair")
            with_right_line_pencil+=1
            B+=1
            internal+=not bool(set(right[lines[0]])&set(right[lines[1]]))
        source_total=true_original_projection_charge(g,current,cls)
        if B!=source_total["true_ORIGINAL_Q_by_class"].get(
                "B-left/A-right",{}).get("count",0):
            raise AssertionError("independent original GF5 B/A count disagrees")
        if not 0<=internal<=B or internal>source_total["source_L_charge"]:
            raise AssertionError("internal source L charge not subset of actual AA4K true charge")
        observations.append({
            "seven_original_S":full["S_seven"],
            "B_left_A_right_actual_positive_Q":B,
            "B_left_A_right_true_original_internal_line_charge":internal,
            "B_left_A_right_true_original_internal_line_charges_uncovered":B-internal,
            "independent_class_sensitive_original_L_charge":
                source_total["source_L_charge"],
            "actual_source_L_internal_charge_subset_verified":True,
        })
    if len(observations)!=24 or observations[0]["seven_original_S"]!={
        "S68":68,"S72":72}[scheme]:
        raise AssertionError("actual W32 source four-factor baseline changed")
    keys=tuple(observations[0])
    ranges={k:{"min":min(row[k] for row in observations),
               "max":max(row[k] for row in observations)}
            for k in keys if type(observations[0][k]) is int}
    return {
        "scheme":scheme,
        "true_original_source_four_point_block":block,
        "complete_genuinely_injected_K6_states":24,
        "all_original_sixset_candidates_per_state":62370,
        "original_W32_uniform_random_expectation_source_BA_Q_count_exact":
            genuine_original_W32_exact_BA_source_count()[
                "independently_enumerated_original_B_point_A_line_Q_exact"],
        "all_h_random_injection_expectation_theorem_not_mean_of_this_fiber":True,
        "all_24_full_original_GF5_observations":observations,
        "exact_ranges":ranges,
        "root_A":"OPEN","root_B":"OPEN",
    }


def report(scheme=None):
    x={
        "slice":"HYP105-ISSUE230-D6-AA4-M-UNIFORM-INJECTION-CHARGE",
        "all_h_exact_random_projection_probabilities":
            tuple({**{k:(str(v) if isinstance(v,Fraction) else v)
                        for k,v in exact_random_projection_probabilities(2**h).items()}}
                  for h in range(1,9)),
        "all_h_exact_random_full_map_expectation_lower":
            tuple(exact_random_global_charge_theorem(2**h)
                  for h in range(1,9)),
        "exact_original_W32_source_BA_sixset_count":
            genuine_original_W32_exact_BA_source_count(),
        "all_h_expected_I_omega_s6_but_not_uniform_minimum":True,
        "deterministic_all_h_I_omega_s6_PROVED":False,
        "root_A":"OPEN","root_B":"OPEN",
        "full_GF5_R3_PROVED":False,"ASET_exponent_PROVED":False,
    }
    if scheme:
        x["true_original_W32"]=original_W32_BA_internal_charge_fiber(scheme)
    return x


if __name__=="__main__":
    import argparse,json
    p=argparse.ArgumentParser()
    p.add_argument("--scheme",choices=("S68","S72"))
    args=p.parse_args()
    print(json.dumps(report(args.scheme),indent=2,sort_keys=True))
