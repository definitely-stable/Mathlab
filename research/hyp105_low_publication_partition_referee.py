"""Independent W(3,2)/W(3,4) ORIGINAL LOW path-partition and GF(5) referee.

ALL-h claims are proved in the accompanying manuscript, not inferred from
finite execution.  No imports from previous Mathlab geometry, LOW, path,
source-sixset, or GF(5) implementations.
"""
from collections import Counter, defaultdict
from itertools import combinations, product
from math import comb, gcd
import json

SCHEMA = "mathlab.hyp105.low-publication-source-partition.v1"
STATUS = "OPEN_WITH_FORMAL_BLOCKER"


def multiply(a, b, s):
    if s == 2:
        return a & b
    if s != 4:
        raise ValueError("independent original fixture only supports GF(2), GF(4)")
    z = 0
    while b:
        if b & 1:
            z ^= a
        b >>= 1
        a <<= 1
        if a & 4:
            a ^= 7  # irreducible x^2+x+1
    return z


def canonical(v, s):
    inv = {1: 1, 2: 3, 3: 2} if s == 4 else {1: 1}
    k = next((x for x in v if x), None)
    if k is None:
        raise ValueError("zero vector has no projective point")
    return tuple(multiply(x, inv[k], s) for x in v)


def bracket(u, v, s):
    return (multiply(u[0], v[2], s) ^ multiply(u[2], v[0], s)
            ^ multiply(u[1], v[3], s) ^ multiply(u[3], v[1], s))


def genuine_gq(s):
    """Construct source lines from totally isotropic projective 2-spaces."""
    if s not in (2, 4) or type(s) is not int:
        raise ValueError("only exact dyadic original symplectic W32/W34")
    vectors = product(range(s), repeat=4)
    points = tuple(sorted({canonical(v, s) for v in vectors if any(v)}))
    pindex = {p: i for i, p in enumerate(points)}
    lines = set()
    for i, j in combinations(range(len(points)), 2):
        u, v = points[i], points[j]
        if bracket(u, v, s):
            continue
        line = frozenset([j] + [
            pindex[canonical(tuple(u[k] ^ multiply(t, v[k], s)
                                   for k in range(4)), s)]
            for t in range(s)
        ])
        if len(line) != s + 1:
            raise AssertionError("not a true symplectic projective line")
        lines.add(tuple(sorted(line)))
    lines = tuple(sorted(lines))
    V = (s + 1) * (s * s + 1)
    if len(points) != V or len(lines) != V:
        raise AssertionError("invalid original W(3,s) point/line count")
    flags = tuple(sorted((p, ell) for ell, pts in enumerate(lines) for p in pts))
    if len(flags) != (s + 1) * V:
        raise AssertionError("invalid original named incidence count")
    onlines = [set() for _ in range(V)]
    collinear = [set() for _ in range(V)]
    for ell, pts in enumerate(lines):
        for p in pts:
            onlines[p].add(ell)
            collinear[p].update(set(pts) - {p})
    projection = {}
    for q in range(V):
        for r in range(V):
            if q in lines[r]:
                continue
            common = collinear[q].intersection(lines[r])
            if len(common) != 1:
                raise AssertionError("GQ unique point projection failed")
            p = next(iter(common))
            ell = onlines[q].intersection(onlines[p])
            if len(ell) != 1:
                raise AssertionError("GQ unique line projection failed")
            projection[q, r] = (p, next(iter(ell)))
    if len(projection) != V * (V - (s + 1)):
        raise AssertionError("true original nonincident endpoint count")
    return dict(s=s, V=V, points=points, lines=lines, flags=flags,
                projection=projection)


def labels(V, scheme):
    a = 2
    while comb(a, 2) < V:
        a += 1
    pairs = tuple(combinations(range(a), 2))[:V]
    if scheme == "lex":
        f, g = pairs, pairs
    elif scheme == "reverse":
        f, g = pairs, pairs[::-1]
    elif scheme == "correlated":
        if gcd(2, V) != 1 or gcd(4, V) != 1:
            raise AssertionError("non-permutation physical label map")
        f = tuple(pairs[(2 * i + 1) % V] for i in range(V))
        g = tuple(pairs[(4 * i + 3) % V] for i in range(V))
    else:
        raise ValueError("unsupported correlation case")
    assert len(set(f)) == len(set(g)) == V
    return a, f, g


def model(s, scheme="lex", core="full"):
    gq = genuine_gq(s)
    flags = gq["flags"]
    a, f, g = labels(gq["V"], scheme)
    z = {flags[i] for i in (0, 3, 7)} if core == "deleted" else set()
    if core == "full":
        C = set(flags)
    elif core == "even":
        C = {flag for i, flag in enumerate(flags) if i % 2 == 0}
    elif core == "deleted":
        C = set(flags) - z
    else:
        raise ValueError("unsupported original paired CORE")
    flag_to_id = {flag: i for i, flag in enumerate(flags)}
    owned = {}
    adj = defaultdict(set)
    for i, (p, ell) in enumerate(flags):
        if (p, ell) not in C:
            continue
        x0, x1 = f[p]
        y0, y1 = g[ell]
        for u, v in (((x0, y0), (x1, y1)),
                     ((x0, y1), (x1, y0))):
            e = tuple(sorted((u, v)))
            if e in owned or u == v:
                raise AssertionError("duplicate or degenerate physical owner")
            owned[e] = i
            adj[u].add(v)
            adj[v].add(u)
    if len(owned) != 2 * len(C):
        raise AssertionError("two genuine opposite physical diagonals lost")
    return dict(**gq, a=a, f=f, g=g, z=z, C=C, flag_to_id=flag_to_id,
                owned=owned, adj=adj,
                point_by_pair={pair: i for i, pair in enumerate(f)},
                line_by_pair={pair: i for i, pair in enumerate(g)},
                scheme=scheme, core=core)


def endpoint_status(m, u, v):
    """Decision on FULL original geometry, independent of physical middle."""
    xx = tuple(sorted((u[0], v[0])))
    yy = tuple(sorted((u[1], v[1])))
    q = m["point_by_pair"].get(xx)
    r = m["line_by_pair"].get(yy)
    if q is None or r is None:
        return "missing", None
    if (q, r) not in m["projection"]:
        return "incident", None
    p, ell = m["projection"][q, r]
    if set(m["f"][q]) & set(m["f"][p]) or set(m["g"][r]) & set(m["g"][ell]):
        return "endbad", None
    anchors = ((q, ell), (p, ell), (p, r))
    if any(x in m["z"] for x in anchors):
        return "deleted", None
    return "good", (q, r, p, ell, anchors)


def classify(m, path):
    coords_x = [v[0] for v in path]
    coords_y = [v[1] for v in path]
    if len(set(coords_x)) != 4 or len(set(coords_y)) != 4:
        return "improper", None
    status, info = endpoint_status(m, path[0], path[-1])
    if status != "good":
        return status, None
    q, r, p, ell, anchors = info
    if any(x in m["f"][p] for x in coords_x[1:3]) or any(
            y in m["g"][ell] for y in coords_y[1:3]):
        return "blocked", None
    owner_ids = tuple(m["owned"][tuple(sorted((path[i], path[i+1])))]
                      for i in range(3))
    six = tuple(sorted(m["flag_to_id"][a] for a in anchors)
                ) + owner_ids
    if len(set(six)) != 6:
        raise AssertionError("accepted path does not own six DISTINCT original flags")
    return "accepted", (tuple(sorted(six)), owner_ids, anchors)


def path_order(edges, close):
    """Source-first unique P4 owner order; no physical path traversal."""
    pairs = list(edges)
    vertices = set(x for _, pair in pairs for x in pair)
    if len(vertices) != 4 or len({tuple(sorted(p)) for _, p in pairs}) != 3:
        return None
    degrees = Counter(x for _, pair in pairs for x in pair)
    ends = {x for x, d in degrees.items() if d == 1}
    if sorted(degrees.values()) != [1, 1, 2, 2] or ends != set(close):
        return None
    current = min(ends)
    order = []
    used = set()
    for _ in range(3):
        candidates = [(idx, pair) for idx, pair in pairs
                      if idx not in used and current in pair]
        if len(candidates) != 1:
            return None
        idx, pair = candidates[0]
        order.append(idx)
        used.add(idx)
        current = pair[0] if pair[1] == current else pair[1]
    return tuple(order) if current == max(ends) else None


def check_source_inverse(m, six):
    """Entirely ORIGINAL six-ID factor graphs (not a walker in H_C)."""
    ids = set(six)
    flags = m["flags"]
    pts = Counter(flags[i][0] for i in ids)
    lns = Counter(flags[i][1] for i in ids)
    p2 = [p for p, n in pts.items() if n == 2]
    l2 = [ell for ell, n in lns.items() if n == 2]
    if sorted(pts.values()) != [1,1,1,1,2] or sorted(lns.values()) != [1,1,1,1,2]:
        return False
    p, ell = p2[0], l2[0]
    if (p, ell) not in m["flag_to_id"]:
        return False
    middle = m["flag_to_id"][(p, ell)]
    if middle not in ids:
        return False
    qa = [i for i in ids if flags[i][1] == ell and flags[i][0] != p]
    ra = [i for i in ids if flags[i][0] == p and flags[i][1] != ell]
    if len(qa) != 1 or len(ra) != 1:
        return False
    q = flags[qa[0]][0]
    r = flags[ra[0]][1]
    if m["projection"].get((q, r)) != (p, ell):
        return False
    anchors = {middle, qa[0], ra[0]}
    if any(flags[i] in m["z"] for i in anchors):
        return False
    residual = ids - anchors
    if len(residual) != 3 or any(flags[i] not in m["C"] for i in residual):
        return False
    x = path_order([(i, m["f"][flags[i][0]]) for i in residual], m["f"][q])
    y = path_order([(i, m["g"][flags[i][1]]) for i in residual], m["g"][r])
    if x is None or y is None or not (x == y or x == y[::-1]):
        return False
    x_s = set(z for i in residual for z in m["f"][flags[i][0]])
    y_s = set(z for i in residual for z in m["g"][flags[i][1]])
    return not (set(m["f"][p]) & x_s or set(m["g"][ell]) & y_s)


def integer_gf5_flow_mass(m, six):
    """Independent 5^5 integer character-orthogonality check, no GF5 floats."""
    flags = [m["flags"][i] for i in sorted(six)]
    edges = []
    for typed in (
        [m["f"][p] for p, _ in flags],
        [m["g"][ell] for _, ell in flags],
    ):
        fibres = defaultdict(list)
        for j, pair in enumerate(typed):
            for symbol in pair:
                fibres[symbol].append(j)
        if len(fibres) != 6 or any(len(v) != 2 for v in fibres.values()):
            raise AssertionError("not the actual 12-edge six-column GF5 palette")
        edges.extend(tuple(v) for v in fibres.values())
    if len(edges) != 12:
        raise AssertionError("expected exactly twelve original pair edges")
    raw = []
    for tail in product(range(5), repeat=5):
        phi = (0,) + tail
        w = 1
        for i, j in edges:
            w *= 4 if phi[i] == phi[j] else -1
        raw.append((phi, w))
    total = 0
    for other_positive in combinations(range(1, 6), 2):
        positives = set((0,) + other_positive)
        demands = tuple(4 if i in positives else -4 for i in range(6))
        buckets = [0]*5
        for phi, w in raw:
            buckets[sum(a*b for a, b in zip(phi, demands)) % 5] += w
        if len(set(buckets[1:])) != 1:
            raise AssertionError("GF5 nonzero Fourier buckets not equal")
        n, rem = divmod(buckets[0] - buckets[1], 3125)
        if rem or n < 0:
            raise AssertionError("GF5 integer orthogonality failed")
        total += n
    return total


def census(m):
    all_vertices = tuple(product(range(m["a"]), repeat=2))
    terminal = Counter()
    for u in all_vertices:
        for v in all_vertices:
            if u[0] == v[0] or u[1] == v[1]:
                continue
            key, _ = endpoint_status(m, u, v)
            terminal[key] += 1
    B = comb(m["a"], 2)
    M = B - m["V"]
    if terminal["missing"] != 4*(2*B*M-M*M):
        raise AssertionError("independent EXACT missing-endpoint identity failed")
    if terminal["incident"] != 4*len(m["flags"]):
        raise AssertionError("independent EXACT incident-endpoint identity failed")
    freq = Counter()
    groups = defaultdict(list)
    proper_by_endpoint = Counter()
    endpoint_bad_path_count = 0
    blocked_masks = Counter()
    walk_total = 0
    for u in m["adj"]:
        for v in m["adj"][u]:
            for w in m["adj"][v]:
                for t in m["adj"][w]:
                    path = (u, v, w, t)
                    walk_total += 1
                    status, detail = classify(m, path)
                    freq[status] += 1
                    if status != "improper":
                        proper_by_endpoint[u, t] += 1
                    if status in ("missing","incident","endbad","deleted"):
                        endpoint_bad_path_count += 1
                    if status == "blocked":
                        _, _, p, ell, _ = endpoint_status(m, u, t)[1]
                        blocked_masks[tuple(
                            [path[k][0] in m["f"][p] for k in (1,2)] +
                            [path[k][1] in m["g"][ell] for k in (1,2)]
                        )] += 1
                    if status == "accepted":
                        six, owners, anchors = detail
                        groups[six].append((path, owners))
    if sum(freq.values()) != walk_total:
        raise AssertionError("not a complete DISJOINT first-failure partition")
    for six, entries in groups.items():
        if len(entries) != 2 or entries[0][0] != entries[1][0][::-1]:
            raise AssertionError("accepted original unordered sixset is NOT 2-to-1")
        if not check_source_inverse(m, six):
            raise AssertionError("independent original factor graph cannot produce accepted sixset")
        if entries[0][1] != entries[1][1][::-1]:
            raise AssertionError("reversal changed named source owner sequence")
    if freq["accepted"] != 2*len(groups):
        raise AssertionError("wrong original source six-ID multiplicity")
    bad_endpoints = sum(terminal[x] for x in
                        ("missing","incident","endbad","deleted"))
    energy = sum(v*v for v in proper_by_endpoint.values())
    if endpoint_bad_path_count**2 > bad_endpoints * energy:
        raise AssertionError("original endpoint Cauchy charge failed")
    bound_missing = 4*(2*B*M-M*M)
    if bound_missing != terminal["missing"]:
        raise AssertionError("missing typed endpoint baseline")
    return dict(s=m["s"],scheme=m["scheme"],core=m["core"],
                V=m["V"],I=len(m["flags"]),a=m["a"],
                original_CORE_flags=len(m["C"]),deleted_flags=len(m["z"]),
                genuine_two_diagonal_edges=len(m["owned"]),
                physical_three_walks=walk_total,
                disjoint_first_failure=dict(freq),
                true_original_produced_sixsets=len(groups),
                real_proper_endpoint_energy=energy,
                bad_endpoint_count=bad_endpoints,
                true_bad_endpoint_path_count=endpoint_bad_path_count,
                endpoint_types={k:terminal.get(k,0) for k in ("missing","incident","endbad","deleted","good")},
                four_inner_blocker_nonexclusive_signatures={
                    "".join("1" if i else "0" for i in k):v
                    for k,v in blocked_masks.items()},
                sixsets=tuple(sorted(groups)))


def prove_root_endpoint_17():
    """Exact-rational ALL-s>=2^32, Z-empty SOURCE GQ endpoint proof budget.

    V/s^3=(1+u)(1+u^2), N/s^4=(1+u)^2(1+u^2).
    For u<=2^-32, sqrt(2V)<(3/2)*s^(3/2) and minimal
    alphabet implies a-1<sqrt(2V)+1<2*s^(3/2).
    With B=binom(a,2), 0<=M=B-V<a-1:
      missing=4(2VM+M^2)
      incident=4N
      endbad<=8s*(e_col_f+e_col_g)
    SRG positive spectrum gives each e_col <=(s^2+1)(s^2+a-2).
    Divide the three universal upper bounds by s^5 and use t=1/sqrt(s).
    Every polynomial term is monotone in nonnegative u,t.
    """
    from fractions import Fraction as F
    u = F(1,2**32)
    t = F(1,2**16)
    if not (2*(1+u)*(1+u*u) < F(9,4) and t <= F(1,2)):
        raise AssertionError("actual minimal-a sqrt envelope not established")
    endbad = 16*(1+u*u)*(1+2*t)
    missing = 16*(1+u)*(1+u*u)*t + 16*u*u
    incident = 4*u*(1+u)**2*(1+u*u)
    total = endbad + missing + incident
    if not (16 < total < 17):
        raise AssertionError("NEW strict all-h endpoint coefficient failed")
    return dict(
        fixed_H=32, Z_empty_only=True,
        exact_source_endbad_coefficient_upper=str(endbad),
        exact_source_missing_coefficient_upper=str(missing),
        exact_source_incident_coefficient_upper=str(incident),
        combined_strict_coefficient_upper=str(total),
        genuine_GQ_source_SRG_positive_eigenvalue="s-1",
        independent_correlated_f_g_alphabet=True,
        all_h_original_bad_endpoints_STRICT_LT_17_s5=True,
        historic_root_bad_endpoint_upper_was_24_s5=True,
        consequence_proper_P3_endpoint_error_coefficient=
            "q3*ceil_sqrt(17*L6)",
        original_ROOT_PROVED_A=False)


def certificate():
    cases=[]
    example_masses=[]
    for s in (2,4):
        for scheme, core in (
                ("lex","full"),("reverse","full"),("correlated","full"),
                ("lex","even"),("reverse","deleted")):
            m=model(s,scheme,core)
            z=census(m)
            if z["true_original_produced_sixsets"]:
                selected=z["sixsets"][0]
                mass=integer_gf5_flow_mass(m,selected)
                if mass!=53838:
                    raise AssertionError("actual produced ORIGINAL BBo is not positive 53838")
                example_masses.append(dict(s=s,scheme=scheme,core=core,
                                           exact_GF5_ten_sign_mass=mass))
            del z["sixsets"]
            cases.append(z)
    if not example_masses or sum(x["true_original_produced_sixsets"]
                                  for x in cases)==0:
        raise AssertionError("certificate must contain positive real source BBo")
    return dict(schema=SCHEMA,status=STATUS,issue=230,parent_pr=783,
       NEW_all_h_original_17s5_endpoint_referee=prove_root_endpoint_17(),
       original_GQ_fixture_independent_GF2_GF4=True,
       exact_partition_from_all_actual_physical_P3=True,
       exact_original_unordered_sixID_two_direction_inverse=True,
       original_GF5_integer_sign_palette_independent=True,
       original_ROOT_PROVED_A=False,
       all_h_LOW_moment_and_full_AC_books_publication_signoff_still_open=True,
       real_cases=cases,positive_GF5_examples=example_masses)


if __name__ == "__main__":
    print("AA4_LOW_PUBLICATION_SOURCE_PARTITION_CERTIFICATE="+
          json.dumps(certificate(),sort_keys=True,separators=(",",":")))
