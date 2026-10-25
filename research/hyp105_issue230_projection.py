"""Exact original-GQ projection closure of synchronized physical three-paths.

The accompanying asymptotic theorem counts >=(16-o(1))*s^6 paths for every
global pair injection. This oracle distinguishes the still-unproved closure
gate; it never promotes a path count to a universal seven-family bound.
No seven-family classifier, palette count or random-mean transfer enters
the path enumeration or unique-projection reconstruction.
"""
from collections import Counter
from itertools import combinations
import json
import random

from hyp105_issue230_proof_audit import parameters, frozen_model, _geometry, _model


class ProjectionClosure:
    """Finite full-GQ validation and definition-level physical path enumeration."""
    def __init__(self, model):
        p = parameters(model['s'])
        self.s, self.a, self.v, self.delta = p['s'], p['a'], p['V'], p['Delta']
        if self.v > 600:
            raise ValueError('projection oracle capped at V<=600')
        if model['a'] != self.a:
            raise ValueError('minimal physical alphabet required')

        def pair_map(name):
            labels = tuple(tuple(e) for e in model[name])
            if (len(labels) != self.v or len(set(labels)) != self.v
                    or any(len(e) != 2 or any(isinstance(x, bool) or not isinstance(x, int)
                                             for x in e)
                           or not 0 <= e[0] < e[1] < self.a for e in labels)):
                raise ValueError('complete injective canonical physical pair map required')
            return labels

        self.f, self.g = pair_map('left_labels'), pair_map('right_labels')
        self.fi = {e: q for q, e in enumerate(self.f)}
        self.gi = {e: r for r, e in enumerate(self.g)}
        self.edges = tuple(tuple(e) for e in model['incidences'])
        if (len(self.edges) != self.v*self.delta or len(set(self.edges)) != len(self.edges)
                or any(len(e) != 2 or any(isinstance(x, bool) or not isinstance(x, int)
                                         or not 0 <= x < self.v for x in e)
                       for e in self.edges)):
            raise ValueError('distinct complete original incidences required')
        self.edge_id = {e: i for i, e in enumerate(self.edges)}
        self.lines = [set() for _ in range(self.v)]
        self.point_lines = [set() for _ in range(self.v)]
        for q, l in self.edges:
            self.lines[l].add(q)
            self.point_lines[q].add(l)
        if any(len(x) != self.delta for x in self.lines+self.point_lines):
            raise ValueError('original regularity invalid')
        meetings = set()
        for neighbors in self.point_lines:
            for pair in combinations(sorted(neighbors), 2):
                if pair in meetings:
                    raise ValueError('original partial linearity violated')
                meetings.add(pair)
        self.projection = {}
        for q, neighbors in enumerate(self.point_lines):
            for l in neighbors:
                for p in self.lines[l]-{q}:
                    for r in self.point_lines[p]-{l}:
                        if (q, r) in self.edge_id or (q, r) in self.projection:
                            raise ValueError('original GQ projection axiom violated')
                        self.projection[q, r] = p, l
        if len(self.projection) != self.v**2-len(self.edges):
            raise ValueError('original GQ projection axiom incomplete')

        self.adj = [[] for _ in range(self.a**2)]
        seen = set()
        for i, (p, l) in enumerate(self.edges):
            u, v = self.f[p]
            x, y = self.g[l]
            for b, c in ((u*self.a+x, v*self.a+y), (u*self.a+y, v*self.a+x)):
                edge = tuple(sorted((b, c)))
                if edge in seen:
                    raise AssertionError('injective pair labels must give distinct diagonals')
                seen.add(edge)
                self.adj[b].append((c, i))
                self.adj[c].append((b, i))

    def original_cubic_counts(self):
        """Count ALL original length-three walks, including backtracking."""
        counts = Counter()
        for q, neighbors in enumerate(self.point_lines):
            for l in neighbors:
                for p in self.lines[l]:
                    counts.update((q, r) for r in self.point_lines[p])
        return counts

    def census(self, *, max_paths=20_000_000, collect_witnesses=False):
        if isinstance(max_paths, bool) or not isinstance(max_paths, int) or max_paths < 0:
            raise ValueError('nonnegative integer path budget required')
        degrees = tuple(map(len, self.adj))
        walk_bound = sum((degrees[u]-1)*(degrees[v]-1)
                         for u, neighbors in enumerate(self.adj) for v, _ in neighbors)
        if walk_bound > max_paths:
            raise ValueError('complete physical path budget exceeded')
        counts = Counter()
        witness_counts = Counter() if collect_witnesses else None
        a = self.a
        for u, neighbors in enumerate(self.adj):
            x0, y0 = divmod(u, a)
            for v, e1 in neighbors:
                x1, y1 = divmod(v, a)
                for w, e2 in self.adj[v]:
                    x2, y2 = divmod(w, a)
                    if x2 in (x0, x1) or y2 in (y0, y1):
                        continue
                    for z, e3 in self.adj[w]:
                        x3, y3 = divmod(z, a)
                        if x3 in (x0, x1, x2) or y3 in (y0, y1, y2):
                            continue
                        counts['proper_P3'] += 1
                        q = self.fi.get(tuple(sorted((x0, x3))))
                        r = self.gi.get(tuple(sorted((y0, y3))))
                        if q is None or r is None:
                            counts['missing'] += 1
                            continue
                        if (q, r) in self.edge_id:
                            counts['incident'] += 1
                            continue
                        p, l = self.projection[q, r]
                        left = bool(set(self.f[p]) & {x0, x1, x2, x3})
                        right = bool(set(self.g[l]) & {y0, y1, y2, y3})
                        if left or right:
                            counts['blocked'] += 1
                            counts['blocked_left'] += left
                            counts['blocked_right'] += right
                            counts['blocked_both'] += left and right
                            continue
                        counts['unblocked'] += 1
                        if witness_counts is not None:
                            six = tuple(sorted((e1, e2, e3, self.edge_id[p, r],
                                                self.edge_id[p, l], self.edge_id[q, l])))
                            if len(set(six)) != 6:
                                raise AssertionError('unblocked closure must use six distinct incidences')
                            witness_counts[six] += 1
        keys = ('proper_P3', 'missing', 'incident', 'blocked', 'unblocked',
                'blocked_left', 'blocked_right', 'blocked_both')
        result = {k: counts[k] for k in keys}
        if result['proper_P3'] != sum(result[k] for k in keys[1:5]):
            raise AssertionError('proper paths must have exactly one closure status')
        if result['unblocked'] % 2:
            raise AssertionError('every synchronized BB path has its reverse')
        if witness_counts is not None and any(n != 2 for n in witness_counts.values()):
            raise AssertionError('original synchronized BB sixsets have exact multiplicity two')
        result.update({'s': self.s, 'a': a, 'original_incidences': len(self.edges),
                       'diagonal_edges': sum(degrees)//2, 'max_degree': max(degrees),
                       'unrestricted_path_budget_bound': walk_bound,
                       'synchronized_BBo': result['unblocked']//2,
                       'universal_S_lower_proved': False})
        if witness_counts is not None:
            result['witness_multiplicities'] = dict(witness_counts)
        return result


def fixture(power, scheme):
    if power == 1:
        return frozen_model(scheme)
    if power not in (2, 3) or scheme not in ('lex', 'random'):
        raise ValueError('finite fixtures require powers 1/2/3 and a known scheme')
    _, points, lines, incidences = _geometry(power)
    s = 2**power
    pairs = tuple(combinations(range(parameters(s)['a']), 2))
    f, g = list(pairs), list(pairs)
    if scheme == 'random':
        rng = random.Random(230+power)
        rng.shuffle(f)
        rng.shuffle(g)
    return _model(s, points, lines, incidences, f[:len(points)], g[:len(lines)])


def report():
    records = []
    for power, schemes in ((1, ('lex', 'reverse', 'S68', 'S72')),
                            (2, ('lex', 'random')), (3, ('lex', 'random'))):
        for scheme in schemes:
            row = ProjectionClosure(fixture(power, scheme)).census()
            row['scheme'] = scheme
            records.append(row)
    return {'scope': 'exact full ORIGINAL GQ projection gate; finite data are not Branch A/B',
            'oriented_unblocked_path_to_sixset_multiplicity': 2,
            'uniform_endpoint_complete_P3_asymptotic_lower_constant': 16,
            'universal_S_lower_proved': False, 'records': records}


if __name__ == '__main__':
    print(json.dumps(report(), indent=2, sort_keys=True))
