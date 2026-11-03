"""AA4-DETG5: deterministic original-GF5 sixflag assignment by exact conditioning.

For any finite DISTINCT ORIGINAL selected D6 / produced aligned BBo
source-sixset family on the SAME fixed globally injected f,g:
  E[number of signed events] =
     (54162 * #D6 + 53838 * #produced BBo) / 51**6.

A fixed 51-valued checksum-4 palette per ORIGINAL source flag can be
chosen greedily by EXACT conditional expectations, never assuming
independence of overlapping sixsets. The resulting event count is no
more than that expectation. If the numerator <51**6 it is EXACTLY zero.
We validate actual W(3,2) / W(3,4) source IDs; no synthetic flags.

The completion-counter is a new ORIGINAL source-coordinate affine
GF(5) inclusion-exclusion with fixed column palettes and residual
per-component Kirchhoff demands. It does not import previous GF5 flow
solvers. It never enumerates 51**6 full assignments.
"""
from collections import Counter,defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import comb, isqrt

from hyp105_full_physical_degree_tail import genuine_source


PALETTES=tuple(x for x in product(range(1,5),repeat=4) if sum(x)%5==4)
SIGNS=tuple(frozenset((0,i,j)) for i,j in combinations(range(1,6),2))
DENOM=51**6
WEIGHTS={"D6":54162,"BBo-produced":53838}
assert len(PALETTES)==51 and len(SIGNS)==10


def _minimal_alphabet(v):
    a=(1+isqrt(1+8*v))//2
    while comb(a,2)<v:a+=1
    while a>2 and comb(a-1,2)>=v:a-=1
    return a


def _check_source(power,f,g):
    if type(power) is not int or power not in (1,2):
        raise ValueError("finite ORIGINAL source fixture only genuine W32/W34")
    s,v,flags=genuine_source(power)
    a=_minimal_alphabet(v)
    legal=set(combinations(range(a),2))
    try:
        f=tuple(tuple(t) for t in f)
        g=tuple(tuple(t) for t in g)
    except (TypeError,ValueError) as exc:
        raise ValueError("missing complete fixed original source maps") from exc
    if (len(f)!=v or len(g)!=v or len(set(f))!=v
        or len(set(g))!=v or any(t not in legal for t in f+g)):
        raise ValueError("complete separately globally pair-injective maps required")
    return (s,v,tuple(flags),f,g)


def _is_named_c6(edges):
    if len(edges)!=6 or len(set(edges))!=6:
        return False
    adj=[set() for _ in range(6)]
    for i,j in edges:
        if i==j:return False
        adj[i].add(j);adj[j].add(i)
    if any(len(z)!=2 for z in adj):
        return False
    reached={0}
    todo=[0]
    while todo:
        for v in adj[todo.pop()]:
            if v not in reached:
                reached.add(v);todo.append(v)
    return len(reached)==6


def _source_coordinate_edges(flags,ids,f,g):
    """Twelve pairs (column i, coefficient slot, column j, slot)."""
    physical=[]
    byside=[]
    for side,labels in ((0,f),(1,g)):
        occupied=defaultdict(list)
        for j,id_ in enumerate(ids):
            factor=flags[id_][side]
            for slot,coordinate in enumerate(labels[factor]):
                occupied[coordinate].append((j,2*side+slot))
        if len(occupied)!=6 or any(len(z)!=2 for z in occupied.values()):
            raise ValueError("not 6 physical coordinates of degree two per type")
        pairs=[]
        for coordinate in sorted(occupied):
            first,last=sorted(occupied[coordinate])
            if first[0]==last[0]:
                raise ValueError("physical loop in ORIGINAL dual")
            physical.append((first[0],first[1],last[0],last[1]))
            pairs.append((first[0],last[0]))
        byside.append(tuple(sorted(pairs)))
    if len(physical)!=12:
        raise AssertionError("incorrect true original 12 physical coordinates")
    return tuple(physical),tuple(byside)
