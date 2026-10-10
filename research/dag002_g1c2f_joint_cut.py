#!/usr/bin/env python3
"""DAG-002 G1-C2-F: exact, restricted joint information-cut frontier.

Elementary cross-history pigeonhole and binary-probe transcript counting.
No novelty claim or unrestricted DAG/cell-probe theorem.
"""
from dataclasses import dataclass
from itertools import combinations
from math import comb


def ball_volume(cells, changed):
    if (any(type(x) is not int for x in (cells, changed))
            or cells < 0 or changed < 0):
        raise ValueError("nonnegative integer Hamming-ball dimensions required")
    return sum(comb(cells, j) for j in range(min(cells, changed) + 1))


def hamming_ball(cells, changed):
    """Exactly all physical words reachable from one fixed zero record."""
    if (any(type(x) is not int for x in (cells, changed))
            or cells < 0 or changed < 0 or cells > 12):
        raise ValueError("enumeration supports 0 <= cells <= 12")
    return tuple(sum(1 << i for i in group)
                 for k in range(min(changed, cells) + 1)
                 for group in combinations(range(cells), k))


@dataclass(frozen=True)
class Cut:
    history_bits: int
    local_bits: int
    update_probes: int
    new_cells: int
    changed_cells: int
    target_vectors: int
    read_transcript_cap: int
    new_record_cap: int
    joint_cap: int
    allowed_by_cuts: bool


def joint_cut(history_bits, local_bits, update_probes, new_cells, changed_cells):
    """Necessary bounds, NOT sufficient for arbitrary schemes or DAG families.

    Frozen same new-command, deterministic update; prior differing histories
    visible only as H trusted bits plus up to R binary old-cell read answers.
    New record begins as identical zero N-bit word, with <=W net changes.
    Queries inspect H retained bits plus ONLY this new record and fixed code.
    No extra changing ROM/directory/address encoding or out-of-band source.
    """
    params = (history_bits, local_bits, update_probes, new_cells, changed_cells)
    if any(type(v) is not int or v < 0 for v in params):
        raise ValueError("nonnegative integer dimensions required")
    if not 0 <= local_bits <= history_bits or new_cells > 10000:
        raise ValueError("H<=history_bits and bounded new record required")
    k = 1 << history_bits
    probe_capacity = 1 << (local_bits + update_probes)
    record_capacity = (1 << local_bits) * ball_volume(new_cells, changed_cells)
    return Cut(history_bits, local_bits, update_probes, new_cells, changed_cells,
               k, probe_capacity, record_capacity,
               min(probe_capacity, record_capacity),
               k <= min(probe_capacity, record_capacity))


@dataclass(frozen=True)
class Witness:
    """Special promise family, not a complete all-history DAG index."""
    history_bits: int
    local_bits: int
    update_probes: int
    new_cells: int
    changed_cells: int
    codewords: tuple[int, ...]

    def old_prefix(self, history_mask):
        """Antichain of m nodes; latest old node m has parents=history_mask."""
        m = self.history_bits
        return tuple(() for _ in range(m)) + (
            tuple(i for i in range(m) if history_mask & (1 << i)),)

    def update(self, old_parent_mask):
        m, h = self.history_bits, self.local_bits
        if (type(old_parent_mask) is not int
                or not 0 <= old_parent_mask < (1 << m)):
            raise ValueError("invalid previous parent mask")
        # Local state is maintained at the earlier append, when that append
        # receives the full m-bit parent-incidence command; not free prehistory.
        trusted = old_parent_mask & ((1 << h) - 1)
        observations = tuple((old_parent_mask >> i) & 1
                             for i in range(h, m))
        unseen = sum(bit << j for j, bit in enumerate(observations))
        return trusted, self.codewords[unseen], len(observations)

    def query_vector(self, trusted, remote_word):
        h, m = self.local_bits, self.history_bits
        if type(trusted) is not int or not 0 <= trusted < (1 << h):
            raise ValueError("invalid trusted bits")
        if type(remote_word) is not int or remote_word not in self.codewords:
            raise ValueError("non-codeword")
        # Target-only query: no old remote/source bytes are accessible.
        residual = self.codewords.index(remote_word)
        return (1 << m) | trusted | (residual << h)


def construct_matching_witness(history_bits, local_bits, update_probes,
                               new_cells, changed_cells):
    c = joint_cut(history_bits, local_bits, update_probes,
                  new_cells, changed_cells)
    if not c.allowed_by_cuts:
        return None
    # Promise-family matching construction: local H old message bits and
    # R=m-H old binary-cell reads; constant public enumerative record code.
    remaining = history_bits - local_bits
    words = hamming_ball(new_cells, changed_cells)
    if update_probes < remaining or len(words) < (1 << remaining):
        return None
    return Witness(history_bits, local_bits, remaining, new_cells,
                   changed_cells, words[:1 << remaining])


def independent_ancestor_dfs(parents, ancestor, target):
    todo, seen = [target], set()
    while todo:
        v = todo.pop()
        if v == ancestor:
            return True
        if v not in seen:
            seen.add(v)
            todo.extend(parents[v])
    return False


def verify_witness(cert, allowed_probes, full_history=True):
    if cert is None:
        return False
    try:
        m, h = cert.history_bits, cert.local_bits
        expected_words = 1 << (m - h)
        if (len(cert.codewords) != expected_words
                or len(set(cert.codewords)) != expected_words
                or any(type(word) is not int or word < 0
                       or word >= (1 << cert.new_cells)
                       or word.bit_count() > cert.changed_cells
                       for word in cert.codewords)):
            return False
        if (cert.update_probes != m - h or
                cert.update_probes > allowed_probes):
            return False
        for e in range(1 << m):
            local, word, read_count = cert.update(e)
            if read_count > allowed_probes:
                return False
            result = cert.query_vector(local, word)
            if result != ((1 << m) | e):
                return False
            if full_history:
                old = cert.old_prefix(e)
                full = old + ((m,),)
                exact = sum(1 << i for i in range(m + 1)
                            if independent_ancestor_dfs(full, i, m + 1))
                if result != exact:
                    return False
        return True
    except (TypeError, ValueError, IndexError, AttributeError):
        return False


def report():
    checked = 0
    for m in range(6):
        for h in range(m + 1):
            for cells in range(6):
                for w in range(cells + 1):
                    r = m - h
                    bound = joint_cut(m, h, r, cells, w)
                    cert = construct_matching_witness(m, h, r, cells, w)
                    assert (cert is not None) == bound.allowed_by_cuts
                    if cert is not None:
                        assert verify_witness(cert, r)
                    checked += 1
    print("DAG_G1C2F_EXACT_READ_WRITE_LOCAL_CUT_PASS", checked)
    print("DAG_G1C2F_MATCHING_PROMISE_FAMILY_CERT_PASS")
    print("DAG_G1C2F_CLASSICAL_PIGEONHOLE_NOVELTY_STOP")


if __name__ == "__main__":
    report()
