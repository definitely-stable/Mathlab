"""AA4-CD — true original W3 one-sided fixed-(f,g) seven-GF5 certificate.

Source: genuine symplectic W(3,2^h) for all h>=1, SIX DISTINCT
original incidence IDs Q projected onto SAME physical point/LINE factor
injections f,g, possibly arbitrarily correlated. Six WHOLE original
LINE-source-factor image swap pairs define one globally coherent cube.

Unlike #602's absolute high-degree residual, for a LOWER bound on the
UNCHANGED historical seven-class weighted score only the NEGATIVE
Walsh highpass is relevant. Exact one-sided source-support envelope:

  R_Q(x) >= -2^-k sum_{y in necessary physical support}
                                  max(-K_k(x xor y),0).

This is valid without knowing whether a candidate Q is historical
GF5 accepted on the RIGHT; actual physical right 2-factor screening
is a necessary condition. It can strictly improve the lower certificate
even if no new uniform abstract eta6 bound is proved. Branch A/B/C
remain unproved.
"""
from collections import Counter
from fractions import Fraction

from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4bq_all_seven_reverse_switching import (
    validate_disjoint_factor_swaps,
)
from hyp105_issue230_d6aa4br_all_seven_signed_source_flux import (
    immutable_original_sixflag_class,
)
from hyp105_issue230_d6aa4bx_all_seven_center_kernel import (
    high_degree_boolean_kernel,
)
from hyp105_issue230_d6aa4cb_original_parity_affine_center import (
    _source_parity_raw,_right_two_factor_local,
    true_original_W32_g_conditioned_all_seven_center,
)
from hyp105_g5e2b3e1b0_seven_signature import R3_CERTIFIED_FLOORS
from hyp105_g5e2b3e1a_fixed_leading import selected_left_six


def one_sided_signed_support_certificate(support,k,reference=0):
    """Exact integer/Fraction one-sided Walsh uncertainty, NO classifier.

    Every actual historical GF5 acceptance I(y) is in {0,1} and is 0
    outside the supplied necessary source-Q right geometric support.
    Therefore -Eminus <= R_Q(reference) <= Eplus.
    This remains true when k=4,5,6 and Qs are arbitrarily correlated.
    """
    if type(k) is not int or not 0<=k<=6:
        raise ValueError("a sixflag touches between zero and six packets")
    if type(reference) is not int or not 0<=reference<(1<<k):
        raise ValueError("reference vertex belongs to the actual local cube")
    support=tuple(support)
    if len(set(support))!=len(support) or any(
        type(y) is not int or y<0 or y>=(1<<k) for y in support
    ):
        raise ValueError("invalid or duplicate local physical map-state IDs")
    if k<=3:
        return {"minus":Fraction(0),"plus":Fraction(0),
                "null_cutoff":True}
    K=high_degree_boolean_kernel(k)
    pos=sum(max(K[reference^y],0) for y in support)
    neg=sum(max(-K[reference^y],0) for y in support)
    return {
        "minus":Fraction(neg,1<<k),
        "plus":Fraction(pos,1<<k),
        "null_cutoff":False,
        "n_physically_possible_states":len(support),
    }


def true_original_W32_one_sided_f_g_seven_center(model,pairs):
    """All seven positive historical source types, original Q unchanged.

    Scans 62370 LEFT physically six-coordinate eligible original Q once,
    uses NO original RIGHT GF5 classifier. Only original physical g
    parity/degree support and known IMMUTABLE source class. The parent
    two-sided #602 geometry bound is independently checked for nesting.
    """
    s,V,a,inc,f,g,_,_=_original_source(model)
    if (s,V,a)!=(2,15,6):
        raise ValueError("finite historical census source W32/K6 only")
    pairs=validate_disjoint_factor_swaps(V,pairs)
    if len(pairs)!=6:raise ValueError("six DISJOINT real original LINE packets")
    weights=R3_CERTIFIED_FLOORS
    result={
        "parity_minus_center":Fraction(0),
        "parity_plus_center":Fraction(0),
        "right_2factor_minus_center":Fraction(0),
        "right_2factor_plus_center":Fraction(0),
        "parity_minus_uniform":Fraction(0),
        "parity_plus_uniform":Fraction(0),
        "right_2factor_minus_uniform":Fraction(0),
        "right_2factor_plus_uniform":Fraction(0),
    }
    stats=Counter()
    count=0
    for Q,_ in selected_left_six(model):
        tag=immutable_original_sixflag_class(Q,inc)
        if tag not in weights:continue
        used,deltas,base,rank,parity=_source_parity_raw(Q,inc,g,pairs)
        k=len(used)
        if k<=3:continue
        count+=1
        stats[("touch",k)]+=1
        if not parity:stats[("parity_impossible",k)]+=1
        right=tuple(y for y in parity if
            _right_two_factor_local(Q,inc,g,pairs,used,y))
        if not right:stats[("2factor_impossible",k)]+=1
        for name,S in (("parity",parity),("right_2factor",right)):
            src=one_sided_signed_support_certificate(S,k,reference=0)
            weight=weights[tag]
            result[name+"_minus_center"]+=weight*src["minus"]
            result[name+"_plus_center"]+=weight*src["plus"]
            if S:
                bounds=(one_sided_signed_support_certificate(S,k,x)
                        for x in range(1<<k))
                maxneg=Fraction(0);maxpos=Fraction(0)
                for z in bounds:
                    maxneg=max(maxneg,z["minus"])
                    maxpos=max(maxpos,z["plus"])
            else:
                maxneg=Fraction(0);maxpos=Fraction(0)
            result[name+"_minus_uniform"]+=weight*maxneg
            result[name+"_plus_uniform"]+=weight*maxpos
    parent=true_original_W32_g_conditioned_all_seven_center(model,pairs)
    old=parent["true_original_g_quenched_all_seven_envelopes"]
    # The historical f-only parent #601 cap is universal, and the
    # existing two-sided #602 per-Q center/whole bound is also valid.
    # Capping a lower-tail envelope preserves the one-sided inequality.
    for name in ("parity","right_2factor"):
        for which in ("center","uniform"):
            for sign in ("minus","plus"):
                label=name+"_"+sign+"_"+which
                result[label]=min(result[label],old[
                    name+("_original_center" if which=="center" else "_uniform")])
    for which in ("center","uniform"):
        for sign in ("minus","plus"):
            if result["right_2factor_"+sign+"_"+which]>result[
                "parity_"+sign+"_"+which]:
                raise AssertionError("necessary original right supports nested")
    for name in ("parity","right_2factor"):
        for sign in ("minus","plus"):
            if result[name+"_"+sign+"_center"]>result[
                name+"_"+sign+"_uniform"]:
                raise AssertionError("uniform original one-sided error smaller than center")
    return {
        "s":s,"V":V,"a":a,
        "six_actual_original_source_LINE_swap_packets":pairs,
        "actual_original_Q_with_k_ge4":count,
        "physical_impossibility_statistics":dict(stats),
        "unchanged_full_g_conditioned_one_sided_GF5_seven_envelopes":result,
        "prior_two_sided_original_g_conditioned":old,
        "right_historical_GF5_classifier_used_for_support":False,
        "valid_for_all_complete_original_correlated_f_g":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


def true_original_W32_signed_seven_center_lower(model,pairs):
    """Independent full historical census verifies new ONE-SIDED lower."""
    from hyp105_issue230_d6aa4bx_all_seven_center_kernel import (
        true_original_W32_all_seven_center_envelope,
    )
    gonly=true_original_W32_one_sided_f_g_seven_center(model,pairs)
    historic=true_original_W32_all_seven_center_envelope(model,pairs)
    errors=gonly["unchanged_full_g_conditioned_one_sided_GF5_seven_envelopes"]
    signed=historic["signed_higher_order_weighted_values"]
    low=historic["degree_at_most_three_weighted_values"]
    W=historic["full_64_original_GF5_seven_weighted_necessary_numerators"]
    E_lower=errors["right_2factor_minus_center"]
    E_upper=errors["right_2factor_plus_center"]
    if not (-E_lower<=signed[0]<=E_upper):
        raise AssertionError("original genuine seven-class signed center interval wrong")
    # Uniform errors bound signed residual at all 64 complete maps.
    if any(not -errors["right_2factor_minus_uniform"]<=v<=
           errors["right_2factor_plus_uniform"] for v in signed):
        raise AssertionError("genuine full GF5 64map signed one-sided uniform bound broken")
    floor=max(Fraction(0),low[0]-E_lower)
    if floor>W[0]:
        raise AssertionError("ONE-SIDED historical original GF5 lower excluded true count")
    return {
        "original_UNCHANGED_seven_GF5_weighted_count":W[0],
        "historical_zero_through_third_signed_projection":low[0],
        "historical_signed_high_order_correction":signed[0],
        "new_certified_UNCHANGED_seven_GF5_weighted_lower":floor,
        "prior_absolute_right_2factor_error":
            gonly["prior_two_sided_original_g_conditioned"][
                "right_2factor_original_center"],
        "new_one_sided_negative_error":E_lower,
        "new_one_sided_positive_error":E_upper,
        "all_64_complete_right_global_maps_one_sided_verified":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }
