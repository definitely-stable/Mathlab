"""HYP-105 issue #230 D3 — exact double-centered GQ endpoint energy.

New all-h exact algebra (for ONE globally coherent ORIGINAL W(3,s) f,g):
  B = F 1_{B_L union B_R} L^T,  D = F Inc_GQ L^T.
  D = (Delta/V) k_f k_g^T + R, k_f=F*1, k_g=L*1.
  R*1=0, 1^T*R=0, and ||R||_F^2 <= 8s(a-1)V.
  W=<B,D>=W_mean+W_center,
  W_mean=(Delta/V) sum_(q,r bad) d_f(q)d_g(r),
  W_center=<B_double_centered,R>.
  |W_center|^2 <= ||B_double_centered||_F^2 ||R||_F^2.

This does NOT establish W=o(s^(59/10)), Branch A or B, or any
universal compensation for INTERNAL-ONLY blocked three-paths.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
import json

from hyp105_issue230_projection import ProjectionClosure,fixture
from hyp105_issue230_endpoint_mixedbook_d2 import (
    _chord_ledger,original_pencil_bad_pairs,_typed_degrees,
)


def _pencil_motifs(core):
    """INDEPENDENT ORIGINAL unordered physical coordinate intersections."""
    Mf=0
    Mg=0
    for points in core.lines:
        counts=Counter(y for q in points for y in core.f[q])
        Mf+=sum(c*(c-1)//2 for c in counts.values())
    for lines in core.point_lines:
        counts=Counter(y for r in lines for y in core.g[r])
        Mg+=sum(c*(c-1)//2 for c in counts.values())
    return Mf,Mg


def _fraction_fields(q):
    return str(q.numerator)+"/"+str(q.denominator)


def double_centered_energy(model):
    core=ProjectionClosure(model)
    a=core.a
    V=core.v
    Delta=core.delta
    s=core.s
    led=_chord_ledger(core)
    original_left,original_right=original_pencil_bad_pairs(core)
    union=original_left|original_right
    Mf,Mg=_pencil_motifs(core)
    if len(original_left)!=2*s*Mf or len(original_right)!=2*s*Mg:
        raise AssertionError("bad pair cardinality != 2s ORIGINAL concurrent physical intersection count")
    if len(union)>2*s*(Mf+Mg):
        raise AssertionError("ORIGINAL bad-pair union inequality failed")
    if len(union)!=len(original_left)+len(original_right)-len(original_left&original_right):
        raise AssertionError("TRUE ORIGINAL inclusion exclusion failed")

    # Exact F*U*L^T physical four-coordinate tensor, independently
    # generated from actual ORIGINAL bad pairs rather than physical chords.
    tensor=[0]*(a*a)
    for q,r in union:
        for u in core.f[q]:
            for x in core.g[r]:
                tensor[u*a+x]+=1
    if tensor!=led["Bdeg"]:
        raise AssertionError("F * U * L^T != independent two-chord physical bad relation")

    kf=Counter(x for pair in core.f for x in pair)
    kg=Counter(x for pair in core.g for x in pair)
    if sum(kf.values())!=2*V or sum(kg.values())!=2*V:
        raise AssertionError("every physical unordered pair has exactly two coordinates")
    if any(kf[u]>a-1 or kg[u]>a-1 for u in range(a)):
        raise AssertionError("global original pair injectivity star degree exceeded")

    # Independent ORIGINAL incidence product F Inc_GQ L^T.
    dg=_typed_degrees(core)
    if dg!=led["Hdeg"]:
        raise AssertionError("physical full-G degree != true ORIGINAL incidence product")
    W=sum(b*d for b,d in zip(tensor,dg))
    if W!=led["W"]:
        raise AssertionError("four-index ORIGINAL tensor contraction != D2 W")

    # All denominators are exact integers. Scaling by V avoids floating
    # point and permits a direct pairwise row/column zero-sum audit.
    Rscaled=[V*dg[u*a+x]-Delta*kf[u]*kg[x]
             for u in range(a) for x in range(a)]
    for u in range(a):
        if sum(Rscaled[u*a+x] for x in range(a)):
            raise AssertionError("GQ spectral residual must have ZERO physical row sum")
    for x in range(a):
        if sum(Rscaled[u*a+x] for u in range(a)):
            raise AssertionError("GQ spectral residual must have ZERO physical column sum")
    # Centered direct constant term and independent original (q,r) form.
    weighted_original=sum(
        sum(kf[u] for u in core.f[q])*sum(kg[x] for x in core.g[r])
        for q,r in union)
    weighted_physical=sum(tensor[u*a+x]*kf[u]*kg[x]
                          for u in range(a) for x in range(a))
    if weighted_original!=weighted_physical:
        raise AssertionError("ORIGINAL bad-pair and physical mean contractions disagree")
    mean=Fraction(Delta*weighted_original,V)
    centered=Fraction(V*W-Delta*weighted_original,V)
    if mean+centered!=W:
        raise AssertionError("EXACT original mean + spectral correlation != actual energy")

    rows=[sum(tensor[u*a+x] for x in range(a)) for u in range(a)]
    cols=[sum(tensor[u*a+x] for u in range(a)) for x in range(a)]
    total=sum(tensor)
    if total!=4*len(union) or sum(rows)!=total or sum(cols)!=total:
        raise AssertionError("true GQ original 4-index relation mass")
    # a^2 * center(B) = a^2 B - a rowSum - a colSum + total.
    centered_Bscaled=[
        a*a*tensor[u*a+x]-a*rows[u]-a*cols[x]+total
        for u in range(a) for x in range(a)]
    for u in range(a):
        if sum(centered_Bscaled[u*a+x] for x in range(a)):
            raise AssertionError("double-centered original bad relation row sum nonzero")
    for x in range(a):
        if sum(centered_Bscaled[u*a+x] for u in range(a)):
            raise AssertionError("double-centered original bad relation col sum nonzero")
    # Because R is double-centered, each discarded additive row/column
    # component has ZERO contraction with R.
    numerator_C=sum(t*t for t in centered_Bscaled)
    numerator_R=sum(t*t for t in Rscaled)
    scaled_pair_inner=sum(b*r for b,r in zip(centered_Bscaled,Rscaled))
    if scaled_pair_inner!=a*a*(V*W-Delta*weighted_physical):
        raise AssertionError("double-centered physical bad relation changed exact spectral energy")
    # Integer-only Cauchy, equivalent to
    # ((V W - Delta S)/V)^2 <= (C2/a^4)*(R2/V^2).
    lhs=scaled_pair_inner**2
    rhs=numerator_C*numerator_R
    if lhs>rhs:
        raise AssertionError("exact centered Cauchy failed (not float)")
    # Independent moment identity: ||Bcenter||² = ||B||²
    # -sum row²/a -sum col²/a + total²/a².
    moment=Fraction(sum(z*z for z in tensor),1)
    moment-=Fraction(sum(z*z for z in rows),a)
    moment-=Fraction(sum(z*z for z in cols),a)
    moment+=Fraction(total*total,a*a)
    if moment!=Fraction(numerator_C,a**4):
        raise AssertionError("independent four-term ANOVA double-centering identity failed")
    Rnorm=Fraction(numerator_R,V*V)
    Rbound=8*s*(a-1)*V
    if Rnorm>Rbound:
        raise AssertionError("ORIGINAL GQ expander singular norm certificate failed")
    # Uniform all-h upper on mean, not strict-small energy:
    mean_cap=Fraction(4*Delta*(a-1)**2*len(union),V)
    if mean>mean_cap:
        raise AssertionError("global physical point/line star mean cap failed")
    full_Rnorm_cap=Fraction(8*s*(a-1)*V,1)
    # Is the sufficient double-centered test for W_G small proved?
    # No: a finite h check does not imply all-f,g asymptotic o.
    return {
        "s":s,"a":a,"V":V,
        "same_global_original_f_g":True,
        "complete_TRUE_original_GQ":True,
        "left_concurrent_physical_Mf":Mf,
        "true_dual_concurrent_physical_Mg":Mg,
        "left_bad_pair_count":len(original_left),
        "right_bad_pair_count":len(original_right),
        "union_bad_original_pair_count":len(union),
        "joint_bad_original_pair_count":len(original_left&original_right),
        "all_h_bad_set_cardinality_le_2s_Mf_plus_Mg":True,
        "physical_bad_relation_two_chords_per_pair":True,
        "all_h_exact_F_U_Ltranspose":True,
        "all_h_exact_F_IncGQ_Ltranspose":True,
        "physical_full_G_endpoint_energy_W":W,
        "physical_coordinate_row_degree_sums":True,
        "spectral_R_has_ZERO_row_column_sums":True,
        "double_centered_original_bad_relation_ZERO_row_column_sums":True,
        "W_mean":_fraction_fields(mean),
        "W_centered_correlation":_fraction_fields(centered),
        "W_mean_cap_original_star":_fraction_fields(mean_cap),
        "mean_original_weight_integer":weighted_original,
        "mean_physical_weight_integer":weighted_physical,
        "centered_B_Frobenius_squared":_fraction_fields(moment),
        "original_GQ_residual_R_Frobenius_squared":_fraction_fields(Rnorm),
        "original_GQ_R_squared_norm_analytic_bound":str(Rbound),
        "exact_integer_double_centered_Cauchy":lhs<=rhs,
        "double_centered_Cauchy_residual_square_numerator":lhs,
        "double_centered_Cauchy_capacity_square_numerator":rhs,
        "Cauchy_ratio_squared":_fraction_fields(Fraction(lhs,rhs) if rhs else Fraction(0)),
        "uniform_new_10pct_exponent_gain_proved":False,
        "universal_W_H_small_o_s59over10_proved":False,
        "universal_endpoint_blocking_E_small_proved":False,
        "universal_internal_only_I_small_proved":False,
        "issue230_Branch_A":"OPEN",
        "issue230_Branch_B":"OPEN",
    }


def report():
    rows=[]
    for h,schemes in ((1,("lex","reverse","S68","S72")),
                      (2,("lex","random")), (3,("random",))):
        for scheme in schemes:
            x=double_centered_energy(fixture(h,scheme))
            x["scheme"]=scheme
            rows.append(x)
    return {
        "slice":"ISSUE230-D3-DOUBLE-CENTERED-ORIGINAL-GQ-ENERGY",
        "scope":"exact ALL-h identities and finite actual W32/W34/W38, not Branch A/B",
        "original_unit_mean_P2_P7":"FALSE by coherent actual S68",
        "mean_barrier":"O(s^6) from existing M_f,M_g=O(s^4); need power saving",
        "center_barrier":"need double-centered relation Frobenius power improvement",
        "uniform_W_upper_o_s59over10":"OPEN",
        "all_h_seven_S_lower":"OPEN",
        "records":rows,
    }


if __name__=="__main__":
    print(json.dumps(report(),sort_keys=True,indent=2))
