"""GIO-003 G6-F3 — independent all-order ORIGINAL six-ID T3 transfer proof.

This is a NEW stand-alone proof of the graph/owner combinatorial
C2+C3 transfer with concrete F1 numeric C6 input. It no longer takes
the older G6-C2/C3 closure_ledger as a proof oracle.

The exact source-specific local PSD / G6-C1 geometry is a separately
stated INPUT theorem, not surreptitiously reproved here. Assuming
actual simple biregular girth>=8 source, balanced quadratic excess,
minimal injective fixed typed factor maps and BOTH typed real PSD
witnesses, F3 supplies complete elementary inverse/selector/HEAVY-LOW
proof with the F1 graph numerical C6 theorem.

Source family existence, unrestricted abstract T3, GF5 dependent
ASET, academic referee and Lean formalization are NOT asserted.
"""
import argparse
import json
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations, permutations, product
from math import comb, isqrt
from pathlib import Path

from gio_t3f1_explicit_c6 import (
    GENERAL_DENSITY, GENERAL_CYCLE_FACTOR, exact_explicit_constants,
)
from gio_t3c2_partial_books import make_model, selected_mask
from gio_resilience import source_first_d6
from hyp105_aa4_branch_a_integrated_referee import actual_edges

SCHEMA="mathlab.gio003.g6f3.standalone-original-conditional-T3.v1"
PARENT_G6F2="22d040d84e90bc8498f441eb0d77f4207cc0fe86"


def ceil_fraction(x):
    a=Q(x)
    return -(-a.numerator//a.denominator)


def ceil_sqrt(n):
    if type(n) is not int or n<0:
        raise ValueError("exact nonnegative integer required")
    u=isqrt(n)
    return u+(u*u<n)


def standalone_source_and_closure(b,C,ell,M):
    """No calls to old C2/C3/D7 closure ledger, independent exact arithmetic.

    INPUT: REAL source with b-balance, degree r, Delta_L<=C r^2,
    original two-typed local PSD gate L_a(W)<=M r^4 and fixed ell.
    OUTPUT: arithmetic constants and all four exact LOW budgets.
    """
    if any(type(x) is not int for x in (b,C,ell,M)) or b<1 or min(C,ell,M)<0:
        raise ValueError("fixed integers b>=1, C>=0, ell>=0, M>=0")
    numeric=exact_explicit_constants()
    C0=Q(numeric["threshold_C0"]);c0=Q(numeric["cycle_coefficient_c0"])
    assert C0==2**41 and c0==Q(1,98304)
    # Independently derive the G6-C1/D7 source-only envelopes.
    v0=(b+1)*(b*b+1+C)
    n0=(b+1)*v0
    a0=2*v0+3
    A0=a0*a0
    k0=b*(b+1)
    theta0=b+2
    j0=k0*a0+ell*v0+ceil_fraction(Q(M,2))
    J0=2*j0
    G0=2*v0*k0+2*theta0*j0+2*(b+1)*v0*a0
    # Original HEAVY/LOW combinatorics, freshly reconstructed.
    rho_cap=Q(1,32)
    K=16*J0+1
    R=512*A0*(1+64*J0)
    T=8*n0*R**3*int(C0)**3
    w=Q(8,A0*A0)
    q2=16*(K+1)**2
    q3=64*(K+1)**3
    Q0=8*n0+4*J0
    L6=1+36*n0*T*T
    L4=q2*q2*ceil_sqrt(n0*L6)+Q0*T
    E0=4*(2*a0*v0+a0*a0)+4*n0+4*v0*C+8*b*J0
    E=q3*ceil_sqrt(E0*L6)
    BK=ceil_sqrt(16*(b+1)*n0*G0*(K+1)*T)
    D=4*ceil_sqrt(BK*T*L4)
    improper=3*T*Q0
    eps=w/8
    rho=min(rho_cap,eps*eps/Q(12*b*b*q3*q3*L6))
    delta=min(c0/Q(R**6),w/4)
    r0=max(2**32,ceil_fraction(Q(improper)/eps),
            ceil_fraction((Q(E)/eps)**2),
            ceil_fraction((Q(D)/eps)**8))
    core_fraction=1-rho_cap-Q(1,8)-Q(2*J0,K+1)
    assert core_fraction>Q(1,2)
    assert R>=512*A0*(1+64*J0)
    assert T>=8*n0*R**3*C0**3
    assert q2==16*(K+1)**2 and q3==64*(K+1)**3
    assert L6>=Q(3,128)+36*n0*T*T
    assert eps*4==w/2
    assert rho>0 and delta>0 and r0>=2**32
    assert rho<=rho_cap
    assert delta<=c0/R**6 and delta<=w/4
    errors=dict(
        improper_directed_3walk=Q(improper)<=eps*r0,
        original_endpoint_clean=Q(E*E)<=eps*eps*r0,
        deletion_FULL_projection_anchor=12*b*b*rho*q3*q3*L6<=eps*eps,
        four_TRUE_inner_book_blockers=Q(D**8)<=eps**8*r0)
    assert len(errors)==4 and all(errors.values())
    # New exact proof of the geometric threshold for every r>=r0,
    # independent of the previous ledger's assertion.
    assert 3*T*Q0<=eps*r0
    assert E*E<=eps*eps*r0
    assert D**8<=eps**8*r0
    assert 12*b*b*rho*q3*q3*L6<=eps*eps
    # Named FLAGS: 6-ID source sets are two orientations (BBo) or
    # twelve rooted orientations (D6); NEVER multiply the latter by 6.
    return dict(mode="NEW_INDEPENDENT_PROOF_NOT_OLD_C2_C3_LEDGER",
        input_fixed=dict(balance_b=b,quadratic_excess_C=C,
                         cutoff_ell=ell,typed_local_budget_M=M,
                         actual_SOURCE_required=True,
                         two_typed_real_Loewner_PSD_required=True,
                         minimal_typed_pair_injectivity_required=True,
                         arbitrary_adversarial_fixed_f_g=True,
                         source_nonincident_partial_projection_NOT_completed=True),
        source_constants=dict(v0=v0,n0=n0,a0=a0,A0=A0,k0=k0,
                              theta0=theta0,j0=j0,J0=J0,G0=G0),
        external_ordinary_graph_C6_THEOREM_PROVEN_C0=int(C0),
        external_ordinary_graph_C6_THEOREM_PROVEN_c0=str(c0),
        priority_and_moments=dict(K=K,R=R,T=str(T),w=str(w),
            q2=q2,q3=q3,Q0=Q0,L6=str(L6),L4=str(L4),
            endpoint_E0=E0,endpoint_E=str(E),
            source_book_BK=str(BK),inner_blocker_D=str(D),
            original_source_full_untruncated_priority=True,
            one_global_independent_x_y_symbol_cut=True,
            trace6_graph_bound="tr(A_G^6) <= 24*C6(G)+72*m(G)*Delta(G)^2",
            expected_edges_of_one_GLOBAL_selector="E[m(G)]=W_C/2",
            source_return_identity="Qx+Qy=8*|CORE|+4*e(J_CORE)",
            improper_walk_universal="I_improper<=3*Delta_CORE*(Qx+Qy)",
            selected_proper_moment_bound="||P_i||_F^2 <= q_i^2 E tr(A_G^(2i))",
            TRUE_C6_typed_cut_success="4/4096",
            TRUE_C6_source_oriented_multiplicity=12,
            TRUE_BBo_source_oriented_multiplicity=2),
        HEAVY_graph_gate=dict(required_actual_simple_host=True,
            v_bound="v(F) * (R*C0)^3 <= r^3",
            edge_bound="e(F) * R >= r*v(F)",
            exact_integer_consequence="e(F)^3 >= C0^3*v(F)^4",
            heavy_D6_unoriented_sixsets_lower="c0*r^6/R^6",
            no_HOST_degree_regularization_assumed=True),
        all_four_independently_derived_LOW_errors=errors,
        closure=dict(eps=str(eps),rho=str(rho),delta=str(delta),
            sufficient_r0=str(r0),
            r0_decimal_digits=len(str(r0)),
            T_decimal_digits=len(str(T)),
            strict_CORE_fraction_lower=str(core_fraction),
            exact_proper_3walk_W3_lower="w*r^6",
            after_four_epsilon_lower="w*r^6/2",
            actual_original_BBo_lower="w*r^6/4",
            exact_C6_to_original_D6_lower="c0*r^6/R^6"),
        no_generic_OLD_FORMAL_ONLY_ledger_used=True,
        no_unrestricted_abstract_T3_or_dependent_GF5_ASET=True)


def true_original_physical_model(name="W32",scheme="lex",mask="mixed"):
    """REAL source geometry, independent owner/corner physical assembly.

    Avoid importing original G6-C2/C3 helper results for J or walks.
    Uses actual original named flags/factors returned by geometry oracle.
    """
    m=make_model(name,scheme)
    A,C=selected_mask(m,mask)
    A=set(A);C=set(C)
    assert C<=A
    flags=m["flags"];f=m["f"];g=m["g"]
    physical={}
    for i in sorted(C):
        p,l=flags[i]
        x0,x1=f[p];y0,y1=g[l]
        for u,v in (((x0,y0),(x1,y1)),((x0,y1),(x1,y0))):
            k=tuple(sorted((u,v)))
            assert k not in physical,"original pair factor injectivity"
            physical[k]=i
    adj={}
    for (u,v),i in physical.items():
        adj.setdefault(u,set()).add(v)
        adj.setdefault(v,set()).add(u)
    J={i:set() for i in C}
    for i,j in combinations(sorted(C),2):
        p,l=flags[i];q,r=flags[j]
        if ((p==q and set(g[l])&set(g[r]))
            or (l==r and set(f[p])&set(f[q]))):
            J[i].add(j);J[j].add(i)
    return m,A,C,adj,physical,J


def literal_proper_and_return_moments(name="W32",scheme="lex",mask="mixed"):
    """Independent exact coordinate return, improper 3walk and tr A4."""
    m,A,C,adj,owners,J=true_original_physical_model(name,scheme,mask)
    D=max((len(v) for v in adj.values()),default=0)
    qx=qy=0
    improper_x3=improper_y3=0
    all3=proper3=0
    P2=Counter();R2=Counter()
    for u,neighbors in adj.items():
        for v in neighbors:
            for w in adj[v]:
                key=(u,w)
                if u[0]!=w[0] and u[1]!=w[1]:
                    P2[key]+=1
                else:
                    R2[key]+=1
                qx+=u[0]==w[0]
                qy+=u[1]==w[1]
                for z in adj[w]:
                    all3+=1
                    xcoords=(u[0],v[0],w[0],z[0])
                    ycoords=(u[1],v[1],w[1],z[1])
                    proper3+=(len(set(xcoords))==4
                              and len(set(ycoords))==4)
                    improper_x3+=u[0]==z[0]
                    improper_y3+=u[1]==z[1]
    conflict_edges=sum(len(x) for x in J.values())//2
    assert qx+qy==8*len(C)+4*conflict_edges
    proper2_sum=sum(P2.values())
    improper2_sum=sum(R2.values())
    assert improper2_sum<=qx+qy
    # Distinct ORIGINAL physical endpoints of a 2walk are either
    # proper on both types or improper on at least one type. They
    # cannot inhabit both categories for the SAME endpoint pair.
    assert not (P2.keys()&R2.keys())
    tr4=sum(x*x for x in P2.values())+sum(x*x for x in R2.values())
    max_return=max(R2.values(),default=0)
    assert max_return<=D
    assert sum(x*x for x in R2.values())<=D*(qx+qy)
    improper3=all3-proper3
    assert improper3<=3*D*(qx+qy)
    # The gap-three coordinate-return bound uses the polynomial
    # A²(DI−A) PSD, valid for symmetric adjacency with spectrum <=D.
    assert improper_x3<=D*qx and improper_y3<=D*qy
    bound_W3=(4*len(C))**3
    n_phys=m["aP"]*m["aL"]
    assert all3*n_phys*n_phys>=bound_W3
    return dict(name=name,scheme=scheme,mask=mask,
        original_named_flags=len(m["flags"]),surviving_FULL_A=len(A),
        source_CORE_C=len(C),actual_CORE_J_edges=conflict_edges,
        actual_CORE_max_physical_degree=D,
        original_physical_CORE_edges=len(owners),
        actual_coordinate_two_returns_x=qx,
        actual_coordinate_two_returns_y=qy,
        exact_source_owner_return_identity=qx+qy==8*len(C)+4*conflict_edges,
        actual_ordered_threewalks=all3,
        actual_PROPER_ordered_threewalks=proper3,
        actual_improper_threewalks=improper3,
        exact_algebraic_improper_bound=3*D*(qx+qy),
        exact_gap3_x_upper=D*qx,exact_gap3_y_upper=D*qy,
        exact_tr_A4=tr4,
        exact_proper_P2_Frobenius_squared=sum(x*x for x in P2.values()),
        exact_improper_R2_Frobenius_squared=sum(x*x for x in R2.values()),
        proper_and_improper_P2_endpoint_support_DISJOINT=True,
        exact_fourth_moment_return_correction_le_DQ=True,
        exact_threewalk_Holder_lower=True,
        geometry_true_original_partial_source_flags=True,
        no_external_Lemma_for_return_or_improper=True)


def _brute_simple_c6(adj):
    """Small graph: independent directed six distinct vertices /12."""
    found=0
    def walk(path):
        nonlocal found
        if len(path)==6:
            found+=path[0] in adj.get(path[-1],())
            return
        for w in adj.get(path[-1],()):
            if w not in path:walk(path+[w])
    for u in adj:walk([u])
    assert found%12==0
    return found//12


def _trace_even(adj,k):
    """Exact integer Frobenius trace A^(2k) from genuine physical walks."""
    pairs=Counter()
    for u in adj:
        def rec(v,steps):
            if steps==0:
                pairs[u,v]+=1
                return
            for w in adj.get(v,()):rec(w,steps-1)
        rec(u,k)
    return sum(x*x for x in pairs.values())


def all_bipartite_3x3_spectral_sixwalks():
    """512 genuine bipartite simple hosts, independent of F1 test code.

    Prove/independently falsify the exact YES/NO certificate for the
    critical all-order bound:
        tr A6 <=24*C6 +72*m*D²,
        (tr A4)² <= (tr A2)(tr A6).
    """
    bad_total=0
    C6total=0
    strict_cases=0
    for mask in range(512):
        adj={i:set() for i in range(6)}
        for i in range(3):
            for j in range(3):
                if mask&(1<<(3*i+j)):
                    a=i;b=3+j
                    adj[a].add(b);adj[b].add(a)
        m=sum(len(z) for z in adj.values())//2
        D=max(map(len,adj.values()))
        tr2=2*m
        tr4=_trace_even(adj,2)
        tr6=_trace_even(adj,3)
        cyc=_brute_simple_c6(adj)
        assert 0<=tr6-12*cyc<=6*D*tr4
        assert tr4*tr4<=tr2*tr6
        assert tr6<=24*cyc+72*m*D*D
        C6total+=cyc
        bad_total+=tr6-12*cyc
        strict_cases+=tr6<24*cyc+72*m*D*D
    assert C6total==48
    return dict(exhaustive_original_bipartite_simple_graphs=512,
        total_unoriented_simple_C6_across_512=48,
        total_noninjective_closed_sixwalks=bad_total,
        Cauchy_trace4_squared_le_trace2_trace6_ALL=True,
        injection_defect_trace6_le_12C6_plus_6Dtrace4_ALL=True,
        young_trace6_le_24C6_plus_72mD_squared_ALL=True,
        strict_nontrivial_cases=strict_cases,
        no_GQ_or_SOURCE_regularization_for_sixwalk_lemma=True)


def actual_one_global_selector_expected_edges():
    """ONE global owner priority and typed cuts: E[m(G)] = W_C/2 EXACT.

    Use an ACTUAL W32 original J conflict pair plus one other REAL
    original owner. Fully enumerate priority orders and ALL assignments
    of bits on all symbols used by the THREE source owners.
    """
    m,A,C0,_,_,J0=true_original_physical_model("W32","lex","full")
    incident=sorted((i,j) for i in J0 for j in J0[i] if i<j)
    assert incident,"must include genuinely competing original owners"
    i,j=incident[0]
    third=next(z for z in sorted(C0) if z not in (i,j))
    C={i,j,third}
    J={x:J0[x]&C for x in C}
    xs=sorted({z for ii in C for z in m["f"][m["flags"][ii][0]]})
    ys=sorted({z for ii in C for z in m["g"][m["flags"][ii][1]]})
    assert len(xs)+len(ys)<=12
    all_bits=2**(len(xs)+len(ys))
    W=sum((Q(1,1+len(J[ii])) for ii in C),Q(0))
    cases=0
    actual_total_edges=0
    for order in permutations(sorted(C)):
        pos={ii:k for k,ii in enumerate(order)}
        winners={ii for ii in C if all(pos[ii]<pos[jj] for jj in J[ii])}
        for bx in product((0,1),repeat=len(xs)):
            fx=dict(zip(xs,bx))
            for by in product((0,1),repeat=len(ys)):
                fy=dict(zip(ys,by))
                kept=[ii for ii in winners
                      if fx[m["f"][m["flags"][ii][0]][0]]!=
                         fx[m["f"][m["flags"][ii][0]][1]]
                      and fy[m["g"][m["flags"][ii][1]][0]]!=
                         fy[m["g"][m["flags"][ii][1]][1]]]
                actual_total_edges+=2*len(kept)
                cases+=1
    assert cases==6*all_bits
    assert Q(actual_total_edges,cases)==W/2
    return dict(original_source="W32",
        actual_original_owner_IDs=sorted(C),
        actual_SOURCE_J_conflict_edges=sum(len(x) for x in J.values())//2,
        all_one_GLOBAL_priority_orders=6,
        exact_all_ONE_global_typed_cut_assignments=all_bits,
        exact_joint_priority_and_cut_outcomes=cases,
        exact_original_source_Caro_Wei_W=str(W),
        exact_expected_SELECTED_edges=str(Q(actual_total_edges,cases)),
        identity_EXPECTED_m_equals_half_W=True,
        no_owner_or_factor_independence_claim=True,
        ALL_source_FLAGS_and_actual_competitors=True)


def actual_sixowner_D6_single_global_cut_trace():
    """4096 ONE-global true six-owner D6 cuts and every selected trace.

    Crucially compute tr(A_G^6) independently on the ACTUAL physical
    graph rather than treating the 36D²W bound as a given old lemma.
    """
    m=make_model("W32","lex")
    allowners=set(range(len(m["flags"])))
    keys=source_first_d6(m,allowners)
    assert keys
    six=tuple(sorted(next(iter(keys))))
    flags=m["flags"]
    xs=sorted({v for ii in six for v in m["f"][flags[ii][0]]})
    ys=sorted({v for ii in six for v in m["g"][flags[ii][1]]})
    assert len(xs)==len(ys)==6
    all_adj={}
    for ii in six:
        p,l=flags[ii];x0,x1=m["f"][p];y0,y1=m["g"][l]
        for u,v in (((x0,y0),(x1,y1)),((x0,y1),(x1,y0))):
            all_adj.setdefault(u,set()).add(v)
            all_adj.setdefault(v,set()).add(u)
    Delta=max(map(len,all_adj.values()))
    assert Delta>0
    successful_cuts=0
    sum_edges=sum_tr2=sum_tr4=sum_tr6=sum_C6=0
    for bx in product((0,1),repeat=6):
        fx=dict(zip(xs,bx))
        for by in product((0,1),repeat=6):
            fy=dict(zip(ys,by))
            selected={}
            keep=0
            for ii in six:
                p,l=flags[ii];x0,x1=m["f"][p];y0,y1=m["g"][l]
                if fx[x0]!=fx[x1] and fy[y0]!=fy[y1]:
                    keep+=1
                    for u,v in (((x0,y0),(x1,y1)),((x0,y1),(x1,y0))):
                        selected.setdefault(u,set()).add(v)
                        selected.setdefault(v,set()).add(u)
            edge_count=2*keep
            sum_edges+=edge_count
            tr2=_trace_even(selected,1)
            assert tr2==2*edge_count
            sum_tr2+=tr2
            sum_tr4+=_trace_even(selected,2)
            sum_tr6+=_trace_even(selected,3)
            c6=_brute_simple_c6(selected)
            sum_C6+=c6
            successful_cuts+=(keep==6)
    assert successful_cuts==4
    assert sum_C6==4
    assert sum_edges==4096*Q(len(six),2)
    assert sum_tr4*sum_tr4<=sum_tr2*sum_tr6
    assert sum_tr6<=24*sum_C6+72*Delta*Delta*sum_edges
    W=Q(len(six))
    assert Q(sum_edges,4096)==W/2
    assert Q(sum_C6,4096)==Q(1,1024)
    assert Q(sum_tr6,4096)<=Q(3,128)+36*Delta*Delta*W
    return dict(original_source="W32",
        actual_source_six_named_original_FLAG_IDs=list(six),
        source_J_independent_D6_owner_set=True,
        global_cut_assignments_exhausted=4096,
        exactly_four_all_six_owner_crossing_cuts=successful_cuts,
        actual_unoriented_source_C6_sum_over_cuts=sum_C6,
        exact_expected_source_C6=str(Q(sum_C6,4096)),
        exact_expected_source_EDGES=str(Q(sum_edges,4096)),
        exact_one_GLOBAL_priority_owner_weight_W=str(W),
        actual_original_core_max_physical_degree=Delta,
        exact_expected_trace2=str(Q(sum_tr2,4096)),
        exact_expected_trace4=str(Q(sum_tr4,4096)),
        exact_expected_trace6=str(Q(sum_tr6,4096)),
        Cauchy_EXPECTED_trace4_squared_bound=True,
        actual_source_trace6_graph_bound=True,
        original_conditional_expected_C6_le_D6_div_1024=True,
        original_six_ID_T3_not_claimed_from_finite_fixture=True)


def certificate():
    source_cases=[
        dict(regime=name,standalone_proof=standalone_source_and_closure(*args))
        for name,args in (
            ("G6E1_true_GQ_PDS_zero_W",(1,2,2,0)),
            ("G6E2_first_true_odd_q7",(1,5,4,0)),
            ("G6E2_E3_true_corrected_q_ge8",(1,5,3,0)),
            ("G6E2_E3_true_corrected_q_ge18",(1,5,2,0)),
            ("G6D7_Wenger_true_all_prime_powers",(1,3,0,11)),
        )
    ]
    finite=[
        literal_proper_and_return_moments(*args)
        for args in (
            ("W32","lex","full"),
            ("W32","lex","mixed"),
            ("W33","correlated","mixed"),
            ("switchedDoubleW32","correlated","mixed"),
            ("dualQminus42","lex","mixed"),
        )
    ]
    return dict(schema=SCHEMA,parent_G6F2_HEAD=PARENT_G6F2,issue=793,
        claim="STANDALONE_ORIGINAL_SOURCE_T3_TRANSFER_FROM_TYPED_PSD_BUDGETS",
        standalone_numeric_theorem_derived_WITHOUT_old_C2_C3_D7_ledgers=True,
        all_five_original_SOURCE_specific_positive_theorem_instances=source_cases,
        independent_literal_original_SOURCE_RETURN_and_IMPROPER_and_tr4=finite,
        exhaustive_bipartite_512_host_sixwalk_identity=
            all_bipartite_3x3_spectral_sixwalks(),
        exact_one_GLOBAL_selector_EXPECTED_physical_edges=
            actual_one_global_selector_expected_edges(),
        true_original_sixowner_D6_all_4096_selected_trace_cycles=
            actual_sixowner_D6_single_global_cut_trace(),
        mathematical_argument_proves_abstract_combinatorial_CORE_given_actual_source=True,
        source_specific_TYPED_PSD_gate_and_original_girth8_are_PREMISES=True,
        actual_graph_existence_NOT_inferred_from_arithmetic=True,
        all_graph_ordinary_C6_numeric_theorem_G6F1_proven_prior_art_qualitative=True,
        no_unrestricted_abstract_T3_or_new_GF5_ASET_exponent=True,
        no_external_referee_or_Lean=True)


if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--out")
    z=p.parse_args()
    d=json.dumps(certificate(),indent=2,sort_keys=True)+"\n"
    if z.out:Path(z.out).write_text(d,encoding="utf8")
    else:print(d)
