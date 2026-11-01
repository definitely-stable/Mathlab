"""HYP-105 AA4-EPSOPT: sharp coarse-CORE-budget heavy-tail epsilon.

INDEPENDENT exact Fractions / integers for the already proven SS6+core
Branch A chain; external C_graph,c_graph are NOT known numerical constants.
Also independently audit true ORIGINAL W32/W34 FULL heavy-flag deletion,
actual original pencil conflicts and BOTH original physical diagonals.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb, isqrt

from hyp105_full_physical_degree_tail import genuine_source

EPS_OLD=Fraction(1,8)
EPS_OPT=Fraction(13,32)
K_DEFAULT=64
PALETTE=51**6
D6_SIGNED=54162
BBO_SIGNED=53526


def _positive_exact(x):
    if type(x) not in (int,Fraction):
        raise ValueError("C,c,epsilon must be exact rational, not float/bool")
    r=Fraction(x)
    if r<=0:
        raise ValueError("positive exact constant required")
    return r


def _ceil(q):
    return -(-q.numerator//q.denominator)


def _sqrt_ceiling(x):
    v=isqrt(x)
    return v+(v*v<x)


def minimal_alphabet(V):
    a=2
    while comb(a,2)<V:
        a+=1
    return a


def source_budget(s,eps=EPS_OPT):
    """Check all-h CORE count and prove the asymptotically optimal
    epsilon within the unchanged coarse N>=s4 and 4Cs/K<=3s4/32.
    """
    if type(s) is not int or s<64 or s&(s-1):
        raise ValueError("s must be a dyadic power >=64")
    eps=_positive_exact(eps)
    a=minimal_alphabet((s+1)*(s*s+1))
    V=(s+1)*(s*s+1)
    N=(s+1)*V
    Cs=(s*s+1)*(s*s+a-2)
    s4=s**4
    if not (N>=s4 and Cs<=Fraction(3,2)*s4 and a*a<=4*s**3):
        raise AssertionError("published all-h GQ alphabet/book prerequisites fail")
    # E_T < eps*s4, ORIGINAL conflict high-deg flags <=4Cs/K.
    # The crude universal s-independent lower is
    # 2*N0 > 2*(1 - eps - 3/32)*s4.
    uniform_core_coefficient=2*(1-eps-Fraction(3,32))
    exact_core_lower=2*(Fraction(N)-eps*s4-Fraction(4*Cs,K_DEFAULT))
    return {
        "s":s,"V":V,"N":N,"Cs":Cs,"a":a,
        "epsilon":eps,
        "uniform_m0_over_s4_lower":uniform_core_coefficient,
        "source_sharper_m0_lower":exact_core_lower,
        "universal_coarse_density_valid":uniform_core_coefficient>=1,
        "maximal_epsilon_from_coarse_budget":EPS_OPT,
    }


def root_certificate(C,c,eps=EPS_OPT):
    """Integer sufficient h0 and exact physical full degree-tail constant.

    SS6: e(F)>=C_graph*v(F)^(4/3) --> C6>=c_graph*(e/v)^6.
    This function only propagates that EXTERNAL, existential theorem.
    C,c values entered here are purely symbolic/test rational placeholders.
    """
    C,c,eps=map(_positive_exact,(C,c,eps))
    if eps>EPS_OPT:
        raise ValueError("epsilon exceeds unchanged coarse CORE density budget")
    T=max(1,_ceil(Fraction(2**40)*C**3/eps**6))
    alpha=c*eps**12/Fraction(2**72)
    delta=min(Fraction(1,8),alpha)
    sigma2_inv=16*(K_DEFAULT+1)**2
    sigma3_inv=64*(K_DEFAULT+1)**3
    L6=24+288*T**2
    L4_upper=2*sigma2_inv**2*_sqrt_ceiling(8*L6)+40*T
    B0_upper=64*_sqrt_ceiling((K_DEFAULT+1)*T)
    # Three errors in BBo >= s6/4 -34T*s5 -(LE/2)*s^(11/2)
    #                    -2sqrt(B0*T*L4)*s^(47/8):
    # each <= s6/24 iff respectively s>=816T, s>=144LE²,
    # and s>=48^8*(B0*T*L4)^4.
    candidates={
        "source_prereq":64,
        "proper_walk_loss":816*T,
        "exceptional_endpoint_loss":144*21*sigma3_inv**2*L6,
        "all_four_internal_blockers":48**8*(B0_upper*T*L4_upper)**4,
    }
    s0=max(candidates.values())
    h0=max(1,(s0-1).bit_length())
    if not (2**h0>=s0 and (h0==1 or 2**(h0-1)<s0)):
        raise AssertionError("dyadic exact h0 off by one")
    if not (0<delta<=Fraction(1,8) and eps<=EPS_OPT):
        raise AssertionError("invalid theorem constants")
    return {
        "epsilon":eps,"T":T,
        "alpha_external_heavy_D6":alpha,"delta_S_seven":delta,
        "h0_sufficient":h0,"s0_sufficient_integer":s0,
        "sufficient_components":candidates,
        "L6":L6,"L4_ceil":L4_upper,"B0_ceil":B0_upper,
        "sigma2_inv":sigma2_inv,"sigma3_inv":sigma3_inv,
        "R3_floor_conditioned_on_geometric_lemma":
            min(Fraction(D6_SIGNED)*delta,
                Fraction(BBO_SIGNED,8))/PALETTE,
        "R3_floor_simple":
            Fraction(BBO_SIGNED)*delta/PALETTE,
        "graph_constants_are_unverified_placeholders":True,
    }


def verify_exact_dyadic_losses(C,c,eps,h):
    cert=root_certificate(C,c,eps)
    if type(h) is not int or h<1:
        raise ValueError("integer dyadic exponent required")
    s=1<<h
    q=cert["sufficient_components"]
    return {
        "all_three_errors_le_sixth_over24":
          s>=q["proper_walk_loss"] and
          s>=q["exceptional_endpoint_loss"] and
          s>=q["all_four_internal_blockers"],
        "core_prerequisites_met":s>=64 and cert["epsilon"]<=EPS_OPT,
        "correct_sufficient_h0":h>=cert["h0_sufficient"],
    }


def _edge(u,v):
    return tuple(sorted((u,v)))


def genuine_original_pruning(power, f, g, T, *, K=K_DEFAULT):
    """Independent source-first exact ORIGINAL flag/physical bookkeeping.

    Works for small W32/W34 too, but the coarse universal s>=64 inequalities
    are NOT inferred from small finite sources.
    """
    if type(power) is not int or power not in (1,2):
        raise ValueError("genuine original W(3,2^h) generator supports h=1,2")
    T=_positive_exact(T)
    if type(K) is not int or K<1:
        raise ValueError("K must be positive integer")
    s,V,flags=genuine_source(power)
    a=minimal_alphabet(V)
    pairs=set(combinations(range(a),2))
    if (len(f)!=V or len(g)!=V or len(set(f))!=V or len(set(g))!=V or
        any(tuple(z) not in pairs for z in tuple(f)+tuple(g))):
        raise ValueError("complete globally injected typed pair maps required")
    deg=Counter()
    owner_edges=[]
    edge_owners={}
    for i,(p,ell) in enumerate(flags):
        x,z=f[p];y,w=g[ell]
        diagonals=(_edge((x,y),(z,w)),_edge((x,w),(z,y)))
        for uv in diagonals:
            if uv in edge_owners:
                raise AssertionError("physical diagonal original owner duplicated")
            edge_owners[uv]=i
            for v in uv:deg[v]+=1
        owner_edges.append(diagonals)
    if len(edge_owners)!=2*len(flags) or sum(deg.values())!=4*len(flags):
        raise AssertionError("full physical original incidence count invalid")
    heavy={v for v,d in deg.items() if d>T*s}
    heavy_edges={e for e in edge_owners if any(v in heavy for v in e)}
    heavy_ids={edge_owners[e] for e in heavy_edges}
    if len(heavy_ids)>len(heavy_edges):
        raise AssertionError("deleting whole original flags > physical edges")
    # ORIGINAL source flag conflicts computed directly from every pair of IDs.
    n=len(flags)
    conflict_degree=[0]*n
    conflict_edges=0
    for i in range(n):
        p,ell=flags[i]
        for j in range(i+1,n):
            q,r=flags[j]
            bad=((p==q and bool(set(g[ell])&set(g[r]))) or
                 (ell==r and bool(set(f[p])&set(f[q]))))
            if bad:
                conflict_edges+=1
                conflict_degree[i]+=1
                conflict_degree[j]+=1
    high_conflict={i for i,d in enumerate(conflict_degree) if d>K}
    if len(high_conflict)*K>=2*conflict_edges+K:
        raise AssertionError("degree-sum original conflict deletion budget violated")
    core=set(range(n))-heavy_ids-high_conflict
    core_degree=Counter()
    for i in core:
        for u,v in owner_edges[i]:
            core_degree[u]+=1
            core_degree[v]+=1
    if any(v in heavy for v in core_degree):
        raise AssertionError("core contains full-H heavy endpoint")
    if any(core_degree[v]>T*s for v in core_degree):
        raise AssertionError("core physical degree cap not inherited")
    if any(conflict_degree[i]>K for i in core):
        raise AssertionError("original source conflict core degree cap fails")
    m0=2*len(core)
    if m0<2*(n-len(heavy_edges)-len(high_conflict)):
        raise AssertionError("original heavy edge deletion overcount")
    return {
        "s":s,"original_flags":n,"full_edges":len(edge_owners),
        "full_degree_sum":sum(deg.values()),"heavy_vertices":len(heavy),
        "full_heavy_edges":len(heavy_edges),
        "deleted_heavy_original_flags":len(heavy_ids),
        "original_conflict_edges":conflict_edges,
        "deleted_high_conflict_original_flags":len(high_conflict),
        "original_core_flags":len(core),"core_physical_edges":m0,
        "core_max_degree":max(core_degree.values(),default=0),
        "core_max_full_conflict_degree":max((conflict_degree[i] for i in core),default=0),
        "bookkeeping_valid":True,
    }
