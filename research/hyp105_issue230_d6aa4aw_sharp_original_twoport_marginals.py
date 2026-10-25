"""HYP-105 #230 AA4-AW: SHARP fixed-global two-port marginal GF5 pre-Hall gate.

Parent AA4-AV #554 already proves genuine original GOOD source A/A wedge
mass >=s^6/10 (h>=16) and exact globally correlated original four-port
incidence transport X_i. Earlier AA4-AR already proves an equivalent
quadratic four-port POLARIZATION. These are PRIOR, NOT new claims here.

NEW useful exactly quantified pre-Hall transfer: if four bins
x00,x01,x10,x11 are nonnegative integers, with point port marginals
(r0,r1), line port marginals (c0,c1), R=x00*x11+x01*x10,
the SHARP INTEGER minimum of R over all 4-bin arrays with those
SAME port marginals is obtained by minimizing a convex quadratic
  2t^2+(D-2r0-2c0)t+r0*c0
for integer t=x00 in
  max(0,r0+c0-D) <=t<=min(r0,c0).
The minimum is reached at clipped floor or ceil of
  (2r0+2c0-D)/4.
All port marginal counts can be determined separately from real source
D-neighbor physical coordinate overlaps; no assumption f and g
independent, no fake six-source incident flags.

NEW SHARP UNIFORM LOCAL PHYSICAL OPPOSITE TRANSFER:
  R >= ceil(min(r0,r1)*min(c0,c1)/2).
Tight for balanced (r0=r1=c0=c1 even) with all four bins equal.
AND: R>0 iff BOTH point port counts are positive AND BOTH line port
counts positive. Hence any genuine original good source D center with
two physically occupied point ports and two line ports forces ≥1 actual
three-distinct-point-and-line physically opposite GOOD D wedge.

Summing a true ORIGINAL GQ source model over one fixed f,g gives
 R_GOOD >= Σ_i sharp_integer_Frechet_bound_i
        >= (1/2) Σ_i min(point ports)_i*min(line ports)_i.
This is an ALL-h, all fixed f,g PRE-HALL inequality. It is NOT a
positive universal lower on that cross-port minority energy, and
even R_GOOD>0 is NOT a selected GF5 six-ID Hall completion.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations

from hyp105_issue230_d6aa4ar_good_wedges_port_balance import (
    _good_D_edge_graph)
from hyp105_issue230_d6aa4av_global_source_aa_good_wedges import (
    universal_original_AA_good_wedge_lower,
    exact_true_original_good_D_source_multiplicity_partition,
    exact_original_corrected_two_type_four_bin_transport,
)


def _validate_port_bins(bins):
    if (len(bins)!=4 or any(type(x) is not int or x<0 for x in bins)):
        raise ValueError("four nonnegative INTEGER original port-bin counts required")
    return tuple(bins)


def exact_sharp_integer_twoport_marginal_lower(point0,point1,line0,line1):
    """An ALL-INTEGER sharp minimum over original nonnegative 2x2 bins
    with EXACT same individual point and line physical port marginals.
    No false unconditional all-f,g strictly positive assertion.
    """
    if any(type(x) is not int or x<0
           for x in (point0,point1,line0,line1)):
        raise ValueError("nonnegative integer physical port marginals required")
    D=point0+point1
    if D!=line0+line1:
        raise ValueError("point and line port marginals must sum to same source degree")
    lower=max(0,point0+line0-D)
    upper=min(point0,line0)
    xstar_numerator=2*point0+2*line0-D
    q=xstar_numerator//4
    candidates={lower,upper,max(lower,min(upper,q)),
                max(lower,min(upper,q+1))}
    evaluated={}
    for t in candidates:
        if not lower<=t<=upper:
            raise AssertionError("outside integer feasible 2x2 original physical port")
        v=2*t*t+(D-2*point0-2*line0)*t+point0*line0
        bins=(t,point0-t,line0-t,D-point0-line0+t)
        if min(bins)<0:
            raise AssertionError("negative physical port bin from marginals")
        if v!=bins[0]*bins[3]+bins[1]*bins[2]:
            raise AssertionError("physical opposite integer quadratic mismatch")
        evaluated[t]=v
    minval=min(evaluated.values())
    argmin=min(t for t,v in evaluated.items() if v==minval)
    a=min(point0,point1)
    b=min(line0,line1)
    minority_floor=(a*b+1)//2
    if minval<minority_floor:
        raise AssertionError("twoport Fréchet lower below sharp minority-product inequality")
    return dict(
        D_actual_original_source_neighbor_degree=D,
        fixed_point_physical_port_marginals=(point0,point1),
        fixed_line_physical_port_marginals=(line0,line1),
        exact_permitted_original_joint_bin_x00_integer_interval=(lower,upper),
        unique_smallest_feasible_x00_argmin=argmin,
        exact_SHARP_fixed_both_marginals_minimum_opposite_wedges=minval,
        uniform_half_minorities_CEILING_lower=minority_floor,
        all_four_actual_source_bin_counts_nonnegative=True,
        two_typed_opposite_FORCED_iff_each_typed_port_active=(a>0 and b>0),
        NOT_an_all_global_GF5_selected_six_Q_lower=True,
    )


def all_h_abstract_good_original_port_marginal_gate(s,positive_minorities):
    """A precise NON-CIRCULAR conditional root-frontier certificate.

    The SOURCE AA GOOD wedge floor s6/10 from parent #554 is ALL GLOBAL
    for dyadic h>=16. A separate physical minority-product lower is
    STILL UNPROVED. When supplied as a CONDITIONAL assumption, it
    yields a TRUE source opposite-port 3-flag floor, NOT selected GF5.
    """
    source=universal_original_AA_good_wedge_lower(s)
    q=Fraction(positive_minorities)
    if q<0:
        raise ValueError("nonnegative ASSUMED minority product lower")
    return dict(
        s=s,all_fixed_original_f_g_source_AA_good_wedges_lower=source[
          "universal_source_AA_good_centered_two_D_edge_wedge_lower"],
        assumed_GLOBAL_true_original_good_twoport_minority_product_lower=q,
        conditional_opposite_true_original_GOOD_3flag_lower=q/2,
        true_original_sharp_minority_product_inequality_ALL_h=True,
        all_global_minority_product_positive_NOT_PROVED=True,
        original_residual_threeflag_Hall_positive_NOT_PROVED=True,
        selected_original_seven_GF5_sixQ_s6_NOT_PROVED=True,
    )


def exact_TRUE_original_twoport_marginal_repair_frontier(model):
    """Complete finite real symplectic original W32/W34 point+line
    typed globally injected f,g, same actual source GQ incidence.

    Compute actual GOOD original D bin table by literal true-source
    neighbor physical port IDs. Compare local exact opposite vs sharp
    ONLY-MARGINAL lower and the independent parent's ALL-D transport.
    """
    G,good,neighbors,badP,badL=_good_D_edge_graph(model)
    inc,left,right=G["inc"],G["left"],G["right"]
    gross=degree_sq=0
    sharp=minority=active=opposite=0
    strict_marginal_slack=0
    zero_active=0
    row_port_zero=col_port_zero=0
    port_hadamard=Counter()
    act_hist=Counter()
    tight_centers=0
    for i,row in enumerate(neighbors):
        p,l=inc[i]
        left_ports={v:j for j,v in enumerate(sorted(left[p]))}
        right_ports={v:j for j,v in enumerate(sorted(right[l]))}
        bins=[0,0,0,0]
        for j,cp,cl in row:
            if (cp not in left_ports or cl not in right_ports):
                raise AssertionError("true globally assigned original physical port not on center factor")
            bins[2*left_ports[cp]+right_ports[cl]]+=1
        x00,x01,x10,x11=_validate_port_bins(bins)
        D=sum(bins)
        r0=x00+x01;r1=x10+x11
        c0=x00+x10;c1=x01+x11
        q=exact_sharp_integer_twoport_marginal_lower(r0,r1,c0,c1)
        ri=x00*x11+x01*x10
        lo=q["exact_SHARP_fixed_both_marginals_minimum_opposite_wedges"]
        mn=q["uniform_half_minorities_CEILING_lower"]
        if ri<lo or lo<mn:
            raise AssertionError("genuine original true D twoport sharp lower failed")
        row_is_active=min(r0,r1)>0
        col_is_active=min(c0,c1)>0
        if (ri>0)!=(row_is_active and col_is_active):
            raise AssertionError("original GOOD opposite twoport iff row and col both physically active")
        # Parent AA4-AR has a quadratic polarized identity in
        # different orthogonal coordinates. This is SAME prior identity
        # in point/line port margins, not claimed a new algebraic law.
        A=r0-r1;B=c0-c1;C=x00+x11-x01-x10
        if 8*ri!=D*D+C*C-A*A-B*B:
            raise AssertionError("original source Hadamard four-port identity")
        port_hadamard["D2"]+=D*D
        port_hadamard["A2"]+=A*A
        port_hadamard["B2"]+=B*B
        port_hadamard["C2"]+=C*C
        gross+=D*(D-1)//2
        degree_sq+=D*D
        sharp+=lo
        minority+=mn
        opposite+=ri
        active+=int(row_is_active and col_is_active)
        zero_active+=int(not(row_is_active and col_is_active))
        row_port_zero+=int(not row_is_active)
        col_port_zero+=int(not col_is_active)
        strict_marginal_slack+=ri-lo
        tight_centers+=int(ri==lo)
        act_hist[(r0,r1,c0,c1)]+=1
    if 8*opposite!=port_hadamard["D2"]+port_hadamard["C2"]-port_hadamard["A2"]-port_hadamard["B2"]:
        raise AssertionError("global original fourport Hadamard energy")
    if not opposite>=sharp>=minority>=active:
        raise AssertionError("original physical port transfer chain violated")
    if gross != (degree_sq-2*len(good))//2:
        raise AssertionError("original source centered wedge handshake")
    parent=exact_true_original_good_D_source_multiplicity_partition(model)
    if parent["source_all_GOOD_centered_two_D_edge_wedges"]!=gross:
        raise AssertionError("source A/A GOOD 3flags and physical port energy same original D source graph")
    if opposite>parent["source_AA_three_distinct_point_and_line_GOOD_D_wedges"]:
        raise AssertionError("physical opposite wedge not TRUE ORIGINAL source A/A")
    # Other parent transports ALL D pairs; our more restrictive GOOD
    # subset must never have more physically opposite wedges.
    allD=exact_original_corrected_two_type_four_bin_transport(model)
    if opposite>allD["genuine_original_ALL_D_two_typed_physically_opposite_wedges"]:
        raise AssertionError("GOOD source D opposite wedges exceed ALL source D")
    return dict(
        s=G["s"],
        N_genuine_original_source_incidence_flags=len(inc),
        actual_original_GOOD_D_edges=len(good),
        all_actual_original_GOOD_centered_source_wedges=gross,
        parent_real_source_AA_good_wedges=parent[
          "source_AA_three_distinct_point_and_line_GOOD_D_wedges"],
        physically_opposite_ACTUAL_original_GOOD_D_centered_3flag_wedges=opposite,
        independently_all_D_physical_opposite_wedge_count=allD[
          "genuine_original_ALL_D_two_typed_physically_opposite_wedges"],
        exact_only_port_marginal_sharp_lower=sharp,
        universal_half_minority_product_ceiling_sum_lower=minority,
        number_of_both_physical_ports_active_TRUE_source_centers=active,
        number_of_no_opposite_eligible_TRUE_source_centers=zero_active,
        number_point_port_monochromatic_centers=row_port_zero,
        number_line_port_monochromatic_centers=col_port_zero,
        true_original_centered_marginal_lower_slack= strict_marginal_slack,
        count_centers_attaining_sharp_same_marginal_lower=tight_centers,
        all_original_center_port_marginal_histogram=dict(act_hist),
        hadamard_degree_and_signed_color_imbalance_energy=dict(port_hadamard),
        exactly_TRUE_original_8R_D2_plus_C2_minus_A2_minus_B2=True,
        all_h_every_global_f_g_sharp_twoport_marginal_transfer_proved=True,
        no_all_global_minority_positive_lower_YET=True,
        positive_wedges_not_the_same_as_seven_GF5_sixID_Q=True,
    )
