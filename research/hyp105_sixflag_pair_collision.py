"""HYP-105 / #230 AA4-SFC: exact six-original-flag collision decomposition.

Finite W(3,2)/W(3,4) oracle and all-h structural theorem.
N3 is the AA4-WE proper directed physical 3-walk multiplicity grouped by
genuine original nonincident typed POINT/LINE endpoint IDs.

The *unordered* source incidence-ID triplet is well-defined and distinct.
At fixed (q,r), each triplet appears exactly twice (walk and reverse).
Two distinct triplets cannot share exactly TWO original incidence IDs.
Q=sum N3^2=2P+8(C0+C1), where C0/C1 are unordered pairs of
different reverse-orbits with zero/one common source flag respectively.
C0 has six different original source incidence IDs; it is NOT the same
as a GF(5)-accepted original six-flag class of root issue #230.
"""
from collections import Counter, defaultdict
from itertools import combinations

from hyp105_b1_symplectic import symplectic_gq
from hyp105_physical_degree_energy import (
    minimal_alphabet, _verify_typed_injections,
)


def source_sixflag_collision_census(power, f, g, *, verify_with_previous=True):
    """Finite all-source-ID independent census; only power=1/2 due to cost.

    Enumerates TRUE W(3,2^power) source flags, the physical graph,
    coordinate-distinct directed 3-walks and their ORIGINAL three-flag
    provenance. Counts all ordered path-pairs at each nonincident
    original endpoint via reverse-orbit compression.
    """
    if type(power) is not int or power not in (1, 2):
        raise ValueError("finite full walk oracle only supports h=1,2")
    s = 1 << power
    _, points, lines, flags = symplectic_gq(power)
    V = (s+1)*(s*s+1)
    if len(points) != V or len(lines) != V or len(flags) != V*(s+1):
        raise AssertionError("not the original symplectic W(3,s)")
    a = minimal_alphabet(V)
    f, g = tuple(map(tuple, f)), tuple(map(tuple, g))
    _verify_typed_injections(a, V, f, g)
    source_flag_set = set(flags)
    fi = {frozenset(edge): p for p, edge in enumerate(f)}
    gi = {frozenset(edge): l for l, edge in enumerate(g)}
    original_incidence = [set() for _ in range(V)]
    for p, l in flags:
        original_incidence[p].add(l)
    if len(source_flag_set) != len(flags):
        raise AssertionError("duplicate original incidence IDs")

    physical_adj = defaultdict(list)
    for p, l in flags:
        u, v = f[p]
        x, y = g[l]
        for v0, v1 in (((u, x), (v, y)), ((u, y), (v, x))):
            physical_adj[v0].append(v1)
            physical_adj[v1].append(v0)
    if any(len(v) != len(set(v)) for v in physical_adj.values()):
        raise AssertionError("injective source images cannot create parallel arcs")

    grouped = defaultdict(list)
    proper = missing = incident = 0
    for v0, nb0 in physical_adj.items():
        for v1 in nb0:
            for v2 in physical_adj[v1]:
                if (len({v0[0],v1[0],v2[0]}) != 3 or
                        len({v0[1],v1[1],v2[1]}) != 3):
                    continue
                for v3 in physical_adj[v2]:
                    if (len({v0[0],v1[0],v2[0],v3[0]}) != 4 or
                            len({v0[1],v1[1],v2[1],v3[1]}) != 4):
                        continue
                    proper += 1
                    q = fi.get(frozenset((v0[0],v3[0])))
                    r = gi.get(frozenset((v0[1],v3[1])))
                    if q is None or r is None:
                        missing += 1
                        continue
                    if r in original_incidence[q]:
                        incident += 1
                        continue
                    vertices = (v0,v1,v2,v3)
                    point_ids, line_ids, flag_ids = [], [], []
                    for i in range(3):
                        a0, a1 = vertices[i], vertices[i+1]
                        p = fi[frozenset((a0[0], a1[0]))]
                        l = gi[frozenset((a0[1], a1[1]))]
                        if (p,l) not in source_flag_set:
                            raise AssertionError("physical arc not an original flag")
                        point_ids.append(p)
                        line_ids.append(l)
                        flag_ids.append(p*V+l)
                    if (len(set(point_ids)) != 3 or
                            len(set(line_ids)) != 3 or
                            len(set(flag_ids)) != 3):
                        raise AssertionError("proper path must use three distinct source factor/flag IDs")
                    grouped[q,r].append(tuple(sorted(flag_ids)))

    P = sum(map(len,grouped.values()))
    U = V*s*s*(s+1)
    if len(grouped) > U:
        raise AssertionError("invalid original nonincident universe")
    Q = [0,0,0,0]
    C0 = C1 = total_orbits = 0
    bad_P = bad_Q = bad_C0 = bad_C1 = 0
    good_P = good_Q = 0
    class_bad = [0,0,0,0]
    class_good = [0,0,0,0]
    for (q,r), directed_triplets in grouped.items():
        counts = Counter(directed_triplets)
        if any(n != 2 for n in counts.values()):
            raise AssertionError("a source-flag triple must have exactly walk/reverse")
        orbit_keys = list(counts)
        t = len(orbit_keys)
        if 2*t != len(directed_triplets):
            raise AssertionError("not a reversal orbit partition")
        total_orbits += t
        local = [0,0,0,4*t]
        for a0,a1 in combinations(orbit_keys,2):
            common = len(set(a0).intersection(a1))
            if common >= 2:
                raise AssertionError("two different 3-edge source paths cannot share two flags at same endpoint")
            local[common] += 8
        for j in range(4):
            Q[j] += local[j]
        C0 += local[0]//8
        C1 += local[1]//8

        candidate = [(p,l0) for p in lines[r] for l0 in original_incidence[q]
                     if p in lines[l0]]
        if len(candidate) != 1:
            raise AssertionError("genuine GQ unique source 3-path failed")
        p,l0 = candidate[0]
        bad = bool(set(f[q]).intersection(f[p]) or set(g[r]).intersection(g[l0]))
        if bad:
            bad_P += 2*t
            bad_Q += sum(local)
            bad_C0 += local[0]//8
            bad_C1 += local[1]//8
            for j in range(4):
                class_bad[j] += local[j]
        else:
            good_P += 2*t
            good_Q += sum(local)
            for j in range(4):
                class_good[j] += local[j]

    Q_direct = sum(len(directed_triplets)**2 for directed_triplets in grouped.values())
    if (sum(Q) != Q_direct or Q[2] or Q[3] != 2*P
            or Q[0] != 8*C0 or Q[1] != 8*C1
            or P != proper-missing-incident or P != 2*total_orbits):
        raise AssertionError("six-flag collision-moment identity failed")
    if (bad_P+good_P != P or bad_Q+good_Q != Q_direct
            or any(class_bad[i]+class_good[i] != Q[i] for i in range(4))):
        raise AssertionError("bad/good endpoint collision partition failed")
    if verify_with_previous:
        if power == 1:
            from hyp105_weighted_variance_transfer import w32_weighted_census
            prior = w32_weighted_census(f,g,verify_corner_join=True)
            expected = (prior["P"],prior["Q"],prior["M"])
        else:
            from hyp105_w34_weighted_endpoint import weighted_endpoint_profile
            prior = weighted_endpoint_profile(f,g,verify_join=True)
            expected = (prior["path_mass"],prior["N3_sum_squares"],prior["bad_path_mass"])
        if (P,Q_direct,bad_P) != expected:
            raise AssertionError("independent prior physical 3-walk oracle disagrees")
    return {
        "s":s,"V":V,"a":a,"U":U,
        "physical_proper":proper,"missing":missing,"incident":incident,
        "P":P,"Q":Q_direct,"C0":C0,"C1":C1,
        "Q0_six_distinct_source_flags":Q[0],
        "Q1_five_distinct_source_flags":Q[1],
        "Q2_forbidden_two_shared_flags":Q[2],
        "Q3_reverse_orbit":Q[3],
        "reverse_orbits":total_orbits,
        "occupied_source_endpoint_pairs":len(grouped),
        "zero_source_endpoint_pairs":U-len(grouped),
        "max_N3":max(map(len,grouped.values()),default=0),
        "bad_P":bad_P,"good_P":good_P,
        "bad_Q":bad_Q,"good_Q":good_Q,
        "bad_C0":bad_C0,"bad_C1":bad_C1,
        "bad_Q_strata":tuple(class_bad),
        "good_Q_strata":tuple(class_good),
        "uniform_chi_square_proved":False,
        "root_GF5_sevenclass_proved":False,
    }
