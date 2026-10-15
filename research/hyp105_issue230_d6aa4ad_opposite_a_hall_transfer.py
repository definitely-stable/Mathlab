"""HYP-105 issue #230 / AA4-AD: exact opposite-physical-A Hall transfer.

ALL-h genuine ORIGINAL W(3,2^h), complete GLOBALLY injected typed
physical pair-labels. Fix a TRUE doubled B source root p, two DISTINCT
actual source flags incident to it, and one physically REALIZED B-side
C4 of four distinct additional original source factors q0..q3.
Original opposite factor neighbors Ai=N(qi)\\{u0,u1} are held fixed.

Every accepted GF5 B/A or A/B six-incidence-ID Q is uniquely obtained
from exactly ONE simple six-physical-edge 2-factor H containing the two
pinned OPPOSITE physical edges g(u0),g(u1), whose other four physical
edges belong to globally injected g's image, and from ONE permutation
assigning the four distinct original opposite source factors
g^{-1}(H\\{g(u0),g(u1)}) to q0..q3, with membership in Ai.

The exact accepted count is sum_H permanent_4(incidence_matrix_H).
Hall's theorem gives permanent_4>0 iff every row subset has at least
as many candidate columns. This is a real second-gate equivalence, not
a positive universal count and not an assertion of statistical
independence of the global physical maps.

Prior exact ORIGINAL source forest four-rook permanent belongs to
parallel AA4-Y5 #507; THIS theorem adds the previously missing
opposite-side PHYSICAL 2-factor completion and Hall transfer gate.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations,permutations,product
from math import comb

from hyp105_issue230_d6aa4ab_minimax_orbit_normalform import (
    _valid_original_model,
)
from hyp105_issue230_d6aa4q_two_sided_seven_join import (
    exact_two_sided_original_seven_join,
    strict_true_W32_model,
)


def edge(u,v):
    if type(u) is not int or type(v) is not int or u==v:
        raise ValueError("physical edge needs two distinct integer coordinates")
    return (u,v) if u<v else (v,u)


def _check_physical_edge(e,a):
    try:
        e=tuple(e)
    except TypeError as exc:
        raise ValueError("physical edge must be iterable") from exc
    if (len(e)!=2 or any(type(x) is not int for x in e)
            or not 0<=e[0]<e[1]<a):
        raise ValueError("canonical unordered physical pair required")
    return e


@lru_cache(maxsize=1)
def six_vertex_two_factors():
    """All 60 undirected C6 and all 10 two-triangle sets on [0..5].

    Entirely independent combinatorial construction; no GF5 signature
    or existing 70-mode two-factor library is imported.
    """
    vertices=tuple(range(6))
    factors=set()
    for ordered in permutations(vertices[1:]):
        ring=(0,)+ordered
        if ring[1]>ring[-1]:
            continue  # reverse is the same undirected cycle
        physical=frozenset(edge(ring[i],ring[(i+1)%6]) for i in range(6))
        factors.add(physical)
    for other_two in combinations(vertices[1:],2):
        first=frozenset((0,)+other_two)
        second=frozenset(vertices)-first
        physical=frozenset(
            edge(u,v) for triangle in (first,second)
            for u,v in combinations(sorted(triangle),2))
        factors.add(physical)
    if len(factors)!=70:
        raise AssertionError("true six-vertex 2-factor count !=70")
    return tuple(sorted(tuple(sorted(H)) for H in factors))


def _validate_pinned(e0,e1,a):
    p0,p1=_check_physical_edge(e0,a),_check_physical_edge(e1,a)
    if p0==p1:
        raise ValueError("globally injected opposite labels must be distinct")
    return p0,p1


def pinned_twofactor_completions(e0,e1,a):
    """Enumerate exactly all physical six-vertex 2factors containing
    two distinct pinned K_a physical edges (including unoccupied ones).

    For a>6 avoid enumerating C(a,6) unrelated physical coordinate
    sets: only sets containing the 3 or 4 pinned coordinates are needed.
    """
    e0,e1=_validate_pinned(e0,e1,a)
    fixed=frozenset(e0+e1)
    needed=6-len(fixed)
    candidates=tuple(x for x in range(a) if x not in fixed)
    result=[]
    for addition in combinations(candidates,needed):
        vertices=tuple(sorted(fixed|set(addition)))
        for form in six_vertex_two_factors():
            H=tuple(sorted(edge(vertices[u],vertices[v]) for u,v in form))
            if e0 in H and e1 in H:
                result.append(H)
    if len(set(result))!=len(result):
        raise AssertionError("physical 2factor listed more than once")
    # Complete K_a patterns containing two fixed physical edges:
    # see physical-degree two-factor elementary counting.
    adjacent=bool(set(e0)&set(e1))
    expected=(7*comb(a-3,3) if adjacent
              else 14*comb(a-4,2))
    if len(result)!=expected:
        raise AssertionError("physical two-pinned A count mismatch")
    return tuple(result)


def _four_permanent_and_hall(rows):
    """Four labelled original source factors -> four labelled physical
    completion edges; each row lists possible column indices 0..3.
    """
    if len(rows)!=4:
        raise ValueError("four original C4 factors required")
    sets=tuple(frozenset(z) for z in rows)
    if any(any(type(j) is not int or not 0<=j<4 for j in z) for z in sets):
        raise ValueError("columns must be physical completion slots 0..3")
    witness=None
    for k in range(1,5):
        for choose in combinations(range(4),k):
            union=set().union(*(sets[i] for i in choose))
            if len(union)<k:
                witness={"original_row_subset":choose,
                         "possible_physical_slots":tuple(sorted(union)),
                         "Hall_deficit":k-len(union)}
                break
        if witness is not None:break
    permanent=sum(all(p[i] in sets[i] for i in range(4))
                  for p in permutations(range(4)))
    if (permanent>0)!=(witness is None):
        raise AssertionError("four-source actual Hall iff permanent >0 failed")
    return permanent,witness


def opposite_physical_A_Hall_transfer(model,*, B_side, root,
                                      pinned_original_Q, four_sources):
    """Exact new physical-A 2-factor transfer gate for ONE genuine
    original B-source root+two REAL source flags+one physical C4 pattern.

    Model has ONE common true GQ original I, a COMPLETE injected f for
    all point factors and a COMPLETE injected g for all line factors;
    side=0 is repeated original point, 1 is repeated original line.

    The finite executable validates a true symplectic indexed W(3,s)
    model; the abstract proof holds all h and the finite algorithm
    scales with the pinned two-physical-edge completions.
    """
    v,a,inc=_valid_original_model(model)
    if B_side not in (0,1) or type(B_side) is not int:
        raise ValueError("B_side must be 0 (point) or 1 (line)")
    if type(root) is not int or not 0<=root<v:
        raise ValueError("true original B-source root index required")
    flags=tuple(pinned_original_Q)
    if (len(flags)!=2 or len(set(flags))!=2
            or any(type(i) is not int or not 0<=i<len(model["incidences"])
                   for i in flags)):
        raise ValueError("two different actual original flag IDs required")
    original=tuple(tuple(z) for z in model["incidences"])
    if any(original[i][B_side]!=root for i in flags):
        raise ValueError("both REAL pinned source flags must use repeated root")
    pins=tuple(original[i][1-B_side] for i in flags)
    if pins[0]==pins[1]:
        raise ValueError("actual original source incidence simplicity violated")
    q=tuple(four_sources)
    if (len(q)!=4 or len(set(q))!=4 or root in q or
            any(type(x) is not int or not 0<=x<v for x in q)):
        raise ValueError("four distinct original other-side singleton B factors")
    side_labels=tuple(tuple(x) for x in model["left_labels" if B_side==0 else "right_labels"])
    opposite_labels=tuple(tuple(x) for x in model["right_labels" if B_side==0 else "left_labels"])
    phys_root=side_labels[root]
    complement=frozenset(x for x in range(a) if x not in phys_root)
    physical_edges=tuple(side_labels[x] for x in q)
    if (len(complement)<4 or
            any(not set(e)<=complement for e in physical_edges)):
        raise ValueError("four singleton source images must lie in complementary physical coordinates")
    deg=Counter(x for e in physical_edges for x in e)
    if len(deg)!=4 or any(m!=2 for m in deg.values()):
        raise ValueError("four physical singleton source pairs must form complementary C4")
    # A 4-cycle on 4 vertices has 4 different simple edges. Degree-two
    # can also represent two disjoint doubled edges, but global
    # injectivity disallows doubled physical original factor images.
    if len(set(physical_edges))!=4:
        raise ValueError("globally injected original B-side physical C4 required")
    graph={x:set() for x in deg}
    for u,w in physical_edges:
        graph[u].add(w);graph[w].add(u)
    start=next(iter(graph));seen={start};pending=[start]
    while pending:
        for w in graph[pending.pop()]:
            if w not in seen:seen.add(w);pending.append(w)
    if len(seen)!=4:
        raise ValueError("B-side physical singletons must be connected C4")
    bysource=[set() for _ in range(v)]
    for pt,line in original:
        bysource[(pt,line)[B_side]].add((pt,line)[1-B_side])
    choices=tuple(frozenset(bysource[x]-set(pins)) for x in q)
    inverse={e:i for i,e in enumerate(opposite_labels)}
    e0,e1=opposite_labels[pins[0]],opposite_labels[pins[1]]
    physical=pinned_twofactor_completions(e0,e1,a)
    occupied=with_hall=accepted=0
    hall_failure=Counter()
    first_blocker=None
    for H in physical:
        remainder=tuple(e for e in H if e not in (e0,e1))
        if len(remainder)!=4:
            raise AssertionError("two pinned physical edges missing in completion")
        if any(e not in inverse for e in remainder):
            continue
        occupied+=1
        opposite_sources=tuple(inverse[e] for e in remainder)
        rows=tuple(frozenset(j for j,line in enumerate(opposite_sources)
                             if line in choices[i]) for i in range(4))
        permanent,witness=_four_permanent_and_hall(rows)
        if witness is not None:
            hall_failure[witness["Hall_deficit"]]+=1
            if first_blocker is None:first_blocker=witness
        else:
            with_hall+=1
        accepted+=permanent
    if not 0<=with_hall<=occupied<=len(physical):
        raise AssertionError("accepted true original GF5 Hall hierarchy invalid")
    if not with_hall<=accepted<=24*with_hall:
        raise AssertionError("Hall-positive four-rook permanent bounded by 24")
    return {
        "B_side":"point" if B_side==0 else "line",
        "original_root":root,
        "actual_original_root_flags":flags,
        "four_original_singleton_factors":q,
        "opposite_pinned_original_factors":pins,
        "opposite_pinned_physical_relation":(
            "adjacent" if set(e0)&set(e1) else "disjoint"),
        "all_physical_two_factors_with_pinned_edges":len(physical),
        "fully_occupied_opposite_physical_two_factors":occupied,
        "occupied_completions_rejected_by_Hall":occupied-with_hall,
        "completions_passing_all_4x4_Hall_subsets":with_hall,
        "accepted_distinct_original_six_Q_through_permanents":accepted,
        "first_Hall_obstruction":first_blocker,
        "Hall_deficit_histogram":dict(sorted(hall_failure.items())),
        "all_h_original_Hall_gate_formula_exact":True,
        "fixed_global_point_and_line_images_required":True,
        "not_an_every_global_maps_positive_lower":True,
    }


def _W32_true_physical_C4_sources(labels,root):
    """Independent full K6 enumerator: 3 root-C4 patterns per root."""
    physical=tuple(labels)
    inverse={e:i for i,e in enumerate(physical)}
    if len(physical)!=15 or len(inverse)!=15:
        raise ValueError("genuine complete K6 source labels required")
    complement=tuple(c for c in range(6) if c not in physical[root])
    all_edges=set(combinations(complement,2))
    ans=[]
    for matching in (
        ((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))
    ):
        omitted={edge(complement[i],complement[j]) for i,j in matching}
        C4=tuple(sorted(all_edges-omitted))
        q=tuple(inverse[e] for e in C4)
        if len(set(q))!=4:
            raise AssertionError("original four C4 source factors duplicated")
        ans.append(q)
    if len(set(ans))!=3:
        raise AssertionError("K6 root physical C4 has 3 source configurations")
    return ans


def independent_W32_original_second_gate_census(scheme, *, brute_force=True):
    """Strict REAL symplectic W32: all 45 root/two-flag cohorts x 3
    realized source B C4 patterns x both typed sides, independent
    original GF5 historical seven-tag and two-side Q join crosschecks.
    """
    from hyp105_issue230_projection import fixture
    model=fixture(1,scheme)
    inc,left,right=strict_true_W32_model(model)
    global_labels=(left,right)
    joint=exact_two_sided_original_seven_join(model,independent_history=True)
    report={}
    for side in (0,1):
        byroot=[[] for _ in range(15)]
        neighbors=[set() for _ in range(15)]
        for j,(p,l) in enumerate(inc):
            byroot[(p,l)[side]].append(j)
            neighbors[(p,l)[side]].add((p,l)[1-side])
        tally=Counter();zeros=0;Hall_zero=0;nonzero=0;direct_match=0
        records=[]
        for root in range(15):
            for pinned in combinations(byroot[root],2):
                frozen={inc[j][1-side] for j in pinned}
                for q in _W32_true_physical_C4_sources(global_labels[side],root):
                    row=opposite_physical_A_Hall_transfer(
                        model,B_side=side,root=root,
                        pinned_original_Q=pinned,four_sources=q)
                    direct=0;forests=0
                    if brute_force:
                        Ai=tuple(neighbors[u]-frozen for u in q)
                        for assignments in product(*Ai):
                            if len(set(assignments))!=4:continue
                            forests+=1
                            physical=tuple(global_labels[1-side][t] for t in
                                           tuple(frozen)+assignments)
                            degree=Counter(x for e in physical for x in e)
                            if len(degree)==6 and set(degree.values())=={2}:
                                direct+=1
                        if row["accepted_distinct_original_six_Q_through_permanents"]!=direct:
                            raise AssertionError("TRUE ORIGINAL second gate direct incidence-Q != Hall 2factor permanent")
                    tally["physical2factor"]+=row["all_physical_two_factors_with_pinned_edges"]
                    tally["occupied"]+=row["fully_occupied_opposite_physical_two_factors"]
                    tally["hall"]+=row["completions_passing_all_4x4_Hall_subsets"]
                    tally["accepted"]+=row["accepted_distinct_original_six_Q_through_permanents"]
                    tally["source_forests"]+=forests
                    if not row["accepted_distinct_original_six_Q_through_permanents"]:
                        zeros+=1
                        if not row["completions_passing_all_4x4_Hall_subsets"]:
                            Hall_zero+=1
                    else:nonzero+=1
                    direct_match+=int(row["accepted_distinct_original_six_Q_through_permanents"]==direct)
                    records.append(row)
        tag=("B-left/A-right" if side==0 else "A-left/B-right")
        if len(records)!=135:
            raise AssertionError("genuine original W32 needs exactly 45*3 B cohorts per side")
        if tally["accepted"]!=joint["accepted_seven_GF5_original_Q_by_tag"][tag]:
            raise AssertionError("GF5 historical original six-Q BA count != exact physical-Hall transfer")
        if brute_force and tally["source_forests"]<=tally["accepted"]:
            raise AssertionError("true W32 physical source-A gate should reject some source forests")
        report[tag]={
            "actual_original_B_root_two_flag_C4_cohorts":len(records),
            "all_physical_candidate_2factors":tally["physical2factor"],
            "fully_occupied_opposite_physical_2factors":tally["occupied"],
            "actual_two_factor_completions_passing_original_Hall":tally["hall"],
            "source_only_distinct_original_flag_forests":tally["source_forests"],
            "accepted_actual_original_GF5_BA":tally["accepted"],
            "zero_accepted_cohorts":zeros,
            "Hall_zero_accepted_cohorts":Hall_zero,
            "positive_accepted_cohorts":nonzero,
            "independent_original_direct_four_choice_confirmations":direct_match,
            "all_actual_original_Q_and_full_global_label_constraints_checked":True,
        }
    return {
        "slice":"HYP105-D6-AA4-AD-OPPOSITE-PHYSICAL-A-HALL-TRANSFER",
        "scheme":scheme,"s":2,
        "original_true_incidence_flags":45,
        "per_B_A_historical_GF5_tag":report,
        "full_original_GF5_S":joint["accepted_seven_GF5_original_S"],
        "root_A":"OPEN","root_B":"OPEN","root_C":"OPEN",
    }


def analytic_physical_gate_counts(s):
    from hyp105_issue230_proof_audit import parameters
    p=parameters(s)
    a=p["a"]
    if a<6:raise AssertionError("physical 6vertex twofactor needs >=6")
    return {"s":s,"a":a,"K":p["K"],
            "adjacent_pinned_physical_2factors":7*comb(a-3,3),
            "disjoint_pinned_physical_2factors":14*comb(a-4,2),
            "all_h_exact_second_gate_Hall_permanent":True,
            "adversarial_GF5_positive_omega_s6_PROVED":False}


if __name__=="__main__":
    import argparse,json
    p=argparse.ArgumentParser()
    p.add_argument("--scheme",choices=("S68","S72","lex","reverse"))
    args=p.parse_args()
    x=(independent_W32_original_second_gate_census(args.scheme)
       if args.scheme else
       {"orders":[analytic_physical_gate_counts(1<<h) for h in range(1,10)]})
    print(json.dumps(x,indent=2,sort_keys=True))
