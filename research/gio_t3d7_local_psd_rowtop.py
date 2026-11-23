"""GIO-003 G6-D7: factor-sparse local PSD row-top source transfer.

For an ACTUAL original, simple thick (s,t)-biregular girth>=8 source,
let A be the ORIGINAL point (or line) collinearity adjacency.
For its minimal pair-label alphabet a, every permissible two-symbol
pair-injective map f has H H^T diagonal 2, offdiagonal 0/1 and at most
2(a-2) nonzeros offdiagonal in each row.

Given W>=0 and W>=P(A-ell*r*I)P in Loewner order, define
 L_a(W)=2tr W + sum_i TOP_{2(a-2)} {max(W_ij,0):j!=i}.
If L_a(W)<=M*r^4 on BOTH source types, every fixed arbitrary f,g
has J_original=O(r^4), and the inherited G6-C1 Gram=O(r^(11/2)).
NO global eigenvalue, positive-tail or Schatten-moment bound is required.

All finite PSD tests use rational Sylvester inertia. This is a
CONDITIONAL source transfer relying on the established G6-C2/C3
original FULL/CORE/HEAVY/LOW machinery, not unrestricted T3.
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
from gio_t3d4_few_outliers import original_source_case, exact_symmetric_inertia
from gio_t3d5_positive_tail import (
    source_adjacency, centered_cutoff_operator, witness_for_fixture,
)
from gio_t3d6_squared_tail import published_Wenger_squared_tail

SCHEMA="mathlab.gio003.g6d7.local-psd-rowtop.v1"
PARENT_G6D6="e4491693df03c263401f3cd8baa8d81278ec68c4"


def minimal_pair_alphabet(V):
    """Smallest exact a>=2 with binom(a,2)>=V, no floats."""
    if type(V) is not int or V<1:
        raise ValueError("positive integer number of original vertices")
    a=2
    while a*(a-1)//2<V:
        a+=1
    assert a*(a-1)//2>=V and (a-1)*(a-2)//2<V
    return a


def _rational_symmetric(W,n):
    if len(W)!=n or any(len(z)!=n for z in W):
        raise ValueError("exact full original-source matrix dimension required")
    if any(type(z) is bool for row in W for z in row):
        raise ValueError("Boolean entries are not an exact rational witness")
    try:
        M=[[Q(z) for z in row] for row in W]
    except (TypeError,ValueError,ZeroDivisionError) as exc:
        raise ValueError("exact rational entries required") from exc
    if any(M[i][j]!=M[j][i] for i in range(n) for j in range(i+1,n)):
        raise ValueError("symmetric witness required")
    return M


def row_top_local_energy(W,a):
    """Exact factor-independent upper bound for tr(W H H^T).

    Each original factor pair is unique, hence X=H H^T has diagonal 2,
    offdiagonal x_ij in {0,1}, with at most 2(a-2) positive offdiagonal
    entries per row (two symbols; each occurs in at most a-1 pairs).
    No independence, eigenvector incoherence, global Schatten gate,
    or GQ axiom is used.
    """
    if type(a) is not int or a<2:
        raise ValueError("minimal alphabet >=2 required")
    n=len(W)
    W=_rational_symmetric(W,n)
    cap=min(n-1,2*(a-2))
    diag=2*sum((W[i][i] for i in range(n)),Q(0))
    tops=[]
    counts=[]
    for i in range(n):
        positive=sorted((W[i][j] for j in range(n)
                         if i!=j and W[i][j]>0),reverse=True)
        tops.append(sum(positive[:cap],Q(0)))
        counts.append(min(len(positive),cap))
    off=sum(tops,Q(0))
    return dict(original_vertices=n,alphabet=a,
        max_admissible_shared_symbol_neighbors=cap,
        double_diagonal_trace=str(diag),
        positive_top_offdiagonal=str(off),
        exact_rowtop_energy=str(diag+off),
        exact_numerator=(diag+off).numerator,
        exact_denominator=(diag+off).denominator,
        positive_entries_selected_by_row=counts,
        rowtop_is_factor_independent=True,
        no_global_spectral_moment_used=True)


def exact_local_psd_source(neighbors,W,ell,r,M):
    """Certify W>=0, W>=P(A-ell*r I)P, rowtop<=M*r^4.

    A is constructed from literal ORIGINAL source collinearity neighbor
    sets and validated regular/symmetric by source_adjacency.
    Sylvester congruence uses exact fractions (no numeric eigenvalues).
    """
    if any(type(z) is not int for z in (ell,r,M)) or ell<0 or r<2 or M<0:
        raise ValueError("exact integer ell,M>=0 and original r>=2 required")
    A,k=source_adjacency(neighbors)
    n=len(A)
    W=_rational_symmetric(W,n)
    D=centered_cutoff_operator(neighbors,ell*r)
    remain=[[W[i][j]-D[i][j] for j in range(n)] for i in range(n)]
    win=exact_symmetric_inertia(W)
    rin=exact_symmetric_inertia(remain)
    if win["negative"] or rin["negative"]:
        raise ValueError("W PSD and W>=centered source cutoff both required")
    a=minimal_pair_alphabet(n)
    loc=row_top_local_energy(W,a)
    value=Q(loc["exact_rowtop_energy"])
    if value<0 or value>M*r**4:
        raise ValueError("PSD local row-top source budget exceeded")
    return dict(source_original_vertices=n,source_original_degree=k,
        r=r,ell=ell,M=M,minimum_pair_alphabet=a,
        W_PSD_exact_inertia=win,W_dominance_PSD_exact_inertia=rin,
        local=loc,budget_rhs=M*r**4,
        exact_r4_local_budget=True,
        source_not_synthetic_missing_F=True,
        no_D2_centered_F0_norm_gate=True,
        no_D4_outlier_count_gate=True,
        no_D5_positive_trace_tail_gate=True,
        no_D6_positive_schatten2_gate=True,
        no_eigenvector_delocalization=True)


def diagonal_wenger_witness(neighbors,q):
    """Source-first qI candidate for original Wenger point/line types.

    Only degree/size is prechecked. The actual Loewner domination is
    independently tested by exact_local_psd_source on ORIGINAL edges.
    All-order validity is derived separately from published W2(q)
    centered collinearity spectrum {-q,0,q}, not from this heuristic.
    """
    A,k=source_adjacency(neighbors)
    n=len(A)
    if type(q) is not int or q<3 or n!=q**3 or k!=q*(q-1):
        raise ValueError("actual source must match Wenger q^3 and q(q-1)")
    return [[Q(q if i==j else 0) for j in range(n)]
            for i in range(n)]


def source_local_constants(b,C,ell,M):
    """Uniform fixed-before-source A1/Gram constant envelope."""
    if any(type(x) is not int for x in (b,C,ell,M)) or (
        b<1 or C<0 or ell<0 or M<0):
        raise ValueError("fixed integer b>=1,C,ell,M>=0 required")
    v0=(b+1)*(b*b+1+C)
    n0=(b+1)*v0
    a0=2*v0+3
    A0=a0*a0
    k0=b*(b+1)
    theta0=b+2
    # 2e_col<=2k(a-1)+2ell*r*V+L_a(W); L<=M*r^4.
    j0=k0*a0+ell*v0+(M+1)//2
    J0=2*j0
    G0=2*v0*k0+2*theta0*j0+2*(b+1)*v0*a0
    return dict(balance_b=b,quadratic_excess_C=C,
        cutoff_ell=ell,local_PSD_M=M,
        source_V0=v0,source_N0=n0,alphabet_a0=a0,
        physical_vertices_A0=A0,point_degree_k0=k0,
        theta0=theta0,half_local_budget_ceiling=(M+1)//2,
        each_collinearity_conflict_j0=j0,
        original_owner_conflict_J0=J0,
        original_pencil_Gram_G0=G0,
        source_conditional_on_BOTH_original_types=True,
        source_alphabet_independent_of_labels=True,
        no_global_Schatten_or_trace_gate=True,
        no_GQ_or_source_synthetic_projection=True)


def integrated_local_ledger(b=1,C=3,ell=0,M=11,
                            C0=Q(1),c0=Q(1)):
    """Use accepted G6-C2/C3 original HEAVY/LOW with new A1 certificate.

    C0=c0=1 are FORMAL numerical placeholders, not published constants.
    """
    if type(C0) is not Q or type(c0) is not Q or C0<1 or not 0<c0<=1:
        raise ValueError("formal external C6 constants must be rationals")
    a=source_local_constants(b,C,ell,M)
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
        claim="CONDITIONAL_T3_QUADRATIC_EXCESS_LOCAL_PSD_ROW_TOP",
        FORMAL_ONLY=True,external_C6_numeric_constants_unverified=True,
        fixed_before_source=dict(balance_b=b,quadratic_C=C,
            ell=ell,local_M=M,external_C0=str(C0),external_c0=str(c0)),
        source=a,
        selector=dict(K=K,R=R,T=T,w=str(w),q2=q2,q3=q3,
            same_global_original_owner_and_typed_bits=True),
        moments=dict(Q0=Q0,L6=L6,L4=L4,E0=E0,E=E,
            BK=BK,D=D,improper=improper,
            original_missing_endpoint_bound="4V_P Delta_L<=4v0*C*r^5",
            local_source_gate="on BOTH original source types exists W>=0, W>=P(A-ell*rI)P, L_a(W)<=M*r^4",
            no_global_spectral_moment_or_rank_assumption=True),
        closure=dict(eps=str(eps),rho=str(rho),delta=str(delta),
            sufficient_r0=str(r0),all_four_LOW_errors_exact=True),
        prerequisites=dict(parent_G6D6_HEAD=PARENT_G6D6,
            actual_original_girth8_incidence=True,
            inherited_G6C2_FULL_CORE_original_inverse=True,
            inherited_G6C3_HEAVY_LOW_original_selector=True,
            external_ordinary_graph_C6_theorem_required=True),
        no_unrestricted_T3=True,no_new_ASET_exponent=True,
        no_external_referee_or_Lean=True,
        no_novel_graph_family_discovered=True)


def published_Wenger_local_diagonal(q,ell=0,M=11):
    """True published prime-power Wenger qI diagonal certificate.

    Original point/line centered adjacency levels -q,0,q.
    For ell=0, qI >= centered A by this known spectrum.
    L_a(qI)=2qn=2q^4 because every offdiagonal is zero.
    Fixed M=11 works for EVERY q>=3 (q/r <=3/2).

    Arithmetic accepts integer q but existence requires PRIME POWER.
    Does NOT instantiate q^3 matrices for large q.
    """
    if any(type(x) is not int for x in (q,ell,M)) or q<3 or ell!=0 or M<0:
        raise ValueError("prime-power Wenger symbolic ell=0, q>=3")
    r=q-1
    energy=2*q**4
    d6=published_Wenger_squared_tail(q,ell=0,M=M,nu_D5=M)
    return dict(q=q,r=r,cutoff_ell=ell,fixed_local_M=M,
        existing_Wenger_source_prime_power_required=True,
        symbolic_published_spectrum_not_large_graph_instantiation=True,
        actual_original_Wenger_n=q**3,
        actual_original_Moore_excess=2*q*r,
        diagonal_W_is_qI_and_PSD_majorant=True,
        exact_diagonal_local_rowtop=energy,
        local_rowtop_gate=energy<=M*r**4,
        fixed_source_quadratic_excess_C3=(2*q*r<=3*r*r),
        D6_squared_tail_same_ell_M=d6["D6_squared_tail_gate"],
        D5_first_tail_same_ell_M=d6["D5_first_tail_gate"],
        d6_positive_squared_excess=d6["positive_tail_squared"],
        D4_count_and_D2_NOT_claimed_to_fail=True)


def actual_case(name,scheme="lex",mode=None):
    """Genuine original source and dual: exact rational Loewner and J/Gram."""
    if mode is None:
        mode="diagonal" if name.startswith("wenger") else "legacy"
    src,maps=original_source_case(name,scheme)
    s,t=src["s"],src["t"]
    r=min(s,t)
    b=exact_ceil(Q(max(s,t),r))
    C=exact_ceil(Q(src["excess_lines"],r*r))
    ell=0 if mode=="diagonal" else (1 if mode=="projector" else 2)
    M=11 if mode=="diagonal" else (50 if mode=="projector"
                                  else 20 if name.startswith("double") else 0)
    const=source_local_constants(b,C,ell,M)
    cert={};sources={}
    for side in ("point","line"):
        nbr=src["neighbors_point" if side=="point" else "neighbors_line"]
        if mode=="diagonal":
            W=diagonal_wenger_witness(nbr,s+1)
        elif mode=="projector":
            W=witness_for_fixture(name,src,side,ell)
        else:
            W=witness_for_fixture(name,src,side,ell)
        cert[side]=exact_local_psd_source(nbr,W,ell,r,M)
        sources[side]=W
    DP,DL,_=defect_matrices(src)
    p=typed_conflicts_and_gram(src,maps["f"],src["neighbors_point"],DP,s,t)
    l=typed_conflicts_and_gram(src,maps["g"],src["neighbors_line"],DL,t,s)
    J=direct_original_owner_conflicts(src,maps)["J"]
    assert J==p["e_col"]+l["e_col"]
    j0,G0=const["each_collinearity_conflict_j0"],const["original_pencil_Gram_G0"]
    assert all(y["e_col"]<=j0*r**4 and y["gram"]**2<=G0**2*r**11
               for y in (p,l))
    assert J<=const["original_owner_conflict_J0"]*r**4
    return dict(name=name,scheme=scheme,witness_mode=mode,
        original_points=src["points"],original_lines=len(src["lines"]),
        original_flags=len(src["flags"]),
        s=s,t=t,r=r,delta_line=src["excess_lines"],
        delta_point=src["excess_points"],
        exact_source_two_sided_certificates=cert,
        original_J=J,original_point_conflicts=p["e_col"],
        original_line_conflicts=l["e_col"],
        point_Gram=p["gram"],line_Gram=l["gram"],
        finite_fixture_M_selected_only_after_source=True,
        actual_original_source_no_synthetic_F=True,
        original_GQ_axiom_not_used=True,
        source_constants=const)


def certificate():
    fixtures=[actual_case(*a) for a in (
        ("wenger3","lex","diagonal"),("wenger3","correlated","diagonal"),
        ("wenger5","lex","diagonal"),("wenger5","correlated","diagonal"),
        ("wenger3","lex","projector"),("wenger5","lex","projector"),
        ("W32","lex","legacy"),("Qminus24","lex","legacy"),
        ("dualQminus42","lex","legacy"),
        ("doubleW32","lex","legacy"),
        ("doubleQminus24","lex","legacy"),
        ("doubleDualQminus42","lex","legacy"),
    )]
    symbolic=[published_Wenger_local_diagonal(q) for q in
        (3,4,5,7,8,11,13,16,17,19,23,31,32,64,101)]
    assert all(z["local_rowtop_gate"] and z["fixed_source_quadratic_excess_C3"]
               for z in symbolic)
    assert all(not z["D6_squared_tail_same_ell_M"]
               and not z["D5_first_tail_same_ell_M"]
               for z in symbolic if z["r"]>=8)
    ledger=[integrated_local_ledger(*z) for z in
        ((1,3,0,11),(1,3,2,0),(2,12,2,20))]
    return dict(schema=SCHEMA,issue=793,parent_G6D6_HEAD=PARENT_G6D6,
        claim="CONDITIONAL_T3_QUADRATIC_EXCESS_LOCAL_PSD_ROW_TOP",
        actual_source_exact_loewner_and_local_certificate=fixtures,
        published_prime_power_Wenger_diagonal_symbolic_family=symbolic,
        all_order_formal_original_HEAVY_LOW_ledgers=ledger,
        fixed_cutoff_infinite_Wenger_separation_from_D5_D6=True,
        existing_Wenger_already_satisfies_optimized_D2=True,
        no_new_unrestricted_T3_or_ASET=True,
        no_new_graph_family_discovered=True,
        standard_PSD_Loewner_and_sparse_row_capacity_prior_art=True,
        external_referee_or_Lean_not_claimed=True)


if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--out")
    args=ap.parse_args()
    data=certificate()
    blob=json.dumps(data,sort_keys=True,indent=2)+"\n"
    if args.out:
        Path(args.out).write_text(blob,encoding="utf-8")
    else:
        print(blob)
