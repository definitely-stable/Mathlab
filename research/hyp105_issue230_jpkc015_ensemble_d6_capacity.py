"""HYP-105 JPKC-015: exact ensemble D6 and ORIGINAL matching capacity.

J51: for INDEPENDENT uniform GLOBAL point/line injections into K_a
     physical pair labels, every ORIGINAL six-edge incidence matching Q
     is D6 with probability 60*((a)_6/(C(a,2))_6)^2.
J52: all-h ensemble E[D6]=M6(W(3,s))*p and E[D6]~(16/3)s^6
     at the MINIMAL physical pair alphabet a; explicit all-h lower.
J53: independent original bipartite W32 six-matching DP and dual
     physical-cycle count, no seven-census or physical P3 proxy.

NOT a universal all-label minimum; Root A/B and ASET remain OPEN.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from math import comb, factorial, prod
import argparse
import json

from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1b0_seven_signature import R3_CERTIFIED_FLOORS


def falling(n,k):
    if type(n) is not int or type(k) is not int or n<0 or k<0 or k>n:
        raise ValueError("integer n>=k>=0 required")
    return prod(n-j for j in range(k))


def finite_original_geometry(s):
    if type(s) is not int or s<2 or s&(s-1):
        raise ValueError("true prime-power family s=2^h, h>=1 required")
    v=(s+1)*(s*s+1)
    m=v*(s+1)
    a=6
    while comb(a,2)<v:
        a+=1
    N=comb(a,2)
    if not (a>=6 and N>=v and (a==6 or comb(a-1,2)<v)):
        raise AssertionError("not minimal physical pair label alphabet")
    if not (v>=15 and v-10>=v/3 and N<2*v):
        raise AssertionError("all-h large physical alphabet bounds failed")
    return {"s":s,"original_points":v,"original_lines":v,
            "original_degree":s+1,"original_incidence_columns":m,
            "minimal_physical_coordinate_symbols":a,
            "physical_pairs_available":N}


def exact_D6_probability_minimal_alphabet(s):
    geo=finite_original_geometry(s)
    a=geo["minimal_physical_coordinate_symbols"]
    N=geo["physical_pairs_available"]
    p=Fraction(60*falling(a,6)**2,falling(N,6)**2)
    if not 0<p<=1:
        raise AssertionError("source matching to aligned D6 physical-dual probability outside [0,1]")
    return p


def original_six_matching_bounds(s):
    """All-h provable greedy LOWER and source edge-subset UPPER M6."""
    geo=finite_original_geometry(s)
    M=geo["original_incidence_columns"]
    d=geo["original_degree"]
    # A partial size-j bipartite matching forbids no more than 2*j*d
    # original incidences by its selected point/line endpoints.
    ordered_lower=prod(M-2*j*d for j in range(6))
    if ordered_lower<=0:
        raise AssertionError("greedy six original incidence matching lower lost positivity")
    lower=Fraction(ordered_lower,factorial(6))
    upper=comb(M,6)
    if lower>upper:
        raise AssertionError("greedy matching bound violates edge-subset upper")
    return lower,upper


def all_h_ensemble_certificate(s):
    """Exact per-Q expectation, unconditional in the UNIFORM INJECTION ensemble.

    Constrains E[S]>=E[D6], but DOES NOT constrain min_{f,g} S.
    """
    geo=finite_original_geometry(s)
    p=exact_D6_probability_minimal_alphabet(s)
    M6_lower,M6_upper=original_six_matching_bounds(s)
    lower=M6_lower*p
    upper=M6_upper*p
    # For all s>=2:
    # M-10*d >= M/3, where M=V*d and V>=15.
    # (a)_6 >= (a/6)^6, (N)_6<=N^6;
    # a^2>=2V, N<2V, hence (a/N)^12>(2V)^-6.
    # E[D6] >= (s+1)^6/(12*3^6*6^12*2^6).
    explicit=Fraction((s+1)**6,12*3**6*6**12*2**6)
    if not (lower>=explicit>0 and upper>=lower):
        raise AssertionError("rigorous all-h ensemble Omega(s^6) floor regression")
    # Dimensionless diagnostics ARE NOT a proof of the asymptotic limit:
    # the proof follows separately from M6/M^6 ->1/720,
    # a^2/V->2 and N/V->1 under the minimal alphabet.
    return {
        **geo,
        "exact_probability_D6_given_six_distinct_true_original_point_line_factors":
            str(p),
        "greedy_proved_original_six_matching_count_lower":str(M6_lower),
        "combinatorial_original_six_matching_count_upper":str(M6_upper),
        "all_h_rigorous_ensemble_E_D6_lower":str(lower),
        "all_h_rigorous_ensemble_E_D6_upper":str(upper),
        "all_h_simple_explicit_ensemble_E_D6_Omega_s6_lower":str(explicit),
        "asymptotic_exact_ensemble_E_D6_over_s6_limit":"16/3",
        "asymptotic_limit_proof_by_degree_greedy_squeeze":True,
        "full_GQ_global_injective_left_right_labels":True,
        "D6_Gf5_necessary_R3_floor_per_original_sixset":
            R3_CERTIFIED_FLOORS["D6"],
        "GF5_floor_denominator":51**6,
        "all_h_minimum_over_labelings_proved":False,
        "infinite_correlated_low_S_counterexample_found":False,
        "new_ASET_exponent":False,
    }


def exact_original_W32_six_matchings(model, *, swap_bipartition=False,
                                     max_dp_states=100_000):
    """Independent DP over real ORIGINAL source incidence bipartite graph.

    Visit each ORIGINAL point exactly once; skip it or select one of its
    TRUE ORIGINAL incident lines whose ID was not selected earlier.
    Sum final 6-bit right-factor masks to count six DISTINCT point and
    six DISTINCT line edge matchings. No f/g physical pairs or 7-census.
    """
    edges=tuple(tuple(e) for e in model["incidences"])
    if model.get("s")!=2 or len(edges)!=45:
        raise ValueError("independent exact ORIGINAL 6-matching DP is W32 only")
    npoint=len(model["left_labels"])
    nline=len(model["right_labels"])
    if (npoint,nline)!=(15,15):
        raise ValueError("real W32 15 original point/line factors required")
    adj=[set() for _ in range(15)]
    found=set()
    for p,l in edges:
        if p not in range(15) or l not in range(15) or (p,l) in found:
            raise ValueError("simple original source incidence bipartite host required")
        found.add((p,l))
        u,v=(l,p) if swap_bipartition else (p,l)
        adj[u].add(v)
    if any(len(x)!=3 for x in adj):
        raise ValueError("original W32 has 3-regular point/line factors")
    if type(max_dp_states)!=int or max_dp_states<1:
        raise ValueError("positive six-matching dynamic-state budget required")
    dp={0:1}
    for p in range(15):
        nx=dp.copy()
        for mask,count in dp.items():
            if mask.bit_count()>=6:
                continue
            for line in sorted(adj[p]):
                bit=1<<line
                if not mask&bit:
                    nx[mask|bit]=nx.get(mask|bit,0)+count
        if len(nx)>max_dp_states:
            raise ValueError("original source matching DP budget exceeded")
        dp=nx
    mass=sum(cnt for mask,cnt in dp.items() if mask.bit_count()==6)
    if mass<=0 or len(dp)>max_dp_states:
        raise AssertionError("original W32 true 6-matchings invalid")
    return {"true_original_W32_6_matching_count":mass,
            "original_matching_dp_right_masks":len(dp),
            "original_bipartition_swapped":swap_bipartition,
            "real_original_incidence_host_validated":True}


def independent_small_physical_sixcycle_count(a):
    """Physical graph counting by 6-coordinate subset, cycle, slot bijection.

    For a physical six-cycle choose 6 distinct coordinate labels,
    one unoriented Hamiltonian 6-cycle on them, and a bijection from
    six NAMED original incidence positions to its six distinct edges.
    Unlike J51's dual-edge specification, this counts graph cycles.
    """
    if type(a)!=int or a<6:
        raise ValueError("physical six-cycle requires >=6 distinct coordinates")
    return comb(a,6)*(factorial(5)//2)*factorial(6)


def finite_W32_exact_expectation(scheme="lex"):
    if scheme not in ("lex","reverse","S68","S72"):
        raise ValueError("only genuine original W32 fixture accepted")
    model=fixture(1,scheme)
    geo=finite_original_geometry(2)
    if geo["minimal_physical_coordinate_symbols"]!=6:
        raise AssertionError("W32 K6 global physical alphabet")
    dp=exact_original_W32_six_matchings(model)
    mirror=exact_original_W32_six_matchings(model,swap_bipartition=True)
    if dp["true_original_W32_6_matching_count"]!=mirror[
        "true_original_W32_6_matching_count"]:
        raise AssertionError("independent point/line DP disagrees on ORIGINAL 6-matchings")
    a=6
    N=comb(a,2)
    physical_cycle_count=independent_small_physical_sixcycle_count(a)
    if physical_cycle_count!=60*falling(a,6):
        raise AssertionError("independent physical-coordinate cycle count != J51 dual count")
    p=exact_D6_probability_minimal_alphabet(2)
    matching=dp["true_original_W32_6_matching_count"]
    expected=matching*p
    lower,upper=original_six_matching_bounds(2)
    if not lower<=matching<=upper:
        raise AssertionError("original six-source matching count violates independent greedy bounds")
    return {
        "scheme":scheme,"true_original_W32_6_matching_count":matching,
        "W32_original_source_dp_masks":dp["original_matching_dp_right_masks"],
        "independent_swapped_source_matching_dp_equal":True,
        "physical_sixcycle_named_edge_assignment_count":
            physical_cycle_count,
        "independent_graph_cycle_vs_dual_cycle_count_equal":True,
        "exact_uniform_GLOBAL_injection_ensemble_D6_expectation":str(expected),
        "exact_ensemble_Gf5_D6_R3_floor_numerator_expectation":
            str(expected*R3_CERTIFIED_FLOORS["D6"]),
        "mean_not_worst_case":True,
        "actual_fixed_scheme_D6_count_NOT_used_for_ensemble_mean":True,
    }


def report():
    return {"slice":"JPKC-015",
            "finite_W32":finite_W32_exact_expectation(),
            "ensemble_bounds":[all_h_ensemble_certificate(s)
                               for s in (2,4,8,16)],
            "root_A_proved":False,"root_B_constructed":False}


if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--s",type=int)
    ap.add_argument("--scheme",choices=("lex","reverse","S68","S72"))
    a=ap.parse_args()
    out=(all_h_ensemble_certificate(a.s) if a.s is not None else
         finite_W32_exact_expectation(a.scheme) if a.scheme else report())
    print(json.dumps(out,indent=2,sort_keys=True))
