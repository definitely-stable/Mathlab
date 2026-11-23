"""GIO-003/G6-D5: conditional positive spectral-tail transfer.

All source matrices are from ACTUAL original simple (s,t)-biregular
girth>=8 incidence graphs. No synthetic missing projections or GQ
completion. The positive-tail sufficient hypothesis is weaker than
G6-D4's critical outlier-rank gate: it charges ONLY eigenvalue excess
above ell*r, not the count or the full centered missing F0 norm.

The finite verifier accepts rational PSD *majorant witnesses* and
uses exact Sylvester congruence to avoid numerical eigensolvers.
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

SCHEMA="mathlab.gio003.g6d5.positive-tail-psd.v1"
PARENT_G6D4="2fc2761fd5cb25db16150b08f60922e937fb05ff"


def source_adjacency(neighbors):
    """Literal exact symmetric collinearity adjacency; no F construction."""
    n=len(neighbors)
    if n<2 or any(type(z) is not set for z in neighbors):
        raise ValueError("actual original source neighbor sets required")
    k=len(neighbors[0])
    if any(len(v)!=k or i in v or any(j<0 or j>=n for j in v)
           for i,v in enumerate(neighbors)):
        raise ValueError("original regular simple adjacency required")
    if any(i not in neighbors[j] for i in range(n) for j in neighbors[i]):
        raise ValueError("original adjacency must be undirected")
    return [[int(j in neighbors[i]) for j in range(n)] for i in range(n)],k


def centered_cutoff_operator(neighbors,threshold):
    """P(A-threshold I)P=A-threshold I-(k-threshold)J/n exactly."""
    if type(threshold) is not int or threshold<0:
        raise ValueError("nonnegative integer cutoff required")
    A,k=source_adjacency(neighbors)
    n=len(A)
    return [[Q(A[i][j]-(threshold if i==j else 0))
             -Q(k-threshold,n) for j in range(n)] for i in range(n)]


def _zero(n):
    return [[Q(0) for _ in range(n)] for _ in range(n)]


def exact_positive_tail_psd(neighbors,W,ell,r,nu):
    """Certificate: W>=0, W>=P(A-ell*r I)P, Tr W<=nu*r^(5/2).

    Since W is a *rational PSD* majorant, its trace is an upper
    bound for the positive-part spectral trace, by Ky Fan/spectral
    minimax. NO floating square roots: (Tr W)^2<=nu^2*r^5.
    This is a SUFFICIENT computable witness, not an algorithm
    finding the optimal positive part of an arbitrary source.
    """
    if any(type(x) is not int for x in (ell,r,nu)) or ell<0 or r<2 or nu<0:
        raise ValueError("fixed integer ell,nu>=0 and thick r>=2")
    A,k=source_adjacency(neighbors)
    n=len(A)
    if len(W)!=n or any(len(row)!=n for row in W):
        raise ValueError("conforming rational PSD witness required")
    try:
        W=[[Q(x) for x in row] for row in W]
    except (ValueError,TypeError,ZeroDivisionError) as e:
        raise ValueError("exact rational witness required") from e
    if any(W[i][j]!=W[j][i] for i in range(n) for j in range(i+1,n)):
        raise ValueError("PSD witness must be symmetric")
    cutoff=ell*r
    D=centered_cutoff_operator(neighbors,cutoff)
    Z=[[W[i][j]-D[i][j] for j in range(n)] for i in range(n)]
    w_in=exact_symmetric_inertia(W)
    z_in=exact_symmetric_inertia(Z)
    trace=sum(W[i][i] for i in range(n))
    if w_in["negative"] or z_in["negative"] or trace<0:
        raise ValueError("invalid Loewner PSD majorant witness")
    if trace**2>nu**2*r**5:
        raise ValueError("certified positive-tail trace exceeds fixed budget")
    return dict(vertices=n,degree=k,cutoff=cutoff,source_r=r,
        fixed_nu=nu,trace_W=str(trace),
        trace_W_num=trace.numerator,trace_W_den=trace.denominator,
        exact_squared_tail_gate=trace**2<=nu**2*r**5,
        W_PSD_exact_inertia=w_in,dominance_PSD_exact_inertia=z_in,
        verified_source_positive_tail_upper=str(trace),
        centered_principal_mode_not_counted=True,
        exact_rational_no_numeric_eigensolvers=True,
        no_claim_optimal_W_for_arbitrary_source=True)


def wenger_q_eigenspace_witness(neighbors,q,ell):
    """All-entry rational polynomial projector for REAL prime-field W2(q).

    The classical published centered collinearity eigenvalues are
    -q,0,+q, and the principal degree k=q(q-1). The +q centered
    spectral projector is Q= A(A+qI)/(2q²)
                       -k(k+q)/(2q²*n) J.
    This uses the genuine original collinearity graph; the PSD
    witness is independently validated by exact rational inertia.
    """
    A,k=source_adjacency(neighbors)
    n=len(A);r=q-1
    if type(q) is not int or q<3 or n!=q**3 or k!=q*(q-1):
        raise ValueError("this exact witness is only for actual Wenger W2(q)")
    alpha=max(0,q-ell*r)
    if alpha==0:
        return _zero(n)
    out=[]
    for i in range(n):
        row=[]
        for j in range(n):
            a2=len(neighbors[i]&neighbors[j])
            eigproj=(Q(a2+q*A[i][j],2*q*q)
                     -Q(k*(k+q),2*q*q*n))
            row.append(alpha*eigproj)
        out.append(row)
    assert all(out[i][j]==out[j][i] for i in range(n) for j in range(i+1,n))
    assert all(sum(row)==0 for row in out)
    expected=Q(q*(q-1)**2,2)*alpha
    assert sum(out[i][i] for i in range(n))==expected
    return out


def doubled_gq_sign_witness(neighbors,ell,r):
    """Exact rank-one centered PSD witness for two literal GQ components.

    The source is validated separately using original-incidence
    source_graph. Only one extra (block-sign) principal-sized mode
    remains after the trivial one-ones mode is removed; all local GQ
    nonprincipal eigenvalues are <=ell*r in these named fixtures.
    The second Loewner gate independently verifies this for each side.
    """
    A,k=source_adjacency(neighbors)
    n=len(A)
    if n%2:
        raise ValueError("doubled source must have equal-sized components")
    sign=[1 if i<n//2 else -1 for i in range(n)]
    if any(sum(A[i][j]*sign[j] for j in range(n))!=k*sign[i]
           for i in range(n)):
        raise ValueError("not an original double-component sign eigenvector")
    extra=max(0,k-ell*r)
    return [[Q(extra*sign[i]*sign[j],n) for j in range(n)]
            for i in range(n)]


def witness_for_fixture(name,src,side,ell):
    neighbors=src["neighbors_point" if side=="point" else "neighbors_line"]
    r=min(src["s"],src["t"])
    if name in ("wenger3","wenger5"):
        return wenger_q_eigenspace_witness(neighbors,src["s"]+1,ell)
    if name in ("doubleW32","doubleQminus24","doubleDualQminus42"):
        return doubled_gq_sign_witness(neighbors,ell,r)
    if name in ("W32","Qminus24","dualQminus42"):
        return _zero(len(neighbors))
    raise ValueError("this is a bounded finite witness generator, not a source oracle")


def tail_mixing_constants(b,C,ell,nu):
    """Uniform original-source fixed constants from POSITIVE spectral tail."""
    if any(type(v) is not int for v in (b,C,ell,nu)) or (
        b<1 or C<0 or ell<0 or nu<0):
        raise ValueError("fixed integer b>=1,C,ell,nu>=0")
    v0=(b+1)*(b*b+1+C)
    n0=(b+1)*v0
    a0=2*v0+3
    A0=a0*a0
    k0=b*(b+1)
    theta0=b+2
    # All source positive tails: sum (lambda-ell*r)_+ <=nu*r^(5/2)
    # e_col <=k*(a-1)+ell*r*V+(a-1)*tail, with a-1<=a0*r^(3/2).
    j0=k0*a0+ell*v0+a0*nu
    J0=2*j0
    G0=2*v0*k0+2*theta0*j0+2*(b+1)*v0*a0
    return dict(balance_b=b,quadratic_excess_C=C,
        centered_cutoff_ell=ell,positive_excess_tail_nu=nu,
        source_V0=v0,source_N0=n0,alphabet_a0=a0,
        physical_vertices_A0=A0,point_degree_k0=k0,theta0=theta0,
        each_collinearity_conflict_j0=j0,original_owner_conflict_J0=J0,
        original_pencil_Gram_G0=G0,
        no_global_F0_norm_gate=True,
        no_positive_outlier_rank_gate=True,
        no_eigenvector_delocalization_gate=True,
        dual_original_source_required=True)


def integrated_tail_ledger(b=1,C=3,ell=1,nu=2,C0=Q(1),c0=Q(1)):
    """G6-C3/2 historic FULL/CORE transfer with new A1 source bound.

    External ordinary graph C6 numeric parameters are FORMAL_ONLY.
    """
    if type(C0) is not Q or type(c0) is not Q or C0<1 or not 0<c0<=1:
        raise ValueError("external C0>=1,c0 in (0,1] exact rational required")
    a=tail_mixing_constants(b,C,ell,nu)
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
    # Original missing projection endpoints are O(r^5), NOT o(r^5).
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
       claim="CONDITIONAL_QUADRATIC_T3_POSITIVE_SPECTRAL_TAIL",
       FORMAL_ONLY=True,external_numeric_graph_C6_NOT_verified=True,
       fixed_before_source=dict(balance_b=b,quadratic_C=C,
           centered_cutoff_ell=ell,positive_tail_nu=nu,
           external_C0=str(C0),external_c0=str(c0)),
       source=a,
       selector=dict(K=K,R=R,T=T,w=str(w),q2=q2,q3=q3,
           one_global_original_owner_and_bit_selector=True),
       moments=dict(Q0=Q0,L6=L6,L4=L4,E0=E0,E=E,
           mixed_book_BK=BK,blocker_D=D,improper=improper,
           positive_tail_gate="for BOTH collinearity types tau_ell=sum_{lambda on 1_perp} max(lambda-ell*r,0) <= nu*r^(5/2)",
           exact_psd_sufficient_witness="W>=0, W>=P(A-ell*rI)P; (trace W)^2<=nu^2*r^5",
           original_missing_endpoint_bound="4V_P Delta_L<=4v0*C*r^5"),
       closure=dict(eps=str(eps),rho=str(rho),delta=str(delta),
           sufficient_r0=str(r0),all_four_LOW_errors_exact=True),
       prerequisites=dict(parent_G6D4_HEAD=PARENT_G6D4,
           actual_original_source_girth8=True,
           inherited_G6C2_FULL_CORE_original_inverse=True,
           inherited_G6C3_HEAVY_LOW_single_selector=True,
           external_ordinary_C6_theorem_required=True),
       no_unrestricted_T3=True,no_new_infinite_gap_separation_family=True,
       no_new_ASET_exponent=True,
       no_external_referee_or_Lean=True)


def finite_case(name,scheme="lex",ell=1,nu=2):
    """Two real types, exact PSD upper certificates, all original source IDs."""
    src,maps=original_source_case(name,scheme)
    s,t=src["s"],src["t"];r=min(s,t)
    b=exact_ceil(Q(max(s,t),r))
    C=exact_ceil(Q(src["excess_lines"],r*r))
    a=tail_mixing_constants(b,C,ell,nu)
    bound={}
    prev={}
    for side in ("point","line"):
        neighbors=src["neighbors_point" if side=="point" else "neighbors_line"]
        W=witness_for_fixture(name,src,side,ell)
        bound[side]=exact_positive_tail_psd(neighbors,W,ell,r,nu)
        prev[side]=actual_outlier_count(neighbors,ell*r)
    DP,DL,_=defect_matrices(src)
    pd=typed_conflicts_and_gram(src,maps["f"],src["neighbors_point"],DP,s,t)
    ld=typed_conflicts_and_gram(src,maps["g"],src["neighbors_line"],DL,t,s)
    J=direct_original_owner_conflicts(src,maps)["J"]
    j0,G0=a["each_collinearity_conflict_j0"],a["original_pencil_Gram_G0"]
    assert J==pd["e_col"]+ld["e_col"]
    for d in (pd,ld):
        assert d["e_col"]<=j0*r**4
        assert d["gram"]**2<=G0**2*r**11
    assert J<=a["original_owner_conflict_J0"]*r**4
    rank_fails=any(
        prev[side]["centered_positive_outliers"]**6>nu**6*r**7
        for side in ("point","line"))
    if name in ("wenger3","wenger5") and ell==1 and nu==2:
        q=s+1
        assert rank_fails
        assert all(Q(bound[side]["trace_W"])==Q(q*(q-1)**2,2)
                   for side in ("point","line"))
    return dict(kind=name,scheme=scheme,
       source_s=s,source_t=t,r=r,
       original_points=src["points"],original_lines=len(src["lines"]),
       original_flags=len(src["flags"]),
       actual_Moore_excess_lines=src["excess_lines"],
       actual_Moore_excess_points=src["excess_points"],
       finite_fixture_constants_selected_AFTER_source=True,
       exact_psd_tail_witnesses=bound,
       exact_source_positive_outlier_rank=prev,
       previous_G6D4_rank_gate_fails_at_same_ell_nu=rank_fails,
       original_conflicts_J=J,point_collinearity_conflicts=pd["e_col"],
       line_collinearity_conflicts=ld["e_col"],
       point_original_gram=pd["gram"],line_original_gram=ld["gram"],
       source_constants=a,
       true_original_source_not_synthetic_F=True,
       no_GQ_projection_completion=True)


def certificate():
    examples=[
        finite_case("wenger3","lex",1,2),
        finite_case("wenger3","correlated",1,2),
        finite_case("wenger5","lex",1,2),
        finite_case("W32","lex",2,2),
        finite_case("Qminus24","lex",2,2),
        finite_case("dualQminus42","lex",2,2),
        finite_case("doubleW32","lex",2,2),
        finite_case("doubleQminus24","lex",2,2),
        finite_case("doubleDualQminus42","lex",2,2),
    ]
    ledgers=[integrated_tail_ledger(*v) for v in
        ((1,3,1,2),(1,3,2,0),(2,12,2,2))]
    return dict(schema=SCHEMA,issue=793,parent_G6D4_HEAD=PARENT_G6D4,
        claim="CONDITIONAL_QUADRATIC_T3_POSITIVE_SPECTRAL_TAIL",
        exact_actual_source_PSD_witnesses=examples,
        formal_all_order_source_and_four_error_ledgers=ledgers,
        strict_finite_Wenger5_separation_from_D4_at_same_parameters=True,
        no_infinite_separation_claim=True,
        no_unrestricted_T3_or_ASET=True,
        no_external_referee_or_Lean=True,
        source_original_six_ID_and_flags_only=True,
        spectral_Ky_Fan_PSD_majorant_is_standard_prior_art=True)


if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--out")
    args=ap.parse_args()
    out=certificate()
    blob=json.dumps(out,sort_keys=True,indent=2)+"\n"
    if args.out:
        Path(args.out).write_text(blob,encoding="utf-8")
    else:
        print(blob)
