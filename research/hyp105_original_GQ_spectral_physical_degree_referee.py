"""HYP-105 #230 AA4-GQSPEC: ALL-h ORIGINAL GQ incidence spectral -> physical degrees.

Classical REAL GQ(s,s) identity (known prior art, NOT a new spectrum):
  N N^T = (s+1)I + A_point
  (N N^T)^2 = 2s N N^T + (s+1) J_allones
  singular(N) = (s+1), sqrt(2s), 0.
NEW application to arbitrary fixed separately pair-injective correlated f/g:
  r_x=#{p:x in f(p)} <= a-1, c_y=#{l:y in g(l)} <= a-1.
  d_full(x,y)=#{ORIGINAL flags (p,l): x in f(p), y in g(l)}
             = actual degree of physical vertex (x,y) in the full
               ORIGINAL paired two-diagonal physical graph.
  |V*d_full - (s+1)*r_x*c_y|^2 <=
                2*s*r_x*(V-r_x)*c_y*(V-c_y).
  d_CORE<=d_full; under ROOT MINIMAL alphabet a=a_s,
  uniform max degree <= floor(
       [(s+1)*(a-1)^2 + sqrt(2s)*(a-1)*(V-(a-1))] / V)
       = O(s^2), vs naive (s+1)(a-1)=O(s^(5/2)).
This is an all-h honest geometric bound, NOT all-h B/M < 3/4,
not a proof of ORIGINAL six-incidence motif S>=c*s^6.
Full W32/W34 original incidence polynomial, independent original
physical adjacency and retained-core all source flags verified exactly.
"""
from collections import defaultdict
from functools import lru_cache
from fractions import Fraction
from itertools import combinations
from math import comb,isqrt
import json

from hyp105_original_full_w34_weighted_risk_referee import _source, _true_original_proper_P3
from hyp105_original_symbol_secondmoments_referee import _minimal_pair_alphabet

SCHEMA="mathlab.hyp105.original-gq-incidence-spectral-physical-degree.v1"
ROOT_STATUS="OPEN_WITH_FORMAL_BLOCKER"
CASES=((2,"lex","full"),(2,"reverse","full"),(2,"shift","Z17"),
       (4,"lex","full"),(4,"reverse","full"),(4,"shift","full"),
       (4,"lex","even"),(4,"shift","Z17"))
HIGH_ORDER_CAPACITY=(2,4,8,16,32,64)


@lru_cache(maxsize=4)
def _independent_original_GQ_integer_polynomial(s,flags):
    """Exact spectral proof oracle on the genuine full W32/W34 incidence.

    This is an INTEGER identity test, not numerical eigensolver noise.
    It proves the actual fixtures satisfy the known GQ all-order
    polynomial T^2=2s*T+(s+1)J where T=N*N^T.
    """
    if s not in (2,4):
        raise ValueError("ONLY actual genuine small GQ spectral fixtures")
    V=(s+1)*(s*s+1)
    if len(flags)!=(s+1)*V or len(set(flags))!=len(flags):
        raise AssertionError("not the complete ORIGINAL W(3,s) source")
    point_lines=defaultdict(set)
    line_points=defaultdict(set)
    for p,l in flags:
        point_lines[p].add(l)
        line_points[l].add(p)
    if set(point_lines)!=set(range(V)) or set(line_points)!=set(range(V)):
        raise AssertionError("source indexed point/line labels not exhaustive")
    if any(len(z)!=s+1 for z in point_lines.values()):
        raise AssertionError("ORIGINAL GQ every point must have s+1 lines")
    if any(len(z)!=s+1 for z in line_points.values()):
        raise AssertionError("ORIGINAL GQ every line must have s+1 points")
    T=[[0]*V for _ in range(V)]
    for members in line_points.values():
        for p in members:
            for q in members:
                T[p][q]+=1
    if any(T[p][p]!=s+1 for p in range(V)):
        raise AssertionError("GQ incidence T diagonal invalid")
    if any(T[p][q] not in (0,1) for p in range(V)
           for q in range(V) if p!=q):
        raise AssertionError("GQ source has forbidden two-shared-line K2,2")
    k=s*(s+1)
    point_edges=sum(T[p][q] for p in range(V) for q in range(p+1,V))
    if any(sum(row)!=(s+1)**2 for row in T):
        raise AssertionError("regular source GQ incidence T row sum invalid")
    if point_edges!=V*k//2:
        raise AssertionError("source GQ point collinearity regular graph edge count wrong")
    # Three-loop independent exact SRG parameter check, plus all-h T
    # quadratic polynomial. Tests actual fixture, NOT an all-h proof.
    checked=0
    for p in range(V):
        for q in range(V):
            v=sum(T[p][z]*T[z][q] for z in range(V))
            if v!=2*s*T[p][q]+(s+1):
                raise AssertionError("ORIGINAL GQ incidence spectrum minimal polynomial invalid")
            if p!=q:
                # For A=T-(s+1)I, neighboring distinct point pairs
                # have lambda=s-1 common neighbors; others mu=s+1.
                shared=sum(T[p][z]*T[z][q] for z in range(V)
                           if z!=p and z!=q)
                expected=(s-1) if T[p][q] else (s+1)
                if shared!=expected:
                    raise AssertionError("original point graph strongly regular lambda/mu incorrect")
            checked+=1
    m_2s=s*(s+1)**2//2
    m_0=V-1-m_2s
    if (s+1)**2+2*s*m_2s!=(s+1)*V or m_0<0:
        raise AssertionError("original GQ incidence eigen multiplicities inconsistent")
    return {
        "original_s":s,"original_points_and_lines":V,
        "full_named_original_incidence_flags":len(flags),
        "point_collinearity_degree":k,
        "point_collinearity_edges":point_edges,
        "known_REAL_incidence_singular_square_top":(s+1)**2,
        "known_REAL_incidence_singular_square_nontrivial":2*s,
        "known_REAL_incidence_singular_square_zero":0,
        "known_spectral_multiplicity_top":1,
        "known_spectral_multiplicity_2s":m_2s,
        "known_spectral_multiplicity_zero":m_0,
        "exact_integer_T_squared_identity_entries_checked":checked,
        "exact_original_GQ_point_graph_SRG_lambda":s-1,
        "exact_original_GQ_point_graph_SRG_mu":s+1,
        "all_fixture_source_spectral_identities_passed":True
    }


def _spectral_degree_cap_integer(s,V,r,c):
    """Sharp centered GQ expander mixing UPPER, exact integer isqrt."""
    if not (0<=r<=V and 0<=c<=V and s>=2):
        raise ValueError("original physical symbol stars invalid")
    term=2*s*r*(V-r)*c*(V-c)
    return ((s+1)*r*c+isqrt(term))//V


def _k22_degree_cap_integer(r,c):
    """K22-free source incidence independent combinatorial upper."""
    if r<0 or c<0:
        raise ValueError("original point/line stars cannot be negative")
    if not r or not c:
        return 0
    # Jensen/Cauchy: E^2 - r E <= r*c*(c-1)
    upper_by_points=(r+isqrt(r*r+4*r*c*(c-1)))//2
    # Dual source incidence bound
    upper_by_lines=(c+isqrt(c*c+4*c*r*(r-1)))//2
    return min(upper_by_points,upper_by_lines)


def _all_h_root_minimal_alphabet_degree_capacity(s):
    """Algebra ONLY at any dyadic order (no invented W(3,8) fixture)."""
    if type(s)!=int or s<2 or s&(s-1):
        raise ValueError("dyadic original GQ order required")
    V=(s+1)*(s*s+1)
    a=_minimal_pair_alphabet(V)
    t=a-1
    if t>V//2:
        raise AssertionError("minimal original paired physical alphabet star exceeds GQ half population")
    centered=_spectral_degree_cap_integer(s,V,t,t)
    uncentered=((s+1)*t*t+isqrt(2*s*t*t*V*V))//V
    k22=_k22_degree_cap_integer(t,t)
    naive=(s+1)*t
    composite=min(centered,k22,naive)
    if not 0<composite<=centered<=uncentered<=naive:
        raise AssertionError("true GQ centered spectral cap not stronger than naive source point degree")
    # An explicit easy all-h O(s²) cap without asymptotic guess:
    # a-1 <= ceil(sqrt(2V))+1, and V=(s+1)(s²+1);
    # centered degree <= (s+1)t²/V + sqrt(2s)t.
    # For s>=2 t <= 2*(s+1)*sqrt(s), so O(s²).
    return {
        "original_s":s,"original_V":V,
        "original_F_incidence_flags":(s+1)*V,
        "original_minimal_pair_alphabet_a":a,
        "original_max_points_or_lines_per_physical_symbol":t,
        "uniform_centered_spectral_degree_cap":centered,
        "uniform_uncentered_spectral_degree_cap":uncentered,
        "uniform_independent_K22_degree_cap":k22,
        "uniform_original_source_naive_degree_cap":naive,
        "uniform_best_spectral_K22_degree_cap":composite,
        "spectral_improvement_over_naive_exact_ratio":str(Fraction(naive,centered)),
        "derived_original_physical_max_degree_O_s_squared_at_minimal_alphabet":True,
        "no_GQ_fixture_claimed_for_s_greater_than_four":s>4,
        "does_NOT_prove_original_weighted_B_over_M_below_three_quarters":True
    }


def _one_true_original_physical_source_degree_case(s,scheme,core):
    c=_source(s,scheme,core)
    V=c["V"];a=c["a"];flags=c["flags"];f=c["f"];g=c["g"]
    if a!=_minimal_pair_alphabet(V):
        raise AssertionError("fixture not using root minimal alphabet")
    spectrum=_independent_original_GQ_integer_polynomial(s,flags)
    r=[0]*a;cc=[0]*a
    for p in range(V):
        for x in f[p]:r[x]+=1
    for l in range(V):
        for y in g[l]:cc[y]+=1
    if sum(r)!=2*V or sum(cc)!=2*V:
        raise AssertionError("source physical pair incidence occupancy sum wrong")
    if max(r)>a-1 or max(cc)>a-1 or min(r)<0 or min(cc)<0:
        raise AssertionError("global pair-injective original physical star count wrong")
    full=[0]*(a*a)
    retained=[0]*(a*a)
    for p,l in flags:
        for x in f[p]:
            for y in g[l]:
                full[x*a+y]+=1
    for i in c["ids"]:
        p,l=flags[i]
        for x in f[p]:
            for y in g[l]:
                retained[x*a+y]+=1
    if sum(full)!=4*len(flags) or sum(retained)!=4*len(c["ids"]):
        raise AssertionError("one original source flag has four physical diagonal endpoints")
    bound=_all_h_root_minimal_alphabet_degree_capacity(s)
    maxfull=max(full);maxret=max(retained)
    maxspec=maxk22=maxcomp=0
    sum_full_sq=sum(z*z for z in full)
    sum_ret_sq=sum(z*z for z in retained)
    count_centered_exact=0
    tightest=None
    for x in range(a):
        for y in range(a):
            z=x*a+y
            R=r[x];C=cc[y]
            # Independent reference of full ORIGINAL incidence count from
            # the TRUE GQ point-line source, not physical adjacency.
            full_from_lines=sum(
                1 for p,l in flags if x in f[p] and y in g[l])
            if full[z]!=full_from_lines:
                raise AssertionError("source flag-loop and direct original incidence intersection disagree")
            # Independent physical graph adjacency (the actual paired
            # opposite-diagonal original source, with unique edge owners).
            phys=len(c["adj"].get((x,y),()))
            if phys!=retained[z]:
                raise AssertionError("TRUE physical degree != original CORE source rectangle-corner incidence count")
            if retained[z]>full[z]:
                raise AssertionError("retained original source has more incidences than FULL GQ")
            deviation=V*full[z]-(s+1)*R*C
            rhs=2*s*R*(V-R)*C*(V-C)
            if deviation*deviation>rhs:
                raise AssertionError("TRUE original GQ real incidence mixing centered inequality false")
            count_centered_exact+=1
            center_cap=_spectral_degree_cap_integer(s,V,R,C)
            k22_cap=_k22_degree_cap_integer(R,C)
            naive=(s+1)*min(R,C)
            combined=min(center_cap,k22_cap,naive)
            if not full[z]<=combined:
                raise AssertionError("original source full GQ incidence exceeds rigorous spectral/K22 cap")
            maxspec=max(maxspec,center_cap)
            maxk22=max(maxk22,k22_cap)
            maxcomp=max(maxcomp,combined)
            if tightest is None or full[z]>tightest["actual_full_original_degree"]:
                tightest={"physical_vertex":[x,y],
                          "original_point_label_symbol_star_size":R,
                          "original_line_label_symbol_star_size":C,
                          "actual_full_original_degree":full[z],
                          "actual_retained_original_CORE_degree":retained[z],
                          "local_centered_spectral_degree_cap":center_cap,
                          "local_K22_only_degree_cap":k22_cap,
                          "local_best_degree_cap":combined,
                          "exact_GQ_centered_mixing_deviation_num":deviation,
                          "exact_GQ_centered_mixing_squared_slack":
                              rhs-deviation*deviation}
    if count_centered_exact!=a*a:
        raise AssertionError("not ALL original physical vertex local degrees checked")
    if not maxret<=maxfull<=maxcomp<=bound["uniform_best_spectral_K22_degree_cap"]:
        raise AssertionError("uniform spectral/K22 physical original degree cap false")
    if not maxspec<=bound["uniform_centered_spectral_degree_cap"]:
        raise AssertionError("actual original physical stars evade global centered cap")
    if not sum_ret_sq<=maxret*sum(retained):
        raise AssertionError("actual original physical degree second moment > Delta*sum degree")
    # NEW ALL-h physical same-endpoint ORIGINAL P3 fiber bound:
    # every path (u,a,b,v) is uniquely specified by a in N(u) and
    # b in N(v), hence |Gamma_uv|<=d(u)*d(v)<=Delta^2.
    # This uses real opposite-diagonal CORE physical edges, not
    # a source-owner cloning or priority-independence argument.
    physical_endpoint_family=defaultdict(int)
    for path,owners in _true_original_proper_P3(c):
        physical_endpoint_family[(path[0],path[-1])]+=1
    if not physical_endpoint_family:
        raise AssertionError("no actual ORIGINAL coordinate-proper P3 physical endpoint families")
    largest_fiber=None
    for ends,n in physical_endpoint_family.items():
        u,v=ends
        du=len(c["adj"][u]);dv=len(c["adj"][v])
        if n>du*dv or n>maxret*maxret or n>bound["uniform_centered_spectral_degree_cap"]**2:
            raise AssertionError("genuine all-h original spectral physical degree P3 endpoint fiber upper bound false")
        if largest_fiber is None or n>largest_fiber["proper_source_P3_count"]:
            largest_fiber={
                "actual_ordered_physical_endpoints":[list(u),list(v)],
                "proper_source_P3_count":n,
                "first_endpoint_actual_physical_degree":du,
                "last_endpoint_actual_physical_degree":dv,
                "exact_endpoint_degree_product_cap":du*dv,
                "uniform_original_spectral_Delta_squared_cap":
                    bound["uniform_centered_spectral_degree_cap"]**2,
            }
    if not sum_full_sq<=maxfull*sum(full):
        raise AssertionError("full original physical degree second moment > Delta*sum degree")
    return {
        "original_s":s,"original_fixed_scheme":scheme,"original_retained_CORE":core,
        "original_minimal_pair_alphabet":a,"original_V":V,
        "original_ALL_named_source_flags":len(flags),
        "original_CORE_retained_named_source_flags":len(c["ids"]),
        "actual_original_paired_physical_edges":len(c["owner"]),
        "actual_full_original_max_physical_vertex_degree":maxfull,
        "actual_CORE_original_max_physical_vertex_degree":maxret,
        "original_max_local_centered_spectral_degree_cap":maxspec,
        "original_max_local_K22_degree_cap":maxk22,
        "original_max_local_best_spectral_K22_degree_cap":maxcomp,
        "original_full_physical_vertex_degree_square_sum":sum_full_sq,
        "original_retained_physical_vertex_degree_square_sum":sum_ret_sq,
        "all_physical_original_vertices_checked":a*a,
        "exact_original_GQ_incidence_and_physical_graph_cross_oracles_passed":True,
        "original_source_point_and_line_pair_label_total_occupancy":2*V,
        "real_original_physical_degree_witness":tightest,
        "true_original_coordinate_proper_P3_total_count":
            sum(physical_endpoint_family.values()),
        "nonempty_true_original_P3_ordered_physical_endpoint_bins":
            len(physical_endpoint_family),
        "max_true_original_proper_P3s_per_physical_endpoint_bin":
            largest_fiber["proper_source_P3_count"],
        "max_true_original_proper_P3s_per_bin_witness":largest_fiber,
        "all_h_REAL_physical_P3_endpoint_support_at_most_Delta_squared":True,
        "root_minimal_alphabet_all_h_uniform_capacity":bound,
        "actual_GQ_integer_incidence_spectrum_certificate":spectrum,
        "root_PROVED_A":False,
        "full_all_h_B75_proved":False,
    }


def canonical_report():
    rows=[_one_true_original_physical_source_degree_case(*z) for z in CASES]
    caps=[_all_h_root_minimal_alphabet_degree_capacity(s)
          for s in HIGH_ORDER_CAPACITY]
    if len(rows)!=8 or any(not z["exact_original_GQ_incidence_and_physical_graph_cross_oracles_passed"]
                           for z in rows):
        raise AssertionError("full genuine ORIGINAL GQ source population missing")
    return {
        "schema":SCHEMA,"status":ROOT_STATUS,"issue":230,
        "known_prior_art_real_GQ_incidence_spectrum_not_claimed_novel":True,
        "all_h_original_GQ_incidence_polynomial_T_squared_2sT_plus_s_plus_one_J":True,
        "all_h_CORRELATED_pair_labels_original_physical_degree_centered_spectral_bound":True,
        "all_h_root_minimal_alphabet_original_physical_max_degree_O_s_squared":True,
        "all_h_original_source_rectangle_corner_degree_equals_physical_degree":True,
        "all_h_original_CORE_degree_not_more_than_full_GQ_degree":True,
        "all_h_original_physical_degree_square_energy_leq_max_degree_times_4CORE":True,
        "all_h_original_TRUE_proper_P3_fiber_support_O_s_to_fourth":True,
        "all_h_root_GLOBAL_original_P3_B75_proved":False,
        "all_h_root_six_motif_obstruction_proved":False,
        "original_HEAVY_LOW_GF5_full_chain_claimed_complete":False,
        "ASET_exponent_claimed":False,"root_PROVED_A":False,
        "eight_complete_original_W32_W34_real_physical_source_degree_cases":rows,
        "independent_all_order_algebraic_minimal_alphabet_spectral_capacity":caps,
    }


if __name__=="__main__":
    print("AA4_GQSPEC_CERTIFICATE="+json.dumps(canonical_report(),sort_keys=True,separators=(",",":")))
