"""HYP-105 AA4-CI: exact dual-aware S6 orbit of a fixed genuine original POINT-A fiber.

Fix SIX distinct actual original POINT source IDs P and a COMPLETE globally
injective true-original W(3,2^h) POINT f with six selected physical pair
images forming ONE physical C6. Fix ANY correlated complete original LINE g.

For ALL 6! complete GLOBAL f permutations of those six whole source-factor
images (all other original f images unchanged), the HISTORICAL seven-GF5
weighted score on all true distinct original six-incidence Q choosing EXACTLY
one incident source flag at each p in P is:

    T(pi) = 45600*N_B + 43320*N_C + 5643*H[dual_C6(pi)].

H is exact original-Q right source-A physical connected six-position
dual-cycle histogram over the SIXTY labeled Hamiltonian sixcycles.
Every cycle appears at exactly 12 of 720 f permutations. The source
right-B / right-C physically accepted counts are invariant across ALL
720 maps; none of the other four historical positive source classes can
occur because the point-source type is fixed A.

This is NOT a full all-seven S_s theorem or all-h Branch A/B/C.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import permutations, product
from math import factorial

from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4cg_four_shared_edge_two_completion import (
    classify_seven_all_a_original_Q,
)
from hyp105_issue230_d6aa4ch_maximal_d6_fan_physical_gram_nogo import (
    _full_pair_injection, _match_unique, SIX_CYCLE,
    original_maximal_D6_fan,
)
from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1b0_seven_signature import R3_CERTIFIED_FLOORS

PERMS=tuple(permutations(range(6)))
assert len(PERMS)==factorial(6)==720
W_B=R3_CERTIFIED_FLOORS["A-left/B-right"]
W_C=R3_CERTIFIED_FLOORS["C/A"]
W_D=R3_CERTIFIED_FLOORS["D6"]
assert (W_B,W_C,W_D)==(45600,43320,5643)


def _six_position_dual_cycle(edges):
    """Independently build the actual six-column physical incidence dual.

    Returns a labeled Hamiltonian 6-cycle key on six *source incidence
    positions* 0..5, or None for invalid physical 2factor / two triangles.
    """
    if len(edges)!=6:return None
    coordinate={}
    for j,edge in enumerate(edges):
        if len(edge)!=2 or edge[0]==edge[1]:
            return None
        for c in edge:
            coordinate.setdefault(c,[]).append(j)
    if len(coordinate)!=6 or any(len(ids)!=2 for ids in coordinate.values()):
        return None
    dual=frozenset(frozenset(ids) for ids in coordinate.values())
    if len(dual)!=6 or any(len(e)!=2 for e in dual):
        return None
    adjacency=[set() for _ in range(6)]
    for edge in dual:
        i,j=tuple(edge)
        adjacency[i].add(j);adjacency[j].add(i)
    if any(len(z)!=2 for z in adjacency):
        return None
    # One direct graph traversal; do not assume an ordering on physical labels.
    stack=[0];visited=set()
    while stack:
        p=stack.pop()
        if p in visited:continue
        visited.add(p)
        stack.extend(adjacency[p]-visited)
    return dual if len(visited)==6 else None


def _six_position_dual_any(edges):
    """Degree-2 six-coordinate graph dual, connected or not."""
    if len(edges)!=6:return None
    coordinate={}
    for j,edge in enumerate(edges):
        if len(edge)!=2 or edge[0]==edge[1]:return None
        for c in edge:coordinate.setdefault(c,[]).append(j)
    if len(coordinate)!=6 or any(len(z)!=2 for z in coordinate.values()):
        return None
    dual=frozenset(frozenset(ids) for ids in coordinate.values())
    return dual if len(dual)==6 and all(len(e)==2 for e in dual) else None


def complete_original_f_orbit(f,point_ids,perm):
    """One legal WHOLE-original POINT source image permutation."""
    points=tuple(point_ids)
    if len(points)!=6 or len(set(points))!=6 or any(type(p) is not int or not 0<=p<len(f) for p in points):
        raise ValueError("six different real original POINT factor IDs required")
    if tuple(sorted(perm))!=tuple(range(6)):
        raise ValueError("complete six-permutation of point physical images required")
    f=tuple(tuple(sorted(e)) for e in f)
    images=tuple(f[p] for p in points)
    changed=list(f)
    for i,p in enumerate(points):changed[p]=images[perm[i]]
    if len(set(changed))!=len(changed):
        raise AssertionError("global original f orbit must stay fully injected")
    return tuple(changed)


def original_cycle_orbit(f,point_ids):
    """60 possible original six-incidence-position dual C6, 12 maps each."""
    points=tuple(point_ids)
    if len(points)!=6 or len(set(points))!=6 or any(type(p) is not int or not 0<=p<len(f) for p in points):
        raise ValueError("six distinct actual original POINT source factors needed")
    images=tuple(f[p] for p in points)
    if len(set(images))!=6:
        raise ValueError("full source f must be injected on fixed six POINTs")
    if _six_position_dual_cycle(images) is None:
        raise ValueError("selected source POINT images must form connected physical C6")
    cycle_by_perm=tuple(_six_position_dual_cycle(tuple(images[j] for j in perm))
                        for perm in PERMS)
    if any(k is None for k in cycle_by_perm):
        raise AssertionError("whole-image source permutations of C6 must preserve C6")
    multiplicity=Counter(cycle_by_perm)
    if len(multiplicity)!=60 or set(multiplicity.values())!={12}:
        raise AssertionError("Hamiltonian cycle S6 orbit must have 60 cycles of size 12")
    return cycle_by_perm,multiplicity


def original_point_A_fiber(model,point_ids):
    """Exact original-GQ source sixflag fiber with 6 distinct POINT IDs.

    Enumerate each true original Q ONCE, via complete original incidence
    stars. Its LINE-side source profile and physical dual refer to the
    SAME six fixed source-incidence positions and the ONE complete g.
    """
    s,V,a,inc,f,g,by_point,_=_original_source(model)
    points=tuple(point_ids)
    cycle_by_perm,orbit=original_cycle_orbit(f,points)
    source_flag_stars=tuple(tuple(sorted(by_point[p])) for p in points)
    hist=Counter()
    records=[]
    counters=Counter()
    for flags in product(*source_flag_stars):
        if len(set(flags))!=6:
            raise AssertionError("one original flag per six distinct source POINTs")
        lines=tuple(inc[j][1] for j in flags)
        m=tuple(sorted(Counter(lines).values()))
        source={ (1,1,1,1,1,1):"A", (1,1,1,1,2):"B", (2,2,2):"C" }.get(m)
        physical=tuple(g[l] for l in lines)
        degree=Counter(c for e in physical for c in e)
        if len(degree)!=6 or set(degree.values())!={2}:continue
        if source is None:
            raise AssertionError("genuine six-coordinate original physical 2factor had forbidden original source partition")
        original_Q=tuple(sorted(flags))
        if source=="B":
            counters["B"]+=1
            records.append((original_Q,"B",None))
        elif source=="C":
            counters["C"]+=1
            records.append((original_Q,"C",None))
        elif source=="A":
            dual=_six_position_dual_cycle(physical)
            if dual is not None:
                hist[dual]+=1
                counters["A_physical_C6"]+=1
                records.append((original_Q,"D6_cyclic",dual))
            else:
                counters["A_physical_two_triangles"]+=1
        else:raise AssertionError("unexpected original POINT-A right class")
    baseline=W_B*counters["B"]+W_C*counters["C"]
    scores=tuple(baseline+W_D*hist[cyc] for cyc in cycle_by_perm)
    mean=Fraction(baseline)+Fraction(W_D*counters["A_physical_C6"],60)
    second=Fraction(sum(t*t for t in scores),720)
    mean2=sum(scores,0)
    if Fraction(mean2,720)!=mean:
        raise AssertionError("original 6factor orbit first moment != 60 cycle count identity")
    exact2=Fraction(baseline**2)+2*baseline*Fraction(
        W_D*counters["A_physical_C6"],60)+Fraction(
        W_D*W_D*sum(n*n for n in hist.values()),60)
    if second!=exact2:
        raise AssertionError("original 6factor orbit second moment collision spectrum mismatch")
    return {
        "s":s,"V":V,"a":a,"point_ids":points,
        "true_original_incidence_Q_count":(s+1)**6,
        "physically_eligible_named_source_Q":len(records),
        "source_class_counts":dict(counters),
        "eligible_actual_original_Q":tuple(records),
        "right_cyclic_dual_hist":dict(hist),
        "active_cyclic_dual_types":len(hist),
        "all_60_orbit_cycle_types":60,
        "per_cycle_original_f_complete_maps":12,
        "orbit_scores":scores,
        "original_baseline_B_C_weighted":baseline,
        "original_exact_orbit_mean":mean,
        "original_exact_orbit_second_moment":second,
        "original_exact_orbit_variance":second-mean*mean,
        "global_f_orbit_uses_same_six_source_IDs":True,
        "all_seven_classes_on_pointA_fiber_only_B_C_D6":True,
        "universal_full_original_S_lower_proved":False,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


def original_D6_fan_orbit(power):
    """AA4-CH original fixed named fan: exactly 12 D6 maps, 708 zero."""
    z=original_maximal_D6_fan(power)
    s,V,a,inc,f,g,_,_=_original_source(z["normal_model"])
    points=z["point_ids"];fan=z["fan"]
    hist=Counter()
    for Q in fan:
        right=tuple(g[inc[next(j for j in Q if inc[j][0]==p)][1]] for p in points)
        key=_six_position_dual_cycle(right)
        if key is None:raise AssertionError("genuine maximal fan needs right dual C6")
        hist[key]+=1
    by_perm,orbits=original_cycle_orbit(f,points)
    scored=tuple(W_D*hist[k] for k in by_perm)
    if len(hist)!=1 or tuple(hist.values())!=(s+1,) or scored.count(W_D*(s+1))!=12 or scored.count(0)!=708:
        raise AssertionError("original maximal D6 fan S6 cycle distribution wrong")
    return {"s":s,"fan_size":s+1,"positive_global_f_orbit_maps":12,
            "zero_global_f_orbit_maps":708,
            "weighted_fan_original_at_positive":W_D*(s+1),
            "weighted_fan_original_orbit_mean":Fraction(W_D*(s+1),60),
            "one_complete_original_g_unchanged":True}


def original_B_C_D6_mixed_fixture(power):
    """One TRUE W34/W38 original POINT-A fiber contains right B, C and D6.

    Construct physical right B repeated edge+4cycle, right C three
    duplicated disjoint edges, and right A aligned D6. All three are
    distinct TRUE original six-incidence sets on SAME six POINT IDs,
    with ONE complete globally injected g and one complete f.
    """
    if type(power) is not int or power not in (2,3):
        raise ValueError("finite symplectic original W34/W38 fixtures only")
    model=fixture(power,"lex")
    s,V,a,inc,f,g,by_p,by_l=_original_source(model)
    point_sets=tuple(frozenset(inc[j][0] for j in src) for src in by_l)
    triples=None
    for x in range(V):
        rest=[y for y in range(x+1,V) if not(point_sets[x]&point_sets[y])]
        for i,y in enumerate(rest):
            for z in rest[i+1:]:
                if not (point_sets[x]&point_sets[z] or point_sets[y]&point_sets[z]):
                    triples=(x,y,z);break
            if triples:break
        if triples:break
    if triples is None:raise AssertionError("genuine original GQ requires three disjoint LINE stars")
    pts=tuple(p for l in triples for p in sorted(point_sets[l])[:2])
    if len(set(pts))!=6:raise AssertionError("selected actual original POINTs are repeated")
    stars=tuple(set(inc[j][1] for j in by_p[p]) for p in pts)
    anchor=set(triples)
    lx=next(v for v in sorted(stars[3]-anchor))
    ly=next(v for v in sorted(stars[5]-anchor-{lx}))
    locked=anchor|{lx,ly}
    candidates=tuple(tuple(sorted(star-locked)) for star in stars)
    extra=_match_unique(candidates)
    if len(set(extra))!=6 or set(extra)&locked:
        raise AssertionError("original source D6 LINE SDR incompatible with B/C anchors")
    f=_full_pair_injection(V,a,dict(zip(pts,SIX_CYCLE)))
    cycle6=((6,7),(7,8),(8,9),(9,10),(10,11),(6,11))
    pins={triples[0]:(0,1),triples[1]:(2,3),triples[2]:(4,5),
          lx:(3,4),ly:(2,5)}
    pins.update(dict(zip(extra,cycle6)))
    g=_full_pair_injection(V,a,pins)
    ids={(p,l):j for j,(p,l) in enumerate(inc)}
    C=tuple(sorted(ids[pts[i],triples[i//2]] for i in range(6)))
    B=tuple(sorted(ids[pts[i],l] for i,l in enumerate((
        triples[0],triples[0],triples[1],lx,triples[2],ly))))
    D=tuple(sorted(ids[pts[i],extra[i]] for i in range(6)))
    mm=dict(model,left_labels=f,right_labels=g)
    if any(len(set(q))!=6 for q in (C,B,D)):
        raise AssertionError("original P-fiber Q IDs not six-distinct")
    if {classify_seven_all_a_original_Q(B,f,g,inc),
        classify_seven_all_a_original_Q(C,f,g,inc),
        classify_seven_all_a_original_Q(D,f,g,inc)}!={"A-left/B-right","C/A","D6"}:
        raise AssertionError("original same fixed full-g mixed all-3 selected classes construction failed")
    return mm,pts,{"B":B,"C":C,"D6":D}
