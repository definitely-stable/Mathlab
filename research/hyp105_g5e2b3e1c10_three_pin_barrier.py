"""HYP-105 C10: all-h GQ three-pin ZERO barrier for C8 fiber relaxation.

Strengthens C9 (two pins) using the original doubled-point wedge and a
pinned THIRD original line on one of the physical singleton C4 edges.
It does NOT show existence of any right map with actual U_B/A = 0.
"""
from fractions import Fraction
from math import comb

from hyp105_g5e2b3e1c9_two_pin_barrier import (
    minimal_pair_alphabet, analytic_s_ge_64_gate,
)


def three_pin_capacity_certificate(s):
    """Uniform source support plus physically occupied target cover.

    For D of three pinned original lines, r=|R∩D|, n=V-3, m=6-r:
    any positive source sixset must contain an original GQ concurrence
    pair. If the UNIQUE distinguished original doubled-point pair lies
    inside A=R∩D, the witness case contributes at most:
      r=2: W2=3*C(a-2,4)*(s+1)^4 (C3);
      r=3: <=C(3,2)*W3, W3=2*C(a-4,2)*(s+1)^4.
    Proof for W3: choose ORIGINAL singleton q on the third fixed right
    line (<=s+1 choices), physical C4 containing f(q) (exactly
    <=2*C(a-4,2) choices), then choose remaining three ORIGINAL
    singleton right lines (<= (s+1)^3). One actual motif cannot
    contribute more than this count.

    Other concurrence pairs occur fully among unpinned or across a
    pin and unpinned line: union bounded by E*C(n-2,m-2)
    +r*d*C(n-1,m-1). A target pinned class with r=0 has at most
    T0=70*C(a,6) physical 2factors; with r>=1 it has at most
    T1=28*C(a-2,4) 2factors through any ONE pinned physical edge.
    """
    if type(s) is not int or s < 2 or s & (s-1):
        raise ValueError("s must be 2**h, h>=1")
    V=(s+1)*(s*s+1)
    a=minimal_pair_alphabet(V)
    n=V-3
    d=s*(s+1)
    E=V*d//2
    W2=3*comb(a-2,4)*(s+1)**4
    W3=2*comb(a-4,2)*(s+1)**4
    T0=70*comb(a,6)
    T1=28*comb(a-2,4)
    classes=[]
    for r in range(4):
        m=6-r
        capacity=comb(n,m)
        uncovered_by_pinned_pairs=(E*comb(n-2,m-2)
                                   +r*d*comb(n-1,m-1))
        anchored= W2 if r==2 else (3*W3 if r==3 else 0)
        target=T0 if r==0 else T1
        bound=uncovered_by_pinned_pairs+anchored+target
        classes.append({
            "r":r,"m":m, "capacity":capacity,
            "source_nonpinned_concurrence_support_upper":
                uncovered_by_pinned_pairs,
            "source_pinned_witness_support_upper":anchored,
            "physical_occupied_target_class_upper":target,
            "support_plus_target_upper":bound,
            "strict_zero_cell_slack":capacity-bound,
            "support_plus_target_ratio":Fraction(bound,capacity),
            "all_classes_relax_to_zero":bound<capacity,
        })
    return {
        "s":s,"V":V,"a":a,"n":n,
        "GQ_concurrence_edges":E,
        "GQ_line_degree":d,
        "C3_original_distinguished_pair_cap":W2,
        "C10_distinguished_pair_plus_third_line_cap_per_pair":W3,
        "physical_full_target_sixsets":T0,
        "physical_target_degree_one":T1,
        "classes":tuple(classes),
        "all_original_D_and_all_images_p":True,
        "actual_zero_overlap_map_proved":False,
    }


def analytic_s_ge_64_three_pin_gate():
    """Rational coefficient proof for EVERY s>=64, no finite extrapolation.

    V<=11/10 s^3, d<=11/10 s^2, E<=121/200 s^5,
    n,n-1>=(99/100)s^3, n-3>=(98/100)s^3,
    a^2<=4s^3. For r<=3,m=6-r, r*m<=9,m(m-1)<=30:
      concurrence ratio <19/s, crossed-pair ratio <=10/s.
    For r=2, W2/C(n,4)<77/s² (C9);
    for r=3, 3W3/C(n,3)<113/s².
    For r=0, T0/C(n,6)<163/s³ (C9 bound via C(n,4));
    for r>=1, T1/C(n,m)<119/s³ (via C(n,3)).
    Thus all ratios <29/s+113/s²+163/s³ <1 for s>=64.
    """
    c9=analytic_s_ge_64_gate()
    coeff=(
        Fraction(30)*Fraction(121,200)/Fraction(99,100)**2,
        Fraction(9)*Fraction(11,10)/Fraction(99,100),
        Fraction(24)*2*Fraction(11,10)**4/Fraction(98,100)**4,
        Fraction(3*4*6)*Fraction(11,10)**4/Fraction(98,100)**3,
        Fraction(24)*Fraction(56,9)/Fraction(98,100)**4,
        Fraction(112)/Fraction(98,100)**3,
    )
    strict=(19,10,77,113,163,119)
    # Crossed-pair coefficient is exactly 10, so <=10/s is valid.
    # Other five coefficients are strictly below their rounded caps.
    if any((a > b if i == 1 else a >= b)
           for i,(a,b) in enumerate(zip(coeff,strict))):
        raise AssertionError("three-pin symbolic rational constants fail")
    if coeff[1] != 10:
        raise AssertionError("crossed-pair sharp coefficient unexpectedly moved")
    tail=Fraction(29,64)+Fraction(113,64**2)+Fraction(163,64**3)
    if tail>=1:
        raise AssertionError("three-pin analytic tail lacks strict slack")
    return {
        "s_min":64,
        "symbolic_bound":"29/s+113/s**2+163/s**3",
        "exact_coefficients":tuple(str(v) for v in coeff),
        "tail_at_s64":tail,
        "tail_positive_slack":1-tail,
        "C9_tail_verified":c9["proves_all_real_s_at_least_64_given_parameter_bounds"],
        "uniform_all_s_ge_64":True,
    }


def all_h_three_pin_zero_barrier(s):
    """All powers >=16: base exact integers plus symbolic tail proof."""
    d=three_pin_capacity_certificate(s)
    if s<16:
        d["three_pin_zero_proved"]=False
        d["proof_scope"]="BELOW_PROVEN_THRESHOLD_NOT_DECIDED"
        return d
    if s in (16,32):
        proof="EXACT_INTEGER_BASE_CASE"
    else:
        analytic_s_ge_64_three_pin_gate()
        proof="UNIFORM_RATIONAL_ANALYTIC_TAIL"
    if any(not x["all_classes_relax_to_zero"] for x in d["classes"]):
        raise AssertionError("three-pin all-h theorem contradicted")
    d.update({
        "three_pin_zero_proved":True,
        "proof_scope":proof,
        "zero_for_every_D_with_cardinality_at_most_3":True,
        "does_NOT_prove_actual_g_zero":True,
        "does_NOT_prove_full_seven_GF5_S":True,
    })
    return d


if __name__=="__main__":
    import json
    diag=[]
    for s in (2,4,8,16,32,64,128,256,512,1024):
        d=all_h_three_pin_zero_barrier(s)
        diag.append({
            "s":s,"a":d["a"],
            "maximum_ratio":str(max(c["support_plus_target_ratio"] for c in d["classes"])),
            "zero_rearrangement_proved":d["three_pin_zero_proved"],
            "proof_scope":d["proof_scope"],
        })
    print(json.dumps({"analytic_tail":analytic_s_ge_64_three_pin_gate(),
                      "integer_diagnostics":diag},
                     indent=2,sort_keys=True,default=str))
