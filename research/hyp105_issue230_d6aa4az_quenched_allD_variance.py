"""HYP-105 AA4-AZ: rigorous ONE-global-line-permutation ALL-D wedge variance.

An independent probability proof is in the companion research Markdown.
This is NOT a uniform fixed-g GOOD-port or six-ID GF5 theorem.
"""
from collections import Counter, defaultdict
from itertools import combinations
from fractions import Fraction
from hyp105_issue230_d6aa4ay_quenched_allD_opposite_mean import (
    _params, physical_edge_port_energy, physical_energy_universal_deficit_lower,
)


def original_line_triple_weights(model):
    """True original incidence triples with opposite physical POINT ports."""
    V, a, _, _ = _params(model["s"])
    d = model["s"] + 1
    inc = tuple(map(tuple, model["incidences"]))
    f = tuple(tuple(sorted(e)) for e in model["left_labels"])
    if len(inc) != V*d or len(set(inc)) != len(inc) or len(f) != V or len(set(f)) != V:
        raise ValueError("complete distinct original incidence and injected point labels required")
    if any(len(e) != 2 or e[0] == e[1] or min(e) < 0 or max(e) >= a for e in f):
        raise ValueError("invalid point image")
    nbr = [set() for _ in range(V)]
    line_degrees = [0]*V
    for p,l in inc:
        if not 0 <= p < V or not 0 <= l < V:
            raise ValueError("source factor outside range")
        nbr[p].add(l)
        line_degrees[l] += 1
    if any(len(v) != d for v in nbr) or any(x != d for x in line_degrees):
        raise ValueError("source not d-regular")
    stars = [[] for _ in range(a)]
    for p,(u,v) in enumerate(f):
        stars[u].append(p)
        stars[v].append(p)
    w = defaultdict(int)
    for p,l in inc:
        u,v = f[p]
        for q0 in stars[u]:
            if q0 == p:
                continue
            for q1 in stars[v]:
                if q1 == p:
                    continue
                if q0 == q1:
                    raise AssertionError("point injection violated")
                for k0 in nbr[q0]:
                    if k0 == l:
                        continue
                    for k1 in nbr[q1]:
                        if k1 not in (l,k0):
                            w[l,k0,k1] += 1
    return dict(w)


def source_influences(weights, V):
    one, pair = Counter(), Counter()
    B = 0
    for ids,n in weights.items():
        if (not isinstance(ids,tuple) or len(ids) != 3 or len(set(ids)) != 3 or
                any(type(i) is not int or i < 0 or i >= V for i in ids) or
                type(n) is not int or n <= 0):
            raise ValueError("positive weighted triple of distinct source line IDs required")
        B += n
        for i in ids:
            one[i] += n
        for ij in combinations(sorted(ids),2):
            pair[ij] += n
    if B <= 0 or sum(one.values()) != 3*B or sum(pair.values()) != 3*B:
        raise ValueError("nonempty valid source line triple ledger required")
    return B,max(one.values()),max(pair.values())


def permutation_variance_certificate(weights, right_edges, a):
    """For ANY weighted three-line statistic under ONE uniform whole bijection."""
    E = tuple(tuple(sorted(edge)) for edge in right_edges)
    V = len(E)
    if V < 6 or len(set(E)) != V:
        raise ValueError("at least six globally distinct physical right edges required")
    T = physical_edge_port_energy(E,a)
    if T <= 0:
        raise ValueError("positive opposite right edge port energy required")
    B,M1,M2 = source_influences(weights,V)
    p = Fraction(2*T,V*(V-1)*(V-2))
    q = Fraction((V-3)*(V-4)*(V-5),V*(V-1)*(V-2))
    H = 2*(a-2)**2
    P1 = Fraction(H*H,(V-1)*(V-2)*(V-3)*(V-4))
    eta = 1/q-1 + Fraction(3*M1,B)*P1/(p*p) + Fraction(3*M2,B)/p
    return {"V":V,"B":B,"M1":M1,"M2":M2,"p":p,"q":q,
            "one_overlap_probability_upper":P1,"mean":B*p,
            "relative_variance_upper":eta,
            "half_mean_lower_tail_upper":min(Fraction(1),4*eta),
            "root_230":"OPEN_WITH_FORMAL_BLOCKER"}


def uniform_original_variance_envelope(s):
    """For ALL dyadic original orders: all fixed global f and right edge support."""
    V,a,_,m = _params(s)
    d,t = s+1,a-2
    L = physical_energy_universal_deficit_lower(V,a,m)
    if 2*L < V*V:
        raise AssertionError("prior original support bound changed")
    B0 = d*(d-1)*(d-2)*L
    p0 = Fraction(2*L,V*(V-1)*(V-2))
    M10,M20 = 5*d**3*t*t,8*d**3*t
    q = Fraction((V-3)*(V-4)*(V-5),V*(V-1)*(V-2))
    P1 = Fraction(4*t**4,(V-1)*(V-2)*(V-3)*(V-4))
    eta = 1/q-1 + Fraction(3*M10,B0)*P1/(p0*p0) + Fraction(3*M20,B0)/p0
    mean0 = Fraction(2*d*(d-1)*(d-2)*L*L,V*(V-1)*(V-2))
    if mean0 < Fraction(s**6,2):
        raise AssertionError("prior all-h mean bound changed")
    return {"s":s,"h":s.bit_length()-1,"V":V,"a":a,"m":m,
            "source_B_lower":B0,"source_M1_upper":M10,
            "source_M2_upper":M20,"mean_lower":mean0,
            "relative_variance_upper":eta,
            "half_mean_lower_tail_upper":min(Fraction(1),4*eta),
            "fixed_g_lower_PROVED":False,"good_or_sixGF5_PROVED":False,
            "root_230":"OPEN_WITH_FORMAL_BLOCKER"}
