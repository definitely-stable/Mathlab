"""HYP-105 #230 AA4-BS: all-seven ORIGINAL W3 source-local Walsh covariance.

ALL genuine symplectic W(3,2^h), all h>=1, arbitrary COMPLETE
correlated typed globally injected physical f,g: disjoint WHOLE original
LINE factor-image transposition bits form a single family of full global
maps. Each REAL six-distinct-original-incidence Q depends on <=6 bits.

Its Walsh coefficient on T vanishes unless each T-swap touches at least
one TRUE original LINE factor in Q. Thus covariance of the acceptance
indicators of two original Q is zero when their touched SWAP-PAIR sets
are disjoint, even though the full source incidence system is coupled.
Classwise covariance is the exact Gram matrix of nonconstant historical
seven-GF5 source-local Fourier coefficients; selected necessary
R3-floor weighted variance has an exact positive sum-of-squares formula.

This does NOT imply initial-map S_seven>0, nor root #230 A/B/C.
The Walsh, Gram, Parseval and Poincare identities are classical, NOT
claimed original discoveries; the all-h genuine W3 coefficient counting
and W32 full seven-GF5 independently classified oracle are scoped work.
"""
from fractions import Fraction
from itertools import combinations
from math import comb

from hyp105_issue230_d6aa4ay_quenched_allD_opposite_mean import _params
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4bq_all_seven_reverse_switching import (
    validate_disjoint_factor_swaps, apply_disjoint_factor_swaps,
)
from hyp105_issue230_d6aa4br_all_seven_signed_source_flux import (
    SEVEN, immutable_original_sixflag_class,
)
from hyp105_g5e2b3e1b0_seven_signature import (
    R3_CERTIFIED_FLOORS, classify_seven_prechecked,
)
from hyp105_g5e2b3e1a_fixed_leading import selected_left_six


def true_original_line_swap_support(Q, incidences, swap_pairs, V):
    """Exact original six-incidence LINE source support on disjoint swap pairs.

    Each selected true original Q has at most 6 distinct LINE factors.
    One physical source-factor transposition pair can be "touched" by
    EITHER endpoint of the pair; shared incidence Q is NOT required.
    """
    inc=tuple(tuple(pair) for pair in incidences)
    Q=tuple(Q)
    if len(Q)!=6 or len(set(Q))!=6 or any(
        type(j) is not int or j<0 or j>=len(inc) for j in Q
    ):
        raise ValueError("six DISTINCT original incidence IDs required")
    if any(len(e)!=2 or any(type(v) is not int or not 0<=v<V for v in e)
           for e in inc):
        raise ValueError("actual typed original point/line factors required")
    pairs=validate_disjoint_factor_swaps(V,swap_pairs)
    lines={inc[j][1] for j in Q}
    mask=sum((1<<i) for i,(u,v) in enumerate(pairs) if u in lines or v in lines)
    if mask.bit_count()>len(lines) or mask.bit_count()>6:
        raise AssertionError("six true source flags hit more than six disjoint swaps")
    return mask


def all_h_true_original_source_walsh_bound(s, t):
    """Exact integer all-h UPPER on #real Q touching t disjoint LINE swap pairs.

    V=(s+1)(s^2+1), d=s+1, M=V*d original incidence flags.
    For t disjoint paired original LINE source ID swaps, any genuine Q
    sensitive to all t has >=1 actual original incidence flag on one
    of the two lines in EACH pair. Choose one witness flag per pair:
    <=(2d)^t possibilities (different line pairs -> distinct flags).
    Choose remaining 6-t distinct flags: <=binom(M-t,6-t).
    Not an estimate of physical acceptance or signed covariance.
    """
    if type(s) is not int or s<2 or s&(s-1):
        raise ValueError("genuine dyadic symplectic s>=2")
    if type(t) is not int or t<1:
        raise ValueError("nonempty Walsh subset size t>=1")
    V,a,_,_=_params(s)
    d=s+1
    M=V*d
    bound=(2*d)**t*comb(M-t,6-t) if t<=6 else 0
    total=comb(M,6)
    return {
        "s":s,"d_original_incident_flags_per_source_LINE":d,
        "V_original_LINE_factors":V,
        "M_true_original_incidence_flags":M,
        "t_disjoint_swap_pairs":t,
        "max_original_sixflag_Q_touching_ALL_t":min(total,bound),
        "maximum_abs_unweighted_nonconstant_Walsh_coefficient":
            Fraction(min(total,bound),2),
        "maximum_abs_selected_GF5_weighted_nonconstant_Walsh_coefficient":
            Fraction(max(R3_CERTIFIED_FLOORS.values())*min(total,bound),2),
        "all_true_original_six_ID_semantics":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


def unnormalized_walsh(values):
    """Walsh-Hadamard transform on full 2^m bit-mask cube, exact integers."""
    values=tuple(values)
    n=len(values)
    if not n or n&(n-1) or any(type(v) is not int for v in values):
        raise ValueError("2^m signed/integer complete cube values needed")
    w=list(values)
    step=1
    while step<n:
        for base in range(0,n,2*step):
            for i in range(step):
                a=w[base+i];b=w[base+step+i]
                w[base+i]=a+b
                w[base+step+i]=a-b
        step*=2
    return tuple(w)


def exact_individual_original_six_Q_cube(model,Q,source_line_swaps):
    """True original six-flag historical ACCEPTANCE indicator on full global cube."""
    s,V,a,inc,f,g,_,_=_original_source(model)
    pairs=validate_disjoint_factor_swaps(V,source_line_swaps)
    if len(pairs)>6:
        raise ValueError("finite individual-Q full cube <=6 pairs")
    support=true_original_line_swap_support(Q,inc,pairs,V)
    static=immutable_original_sixflag_class(Q,inc)
    values=[]
    for mask in range(1<<len(pairs)):
        swapped=apply_disjoint_factor_swaps(g,pairs,
            tuple(i for i in range(len(pairs)) if mask&(1<<i)))
        tag=classify_seven_prechecked(Q,f,swapped,inc)
        if tag is not None and tag!=static:
            raise AssertionError("one true ORIGINAL Q crossed seven positive classes")
        values.append(int(tag is not None))
    coeff=unnormalized_walsh(values)
    if any(value for T,value in enumerate(coeff) if T&~support):
        raise AssertionError("Walsh coefficient on source-factor-disjoint swap mask nonzero")
    return {
        "Q":tuple(Q),"original_source_class":static,
        "touched_source_LINE_pair_mask":support,
        "historical_G5_accepted_indicator_at_each_FULL_global_map":tuple(values),
        "unnormalized_Walsh_numerators":coeff,
    }


def exact_true_W32_seven_walsh_gram(model,source_line_swaps):
    """All 62,370 TRUE-original W32 left six-Q; exact seven-class Gram.

    State results are counts on complete original globally injected
    source maps; no independent per-Q resampling of g. Classifier is
    historical. Each Q's exact Walsh support is independently checked.
    """
    s,V,a,inc,f,g,_,_=_original_source(model)
    if (s,V,a)!=(2,15,6):
        raise ValueError("finite exact original seven-Walsh oracle needs genuine W32 K6")
    pairs=validate_disjoint_factor_swaps(V,source_line_swaps)
    m=len(pairs)
    if not 1<=m<=4:
        raise ValueError("finite full original W32 cube 1..4 disjoint swaps")
    n=1<<m
    states=tuple(apply_disjoint_factor_swaps(g,pairs,
        tuple(i for i in range(m) if mask&(1<<i))) for mask in range(n))
    rows=tuple(Q for Q,_ in selected_left_six(model))
    if len(rows)!=62370 or len(set(rows))!=62370:
        raise AssertionError("historical genuine original W32 left candidate census changed")
    counts={c:[0]*n for c in SEVEN}
    numer={c:[0]*n for c in SEVEN}
    witness_support_counts=[0]*n
    nonconstant_Q=0
    first_witnesses=[]
    for Q in rows:
        tag=immutable_original_sixflag_class(Q,inc)
        if tag is None:
            continue
        D=true_original_line_swap_support(Q,inc,pairs,V)
        vals=[]
        for h in states:
            actual=classify_seven_prechecked(Q,f,h,inc)
            if actual is not None and actual!=tag:
                raise AssertionError("genuine original Q changed historical seven GF5 tag")
            vals.append(int(actual is not None))
        for mask,v in enumerate(vals):
            counts[tag][mask]+=v
        qhat=unnormalized_walsh(vals)
        if any(v for T,v in enumerate(qhat) if T&~D):
            raise AssertionError("source Q Fourier support locality violated")
        if any(qhat[1:]):
            nonconstant_Q+=1
            if len(first_witnesses)<8:
                first_witnesses.append((Q,tag,D,tuple(vals)))
        for T,x in enumerate(qhat):
            numer[tag][T]+=x
            if not T&~D:
                witness_support_counts[T]+=1
    for c in SEVEN:
        if unnormalized_walsh(counts[c])!=tuple(numer[c]):
            raise AssertionError("all-Q localized Walsh sum != independent total counts transform")
    # Each class score, and the weighted seven-class necessary GF5 floor.
    weights=R3_CERTIFIED_FLOORS
    weighted=tuple(sum(weights[c]*counts[c][x] for c in SEVEN) for x in range(n))
    weighted_hat=unnormalized_walsh(weighted)
    covariance={}
    for c in SEVEN:
        for d in SEVEN:
            covariance[(c,d)]=Fraction(
                sum(numer[c][T]*numer[d][T] for T in range(1,n)),n*n)
            direct=Fraction(sum(counts[c][x]*counts[d][x] for x in range(n)),n)\
              -Fraction(sum(counts[c]),n)*Fraction(sum(counts[d]),n)
            if direct!=covariance[(c,d)]:
                raise AssertionError("source-local Walsh Gram != independent direct GF5 covariance")
    var=Fraction(sum(x*x for x in weighted_hat[1:]),n*n)
    direct_var=Fraction(sum(x*x for x in weighted),n)\
      -Fraction(sum(weighted),n)**2
    if var!=direct_var or var<0:
        raise AssertionError("selected true GF5 floor covariance/variance contradicts Parseval")
    poincare=Fraction(sum(T.bit_count()*weighted_hat[T]**2 for T in range(1,n)),n*n)
    direct_poincare=Fraction(sum(
        (weighted[mask]-weighted[mask^(1<<j)])**2
        for j in range(m) for mask in range(n)),4*n)
    if poincare!=direct_poincare or poincare<var:
        raise AssertionError("cube original weighted gradient/Poincare inequality fails")
    for T in range(1,n):
        if T.bit_count()>6 and weighted_hat[T]:
            raise AssertionError("all-seven six-source-flag degree bound failed")
    return {
        "m":m,"n_actual_COMPLETE_original_global_maps":n,
        "source_LINE_disjoint_transpositions":pairs,
        "genuine_original_left_sixflag_Q_count":len(rows),
        "per_vertex_all_seven_GF5_counts":
          tuple({c:counts[c][x] for c in SEVEN} for x in range(n)),
        "seven_class_Walsh_numerators":{c:tuple(numer[c]) for c in SEVEN},
        "seven_class_covariance_matrix":covariance,
        "historical_selected_GF5_floor_weighted_values":weighted,
        "historical_selected_GF5_floor_weighted_Walsh_numerators":weighted_hat,
        "weighted_original_GF5_floor_variance":var,
        "weighted_gradient_Poincare_energy":poincare,
        "strict_higher_order_gradient_energy":poincare-var,
        "TRUE_original_Q_with_nonconstant_acceptance_under_cube":nonconstant_Q,
        "first_true_original_six_Q_witnesses":tuple(first_witnesses),
        "max_number_original_six_Q_sensitive_to_each_Walsh_T":
          tuple(witness_support_counts),
        "full_original_right_image_support_unchanged":all(set(h)==set(g) for h in states),
        "original_UNCHANGED_S_lower_NOT_PROVED":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }
