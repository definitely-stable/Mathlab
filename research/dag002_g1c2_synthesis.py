#!/usr/bin/env python3
"""G1-C2-A: exact finite synthesis of fixed-code bounded-read online protocols.

Classical finite game/circuit enumeration; not a novel bound, not a general
dynamic DAG implementation, not authenticated and not a physical I/O model.
"""
from dataclasses import dataclass
from functools import lru_cache


def width(n):
    return (n - 1).bit_length() if n > 1 else 0


@dataclass(frozen=True)
class ToyModel:
    n: int
    N: int
    H: int
    decoder: tuple[int, ...]
    deltas: tuple[int, ...]

    def __post_init__(self):
        if any(type(x) is not int for x in (self.n, self.N, self.H)):
            raise ValueError("dimensions must be integers, not booleans")
        if not (1 <= self.n <= 2 and 0 <= self.N <= 3 and 0 <= self.H <= 1
                and self.N + self.H <= 3):
            raise ValueError("small exact model: n<=2, N<=3, H<=1, N+H<=3")
        if type(self.decoder) is not tuple or len(self.decoder) != (1 << (self.N+self.H)):
            raise ValueError("complete decoder table required")
        if any(type(x) is not int or not 0 <= x < (1 << self.n) for x in self.decoder):
            raise ValueError("invalid decoder output")
        if (type(self.deltas) is not tuple or not self.deltas or
                len(set(self.deltas)) != len(self.deltas) or
                any(type(x) is not int or not 0 <= x < (1 << self.n) for x in self.deltas)):
            raise ValueError("distinct, legal, nonempty delta alphabet required")

    @property
    def states(self):
        return range(1 << (self.N + self.H))

    def local(self, s):
        return s >> self.N

    def remote(self, s):
        return s & ((1 << self.N) - 1)


@dataclass(frozen=True)
class Budget:
    query_reads: int
    update_reads: int
    remote_writes: int
    local_flips: int
    codebook_bits: int | None = None
    net_changes: int | None = None

    def __post_init__(self):
        values = (self.query_reads, self.update_reads, self.remote_writes, self.local_flips)
        if any(type(x) is not int or x < 0 for x in values):
            raise ValueError("integer nonnegative resource budgets required")
        if self.remote_writes > 1 or self.update_reads > 2 or self.query_reads > 2:
            raise ValueError("finite implementation supports Wphys<=1, R,P<=2")
        if self.codebook_bits is not None and (type(self.codebook_bits) is not int or
                                               self.codebook_bits < 0):
            raise ValueError("invalid fixed-grammar codebook budget")
        if self.net_changes is not None and (type(self.net_changes) is not int or
                                              not 0 <= self.net_changes <= self.remote_writes):
            raise ValueError("W_net must lie in [0, W_phys]")


def action_alphabet(m):
    """Remote no-op/constant overwrite plus assigned trusted local-state value."""
    return tuple((None, 0, h) for h in range(1 << m.H)) + tuple(
        (addr, bit, h) for addr in range(m.N) for bit in (0, 1)
        for h in range(1 << m.H))


def apply_action(m, state, action):
    addr, bit, new_local = action
    remote = m.remote(state)
    if addr is not None:
        remote = (remote & ~(1 << addr)) | (bit << addr)
    return (new_local << m.N) | remote


def tree_cost(tree, addresses, leaves):
    """Exact tabulated payload in this prefix grammar; shared header excluded."""
    if tree[0] == "leaf":
        return 1 + width(leaves)
    if tree[0] != "read":
        raise ValueError("unknown tree node")
    return (1 + width(addresses) + tree_cost(tree[2], addresses, leaves)
            + tree_cost(tree[3], addresses, leaves))


def run_tree(tree, m, state):
    reads = 0
    while tree[0] == "read":
        _, addr, zero, one = tree
        if type(addr) is not int or not 0 <= addr < m.N:
            raise ValueError("invalid probe address")
        reads += 1
        tree = one if (m.remote(state) >> addr) & 1 else zero
    if tree[0] != "leaf":
        raise ValueError("invalid leaf")
    return tree[1], reads


def _optimal_tree(m, states, depth, leaves, valid):
    """Minimal prefix-size binary decision tree for a fixed local+operation."""
    leaf_cost = 1 + width(len(leaves))

    @lru_cache(None)
    def solve(subset, remaining):
        if not subset:
            return leaf_cost, ("leaf", 0)
        for idx, action in enumerate(leaves):
            if all(valid(action, state) for state in subset):
                return leaf_cost, ("leaf", idx)
        if remaining == 0:
            return None
        best = None
        for addr in range(m.N):
            left = tuple(s for s in subset if not ((m.remote(s) >> addr) & 1))
            right = tuple(s for s in subset if (m.remote(s) >> addr) & 1)
            if not left or not right:
                continue
            a, b = solve(left, remaining - 1), solve(right, remaining - 1)
            if a is None or b is None:
                continue
            candidate = (1 + width(m.N) + a[0] + b[0],
                         ("read", addr, a[1], b[1]))
            if best is None or candidate[0] < best[0]:
                best = candidate
        return best

    return solve(tuple(sorted(states)), depth)


def synthesize_invariant(m, b, initial, required_states=()):
    """Enumerate all closed invariants, fixed query/update trees, and T budget.

    Updater programs branch only on charged remote reads and known trusted
    local bits. Invariants are allowed to exclude arbitrary other codewords;
    require additional states explicitly for a full-domain theorem.
    """
    if type(initial) is not int or initial not in m.states:
        raise ValueError("invalid initial physical+local state")
    if b.local_flips > m.H:
        raise ValueError("local flip budget exceeds local-state capacity")
    if (any(type(s) is not int or s not in m.states for s in required_states) or
            len(set(required_states)) != len(required_states)):
        raise ValueError("required states must be unique and valid")
    required_mask = sum(1 << s for s in required_states)
    actions = action_alphabet(m)
    masks = [v for v in range(1, 1 << (1 << (m.N + m.H)))
             if v & (1 << initial) and (v & required_mask) == required_mask]
    masks.sort(key=lambda v: (-v.bit_count(), v))
    best = None
    for mask in masks:
        live = frozenset(s for s in m.states if mask & (1 << s))
        if best is not None and len(live) < len(best[0]):
            break
        programs, bits, accepted = {}, 0, True
        for local in range(1 << m.H):
            group = tuple(s for s in live if m.local(s) == local)
            for i in range(m.n):
                result = _optimal_tree(m, group, b.query_reads, (0, 1),
                    lambda answer, s, i=i: answer == ((m.decoder[s] >> i) & 1))
                if result is None:
                    accepted = False
                    break
                bits += result[0]
                programs[("query", i, local)] = result[1]
            if not accepted:
                break
            for delta in m.deltas:
                def valid(action, state, delta=delta):
                    addr, _, next_local = action
                    if addr is not None and b.remote_writes == 0:
                        return False
                    if (m.local(state) ^ next_local).bit_count() > b.local_flips:
                        return False
                    dest = apply_action(m, state, action)
                    if b.net_changes is not None and (
                            m.remote(state) ^ m.remote(dest)).bit_count() > b.net_changes:
                        return False
                    return dest in live and m.decoder[dest] == (m.decoder[state] ^ delta)

                result = _optimal_tree(m, group, b.update_reads, actions, valid)
                if result is None:
                    accepted = False
                    break
                bits += result[0]
                programs[("update", local, delta)] = result[1]
            if not accepted:
                break
        if not accepted or (b.codebook_bits is not None and bits > b.codebook_bits):
            continue
        candidate = (live, programs, bits)
        if best is None or bits < best[2]:
            best = candidate
    return best


def verify_certificate(m, b, certificate, initial):
    """Re-evaluate every reachable state and operation, independently of solver."""
    if certificate is None:
        return False
    try:
        live, programs, claimed_bits = certificate
        if initial not in live or any(s not in m.states for s in live):
            return False
        actions = action_alphabet(m)
        bits = 0
        for local in range(1 << m.H):
            group = tuple(s for s in live if m.local(s) == local)
            for i in range(m.n):
                tree = programs[("query", i, local)]
                bits += tree_cost(tree, m.N, 2)
                for state in group:
                    answer, reads = run_tree(tree, m, state)
                    if reads > b.query_reads or answer != ((m.decoder[state] >> i) & 1):
                        return False
            for delta in m.deltas:
                tree = programs[("update", local, delta)]
                bits += tree_cost(tree, m.N, len(actions))
                for state in group:
                    action_id, reads = run_tree(tree, m, state)
                    if type(action_id) is not int or not 0 <= action_id < len(actions):
                        return False
                    addr, _, _ = action = actions[action_id]
                    next_state = apply_action(m, state, action)
                    net = (m.remote(state) ^ m.remote(next_state)).bit_count()
                    if (reads > b.update_reads or
                            (addr is not None) > b.remote_writes or
                            (b.net_changes is not None and net > b.net_changes) or
                            (m.local(state) ^ m.local(next_state)).bit_count() > b.local_flips or
                            next_state not in live or
                            m.decoder[next_state] != (m.decoder[state] ^ delta)):
                        return False
        return (bits == claimed_bits and
                (b.codebook_bits is None or bits <= b.codebook_bits))
    except (KeyError, ValueError, IndexError, TypeError, RecursionError):
        return False


def examples():
    return (ToyModel(1, 1, 0, (0, 1), (0, 1)),
            ToyModel(1, 0, 1, (0, 1), (0, 1)))


def report():
    direct, trusted = examples()
    assert synthesize_invariant(direct, Budget(1, 0, 1, 0), 0) is None
    r1 = synthesize_invariant(direct, Budget(1, 1, 1, 0), 0)
    h1 = synthesize_invariant(trusted, Budget(0, 0, 0, 1), 0)
    assert verify_certificate(direct, Budget(1, 1, 1, 0), r1, 0)
    assert verify_certificate(trusted, Budget(0, 0, 0, 1), h1, 0)
    print("DAG_G1C2_R0_BLIND_OVERWRITE_FALSIFIER_PASS")
    print("DAG_G1C2_R1_FIXED_PROGRAM_CERT_PASS", r1[2])
    print("DAG_G1C2_TRUSTED_H1_ESCAPE_PASS", h1[2])
    print("DAG_G1C2_TABULATED_T_CERT_PASS")
    print("NOVELTY_UNPROVED_FINITE_SYNTHESIS")


if __name__ == "__main__":
    report()
