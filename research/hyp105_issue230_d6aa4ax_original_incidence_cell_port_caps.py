"""HYP-105 #230 AA4-AX: true ORIGINAL F^T B G cell-cap forced GOOD ports.

Parent #556 proved a SHARP full-GOOD-marginal Fréchet envelope and
R_good>=1/2 sum_i minP_i*minL_i; #554 source GOOD A/A wedge
Omega(s6). Parent #538 proved the true ORIGINAL symplectic GQ
spectral physical coordinate CELL cap K. All PRIOR, credited.

NEW ALL h≥1 (genuine ORIGINAL W(3,s), globally injected typed f,g):
Every center true source incident flag i=(p,l) belongs to all four
physical mixed coordinate cells M[c,e]=(F^T B G)[c,e], each including
this same actual ORIGINAL source flag at least once. Other actual
GOOD D neighbors are a subset of those cells; a genuine D neighbor
belongs to exactly ONE center point-port and ONE center line-port.
If D_i is its GOOD degree and M the single true global mixed tensor,
then
  point row upper U^P_u=sum_v(M[c_u,e_v]-1)
  line column upper U^L_v=sum_u(M[c_u,e_v]-1).
This uses only the ACTUAL source incidence transport and D_i, not
the GOOD 2x2 joint distribution. Hence
  min point GOOD port degree >= (D_i-max_u U^P_u)_+
  min line  GOOD port degree >= (D_i-max_v U^L_v)_+.
Using the exact source-degenerate subtractions of #554, the
ALL-D 2x2 tensor X similarly supplies STRICTER row/column uppers.
By #556 this implies new deterministic original same-global
  R_GOOD >= sum_i ceil(p_i*l_i/2)
where p_i,l_i are these forced minorities. The spectrum-only K
gives the uniform all-h weaker certificate
  R_GOOD >= sum_i ceil((D_i - (2 floor(K)-2))_+^2/2).
NO positive s6 all-global proof: this may be ZERO in real finite maps.

NEW rigorous METHOD NO-GO: for all dyadic h>=16, the known scalar
source GOOD D lower E_min from #538, source A/A GOOD wedge lower
W_AA>=s6/10 from #554, and single original source spectral cell
cap K are simultaneous with ABSTRACT local four-bin degree data
  degree_i=4(s+1), x00_i=degree_i, other three x=0,
  edge energy=N degree/2=2V(s+1)^2 >= E_min,
  all source-distinct centered wedges proxy=N*C(degree,2)>=s6/10,
  degree+1 <=floor(K),
  R_i=0.
This is an ABSTRACT RELAXATION numerical nonimplication of those
SCALAR premises ONLY, NOT a true GQ global f,g counterexample and
NOT a valid all-h seven GF5 counterfamily. Specifically the
per-center physical cell chosen may not be globally realizable.
Requires genuine globally constrained incidence-cell correlations.
"""
from fractions import Fraction
from math import comb

from hyp105_issue230_d6aa4ap_uniform_good_original_D_spectral import (
    global_good_original_D_spectral_certificate)
from hyp105_issue230_d6aa4ar_good_wedges_port_balance import (
    _good_D_edge_graph)
from hyp105_issue230_d6aa4av_global_source_aa_good_wedges import (
    exact_original_corrected_two_type_four_bin_transport,
    exact_true_original_good_D_source_multiplicity_partition,
    universal_original_AA_good_wedge_lower)
from hyp105_issue230_d6aa4aw_sharp_original_twoport_marginals import (
    exact_sharp_integer_twoport_marginal_lower,
)


def integer_half_ceiling(n):
    if type(n) is not int or n<0:
        raise ValueError("integer nonnegative charge")
    return (n+1)//2


def all_h_spectral_original_port_cap_no_go(s):
    """Proves genuine original GQ spectral per-cell/port row cap;
    separately gives honest ABSTRACT SCALAR-only false inference.
    No fake huge original symplectic geometry instantiated.
    """
    z=global_good_original_D_spectral_certificate(s)
    V,d,a=z["V"],z["d"],z["a"]
    N=V*d
    cap=int(z["original_coordinate_cell_incidence_uniform_upper"])
    # Each true ORIGINAL center source flag belongs to ALL FOUR
    # actual point/line coordinate cells among f(p)xg(l).
    row_col_cap=2*cap-2
    # This is a scalar DATA relaxation, not a genuine f/g model.
    all_center_degree=4*d
    abstract_edges=N*all_center_degree//2
    abstract_source_AA_wedges=N*comb(all_center_degree,2)
    # Parent AA4-AP all-map GOOD lower does not exceed
    # 2 V d² by physical K_a minimality: a²>2V, D0<2Vd².
    assert abstract_edges>=z[
        "globally_port_good_unordered_D_explicit_lower"]
    assert a-1>=d
    assert cap>=2*d+1
    if s>=1<<16:
        assert cap>=all_center_degree+1
        assert row_col_cap>=all_center_degree
        assert abstract_source_AA_wedges>=Fraction(s**6,10)
    return dict(
        s=s,h=z["h"],V=V,d=d,a=a,
        true_original_incidence_flag_vertices=N,
        original_GQ_expander_physical_cell_upper_exact_rational=z[
            "original_coordinate_cell_incidence_uniform_upper"],
        original_GQ_integer_cell_upper=floor_int(cap),
        all_global_true_original_one_typed_port_row_upper=row_col_cap,
        scalar_SOURCE_GOOD_unordered_D_uniform_floor=z[
            "globally_port_good_unordered_D_explicit_lower"],
        abstract_relaxation_all_center_degree=all_center_degree,
        abstract_relaxation_all_D_edges=abstract_edges,
        abstract_relaxation_source_distinct_wedges_NUMERICAL_proxy=abstract_source_AA_wedges,
        abstract_relaxation_four_bin=(all_center_degree,0,0,0),
        abstract_relaxation_twoport_opposite_wedges_ZERO=True,
        for_h16_scalar_GOOD_and_AA_and_cell_CAP_consistent_with_abstract_R_zero=(
            z["h"]>=16),
        ABSTRACT_not_global_true_original_GQ_source_or_real_global_f_g=True,
        NO_unconditional_original_twoport_minorities_positive_proved=True,
        root_issue230_original_seven_GF5_s6_OPEN=True,
    )


def floor_int(n):
    return int(n)


def exact_true_original_incidence_cell_forced_good_ports(model):
    """STRICT TRUE original finite W32/W34 fixed SAME complete f,g.

    Only D_i GOOD uncolored degrees, ORIGINAL mixed incidence M=F^T B G
    and corrected (ALL D, not GOOD) X_i are used to FORCE a lower on
    local GOOD point & line physical port minorities; no GOOD port
    colors are consulted for the forced floors.

    An INDEPENDENT literal original GOOD D-neighbor per-port oracle is
    used *afterwards* only to certify the derived floor and report
    the exact real value. No source geometry or physical global maps
    are resampled. Big h source model is NOT materialized.
    """
    G,good,neighbors,badP,badL=_good_D_edge_graph(model)
    prior=exact_original_corrected_two_type_four_bin_transport(model)
    inc,f,g=G["inc"],G["left"],G["right"]
    if len(inc)!=len(prior["true_original_centered_flag_D_2by2_point_line_port_tensor"]):
        raise AssertionError("true original GQ source incidence flag tensor mismatch")
    M=prior["true_original_full_physical_coordinate_transport"]
    spectral=global_good_original_D_spectral_certificate(G["s"])
    Kcap=int(spectral["original_coordinate_cell_incidence_uniform_upper"])
    scalar_upper=2*Kcap-2
    sums={"spectral":0,"physical_raw":0,"source_corrected":0}
    activated={"spectral":0,"physical_raw":0,"source_corrected":0}
    exact_opposite=0
    exact_minority_sum=0
    exact_sharp_min=0
    exact_source_good_degrees=0
    too_large_source_factor=0
    raw_slack=corrected_slack=0
    hist={}
    for i,(p,l) in enumerate(inc):
        c0,c1=sorted(f[p]);e0,e1=sorted(g[l])
        cells=((M[c0][e0],M[c0][e1]),
               (M[c1][e0],M[c1][e1]))
        if min(cells[0]+cells[1])<1:
            raise AssertionError("true ORIGINAL flag not present in ALL its own four mixed physical source cells")
        if max(cells[0]+cells[1])>Kcap:
            raise AssertionError("true original GQ incidence spectral CELL upper breached")
        Uprow=(sum(cells[0])-2,sum(cells[1])-2)
        Uline=(cells[0][0]+cells[1][0]-2,
               cells[0][1]+cells[1][1]-2)
        xx=prior["true_original_centered_flag_D_2by2_point_line_port_tensor"][i]
        Uprow_corrected=(xx[0]+xx[1],xx[2]+xx[3])
        Uline_corrected=(xx[0]+xx[2],xx[1]+xx[3])
        if any(x>y for x,y in zip(Uprow_corrected,Uprow)):
            raise AssertionError("source corrected original D physical point-port cap > raw M incidence capacity")
        if any(x>y for x,y in zip(Uline_corrected,Uline)):
            raise AssertionError("source corrected original D physical line-port cap > raw M incidence capacity")
        D=len(neighbors[i])
        floors={}
        for name,p_max,l_max in (
            ("spectral",scalar_upper,scalar_upper),
            ("physical_raw",max(Uprow),max(Uline)),
            ("source_corrected",max(Uprow_corrected),max(Uline_corrected)),
        ):
            P=max(0,D-p_max)
            L=max(0,D-l_max)
            floors[name]=(P,L)
            charge=integer_half_ceiling(P*L)
            sums[name]+=charge
            activated[name]+=int(P>0 and L>0)
        if not (sums["spectral"]<=sums["physical_raw"]<=sums["source_corrected"]):
            raise AssertionError("nested ORIGINAL physical-source port cap floors")
        # Last part is REFEREE ONLY: a second actual true original
        # adjacency list calculates the physical GOOD 2x2 buckets.
        ports_p={v:j for j,v in enumerate((c0,c1))}
        ports_l={v:j for j,v in enumerate((e0,e1))}
        bins=[0,0,0,0]
        for j,cp,cl in neighbors[i]:
            bins[2*ports_p[cp]+ports_l[cl]]+=1
        row=(bins[0]+bins[1],bins[2]+bins[3])
        col=(bins[0]+bins[2],bins[1]+bins[3])
        for name,(mp,ml) in floors.items():
            if (min(row)<mp or min(col)<ml):
                raise AssertionError("invalid true original port minority forced by source mixed incidence matrix")
        R=bins[0]*bins[3]+bins[1]*bins[2]
        exact_opposite+=R
        exact_minority_sum+=integer_half_ceiling(min(row)*min(col))
        exact_sharp_min+=exact_sharp_integer_twoport_marginal_lower(
            row[0],row[1],col[0],col[1])[
                "exact_SHARP_fixed_both_marginals_minimum_opposite_wedges"]
        if R<integer_half_ceiling(floors["source_corrected"][0]*
                                   floors["source_corrected"][1]):
            raise AssertionError("true original strict source incidence cap physical opposite lower violated")
        exact_source_good_degrees+=D
        hist[D]=hist.get(D,0)+1
        raw_slack+=max(Uprow)-max(Uprow_corrected)
        corrected_slack+=max(Uline)-max(Uline_corrected)
    if exact_source_good_degrees!=2*len(good):
        raise AssertionError("source GOOD D graph handshake")
    if not(sums["spectral"]<=sums["physical_raw"]<=sums["source_corrected"]
           <=exact_minority_sum<=exact_sharp_min<=exact_opposite):
        raise AssertionError("nested true ORIGINAL source/physical port pre-Hall charge")
    p=exact_true_original_good_D_source_multiplicity_partition(model)
    if exact_opposite>p["source_AA_three_distinct_point_and_line_GOOD_D_wedges"]:
        raise AssertionError("original GOOD twoport 3flag must be source A/A")
    return dict(
        s=G["s"],
        N_true_original_incidence_flag_IDs=len(inc),
        actual_GOOD_D_original_unordered_source_edges=len(good),
        TRUE_original_source_AA_GOOD_centered_wedges=p[
            "source_AA_three_distinct_point_and_line_GOOD_D_wedges"],
        actual_physical_GOOD_D_opposite_twoport_3flag_wedges=exact_opposite,
        true_original_GOOD_degree_histogram=hist,
        pure_GQ_SPECTRAL_cell_only_forced_opposite_integer_lower=sums["spectral"],
        TRUE_original_mixed_FtBG_RAW_cell_forced_opposite_integer_lower=sums["physical_raw"],
        SOURCE_DEGENERACY_corrected_ALL_D_cell_forced_good_opposite_lower=sums["source_corrected"],
        full_GOOD_independently_colored_half_minority_opposite_lower=exact_minority_sum,
        full_GOOD_sharp_actual_port_marginal_opposite_lower=exact_sharp_min,
        high_GOOD_degree_source_centers_forced_both_ports_by_spectral_cap=activated["spectral"],
        true_source_centers_forced_both_ports_by_RAW_mixed_cells=activated["physical_raw"],
        true_source_centers_forced_both_ports_by_corrected_ALL_D_cell_cap=activated["source_corrected"],
        raw_and_corrected_point_CAP_slack_total=raw_slack,
        raw_and_corrected_line_CAP_slack_total=corrected_slack,
        actual_original_port_distribution_REFEREE_only=True,
        source_GQ_incidence_transport_forced_partial_GF5_preHall_not_final_selected=True,
        all_global_positive_minority_sum_NOT_PROVED=True,
        root230_Branch_A_B_C_OPEN=True,
    )
