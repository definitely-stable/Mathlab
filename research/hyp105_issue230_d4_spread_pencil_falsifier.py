"""HYP-105 #230 D4: constructive ALL-h NO-GO for the D3 *route*.

A Desarguesian symplectic spread of the ORIGINAL W(3,s) plus an explicit
INJECTIVE unordered-physical-pair map f forces M_f=Omega(s^4).
Balanced missing-edge-cycle right map g also forces W_mean=Omega(s^6).

These disprove the two PROPOSED D3 sufficient conditions
    M_f+M_g=o(s^(39/10)) and W_mean=o(s^(59/10)).
They do NOT disprove the original seven-positive-family universal lower
S=Omega(s^6) (Branch A), nor construct S=o(s^6) (Branch B).
"""
from itertools import combinations
from math import comb
import json

from hyp105_b1_symplectic import GF2Power, normalized, symplectic
from hyp105_issue230_proof_audit import _geometry, _model, parameters
from hyp105_issue230_d3_double_centered_energy import (
    _pencil_motifs,double_centered_energy,
)
from hyp105_issue230_projection import ProjectionClosure


def plan(s):
    """Exact all-h arithmetic, no finite enumeration or asymptotic fit."""
    p=parameters(s)
    a,V=p["a"],p["V"]
    g=a//4
    nonanchor=a-g
    t=nonanchor//(2*(s+1))
    used=g*t
    if s>=4 and not (g>0 and t>0 and used<=s*s+1):
        raise AssertionError("constructive grouping lacks original spread capacity")
    if used*(s+1)>V or t*(s+1)>nonanchor:
        raise AssertionError("group palette capacity violated")
    bad_point_pair_floor=used*comb(s+1,2)
    original_bad_pair_floor=2*s*bad_point_pair_floor
    # For each selected q, physical f-coordinate anchor has at least
    # t(s+1) globally labelled ORIGINAL POINTS; for any ORIGINAL r,
    # the cycle-deletion right g star degree of both endpoints >=a-3.
    right_star_floor=2*(a-3)
    d_f_floor=t*(s+1)
    # Exact integer numerator for lower bound on Wmean:
    # Delta/V * (#selected original bad (q,r)) * d_f_floor * d_g_floor.
    mean_floor_num=(s+1)*original_bad_pair_floor*d_f_floor*right_star_floor
    mean_floor_den=V
    return {
        **p,
        "anchor_coordinates":g,
        "other_coordinates":nonanchor,
        "spread_lines_per_anchor":t,
        "selected_disjoint_original_spread_lines":used,
        "total_spread_lines":s*s+1,
        "selected_original_points":used*(s+1),
        "forced_original_collinear_shared_coordinate_Mf_floor":bad_point_pair_floor,
        "forced_original_left_endpoint_bad_pairs_floor":original_bad_pair_floor,
        "left_source_coordinate_star_degree_floor":d_f_floor,
        "balanced_right_g_coordinate_star_degree_floor":a-3,
        "right_pair_star_sum_floor":right_star_floor,
        "exact_rational_mean_lower_numerator":mean_floor_num,
        "exact_rational_mean_lower_denominator":mean_floor_den,
        "unselected_original_points_count":V-used*(s+1),
        "unused_physical_pair_capacity_after_selected":comb(a,2)-used*(s+1),
        "constructive_obstruction":"M_f Omega(s^4), W_mean Omega(s^6)",
        "proved_ALL_h_asymptotic_Mf_coefficient":"3/32",
        "proved_ALL_h_asymptotic_Wmean_coefficient":"9/32",
        "original_7_family_S_lower_proved":False,
        "infinite_original_S_small_counterexample_proved":False,
    }


def irreducible_symmetric_parameter(field):
    """Find c in GF(2^h) with z²+c z+1 rootless (degree-2 extension)."""
    for c in range(1,field.q):
        if all(field.mul(z,z)^field.mul(c,z)^1 for z in range(field.q)):
            return c
    raise AssertionError("no irreducible quadratic / symplectic Desarguesian spread")


def actual_original_symplectic_spread(power):
    """Construct q²+1 TRUE ORIGINAL isotropic projective lines, not a surrogate.

    Standard form used by project's symplectic_gq:
      <(x,y),(x',y')> = x dot y'+y dot x'.
    For each (b,d) in F_q², M=[[b,d],[d,b+c*d]] is symmetric.
    Difference is invertible because det M=b²+cbd+d² != 0.
    Hence their graph projective lines and the vertical line partition
    every original projective point and are totally isotropic.
    """
    field,points,lines,incidences=_geometry(power)
    q=field.q
    if q>16:
        raise ValueError("finite explicit original symplectic geometry restricted to project's supported GF")
    c=irreducible_symmetric_parameter(field)
    ix={p:i for i,p in enumerate(points)}
    l_ix={tuple(line):i for i,line in enumerate(lines)}
    xreps=[(1,z) for z in range(q)]+[(0,1)]
    def from_graph(b,d):
        entries=[]
        for x0,x1 in xreps:
            y0=field.mul(b,x0)^field.mul(d,x1)
            y1=field.mul(d,x0)^field.mul(b^field.mul(c,d),x1)
            pp=normalized((x0,x1,y0,y1),field)
            entries.append(ix[pp])
        return tuple(sorted(entries))
    spread=[]
    for b in range(q):
        for d in range(q):
            original_line=from_graph(b,d)
            if original_line not in l_ix:
                raise AssertionError("symmetric graph is NOT an ORIGINAL W(3,s) isotropic line")
            spread.append(l_ix[original_line])
    vert=tuple(sorted(ix[normalized((0,0,x0,x1),field)] for x0,x1 in xreps))
    if vert not in l_ix:
        raise AssertionError("vertical line not ORIGINAL isotropic")
    spread.append(l_ix[vert])
    if len(spread)!=q*q+1 or len(set(spread))!=len(spread):
        raise AssertionError("symplectic spread size or distinctness")
    point_count=[0]*len(points)
    for l in spread:
        for p in lines[l]:
            point_count[p]+=1
    if any(n!=1 for n in point_count):
        raise AssertionError("explicit original symplectic spread does not PARTITION points")
    # independently check ORIGINAL alternating orthogonality for every
    # unordered pair in each spread line.
    for l in spread:
        for p,r in combinations(lines[l],2):
            if symplectic(points[p],points[r],field):
                raise AssertionError("nonisotropic original symplectic spread chord")
    return (field,points,lines,incidences),tuple(spread),c


def balanced_right_labels(s,a):
    """Full original-line pair injection: remove <=a-2 cycle edges only.

    The omitted edges have maximum physical vertex-degree TWO. Every
    coordinate therefore participates in >=a-3 original line labels.
    """
    p=parameters(s)
    excess=comb(a,2)-p["V"]
    if not 0<=excess<a-1:
        raise AssertionError("minimal palette slack inconsistent")
    skipped={tuple(sorted((i,(i+1)%a))) for i in range(excess)}
    if len(skipped)!=excess:
        raise AssertionError("cycle excess edges not distinct")
    edges=tuple(e for e in combinations(range(a),2) if e not in skipped)
    if len(edges)!=p["V"] or len(set(edges))!=p["V"]:
        raise AssertionError("balanced right global pair injection incomplete")
    stars=[0]*a
    for x,y in edges:
        stars[x]+=1
        stars[y]+=1
    if min(stars)<a-3:
        raise AssertionError("omitted-cycle right star degree is not balanced")
    return edges


def true_spread_counterfamily(power, *, check_full_energy=True):
    """Actual W34/W38 example, with complete ORIGINAL incidences and f,g."""
    if power not in (2,3):
        raise ValueError("full genuine finite original instances restricted to GF4/GF8")
    (field,points,lines,incidences),spread,c=actual_original_symplectic_spread(power)
    q=field.q
    p=plan(q)
    a,V=p["a"],p["V"]
    g=p["anchor_coordinates"]
    t=p["spread_lines_per_anchor"]
    L=g*t
    if L>len(spread) or not L:
        raise AssertionError("not enough ORIGINAL symplectic spread lines")
    left=[None]*V
    # Use coordinate i as one endpoint for EVERY point on t spread
    # lines; distinct other endpoints only.  No pair reused globally.
    nanchor=g
    for i in range(g):
        pts=[u for l in spread[i*t:(i+1)*t] for u in lines[l]]
        if len(pts)!=t*(q+1) or len(set(pts))!=len(pts):
            raise AssertionError("original selected lines not disjoint")
        for j,u in enumerate(pts):
            if left[u] is not None:
                raise AssertionError("original spread grouping repeats a physical point")
            left[u]=(i,nanchor+j)
    seen={e for e in left if e is not None}
    if len(seen)!=L*(q+1):
        raise AssertionError("selected global physical labels reused")
    remainder=iter(e for e in combinations(range(a),2) if e not in seen)
    for u in range(V):
        if left[u] is None:
            left[u]=next(remainder)
    if len(set(left))!=V:
        raise AssertionError("entire ORIGINAL f injection invalid")
    right=balanced_right_labels(q,a)
    model=_model(q,points,lines,incidences,left,right)
    core=ProjectionClosure(model)
    Mf,Mg=_pencil_motifs(core)
    if Mf<p["forced_original_collinear_shared_coordinate_Mf_floor"]:
        raise AssertionError("constructed true original M_f smaller than all-h symbolic proof")
    if check_full_energy:
        d3=double_centered_energy(model)
        if d3["left_concurrent_physical_Mf"]!=Mf:
            raise AssertionError("independent original GQ spectral Mf census inconsistent")
        from fractions import Fraction
        floor=Fraction(p["exact_rational_mean_lower_numerator"],
                       p["exact_rational_mean_lower_denominator"])
        if Fraction(d3["W_mean"])<floor:
            raise AssertionError("real signed ORIGINAL energy violates spread mean floor")
        signed={
            "complete_original_bad_GQ_pairs":d3["union_bad_original_pair_count"],
            "W_full_original_GQ":d3["physical_full_G_endpoint_energy_W"],
            "W_original_mean":d3["W_mean"],
            "W_original_signed_corr":d3["W_centered_correlation"],
            "mean_lower_checked":True,
        }
    else:
        signed={"mean_lower_checked":False}
    return {
        **p,"extension_power":power,
        "chosen_irreducible_matrix_parameter_c":c,
        "all_spread_lines_are_true_original_W3s":True,
        "spread_partitions_all_original_points":True,
        "global_left_unordered_pair_injection":True,
        "global_right_unordered_pair_injection":True,
        "true_original_right_label_star_min":min(
            Counter(x for e in right for x in e).values()),
        "Mf_actual":Mf,"Mg_actual":Mg,
        "Mf_floor_attained_or_exceeded":True,
        **signed,
    }


def report():
    # s16..s1024 arithmetic is all-h analytic (NO fake geometric finite
    # certificate). Explicit q4/q8 tests are true ORIGINAL symplectic GQ.
    true=[true_spread_counterfamily(power) for power in (2,3)]
    analytic=[plan(2**h) for h in (4,5,6,7,8,9,10)]
    return {
        "slice":"HYP105-ISSUE230-D4-TRUE-SYMPLECTIC-SPREAD-ROUTE-FALSIFIER",
        "all_h_counterfamily_for_D3_Mf_little_o":True,
        "all_h_counterfamily_for_D3_Wmean_little_o":True,
        "all_h_Mf_asymptotic_lower_coefficient":"3/32",
        "all_h_Wmean_asymptotic_lower_coefficient":"9/32",
        "universal_original_Mf_o_s39over10":"FALSE",
        "universal_original_Wmean_o_s59over10":"FALSE",
        "universal_FULL_signed_W_G_o_s59over10":"NOT ESTABLISHED",
        "universal_PR394_pruned_W_H_o_s59over10":"NOT ESTABLISHED",
        "universal_all_seven_S_lower":"OPEN",
        "infinite_Branch_B_S_small":"NOT ESTABLISHED",
        "actual_original_geometry_certificates":true,
        "symbolic_all_h_parameter_certificates":analytic,
    }


if __name__=="__main__":
    print(json.dumps(report(),sort_keys=True,indent=2))
