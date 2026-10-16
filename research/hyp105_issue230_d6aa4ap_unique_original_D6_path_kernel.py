"""HYP-105 #230 AA4-AP: ORIGINAL D6 unique path-aligned source-Hall kernel.

Fix actual original W(3,2^h), h>=1, same complete globally injected
typed physical edge maps f,g and ACTUAL source D-compatible anchor
e0=(p0,l0), e1=(p1,l1). On both typed physical projections, the
D6 selected alignment condition requires a physical connected C6.

Fix a connected physical C6 residual P5 path on each typed side,
oriented from the nonshared port of e0 to that of e1. Both physical
cycle-dual graphs have the two original flag positions e0,e1 as
FIXED ADJACENT vertices. A C6 automorphism fixing two adjacent
vertices pointwise is the IDENTITY. Thus their four residual flag
positions must agree in path order. At most ONE of 24 source
4-slot permutations can align the two physical C6 column-duals.
The unique original D6 candidate has true source flags
    (p2,l2), (p3,l3), (p4,l4), (p5,l5),
with typed original factor labels in ordered path edge positions.
Acceptance is exactly product of 4 true original GQ incidence bits,
on the SAME actual original f/g, without an independent map redraw.

This new restricted all-h exact Boolean 4-neighbor D6 path kernel is
independent of general 0/1/2 actual original four-rook Hall permanent
(earlier AA4-AE #512), and proves even an induced original C8
two-completion source Hall template contains at most one aligned D6.
No all-global original selected 7-class positive lower is claimed.
"""
from collections import Counter
from itertools import permutations,product
from math import comb
from hyp105_issue230_d6aa4al_global_original_coordinate_transport import (
    _actual_strict_original_transport,_parameters)
from hyp105_issue230_d6aa4an_port_completion_hall_funnel import (
    true_original_D_physical_ports)

def _edge(u,v):
    if u==v:raise ValueError("loop not a physical edge")
    return (u,v) if u<v else (v,u)

def occupied_oriented_original_P5_paths(ports,global_original_labels,a):
    """True original point or line source factor path tuples in fixed
    order e0-port to e1-port. Never fabricate missing physical labels."""
    ports=tuple(ports)
    if len(ports)!=3 or len(set(ports))!=3:
        raise ValueError("D anchor requires common center and two ports")
    center,first,last=ports
    inv={tuple(e):i for i,e in enumerate(global_original_labels)}
    if len(inv)!=len(global_original_labels):
        raise ValueError("source factor global physical images not injected")
    if _edge(center,first) not in inv or _edge(center,last) not in inv:
        raise ValueError("D anchor not occupied")
    other=tuple(v for v in range(a) if v not in ports)
    paths={}
    for alpha,beta,gamma in permutations(other,3):
        edges=(_edge(first,alpha),_edge(alpha,beta),
               _edge(beta,gamma),_edge(gamma,last))
        if all(e in inv for e in edges):
            src=tuple(inv[e] for e in edges)
            if len(set(src))!=4 or src in paths:
                raise AssertionError("same original global physical path duplicated")
            paths[src]=(alpha,beta,gamma)
    return paths

def true_original_D6_direct_path_kernel(model,pair,*,direction="point",
                                        include_Q=False,max_first_paths=None):
    """Exact D6 genuine source four-flag acceptance via original
    four-neighbor Cartesian tuples, not 24-permutation Hall matching.
    Source point-first and line-first are independent sparse oracles.

    max_first_paths is used only for EXPLICIT partial finite tests.
    """
    s,V,d,a,left,right,inc,np,nl=_actual_strict_original_transport(model)
    pair=tuple(pair)
    ports=true_original_D_physical_ports(inc,left,right,pair)
    pl=occupied_oriented_original_P5_paths(ports[0],left,a)
    ll=occupied_oriented_original_P5_paths(ports[1],right,a)
    if direction not in ("point","line"):
        raise ValueError("point or line direction required")
    if max_first_paths is not None and (
        type(max_first_paths) is not int or max_first_paths<1):
        raise ValueError("positive integer source path budget")
    first=pl if direction=="point" else ll
    other=ll if direction=="point" else pl
    nbs=np if direction=="point" else nl
    index={tuple(flag):i for i,flag in enumerate(inc)}
    selected=set()
    compared=examined=0
    for first4 in first:
        if max_first_paths is not None and examined>=max_first_paths:break
        examined+=1
        for second4 in product(*(nbs[x] for x in first4)):
            compared+=1
            if second4 not in other:continue
            ps=first4 if direction=="point" else second4
            ls=second4 if direction=="point" else first4
            flags=tuple(index.get((p,l)) for p,l in zip(ps,ls))
            if (None in flags or len(set(flags))!=4 or
                    set(flags)&set(pair)):
                raise AssertionError("not true four DISTINCT ORIGINAL incidences")
            Q=tuple(sorted(pair+flags))
            if len(Q)!=6 or len(set(Q))!=6 or Q in selected:
                raise AssertionError("double counted same six TRUE source flag IDs")
            selected.add(Q)
    if max_first_paths is None and len(selected)>min(
            len(pl)*len(ll),len(pl)*d**4,len(ll)*d**4):
        raise AssertionError("GQ four-neighbor D6 path bound")
    return {
        "s":s,"source_actual_D_pair":pair,"direction":direction,
        "point_occupied_original_P5_paths":len(pl),
        "line_occupied_original_P5_paths":len(ll),
        "physically_occupied_P5xP5_template_pairs":len(pl)*len(ll),
        "source_original_GQ_four_neighbor_tuples_examined":compared,
        "first_typed_original_P5_paths_examined":examined,
        "partial_source_first_paths_only":max_first_paths is not None,
        "accepted_original_D6_D_anchor_charge":len(selected),
        "accepted_true_original_D6_six_incidence_Q":
            tuple(sorted(selected)) if include_Q else None,
        "unique_D6_original_source_4flag_per_physical_P5xP5":True,
        "all_h_complete_D6_4neighbor_source_upper":
            min(len(pl)*len(ll),len(pl)*d**4,len(ll)*d**4),
        "NO_all_map_GF5_seven_six_Q_lower":True}

def independent_D6_physical_pairs(model,pair,*,max_physical_pairs=None):
    """Independent physical-template-pair-MAJOR oracle, no d^4 source
    neighbor expansion. Exhaustive unless a budget is EXPLICIT."""
    s,V,d,a,left,right,inc,np,nl=_actual_strict_original_transport(model)
    ports=true_original_D_physical_ports(inc,left,right,pair)
    pl=occupied_oriented_original_P5_paths(ports[0],left,a)
    ll=occupied_oriented_original_P5_paths(ports[1],right,a)
    index={tuple(flag):i for i,flag in enumerate(inc)}
    checked=0;got=set()
    for p4 in pl:
        for l4 in ll:
            if max_physical_pairs is not None and checked>=max_physical_pairs:
                break
            checked+=1
            flags=tuple(index.get((p,l)) for p,l in zip(p4,l4))
            if None in flags:continue
            if len(set(flags))!=4 or set(flags)&set(pair):
                raise AssertionError("D6 physical matched original flag duplicate")
            Q=tuple(sorted(pair+flags))
            if Q in got:raise AssertionError("physical path template re-used source Q")
            got.add(Q)
        if max_physical_pairs is not None and checked>=max_physical_pairs:
            break
    return {"physical_template_pairs_examined":checked,
            "accepted_original_D6_D_anchor_charge":len(got),
            "partial_physical_only":max_physical_pairs is not None,
            "original_D6_six_Q":tuple(sorted(got))}

def true_original_W32_all_D6_source_path_census(model,*,
                                                independent_physical=False,
                                                historical_Q_first=True):
    """True W32 all ACTUAL source D pairs, unique path D6, independent
    original historical 7-tag Q-FIRST comparison."""
    from hyp105_issue230_d6aa4am_genuine_pair_sixcharge import (
        original_D_pair_index,exact_W32_original_seven_pair_extension_certificate)
    s,V,d,a,left,right,inc,np,nl=_actual_strict_original_transport(model)
    if (s,V,a,len(inc))!=(2,15,6,45):
        raise ValueError("complete original W32 only")
    D=original_D_pair_index(model)
    union=set();charge=0;positive=0;hist=Counter()
    for pair in sorted(D):
        z=true_original_D6_direct_path_kernel(
            model,pair,include_Q=True)
        selected=set(z["accepted_true_original_D6_six_incidence_Q"])
        if independent_physical:
            other=independent_D6_physical_pairs(model,pair)
            if selected!=set(other["original_D6_six_Q"]):
                raise AssertionError("physical-pair-major independent D6 disagreement")
        charge+=len(selected);positive+=bool(selected)
        hist[len(selected)]+=1
        union.update(selected)
    if charge!=6*len(union):
        raise AssertionError("original aligned D6 must have SIX D anchors")
    if historical_Q_first:
        prior=exact_W32_original_seven_pair_extension_certificate(
            model,independent_oracle=True)
        if (charge!=prior["seven_original_D_extension_E_by_tag"]["D6"] or
                len(union)!=prior["seven_original_S_by_tag"]["D6"]):
            raise AssertionError("historical original Q-FIRST seven-GF5 D6 not equal")
    return {
        "s":s,"actual_original_D_pairs":len(D),
        "exact_D6_true_original_D_anchor_charge":charge,
        "exact_D6_unique_true_original_six_Q":len(union),
        "D_anchor_with_positive_D6_extensions":positive,
        "D_anchor_D6_charge_histogram":dict(hist),
        "independent_physical_D6_oracle":bool(independent_physical),
        "historical_Q_FIRST_selected_seven_D6_agreed":bool(historical_Q_first),
        "NO_universal_all_seven_GF5_positive_s6_lower":True}

def all_h_original_D6_unique_source_path_upper(s):
    V,d,a=_parameters(s)
    count=6*comb(a-3,3)
    return {
        "s":s,"V":V,"d":d,"a":a,
        "full_Ka_P5_per_typed_side":count,
        "full_Ka_physical_P5xP5_template_capacity":count*count,
        "true_original_source_neighbor_cap_per_D_anchor":
            min(count*count,count*d**4),
        "aligned_original_D6_at_most_ONE_per_occupied_physical_P5xP5":True,
        "non_P5_template_cannot_be_D6":True,
        "no_root_issue230_A_B_C_proof":True}
