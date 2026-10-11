"""HYP-105 C24-B8-G: all-h host-slack-aware pointwise pair certificate.

A ONE global original-right injection into distinct physical K_a edges. The
exact B8-E Johnson coefficient gamma is treated as input; NO independent
sampling of pair indicators or six-incidence motifs. Every returned bound is
an exact rational lower bound on P_2(g), not on S(f,g) without a residual gate.

For MINIMAL hosts (C(a-1,2)<n<=C(a,2)), the unused q=m-n edges satisfy
0<=q<=a-2. Among occupied physical edges the degree of each is in [d-q,d]
after intersection with [0,n-1]. The TOTAL adjacency count has further
exact attainable bounds from the deleted q-edge physical subgraph.
"""
from fractions import Fraction
from itertools import combinations
from math import comb


def minimal_host_capacity(a, n):
    """Exact minimal host, degree interval and *sharp* total adjacency range."""
    if (type(a) is not int or type(n) is not int or a < 4 or
            n < 4 or not comb(a-1,2) < n <= comb(a,2)):
        raise ValueError("minimal K_a host with integers a>=4 and 4<=n<=C(a,2) required")
    m=comb(a,2)
    q=m-n
    degree=2*(a-2)
    lo=max(0,degree-q)
    hi=min(degree,n-1)
    total_full=m*(a-2)
    base=total_full-degree*q
    # Deleted q-edge simple graph H on a physical vertices:
    # E(L(H)) = sum_u C(deg_H(u),2), attaining the displayed extrema.
    deleted_min=max(0,2*q-a)
    deleted_max=comb(q,2)
    A_min=base+deleted_min
    A_max=base+deleted_max
    if not (q<=a-2 and lo<=hi and
            Fraction(n*lo,2)<=A_min<=A_max<=Fraction(n*hi,2)):
        raise AssertionError("physical deleted-edge capacity inconsistent")
    return {
        "a":a, "n":n, "m":m, "unused_physical_edges":q,
        "host_line_graph_degree":degree,
        "occupied_row_degree_min":lo, "occupied_row_degree_max":hi,
        "deleted_line_graph_adjacency_min":deleted_min,
        "deleted_line_graph_adjacency_max":deleted_max,
        "occupied_adjacency_total_min":A_min,
        "occupied_adjacency_total_max":A_max,
        "total_adjacency_extrema_attainable":True,
        "minimal_host_required":True,
    }


def _coefficients(coefficients, n):
    pairs=tuple(combinations(range(n),2))
    if not isinstance(coefficients,dict) or set(coefficients)!=set(pairs):
        raise ValueError("full unordered original-line pair coefficient matrix required")
    if any(type(coefficients[e]) not in (int,Fraction) for e in pairs):
        raise ValueError("exact rational pair coefficients only")
    return {e:Fraction(coefficients[e]) for e in pairs}


def _prepared(coefficients, a, n):
    par=minimal_host_capacity(a,n)
    w=_coefficients(coefficients,n)
    lo,hi=(par["occupied_row_degree_min"],par["occupied_row_degree_max"])
    prefixes=[]
    for i in range(n):
        ordered=sorted(w[(min(i,j),max(i,j))] for j in range(n) if j!=i)
        pref=[Fraction(0)]
        for v in ordered[:hi]:
            pref.append(pref[-1]+v)
        prefixes.append(tuple(pref[lo:hi+1]))
    center=Fraction(4,a+1)*sum(w.values(),Fraction(0))
    return par,w,tuple(prefixes),center


def _dual_bound(par,prefixes,center,shift):
    """Every shift is valid: row-degree relaxation plus exact A range."""
    t=Fraction(shift)
    lo=par["occupied_row_degree_min"]
    adjacency=(par["occupied_adjacency_total_min"] if t>=0
               else par["occupied_adjacency_total_max"])
    row_total=sum((
        min(v-t*(lo+k) for k,v in enumerate(row))
        for row in prefixes),Fraction(0))
    return row_total/2+t*adjacency-center


def certified_pair_degree_lower(coefficients,a,n,*,max_exact_candidates=6000):
    """All-h rational bound; exact 1D degree-relaxation dual when budget permits.

    The best t in this PARTICULAR relaxation occurs at t=0 or where two
    prefix-cost affine pieces cross. Enumerate all such rational breakpoints
    when n*C(hi-lo+1,2)<=budget; otherwise use the certified t=0 value
    (also evaluate min/max original weights) with an explicit nonoptimal flag.
    The cutoff affects *sharpness only*, NEVER validity.
    """
    if type(max_exact_candidates) is not int or max_exact_candidates<1:
        raise ValueError("positive integer breakpoint budget required")
    par,w,rows,center=_prepared(coefficients,a,n)
    lo=par["occupied_row_degree_min"]
    k_count=par["occupied_row_degree_max"]-lo+1
    candidate_upper=n*comb(k_count,2)+1
    all_breakpoints_considered=candidate_upper<=max_exact_candidates
    candidates={Fraction(0)}
    if all_breakpoints_considered:
        for row in rows:
            for i,j in combinations(range(len(row)),2):
                candidates.add((row[j]-row[i])/(j-i))
    elif w:
        candidates.add(min(w.values()))
        candidates.add(max(w.values()))
    best_t=None
    best=None
    naive=_dual_bound(par,rows,center,Fraction(0))
    for t in sorted(candidates):
        value=_dual_bound(par,rows,center,t)
        if best is None or value>best or (value==best and (best_t is None or abs(t)<abs(best_t))):
            best,best_t=value,t
    if best is None or best<naive:
        raise AssertionError("dual lower lost t=0 candidate")
    return {
        "host":par,
        "projected_pair_feature_count":comb(n,2),
        "uncentered_global_pair_lower":best+center,
        "centering_offset":center,
        "certified_global_projection_lower":best,
        "unshifted_row_lower":naive,
        "selected_adjacency_price":best_t,
        "candidate_prices_evaluated":len(candidates),
        "complete_piecewise_linear_dual_scan":all_breakpoints_considered,
        "candidate_upper_bound":candidate_upper,
        "no_claim_global_quadratic_assignment_optimality":True,
        "no_unproved_nonlinear_residual_bound":True,
    }


def evaluate_global_projection(coefficients,physical_right_injection,a):
    """Independent exact contraction using one COMPLETE physical injection."""
    if not isinstance(physical_right_injection,(tuple,list)):
        raise ValueError("complete physical right injection required")
    n=len(physical_right_injection)
    minimal_host_capacity(a,n)
    w=_coefficients(coefficients,n)
    host=set(combinations(range(a),2))
    if (any(type(e) is not tuple or e not in host
            for e in physical_right_injection)
            or len(set(physical_right_injection))!=n):
        raise ValueError("distinct canonical physical host edge images required")
    p=Fraction(4,a+1)
    z={pair:int(bool(set(physical_right_injection[pair[0]]) &
                         set(physical_right_injection[pair[1]])))
       for pair in w}
    return {
        "centered_projection":sum((c*(z[e]-p) for e,c in w.items()),Fraction(0)),
        "occupied_adjacency_count":sum(z.values()),
        "occupied_row_degrees":tuple(sum(z[min(i,j),max(i,j)]
                                         for j in range(n) if i!=j)
                                      for i in range(n)),
    }


def residual_separation_gate(mean,certified_projection_lower,observed_residual):
    """A witnessed R value upper bounds every possible all-g residual floor.

    If mu+L_P+R(g_witness)<=0, NO independent uniform residual lower bound
    can make this particular separated inequality prove S>0.
    This says nothing about whether the genuine S itself has positive min.
    """
    if any(type(v) not in (int,Fraction)
           for v in (mean,certified_projection_lower,observed_residual)):
        raise ValueError("exact rational certificate and pointwise witness required")
    mu,L,r=map(Fraction,(mean,certified_projection_lower,observed_residual))
    threshold=-mu-L
    return {
        "residual_uniform_lower_must_exceed":threshold,
        "witness_residual":r,
        "separated_positive_gate_ruled_out_by_witness":r<=threshold,
        "required_projection_lower_improvement_strictly_more_than":
            max(Fraction(0),threshold-r),
        "not_a_minimum_S_or_residual_estimate":True,
    }
