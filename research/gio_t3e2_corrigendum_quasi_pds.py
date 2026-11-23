"""GIO-003/G6-E2: 2021 CORRIGENDUM-safe (q-1)-regular original sources.

2021 correction to Abreu et al. 2015 EJC 22(2) P2.10 explicitly
RETRACTS the false all-order 2q(q-1)^2 family (its purported perfect
dominating set fails for q>=7). The corrected odd-prime-power q>=7
family is q-1 regular, girth 8, of order 2q(q^2-q-4). It removes an
explicit QUASI-perfect dominating S from the ACTUAL q-regular source
G_q^x in G6-E1, and then removes a literal MATCHING M to repair degree.

New Mathlab source theorem: let B denote the ORIGINAL parent GQ(q,q)
incidence. Final source C is an induced row/column submatrix B[U,V]
minus a matching incidence E. Interlacing plus Weyl gives
  sigma_2(C) <= sqrt(2q)+1 <=(9/4)sqrt(r), r=q-2>=5.
Corrected G6-D1 ORIGINAL cubic then bounds
  ||F0||^2 <= (194481/4096)r^3 <48r^3
on BOTH types, with no unproved independent spectral assumption.

All-order published existence: odd prime powers q>=7, x,y satisfying
the corrigendum conditions; only REAL literal finite fields q=5,7
are built as finite falsifiers here. 2015 family is NEVER asserted.
"""
import argparse
import json
from collections import Counter
from fractions import Fraction as Q
from itertools import product
from pathlib import Path

from gio_t3d3_affine_arc import Field
from gio_t3e1_subgq_pds import actual_smaller_source
from gio_t3c_intrinsic_defect import (
    source_graph,typed_maps,defect_matrices,
    exact_second_walk_identity,typed_conflicts_and_gram,
    direct_original_owner_conflicts,
)
from gio_t3d2_centered_sixth import (
    integrated_quadratic_direct_ledger,
    uniform_direct_spectral_constants,
)

SCHEMA="mathlab.gio003.g6e2.corrigendum-2021-quasipds.v1"
PARENT_G6E1="d82b8d784710e47e37ca30d912ee097f9dfbea57"
PAPER="https://www.combinatorics.org/ojs/index.php/eljc/article/download/v22i2p10/pdf/"
CORRIGENDUM_DATE="2021-05-18"


def eligible_odd_parameters(field,x,y):
    """Enforce ACTUAL corrected Theorem 5, not original false claim."""
    q=field.q
    if type(x) is not int or type(y) is not int or not (0<=x<q and 0<=y<q):
        raise ValueError("two exact field-coordinate labels required")
    if q<5 or q%2==0:
        raise ValueError("corrected Theorem 5 only odd prime powers q>=5")
    one=1;minusone=field.sub(0,one)
    if len({0,one,minusone,x,y})!=5:
        raise ValueError("2021 corrigendum distinct 0,+1,-1,x,y required")
    if q>5 and q%4==1:
        if field.add(field.mul(x,x),one)!=0:
            raise ValueError("q=1 mod4 corrigendum requires x^2+1=0")
        if y!=field.inv(x):
            raise ValueError("q=1 mod4 corrigendum requires y=x^(-1)")
    return dict(q=q,x=x,y=y,odd_prime_power_REQUIRED=True,
        correct_2021_nonzero_pair_conditions=True,
        q1mod4_quadratic_and_inverse_constraints_checked=(q>5 and q%4==1),
        q5_special_allowance=(q==5),
        false_2015_perfect_dominating_theorem_RETRACTED=True)


def stage_one_adjacency(instance):
    """Actual original G_q^x adjacency with ORIGINAL parent coordinate labels."""
    src=instance["new_original_source"]
    n=src["points"]
    names=instance["parent_names"]
    pts=instance["kept_parent_points"]
    lns=instance["kept_parent_lines"]
    point_lookup={names[original]:p for p,original in enumerate(pts)}
    line_lookup={names[original]:l for l,original in enumerate(lns)}
    adj=[set() for _ in range(2*n)]
    for ell,line in enumerate(src["lines"]):
        for p in line:
            adj[p].add(n+ell)
            adj[n+ell].add(p)
    assert all(len(z)==instance["q"] for z in adj)
    return dict(source=src,n=n,adj=adj,
        point_lookup=point_lookup,line_lookup=line_lookup,
        point_names=tuple(names[i] for i in pts),
        line_names=tuple(names[i] for i in lns))


def _closed_neighbors(adjacency,indices):
    out=set(indices)
    for i in indices:
        out.update(adjacency[i])
    return out


def corrected_S_and_M(field,x,y):
    """Literal 2021 corrigendum Theorem 5 source deletions and matching.

    All names are in G_q^x ORIGINAL point/line coordinates, NOT GQ
    completed point->line projections or synthetic F entries.
    """
    gate=eligible_odd_parameters(field,x,y)
    q=field.q
    stage=stage_one_adjacency(actual_smaller_source(field,xi=x))
    n=stage["n"]
    # 2021 S = union_j N_G[(infty,y,j)_POINT] union N_G[R_LINES]
    roots_P=[stage["point_lookup"][(q,y,j)] for j in range(q)]
    one=1
    negativeone=field.sub(0,one)
    R=set()
    for b in range(q):
        twice=field.add(b,b)
        for a,t in ((one,field.sub(0,twice)),
                    (negativeone,twice)):
            R.add(n+stage["line_lookup"][(a,b,t)])
    assert len(R)==2*q
    deletion=_closed_neighbors(stage["adj"],roots_P)|_closed_neighbors(stage["adj"],R)
    expected=2*q*q+4*q
    if len(deletion)!=expected:
        raise AssertionError(("2021 quasi-dominating deletion cardinality",q,
                              len(deletion),expected))
    kept=set(range(2*n))-deletion
    each_removed=q*q+2*q
    assert sum(i<n for i in deletion)==each_removed
    assert sum(i>=n for i in deletion)==each_removed
    deg_before={v:len(stage["adj"][v]&kept) for v in kept}
    if not set(deg_before.values())<={q-1,q}:
        raise AssertionError(("quasi-perfect bad degrees",q,Counter(deg_before.values())))
    # 2021 matching M: a not in {0,1,-1,x,y}; b over Fq;
    # t=-b(a+a^{-1}), edges ((a,b,t)_LINE, (infty,a,t)_POINT).
    forbidden={0,one,negativeone,x,y}
    matching=[]
    for a in range(q):
        if a in forbidden:
            continue
        multiplier=field.add(a,field.inv(a))
        for b in range(q):
            t=field.sub(0,field.mul(b,multiplier))
            p=stage["point_lookup"][(q,a,t)]
            ell=n+stage["line_lookup"][(a,b,t)]
            if p not in kept or ell not in kept or ell not in stage["adj"][p]:
                raise AssertionError(("not actual residual original matching edge",q,a,b))
            matching.append((p,ell))
    used=[z for pair in matching for z in pair]
    if len(used)!=len(set(used)):
        raise AssertionError("2021 M is not a matching")
    exactly_deg_q={v for v in kept if deg_before[v]==q}
    if exactly_deg_q!=set(used):
        raise AssertionError(("2021 matching does not cover EXACT degree-q survivors",
                              q,len(exactly_deg_q),len(used)))
    assert len(matching)==q*(q-5)
    assert len(kept)==2*q*(q*q-q-4)
    assert all(deg_before[v]==q-1 for v in kept-set(used))
    return dict(stage=stage,kept=kept,deleted=deletion,
        matched_original_edges=tuple(matching),
        deg_before=deg_before,matching_vertices=set(used),
        params=gate,
        exactly_degree_q_survivors_matched=True,
        published_S_QUASI_not_perfect=True,
        S_removed_each=each_removed,
        matching_count=len(matching),
        M_empty_only_in_q5=(q==5),
        corrected_2021_matching_applied_not_falsely_ignored=True)


def actual_corrigendum_source(field,x,y):
    """Source-first q−1-regular original incidence from S+M correction."""
    q=field.q
    z=corrected_S_and_M(field,x,y)
    stage=z["stage"]
    n=stage["n"]
    point_indices=sorted(v for v in z["kept"] if v<n)
    line_indices=sorted(v-n for v in z["kept"] if v>=n)
    expect=q*(q*q-q-4)
    assert len(point_indices)==len(line_indices)==expect
    point_index={p:i for i,p in enumerate(point_indices)}
    to_remove={(p,ell-n) for p,ell in z["matched_original_edges"]}
    reduced=[]
    for ell in line_indices:
        original=stage["source"]["lines"][ell]
        in_reduced=set(original)&set(point_indices)
        in_reduced={p for p in in_reduced if (p,ell) not in to_remove}
        assert len(in_reduced)==q-1
        reduced.append({point_index[p] for p in in_reduced})
    src=source_graph(reduced,expect,q-2,q-2)
    r=q-2
    # CorRECTED (2021) Moore count, NOT false 2015 q(q−1)².
    delta=4*r*r+3*r-5
    assert delta==4*q*q-13*q+5
    assert src["excess_lines"]==src["excess_points"]==delta
    assert delta<=5*r*r
    assert len(src["flags"])==q*(q-1)*(q*q-q-4)
    assert len(src["projected"])==expect*(q-1)*r*r
    assert all(v==3*r*r for v in src["projection_load"].values())
    # Independent reconstruct every final original flag from G_q^x
    # actual source adjacency and M, never a GQ projection completion.
    assert all({point_indices[p] for p in line}
        ==((set(stage["source"]["lines"][line_indices[i]])&
            set(point_indices))-
           {pp for pp,e in to_remove if e==line_indices[i]})
               for i,line in enumerate(src["lines"]))
    return dict(q=q,field=field,intermediate=z,
        new_source=src,
        original_stage_point_indices=tuple(point_indices),
        original_stage_line_indices=tuple(line_indices),
        original_M_edges=tuple(sorted(to_remove)),
        actual_original_incidence_after_S_and_matching=True)


def spectral_compression_with_matching(q):
    """Exact global spectral envelope for ALL corrected odd q>=7.

    Γ_q singular levels σ1=q+1, σ2=sqrt(2q); final source = induced
    original submatrix minus partial permutation matching E, ||E||=1.
    Weyl: σ2(final) <=sqrt(2q)+1. For r=q-2>=5:
      2q <=49r/16,  1<=sqrt(r)/2
      sqrt(2q)+1 <=(9/4)sqrt(r)
      x_centered<=81r/16.
    Then original corrected G6-D1 p(x)=x(x-2r)^2 yields
      ||F0||² <=max(32r³/27,194481r³/4096) <48r³.
    """
    if type(q) is not int or q<7 or q%2==0:
        raise ValueError("corrected odd q>=7 symbolic source only")
    r=q-2
    assert 2*q*16 <=49*r
    assert r>=4
    max_x=Q(81*r,16)
    critical=Q(32*r**3,27)
    endpoint=max_x*(max_x-2*r)**2
    worst=max(critical,endpoint)
    assert endpoint==Q(194481*r**3,4096)
    assert Q(194481,4096)<48
    assert worst<48*r**3
    # The genuine first singular value (q-1) exceeds σ2 bound:
    # (q−1)>sqrt(2q)+1  iff (q−2)^2>2q.
    assert (q-2)**2>2*q
    return dict(q=q,r=r,original_q_minus_one_degree=q-1,
        parent_GQ_second_sigma_squared=2*q,
        MATCHING_operator_norm_exactly_one=True,
        original_centered_second_sigma_bound="sqrt(2q)+1",
        exact_nonprincipal_T_eigenvalue_bound=str(max_x),
        exact_centered_G6D1_cubic_upper=str(worst),
        uniform_fixed_kappa=48,
        centered_F0_squared_bound=48*r**3,
        uniform_quadratic_excess_C=5,
        original_Moore_excess=4*r*r+3*r-5,
        connectedness_from_strict_singular_gap=True,
        field_existence_requires_corrected_2021_theorem=True,
        q_odd_prime_power_required=True,
        old_2015_perfect_dominating_order_RETRACTED=True,
        no_synthetic_missing_matrix=True)


def literal_case(q,x,y,scheme="lex",check_full_original_F0=False):
    field=Field(q)
    ins=actual_corrigendum_source(field,x,y)
    src=ins["new_source"]
    labels=typed_maps(src,scheme)
    delta=src["excess_lines"]
    dpoint,dline,_=defect_matrices(src)
    r=q-2
    point=typed_conflicts_and_gram(
        src,labels["f"],src["neighbors_point"],dpoint,r,r)
    line=typed_conflicts_and_gram(
        src,labels["g"],src["neighbors_line"],dline,r,r)
    J=direct_original_owner_conflicts(src,labels)
    assert J["J"]==point["e_col"]+line["e_col"]
    # G6-D2 all-order transfer for q>=7, not for exceptional q5.
    env=spectral_compression_with_matching(q) if q>=7 else None
    if env:
        constants=uniform_direct_spectral_constants(1,5,48)
        assert J["J"]<=constants["original_owner_conflict_J0"]*r**4
        assert point["gram"]**2<=constants["original_pencil_Gram_G0"]**2*r**11
        assert line["gram"]**2<=constants["original_pencil_Gram_G0"]**2*r**11
    source_spectrum={}
    if check_full_original_F0:
        # A larger independent numeric-free original incidence check;
        # q=5 is finite special only, q>=7 can be huge.
        from gio_t3e1_subgq_pds import exact_original_centered_missing_PSD
        for side in ("point","line"):
            source_spectrum[side]=exact_original_centered_missing_PSD(
                src,48,side)
    return dict(q=q,x=x,y=y,scheme=scheme,
        genuine_smaller_source_each_side=src["points"],
        original_degree=q-1,original_r=r,
        original_named_flags=len(src["flags"]),
        original_Moore_excess=delta,
        corrected_2021_quasi_domination_S_size=len(ins["intermediate"]["deleted"]),
        S_removed_per_side=ins["intermediate"]["S_removed_each"],
        residual_pre_M_matching_edges=ins["intermediate"]["matching_count"],
        every_degree_q_residual_matched=ins["intermediate"][
            "exactly_degree_q_survivors_matched"],
        no_false_2015_PDS_claim=ins["intermediate"]["params"][
            "false_2015_perfect_dominating_theorem_RETRACTED"],
        original_source_projected_loads_all_exact=True,
        actual_source_after_S_plus_M=ins[
            "actual_original_incidence_after_S_and_matching"],
        independent_original_point_conflicts=point["e_col"],
        independent_original_line_conflicts=line["e_col"],
        original_total_J=J["J"],
        original_point_Gram=point["gram"],
        original_line_Gram=line["gram"],
        exact_full_original_missing_PSD=source_spectrum,
        uniform_all_order_spectral_gate=env,
        q5_is_finite_exception_NOT_an_infinite_family=(q==5),
        no_unrestricted_T3_or_ASET=True)



def literal_corrected_six_original_ID_witness(q,x,y,scheme="lex",
                                               max_walks=3000000):
    """Find one TRUE corrected-original six-flag BBo via physical 3walk.

    Only six actual ORIGINAL flag owners are submitted to three
    independently implemented historical BBo inverses. The actual
    G_q^x - S - M source is NOT GQ-completed and NOT synthetic.
    A FULL anchor deletion must destroy the targeted witness.
    """
    from hyp105_aa4_branch_a_integrated_referee import (
        actual_edges,historical_bbo,
    )
    from gio_t3c2_partial_books import inverse_certificate
    ins=actual_corrigendum_source(Field(q),x,y)
    src=ins["new_source"]
    typed=typed_maps(src,scheme)
    projection={(p,l):(anchors[1][0],anchors[1][1])
                for (p,l),anchors in src["projected"].items()}
    model=dict(src,**typed,projection=projection,
        flag_to_id={flag:i for i,flag in enumerate(src["flags"])})
    FULL=frozenset(range(len(src["flags"])))
    actual,owner=actual_edges(model,FULL)
    found=None
    examined=0
    for v0 in sorted(actual):
        if found is not None:break
        for v1 in sorted(actual[v0]):
            if found is not None:break
            for v2 in sorted(actual[v1]):
                if found is not None:break
                for v3 in sorted(actual[v2]):
                    examined+=1
                    if examined>max_walks:
                        raise AssertionError("true source BBo missing within bounded physical threewalk search")
                    vs=(v0,v1,v2,v3)
                    xs={v[0] for v in vs}
                    ys={v[1] for v in vs}
                    if len(xs)!=4 or len(ys)!=4:
                        continue
                    p=model["point_by_pair"].get(tuple(sorted((v0[0],v3[0]))))
                    ell=model["line_by_pair"].get(tuple(sorted((v0[1],v3[1]))))
                    if p is None or ell is None or (p,ell) not in projection:
                        continue
                    foot,join=projection[p,ell]
                    if set(model["f"][foot])&xs or set(model["g"][join])&ys:
                        continue
                    anchors=tuple(model["flag_to_id"][flag] for flag in
                        ((p,join),(foot,join),(foot,ell)))
                    residual=tuple(owner[tuple(sorted((a,b)))]
                        for a,b in zip(vs,vs[1:]))
                    if len(set(anchors))!=3 or len(set(residual))!=3:
                        continue
                    if len(set(anchors+residual))!=6:
                        continue
                    six=tuple(sorted(anchors+residual))
                    if not historical_bbo(model,six):
                        continue
                    found=(anchors,residual,six,vs)
                    break
    if found is None:
        raise AssertionError("corrected q-1 source has no found genuine six flag BBo")
    anchors,residual,six,path=found
    A=frozenset(six)
    C=frozenset(residual)
    original=inverse_certificate(model,A,C)
    assert original["original_source_motifs"]>=1
    assert original["manual_physical_first_equals_published"]
    assert original["manual_physical_first_equals_source_owner_join"]
    assert original["exact_original_six_ID_nontrivial_inverse"]
    assert original["missing_projections_not_completed"]
    after=inverse_certificate(model,A-{anchors[0]},C)
    assert after["original_source_motifs"]==0
    return dict(q=q,scheme=scheme,
        true_corrected_original_source_flags=len(src["flags"]),
        original_M_edges_removed=len(ins["original_M_edges"]),
        bounded_actual_physical_threewalks_examined=examined,
        three_original_FULL_projection_anchor_IDs=anchors,
        three_original_CORE_physical_owner_IDs=residual,
        actual_six_distinct_original_flag_IDs=six,
        actual_six_original_flag_coordinates=[
            src["flags"][k] for k in six],
        original_six_ID_physical_path=path,
        independently_confirmed_produced_BBo_count=original[
            "original_source_motifs"],
        all_three_historical_BBo_inverses_exact_agree=True,
        removing_original_FULL_anchor_destroys_witness=True,
        no_fabricated_projection_or_parent_completion=True,
        finite_positive_not_asymptotic_count=True)



def exact_all_order_ledger():
    d=integrated_quadratic_direct_ledger(
        b=1,C=5,kappa=48,C0=Q(1),c0=Q(1))
    f=d["fixed_before_source"]
    assert (f["balance_b"],f["quadratic_C"],
            f["centered_operator_kappa"])==(1,5,48)
    assert d["FORMAL_ONLY"] and d["moment_sixth_condition_is_NOT_required"]
    return d


def certificate():
    finite=[literal_case(5,2,3,"lex",True),
            literal_case(7,2,3,"lex",False),
            literal_case(7,2,3,"correlated",False)]
    symbolic=[spectral_compression_with_matching(q) for q in
              (7,9,11,13,17,19,23,25,27,31,49,81,101,121)]
    d=exact_all_order_ledger()
    return dict(schema=SCHEMA,issue=793,
        parent_G6E1_HEAD=PARENT_G6E1,
        published_2015_paper_and_MAY_2021_corrigendum=PAPER,
        corrigendum_date=CORRIGENDUM_DATE,
        claim="CONDITIONAL_G6D2_T3_CORRECTED_2021_QMINUS1_PDS_PLUS_MATCHING",
        true_original_corrected_quasi_PDS_source_examples=finite,
        fixed_all_odd_prime_power_symbolic_spectral_transfer=symbolic,
        inherited_G6D2_DIRECT_four_low_ledger=d,
        first_original_2015_q_minus1_family_RETRACTED=True,
        corrected_2021_matching_is_required=True,
        corrected_family_exists_for_odd_prime_power_q_ge7=True,
        no_new_worldwide_graph_construction=True,
        new_to_Mathlab_true_source_degree_q_minus_1=True,
        no_independent_F0_assumption_or_sixth_moment=True,
        no_unrestricted_T3_or_new_ASET_exponent=True,
        no_external_human_referee_or_Lean=True)


if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--out")
    args=ap.parse_args()
    d=certificate()
    text=json.dumps(d,sort_keys=True,indent=2)+"\n"
    if args.out:
        Path(args.out).write_text(text,encoding="utf-8")
    else:
        print(text)
