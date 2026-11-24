"""GIO-003 G6-E3: TRUE EVEN characteristic corrected 2021 Theorem 6.

Construct original q-regular G_q^x from the GQ(q,q) parent, then use
the DIFFERENT even-field quasi-perfect dominating S and matching M
in the May-18-2021 publisher corrigendum (pp.10-11). In GF(2^e)
addition = XOR; the infinity marker q is never a field element.

All-order source gate, q=2^e>=8:
 r=q-2>=6, |P|=|L|=q(q^2-q-4), degree q-1, Delta=4r^2+3r-5.
 sigma2(C)<=sqrt(2q)+1<=5 sqrt(r/6);
 x_centered in [0,25r/6]; corrected source-original cubic p(x)=
 x(x-2r)^2 gives ||F0||^2 <= (4225/216) r^3 < 20 r^3.
 Source gate (b,C,kappa)=(1,5,20), on BOTH original typed sides.

The corrected graph family, domination and matching are PUBLISHED
prior art; project-specific G6-D2 DIRECT spectral transfer is an
application of standard GQ singular interlacing and Weyl.
"""
import argparse
import json
from collections import Counter
from functools import lru_cache
from fractions import Fraction as Q
from pathlib import Path

from gio_t3d3_affine_arc import Field
from gio_t3e1_subgq_pds import actual_smaller_source
from gio_t3e2_corrigendum_quasi_pds import stage_one_adjacency, _closed_neighbors
from gio_t3c_intrinsic_defect import (
    source_graph, typed_maps, defect_matrices,
    exact_second_walk_identity, typed_conflicts_and_gram,
    direct_original_owner_conflicts,
)
from gio_t3d2_centered_sixth import (
    uniform_direct_spectral_constants,
    integrated_quadratic_direct_ledger,
)

SCHEMA="mathlab.gio003.g6e3.even-2021-corrigendum-matching-k20.v1"
PARENT_G6E2="ddac1e2eeb52556e7abda95f57ee6f5fd9c4a4ec"
PAPER="https://www.combinatorics.org/ojs/index.php/eljc/article/download/v22i2p10/pdf/"
CORRIGENDUM_DATE="2021-05-18"
CORRECTED_THEOREM="6 (even prime-power q>=8), pp. 10-11"


def even_params(field,x,m):
    """Corrected Theorem 6, with extra fail-closed distinctness.

    Published m !=0,1,x and x!=0,1. We ALSO require x!=m^(-1):
    otherwise the set {0,1,x,m,m^-1} has only 4 distinct elements,
    invalidating the q(q-5) counting gate. This is a deliberately
    more restrictive all-order SUBFAMILY, always available q>=8.
    """
    q=field.q
    if any(type(v) is not int for v in (x,m)) or not (
        0<=x<q and 0<=m<q):
        raise ValueError("exact source finite-field x,m labels required")
    if q<8 or q&(q-1):
        raise ValueError("corrected even source requires q=2^e>=8")
    inv=field.inv(m) if m else None
    if len({0,1,x,m,inv})!=5:
        raise ValueError("require distinct 0,1,x,m,m^-1 (source subfamily)")
    return dict(q=q,x=x,m=m,inverse_m=inv,
        characteristic_two_field_verified=True,
        corrected_2021_Theorem_6_not_odd_Theorem_5=True,
        no_false_2015_perfect_domination=True,
        stricter_x_not_inverse_m_gate=True,
        published_prime_power_existence_REQUIRED=True)


@lru_cache(maxsize=4)
def _cached_stage(q,x):
    """Build genuine original GQ and q-regular sub-incidence only once."""
    return stage_one_adjacency(actual_smaller_source(Field(q),xi=x))


def corrected_even_S_and_M(field,x,m):
    """LITERAL published Thm6 closed 1-neighborhoods and matching.

    R={(m,b,(m+m^-1)b)_LINE,(m^-1,b,(m+m^-1)b)_LINE:b in Fq}
    S=(union_c N_G[(inf,1,c)_POINT]) union N_G[R].
    M: original ((inf,a,(a+a^-1)b)_POINT,
                 (a,b,(a+a^-1)b)_LINE)
       for a outside 0,1,x,m,m^-1 and all b in Fq.
    """
    cfg=even_params(field,x,m)
    q=field.q
    stage=_cached_stage(q,x)
    n=stage["n"]
    m_inverse=cfg["inverse_m"]
    alpha=field.add(m,m_inverse)
    roots=[stage["point_lookup"][(q,1,c)] for c in range(q)]
    assert len(set(roots))==q
    R=set()
    for b in range(q):
        t=field.mul(alpha,b)
        R.add(n+stage["line_lookup"][(m,b,t)])
        R.add(n+stage["line_lookup"][(m_inverse,b,t)])
    assert len(R)==2*q
    closed_roots=_closed_neighbors(stage["adj"],roots)
    closed_R=_closed_neighbors(stage["adj"],R)
    deleted=closed_roots|closed_R
    assert len(closed_roots)==q*(q+1)
    assert len(closed_R)==q*q+3*q
    assert not closed_roots&closed_R
    assert len(deleted)==2*q*q+4*q
    half_removed=q*q+2*q
    assert sum(p<n for p in deleted)==half_removed
    assert sum(p>=n for p in deleted)==half_removed
    kept=set(range(2*n))-deleted
    assert len(kept)==2*q*(q*q-q-4)
    pre_degree={v:len(stage["adj"][v]&kept) for v in kept}
    assert set(pre_degree.values())<={q-1,q}
    forbidden={0,1,x,m,m_inverse}
    edges=[]
    for a in range(q):
        if a in forbidden:
            continue
        for b in range(q):
            t=field.mul(field.add(a,field.inv(a)),b)
            p=stage["point_lookup"][(q,a,t)]
            line=n+stage["line_lookup"][(a,b,t)]
            assert p in kept and line in kept
            assert line in stage["adj"][p]
            edges.append((p,line))
    assert len(edges)==q*(q-5)
    endpoints=[v for edge in edges for v in edge]
    assert len(set(endpoints))==len(endpoints)
    exactly_degree_q={v for v in kept if pre_degree[v]==q}
    assert exactly_degree_q==set(endpoints)
    assert all(pre_degree[v]==q-1 for v in kept-set(endpoints))
    return dict(q=q,stage=stage,parameters=cfg,kept=kept,
        deleted=deleted,R=R,closed_root_set=closed_roots,
        closed_R=closed_R,matching_original_flags=tuple(edges),
        degree_before_matching=pre_degree,
        matched_high_degree_vertices=set(endpoints),
        removed_per_original_type=half_removed,
        quasi_perfect_not_perfect=True,
        characteristic_two_b_plus_b_zero=all(
            field.add(b,b)==0 for b in range(q)),
        matching_exactly_repairs_every_high_degree_original_vertex=True,
        matching_is_NOT_optional=True,
        no_synthetic_missing_source_F=True)


@lru_cache(maxsize=4)
def actual_even_source(q=8,x=2,m=3):
    """Genuine final 2021-corrected original q−1 regular incidence."""
    field=Field(q)
    data=corrected_even_S_and_M(field,x,m)
    stage=data["stage"]
    n=stage["n"]
    keepP=tuple(sorted(v for v in data["kept"] if v<n))
    keepL=tuple(sorted(v-n for v in data["kept"] if v>=n))
    count=q*(q*q-q-4)
    assert len(keepP)==len(keepL)==count
    local={v:i for i,v in enumerate(keepP)}
    matched={(p,l-n) for p,l in data["matching_original_flags"]}
    final=[]
    for ell in keepL:
        line=(set(stage["source"]["lines"][ell])&set(keepP))
        line={p for p in line if (p,ell) not in matched}
        assert len(line)==q-1
        final.append({local[p] for p in line})
    src=source_graph(final,count,q-2,q-2)
    r=q-2
    delta=4*r*r+3*r-5
    assert src["excess_lines"]==src["excess_points"]==delta
    assert delta<=5*r*r
    assert len(src["flags"])==q*(q-1)*(q*q-q-4)
    assert len(src["projected"])==count*(q-1)*r*r
    assert all(z==3*r*r for z in src["projection_load"].values())
    # Independent source-first reverse-embedding into the ACTUAL
    # original G_q^x, not the completed parent projection.
    assert all({keepP[p] for p in line}
        ==((set(stage["source"]["lines"][keepL[i]])&set(keepP))
           -{p for p,ell in matched if ell==keepL[i]})
               for i,line in enumerate(src["lines"]))
    return dict(q=q,field=field,original_source=src,
        true_quasi_domination=data,keep_original_stage_points=keepP,
        keep_original_stage_lines=keepL,
        original_matching_flags_deleted=tuple(sorted(matched)),
        true_original_induced_then_matching=True,
        corrected_2021_even_source=True)


def even_matching_spectral_envelope(q):
    """Uniform exact source theorem for EVERY published even q>=8.

    Parent true GQ(q,q) singular squares: (q+1)^2,2q,0.
    Final C=parent row/column submatrix K - E (matching), ||E||=1.
    Sigma2(C)<=sqrt(2q)+1, and with r=q-2>=6:
      2q=2r+4 <= (8/3)r,
      1<=sqrt(r/6),
      sqrt(2q)+1 <= (4/sqrt6 +1/sqrt6)*sqrt(r)
                   =5 sqrt(r/6).
    x in centered spectrum(C C^T) <=25r/6.
    Original corrected G6-D1 centered cubic x(x-2r)^2:
      max_[0,25r/6] =max(32r^3/27,4225r^3/216)
                    =4225r^3/216 <20r^3.
    """
    if type(q) is not int or q<8 or q&(q-1):
        raise ValueError("even prime-power q=2^e>=8 required")
    r=q-2
    assert r>=6 and 2*q*3<=8*r
    # leading q-1 regular singular mode is isolated:
    # q-1>sqrt(2q)+1  iff (q-2)^2>2q
    assert r*r>2*q
    x_bound=Q(25*r,6)
    stationary=Q(32*r**3,27)
    endpoint=x_bound*(x_bound-2*r)**2
    worst=max(stationary,endpoint)
    assert endpoint==Q(4225*r**3,216)
    assert worst<20*r**3
    delta=4*r*r+3*r-5
    assert delta<=5*r*r
    return dict(q=q,r=r,original_regular_degree=q-1,
        final_points_per_side=q*(q*q-q-4),
        original_flags=q*(q-1)*(q*q-q-4),
        original_quadratic_Moore_excess=delta,
        fixed_quadratic_C=5,
        original_parent_GQ_second_singular_squared=2*q,
        matching_perturbation_operator_norm=1,
        second_singular_bound="sqrt(2q)+1",
        exact_centered_T_upper=str(x_bound),
        cubic_internal_critical=str(stationary),
        cubic_interval_endpoint=str(endpoint),
        exact_F0_squared_cubic_upper=str(worst),
        uniform_kappa=20,
        uniform_r_cubed_envelope=20*r**3,
        strict_connectivity_from_first_singular_gap=True,
        corrected_even_2021_theorem_6_required=True,
        actual_all_orders_exist_only_for_supported_prime_powers=True,
        source_distinct_from_odd_G6E2=True,
        no_independent_F0_operator_or_sixth_moment_gate=True)


def literal_source_case(q,x,m,scheme="lex"):
    ins=actual_even_source(q,x,m)
    src=ins["original_source"]
    r=q-2
    maps=typed_maps(src,scheme)
    dp,dl,_=defect_matrices(src)
    exact_second_walk_identity(src["neighbors_point"],dp,r,r)
    exact_second_walk_identity(src["neighbors_line"],dl,r,r)
    pc=typed_conflicts_and_gram(
        src,maps["f"],src["neighbors_point"],dp,r,r)
    lc=typed_conflicts_and_gram(
        src,maps["g"],src["neighbors_line"],dl,r,r)
    J=direct_original_owner_conflicts(src,maps)["J"]
    assert J==pc["e_col"]+lc["e_col"]
    constants=uniform_direct_spectral_constants(1,5,20)
    assert J<=constants["original_owner_conflict_J0"]*r**4
    assert pc["gram"]**2<=constants["original_pencil_Gram_G0"]**2*r**11
    assert lc["gram"]**2<=constants["original_pencil_Gram_G0"]**2*r**11
    return dict(q=q,x=x,m=m,scheme=scheme,
        actual_original_points=src["points"],
        actual_original_lines=len(src["lines"]),
        actual_original_flags=len(src["flags"]),
        original_source_degree=q-1,r=r,
        actual_original_Moore_excess=src["excess_lines"],
        true_quasi_deleted_vertices=len(ins["true_quasi_domination"]["deleted"]),
        true_quasi_degree_q_count=sum(
            v==q for v in ins["true_quasi_domination"]["degree_before_matching"].values()),
        original_matching_edges_removed=len(ins["original_matching_flags_deleted"]),
        original_source_original_3st_projection_load=3*r*r,
        original_flags_from_corrected_S_plus_M=True,
        original_J=J,original_point_conflicts=pc["e_col"],
        original_line_conflicts=lc["e_col"],
        original_point_Gram=pc["gram"],original_line_Gram=lc["gram"],
        all_order_spectral_envelope=even_matching_spectral_envelope(q),
        no_synthetic_missing_projection=True,
        independent_sixth_moment_not_assumed=True,
        no_unrestricted_T3=True)


def original_six_ID_BBo(q=8,x=2,m=3,scheme="lex",
                       max_walks=100000):
    """One TRUE six-ID BBo on corrected EVEN original source.

    Reconstruct directly from original flag owners, and confirm three
    historical source-first/physical inverse algorithms. No synthetic F.
    """
    from hyp105_aa4_branch_a_integrated_referee import (
        actual_edges,historical_bbo,
    )
    from gio_t3c2_partial_books import inverse_certificate
    ins=actual_even_source(q,x,m)
    src=ins["original_source"]
    maps=typed_maps(src,scheme)
    projection={(p,l):(anchors[1][0],anchors[1][1])
                for (p,l),anchors in src["projected"].items()}
    model=dict(src,**maps,projection=projection,
        flag_to_id={flag:i for i,flag in enumerate(src["flags"])})
    FULL=frozenset(range(len(src["flags"])))
    physical,owner=actual_edges(model,FULL)
    result=None
    examined=0
    for v0 in sorted(physical):
        if result is not None:break
        for v1 in sorted(physical[v0]):
            if result is not None:break
            for v2 in sorted(physical[v1]):
                if result is not None:break
                for v3 in sorted(physical[v2]):
                    examined+=1
                    if examined>max_walks:
                        raise AssertionError("bounded true source BBo physical search exhausted")
                    vs=(v0,v1,v2,v3)
                    X={z[0] for z in vs};Y={z[1] for z in vs}
                    if len(X)!=4 or len(Y)!=4:
                        continue
                    p=model["point_by_pair"].get(tuple(sorted((v0[0],v3[0]))))
                    line=model["line_by_pair"].get(tuple(sorted((v0[1],v3[1]))))
                    if p is None or line is None or (p,line) not in projection:
                        continue
                    foot,join=projection[p,line]
                    if set(model["f"][foot])&X or set(model["g"][join])&Y:
                        continue
                    anchors=tuple(model["flag_to_id"][z] for z in
                                  ((p,join),(foot,join),(foot,line)))
                    residual=tuple(owner[tuple(sorted((u,v)))]
                                   for u,v in zip(vs,vs[1:]))
                    if len(set(anchors+residual))!=6:
                        continue
                    six=tuple(sorted(anchors+residual))
                    if not historical_bbo(model,six):
                        continue
                    result=(anchors,residual,six,vs)
                    break
    if result is None:
        raise AssertionError("no true corrected even-source six-ID witness")
    anchors,residual,six,vs=result
    a=frozenset(six)
    c=frozenset(residual)
    inv=inverse_certificate(model,a,c)
    assert inv["original_source_motifs"]>=1
    assert inv["manual_physical_first_equals_published"]
    assert inv["manual_physical_first_equals_source_owner_join"]
    assert inv["exact_original_six_ID_nontrivial_inverse"]
    assert inv["missing_projections_not_completed"]
    after=inverse_certificate(model,a-{anchors[0]},c)
    assert after["original_source_motifs"]==0
    return dict(q=q,x=x,m=m,scheme=scheme,
        true_original_flags=len(src["flags"]),
        required_original_matching_edges_removed=len(
            ins["original_matching_flags_deleted"]),
        actual_original_physical_threewalks_examined=examined,
        original_FULL_3flag_projection_anchors=anchors,
        original_CORE_physical_owner_flags=residual,
        six_distinct_original_flag_IDs=six,
        six_original_source_flag_coordinates=[src["flags"][idx] for idx in six],
        original_physical_threewalk_states=vs,
        independent_three_original_six_ID_inverses_agree=True,
        original_BBo_count_at_least_one=inv["original_source_motifs"],
        deleting_one_original_FULL_anchor_falsifies=True,
        finite_original_witness_not_asymptotic_T3=True,
        no_GQ_completion_or_synthetic_F=True)


def all_order_direct_ledger():
    z=integrated_quadratic_direct_ledger(
        b=1,C=5,kappa=20,C0=Q(1),c0=Q(1))
    f=z["fixed_before_source"]
    assert (f["balance_b"],f["quadratic_C"],
            f["centered_operator_kappa"])==(1,5,20)
    assert z["FORMAL_ONLY"]
    assert z["moment_sixth_condition_is_NOT_required"]
    return z


def certificate():
    case=literal_source_case(8,2,3,"lex")
    correlated=literal_source_case(8,2,3,"correlated")
    positive=original_six_ID_BBo(8,2,3,"lex")
    symbolic=[even_matching_spectral_envelope(q) for q in
              (8,16,32,64,128,256,512,1024)]
    assert all(x["uniform_kappa"]==20 for x in symbolic)
    return dict(schema=SCHEMA,parent_G6E2_HEAD=PARENT_G6E2,
        issue=793,corrigendum_publisher_pdf=PAPER,
        corrigendum_date=CORRIGENDUM_DATE,
        cited_published_theorem=CORRECTED_THEOREM,
        claim="CONDITIONAL_G6D2_T3_CORRECTED_EVEN_2021_PDS_MATCHING_K20",
        exact_even_GF8_true_original_source_cases=[case,correlated],
        actual_even_GF8_original_six_ID_positive_BBo=positive,
        published_even_prime_power_all_order_spectral_envelope=symbolic,
        inherited_G6D2_DIRECT_formal_ledger=all_order_direct_ledger(),
        true_even_characteristic_all_order_GQ_source_family=True,
        published_graph_family_PRIOR_ART_not_new=True,
        sharper_even_only_kappa20_vs_odd_kappa48=True,
        no_sixth_moment_or_independent_source_spectrum_hypothesis=True,
        no_unrestricted_abstract_T3_or_new_GF5_ASET_exponent=True,
        no_external_academic_referee_or_Lean=True)


if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--out")
    args=p.parse_args()
    d=certificate()
    blob=json.dumps(d,indent=2,sort_keys=True)+"\n"
    if args.out:
        Path(args.out).write_text(blob,encoding="utf-8")
    else:
        print(blob)
