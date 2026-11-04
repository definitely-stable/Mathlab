"""Certified finite source-ID hypergraph covers; independent of GF5 enumeration.

Every edge contains 4 or 6 DISTINCT original source IDs. An abstract
hitting set is necessary, but NOT sufficient for legal GF5 recoloring.
"""
from itertools import combinations
from collections import Counter


def normalize_edges(edges, n=425):
    out = set()
    for item in edges:
        ids = tuple(item)
        if len(ids) not in (4, 6) or len(set(ids)) != len(ids):
            raise ValueError("original event must contain 4 or 6 distinct IDs")
        if any(type(x) is not int or x < 0 or x >= n for x in ids):
            raise ValueError("invalid ORIGINAL source ID")
        out.add(tuple(sorted(ids)))
    return tuple(sorted(out))


def covers(edges, ids):
    chosen = set(ids)
    return all(not chosen.isdisjoint(edge) for edge in edges)


def verify_disjoint_packing(edges, packing):
    valid = set(edges)
    seen = set()
    for e in packing:
        if tuple(e) not in valid or not seen.isdisjoint(e):
            raise AssertionError("invalid vertex-disjoint original event witness")
        seen.update(e)
    return len(packing)


def greedy_packing(edges, restarts=192):
    edges = normalize_edges(edges)
    if not edges:
        return ()
    if type(restarts) is not int or not 1 <= restarts <= 1024:
        raise ValueError("invalid packing restart budget")
    degree = Counter(v for e in edges for v in e)
    best = ()
    for seed in range(restarts):
        if seed % 3 == 0:
            order = sorted(edges, key=lambda e:
                (sum(degree[v] for v in e), len(e), e))
        elif seed % 3 == 1:
            order = sorted(edges, key=lambda e:
                (max(degree[v] for v in e), len(e),
                 sum((v+23)*(seed+1) for v in e) % 104729, e))
        else:
            order = sorted(edges, key=lambda e:
                (sum(((v+17)*(seed*2654435761+1)) & 0xffffffff for v in e)
                 & 0xffffffff, e))
        used = set()
        picked = []
        for e in order:
            if used.isdisjoint(e):
                picked.append(e)
                used.update(e)
        if len(picked) > len(best):
            best = tuple(picked)
    verify_disjoint_packing(edges, best)
    return best


def greedy_cover(edges, seed_cover=()):
    edges = normalize_edges(edges)
    if not edges:
        return ()
    candidate = set(seed_cover)
    if candidate and not covers(edges, candidate):
        raise ValueError("seed source IDs do not hit all events")
    while not covers(edges, candidate):
        uncovered = [e for e in edges if candidate.isdisjoint(e)]
        degree = Counter(v for e in uncovered for v in e)
        candidate.add(min(degree, key=lambda v: (-degree[v], v)))
    for v in sorted(candidate, reverse=True):
        if covers(edges, candidate-{v}):
            candidate.remove(v)
    return tuple(sorted(candidate))


def dominated_source_kernel(edges):
    """Exact unweighted transversal reduction using incidence containment.

    If incidence(v) is a subset of incidence(u), choosing u dominates
    choosing v for source-ID COVER purposes. A minimum cover exists
    without v. For equal incidence masks retain the least ORIGINAL ID.
    This is NOT a theorem about GF5 legal recoloring feasibility.
    """
    edges = normalize_edges(edges)
    masks = {v: sum(1<<j for j,e in enumerate(edges) if v in e)
             for e in edges for v in e}
    kept = []
    dropped = {}
    for v,m in sorted(masks.items()):
        dominators = [u for u,q in masks.items() if u!=v and
                      (m&q)==m and (m!=q or u<v)]
        if dominators:
            dropped[v]=min(dominators,
                           key=lambda u:(-masks[u].bit_count(),u))
        else:
            kept.append(v)
    if len(kept)+len(dropped)!=len(masks):
        raise AssertionError("original source incidence domination incomplete")
    if any(not any(v in e for v in kept) for e in edges):
        raise AssertionError("domination pruning deleted every representative")
    return tuple(kept),dropped


def bounded_exact_cover(edges, upper_cover, max_nodes=250000):
    """Exact original source-ID transversal or rigorous bounded interval.

    Exhaustive branching uses only nondominated flags: every deleted
    v has a certified incidence-superset witness u, so some minimum
    solution avoids v. Complete per-k UNSAT search validates lower.
    An incomplete depth NEVER increases the certified lower bound.
    """
    edges = normalize_edges(edges)
    cover = tuple(sorted(set(upper_cover)))
    if not covers(edges, cover):
        raise ValueError("not a valid upper-bound source cover")
    if type(max_nodes) is not int or max_nodes < 1:
        raise ValueError("positive exact solver budget required")
    if not edges:
        return dict(status="EXACT", lower=0, upper=0, cover=(), nodes=0,
                    exhausted_depths=(),original_active_ids=0,
                    nondominated_candidate_ids=0)
    kept,dropped=dominated_source_kernel(edges)
    masks = {v: sum(1<<j for j,e in enumerate(edges) if v in e)
             for v in kept}
    candidates = tuple(tuple(v for v in e if v in masks) for e in edges)
    if any(not group for group in candidates):
        raise AssertionError("source domination left an uncovered original event")
    base = len(greedy_packing(edges))
    full = (1<<len(edges))-1
    nodes = 0
    exhausted = False
    proved = []

    def decide(k):
        nonlocal nodes, exhausted
        memo = {}
        def search(remaining,slots):
            nonlocal nodes, exhausted
            nodes += 1
            if nodes>max_nodes:
                exhausted=True
                return None
            if remaining==0:
                return ()
            if slots<=0:
                return False
            if memo.get(remaining,-1)>=slots:
                return False
            active=[j for j in range(len(edges)) if remaining & (1<<j)]
            # Pairwise vertex-disjoint ORIGINAL event edges demand
            # distinct selected source IDs (safe packing lower bound).
            used=set()
            packing_lb=0
            for j in active:
                e=edges[j]
                if used.isdisjoint(e):
                    packing_lb+=1
                    used.update(e)
            degree=Counter(v for j in active for v in candidates[j])
            max_degree=max(degree.values())
            if max(packing_lb,
                   (len(active)+max_degree-1)//max_degree)>slots:
                memo[remaining]=slots
                return False
            # Branch on the smallest remaining NONDOMINATED source
            # options of one uncovered event. This is exhaustive after
            # the proved containment reduction, not a heuristic omission.
            pivot=min(active,key=lambda j:
                      (len(candidates[j]),
                       -sum(degree[v] for v in candidates[j]),j))
            for v in sorted(candidates[pivot],
                            key=lambda x:(-degree[x],x)):
                answer=search(remaining & ~masks[v],slots-1)
                if answer is None:
                    return None
                if answer is not False:
                    return (v,)+answer
            memo[remaining]=slots
            return False
        return search(full,k)

    for k in range(base,len(cover)+1):
        answer=decide(k)
        if answer is None:
            break
        if answer is False:
            proved.append(k)
        else:
            answer=tuple(sorted(set(answer)))
            if len(answer)>k or not covers(edges, answer):
                raise AssertionError("incomplete original cover claimed exact")
            return dict(status="EXACT",lower=len(answer),upper=len(answer),
                        cover=answer,nodes=nodes,
                        exhausted_depths=tuple(proved),
                        original_active_ids=len(kept)+len(dropped),
                        nondominated_candidate_ids=len(kept))
    if not exhausted:
        raise AssertionError("known true upper bound must be found")
    return dict(status="BOUNDED",
                lower=proved[-1]+1 if proved else base,
                upper=len(cover),cover=cover,nodes=nodes,
                exhausted_depths=tuple(proved),
                original_active_ids=len(kept)+len(dropped),
                nondominated_candidate_ids=len(kept))


def brute_force_min_cover(edges):
    """Independent subsets oracle; tiny source-ID fixtures only."""
    edges=normalize_edges(edges, n=10000)
    vertices=sorted(set(v for e in edges for v in e))
    if len(vertices)>14:
        raise ValueError("fixture too large for brute force")
    for k in range(len(vertices)+1):
        for xs in combinations(vertices,k):
            if covers(edges,xs):
                return xs
    raise AssertionError("finite hypergraphs have a cover")


def canonical_signed_partition(parts,k):
    if len(parts)!=2:
        raise ValueError("needs two original source subsets")
    a,b=(tuple(int(v) for v in part) for part in parts)
    if (len(a)!=k or len(b)!=k or
        tuple(sorted(a))!=a or tuple(sorted(b))!=b
        or not a<b or len(set(a+b))!=2*k
        or any(v<0 for v in a+b)):
        raise ValueError("not a disjoint canonical original signed event")
    return (a,b)
