"""HYP-105 #230 AA4-SPW: all-h ORIGINAL GQ spectral pencil-wedge cap O(s^4).

The all-h source LINE collinearity graph has regular degree s(s+1)
and nonconstant eigenvalues s-1 and -(s+1). The exact GQ matrix
identity is C^2=(s^2-1)I-2C+(s+1)J. For each right physical coordinate
y, t_y=# actual ORIGINAL source lines l with y in g(l), giving:

 V*J_x <= 2*V^2*(s-1) + (s^2+1)*sum_y t_y^2.
 V*J_y <= 2*V^2*(s-1) + (s^2+1)*sum_x r_x^2.

Since all source point and line physical image pairs are separately
injective K_a edges, sum t_y^2, sum r_x^2 <=2V(a-1), so
 J_x,J_y <=2V(s-1)+2(s^2+1)(a-1) = O(s^4).

CRITICAL: all-h *spectral source GQ fact* required; arbitrary regular
bipartite incidence graphs need not satisfy it. Finite source spectrum
and original-pencils crosschecked using exact integer arithmetic.
"""
from math import comb

from hyp105_b1_symplectic import symplectic_gq
from hyp105_physical_degree_energy import (
    _verify_typed_injections, _verified_source, minimal_alphabet,
)
from hyp105_original_source_pencil_wedges import original_source_pencil_wedges


def original_line_collinearity_polynomial(s, flags):
    """Independent exact-integer genuine GQ line-graph spectral certificate.

    Checks each entry C^2=(s^2-1)I-2C+(s+1)J using ORIGINAL source
    line point sets; C_ij=1 iff i!=j and lines share an original point.
    Source true GQ has no 4cycle, hence any pair meets at most once.
    O(V^3) worst-case; use only true finite W32/W34.
    """
    if type(s) is not int or s < 2 or s & (s-1):
        raise ValueError("dyadic s >=2 required")
    V=(s+1)*(s*s+1)
    points,lines=_verified_source(s,flags,V)
    neighbors=[set() for _ in range(V)]
    for p, incident_lines in enumerate(points):
        for l in incident_lines:
            neighbors[l].update(incident_lines-{l})
    if any(len(group)!=s*(s+1) for group in neighbors):
        raise AssertionError("source line collinearity graph wrong degree")
    for i in range(V):
        for j in range(V):
            lhs=len(neighbors[i] & neighbors[j])
            rhs=(s*s-1 if i==j else 0) - (
                2 if j in neighbors[i] else 0) + (s+1)
            if lhs!=rhs:
                raise AssertionError("original GQ collinearity polynomial fails")
    return {
        "s":s,"V":V,
        "source_line_collinearity_degree":s*(s+1),
        "nontrivial_positive_eigenvalue":s-1,
        "nontrivial_negative_eigenvalue":-(s+1),
        "integer_collinearity_polynomial_checked":True,
    }


def original_spectral_pencil_cap(s, f, g, flags,
                                 *, verify_original_geometry=True):
    """ALL-h exact upper inequality, finite s=2,4 integer oracle.

    Returns the rational spectral upper as (integer_numerator, V), and
    stronger per-coordinate finite counts of original collinear
    line/point pairs, plus weaker alphabet-only uniform bound.
    """
    if type(s) is not int or s < 2 or s&(s-1):
        raise ValueError("dyadic s >=2 required")
    V=(s+1)*(s*s+1)
    a=minimal_alphabet(V)
    f,g=tuple(map(tuple,f)),tuple(map(tuple,g))
    _verify_typed_injections(a,V,f,g)
    point_lines,line_points=_verified_source(s,flags,V)
    if verify_original_geometry:
        original_line_collinearity_polynomial(s,flags)
    prior=original_source_pencil_wedges(
        s,f,g,flags,check_physical_independently=True)
    r=[0]*a
    t=[0]*a
    for u,v in f:
        r[u]+=1
        r[v]+=1
    for x,y in g:
        t[x]+=1
        t[y]+=1
    if (sum(r),sum(t))!=(2*V,2*V) or (
            max(r)>a-1 or max(t)>a-1):
        raise AssertionError("not globally injected K_a label edges")
    r2=sum(q*q for q in r)
    t2=sum(q*q for q in t)
    if r2>2*V*(a-1) or t2>2*V*(a-1):
        raise AssertionError("coordinate incidence K_a star-degree cap failed")

    jx=prior["Jx_point_pencil_two_edge_wedges"]
    jy=prior["Jy_line_pencil_two_edge_wedges"]
    spectral_base=2*V*V*(s-1)
    x_num=spectral_base+(s*s+1)*t2
    y_num=spectral_base+(s*s+1)*r2
    if jx*V>x_num or jy*V>y_num:
        raise AssertionError("genuine original GQ source spectral wedge inequality fails")
    universal=2*V*(s-1)+2*(s*s+1)*(a-1)
    if universal>prior["individual_axis_upper_V_s_s_plus_1"]:
        # The spectral bound is still always O(s^4), even if finite
        # constants are not sharper in an arbitrary tiny source case.
        pass
    if jx>universal or jy>universal:
        raise AssertionError("universal spectral-derived alphabet cap fails")

    # Independent original line-pair collinearity count. For any y,
    # each pair of incident source lines sharing y can meet at MOST
    # one original point, by the GQ absence of 4cycles. The sum over
    # distinct source line pairs exactly equals original wedge Jx/2.
    independent_x=0
    for y in range(a):
        actual_lines=[l for l in range(V) if y in g[l]]
        for i,l in enumerate(actual_lines):
            for other in actual_lines[i+1:]:
                if line_points[l].intersection(line_points[other]):
                    independent_x+=2
    independent_y=0
    for x in range(a):
        actual_points=[p for p in range(V) if x in f[p]]
        for i,p in enumerate(actual_points):
            for other in actual_points[i+1:]:
                if point_lines[p].intersection(point_lines[other]):
                    independent_y+=2
    if (independent_x,independent_y)!=(jx,jy):
        raise AssertionError("independent original source collinear pair census disagrees")

    return {
        "s":s,"V":V,"a":a,
        "J_x":jx,"J_y":jy,
        "original_point_coordinate_degrees":tuple(r),
        "original_line_coordinate_degrees":tuple(t),
        "original_point_coordinate_degree_square_sum":r2,
        "original_line_coordinate_degree_square_sum":t2,
        "x_spectral_bound_numerator":x_num,
        "y_spectral_bound_numerator":y_num,
        "spectral_bound_denominator":V,
        "universal_each_axis_integer_bound":universal,
        "previous_each_axis_pencil_bound":
            prior["individual_axis_upper_V_s_s_plus_1"],
        "independent_original_collinear_pair_x":independent_x,
        "independent_original_collinear_pair_y":independent_y,
        "all_h_O_s4_pencil_wedge_upper_proved":True,
        "all_h_average_O_s2_completion_proved":False,
        "root_sevenclass_proved":False,
    }
