"""HYP-105 AA4-CN: exact original GF5 two-fiber dual compatibility block ledger.

All-h genuine original W(3,2^h), arbitrary correlated complete globally
injected typed f,g, EIGHT genuine original POINT sources forming TWO physical
connected C6 sixpoint fibers with FOUR shared source POINT factors. On ONE
96-state global complete original f orbit G=S4(shared)×S2×S2, fixed full g:

  completion cherry: q=24 reachable labeled column duals per fiber,
    each appears four times, compatible A/B dual pairs: 48,
    each cooccurs twice in 96 global states.
  completion C4 switch: q=12 duals per fiber, each eight times,
    compatible pairs:24, each cooccurs four times.

In BOTH cases the unweighted bipartite dual compatibility matrix on
reachable duals is a disjoint union of (q/2) all-ones 2×2 blocks (K2,2),
rank q/2. This finite 96-orbit integer certificate applies all-h by
physical completion isomorphism; no original flag independence.

Let H_A/H_B count TRUE six-distinct original incidence IDs with source
POINT-A, source LINE-A, right physical connected C6, and right column
dual C reachable on the left global orbit. Define
  M = (sum H_A)(sum H_B)
  K = sum_{compatible C,D} H_A(C) H_B(D).
For exact historical selected GF5 all-seven source POINT-A FIBER scores
  F_i(x)=B_i+5643 H_i(C_i(x)), B_i source right B/C fixed,
their covariance on ONE 96-map full f orbit is exactly
  Cov(F_A,F_B)=5643^2 * ((q/2)*K - M) / q^2.

True original incident Q-pair overlap k=0..4 gives finer exact sum:
 M=Σ_k M_k, K=Σ_k K_k,
 Cov=5643²/q² * Σ_k ((q/2)K_k-M_k).
The B/C invariant baseline CANNOT compensate this covariance; only
other historical D6 original Q pair contributions can. This does not
claim all-h global fixed-map S_s lower or all-seven cancellation.
"""
from collections import Counter, defaultdict
from fractions import Fraction

from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4ci_dual_cycle_orbit_fiber_invariant import (
    W_D, _six_position_dual_cycle,
)
from hyp105_issue230_d6aa4cl_shared_four_point_fibers_covariance import (
    GRAPH_CASES, FAMILIES, ORBIT, _cov, original_two_fiber_same_global_96_orbit,
    genuine_original_two_fiber_fixture,
)
from hyp105_issue230_d6aa4cm_negative_original_named_pair_covariance import (
    true_original_negative_D6_pair_fixture,
)
from hyp105_issue230_d6aa4cl_shared_four_point_fibers_covariance import (
    complete_overlapping_global_f,
)
from hyp105_issue230_d6aa4cg_four_shared_edge_two_completion import (
    classify_seven_all_a_original_Q,
)

CASES={"vertex_replacement":(24,4,2,12),
       "four_cycle_switch":(12,8,4,6)}


def _canon_cycle(c):
    return tuple(sorted(tuple(sorted(e)) for e in c))


def exact_original_dual_96_compatibility(case):
    """Exhaustively certify both 96-state canonical completion geometries."""
    if case not in CASES:
        raise ValueError("known 4-common-original-POINT physical C6 completion required")
    q,preimage,multiplicity,nblocks=CASES[case]
    shared,exclusive_A,exclusive_B=GRAPH_CASES[case]
    edges=tuple(shared+exclusive_A+exclusive_B)
    joint=Counter()
    left=Counter();right=Counter()
    for sigma,alpha,beta in ORBIT:
        f=tuple(edges[sigma[i]] for i in range(4))+(
            edges[4+alpha],edges[5-alpha],edges[6+beta],edges[7-beta])
        cA=_six_position_dual_cycle(tuple(f[i] for i in FAMILIES["A"]))
        cB=_six_position_dual_cycle(tuple(f[i] for i in FAMILIES["B"]))
        if cA is None or cB is None:
            raise AssertionError("ONE globally injected f should keep both physical C6 families")
        left[cA]+=1;right[cB]+=1;joint[(cA,cB)]+=1
    if len(ORBIT)!=96 or len(left)!=q or len(right)!=q:
        raise AssertionError("96-map source dual orbit support wrong")
    if set(left.values())!={preimage} or set(right.values())!={preimage}:
        raise AssertionError("each original incidence-column dual orbit count not constant")
    if len(joint)!=2*q or set(joint.values())!={multiplicity}:
        raise AssertionError("both dual compatibility numbers/multiplicity wrong")
    graph={}
    for a,b in joint:
        graph.setdefault(("A",a),set()).add(("B",b))
        graph.setdefault(("B",b),set()).add(("A",a))
    if len(graph)!=2*q or any(len(neigh)!=2 for neigh in graph.values()):
        raise AssertionError("two regular degree-two original dual compatibility graph required")
    seen=set();components=[]
    for node in graph:
        if node in seen:continue
        stack=[node];seen.add(node);current=set()
        while stack:
            u=stack.pop();current.add(u)
            for v in graph[u]:
                if v not in seen:
                    seen.add(v);stack.append(v)
        A={u[1] for u in current if u[0]=="A"}
        B={u[1] for u in current if u[0]=="B"}
        if len(A)!=2 or len(B)!=2 or any((a,b) not in joint for a in A for b in B):
            raise AssertionError("every original dual coacceptance component must be K2,2")
        components.append((frozenset(A),frozenset(B)))
    if len(components)!=nblocks:
        raise AssertionError("all-original 96-map compatibility blocks expected q/2")
    return {
       "case":case,"dual_types_each":q,
       "preimages_per_dual_in_96":preimage,
       "compatible_dual_pairs":len(joint),
       "incompatible_dual_pairs":q*q-len(joint),
       "number_of_K2_2_blocks":len(components),
       "binary_compatibility_matrix_rank":len(components),
       "joint_states_per_compatible_dual_pair":multiplicity,
       "entire_96_state_joint_counter":dict(joint),
       "reachable_A_duals":frozenset(left),
       "reachable_B_duals":frozenset(right),
       "blocks":tuple(components),
       "covariance_compatible_coefficient":Fraction(q,2),
       "covariance_exact_scale":Fraction(W_D*W_D,q*q),
       "all_h_genuine_source_eligible_when_both_physical_C6":True,
    }


def _true_original_D6_orbit_active_Q(fiber,reachable):
    """Only original Q eligible as historical D6 on at least one whole f state."""
    out=[]
    for original_Q,right_kind,cycle in fiber["eligible_actual_original_Q"]:
        if right_kind=="D6_cyclic" and cycle in reachable:
            out.append((tuple(original_Q),cycle))
    if len(out)!=sum(fiber["right_cyclic_dual_hist"].get(c,0) for c in reachable):
        raise AssertionError("original 6-ID source D6 reachable histogram mismatch")
    return tuple(out)


def original_twofiber_pairwise_D6_compensation_ledger(model,point_ids):
    """Exact TRUE original sixflag-Q pair block sign, under SAME complete 96 f maps."""
    z=original_two_fiber_same_global_96_orbit(model,point_ids)
    cert=exact_original_dual_96_compatibility(z["genuine_four_shared_edge_type"])
    fam=z["original_histograms"]
    candidates={
        "A":_true_original_D6_orbit_active_Q(fam["A"],cert["reachable_A_duals"]),
        "B":_true_original_D6_orbit_active_Q(fam["B"],cert["reachable_B_duals"]),
    }
    # Every original source POINT-A sixflag Q is an IMMUTABLE original
    # six-distinct incidence-ID key. Pair overlap counts true original
    # incidence IDs, never coincident physical edge labels.
    sourceA=candidates["A"];sourceB=candidates["B"]
    M_k=Counter();K_k=Counter()
    K=0
    compatible=cert["entire_96_state_joint_counter"]
    for QA,ca in sourceA:
        sa=set(QA)
        for QB,cb in sourceB:
            intersection=len(sa.intersection(QB))
            if not 0<=intersection<=4:
                raise AssertionError("two different original six-POINT source sets share at most four original incidences")
            M_k[intersection]+=1
            if (ca,cb) in compatible:
                K+=1;K_k[intersection]+=1
    M=len(sourceA)*len(sourceB)
    if sum(M_k.values())!=M or sum(K_k.values())!=K:
        raise AssertionError("true original pairwise overlap ledger not exhaustive")
    q=cert["dual_types_each"]
    coeff=q//2
    whole_cov=Fraction(W_D*W_D*(coeff*K-M),q*q)
    if whole_cov!=z["historical_score_covariance_A_B"]:
        raise AssertionError("full true original historical GF5 twofiber signed covariance != integer compatible Q pair census")
    signed_by_original_Q_intersection={
        k:coeff*K_k[k]-M_k[k] for k in range(5)}
    if sum(signed_by_original_Q_intersection.values())!=coeff*K-M:
        raise AssertionError("true original Q-intersection signed cancellation mismatch")
    # Invariant historical B/C weighted GF5 score (source LINE B/C)
    # varies by neither shared nor exclusive POINT factor permutations,
    # hence cannot change any covariance, even though its positive
    # contribution is part of each full accepted 7-class fiber score.
    return {
        "s":z["s"],"V":z["V"],"a":z["a"],
        "completion_case":cert["case"],
        "original_eight_POINT_sources":tuple(point_ids),
        "original_sixflag_Q_fiber_size_each":z["original_Q_fiber_size_each"],
        "right_original_D6_Q_active_A":len(sourceA),
        "right_original_D6_Q_active_B":len(sourceB),
        "original_Q_active_records_A":sourceA,
        "original_Q_active_records_B":sourceB,
        "physical_compatibility_certificate":cert,
        "M_all_original_D6_Q_pairs":M,
        "K_compatible_original_D6_Q_pairs":K,
        "M_minus_K_incompatible_original_D6_Q_pairs":M-K,
        "M_by_number_shared_TRUE_original_incidence_IDs":dict(M_k),
        "K_by_number_shared_TRUE_original_incidence_IDs":dict(K_k),
        "signed_coefficient_by_TRUE_original_Q_incidence_overlap":signed_by_original_Q_intersection,
        "exact_invariant_historical_BC_baseline_A":fam["A"]["original_baseline_B_C_weighted"],
        "exact_invariant_historical_BC_baseline_B":fam["B"]["original_baseline_B_C_weighted"],
        "exact_original_twofiber_GF5_covariance":whole_cov,
        "reported_original_twofiber_covariance":z["historical_score_covariance_A_B"],
        "same_complete_global_original_f_and_unchanged_g":True,
        "only_original_rightA_D6_incidence_pairs_create_covariance":True,
        "full_original_GQ_S_s_NOT_COMPUTED":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


def original_AA4CM_negative_named_and_full_ledger(power):
    """Original W34 vs W38: fix SAME 12-source-LINE witness then count all active Q."""
    f=true_original_negative_D6_pair_fixture(power)
    ledger=original_twofiber_pairwise_D6_compensation_ledger(
        f["actual_original_model"],f["eight_REAL_original_POINT_source_ids"])
    Q_A=f["QA_six_true_original_incidence_IDs"]
    Q_B=f["QB_six_true_original_incidence_IDs"]
    LA={q:cycle for q,cycle in ledger["original_Q_active_records_A"]}
    LB={q:cycle for q,cycle in ledger["original_Q_active_records_B"]}
    if Q_A not in LA or Q_B not in LB:
        raise AssertionError("true original selected negative Q absent from entire D6 compatible-Q census")
    if (LA[Q_A],LB[Q_B]) in ledger["physical_compatibility_certificate"]["entire_96_state_joint_counter"]:
        raise AssertionError("AA4-CM true original 12-source selected negative pair became compatible")
    # EXACT old observed distinctions, avoid all-h extrapolating them.
    expected=Fraction(-10614483,32) if power==2 else Fraction(0)
    if ledger["exact_original_twofiber_GF5_covariance"]!=expected:
        raise AssertionError("original W34 negative versus W38 zero full-family contradiction")
    return {"source_original":f,"pairwise":ledger,
            "negative_selected_original_Q_covariance":Fraction(-W_D*W_D,576),
            "complete_original_twofiber_covariance":expected,
            "no_universal_all_h_sign_inference":True}
