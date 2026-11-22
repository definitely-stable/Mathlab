"""GIO-003 G6-D2: centered missing-projection sixth-moment transfer.

For actual finite simple thick biregular girth>=8 incidence, define the
original missing-threepath matrix F from G6-D1. The original cubic
identity on 1-perp needs ONLY ||F0||^2, not ||F||^2.

S6=tr((F F^T)^3)-(DeltaL DeltaP)^3 equals sum of sixth powers of
NONTRIVIAL singular values. If source has DeltaL<=C*r^2 AND
S6<=M*r^9 with FIXED b,C,M, the old G6-C3 original six-ID HEAVY/LOW
proof yields a conditional nonGQ T3 quadratic-excess theorem.

The sixth-moment bound is ADDITIONAL, NOT established merely by
biregularity, girth>=8 or bounded quadratic excess.
All test graph constants C0,c0 are FORMAL_ONLY existential placeholders.
"""
import argparse
import json
from fractions import Fraction as Q
from itertools import product
from math import gcd, isqrt
from pathlib import Path

from gio_t3c2_partial_books import make_model
from gio_t3d_cubic_missing import (
    construct_missing_matrices, polynomial_identity, cube_ceil,
    matmul, transpose, ceil, sqrt_ceil,
)

SCHEMA="mathlab.gio003.g6d2.centered-missing-sixth.v1"
PARENT_G6D1="0f0d4b5f76373a00513d9085ee5d3cfa011d5c0f"


def exact_ceil(x):
    x=Q(x)
    return -(-x.numerator//x.denominator)


def raw_trace_cube(K):
    """Count all rooted typed closed 6walks in F, without eigensolvers."""
    n=len(K)
    assert all(len(row)==n for row in K)
    return sum(K[i][j]*K[j][k]*K[k][i]
               for i in range(n) for j in range(n) for k in range(n))


def sixth_moment_certificate(mats):
    """Exact parent F and independent point/line trace6 with cancellation."""
    F=mats["F"]
    P,L=mats["vp"],mats["vl"]
    dl,dp=mats["delta_line"],mats["delta_point"]
    assert P>=2 and L>=2
    Kp=matmul(F,transpose(F))
    Kl=matmul(transpose(F),F)
    principal=dl*dp
    assert all(sum(row)==principal for row in Kp)
    assert all(sum(row)==principal for row in Kl)
    trp=raw_trace_cube(Kp)
    trl=raw_trace_cube(Kl)
    assert trp==trl
    s6=trp-principal**3
    s2=P*dl-principal
    assert s2==L*dp-principal
    assert s6>=0 and s2>=0
    assert s2==0 if dl==0 else s2>0
    # For n=P-1 nonnegative nontrivial eigenvalues h_j of Kp:
    # (sum_j h_j)^3 <= (P-1)^2 sum_j h_j^3.
    assert (P-1)**2*s6>=s2**3
    assert (L-1)**2*s6>=s2**3
    # The same principal eigen is removed ONCE. In disconnected sources
    # there may be ANOTHER eigen with the same value, which remains in s6.
    return dict(source_points=P,source_lines=L,delta_line=dl,delta_point=dp,
        ordinary_closed_sixwalks_point_rooted=trp,
        ordinary_closed_sixwalks_line_rooted=trl,
        trivial_singular_sixth_power=principal**3,
        exact_centered_S6=s6,exact_centered_S2=s2,
        Jensen_lower_point=str(Q(s2**3,(P-1)**2)),
        Jensen_lower_line=str(Q(s2**3,(L-1)**2)),
        Frobenius_ordinary_point_energy_trace=P*dl,
        strict_nonGQ_S6_positive=(s6>0),
        no_unjustified_F_norm_equals_F0_norm=True,
        no_source_GQ_completion=True)


def exact_codegrees(mats):
    """Literal number of common original MISSING lines for each pair."""
    F=mats["F"];P,L=mats["vp"],mats["vl"]
    K=[[sum(F[p][ell] and F[q][ell] for ell in range(L))
        for q in range(P)] for p in range(P)]
    assert all(K[p][p]==mats["delta_line"] for p in range(P))
    return K


def centered_gram(mats):
    K=exact_codegrees(mats)
    P=mats["vp"]
    lam=mats["delta_line"]*mats["delta_point"]
    beta=Q(lam,P)
    H=[[Q(K[i][j])-beta for j in range(P)] for i in range(P)]
    assert all(sum(row)==0 for row in H)
    assert H==transpose(H)
    return H


def fractional_psd(A):
    """Exact symmetric rational Schur-complement PSD certificate.

    Pivot zero is legal only when the entire remaining off-diagonal
    entry vanishes. No floating Cholesky or random Rayleigh acceptance.
    """
    n=len(A)
    if any(len(row)!=n for row in A):
        raise ValueError("square matrix required")
    M=[[Q(x) for x in row] for row in A]
    if M!=transpose(M):
        raise ValueError("symmetric matrix required")
    positive=0;zero=0
    for i in range(n):
        pivot=M[i][i]
        if pivot<0:
            return dict(PSD=False,negative_pivot_at=i,positive=positive,zero=zero)
        if pivot==0:
            if any(M[j][i] for j in range(i+1,n)):
                return dict(PSD=False,zero_pivot_nonzero_cross_at=i,
                            positive=positive,zero=zero)
            zero+=1
            continue
        positive+=1
        for j in range(i+1,n):
            for k in range(j,n):
                v=M[j][k]-M[j][i]*M[k][i]/pivot
                M[j][k]=v
                M[k][j]=v
    return dict(PSD=True,positive=positive,zero=zero)


def direct_centered_spectral_certificate(mats):
    """Find EXACT integer kappa with 0 <= F0F0^T <= kappa*r^3 * I.

    Note that the inequality on all vectors is equivalent to the
    centered 1-perp source spectral condition, since centered Gram H is
    PSD, and has zero eigenvalue on the constant vector.
    """
    P=mats["vp"];r=min(mats["s"],mats["t"])
    H=centered_gram(mats)
    six=sixth_moment_certificate(mats)
    # S6 >= max_centered_eigenvalue^3; kappa is ceiling of that
    # eigenvalue divided by r^3.
    upper=exact_ceil(Q(cube_ceil(six["exact_centered_S6"]),r**3))
    assert upper>=0
    def check(k):
        A=[[Q(k*r**3)*(i==j)-H[i][j] for j in range(P)]
           for i in range(P)]
        return fractional_psd(A)["PSD"]
    assert check(upper)
    lo=0;hi=upper
    while lo<hi:
        mid=(lo+hi)//2
        if check(mid):
            hi=mid
        else:
            lo=mid+1
    assert check(lo)
    if lo:
        assert not check(lo-1)
    row_L1=max((sum(abs(z) for z in row) for row in H),default=Q(0))
    assert row_L1>=0
    eta_integer=exact_ceil(row_L1)
    eta_kappa=exact_ceil(Q(row_L1,r**3))
    assert check(eta_kappa)
    assert lo<=eta_kappa and lo<=upper
    return dict(exact_min_integer_centered_norm_kappa=lo,
        actual_certified_centered_norm_squared_upper=lo*r**3,
        Sixth_moment_operator_bound_integer=upper,
        actual_codegree_row_abs_max=str(row_L1),
        row_abs_integer_ceil=eta_integer,
        row_abs_scaled_kappa=eta_kappa,
        exact_centered_Gram_PSD_passed=True,
        exact_prior_kappa_minus_one_fails=bool(lo),
        independent_codegree_L1_sufficiency_verified=True,
        nontrivial_sixth_moment_sufficient_not_necessary=True)


def mixing_constants(b,C,M):
    """All-order exact source envelopes under fixed QUADRATIC excess+C6 moment."""
    if any(type(z) is not int for z in (b,C,M)) or b<1 or C<0 or M<0:
        raise ValueError("fixed integer b>=1, C>=0, M>=0 before family")
    v0=(b+1)*(b*b+1+C)
    n0=(b+1)*v0
    a0=2*v0+3
    A0=a0*a0
    k0=b*(b+1)
    theta0=b+2
    rootM=cube_ceil(M)
    source_root=cube_ceil(4*rootM)
    lambda0=5*b+1+source_root
    j0=k0*a0+lambda0*v0
    J0=2*j0
    G0=2*v0*k0+2*theta0*j0+2*(b+1)*v0*a0
    return dict(balance_b=b,quadratic_excess_C=C,
         centered_sixth_moment_M=M,
         source_V0=v0,source_N0=n0,
         alphabet_a0=a0,physical_vertices_A0=A0,
         point_degree_k0=k0,theta0=theta0,
         centered_operator_kappa0=rootM,
         cubic_source_root0=source_root,
         source_collinearity_Lambda0=lambda0,
         collinearity_conflict_j0=j0,original_owner_conflict_J0=J0,
         original_pencil_Gram_G0=G0,
         structural_M_is_AN_ADDITIONAL_assumption=True)


def integrated_quadratic_moment_ledger(b=1,C=0,M=0,C0=Q(1),c0=Q(1)):
    """Source independent HEAVY/LOW closure, but WITH two explicit gates.

    (1) DeltaL <=C r^2, (2) centered S6(F) <=M r^9.
    Numeric C0,c0 are formal published-constant placeholders ONLY.
    """
    if type(C0) is not Q or type(c0) is not Q or C0<1 or not 0<c0<=1:
        raise ValueError("admissible external C0>=1, 0<c0<=1 exact rationals")
    a=mixing_constants(b,C,M)
    v0,n0,a0,A0=(a[k] for k in
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
    # Different from G6-D1: |P|DeltaL <= v0*C*r^5 exactly
    # under the new QUADRATIC cap. No missing-projection is completed.
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
    assert 12*b*b*rho*q3*q3*L6<=eps*eps
    assert improper<=eps*r0
    assert E*E<=eps*eps*r0
    assert D**8<=eps**8*r0
    return dict(schema=SCHEMA,
       claim="CONDITIONAL_INTRINSIC_QUADRATIC_T3_WITH_CENTERED_MISSING_SIXTH_MOMENT",
       FORMAL_ONLY=True,external_numeric_C6_constants_NOT_verified=True,
       fixed_before_source=dict(balance_b=b,quadratic_C=C,
             centered_M=M,external_graph_C0=str(C0),external_graph_c0=str(c0)),
       source=a,
       selector=dict(K=K,R=R,T=T,w=str(w),q2=q2,q3=q3,
                     single_global_owner_priority=True,
                     single_global_typed_bit_pair=True),
       moments=dict(Q0=Q0,L6=L6,L4=L4,E0=E0,E=E,
           mixed_book_BK=BK,blocker_D=D,improper=improper,
           new_moore_hole_coefficient=4*v0*C,
           missing_projection_gate="Delta_L<=C*r^2",
           centered_moment_gate="tr((FFt)^3)-(DeltaL*DeltaP)^3 <= M*r^9"),
       closure=dict(rho=str(rho),delta=str(delta),eps=str(eps),
                    sufficient_r0=str(r0),
                    four_LOW_errors_each_below_eps=True,
                    LOW_BBo_produced_lower="w*r^6/4",
                    HEAVY_original_D6_lower="c0*r^6/R^6"),
       prerequisites=dict(parent_G6D1_HEAD=PARENT_G6D1,
          inherited_G6C3_shared_selector=True,
          inherited_G6C2_FULL_CORE_original_BBo_inverse=True,
          real_external_ordinary_graph_C6_count_required=True),
       exact_no_GQ_witness_required=True,
       no_unconditional_quadratic_T3=True,
       no_infinite_nonGQ_quadratic_moment_family_claim=True,
       no_unrestricted_ASET_exponent=True,
       no_external_referee_or_Lean=True)


def validate_family_gate(s,t,DL,DP,s6,deleted,record):
    if any(type(x) is not int for x in (s,t,DL,DP,s6,deleted)):
        raise ValueError("source counts, moments and deletion count must be exact integers")
    f=record["fixed_before_source"];b,C,M=f["balance_b"],f["quadratic_C"],f["centered_M"]
    r=min(s,t)
    if r<int(record["closure"]["sufficient_r0"]) or max(s,t)>b*r:
        raise ValueError("outside sufficient threshold or balance")
    if DL<0 or DP<0 or s6<0 or (s+1)*DL!=(t+1)*DP:
        raise ValueError("invalid source excess, moment or degree balance")
    if DL>C*r*r:
        raise ValueError("outside quadratic Moore-excess cap")
    if s6>M*r**9:
        raise ValueError("centered sixth moment too large")
    if deleted<0 or deleted>Q(record["closure"]["rho"])*r**4:
        raise ValueError("original source deletions over resilience radius")
    return True


def finite_source_case(name,scheme="lex"):
    m=make_model(name,scheme)
    mat=construct_missing_matrices(m)
    assert polynomial_identity(mat)["exact_point_and_line_cubic_identity"]
    moments=sixth_moment_certificate(mat)
    exact=direct_centered_spectral_certificate(mat)
    r=min(mat["s"],mat["t"])
    C=exact_ceil(Q(mat["delta_line"],r*r))
    M=exact_ceil(Q(moments["exact_centered_S6"],r**9))
    # These C,M are selected *after* seeing this one finite fixture:
    # they are NOT an asymptotic fixed-family certificate.
    constants=mixing_constants(
       (max(mat["s"],mat["t"])+r-1)//r,C,M)
    assert moments["exact_centered_S6"]<=M*r**9
    assert mat["delta_line"]<=C*r*r
    point_cap=constants["source_collinearity_Lambda0"]*r
    old_cap=2*(mat["s"]+mat["t"])+mat["t"]+1+cube_ceil(
        4*mat["delta_line"]*mat["delta_point"])
    # New proven cap can differ from old full-norm cap; deliberately
    # no universal strict improvement claim on every small fixture.
    return dict(kind=name,scheme=scheme,source_s=mat["s"],source_t=mat["t"],
         points=mat["vp"],lines=mat["vl"],
         exact_centered_moments=moments,
         exact_centered_spectral=exact,
         fixture_selected_quadratic_C=C,
         fixture_selected_centered_M=M,
         uniform_family_spectral_bound=point_cap,
         previous_crude_full_norm_bound=old_cap,
         old_source_missing_operator_full_norm_squared=(
            mat["delta_line"]*mat["delta_point"]),
         actual_spectral_one_perp_gate=exact["exact_min_integer_centered_norm_kappa"],
         no_infinite_family_deduced_from_fixture=True)


def synthetic_2block_missing_barrier(q=2):
    """REGULAR missing mask countermodel, NEVER an incidence graph claim.

    n=2*q^3, two disconnected q^2-regular circulant bipartite
    components of size q^3 per side. The block sign +/-1 is a
    nontrivial singular vector with singular value q^2, hence
    centered squared norm >=q^4, and S6>=q^12. Thus a bound
    O(q^3) on ||F0||^2 cannot follow from 0/1 constant row/col
    sums and Delta=q^2 ALONE, independent of any incidence constraints.
    """
    if type(q) is not int or q<2:
        raise ValueError("integer q>=2 required")
    block=q**3;d=q*q;n=2*block
    assert d<=block
    F=[[0]*n for _ in range(n)]
    for side in (0,1):
        for i in range(block):
            for k in range(d):
                F[side*block+i][side*block+(i+k)%block]=1
    assert all(sum(row)==d for row in F)
    assert all(sum(F[i][j] for i in range(n))==d for j in range(n))
    sign=[1]*block+[-1]*block
    assert sum(sign)==0
    v=[sum(F[i][j]*sign[j] for j in range(n)) for i in range(n)]
    assert v==[d*z for z in sign]
    # Centered F0 agrees with F on the zero-sum block-sign mode.
    # The principal all-ones singular vector is separate.
    K=matmul(F,transpose(F))
    six=raw_trace_cube(K)-d**6
    assert six>=d**6
    return dict(q=q,symmetric_zero_one_degree=d,
       source_like_part_size=n,
       centered_block_sign_exact_singular_value=d,
       centered_squared_spectral_lower=d*d,
       centered_operator_over_q_cubed=str(Q(d*d,q**3)),
       centered_S6_lower=d**6,actual_centered_S6=six,
       sixth_moment_over_q_ninth_lower=str(Q(d**6,q**9)),
       mask_IS_NOT_verified_as_incidence_source=True,
       no_unconditional_quadratic_conclusion_from_degree_counts=True)


def uniform_direct_spectral_constants(b,C,kappa):
    """Quadratic source envelope, WITHOUT any sixth-moment assumption."""
    if any(type(z) is not int for z in (b,C,kappa)) or b<1 or C<0 or kappa<0:
        raise ValueError("fixed integer b>=1,C>=0,kappa>=0")
    # Same algebraic envelopes as moment ledger, but kappa is a separately
    # assumed centered OPERATOR bound (NOT deduced from S6 here).
    x=mixing_constants(b,C,kappa**3)
    x.pop("centered_sixth_moment_M")
    x.pop("structural_M_is_AN_ADDITIONAL_assumption")
    x["centered_operator_kappa0"]=kappa
    x["structural_centered_spectral_bound_is_AN_ADDITIONAL_assumption"]=True
    return x


def integrated_quadratic_direct_ledger(b=1,C=3,kappa=3,C0=Q(1),c0=Q(1)):
    """Correct transfer using ||F0||^2 <= kappa*r^3, not S6<=M*r^9."""
    if type(kappa) is not int or kappa<0:
        raise ValueError("fixed centered integer kappa>=0")
    # Shared all-error arithmetic is reused with M=kappa^3 solely as a
    # parametrization yielding cube_ceil(M)=kappa. A moment gate is NOT
    # imported as a hypothesis in this alternative theorem.
    z=integrated_quadratic_moment_ledger(b,C,kappa**3,C0,c0)
    z["claim"]="CONDITIONAL_INTRINSIC_QUADRATIC_T3_WITH_DIRECT_CENTERED_SPECTRAL_GATE"
    z["fixed_before_source"].pop("centered_M")
    z["fixed_before_source"]["centered_operator_kappa"]=kappa
    z["source"]=uniform_direct_spectral_constants(b,C,kappa)
    z["moments"].pop("centered_moment_gate")
    z["moments"]["centered_spectral_gate"]="lambda_max(F F^T-(DeltaL*DeltaP/|P|)*J) <= kappa*r^3"
    z["moment_sixth_condition_is_NOT_required"]=True
    z["exact_LDL_source_certificate_available"]=True
    z["no_unconditional_quadratic_T3"]=True
    return z


def validate_direct_family_gate(s,t,DL,DP,observed_kappa,deleted,ledger):
    """No assumption on S6, only a directly certified centered F norm."""
    if any(type(x) is not int for x in (s,t,DL,DP,observed_kappa,deleted)):
        raise ValueError("all source and spectral inputs must be exact integers")
    f=ledger["fixed_before_source"]
    b,C,kappa=(f["balance_b"],f["quadratic_C"],f["centered_operator_kappa"])
    r=min(s,t)
    if r<int(ledger["closure"]["sufficient_r0"]) or max(s,t)>b*r:
        raise ValueError("balance/threshold failure")
    if DL<0 or DP<0 or (s+1)*DL!=(t+1)*DP or DL>C*r*r:
        raise ValueError("invalid source Moore excess")
    if observed_kappa<0 or observed_kappa>kappa:
        raise ValueError("source lacks centered spectral gate")
    if deleted<0 or deleted>Q(ledger["closure"]["rho"])*r**4:
        raise ValueError("source deletion exceeds budget")
    return True


def is_prime(q):
    if type(q) is not int or q<2:
        return False
    return all(q%d for d in range(2,isqrt(q)+1))


def wenger_W2_prime_source(q):
    """Literal **prime** field realization of published Wenger W'_2(q).

    Points (a,b,c), lines [u,v,w] over F_q, with v+b=u*a and
    w+c=u*a^2; THIS is the W'_2(q) monomial representation, which
    the Cioaba-Lazebnik-Li paper proves is isomorphic to W_2(q).
    The all-prime-POWERS existence theorem uses that published result;
    this finite oracle intentionally implements only actual prime fields.
    """
    if not is_prime(q) or q<3:
        raise ValueError("finite literal oracle requires a prime q>=3")
    pts=list(product(range(q),repeat=3))
    lins=list(product(range(q),repeat=3))
    pindex={p:i for i,p in enumerate(pts)}
    lindex={ell:i for i,ell in enumerate(lins)}
    lines=[set() for _ in lins]
    for p,(a,b,c) in enumerate(pts):
        for u in range(q):
            name=(u,(u*a-b)%q,(u*a*a-c)%q)
            lines[lindex[name]].add(p)
    assert all(len(x)==q for x in lines)
    from gio_t3c_intrinsic_defect import source_graph
    source=source_graph(lines,q**3,q-1,q-1)
    assert len(source["flags"])==q**4
    assert source["excess_lines"]==2*q*(q-1)
    assert source["excess_points"]==2*q*(q-1)
    return source


def wenger_W2_spectral_parameters(q):
    """ALL prime powers q>=3: published exact W2(q) spectrum + arithmetic.

    Published source: Cioaba, Lazebnik, Li (2014), Theorem 2.1.
    T=BB^T eigenvalues q^2 (one), 0, q, 2q.
    The multiplicities m0,m1,m2 count nonzero polynomial coefficients.
    Here r=q-1, source Moore excess 2qr, and centered F0 Gram equals
    T(T-2rI)^2 on 1^perp, so its nonzero spectra are
       q*(q-2)^2, 8q.
    """
    if type(q) is not int or q<3:
        raise ValueError("q>=3 integer (and separately PRIME POWER) required")
    r=q-1
    m1=2*q*(q-1)
    m2=q*(q-1)**2//2
    assert q*(q-1)**2%2==0
    m0=q**3-1-m1-m2
    assert m0>=0 and 1+m0+m1+m2==q**3
    a=q*(q-2)**2
    b=8*q
    spectral=max(a,b)
    # Exact inequalities valid for all integers q>=3:
    assert r**3-a==r*r+r-1>0
    assert 3*r**3-b==(r-2)*(3*r*r+6*r+4)>=0
    assert 2*q*r<=3*r*r
    s6=m1*a**3+m2*b**3
    s2=m1*a+m2*b
    # Also derived by F 0/1 row sums, without published multiplicities.
    DL=2*q*r
    assert s2==q**3*DL-DL**2
    return dict(q=q,r=r,actual_source_vertices_per_part=q**3,
        actual_source_degree=q,actual_girth=8,
        actual_Moore_excess_each=DL,
        source_nongq_for_all_q_ge3=True,
        eigenvalues_BBt_nontrivial=[0,q,2*q],
        eigen_multiplicities_BBt=dict(zero=m0,q=m1,two_q=m2,
                                   principal_q_squared=1),
        centered_F0_nontrivial_spectral_levels=[0,a,b],
        exact_centered_F0_norm_squared=spectral,
        uniform_fixed_operator_kappa=3,
        uniform_quadratic_excess_C=3,
        source_balance_b=1,
        centered_source_second_moment=s2,
        centered_source_sixth_moment=s6,
        six_moment_over_r_ninth=str(Q(s6,r**9)),
        direct_centered_gate_verified_for_all_integer_q_ge3=True,
        # Mathematical all-q proof requires a prime-power q. The purely
        # integer spectral envelope itself holds for all q>=3.
        actual_family_exists_for_all_prime_powers_q_ge3_by_published_work=True,
        published_W2_not_newly_discovered=True,
        known_induced_GQ_embedding_not_assumed_in_source_T3_proof=True)


def wenger_finite_exact_case(q):
    """Small actual Wenger W'_2 prime field, exact source polynomial checks."""
    m=wenger_W2_prime_source(q)
    mat=construct_missing_matrices(m)
    identity=polynomial_identity(mat)
    assert identity["exact_point_and_line_cubic_identity"]
    P=m["points"]
    T=mat["T"]
    def shift(scale):
        return [[T[i][j]-scale*(i==j) for j in range(P)]
                for i in range(P)]
    left=matmul(matmul(T,shift(q)),shift(2*q))
    constant=q*(q-1)*(q-2)
    assert all(v==constant for row in left for v in row)
    expected=wenger_W2_spectral_parameters(q)
    exact=sixth_moment_certificate(mat)
    assert exact["exact_centered_S6"]==expected["centered_source_sixth_moment"]
    assert exact["exact_centered_S2"]==expected["centered_source_second_moment"]
    assert mat["delta_line"]==expected["actual_Moore_excess_each"]
    assert mat["delta_point"]==expected["actual_Moore_excess_each"]
    if q==3:
        cert=direct_centered_spectral_certificate(mat)
        assert cert["exact_min_integer_centered_norm_kappa"]==3
    return dict(q=q,points=P,lines=len(m["lines"]),
      original_source_flags=len(m["flags"]),
      genuine_original_source_graph_girth8=True,
      cubic_identity_point_line_exact=True,
      all_entries_published_W2_spectral_polynomial_exact=True,
      spectral_polynomial_constant=constant,
      centered_S2_checked_against_published_eigen_multiplicities=True,
      centered_S6_checked_against_published_eigen_multiplicities=True,
      genuine_nongq_delta=m["excess_lines"],
      actual_sixth_moment=exact["exact_centered_S6"],
      published_formula_centered_kappa=3,
      exact_PSD_q3_sharp=(q==3),
      never_assumed_GQ_source_projection_completeness=True)


def wenger_quadratic_theorem_ledger():
    """A GENUINELY NONVACUOUS prime-power family, external C6 numeric formal."""
    fixed=integrated_quadratic_direct_ledger(1,3,3,Q(1),Q(1))
    assert fixed["moment_sixth_condition_is_NOT_required"]
    return dict(family="published_Wenger_W2(q)_for_all_prime_powers_q_ge3",
       source_fixed_parameters=dict(b=1,C=3,kappa=3),
       theorem="D6+BBo_produced>=delta*r^6 for all sufficiently large q",
       deletions="any named original source |Z|<=rho*r^4",
       arbitrary_complete_minimal_injective_factor_maps=True,
       no_GQ_witness_in_abstract_proof=True,
       published_W2_is_known_induced_GQ_subgraph=True,
       cited_published_spectrum_is_NOT_our_novelty=True,
       no_external_numeric_C6_theorem_constants_certified=True,
       example_formal_ledger=fixed)


def certificate():
    cases=[finite_source_case(name,scheme) for name,scheme in (
        ("W32","lex"),("W33","lex"),
        ("Qminus24","lex"),("dualQminus42","lex"),
        ("doubleW32","lex"),("switchedDoubleW32","lex"),
        ("switchedDoubleW32","correlated"),("Qminus24","correlated"))]
    ledgers=[integrated_quadratic_moment_ledger(b,C,M,C0,c0)
       for b,C,M,C0,c0 in ((1,0,0,Q(1),Q(1)),
          (1,1,1,Q(1),Q(1)),(2,2,8,Q(2),Q(1,2)),
          (3,4,64,Q(3),Q(1,3)))]
    barriers=[synthetic_2block_missing_barrier(q) for q in (2,3)]
    wenger_finite=[wenger_finite_exact_case(q) for q in (3,5)]
    wenger_symbolic=[wenger_W2_spectral_parameters(q)
       for q in (3,4,5,7,8,9,11,16,25,101)]
    direct_ledgers=[integrated_quadratic_direct_ledger(b,C,k)
       for b,C,k in ((1,3,3),(2,4,4),(3,5,8))]
    return dict(schema=SCHEMA,issue=793,meta_issue=790,
       parent_G6D1_HEAD=PARENT_G6D1,
       claim="CONDITIONAL_QUADRATIC_T3_SPECTRAL_GATE_WITH_EXPLICIT_WENGER_FAMILY",
       exact_source_finite_checks=cases,
       exact_all_order_formal_ledgers=ledgers,
       zero_one_regular_F_barriers_not_source_graphs=barriers,
       actual_Wenger_prime_field_sources=wenger_finite,
       published_Wenger_prime_power_symbolic=wenger_symbolic,
       direct_centered_spectral_family_ledgers=direct_ledgers,
       explicit_infinite_Wenger_nongq_quadratic_T3=wenger_quadratic_theorem_ledger(),
       exact_nontrivial_sixth_moment_proof=True,
       six_moment_scale_matches_Jensen_lower_bound=True,
       full_quadratic_without_a_spectral_gate_remains_OPEN=True,
       sixth_moment_condition_is_sufficient_not_necessary=True,
       real_positive_excess_infinite_family_from_published_Wenger=True,
       published_Wenger_spectral_theorem_is_prior_art=True,
       no_unrestricted_T3_or_ASET_claim=True,
       no_external_referee_or_Lean=True)


if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--out",default="gio003-g6d2-centered-sixth.json")
    args=p.parse_args()
    z=certificate()
    Path(args.out).write_text(json.dumps(z,sort_keys=True,indent=2)+"\n",
                              encoding="utf-8")
    print("PASS_GIO003_G6D2_CENTERED_SIXTH_MOMENT_CERTIFICATE")
