"""HYP-105 G5-E0: exact GF5 prescribed-boundary nowhere-zero flow reduction.

This is a model-specific application of CLASSICAL nowhere-zero (A,b)-flows.
Fu–Ren–Wang 2025 gives the general b-compatible spanning-subgraph formula
(DOI: 10.1016/j.aam.2025.102901); no originality claim for that identity.

Only small configurations <=4 support4 columns (<=16 incidence edges)
are enumerated. The mathematical inclusion-exclusion identity holds for
any finite incidence graph; direct O(2^E) computation is not scalable.
"""
from fractions import Fraction

from hyp105_g5d_trade_rank import signed_trade_rank_report, trade_linear_system


def exact_nonzero_trade_flow(supports, signs, max_edges=16):
    """Count exact nonzero GF5 signed trades, as prescribed boundary flows.

    Edges are (column i, touched coordinate j). Orient column->coordinate.
    After variable change z_{ij}=sign_i * weight_{ij}, boundary demands are
    4*sign_i at column vertices and 0 at coordinate vertices.
    Nonzero GF5 coefficients correspond bijectively to nowhere-zero flows.

    For each edge deletion set Z apply inclusion/exclusion: remaining
    unconstrained GF5 affine flow count is q^(E'-V+C') precisely when
    each connected component has zero total boundary, otherwise zero.
    """
    report = signed_trade_rank_report(supports, signs)
    matrix, rhs, coords, _ = trade_linear_system(supports, signs)
    t = len(supports)
    n = t + len(coords)
    edges = tuple((i, t + coords.index(c))
                  for i, row in enumerate(supports) for c in row)
    E = len(edges)
    if E > max_edges:
        raise ValueError("direct 2^E flow oracle exceeds compute cap")
    demands = tuple((4 * epsilon) % 5 for epsilon in signs) + (0,)*len(coords)
    total = 0

    for zero_mask in range(1 << E):
        parent = list(range(n))

        def find(i):
            while parent[i] != i:
                parent[i] = parent[parent[i]]
                i = parent[i]
            return i

        kept = 0
        for e, (u, v) in enumerate(edges):
            if zero_mask >> e & 1:
                continue
            kept += 1
            ru, rv = find(u), find(v)
            if ru != rv:
                parent[rv] = ru

        balances = {}
        for v in range(n):
            root = find(v)
            balances[root] = (balances.get(root, 0) + demands[v]) % 5
        if any(value for value in balances.values()):
            continue

        components = len(balances)
        cycle_rank = kept - n + components
        if cycle_rank < 0:
            raise AssertionError("graphic cyclomatic rank cannot be negative")
        value = 5**cycle_rank
        total += (-1 if zero_mask.bit_count() & 1 else 1) * value

    if not 0 <= total <= 51**t:
        raise AssertionError("inclusion-exclusion is not a valid probability count")
    fraction = Fraction(total, 51**t)
    if fraction > report["nonzero_palette_upper"]:
        raise AssertionError("exact flow probability exceeds D4 field-rank bound")
    return {
        "t": t,
        "v": report["v"],
        "components": report["components"],
        "edge_variables": E,
        "number_of_nonzero_GF5_weight_assignments": total,
        "total_checksum4_nonzero_weight_assignments": 51**t,
        "exact_probability": fraction,
        "rank_upper": report["nonzero_palette_upper"],
        "method": "published prescribed-boundary nowhere-zero flow inclusion-exclusion",
        "asymptotic_improvement_proven": False,
    }
