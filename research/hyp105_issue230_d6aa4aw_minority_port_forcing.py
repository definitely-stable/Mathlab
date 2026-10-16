"""HYP-105 #230 AA4-AW — exact source-original two-type MINORITY PORT
forcing, true GQ source incidence flags & single globally fixed f,g.

All-h local deterministic 2x2 nonnegative integer fact:
 X=[a,b;c,d] are four actual GOOD D-neighbor original source-flag
 counts by the TWO endpoint coordinates of a fixed original point
 physical factor f(p) and independently TWO endpoint coordinates
 of its incident original line physical factor g(l).
 Row marginals r0=a+b,r1=c+d are point-typed physical ports.
 Col marginals c0=a+c,c1=b+d are line-typed physical ports.
 Let k=min(r0,r1), ell=min(c0,c1), m=min(k,ell).
 Number R=a*d+b*c of two-typed OPPOSITE GOOD source 3flag wedges:
   R >= k*ell - floor(m*m/2) >= k*ell/2.
   R>0 IFF k>0 and ell>0, no two-map independence needed.
 The first bound is SHARP for k=ell even with all X=m/2, and
 R_min for exact four fixed marginals is found by optimizing the
 convex quadratic on the 2x2 transportation interval (integer).

This reduces the ALL-GLOBAL two-type opposite-port survival gate
to simultaneous NONZERO single-side margins; no unconditional
minority-port product mass has yet been proven for every f,g.

Combined CONDITIONAL quantitative gate:
 all-h h>=16 AA4-AV source-AA GOOD mass >=s6/10 implies
 sum_i GOOD degrees squared >=s6/5.
 If sum_i k_i*ell_i >= alpha*sum_i deg(i)^2 (UNPROVED for ALL f,g)
 then R_good >=alpha*s6/10.
 If in addition beta-fraction of these R_good distinct wedges lies
 in accepted true-original seven-GF5 six-source-ID Q (UNPROVED),
 the existing at-most-6 per-Q charge yields
        S_s(f,g) >= alpha*beta*s6/60.
 No claim of unconditional original S>=c*s6 or true Hall positivity.
"""
from collections import Counter
from fractions import Fraction

from hyp105_issue230_d6aa4ar_good_wedges_port_balance import (
    _good_D_edge_graph,exact_true_original_good_D_two_port_wedge_certificate)
from hyp105_issue230_d6aa4av_global_source_aa_good_wedges import (
    exact_true_original_good_D_source_multiplicity_partition,
    universal_original_AA_good_wedge_lower)


def _validate_four_good_source_port_bins(bins):
    try:
        x=tuple(bins)
    except TypeError as exc:
        raise ValueError("four literal nonnegative integer original port bins") from exc
    if len(x)!=4 or any(type(z)!=int or z<0 for z in x):
        raise ValueError("four nonnegative integer original port bins required")
    return x


def exact_two_type_integer_port_marginal_minimum(bins):
    """SHARP integer lower among ALL 2x2 matrices with SAME margins.

    This sharp minimum is a combinatorial inequality (not a
    realization theorem for arbitrary actual original symplectic
    global physical f,g), proved by feasible t=x00 integer interval
    and convex quadratic t*x11+x01*x10.
    """
    a,b,c,d=_validate_four_good_source_port_bins(bins)
    n=a+b+c+d
    r0,r1=a+b,c+d
    c0,c1=a+c,b+d
    k=min(r0,r1)
    ell=min(c0,c1)
    m=min(k,ell)
    lower_t=max(0,r0+c0-n)
    upper_t=min(r0,c0)
    if lower_t>upper_t:
        raise AssertionError("actual two-type margins cannot yield empty 2x2 transport")
    def value(t):
        return t*(n-r0-c0+t)+(r0-t)*(c0-t)
    # vertex t_star = (2*r0+2*c0-n)/4, EXACT integer arithmetic
    vertex_num=2*r0+2*c0-n
    floor_t=vertex_num//4
    ceil_t=-((-vertex_num)//4)
    candidates={lower_t,upper_t,
                min(upper_t,max(lower_t,floor_t)),
                min(upper_t,max(lower_t,ceil_t))}
    sharp_min=min(value(t) for t in candidates)
    sharp_max=max(value(lower_t),value(upper_t))
    real=a*d+b*c
    exact_minor_floor=k*ell-(m*m//2)
    if not (0<=exact_minor_floor<=sharp_min<=real<=sharp_max):
        raise AssertionError("exact source 2x2 port integer marginal-minimax ordering")
    if (real>0)!=(k>0 and ell>0):
        raise AssertionError("same-global-source two-typed opposite wedge local positivity iff both one-sided port supports")
    # AA4-AR diagonal polarization simplifies to two one-sided
    # marginal contrasts, with an independent residual parity term.
    point_contrast=r0-r1
    line_contrast=c0-c1
    diagonal_contrast=a+d-b-c
    if 8*real!=n*n+diagonal_contrast**2-point_contrast**2-line_contrast**2:
        raise AssertionError("one-sided marginals exact polarization")
    return dict(
        literal_2by2_original_source_good_port_bins=(a,b,c,d),
        original_good_D_source_flag_degree=n,
        point_port_marginals=(r0,r1),
        line_port_marginals=(c0,c1),
        minor_point_port=k,
        minor_line_port=ell,
        source_good_two_typed_opposite_wedges=real,
        sharp_integer_minimum_OPPOSITE_for_fixed_point_line_marginals=sharp_min,
        sharp_integer_maximum_OPPOSITE_for_fixed_point_line_marginals=sharp_max,
        all_margins_minority_lower=k*ell-m*m//2,
        half_minor_product_lower=Fraction(k*ell,2),
        both_one_sided_point_line_ports_nonempty=(k>0 and ell>0),
        exact_original_two_typed_port_positivity_IFF_both_marginals_nonzero=True,
        point_one_sided_contrast=point_contrast,
        line_one_sided_contrast=line_contrast,
        full_two_type_diagonal_contrast=diagonal_contrast,
        gamma_delta_exact_one_sided_polarization=True,
        arbitrary_physical_source_GQ_realizability_of_minimax_NOT_CLAIMED=True,
    )


def exact_true_original_good_minority_port_certificate(model):
    """FULL genuine original-source GOOD D graph, same global typed f/g.

    Source-first four port bins on EVERY real source point-line flag.
    Compute sum_i k_i ell_i; prove exact real opposite wedge support
    and both sharp fixed marginal and universal minority lower.
    Separately independent original source AA good wedge population.
    """
    G,good,neighbors,badP,badL=_good_D_edge_graph(model)
    inc,left,right=G["inc"],G["left"],G["right"]
    per=[]
    categories=Counter()
    sum_minprod=0
    sum_minorbound=0
    sum_sharp=0
    observed_R=0
    deg2=0
    for i,(p,l) in enumerate(inc):
        point={c:j for j,c in enumerate(sorted(left[p]))}
        line={e:j for j,e in enumerate(sorted(right[l]))}
        x=[0,0,0,0]
        for j,cp,cl in neighbors[i]:
            if cp not in point or cl not in line:
                raise AssertionError("actual original D edge shared physical color not center endpoint")
            x[2*point[cp]+line[cl]]+=1
        z=exact_two_type_integer_port_marginal_minimum(x)
        per.append(z)
        categories[("two_point_ports" if z["minor_point_port"] else "one_point_port",
                    "two_line_ports" if z["minor_line_port"] else "one_line_port")]+=1
        sum_minprod+=z["minor_point_port"]*z["minor_line_port"]
        sum_minorbound+=z["all_margins_minority_lower"]
        sum_sharp+=z["sharp_integer_minimum_OPPOSITE_for_fixed_point_line_marginals"]
        observed_R+=z["source_good_two_typed_opposite_wedges"]
        deg2+=z["original_good_D_source_flag_degree"]**2
    old=exact_true_original_good_D_two_port_wedge_certificate(model)
    if observed_R!=old["good_D_original_OPPOSITE_TWO_TYPED_port_wedges"]:
        raise AssertionError("true original all-port bin and earlier independent AA4-AR GOOD opposite Q disagree")
    if deg2!=old["true_original_good_D_degree_squared_energy"]:
        raise AssertionError("true original GOOD source degree^2")
    if not (Fraction(sum_minprod,2)<=sum_minorbound<=sum_sharp<=observed_R):
        raise AssertionError("all-global original minority-port exact lower chain")
    source=exact_true_original_good_D_source_multiplicity_partition(model)
    if (observed_R>source["source_AA_three_distinct_point_and_line_GOOD_D_wedges"]
            or observed_R>old["good_D_original_TWO_EDGE_unordered_wedges"]):
        raise AssertionError("original both typed port opposite source wedge must be source AA")
    if sum(categories.values())!=len(inc):
        raise AssertionError("each genuine original source flag belongs to exactly one one-sided physical support category")
    return dict(
        s=G["s"],
        original_source_flag_vertex_count=len(inc),
        original_good_D_pair_count=len(good),
        original_source_AA_good_threeflag_wedge_count=source[
            "source_AA_three_distinct_point_and_line_GOOD_D_wedges"],
        original_both_typed_opposite_GOOD_threeflag_wedge_count=observed_R,
        original_good_D_degree_squared_energy=deg2,
        original_sum_two_marginal_minor_products=sum_minprod,
        true_original_half_minority_product_lower=Fraction(sum_minprod,2),
        true_original_improved_integer_minority_bound=sum_minorbound,
        true_original_SHARP_fixed_marginals_lower=sum_sharp,
        original_source_port_support_categories=dict(categories),
        genuine_source_original_per_flag_four_port_marginal_certificates=tuple(per),
        exact_source_two_typed_opposite_present_IFF_both_one_sided_ports_active=True,
        conditional_uniform_minority_product_lower_NOT_PROVED=True,
        true_source_three_new_flag_Hall_positive_NOT_PROVED=True,
        selected_original_GF5_s6_NOT_PROVED=True,
    )


def conditional_all_h_minor_ports_to_seven_GF5(s,alpha,beta):
    """STRICTLY CONDITIONAL all-global ORIGINAL 2 sequential hypotheses.

    H1: sum true GOOD k_i*ell_i >=alpha*sum true GOOD deg_i^2
        on every actual original globally fixed f,g; NOT proved.
    H2: at least beta-fraction of genuinely original GOOD opposite
        distinct 3-incidence flag wedges belongs to an accepted
        SIX-DISTINCT-ORIGINAL-ID selected seven-GF5 six-Q; NOT proved.
    Then h>=16 AA4-AV sourceAA>=s6/10 plus R>=.5 sum k ell
    plus at most SIX wedges per accepted original six-Q gives
        S>=ceil(alpha*beta*s6/60).
    """
    z=universal_original_AA_good_wedge_lower(s)
    a,b=Fraction(alpha),Fraction(beta)
    if not (0<=a<=Fraction(1,4) and 0<=b<=1):
        raise ValueError("alpha in [0,1/4] minority product energy ratio, beta in [0,1] actual seven-GF5 original wedge coverage")
    val=(a*b*Fraction(s**6,60)
         if z["source_AA_all_global_s6_over_10_PROVED"] else None)
    return dict(
        s=s,h=z["h"],
        assumed_uniform_original_GOOD_minority_product_degree_squared_ratio=a,
        assumed_original_TRUE_seven_GF5_six_ID_Q_wedge_coverage_fraction=b,
        all_h_sufficient_conditional_original_S_GF5_lower_rational=val,
        conditional_integer_minimum_S=(
            (val.numerator+val.denominator-1)//val.denominator
            if val is not None else None),
        hypothesis_H1_all_f_g_one_sided_port_minority_mass_UNPROVED=True,
        hypothesis_H2_all_f_g_six_original_ID_GF5_continuation_UNPROVED=True,
        original_unconditional_seven_GF5_S_s6_NOT_PROVED=True,
    )
