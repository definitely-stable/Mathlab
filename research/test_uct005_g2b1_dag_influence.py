"""UCT-005 G2-B1: independent XOR-path and hash-dependency finite falsifiers.

Mathematical results are restricted to the explicit linear XOR / eager hash
representations. This is NOT a computational hash-security proof or a new
asymptotic universal theorem.
"""
from hashlib import sha256
from itertools import product
import unittest


def sources(parents):
    return tuple(v for v, pred in enumerate(parents) if not pred)


def node_values(parents, source_bits):
    out = []
    for i, pred in enumerate(parents):
        if not pred:
            out.append(source_bits[i])
        else:
            v = 0
            for j in pred:
                v ^= out[j]
            out.append(v)
    return tuple(out)


def path_counts(parents, source):
    """Exact directed path counts, not modulo 2 and not mere reachability."""
    p = []
    for v, pred in enumerate(parents):
        if v == source:
            p.append(1)
        elif not pred:
            p.append(0)
        else:
            p.append(sum(p[u] for u in pred))
    return tuple(p)


def domain_sep_digest(parents, values):
    """Fixed labelled DAG; bytes include node type, own output, every predecessor."""
    out = []
    for v, pred in enumerate(parents):
        preamble = (b"UCT005-G2B1-SOURCE-v1" if not pred
                    else b"UCT005-G2B1-INTERNAL-v1")
        payload = (preamble + v.to_bytes(4, "big") +
                   bytes([values[v]]) + len(pred).to_bytes(4, "big"))
        for u in pred:
            payload += u.to_bytes(4, "big") + out[u]
        out.append(sha256(payload).digest())
    return tuple(out)


def brute_independent_path_count(parents, source, dest):
    """Exhaustively enumerate simple topologically increasing paths."""
    if source == dest:
        return 1
    stack = [source]
    total = 0

    def visit(v):
        nonlocal total
        if v == dest:
            total += 1
            return
        for nxt in range(v + 1, len(parents)):
            if v in parents[nxt]:
                visit(nxt)

    visit(source)
    return total


def all_topological_graphs(n):
    edges = [(u, v) for v in range(n) for u in range(v)]
    for flags in product((0, 1), repeat=len(edges)):
        parents = [[] for _ in range(n)]
        for bit, (u, v) in zip(flags, edges):
            if bit:
                parents[v].append(u)
        yield tuple(tuple(row) for row in parents)


def diamond(K):
    """s=0, a=1, b=2, sinks=3..K+2 with two s->sink paths."""
    assert K >= 1
    return ((), (0,), (0,)) + tuple((1, 2) for _ in range(K))


def odd_fanout(K):
    assert K >= 1
    return ((), (0,), (0,)) + tuple((1,) for _ in range(K))


def probe_stats(parents, s, seed=None):
    """Mutate only s in independent source state; compare both representations."""
    if seed is None:
        seed = {x: 0 for x in sources(parents)}
    before = node_values(parents, seed)
    bh = domain_sep_digest(parents, before)
    updated = dict(seed)
    updated[s] ^= 1
    after = node_values(parents, updated)
    ah = domain_sep_digest(parents, after)
    semantic = tuple(i for i in range(len(parents)) if before[i] != after[i])
    structural = tuple(i for i in range(len(parents)) if bh[i] != ah[i])
    return semantic, structural


class Uct005G2B1DagFalsifier(unittest.TestCase):
    def test_exhaustive_graphs_source_assignments_and_path_enumeration(self):
        graph_count = 0
        for n in range(1, 5):
            for parents in all_topological_graphs(n):
                graph_count += 1
                srcs = sources(parents)
                for s in srcs:
                    counts = path_counts(parents, s)
                    for dest in range(n):
                        self.assertEqual(
                            counts[dest],
                            brute_independent_path_count(parents, s, dest))
                    expected_semantic = tuple(i for i, p in enumerate(counts)
                                              if p % 2)
                    expected_structural = tuple(i for i, p in enumerate(counts)
                                                if p > 0)
                    for assignment in product((0, 1), repeat=len(srcs)):
                        seed = dict(zip(srcs, assignment))
                        semantic, structural = probe_stats(parents, s, seed)
                        self.assertEqual(semantic, expected_semantic)
                        self.assertEqual(structural, expected_structural)
                        self.assertTrue(set(semantic).issubset(structural))
        self.assertEqual(graph_count, 75)  # 1+2+8+64

    def test_unbounded_diamond_fanout_separates_semantic_and_hash(self):
        for K in (1, 2, 3, 8, 16, 64):
            G = diamond(K)
            paths = path_counts(G, 0)
            self.assertEqual(paths[:3], (1, 1, 1))
            self.assertEqual(paths[3:], (2,) * K)
            semantic, structural = probe_stats(G, 0)
            self.assertEqual(semantic, (0, 1, 2))
            self.assertEqual(structural, tuple(range(K + 3)))
            self.assertEqual(len(structural) - len(semantic), K)
            self.assertEqual(len(structural) / len(semantic), (K + 3) / 3)

    def test_odd_fanout_has_no_path_cancellation(self):
        for K in (1, 8, 32):
            G = odd_fanout(K)
            semantic, structural = probe_stats(G, 0)
            self.assertEqual(semantic, structural)
            self.assertEqual(len(semantic), K + 3)

    def test_no_universal_eager_write_lower_bound(self):
        # Same FLIP / READ task; materialized stores K+3 nodes and touches
        # 3 semantic bits, lazy source-only store touches 1 input bit and
        # recomputes on each READ. Do not misprice lazy query work as zero.
        for K in (1, 2, 7, 15):
            G = diamond(K)
            semantic, structural = probe_stats(G, 0)
            eager_changed_node_bits = len(semantic)
            eager_changed_hash_digests = len(structural)
            lazy_source_changed_bits = 1
            self.assertEqual(eager_changed_node_bits, 3)
            self.assertEqual(eager_changed_hash_digests, K + 3)
            self.assertEqual(lazy_source_changed_bits, 1)
            source_state = {0: 1}
            self.assertEqual(node_values(G, source_state)[-1], 0)

    def test_source_local_flip_twice_returns_same_digest_without_epoch(self):
        G = diamond(9)
        a = {0: 0}
        b = {0: 1}
        v0 = node_values(G, a)
        v1 = node_values(G, b)
        self.assertNotEqual(domain_sep_digest(G, v0),
                            domain_sep_digest(G, v1))
        self.assertEqual(domain_sep_digest(G, v0),
                         domain_sep_digest(G, node_values(G, a)))
        # Therefore a bare digest without a version is NOT a freshness token.
        self.assertEqual(v0[-1], v1[-1])

if __name__ == "__main__":
    unittest.main()
