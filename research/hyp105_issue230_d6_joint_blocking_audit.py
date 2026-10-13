"""HYP-105 #230 D6-A: SAME-map energy / 16-atom / seven-family joint audit.

This is a finite, falsifiable diagnostic, NOT an all-h bound on S, E or I.
For W(3,2), S is the full accepted seven-family original sixset count.
For W(3,4), ONLY the genuine synchronized BB-overlap subcount is known:
using it as the full S is forbidden and explicitly rejected here.
All rows use one complete, globally injective original f,g; never independently
shuffle parts of a physical graph after constructing the original GQ.
"""
from fractions import Fraction
import json

from hyp105_issue230_anchor_blocking import anchor_ledger
from hyp105_issue230_projection import ProjectionClosure, fixture
from hyp105_issue230_endpoint_mixedbook_d2 import _chord_ledger
from hyp105_issue230_d5_retained_energy import true_spread_global_model
from hyp105_g5e2b3e1b0_seven_signature import (
    seven_census, R3_CERTIFIED_FLOORS,
)


def finite_frontier(s, blocked, seven, lam=0):
    """EXACT finite necessary eta ceiling if the o(s^6) remainder is ZERO.

    For C <= (16-eta)*s^6 + Lambda*S, rearrangement requires
    eta <= 16 - C/s^6 + Lambda*S/s^6.
    It is NOT an all-h necessary condition with an unspecified o(s^6).
    """
    if type(s) is not int or s < 2 or s & (s-1):
        raise ValueError("s must be a power of two >=2")
    if type(blocked) is not int or blocked < 0:
        raise ValueError("nonnegative exact integer blocked count required")
    if seven is None:
        raise ValueError("full seven-family S required; BB subset is insufficient")
    if type(seven) is not int or seven < 0:
        raise ValueError("full seven-family S must be a nonnegative integer")
    lam = Fraction(lam)
    if lam < 0:
        raise ValueError("nonnegative Lambda required")
    return Fraction(16) - Fraction(blocked, s**6) + lam*Fraction(seven, s**6)


def joint_record(model, scheme, *, compute_full_seven, independent_paths=True):
    """Join independently implemented ORIGINAL geometric oracles on SAME f,g."""
    core=ProjectionClosure(model)
    atoms=anchor_ledger(model, verify_middle_edges=independent_paths)
    chords=_chord_ledger(core)
    s=core.s
    c=atoms["blocked"]
    e=atoms["endpoint_bad_pair_weight"]
    i=atoms["internal_only_weight"]
    c0=atoms["unblocked"]
    mask=atoms["exact_sixteen_mask_histogram"]
    if c!=e+i or c!=sum(mask[1:]) or c0!=mask[0]:
        raise AssertionError("D6 exact E+I or 16-atom conservation failed")
    if e!=atoms["endpoint_only_weight"]+atoms["mixed_endpoint_internal_weight"]:
        raise AssertionError("D6 original endpoint union changed")
    if c0%2:
        raise AssertionError("true ORIGINAL BB-overlap reversal multiplicity is two")
    if atoms["nonincident_endpoint_complete"]!=c+c0:
        raise AssertionError("nonincident ORIGINAL path balance changed")
    if atoms["proper_P3"] != (
        atoms["missing"]+atoms["incident"]+c+c0
    ):
        raise AssertionError("all physical proper P3 states must be accounted for")
    w=chords["W"]
    if not isinstance(w,int) or w<0:
        raise AssertionError("original chord energy must be a nonnegative integer")

    full_s=None
    weighted_floor=None
    family_counts=None
    eta_lam0=None
    eta_lam1=None
    if compute_full_seven:
        if s!=2:
            raise ValueError("full seven-census is accepted only for W(3,2)")
        exact=seven_census(model, independent_checks=True)
        full_s=exact["S_seven"]
        family_counts=exact["seven_class_motif_counts"]
        weighted_floor=exact["GF5_seven_lower_numerator"]
        if sum(family_counts.values())!=full_s:
            raise AssertionError("seven true-original sixset classes must be disjoint")
        if sum(family_counts[k]*v for k,v in R3_CERTIFIED_FLOORS.items())!=weighted_floor:
            raise AssertionError("original GF5 class weights changed")
        if family_counts["B/B-overlap"]<c0//2 or full_s<c0//2:
            raise AssertionError("genuine BB-synchronized sixsets missing from seven-family count")
        eta_lam0=finite_frontier(s,c,full_s,0)
        eta_lam1=finite_frontier(s,c,full_s,1)
    elif s==2:
        raise ValueError("W32 full seven-class census must not be silently omitted")

    # The bound from D2 is E <= 24 t W + sqrt(192 |B_bad| D6).
    # 24 t W is a NONNEGATIVE sufficient upper term, not a lower bound.
    # If already >=E it yields no useful E control even when D6=0.
    t=chords["max_block"]
    if t < 0:
        raise AssertionError("negative original physical coordinate block degree")
    small_book=24*t*w
    return {
        "s":s,"a":core.a,"scheme":scheme,
        "complete_same_original_global_pair_maps":True,
        "proper_P3":atoms["proper_P3"],
        "original_endpoint_missing":atoms["missing"],
        "original_endpoint_incident":atoms["incident"],
        "nonincident_endpoint_complete":atoms["nonincident_endpoint_complete"],
        "sixteen_exact_blocking_atoms":mask,
        "E_endpoint_bad_proper_P3":e,
        "I_safe_endpoint_internal_only_proper_P3":i,
        "C_joint_blocked_proper_P3":c,
        "BB_sync_accepted_sixsets":c0//2,
        "D2_exact_bad_endpoint_energy_W":w,
        "D2_coordinate_block_t":t,
        "D2_24tW_small_book_upper_term":small_book,
        "D2_small_book_alone_is_vacuous":small_book>=e,
        "full_seven_S":full_s,
        "full_seven_counts":family_counts,
        "seven_GF5_risk_necessary_numerator":weighted_floor,
        "finite_ZERO_remainder_eta_ceiling_at_Lambda0":(
            str(eta_lam0) if eta_lam0 is not None else None),
        "finite_ZERO_remainder_eta_ceiling_at_Lambda1":(
            str(eta_lam1) if eta_lam1 is not None else None),
        "complete_W32_independent_endpoint_first_path_oracle":(
            atoms["independent_original_endpair_middle_edge_oracle"]),
        "all_h_energy_small_o_falsified_D5":True,
        "all_h_universal_seven_S_lower_PROVED":False,
        "all_h_C_compensation_PROVED":False,
        "infinite_small_S_counterexample_PROVED":False,
    }


def report():
    rows=[]
    for scheme in ("lex","reverse","S68","S72"):
        rows.append(joint_record(
            fixture(1,scheme),"W32-"+scheme,
            compute_full_seven=True,
        ))
    for mode in ("balanced","reverse"):
        model,_,_,_=true_spread_global_model(2,mode)
        rows.append(joint_record(
            model,"W34-D5-spread-"+mode,
            compute_full_seven=False,
        ))
    return {
        "slice":"ISSUE230-D6-A-COUPLED-ENERGY-BLOCKING-SEVEN-AUDIT",
        "scope":"complete W32 seven-class; W34 ONLY synchronized-BB lower, not full S",
        "mathematical_statement":"EXACT C=E+I and S>=BB_sync; finite zero-remainder eta ceiling only",
        "universal_compensation_C_upper":"OPEN",
        "conditional_small_S_W_upper":"OPEN",
        "all_h_universal_S_Omega_s6":"OPEN",
        "infinite_small_S_Branch_B":"OPEN",
        "finite_complete_same_original_labelings":rows,
    }


if __name__=="__main__":
    print(json.dumps(report(),sort_keys=True,indent=2))
