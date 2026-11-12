"""HYP-105 #230 AA4-NBRCHARGE: genuine ORIGINAL middle overlap neighborhoods.

New ALL-h fixed-correlated-source lemmas (not the root theorem):
 For real proper physical P3s with fixed ordered endpoints u,v let
 w_i = sum of exact positive source selector marginals for middle ORIGINAL
 source flag i=(p,l), W=sum_i w_i, M=W^2 and D=sum_gamma p_gamma^2.
 Let H_ij = 1 if f(p_i) intersects f(p_j) OR g(l_i) intersects g(l_j);
 H_ii=1. Then R=Ox+Oy-Oxy=sum_ij H_ij w_iw_j, G00=M-R and
 full G=M-R+D+G11, B=R-D-G11 (previous #760 exact identity).

 NEW independent O(q) per occupied original middle flag local charge:
 N_i = X_x1+X_x2-P_p+Y_y1+Y_y2-L_l
   - [sum_xy in f(p)xg(l) Z_xy - sum_y in g(l) U_py
      -sum_x in f(p) V_lx + w_i]
 = sum_{j:H_ij=1} w_j.
 Thus R=sum_i w_i N_i. This is independently checked against actual
 source-flag inverted-label adjacency postings and source moments.
 If B_uv/M_uv>3/4, then SOME original middle i has
 N_i/W>3/4+(D+G11)/M. The closed source overlap neighborhood of i
 is at most d=1+min(F-1,2*((2a-3)*(s+1)-1)) flags (root minimal a),
 and is true named GQ ORIGINAL point/line source flags, no fake owners.
 Each nonempty endpoint source group has d_uv<=d; Laplacian identity
 R=sum_i d_i w_i²-sum_{i<j,H_ij=1}(w_i-w_j)^2
 plus spectral/top-mass source bounds. Neither implies all-label
 weighted global B/M<3/4 without a GQ-endpoint concentration bound.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
import json

from hyp105_original_full_w34_weighted_risk_referee import (
    _source, _true_original_proper_P3, _rank_probability3
)
from hyp105_original_symbol_secondmoments_referee import (
    _potential_original_middle_label_overlap_degree_bound,
    _minimal_pair_alphabet
)

SCHEMA="mathlab.hyp105.original-middle-overlap-neighborhood-charge.v1"
STATUS="OPEN_WITH_FORMAL_BLOCKER"
CASES=((2,"lex","full"),(2,"reverse","full"),(2,"shift","Z17"),
       (4,"lex","full"),(4,"reverse","full"),(4,"shift","full"),
       (4,"lex","even"),(4,"shift","Z17"))


def _sq(weights):
    return sum((x*x for x in weights.values()),Fraction(0))


def _one_true_source_endpoint_charge(group,c):
    if not group:
        raise ValueError("a genuine nonempty physical endpoint family required")
    f=c["f"];g=c["g"];flags=c["flags"]
    by_mid=defaultdict(Fraction)
    x_occ=defaultdict(Fraction);y_occ=defaultdict(Fraction)
    xy_occ=defaultdict(Fraction);point_occ=defaultdict(Fraction)
    line_occ=defaultdict(Fraction)
    py_occ=defaultdict(Fraction);lx_occ=defaultdict(Fraction)
    first=defaultdict(Fraction);last=defaultdict(Fraction)
    fp=defaultdict(Fraction);fl=defaultdict(Fraction);fi=defaultdict(Fraction)
    lp=defaultdict(Fraction);ll=defaultdict(Fraction);li=defaultdict(Fraction)
    D=Fraction(0)
    expected_ends=(group[0][0][0],group[0][0][-1])
    for path,owners,w in group:
        if len(path)!=4 or len(owners)!=3 or not isinstance(w,Fraction) or w<=0:
            raise AssertionError("not a genuine positive ORIGINAL three-owner physical P3 marginal")
        if (path[0],path[-1])!=expected_ends:
            raise AssertionError("incompatible physical endpoints supplied in one source bin")
        i=owners[1];p,l=flags[i]
        a,b=path[1],path[2]
        if tuple(sorted((a[0],b[0])))!=f[p] or tuple(sorted((a[1],b[1])))!=g[l]:
            raise AssertionError("physical original middle directed edge source inverse failed")
        by_mid[i]+=w;D+=w*w
        first[a]+=w;last[b]+=w
        fp[(p,a)]+=w;fl[(l,a)]+=w;fi[(i,a)]+=w
        lp[(p,b)]+=w;ll[(l,b)]+=w;li[(i,b)]+=w
    W=sum(by_mid.values(),Fraction(0));M=W*W
    for i,w in by_mid.items():
        p,l=flags[i]
        point_occ[p]+=w;line_occ[l]+=w
        for x in f[p]:
            x_occ[x]+=w;lx_occ[(l,x)]+=w
        for y in g[l]:
            y_occ[y]+=w;py_occ[(p,y)]+=w
        for x in f[p]:
            for y in g[l]:
                xy_occ[(x,y)]+=w
    if sum(x_occ.values(),Fraction(0))!=2*W or sum(y_occ.values(),Fraction(0))!=2*W:
        raise AssertionError("genuine paired ORIGINAL middle coordinates not twice weight")
    postings_x=defaultdict(set);postings_y=defaultdict(set)
    for i in by_mid:
        p,l=flags[i]
        for x in f[p]:postings_x[x].add(i)
        for y in g[l]:postings_y[y].add(i)
    q=len(by_mid)
    neighborhood={}
    weighted_neighbor={}
    independent_symbol_formula={}
    degrees={}
    delta=0
    sum_weighted_d_sq=Fraction(0)
    R_direct=Fraction(0)
    first_heavy=None
    for i,w in by_mid.items():
        p,l=flags[i]
        xn=set().union(*(postings_x[x] for x in f[p]))
        yn=set().union(*(postings_y[y] for y in g[l]))
        neigh=xn|yn
        if i not in neigh:
            raise AssertionError("closed source ORIGINAL middle overlap neighborhood omitted itself")
        N=sum((by_mid[j] for j in neigh),Fraction(0))
        # SECOND COMPLETELY INDEPENDENT O(1)-postings arithmetic oracle:
        SX=sum((x_occ[x] for x in f[p]),Fraction(0))-point_occ[p]
        SY=sum((y_occ[y] for y in g[l]),Fraction(0))-line_occ[l]
        SXY=(sum((xy_occ[(x,y)] for x in f[p] for y in g[l]),Fraction(0))
             -sum((py_occ[(p,y)] for y in g[l]),Fraction(0))
             -sum((lx_occ[(l,x)] for x in f[p]),Fraction(0))+w)
        formula=SX+SY-SXY
        if formula!=N or not w<=N<=W:
            raise AssertionError("two independent true ORIGINAL overlap neighborhood mass oracles disagree")
        degrees[i]=len(neigh)
        neighborhood[i]=neigh
        weighted_neighbor[i]=N
        independent_symbol_formula[i]=formula
        delta=max(delta,len(neigh))
        sum_weighted_d_sq+=len(neigh)*w*w
        R_direct+=w*N
    if not 1<=delta<=q:
        raise AssertionError("genuine original occupied source neighborhood size invalid")
    # A THIRD independent source moment-squared global double count:
    Ox=_sq(x_occ)-_sq(point_occ)
    Oy=_sq(y_occ)-_sq(line_occ)
    Oxy=_sq(xy_occ)-_sq(py_occ)-_sq(lx_occ)+_sq(by_mid)
    R_moment=Ox+Oy-Oxy
    if R_direct!=R_moment or not 0<=R_direct<=M:
        raise AssertionError("source rank exact pair-label union mismatch: 3 independent overlap oracles")
    # Full original shared-corner compatible mass; no J or pairs-of-paths:
    G11=(_sq(first)-_sq(fp)-_sq(fl)+_sq(fi)
         +_sq(last)-_sq(lp)-_sq(ll)+_sq(li))
    G=M-R_direct+D+G11
    B=M-G
    if not 0<=B<=M or G<D or G11<0:
        raise AssertionError("source all-h G/B positivity and original diagonal conservation failed")
    # Weighted source graph Laplacian identity (loops vanish in the energy).
    lap=Fraction(0)
    for i,j in combinations(sorted(by_mid),2):
        if j in neighborhood[i]:
            if i not in neighborhood[j]:
                raise AssertionError("false asymmetric source label overlap neighborhood")
            lap+=(by_mid[i]-by_mid[j])**2
    if sum_weighted_d_sq-R_direct!=lap:
        raise AssertionError("ALL-h named ORIGINAL middle overlap Laplacian energy identity false")
    Q=_sq(by_mid)
    max_single=max(by_mid.values())
    rho=max(weighted_neighbor.values())/W
    top_mass=sum(sorted(by_mid.values(),reverse=True)[:delta],Fraction(0))
    capacity=_potential_original_middle_label_overlap_degree_bound(c["s"],c["a"])
    d_global=1+capacity["unweighted_source_middle_pair_overlap_max_degree_cap"]
    if delta>d_global or q>len(c["ids"]):
        raise AssertionError("genuine source overlap neighborhood degree exceeds all-h minimal-alphabet capacity")
    # Four independent ALL-h upper constraints on the exact overlap R:
    spectral=delta*Q
    top=W*top_mass
    max_weight=delta*W*max_single
    weighted_max=rho*M
    if any(R_direct>bound for bound in (spectral,top,max_weight,weighted_max)):
        raise AssertionError("ALL-h source weighted overlap degree/mass/spectral upper false")
    # If exact B exceeds 75%, necessarily SOME closed source middle
    # neighborhood carries > 75% of W plus the exact D+G11 correction.
    threshold=Fraction(3,4)+(D+G11)/M
    candidate_heavy=rho>=threshold
    safe_from_rho=rho<threshold
    if B/M>Fraction(3,4) and not rho>threshold:
        raise AssertionError("strict original B75 BAD endpoint without source heavy middle-neighborhood witness")
    if safe_from_rho and not B/M<Fraction(3,4):
        raise AssertionError("strict safe B75 neighborhood test emitted unsupported false conclusion")
    degree_upper_B=sum_weighted_d_sq-D-G11
    spectral_safe=degree_upper_B<3*M/4
    if spectral_safe and not B/M<Fraction(3,4):
        raise AssertionError("source graph weighted-degree risk upper falsely classified endpoint safe")
    # Source top-d middle owner test, coarser than exact max neighborhood:
    top_safe=top-D-G11<3*M/4
    if top_safe and not B/M<Fraction(3,4):
        raise AssertionError("source middle overlap top-d risk cap falsely certified safe")
    witness_id=max(weighted_neighbor,key=weighted_neighbor.get)
    witness_p,witness_l=flags[witness_id]
    return {
        "M":M,"G":G,"B":B,"D":D,"G11":G11,"R":R_direct,
        "R_middle_symbol_second_moments":R_moment,
        "Q_original_middle_flag_group_energy":Q,
        "delta_occupied_original_middle_flag_overlap_closed_degree":delta,
        "all_h_source_overlap_degree_capacity_including_self":d_global,
        "source_middle_flag_effective_support":M/Q,
        "weighted_source_neighbor_max_fraction":rho,
        "top_degree_source_middle_weight_fraction":top_mass/W,
        "source_laplacian_nonnegative_variance":lap,
        "source_weighted_degree_square_energy":sum_weighted_d_sq,
        "source_spectral_degree_R_upper":spectral,
        "source_top_degree_R_upper":top,
        "source_max_single_group_R_upper":max_weight,
        "source_max_neighbor_R_upper":weighted_max,
        "actual_strict_local_BAD_B_gt_three_quarters":B/M>Fraction(3,4),
        "source_heavy_neighborhood_necessary_candidate":candidate_heavy,
        "source_max_neighbor_strict_SAFE_certificate":safe_from_rho,
        "source_weighted_degree_strict_SAFE_certificate":spectral_safe,
        "source_top_degree_strict_SAFE_certificate":top_safe,
        "source_bad_threshold_heavy_neighborhood_fraction":threshold,
        "nonempty_source_middle_flags":q,
        "paths":len(group),
        "witness_middle_flag":witness_id,
        "witness_middle_point":witness_p,
        "witness_middle_line":witness_l,
        "witness_middle_f_label":list(f[witness_p]),
        "witness_middle_g_label":list(g[witness_l]),
        "witness_max_neighborhood_source_flag_count":degrees[witness_id],
        "witness_max_neighborhood_source_weight":weighted_neighbor[witness_id],
        "witness_original_source_flag_ids":sorted(neighborhood[witness_id])
    }


def _one_full_original_source_case(s,scheme,core):
    c=_source(s,scheme,core)
    bins=defaultdict(list)
    rank={}
    for physical,owners in _true_original_proper_P3(c):
        source=tuple(sorted(owners))
        if source not in rank:
            rank[source]=_rank_probability3(source,c["J"])/64
        bins[(physical[0],physical[-1])].append((physical,owners,rank[source]))
    if not bins:
        raise AssertionError("empty genuine original physical P3 population")
    sums=defaultdict(Fraction)
    counts=defaultdict(int)
    M_bad=M_heavy=M_rho_safe=M_degree_safe=M_top_safe=Fraction(0)
    first_bad=None
    max_src_degree=0
    for ends,group in bins.items():
        z=_one_true_source_endpoint_charge(group,c)
        for key in ("M","G","B","D","G11","R","Q_original_middle_flag_group_energy",
                    "source_laplacian_nonnegative_variance","source_weighted_degree_square_energy",
                    "source_spectral_degree_R_upper","source_top_degree_R_upper",
                    "source_max_single_group_R_upper","source_max_neighbor_R_upper"):
            sums[key]+=z[key]
        counts["real_physical_ordered_endpoints"]+=1
        counts["full_real_original_proper_directed_P3s"]+=len(group)
        counts["nonempty_original_middle_owner_groups"]+=z["nonempty_source_middle_flags"]
        max_src_degree=max(max_src_degree,z["delta_occupied_original_middle_flag_overlap_closed_degree"])
        if z["actual_strict_local_BAD_B_gt_three_quarters"]:
            M_bad+=z["M"]
            counts["actual_local_strict_bad_endpoint_bins"]+=1
            if first_bad is None:
                first_bad={
                    "endpoints":[list(ends[0]),list(ends[1])],
                    "B_over_M":str(z["B"]/z["M"]),
                    "max_neighborhood_relative_weight":str(z["weighted_source_neighbor_max_fraction"]),
                    "necessary_relative_threshold":str(z["source_bad_threshold_heavy_neighborhood_fraction"]),
                    "witness_original_middle_flag":z["witness_middle_flag"],
                    "witness_middle_f_label":z["witness_middle_f_label"],
                    "witness_middle_g_label":z["witness_middle_g_label"],
                    "witness_neighborhood_original_flag_count":
                        z["witness_max_neighborhood_source_flag_count"],
                    "witness_source_flag_ids":z["witness_original_source_flag_ids"]
                }
        if z["source_heavy_neighborhood_necessary_candidate"]:
            M_heavy+=z["M"]
            counts["source_heavy_neighborhood_candidate_endpoint_bins"]+=1
        if z["source_max_neighbor_strict_SAFE_certificate"]:
            M_rho_safe+=z["M"]
            counts["source_max_neighborhood_certified_strict_safe_bins"]+=1
        if z["source_weighted_degree_strict_SAFE_certificate"]:
            M_degree_safe+=z["M"]
            counts["source_degree_square_certified_strict_safe_bins"]+=1
        if z["source_top_degree_strict_SAFE_certificate"]:
            M_top_safe+=z["M"]
            counts["source_top_degree_mass_certified_strict_safe_bins"]+=1
    M=sums["M"];G=sums["G"];B=sums["B"];D=sums["D"]
    R=sums["R"];G11=sums["G11"]
    if not M>0 or not G>0 or B<0 or G+B!=M or B!=R-D-G11:
        raise AssertionError("ALL-h ORIGINAL complete source mass charge not consistent")
    if not 0<=M_bad<=M_heavy<=M or not 0<=M_rho_safe<=M:
        raise AssertionError("source heavy neighborhood bad endpoint containment false")
    if M_rho_safe+M_bad>M or M_degree_safe+M_bad>M or M_top_safe+M_bad>M:
        raise AssertionError("source degree/neighbor/source top-d false strict B75 certification")
    if M_rho_safe!=M-M_heavy:
        # Strict good rho gate rho<threshold and heavy candidate rho>=
        raise AssertionError("source overlap neighborhood strict safe/candidate partition inconsistent")
    if not 0<=max_src_degree<=1+_potential_original_middle_label_overlap_degree_bound(
            s,c["a"])["unweighted_source_middle_pair_overlap_max_degree_cap"]:
        raise AssertionError("observed original overlap degree exceeds full-source alphabet bound")
    return {
        "original_s":s,"original_scheme":scheme,"original_CORE":core,
        "original_minimal_alphabet":c["a"],
        "original_GQ_named_flags":len(c["flags"]),
        "source_retained_CORE_original_flags":len(c["ids"]),
        "actual_source_real_physical_diagonal_edges":len(c["owner"]),
        "source_priority_original_triple_sets":len(rank),
        "complete_original_actual_path_census":True,
        "moments":{k:str(v) for k,v in sorted(sums.items())},
        "total_M":str(M),"total_G":str(G),"total_B":str(B),
        "exact_B_over_M":str(B/M),
        "original_neighborhood_overlap_R_over_M":str(R/M),
        "source_heavy_neighborhood_candidate_M_share":str(M_heavy/M),
        "source_max_neighborhood_strict_SAFE_M_share":str(M_rho_safe/M),
        "source_weighted_degree_strict_SAFE_M_share":str(M_degree_safe/M),
        "source_top_degree_strict_SAFE_M_share":str(M_top_safe/M),
        "actual_source_strict_local_bad_M_share":str(M_bad/M),
        "max_occupied_middle_original_flag_overlap_closed_degree":max_src_degree,
        "source_overlap_all_h_minimal_alphabet_capacity":
            _potential_original_middle_label_overlap_degree_bound(s,c["a"]),
        "first_actual_bad_real_original_source_neighborhood_witness":first_bad,
        "counts":dict(sorted(counts.items())),
        "root_PROVED_A":False,
        "all_h_global_B_over_M_below_three_quarters_PROVED":False
    }


def canonical_report():
    rows=[_one_full_original_source_case(*case) for case in CASES]
    expected=[1346,1154,838,83892,82846,79404,9966,66418]
    if [x["counts"]["full_real_original_proper_directed_P3s"] for x in rows]!=expected:
        raise AssertionError("full real original W32/W34 path population differs from independently established source")
    return {
        "schema":SCHEMA,"issue":230,"status":STATUS,
        "all_h_source_closed_overlap_neighborhood_exact_postings_and_symbol_moment_mass":True,
        "all_h_original_point_line_source_pair_label_overlap_degree_capacity":True,
        "all_h_weighted_neighborhood_Laplacian_variance_and_spectral_upper":True,
        "all_h_strict_local_BAD_B75_forces_one_heavy_original_middle_neighborhood":True,
        "all_h_global_BAD_B75_forces_some_local_heavy_original_middle_neighborhood":True,
        "this_does_NOT_claim_all_h_uniform_75_percent_good_mass":True,
        "root_PROVED_A":False,
        "all_h_global_B_over_M_below_three_quarters_PROVED":False,
        "ASET_exponent_claimed":False,
        "infinite_correlated_counterfamily_claimed":False,
        "true_original_W32_W34_full_source_neighborhood_censuses":rows
    }


if __name__=="__main__":
    print("AA4_NBRCHARGE_CERTIFICATE="+json.dumps(canonical_report(),sort_keys=True,separators=(",",":")))
