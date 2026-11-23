"""GIO-003 / G6-D4: few positive collinearity outliers, no F0 norm gate.

Conditional source transfer ONLY. All source geometry is actual original
simple (s,t)-biregular girth>=8 incidence, never a GQ-completed F.
The new key bound uses the *factor-incidence* 0/1 matrix H with row
degree 2 and column degree <=a-1, thus ||H||^2<=2(a-1).
This eliminates a previously proposed eigenvector-delocalization gate.
"""
import argparse
import json
from fractions import Fraction as Q
from pathlib import Path

from gio_t3c_intrinsic_defect import (
    source_graph, typed_maps, defect_matrices, typed_conflicts_and_gram,
    direct_original_owner_conflicts,
)
from gio_t3c2_partial_books import make_model
from gio_t3d_cubic_missing import cube_ceil, sqrt_ceil
from gio_t3d2_centered_sixth import (
    exact_ceil, wenger_W2_prime_source, wenger_W2_spectral_parameters,
)

SCHEMA="mathlab.gio003.g6d4.few-positive-collinearity-outliers.v1"
PARENT_G6D1_FIX="2940b21deefaa997f78f3f9b0ec7beb8047f7334"


def _swap_symmetric(M,i,j):
    if i==j:
        return
    M[i],M[j]=M[j],M[i]
    for row in M:
        row[i],row[j]=row[j],row[i]


def exact_symmetric_inertia(matrix):
    """Sylvester inertia by *exact rational congruences*, not eigensolvers.

    Use 1x1 nonzero diagonal Schur pivots. For the remaining all-zero
    diagonals, a 2x2 [[0,z],[z,0]] pivot contributes (+1,-1); its
    inverse gives an exact symmetric Schur update. If all entries zero,
    all remaining eigenvalues are zero. Works for indefinite matrices
    without positive-definite Cholesky assumptions or floating tolerance.
    """
    n=len(matrix)
    if n<1 or any(len(row)!=n for row in matrix):
        raise ValueError("nonempty square matrix required")
    A=[[Q(x) for x in row] for row in matrix]
    if any(A[i][j]!=A[j][i] for i in range(n) for j in range(i+1,n)):
        raise ValueError("exact symmetry required")
    pos=neg=zero=pair=0
    k=0
    while k<n:
        i=next((i for i in range(k,n) if A[i][i]),None)
        if i is not None:
            _swap_symmetric(A,k,i)
            d=A[k][k]
            pos+=(d>0)
            neg+=(d<0)
            for x in range(k+1,n):
                akx=A[x][k]
                for y in range(x,n):
                    v=A[x][y]-akx*A[y][k]/d
                    A[x][y]=v
                    A[y][x]=v
            k+=1
            continue
        edge=next(((i,j) for i in range(k,n)
                         for j in range(i+1,n) if A[i][j]),None)
        if edge is None:
            zero+=n-k
            break
        i,j=edge
        _swap_symmetric(A,k,i)
        if j==k:
            j=i
        _swap_symmetric(A,k+1,j)
        z=A[k][k+1]
        assert A[k][k]==A[k+1][k+1]==0 and z!=0
        for x in range(k+2,n):
            ax,bx=A[x][k],A[x][k+1]
            for y in range(x,n):
                v=A[x][y]-(ax*A[y][k+1]+bx*A[y][k])/z
                A[x][y]=v
                A[y][x]=v
        pos+=1
        neg+=1
        pair+=1
        k+=2
    assert pos+neg+zero==n
    return dict(positive=pos,negative=neg,zero=zero,
                two_by_two_indefinite_pivots=pair,
                exact_rational_congruence=True)


def actual_outlier_count(neighbors,threshold):
    """Count eigen(A|1_perp)>threshold; correct even if disconnected.

    A is the *actual original source* point or line collinearity graph.
    Its regular all-ones vector contributes exactly one eigenvalue k.
    Other copies of eigenvalue k (disconnected sources) are retained.
    """
    if type(threshold) is not int or threshold<0:
        raise ValueError("exact nonnegative integral threshold required")
    n=len(neighbors)
    if n<1 or any(type(x) is not set for x in neighbors):
        raise ValueError("actual undirected adjacency sets required")
    degree=len(neighbors[0])
    if any(len(row)!=degree or i in row for i,row in enumerate(neighbors)):
        raise ValueError("irregular or looped source collinearity")
    if any(i not in neighbors[j] for i in range(n) for j in neighbors[i]):
        raise ValueError("non-symmetric adjacency")
    M=[[int(j in neighbors[i])-(threshold if i==j else 0)
        for j in range(n)] for i in range(n)]
    z=exact_symmetric_inertia(M)
    nout=z["positive"]-int(degree>threshold)
    assert 0<=nout<=n-1
    return dict(vertices=n,degree=degree,threshold=threshold,
                positive_all=z["positive"],trivial_positive_removed=int(degree>threshold),
                centered_positive_outliers=nout,inertia=z,
                no_numeric_eigensolver=True)


def original_source_case(name,scheme="lex"):
    if name in ("doubleQminus24","doubleDualQminus42"):
        old=make_model("Qminus24" if name=="doubleQminus24"
                       else "dualQminus42")
        P=old["points"]
        lines=[set(line) for line in old["lines"]]
        lines += [{p+P for p in line} for line in old["lines"]]
        src=source_graph(lines,2*P,old["s"],old["t"])
    elif name in ("wenger3","wenger5"):
        src=wenger_W2_prime_source(3 if name=="wenger3" else 5)
    else:
        src=make_model(name,scheme)
    maps=typed_maps(src,scheme)
    return src,maps


def outlier_mixing_constants(b,C,ell,nu):
    """Exact all-order O(r^4) source conflict and O(r^11/2) Gram bounds.

    With Delta_L<=C*r^2 and max(s,t)<=b*r:
      centered positive collinearity eigenvalues exceeding ell*r
      have multiplicity at most nu*r, on BOTH point and line sides.
    The cubic source identity bounds every such eigenvalue by
      (4*b+cube_ceil(4*(b+1)*C^2))*r^(4/3).
    Factor incidence H has max row 2, max column (a-1), hence
      sum_x <1_Sx,A 1_Sx> <=
         2*k*(a-1)+2*ell*r*V+
         2*(a-1)*sum_exceptional positive lambda.
    """
    if any(type(v) is not int for v in (b,C,ell,nu)) or (
            b<1 or C<0 or ell<0 or nu<0):
        raise ValueError("fixed exact integer b>=1; C,ell,nu>=0")
    v0=(b+1)*(b*b+1+C)
    n0=(b+1)*v0
    a0=2*v0+3
    A0=a0*a0
    k0=b*(b+1)
    theta0=b+2
    cubic_root=cube_ceil(4*(b+1)*C*C)
    upper_outlier_lambda0=4*b+cubic_root
    j0=k0*a0+ell*v0+a0*nu*upper_outlier_lambda0
    J0=2*j0
    G0=2*v0*k0+2*theta0*j0+2*(b+1)*v0*a0
    return dict(balance_b=b,quadratic_excess_C=C,
                regular_centered_cutoff_ell=ell,outlier_count_nu=nu,
                source_V0=v0,source_N0=n0,alphabet_a0=a0,
                physical_vertices_A0=A0,point_degree_k0=k0,
                theta0=theta0,cubic_source_root0=cubic_root,
                exceptional_lambda_coefficient=upper_outlier_lambda0,
                each_collinearity_conflict_j0=j0,
                original_owner_conflict_J0=J0,original_pencil_Gram_G0=G0,
                factor_incidence_norm_square_coefficient=2,
                no_eigenvector_delocalization_assumption=True,
                no_global_F0_operator_norm_assumption=True)


def integrated_outlier_ledger(b=1,C=3,ell=2,nu=1,C0=Q(1),c0=Q(1)):
    """Exact FULL/CORE HEAVY/LOW parameter reuse, strictly conditional.

    The imported G6-C3/2 argument uses source only via J0,G0,
    source sizes/alphabets, original missing endpoints and original
    3st source-projection loads. External ordinary-graph C6 constants
    remain FORMAL placeholders (not independently numerically proved).
    """
    if type(C0) is not Q or type(c0) is not Q or C0<1 or not 0<c0<=1:
        raise ValueError("exact external C0>=1 and 0<c0<=1")
    a=outlier_mixing_constants(b,C,ell,nu)
    v0,n0,a0,A0=(a[k] for k in
                 ("source_V0","source_N0","alphabet_a0","physical_vertices_A0"))
    J0,G0=a["original_owner_conflict_J0"],a["original_pencil_Gram_G0"]
    rho_cap=Q(1,32)
    Ksel=16*J0+1
    assert Q(7,8)-rho_cap-Q(2*J0,Ksel+1)>Q(1,2)
    R=512*A0*(1+64*J0)
    T=exact_ceil(8*n0*R**3*C0**3)
    w=Q(8,A0*A0)
    q2=16*(Ksel+1)**2
    q3=64*(Ksel+1)**3
    Q0=8*n0+4*J0
    L6=1+exact_ceil(36*n0*T*T)
    L4=q2*q2*sqrt_ceil(n0*L6)+Q0*T
    # Quadratic excess: original missing endpoints <=4*v0*C*r^5.
    E0=4*(2*a0*v0+a0*a0)+4*n0+4*v0*C+8*b*J0
    E=q3*sqrt_ceil(E0*L6)
    BK=sqrt_ceil(16*(b+1)*n0*G0*(Ksel+1)*T)
    D=4*sqrt_ceil(BK*T*L4)
    improper=3*T*Q0
    eps=w/8
    rho=min(rho_cap,eps*eps/Q(12*b*b*q3*q3*L6))
    delta=min(c0/Q(R**6),w/4)
    r0=max(2**32,exact_ceil(Q(improper)/eps),
           exact_ceil((Q(E)/eps)**2),
           exact_ceil((Q(D)/eps)**8))
    assert rho>0 and delta>0 and r0>0
    assert improper<=eps*r0 and E*E<=eps*eps*r0
    assert D**8<=eps**8*r0
    assert 12*b*b*rho*q3*q3*L6<=eps*eps
    return dict(schema=SCHEMA,issue=793,
        claim="CONDITIONAL_T3_QUADRATIC_EXCESS_FEW_POSITIVE_OUTLIERS",
        FORMAL_ONLY=True,
        fixed_before_source=dict(balance_b=b,quadratic_C=C,
            eigenvalue_cutoff_ell=ell,outlier_multiplicity_nu=nu,
            external_C0=str(C0),external_c0=str(c0)),
        source=a,
        selector=dict(K=Ksel,R=R,T=T,w=str(w),q2=q2,q3=q3,
            same_single_global_typed_selector=True),
        moments=dict(Q0=Q0,L6=L6,L4=L4,E0=E0,E=E,
            mixed_book_BK=BK,blocker_D=D,improper=improper,
            missing_endpoint_bound="4*V_P*Delta_L<=4*v0*C*r^5",
            new_source_gate="for BOTH collinearity types, count(lambda>ell*r on 1_perp)<=nu*r",
            no_centered_F0_operator_or_sixth_moment_gate=True),
        closure=dict(rho=str(rho),delta=str(delta),eps=str(eps),
            sufficient_r0=str(r0),four_LOW_errors_each_below_eps=True),
        prerequisites=dict(parent_G6D1_FIX_HEAD=PARENT_G6D1_FIX,
            actual_original_source_girth_at_least_8=True,
            inherited_G6C3_HEAVY_LOW=True,
            inherited_G6C2_FULL_CORE_inverse=True,
            real_external_C6_constants_required=True),
        no_unrestricted_T3=True,
        no_new_infinite_family_with_bad_global_F0_claim=True,
        no_external_referee_or_Lean=True,
        no_improved_ASET_exponent=True)


def source_case(name,scheme="lex",ell=2,nu=1):
    """Independent literal source, exact symmetric inertia and adversarial maps."""
    src,maps=original_source_case(name,scheme)
    s,t=src["s"],src["t"]
    r=min(s,t)
    b=exact_ceil(Q(max(s,t),r))
    C=exact_ceil(Q(src["excess_lines"],r*r))
    constants=outlier_mixing_constants(b,C,ell,nu)
    outp=actual_outlier_count(src["neighbors_point"],ell*r)
    outl=actual_outlier_count(src["neighbors_line"],ell*r)
    assert outp["centered_positive_outliers"]<=nu*r
    assert outl["centered_positive_outliers"]<=nu*r
    DP,DL,_=defect_matrices(src)
    pd=typed_conflicts_and_gram(src,maps["f"],src["neighbors_point"],DP,s,t)
    ld=typed_conflicts_and_gram(src,maps["g"],src["neighbors_line"],DL,t,s)
    J=direct_original_owner_conflicts(src,maps)["J"]
    assert J==pd["e_col"]+ld["e_col"]
    j0=constants["each_collinearity_conflict_j0"]
    G0=constants["original_pencil_Gram_G0"]
    for dat in (pd,ld):
        assert dat["e_col"]<=j0*r**4
        assert dat["gram"]**2<=G0*G0*r**11
    assert J<=constants["original_owner_conflict_J0"]*r**4
    if name in ("doubleW32","doubleQminus24","doubleDualQminus42"):
        assert outp["centered_positive_outliers"]==1
        assert outl["centered_positive_outliers"]==1
    if name in ("wenger3","wenger5"):
        w=wenger_W2_spectral_parameters(3 if name=="wenger3" else 5)
        assert outp["centered_positive_outliers"]==0
        assert outl["centered_positive_outliers"]==0
        assert w["actual_Moore_excess_each"]==src["excess_lines"]
    # A finite parameter C chosen AFTER the fixture is a unit test,
    # not proof of a uniform infinite spectral family.
    return dict(kind=name,scheme=scheme,source_s=s,source_t=t,
        r=r,points=src["points"],lines=len(src["lines"]),
        original_source_flags=len(src["flags"]),
        delta_line=src["excess_lines"],delta_point=src["excess_points"],
        fixed_FAMILY_parameters_NOT_deduced_from_fixture=True,
        centered_point_inertia=outp,centered_line_inertia=outl,
        actual_fixed_map_point_conflicts=pd["e_col"],
        actual_fixed_map_line_conflicts=ld["e_col"],
        actual_original_owner_conflicts=J,
        point_gram=pd["gram"],line_gram=ld["gram"],
        finite_source_constants=constants,
        true_source_not_synthetic_missing_F=True,
        no_GQ_completion=True)


def certificate():
    ledgers=[integrated_outlier_ledger(*v) for v in
             ((1,3,2,1),(1,3,2,0),(2,12,2,1))]
    fixtures=[source_case(*v) for v in
       (("W32","lex"),("Qminus24","lex"),
        ("dualQminus42","lex"),("doubleW32","lex"),
        ("doubleQminus24","lex"),("doubleDualQminus42","lex"),
        ("wenger3","lex"),("wenger3","correlated"),
        ("wenger5","lex"))]
    return dict(schema=SCHEMA,issue=793,
        parent_G6D1_FIX_HEAD=PARENT_G6D1_FIX,
        claim="CONDITIONAL_T3_QUADRATIC_EXCESS_FEW_POSITIVE_OUTLIERS",
        novel_in_program_factor_incidence_trace_bound=True,
        eigenvector_delocalization_NOT_required=True,
        unconditional_quadratic_excess_T3_NOT_proved=True,
        new_infinite_bad_gap_family_NOT_constructed=True,
        exact_source_inertia_finite_falsifiers=fixtures,
        all_order_formal_ledgers=ledgers,
        source_GQ_axiom_NOT_used=True,
        prior_art_spectral_decomposition_and_inertia=True,
        external_referee_or_Lean_NOT_claimed=True)


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
