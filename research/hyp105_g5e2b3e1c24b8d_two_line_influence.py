"""HYP-105 B8-D: all-h exact two-line covariance under ONE complete g.

Input B2 fibers preserve original multiplicity, incidence positions and
the matched D6 dual cycle. No independent per-source global injections.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb

from hyp105_g5e2b3e1c24b8a_physical_tensor import TAGS
from hyp105_g5e2b3e1c24b8b_signed_physical_balance import (
    PROFILE_A, PROFILE_B, PROFILE_C, profile_probability,
    d6_signature_probability,
)


def adjacency_probability(a):
    if type(a) is not int or a < 6:
        raise ValueError("a must be an integer >= 6")
    return Fraction(4, a + 1)


def shape(tag, lines, signature):
    if tag not in TAGS or len(lines) != 6 or any(
            type(x) is not int or x < 0 for x in lines):
        raise ValueError("tagged six original right incidence positions required")
    counts = Counter(lines)
    profile = tuple(sorted(counts.values(), reverse=True))
    if profile not in (PROFILE_A, PROFILE_B, PROFILE_C):
        raise ValueError("invalid physical right endpoint profile")
    if tag == "D6":
        if profile != PROFILE_A or signature is None:
            raise ValueError("D6 needs distinct lines and connected left signature")
        sig = frozenset(tuple(e) for e in signature)
        if (len(sig) != 6 or
                any(len(e) != 2 or e[0] >= e[1] or
                    any(type(v) is not int or v not in range(6) for v in e)
                    for e in sig) or
                Counter(v for e in sig for v in e) != Counter({i:2 for i in range(6)})):
            raise ValueError("invalid six-position D6 signature")
        graph = {i:set() for i in range(6)}
        for u,v in sig:
            graph[u].add(v)
            graph[v].add(u)
        reached, todo = {0}, [0]
        while todo:
            for v in graph[todo.pop()]:
                if v not in reached:
                    reached.add(v)
                    todo.append(v)
        if len(reached) != 6:
            raise ValueError("disconnected D6 signature")
        return counts, profile, sig
    if signature is not None:
        raise ValueError("ordinary motif cannot carry D6 signature")
    return counts, profile, None


def right_probability(a, tag, profile):
    return (d6_signature_probability(a) if tag == "D6"
            else profile_probability(a, profile))


def selected_pairs(profile):
    return {PROFILE_A:6, PROFILE_B:4, PROFILE_C:0}[profile]


def neighbors(profile, counts, i):
    return 0 if profile == PROFILE_C or (
        profile == PROFILE_B and counts[i] == 2) else 2


def inside_theta(tag, lines, signature, profile, counts, i, j):
    if tag == "D6":
        return Fraction(int(tuple(sorted((lines.index(i),lines.index(j))))
                            in signature))
    if profile == PROFILE_A:
        return Fraction(2,5)
    if profile == PROFILE_B and counts[i] == counts[j] == 1:
        return Fraction(2,3)
    return Fraction(0)


def theta(a, tag, lines, signature, counts, profile, i, j):
    """P(adjacent pinned edges | given right six-motif accepted)."""
    if type(i) is not int or type(j) is not int or min(i,j)<0 or i==j:
        raise ValueError("distinct nonnegative original line IDs required")
    k, m = len(counts), comb(a,2)
    if i in counts and j in counts:
        return inside_theta(tag,lines,signature,profile,counts,i,j)
    if i in counts or j in counts:
        v = i if i in counts else j
        return Fraction(2*(a-2)-neighbors(profile,counts,v),m-k)
    # BOTH outside: remove all k selected vertices from L(K_a).
    remaining = m*(a-2)-2*k*(a-2)+selected_pairs(profile)
    return Fraction(2*remaining,(m-k)*(m-k-1))


def source_influence(a, tag, lines, signature, i, j):
    """Exact rational per-original-sixset mean, conditional means and I."""
    lines = tuple(lines)
    counts, profile, signature = shape(tag,lines,signature)
    p = adjacency_probability(a)
    mu = right_probability(a,tag,profile)
    z = theta(a,tag,lines,signature,counts,profile,i,j)
    cov = mu*(z-p)
    influence = cov/(p*(1-p))
    return {"mean":mu, "adj":mu+(1-p)*influence,
            "dis":mu-p*influence, "theta":z,
            "covariance":cov, "influence":influence}


def compiled_matrix(source, a, n):
    """All n*(n-1)/2 exact influences in O(records*6^2 + 7*n^2).

    Every original sixset receives the SAME global injection law; no g
    optimization and no enumeration of global completions is performed.
    """
    m=comb(a,2) if type(a) is int and a>=6 else 0
    if (not isinstance(source,dict) or "records" not in source
            or "static_eligible" not in source or
            type(n) is not int or not 2<=n<=m):
        raise ValueError("valid compiled left source and 2<=n<=M required")
    p=adjacency_probability(a)
    state={tag:{"mu":Fraction(0),"base":Fraction(0),
                "one":defaultdict(Fraction),"both":defaultdict(Fraction)}
           for tag in TAGS}
    pop=Counter()
    for tag,raw,sig,mult in source["records"]:
        if type(mult) is not int or mult<=0:
            raise ValueError("positive original multiplicity required")
        lines=tuple(raw)
        counts,profile,sig=shape(tag,lines,sig)
        if max(counts)>=n:
            raise ValueError("source line exceeds original population")
        k=len(counts)
        w=mult*right_probability(a,tag,profile)
        pop[tag]+=mult
        st=state[tag]
        st["mu"]+=w
        z0=Fraction(2*(m*(a-2)-2*k*(a-2)+selected_pairs(profile)),
                    (m-k)*(m-k-1))
        st["base"]+=w*z0
        one={}
        for i in counts:
            one[i]=Fraction(2*(a-2)-neighbors(profile,counts,i),m-k)
            st["one"][i]+=w*(one[i]-z0)
        for i,j in combinations(sorted(counts),2):
            z2=inside_theta(tag,lines,sig,profile,counts,i,j)
            st["both"][(i,j)]+=w*(z2-one[i]-one[j]+z0)
    if sum(pop.values())!=source["static_eligible"]:
        raise AssertionError("compressed ORIGINAL multiplicities lost")
    matrix={}
    by_tag={tag:{} for tag in TAGS}
    mu=sum((state[t]["mu"] for t in TAGS),Fraction(0))
    for i,j in combinations(range(n),2):
        value=Fraction(0)
        for tag in TAGS:
            s=state[tag]
            joint=s["base"]+s["one"][i]+s["one"][j]+s["both"][(i,j)]
            v=(joint-p*s["mu"])/(p*(1-p))
            by_tag[tag][(i,j)]=v
            value+=v
        matrix[(i,j)]=value
    rows={i:sum((matrix[min(i,j),max(i,j)]
                 for j in range(n) if i!=j),Fraction(0))
          for i in range(n)}
    if n==m and any(rows.values()):
        raise AssertionError("full K_a edge bijection requires zero row sums")
    return {"mean":mu, "p_adj":p, "matrix":matrix,
            "by_tag_matrix":by_tag, "by_tag_mean":{
                t:state[t]["mu"] for t in TAGS},
            "populations":{t:pop[t] for t in TAGS},
            "row_sums":rows, "unoccupied_edges":m-n,
            "full_bijection_row_theorem":n==m,
            "restricted_structural_result_only":True}
