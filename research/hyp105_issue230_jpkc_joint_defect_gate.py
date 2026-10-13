"""JPKC-001: same-map ORIGINAL projection and independent Kikuchi-energy ledger.

This is a FINITE, exact, fail-closed oracle on the PR #394 projection branch.
The all-h two-defect NECESSITY lemma is proved in the companion document.
No all-h JPKC dichotomy, seven-family lower, or ASET exponent is claimed.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb
import argparse
import json

from hyp105_issue230_projection import ProjectionClosure, fixture
from hyp105_g5e2b3e1b0_seven_signature import seven_census


def _graph(closure):
    """Independently materialize both ORIGINAL diagonals from the validated labels."""
    a = closure.a
    neighbors = [set() for _ in range(a*a)]
    for p, l in closure.edges:
        x, xp = closure.f[p]
        y, yp = closure.g[l]
        for u, v in ((x*a+y, xp*a+yp), (x*a+yp, xp*a+y)):
            if u == v or v in neighbors[u]:
                raise AssertionError("duplicated or degenerate original Kikuchi edge")
            neighbors[u].add(v)
            neighbors[v].add(u)
    if sum(map(len, neighbors)) != 4*len(closure.edges):
        raise AssertionError("exact two-diagonal incidence count failed")
    return tuple(frozenset(row) for row in neighbors)


def _path3_and_theta(adj):
    """Independent path-pair energy and K2 coincidence formula (no cycle census)."""
    n = len(adj)
    path_counts = Counter()
    for u in range(n):
        for b in adj[u]:
            for c in adj[b]:
                if c == u:
                    continue
                for v in adj[c]:
                    if v != b and v != u:
                        path_counts[(u, v)] += 1
    p3 = sum(path_counts.values())
    square = sum(k*k for k in path_counts.values())
    triangles = sum(
        1 for u in range(n) for v in adj[u] if v > u
        for w in adj[u].intersection(adj[v]) if w > v
    )
    codeg = Counter()
    for center in range(n):
        for u, v in combinations(sorted(adj[center]), 2):
            codeg[(u, v)] += 1
    degrees = tuple(map(len, adj))
    pendant = 0
    diamond = 0
    c4_double = 0
    for (u, v), c in codeg.items():
        pair = comb(c, 2)
        c4_double += pair
        touch = int(v in adj[u])
        pendant += 4*pair*(degrees[u]+degrees[v]-4-2*touch)
        if touch:
            diamond += 2*c*(c-1)
    if c4_double % 2:
        raise AssertionError("each 4-cycle must have two opposite pairs")
    bowties = 0
    for center in range(n):
        incident = [codeg[(min(center,u), max(center,u))] for u in adj[center]]
        triangles_center, parity = divmod(sum(incident), 2)
        if parity:
            raise AssertionError("triangle endpoint multiplicity not even")
        bowties += comb(triangles_center, 2) - sum(comb(x, 2) for x in incident)
    if min(pendant,diamond,bowties) < 0:
        raise AssertionError("K2 coincidence components cannot be negative")
    theta = pendant + diamond + 16*bowties
    numerator = square-p3-theta
    if numerator < 0 or numerator % 12:
        raise AssertionError("K2 3-path collision identity does not yield a C6 count")
    return {
        "P3":p3, "sum_P3_squared":square, "C3":triangles,
        "C4":c4_double//2, "Theta":theta,
        "Theta_pendant":pendant, "Theta_diamond":diamond,
        "Theta_bowtie":16*bowties, "C6_from_K2":numerator//12,
    }


def _cycles_independent(adj, a, *, max_cycles):
    """Direct graph DFS; each undirected simple C6 counted once by min/reversal."""
    if type(max_cycles) is not int or max_cycles < 1:
        raise ValueError("positive direct C6 budget required")
    total=proper=0
    types=Counter()
    for start in range(len(adj)):
        path=[start]
        used={start}
        def extend():
            nonlocal total,proper
            last=path[-1]
            if len(path)==6:
                if start in adj[last] and path[1]<last:
                    total+=1
                    if total>max_cycles:
                        raise ValueError("complete direct C6 budget exceeded")
                    xgood=len({v//a for v in path})==6
                    ygood=len({v%a for v in path})==6
                    types[("proper" if xgood and ygood else "improper")]+=1
                    proper+=int(xgood and ygood)
                return
            for nxt in adj[last]:
                if nxt<=start or nxt in used:
                    continue
                used.add(nxt)
                path.append(nxt)
                extend()
                path.pop()
                used.remove(nxt)
        extend()
    return {
        "C6_DFS":total, "D6_proper_DFS":proper,
        "C6_improper_DFS":total-proper,
        "cycle_types":dict(types),
    }


def joint_record(model, *, exact_cycles=True, seven=False, max_cycles=3_000_000):
    """Exact same complete f,g on both sides; no independently redrawn images."""
    ctx=ProjectionClosure(model)
    projection=ctx.census()
    adj=_graph(ctx)
    energy=_path3_and_theta(adj)
    a,s=ctx.a,ctx.s
    N=len(ctx.edges)
    degrees=[len(row) for row in adj]
    if sum(degrees)!=4*N:
        raise AssertionError("two incidence diagonals lost")
    d=Fraction(4*N, a*a)
    if d<3:
        raise AssertionError("K3 peeling monotonicity hypothesis not available")
    p3_floor=4*N*(d-1)**2-6*energy["C3"]
    if Fraction(energy["P3"])<p3_floor:
        raise AssertionError("known all-h K3 path floor violated")
    P3=energy["P3"]
    L=Fraction(P3)*(Fraction(P3,a**4)-1)
    if L<0:
        raise AssertionError("unexpected negative Cauchy-Schwarz source")
    out={
        "s":s, "a":a, "global_injections_both_sides":True,
        "original_incidence_count":N, "graph_edges":2*N,
        "graph_vertices":a*a, "max_graph_degree":max(degrees),
        "projection":{k:projection[k] for k in (
            "proper_P3","missing","incident","blocked",
            "blocked_left","blocked_right","blocked_both",
            "unblocked","synchronized_BBo")},
        "kikuchi":energy,
        "P3_K3_floor_exact":str(p3_floor),
        "L_P3_exact":str(L),
        "P3_Cauchy_Schwarz_slack_exact":
            str(Fraction(energy["sum_P3_squared"])-Fraction(P3*P3,a**4)),
        "direct_C6_exhaustive":bool(exact_cycles),
        "universal_A_proved":False,
        "counterexample_B_proved":False,
    }
    if exact_cycles:
        cycles=_cycles_independent(adj,a,max_cycles=max_cycles)
        if cycles["C6_DFS"] != energy["C6_from_K2"]:
            raise AssertionError("K2 C6 algebra differs from independent DFS")
        D6=cycles["D6_proper_DFS"]
        improper=cycles["C6_improper_DFS"]
        k_defect=energy["Theta"]+12*improper
        k_gap=L-k_defect
        if 12*D6 < k_gap:
            raise AssertionError("Kikuchi proper-C6 conditional floor invalid")
        if k_defect < L-12*D6:
            raise AssertionError("Kikuchi defect necessary condition invalid")
        out["kikuchi"].update(cycles)
        out["joint"]={
            "full_graph_anchor_blocked_P3":projection["blocked"],
            "kikuchi_coincidence_plus_12_improper":k_defect,
            "kikuchi_exact_surplus_K":str(k_gap),
            "kikuchi_lower_bound_slack_exact":str(12*D6-k_gap),
            "blocked_is_full_G_not_retained_H":True,
            "finite_JPKC_dichotomy_proved":False,
        }
    if seven:
        if s!=2 or not exact_cycles:
            raise ValueError("complete original seven-family cross-check limited to W32")
        actual=seven_census(model,independent_checks=False)
        S=actual["S_seven"]
        D6=out["kikuchi"]["D6_proper_DFS"]
        if D6!=actual["seven_class_motif_counts"]["D6"]:
            raise AssertionError("Kikuchi proper C6 != original seven-census D6")
        if projection["synchronized_BBo"]>actual["seven_class_motif_counts"]["B/B-overlap"]:
            raise AssertionError("original geometric closure exceeds accepted BB class")
        if S<D6 or S<projection["synchronized_BBo"]:
            raise AssertionError("selected seven-S cannot be smaller than subclass")
        out["seven_original"]={
            "S":S,
            "seven_class_counts":actual["seven_class_motif_counts"],
            "selected_GF5_numerator":actual["GF5_seven_lower_numerator"],
            "exact_D6_and_BBo_subclass_reconciled":True,
        }
    return out


def report(*, include_w34=False):
    samples=[(1,"lex"),(1,"reverse"),(1,"S68"),(1,"S72")]
    if include_w34:
        samples.extend([(2,"lex"),(2,"random")])
    return {
        "scope":"finite true-GQ same-map PR394/Kikuchi JPKC falsification gate",
        "all_h_necessary_conditional_lemma_in_docs":True,
        "all_h_dichotomy_PROVED_A":False,
        "records":[dict(scheme=scheme,**joint_record(
            fixture(h,scheme),seven=(h==1))) for h,scheme in samples],
    }


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--w34",action="store_true")
    args=parser.parse_args()
    print(json.dumps(report(include_w34=args.w34),sort_keys=True,indent=2))
