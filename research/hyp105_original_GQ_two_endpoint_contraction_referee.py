"""HYP-105 #230 AA4-GQ2EP: ALL-h ORIGINAL two-endpoint incidence contraction.

Given any genuine symplectic W(3,s) with separately globally pair-injective
but arbitrarily correlated fixed source point-pair f and line-pair g maps,
take any real paired ORIGINAL retained incidence CORE. For actual physical
vertices u,v let X_u,Y_u and X_v,Y_v be projections of the TRUE physical
CORE neighbors of each endpoint onto their x- and y-coordinates.

For every ORIGINAL source point p, define phi_uv(p) as the number (0,1,2)
of ORIENTATIONS (a_x,b_x) of its named physical pair f(p) with
a_x in X_u, b_x in X_v and all u_x,a_x,b_x,v_x distinct.
Define psi_uv(l) similarly for genuine source line g(l) and y symbols.

For the ORIGINAL full incidence matrix N and CORE submatrix N_C,
    properP3_uv <= phi_uv^T N_C psi_uv <= phi_uv^T N psi_uv
               <= floor(((s+1)*S_phi*S_psi
                   + sqrt(2s*(V*Q_phi-S_phi^2)*(V*Q_psi-S_psi^2)))/V).
This is the WEIGHTED centered expander-mixing bound with the KNOWN GQ
nontrivial singular value sqrt(2s), not a claim of a new spectrum.
All numbers are exact INTEGERS; no float or guessed randomness.

The first contraction is only an upper bound, NOT an equality: the
coordinate projections can match without actual coupled physical
endpoint adjacency. The difference is recorded as an exact nonnegative
"source orientation-coupling defect", validated independently by
enumerating genuine original four oriented physical middle edges.

The all-h incidence contraction is a REAL two-endpoint input; it does NOT
prove a lower bound on selector-compatible weighted G/M, strict B75
uniformity, original six-motif theorem, or an ASET exponent.
"""
from collections import defaultdict
from fractions import Fraction
from math import isqrt
import json

from hyp105_original_full_w34_weighted_risk_referee import (
    _source,_true_original_proper_P3
)
from hyp105_original_GQ_spectral_physical_degree_referee import (
    _all_h_root_minimal_alphabet_degree_capacity
)

SCHEMA="mathlab.hyp105.original-GQ-two-endpoint-oriented-shadow-contraction.v1"
ROOT_STATUS="OPEN_WITH_FORMAL_BLOCKER"
CASES=((2,"lex","full"),(2,"reverse","full"),(2,"shift","Z17"),
       (4,"lex","full"),(4,"reverse","full"),(4,"shift","full"),
       (4,"lex","even"),(4,"shift","Z17"))


def _oriented_source_pair_star(pairs,neighbors_u,neighbors_v,ucoord,vcoord):
    """All-order f OR g two-endpoint proper coordinate orientation vector."""
    if ucoord==vcoord:
        return tuple(0 for _ in pairs)
    out=[]
    for a,b in pairs:
        if len({ucoord,a,b,vcoord})!=4:
            out.append(0)
            continue
        value=int(a in neighbors_u and b in neighbors_v)
        value+=int(b in neighbors_u and a in neighbors_v)
        if value not in (0,1,2):
            raise AssertionError("genuine original two-symbol orientation multiplicity invalid")
        out.append(value)
    return tuple(out)


def _true_source_two_endpoint_shadow_one_bin(c,ends,proper_count,source_lines=None):
    """Exact source-GQ incidence contraction; NO direct P3 enumeration here."""
    u,v=ends
    if u==v:
        raise AssertionError("proper physical 3path cannot have identical endpoints")
    s=c["s"];V=c["V"];a=c["a"]
    adj=c["adj"];f=c["f"];g=c["g"]
    if source_lines is None:
        source_lines=defaultdict(list)
        for p,l in c["flags"]:
            source_lines[p].append(l)
    Nu=adj.get(u,set());Nv=adj.get(v,set())
    Xu={w[0] for w in Nu};Xv={w[0] for w in Nv}
    Yu={w[1] for w in Nu};Yv={w[1] for w in Nv}
    phi=_oriented_source_pair_star(f,Xu,Xv,u[0],v[0])
    psi=_oriented_source_pair_star(g,Yu,Yv,u[1],v[1])
    Sx=sum(phi);Sy=sum(psi)
    Qx=sum(t*t for t in phi);Qy=sum(t*t for t in psi)
    if Sx*Sx>V*Qx or Sy*Sy>V*Qy:
        raise AssertionError("original endpoint source orientation centered norm negative")
    full=sum(t*sum(psi[l] for l in source_lines[p])
             for p,t in enumerate(phi) if t)
    retained=sum(phi[p]*psi[l] for i in c["ids"]
                 for p,l in (c["flags"][i],))
    if retained>full:
        raise AssertionError("retained source original GQ has more incidences than FULL")
    mean_num=(s+1)*Sx*Sy
    rad=2*s*(V*Qx-Sx*Sx)*(V*Qy-Sy*Sy)
    spectral=(mean_num+isqrt(rad))//V
    # Exact centered weighted GQ mixing inequality; no eigen numeric approx.
    deviation=V*full-mean_num
    if deviation*deviation>rad or full>spectral:
        raise AssertionError("true original GQ two-endpoint weighted spectral mixing violated")
    du=len(Nu);dv=len(Nv)
    degree=du*dv
    if not 0<=proper_count<=retained<=full<=spectral:
        raise AssertionError("true source 3P3 shadow/GQ spectral inequality chain violated")
    if proper_count>degree:
        raise AssertionError("original proper P3 physical endpoint degree-product gate violated")
    root=_all_h_root_minimal_alphabet_degree_capacity(s)
    if proper_count>root["uniform_centered_spectral_degree_cap"]**2:
        raise AssertionError("original source spectral Delta² P3 fiber violated")
    return {
        "actual_proper_P3":proper_count,
        "source_full_GQ_projection_orientation_shadow":full,
        "source_retained_CORE_projection_orientation_shadow":retained,
        "source_WEIGHTED_centered_GQ_spectral_shadow_upper":spectral,
        "source_full_shadow_to_retained_deleted_incidence_gap":full-retained,
        "source_retained_shadow_to_true_physical_coupling_defect":retained-proper_count,
        "source_weighted_spectral_to_full_shadow_slack":spectral-full,
        "source_endpoint_actual_degree_product_upper":degree,
        "source_two_endpoint_min_degree_and_shadow_upper":min(degree,retained),
        "source_two_endpoint_min_degree_and_spectral_upper":min(degree,spectral),
        "original_endpoint_neighbor_first_x_count":len(Xu),
        "original_endpoint_neighbor_last_x_count":len(Xv),
        "original_endpoint_neighbor_first_y_count":len(Yu),
        "original_endpoint_neighbor_last_y_count":len(Yv),
        "source_phi_sum":Sx,"source_psi_sum":Sy,
        "source_phi_square_sum":Qx,"source_psi_square_sum":Qy,
        "source_weighted_GQ_mixing_deviation":deviation,
        "source_weighted_GQ_mixing_squared_slack":rad-deviation*deviation,
        "source_GQ_minimal_alphabet_degree_cap":root["uniform_centered_spectral_degree_cap"],
        "all_h_source_orientation_phi_psi_range_0_to_2":True
    }


def _independent_direct_physical_orientation_source_shadow(c,ends):
    """Independent physically oriented source-flag oracle (test-only).

    Enumerates the FOUR real ORIENTED diagonals of EVERY retained original
    incidence flag, not the phi/psi or previous proper-P3 enumerator.
    Returns (projection-shadow count, actual all-coordinate-proper
    physical P3 count) as independent orientation-level exact integers.
    """
    u,v=ends
    adj=c["adj"]
    Xu={z[0] for z in adj.get(u,set())}
    Yu={z[1] for z in adj.get(u,set())}
    Xv={z[0] for z in adj.get(v,set())}
    Yv={z[1] for z in adj.get(v,set())}
    shadow=actual=0
    for i in c["ids"]:
        p,l=c["flags"][i]
        x0,x1=c["f"][p];y0,y1=c["g"][l]
        for a,b in (((x0,y0),(x1,y1)),((x1,y1),(x0,y0)),
                    ((x0,y1),(x1,y0)),((x1,y0),(x0,y1))):
            if len({u[0],a[0],b[0],v[0]})!=4:
                continue
            if len({u[1],a[1],b[1],v[1]})!=4:
                continue
            if (a[0] in Xu and a[1] in Yu and
                    b[0] in Xv and b[1] in Yv):
                shadow+=1
                if a in adj.get(u,()) and b in adj.get(v,()):
                    actual+=1
    return shadow,actual


def _full_original_source_two_endpoint_case(s,scheme,core):
    c=_source(s,scheme,core)
    source_lines=defaultdict(list)
    for p,l in c["flags"]:
        source_lines[p].append(l)
    # Independent prior original source proper physical P3 enumerator;
    # main two-endpoint source shadow computation does NOT use it.
    path_by_ends=defaultdict(int)
    for path,owners in _true_original_proper_P3(c):
        path_by_ends[(path[0],path[-1])]+=1
    if not path_by_ends:
        raise AssertionError("missing actual true original physical threepaths")
    nsum=sum(path_by_ends.values())
    n2=sum(q*q for q in path_by_ends.values())
    sums=defaultdict(int)
    counts=defaultdict(int)
    worst=None;improvement=None
    max_n=0;max_shadow=0;max_spectral=0;max_degreeprod=0
    for ends,n in path_by_ends.items():
        z=_true_source_two_endpoint_shadow_one_bin(c,ends,n,source_lines)
        max_n=max(max_n,n)
        max_shadow=max(max_shadow,z["source_retained_CORE_projection_orientation_shadow"])
        max_spectral=max(max_spectral,z["source_WEIGHTED_centered_GQ_spectral_shadow_upper"])
        max_degreeprod=max(max_degreeprod,z["source_endpoint_actual_degree_product_upper"])
        for k in ("source_full_GQ_projection_orientation_shadow",
                  "source_retained_CORE_projection_orientation_shadow",
                  "source_WEIGHTED_centered_GQ_spectral_shadow_upper",
                  "source_full_shadow_to_retained_deleted_incidence_gap",
                  "source_retained_shadow_to_true_physical_coupling_defect",
                  "source_weighted_spectral_to_full_shadow_slack",
                  "source_endpoint_actual_degree_product_upper"):
            sums[k]+=z[k]
        sums["source_actual_proper_path_count"]+=n
        sums["source_actual_proper_path_count_square"]+=n*n
        for key,field in (("degree_product_upper_square_sum","source_endpoint_actual_degree_product_upper"),
                          ("retained_middle_projection_upper_square_sum","source_retained_CORE_projection_orientation_shadow"),
                          ("spectral_middle_projection_upper_square_sum","source_WEIGHTED_centered_GQ_spectral_shadow_upper"),
                          ("degree_and_retained_upper_square_sum","source_two_endpoint_min_degree_and_shadow_upper"),
                          ("degree_and_spectral_upper_square_sum","source_two_endpoint_min_degree_and_spectral_upper")):
            sums[key]+=z[field]**2
        if z["source_retained_CORE_projection_orientation_shadow"]<z["source_endpoint_actual_degree_product_upper"]:
            counts["bins_retained_source_shadow_strictly_beats_degree_product"]+=1
            sums["proper_P3_square_weight_on_retained_improved_bins"]+=n*n
        if z["source_WEIGHTED_centered_GQ_spectral_shadow_upper"]<z["source_endpoint_actual_degree_product_upper"]:
            counts["bins_spectral_GQ_shadow_strictly_beats_degree_product"]+=1
            sums["proper_P3_square_weight_on_spectral_improved_bins"]+=n*n
        if z["source_retained_shadow_to_true_physical_coupling_defect"]>0:
            counts["bins_with_NONZERO_original_two_endpoint_projection_coupling_defect"]+=1
        if z["source_full_shadow_to_retained_deleted_incidence_gap"]>0:
            counts["bins_with_positive_original_deleted_incidence_shadow"]+=1
        counts["nonempty_ordered_physical_proper_P3_endpoint_bins"]+=1
        if worst is None or n>worst["actual_proper_P3"]:
            worst={"ordered_physical_endpoints":[list(ends[0]),list(ends[1])],
                   **z}
        relative_gain=z["source_endpoint_actual_degree_product_upper"]-z["source_two_endpoint_min_degree_and_shadow_upper"]
        if improvement is None or relative_gain>improvement["absolute_improvement"]:
            improvement={"ordered_physical_endpoints":[list(ends[0]),list(ends[1])],
                         "absolute_improvement":relative_gain,
                         **z}
    if sums["source_actual_proper_path_count"]!=nsum or sums["source_actual_proper_path_count_square"]!=n2:
        raise AssertionError("genuine source complete P3 endpoint square conservation false")
    if not sums["degree_and_retained_upper_square_sum"]>=n2 or not sums["degree_and_spectral_upper_square_sum"]>=n2:
        raise AssertionError("two-endpoint GQ source Frobenius moment upper bound false")
    if sums["source_full_GQ_projection_orientation_shadow"]!=(
            sums["source_retained_CORE_projection_orientation_shadow"]+
            sums["source_full_shadow_to_retained_deleted_incidence_gap"]):
        raise AssertionError("source full-to-retained original GQ shadow conservation false")
    if sums["source_retained_CORE_projection_orientation_shadow"]!=(
            nsum+sums["source_retained_shadow_to_true_physical_coupling_defect"]):
        raise AssertionError("source original physical endpoint coupling defect identity false")
    return {
        "original_s":s,"original_label_scheme":scheme,"original_retained_CORE":core,
        "original_named_full_GQ_flags":len(c["flags"]),
        "original_named_retained_CORE_flags":len(c["ids"]),
        "original_actual_physical_edges":len(c["owner"]),
        "original_minimal_physical_pair_alphabet":c["a"],
        "exact_TRUE_original_proper_directed_P3s":nsum,
        "exact_original_proper_P3_endpoint_count_square":n2,
        "max_original_true_proper_P3s_same_endpoint_bin":max_n,
        "max_ORIGINAL_retained_two_endpoint_orientation_shadow":max_shadow,
        "max_original_spectral_two_endpoint_orientation_shadow":max_spectral,
        "max_original_actual_endpoint_degree_product":max_degreeprod,
        "exact_full_two_endpoint_source_moments":dict(sorted(sums.items())),
        "counts":dict(sorted(counts.items())),
        "max_real_original_P3_endpoint_witness":worst,
        "max_absolute_ORIGINAL_shadow_vs_degree_improvement_witness":improvement,
        "true_source_GQ_full_core_retained_proper_path_conservation":True,
        "all_h_ROOT_two_endpoint_weighted_B75_proved":False,
        "root_PROVED_A":False
    }


def canonical_report():
    rows=[_full_original_source_two_endpoint_case(*case) for case in CASES]
    baseline=[1346,1154,838,83892,82846,79404,9966,66418]
    if [z["exact_TRUE_original_proper_directed_P3s"] for z in rows]!=baseline:
        raise AssertionError("independent true original full proper P3 population mismatch")
    return {
        "schema":SCHEMA,"issue":230,"status":ROOT_STATUS,
        "classical_GQ_real_incidence_spectrum_not_claimed_novel":True,
        "all_h_original_CORRELATED_two_endpoint_GQ_incidence_weighted_projection_contraction":True,
        "all_h_all_source_retained_and_full_GQ_shadow_ordering":True,
        "all_h_original_weighted_centered_GQ_two_endpoint_spectral_upper":True,
        "all_h_original_two_endpoint_physical_coupling_defect_nonnegative":True,
        "all_h_original_P3_endpoint_count_square_Frobenius_shadow_upper":True,
        "all_h_root_GLOBAL_original_P3_B75_proved":False,
        "all_h_root_original_six_motif_S_s_floor_proved":False,
        "original_HEAVY_LOW_GF5_complete_claimed":False,
        "ASET_exponent_claimed":False,
        "root_PROVED_A":False,
        "eight_complete_genuine_ORIGINAL_W32_W34_two_endpoint_spectral_cases":rows
    }


if __name__=="__main__":
    print("AA4_GQ2EP_CERTIFICATE="+json.dumps(canonical_report(),sort_keys=True,separators=(",",":")))
