"""HYP-105 AA4-CG-NOGO: projective-plane graphs falsify density-only
codegree-clique replacement for balanced ordinary C6 supersaturation.

Self-contained PG(2,p) incidence graphs over PRIME fields F_p, for an
UNBOUNDED family (Euclid), not necessarily true source W(3,2^h).
NO claim of an original-GQ correlated-map counterexample to Branch A.
"""
from fractions import Fraction
from itertools import product
from math import comb,isqrt

from hyp105_independent_codegree_c6_source_referee import (
    bipartite_c6_codegree, exact_codegree_clique_certificate,
    bipartite_c6_direct_six_vertex_oracle,
)


def _prime(p):
    if type(p) is not int or p<2:
        raise ValueError("p must be a genuine prime field characteristic")
    for d in range(2,isqrt(p)+1):
        if p%d==0:
            raise ValueError("p must be prime, not prime-power field label")
    return p


def _normalize_projective(v,p):
    if all(x==0 for x in v):raise ValueError("zero projective vector")
    i=next(x for x in v if x)
    inv=pow(i,-1,p)
    return tuple(x*inv%p for x in v)


def projective_plane_prime(p):
    """PG(2,p) constructed with NO historical source/geometry classes.

    The same normalized NONZERO homogeneous triples index points and
    line covectors; incidence is a.x+b.y+c.z = 0 in Fp.
    """
    p=_prime(p)
    vectors=tuple(sorted({_normalize_projective(v,p)
                          for v in product(range(p),repeat=3)
                          if any(v)}))
    n=p*p+p+1
    if len(vectors)!=n:raise AssertionError("PG2 number of points wrong")
    rows=tuple(sum(1<<j for j,l in enumerate(vectors)
                   if sum(a*b for a,b in zip(pt,l))%p==0)
               for pt in vectors)
    if len(rows)!=n or any(x.bit_count()!=p+1 for x in rows):
        raise AssertionError("PG2 flags degree not p+1")
    # INDEPENDENT source-free finite pairing check, not invoking C6 code.
    all_pair_codegrees={
        (rows[i]&rows[j]).bit_count()
        for i in range(n) for j in range(i+1,n)
    }
    if all_pair_codegrees!={1}:
        raise AssertionError("some projective point pair has !=1 line")
    e=sum(r.bit_count() for r in rows)
    if e!=n*(p+1):
        raise AssertionError("incorrect number of projective incidence edges")
    return {"p":p,"n_side":n,"vertices":2*n,"edges":e,
            "normalized_projective_vectors":vectors,
            "row_neighborhoods":rows,
            "pairwise_left_codegrees":frozenset(all_pair_codegrees)}


def projective_triangle_count_exact(p):
    """Source-independent symbolic count: every noncollinear 3-point
    triple produces ONE 6cycle of distinct lines in the incidence graph.

    Each collinear triple lies on exactly one line, which contains
    p+1 points. Therefore #C6 = C(n,3)-n*C(p+1,3).
    """
    p=_prime(p)
    n=p*p+p+1
    total=comb(n,3)-n*comb(p+1,3)
    if total<=0:raise AssertionError("real projective plane lacks 6cycles")
    return total


def projective_nogo_certificate(p,*,direct_small=False):
    pg=projective_plane_prime(p)
    rows=pg["row_neighborhoods"]
    n=pg["n_side"]
    symbolic=projective_triangle_count_exact(p)
    codegree=bipartite_c6_codegree(rows,n)["ordinary_unoriented_C6"]
    if codegree!=symbolic:
        raise AssertionError("independent projective triangle and exact C6 oracle mismatch")
    if direct_small and p<=3:
        if bipartite_c6_direct_six_vertex_oracle(rows,n)!=codegree:
            raise AssertionError("third direct nonzero-injective C6 oracle disagrees")
    clique=exact_codegree_clique_certificate(rows,n,range(n))
    if clique["min_codegree"]!=1 or clique["guaranteed_C6"]!=0:
        raise AssertionError("projective plane has spurious 3-codegree clique")
    ratio=Fraction(pg["edges"]**3,pg["vertices"]**4)
    exact=Fraction((p+1)**3,16*n)
    if ratio!=exact or ratio<Fraction(p,16):
        raise AssertionError("projective plane balanced density lower wrong")
    return {
        "p":p,"v":pg["vertices"],"e":pg["edges"],
        "exact_C6":symbolic,
        "max_left_pair_codegree":1,
        "local_k_ge_3_codegree_clique_exists":False,
        "positive_codegree_local_lower":0,
        "e_cubed_over_v_fourth":ratio,
        "density_lower_p_over16":Fraction(p,16),
        "scale":"ordinary simple bipartite graphs, NOT original W(3,2^h) maps",
    }


def density_threshold_symbolic(p, graph_C):
    """Exact rational criterion e>=C*v^(4/3) iff e^3>=C^3*v^4.

    If p >= 16*C^3 then ordinary PG(2,p) automatically satisfies it.
    There are arbitrarily large primes; NO such density threshold can
    force existence of a k>=3 codegree clique in arbitrary graphs.
    """
    p=_prime(p)
    if type(graph_C) not in (int,Fraction) or Fraction(graph_C)<=0:
        raise ValueError("positive exact rational trial graph_C required")
    C=Fraction(graph_C)
    n=p*p+p+1
    e=n*(p+1)
    v=2*n
    exact=(Fraction(e**3,v**4)>=C**3)
    sufficient=(Fraction(p)>=16*C**3)
    if sufficient and not exact:
        raise AssertionError("exact density theorem violated")
    return {"p":p,"C_test":C,
            "exact_balanced_edge_threshold_met":exact,
            "sufficient_p_ge16C3":sufficient,
            "ratio_e3_over_v4":Fraction(e**3,v**4),
            "does_not_constrain_original_source_selected_graphs":True}
