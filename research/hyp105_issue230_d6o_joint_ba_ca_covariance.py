"""HYP-105 #230 D6-O: exact B-left/A-right and C-left/A-right covariance.

Fix ANY globally injective left map f on the ORIGINAL points of W(3,s).
Let b_f(L),c_f(L) count distinct ORIGINAL 6-incidence sixsets with left
physical B/C and exactly the six distinct ORIGINAL right line IDs in L.
For each fixed globally injective right physical map g:
    U_B = sum_L b_f(L)*A_g(L),  U_C = sum_L c_f(L)*A_g(L).
Both use the SAME right A two-factor mask A_g, not independent masks.

For uniform complete right injection g, and D6-N exact universal
q_k(a)=Pr(A_g(L)=A_g(M)=1 | |L intersect M|=k), let
N_XY(k)=sum_{L,M:intersection size k} x_f(L)y_f(M) (ORDERED).
Then E[U_X U_Y]=sum_k N_XY(k)*q_k(a),
Cov(U_B,U_C)=sum_k N_BC(k)*q_k(a)-p_A**2 W_B W_C,
Var(U_B+U_C)=Var(U_B)+Var(U_C)+2Cov(U_B,U_C).
Weights 45600 / 43320 give the EXACT moment of a SELECTED
GF(5) lower numerator (not the full seven or total R3).

New exact binomial-inversion algorithm for mixed original support spectra:
Z_X(T)=sum_{L superset T}x_f(L), |T|=r<=6,
M_r(X,Y)=sum_{|T|=r} Z_X(T)Z_Y(T)
        =sum_{k=r}^6 binom(k,r)N_XY(k),
N_XY(k)=sum_{r=k}^6 (-1)**(r-k)*binom(r,k)*M_r(X,Y).
This uses 64 subsets per original six-line support and never enumerates
pairs of supports. Both equalities are all-finite-h combinatorial theorems.

All finite W32 actual oracles are GENUINE complete ORIGINAL GQ models.
Neither random-right second moment nor finite joint zeros/positivity
settles all-label Branch A or infinite correlated Branch B.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb
import json

from hyp105_issue230_d6n_exact_correlated_ca_overlap import (
    exact_right_A_overlap_kernel, _is_right_physical_A,
)
from hyp105_g5e2b3e1a_fixed_leading import (
    selected_left_six, validated_small_model,
)
from hyp105_g5e2b3e1b0_seven_signature import (
    R3_CERTIFIED_FLOORS, seven_census,
)


def original_sixline_weights_BC(model):
    """Complete W32 ORIGINAL sixset scan; B/C disjoint as left projections."""
    validated_small_model(model)
    edges = model["incidences"]
    answer = {"B": Counter(), "C": Counter()}
    for ids, kind in selected_left_six(model):
        if kind not in answer:
            continue
        lines = tuple(sorted(edges[i][1] for i in ids))
        if len(set(lines)) == 6:
            answer[kind][lines] += 1
    if not all(answer.values()):
        raise AssertionError("true original B/C positive support empty")
    return answer


def _validate_six_weights(weights, v):
    if not isinstance(weights, dict) and not isinstance(weights, Counter):
        raise ValueError("original sixline weights must be mapping")
    if type(v) is not int or v < 6:
        raise ValueError("invalid original line universe")
    canon = Counter()
    for original, w in weights.items():
        try:
            line_ids = tuple(original)
        except TypeError as exc:
            raise ValueError("non iterable original line support") from exc
        if (len(line_ids) != 6 or
                any(type(x) is not int or x < 0 or x >= v for x in line_ids)
                or len(set(line_ids)) != 6 or
                type(w) is not int or w <= 0):
            raise ValueError("requires six distinct original lines, integer weight>0")
        canon[tuple(sorted(line_ids))] += w
    return canon


def subset_extension_profile(weights):
    """Sparse 7-rank integer zeta transform; 64*|supp(weights)| updates."""
    levels = [Counter() for _ in range(7)]
    for six, multiplicity in weights.items():
        for r in range(7):
            for subset in combinations(six, r):
                levels[r][subset] += multiplicity
    return levels


def original_mixed_overlap_spectrum(weights_x, weights_y, original_line_count):
    """Exact ordered N_k via binomial inverse, no quadratic support pairs."""
    x = _validate_six_weights(weights_x, original_line_count)
    y = _validate_six_weights(weights_y, original_line_count)
    zx = subset_extension_profile(x)
    zy = subset_extension_profile(y)
    moments = [sum(v*zy[r].get(t, 0) for t,v in zx[r].items())
               for r in range(7)]
    spectrum = [
        sum((-1)**(r-k)*comb(r,k)*moments[r] for r in range(k,7))
        for k in range(7)
    ]
    wx, wy = sum(x.values()), sum(y.values())
    if (sum(spectrum) != wx*wy or
            any(n < 0 for n in spectrum) or
            spectrum[6] != sum(w*y.get(six, 0) for six,w in x.items())):
        raise AssertionError("exact mixed support spectrum conservation failed")
    return {
        "extension_binomial_moments": moments,
        "ordered_overlap_spectrum": spectrum,
        "weight_total_x": wx,
        "weight_total_y": wy,
        "common_original_sixline_support_weight_product": spectrum[6],
    }


def _moments_one_pair(w, labels, a):
    """Joint moment primitive computed with the D6-N q_k universal kernel."""
    labels = tuple(tuple(pair) for pair in labels)
    valid = set(combinations(range(a), 2))
    if (type(a) is not int or a < 6 or len(labels) > comb(a,2)
            or len(set(labels)) != len(labels)
            or any(pair not in valid for pair in labels)):
        raise ValueError("complete canonical globally injective right map required")
    canon = {t: _validate_six_weights(x, len(labels)) for t,x in w.items()}
    if set(canon) != {"B", "C"}:
        raise ValueError("exactly B and C ORIGINAL classes required")
    kernel = exact_right_A_overlap_kernel(a)
    p = kernel["single_A_probability"]
    q = kernel["joint_A_probability_by_common_original_line_count"]
    ov = {}
    moment = {}
    for x,y in (("B","B"), ("C","C"), ("B","C")):
        row = original_mixed_overlap_spectrum(
            canon[x],canon[y],len(labels))
        ov[x+y] = row
        moment[x+y] = sum((n*q[k] for k,n
                            in enumerate(row["ordered_overlap_spectrum"])),
                            Fraction())
    W = {t:sum(canon[t].values()) for t in ("B","C")}
    mean = {t:p*W[t] for t in ("B","C")}
    var = {t:moment[t+t]-mean[t]**2 for t in ("B","C")}
    cov = moment["BC"]-mean["B"]*mean["C"]
    union_mean = mean["B"]+mean["C"]
    union_second = moment["BB"]+2*moment["BC"]+moment["CC"]
    union_var = var["B"]+2*cov+var["C"]
    if (union_var != union_second-union_mean**2
            or any(t < 0 for t in var.values())
            or union_var < 0):
        raise AssertionError("exact joint second moment / variance inconsistent")
    r_B = R3_CERTIFIED_FLOORS["B-left/A-right"]
    r_C = R3_CERTIFIED_FLOORS["C/A"]
    if (r_B,r_C)!=(45600,43320):
        raise AssertionError("source GF5 seven-positive certificate changed")
    risk_mean = r_B*mean["B"]+r_C*mean["C"]
    risk_second = (r_B**2*moment["BB"]+
                   2*r_B*r_C*moment["BC"]+
                   r_C**2*moment["CC"])
    risk_var = risk_second-risk_mean**2
    if risk_var < 0:
        raise AssertionError("negative selected GF5 risk-numerator variance")
    actual = {
        kind:sum(weight for six,weight in canon[kind].items()
                 if _is_right_physical_A(six,labels))
        for kind in ("B","C")
    }
    actual_supports = {
        kind:sum(_is_right_physical_A(six,labels)
                 for six in canon[kind])
        for kind in ("B","C")
    }
    observed_numer = r_B*actual["B"]+r_C*actual["C"]
    return {
        "original_line_count":len(labels),
        "a":a,
        "B": {"original_sixsets_with_distinct_right_lines":W["B"],
              "right_random_mean":str(mean["B"]),
              "right_random_variance":str(var["B"]),
              "actual_fixed_g_directional_sixsets":actual["B"],
              "actual_fixed_g_positive_supports":actual_supports["B"]},
        "C": {"original_sixsets_with_distinct_right_lines":W["C"],
              "right_random_mean":str(mean["C"]),
              "right_random_variance":str(var["C"]),
              "actual_fixed_g_directional_sixsets":actual["C"],
              "actual_fixed_g_positive_supports":actual_supports["C"]},
        "ordered_BB_original_line_overlap":ov["BB"],
        "ordered_CC_original_line_overlap":ov["CC"],
        "ordered_BC_original_line_overlap":ov["BC"],
        "joint_BC_second_moment":str(moment["BC"]),
        "joint_BC_covariance":str(cov),
        "joint_BC_covariance_sign":(
            "positive" if cov>0 else "negative" if cov<0 else "zero"),
        "B_plus_C_right_random_mean":str(union_mean),
        "B_plus_C_right_random_second_moment":str(union_second),
        "B_plus_C_right_random_variance":str(union_var),
        "B_plus_C_random_right_P_positive_Paley_Zygmund":
            str(union_mean**2/union_second),
        "B_plus_C_actual_fixed_g":actual["B"]+actual["C"],
        "B_plus_C_actual_fixed_g_minus_mean":
            str(actual["B"]+actual["C"]-union_mean),
        "GF5_selected_positive_numerator_weights":{"B":r_B,"C":r_C},
        "GF5_selected_numerator_right_random_mean":str(risk_mean),
        "GF5_selected_numerator_right_random_variance":str(risk_var),
        "GF5_selected_numerator_right_random_second_moment":str(risk_second),
        "GF5_selected_numerator_actual_fixed_g":observed_numer,
        "GF5_selected_R3_expected_lower":str(risk_mean/(51**6)),
        "GF5_selected_numerator_P_positive_Paley_Zygmund":
            str(risk_mean**2/risk_second),
        "separate_right_random_events_are_not_independent":True,
        "right_random_positive_mean_is_not_all_g_lower":True,
        "all_h_joint_moment_formula":"EXACT-CONDITIONAL-ON-FIXED-LEFT-F",
        "Branch_A":"OPEN","Branch_B":"OPEN",
    }


def genuine_W32_joint_BC_report():
    from hyp105_issue230_projection import fixture
    cases = []
    for scheme in ("lex","reverse","S68","S72"):
        model=fixture(1,scheme)
        weights=original_sixline_weights_BC(model)
        row=_moments_one_pair(weights,model["right_labels"],model["a"])
        row["scheme"]=scheme
        full=seven_census(model,independent_checks=False)
        row["true_full_seven_S"] = full["S_seven"]
        row["true_full_seven_B_left_A_right"] = (
            full["seven_class_motif_counts"]["B-left/A-right"])
        row["true_full_seven_aggregate_C_A"] = (
            full["seven_class_motif_counts"]["C/A"])
        if (row["B"]["actual_fixed_g_directional_sixsets"] !=
                row["true_full_seven_B_left_A_right"] or
                row["C"]["actual_fixed_g_directional_sixsets"] >
                row["true_full_seven_aggregate_C_A"] or
                row["B_plus_C_actual_fixed_g"] > row["true_full_seven_S"]):
            raise AssertionError("true original GF5-positive class containment failed")
        cases.append(row)
    if (cases[0]["B"]["right_random_mean"] !=
            cases[1]["B"]["right_random_mean"] or
            cases[0]["joint_BC_covariance"] !=
            cases[1]["joint_BC_covariance"]):
        raise AssertionError("lex / reverse share the EXACT same fixed left injection")
    if [r["C"]["actual_fixed_g_directional_sixsets"] for r in cases] != [4,0,0,2]:
        raise AssertionError("D6-N original right C/A fixed-g controls changed")
    return {
        "slice":"HYP105-ISSUE230-D6O-EXACT-JOINT-BA-CA-COVARIANCE",
        "theorem":"ALL-FINITE-H-EXACT-MIXED-COVARIANCE",
        "fixed_right_all_g_identity":True,
        "uniform_right_random_only_moments":True,
        "real_complete_original_W32_seven_S_checked":True,
        "complete_W34_W38_seven_S":"NOT-CLAIMED",
        "Branch_A":"OPEN","Branch_B":"OPEN",
        "cases":cases
    }


if __name__ == "__main__":
    print(json.dumps(genuine_W32_joint_BC_report(), indent=2, sort_keys=True))
