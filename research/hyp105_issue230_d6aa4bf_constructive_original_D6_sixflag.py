"""HYP-105 #230 AA4-BF: deterministic EXACT original SIX-ID selected D6 construction.

Parent #568 proves a >=s^6 true-original historical D6 conditional
mean for up to floor(V/16) arbitrary ORIGINAL line-factor image pins.
NEW: construct the COMPLETE globally injected right map by exact
conditional expectations, valid with ADAPTIVE ORIGINAL line source
factor arrival order chosen by a separate adversary. This directly
derandomizes SIX distinct ORIGINAL incidence-ID D6, not the 3-flag
GOOD statistic of independent sibling #566. Generic conditional
expectation is classical; source-specific certificate is new.

Fixed original source candidate weight w(l0,...,l5) counts actual
six incidence-ID sets whose globally fixed f(point) physical images
form a simple C6 in ordered source flag positions; the six original
LINE IDs are all distinct. Right favorable image tuples are ordered
six pair edges that form an occupied simple physical C6 in the SAME
six flag-position cycle. All one-global g completions correlated.

For partial global map psi with n remaining line images and mask
of already assigned source tuple positions, EXACT conditional
D6_free expectation = sum_tau w_tau * N_psi(tau)/(n)_(6-|mask|).
At every step, every free physical image candidate is evaluated in
Fraction arithmetic and exact averaging (tower) is asserted. Choose
the maximum, and repeat to complete. Parent #568 then implies
D6_full >= D6_free >= s^6, s>=32 and initial k<=floor(V/16).

The exhaustive true-original finite source enumeration is bounded
to W(3,2) for GitHub-hosted QA, with historical six GF5 oracle
crosschecks, NOT a fake high-s computational benchmark.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations, product
from math import comb

from hyp105_issue230_d6aa4be_original_D6_pins import (
    falling, original_D6_sixflag_pinned_envelope,
)


def _pair(e, a):
    if (not isinstance(e,(tuple,list)) or len(e)!=2 or
        any(type(x) is not int or not 0<=x<a for x in e)
        or e[0]==e[1]):
        raise ValueError("source factor image must be one physical unordered K_a edge")
    return tuple(sorted(e))


def _support(physical_edges,a):
    E=tuple(_pair(e,a) for e in physical_edges)
    if len(E)!=len(set(E)):
        raise ValueError("entire occupied ORIGINAL LINE image support must be injective")
    return E


def _pins_indices(pins,E,a):
    if not isinstance(pins,dict):
        raise ValueError("source line pins must be dict")
    lookup={e:i for i,e in enumerate(E)}
    fixed={}
    for l,e in pins.items():
        if type(l) is not int or not 0<=l<len(E):
            raise ValueError("actual original LINE source ID out of complete global range")
        e=_pair(e,a)
        if e not in lookup:
            raise ValueError("pinned original LINE image outside fixed occupied support")
        fixed[l]=lookup[e]
    if len(set(fixed.values()))!=len(fixed):
        raise ValueError("two original LINE source factors pinned to same physical edge")
    return fixed


def physically_ordered_original_D6_right_targets(physical_support,a):
    """All ordered source-position actual physically occupied right C6.

    Connected six-vertex cycles only; 12 orderings per undirected C6
    under the one fixed canonical POINT flag cyclic source ordering.
    Counts EXACT true-original source D6 physical target position maps.
    """
    E=_support(physical_support,a)
    owners={e:i for i,e in enumerate(E)}
    targets=set()
    for vertices in permutations(range(a),6):
        edges=tuple(_pair((vertices[i],vertices[(i+1)%6]),a)
                    for i in range(6))
        if all(e in owners for e in edges):
            targets.add(tuple(owners[e] for e in edges))
    return tuple(sorted(targets))


def original_W32_true_six_ID_D6_source_weights(model):
    """Real W(3,2) EXACT six-source incidence flagged C6 source pool.

    Normalize each undirected point-side C6 exactly once by its
    smallest physical vertex and smallest next physical neighbor;
    choose each of d^6 original source LINE assignments only if
    ALL SIX line source factors are distinct. Actual original
    incidence ID sixsets, NOT made-up GQ flags.
    """
    if model["s"]!=2 or model["a"]!=6:
        raise ValueError("finite exhaustive source Q oracle only for genuine W32")
    E=_support(model["left_labels"],6)
    V=len(E)
    inc=tuple(tuple(x) for x in model["incidences"])
    if V!=15 or len(inc)!=45 or len(set(inc))!=45:
        raise ValueError("genuine W32 full source geometry required")
    point_of_edge={e:p for p,e in enumerate(E)}
    neighbors=[[] for _ in range(V)]
    ids={}
    for i,(p,l) in enumerate(inc):
        if not (0<=p<V and 0<=l<V):
            raise ValueError("genuine original source factor out of range")
        neighbors[p].append(l)
        ids[(p,l)]=i
    if any(len(row)!=3 for row in neighbors):
        raise ValueError("W32 actual original source point degree mismatch")
    # Independently guard actual original line degree as well.
    if any(sum(l in row for row in neighbors)!=3 for l in range(V)):
        raise ValueError("not genuine W32 point-line regular incidence")
    cycles={}
    for vertices in permutations(range(6),6):
        physical=tuple(_pair((vertices[i],vertices[(i+1)%6]),6)
                       for i in range(6))
        if not all(e in point_of_edge for e in physical):
            continue
        key=frozenset(physical)
        if key not in cycles:
            # Turn raw undirected physical C6 into one canonical
            # orientation; this affects tuple positions only.
            cycles[key]=None
    if len(cycles)!=60:
        raise AssertionError("real complete original W32 point support has exactly 60 C6")
    weighted=Counter()
    source_Q=[]
    for edges in cycles:
        vertices={v for e in edges for v in e}
        v0=min(vertices)
        two=sorted(v for e in edges if v0 in e for v in e if v!=v0)
        if len(two)!=2:raise AssertionError("point physical C6 degree")
        path=[v0,two[0]]
        while len(path)<6:
            adj={v for e in edges if path[-1] in e for v in e if v!=path[-1]}
            nxt=next((v for v in sorted(adj) if v!=path[-2]),None)
            if nxt is None or nxt in path:
                raise AssertionError("point physical C6 not connected")
            path.append(nxt)
        actual=tuple(_pair((path[i],path[(i+1)%6]),6) for i in range(6))
        if set(actual)!=edges:
            raise AssertionError("canonical physical C6 orientation not full")
        points=tuple(point_of_edge[e] for e in actual)
        for line_ids in product(*(neighbors[p] for p in points)):
            if len(set(line_ids))!=6:
                continue
            Q=tuple(ids[(p,l)] for p,l in zip(points,line_ids))
            weighted[tuple(line_ids)]+=1
            source_Q.append(Q)
    if len(source_Q)!=sum(weighted.values()) or len(set(tuple(sorted(Q)) for Q in source_Q))!=len(source_Q):
        raise AssertionError("real ORIGINAL source Q six-incidence sets duplicated")
    if len(source_Q) not in (18716,21186):
        raise AssertionError("historical genuine original W32 eligible source Q pool drifted")
    return {"s":2,"V":V,"source_weighted_ordered_six_ORIGINAL_line_ID_tuples":dict(weighted),
            "actual_six_distinct_original_incidence_ID_Q_in_C6_positions":tuple(source_Q),
            "actual_eligible_source_Q_total":len(source_Q),
            "point_occupied_C6":len(cycles)}


def _valid_original_weighted_six(weights,V):
    if not isinstance(weights,dict):
        raise ValueError("source weights dict required")
    for key,w in weights.items():
        if (not isinstance(key,tuple) or len(key)!=6 or len(set(key))!=6 or
            any(type(x) is not int or not 0<=x<V for x in key) or
            type(w) is not int or w<=0):
            raise ValueError("six distinct true-original source LINE IDs and positive integer weights")
    return weights


def exact_one_global_six_ID_D6_conditional_mean(
        weights,E,a,pins,*,physical_targets=None):
    """ONE uniform global remaining original LINE permutation, not
    independently randomized physical images of each source Q.
    Six-bit fixed image-position masks; exact source/physical buckets.
    """
    E=_support(E,a);V=len(E)
    _valid_original_weighted_six(weights,V)
    locked=_pins_indices(pins,E,a)
    free=set(range(V))-set(locked.values())
    n=len(free)
    targets=(physically_ordered_original_D6_right_targets(E,a)
             if physical_targets is None else physical_targets)
    feasible=Counter()
    for target in targets:
        if len(target)!=6 or len(set(target))!=6 or any(
                type(x) is not int or not 0<=x<V for x in target):
            raise ValueError("physically valid six-target tuples must contain distinct occupied edges")
        for mask in range(64):
            if any(target[j] not in free for j in range(6)
                   if not mask&(1<<j)):
                continue
            key=(mask,tuple(target[j] for j in range(6)
                            if mask&(1<<j)))
            feasible[key]+=1
    groups=Counter()
    for six,w in weights.items():
        mask=sum(1<<j for j in range(6) if six[j] in locked)
        pattern=tuple(locked[six[j]] for j in range(6) if mask&(1<<j))
        groups[(mask,pattern)]+=w
    result=Fraction(0)
    for (mask,pattern),w in groups.items():
        unassigned=6-mask.bit_count()
        if unassigned>n:
            raise AssertionError("source six distinct LINE IDs beyond remaining full map pool")
        num=feasible.get((mask,pattern),0)
        if num:
            result+=Fraction(w*num,falling(n,unassigned))
    return result


def independently_literal_original_D6_six_ID_charge(weights,g,E,a):
    """Independent terminal one-whole-g original sixflag C6 evaluator.

    For a source sixLINE ID tuple in canonical left physical C6
    order, the six right physical image edges must connect in cyclic
    positional order, visit six distinct physical vertices, and have
    no diagonals; the existing W32 historical sevenGF5 classifier
    provides a SECOND source-ID based independent finite referee.
    """
    E=_support(E,a);V=len(E)
    _valid_original_weighted_six(weights,V)
    g=_support(g,a)
    if len(g)!=V or set(g)!=set(E):
        raise ValueError("not a complete globally injected original line source image")
    total=0
    for six,w in weights.items():
        physical=tuple(g[i] for i in six)
        if len({v for e in physical for v in e})!=6:
            continue
        adjacent=[]
        for j in range(6):
            z=set(physical[j])&set(physical[(j+1)%6])
            if len(z)!=1:
                break
            adjacent.append(next(iter(z)))
        if len(adjacent)==6 and len(set(adjacent))==6:
            total+=w
    return total


def exact_six_ID_D6_choose_next_global_line_image(
        weights,E,a,pins,source_LINE_id,*,physical_targets=None):
    """ADVERSARY selects next original source LINE ID; algorithm picks
    actual available right image with maximal EXACT conditional mean.
    """
    E=_support(E,a); V=len(E)
    locked=_pins_indices(pins,E,a)
    if type(source_LINE_id) is not int or not 0<=source_LINE_id<V or source_LINE_id in locked:
        raise ValueError("next actual ORIGINAL LINE ID must be currently unassigned")
    targets=(physically_ordered_original_D6_right_targets(E,a)
             if physical_targets is None else physical_targets)
    before=exact_one_global_six_ID_D6_conditional_mean(
        weights,E,a,pins,physical_targets=targets)
    free=tuple(i for i in range(V) if i not in set(locked.values()))
    tried=[]
    for j in free:
        trial=dict(pins);trial[source_LINE_id]=E[j]
        val=exact_one_global_six_ID_D6_conditional_mean(
            weights,E,a,trial,physical_targets=targets)
        tried.append((j,val))
    if sum((v for _,v in tried),Fraction())!=before*len(free):
        raise AssertionError("SIX-ID one-global-permutation conditional expectation TOWER")
    target,after=min(tried,key=lambda z:(-z[1],z[0]))
    if after<before:
        raise AssertionError("D6 sixflag conditional expectation should NEVER decrease")
    new=dict(pins);new[source_LINE_id]=E[target]
    return {"selected_REAL_original_LINE_source_factor_ID":source_LINE_id,
            "chosen_legal_physical_occupied_edge":E[target],
            "conditional_mean_before":before,
            "conditional_mean_after":after,
            "exact_tower_verified":True,
            "all_remaining_legal_next_images_checked":len(free),
            "updated_original_source_LINE_pins":new}


def construct_one_global_original_six_ID_D6_from_pins(
        weights,E,a,pins,*,source_order=None,max_steps=None,
        validate_floor_s=None,physical_targets=None):
    """Construct a complete ORIGINAL LINE g by exact conditional
    expectation for SIX-ID D6. max_steps requests partial proof only.

    For genuine original dyadic s>=32, when source weights = ALL
    real original Q avoiding initially pinned LINE IDs, and k<=V/16,
    parent #568's rigorous lower on initial conditional mean applies.
    """
    E=_support(E,a);V=len(E)
    _valid_original_weighted_six(weights,V)
    locked=_pins_indices(pins,E,a)
    orig=dict(pins)
    if validate_floor_s is not None:
        if type(validate_floor_s) is not int or validate_floor_s<32:
            raise ValueError("only proven dyadic original s>=32")
        expected_V=(validate_floor_s+1)*(validate_floor_s**2+1)
        if expected_V!=V:
            raise ValueError("source GQ original right V support does not match s")
        certificate=original_D6_sixflag_pinned_envelope(
            validate_floor_s,len(pins))
    else:
        certificate=None
    targets=(physically_ordered_original_D6_right_targets(E,a)
             if physical_targets is None else physical_targets)
    initial=exact_one_global_six_ID_D6_conditional_mean(
        weights,E,a,pins,physical_targets=targets)
    if certificate is not None and initial<certificate[
            "one_global_conditional_original_sixID_D6_expected_count_lower"]:
        raise AssertionError("true original sixflag source pool violates parent pinned lower")
    free_sources=tuple(i for i in range(V) if i not in pins)
    if source_order is None:
        source_order=free_sources
    else:
        source_order=tuple(source_order)
        if len(source_order)!=len(free_sources) or set(source_order)!=set(free_sources):
            raise ValueError("every remaining ORIGINAL LINE source factor ID exactly once")
    if max_steps is not None:
        if type(max_steps) is not int or not 0<=max_steps<=len(free_sources):
            raise ValueError("valid nonnegative step budget")
        source_order=source_order[:max_steps]
    current=dict(pins);history=[]
    for line in source_order:
        v=exact_six_ID_D6_choose_next_global_line_image(
            weights,E,a,current,line,physical_targets=targets)
        current=v["updated_original_source_LINE_pins"]
        history.append((line,v["conditional_mean_before"],v["conditional_mean_after"]))
    final=exact_one_global_six_ID_D6_conditional_mean(
        weights,E,a,current,physical_targets=targets)
    if final<initial:
        raise AssertionError("global D6 sixID exact conditional expectation decreases")
    done=len(current)==V
    mapping=tuple(_pair(current[i],a) for i in range(V)) if done else None
    actual=independently_literal_original_D6_six_ID_charge(
        weights,mapping,E,a) if done else None
    if done and Fraction(actual)!=final:
        raise AssertionError("literal full globally fixed g original D6 sixID count != exact conditional mean")
    return {"initial_adversarial_real_original_line_source_pins":orig,
            "last_globally_injective_real_original_source_pins":current,
            "fixed_entire_physical_right_edge_support_preserved":True,
            "original_line_factor_adaptive_arrival_order":tuple(source_order),
            "conditional_original_sixID_D6_mean_initial":initial,
            "conditional_original_sixID_D6_mean_last":final,
            "D6_potential_non_decreasing_all_steps":True,
            "one_complete_legal_original_global_right_g":mapping,
            "complete_global_selected_original_sixID_D6_charge":actual,
            "complete":done,
            "step_original_D6_fraction_history":tuple(history),
            "all_h_parent_sixID_D6_mean_lower_used":certificate,
            "some_constructed_global_g_D6_at_least_s6_if_parent_proven":
                bool(done and certificate is not None and actual>=validate_floor_s**6),
            "ROOT_230_all_fully_fixed_adversarial_f_g_NOT_proved":True,
            "same_original_SOURCE_incidence_ids_fixed":True}
