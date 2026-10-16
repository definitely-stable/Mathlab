"""HYP-105 #230 AA4-AZ: exact quenched TRUE ORIGINAL GOOD-port wedge mean.

FIX arbitrary complete original point globally injective f and ANY right
occupied physical unordered-pair edge support E. Draw ONE uniformly
random WHOLE global original LINE factor bijection g onto E. The source
W(3,s) is genuine; all centered wedge events use three different TRUE
original point/line IDs and ACTUAL distinct original source flags.

The globally "bad" physical coordinates of AA4-AO depend ONLY on the
occupied physical edge support, not on the original LINE assignment.
Thus ALL GOOD opposite point/line 3-flag quenched expectation factors
EXACTLY through induced CLEAN physical edge degree 2-port energy.

All-h h>=5 rigorous >=s^6/128 EXPECTATION uniformly in f and E;
NO deterministic fixed-adversarial-g, six-ID GF5 accepted, or root #230
A/B/C conclusion. This does not duplicate PR #544 high-probability D6.
"""
from math import comb
from fractions import Fraction

from hyp105_issue230_d6aa4ay_quenched_allD_opposite_mean import (
    _params, physical_edge_port_energy
)


def support_bad_clean_energy(occupied,a):
    """Exact AA4-AO physical bad coordinates, clean induced E, rooted T."""
    E=tuple(tuple(sorted(edge)) for edge in occupied)
    if len(set(E))!=len(E) or any(len(edge)!=2 or edge[0]==edge[1] or
                                  min(edge)<0 or max(edge)>=a for edge in E):
        raise ValueError("one complete globally injected physical image support required")
    expected={tuple(edge) for edge in __import__("itertools").combinations(range(a),2)}
    missing=expected-set(E)
    degree_missing=[0]*a
    for u,v in missing:
        degree_missing[u]+=1
        degree_missing[v]+=1
    bad=frozenset(i for i,n in enumerate(degree_missing) if 16*n>=a)
    clean=tuple(e for e in E if not (set(e)&bad))
    physical_energy=physical_edge_port_energy(clean,a)
    t=a-len(bad)
    if len(bad)>31:
        raise AssertionError("minimal image bad-coordinate bound exceeded")
    if physical_energy<0:
        raise AssertionError("negative physical induced clean edge-energy")
    return {
        "a":a,
        "bad_coordinates":tuple(sorted(bad)),
        "clean_coordinate_count":t,
        "clean_occupied_edge_count":len(clean),
        "global_occupied_edge_count":len(E),
        "missing_physical_edges":len(missing),
        "clean_induced_occupied_edges":clean,
        "CLEAN_physical_two_opposite_port_root_energy":physical_energy,
        "coordinate_clean_threshold_is_16_missing_degree_less_than_a":True,
    }


def universal_original_clean_twoport_support_floor(s):
    """All genuine dyadic h>=5: T(E_clean)>=V²/16 uniformly E.

    Only one minimal physical K_a support per type is assumed, not a
    fake synthetic high-order GQ or independent factor assignment.
    """
    if type(s) is not int or s<2 or s&(s-1):
        raise ValueError("actual dyadic original W(3,2^h) order required")
    V,a,K,m=_params(s);d=s+1
    t=a-31
    if s>=32:
        assert a>=261 and t>=128 and t*2>=a and m<=a-2<=2*t
        # Delete up to 31 bad vertices; at most m missing K_a edges.
        # Any >=t clean vertices yield at least C(t,2)-m clean edges.
        # Missing-degree lower on that induced t-vertex graph:
        floor=(comb(t,2)-m)*(t-2)**2 - 2*m*(t-1)*(t-2)
        if floor< t**4//4 or floor*16<V*V:
            raise AssertionError("uniform original clean physical energy proof fails")
        # Rigor independent of random test sample: for t>=128,
        # E_clean>= (7/16)t², (t-2)²>9t²/10,
        # 2m(t-1)(t-2)<=4t³<=t⁴/32.
        # Therefore L >= (7/16)*(9/10)t4-t4/32 > t4/4.
        if not (16*(comb(t,2)-m)>=7*t*t
                and 10*(t-2)**2>=9*t*t
                and 32*4*t**3<=t**4):
            raise AssertionError("exact rational dyadic t>=128 proof gates fail")
        universal_port_energy=Fraction(V*V,16)
        mean_floor=Fraction(
            2*d*(d-1)*(d-2),V*(V-1)*(V-2))*universal_port_energy**2
        if mean_floor<Fraction(s**6,128):
            raise AssertionError("genuine ORIGINAL GOOD port quenched ≥s6/128 unsupported")
        certified=True
    else:
        t_floor=None
        universal_port_energy=None
        mean_floor=None
        certified=False
        floor=None
    return {
        "s":s,"h":s.bit_length()-1,"V":V,"d":d,"a":a,"m":m,
        "physical_BAD_coordinate_count_upper":31,
        "conservative_clean_coordinate_count":t,
        "minimal_induced_clean_T_exact_deficit_floor":floor,
        "uniform_clean_T_ge_V_squared_over_16_proved":certified,
        "uniform_ONE_complete_right_global_original_g_E_GOOD_opposite_wedges_ge_s6_over128":
            certified,
        "uniform_original_GOOD_opposite_3flag_expected_lower":mean_floor,
        "complete_FIXED_adversarial_original_right_g_minimax_PROVED":False,
        "accepted_original_7_GF5_six_ID_minimax_PROVED":False,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


def genuine_original_fixed_point_GOOD_source_potential(model):
    """True W32/W34 original centered good point-opposite threeflags Bgood(f).

    Two outer f source edges use OPPOSITE center point physical endpoints;
    all THREE f pair edges are occupied in the induced CLEAN support.
    The source incidence original LINE choices are genuinely from W(3,s).
    """
    s=model["s"];V,a,K,m=_params(s);d=s+1
    f=tuple(tuple(sorted(x)) for x in model["left_labels"])
    inc=tuple(tuple(q) for q in model["incidences"])
    if len(f)!=V or len(set(f))!=V or len(inc)!=V*d:
        raise ValueError("not genuine original complete typed point support")
    E=support_bad_clean_energy(f,a)
    goodpoints={i for i,edge in enumerate(f) if edge in E[
        "clean_induced_occupied_edges"]}
    neighborlines=[set() for _ in range(V)]
    source=set(inc)
    if len(source)!=len(inc):
        raise ValueError("repeated original source incidence ID")
    for p,l in inc:
        if not (0<=p<V and 0<=l<V):
            raise ValueError("original source flag index invalid")
        neighborlines[p].add(l)
    if any(len(x)!=d for x in neighborlines):
        raise ValueError("not true original d-regular point source incidence")
    port=[[] for _ in range(a)]
    for p in goodpoints:
        u,v=f[p]
        port[u].append(p)
        port[v].append(p)
    total=0
    centers=0
    for p,l in inc:
        if p not in goodpoints:continue
        centers+=1
        u,v=f[p]
        for q0 in port[u]:
            if q0==p:continue
            for q1 in port[v]:
                if q1==p or q0==q1:
                    raise AssertionError("globally injected clean f point source IDs repeat")
                lines0=neighborlines[q0]-{l}
                lines1=neighborlines[q1]-{l}
                total+=len(lines0)*len(lines1)-len(lines0&lines1)
    lower=d*(d-1)*(d-2)*E["CLEAN_physical_two_opposite_port_root_energy"]
    if total<lower:
        raise AssertionError("genuine original GOOD point-source wedge floor false")
    return {
        "s":s,"V":V,"d":d,"a":a,
        "true_original_incidence_centers_with_clean_POINT_factor":centers,
        "CLEAN_original_fixed_f_physical_point_opposite_true_source_3flag_count":total,
        "CLEAN_true_original_point_source_regular_degree_lower":lower,
        "clean_point_physical_support":E,
        "same_original_source_incidence_IDs_used_for_every_global_g":True,
    }


def quenched_genuine_original_GOOD_opposite_mean(model):
    """Exact one-global-right-bijection mean for GOOD opposite original wedges.

    Original globally_bad physical coords are a function of E_g ONLY.
    All real original center LINE factor assignment permutations to
    this SAME physical support therefore have identical bad vertices.
    """
    p=genuine_original_fixed_point_GOOD_source_potential(model)
    s,V,a,d=p["s"],p["V"],p["a"],p["d"]
    g=tuple(tuple(sorted(x)) for x in model["right_labels"])
    if len(g)!=V or len(set(g))!=V:
        raise ValueError("not complete one globally injected original source LINE map")
    right=support_bad_clean_energy(g,a)
    T_right=right["CLEAN_physical_two_opposite_port_root_energy"]
    P=Fraction(2*T_right,V*(V-1)*(V-2))
    mean=P*p["CLEAN_original_fixed_f_physical_point_opposite_true_source_3flag_count"]
    exact_floor=P*p["CLEAN_true_original_point_source_regular_degree_lower"]
    proof=universal_original_clean_twoport_support_floor(s)
    if proof["uniform_clean_T_ge_V_squared_over_16_proved"]:
        if mean<exact_floor or exact_floor<proof[
                "uniform_original_GOOD_opposite_3flag_expected_lower"]:
            raise AssertionError("exact GOOD quenched all-h support lower violated")
    return {
        "s":s,"V":V,"a":a,
        "fixed_original_POINT_side_TRUE_source_GOOD_opposite_triples":
            p["CLEAN_original_fixed_f_physical_point_opposite_true_source_3flag_count"],
        "fixed_original_right_clean_support_port_energy":T_right,
        "exact_original_right_ordered_three_DISTINCT_line_edge_probability":P,
        "exact_one_global_original_LINE_bijection_GOOD_opposite_wedge_mean":mean,
        "fixed_point_GOOD_source_degree_lower_expectation":exact_floor,
        "uniform_all_support_theorem":proof,
        "original_LINE_bad_coordinates_are_support_only":True,
        "given_FIXED_adversarial_original_f_g_GOOD_lower_PROVED":False,
        "GOOD_opposite_threeflag_NOT_selected_seven_GF5_sixflag":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


if __name__=="__main__":
    import json
    from hyp105_issue230_projection import fixture
    for h,name in ((1,"S68"),(1,"S72"),(1,"lex"),(2,"lex"),(2,"random")):
        model=fixture(h,name)
        z=quenched_genuine_original_GOOD_opposite_mean(model)
        print("AA4AZ_GOOD_QUENCHED",h,name,json.dumps({
            k:str(v) for k,v in z.items() if k!="uniform_all_support_theorem"},sort_keys=True))
    for h in range(1,30):
        z=universal_original_clean_twoport_support_floor(1<<h)
        print("AA4AZ_ALL_H",h,z["a"],z["uniform_original_GOOD_opposite_3flag_expected_lower"])
