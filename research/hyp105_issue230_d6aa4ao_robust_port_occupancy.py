"""HYP-105 #230 AA4-AO: globally injected original D-port PHYSICAL occupation.

Fix one genuine original W(3,2^h) bilateral D pair with a shared physical
coordinate on each typed globally injective edge image. The residual
point- and line-side AA4-AN port patterns P5, K2+C3, P3+double K2
must use globally occupied actual source factor physical edges.

Let U=[a]\\{center,p,q}, n=a-3 and M be missing global physical
edge images, m=|M|<=a-2. Dp,Dq count missing edges from the two ports
into U; i counts missing edges entirely within U.

TOTAL directed P5 templates = n(n-1)(n-2).
Deletion union bound, exact for ANY globally injected image:
  occupied P5 >= max(0,
      (n-Dp-Dq)*(n-1)*(n-2) -4*i*(n-2))
             >= max(0,(n-m)*(n-1)*(n-2)) when n>=5.

If m<=a-4=n-1 then EVERY original D pair on EACH typed side
has >=(n-m)(n-1)(n-2) occupied P5, even for adversarial f,g.
Point/line two-sided physical P5-P5 count >= the square.

If m=a-3=n and n>=7: when physical port-port p-q edge is
occupied, deleting at most n edges inside K_n still leaves
a physical triangle (Mantel). Else p-q consumes one missing
edge, leaving at most n-1 deleted other edges and the P5
union bound is positive. Thus EVERY actual D pair has some
occupied port completion on EACH side for m<=a-3.
If m=a-2 the abstract K_a image can leave a port isolated
outside its existing center edge: no physical residual at all.
That is SHARPNESS for arbitrary physical injection, NOT an
actual infinite original W(3,s) source counterfamily.

For "good" ports with Dp+Dq<=n/4 on each typed side, n>=32,
m<=n+1, occupied typed P5 >=n(n-1)(n-2)/2.
If both typed ports are good, the product gives >=1/4
[n(n-1)(n-2)]^2 two-sided occupied PHYSICAL P5 templates.

NONE of these all-h physical bounds proves genuine source Hall
or selected original seven-GF5 acceptance. A lower on the
number of D pairs with GOOD physical ports is also UNKNOWN.
"""
from fractions import Fraction
from itertools import combinations
from math import comb

from hyp105_issue230_d6aa4al_global_original_coordinate_transport import (
    _parameters,_actual_strict_original_transport)
from hyp105_issue230_d6aa4an_port_completion_hall_funnel import (
    true_original_D_physical_ports,physical_D_pair_half_patterns,
    _strict_occupied_half_patterns,physical_edge)


def _physical_missing_edges(a,occupied):
    E=frozenset(tuple(sorted(e)) for e in occupied)
    if (type(a) is not int or a<6 or
        any(len(e)!=2 or e[0]==e[1] or
            min(e)<0 or max(e)>=a for e in E)):
        raise ValueError("simple physical K_a edge image required")
    return frozenset(combinations(range(a),2))-E


def physical_P5_robust_certificate(ports,a,occupied):
    """Exact physical P5 count, and pointwise missing-edge lower."""
    c,p,q=tuple(ports)
    if len({c,p,q})!=3 or any(v<0 or v>=a for v in (c,p,q)):
        raise ValueError("three different physical coordinates")
    E=frozenset(tuple(sorted(e)) for e in occupied)
    if physical_edge(c,p) not in E or physical_edge(c,q) not in E:
        raise ValueError("actual pinned physical edges must be occupied")
    M=_physical_missing_edges(a,E)
    U=frozenset(range(a))-{c,p,q}
    n=len(U)
    dp=sum(physical_edge(p,x) in M for x in U)
    dq=sum(physical_edge(q,x) in M for x in U)
    inner=sum(e[0] in U and e[1] in U for e in M)
    pq_missing=int(physical_edge(p,q) in M)
    formal=n*(n-1)*(n-2)
    union_bound=max(0,(n-dp-dq)*(n-1)*(n-2)-4*inner*(n-2))
    crude=max(0,(n-len(M))*(n-1)*(n-2))
    actual=sum(all(physical_edge(v,w) in E for v,w in
                   ((p,x),(x,y),(y,z),(z,q)))
               for x in U for y in U if y!=x
               for z in U if z!=x and z!=y)
    if not (actual>=union_bound>=crude):
        raise AssertionError("missing-edge deletion P5 bound failed")
    return dict(a=a,n=n,missing_global_physical_edges=len(M),
                missing_port_p_to_U=dp,missing_port_q_to_U=dq,
                missing_internal_U_edges=inner,
                missing_direct_port_port=pq_missing,
                actual_occupied_P5=actual,
                formal_P5=formal,
                exact_union_bound_P5=union_bound,
                universal_m_only_bound_P5=crude,
                physical_good_ports=(dp+dq)*4<=n,
                this_is_PHYSICAL_not_original_Hall=True)


def all_h_robust_original_D_port_physical_theorem(s):
    """All-h guarantee for actual original W(3,2^h) physical images."""
    V,d,a=_parameters(s)
    n=a-3;m=comb(a,2)-V
    assert 0<=m<=a-2 and n>=3
    P5_lower=max(0,(n-m)*(n-1)*(n-2))
    every_pair_P5=m<=n-1
    # For s>=4, a>=14 n>=11, Mantel guarantees a triangle
    # within U after at most n physical edge deletions:
    # C(n,2)-n > floor(n²/4), checked by integer inequality.
    if n>=7 and m<=n:
        assert comb(n,2)-n>n*n//4
    any_pattern=(m<=n-1 or n>=7 and m<=n)
    good_P5=(Fraction(n*(n-1)*(n-2),2) if a>=35 else None)
    return dict(
        s=s,V=V,a=a,d=d,global_physical_missing_edges_per_type=m,
        auxiliary_coordinates=n,
        each_original_D_pair_typed_occupied_P5_lower=P5_lower,
        each_original_D_pair_two_side_occupied_P5_P5_lower=P5_lower**2,
        unconditional_typed_P5_positive_for_every_original_D=every_pair_P5,
        unconditional_some_typed_physical_pattern_for_every_original_D=any_pattern,
        conditional_both_port_missing_sum_at_most_n_over_4=True,
        conditional_typed_good_P5_lower=good_P5,
        conditional_two_side_good_P5_P5_lower=(
            good_P5**2 if good_P5 is not None else None),
        all_complete_original_global_injections=True,
        number_of_good_D_pairs_lower_NOT_PROVED=True,
        accepted_original_Hall_Q_positive_NOT_PROVED=True,
        original_seven_GF5_s6_lower_NOT_PROVED=True,
    )


def genuine_original_D_pair_robust_occupation(model,pair):
    """Same global f,g: real source D pair, true physical occupied edge."""
    s,V,d,a,left,right,inc,np,nl=_actual_strict_original_transport(model)
    pair=tuple(pair)
    ports=true_original_D_physical_ports(inc,left,right,pair)
    t=all_h_robust_original_D_port_physical_theorem(s)
    sides=[]
    for side in (0,1):
        physical=(left,right)[side]
        z=physical_P5_robust_certificate(ports[side],a,physical)
        independent=physical_D_pair_half_patterns(model,pair,side=side)
        assert independent["physical_occupied_topology_counts"].get("P5",0)==z[
            "actual_occupied_P5"]
        assert z["actual_occupied_P5"]>=t[
            "each_original_D_pair_typed_occupied_P5_lower"]
        if z["physical_good_ports"] and a>=35:
            assert z["actual_occupied_P5"]>=t[
                "conditional_typed_good_P5_lower"]
        sides.append(dict(z,
             all_three_occupied_physical_patterns=independent[
                 "physical_occupied_total"],
             physical_three_class_counts=independent[
                 "physical_occupied_topology_counts"]))
    return dict(
        s=s,original_D_pair=pair,
        original_point_physical=sides[0],original_line_physical=sides[1],
        occupied_two_side_P5_P5_physical_template_count=(
            sides[0]["actual_occupied_P5"]*sides[1]["actual_occupied_P5"]),
        theorem=t,
        all_h_original_source_Hall_lower_NOT_PROVED=True)


def independent_abstract_isolated_port_sharpness(a):
    """ABSTRACT complete physical injection, NOT an actual W(3,s)."""
    if type(a) is not int or a<8:
        raise ValueError("abstract physical alphabet a>=8")
    c,p,q=0,1,2
    deleted=frozenset(physical_edge(p,v) for v in range(a) if v!=c)
    assert len(deleted)==a-2
    E=frozenset(combinations(range(a),2))-deleted
    z=physical_P5_robust_certificate((c,p,q),a,E)
    inv={edge:j for j,edge in enumerate(sorted(E))}
    entries,formal,occupied=_strict_occupied_half_patterns((c,p,q),a,inv)
    assert z["actual_occupied_P5"]==0 and not entries
    return dict(a=a,missing_physical_edges=len(deleted),
                globally_injected_source_factor_count=len(E),
                occupied_residual_patterns=len(entries),
                physical_only_not_a_real_symplectic_GQ=True,
                no_infinite_original_source_counterfamily_claim=True)
