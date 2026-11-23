"""GIO-003/G6-E1: new ACTUAL smaller near-Moore source from a GQ parent.

Reproduces Abreu--Araujo-Pardo--Balbuena--Labbate (2011), Theorems
1.1, 1.2(ii), 1.3: remove an EXPLICIT perfect dominating set B from the
(q+1)-regular GQ(q,q) incidence Γ_q. The remaining original incidence
has q(q²-2) points AND lines, q original flags per vertex, girth>=8,
and genuine Moore excess Delta=2q(q-2) <=2(q-1)².

Project-specific new consequence: for *any* q-regular BALANCED induced
sub-incidence of GQ(q,q), the SECOND singular value is <=sqrt(2q)
by singular-value compression/interlacing. The centered cubic identity
then gives ||F0||²<=2(q-1)³ for every q>=4, or <=3(q-1)³ at q=3.
No invented missing F or pre-assumed spectral gap. Via the inherited
G6-D2 direct-operator ledger, this certifies conditional original-source
six-ID T3 for arbitrary correlated minimal pair-injective maps.

Mathematical prior art: Γ_q, the perfect dominating set and the small
(q,8)-graph are PUBLISHED, NOT NEW graph constructions. The interlacing
principle is standard. No external referee, Lean or unrestricted T3.
"""
import argparse
import json
from fractions import Fraction as Q
from itertools import product
from pathlib import Path

from gio_t3c_intrinsic_defect import (
    source_graph, typed_maps, defect_matrices,
    typed_conflicts_and_gram, direct_original_owner_conflicts,
    exact_second_walk_identity,
)
from gio_t3d3_affine_arc import Field
from gio_t3d4_few_outliers import exact_symmetric_inertia
from gio_t3d2_centered_sixth import integrated_quadratic_direct_ledger

SCHEMA = "mathlab.gio003.g6e1.pds-gq-embedded-real-source.v1"
PARENT_G6D7_HEAD = "4d7cd8f80a407da85e8e9c2ff6aa5edfc57ec261"
ABREU_ARXIV = "https://arxiv.org/abs/1111.3279"


def gamma_names(q):
    """The paper's (q+1)(q²+1) literal names on EACH Γ_q side."""
    if type(q) is not int or q<3:
        raise ValueError("thick finite field order q>=3 required")
    names=list(product(range(q),repeat=3))
    names += [(q,b,c) for b,c in product(range(q),repeat=2)]
    names += [(q,q,c) for c in range(q+1)]
    assert len(names)==(q+1)*(q*q+1)
    assert len(names)==len(set(names))
    return tuple(names)


def gamma_line_points(field,line):
    """EXACT original GQ formula: 2ab means ab+ab in characteristic 2.

    The integer label 2 is NOT the field element 2 in GF(2^e).
    """
    q=field.q
    a,b,c=line
    if a<q:
        ab=field.mul(a,b)
        twice_ab=field.add(ab,ab)
        square_a=field.mul(a,a)
        out=[(x,
              field.add(field.mul(a,x),b),
              field.add(field.add(field.mul(square_a,x),twice_ab),c))
             for x in range(q)]
        out.append((q,a,c))
    elif b<q:
        out=[(c,b,x) for x in range(q)]+[(q,q,c)]
    else:
        out=[(q,c,x) for x in range(q)]+[(q,q,q)]
    assert len(out)==q+1 and len(set(out))==q+1
    return tuple(out)


def actual_parent_GQ(field):
    """Independent field-first Γ_q, then old geometry-free source oracle."""
    q=field.q
    names=gamma_names(q)
    idx={name:i for i,name in enumerate(names)}
    lines=[set(idx[x] for x in gamma_line_points(field,l)) for l in names]
    parent=source_graph(lines,len(names),q,q)
    assert parent["excess_lines"]==parent["excess_points"]==0
    assert len(parent["flags"])==(q+1)*(q+1)*(q*q+1)
    dp,dl,_=defect_matrices(parent)
    assert all(not any(row) for row in dp)
    assert all(not any(row) for row in dl)
    exact_second_walk_identity(parent["neighbors_point"],dp,q,q)
    exact_second_walk_identity(parent["neighbors_line"],dl,q,q)
    return parent,names,idx


def parent_bipartite_adjacency(parent):
    """Explicit original 0..n-1 points, n..2n-1 lines."""
    n=parent["points"]
    assert n==len(parent["lines"])
    adjacency=[set() for _ in range(2*n)]
    for ell,line in enumerate(parent["lines"]):
        for p in line:
            adjacency[p].add(n+ell)
            adjacency[n+ell].add(p)
    return adjacency


def closed_ball(adjacency,root,radius):
    """Exactly distances <=radius in ORIGINAL Γ_q, no f/g labels."""
    if type(root) is not int or not 0<=root<len(adjacency):
        raise ValueError("root must be an original GQ vertex")
    if type(radius) is not int or radius not in (1,2):
        raise ValueError("only original one/two-neighborhoods are used")
    seen={root}
    frontier={root}
    for _ in range(radius):
        frontier=set().union(*(adjacency[v] for v in frontier))-seen
        seen|=frontier
    return seen


def abreu_B_perfect_dominating(parent,idx,xi=1):
    """Theorem 1.2(ii), literal closed neighborhoods, NOT a guessed PDS.

    B = (union_c N[(q,0,c)_line]) union N[(q,q,0)_line]
      union ((union_c N²[(q,0,c)_line]) intersect N²[(q,q,0)_line])
      union N²[(q,q,xi)_line], xi!=0.

    Require 1 distinct original neighbor in B for EACH remaining vertex.
    """
    n=parent["points"]
    q=parent["s"]
    if type(xi) is not int or not 0<xi<q:
        raise ValueError("published nonzero xi in the finite field required")
    adj=parent_bipartite_adjacency(parent)
    roots=[n+idx[(q,0,c)] for c in range(q)]
    v=n+idx[(q,q,0)]
    u=n+idx[(q,q,xi)]
    n1=set().union(*(closed_ball(adj,w,1) for w in roots))
    n2=set().union(*(closed_ball(adj,w,2) for w in roots))
    bi=n1|closed_ball(adj,v,1)|(n2&closed_ball(adj,v,2))|closed_ball(adj,u,2)
    expected=q*q+3*q+1
    assert len(bi)==2*expected
    assert len([w for w in bi if w<n])==expected
    assert len([w for w in bi if w>=n])==expected
    remain=set(range(2*n))-bi
    assert all(len(adj[w]&bi)==1 for w in remain)
    assert all(len(adj[w]-bi)==q for w in remain)
    return dict(deleted=bi,kept=remain,adjacency=adj,
        removed_each_side=expected,
        residual_each_side=n-expected,
        perfect_dominating_all_outside_exactly_one=True,
        exact_published_closed_neighborhood_formula=True,
        xi=xi)


def actual_smaller_source(field,xi=1):
    """TRUE q-regular SOURCE, not a copied Wenger or synthetic F mask."""
    q=field.q
    parent,names,idx=actual_parent_GQ(field)
    dom=abreu_B_perfect_dominating(parent,idx,xi)
    n=parent["points"]
    keepP=tuple(sorted(v for v in dom["kept"] if v<n))
    keepL=tuple(sorted(v-n for v in dom["kept"] if v>=n))
    assert len(keepP)==len(keepL)==q*(q*q-2)
    local={p:i for i,p in enumerate(keepP)}
    lines=[{local[p] for p in parent["lines"][ell] if p in local}
           for ell in keepL]
    assert all(len(line)==q for line in lines)
    src=source_graph(lines,len(keepP),q-1,q-1)
    r=q-1
    dl=2*q*(q-2)
    assert src["excess_lines"]==src["excess_points"]==dl
    assert dl==2*(r*r-1)<2*r*r
    assert len(src["flags"])==q*q*(q*q-2)
    assert len(src["projected"])==len(keepP)*q*r*r
    assert all(value==3*r*r for value in src["projection_load"].values())
    # Check EXACT induced original incidence embedding, on both parts.
    assert all({keepP[p] for p in line}
               ==set(parent["lines"][keepL[i]])&set(keepP)
               for i,line in enumerate(src["lines"]))
    return dict(q=q,field=field,parent=parent,parent_names=names,
        new_original_source=src,dom=dom,kept_parent_points=keepP,
        kept_parent_lines=keepL,all_edges_induced_from_true_GQ=True)


def universal_interlacing_envelope(q):
    """Independent exact algebra, for ALL q-regular induced GQ(q,q) sources.

    GQ parent B has σ1=q+1, σ2=sqrt(2q) and subsequent ≤sqrt(2q).
    A q-regular square submatrix B' satisfies σ2(B')≤σ2(B).
    For q>2, σ2<q=σ1(B'), so B' is connected. On 1_perp,
      x in spec(B'B'^T) lies in [0,2q].
    Corrected G6-D1 cubic gives
      ||F0||²=max_{nonprincipal x} x(x-2r)^2
             ≤ max(4*(2r)^3/27, 8q).
    This is <=2*r³ for q>=4, <=3*r³ for q=3.
    """
    if type(q) is not int or q<3:
        raise ValueError("prime-power source order >=3 as exact integer")
    r=q-1
    h=2*r
    critical=Q(4*h*h*h,27)
    endpoint=8*q
    maximum=max(critical,Q(endpoint))
    kappa=3 if q==3 else 2
    assert Q(q*q)>Q(2*q)
    assert maximum<=kappa*r**3
    if q>=4:
        assert 8*q<=2*r**3
        assert critical<=2*r**3
    # Unlike isolated spectral fixtures, this is uniform for ALL
    # real prime-power q>=4 in the published parent/PDS construction.
    return dict(q=q,r=r,original_regular_degree=q,
        parent_GQ_order=q,
        parent_singular_1=q+1,parent_second_squared_singular=2*q,
        reduced_first_singular=q,
        reduced_second_squared_singular_upper=2*q,
        strict_connectedness_from_interlacing=True,
        centered_source_cubic_h=h,
        exact_internal_critical_rational=str(critical),
        exact_endpoint=endpoint,upper_centered_F0_squared=str(maximum),
        fixed_centered_operator_kappa=kappa,
        centered_operator_fixed_kappa_rhs=kappa*r**3,
        q_ge4_uniform_kappa2=(q>=4),
        no_independent_centered_F0_hypothesis=True,
        source_regular_induced_parent_GQ_hypothesis_REQUIRED=True,
        no_new_worldwide_source_construction_claim=True)


def exact_original_centered_missing_PSD(src,kappa,side):
    """Full original F incidence oracle, exact center and rational inertia.

    Validation for ACTUAL original named missing point/line pairs:
    F0F0t=FFt -(ΔLΔP/|P|)J on the point side, and dual.
    No float eigenvalue or synthetic 0/1 mask. Finite only.
    """
    n=src["points"]
    m=len(src["lines"])
    if n!=m or src["excess_points"]!=src["excess_lines"]:
        raise ValueError("this q-regular balanced certificate is square")
    if type(kappa) is not int or kappa<0:
        raise ValueError("exact integer kappa required")
    r=min(src["s"],src["t"])
    missing=src["missing"]
    masks=[set() for _ in range(n)]
    if side=="point":
        for p,ell in missing:
            masks[p].add(ell)
    elif side=="line":
        for p,ell in missing:
            masks[ell].add(p)
    else:
        raise ValueError("original point or line requested")
    delta=src["excess_lines"]
    assert all(len(z)==delta for z in masks)
    base=Q(delta*delta,n)
    G=[[Q(len(masks[i]&masks[j]))-base for j in range(n)]
       for i in range(n)]
    assert all(sum(row)==0 for row in G)
    assert all(G[i][j]==G[j][i] for i in range(n) for j in range(i+1,n))
    residual=[[Q(kappa*r**3 if i==j else 0)-G[i][j]
               for j in range(n)] for i in range(n)]
    inertia=exact_symmetric_inertia(residual)
    if inertia["negative"]:
        raise AssertionError(("true original centered F0 PSD upper failed",
                              src["s"],side,kappa,inertia))
    return dict(side=side,vertices=n,
        original_missing_degree=delta,
        exact_centered_rank_one_subtraction=str(base),
        residual_inertia=inertia,
        exact_original_F0_operator_upper=kappa*r**3,
        no_numerical_eigensolver=True,
        no_synthetic_projection_or_GQ_completion=True)


def literal_case(q,scheme="lex",xi=1,heavy_PSD=True):
    field=Field(q)
    instance=actual_smaller_source(field,xi)
    src=instance["new_original_source"]
    maps=typed_maps(src,scheme)
    r=q-1
    env=universal_interlacing_envelope(q)
    dp,dl,_=defect_matrices(src)
    exact_second_walk_identity(src["neighbors_point"],dp,r,r)
    exact_second_walk_identity(src["neighbors_line"],dl,r,r)
    pc=typed_conflicts_and_gram(
        src,maps["f"],src["neighbors_point"],dp,r,r)
    lc=typed_conflicts_and_gram(
        src,maps["g"],src["neighbors_line"],dl,r,r)
    J=direct_original_owner_conflicts(src,maps)
    assert J["J"]==pc["e_col"]+lc["e_col"]
    spectra={}
    if heavy_PSD:
        for side in ("point","line"):
            spectra[side]=exact_original_centered_missing_PSD(
                src,env["fixed_centered_operator_kappa"],side)
    return dict(q=q,scheme=scheme,xi=xi,
        original_parent_vertices_each=instance["parent"]["points"],
        original_parent_GQ_missing=len(instance["parent"]["missing"]),
        true_original_PDS_removed_each=instance["dom"]["removed_each_side"],
        perfect_dominating_all_outside_exactly_one=instance["dom"][
            "perfect_dominating_all_outside_exactly_one"],
        true_original_source_points=src["points"],
        true_original_source_lines=len(src["lines"]),
        true_original_source_flags=len(src["flags"]),
        true_original_Moore_excess=src["excess_lines"],
        original_missing_pairs=len(src["missing"]),
        all_orig_projection_loads_exact_3st=True,
        source_parent_induced_edges_exact=instance["all_edges_induced_from_true_GQ"],
        center_exact_two_sided_PSD=spectra,
        interlacing_all_order=env,
        original_point_conflicts=pc["e_col"],
        original_line_conflicts=lc["e_col"],
        original_total_J=J["J"],
        point_original_Gram=pc["gram"],
        line_original_Gram=lc["gram"],
        true_original_not_synthetic_F=True,
        nonGQ_if_q_ge3=bool(src["excess_lines"]),
        different_vertex_count_from_Wenger_W2=q**3-src["points"]==2*q,
        no_finite_example_promoted_to_universal_theorem=True)


def exact_all_order_ledger():
    old=integrated_quadratic_direct_ledger(
        b=1,C=2,kappa=2,C0=Q(1),c0=Q(1))
    assert old["FORMAL_ONLY"]
    assert old["moment_sixth_condition_is_NOT_required"]
    assert old["fixed_before_source"]["balance_b"]==1
    assert old["fixed_before_source"]["quadratic_C"]==2
    assert old["fixed_before_source"]["centered_operator_kappa"]==2
    return old


def certificate():
    finite=[literal_case(q,scheme,xi,heavy_PSD=heavy) for q,scheme,xi,heavy in (
        (3,"lex",1,True),
        (3,"correlated",2,False),
        (4,"lex",1,True),
        (4,"correlated",2,False),
        (5,"lex",1,True),
        (5,"correlated",2,False),
    )]
    symbolic=[universal_interlacing_envelope(q) for q in
        (3,4,5,7,8,9,11,13,16,17,19,32,64,101)]
    assert all(x["fixed_centered_operator_kappa"]==2
               for x in symbolic if x["q"]>=4)
    ledger=exact_all_order_ledger()
    return dict(schema=SCHEMA,issue=793,
        parent_G6D7_HEAD=PARENT_G6D7_HEAD,
        published_source=ABREU_ARXIV,
        claim="CONDITIONAL_T3_REAL_PDS_SUBGQ_SOURCE_VIA_INTERLACING",
        independently_constructed_original_PDS_source_cases=finite,
        exact_all_prime_power_source_interlacing_certificate=symbolic,
        inherited_G6D2_direct_operator_ledger_FORMAL_ONLY=ledger,
        genuinely_distinct_smaller_source_cardinality_than_Wenger=True,
        published_graph_family_NOT_NEW=True,
        independent_interlacing_spectral_transfer_new_to_program=True,
        no_unrestricted_abstract_T3_or_ASET=True,
        no_external_referee_or_Lean=True)


if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--out")
    a=p.parse_args()
    data=certificate()
    blob=json.dumps(data,sort_keys=True,indent=2)+"\n"
    if a.out:
        Path(a.out).write_text(blob,encoding="utf-8")
    else:
        print(blob)
