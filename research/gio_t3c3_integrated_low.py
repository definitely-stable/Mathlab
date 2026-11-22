"""GIO-003/G6-C3 integrated all-order intrinsic HEAVY/LOW ledger.

Input: exact G6-C1 spectral/defect and G6-C2 original FULL/CORE
three-corner blocker lemmas, and the SAME global owner-priority/coherent
cut selector with its six-walk moment lemma from accepted #230/#799.

The bound is for any ACTUAL (s,t)-biregular girth>=8 source with
FIXED balance b and FIXED LINEAR Moore excess Delta_L <= C*r.
No GQ-template, field or full projection assumption.

External ordinary graph C6 supersaturation constants C0,c0 remain
EXISTENTIAL. Numeric sample ledgers are FORMAL_ONLY; no infinite
non-GQ positive-small-excess existence is asserted.
"""
import argparse
import json
import random
from collections import Counter,defaultdict
from fractions import Fraction as Q
from itertools import permutations,product
from math import isqrt
from pathlib import Path

from gio_t3c2_partial_books import (
    make_model, selected_mask, original_source_conflict_degrees,
    full_core_book, fourblocker_triple_injection, endpoint_mask,
    manual_produced_bbo,
)
from gio_t3c_intrinsic_defect import (
    defect_matrices, typed_conflicts_and_gram, spectral_cap,
    coarse_linear_excess_ledger,
)
from hyp105_aa4_branch_a_integrated_referee import actual_edges,physical_d6
from gio_resilience import source_first_d6

SCHEMA="mathlab.gio003.g6c3.intrinsic-low-closure.v1"
PARENT_C1="8932e4c76c2d04c3e1c15f7f56f15a50a7d8f918"
PARENT_C2="bc82adeef2574c1985cca49b786d3b3447f1758d"


def ceil(x):
    v=Q(x)
    return -(v.numerator//-v.denominator)


def sqrt_ceil(x):
    v=ceil(x)
    if v<0:
        raise ValueError("square root of negative rational")
    s=isqrt(v)
    return s+(s*s<v)


def external_constants(C0,c0):
    """Fail closed: these are *formal* bounding parameters, not observed."""
    if type(C0) is not Q or type(c0) is not Q:
        raise ValueError("require explicit exact rational external graph parameters")
    if C0<1 or not (0<c0<=1):
        raise ValueError("C0>=1 and 0<c0<=1 required")
    return C0,c0


def closure_ledger(b=1,C=0,C0=Q(1),c0=Q(1)):
    """Fixed-order all-step arithmetic, directly from original hypotheses.

    This is an implication for every real admissible published C6 pair
    C0>=C_graph, c0<=c_graph; default sample numbers are NOT certified.
    """
    if type(b) is not int or type(C) is not int or b<1 or C<0:
        raise ValueError("b>=1,C>=0 must be fixed integers before source")
    external_constants(C0,c0)
    v0=(b+1)*(b*b+1+C)
    n0=(b+1)*v0
    a0=2*v0+3
    A0=a0*a0
    k0=b*(b+1)
    theta0=b+2
    lambda0=theta0+(b+1)*(b+C)
    j0=k0*a0+lambda0*v0
    J0=2*j0
    G0=2*v0*k0+2*theta0*j0+2*(b+1)*v0*a0

    # HEAVY: source flags survive any |Z|<=rho_cap*r^4, original owner
    # independent set has size >= r^4/[32(1+64 J0)].
    rho_cap=Q(1,32)
    K=16*J0+1
    c=Q(1,2)
    core_before_rho=1-Q(1,8)-rho_cap-Q(2*J0,K+1)
    assert core_before_rho>c
    R=512*A0*(1+64*J0)
    T=ceil(8*n0*R**3*C0**3)
    assert T>=8*n0*R**3*C0**3
    w=(4*c)**3/Q(A0*A0)
    assert w==Q(8,A0*A0)
    assert R>=512*A0*(1+64*J0)

    # The ONE shared priority-on-original-owner + coherent global typed
    # symbol-cut selector: q_i=4^i(K+1)^i. Its moment inequalities are
    # inherited from the merged #799 LOW core, with no GQ premise.
    q2=16*(K+1)**2
    q3=64*(K+1)**3
    Q0=8*n0+4*J0
    L6=1+ceil(36*n0*T*T)
    L4=q2*q2*sqrt_ceil(n0*L6)+Q0*T

    # New intrinsic projection defect enters here ONLY:
    # 4|P|Delta_L <=4*v0*C*r^4 <=4*v0*C*r^5.
    E0=4*(2*a0*v0+a0*a0)+4*n0+4*v0*C+8*b*J0
    E=q3*sqrt_ceil(E0*L6)
    BK=sqrt_ceil(16*(b+1)*n0*G0*(K+1)*T)
    D=4*sqrt_ceil(BK*T*L4)
    improper=3*T*Q0

    eps=w/8
    rho=min(rho_cap,eps*eps/Q(12*b*b*q3*q3*L6))
    delta=min(c0/Q(R**6),w/4)
    r0=max(2**32,ceil(Q(improper)/eps),
           ceil((Q(E)/eps)**2),
           ceil((Q(D)/eps)**8))
    assert rho>0 and delta>0 and r0>=2**32
    assert 12*b*b*rho*q3*q3*L6<=eps*eps
    assert improper<=eps*r0
    assert E*E<=eps*eps*r0
    assert D**8<=eps**8*r0
    assert eps*4==w/2
    assert delta<=w/4
    assert delta<=c0/Q(R**6)
    assert (4*c)**3/Q(A0*A0)==w

    return dict(schema=SCHEMA,FORMAL_ONLY=True,
       fixed_before_source=dict(balance_b=b,line_excess_C=C,
                                external_C0=str(C0),external_c0=str(c0)),
       published_graph_numeric_constants_not_supplied=True,
       hypotheses=dict(thick_integer_order=True,simple_source=True,
                        biregular_source=True,girth_at_least_8=True,
                        delta_line_upper="C*r",
                        fixed_physical_alphabet="two separate minimal pair alphabets",
                        arbitrary_complete_injective_factor_maps=True,
                        independent_sampling_of_factor_maps=False,
                        GQ_witness_required=False),
       envelopes=dict(V0=v0,N0=n0,a0=a0,A0=A0,k0=k0,theta0=theta0,
           Lambda0=lambda0,collinearity_j0=j0,owner_J0=J0,pencil_G0=G0),
       selector=dict(rho_cap=str(rho_cap),K=K,T=str(T),
           cut_path_q2=q2,cut_path_q3=q3,
           one_global_owner_priority=True,one_global_typed_symbol_cut_pair=True,
           independent_reselection_per_path=False,
           normalized_C6_cut_probability="1/1024",
           W_C_bound="sum 1/(1+d_JC(i)) <= N",
           HEAVY_R=R,LOW_C_core_lower=str(c),
           LOW_3walk_lower=str(w),
           strict_core_before_cap=str(core_before_rho)),
       moment=dict(Q0=Q0,L6=L6,L4=L4,
           corrected_Moore_holes_coefficient=4*v0*C,
           endpoint_E0=E0,endpoint_clean_E=E,
           source_full_core_BK=BK,physical_fourblocker_D=D,
           improper_coefficient=improper),
       closure=dict(rho=str(rho),delta=str(delta),eps=str(eps),
           sufficient_integer_r0=str(r0),
           HEAVY_D6_lower="c0*r^6/R^6",
           LOW_proper_3walk_lower="w*r^6",
           LOW_improper_upper="3*T*Q0*r^5",
           LOW_clean_endpoint_upper="E*r^(11/2)",
           LOW_deleted_anchor_upper="q3*sqrt(12*b^2*rho*L6)*r^6",
           LOW_inner_blockers_upper="D*r^(47/8)",
           total_four_epsilon_upper="w/2",
           LOW_produced_BBo_lower="w*r^6/4",
           arithmetic_gates_validated=True,
           no_independent_graph_C6_numeric_radius=True),
       proof_dependencies=[
         "merged_230_799_global_owner_priority_coherent_cuts",
         "G6C1_intrinsic_defect_and_conflict_spectra",
         "G6C2_partial_original_projection_and_fourblocker_triple_injection",
         "published_ordinary_graph_C6_supersaturation_existential"],
       label="DERIVED_CONDITIONAL_INTRINSIC_T3_LINEAR_MOORE_EXCESS",
       no_infinite_nonGQ_linear_excess_family_claim=True,
       no_unrestricted_T3_without_small_excess=True,
       no_unrestricted_ASET_exponent=True,
       no_external_human_referee_or_Lean=True)


def validate_ledger_domain(s,t,delta_line,deleted,record):
    """Pure symbolic integer-domain guard. Does not synthesize a giant graph."""
    if any(type(x) is not int for x in (s,t,delta_line,deleted)):
        raise ValueError("integer source order/excess/deletion counts only")
    info=record["fixed_before_source"]
    b,C=info["balance_b"],info["line_excess_C"]
    r=min(s,t)
    if r<int(record["closure"]["sufficient_integer_r0"]):
        raise ValueError("below formal all-order threshold")
    if max(s,t)>b*r or delta_line<0 or delta_line>C*r:
        raise ValueError("outside fixed balance and linear-excess family")
    if deleted<0 or deleted>Q(record["closure"]["rho"])*r**4:
        raise ValueError("outside adversarial original flag deletion budget")
    if not record["closure"]["arithmetic_gates_validated"]:
        raise AssertionError("unverified proof ledger")
    return True


def owner_conflict_graph(m,ids):
    fs=m["flags"];ids=set(ids)
    adj={i:set() for i in ids}
    for i in sorted(ids):
        p,l=fs[i]
        for j in sorted(ids):
            if j<=i:
                continue
            q,r=fs[j]
            share=((p==q and bool(set(m["g"][l]) & set(m["g"][r])))
                   or (l==r and bool(set(m["f"][p]) & set(m["f"][q]))))
            if share:
                adj[i].add(j);adj[j].add(i)
    return adj


def actual_physical_degrees(m,ids):
    adj,own=actual_edges(m,ids)
    return adj,own,{v:len(nbr) for v,nbr in adj.items()}


def frozen_heavy_low_core(m,A,physical_threshold,K):
    """Reconstruct original FULL-flag LOW core; DO NOT recompute projection."""
    if type(physical_threshold) is not int or physical_threshold<0:
        raise ValueError("nonnegative integer physical degree threshold required")
    if type(K) is not int or K<0:
        raise ValueError("nonnegative integer conflict cap required")
    full=frozenset(range(len(m["flags"])))
    if not set(A)<=full:
        raise ValueError("A must contain only original named source flags")
    adjacency,owners,deg=actual_physical_degrees(m,full)
    heavy={v for v,d in deg.items() if d>physical_threshold}
    edge_touched={e:i for e,i in owners.items() if set(e)&heavy}
    edge_count=len(edge_touched)
    owner_touched=set(edge_touched.values())
    conflict=owner_conflict_graph(m,full)
    hot={i for i in full if len(conflict[i])>K}
    C=frozenset(set(A)-owner_touched-hot)
    jC=owner_conflict_graph(m,C)
    hc,_,dc=actual_physical_degrees(m,C)
    assert all(x<=K for x in map(len,jC.values()))
    assert all(x<=physical_threshold for x in dc.values())
    assert len(C)>=len(full)-(len(full)-len(A))-edge_count-len(hot)
    assert len(hot)*(K+1)<=sum(len(x) for x in conflict.values())
    J_full=sum(map(len,conflict.values()))//2
    assert len(hot)<=2*J_full//(K+1)
    assert len(C)>=len(full)-(len(full)-len(A))-edge_count-(2*J_full//(K+1))
    return dict(C=C,frozen_full_heavy_count=len(heavy),
        full_heavy_touching_edges=edge_count,
        owners_removed_by_heavy=len(owner_touched),
        full_high_conflict_owners=len(hot),
        FULL_source_owner_J_edges=J_full,
        actual_CORE_max_physical_degree=max(dc.values(),default=0),
        actual_CORE_max_J=max(map(len,jC.values()),default=0),
        counted_initial_source=len(full),
        surviving_original_A=len(A),
        actual_CORE_size=len(C))


def counted_walks(adj,length,proper=False):
    """Literal ordered physical walks, even if graph itself non-bipartite."""
    out=defaultdict(int)
    for start in adj:
        def rec(path):
            if len(path)==length+1:
                if (not proper or (len({v[0] for v in path})==len(path)
                                   and len({v[1] for v in path})==len(path))):
                    out[path[0],path[-1]]+=1
                return
            for next_vertex in adj[path[-1]]:
                rec(path+[next_vertex])
        rec([start])
    return dict(out)


def trace_even(adj,i):
    """tr(A^(2i)) = sum_uv (# ordered physical iwalks u->v)^2."""
    n=counted_walks(adj,i,False)
    return sum(x*x for x in n.values())


def coordinate_returns(adj):
    """Two independent typed projections of literal length-two walks."""
    x=y=0
    for u in adj:
        for v in adj[u]:
            for w in adj[v]:
                x+=(u[0]==w[0])
                y+=(u[1]==w[1])
    return x,y


def walk_and_selector_finite(name="W32",scheme="lex",mask="full",threshold=2,K=3):
    m=make_model(name,scheme)
    A,_=selected_mask(m,mask)
    core=frozen_heavy_low_core(m,A,threshold,K)
    C=core["C"]
    h,_,d=actual_physical_degrees(m,C)
    j=owner_conflict_graph(m,C)
    qx,qy=coordinate_returns(h)
    eJ=sum(map(len,j.values()))//2
    assert qx+qy==8*len(C)+4*eJ
    # No GQ / no field / no random selected geometry used here.
    W3=sum(len(h[u])*len(h[v]) for u in h for v in h[u])
    product_alphabet=m["aP"]*m["aL"]
    assert W3*product_alphabet**2 >= (4*len(C))**3
    P2=counted_walks(h,2,True)
    P3=counted_walks(h,3,True)
    tr4=trace_even(h,2)
    blocker=fourblocker_triple_injection(m,A,C)
    for v in blocker["positions"].values():
        assert v["actual_proper_blocked_paths"]**2<=v["exact_Cauchy_inner_blocker_upper_squared"]
    if C:
        # One shared global owner priority and one pair of global
        # symbol cut functions; test many deterministic adversarial seeds.
        for seed in (0,1,7,31):
            rng=random.Random(seed+len(C)+m["s"]*101)
            order=list(C);rng.shuffle(order)
            rank={i:j for j,i in enumerate(order)}
            minima={i for i in C if all(rank[i]<rank[k] for k in j[i])}
            for i in minima:
                assert not (minima & j[i])
            bitx={x:rng.randint(0,1) for x in range(m["aP"])}
            bity={y:rng.randint(0,1) for y in range(m["aL"])}
            keep={i for i in minima
                  if bitx[m["f"][m["flags"][i][0]][0]] !=
                     bitx[m["f"][m["flags"][i][0]][1]]
                  and bity[m["g"][m["flags"][i][1]][0]] !=
                      bity[m["g"][m["flags"][i][1]][1]]}
            selected,_,_=actual_physical_degrees(m,keep)
            for u in selected:
                for v in selected[u]:
                    assert bitx[u[0]]!=bitx[v[0]]
                    assert bity[u[1]]!=bity[v[1]]
            observed_all=physical_d6(m,keep,rainbow_only=False)
            observed_proper=physical_d6(m,keep,rainbow_only=True)
            assert observed_all==observed_proper
    return dict(kind=name,scheme=scheme,mask=mask,
       source_s=m["s"],source_t=m["t"],
       original_source_flags=len(m["flags"]),
       A_remaining_flags=len(A),LOW_core=len(C),
       frozen_heavy_edges=core["full_heavy_touching_edges"],
       FULL_high_conflict_owners=core["full_high_conflict_owners"],
       physical_vertex_alphabet_product=product_alphabet,
       original_CORE_J_edges=eJ,
       coordinate_return_Qx=qx,coordinate_return_Qy=qy,
       return_formula_exact=True,
       physical_core_max_degree=max(d.values(),default=0),
       threewalks_all=W3,
       ordered_proper_two_walker_total=sum(P2.values()),
       ordered_proper_three_walker_total=sum(P3.values()),
       exact_walk_Jensen_lower=True,
       actual_uncut_trace_A4=tr4,
       actual_inner_blocker_bound_four_positions=True,
       shared_priority_and_two_global_cuts_checked=bool(C),
       source_partial_projection_not_completed=True)


def exact_coherent_cut_path_probability(name="W32"):
    """Exhaustive 4^i coherent typed cut for a real proper i-edge path.

    Select the three proper path's named owners only; these original
    owners are pairwise nonadjacent in the source conflict graph.
    Every cut assignment is enumerated, NOT Monte Carlo.
    """
    m=make_model(name)
    allids=frozenset(range(len(m["flags"])))
    H,owner=actual_edges(m,allids)
    witness=None
    for u in sorted(H):
        if witness is not None:
            break
        for v in sorted(H[u]):
            for w in sorted(H[v]):
                for z in sorted(H[w]):
                    path=(u,v,w,z)
                    if len({x for x,y in path})!=4 or len({y for x,y in path})!=4:
                        continue
                    ids=tuple(owner[tuple(sorted(edge))] for edge in zip(path,path[1:]))
                    if len(set(ids))==3:
                        witness=(path,ids)
                        break
                if witness:
                    break
            if witness:
                break
    assert witness is not None
    path,ids=witness
    assert len(set(ids))==3
    assert all(not val for val in owner_conflict_graph(m,ids).values())

    out={}
    for length in (2,3):
        v=path[:length+1]
        required=ids[:length]
        xs=sorted({p[0] for p in v})
        ys=sorted({p[1] for p in v})
        assert len(xs)==len(ys)==length+1
        count=0
        total=2**(2*(length+1))
        for xb in product((0,1),repeat=length+1):
            bitsx=dict(zip(xs,xb))
            for yb in product((0,1),repeat=length+1):
                bitsy=dict(zip(ys,yb))
                if all(bitsx[v[i][0]]!=bitsx[v[i+1][0]]
                       and bitsy[v[i][1]]!=bitsy[v[i+1][1]]
                       for i in range(length)):
                    count+=1
        assert count*4**length==total
        out[str(length)]=dict(exact_cut_success=count,
            exact_assignments=total,exact_probability=f"1/{4**length}",
            independent_owner_priority_success_probability="1",
            literal_original_distinct_owners=True)
    return dict(kind=name,source_owner_ids=ids,proper_witness=path,
                cut_probabilities=out,
                full_global_selection_not_replaced_by_pathwise_cuts=True)


def exact_shared_competitor_priority_certificate():
    """All 5! global priority orders: local winner events are NOT independent.

    Three desired named owners (0,1,2) have no internal J edges,
    but share two actual potential competitor IDs 3,4. This is a
    deliberately correlated local-minimum example; the valid bound is
    product(1/(d_i+1)), not multiplication of true event probabilities.
    """
    edges=((0,3),(0,4),(1,3),(1,4),(2,3))
    graph={i:set() for i in range(5)}
    for i,j in edges:
        graph[i].add(j);graph[j].add(i)
    desired={0,1,2}
    assert all(not (graph[i]&desired) for i in desired)
    success=0
    for order in permutations(range(5)):
        position={v:p for p,v in enumerate(order)}
        if all(all(position[i]<position[j] for j in graph[i])
               for i in desired):
            success+=1
    p=Q(success,120)
    product_floor=Q(1,3)*Q(1,3)*Q(1,2)
    assert p>=product_floor and p>product_floor
    return dict(source="five_named_owners_shared_competitors",
                exact_all_priority_orders=120,
                exact_simultaneous_local_minima_orders=success,
                exact_probability=str(p),
                independent_event_product_lower=str(product_floor),
                shared_competitor_correlation_nontrivial=True,
                all_priorities_are_ONE_global_order=True)


def exact_threeowner_shared_cut_moments(name="W32"):
    """Exhaustive ONE global cut on a real 3-owner proper physical path.

    For independent original owners the local-min priority retains all;
    enumerate physical G over every shared typed bit assignment, and
    verify the genuine Frob(P2/P3)^2 <= q_i^2 E trace(A_G^(2i))
    on this source, not a separate cut per queried path.
    """
    m=make_model(name)
    witness=exact_coherent_cut_path_probability(name)
    ids=tuple(witness["source_owner_ids"])
    J=owner_conflict_graph(m,ids)
    assert all(len(x)==0 for x in J.values())
    H,_=actual_edges(m,ids)
    xs=sorted({symbol for i in ids for symbol in m["f"][m["flags"][i][0]]})
    ys=sorted({symbol for i in ids for symbol in m["g"][m["flags"][i][1]]})
    assert len(xs)==len(ys)==4
    cuts=2**(len(xs)+len(ys))
    sum_tr4=0;sum_tr6=0
    event_count=0
    for bx in product((0,1),repeat=len(xs)):
        xbits=dict(zip(xs,bx))
        for by in product((0,1),repeat=len(ys)):
            ybits=dict(zip(ys,by))
            keep=set()
            for i in ids:
                p,l=m["flags"][i]
                xx=m["f"][p];yy=m["g"][l]
                if xbits[xx[0]]!=xbits[xx[1]] and ybits[yy[0]]!=ybits[yy[1]]:
                    keep.add(i)
            selected,_=actual_edges(m,keep)
            for u in selected:
                for v in selected[u]:
                    assert xbits[u[0]]!=xbits[v[0]]
                    assert ybits[u[1]]!=ybits[v[1]]
            sum_tr4+=trace_even(selected,2)
            sum_tr6+=trace_even(selected,3)
            event_count+=(len(keep)==3)
    assert event_count*64==cuts
    p2=counted_walks(H,2,True)
    p3=counted_walks(H,3,True)
    fro2=sum(x*x for x in p2.values())
    fro3=sum(x*x for x in p3.values())
    assert fro2*cuts<=16**2*sum_tr4
    assert fro3*cuts<=64**2*sum_tr6
    return dict(kind=name,independent_original_owners=3,
        enumerated_one_global_typed_cut_assignments=cuts,
        all_three_original_owners_preserved_cut_count=event_count,
        cut_probability_three_owner="1/64",
        exact_original_proper_P2_Frobenius_square=fro2,
        exact_original_proper_P3_Frobenius_square=fro3,
        sum_selected_true_trace_A4_over_all_cuts=sum_tr4,
        sum_selected_true_trace_A6_over_all_cuts=sum_tr6,
        same_global_selector_moment_inequalities_exact=True,
        no_pathwise_resampling=True)


def exact_d6_cut_probability(name="W32"):
    """One original D6 -> exactly 4 valid coherent cuts among 2^12."""
    m=make_model(name)
    D=source_first_d6(m,frozenset(range(len(m["flags"]))))
    assert D
    key=next(iter(sorted(D)))
    physical=physical_d6(m,key)
    assert len(physical)==1
    path=next(iter(physical.values()))
    xs=sorted({z[0] for z in path})
    ys=sorted({z[1] for z in path})
    assert len(xs)==len(ys)==6
    valid=0
    for xb in product((0,1),repeat=6):
        bx=dict(zip(xs,xb))
        for yb in product((0,1),repeat=6):
            by=dict(zip(ys,yb))
            if all(bx[path[i][0]]!=bx[path[(i+1)%6][0]]
                   and by[path[i][1]]!=by[path[(i+1)%6][1]]
                   for i in range(6)):
                valid+=1
    assert valid==4
    return dict(kind=name,original_six_source_ID_count=6,
                exact_favorable_typed_cut_assignments=valid,
                exact_total_typed_cut_assignments=2**12,
                probability_reduced="1/1024",no_independent_cuts_per_cycle=True)


def certificate():
    ledgers=[closure_ledger(b,C,C0,c0)
        for b,C,C0,c0 in ((1,0,Q(1),Q(1)),
                          (1,1,Q(1),Q(1)),
                          (2,2,Q(2),Q(1,2)),
                          (3,5,Q(3),Q(1,3)))]
    finite=[walk_and_selector_finite(*args)
        for args in (("W32","lex","full",2,3),
            ("W32","lex","mixed",2,3),
            ("W33","lex","mixed",3,4),
            ("Qminus24","lex","mixed",3,4),
            ("dualQminus42","lex","mixed",3,4),
            ("doubleW32","lex","full",2,3),
            ("switchedDoubleW32","lex","mixed",2,3),
            ("switchedDoubleW32","correlated","mixed",3,4),
            ("W32","lex","empty_core",1,1),
            ("W32","lex","full",100,100),
            ("W33","lex","mixed",100,100),
            ("Qminus24","lex","mixed",100,100),
            ("switchedDoubleW32","correlated","mixed",100,100))]
    return dict(schema=SCHEMA,parent_issue=793,meta_issue=790,
       parent_G6C1_HEAD=PARENT_C1,parent_G6C2_HEAD=PARENT_C2,
       exact_formal_ledgers=ledgers,
       finite_global_core_falsifiers=finite,
       local_coherent_cut_probability=exact_coherent_cut_path_probability(),
       local_D6_coherent_cut_probability=exact_d6_cut_probability(),
       exact_threeowner_same_global_selected_moments=exact_threeowner_shared_cut_moments(),
       shared_competitor_global_priority=exact_shared_competitor_priority_certificate(),
       claim="CONDITIONAL_INTRINSIC_T3_LINEAR_EXCESS_HEAVY_LOW_CLOSED",
       no_claim_external_C6_numeric_constants=True,
       no_infinite_nonGQ_linear_excess_existence=True,
       no_unrestricted_incidence_T3=True,
       no_general_ASET_exponent=True,
       no_external_human_referee_or_Lean=True)


if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--out",default="gio003-g6c3-integrated-low-closure.json")
    args=p.parse_args()
    z=certificate()
    Path(args.out).write_text(json.dumps(z,sort_keys=True,indent=2)+"\n",
                              encoding="utf-8")
    print("PASS_GIO003_G6C3_INTRINSIC_INTEGRATED_LEDGER")
