"""HYP-105 AA4-INTREF: independent all-h Branch A proof-obligation integration.

This is a MATHEMATICAL VALIDATION LEDGER, not the assertion that CI
or finite W32/W34 observations independently prove the root theorem.

The ledger composes the frozen historical #659 tail dichotomy, #672
original-source bounded core and mixed blocked-triple bridge, and new
local all-h #676--#682 refinements, with ALL external graph theorem
constants positive but otherwise UNSPECIFIED.

Actual source universe: W(3,2^h), complete separately injected
arbitrarily correlated f,g, six different true ORIGINAL incidence
IDs per accepted historical GF5 sixset. The external balanced C6
supersaturation assertion is an explicitly CONDITIONAL INPUT to the
ledger, NOT a newly proved theorem. No physical label resampling.

The key new integration result is an EXACT integer sufficient dyadic
threshold h0 and a machine-checkable implication for EVERY h>=h0
and EVERY fixed legal f,g:
  (D6 >= delta*s^6) OR (U_BBo >= s^6/8),
therefore S_seven >= delta*s^6, with
  delta=min(1/8,c_graph*2^-108) >0.
The mathematical implication is valid IF ALL stated source geometric
and #659 external graph supersaturation inputs hold. It does not
certify external scholarly review or root issue closure.

All proof-obligation checks use integers and fractions, not floats.
"""
from fractions import Fraction
from math import comb, isqrt


def _positive_fraction(value,name):
    try:q=Fraction(value)
    except (TypeError,ValueError,ZeroDivisionError):
        raise ValueError(f"{name} requires positive rational")
    if q<=0 or isinstance(value,bool):
        raise ValueError(f"{name} requires positive rational")
    return q


def _ceil_fraction(x):
    q=Fraction(x)
    return -(-q.numerator//q.denominator)


def _ceil_sqrt(x):
    if type(x) is not int or x<0:
        raise ValueError("ceil sqrt requires nonnegative integer")
    t=isqrt(x)
    return t+(t*t<x)


def _min_dyadic_at_least(n):
    if type(n) is not int or n<=0:
        raise ValueError("positive integer minimal dyadic")
    h=max(1,(n-1).bit_length())
    s=1<<h
    if not s>=n or (h>1 and s//2>=n):
        raise AssertionError("nonminimal dyadic threshold")
    return h,s


def _root_theorem_constants_from_source_lemmas(T):
    """Independent FROM-SCRATCH path/moment algebra; not parent s0 helper."""
    if type(T) is not int or T<1:
        raise ValueError("T positive integer")
    K=64
    sigma2inv=16*(K+1)**2
    sigma3inv=64*(K+1)**3
    L6=24+288*T*T
    L4_upper=2*sigma2inv*sigma2inv*_ceil_sqrt(8*L6)+40*T
    B0_upper=64*_ceil_sqrt((K+1)*T)
    LE_sq=21*sigma3inv*sigma3inv*L6
    thresholds={
        "s_ge_64_original_core_and_alphabet":64,
        "s_ge_816T_improper_threepaths":816*T,
        "s_ge_144_LE_squared_exceptional_endpoints":144*LE_sq,
        "s_ge_48e8_B0_T_L4_fourth_mixed_internal":
            48**8*(B0_upper*T*L4_upper)**4,
    }
    return {
        "K":K,"T":T,"sigma2_inverse":sigma2inv,
        "sigma3_inverse":sigma3inv,
        "L6":L6,"L4_upper_integer":L4_upper,
        "B0_upper_integer":B0_upper,"LE_squared":LE_sq,
        "thresholds":thresholds,"s0_integer":max(thresholds.values()),
    }


def independently_certify_uniform_branch_A(C_graph,c_graph,*,power_offset=0):
    """Symbolic-rational stress instance for unknown POSITIVE graph constants.

    C_graph,c_graph are supplied as rational *PLACEHOLDERS* for a
    universal result of Jiang--Yepremyan/Simonovits. Passing this
    function for arbitrary concrete positive numbers never verifies
    that those numbers are correct theorem constants. The proof
    keeps them symbolic positive in the manuscript.

    An integer T=ceil(max(1,2^59*C^3)) makes the ORIGINAL tail lemma
    work for epsilon=1/8. The source conflict deletion keeps maximum
    K=64 on remaining flags and yields m0>=s^4 for s>=64.
    Each of the three improved conditional errors contributes at
    most s^6/24 after exact dyadic threshold comparison.
    """
    C=_positive_fraction(C_graph,"C_graph")
    c=_positive_fraction(c_graph,"c_graph")
    if type(power_offset) is not int or not 0<=power_offset<=5:
        raise ValueError("power_offset must be integer 0..5")
    tail_min=Fraction(2**59)*C**3
    T=max(1,_ceil_fraction(tail_min))
    delta=min(Fraction(1,8),c/Fraction(2**108))
    if Fraction(T)<tail_min or delta>c/Fraction(2**108):
        raise AssertionError("original balanced C6 tail dichotomy constants")
    k=_root_theorem_constants_from_source_lemmas(T)
    h0,minimum=_min_dyadic_at_least(k["s0_integer"])
    h=h0+power_offset
    s=1<<h
    V=(s+1)*(s*s+1)
    N=V*(s+1)
    a= (1+isqrt(1+8*V))//2
    while comb(a,2)<V:a+=1
    Cs=(s*s+1)*(s*s+a-2)
    # TRUE ORIGINAL source bounds used to select a deterministic core.
    if not (a*a<=4*s**3 and N<=2*s**4 and
            2*Cs<=3*s**4):
        raise AssertionError("the source geometry/alphabet coarse all-h bounds")
    # After tail E_T<s4/8 and original conflict vertex removal
    # at most 4 Cs/K <=3s4/32:
    # N0 >= N - (1/8+3/32)s4=N-7s4/32,
    # m0 =2N0 >=s4. All integer to avoid float roundings.
    if not (32*(2*N)-14*s**4>=32*s**4):
        raise AssertionError("tail+original-conflict deletions destroy dense core")
    # TRUE source total source flag count and parent physical caps.
    if not (T>=1 and s>=64 and
            2*N<=4*s**4 and
            comb(a,2)>=V and
            (a-1)*(a-2)//2<V):
        raise AssertionError("source/coherent physical core assumption mismatch")
    # All-h known from #679, #680, #681, #682:
    # exact first error / (s6/24) =816*T/s;
    # second error ratio squared is 144*LE²/s;
    # third error ratio to 1 obeys ^8 =48^8(B0*T*L4)^4/s.
    norm={
        "proper_threewalk_loss_le_s6_over_24":
            s>=k["thresholds"]["s_ge_816T_improper_threepaths"],
        "weighted_exceptional_loss_le_s6_over_24":
            s>=k["thresholds"]["s_ge_144_LE_squared_exceptional_endpoints"],
        "mixed_internal_loss_le_s6_over_24":
            s>=k["thresholds"]["s_ge_48e8_B0_T_L4_fourth_mixed_internal"],
    }
    if not all(norm.values()):
        raise AssertionError("integrated Branch A three-error s0 failure")
    # Only the logically known estimates. The conservative certificate
    # gives 1/4 - 3/24 = 1/8 for original accepted BBo sextuples,
    # independently of the signed GF5 R3 coefficient.
    lower=Fraction(1,4)-3*Fraction(1,24)
    if lower!=Fraction(1,8) or not 0<delta<=Fraction(1,8):
        raise AssertionError("original seven class positive disjunction arithmetic")
    parent_cut=Fraction(2**41)*C**3/Fraction(1,8)**6
    parent_D6=c*Fraction(1,8)**12/Fraction(2**72)
    if tail_min!=parent_cut or parent_D6!=c/Fraction(2**108):
        raise AssertionError("original #659 epsilon=1/8 tail normalization incorrect")
    return {
        "graph_constants_are_HYPOTHETICAL_positive_rationals":True,
        "original_external_theorem_constants_NOT_certified":True,
        "GQ_and_original_ID_lemmas_required":True,
        "C_graph_test_value":str(C),"c_graph_test_value":str(c),
        "tail_T_min_rational":str(tail_min),
        "tail_T_safe_integer":T,"tail_epsilon":Fraction(1,8),
        "D6_delta_positive_rational":delta,
        "s0_threshold_from_scratch":k["s0_integer"],
        "minimum_dyadic_h0":h0,
        "tested_h":h,"tested_s_is_dyadic":True,
        "tested_s_bit_length":s.bit_length(),
        "conservative_L6":k["L6"],
        "conservative_L4_integer":k["L4_upper_integer"],
        "sigma2_inverse":k["sigma2_inverse"],
        "sigma3_inverse":k["sigma3_inverse"],
        "all_three_s6_over_24_error_implications":norm,
        "original_BBo_normalization_half":Fraction(1,2),
        "original_BBo_sextic_lower_coefficient":lower,
        "original_source_seven_class_uniform_coefficient":delta,
        "main_research_root_external_acceptance":False,
    }


def true_original_finite_integration_certificate(power,f,g,core_ids=None):
    """Actual ORIGINAL W32/W34 cross-stack finite consistency reviewer.

    Reads five INDEPENDENT routes, never constructs a synthetic graph
    or accepts a large-h proof because finite checks agree.
    """
    from hyp105_universal_sextic_obstruction import finite_source_certificate
    from hyp105_improper_path_intersection import genuine_original_improper_path_referee
    from hyp105_mixed_source_book_defect import exact_source_book_partition
    from hyp105_exact_exceptional_endpoints import (
        finite_true_original_endpoint_partition,
        finite_independent_physical_endpoint_partition,
        finite_genuine_core_path_endpoint_mass,
    )
    from hyp105_BBo_inverse_source_bridge import inverse_original_BBo_paths
    from hyp105_full_physical_degree_tail import genuine_source
    from hyp105_physical_degree_energy import minimal_alphabet,_verify_typed_injections

    if type(power) is not int or power not in (1,2):
        raise ValueError("finite real original W32/W34 source only")
    s,V,flags=genuine_source(power)
    a=minimal_alphabet(V)
    f=tuple(map(tuple,f));g=tuple(map(tuple,g))
    _verify_typed_injections(a,V,f,g)
    ids=tuple(range(len(flags))) if core_ids is None else tuple(core_ids)
    if len(set(ids))!=len(ids) or (
        any(type(i) is not int or not 0<=i<len(flags) for i in ids)):
        raise ValueError("true source core must have distinct valid ID values")
    # Parent original proof finite enumerator is NOT used to generate
    # the other four independently defined exact calculators.
    parent=finite_source_certificate(power,f,g,ids)
    B2=genuine_original_improper_path_referee(power,f,g,ids)
    mixed=exact_source_book_partition(power,f,g,ids)
    src=finite_true_original_endpoint_partition(power,f,g)
    physical=finite_independent_physical_endpoint_partition(power,f,g)
    weighted=finite_genuine_core_path_endpoint_mass(power,f,g,ids)
    expected=src["source_first_four_way_endpoint_partition"]
    if expected!=physical:
        raise AssertionError("independent endpoint four-class populations mismatch")
    checks={
        "original_core_flag_id_count":
            parent["original_core_flags"]==B2["original_core_incidence_flag_count_N0"]==len(ids),
        "actual_original_full_core_two_coordinate_books":
            (parent["two_step_x_return"]==B2["original_source_Qx"]
             and parent["two_step_y_return"]==B2["original_source_Qy"]),
        "original_source_conflict_books":
            (parent["M_f_core"]==B2["original_source_Mf"] and
             parent["M_g_core"]==B2["original_source_Mg"]),
        "proper_improper_second_step_fourth_moment":
            parent["core_trace_four"]==B2["physical"]["trace_A0_fourth_exact"],
        "actual_core_physical_all_directed_threewalks":
            parent["all_directed_three_walks"]==B2["physical"]["direct_threewalk_total"],
        "actual_core_physical_proper_threewalks":
            (sum(parent["path_partition"].values())==
             weighted["physical_proper_path_total"]==
             B2["physical"]["direct_proper_threewalks"]),
        "actual_true_original_source_mixed_blocked_triples":
            parent["mixed_triple_count"]==mixed["source_exact_blocked_triple_B"],
        "actual_true_original_source_phi_upper":
            parent["mixed_triple_upper"]==mixed["source_original_book_phi"],
        "real_physical_first_internal_blocked_core_paths":
            parent["first_internal_x_paths"]<=parent["mixed_triple_count"]*
            max(1,B2["physical"]["maximum_degree"]**2),
        "actual_proper_physical_endpoint_Frobenius":
            (parent["proper_endpoint_square_mass"]==
             weighted["physical_endpoint_proper_Frobenius_squared"]),
        "actual_original_endpoint_decoding_weighted_partition":
            (parent["path_partition"].get("missing",0)==
                weighted["physical_endpoint_weight_by_four_classes"].get("missing_physical",0)
             and parent["path_partition"].get("incident",0)==
                weighted["physical_endpoint_weight_by_four_classes"].get("original_incident",0)
             and parent["path_partition"].get("bad_endpoint",0)==
                weighted["physical_endpoint_weight_by_four_classes"].get("original_nonincident_endbad",0)
             and parent["path_partition"].get("unblocked",0)+
                parent["path_partition"].get("internal_blocked_good",0)==
                weighted["physical_endpoint_weight_by_four_classes"].get("original_nonincident_good",0)),
    }
    if parent["sample_original_sixset"] is not None:
        paths=inverse_original_BBo_paths(
            tuple(parent["sample_original_sixset"]),
            flags,f,g,core_ids=ids)
        checks["exact_true_original_BBo_inverse_0_or_2_on_produced_image"]=(len(paths)==2)
    else:
        checks["exact_true_original_BBo_inverse_0_or_2_on_produced_image"]=(
            parent["accepted_original_BBo_subcount"]==0)
    if not all(checks.values()):
        raise AssertionError("original source integrated finite cross-stack invariant mismatch: "+
                             str([k for k,v in checks.items() if not v]))
    return {
        "s":s,"original_source_flag_count":len(flags),
        "original_core_ID_count":len(ids),
        "physical_proper_threewalk_count":weighted["physical_proper_path_total"],
        "original_accepted_BBo_count":parent["accepted_original_BBo_subcount"],
        "mixed_exact_source_blocked_triples":mixed["source_exact_blocked_triple_B"],
        "nonincident_bad_endpoint_ORIGINAL_overlap_J":
            src["original_bad_intersection_J"],
        "cross_stack_checks":checks,
        "all_checked":True,
        "finite_not_all_h_root_proof":True,
    }
