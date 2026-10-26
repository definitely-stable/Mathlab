"""HYP-105 / #230 AA4-LCR-W: exact source-pencil wedge conservation.

New all-h GQ-source identity for the TOTAL population of physical two-edge
coordinate-backtracking wedges (not physical C6 completions).
Every physical coordinate-edge source map must be complete and typed
globally injected. Arbitrary correlation f/g is allowed.

Jx=2 sum_{source point p, physical line-coordinate y}
  binom(# original lines l incident p with y in g(l), 2);
Jy=2 sum_{source line l, physical point-coordinate x}
  binom(# original points p incident l with x in f(p), 2).
Each Jx,Jy <= V*s*(s+1) = O(s^5).
"""
from math import comb

from hyp105_physical_degree_energy import (
    minimal_alphabet, _verify_typed_injections, _verified_source,
)
from hyp105_physical_rainbow_c6 import build_original_physical_graph


def original_source_pencil_wedges(s, f, g, flags,
                                  *, check_physical_independently=True):
    """Exact number of *unoriented 2-edge wedges* centered at physical corners.

    Coordinates x/y of the endpoints of an x/y-backtracking wedge match;
    the full physical endpoints are always distinct because their other
    coordinate differs. The x-wedge shares one genuine original POINT
    source factor, the y-wedge shares one original LINE source factor.
    """
    if type(s) is not int or s < 2 or s & (s-1):
        raise ValueError("dyadic s>=2 required")
    V=(s+1)*(s*s+1)
    a=minimal_alphabet(V)
    f=tuple(map(tuple,f))
    g=tuple(map(tuple,g))
    _verify_typed_injections(a,V,f,g)
    _verified_source(s,flags,V)
    point_y=[[0]*a for _ in range(V)]
    line_x=[[0]*a for _ in range(V)]
    for p,l in flags:
        for y in g[l]:
            point_y[p][y]+=1
        for x in f[p]:
            line_x[l][x]+=1
    d=s+1
    if any(sum(row)!=2*d or max(row)>d for row in point_y+line_x):
        raise AssertionError("original pencil source degree not preserved")
    jx=2*sum(comb(k,2) for row in point_y for k in row)
    jy=2*sum(comb(k,2) for row in line_x for k in row)
    cap=V*s*(s+1)
    if not (0<=jx<=cap and 0<=jy<=cap):
        raise AssertionError("global injectivity/source regularity wedge upper bound failed")
    direct_x=direct_y=None
    if check_physical_independently:
        adjacency,_=build_original_physical_graph(s,f,g,flags)
        direct_x=direct_y=0
        for center,neighbors in adjacency.items():
            groups_x={}
            groups_y={}
            for neighbor in neighbors:
                groups_x[neighbor[0]]=groups_x.get(neighbor[0],0)+1
                groups_y[neighbor[1]]=groups_y.get(neighbor[1],0)+1
            direct_x+=sum(comb(k,2) for k in groups_x.values())
            direct_y+=sum(comb(k,2) for k in groups_y.values())
        if (direct_x,direct_y)!=(jx,jy):
            raise AssertionError("physical centered-wedge oracle disagrees with original source-pencil oracle")
    return {
        "s":s,"V":V,"a":a,
        "Jx_point_pencil_two_edge_wedges":jx,
        "Jy_line_pencil_two_edge_wedges":jy,
        "individual_axis_upper_V_s_s_plus_1":cap,
        "Jx_direct_physical":direct_x,
        "Jy_direct_physical":direct_y,
        "maximum_source_point_pencil_symbol_degree":
            max(map(max,point_y)),
        "maximum_source_line_pencil_symbol_degree":
            max(map(max,line_x)),
        "all_h_wedge_upper_O_s5_proved":True,
        "C6_completion_average_bound_proved":False,
        "all_h_defect_upper_O_s6_proved":False,
        "root_sevenclass_proved":False,
    }
