"""GIO-003 G6-D6: Schatten-2 positive spectral square-tail source transfer.

The ORIGINAL point/line collinearity A is derived from true simple thick
(s,t)-biregular, girth>=8 source flags. No synthetic F, GQ completion,
independent f/g randomness or numerical eigensolver.

The new all-order A1 source gate is the *second* centered positive part:
  E2_ell(A)=sum_{lambda in Spec(A|1_perp)}(lambda-ell*r)_+**2
           <= M*r**(7/2).
Unlike the G6-D5 trace tail, E2 may remain small when the count/trace
of small positive outliers is large. With a pair-injective two-symbol
factor map H, ||H H^T||_F^2=2V+sum_x d_x^2<=2Va;
Schatten Cauchy--Schwarz yields J_original=O(r**4) for ALL fixed f/g.

Rational PSD W>=0 and W>=P(A-ell*rI)P certifies the *SQUARED*
positive tail via Weyl monotonicity: E2<=tr(W^2).
"""
import argparse
import json
from fractions import Fraction as Q
from pathlib import Path

from gio_t3c_intrinsic_defect import (
    defect_matrices, typed_conflicts_and_gram, direct_original_owner_conflicts,
)
from gio_t3d_cubic_missing import sqrt_ceil
from gio_t3d2_centered_sixth import exact_ceil
from gio_t3d4_few_outliers import (
    original_source_case, exact_symmetric_inertia, actual_outlier_count,
)
from gio_t3d5_positive_tail import (
    source_adjacency, centered_cutoff_operator, witness_for_fixture,
    published_Wenger_symbolic_tail,
)

SCHEMA="mathlab.gio003.g6d6.positive-squared-tail.v1"
PARENT_G6D5="39ef3c1643a3be06e068b69730545e8095223229"


def exact_squared_tail_psd(neighbors,W,ell,r,M):
    """Check REAL ORIGINAL source and sufficient rational Loewner witness.

    W>=0, W>=P(A-ell*rI)P imply lambda_i(W)>=lambda_i(D) for
    descending eigenvalues (Weyl monotonicity). Thus
      sum_i max(lambda_i(D),0)^2 <= tr(W^2).
    The integer/rational gate tr(W^2)^2 <= M^2*r^7 is equivalent
    to tr(W^2) <= M*r^(7/2); no floating powers are evaluated.

    This certificate is sufficient, not an assertion that we find an
    optimal W or that the centered spectrum is fully known.
    """
    if any(type(x) is not int for x in (ell,r,M)) or ell<0 or r<2 or M<0:
        raise ValueError("ell,M nonnegative integers and thick r>=2")
    A,k=source_adjacency(neighbors)
    n=len(A)
    if len(W)!=n or any(len(z)!=n for z in W):
        raise ValueError("square original-source PSD witness required")
    try:
        W=[[Q(z) for z in row] for row in W]
    except (TypeError,ValueError,ZeroDivisionError) as e:
        raise ValueError("witness entries must be exact rationals") from e
    if any(W[i][j]!=W[j][i] for i in range(n) for j in range(i+1,n)):
        raise ValueError("symmetric witness required")
    D=centered_cutoff_operator(neighbors,ell*r)
    W_minus_D=[[W[i][j]-D[i][j] for j in range(n)]
               for i in range(n)]
    pos=exact_symmetric_inertia(W)
    difference=exact_symmetric_inertia(W_minus_D)
    if pos["negative"] or difference["negative"]:
        raise ValueError("W>=0 and W>=D must BOTH hold in Loewner order")
    # For symmetric W, tr(W^2)=sum_{i,j}W_ij^2.
    squared_energy=sum((W[i][j]*W[i][j] for i in range(n)
                        for j in range(n)),Q(0))
    if squared_energy*squared_energy>Q(M*M*r**7):
        raise ValueError("witness exceeds fixed positive square-tail budget")
    return dict(vertices=n,source_original_degree=k,source_r=r,
        cutoff=ell*r,positive_squared_tail_fixed_M=M,
        exact_symmetric_W_PSD=pos,exact_symmetric_dominance_PSD=difference,
        witness_trace_W_squared=str(squared_energy),
        witness_energy_num=squared_energy.numerator,
        witness_energy_den=squared_energy.denominator,
        exact_seventh_power_gate=True,
        original_source_centered_projection=True,
        finite_sufficient_not_necessary_PSD_witness=True,
        no_floating_spectral_decomposition=True)


def original_factor_frobenius(src,typed_labels,side):
    """Independent literal two-symbol H H^T Frobenius invariant.

    H_p,x=1 if the actual source point/line p carries symbol x.
    Pair-injectivity implies |f(p) intersect f(q)|<=1 for p!=q.
    Hence sum_{p,q} |f(p) intersect f(q)|^2
          =2V+sum_x d_x^2 <=2V*a.
    """
    n=src["points"] if side=="point" else len(src["lines"])
    if len(typed_labels)!=n or len(set(typed_labels))!=n:
        raise ValueError("globally pair-injective factor labels required")
    fibers={}
    a=max(x for pair in typed_labels for x in pair)+1
    for p,pair in enumerate(typed_labels):
        if len(pair)!=2 or pair[0]==pair[1]:
            raise ValueError("two distinct factor symbols per vertex")
        for x in pair:
            fibers.setdefault(x,set()).add(p)
    if any(len(z)>a-1 for z in fibers.values()):
        raise ValueError("pair-injective row occupancy violated")
    frob2=2*n+sum(len(z)**2 for z in fibers.values())
    # Completely independent direct two-by-two overlap census.
    direct=sum(len(set(typed_labels[i])&set(typed_labels[j]))**2
               for i in range(n) for j in range(n))
    assert frob2==direct
    assert frob2<=2*n*a
    return dict(vertices=n,alphabet=a,factor_incidence_frob_squared=frob2,
        direct_pair_overlap_squared=direct,
        sum_fiber_occupancy_squared=sum(len(z)**2 for z in fibers.values()),
        factor_trace_critical_bound=2*n*a,
        complete_two_symbol_paired_fiber_identity=True)


def source_quadratic_tail_constants(b,C,ell,M):
    """Fixed BEFORE a source family, no unknown R0-dependent parameters."""
    if any(type(z) is not int for z in (b,C,ell,M)) or (
            b<1 or C<0 or ell<0 or M<0):
        raise ValueError("fixed b>=1, C,ell,M>=0 exact integers")
    v0=(b+1)*(b*b+1+C)
    n0=(b+1)*v0
    a0=2*v0+3
    A0=a0*a0
    k0=b*(b+1)
    theta0=b+2
    weighted_square_root=sqrt_ceil(2*v0*a0*M)
    # 1/2*sqrt(2 v0 a0 M) <=sqrt_ceil(2 v0 a0 M).
    j0=k0*a0+ell*v0+weighted_square_root
    J0=2*j0
    G0=2*v0*k0+2*theta0*j0+2*(b+1)*v0*a0
    assert weighted_square_root**2>=2*v0*a0*M
    return dict(balance_b=b,quadratic_excess_C=C,
        centered_cutoff_ell=ell,positive_squared_tail_M=M,
        source_V0=v0,source_N0=n0,alphabet_a0=a0,
        physical_vertices_A0=A0,point_degree_k0=k0,
        theta0=theta0,weighted_tail_root0=weighted_square_root,
        each_collinearity_conflict_j0=j0,
        original_owner_conflict_J0=J0,original_pencil_Gram_G0=G0,
        no_D5_first_positive_tail_gate=True,
        no_D4_outlier_count_gate=True,
        no_global_F0_operator_norm_gate=True,
        no_eigenvector_delocalization_gate=True,
        no_independent_random_factor_map_assumption=True)


def integrated_square_tail_ledger(b=1,C=3,ell=1,M=1,
                                  C0=Q(1),c0=Q(1)):
    """Source-level sufficient transfer, inherited C2/C3 only.

    C0,c0 are symbolic/existential graph C6 constants, with 1 used
    in certificate as FORMAL placeholders, NOT published numeric values.
    """
    if type(C0) is not Q or type(c0) is not Q or C0<1 or not 0<c0<=1:
        raise ValueError("admissible exact external graph C6 constants required")
    a=source_quadratic_tail_constants(b,C,ell,M)
    v0,n0,a0,A0=(a[z] for z in
        ("source_V0","source_N0","alphabet_a0","physical_vertices_A0"))
    J0,G0=a["original_owner_conflict_J0"],a["original_pencil_Gram_G0"]
    rho_cap=Q(1,32)
    K=16*J0+1
    assert Q(7,8)-rho_cap-Q(2*J0,K+1)>Q(1,2)
    R=512*A0*(1+64*J0)
    T=exact_ceil(8*n0*R**3*C0**3)
    w=Q(8,A0*A0)
    q2=16*(K+1)**2
    q3=64*(K+1)**3
    Q0=8*n0+4*J0
    L6=1+exact_ceil(36*n0*T*T)
    L4=q2*q2*sqrt_ceil(n0*L6)+Q0*T
    E0=4*(2*a0*v0+a0*a0)+4*n0+4*v0*C+8*b*J0
    E=q3*sqrt_ceil(E0*L6)
    BK=sqrt_ceil(16*(b+1)*n0*G0*(K+1)*T)
    D=4*sqrt_ceil(BK*T*L4)
    improper=3*T*Q0
    eps=w/8
    rho=min(rho_cap,eps*eps/Q(12*b*b*q3*q3*L6))
    delta=min(c0/Q(R**6),w/4)
    r0=max(2**32,exact_ceil(Q(improper)/eps),
           exact_ceil((Q(E)/eps)**2),
           exact_ceil((Q(D)/eps)**8))
    assert rho>0 and delta>0 and r0>0
    assert improper<=eps*r0 and E*E<=eps*eps*r0 and D**8<=eps**8*r0
    assert 12*b*b*rho*q3*q3*L6<=eps*eps
    return dict(schema=SCHEMA,issue=793,
      claim="CONDITIONAL_T3_QUADRATIC_EXCESS_POSITIVE_SQUARED_TAIL",
      FORMAL_ONLY=True,external_numeric_graph_C6_NOT_verified=True,
      fixed_before_source=dict(balance_b=b,quadratic_C=C,
        centered_cutoff_ell=ell,positive_squared_tail_M=M,
        external_C0=str(C0),external_c0=str(c0)),
      source=a,
      selector=dict(K=K,R=R,T=T,w=str(w),q2=q2,q3=q3,
        one_original_global_owner_and_typed_selector=True),
      moments=dict(Q0=Q0,L6=L6,L4=L4,E0=E0,E=E,
        mixed_book_BK=BK,blocker_D=D,improper=improper,
        original_missing_endpoint_bound="4V_P Delta_L<=4v0*C*r^5",
        new_positive_square_tail_gate="on BOTH original collinearity types: sum (lambda-ell*r)_+^2 <= M*r^(7/2)",
        exact_PSD_certificate="W>=0,W>=P(A-ell*rI)P; tr(W^2)^2<=M^2*r^7"),
      closure=dict(eps=str(eps),rho=str(rho),delta=str(delta),
        sufficient_r0=str(r0),all_four_LOW_errors_exact=True),
      prerequisites=dict(parent_G6D5_HEAD=PARENT_G6D5,
        actual_girth8_original_source=True,
        inherited_G6C2_original_FULL_CORE_inverse=True,
        inherited_G6C3_original_HEAVY_LOW_single_selector=True,
        external_ordinary_graph_C6_theorem_required=True),
      no_unrestricted_T3=True,
      no_ASET_exponent_improvement=True,
      no_external_referee_or_Lean=True,
      no_new_graph_family_discovered=True)


def published_Wenger_squared_tail(q,ell=1,M=1,nu_D5=2):
    """All PRIME POWERS q>=3: published Wenger W2(q) spectrum.

    This arithmetic is defined on integer q>=3, but a graph
    existence statement requires q to be a PRIME POWER separately.
    No fake finite q^3 source constructed for q>5 here.
    """
    if any(type(z) is not int for z in (q,ell,M,nu_D5)) or (
            q<3 or ell<0 or M<0 or nu_D5<0):
        raise ValueError("q>=3 and ell,M,nu_D5>=0 integers required")
    r=q-1
    assert (q*r*r)%2==0
    m2=q*r*r//2
    gap=max(0,q-ell*r)
    square=m2*gap*gap
    first=m2*gap
    return dict(q=q,r=r,ell=ell,M=M,nu_D5=nu_D5,
        published_W2_requires_prime_power_q=True,
        symbolic_only_NOT_original_matrix_instantiation=True,
        original_collinearity_positive_level=q,
        positive_level_multiplicity=m2,
        positive_gap=gap,positive_tail_first=first,
        positive_tail_squared=square,
        D5_first_tail_gate=first*first<=nu_D5*nu_D5*r**5,
        D6_squared_tail_gate=square*square<=M*M*r**7,
        exact_symmetric_both_typed_spectrum_prior_art=True)


def actual_source_case(name,scheme="lex",ell=None,M=None):
    """Finite actual incidence with original owner/Gram + rational PSD W."""
    if ell is None:
        ell=1 if name in ("wenger3","wenger5") else 2
    if M is None:
        M=(1 if name in ("wenger3","wenger5")
           else 8 if name.startswith("double") else 0)
    src,maps=original_source_case(name,scheme)
    s,t=src["s"],src["t"];r=min(s,t)
    b=exact_ceil(Q(max(s,t),r))
    C=exact_ceil(Q(src["excess_lines"],r*r))
    a=source_quadratic_tail_constants(b,C,ell,M)
    bound={};norms={}
    for side in ("point","line"):
        nbr=src["neighbors_point" if side=="point" else "neighbors_line"]
        W=witness_for_fixture(name,src,side,ell)
        bound[side]=exact_squared_tail_psd(nbr,W,ell,r,M)
        norms[side]=original_factor_frobenius(
            src,maps["f" if side=="point" else "g"],side)
    DP,DL,_=defect_matrices(src)
    point=typed_conflicts_and_gram(
        src,maps["f"],src["neighbors_point"],DP,s,t)
    line=typed_conflicts_and_gram(
        src,maps["g"],src["neighbors_line"],DL,t,s)
    J=direct_original_owner_conflicts(src,maps)["J"]
    assert J==point["e_col"]+line["e_col"]
    j0,G0=a["each_collinearity_conflict_j0"],a["original_pencil_Gram_G0"]
    assert all(z["e_col"]<=j0*r**4 and z["gram"]**2<=G0**2*r**11
               for z in (point,line))
    assert J<=a["original_owner_conflict_J0"]*r**4
    return dict(kind=name,scheme=scheme,source_s=s,source_t=t,r=r,
      actual_source_points=src["points"],
      actual_source_lines=len(src["lines"]),
      actual_original_flags=len(src["flags"]),
      actual_Moore_excess_L=src["excess_lines"],
      actual_Moore_excess_P=src["excess_points"],
      exact_positive_square_tail_PSD_certificates=bound,
      independently_checked_original_factor_Frobenius=norms,
      original_source_point_conflicts=point["e_col"],
      original_source_line_conflicts=line["e_col"],
      original_source_J=J,point_original_Gram=point["gram"],
      line_original_Gram=line["gram"],fixed_FAMILY_values_NOT_proved_by_fixture=True,
      finite_fixture_params_selected_AFTER_source=True,
      original_source_not_synthetic_F=True,no_GQ_completion=True,
      source_constants=a)


def certificate():
    cases=[actual_source_case(*a) for a in (
       ("wenger3","lex"),("wenger3","correlated"),
       ("wenger5","lex"),("wenger5","correlated"),
       ("W32","lex"),("Qminus24","lex"),("dualQminus42","lex"),
       ("doubleW32","lex"),("doubleQminus24","lex"),
       ("doubleDualQminus42","lex"))]
    symbolic=[published_Wenger_squared_tail(q) for q in (
        3,4,5,7,8,11,13,16,17,19,23,31,32,64,101)]
    assert all(z["D6_squared_tail_gate"] for z in symbolic)
    assert all(not z["D5_first_tail_gate"] for z in symbolic
               if z["q"]>=16)
    ledgers=[integrated_square_tail_ledger(*p) for p in (
        (1,3,1,1),(1,3,2,0),(2,12,2,8))]
    return dict(schema=SCHEMA,issue=793,parent_G6D5_HEAD=PARENT_G6D5,
      claim="CONDITIONAL_T3_QUADRATIC_EXCESS_POSITIVE_SQUARED_TAIL",
      actual_original_source_independent_finite_checks=cases,
      published_prime_power_Wenger_asymptotic_symbolic_certificate=symbolic,
      exact_all_order_four_error_formal_ledgers=ledgers,
      truly_infinite_Wenger_fixed_cutoff_separation_from_D5_nu2=True,
      same_Wenger_family_already_in_D2_by_different_gate=True,
      no_new_infinite_graph_family_or_unrestricted_T3=True,
      no_external_referee_or_Lean=True,
      standard_Schatten_Holder_and_Wenger_spectra_prior_art=True)


if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--out")
    a=p.parse_args()
    cert=certificate()
    txt=json.dumps(cert,sort_keys=True,indent=2)+"\n"
    if a.out:
        Path(a.out).write_text(txt,encoding="utf-8")
    else:
        print(txt)
