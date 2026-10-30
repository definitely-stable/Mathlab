"""Exact source-exposure and six-ID deletion-resilience falsifiers.

Finite examples check the original-ID identities, not an asymptotic
low-D6 hypothesis or the coefficient-eight limit.
"""
from collections import Counter
from functools import lru_cache
import json
from pathlib import Path
import sys

from hyp105_full_physical_degree_tail import genuine_source, physical
from hyp105_physical_degree_energy import minimal_alphabet, _verify_typed_injections
from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked


def checked_ids(values, total):
    values = tuple(values)
    if len(values) != len(set(values)) or any(type(i) is not int or not 0 <= i < total for i in values):
        raise ValueError('distinct valid original integer flag IDs required')
    return frozenset(values)


@lru_cache(None)
def source_exposure_geometry(power):
    s, V, flags = genuine_source(power)
    pencils = [set() for _ in range(V)]
    lines = [set() for _ in range(V)]
    for p, ell in flags:
        pencils[p].add(ell)
        lines[ell].add(p)
    flag_id = {flag: i for i, flag in enumerate(flags)}
    collinear = [set().union(*(lines[ell] for ell in pencils[q])) - {q} for q in range(V)]

    # Method 1: endpoint-major unique source projection.
    projections = {}
    for q in range(V):
        for r in range(V):
            if r in pencils[q]:
                continue
            ps = collinear[q] & lines[r]
            assert len(ps) == 1
            p = next(iter(ps))
            ls = pencils[q] & pencils[p]
            assert len(ls) == 1
            ell = next(iter(ls))
            projections[q, r] = tuple(flag_id[z] for z in ((q, ell), (p, ell), (p, r)))
    assert len(projections) == len(flags)*s*s

    # Method 2: flag-centered enumeration at each of the three positions.
    postings = []
    for i, (u, v) in enumerate(flags):
        first = {(u, r) for p in lines[v]-{u} for r in pencils[p]-{v}}
        middle = {(q, r) for q in lines[v]-{u} for r in pencils[u]-{v}}
        last = {(q, v) for ell in pencils[u]-{v} for q in lines[ell]-{u}}
        roles = tuple(map(frozenset, (first, middle, last)))
        assert all(len(role) == s*s for role in roles)
        assert len(set.union(first, middle, last)) == 3*s*s
        for position, role in enumerate(roles):
            assert all(projections[endpoints][position] == i for endpoints in role)
        postings.append(roles)
    return s, V, flags, projections, tuple(postings)


def exposure_certificate(power, forbidden):
    s, V, flags, projections, postings = source_exposure_geometry(power)
    forbidden = checked_ids(forbidden, len(flags))
    by_projection = {endpoints for endpoints, chain in projections.items() if forbidden.intersection(chain)}
    by_postings = set()
    for i in forbidden:
        for role in postings[i]:
            by_postings.update(role)
    assert by_projection == by_postings
    histogram = Counter(len(forbidden.intersection(chain)) for chain in projections.values())
    assert sum(k*n for k, n in histogram.items()) == 3*s*s*len(forbidden)
    assert len(by_projection) <= min(len(projections), 3*s*s*len(forbidden))
    return {
        's': s, 'V': V, 'original_flags': len(flags),
        'forbidden_ids': sorted(forbidden), 'forbidden_count': len(forbidden),
        'typed_nonincident_pairs': len(projections),
        'exposed_typed_pairs': len(by_projection),
        'exposed_ordered_physical_endpoint_pairs': 4*len(by_projection),
        'union_bound_typed': min(len(projections), 3*s*s*len(forbidden)),
        'flag_hits_per_projection_histogram': {str(k): histogram[k] for k in range(4)},
        'each_flag_each_position': s*s,
        'each_flag_total_exposure': 3*s*s,
    }


def avoidance_certificate(power, f, g, forbidden=(), core_ids=None):
    s, V, flags, projections, _ = source_exposure_geometry(power)
    a = minimal_alphabet(V)
    f, g = tuple(map(tuple, f)), tuple(map(tuple, g))
    _verify_typed_injections(a, V, f, g)
    forbidden = checked_ids(forbidden, len(flags))
    retained = (frozenset(range(len(flags)))-forbidden if core_ids is None
                else checked_ids(core_ids, len(flags)))
    if retained & forbidden:
        raise ValueError('the path core must exclude every forbidden original flag')
    graph, provenance = physical(sorted(retained), flags, f, g)
    f_inv = {frozenset(pair): p for p, pair in enumerate(f)}
    g_inv = {frozenset(pair): ell for ell, pair in enumerate(g)}
    endpoint_counts = Counter()
    produced = Counter()
    proper = exposed_mass = raw_unblocked = blocked_anchor_mass = anchor_outside_core = 0
    for v0 in graph:
        for v1 in graph[v0]:
            for v2 in graph[v1]:
                if len({v0[0], v1[0], v2[0]}) != 3 or len({v0[1], v1[1], v2[1]}) != 3:
                    continue
                for v3 in graph[v2]:
                    path = (v0, v1, v2, v3)
                    xs, ys = {v[0] for v in path}, {v[1] for v in path}
                    if len(xs) != 4 or len(ys) != 4:
                        continue
                    proper += 1
                    endpoint_counts[v0, v3] += 1
                    q = f_inv.get(frozenset((v0[0], v3[0])))
                    r = g_inv.get(frozenset((v0[1], v3[1])))
                    anchors = projections.get((q, r))
                    if anchors is None:
                        continue
                    exposed = bool(forbidden.intersection(anchors))
                    exposed_mass += exposed
                    # Recover the repeated source point p and line ell.
                    p, ell = flags[anchors[1]]
                    if xs & set(f[p]) or ys & set(g[ell]):
                        continue
                    raw_unblocked += 1
                    if exposed:
                        blocked_anchor_mass += 1
                        continue
                    path_ids = tuple(provenance[tuple(sorted((path[j], path[j+1])))] for j in range(3))
                    original = tuple(sorted(path_ids+anchors))
                    assert len(set(original)) == 6 and not forbidden.intersection(original)
                    if original not in produced:
                        assert classify_seven_prechecked(original, f, g, flags) == 'B/B-overlap'
                    produced[original] += 1
                    anchor_outside_core += any(i not in retained for i in anchors)
    assert all(count == 2 for count in produced.values())
    assert raw_unblocked-blocked_anchor_mass == 2*len(produced)
    exposure = exposure_certificate(power, sorted(forbidden))
    q3 = sum(count*count for count in endpoint_counts.values())
    mask_size = exposure['exposed_ordered_physical_endpoint_pairs']
    assert exposed_mass**2 <= mask_size*q3
    assert mask_size <= 12*s*s*len(forbidden)
    return {
        'exposure': exposure, 'core_original_flags': len(retained),
        'proper_core_paths': proper, 'proper_path_endpoint_square_mass': q3,
        'projection_exposed_path_mass': exposed_mass,
        'raw_unblocked_paths': raw_unblocked,
        'unblocked_paths_rejected_for_forbidden_anchor': blocked_anchor_mass,
        'unblocked_paths_avoiding_all_six_forbidden_ids': 2*len(produced),
        'accepted_original_BBo_subcount_avoiding_Z': len(produced),
        'produced_sixsets': [list(ids) for ids in sorted(produced)],
        'surviving_paths_with_anchor_outside_core': anchor_outside_core,
        'finite_check_proves_asymptotic_coefficient': False,
    }


def certificate_suite():
    model = pair_labeled_symplectic(1, 'lex')
    result = {}
    for label, forbidden in (('empty', ()), ('singleton', (2,)),
                             ('pencil', (0, 1, 2)), ('all', tuple(range(45)))):
        row = avoidance_certificate(1, model['left_labels'], model['right_labels'], forbidden)
        row.pop('produced_sixsets')
        result['W32_lex_'+label] = row
    model = json.loads(Path(__file__).with_name('hyp105_w34_adversarial_certificate.json').read_text())
    for label, forbidden in (('singleton', (0,)), ('pencil', tuple(range(5))),
                             ('spread', tuple(range(0, 425, 17)))):
        # Extra deletions exercise anchors outside the path core and outside Z.
        core = tuple(i for i in range(425) if i % 3 != 0 and i not in forbidden)
        row = avoidance_certificate(2, model['f'], model['g'], forbidden, core)
        row.pop('produced_sixsets')
        result['W34_sparse_'+label] = row
    return result


if __name__ == '__main__':
    payload = json.dumps(certificate_suite(), indent=2, sort_keys=True)+'\n'
    if len(sys.argv) > 1:
        Path(sys.argv[1]).write_text(payload)
    else:
        print(payload, end='')
