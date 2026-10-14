"""Coherent paired-diagonal G* regularization for ORIGINAL W(3,2^h).

All-h analytic density/min-active-degree theorem is in companion proof doc.
Finite graphs never pretend to meet a numerically useful delta*s threshold.
All decisions operate on ORIGINAL incidence IDs; no diagonal is dropped alone.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations

from hyp105_issue230_endpoint_energy import EndpointEnergy
from hyp105_issue230_proof_audit import parameters

POINT_DEGREE_LIMIT = 8
LINE_DEGREE_LIMIT = 160
PEEL_DELTA = Fraction(1, 1_000_000)


def all_h_certificate(s):
    """Exact finite arithmetic sanity check; symbolic forall-h proof is in docs."""
    if type(s) is not int or s < 64 or s & (s - 1):
        raise ValueError('certificate requires s=2^h>=64')
    p = parameters(s)
    V, a, N = p['V'], p['a'], p['V'] * p['Delta']
    C = (s - 1) * V + (s*s + 1) * (a - 1)
    if 2*C > 3*N or a*a > 4*s**3:
        raise AssertionError('uniform spectrally derived envelope failed')
    first = Fraction(N, 24)
    second = Fraction(11*N, 153120)
    third = second / 4
    edges_before_peel = 2*third
    edges_after_peel = edges_before_peel - 2*PEEL_DELTA*s*a*a
    if edges_after_peel <= Fraction(s**4, 40000):
        raise AssertionError('proposed fixed positive density gate invalid')
    return dict(s=s, a=a, V=V, N=N, spectral_source_cap=C,
                spectral_ratio=str(Fraction(C, N)),
                source_stage1_lower=str(first),
                source_stage2_lower=str(second),
                source_two_bichromatic_cuts_lower=str(third),
                paired_edges_after_peeling_lower=str(edges_after_peel),
                requested_edges_lower=str(Fraction(s**4, 40000)),
                degree_factor=str(PEEL_DELTA), universal_s_lower_proved=False)


def _matching_pass(ids, inc, labels, group_index, label_index, degree_limit):
    """At each ORIGINAL source pencil remove heavy pair endpoints then greedily match."""
    groups = defaultdict(list)
    for i in ids:
        groups[inc[i][group_index]].append(i)
    selected = []
    heavy = 0
    collisions = 0
    for original_factor in sorted(groups):
        rows = sorted(groups[original_factor])
        degrees = Counter(coord for i in rows for coord in labels[inc[i][label_index]])
        collisions += sum(n*(n-1)//2 for n in degrees.values())
        used = set()
        for i in rows:
            u, v = labels[inc[i][label_index]]
            if degrees[u] > degree_limit or degrees[v] > degree_limit:
                heavy += 1
                continue
            if u in used or v in used:
                continue
            selected.append(i)
            used.update((u, v))
    if heavy * degree_limit > 2 * collisions:
        raise AssertionError('source book-energy heavy deletion bound violated')
    if len(selected)*(2*degree_limit-1) < len(ids)-heavy:
        raise AssertionError('greedy matching lower bound violated')
    return tuple(sorted(selected)), {
        'input': len(ids), 'survivors': len(selected),
        'high_degree_deleted': heavy, 'collision_energy': collisions,
        'degree_limit': degree_limit,
        'guaranteed_matching_floor': str(Fraction(len(ids), 2*degree_limit-1) -
                    Fraction(2*collisions, degree_limit*(2*degree_limit-1))),
    }


def _conditional_cut(ids, inc, labels, label_index, a):
    """Deterministic conditional-expectation maxcut with weighted source labels."""
    edge_weights = Counter(labels[inc[i][label_index]] for i in ids)
    attached = [[] for _ in range(a)]
    for (u, v), w in edge_weights.items():
        attached[u].append((v, w))
        attached[v].append((u, w))
    colors = [-1] * a
    for v in range(a):
        to_zero = sum(w for u, w in attached[v] if colors[u] == 1)
        to_one = sum(w for u, w in attached[v] if colors[u] == 0)
        colors[v] = 0 if to_zero >= to_one else 1
    kept = tuple(i for i in ids if colors[labels[inc[i][label_index]][0]] !=
                 colors[labels[inc[i][label_index]][1]])
    if 2*len(kept) < len(ids):
        raise AssertionError('conditional expectation cut below half of source weight')
    return kept, tuple(colors)


def _graph(inc, f, g, ids, a):
    adj = [set() for _ in range(a*a)]
    provenance = {}
    for i in ids:
        q, r = inc[i]
        x0, x1 = f[q]
        y0, y1 = g[r]
        for u,v in ((x0*a+y0, x1*a+y1), (x0*a+y1, x1*a+y0)):
            edge = tuple(sorted((u,v)))
            if edge in provenance:
                raise AssertionError('duplicate diagonal or original incidence collision')
            provenance[edge] = i
            adj[u].add(v)
            adj[v].add(u)
    if len(provenance) != 2*len(ids):
        raise AssertionError('both original incidence diagonals not preserved')
    return adj, provenance


def _paired_peel(ids, inc, f, g, a, threshold):
    """Delete both diagonals of every incidence touching any underdegree vertex."""
    ids = set(ids)
    iterations = 0
    while ids:
        adj, prov = _graph(inc, f, g, sorted(ids), a)
        degrees = [len(neigh) for neigh in adj]
        low = {u for u, d in enumerate(degrees) if 0 < d < threshold}
        if not low:
            break
        victims = {prov[tuple(sorted((u,v)))] for u in low for v in adj[u]}
        if not victims or len(victims) > sum(degrees[u] for u in low):
            raise AssertionError('paired low-degree removal audit failed')
        ids.difference_update(victims)
        iterations += 1
    return tuple(sorted(ids)), iterations


def verify_paired_regularizer(model, ids, colors_left, colors_right, *,
                              require_paths=False, walk_budget=3_000_000):
    """Independent physical graph proof oracle, with original incidence provenance."""
    ctx = EndpointEnergy(model, selected=ids)
    a, adj = ctx.a, ctx.adj
    for i in ids:
        p,l = ctx.inc[i]
        x0,x1=ctx.f[p]
        y0,y1=ctx.g[l]
        if colors_left[x0] == colors_left[x1] or colors_right[y0] == colors_right[y1]:
            raise AssertionError('unbichromatic original incidence survived')
    by_point = defaultdict(set)
    by_line = defaultdict(set)
    for i in ids:
        p, l = ctx.inc[i]
        for y in ctx.g[l]:
            if y in by_point[p]:
                raise AssertionError('original point has physical right cherry')
            by_point[p].add(y)
        for x in ctx.f[p]:
            if x in by_line[l]:
                raise AssertionError('original line has physical left cherry')
            by_line[l].add(x)
    for u, ns in enumerate(adj):
        if len({divmod(v,a)[0] for v in ns}) != len(ns):
            raise AssertionError('physical block-row degree >1')
        if len({divmod(v,a)[1] for v in ns}) != len(ns):
            raise AssertionError('physical block-column degree >1')
    for u,ns in enumerate(adj):
        for v in ns:
            if colors_left[u//a] == colors_left[v//a]:
                raise AssertionError('physical bipartiteness failed')
    if require_paths:
        bound = sum((len(adj[v])-1)*(len(adj[w])-1)
                    for v,ns in enumerate(adj) for w in ns)
        if bound > walk_budget:
            raise ValueError('path proof budget exceeded')
        for u,ns in enumerate(adj):
            for v in ns:
                for w in adj[v]-{u}:
                    for z in adj[w]-{v}:
                        if len({u//a,v//a,w//a,z//a}) != 4 or len({
                                u%a,v%a,w%a,z%a}) != 4:
                            raise AssertionError('improper nonbacktracking length3 path')
    return dict(physical_vertices=a*a, physical_edges=len(ctx.provenance),
                min_positive_degree=min((len(x) for x in adj if x), default=0),
                maximum_degree=max(map(len,adj),default=0),
                both_diagonals=len(ctx.provenance)==2*len(ids))


def paired_gstar(model, *, min_degree=None, verify_paths=False,
                 verification_budget=3_000_000):
    """Source-pair-coherent deterministic original incidence selection.

    Default threshold = delta*s. A separate finite integer threshold can
    be used for falsification but is NOT covered by the density theorem.
    """
    context=EndpointEnergy(model)
    inc, f, g, a, s = context.inc,context.f,context.g,context.a,context.s
    if min_degree is not None and (type(min_degree) is not int or min_degree < 0):
        raise ValueError('nonnegative integer min_degree required')
    all_ids=tuple(range(context.N))
    first,diag1=_matching_pass(all_ids,inc,g,0,1,POINT_DEGREE_LIMIT)
    second,diag2=_matching_pass(first,inc,f,1,0,LINE_DEGREE_LIMIT)
    bleft,colors_left=_conditional_cut(second,inc,f,0,a)
    bright,colors_right=_conditional_cut(bleft,inc,g,1,a)
    threshold=PEEL_DELTA*s if min_degree is None else min_degree
    final,iterations=_paired_peel(bright,inc,f,g,a,threshold)
    details=verify_paired_regularizer(model,final,colors_left,colors_right,
                                     require_paths=verify_paths,
                                     walk_budget=verification_budget)
    if details['min_positive_degree'] and details['min_positive_degree'] < threshold:
        raise AssertionError('minimum active degree certificate violated')
    return {
        's':s, 'a':a, 'N':context.N,
        'original_incidence_ids':list(final),
        'stage1_original_count':len(first),
        'stage2_original_count':len(second),
        'stage3_left_color_count':len(bleft),
        'stage4_both_colors_count':len(bright),
        'final_original_count':len(final),
        'removed_by_paired_peeling':len(bright)-len(final),
        'peeling_iterations':iterations,
        'peel_threshold':str(threshold),
        'colors_left':list(colors_left), 'colors_right':list(colors_right),
        'first_stage':diag1, 'second_stage':diag2,
        'graph':details,
        'uniform_theorem_applicable':s >= 64 and min_degree is None,
        'universal_S_lower_proved':False
    }


def report():
    from hyp105_issue230_projection import fixture
    rows=[]
    for scheme in ('lex','reverse','S68','S72'):
        result=paired_gstar(fixture(1,scheme),verify_paths=True)
        rows.append({k:v for k,v in result.items() if k not in (
            'original_incidence_ids','colors_left','colors_right') } | {'scheme':scheme})
    return {'status':'RESTRICTED_THEOREM_C',
            'scope':'finite ORIGINAL W32 coherent G*; asymptotic theorem separately proved',
            'root_proved_A':False,'models':rows}


if __name__ == '__main__':
    import json
    print(json.dumps(report(),indent=2,sort_keys=True))
