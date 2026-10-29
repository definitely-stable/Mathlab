"""Finite, original-source falsifiers for the universal sextic proof.

These exact computations check identities and the B/B-overlap subcount.
They are not computational verification of an all-h asymptotic theorem.
"""
from collections import Counter
from itertools import combinations
import json
from pathlib import Path
import sys

from hyp105_full_physical_degree_tail import genuine_source, physical, conflict_graph
from hyp105_physical_degree_energy import minimal_alphabet, _verify_typed_injections
from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked
from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic


def walk_matrix(adjacency, length):
    """Sparse integer walk matrix; isolated vertices need not be stored."""
    if type(length) is not int or length < 0:
        raise ValueError("nonnegative integer length required")
    result = {u: Counter({u: 1}) for u in adjacency}
    for _ in range(length):
        following = {}
        for u, row in result.items():
            out = Counter()
            for v, count in row.items():
                for w in adjacency[v]:
                    out[w] += count
            following[u] = out
        result = following
    return result


def square_norm(matrix):
    return sum(value * value for row in matrix.values() for value in row.values())


def simple_sixcycles(adjacency):
    """Independent direct DFS; unoriented, unrooted simple cycles."""
    result = 0

    def visit(path):
        nonlocal result
        if len(path) == 6:
            result += path[0] in adjacency[path[-1]] and path[1] < path[-1]
            return
        for w in adjacency[path[-1]]:
            if w > path[0] and w not in path:
                visit(path + (w,))

    for u in adjacency:
        visit((u,))
    return result


def finite_source_certificate(power, f, g, core_ids=None):
    s, V, flags = genuine_source(power)
    a, d = minimal_alphabet(V), s + 1
    f, g = tuple(map(tuple, f)), tuple(map(tuple, g))
    _verify_typed_injections(a, V, f, g)
    ids = tuple(range(len(flags))) if core_ids is None else tuple(core_ids)
    if (len(set(ids)) != len(ids) or
            any(type(i) is not int or not 0 <= i < len(flags) for i in ids)):
        raise ValueError("distinct valid original source IDs required")
    ids = tuple(sorted(ids))
    source_ids = set(ids)
    full, _ = physical(range(len(flags)), flags, f, g)
    core, provenance = physical(ids, flags, f, g)
    delta = max(map(len, core.values()), default=0)
    conflict, mf, mg = conflict_graph(ids, flags, f, g)
    cap = max(map(len, conflict.values()), default=0)
    point_lines = [set() for _ in range(V)]
    line_points = [set() for _ in range(V)]
    for p, ell in flags:
        point_lines[p].add(ell)
        line_points[ell].add(p)
    collinear = [set().union(*(line_points[ell] for ell in point_lines[p])) - {p}
                 for p in range(V)]
    assert all(len(ns) == s*d for ns in collinear)
    projection = {}
    for q in range(V):
        for r in range(V):
            if r in point_lines[q]:
                continue
            ps = collinear[q] & line_points[r]
            assert len(ps) == 1
            p = next(iter(ps))
            ls = point_lines[q] & point_lines[p]
            assert len(ls) == 1
            projection[q, r] = (p, next(iter(ls)))
    flag_id = {flag: i for i, flag in enumerate(flags)}
    finv = {frozenset(pair): p for p, pair in enumerate(f)}
    ginv = {frozenset(pair): ell for ell, pair in enumerate(g)}
    stars = [{p for p in range(V) if x in f[p]} for x in range(a)]
    R = [[0]*a for _ in range(V)]
    R0 = [[0]*a for _ in range(V)]
    for i, (p, ell) in enumerate(flags):
        for y in g[ell]:
            R[p][y] += 1
            if i in source_ids:
                R0[p][y] += 1
    assert max((max(row) for row in R0), default=0) <= cap+1
    Qx = 2*sum(z*z for row in R0 for z in row)
    assert Qx == 4*len(ids)+4*mg
    Cstars = [[len(collinear[p] & stars[x]) for p in range(V)] for x in range(a)]
    mixed = [[sum(R[p][y]*R0[u][y] for y in range(a)) for u in range(V)]
             for p in range(V)]
    first_square = second_square = mixed_sum = triple_upper = 0
    for u, pair in enumerate(f):
        for x, k in (pair, pair[::-1]):
            for p in stars[k]:
                c, value = Cstars[x][p], mixed[p][u]
                first_square += c*c
                second_square += value*value
                mixed_sum += value
                triple_upper += c*value
    spectral_square = 2*sum(z*z for row in Cstars for z in row)
    assert first_square <= spectral_square <= 4*d*d*(V+s*s*(a-1))
    degree_product = sum(len(ns)*len(core.get(v, ())) for v, ns in full.items())
    assert mixed_sum == degree_product
    assert mixed_sum <= 4*len(flags)*delta
    assert second_square <= 2*d*(cap+1)*mixed_sum
    assert triple_upper**2 <= first_square*second_square

    A2 = walk_matrix(core, 2)
    A3 = walk_matrix(core, 3)
    trace4 = square_norm(A2)
    row2 = sum(z for u, row in A2.items() for v, z in row.items() if u[0] == v[0])
    col2 = sum(z for u, row in A2.items() for v, z in row.items() if u[1] == v[1])
    assert row2 == Qx
    assert col2 == 4*len(ids)+4*mf
    row3 = sum(z for u, row in A3.items() for v, z in row.items() if u[0] == v[0])
    col3 = sum(z for u, row in A3.items() for v, z in row.items() if u[1] == v[1])
    # Independent row-vector quadratic contraction, including odd returns.
    row_quadratic = 0
    for x in range(a):
        image = {v: sum(w[0] == x for w in ns) for v, ns in core.items()}
        row_quadratic += sum(image[u]*image[v] for u, ns in core.items() for v in ns)
    assert row3 == row_quadratic <= delta*row2
    assert col3 <= delta*col2
    all_three = sum(sum(row.values()) for row in A3.values())
    assert all_three*(a*a)**2 >= (4*len(ids))**3

    # Triple enumeration is independent of the missing middle vertex v2.
    triples = set()
    for v0, ns in core.items():
        x, y = v0
        for v1 in ns:
            for z in range(a):
                q = finv.get(frozenset((x, z)))
                if q is None:
                    continue
                for w in range(a):
                    r = ginv.get(frozenset((y, w)))
                    anchor = projection.get((q, r))
                    if anchor is not None and v1[0] in f[anchor[0]]:
                        triples.add((v0, v1, (z, w)))
    assert len(triples) <= triple_upper

    counts = Counter()
    originals = Counter()
    proper_endpoints = Counter()
    first_internal_x = 0
    anchor_outside = 0
    for v0, ns in core.items():
        for v1 in ns:
            for v2 in core[v1]:
                if len({v0[0], v1[0], v2[0]}) != 3 or len({v0[1], v1[1], v2[1]}) != 3:
                    continue
                for v3 in core[v2]:
                    path = (v0, v1, v2, v3)
                    xs, ys = {v[0] for v in path}, {v[1] for v in path}
                    if len(xs) != 4 or len(ys) != 4:
                        continue
                    counts['proper'] += 1
                    proper_endpoints[v0, v3] += 1
                    original_path = tuple(provenance[tuple(sorted((path[j], path[j+1])))]
                                          for j in range(3))
                    assert len({flags[i][0] for i in original_path}) == 3
                    assert len({flags[i][1] for i in original_path}) == 3
                    assert all(j not in conflict[i] for i, j in combinations(original_path, 2))
                    q = finv.get(frozenset((v0[0], v3[0])))
                    r = ginv.get(frozenset((v0[1], v3[1])))
                    if q is None or r is None:
                        counts['missing'] += 1
                        continue
                    if (q, r) not in projection:
                        counts['incident'] += 1
                        continue
                    p, ell = projection[q, r]
                    if v1[0] in f[p]:
                        first_internal_x += 1
                        assert (v0, v1, v3) in triples
                    if set(f[p]) & set(f[q]) or set(g[ell]) & set(g[r]):
                        counts['bad_endpoint'] += 1
                        continue
                    if xs & set(f[p]) or ys & set(g[ell]):
                        counts['internal_blocked_good'] += 1
                        continue
                    counts['unblocked'] += 1
                    anchors = tuple(flag_id[z] for z in ((q, ell), (p, ell), (p, r)))
                    original = tuple(sorted(original_path+anchors))
                    assert len(set(original)) == 6
                    if original not in originals:
                        assert classify_seven_prechecked(original, f, g, flags) == 'B/B-overlap'
                    originals[original] += 1
                    anchor_outside += any(i not in source_ids for i in anchors)
    assert all(value == 2 for value in originals.values())
    assert counts['unblocked'] == 2*len(originals)
    assert all_three-counts['proper'] <= 3*delta*(row2+col2)
    assert first_internal_x**2 <= len(triples)*delta*trace4
    assert counts['proper'] == sum(counts[key] for key in
                                  ('missing', 'incident', 'bad_endpoint', 'internal_blocked_good', 'unblocked'))
    return {
        's': s, 'V': V, 'a': a, 'original_core_flags': len(ids),
        'physical_core_edges': 2*len(ids), 'maximum_degree': delta,
        'maximum_conflict_degree': cap, 'M_f_core': mf, 'M_g_core': mg,
        'two_step_x_return': row2, 'two_step_y_return': col2,
        'three_step_x_return': row3, 'three_step_y_return': col3,
        'all_directed_three_walks': all_three, 'core_trace_four': trace4,
        'proper_endpoint_square_mass': sum(z*z for z in proper_endpoints.values()),
        'mixed_triple_count': len(triples), 'mixed_triple_upper': triple_upper,
        'mixed_first_square': first_square, 'mixed_spectral_square': spectral_square,
        'mixed_second_square': second_square, 'mixed_degree_product': mixed_sum,
        'first_internal_x_paths': first_internal_x,
        'path_partition': dict(sorted(counts.items())),
        'accepted_original_BBo_subcount': len(originals),
        'each_original_sixset_path_multiplicity': 2 if originals else None,
        'unblocked_paths_using_anchor_outside_core': anchor_outside,
        'sample_original_sixset': list(min(originals)) if originals else None,
        'finite_computation_proves_all_h': False,
    }


def certificate_suite():
    out = {}
    for scheme in ('lex', 'reverse-line'):
        model = pair_labeled_symplectic(1, scheme)
        out['W32_'+scheme] = finite_source_certificate(1, model['left_labels'], model['right_labels'])
    path = Path(__file__).with_name('hyp105_w34_adversarial_certificate.json')
    model = json.loads(path.read_text())
    out['W34_adversarial_full'] = finite_source_certificate(2, model['f'], model['g'])
    ids = [i for i in range(425) if i % 3 != 0]
    out['W34_adversarial_sparse_core'] = finite_source_certificate(2, model['f'], model['g'], ids)
    return out


if __name__ == '__main__':
    result = certificate_suite()
    payload = json.dumps(result, indent=2, sort_keys=True)+'\n'
    if len(sys.argv) > 1:
        Path(sys.argv[1]).write_text(payload)
    else:
        print(payload, end='')
