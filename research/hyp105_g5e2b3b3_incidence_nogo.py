"""HYP-105 E2-B3.3: RESTRICTED all-h no-go for incidence-matched pair labels.

Let G=W(3,2^h), f:Points -> K_a edges injective, and choose ANY
perfect incidence matching pi:Lines -> Points so (pi(l),l) is an edge.
Set g(l)=f(pi(l)) in the physically disjoint RIGHT coordinate block.

Every left physical C6 gives six matching incidence columns whose right
labels equal their left labels, so D_s >= #C6(f(Points)).
Since f covers V edges of K_a, and K=binom(a,2) with 0<=K-V<a-1,
at most (K-V)*(a-2)_4 cycles of K_a are lost. Hence

    D_s >= (a)_6/12 - (K-V)*(a-2)_4 = Omega(a^6)=Omega(s^9).
    R3(B_s) >= (5643/51^6) * D_s = Omega(s^9).

This blocks ONLY incidence-matched correlated embeddings, not arbitrary
correlated mappings or the ASET conjecture. The theorem needs no finite
enumeration, which is used solely as an independent sanity check.
"""
from math import comb
import json

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_g5e2b3b2_coincident_cycles import (
    physical_six_cycles, exact_coincident_c6,
    exact_alternating_cycle_weight, check_input,
)


def falling(n, k):
    if not isinstance(n, int) or not isinstance(k, int) or n < 0 or k < 0:
        raise ValueError("nonnegative integer falling factorial only")
    out = 1
    for i in range(k):
        out *= n-i
    return out


def forced_sixcycles_lower(s):
    """Rigorous absolute bound valid for ANY injection to minimal K_a."""
    if not isinstance(s, int) or s < 2 or s & (s-1):
        raise ValueError("s must be power of two >=2")
    v = (s+1)*(s*s+1)
    a = 6
    while comb(a,2) < v:
        a += 1
    K = comb(a,2)
    missing = K-v
    if not 0 <= missing < a-1:
        raise AssertionError("minimal alphabet property failed")
    total = falling(a,6)//12
    through_one_edge = falling(a-2,4)
    union_bound = total - missing * through_one_edge
    lower = max(0, union_bound)
    if lower < 0 or lower > total:
        raise AssertionError("invalid union-bound C6 count")
    return {
        "s":s, "a":a, "V":v, "K":K, "missing_pairs":missing,
        "all_Ka_C6":total, "C6_containing_given_pair":through_one_edge,
        "unconditional_C6_lower":lower,
        "fixed_label_D_lower":lower,
        "fixed_label_R3_lower_numerator": 5643 * lower,
        "fixed_label_R3_lower_denominator": 51**6,
        "asymptotic": "D_s=Omega(s^9), R3=Omega(s^9) for incidence-matched labels only",
        "excludes_all_correlated_labels": False,
        "new_ASET_exponent_proved": False,
    }


def canonical_incidence_perfect_matching(model):
    """Deterministic augmenting path algorithm on a verified regular GQ.

    Graph-theoretic ALL-s existence: each side of the Delta-regular
    bipartite GQ graph has V vertices. For any subset S of line vertices,
    Delta|S| incident edges end at N(S), each of whose points has degree
    Delta, so |N(S)| >= |S|. Hall guarantees a perfect matching.
    Lexical DFS augmentation is merely a finite constructive witness.
    """
    _, points, lines, edges = check_input(model)
    if len(points) != len(lines):
        raise ValueError("regular matched bipartite graph must be balanced")
    V=len(points)
    by_line = [[] for _ in range(V)]
    deg_point = [0]*V
    for p,l in edges:
        by_line[l].append(p)
        deg_point[p]+=1
    degrees = {len(x) for x in by_line} | set(deg_point)
    if len(degrees)!=1 or next(iter(degrees))==0:
        raise ValueError("GQ regularity expected; subsets are not guaranteed matchable")
    for row in by_line:
        row.sort()
    point_to_line = [-1]*V

    def augment(lid, visited):
        for point in by_line[lid]:
            if point in visited:
                continue
            visited.add(point)
            previous=point_to_line[point]
            if previous < 0 or augment(previous,visited):
                point_to_line[point] = lid
                return True
        return False

    for lid in range(V):
        if not augment(lid,set()):
            raise AssertionError("Hall-perfect-matching construction failed")
    if set(point_to_line) != set(range(V)):
        raise AssertionError("perfect factor matching not bijective")
    result=[-1]*V
    for point,lid in enumerate(point_to_line):
        result[lid]=point
    if any((point,lid) not in set(edges) for lid,point in enumerate(result)):
        raise AssertionError("nonincident match violates the theorem")
    return tuple(result)


def incidence_matched_labeling(base_model):
    """An explicit, provably BAD correlated all-h pair-injection scheme."""
    pi=canonical_incidence_perfect_matching(base_model)
    model=dict(base_model)
    model["right_labels"]=tuple(base_model["left_labels"][pi[l]]
                                for l in range(len(pi)))
    model["scheme"]="incidence-perfect-matching-aligned"
    model["matching_line_to_point"]=pi
    check_input(model)
    return model


def finite_report():
    """Only GF2/GF4 executable controls; all-h theorem above is symbolic."""
    cases=[]
    for h in (1,2):
        original=pair_labeled_symplectic(h,"lex")
        aligned=incidence_matched_labeling(original)
        bound=forced_sixcycles_lower(original["s"])
        left_cycles=sum(1 for _ in physical_six_cycles(
            original["left_labels"],original["a"]))
        exact=exact_coincident_c6(aligned)
        if not (exact["exact_coincident_C6_factor_matchings_D"]
                >= left_cycles >= bound["unconditional_C6_lower"]):
            raise AssertionError("restricted all-h no-go finite falsifier")
        cases.append({
            "h":h,"s":original["s"],"a":original["a"],"N":original["N"],
            "left_physical_C6_exact":left_cycles,
            "mathematical_absolute_C6_lower":bound["unconditional_C6_lower"],
            "exact_incidence_matched_D":exact[
                "exact_coincident_C6_factor_matchings_D"],
            "exact_GF5_C6_event_weight":exact_alternating_cycle_weight(),
            "fixed_label_R3_lower":"5643*D/51^6",
            "strict_R3_exponent_possible_in_this_class":False,
        })
    return {"scope":"all-h restricted mathematical no-go; executable h=1,2",
            "cases":cases,"no_global_ASET_no_go":True}


if __name__=="__main__":
    print(json.dumps(finite_report(),sort_keys=True,indent=2))
