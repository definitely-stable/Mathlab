"""GIO-003 / G6-D1: cubic missing-projection singular polynomial.

Independently exact on ANY simple (s,t)-biregular original girth>=8
incidence source, not a GQ and not derived from a hidden GQ witness.

Crucial improvement: ||F||^2 <= Delta_L Delta_P instead of
||D|| <= (s+1)Delta_L. Hence intrinsic conflict O(r^4) and
corrected Gram O(r^(11/2)) up to Delta_L<=C*r^(3/2).
Conditional integrated HEAVY/LOW threshold ledger upgraded using
accepted source-independent G6-C3 proof; true external ordinary C6
constants remain existential; sample rational inputs FORMAL_ONLY.

An independent no-go excludes equal-order per-side Moore excess ONE.
This is not claimed novel against classic excess-2 graph literature.
"""
import argparse
import json
import random
from fractions import Fraction as Q
from collections import deque
from math import comb, gcd, isqrt
from pathlib import Path

from gio_t3c2_partial_books import make_model
from gio_t3c_intrinsic_defect import (
    defect_matrices, typed_conflicts_and_gram, direct_original_owner_conflicts,
)
from gio_t3c3_integrated_low import ceil, sqrt_ceil

SCHEMA="mathlab.gio003.g6d1.cubic-missing-projection.v1"
PARENT_G6C3="cc256e6147a3f267c9b11c35771de1ac9609e7ad"


def cube_ceil(n):
    if type(n) is not int or n<0:
        raise ValueError("nonnegative exact integer cube-root input required")
    lo=0;hi=1
    while hi**3<n:
        hi*=2
    while lo<hi:
        mid=(lo+hi)//2
        if mid**3<n:
            lo=mid+1
        else:
            hi=mid
    assert lo**3>=n
    assert lo==0 or (lo-1)**3<n
    return lo


def zeros(n,m):
    return [[0]*m for _ in range(n)]


def matmul(a,b):
    if len(a[0])!=len(b):
        raise ValueError("incompatible matrix dimensions")
    bt=list(zip(*b))
    return [[sum(x*y for x,y in zip(row,col)) for col in bt] for row in a]


def transpose(a):
    return list(map(list,zip(*a)))


def construct_missing_matrices(m):
    """Completely literal point-line F, without the G6-C1 missing list."""
    vp=m["points"];vl=len(m["lines"]);s=m["s"];t=m["t"]
    B=zeros(vp,vl)
    for ell,line in enumerate(m["lines"]):
        for p in line:
            B[p][ell]=1
    T=matmul(B,transpose(B))
    U=matmul(transpose(B),B)
    h=s+t
    three=matmul(T,B)
    F=[[1+h*B[p][ell]-three[p][ell] for ell in range(vl)]
       for p in range(vp)]
    if any(v not in (0,1) for row in F for v in row):
        raise AssertionError("original 3path NOT unique: source invalid")
    if any(F[p][ell] and B[p][ell] for p in range(vp) for ell in range(vl)):
        raise AssertionError("source missing mask on actual incidence")
    DL=vl-(t+1)*(s*t+1)
    DP=vp-(s+1)*(s*t+1)
    assert DL>=0 and DP>=0 and (s+1)*DL==(t+1)*DP
    assert all(sum(row)==DL for row in F)
    assert all(sum(F[p][ell] for p in range(vp))==DP for ell in range(vl))
    assert len({(p,ell) for p in range(vp) for ell in range(vl)
                if F[p][ell]})==vp*DL
    assert T==transpose(T) and U==transpose(U)
    return dict(B=B,F=F,T=T,U=U,delta_line=DL,delta_point=DP,
                vp=vp,vl=vl,s=s,t=t)


def polynomial_identity(mats):
    """Prove *all entries* of cubic point+dual matrix identities exactly.

    [T(T-hI)^2] = FF^T + (|L|-2 Delta_L)*J_P
    [U(U-hI)^2] = F^T F + (|P|-2 Delta_P)*J_L
    where T=BB^T, U=B^TB, and h=s+t.
    """
    B,F,T,U=mats["B"],mats["F"],mats["T"],mats["U"]
    vp,vl=mats["vp"],mats["vl"]
    h=mats["s"]+mats["t"]
    M=matmul(T,B)
    assert all(M[p][ell]-h*B[p][ell]==1-F[p][ell]
               for p in range(vp) for ell in range(vl))
    left=matmul(M,transpose(M))
    mcenter=[[M[p][ell]-h*B[p][ell] for ell in range(vl)] for p in range(vp)]
    assert mcenter==[[1-v for v in row] for row in F]
    for v,a,n,z,other in (
        ("point",T,vp,mats["delta_line"],vl),
        ("line",U,vl,mats["delta_point"],vp)):
        shifted=[[a[i][j]-h*(i==j) for j in range(n)] for i in range(n)]
        poly=matmul(matmul(a,shifted),shifted)
        X=F if v=="point" else transpose(F)
        XX=matmul(X,transpose(X))
        expected_add=other-2*z
        assert all(poly[i][j]==XX[i][j]+expected_add
                   for i in range(n) for j in range(n))
        assert all(XX[i][j]>=0 for i in range(n) for j in range(n))
    # Every projected 3path is read as 1-F off-incidence; no GQ completion.
    return dict(exact_point_and_line_cubic_identity=True,
        original_threewalk_matrix_identity=True,
        original_missing_F_row_sum=mats["delta_line"],
        original_missing_F_col_sum=mats["delta_point"],
        original_missing_F_support=sum(sum(row) for row in F),
        exact_dual_no_GQ_identity=True)


def centered_rayleigh(mats,seed=1043):
    """Test independent centered integer vectors, not floating eigensolvers."""
    r=random.Random(seed)
    FF=matmul(mats["F"],transpose(mats["F"]))
    FtF=matmul(transpose(mats["F"]),mats["F"])
    out={}
    for side,A,n in (("point",FF,mats["vp"]),("line",FtF,mats["vl"])):
        bound=mats["delta_line"]*mats["delta_point"]
        checks=0;max_ratio=Q(0)
        for v in (
                [1]+[-1]+[0]*(n-2),
                [1]+[0]*(n-2)+[-1],
                *[[n*x-sum(samples)
                    for x in samples]
                  for samples in ([r.randrange(-9,10) for _ in range(n)]
                                  for __ in range(12))]):
            assert sum(v)==0
            energy=sum(v[i]*A[i][j]*v[j]
                       for i in range(n) for j in range(n))
            norm=sum(x*x for x in v)
            assert 0<=energy<=bound*norm
            if norm:
                max_ratio=max(max_ratio,Q(energy,norm))
            checks+=1
        out[side]=dict(centered_integer_Rayleigh_checks=checks,
                       exact_norm_square_upper=bound,
                       max_observed_Rayleigh_ratio=str(max_ratio))
    return out


def cubic_bound_finite(mats):
    """Exact characteristic-root envelope on the centered B B^T spectrum.

    For ANY centered eigenvalue x>=0 of T, operator identity forces
    x(x-h)^2 <= Delta_L*Delta_P. If x>=2h, x^3/4<=product.
    All centered point-collinearity eigenvalues therefore have modulus
    <= 2h + (t+1) + ceil_cuberoot(4*Delta_L*Delta_P); true dual.
    """
    s,t=mats["s"],mats["t"]
    DL,DP=mats["delta_line"],mats["delta_point"]
    h=s+t
    z=DL*DP
    phi=cube_ceil(4*z)
    point_cap=2*h+t+1+phi
    line_cap=2*h+s+1+phi
    return dict(source_min_order=min(s,t),delta_line=DL,delta_point=DP,
                missing_operator_norm_squared_upper=z,
                cube_root_term=phi,point_centered_collinearity_cap=point_cap,
                line_centered_collinearity_cap=line_cap,
                exact_source_geometry_free_cubic_envelope=True)


def conflict_finite_gate(m,scheme):
    mats=construct_missing_matrices(m)
    polynomial_identity(mats)
    bound=cubic_bound_finite(mats)
    Dp,Dl,d=defect_matrices(m)
    pp=typed_conflicts_and_gram(m,m["f"],m["neighbors_point"],
                                Dp,m["s"],m["t"])
    ll=typed_conflicts_and_gram(m,m["g"],m["neighbors_line"],
                                Dl,m["t"],m["s"])
    kP=m["s"]*(m["t"]+1)
    kL=m["t"]*(m["s"]+1)
    assert pp["e_col"]<=kP*(m["aP"]-1)+bound["point_centered_collinearity_cap"]*m["points"]
    assert ll["e_col"]<=kL*(m["aL"]-1)+bound["line_centered_collinearity_cap"]*len(m["lines"])
    owners=direct_original_owner_conflicts(m,m)
    assert owners["J"]==pp["e_col"]+ll["e_col"]
    return dict(point=pp,line=ll,
                owners=owners,actual_cubic_bound=bound,
                tested_arbitrary_correlated_labels=scheme=="correlated")


def bounded_cubic_source_constants(b,C):
    if type(b) is not int or type(C) is not int or b<1 or C<0:
        raise ValueError("positive fixed b and nonnegative integer fixed C")
    v0=(b+1)*(b*b+1+C)
    n0=(b+1)*v0
    a0=2*v0+3
    A0=a0*a0
    k0=b*(b+1)
    theta0=b+2
    # DeltaP=(s+1)/(t+1)*DeltaL<= (b+1)*C*r^(3/2)
    # DeltaL*DeltaP <= (b+1)*C^2*r^3.
    root0=cube_ceil(4*(b+1)*C*C)
    lambda0=5*b+1+root0
    j0=k0*a0+lambda0*v0
    J0=2*j0
    G0=2*v0*k0+2*theta0*j0+2*(b+1)*v0*a0
    return dict(b=b,C=C,source_V0=v0,source_N0=n0,alphabet_a0=a0,
                physical_vertices_A0=A0,degree_k0=k0,theta0=theta0,
                cubic_root0=root0,spectral_Lambda0=lambda0,
                point_or_line_conflict_j0=j0,combined_owner_conflict_J0=J0,
                original_pencil_Gram_G0=G0)


def cubic_heavy_low_ledger(b=1,C=0,C0=Q(1),c0=Q(1)):
    """Self-contained exact all-order G6-C3 heavy/low constants with cubic A1.

    C0,c0 sample inputs are hypothetical / FORMAL_ONLY, NOT published
    numeric Simonovits values. This transfer is conditional on same
    accepted general HEAVY/LOW and exact G6-C2 source book inversion.
    """
    if type(C0) is not Q or type(c0) is not Q or C0<1 or not 0<c0<=1:
        raise ValueError("C0>=1 and 0<c0<=1 exact formal rationals only")
    a=bounded_cubic_source_constants(b,C)
    v0,n0,a0,A0=a["source_V0"],a["source_N0"],a["alphabet_a0"],a["physical_vertices_A0"]
    J0,G0=a["combined_owner_conflict_J0"],a["original_pencil_Gram_G0"]
    rho_cap=Q(1,32)
    K=16*J0+1
    core_coeff=Q(1,2)
    assert 1-Q(1,8)-rho_cap-Q(2*J0,K+1)>core_coeff
    R=512*A0*(1+64*J0)
    T=ceil(8*n0*R**3*C0**3)
    w=Q(8,A0*A0)
    q2=16*(K+1)**2
    q3=64*(K+1)**3
    Q0=8*n0+4*J0
    L6=1+ceil(36*n0*T*T)
    L4=q2*q2*sqrt_ceil(n0*L6)+Q0*T
    # Delta_L<=C*r^1.5 gives 4|P|DeltaL <=4v0C*r^4.5,
    # safely <=4v0C*r^5 for every r>=1.
    E0=4*(2*a0*v0+a0*a0)+4*n0+4*v0*C+8*b*J0
    E=q3*sqrt_ceil(E0*L6)
    BK=sqrt_ceil(16*(b+1)*n0*G0*(K+1)*T)
    D=4*sqrt_ceil(BK*T*L4)
    improper=3*T*Q0
    eps=w/8
    rho=min(rho_cap,eps*eps/Q(12*b*b*q3*q3*L6))
    delta=min(c0/Q(R**6),w/4)
    r0=max(2**32,ceil(Q(improper)/eps),
           ceil((Q(E)/eps)**2),ceil((Q(D)/eps)**8))
    assert 0<rho<=rho_cap and 0<delta<=w/4
    assert 12*b*b*rho*q3*q3*L6<=eps**2
    assert improper<=eps*r0
    assert E*E<=eps**2*r0
    assert D**8<=eps**8*r0
    return dict(schema=SCHEMA,FORMAL_ONLY=True,
        external_numeric_graph_C6_constants_NOT_proved=True,
        fixed_before_source=dict(balance_b=b,excess_C=C,
                                 external_C0=str(C0),external_c0=str(c0)),
        linear_source_gate_replaced_by="Delta_L^2 <= C^2*r^3",
        max_moore_excess_scale="C*r^(3/2)",
        source=a,selector=dict(K=K,R=R,T=T,w=str(w),q2=q2,q3=q3),
        moment=dict(Q0=Q0,L6=L6,L4=L4,E0=E0,E=E,
                    mixed_BK=BK,blocker_D=D,improper=improper,
                    distinct_Moore_hole_term="4|P|Delta_L <= 4*v0*C*r^(9/2)"),
        closure=dict(rho=str(rho),delta=str(delta),eps=str(eps),
                     sufficient_r0=str(r0),four_error_budgets_checked=True),
        conditional_theorem="INTRINSIC_T3_L3HALF_USING_ACCEPTED_HEAVY_LOW",
        no_GQ_or_template=True,no_full_unrestricted_T3=True,
        no_existing_positive_excess_infinite_family_asserted=True,
        no_independent_external_referee_or_Lean=True)


def validate_cubic_domain(s,t,DL,DP,deleted,ledger):
    if any(type(x) is not int for x in (s,t,DL,DP,deleted)):
        raise ValueError("source parameters must be exact integers")
    d=ledger["fixed_before_source"]
    b,C=d["balance_b"],d["excess_C"]
    r=min(s,t)
    if r<int(ledger["closure"]["sufficient_r0"]) or max(s,t)>b*r:
        raise ValueError("balance or all-order threshold failure")
    if DL<0 or DP<0 or (s+1)*DL!=(t+1)*DP:
        raise ValueError("Moore excess and degree balance failure")
    if DL*DL>C*C*r**3:
        raise ValueError("excess exceeds fixed C*r^(3/2)")
    if deleted<0 or deleted>Q(ledger["closure"]["rho"])*r**4:
        raise ValueError("deleted source originals exceed resilience radius")
    return True


def delta_one_equal_no_go(q):
    """No (q,q) source with per-part excess exactly ONE, any q>=2.

    If it existed, missing F would be a permutation matrix (each point
    missing one line, each line missing one point), so FF^T=I and for
    T=BB^T the centered cubic polynomial is:
       T(T-2qI)^2 = I.
    Pq(x)=x(x-2q)^2-1 is irreducible over Q for q>=2:
    the only rational-root candidates are ±1; neither is a root.
    Thus Pq must appear with equal 3-root multiplicity m=(V-1)/3
    in the characteristic polynomial of T restricted to 1^perp.
    But trace T on that subspace equals V(q+1)-(q+1)^2 while
    root sum 4q would imply 3*trace=4q(V-1).
    They disagree for all q>=2 (q=2 gap -3; q>=3 strictly negative).
    This is a self-contained special case of historical excess-2
    nonexistence: NO priority/novelty is claimed.
    """
    if type(q) is not int or q<2:
        raise ValueError("integer q>=2")
    V=(q+1)*(q*q+1)+1
    assert V==q**3+q*q+q+2
    P_at_1=(1-2*q)**2-1
    P_at_neg1=-(1+2*q)**2-1
    assert P_at_1!=0 and P_at_neg1!=0
    tr=V*(q+1)-(q+1)**2
    diff=3*tr-4*q*(V-1)
    assert diff<0,("nonexistence trace contradiction failed",q,diff)
    return dict(q=q,putative_vertices_per_side=V,
       possible_equal_cubic_irreducible_root_multiplicity=(V-1)//3,
       charpoly_degree_divisible_by_three=((V-1)%3==0),
       putative_centered_T_trace=tr,
       obligatory_cubic_roots_sum=4*q,
       exact_trace_discrepancy=diff,
       strict_trace_contradiction=True,
       no_equal_order_one_excess_girth8_source=True,
       prior_art_not_claimed_novel=True)


def necessary_small_excess_screen(s,t,DeltaL,DeltaP):
    """EXACT necessary integer conditions; does NOT construct a graph.

    Connectedness is FORCED when source has < 2 Moore components.
    A strict smaller-than-the-degree missing budget forces every
    same-type pair to have incidence distance <=4 and every cross-type
    pair to have distance <=5 (even before assuming connectivity).
    Both directions are only NECESSARY screens, not realization claims.
    """
    if any(type(z) is not int for z in (s,t,DeltaL,DeltaP)):
        raise ValueError("all source parameters must be integers")
    if min(s,t)<2 or DeltaL<0 or DeltaP<0:
        raise ValueError("thick simple source and nonnegative excess required")
    d=gcd(s+1,t+1)
    stepL=(t+1)//d
    stepP=(s+1)//d
    if (s+1)*DeltaL!=(t+1)*DeltaP:
        raise ValueError("degree-side incidence balance violated")
    assert DeltaL%stepL==0 and DeltaP%stepP==0
    level=DeltaL//stepL
    assert DeltaP//stepP==level
    MooreP=(s+1)*(s*t+1)
    MooreL=(t+1)*(s*t+1)
    VP=MooreP+DeltaP
    VL=MooreL+DeltaL
    cap=min(VP//MooreP,VL//MooreL)
    force_connected=(cap==1)
    force_same_type_distance_four=(DeltaL<=t and DeltaP<=s)
    return dict(s=s,t=t,delta_line=DeltaL,delta_point=DeltaP,
        excess_step_lines=stepL,excess_step_points=stepP,
        positive_excess_quantum=level,
        mandatory_total_source_vertices=VP+VL,
        Moore_points=MooreP,Moore_lines=MooreL,
        component_count_upper=cap,
        connectedness_forced_by_size=force_connected,
        diameter_at_most_five_if_actual_source=force_same_type_distance_four,
        actual_source_existence_NOT_proved=True)


def graph_distance_falsifier(m):
    """BFS literal original incidence, not a geometry/projection oracle."""
    P=m["points"];L=len(m["lines"])
    nbr=[set() for _ in range(P+L)]
    for ell,line in enumerate(m["lines"]):
        for p in line:
            nbr[p].add(P+ell)
            nbr[P+ell].add(p)
    unseen=set(range(P+L));components=[];maxdist=0
    while unseen:
        start=min(unseen)
        reach={start:0};todo=deque([start])
        while todo:
            p=todo.popleft()
            for z in nbr[p]:
                if z not in reach:
                    reach[z]=reach[p]+1
                    todo.append(z)
        components.append(len(reach))
        unseen.difference_update(reach)
        # Each connected component must be separately (s,t)-biregular
        # and meet the same Moore point/line lower bounds.
        nP=sum(x<P for x in reach)
        nL=len(reach)-nP
        assert nP>=(m["s"]+1)*(m["s"]*m["t"]+1)
        assert nL>=(m["t"]+1)*(m["s"]*m["t"]+1)
        for point in sorted(reach):
            dist={point:0};q=deque([point])
            while q:
                u=q.popleft()
                for v in nbr[u]:
                    if v not in dist:
                        dist[v]=dist[u]+1
                        q.append(v)
            assert len(dist)==len(reach)
            maxdist=max(maxdist,max(dist.values()))
    z=necessary_small_excess_screen(m["s"],m["t"],
                                    m["excess_lines"],m["excess_points"])
    assert len(components)<=z["component_count_upper"]
    if z["connectedness_forced_by_size"]:
        assert len(components)==1
    if z["diameter_at_most_five_if_actual_source"]:
        assert len(components)==1 and maxdist<=5
    return dict(actual_components=len(components),
        actual_component_sizes=components,
        actual_max_finite_distance=maxdist,
        size_enforced_connected=z["connectedness_forced_by_size"],
        size_enforced_diameter_at_most_five=z["diameter_at_most_five_if_actual_source"],
        literal_BFS_source_not_just_parameter_guess=True)


def finite_case(name,scheme="lex"):
    m=make_model(name,scheme)
    mats=construct_missing_matrices(m)
    identity=polynomial_identity(mats)
    center=centered_rayleigh(mats)
    feasible=necessary_small_excess_screen(m["s"],m["t"],
                        m["excess_lines"],m["excess_points"])
    distances=graph_distance_falsifier(m)
    conflict=conflict_finite_gate(m,scheme)
    b=(max(m["s"],m["t"])+min(m["s"],m["t"])-1)//min(m["s"],m["t"])
    r=min(m["s"],m["t"])
    # C is a per-fixture finite admissibility witness only.
    C=sqrt_ceil(Q(m["excess_lines"]**2,r**3))
    # This C is only a finite single-fixture envelope, never a family bound.
    assert m["excess_lines"]**2<=C*C*r**3
    constants=bounded_cubic_source_constants(b,C)
    assert conflict["owners"]["J"]<=constants["combined_owner_conflict_J0"]*r**4
    for z in ("point","line"):
        assert conflict[z]["gram"]**2<=constants["original_pencil_Gram_G0"]**2*r**11
    return dict(kind=name,scheme=scheme,source_s=m["s"],source_t=m["t"],
                points=m["points"],lines=len(m["lines"]),
                original_source_flags=len(m["flags"]),
                equal_order_positive_excess_vacuity_not_assumed=True,
                cubic_identity=identity,centered_Rayleigh=center,
                necessary_integer_feasibility=feasible,
                actual_source_BFS=distances,
                source_conflict=conflict["owners"],
                direct_cubic_bound=conflict["actual_cubic_bound"],
                checked_finite_b=b,checked_finite_C=C,
                explicit_source_constants=constants,
                finite_case_not_infinite_family=True)


def certificate():
    cases=[finite_case(*x) for x in (
       ("W32","lex"),("W33","lex"),("Qminus24","lex"),
       ("dualQminus42","lex"),("doubleW32","lex"),
       ("switchedDoubleW32","lex"),
       ("switchedDoubleW32","correlated"),
       ("Qminus24","correlated"))]
    formal=[cubic_heavy_low_ledger(b,C,C0,c0) for b,C,C0,c0 in (
       (1,0,Q(1),Q(1)),(1,1,Q(1),Q(1)),
       (2,2,Q(2),Q(1,2)),(3,5,Q(3),Q(1,3)))]
    no_go=[delta_one_equal_no_go(q) for q in (2,3,4,5,7,8,11,16)]
    return dict(schema=SCHEMA,issue=793,meta_issue=790,
      parent_G6C3_HEAD=PARENT_G6C3,
      fixed_balance_quadratic_excess_check="Delta_L^2 <= C^2*r^3",
      exact_finite_sources=cases,
      formal_half_integer_excess_ledgers=formal,
      equal_order_excess_one_nonexistence=no_go,
      no_hidden_nonGQ_existence_claim_in_arithmetic_screen=True,
      claim="CONDITIONAL_T3_EXCESS_O_R_THREE_HALVES_CUBIC_IDENTITY",
      local_cubic_identity_proved_without_GQ=True,
      arbitrary_minimal_factor_maps_uniform_spectral_gate=True,
      source_selector_moments_reused_from_G6C3=True,
      no_unrestricted_T3=True,
      no_infinite_nonGQ_half_integer_excess_family_constructed=True,
      no_Lean_or_independent_external_referee=True,
      no_numeric_external_C6_constants=True)


if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--out",default="gio003-g6d-cubic-missing-projection.json")
    v=p.parse_args()
    z=certificate()
    Path(v.out).write_text(json.dumps(z,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    print("PASS_GIO003_G6D_CUBIC_MISSING_PROJECTION_CERTIFICATE")
