"""HYP-105 #230 D6-M: EXACT all-h GQ collinearity-profile C/A transfer.

This is an ORIGINAL geometric/GF5-positive sixset theorem, NOT another
Hall network. Fix ANY globally injective point-pair map f for W(3,s).
Right line-pair map g is drawn uniformly over all injections into K_a.

An original left C sixset selects exactly 3 distinct original points
p1,p2,p3 with pairwise disjoint physical coordinate pairs f(p_i), and
chooses exactly 2 distinct original incidence-lines at each point.
Its right original lines are distinct according solely to the induced
collinearity type of the three original points in the TRUE GQ:

  zero collinear pairs:       B^3
  one:                       B^3-A^2*B
  two (distinct lines):      B^3-2*A^2*B+A^2
  three (one common line):   Z^3+3*A*Z^2

B=binom(d,2), A=d-1, Z=binom(d-1,2), d=s+1. The GQ axiom excludes
triangles of pairwise-collinear points on three distinct lines.

For six distinct right original factor lines, a uniformly random
injective g creates the right physical A 2-factor on six physical
symbols with probability

    p_A = 6!*70*binom(a,6)/(binom(a,2))_6,

independent of f, right factor identity, or the complete remaining
right labeling. Every such C-left/A-right is a previously CERTIFIED positive GF5
seven-class ORIGINAL sixset, counted once; the preexisting aggregate
"C/A" GF5 tag also includes A-left/C-right and MUST NOT be identified
with this directional expectation. Therefore

    E_g[U_C-left/A-right | f] =
      p_A sum_{disjoint physical f-point triples}Phi_d.

This is EXACT for EVERY finite h and EVERY left f, not a fixed-g lower.
A uniform all-h lower is
  E_g U_C/A >= p_A*T_C_lower*Phi_min,
with Phi_min=Z^3+3*A*Z^2. Also refined GQ-specific lower
  p_A*[T_C_lower B^3 - A^2*B * P_coll*(V-2)]_+
where P_coll=V*s*(s+1)/2 exact ORIGINAL collinear point-pairs.
Both give (35/3+o(1))*s^6, NOT inf_g S=Omega(s^6).

No complete-seven W34/W38 targets, no Branch A/B, no new ASET exponent.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb, factorial
import json

from hyp105_g5e2b3e1b1a_one_sided import left_six_mass, uniform_right_completion_BA
from hyp105_issue230_projection import ProjectionClosure, fixture


def _choose(n,k):
    return comb(n,k) if n>=k>=0 else 0


def _falling(n,k):
    result=1
    for j in range(k):
        result*=n-j
    return result


def exact_three_point_phi(s):
    """Four true GQ 3-point collinearity orbit-type lift polynomials."""
    if type(s) is not int or s<2 or s&(s-1):
        raise ValueError("W(3,s) requires s=2^h, h>=1")
    d=s+1
    B=comb(d,2)
    A=d-1
    Z=comb(d-1,2)
    phi={
        "0-noncollinear":B**3,
        "1-collinear-pair":B**3-A*A*B,
        "2-collinear-path":B**3-2*A*A*B+A*A,
        "3-collinear-same-line":Z**3+3*A*Z*Z,
    }
    if not (0<=phi["3-collinear-same-line"]<=phi["2-collinear-path"]
            <=phi["1-collinear-pair"]<=phi["0-noncollinear"]):
        raise AssertionError("exact all-h GQ collinearity type ordering failed")
    return {
        "s":s,"point_incidence_degree_d":d,
        "two_different_lines_per_point_B":B,
        "line_inclusion_choices_A":A,
        "line_exclusion_choices_Z":Z,
        "six_distinct_right_original_lines_by_type":phi,
        "phi_min_all_original_GQ_point_triples":phi["3-collinear-same-line"],
        "true_GQ_no_nonconcurrent_point_triangle":True,
    }


def exact_right_A_probability(s):
    """Exact uniform random injective original line-pair labeling probability."""
    one=left_six_mass(s)
    a=one["a"]
    K=one["K"]
    favourable=factorial(6)*70*comb(a,6)
    total=_falling(K,6)
    if not 0<favourable<=total:
        raise AssertionError("right factor physical 2-factor probability invalid")
    return Fraction(favourable,total)


def universal_fixed_left_CA_expectation(s):
    """ALL-h all-left-f coefficient with exact rational bounds, NOT fixed-g."""
    one=left_six_mass(s)
    V=one["V"]
    nC=one["physical_pattern_bounds"]["lower"]["C"]
    upper_C=one["physical_pattern_bounds"]["full"]["C"]
    phi=exact_three_point_phi(s)
    B=phi["two_different_lines_per_point_B"]
    A=phi["line_inclusion_choices_A"]
    phi_min=phi["phi_min_all_original_GQ_point_triples"]
    probability=exact_right_A_probability(s)
    # A genuine GF5-positive seven-class different from C/A was already
    # proved by E1-B1A. The two accepted classes are disjoint ORIGINAL
    # sixsets, so expectations ADD on the SAME random right g.
    BA=uniform_right_completion_BA(s)
    # Exact GQ point collinearity: every original point is collinear with
    # s*(s+1) other points, because s+1 lines each contain s others.
    if V*s*(s+1)%2:
        raise AssertionError("GQ collinearity incidence count not integral")
    P=V*s*(s+1)//2
    naive_lower=nC*phi_min
    # For each original collinear point pair at most V-2 possible third
    # original points. Pairwise-disjoint physical f labels can only remove
    # triples, never create collinear pairs.
    refined_num=max(0,nC*B**3-A*A*B*P*(V-2))
    safe_lower=max(naive_lower,refined_num)
    upper=upper_C*B**3
    if not 0<=safe_lower<=upper:
        raise AssertionError("all-left C/A expectation bounds malformed")
    return {
        "s":s,"a":one["a"],"V_original_factor_points":V,
        "d_GQ_original_degree":s+1,
        "missing_left_physical_pairs":one["missing"],
        "full_physical_C_templates":upper_C,
        "uniform_lower_physical_C_templates":nC,
        "exact_original_collinear_point_pairs_P":P,
        "phi":phi,
        "exact_right_random_A_probability":str(probability),
        "naive_C_lifts_with_distinct_right_lines_floor":naive_lower,
        "refined_GQ_pair_collinearity_C_lifts_floor":refined_num,
        "uniform_C_lifts_lower":safe_lower,
        "uniform_C_lifts_upper":upper,
        "uniform_expected_Cleft_Aright_lower":str(safe_lower*probability),
        "previous_B_left_A_right_expected_lower":str(
            BA["expected_U_Bleft_Aright_lower"]),
        "new_joint_disjoint_BA_plus_CA_expected_lower":str(
            safe_lower*probability+BA["expected_U_Bleft_Aright_lower"]),
        "new_joint_disjoint_BA_plus_CA_expected_lower_over_s6":str(
            Fraction(safe_lower*probability+
                     BA["expected_U_Bleft_Aright_lower"],s**6)),
        "new_asymptotic_BA_plus_CA_mean_coefficient":"455/3",
        "uniform_expected_Cleft_Aright_upper":str(upper*probability),
        "uniform_expected_Cleft_Aright_lower_over_s6":str(Fraction(
            safe_lower*probability,s**6)),
        "new_asymptotic_fixed_left_C_A_mean_coefficient":"35/3",
        "uniform_over_ALL_globally_injective_fixed_left_f":True,
        "right_g_uniform_random_injection_ONLY":True,
        "expected_GF5_subclass_orientation":"C-left/A-right-ONLY",
        "aggregate_GF5_tag_C_over_A_includes_both_orientations":True,
        "all_g_or_root_Branch_A_proved":False,
        "infinite_correlated_Branch_B_counterexample_proved":False,
    }


def _collinearity_type(point_lines, triple):
    """Classify genuine GQ 3-point pattern, excluding fake GQ triangles."""
    p,q,r=triple
    pq=point_lines[p]&point_lines[q]
    pr=point_lines[p]&point_lines[r]
    qr=point_lines[q]&point_lines[r]
    if any(len(x)>1 for x in (pq,pr,qr)):
        raise AssertionError("true ORIGINAL GQ point-pair codegree >1")
    hits=sum(bool(x) for x in (pq,pr,qr))
    if hits==3:
        if len(pq&pr&qr)!=1:
            raise AssertionError("GQ forbids nonconcurrent three-point triangle")
    return (
        "0-noncollinear","1-collinear-pair","2-collinear-path",
        "3-collinear-same-line"
    )[hits]


def exact_fixed_left_CA_profile(model):
    """TRUE original W32/W34 original point/line collinearity profile.

    Counts physical C template triples directly from global left f,
    independent of the full seven-family classifier, then exact GQ line
    choices and the random right injection expectation. W38 intentionally
    not instantiated: combinatorial triple enumeration can be costly.
    """
    core=ProjectionClosure(model)
    s=core.s
    if s not in (2,4):
        raise ValueError("actual finite true GQ profile limited to W32/W34")
    phi=exact_three_point_phi(s)[
        "six_distinct_right_original_lines_by_type"]
    images=[frozenset(pair) for pair in core.f]
    pts=tuple(frozenset(ls) for ls in core.point_lines)
    types=Counter()
    disjoint_collinear_pairs=Counter()
    for p in range(core.v):
        for q in range(p+1,core.v):
            if images[p].isdisjoint(images[q]):
                for r in range(q+1,core.v):
                    if images[p].isdisjoint(images[r]) and images[q].isdisjoint(images[r]):
                        kind=_collinearity_type(pts,(p,q,r))
                        types[kind]+=1
    nC=sum(types.values())
    expected_template_upper=15*comb(core.a,6)
    if nC>expected_template_upper:
        raise AssertionError("true ORIGINAL left physical C templates overcount")
    right_distinct=sum(types[k]*phi[k] for k in phi)
    exact=Fraction(right_distinct)*exact_right_A_probability(s)
    universal=universal_fixed_left_CA_expectation(s)
    if not (Fraction(universal["uniform_expected_Cleft_Aright_lower"])
            <=exact<=Fraction(universal["uniform_expected_Cleft_Aright_upper"])):
        raise AssertionError("true GQ C/A expectation violated ALL-h inequality")
    return {
        "scheme":model.get("scheme","unknown"),
        "s":s,"a":core.a,"V":core.v,"original_GQ_incidences":len(core.edges),
        "true_complete_global_left_pair_injection":True,
        "true_complete_global_right_pair_injection":True,
        "physical_left_C_matching_point_triples":nC,
        "left_C_collinearity_original_point_triples_by_type":{
            k:types[k] for k in phi
        },
        "exact_left_C_sixsets_with_six_distinct_original_right_lines":
            right_distinct,
        "exact_expected_g_random_Cleft_Aright":str(exact),
        "exact_expected_g_random_Cleft_Aright_over_s6":str(Fraction(exact,s**6)),
        "universal_lower_expected_Cleft_Aright":universal["uniform_expected_Cleft_Aright_lower"],
        "universal_upper_expected_Cleft_Aright":universal["uniform_expected_Cleft_Aright_upper"],
        "all_h_mathematical_mean_formula":"PROVED-ALL-FINITE-H",
        "actual_fixed_global_right_g_Cleft_Aright":None,
        "expected_GF5_subclass_orientation":"C-left/A-right-ONLY",
        "all_right_g_lower_proved":False,
    }


def report():
    # This report is a genuinely ORIGINAL full-GQ census of C left
    # templates. For s4, it gives an EXACT random-right expectation
    # WITHOUT inventing a full seven-positive W34/W38 target pool.
    actual=[]
    for power, schemes in ((1,("lex","reverse","S68","S72")),
                           (2,("lex","random"))):
        for scheme in schemes:
            model=fixture(power,scheme)
            row=exact_fixed_left_CA_profile(model)
            row["scheme"]=scheme
            actual.append(row)
    return {
        "slice":"HYP105-ISSUE230-D6M-EXACT-GQ-COLLINEARITY-CA-TRANSFER",
        "all_h_exact_fixed_left_random_right_CA_expectation":
            "PROVED-ONE-SIDED-RANDOM-RIGHT",
        "all_h_uniform_expected_Cleft_Aright_coefficient":"35/3",
        "all_h_uniform_expected_BA_plus_CA_coefficient":"455/3",
        "right_model":"UNIFORM-INJECTION-G-CONDITIONAL-ON-ANY-LEFT-F",
        "new_C_A_mean_scope":"C-left/A-right-ONLY-not-aggregate-C/A",
        "full_seven_S_for_W34_W38":"UNKNOWN-NO-BB-SUBSTITUTION",
        "all_h_for_EVERY_correlated_global_f_g":"OPEN",
        "root_Branch_A_or_B":"OPEN",
        "real_complete_GQ_fixed_left_profiles":actual,
        "exact_all_h_rational_bound_checks":[
            universal_fixed_left_CA_expectation(s)
            for s in (2,4,8,16,32,64,128)
        ],
    }


if __name__=="__main__":
    print(json.dumps(report(),indent=2,sort_keys=True))
