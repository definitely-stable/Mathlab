"""HYP-105 E1-K3-F1: all-h shared-source physical-star transport certificates.

For ONE global injective physical point-map f and line-map g,
let P_xp indicate that x is an endpoint of f(p), L_yl similarly,
A_pl the ORIGINAL W(3,s) incidence matrix and D=P*A*L^T.
Write alpha=P*1 and beta=L*1. Then
    row_x(D)=2(s+1)*alpha_x,
    col_y(D)=2(s+1)*beta_y,
    sum(D)=4(s+1)*V,
and, using the NONTRIVIAL singular value sqrt(2s) of A:
    sum_xy (V*D_xy-(s+1)*alpha_x*beta_y)^2
       <= 8*s*V^3 * min(max(alpha), max(beta)).
This bound couples ALL physical stars of the one coherent map.
It does NOT establish a uniform o(s^6) mixed-book estimate or Branch A.

High-degree star counts H_k have simultaneous first-marginal and
spectral Chebyshev upper bounds. A conditional C4-weighted tail
Qstar_k <= binom(Cmax,2)*binom(H_k,2) is valid but generally slack.
"""
from fractions import Fraction
from math import comb
import json

from hyp105_g5e2b3e1k1_kikuchi_c6 import gq_pair_model, kikuchi_graph
from hyp105_g5e2b3e1k3_local_collisions import star_degree_tensor
from hyp105_g5e2b3e1k3e_weighted_codegrees import mixed_weighted_profile


def _choose2(n):
    return n*(n-1)//2 if n >= 2 else 0


def _source_stars(model):
    a=model["a"]
    V=len(model["left_labels"])
    if len(model["right_labels"])!=V:
        raise ValueError("balanced GQ(s,s) required")
    point=[0]*a
    line=[0]*a
    seen_p=set()
    seen_l=set()
    for labels, deg, seen in (
        (model["left_labels"],point,seen_p),
        (model["right_labels"],line,seen_l)
    ):
        for pair in labels:
            if len(pair)!=2 or len(set(pair))!=2:
                raise ValueError("each physical label must be a 2-element edge")
            x,y=pair
            if (type(x) is not int or type(y) is not int or
                    not 0<=x<a or not 0<=y<a):
                raise ValueError("invalid physical endpoint")
            canonical=(min(x,y),max(x,y))
            if canonical in seen:
                raise ValueError("single global source injection required")
            seen.add(canonical)
            deg[x]+=1
            deg[y]+=1
    return point,line


def source_star_transport(model, *, verify_graph=True):
    """Exact shared-star margins and all-h GQ spectral discrepancy certificate.

    Derives D_xy from ORIGINAL incidence tensor independently of Kikuchi
    adjacency. The GQ spectrum used in the inequality is proved via
    point-collinearity strongly regular parameters in the research note;
    its finite s=2,4 polynomial is independently checked by tests.

    All discrepancy comparisons are integer, no floating point epsilon.
    """
    a=model["a"]
    s=model["s"]
    V=len(model["left_labels"])
    if not all(type(x) is int and x>=2 for x in (a,s)):
        raise ValueError("valid original GQ size required")
    if V!=(s+1)*(s*s+1):
        raise ValueError("W(3,s) source point count required")
    if len(model["incidences"])!=(s+1)*V:
        raise ValueError("source GQ incidence count mismatch")
    alpha,beta=_source_stars(model)
    if sum(alpha)!=2*V or sum(beta)!=2*V:
        raise AssertionError("physical label double count")
    original=star_degree_tensor(model)
    if len(original)!=a*a:
        raise AssertionError("source tensor shape mismatch")
    if verify_graph and tuple(len(row) for row in kikuchi_graph(model))!=original:
        raise AssertionError("source vs Kikuchi degree transport mismatch")
    row=[sum(original[x*a+y] for y in range(a)) for x in range(a)]
    col=[sum(original[x*a+y] for x in range(a)) for y in range(a)]
    expected_row=[2*(s+1)*x for x in alpha]
    expected_col=[2*(s+1)*y for y in beta]
    if row!=expected_row or col!=expected_col:
        raise AssertionError("source-star exact row/column transport failure")
    N=(s+1)*V
    if sum(original)!=4*N:
        raise AssertionError("source incidence total degree transport failure")
    mean_max_num=(s+1)*max(alpha)*max(beta)
    residual_num=sum((V*original[x*a+y]-(s+1)*alpha[x]*beta[y])**2
                     for x in range(a) for y in range(a))
    spectral_upper_num=8*s*(V**3)*min(max(alpha),max(beta))
    if residual_num>spectral_upper_num:
        raise AssertionError("GQ spectral Frobenius bound violated")
    # Pointwise expander mixing, with zero-mean subset indicators:
    # |V*d_xy-(s+1)*alpha_x*beta_y|^2 <=
    #     2s * alpha_x * beta_y * (V-alpha_x)*(V-beta_y).
    worst_ratio=Fraction(0)
    for x in range(a):
        for y in range(a):
            e=V*original[x*a+y]-(s+1)*alpha[x]*beta[y]
            bound=2*s*alpha[x]*beta[y]*(V-alpha[x])*(V-beta[y])
            if e*e>bound:
                raise AssertionError("pointwise GQ expander mixing violation")
            if bound:
                worst_ratio=max(worst_ratio,Fraction(e*e,bound))
    return {
        "s":s,"V":V,"a":a,"N":N,
        "left_star_degrees":alpha,"right_star_degrees":beta,
        "max_left_star":max(alpha),"max_right_star":max(beta),
        "row_marginals":row,"column_marginals":col,
        "total_kikuchi_degree":sum(original),
        "max_observed_degree":max(original),
        "mean_max_numerator":mean_max_num,
        "mean_denominator":V,
        "residual_squared_numerator":residual_num,
        "residual_squared_denominator":V*V,
        "spectral_upper_squared_numerator":spectral_upper_num,
        "spectral_slack_ratio":str(Fraction(residual_num,spectral_upper_num))
            if spectral_upper_num else None,
        "worst_pointwise_mixing_ratio":str(worst_ratio),
        "uniform_book_saving_proved":False,
    }


def shared_star_tail_certificate(model, *, max_pairs=40_000,
                                 max_c4=40_000):
    """Joint high-source-star bound and candidate C4-weighted book cap.

    For k>=1, H_k=# {(x,y): D_xy>=k}. Exact margins give
       H_k<=sum_x min(a, floor(2(s+1)*alpha_x/k))
    and its column analogue. For k > max(mean_xy), the spectral
    Frobenius bound gives
       H_k*(k*V-(s+1)*alpha_max*beta_max)^2
         <= 8sV^3*min(alpha_max,beta_max).
    (Both estimates apply simultaneously; cap at a*a.)
    For k>=3 with Qstar_k=sum_mixed choose(c_uv,2)
             1[min(d_u,d_v,Cmax)>=k],
       Qstar_k<=choose(Cmax,2)*choose(H_k,2).
    No claim this improves the exact K3-E source-star bound.
    """
    source=source_star_transport(model)
    weighted=mixed_weighted_profile(model,max_pairs=max_pairs,max_c4=max_c4)
    a,s,V=source["a"],source["s"],source["V"]
    Cmax=weighted["Cmax_girth8"]
    alpha=source["left_star_degrees"]
    beta=source["right_star_degrees"]
    mean_max_num=source["mean_max_numerator"]
    spectral_num=source["spectral_upper_squared_numerator"]
    actual_degree=star_degree_tensor(model)
    diag=[]
    book_cap=0
    for k in range(3,Cmax+1):
        true_high=sum(int(d>=k) for d in actual_degree)
        row_upper=sum(min(a,(2*(s+1)*v)//k) for v in alpha)
        col_upper=sum(min(a,(2*(s+1)*v)//k) for v in beta)
        count_upper=min(a*a,row_upper,col_upper,4*(s+1)*V//k)
        delta_num=k*V-mean_max_num
        spectral_high_upper=None
        if delta_num>0:
            spectral_high_upper=min(a*a,spectral_num//(delta_num**2))
            count_upper=min(count_upper,spectral_high_upper)
        if true_high>count_upper:
            raise AssertionError("shared-source high-star packing failed")
        qstar=int(weighted["source_star_upper_tail"].get(str(k),0))
        qactual=int(weighted["C4_weighted_tail"].get(str(k),0))
        layer_upper=_choose2(count_upper)*_choose2(Cmax)
        if qstar>layer_upper:
            raise AssertionError("C4-weighted star-tail packing bound violated")
        per_layer=min(weighted["mixed_M2"],layer_upper)
        if qactual>qstar or qstar>per_layer:
            raise AssertionError("exact vs bounded C4-weighted tail mismatch")
        book_cap+=per_layer
        diag.append({
            "k":k,"actual_high_stars":true_high,
            "row_marginal_high_star_upper":row_upper,
            "col_marginal_high_star_upper":col_upper,
            "spectral_high_star_upper":spectral_high_upper,
            "combined_high_star_upper":count_upper,
            "actual_C4_weighted_tail":qactual,
            "source_star_C4_weighted_tail":qstar,
            "all_h_joint_tail_upper":per_layer,
        })
    if weighted["B_mixed"]>book_cap:
        raise AssertionError("joint-book upper insufficient")
    return {
        "s":s,"a":a,
        "source_transport":source,
        "B_mixed":weighted["B_mixed"],
        "B_upper_K3E_exact_source_stars":weighted["B_upper_source_star"],
        "B_upper_K3F_joint_marginals_spectrum":book_cap,
        "joint_bound_improves_K3E":book_cap<
            weighted["B_upper_source_star"],
        "C4_weighted_layers":diag,
        "all_h_seven_family_floor_proved":False,
    }


def report():
    out={"slice":"HYP-105-E1-K3-F1",
         "status":"RESTRICTED_THEOREM_C_SHARED_SOURCE_SPECTRAL",
         "seven_family_Omega_s6_proved":False,
         "models":{}}
    for power,scheme,seed in (
        (1,"lex",None),(1,"reverse-line",None),
        (2,"lex",None),(2,"random",20261011),(2,"random",230)
    ):
        m=gq_pair_model(power,scheme,seed)
        x=shared_star_tail_certificate(m)
        key="s%s-%s%s"%(m["s"],scheme,
                        "-"+str(seed) if seed is not None else "")
        # compact: full per-threshold ledger remains available to callers;
        # stdout exposes the bounds and number of useful spectral thresholds.
        layers=x["C4_weighted_layers"]
        x["thresholds_spectral_nontrivial"]=[
            w["k"] for w in layers if
            w["spectral_high_star_upper"] is not None and
            w["spectral_high_star_upper"]<a_square(m["a"])
        ]
        del x["C4_weighted_layers"]
        del x["source_transport"]["left_star_degrees"]
        del x["source_transport"]["right_star_degrees"]
        del x["source_transport"]["row_marginals"]
        del x["source_transport"]["column_marginals"]
        out["models"][key]=x
    return out


def a_square(a):
    return a*a


if __name__=="__main__":
    print(json.dumps(report(),indent=2,sort_keys=True))
