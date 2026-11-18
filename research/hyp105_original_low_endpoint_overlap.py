"""AA4-LOW-ENDPOINT-OVERLAP: all-order exact ORIGINAL deletion overlap.

Assumes a genuine named incidence list of W(3,s); finite tests independently
check the axiom on true W(3,2), W(3,4). No inference from finite tests.
No dependence on earlier HYP-105 proof evaluators or GF5 classifiers.
"""
from collections import Counter, defaultdict
from itertools import combinations
from math import comb
import json

SCHEMA = 'mathlab.hyp105.original-low-endpoint-overlap.v1'


def _source(s, flags):
    if type(s) is not int or s < 2:
        raise ValueError('invalid order')
    V = (s + 1) * (s*s + 1)
    flags = tuple(flags)
    if len(flags) != (s+1)*V or len(set(flags)) != len(flags):
        raise ValueError('invalid ORIGINAL incidence flag count')
    bypoint = [set() for _ in range(V)]
    byline = [set() for _ in range(V)]
    for p, l in flags:
        if type(p) is not int or type(l) is not int or not (0 <= p < V and 0 <= l < V):
            raise ValueError('invalid ORIGINAL source index')
        bypoint[p].add(l)
        byline[l].add(p)
    if any(len(st) != s+1 for st in bypoint+byline):
        raise ValueError('not a regular source')
    return V, flags, bypoint, byline


def _deleted(flags, deleted):
    z = tuple(deleted)
    if len(z) != len(set(z)) or any(type(i) is not int or not (0 <= i < len(flags)) for i in z):
        raise ValueError('duplicate/invalid ORIGINAL deleted ID')
    return frozenset(z)


def exact_source_overlap(s, flags, deleted):
    """O(|I|+|Z|) deletion union with NO physical labeling assumptions.

    All-order mathematical identities proved in the companion manuscript.
    The existing #748 formula M=8s^2|Z|+4(D-H-F) is REUSED, not rediscovered.
    NEW: H+F=T_outer is a closed local quadratic incidence-degree form.
    """
    V, flags, _, _ = _source(s, flags)
    Z = _deleted(flags, deleted)
    dp = Counter(flags[i][0] for i in Z)
    dl = Counter(flags[i][1] for i in Z)
    incidence_quadratic = sum(dp[p]*dl[l] for p, l in flags)
    point_second = sum(d*d for d in dp.values())
    line_second = sum(d*d for d in dl.values())
    outer = (incidence_quadratic - line_second
             - sum(d*(d-1) for d in dp.values()))
    # Known W(3,s) incidence spectrum, applied to deletion degree vectors.
    centered = V*incidence_quadratic - (s+1)*len(Z)**2
    bound = 2*s*(V*point_second-len(Z)**2)*(V*line_second-len(Z)**2)
    spectral_slack = bound-centered**2
    if spectral_slack < 0:
        raise AssertionError('not a genuine GQ incidence-spectrum mask')
    defect = sum((s+1-dp[flags[i][0]])*(s+1-dl[flags[i][1]]) for i in Z)
    touched = 2*s*s*len(Z)-outer+defect
    if not (0 <= outer <= s*s*len(Z) and 0 <= defect <= s*s*len(Z)
            and 0 <= touched <= min(3*s*s*len(Z), V*(V-s-1))):
        raise AssertionError('SOURCE local counts outside genuine GQ bounds')
    star = all(dp[p] == s+1 or dl[l] == s+1 for i in Z for p,l in (flags[i],))
    if (defect == 0) != star:
        raise AssertionError('star iff source factorization failed')
    return {
        's': s, 'original_flags': len(flags), 'deleted': len(Z),
        'outer_overlap': outer, 'middle_only_defect': defect,
        'incidence_degree_quadratic': incidence_quadratic,
        'deleted_point_degree_second': point_second,
        'deleted_line_degree_second': line_second,
        'weighted_GQ_spectral_slack': spectral_slack,
        'touched_projections': touched, 'physical_deleted_endpoint_upper': 4*touched,
        'old_universal_upper': 12*s*s*len(Z),
        'old_defect_upper': 8*s*s*len(Z)+4*defect,
        'star_union': star,
    }


def projection_oracle(s, flags, deleted):
    """Independent FULL GQ (q,r) oracle: never calls exact_source_overlap."""
    V, flags, _, byline = _source(s, flags)
    Z = _deleted(flags, deleted)
    flagid = {pair:i for i,pair in enumerate(flags)}
    collinear = {}
    for l, points in enumerate(byline):
        for p,q in combinations(sorted(points), 2):
            if (p,q) in collinear:
                raise ValueError('two points have two common lines')
            collinear[p,q] = collinear[q,p] = l
    counts = Counter()
    roles = [[0]*len(flags) for _ in range(3)]
    for q in range(V):
        for r in range(V):
            if (q,r) in flagid:
                continue
            paths = [(p,collinear[q,p]) for p in byline[r] if (q,p) in collinear]
            if len(paths) != 1:
                raise ValueError('not a true GQ unique nonincident projection')
            p,l = paths[0]
            ids = (flagid[q,l],flagid[p,l],flagid[p,r])
            if len(set(ids)) != 3:
                raise AssertionError('projection has repeated ORIGINAL flags')
            for j,i in enumerate(ids):
                roles[j][i] += 1
            a,b,c = (i in Z for i in ids)
            counts['all'] += 1
            counts['first'] += int(a)
            counts['middle'] += int(b)
            counts['last'] += int(c)
            counts['outer'] += int(a and c)
            counts['middle_only'] += int(b and not a and not c)
            counts['union'] += int(a or b or c)
    if counts['all'] != V*(V-s-1) or any(
        any(v != s*s for v in role) for role in roles):
        raise AssertionError('GQ original role multiplicity failed')
    return dict(counts)


def outer_dual_oracles(s, flags, deleted):
    """Two different source-first original outer-pair counts, no (q,r) scan."""
    _, flags, bypoint, byline = _source(s, flags)
    Z = _deleted(flags, deleted)
    dp = Counter(flags[i][0] for i in Z)
    dl = Counter(flags[i][1] for i in Z)
    id_of = {fl:i for i,fl in enumerate(flags)}
    first = sum(sum(dp[p] - int(id_of[p,l] in Z)
                    for p in byline[l] if p != q)
                for i in Z for q,l in (flags[i],))
    last = sum(sum(dl[l] - int(id_of[p,l] in Z)
                   for l in bypoint[p] if l != r)
               for i in Z for p,r in (flags[i],))
    return first, last


def label_endpoint_oracle(s, flags, deleted, f, g):
    """Independent real ORIGINAL f/g-correlated source endpoint census.

    O(V^2) finite referee ONLY; not an all-h computational bound.
    """
    V, flags, _, byline = _source(s, flags)
    Z = _deleted(flags, deleted)
    f = tuple(tuple(sorted(pair)) for pair in f)
    g = tuple(tuple(sorted(pair)) for pair in g)
    if len(f) != V or len(g) != V or len(set(f)) != V or len(set(g)) != V:
        raise ValueError('complete separately injected original labels required')
    pool = set(combinations(range(next((a for a in range(2,2*V+2)
                                   if comb(a,2) >= V))),2))
    if any(len(set(x)) != 2 or x not in pool for x in f+g):
        raise ValueError('physical pair label invalid or outside minimal alphabet')
    flagid = {pair:i for i,pair in enumerate(flags)}
    collinear = {}
    for l, points in enumerate(byline):
        for p,q in combinations(sorted(points),2):
            collinear[p,q] = collinear[q,p] = l
    ef = sum(bool(set(f[p])&set(f[q])) for p,q in
             {tuple(sorted((p,q))) for l,pts in enumerate(byline)
              for p,q in combinations(sorted(pts),2)})
    bypoint = [[] for _ in range(V)]
    for p,l in flags: bypoint[p].append(l)
    eg = sum(bool(set(g[l])&set(g[r])) for l,r in
             {tuple(sorted((l,r))) for ls in bypoint
              for l,r in combinations(sorted(ls),2)})
    X = Y = XY = Zany = Zbad = 0
    for q in range(V):
        for r in range(V):
            if (q,r) in flagid: continue
            paths = [(p,collinear[q,p]) for p in byline[r] if (q,p) in collinear]
            if len(paths) != 1: raise ValueError('invalid GQ projection')
            p,l = paths[0]
            x = bool(set(f[q])&set(f[p]))
            y = bool(set(g[r])&set(g[l]))
            z = any(flagid[k] in Z for k in ((q,l),(p,l),(p,r)))
            X += x; Y += y; XY += x and y
            Zany += z; Zbad += z and (x or y)
    if X != 2*s*ef or Y != 2*s*eg:
        raise AssertionError('source endpoint collision multiplicity false')
    B = comb(next(a for a in range(2,2*V+2) if comb(a,2)>=V),2)
    nonz_bad = X + Y - XY
    bad_projection = nonz_bad + Zany - Zbad
    return {'X':X, 'Y':Y, 'XY':XY, 'Z':Zany, 'Z_and_endbad':Zbad,
            'endbad_union':nonz_bad, 'bad_projection_union':bad_projection,
            'physical_bad_endpoint_total':4*(B*B-V*V+len(flags)+bad_projection),
            'physical_total_offcoordinate_endpoints':4*B*B,
            'physical_good_endpoint_total':4*(V*V-len(flags)-bad_projection),
            'original_collinear_point_collisions':ef,
            'original_collinear_line_collisions':eg}


def canonical_certificate():
    """Checks two genuine W(3,s) fixtures; NOT proof by extrapolation."""
    from hyp105_original_defect_factor_referee import genuine_symplectic_source, _cases
    rows=[]
    for s in (2,4):
        flags=genuine_symplectic_source(s)
        for name,Z in _cases(s,flags).items():
            l=exact_source_overlap(s,flags,Z)
            oracle=projection_oracle(s,flags,Z)
            x,y=outer_dual_oracles(s,flags,Z)
            if (l['outer_overlap'] != oracle['outer'] or
                l['outer_overlap'] != x or x != y or
                l['middle_only_defect'] != oracle['middle_only'] or
                l['touched_projections'] != oracle['union']):
                raise AssertionError('three independent ORIGINAL oracles disagree')
            rows.append({'s':s,'case':name,'Z':len(Z),'outer':x,
                         'D':l['middle_only_defect'],'U':l['touched_projections'],
                         'star':l['star_union']})
    return {'schema':SCHEMA,'issue':230,'parent_pr':772,
            'status':'OPEN_WITH_FORMAL_BLOCKER','root_PROVED_A':False,
            'universal_Cheeger_equality_claimed':False,
            'all_order_source_identity_proved_in_manuscript':True,
            'prior_748_equivalent_union_identity_acknowledged':True,
            'finite_verified_orders':[2,4],'rows':rows}


if __name__ == '__main__':
    print('AA4_LOW_ENDPOINT_OVERLAP_CERTIFICATE='+json.dumps(
        canonical_certificate(),sort_keys=True,separators=(',',':')))
