"""Exact original-GQ endpoint/interior collision energy. Research only.

For reversible non-backtracking path law mu: theta_I^2 <= 16N(E_f+E_g).
This is NOT a universal lower bound on S. Full-G diagnostics are NOT G*.
"""
from collections import defaultdict
from fractions import Fraction


def _pair_map(labels, a, n, name):
    try:
        result = tuple(tuple(x) for x in labels)
    except (TypeError, ValueError) as exc:
        raise ValueError(f'{name} requires canonical pairs') from exc
    if (len(result) != n or len(set(result)) != n or any(
            len(t) != 2 or any(type(z) is not int for z in t)
            or not (0 <= t[0] < t[1] < a) for t in result)):
        raise ValueError(f'{name} must be a global injective canonical pair map')
    return result


class EndpointEnergy:
    """Complete globally injected original-GQ model; both diagonals retained."""

    def __init__(self, model, selected=None):
        from hyp105_issue230_proof_audit import parameters
        p = parameters(model['s'])
        self.s, self.a, self.v = p['s'], p['a'], p['V']
        self.N = p['V'] * p['Delta']
        if self.v > 600 or model['a'] != self.a:
            raise ValueError('finite original model exceeds budget or is nonminimal')
        self.f = _pair_map(model['left_labels'], self.a, self.v, 'left')
        self.g = _pair_map(model['right_labels'], self.a, self.v, 'right')
        self.fi = {label: i for i, label in enumerate(self.f)}
        self.gi = {label: i for i, label in enumerate(self.g)}
        self.inc = tuple(tuple(edge) for edge in model['incidences'])
        if (len(self.inc) != self.N or len(set(self.inc)) != self.N or
                any(len(e) != 2 or any(type(z) is not int or z < 0 or z >= self.v for z in e)
                    for e in self.inc)):
            raise ValueError('complete unique original incidence IDs required')
        self.line_points = [set() for _ in range(self.v)]
        self.point_lines = [set() for _ in range(self.v)]
        for q, r in self.inc:
            self.line_points[r].add(q)
            self.point_lines[q].add(r)
        if any(len(x) != p['Delta'] for x in self.line_points + self.point_lines):
            raise ValueError('original factor degree must be s+1')
        self.edge_id = {e: i for i, e in enumerate(self.inc)}
        self.anchor = {}
        for q, q_lines in enumerate(self.point_lines):
            for line in q_lines:
                for point in self.line_points[line] - {q}:
                    for r in self.point_lines[point] - {line}:
                        if (q, r) in self.edge_id or (q, r) in self.anchor:
                            raise ValueError('unique GQ projection violated')
                        self.anchor[q, r] = point, line
        if len(self.anchor) != self.v * self.v - self.N:
            raise ValueError('GQ projection incomplete')
        self.Cf = {(r, x) for r, points in enumerate(self.line_points)
                   for q in points for x in self.f[q]}
        self.Cg = {(q, y) for q, lines in enumerate(self.point_lines)
                   for r in lines for y in self.g[r]}
        if len(self.Cf) > 2*self.N or len(self.Cg) > 2*self.N:
            raise AssertionError('source-coordinate capacity impossible')

        chosen = tuple(range(self.N)) if selected is None else tuple(selected)
        if len(set(chosen)) != len(chosen) or any(
                type(i) is not int or i < 0 or i >= self.N for i in chosen):
            raise ValueError('selected entries must be distinct genuine incidence IDs')
        self.selected = chosen
        self.adj = [set() for _ in range(self.a*self.a)]
        self.provenance = {}
        for i in chosen:
            q, r = self.inc[i]
            x0, x1 = self.f[q]
            y0, y1 = self.g[r]
            for u, v in ((x0*self.a+y0, x1*self.a+y1),
                         (x0*self.a+y1, x1*self.a+y0)):
                e = tuple(sorted((u, v)))
                if e in self.provenance:
                    raise AssertionError('globally injected maps must give distinct diagonals')
                self.provenance[e] = i
                self.adj[u].add(v)
                self.adj[v].add(u)
        self.degree = [len(x) for x in self.adj]
        self.m = len(self.provenance)

    def _iter_nb(self, max_paths):
        if type(max_paths) is not int or max_paths < 1:
            raise ValueError('positive integer walk budget required')
        walked = 0
        for u, neigh in enumerate(self.adj):
            for v in neigh:
                if self.degree[v] <= 1:
                    continue
                for w in self.adj[v] - {u}:
                    if self.degree[w] <= 1:
                        continue
                    for z in self.adj[w] - {v}:
                        walked += 1
                        if walked > max_paths:
                            raise ValueError('complete nonbacktracking path budget exceeded')
                        yield (u, v, w, z), Fraction(
                            1, (self.degree[v]-1)*(self.degree[w]-1))

    def energy(self, *, max_paths=300_000, require_proper=False,
               require_min_degree_two=False, independent_oracle=False):
        """Exact reversible weighted path census.

        The stationary law has total raw weight 2m ONLY with active min
        degree >=2. A graph with leaves gives a conditioned-on-survival
        reversible law instead. This must NOT be substituted for G*.
        """
        active = [d for d in self.degree if d]
        if require_min_degree_two and (not active or min(active) < 2):
            raise ValueError('stationary NB law requires active min-degree >=2')
        nu_f, nu_g = defaultdict(Fraction), defaultdict(Fraction)
        pair_f, pair_g = defaultdict(list), defaultdict(list)
        Z = mass_i = mass_w = mass_bad = Fraction()
        npaths = proper_count = 0
        a = self.a
        for (u, v, w, z), weight in self._iter_nb(max_paths):
            npaths += 1
            Z += weight
            x0, y0 = divmod(u, a)
            x1, y1 = divmod(v, a)
            x2, y2 = divmod(w, a)
            x3, y3 = divmod(z, a)
            proper = (len({x0, x1, x2, x3}) == 4 and
                      len({y0, y1, y2, y3}) == 4)
            if not proper:
                mass_bad += weight
                if require_proper:
                    raise ValueError('NB walk is not coordinate-proper; invalid G*')
            else:
                proper_count += 1
            q = self.fi.get(tuple(sorted((x0, x3)))) if x0 != x3 else None
            r = self.gi.get(tuple(sorted((y0, y3)))) if y0 != y3 else None
            if r is not None:
                nu_f[r, x1] += weight
                if independent_oracle:
                    pair_f[r, x1].append(weight)
            if q is not None:
                nu_g[q, y1] += weight
                if independent_oracle:
                    pair_g[q, y1].append(weight)
            W = ((r is not None and ((r, x1) in self.Cf or (r, x2) in self.Cf))
                 or (q is not None and ((q, y1) in self.Cg or (q, y2) in self.Cg)))
            if W:
                mass_w += weight
            if proper and q is not None and r is not None and (q, r) in self.anchor:
                p, line = self.anchor[q, r]
                end_clean = (set(self.f[p]).isdisjoint(self.f[q]) and
                             set(self.g[line]).isdisjoint(self.g[r]))
                internal = (bool(set(self.f[p]) & {x1, x2}) or
                            bool(set(self.g[line]) & {y1, y2}))
                if end_clean and internal:
                    if not W:
                        raise AssertionError('internal mask must imply W')
                    mass_i += weight
        if not Z:
            raise ValueError('no non-backtracking length-three paths')
        if require_min_degree_two and Z != 2*self.m:
            raise AssertionError('stationary NB normalization must sum to 2m')
        Ef = sum((x/Z)**2 for x in nu_f.values())
        Eg = sum((x/Z)**2 for x in nu_g.values())
        theta_i, theta_w = mass_i/Z, mass_w/Z
        if theta_i > theta_w or theta_w**2 > 16*self.N*(Ef+Eg):
            raise AssertionError('endpoint-interior CS inequality violated')
        actual_cf = sum(x for pair, x in nu_f.items() if pair in self.Cf)
        actual_cg = sum(x for pair, x in nu_g.items() if pair in self.Cg)
        if (actual_cf**2 > len(self.Cf)*sum(x*x for x in nu_f.values()) or
                actual_cg**2 > len(self.Cg)*sum(x*x for x in nu_g.values())):
            raise AssertionError('source support Cauchy-Schwarz failed')
        if independent_oracle:
            # Independent ordered pairs of weighted paths: not square-of-histogram code.
            def collisions(rows):
                return sum(sum(w1*w2 for w1 in seq for w2 in seq)
                           for seq in rows.values()) / Z**2
            if (collisions(pair_f), collisions(pair_g)) != (Ef, Eg):
                raise AssertionError('independent path-pair collision oracle disagreed')
        return {
            's': self.s, 'a': a, 'original_incidences': self.N,
            'selected_original_incidences': len(self.selected),
            'physical_edges': self.m, 'nonbacktracking_walks': npaths,
            'proper_walks': proper_count, 'improper_nb_mass': str(mass_bad/Z),
            'raw_stationary_mass': str(Z), 'conditional_on_survival': Z != 2*self.m,
            'theta_internal_only': str(theta_i), 'theta_W': str(theta_w),
            'E_f': str(Ef), 'E_g': str(Eg),
            'scaled_energy_N': str(self.N*(Ef+Eg)),
            'necessary_threshold_fraction': '1/16',
            'C_f_size': len(self.Cf), 'C_g_size': len(self.Cg),
            'bound_thetaW_squared_minus_16NE': str(theta_w**2-16*self.N*(Ef+Eg)),
            'universal_S_lower_proved': False
        }


def report():
    from hyp105_issue230_projection import fixture
    rows = []
    for scheme in ('lex', 'reverse', 'S68', 'S72'):
        result = EndpointEnergy(fixture(1, scheme)).energy(independent_oracle=True)
        result['scheme'] = scheme
        rows.append(result)
    return {'status': 'RESTRICTED_THEOREM_C',
            'scope': 'full-graph W32 NB diagnostics; NOT regularized G*',
            'root_branch_A': 'OPEN', 'records': rows}


if __name__ == '__main__':
    import json
    print(json.dumps(report(), indent=2, sort_keys=True))
