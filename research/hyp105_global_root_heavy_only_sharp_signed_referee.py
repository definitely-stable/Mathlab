"""HYP-105 AA4-ROOTSHARP: self-contained exact rational end-to-end Branch A gate.

NEW mathematical consequence of independently audited R2/R5/R6 inputs:
for every sufficiently large genuine dyadic W(3,s), every complete,
separately globally injected and arbitrarily correlated fixed f,g,

    51^6 R3(f,g) >= 54162 * delta * s^6,

where delta = min(1/8,c_graph*(beta/32)^6),
beta=5*epsilon^2/(384+40*epsilon), epsilon=1787/4096.

Unlike the previous min(54162*delta,53838/8), the dense branch CANNOT
limit the sharp asymptotic root bound. The loss ledger gives a symbolic
finite h0(C_graph) with NO assumed published numerical graph constants.

This program independently derives and verifies the quantitative
implication of historical R2-heavy, R5-core and R6-aligned inputs.
It is not an external theorem checker and never declares unknown graph
supersaturation constants numerically known. The asymptotic argument
is supplied in the accompanying proof, not inferred from finite h tests.
"""
from fractions import Fraction
from math import comb, isqrt


EPSILON=Fraction(1787,4096)
K=64
MAX_ORIGINAL_BOOK_RATIO=Fraction(6,5)
ANALYTIC_CORE_BUDGET=Fraction(7,16)-Fraction(38245,33554432)
SIGMA2_INV=16*(K+1)**2
SIGMA3_INV=64*(K+1)**3
SHARP_D6=54162
SHARP_PRODUCED_BBO=53838
GF5_PALETTE_SIX=51**6

# Exact strongest unconditional common threshold (delta<=1/8):
# 53838*(1/4-ETA_STAR) = 54162/8.
ETA_STAR=Fraction(1,4)-Fraction(SHARP_D6,8*SHARP_PRODUCED_BBO)


def _rational_positive(value):
    if type(value) not in (int,Fraction) or value<=0:
        raise ValueError("positive exact rational hypothetical graph constant required")
    return Fraction(value)


def _ceil_fraction(value):
    value=Fraction(value)
    return -(-value.numerator//value.denominator)


def _ceil_sqrt(value):
    if type(value) is not int or value<0:
        raise ValueError("nonnegative exact integer square root required")
    x=isqrt(value)
    return x+(x*x<value)


def _ceil_kroot(value,k):
    if type(value) is not int or value<0 or k not in (2,8):
        raise ValueError("exact nonnegative square/eighth integer roots only")
    if value==0:return 0
    hi=1<<((value.bit_length()+k-1)//k)
    lo=0
    while lo<hi:
        m=(lo+hi)//2
        if m**k>=value:hi=m
        else:lo=m+1
    if not (0<hi and (hi-1)**k<value<=hi**k):
        raise AssertionError("integer root upper improperly rounded")
    return hi


def _dyadic_fractional_inverse_upper(h,degree,bits=16):
    """Upper bound for true 2^(-h/degree) in exact Fraction arithmetic.

    Exponent split: h=d*q+r, remainder r>0:
     2^(-h/d)=2^((d-r)/d) / 2^(q+1).
    Numerator rounded UP as integer d-th root at scale 2^bits.
    """
    if type(h) is not int or h<0 or degree not in (2,8):
        raise ValueError("h>=0 and dyadic square/eighth inverse only")
    if type(bits) is not int or not 4<=bits<=32:
        raise ValueError("rational certificate precision must be 4..32 bits")
    q,r=divmod(h,degree)
    if not r:return Fraction(1,2**q)
    scale=1<<bits
    numerator=_ceil_kroot((1<<(degree-r))*scale**degree,degree)
    return Fraction(numerator,scale*(1<<(q+1)))


def _ceil_log2_positive(n):
    if type(n) is not int or n<=0:
        raise ValueError("positive integer for dyadic ceiling")
    return (n-1).bit_length()


def original_source_budget(h):
    """Independent source/GQ formulas, exact for true s=2^h (h>=6)."""
    if type(h) is not int or h<6:
        raise ValueError("source book/core input requires dyadic h>=6")
    s=1<<h
    v=(s+1)*(s*s+1)
    a=max(2,(1+isqrt(1+8*v))//2)
    while comb(a,2)<v:a+=1
    while a>2 and comb(a-1,2)>=v:a-=1
    n=v*(s+1)
    cs=(s*s+1)*(s*s+a-2)
    budget=Fraction(n,s**4)-Fraction(1,2)-Fraction(cs,16*s**4)
    if not (
        comb(a-1,2)<v<=comb(a,2)
        and Fraction(cs,s**4)<MAX_ORIGINAL_BOOK_RATIO
        and EPSILON<ANALYTIC_CORE_BUDGET<=budget
    ):
        raise AssertionError("true-original minimal alphabet/book/core chain invalid")
    return {
        "s":s,"V":v,"N_original_flags":n,"a_minimal":a,
        "Cs_original_pencil_book_bound":cs,
        "true_source_retention_budget":budget,
        "certified_epsilon":EPSILON,
        "sufficient_original_dense_core_physical_edges":s**4,
    }


def source_heavy_beta():
    """Derive heavy source selector retention using Cs<=6s^4/5.

    Actual heavy ORIGINAL flags L>=epsilon*s^4/2.
    Caro-Wei gives L^2/(4Cs+L) original conflict-free source flags,
    and two whole-original-flag coordinate cuts preserve >=one quarter.
    """
    half=EPSILON/2
    beta=(half**2)/(4*(4*MAX_ORIGINAL_BOOK_RATIO+half))
    if beta!=5*EPSILON**2/(384+40*EPSILON):
        raise AssertionError("true-original Caro-Wei source fraction algebra wrong")
    if not Fraction(0)<beta<Fraction(1,4):
        raise AssertionError("source selector fraction illegal")
    return beta


def _gate_inputs(C_graph,c_graph):
    """C,c are rational REGRESSION placeholders, NOT numeric paper constants.

    The real proof allows actual unknown positive reals C,c and chooses
    T>=max(1,2^19 C^3/beta^3), with root radicals defined continuously.
    """
    C=_rational_positive(C_graph)
    c=_rational_positive(c_graph)
    beta=source_heavy_beta()
    T=max(1,_ceil_fraction((2**19*C**3)/beta**3))
    delta=min(Fraction(1,8),c*(beta/32)**6)
    if not 0<delta<=Fraction(1,8):
        raise AssertionError("source heavy D6 lower coefficient not positive")
    l6=24+288*T*T
    l4=2*SIGMA2_INV**2*_ceil_sqrt(8*l6)+56*T
    b0=15*_ceil_sqrt((K+1)*T)
    E=8*SIGMA3_INV*_ceil_sqrt(l6)
    D=4*_ceil_sqrt(b0*T*l4)
    return {
        "hypothetical_C_graph":C,"hypothetical_c_graph":c,
        "beta":beta,"T":T,"delta":delta,
        "sigma2_inverse":SIGMA2_INV,
        "sigma3_inverse":SIGMA3_INV,
        "sixwalk_bound_L6":l6,
        "fourwalk_bound_L4_integer_upper":l4,
        "mixed_original_blocker_B0_integer_upper":b0,
        "exceptional_E_integer_upper":E,
        "four_internal_D_integer_upper":D,
    }


def relative_dense_loss_upper(h, gate, *,bits=16):
    """Exact rational upper of historical R2/R5 dense path loss / 2.

    U_produced/s^6 >= 1/4
       -42T/2^h -(E/2)/2^(h/2) -(D/2)/2^(h/8).
    """
    if type(h) is not int or h<6:
        raise ValueError("h>=6 needed for ALL historical source bounds")
    T=gate["T"]
    E=gate["exceptional_E_integer_upper"]
    D=gate["four_internal_D_integer_upper"]
    return (
        Fraction(42*T,1<<h),
        Fraction(E,2)*_dyadic_fractional_inverse_upper(h,2,bits),
        Fraction(D,2)*_dyadic_fractional_inverse_upper(h,8,bits)
    )


def _separate_sufficient_h(gate,eta):
    """Construct direct analytic h bound, then repair rational root rounding."""
    eta=_rational_positive(eta)
    if eta>Fraction(1,4):
        raise ValueError("dense positive branch error allowance <=1/4")
    T=gate["T"];E=gate["exceptional_E_integer_upper"];D=gate["four_internal_D_integer_upper"]
    side=max(
        64,
        _ceil_fraction(Fraction(126*T,1)/eta),
        _ceil_fraction((Fraction(3*E,2)/eta)**2),
        _ceil_fraction((Fraction(3*D,2)/eta)**8),
    )
    h=_ceil_log2_positive(side)
    while sum(relative_dense_loss_upper(h,gate))>eta:
        h+=1
    return h


def _sharp_sufficient_h(gate,eta):
    h=_separate_sufficient_h(gate,eta)
    # No unjustified monotonicity of the rounded *upper fractions*:
    # the underlying true analytic error is decreasing in h. A witness
    # at this h certifies every larger true order by analytic monotonicity.
    while h>6 and sum(relative_dense_loss_upper(h-1,gate))<=eta:
        h-=1
    if sum(relative_dense_loss_upper(h,gate))>eta:
        raise AssertionError("conservative exact upper fails")
    return h


def whole_root_certificate(C_graph,c_graph):
    """Complete all-branch arithmetic implication, conditional on named lemmas."""
    gate=_gate_inputs(C_graph,c_graph)
    if not (ETA_STAR>0 and
            SHARP_PRODUCED_BBO*(Fraction(1,4)-ETA_STAR)
            ==Fraction(SHARP_D6,8) and
            gate["delta"]<=Fraction(1,8)):
        raise AssertionError("new heavy-only root reduction algebra invalid")
    h_old=_sharp_sufficient_h(gate,Fraction(1,8))
    h_new=_sharp_sufficient_h(gate,ETA_STAR)
    assert h_new>=h_old
    losses=relative_dense_loss_upper(h_new,gate)
    if sum(losses)>ETA_STAR:
        raise AssertionError("new symbolic sharp all-branch gate not certified")
    dense_coefficient_lower=SHARP_PRODUCED_BBO*(Fraction(1,4)-sum(losses))
    heavy_coefficient=SHARP_D6*gate["delta"]
    if dense_coefficient_lower<heavy_coefficient:
        raise AssertionError("dense branch limits what must be heavy-only root")
    return {
        **gate,
        "standalone_original_source_all_h_budget":ANALYTIC_CORE_BUDGET,
        "required_heavy_T_formula":"T >= 2^19 C_graph^3 / beta^3",
        "external_graph_constants_numeric_are_UNKNOWN":True,
        "old_dense_one_eighth_sufficient_h":h_old,
        "new_heavy_only_sufficient_h":h_new,
        "new_dense_loss_target":ETA_STAR,
        "exact_relative_loss_upper_at_h":losses,
        "exact_dense_U_coefficient_lower_at_h":Fraction(1,4)-sum(losses),
        "heavy_D6_coefficient":gate["delta"],
        "signed_D6_numerator":SHARP_D6,
        "signed_aligned_produced_BBo_numerator":SHARP_PRODUCED_BBO,
        "signed_GF5_palette_denominator":GF5_PALETTE_SIX,
        "sharp_full_root_R3_coefficient":Fraction(SHARP_D6,GF5_PALETTE_SIX)*gate["delta"],
        "uniform_all_h_above_h_certificate":True,
        "all_h_depends_on_historical_original_root_and_published_graph_SS6":True,
        "scientific_acceptance":"OPEN_WITH_FORMAL_BLOCKER",
        "not_deterministic_GF5_assignment_theorem":True,
        "not_an_unconditional_numerical_graph_constant":True,
    }


def finite_h_full_root_lower(h,C_graph,c_graph):
    """Nonnegative explicit ALL-h (h>=6) same-f/g bound, even below root h0.

    If D6>=delta*s^6, use signed 54162*D6; otherwise the dense
    original THREE-owner count gives the nonnegative clipped lower.
    No REAL numerical c/C is asserted by this calculator.
    """
    gate=_gate_inputs(C_graph,c_graph)
    losses=relative_dense_loss_upper(h,gate)
    dense=max(Fraction(0),Fraction(1,4)-sum(losses))
    combined=min(SHARP_D6*gate["delta"], SHARP_PRODUCED_BBO*dense)
    if combined<0:
        raise AssertionError("negative nonnegative original risk floor")
    return {
        "h":h,
        "T":gate["T"],
        "delta":gate["delta"],
        "loss_terms_exact_upper":losses,
        "dense_original_BBo_relative_lower":dense,
        "full_original_signed_R3_relative_lower":combined/GF5_PALETTE_SIX,
        "zero_floor_is_allowed_for_finite_h_below_symbolic_h0":dense==0,
    }


if __name__=="__main__":
    import json
    # The values 1,1 are REGRESSION placeholders and never sourced
    # numeric values of the published C6 supersaturation theorem.
    r=whole_root_certificate(Fraction(1),Fraction(1))
    print(json.dumps({
        "WARNING":"ILLUSTRATIVE C_graph=c_graph=1, not verified paper constants",
        "T":str(r["T"]),"delta":str(r["delta"]),
        "previous_h":r["old_dense_one_eighth_sufficient_h"],
        "new_heavy_only_h":r["new_heavy_only_sufficient_h"],
        "new_dense_loss_target":str(r["new_dense_loss_target"]),
        "sharp_R3_floor_coefficient":str(r["sharp_full_root_R3_coefficient"]),
        "acceptance":r["scientific_acceptance"]
    },indent=2))
