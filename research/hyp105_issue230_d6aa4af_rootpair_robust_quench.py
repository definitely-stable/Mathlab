"""HYP-105 #230 / AA4-AF: robust root-PAIR true-original B/A quenched lower.

NEW LOCAL all-h deterministic first gate for EVERY complete original
physical pair injection f and EVERY actual point root p AND each fixed
pair of different ACTUAL original lines through p, not only in sum.

For s=2^h >=4:
 C4_occ(f(p)) >= 3*C(a-2,4) - m*(a-4)*(a-5),
 m=C(a,2)-V, independent of f(p), other occupied physical labels;
 each physically occupied complementary C4 of singleton source
 factors q1..q4 supports >=max(0,s^4-6*(s+1)^2) actual six-distinct
 ORIGINAL source incidence Q with the pinned two root flags.
 These are true ORIGINAL B/A source forests, no opposite physical-A
 assumption. Sum over actual source root and pinned original flag pair
 is DISJOINT and gives a universal anchored source-support lower.

Under ONE uniform complete GLOBAL independent original line injection
 g, each such Q is right-physical-A with exact
 p_A=70*(a)_6/(K)_6. Consequently every rooted pinned original cohort
 satisfies E_g C_BA(cohort;f,g) >= p_A * C4_floor * source_rook_floor.

For s>=8: even >=s/128 per actual original point and pinned line pair;
sum over V*C(s+1,2) root flag pairs yields >=s^6/256.

This is a NEW uniform ROOT-PAIR-local explicit bound. A prior B3.2
one-sided global sum theorem already gives the stronger leading
conditional mean ~140*s6; do NOT relabel it new or suggest
E_g bound implies every adversarial g. Actual full S(f,g) minimax
remains OPEN and this certificate proves no positive universal g lower.
"""
from fractions import Fraction
from itertools import combinations,product
from math import comb,prod

from hyp105_issue230_proof_audit import parameters
from hyp105_issue230_d6aa4ab_minimax_orbit_normalform import _valid_original_model


def _falling(n,k):
    return prod(n-j for j in range(k))


def rootpair_robust_all_h(s):
    p=parameters(s)
    a,K,V,d=p["a"],p["K"],p["V"],s+1
    n=a-2;m=K-V
    if n<4 or not 0<=m<=a-2:
        raise AssertionError("minimal physical alphabet must supply K_a minus at most a-2 edges")
    full=3*comb(n,4)
    per_missing=(n-2)*(n-3)
    c4_floor=max(0,full-m*per_missing)
    # Four different actual B singleton source points, with original
    # neighborhoods Ai=N(qi) minus the two source root line neighbors.
    # Each |Ai|>=d-1=s and |Ai intersect Aj|<=1 (girth 8).
    # A union bound over six row pairs costs at most d^2 each.
    rook_floor=max(0,s**4-6*d*d)
    # More refined greedy floor from Y5: (s)_4.
    greedy=prod(max(0,s-j) for j in range(4))
    rook_floor=max(rook_floor,greedy)
    raw_min=c4_floor*rook_floor
    probability=Fraction(70*_falling(a,6),_falling(K,6))
    local_mean=raw_min*probability
    total=V*comb(d,2)*local_mean
    # Integer-only inequalities to avoid float approximations/rounding.
    if s>=8:
        assert a>=35 and n>=18
        assert a*a<=4*s**3
        assert rook_floor*2>=s**4
        assert c4_floor*1024>=a**4
        assert probability*pow(a,6)>=70
        assert local_mean>=Fraction(s,128)
        assert total>=Fraction(s**6,256)
    return {
        "s":s,"V":V,"d":d,"a":a,"K":K,
        "missing_physical_edge_images_m":m,
        "root_complement_physical_vertices_n":n,
        "all_full_physical_C4_patterns_per_fixed_pair_root":full,
        "C4_containing_one_marked_missing_complement_edge":per_missing,
        "universal_per_original_root_physical_occupied_C4_floor":c4_floor,
        "GQ_original_per_realized_C4_source_rook_floor":rook_floor,
        "per_fixed_original_root_two_actual_flags_SOURCE_BA_floor":raw_min,
        "exact_uniform_COMPLETE_global_opposite_A_probability":
            str(probability),
        "per_rootpair_eligible_opposite_A_mean_lower":str(local_mean),
        "aggregate_over_actual_GQ_roots_and_flags_mean_lower":str(total),
        "per_rootpair_lower_ge_s_over_128_for_s_ge8":
            s>=8 and local_mean>=Fraction(s,128),
        "aggregate_lower_ge_s6_over_256_for_s_ge8":
            s>=8 and total>=Fraction(s**6,256),
        "all_h_every_actual_root_pair_first_gate_PROVED":s>=4,
        "all_h_quantifier":"forall genuine W3s, forall complete global f, forall actual point p, forall distinct true incident lines l0,l1; one complete uniform GLOBAL g",
        "prior_all_h_global_one_sided_conditional_mean_ALREADY_KNOWN":True,
        "forall_f_forall_g_minimax_lower_NOT_PROVED":True,
    }


def occupied_root_C4_source_factors(model,*,side,root):
    """ACTUAL globally injected physical complement K_{a-2} root C4
    source-factor census; no K_a completeness assumption (W34 m>0).
    Returns four original source factor indices per ACTUAL C4.
    """
    V,a,_=_valid_original_model(model)
    if type(side) is not int or side not in (0,1):
        raise ValueError("typed original point/line side 0 or 1 required")
    if type(root) is not int or not 0<=root<V:
        raise ValueError("genuine original source factor root required")
    labels=tuple(tuple(x) for x in
                 model["left_labels" if side==0 else "right_labels"])
    inv={e:i for i,e in enumerate(labels)}
    excluded=set(labels[root])
    outside=tuple(x for x in range(a) if x not in excluded)
    result=[]
    for verts in combinations(outside,4):
        w,x,y,z=verts
        complete=set(combinations(verts,2))
        for pairing in (
            ((w,x),(y,z)),
            ((w,y),(x,z)),
            ((w,z),(x,y)),
        ):
            C4=tuple(sorted(complete-set(pairing)))
            if all(e in inv for e in C4):
                factors=tuple(inv[e] for e in C4)
                if root in factors or len(set(factors))!=4:
                    raise AssertionError("complete global image inverse missing four unique singleton source factors")
                result.append(factors)
    if len(set(result))!=len(result):
        raise AssertionError("one original B physical C4 counted twice")
    return tuple(result)


def independent_physical_C4_cycle_trace(model,*,side,root):
    """Independent adjacency-based undirected 4cycle walk count =trace/8.

    Enumerate oriented 4-step walks x->y->z->w->x with four different
    physical coordinates. Each undirected C4 has 8 choices of start
    + direction, including W34 physical unused-pair holes.
    """
    V,a,_=_valid_original_model(model)
    if type(side) is not int or side not in (0,1) or (
        type(root) is not int or not 0<=root<V):
        raise ValueError("valid typed original root required")
    labels=tuple(model["left_labels" if side==0 else "right_labels"])
    blocked=set(labels[root])
    adj={i:set() for i in range(a) if i not in blocked}
    for u,v in labels:
        if u in adj and v in adj:
            adj[u].add(v);adj[v].add(u)
    count=0
    for x,xs in adj.items():
        for y in xs:
            for z in adj[y]-{x}:
                for w in adj[z]-{x,y}:
                    count+=int(w in xs)
    if count%8:raise AssertionError("physical 4cycle trace must be 8 times un-oriented C4")
    return count//8


def genuine_W34_rootpair_local_certificate(model,*,side=0,root=0,pinned_offset=0,
                                            check_first_C4=6):
    """Independent real original W34 source neighborhood root certificate.

    For ONE actual original root+fixed TWO distinct original incidence
    flags, every occupied B C4 is checked against the universal
    root-wise lower; sample actual SOURCE rook counts independently
    as a literal four-source incidence assignment with all four
    opposite original source factors distinct. No g-acceptance asserted.
    """
    V,a,_=_valid_original_model(model)
    if model["s"] not in (2,4,8):
        raise ValueError("finite genuine original W3s fixture only")
    if type(check_first_C4) is not int or check_first_C4<1:
        raise ValueError("positive exact original rook sample size required")
    inc=tuple(tuple(x) for x in model["incidences"])
    bysource=[[] for _ in range(V)]
    neighbors=[set() for _ in range(V)]
    for idx,e in enumerate(inc):
        bysource[e[side]].append(idx)
        neighbors[e[side]].add(e[1-side])
    if (type(pinned_offset) is not int
        or not 0<=pinned_offset<comb(len(bysource[root]),2)):
        raise ValueError("valid pair of actual original pinned root flags required")
    pinned=tuple(combinations(bysource[root],2))[pinned_offset]
    forbidden={inc[i][1-side] for i in pinned}
    if len(forbidden)!=2:raise AssertionError("actual original GQ pinned neighbors distinct")
    patterns=occupied_root_C4_source_factors(model,side=side,root=root)
    independent=independent_physical_C4_cycle_trace(model,side=side,root=root)
    if len(patterns)!=independent:
        raise AssertionError("genuine root physical C4 trace versus direct pattern inverse")
    universal=rootpair_robust_all_h(model["s"])
    if len(patterns)<universal["universal_per_original_root_physical_occupied_C4_floor"]:
        raise AssertionError("all-h source physical root C4 occupancy floor violated")
    rook_values=[]
    d=model["s"]+1
    for q in patterns[:check_first_C4]:
        Ai=tuple(tuple(neighbors[i]-forbidden) for i in q)
        if min(map(len,Ai))<d-1:
            raise AssertionError("original GQ root line pair forbids a second point meeting both")
        for i,j in combinations(range(4),2):
            if len(set(Ai[i])&set(Ai[j]))>1:
                raise AssertionError("true original source W3s forbids source C4")
        brute=sum(len(set(t))==4 for t in product(*Ai))
        if brute<universal["GQ_original_per_realized_C4_source_rook_floor"]:
            raise AssertionError("genuine 4-rook source pattern below true original lower")
        rook_values.append(brute)
    return {
        "s":model["s"],"side":side,"root":root,
        "actual_original_pinned_incidence_IDs":pinned,
        "physical_C4_occupied":len(patterns),
        "independent_physical_C4_adj_trace":independent,
        "all_h_universal_C4_floor":
            universal["universal_per_original_root_physical_occupied_C4_floor"],
        "actual_original_four_rook_direct_counts_sample":rook_values,
        "all_h_per_C4_true_original_rook_floor":
            universal["GQ_original_per_realized_C4_source_rook_floor"],
        "actual_root_flagpair_SOURCE_BA_lower":universal[
            "per_fixed_original_root_two_actual_flags_SOURCE_BA_floor"],
        "full_global_opposite_physical_A_sampled_NOT_ASSERTED":True,
        "all_h_every_global_g_lower_NOT_PROVED":True,
    }


if __name__=="__main__":
    import json,argparse
    from hyp105_issue230_projection import fixture
    p=argparse.ArgumentParser()
    p.add_argument("--scheme",choices=("lex","random"),default="lex")
    args=p.parse_args()
    print(json.dumps({"all_h":[rootpair_robust_all_h(1<<h)
                                for h in range(1,11)],
                      "real_W34":[genuine_W34_rootpair_local_certificate(
                          fixture(2,args.scheme),side=t,root=u)
                          for t,u in ((0,0),(1,0))]},
                     indent=2,sort_keys=True))
