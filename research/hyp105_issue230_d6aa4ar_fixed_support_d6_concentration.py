"""HYP-105 #230 AA4-AR: fixed-both-physical-support conditional D6 concentration.

For genuine ORIGINAL symplectic W(3,s), s=2^h >=8:
- arbitrary FIXED complete globally injective original point map f;
- arbitrary FIXED set E_g of V physical unordered edges for original lines;
- one uniform GLOBAL bijection of original line factor IDs to E_g.
All source incidence flags share the same original GQ and the SAME
random global line assignment. No per-six-Q redraw.

Exact conditional mean is AA4-AQ #541; absolute overlap/cycle
codegree methods originate in parallel W2-CYC #542 and predecessors.
NEW: condition on *both* physical typed occupied support sets, not
just fixed f with full injection g random over all K_a edges.
The special r=0 correction cancels the EXACT C6(E_g) factor; missing
physical edges never have to be filled or averaged.

For all h>=3 and ALL allowed fixed E_g, f:
 Var(D6)/E[D6]^2 <= eps_exact(V,a,d,m)
 <= 1331600/a² + 162000/d³ <= 827800/s³.
In particular (from AA4-AQ E[D6]>= 2s^6/3),
 Pr(D6>=s^6/3)>=max(0,1-4 eps_exact)
 and Pr(D6>0)>=1/(1+eps_exact).
These are QUENCHED TWO-SUPPORT bounds, NOT an ALL FIXED f,g lower:
finite true W32 S68 and S72 have D6=0 despite favorable mean.

Relative-variance bounds use actual ORIGINAL sixsets (distinct six
points, lines and original incidence flag IDs), shared SOURCE line
overlap r=0..6. Delta_r<=d^6 M_r for r<6, Delta_6<=103680 d^3.
No fabricated large-h source geometry, or independent original flags.
"""
from fractions import Fraction
from math import comb, factorial, perm

from hyp105_issue230_d6aa4aq_conditional_original_D6_mean import (
    all_h_one_side_permutation_D6_theorem,
    minimal_physical_GQ_parameters,
)


def original_fixed_edges_C6_completion(a,r,c):
    """Classical exact C6 containing r given disjoint path edges;
    c path components, 1<=c<=min(r,6-r), r=1..5."""
    if not (type(a) is int and a>=6 and type(r) is int and
            1<=r<=5 and type(c) is int and
            1<=c<=min(r,6-r)):
        raise ValueError("proper simple physical C6 forest path parameters")
    return 2**(c-1)*factorial(5-r)*comb(a-r-c,6-r-c)


def max_true_original_source_C6_path_completion(a,r):
    if not(type(a) is int and a>=6 and type(r) is int
           and 1<=r<=6):
        raise ValueError("a>=6, 1<=r<=6")
    if r==6:return 1
    cap=max(original_fixed_edges_C6_completion(a,r,c)
            for c in range(1,min(r,6-r)+1))
    if a>=35:
        assert cap==perm(a-r-1,5-r)
        assert cap<=a**(5-r)
    return cap


def genuine_original_six_line_codegree_upper(d):
    """A six ORIGINAL LINE source set touches <=6d actual ORIGINAL
    POINT factors; their globally injected f images have <=6d edges.
    Every physical C6 determined by alternating three oriented edges:
    <=(2E)^3/12 cycles. Each 6-cycle allows <=6! assignments of the
    specified six ORIGINAL source line IDs to its six source points.
    """
    if type(d) is not int or d<3:
        raise ValueError("actual GQ original incidence degree >=3")
    return min(d**6,103680*d**3)


def fixed_both_support_conditional_D6_variance_certificate(s):
    """Exact Fraction all-h universal ORIGINAL source sixset overlap
    bound with ONE global random assignment of fixed LINE physical
    image support. Strict all h>=3, s=2^h >=8.

    This evaluates a rigorous upper, NOT the actual finite variance.
    The exact support-dependent mean can be higher, reducing variance.
    """
    if type(s) is not int or s<8 or s&(s-1):
        raise ValueError("genuine W(3,2^h), h>=3 only")
    V,d,a,m=minimal_physical_GQ_parameters(s)
    ref=all_h_one_side_permutation_D6_theorem(s)
    Cmin=ref["minimum_globally_occupied_C6_by_union_bound"]
    qmin=d**4*(d*d-15)
    Nmin=Cmin*qmin
    assert Cmin>0 and qmin>0 and Nmin>0
    pmin=Fraction(12*Cmin,perm(V,6))
    mean_floor=Nmin*pmin
    assert mean_floor>=Fraction(2,3)*s**6

    # Exact r=0 correction: the actual fixed physical support C6
    # count cancels from q_0/p, not replaced by full K_a cycles.
    # For disjoint original LINE source supports their six images
    # sample from the V-6 remaining occupied physical pair labels.
    disjoint_correction=Fraction(perm(V,6),perm(V-6,6))-1
    codegrees={}
    conditional={}
    terms={}
    for k in range(1,7):
        if k<6:
            physical=max_true_original_source_C6_path_completion(a,k)
            delta=d**6*physical
            qr=min(Fraction(1),Fraction(12*physical,perm(V-6,6-k)))
        else:
            delta=genuine_original_six_line_codegree_upper(d)
            qr=Fraction(1)
        codegrees[k]=delta
        conditional[k]=qr
        terms[k]=Fraction(comb(6,k)*delta,Nmin)*qr/pmin

    exact=disjoint_correction+sum(terms.values(),Fraction())
    a_d=Fraction(1331600,a*a)+Fraction(162000,d**3)
    s_upper=Fraction(827800,s**3)

    # Analytic inequalities valid a>=35, d>=9, V>=a²/3:
    #   Cmin >= a^6/30, qmin >= 22d^6/27,
    #   Nmin >= a^6*d^6/40,
    #   pmin >= (2a^6/5)/(V)_6,
    #   1/pmin <= 5a^6/128, V<=a²/2,
    #   V-11>=a²/6,
    #   q0/p-1 <= (1+36/a²)^6-1 <= 252/a² <500/a²,
    #   M_k<=a^(5-k) (k=1..5),
    # => k term <= (75/4)*C(6,k)*6^(6-k)/a²,
    #    sum k1..k5 <= 1331100/a²,
    # => all <= (1331100+500)/a²+162000/d³.
    assert a>=35 and d>=9 and V>=Fraction(a*a,3)
    assert Cmin>=Fraction(a**6,30)
    assert qmin>=Fraction(22*d**6,27)
    assert Nmin>=Fraction(a**6*d**6,40)
    assert pmin>=Fraction(2*a**6,5*perm(V,6))
    assert Fraction(1,pmin)<=Fraction(5*a**6,128)
    assert V-11>=Fraction(a*a,6)
    assert disjoint_correction<=Fraction(500,a*a)
    expected_coeffs={1:874800,2:364500,3:81000,4:10125,5:675}
    for k in range(1,6):
        assert terms[k]<=Fraction(expected_coeffs[k],a*a)
    assert terms[6]<=Fraction(162000,d**3)
    assert sum(expected_coeffs.values())==1331100
    assert Fraction(2*V,a*a)<=1
    assert Fraction(a*a,2)>=s**3
    assert 0<=exact<=a_d<=s_upper

    return {
        "s":s,"V":V,"d":d,"a":a,"missing_line_physical_pair_edges":m,
        "fixed_adversarial_point_source_map_f":True,
        "fixed_adversarial_original_line_physical_EDGE_IMAGE":True,
        "one_GLOBAL_uniform_permutation_of_ORIGINAL_line_factor_ids":True,
        "true_original_source_sixset_lower_N":Nmin,
        "per_actual_source_sixset_conditional_D6_probability_lower":
            pmin,
        "mean_original_D6_lower_from_AA4_AQ":mean_floor,
        "fixed_support_disjoint_original_LINE_overlap_correction":
            disjoint_correction,
        "six_original_line_overlap_codegrees":codegrees,
        "six_conditional_source_line_overlap_prob_upper":
            {k:str(v) for k,v in conditional.items()},
        "six_relative_variance_terms_upper":{k:str(v) for k,v in terms.items()},
        "uniform_fixed_PHYSICAL_SUPPORT_relative_variance_rational_upper":
            exact,
        "all_h_explicit_a_d_relative_variance_upper":a_d,
        "all_h_explicit_s_relative_variance_upper":s_upper,
        "Pr_one_global_assignment_D6_positive_at_least":
            Fraction(1,1+exact),
        "Pr_one_global_assignment_D6_at_least_s6_over3_at_least":
            max(Fraction(0),1-4*exact),
        "all_h_fixed_two_image_support_D6_2nd_moment_O_s_minus3":True,
        "all_two_FIXED_global_factor_MAPS_D6_lower_NOT_PROVED":True,
        "root_issue230_Branch_A_B_C_OPEN":True,
    }
