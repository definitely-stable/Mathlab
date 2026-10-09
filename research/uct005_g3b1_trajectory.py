"""UCT-005 G3-B1: restricted multi-epoch Hamming trajectory packing.

Combinatorial necessary bounds only, not cryptographic soundness,
cell-probe update-time bounds or claims of novel asymptotic mathematics.
"""
from itertools import product
from math import comb


def ball_volume(q: int, cells: int, radius: int) -> int:
    if q < 2 or cells < 0 or radius < 0:
        raise ValueError("invalid alphabet/cells/radius")
    return sum(comb(cells, j) * (q - 1) ** j
               for j in range(min(cells, radius) + 1))


def adaptive_tree_support(q: int, p: int) -> int:
    if q < 2 or p < 0:
        raise ValueError("invalid alphabet/probes")
    # Count every possible internal probe node, including branches
    # that do not occur in a particular execution.
    return sum(q ** j for j in range(p))


def trajectory_capacity_bound(
    *, q: int, cells: int, epochs: int, changed: int, errors: int,
    trusted_bits: int, query_count: int, probes: int
) -> dict:
    """Bound distinct length-epochs observable output histories.

    Valid for a fixed initial remote word, deterministic stateless
    decoders, same public code, <=errors independently reset
    q-ary remote corruptions at each epoch, and <=changed net remote
    Hamming symbol changes per update.

    Trusted labels may change per epoch and are charged at each epoch.
    """
    if (q < 2 or cells < 0 or epochs < 1 or changed < 0 or errors < 0
            or trusted_bits < 0 or query_count < 1 or probes < 0):
        raise ValueError("invalid typed resource parameters")
    support = min(cells, epochs * query_count *
                  adaptive_tree_support(q, probes))
    max_per_label = 0
    maximizing = 0
    rows = []
    for s in range(support + 1):
        walks = ball_volume(q, s, changed) ** epochs
        tube_numer = (ball_volume(q, s, changed + errors) *
                      ball_volume(q, s, changed + 2 * errors) ** (epochs - 1))
        tube_den = ball_volume(q, s, errors) ** epochs
        tube = tube_numer // tube_den
        assert tube >= 1
        upper = min(walks, tube)
        rows.append({"support": s, "walks": walks, "tube": tube, "upper": upper})
        if upper > max_per_label:
            max_per_label = upper
            maximizing = s
    return {
        "accessible_symbols": support,
        "label_histories": 2 ** (trusted_bits * epochs),
        "max_per_label": max_per_label,
        "maximizing_support": maximizing,
        "bound": 2 ** (trusted_bits * epochs) * max_per_label,
        "per_support": rows,
    }


def independent_epoch_capacity_product(q, cells, epochs, changed, errors,
                                       trusted_bits):
    """Loose product of per-epoch G3-A Hamming-volume bounds.

    Using all cells is appropriate as a comparator when actual union
    query support equals cells; it need not be equally tight.
    """
    if min(cells, epochs, changed, errors, trusted_bits) < 0 or epochs < 1 or q < 2:
        raise ValueError("invalid resource tuple")
    output = 2 ** (trusted_bits * epochs)
    for j in range(1, epochs + 1):
        output *= (ball_volume(q, cells, j * changed + errors) //
                   ball_volume(q, cells, errors))
    return output


def words(q, cells):
    return product(range(q), repeat=cells)


def hamming(a, b):
    if len(a) != len(b):
        raise ValueError("incompatible word lengths")
    return sum(x != y for x, y in zip(a, b))


def enumerate_walks(q, cells, epochs, changed):
    """Exact projected paths, not the full represented state graph."""
    if q < 2 or cells < 0 or epochs < 1 or changed < 0:
        raise ValueError("invalid path parameters")
    alphabet = tuple(words(q, cells))
    initial = (0,) * cells
    trajectories = [(initial,)]
    for _ in range(epochs):
        trajectories = [path + (w,)
                        for path in trajectories
                        for w in alphabet
                        if hamming(path[-1], w) <= changed]
    return tuple(path[1:] for path in trajectories)


def exact_max_temporal_tube_packing(trajectories, errors):
    """Maximum e-tube-disjoint code size; small finite instances only.

    Pairwise tube-disjointness is necessary for distinct exact output
    histories. Converse need not give per-epoch independently
    decodable output functions.
    """
    if errors < 0:
        raise ValueError("negative errors")
    n = len(trajectories)
    if n > 32:
        raise ValueError("small-instance oracle only")
    if not n:
        return 0
    size = len(trajectories[0])
    if any(len(t) != size for t in trajectories):
        raise ValueError("unequal epoch horizon")
    compatible = [
        {j for j in range(n) if j != i and
         any(hamming(trajectories[i][ep], trajectories[j][ep]) >
             2 * errors for ep in range(size))}
        for i in range(n)
    ]
    best = 0

    def go(chosen, candidates):
        nonlocal best
        if chosen + len(candidates) <= best:
            return
        if not candidates:
            best = max(best, chosen)
            return
        node = min(candidates, key=lambda i: len(candidates & compatible[i]))
        go(chosen + 1, candidates & compatible[node])
        go(chosen, candidates - {node})

    go(0, set(range(n)))
    return best
