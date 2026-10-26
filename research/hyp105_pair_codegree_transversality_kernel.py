"""HYP-105 #230 AA4-PTK: all-h coordinate transversality kernel.

For three filtered physical pair-common-neighbor sets A,B,C (real
physical corners with typed coordinates x,y), the number T(A,B,C)
of triples with pairwise distinct x AND pairwise distinct y has an
EXACT quadratic-time inclusion-exclusion representation:

 T = sum_{a in A,b in B : a_x!=b_x, a_y!=b_y}
      ( |C| - dCx(a_x)-dCx(b_x)-dCy(a_y)-dCy(b_y)
       + 1_C(a_x,a_y)+1_C(a_x,b_y)
       + 1_C(b_x,a_y)+1_C(b_x,b_y)).

The exact pair collision count of A,B is
 E_AB = sum_x dAx(x)dBx(x) + sum_y dAy(y)dBy(y) - |A intersect B|.
Hence T >= max(0, |A||B||C| - |C|E_AB - |B|E_AC - |A|E_BC).
A second certified bound is
 T >= (|A||B|-E_AB) [|C|-2(max dCx+max dCy)]_+,
and similarly under cyclic permutations; take the maximum.

Each triple of admissible hub corners from the GENUINE source physical
graph determines three A/B/C lists. Prior AA4-PC3 proves
  2*D6_original_GF5 = sum_hub_triples T(A,B,C).
Therefore sum_hub_triples of ANY of the certified local lower
bounds divided by 2 is an all-h D6 lower bound for ANY correlated
complete globally injected true symplectic source W(3,2^h) f,g.

Neither source randomness nor a nonphysical edge is admitted.
Finite independent oracle h=1,2 only; theorem itself is all-h.
"""
from collections import Counter, defaultdict
from itertools import combinations

from hyp105_b1_symplectic import symplectic_gq
from hyp105_physical_rainbow_c6 import build_original_physical_graph
from hyp105_pair_codegree_triangle_d6 import exact_pair_codegree_triangle_d6


def _coordinate_degrees(corners):
    if len(corners) != len(set(corners)):
        raise ValueError("physical corner lists must not contain duplicates")
    if any(len(q)!=2 or not all(type(k) is int and k>=0 for k in q)
           for q in corners):
        raise ValueError("physical corners require two nonnegative typed integer coordinates")
    return Counter(x for x,y in corners),Counter(y for x,y in corners)


def pair_coordinate_collisions(A,B):
    """Exactly the number of cross-set ordered PAIRS sharing x or y."""
    A=tuple(A)
    B=tuple(B)
    ax,ay=_coordinate_degrees(A)
    bx,by=_coordinate_degrees(B)
    ex=sum(count*bx[x] for x,count in ax.items())
    ey=sum(count*by[y] for y,count in ay.items())
    both=len(set(A) & set(B))
    result=ex+ey-both
    if not (0 <= result <= len(A)*len(B)):
        raise AssertionError("coordinate collision union violates pair bound")
    return result


def exact_transverse_three_list_kernel(A,B,C,*,check_symmetry=False):
    """Return EXACT transversal triple count and all-h certified lower bounds.

    In the exact computation C is indexed by (x,y); all work on an
    admissible pair a in A,b in B costs O(1). Complexity O(|A||B|+|C|)
    plus dictionary construction, rather than cubic enumeration.
    """
    A,B,C=tuple(A),tuple(B),tuple(C)
    ax,ay=_coordinate_degrees(A)
    bx,by=_coordinate_degrees(B)
    cx,cy=_coordinate_degrees(C)
    raw=len(A)*len(B)*len(C)
    eab=pair_coordinate_collisions(A,B)
    eac=pair_coordinate_collisions(A,C)
    ebc=pair_coordinate_collisions(B,C)
    pair_AB=len(A)*len(B)-eab
    Cset=set(C)
    accepted=0
    positive_pairs=0
    for a in A:
        for b in B:
            if a[0]==b[0] or a[1]==b[1]:
                continue
            remaining=(len(C)-cx[a[0]]-cx[b[0]]
                       -cy[a[1]]-cy[b[1]]
                       +sum((x,y) in Cset
                            for x in (a[0],b[0])
                            for y in (a[1],b[1])))
            if not (0<=remaining<=len(C)):
                raise AssertionError("inclusion-exclusion residual not a population")
            accepted+=remaining
            positive_pairs+=remaining>0

    union_lower=max(
        0,raw-len(C)*eab-len(B)*eac-len(A)*ebc
    )
    def max_degrees(dx,dy):
        return max(dx.values(),default=0)+max(dy.values(),default=0)
    sequential_lower=max(
        0,
        pair_AB*max(0,len(C)-2*max_degrees(cx,cy)),
        (len(A)*len(C)-eac)*max(0,len(B)-2*max_degrees(bx,by)),
        (len(B)*len(C)-ebc)*max(0,len(A)-2*max_degrees(ax,ay)),
    )
    certified_lower=max(union_lower,sequential_lower)
    if certified_lower>accepted or accepted>raw:
        raise AssertionError("certified deterministic transverse lower failed")
    if check_symmetry:
        for X,Y,Z in ((A,C,B),(B,A,C),(B,C,A),(C,A,B),(C,B,A)):
            # Direct cubic independent oracle for small finite falsifiers:
            alternative=sum(
                1 for x in X for y in Y for z in Z
                if len({x[0],y[0],z[0]})==3
                and len({x[1],y[1],z[1]})==3
            )
            if alternative!=accepted:
                raise AssertionError("independent three-choice population mismatch")
    return {
        "raw_pair_codegree_product":raw,
        "exact_coordinate_transverse_triples":accepted,
        "exact_coordinate_collision_loss":raw-accepted,
        "cross_pairs_AB_valid":pair_AB,
        "cross_pairs_AB_colliding":eab,
        "cross_pairs_AC_colliding":eac,
        "cross_pairs_BC_colliding":ebc,
        "union_collision_lower":union_lower,
        "sequential_degree_lower":sequential_lower,
        "certified_lower":certified_lower,
        "positive_valid_AB_pairs":positive_pairs,
    }


def original_pair_codegree_transversality_profile(power,f,g,
                                                  *,verify_full=True):
    """True W32/W34 original symplectic graph, independent PC3 finite oracle."""
    if type(power) is not int or power not in (1,2):
        raise ValueError("true-source finite profile only for powers h=1,2")
    s=1<<power
    _,points,lines,flags=symplectic_gq(power)
    V=(s+1)*(s*s+1)
    if len(points)!=V or len(lines)!=V:
        raise AssertionError("not the genuine source symplectic GQ")
    graph,_=build_original_physical_graph(
        s,tuple(map(tuple,f)),tuple(map(tuple,g)),flags
    )
    posts=defaultdict(set)
    for free,neighbors in graph.items():
        for a,b in combinations(sorted(neighbors),2):
            posts[a,b].add(free)
    neighbor_pairs=defaultdict(set)
    for a,b in posts:
        neighbor_pairs[a].add(b)
        neighbor_pairs[b].add(a)

    summary=Counter()
    independent_verifications=0
    for h0 in sorted(neighbor_pairs):
        for h1 in sorted(h for h in neighbor_pairs[h0] if h>h0):
            for h2 in sorted(h for h in (
                neighbor_pairs[h0] & neighbor_pairs[h1]) if h>h1):
                hx={h0[0],h1[0],h2[0]}
                hy={h0[1],h1[1],h2[1]}
                if len(hx)!=3 or len(hy)!=3:
                    continue
                A=tuple(sorted(z for z in posts[h0,h1]
                               if z[0] not in hx and z[1] not in hy))
                B=tuple(sorted(z for z in posts[h1,h2]
                               if z[0] not in hx and z[1] not in hy))
                C=tuple(sorted(z for z in posts[h0,h2]
                               if z[0] not in hx and z[1] not in hy))
                if not A or not B or not C:
                    continue
                summary["nonempty_pair_triangle_hub_sets"]+=1
                profile=exact_transverse_three_list_kernel(
                    A,B,C,check_symmetry=(power==1 or
                                         independent_verifications<16))
                if power==1 or independent_verifications<16:
                    independent_verifications+=1
                for key in ("raw_pair_codegree_product",
                            "exact_coordinate_transverse_triples",
                            "exact_coordinate_collision_loss",
                            "union_collision_lower",
                            "sequential_degree_lower",
                            "certified_lower"):
                    summary[key]+=profile[key]
                summary["positive_triangle_hub_sets"]+=(
                    profile["exact_coordinate_transverse_triples"]>0)
                summary["positive_certified_triangle_hub_sets"]+=(
                    profile["certified_lower"]>0)
    oriented=summary["exact_coordinate_transverse_triples"]
    if oriented%2:
        raise AssertionError("true-source pair-codegree double-count is not even")
    prior=None
    if verify_full:
        prior=exact_pair_codegree_triangle_d6(
            power,f,g,verify_historical_gf5=True,
            verify_existing_C6_oracle=True)
        if prior["oriented_pair_codegree_witness_triples"]!=oriented:
            raise AssertionError("independent source-ID pair-codegree D6 oracle disagrees")
    if (summary["raw_pair_codegree_product"]!=
            summary["exact_coordinate_transverse_triples"]+
            summary["exact_coordinate_collision_loss"]):
        raise AssertionError("raw/coordinate-collision conservation fails")
    if summary["certified_lower"]>oriented:
        raise AssertionError("sum of proven lower certificates exceeds true D6")
    return {
        "s":s,"V":V,
        **{key:summary[key] for key in (
            "nonempty_pair_triangle_hub_sets",
            "positive_triangle_hub_sets",
            "positive_certified_triangle_hub_sets",
            "raw_pair_codegree_product",
            "exact_coordinate_transverse_triples",
            "exact_coordinate_collision_loss",
            "union_collision_lower","sequential_degree_lower",
            "certified_lower")},
        "accepted_original_D6":oriented//2,
        "certified_original_D6_lower_numerator":
            summary["certified_lower"],
        "certified_original_D6_lower_denominator":2,
        "independent_small_triangle_cubic_checks":
            independent_verifications,
        "independent_genuine_source_D6_checked":verify_full,
        "all_h_transverse_kernel_identity_proved":True,
        "all_h_sevenclass_Omega_s6_proved":False,
    }
