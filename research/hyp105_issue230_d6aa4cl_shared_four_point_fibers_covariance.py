"""HYP-105 AA4-CL: exact two-overlapping-POINT-fiber GF5 covariance on ONE original f orbit.

For every genuine symplectic W(3,2^h), any correlated fully injected
complete f,g, choose EIGHT different original POINT factor IDs. Fibers
A=(0,1,2,3,4,5), B=(0,1,2,3,6,7) must both form physical C6 on f.

Use ONE GLOBAL 96-state factor-image orbit G=S4(shared) x S2(Aonly)
x S2(Bonly). All 96 f states preserve BOTH six-edge physical C6
multisets; original LINE map g is fixed and every original sixflag Q
is immutable. This is NOT independent six-factor 720-state averaging.

Historical seven GF5 point-source-A fiber scores are exact
  F_A(sigma,alpha)=B_A+5643 H_A(C_A(sigma,alpha))
  F_B(sigma,beta) =B_B+5643 H_B(C_B(sigma,beta)).
Write conditional shared means u(sigma)=mean_alpha F_A,
v(sigma)=mean_beta F_B. Since G is literally a finite product
of legal complete original source factor image permutations:
  Cov_G(F_A,F_B)=Cov_S4(u,v) EXACTLY (not source Q independence).
For six shared transpositions, their mixed gradients are
  E_G,shared (dF_A*dF_B)=E_S4,shared(du*dv).
The real 24-state S4 transposition graph has Laplacian eigenvalues
0,4,6,8,12. Hence exact Poincare and Cauchy:
  |Cov_G(F_A,F_B)|^2 <= (9/16) D4(u)*D4(v),
D4(u)=mean_(24*6)(u(sigma transposed)-u(sigma))^2.
No asserted sign of covariance or forced full original S positivity.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations,permutations

from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4ch_maximal_d6_fan_physical_gram_nogo import (
    _full_pair_injection,_match_unique,
)
from hyp105_issue230_d6aa4ci_dual_cycle_orbit_fiber_invariant import (
    original_point_A_fiber,_six_position_dual_cycle,W_D,
)
from hyp105_issue230_d6aa4cg_four_shared_edge_two_completion import (
    classify_four_common_completion,classify_seven_all_a_original_Q,
)
from hyp105_issue230_d6aa4ck_dual_cycle_transposition_spectral_energy import (
    _matmul,_fraction_vandermonde_multiplicities,
)
from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1b0_seven_signature import R3_CERTIFIED_FLOORS

SHARED=(0,1,2,3)
FAMILIES={"A":(0,1,2,3,4,5),"B":(0,1,2,3,6,7)}
S4=tuple(permutations(range(4)))
S4_INDEX={p:i for i,p in enumerate(S4)}
SWAPS=tuple(combinations(range(4),2))
ORBIT=tuple((sigma,alpha,beta)
            for sigma in S4 for alpha in range(2) for beta in range(2))
assert len(S4)==24 and len(ORBIT)==96
GRAPH_CASES={
 "four_cycle_switch":(
     ((0,1),(1,2),(3,4),(4,5)),
     ((0,5),(2,3)),
     ((0,3),(2,5))),
 "vertex_replacement":(
     ((0,1),(1,2),(2,3),(3,4)),
     ((4,5),(0,5)),
     ((4,6),(0,6))),
}
EIG_S4=(6,2,0,-2,-6)
MULT_S4=(1,9,4,9,1)
LAP_S4=(0,4,6,8,12)


def shared_internal_dual_adjacencies(cycle):
    """How many true six-incidence-position dual edges lie among 4 common columns.

    This quantity is invariant under any global WHOLE original POINT
    source-image permutation in the 96-state S4×S2×S2 group. It is
    exactly 2 for physical shared-edge four-cycle-switch completion
    and 3 for the shared-five-vertex cherry-center completion,
    independently of physical coordinate names and h.
    """
    if (cycle is None or len(cycle)!=6 or any(
            len(edge)!=2 or not set(edge)<=set(range(6)) for edge in cycle)):
        raise ValueError("actual labeled Hamiltonian ORIGINAL six-position dual required")
    degree=Counter(v for edge in cycle for v in edge)
    if len(degree)!=6 or set(degree.values())!={2}:
        raise ValueError("genuine simple six-position dual 2factor required")
    return sum(set(edge)<=set(range(4)) for edge in cycle)


def s4_swap(sigma,i,j):
    if sigma not in S4_INDEX or (i,j) not in SWAPS:
        raise ValueError("valid S4 shared-original POINT factor swap required")
    out=list(sigma);out[i],out[j]=out[j],out[i]
    return tuple(out)


def _s4_adjacency():
    adj=[[0]*24 for _ in S4]
    for i,sigma in enumerate(S4):
        for k,l in SWAPS:
            j=S4_INDEX[s4_swap(sigma,k,l)]
            adj[i][j]+=1
    if any(sum(row)!=6 for row in adj) or any(
            adj[i][j]!=adj[j][i] for i in range(24) for j in range(24)):
        raise AssertionError("original shared POINT-factor S4 graph not 6regular symmetric")
    if any(adj[i][i] for i in range(24)):raise AssertionError("transposition fixed a shared permutation")
    return tuple(tuple(row) for row in adj)


A_S4=_s4_adjacency()


def exact_shared_S4_spectral_certificate():
    """Exact 24x24 INTEGER annihilator, traces and unique rational eigenspectrum."""
    n=24
    identity=tuple(tuple(int(i==j) for j in range(n)) for i in range(n))
    M=identity;trace=[]
    for k in range(5):
        trace.append(sum(M[i][i] for i in range(n)))
        M=_matmul(M,A_S4)
    if tuple(trace)!=(24,0,144,0,2880):
        raise AssertionError("S4 true original source graph power traces changed")
    M=identity
    for root in EIG_S4:
        factor=tuple(tuple(A_S4[i][j]-(root if i==j else 0)
                           for j in range(n)) for i in range(n))
        M=_matmul(M,factor)
    if any(any(row) for row in M):
        raise AssertionError("exact 24x24 S4 integer spectral polynomial not zero")
    mult=_fraction_vandermonde_multiplicities(EIG_S4,trace)
    if mult!=tuple(Fraction(k) for k in MULT_S4):
        raise AssertionError("S4 source-partial-shared spectrum multiplicities wrong")
    return {"states":24,"allowed_shared_original_POINT_transpositions":6,
            "integer_traces":tuple(trace),"polynomial_zero":True,
            "eigenvalues":EIG_S4,"multiplicities":tuple(int(m) for m in mult),
            "laplacian_eigenvalues":LAP_S4,
            "squared_gradient_poincare_lower":Fraction(4,3),
            "mixed_covariance_squared_coefficient":Fraction(9,16),
            "nonlazy_simple_walk_centered_contraction_false":True}


def complete_overlapping_global_f(f,point_ids,state):
    """Reassign 8 WHOLE original POINT-factor physical images ONCE globally."""
    pts=tuple(point_ids)
    if len(pts)!=8 or len(set(pts))!=8 or any(
        type(i) is not int or not 0<=i<len(f) for i in pts):
        raise ValueError("eight different REAL original POINT factor IDs required")
    if not isinstance(state,tuple) or len(state)!=3:
        raise ValueError("one jointly legal original S4 x S2 x S2 state needed")
    sigma,alpha,beta=state
    if sigma not in S4_INDEX or type(alpha) is not int or type(beta) is not int or alpha not in (0,1) or beta not in (0,1):
        raise ValueError("invalid globally consistent overlap shared SOURCE factor state")
    edges=tuple(tuple(sorted(e)) for e in f)
    if len(set(edges))!=len(edges):
        raise ValueError("WHOLE original POINT image map must be injective")
    ordered=tuple(edges[p] for p in pts)
    mapped=tuple(ordered[sigma[i]] for i in range(4))+(
        ordered[4+alpha],ordered[5-alpha],
        ordered[6+beta],ordered[7-beta])
    out=list(edges)
    for p,e in zip(pts,mapped):out[p]=e
    if len(set(out))!=len(out) or set(out)!=set(edges):
        raise AssertionError("two original families must use same globally injected f")
    return tuple(out)


def _mean(xs):
    xs=tuple(xs)
    if not xs:raise ValueError("nonempty exact finite orbit needed")
    return Fraction(sum(xs),len(xs))


def _cov(xs,ys):
    xs=tuple(xs);ys=tuple(ys)
    if len(xs)!=len(ys) or not xs:raise ValueError("paired same-orbit scores required")
    a,b=_mean(xs),_mean(ys)
    return _mean((x-a)*(y-b) for x,y in zip(xs,ys))


def _shared_gradient(u,v):
    vals=tuple(u[sigma] for sigma in S4)
    other=tuple(v[sigma] for sigma in S4)
    d1=d2=mix=0
    for sigma in S4:
        for i,j in SWAPS:
            s=s4_swap(sigma,i,j)
            x=u[s]-u[sigma];y=v[s]-v[sigma]
            d1+=x*x;d2+=y*y;mix+=x*y
    return (Fraction(d1,144),Fraction(d2,144),Fraction(mix,144))


def original_two_fiber_same_global_96_orbit(model,point_ids):
    """Exact simultaneous true-original GF5 two-fiber covariance certificate."""
    s,V,a,inc,f,g,_,_=_original_source(model)
    pts=tuple(point_ids)
    if len(pts)!=8 or len(set(pts))!=8 or any(
        type(i) is not int or not 0<=i<V for i in pts):
        raise ValueError("eight REAL distinct original POINT factor IDs required")
    for fam,indices in FAMILIES.items():
        edge=tuple(f[pts[i]] for i in indices)
        if _six_position_dual_cycle(edge) is None:
            raise ValueError("BOTH true original sixfactor POINT image sets must be C6")
    c=classify_four_common_completion(
        tuple(f[pts[i]] for i in range(4)),
        tuple(f[pts[i]] for i in (4,5)),
        tuple(f[pts[i]] for i in (6,7)))
    if c=="not_both":
        raise AssertionError("physical original overlapping POINT fibers must share genuine 4-edge 2factor")
    fibers={fam:original_point_A_fiber(model,tuple(pts[i] for i in indices))
            for fam,indices in FAMILIES.items()}
    scores={"A":{},"B":{}}
    physical_state=Counter()
    for state in ORBIT:
        fg=complete_overlapping_global_f(f,pts,state)
        cyc={}
        for fam,indices in FAMILIES.items():
            cyc[fam]=_six_position_dual_cycle(tuple(fg[pts[i]] for i in indices))
            if cyc[fam] is None:
                raise AssertionError("one global permutation must preserve both true C6")
            fib=fibers[fam]
            scores[fam][state]=fib["original_baseline_B_C_weighted"]+W_D*fib["right_cyclic_dual_hist"].get(cyc[fam],0)
        physical_state[(cyc["A"],cyc["B"])]+=1
    x=tuple(scores["A"][st] for st in ORBIT)
    y=tuple(scores["B"][st] for st in ORBIT)
    muA={sig:_mean(scores["A"][(sig,alpha,beta)] for alpha in range(2) for beta in range(2))
         for sig in S4}
    muB={sig:_mean(scores["B"][(sig,alpha,beta)] for alpha in range(2) for beta in range(2))
         for sig in S4}
    # Finite PRODUCT GROUP identity: exclusive α and β coordinates are
    # independent UNIFORM coordinates in the constructed ORBIT, NOT an
    # assumed independence of original source-Q events.
    covariance=_cov(x,y)
    if covariance!=_cov(tuple(muA[sig] for sig in S4),
                         tuple(muB[sig] for sig in S4)):
        raise AssertionError("source original inter-fiber covariance must factor only through four shared POINTs")
    DA,DB,mixed=_shared_gradient(muA,muB)
    if covariance**2>Fraction(9,16)*DA*DB:
        raise AssertionError("original twofiber true GF5 covariance violates exact 24-state S4 spectral gap")
    drift=0
    for sig in S4:
        for alpha in range(2):
            for beta in range(2):
                state=(sig,alpha,beta)
                for i,j in SWAPS:
                    nxt=(s4_swap(sig,i,j),alpha,beta)
                    drift+=(scores["A"][nxt]-scores["A"][state])*(
                        scores["B"][nxt]-scores["B"][state])
    if Fraction(drift,96*6)!=mixed:
        raise AssertionError("real complete original shared-factor gradient != conditional mean signed gradient")
    return {
        "s":s,"V":V,"a":a,"genuine_four_shared_edge_type":c,
        "eight_original_POINT_source_factor_IDs":pts,
        "same_original_full_f_and_g_per_global_state":True,
        "all_original_Q_source_IDs_immutable":True,
        "original_Q_fiber_size_each":(s+1)**6,
        "96_legal_COMPLETE_global_original_POINT_maps":len(ORBIT),
        "24_shared_permutation_states":len(S4),
        "global_state_scores":scores,
        "original_histograms":fibers,
        "joint_cyclic_dual_state_counts":dict(physical_state),
        "historical_score_mean_A":_mean(x),"historical_score_mean_B":_mean(y),
        "historical_score_variance_A":_cov(x,x),
        "historical_score_variance_B":_cov(y,y),
        "historical_score_covariance_A_B":covariance,
        "24_shared_conditional_mean_A":muA,"24_shared_conditional_mean_B":muB,
        "shared_squared_gradient_A":DA,
        "shared_squared_gradient_B":DB,
        "shared_mixed_gradient_A_B":mixed,
        "covariance_spectral_9over16_bound_verified":True,
        "entire_global_7GF5_S_s_NOT_computed":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


def genuine_original_two_fiber_fixture(power,case):
    """Real W32 K6 C4-switch or W34/W38 physical cherry-center case.

    Construct TWO actual original source sixflag Q (same true ORIGINAL
    incidence IDs at 4 shared POINT factor IDs), using eight true
    ORIGINAL LINE factor IDs from genuine GQ incidence graph and ONE
    complete globally injected f,g, BOTH accepted historical D6.
    """
    if type(power) is not int or power not in (1,2,3):
        raise ValueError("finite real symplectic W32/W34/W38 only; math for all h")
    if case not in GRAPH_CASES or (power==1 and case!="four_cycle_switch"):
        raise ValueError("W32 K6 has no physical 7th vertex for cherry replacement")
    model=fixture(power,"lex")
    s,V,a,inc,f,g,by_p,by_l=_original_source(model)
    if V<8:raise AssertionError("need eight genuine original POINT factors")
    pts=tuple(range(8))
    shared,ea,eb=GRAPH_CASES[case]
    target=shared+ea+eb
    if classify_four_common_completion(shared,ea,eb)!=case:
        raise AssertionError("original physical two C6 witness not correct completion type")
    f=_full_pair_injection(V,a,dict(zip(pts,target)))
    star=[]
    for p in pts:
        star.append(tuple(sorted(inc[j][1] for j in by_p[p])))
    ls=_match_unique(tuple(star))
    if len(set(ls))!=8:
        raise AssertionError("original 8POINT incidence Hall line SDR failed")
    g=_full_pair_injection(V,a,dict(zip(ls,target)))
    original_ids={(p,l):j for j,(p,l) in enumerate(inc)}
    QA=tuple(sorted(original_ids[pts[i],ls[i]] for i in FAMILIES["A"]))
    QB=tuple(sorted(original_ids[pts[i],ls[i]] for i in FAMILIES["B"]))
    if len(set(QA))!=6 or len(set(QB))!=6 or len(set(QA)&set(QB))!=4:
        raise AssertionError("genuine original Q original incidence ID overlaps wrong")
    if classify_seven_all_a_original_Q(QA,f,g,inc)!="D6" or (
            classify_seven_all_a_original_Q(QB,f,g,inc)!="D6"):
        raise AssertionError("genuine original W3 two-family original six-ID witnesses not same-map historic D6")
    return dict(model,left_labels=f,right_labels=g),pts,{"QA":QA,"QB":QB}
