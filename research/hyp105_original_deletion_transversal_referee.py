"""AA4-DELTRANS: complete finite ORIGINAL W(3,2) six-motif deletion frontier.

A source-first, exact and independent fixed-map referee of the #674
ORIGINAL deletion and #726 source-disjoint palette theorem interfaces.
This DOES NOT prove #674 universal dyadic all-map theorem, whose heavy
physical-degree and mixed FULL/CORE blockers have separate prerequisites.

Independently classify ALL historical left-six-coordinate original W32
sixsets as actual D6 or B/B-overlap, directly reconstructing complete
12 physical coordinate dual incidences, original point/line multiplicity,
and original column-ID matching. Cross-check full accepted source hyperedge
set against the separate, previously accepted seven-family classifier.

Compute EXACT minimum ORIGINAL flag hitting set tau and EXACT max
six-ORIGINAL-ID-disjoint packing nu, with replayable lex-branch exhaustive
UNSAT at tau-1 and a size-tau witness; verify every deletion Z of size
up to 4 by full census of survived original hyperedges, not sampled Z.
A source-ID-deletion is not a palette assignment or a physical-coordinate
deletion and must not be misreported as an R3/coding upper bound.

NEW all-N binomial stochastic-domination theorem:
for t ORIGINAL-ID-disjoint accepted D6/BBo sixsets, each ten-sign union
is an independent original-GF5 event of probability p_i>=q10; therefore
the random palette Hamming repair distance d satisfies
 P(d<r) <= P(Binomial(t,q10)<r)
for every positive INTEGER r. This exact finite integer-tail bound
strengthens the prior Chernoff summary in #726. All-h t=Omega(s^4)
remains conditional on unaccepted #674 geometric source deletion result.
"""
from collections import Counter,defaultdict
from functools import lru_cache
from fractions import Fraction
from itertools import combinations
from math import comb
import json

Q_TEN=Fraction(53526,51**6)
ROOT_ISSUE=230
ROOT_STATUS="OPEN_WITH_FORMAL_BLOCKER"


def _six_original_mask(ids,n):
    ids=tuple(ids)
    if (len(ids)!=6 or len(set(ids))!=6 or
        any(type(i) is not int or i<0 or i>=n for i in ids)):
        raise ValueError("six DISTINCT genuine original incidence flag IDs")
    return sum(1<<i for i in ids)


def _full_half_dual(column_factor_ids,pairs):
    """Return independent true-original six-ID physical coordinate dual.

    Each original source flag's point/line has one globally fixed K_a edge.
    The resulting six ORIGINAL columns must touch exactly six physical
    coordinate symbols twice each. Return six source-column dual edges.
    """
    degree=defaultdict(list)
    for j,factor in enumerate(column_factor_ids):
        label=pairs[factor]
        if (len(label)!=2 or label[0]==label[1]):
            raise ValueError("true original source physical pairs must be proper")
        for x in label:degree[x].append(j)
    if len(degree)!=6 or any(len(ids)!=2 for ids in degree.values()):
        return None
    return tuple(sorted(tuple(sorted(ids)) for ids in degree.values()))


def _connected_original_dual_sixcycle(dual):
    if dual is None or len(dual)!=6 or len(set(dual))!=6:
        return False
    adjacent={i:set() for i in range(6)}
    for u,v in dual:
        adjacent[u].add(v);adjacent[v].add(u)
    found={0};fringe=[0]
    for i in fringe:
        for j in sorted(adjacent[i]-found):
            found.add(j);fringe.append(j)
    return len(found)==6 and all(len(adjacent[i])==2 for i in range(6))


def independent_true_six_motif(ids,flags,f,g):
    """Independent from historical classify_seven_prechecked; exact source."""
    ids=tuple(sorted(ids))
    if len(ids)!=6 or len(set(ids))!=6:
        raise ValueError("exactly six distinct ORIGINAL source flags")
    points=tuple(flags[i][0] for i in ids)
    lines=tuple(flags[i][1] for i in ids)
    LD=_full_half_dual(points,f)
    RD=_full_half_dual(lines,g)
    if LD is None or RD is None:return None
    P=Counter(points);L=Counter(lines)
    if sorted(P.values())==[1]*6 and sorted(L.values())==[1]*6:
        if LD==RD and _connected_original_dual_sixcycle(LD):
            return "D6"
    if sorted(P.values())==[1,1,1,1,2] and sorted(L.values())==[1,1,1,1,2]:
        doubled_left={k for k in range(6) if P[points[k]]==2}
        doubled_right={k for k in range(6) if L[lines[k]]==2}
        if len(doubled_left&doubled_right)==1:
            return "B/B-overlap"
    return None


def original_W32_hypergraph(scheme):
    if scheme not in ("lex","reverse-line"):
        raise ValueError("only original W(3,2) complete pinned maps")
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
    from hyp105_g5e2b3e1a_fixed_leading import selected_left_six
    from hyp105_g5e2b3e1b0_seven_signature import (
        seven_census,classify_seven_prechecked)
    m=pair_labeled_symplectic(1,scheme)
    flags=m["incidences"]
    if (m["s"]!=2 or m["N"]!=45 or len(flags)!=45 or
        len(set(flags))!=45 or len(set(m["left_labels"]))!=15 or
        len(set(m["right_labels"]))!=15):
        raise AssertionError("not true original symplectic W32 factor model")
    real=[]
    scanned=0
    for ids,_ in selected_left_six(m):
        scanned+=1
        tag=independent_true_six_motif(
            ids,flags,m["left_labels"],m["right_labels"])
        historical=classify_seven_prechecked(
            ids,m["left_labels"],m["right_labels"],flags)
        actual=(historical if historical in ("D6","B/B-overlap") else None)
        if tag!=actual:
            raise AssertionError("genuine ORIGINAL six-ID independent classifier disagrees")
        if tag is not None:
            real.append((tuple(sorted(ids)),tag))
    if scanned!=62370 or len(set(ids for ids,_ in real))!=len(real):
        raise AssertionError("not complete true original W32 left sixset audit")
    reference=seven_census(m,independent_checks=True,witness_sets=False)
    expected={"lex":(15,8),"reverse-line":(3,7)}[scheme]
    if (Counter(typ for _,typ in real)!={"D6":expected[0],
                                         "B/B-overlap":expected[1]}
        or reference["seven_class_motif_counts"]["D6"]!=expected[0]
        or reference["seven_class_motif_counts"]["B/B-overlap"]!=expected[1]):
        raise AssertionError("complete original physical positive family count changed")
    return tuple(sorted(real)),len(flags)


def _edge_masks(events,n):
    masks=tuple(sorted(set(_six_original_mask(ids,n) for ids,_ in events)))
    if len(masks)!=len(events):raise AssertionError("duplicate original motif support")
    return masks


def exact_min_original_hitting_set(edge_masks,n):
    """Replayable exact minimum original flag deletion set, no ILP/SAT trust."""
    edges=tuple(sorted(set(edge_masks)))
    if not edges:return {"tau":0,"original_IDs":[],"visited_states":1,
                          "rejected_cardinality_at_tau_minus_1":True}
    if any(x==0 or x>>n for x in edges):
        raise ValueError("not original positive sixset hyperedges")
    # Order chosen by edge conflict score: high coverage edge first.
    def candidates(rem):
        degree=Counter()
        for e in rem:
            for i in range(n):
                if e>>i&1:degree[i]+=1
        critical=max(rem,key=lambda e:sum(degree[i] for i in range(n) if e>>i&1))
        return sorted((i for i in range(n) if critical>>i&1),
                      key=lambda i:(-degree[i],i))
    visits=0
    @lru_cache(maxsize=None)
    def search(rem,budget):
        nonlocal visits
        visits+=1
        if not rem:return ()
        if budget==0:return None
        # Greedy pairwise-disjoint hyperedge lower bound; valid on ANY host.
        occupied=0;packing=0
        for e in sorted(rem,key=lambda z:z.bit_count()):
            if not e&occupied:occupied|=e;packing+=1
        if packing>budget:return None
        for i in candidates(rem):
            reduced=tuple(e for e in rem if not e>>i&1)
            ans=search(reduced,budget-1)
            if ans is not None:return tuple(sorted((i,)+ans))
        return None
    # Greedy upper bound is never needed for correctness; scan k from the
    # proved elementary disjoint packing lower bound to |events|.
    lower=0;occupied=0
    for e in edges:
        if not e&occupied:occupied|=e;lower+=1
    rejected=[]
    solution=None
    for k in range(lower,len(edges)+1):
        sol=search(edges,k)
        if sol is not None:
            solution=sol;break
        rejected.append(k)
    if solution is None:raise AssertionError("cannot hit every finite original event")
    tau=len(solution)
    if any(not(e&sum(1<<i for i in solution)) for e in edges):
        raise AssertionError("computed deletion certificate does NOT hit every motif")
    # Replay all-cardinality refutation at tau-1 without trusting
    # mathematical monotonicity from the search loop.
    if tau and search(edges,tau-1) is not None:
        raise AssertionError("minimum source deletion certificate is nonminimal")
    return {"tau":tau,"original_IDs":list(solution),
            "visited_states":visits,
            "rejected_cardinalities":rejected,
            "rejected_cardinality_at_tau_minus_1":True,
            "minimality_proof":"exhaustive six-way original flag branching,"
                               " sound disjoint-edge lower pruning; no timeout"}


def exact_max_original_disjoint_packing(edge_masks,n):
    """Exact maximum matching of SIX-original-ID hyperedges via finite DP."""
    E=tuple(sorted(set(edge_masks)))
    if any(x==0 or x>>n for x in E):
        raise ValueError("not original source hypergraph edges")
    @lru_cache(maxsize=None)
    def solve(remaining_indices):
        if not remaining_indices:return ()
        first=remaining_indices[0]
        skip=solve(remaining_indices[1:])
        take=(first,)+solve(tuple(
            j for j in remaining_indices[1:] if not E[j]&E[first]))
        return take if len(take)>len(skip) else skip
    witness=solve(tuple(range(len(E))))
    used=0
    for j in witness:
        if used&E[j]:raise AssertionError("not source original disjoint matching")
        used|=E[j]
    return {"nu":len(witness),
            "six_original_ID_sets":[
                [i for i in range(n) if E[j]>>i&1] for j in witness],
            "visited_dynamic_states":solve.cache_info().currsize,
            "exact_maximum_proved_by_include_exclude_DP":True}


def exact_adversarial_original_deletion_profile(edge_masks,n,max_k=4):
    """Every source flag deletion of each size <=min(max_k,n) audited."""
    if type(max_k) is not int or max_k<0 or max_k>n:
        raise ValueError("bad original flag adversarial profile budget")
    E=tuple(edge_masks)
    out=[]
    for k in range(max_k+1):
        min_survivors=len(E);count_min=0;example=None;sum_survivors=0
        for ids in combinations(range(n),k):
            mask=sum(1<<i for i in ids)
            survived=sum((mask&e)==0 for e in E)
            sum_survivors+=survived
            if survived<min_survivors:
                min_survivors=survived;count_min=1;example=list(ids)
            elif survived==min_survivors:count_min+=1
        total=comb(n,k)
        # Independent combinatorial double count: each six-ID source
        # motif avoids exactly C(n-6,k) deletions of cardinality k.
        expected=len(E)*comb(n-6,k) if k<=n-6 else 0
        if sum_survivors!=expected:
            raise AssertionError("original six-source incidence deletion double count failed")
        out.append({
            "deleted_original_ID_cardinality":k,
            "all_adversarial_deletion_subsets_exactly_enumerated":total,
            "minimum_surviving_true_original_six_motifs":min_survivors,
            "number_of_worst_adversarial_source_deletions":count_min,
            "lex_first_worst_source_deletion_IDs":example,
            "exact_total_survivor_events_over_all_deletions":sum_survivors,
            "independent_original_six_ID_double_count":expected,
        })
    return out


def exact_binomial_tail_under_ten_sign_union(t,r):
    """Tight closed-form stochastic-domination bound from source-ID packing.

    Coupling on independent Uniform[0,1] variables shows each exact
    independent motif-union Bernoulli(p_j) with p_j>=Q_TEN dominates
    an independent Bernoulli(Q_TEN). Thus d>=Y stochastically
    dominates Binomial(t,Q_TEN). No finite-h geometric assumptions.
    """
    if (type(t) is not int or type(r) is not int or
        t<0 or t>80 or r<0 or r>t+1):
        raise ValueError("exact fraction sum only supported 0<=t<=80, 0<=r<=t+1")
    P=Fraction(0)
    for j in range(r):
        P+=comb(t,j)*Q_TEN**j*(1-Q_TEN)**(t-j)
    if not 0<=P<=1:raise AssertionError("binomial tail is not a probability")
    return P


def finite_true_original_W32_exact_deletion_report(scheme):
    events,n=original_W32_hypergraph(scheme)
    edges=_edge_masks(events,n)
    cover=exact_min_original_hitting_set(edges,n)
    matching=exact_max_original_disjoint_packing(edges,n)
    if not matching["nu"]<=cover["tau"]<=6*matching["nu"]:
        raise AssertionError("true six-ID cover/matching dual bounds fail")
    profile=exact_adversarial_original_deletion_profile(edges,n,4)
    for row in profile:
        k=row["deleted_original_ID_cardinality"]
        if k<cover["tau"] and row["minimum_surviving_true_original_six_motifs"]<=0:
            raise AssertionError("finite adversarial deletions contradict exact transversal")
        if k==cover["tau"] and row["minimum_surviving_true_original_six_motifs"]!=0:
            raise AssertionError("exact transversal not realized by full k-deletion oracle")
    probability_no_at_least_one_motif=exact_binomial_tail_under_ten_sign_union(
        matching["nu"],1)
    return {
        "schema":"mathlab.hyp105.original-W32-exact-deletion-transversal-and-packing.v1",
        "scheme":scheme,
        "source":"genuine symplectic original W(3,2), 45 incidence-ID flags",
        "true_original_incidence_flags":n,
        "complete_original_physical_left_qualified_sixsets_audited":62370,
        "accepted_true_original_D6_BBo_six_motifs":len(events),
        "accepted_true_original_by_class":dict(Counter(x[1] for x in events)),
        "independent_full_original_sixset_ID_edges":[
            {"original_source_IDs":list(ids),"accepted_class":tag}
            for ids,tag in events],
        "exact_minimum_adversarial_original_ID_deletions":cover,
        "exact_maximum_original_ID_disjoint_six_motif_packing":matching,
        "exhaustive_adversarial_original_ID_deletions_size_0_to_4":profile,
        "binomial_stochastic_lower_original_source_packing_count":matching["nu"],
        "q10_complete_ten_sign_union_probability_min":str(Q_TEN),
        "stochastic_binomial_upper_clean_fraction_using_MAX_packing":
            {"numerator":probability_no_at_least_one_motif.numerator,
             "denominator":probability_no_at_least_one_motif.denominator},
        "root_230_status":ROOT_STATUS,
        "root_allh_geom_branch_A_PROVED_HERE":False,
        "claim_entire_W32_0_3_GF5_R3_exact_computed":False,
        "general_allh_source_packing_requires_external_review_of_674":True,
    }


def run():
    return {
        "schema":"mathlab.hyp105.original-W32-exact-deletion-research.v1",
        "finite_schemes":{
            x:finite_true_original_W32_exact_deletion_report(x)
            for x in ("lex","reverse-line")},
        "root_230_status":ROOT_STATUS,
        "this_is_NOT_a_new_universal_D6_BBo_lower":True,
        "binomial_tail_all_N_theorem_independent_of_674":True,
        "allh_corollary_requires_independently_accepting_674":True,
    }


if __name__=="__main__":
    print("HYP105_AA4_DELTRANS_ORIGINAL_CERTIFICATE="+json.dumps(
        run(),sort_keys=True,separators=(",",":")),flush=True)
