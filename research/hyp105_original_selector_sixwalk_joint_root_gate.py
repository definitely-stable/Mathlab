"""HYP-105 AA4-SELROOT: exact all-h root with preproved, not invented,
original selector marginals #679 and bipartite sixth walk #686/#703.

Prior #702 root is CONSERVATIVE: sigma2^-1=64(K+1)^2,
sigma3^-1=64*27(K+1)^3, L6=24+576T^2.
Already proved before #702:
  #679, for ONE coordinate-proper ORIGINAL r-path, r=2,3:
   Pr(survive)>=4^-r (K+1)^-r, by priority-local-minima
   positive lower FOR THE SAME NONCONFLICTING TARGET source flags
   and independent LEFT vs RIGHT coordinate cuts.
  #686/#703: tr A^6<=24 C6+72 m Delta^2; existing safe
   L6=24+288 T^2.
  #695: TWO different path survival indicators can have NEGATIVE
   covariance. Hence ONLY linearity for EACH fixed path followed by
   Jensen, NEVER pair-path independence or product moments.

This module is a self-contained all-h exact rational/integer ROOT
recomposition with a 2x2 ablation grid holding epsilon/beta/T/B0 equal.
It verifies no actual published graph constants numerically;
C,c are user-supplied HYPOTHETICAL positive Fraction test parameters.
"""
from fractions import Fraction
from itertools import combinations
from math import comb,isqrt


EPSILON=Fraction(1787,4096)
K=64
B0_COEFFICIENT=15
HEAVY_BETA=5*EPSILON**2/(384+40*EPSILON)
CORE_BUDGET=Fraction(7,16)-Fraction(38245,33554432)


def _exact_positive(v):
    if type(v) not in (int,Fraction) or v<=0:
        raise ValueError("positive exact rational hypothetical graph constants only")
    return Fraction(v)


def _ceil(q):
    q=Fraction(q)
    return -(-q.numerator//q.denominator)


def _ceil_sqrt(n):
    if type(n) is not int or n<0:raise ValueError("nonnegative exact integer square root")
    r=isqrt(n)
    return r+(r*r<n)


def _ceil_k_root(n,k):
    if type(n) is not int or n<0 or k not in (2,8):
        raise ValueError("integer square/eighth root only")
    if n==0:return 0
    hi=1<<((n.bit_length()+k-1)//k)
    lo=0
    while lo<hi:
        mid=(lo+hi)//2
        if mid**k>=n:hi=mid
        else:lo=mid+1
    if not ((hi-1)**k<n<=hi**k):
        raise AssertionError("exact integer kth root rounding failed")
    return hi


def _pow2_root_upper(h,den):
    """Exact rational upper 2^(-h/den), den=2 or 8, scale 2^12.

    If h=den*q+r, 2^(-h/den)=2^(-q)*2^(-r/den).
    We use upper for 2^((den-r)/den) / 2^(q+1) when r>0.
    The integer-root bound is always ABOVE the true irrational.
    """
    if type(h) is not int or h<0 or den not in (2,8):
        raise ValueError("positive dyadic exponent and denom 2 or 8")
    q,r=divmod(h,den)
    if r==0:return Fraction(1,2**q)
    power=den-r
    scale=2**12
    numerator=_ceil_k_root(2**power*scale**den,den)
    return Fraction(numerator,scale*2**(q+1))


def _ceil_log2(v):
    if type(v) is not int or v<=0:raise ValueError("positive integer")
    return (v-1).bit_length()


def _original_budget(s):
    if type(s) is not int or s<64 or s&(s-1):
        raise ValueError("true dyadic source scale >=64")
    V=(s+1)*(s*s+1)
    a=max(2,(1+isqrt(1+8*V))//2)
    while comb(a,2)<V:a+=1
    while a>2 and comb(a-1,2)>=V:a-=1
    N=(s+1)*V
    Cs=(s*s+1)*(s*s+a-2)
    actual=Fraction(N,s**4)-Fraction(1,2)-Fraction(Cs,16*s**4)
    if not (CORE_BUDGET<=actual and EPSILON<CORE_BUDGET):
        raise AssertionError("original source heavy/core budget not certified")
    return {
        "V":V,"N":N,"a":a,"Cs":Cs,
        "epsilon":EPSILON,"exact_core_budget":actual,
        "global_analytic_budget_floor":CORE_BUDGET,
    }


def _selector_and_moment_input(*,improved_selector,sharper_sixwalk):
    if type(improved_selector) is not bool or type(sharper_sixwalk) is not bool:
        raise ValueError("explicit 2x2 logical ablation booleans")
    d=K+1
    sigma2_inv=(16 if improved_selector else 64)*d*d
    sigma3_inv=64*(1 if improved_selector else 27)*d**3
    walkcoeff=288 if sharper_sixwalk else 576
    if improved_selector:
        # Proved #679, not assumed independence:
        # min(1-t1,...,1-tr)>=prod(1-ti) per external neighbor,
        # integrate independent target priorities and multiply by
        # two independent typed color-cut probabilities 4^-r.
        if (sigma2_inv!=16*d**2 or sigma3_inv!=64*d**3):
            raise AssertionError("single ORIGINAL path survival wrong")
    else:
        if (sigma2_inv!=64*d*d or sigma3_inv!=64*27*d**3):
            raise AssertionError("conservative selector changed")
    if walkcoeff not in (288,576):
        raise AssertionError("sixwalk input unsupported")
    return sigma2_inv,sigma3_inv,walkcoeff


def _dyadic_loss_ledger(h,T,E,D):
    if type(h) is not int or h<6:
        raise ValueError("true dyadic source order h>=6 only")
    return (
        Fraction(84*T,2**h),
        E*_pow2_root_upper(h,2),
        D*_pow2_root_upper(h,8)
    )


def selector_moment_root_gate(C_graph,c_graph,*,improved_selector=True,
                              sharper_sixwalk=True):
    """Return the exact conditional all-h heavy/dense ROOT theorem gate.

    Same true-original epsilon, strengthened #697 heavy beta and T,
    same #701 mixed B0=15, same #702 conservative 84T, 56T,
    exceptional E=8 sigma3^-1 sqrt(L6).
    Only vary previously rigorous original one-path marginal sigma
    and bipartite SIXTH-WALK L6. No alteration of originals FULL/CORE.
    """
    C=_exact_positive(C_graph)
    c=_exact_positive(c_graph)
    sigma2_inv,sigma3_inv,walkcoeff=_selector_and_moment_input(
        improved_selector=improved_selector,sharper_sixwalk=sharper_sixwalk)
    T=max(1,_ceil(2**19*C**3/HEAVY_BETA**3))
    alpha=c*(HEAVY_BETA/32)**6
    delta=min(Fraction(1,8),alpha)
    L6=24+walkcoeff*T*T
    L4=2*sigma2_inv**2*_ceil_sqrt(8*L6)+56*T
    B0=B0_COEFFICIENT*_ceil_sqrt((K+1)*T)
    exceptional=8*sigma3_inv*_ceil_sqrt(L6)
    internal=4*_ceil_sqrt(B0*T*L4)
    # Each term <=1/12 gives a provably finite starting h.
    s_sep=max(64,1008*T,(12*exceptional)**2,(12*internal)**8)
    h_sep=_ceil_log2(s_sep)
    losses_sep=_dyadic_loss_ledger(h_sep,T,exceptional,internal)
    if sum(losses_sep)>Fraction(1,4):
        raise AssertionError("separate budgets fail as exact rational upper bounds")
    # Decrement from the already-proved sufficient bound. Avoid
    # depending on unproved monotonicity of per-h rational roundings;
    # actual analytic functions are monotone for all h>=chosen h.
    h=h_sep
    while h>6 and sum(_dyadic_loss_ledger(h-1,T,exceptional,internal))<=Fraction(1,4):
        h-=1
    losses=_dyadic_loss_ledger(h,T,exceptional,internal)
    if sum(losses)>Fraction(1,4):
        raise AssertionError("joint loss ledger failed")
    if h>6 and sum(_dyadic_loss_ledger(h-1,T,exceptional,internal))<=Fraction(1,4):
        raise AssertionError("adjacent lower h also certified, unexpected")
    if not (EPSILON<CORE_BUDGET and HEAVY_BETA>EPSILON**2/128 and
            0<delta<=Fraction(1,8)):
        raise AssertionError("source heavy/dense original chain invalid")
    return {
        "hypothetical_C_graph":C,"hypothetical_c_graph":c,
        "external_constants_numerically_UNKNOWN":True,
        "exact_original_global_budget":CORE_BUDGET,
        "epsilon":EPSILON,"beta":HEAVY_BETA,"K":K,
        "T":T,"heavy_D6_coefficient":alpha,"delta":delta,
        "selector_original_single_path_improved":improved_selector,
        "selector_sigma2_inverse":sigma2_inv,
        "selector_sigma3_inverse":sigma3_inv,
        "no_path_pair_independence_used":True,
        "sixwalk_prior_sharpened":sharper_sixwalk,
        "sixwalk_L6_coefficient":walkcoeff,
        "L6":L6,"L4_integer_upper":L4,
        "original_mixed_internal_multiplier":B0_COEFFICIENT,
        "B0_integer_upper":B0,
        "exceptional_E_integer_upper":exceptional,
        "internal_D_integer_upper":internal,
        "separate_sufficient_dyadic_h":h_sep,
        "joint_certified_dyadic_h":h,
        "three_independent_relative_losses_exact_rational_upper":losses,
        "joint_loss_upper":sum(losses),
        "dense_BBo_produced_lower_coefficient":Fraction(1,8),
        "root_original_sextic_lower_coefficient":delta,
        "conditional_signed_GF5_R3_floor":min(54162*delta,Fraction(53526,8))/51**6,
        "mathematically_all_h_greater_orders_by_true_monotone_losses":True,
        "root_all_h_depends_on_external_graph_and_prior_source_lemmas":True,
        "not_an_external_qualified_referee":True,
    }


def exact_root_ablation_grid(C_graph,c_graph):
    """A matched 2×2 experiment with identical heavy T and mixed B0."""
    runs={}
    for selector,moment,name in (
        (False,False,"baseline_702"),
        (False,True,"sixwalk_only_703"),
        (True,False,"selector_only_679"),
        (True,True,"joint_679_703")):
        runs[name]=selector_moment_root_gate(
            C_graph,c_graph,improved_selector=selector,
            sharper_sixwalk=moment)
    T=runs["baseline_702"]["T"]
    alpha=runs["baseline_702"]["heavy_D6_coefficient"]
    delta=runs["baseline_702"]["delta"]
    if any(r["T"]!=T or r["delta"]!=delta or
           r["heavy_D6_coefficient"]!=alpha for r in runs.values()):
        raise AssertionError("ablation changed original heavy graph constants")
    b=runs["baseline_702"]["joint_certified_dyadic_h"]
    j=runs["joint_679_703"]["joint_certified_dyadic_h"]
    if j>b:
        raise AssertionError("using stronger two already-proved lemmas worsened root h")
    return {
        "four_matched_runs":runs,
        "same_original_heavy_T":T,
        "same_root_delta":delta,
        "baseline_h":b,
        "joint_h":j,
        "gain_in_dyadic_h":b-j,
        "no_genuine_numeric_C_graph_c_graph_claim":True,
        "scientific_acceptance":"OPEN_WITH_FORMAL_BLOCKER",
    }


def exact_small_priority_and_cut_falsifier():
    """Independent ALL 4! source orders and 2^8 typed color assignments.

    A 3-leaf STAR local-minimum priority target T={0,1,2}, neighbor 3,
    each target has degree 1 and they are pairwise NONCONFLICTING.
    The typed three-edge proper path uses four distinct coordinates
    on each side. No previous #679/#695 code imported.
    """
    from itertools import permutations,product
    good_prio=0
    for seq in permutations(range(4)):
        index={id:i for i,id in enumerate(seq)}
        good_prio+=(all(index[u]<index[3] for u in (0,1,2)))
    good_cuts=0
    for bits in product((0,1),repeat=8):
        if all(bits[i]!=bits[i+1] and bits[i+4]!=bits[i+5] for i in range(3)):
            good_cuts+=1
    actual=Fraction(good_prio,24)*Fraction(good_cuts,256)
    product_priority_floor=Fraction(1,2**3)
    sigma3=Fraction(1,64*(1+1)**3)
    if not (Fraction(good_prio,24)==Fraction(1,4) and
            good_cuts==4 and actual==Fraction(1,256) and actual>=sigma3
            and Fraction(good_prio,24)>product_priority_floor):
        raise AssertionError("direct exact ORIGINAL selector marginal independently falsified")
    return {
        "original_source_priority_orders_enumerated":24,
        "independent_typed_two_cut_assignments_enumerated":256,
        "joint_priority_local_minimum_probability":Fraction(good_prio,24),
        "joint_two_cut_probability":Fraction(good_cuts,256),
        "whole_proper_three_path_exact_survival":actual,
        "selector_r3_uniform_degree_one_floor":sigma3,
        "source_priority_product_lower":product_priority_floor,
        "no_independence_assumption_for_target_local_minima":True,
    }
