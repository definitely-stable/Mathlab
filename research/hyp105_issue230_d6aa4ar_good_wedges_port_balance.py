"""HYP-105 #230 AA4-AR: genuine-original GOOD D wedge theorem and port defect.

This is the missing deterministic first-two-step analysis after AA4-AP/AQ:
on ACTUAL incidence flag vertices of W(3,s), and the ONE globally
fixed correlated pair of complete physical point/line maps f,g,
AA4-AP proved >=s^5/10 true original GOOD AA4-AL D edges for h>=14.

Cauchy/Jensen gives at least s^6/200 UNORDERED TWO-EDGE GOOD FLAG WEDGES
(i-j-k, j original center) for EVERY h>=14 and EVERY original f,g.
This is a TRUE ORIGINAL 3-FLAG count (not a positive selected GF5 Q).

At each actual original flag j=(p,l), f(p)=(c0,c1), g(l)=(e0,e1).
The four GOOD D-neighbor classes x00,x01,x10,x11 are defined by the
unique two typed physical edge colors of the incident genuine D edge.
A D6-compatible forward transition MUST use the physically opposite
ports in BOTH typed maps, so its undirected count is

  R = sum_j (x00*x11 + x01*x10)
  8 R = SUM_j [deg(j)^2 + (x00+x11-x01-x10)^2
                    - 2*((x00-x11)^2+(x01-x10)^2)].

Every complementary TWO-EDGE original D wedge automatically has
THREE DISTINCT actual original point factors and THREE DISTINCT
actual original line factors: repeated outer source factor would
have to contain both endpoints of the center physical factor pair
and then global physical injectivity forces equality to the center
source factor, contradicting its original D edges.

Thus, under the explicitly CONDITIONAL inequality
   sum_j ((x00-x11)^2+(x01-x10)^2) <= (1/4) sum_j deg(j)^2,
we get R>= sum deg^2/16 >= s^6/800 for every h>=14.
The conditional PORT BALANCE is NOT proved for every f,g, and
even R>0 does NOT prove a rainbow closed D6 sixcycle or any
non-D6 selected GF5 motif, let alone S>=c*s6.

Finite genuine original W32/W34 real two-map audits compare all
numbers to a second literal pairwise wedge enumeration, and
the full historical W32 original seven-Q oracle for D6=0 despite
R>0 is a strict GF5 non-lift test.
"""
from collections import Counter
from fractions import Fraction

from hyp105_issue230_d6aa4aq_colored_original_D_cycle import (
    original_bicolored_D_flag_graph,exact_original_rainbow_D6_cycle_transfer)
from hyp105_issue230_d6aa4ao_robust_port_occupancy import (
    globally_bad_physical_coordinates)
from hyp105_issue230_d6aa4ap_uniform_good_original_D_spectral import (
    global_good_original_D_spectral_certificate)
from hyp105_issue230_d6aa4al_global_original_coordinate_transport import (
    _actual_strict_original_transport)
from hyp105_issue230_d6aa4am_genuine_pair_sixcharge import (
    original_D_pair_index)


def all_h_original_good_wedge_lower(s):
    """Rigorous for ALL genuine ORIGINAL W3s, all global typed f,g, h>=14.

    Computes exact rational lower, no giant fake geometry materialized.
    """
    th=global_good_original_D_spectral_certificate(s)
    V,d,a=th["V"],th["d"],th["a"]
    N=V*d
    h=th["h"]
    edge_min=Fraction(s**5,10) if h>=14 else None
    if h>=14:
        assert N<=2*s**4 and s>=20
        assert edge_min>=Fraction(N,4)
        exact_Jensen=2*edge_min**2/N-edge_min
        simple_floor=Fraction(s**6,200)
        assert exact_Jensen>=simple_floor
        # If the two-color opposite-port energy imbalance is small,
        # complement wedges are forced. NOT a known all-f,g property.
        conditional_complement=Fraction(s**6,800)
    else:
        exact_Jensen=simple_floor=conditional_complement=None
    return dict(
        s=s,h=h,actual_original_flag_vertex_count=N,
        universally_original_good_D_edge_lower=edge_min,
        unconditional_true_original_good_TWO_EDGE_wedge_lower=simple_floor,
        exact_Jensen_good_wedge_floor=exact_Jensen,
        conditional_port_defect_le_quarter_degree_energy_then_true_original_opposite_wedges_lower=conditional_complement,
        SOURCE_good_wedge_s6_PROVED_for_all_f_g=(h>=14),
        OPPOSITE_wedge_s6_unconditional_NOT_PROVED=True,
        rainbow_D6_cycle_positive_NOT_PROVED=True,
        original_full_seven_GF5_S_s6_NOT_PROVED=True,
    )


def _good_D_edge_graph(model):
    """Actual globally fixed original source/physical model, both bad typed sets."""
    s,V,d,a,left,right,inc,np,nl=_actual_strict_original_transport(model)
    G=original_bicolored_D_flag_graph(model)
    badP=frozenset(globally_bad_physical_coordinates(
        a,left)["bad_physical_coordinate_indices"])
    badL=frozenset(globally_bad_physical_coordinates(
        a,right)["bad_physical_coordinate_indices"])
    edge_color=G["edge_colors"]
    good=set()
    neighbors=[[] for _ in inc]
    for (i,j),(cp,cl) in edge_color.items():
        p,l=inc[i]
        q,m=inc[j]
        portp1=next(x for x in left[p] if x!=cp)
        portp2=next(x for x in left[q] if x!=cp)
        portl1=next(x for x in right[l] if x!=cl)
        portl2=next(x for x in right[m] if x!=cl)
        if ({portp1,portp2}&badP) or ({portl1,portl2}&badL):
            continue
        good.add((i,j))
        neighbors[i].append((j,cp,cl))
        neighbors[j].append((i,cp,cl))
    return G,frozenset(good),tuple(tuple(sorted(row)) for row in neighbors),badP,badL


def exact_true_original_good_D_two_port_wedge_certificate(model):
    """True ORIGINAL global TWO-MAP good D graph 2-wedges and defect identity.

    Every count is an INTEGER derived from actual original source flag
    IDs and actual point/line global physical labels. No source
    factor remapping, no mock GQ, no statistical independence.

    Complexity O(N+|D|), including exact independent O(sum deg^2)
    literal wedge oracle left for tests.
    """
    G,good,neighbors,badP,badL=_good_D_edge_graph(model)
    inc,left,right=G["inc"],G["left"],G["right"]
    degree_energy=0
    wedges=0
    opposite_wedges=0
    port_imbalance_energy=0
    diagonal_group_energy=0
    hist=Counter()
    exceptional_source_wedges=0
    for idx,row in enumerate(neighbors):
        p,l=inc[idx]
        coords_p={c:t for t,c in enumerate(sorted(left[p]))}
        coords_l={e:t for t,e in enumerate(sorted(right[l]))}
        bins=[0,0,0,0]
        for j,cp,cl in row:
            if cp not in coords_p or cl not in coords_l:
                raise AssertionError("true ORIGINAL D edge colors absent from center image")
            bins[2*coords_p[cp]+coords_l[cl]]+=1
        x00,x01,x10,x11=bins
        d=len(row)
        w=d*(d-1)//2
        r=x00*x11+x01*x10
        im=(x00-x11)**2+(x01-x10)**2
        gp=(x00+x11-x01-x10)**2
        if 8*r !=d*d+gp-2*im:
            raise AssertionError("true original two-port 4-bin exact polarized identity")
        hist[tuple(bins)]+=1
        degree_energy+=d*d
        wedges+=w
        opposite_wedges+=r
        port_imbalance_energy+=im
        diagonal_group_energy+=gp
    if len(good)!=sum(len(row) for row in neighbors)//2:
        raise AssertionError("true original good-D graph edge handshake failed")
    if 8*opposite_wedges!=degree_energy+diagonal_group_energy-2*port_imbalance_energy:
        raise AssertionError("global actual original port polarization formula")
    exact_plain_jensen=Fraction(2*len(good)**2,len(inc))-len(good)
    if wedges<exact_plain_jensen:
        raise AssertionError("finite actual original source GOOD D Jensen")
    allh=all_h_original_good_wedge_lower(G["s"])
    if allh["SOURCE_good_wedge_s6_PROVED_for_all_f_g"]:
        if wedges<allh["unconditional_true_original_good_TWO_EDGE_wedge_lower"]:
            raise AssertionError("all-h actual original triple wedge floor")
    conditional_fulfilled=4*port_imbalance_energy<=degree_energy
    if conditional_fulfilled and allh["SOURCE_good_wedge_s6_PROVED_for_all_f_g"]:
        if opposite_wedges < allh[
            "conditional_port_defect_le_quarter_degree_energy_then_true_original_opposite_wedges_lower"]:
            raise AssertionError("conditional opposite original wedge lower")
    return dict(
        s=G["s"],V=G["V"],a=G["a"],
        real_original_incidence_flag_vertices=len(inc),
        D_ALL_actual_original_bilateral_edges=len(G["D_edges"]),
        D_GOOD_actual_original_bilateral_edges=len(good),
        D_BAD_actual_original_bilateral_edges=len(G["D_edges"])-len(good),
        good_D_original_TWO_EDGE_unordered_wedges=wedges,
        good_D_original_OPPOSITE_TWO_TYPED_port_wedges=opposite_wedges,
        true_original_good_D_degree_squared_energy=degree_energy,
        true_original_two_typed_port_imbalance_energy=port_imbalance_energy,
        true_original_diagonal_group_imbalance_energy=diagonal_group_energy,
        exact_global_8_R_equals_deg2_plus_group2_minus_2_portdefect=True,
        port_balance_conditional_hypothesis_fulfilled=conditional_fulfilled,
        original_GOOD_D_source_flag_four_bin_histogram=dict(hist),
        independent_original_unordered_wedge_Jensen_floor=exact_plain_jensen,
        point_physical_exception_coords=tuple(sorted(badP)),
        line_physical_exception_coords=tuple(sorted(badL)),
        allh_theorem=allh,
        source_three_DISTINCT_points_lines_per_opposite_wedge=True,
        no_unconditional_source_opposite_wedge_lower_claim=True,
        no_source_six_ID_D6_or_full_GF5_lower_claim=True,
    )


def independent_original_literal_good_two_port_wedges(model):
    """Different finite SOURCE-first literal original i-j-k wedge oracle.

    Does NOT use 4-bin algebra or degree-square counting for number of
    two-edge walks; enumerates literal neighbors (i,k) at each real
    original source incidence flag j and checks physical two-port
    complement and real 3-source-point/3-source-line distinctness.
    Finite W32, W34 ONLY.
    """
    G,good,neighbors,badP,badL=_good_D_edge_graph(model)
    inc,left,right=G["inc"],G["left"],G["right"]
    if len(inc)>500:
        raise ValueError("finite original source wedge literal budget W32/W34 only")
    total=opposite=0
    opposite_examples=[]
    seenbad=0
    for center,row in enumerate(neighbors):
        for offset,first in enumerate(row):
            i,cp,cl=first
            for k,cq,cr in row[offset+1:]:
                if i==k:
                    raise AssertionError("not an actual two-distinct-neighbor wedge")
                total+=1
                if cp==cq or cl==cr:
                    continue
                opposite+=1
                pointids={inc[i][0],inc[center][0],inc[k][0]}
                lineids={inc[i][1],inc[center][1],inc[k][1]}
                if len(pointids)!=3 or len(lineids)!=3:
                    seenbad+=1
                if len(opposite_examples)<10:
                    opposite_examples.append((i,center,k))
    if seenbad:
        raise AssertionError("physical opposite-typed ORIGINAL wedge repeated a source factor")
    return dict(
        s=G["s"],original_good_D_source_edges=len(good),
        actual_original_literal_all_wedges=total,
        actual_original_literal_two_type_opposite_wedges=opposite,
        witness_real_source_threepoint_threeline_opposite_wedges=tuple(opposite_examples),
        bad_repeated_original_factor_opposite_wedges=seenbad,
        independent_from_four_bin_and_degree_identity=True,
    )


def conditional_all_h_good_wedge_to_original_seven_lower(s, covered_fraction):
    """All-map CONDITIONAL true-original 3-flag-to-6-flag charging.

    Given (NOT PROVED) at least fraction alpha of all GOOD original
    3-flag two-D-edge wedges occurs as a 3-subset of at least one TRUE
    positively accepted seven-GF5 SIX-DISTINCT original flag Q, each
    six-Q contains at most 6*C(5,2)=60 centered GOOD source wedges.
    W_good >=s^6/200 for h>=14 therefore forces
      S_selected >= ceil(alpha*s^6/12000).
    The condition is NOT a universal theorem; W32 finite scans
    measure its failure or success for individual global f,g only.
    """
    z=all_h_original_good_wedge_lower(s)
    alpha=Fraction(covered_fraction)
    if alpha<0 or alpha>1:
        raise ValueError("conditional coverage ratio alpha must lie in [0,1]")
    bound=(alpha*Fraction(s**6,12000)
           if z["SOURCE_good_wedge_s6_PROVED_for_all_f_g"] else None)
    return dict(s=s,assumed_original_good_wedge_covered_fraction=alpha,
                per_genuine_original_six_ID_Q_max_centered_good_wedges=60,
                conditional_minimum_selected_original_six_Q_count=(
                    (bound.numerator+bound.denominator-1)//bound.denominator
                    if bound is not None else None),
                exact_rational_asymptotic_lower_if_h_ge_14=bound,
                this_fraction_hypothesis_NOT_PROVED_for_all_f_g=True,
                original_GF5_S_s6_unconditionally_NOT_PROVED=True)


def exact_true_W32_original_seven_covered_good_wedges(model):
    """Exact ORIGINAL W32 same-global-f,g selected seven-Q wedge hypergraph.

    Independent historical seven-Q Oracle; enumerate every genuine
    original GOOD D centered two-edge 3-flag wedge and separately
    each six-ID original Q's potential centered pairs among its SIX
    literal flag IDs. Exact charge incidences, coverage, uncovered,
    per-Q max60, no false per-wedge Q extension assumption.
    """
    from itertools import combinations
    from hyp105_g5e2b3e1b0_seven_signature import seven_census

    G,good,neighbors,badP,badL=_good_D_edge_graph(model)
    if (G["s"],len(G["inc"]),(G["a"]))!=(2,45,6):
        raise ValueError("complete selected source-six Q wedge oracle only genuine W32 K6")
    selected=seven_census(model,independent_checks=False,witness_sets=True)["sets"]
    literal_good_wedges=set()
    for center,row in enumerate(neighbors):
        for a,b in combinations((n for n,_,_ in row),2):
            wedge=(center,)+tuple(sorted((a,b)))
            if wedge in literal_good_wedges:
                raise AssertionError("duplicate ORIGINAL centered D GOOD two-edge wedge")
            literal_good_wedges.add(wedge)
    incidences=0
    covered=set()
    per_tag_incidence=Counter()
    per_tag_Q=Counter()
    Q_hist=Counter()
    for Q,tag in selected.items():
        Q=frozenset(Q)
        local=set()
        for center in Q:
            other=tuple(sorted(Q-{center}))
            for a,b in combinations(other,2):
                wedge=(center,a,b)
                if wedge in literal_good_wedges:
                    local.add(wedge)
        if len(local)>60:
            raise AssertionError("more than 60 centered good wedges inside six true flags")
        incidences+=len(local)
        per_tag_incidence[tag]+=len(local)
        per_tag_Q[tag]+=1
        Q_hist[len(local)]+=1
        covered.update(local)
    source=exact_true_original_good_D_two_port_wedge_certificate(model)
    if len(literal_good_wedges)!=source["good_D_original_TWO_EDGE_unordered_wedges"]:
        raise AssertionError("source-first wedge census differs from port-defect graph")
    if (incidences!=sum(per_tag_incidence.values())
            or len(covered)>len(literal_good_wedges)
            or incidences>60*len(selected)):
        raise AssertionError("original 3-to-6 wedge charging identity wrong")
    return dict(
        s=G["s"],D_GOOD_original_pairs=len(good),
        genuine_original_good_source_three_flag_wedges=len(literal_good_wedges),
        true_original_seven_selected_six_ID_Q=len(selected),
        distinct_good_wedges_covered_by_some_true_original_seven_Q=len(covered),
        distinct_good_wedges_NOT_covered_by_ANY_seven_Q=(
            len(literal_good_wedges)-len(covered)),
        all_original_good_wedge_to_six_Q_charge_incidences=incidences,
        accepted_Q_centered_good_wedge_charge_histogram=dict(sorted(Q_hist.items())),
        original_seven_tag_charge_by_class=dict(per_tag_incidence),
        original_seven_tag_Q_count=dict(per_tag_Q),
        true_original_good_wedge_coverage_fraction=Fraction(
            len(covered),len(literal_good_wedges)),
        all_selected_six_Q_capacity_60_validated=True,
        all_global_good_wedge_positive_covered_fraction_NOT_PROVED=True,
        original_six_ID_GF5_s6_lower_NOT_PROVED=True,
    )
