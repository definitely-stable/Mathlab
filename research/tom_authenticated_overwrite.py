#!/usr/bin/env python3
"""TOM-003-D2: exact structural Merkle batch-overwrite cost/oracle.

NOT an original Merkle primitive or information-theoretically sound proof.
SHA-256 only gives conditional computational authenticity. Assumes that BOTH
the starting Merkle root and initial threshold count were authenticated.
No untrusted old-bit claim or previous-version sibling hash is free.

Nearest prior art: Ethereum SSZ multiproofs; transparency-dev compact ranges.
"""
from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations
from math import ceil, log2
from typing import Mapping, Sequence

DIGEST_BYTES = 32


def check_bits(bits: Sequence[int]) -> None:
    n = len(bits)
    if type(n) is not int or n < 2 or n & (n - 1):
        raise ValueError("tree length must be a power of two >=2")
    if any(type(x) is not int or x not in (0, 1) for x in bits):
        raise ValueError("bits must be 0 or 1")


def leaf_digest(i: int, bit: int) -> bytes:
    if type(i) is not int or i < 0 or i >= (1 << 32):
        raise ValueError("bad leaf index")
    if type(bit) is not int or bit not in (0, 1):
        raise ValueError("bad old/new bit")
    # Position-bound leaf and domain separation are part of the protocol.
    return sha256(b"\x00" + i.to_bytes(4, "big") + bytes([bit])).digest()


def parent_digest(left: bytes, right: bytes) -> bytes:
    if len(left) != DIGEST_BYTES or len(right) != DIGEST_BYTES:
        raise ValueError("bad sibling digest")
    return sha256(b"\x01" + left + right).digest()


def complete_tree(bits: Sequence[int]) -> tuple[bytes, ...]:
    check_bits(bits)
    n = len(bits)
    tree = [b""] * (2 * n)
    for i, bit in enumerate(bits):
        tree[n + i] = leaf_digest(i, bit)
    for i in range(n - 1, 0, -1):
        tree[i] = parent_digest(tree[2 * i], tree[2 * i + 1])
    return tuple(tree)


def selection(n: int, indices: Sequence[int]) -> tuple[int, ...]:
    if type(n) is not int or n < 2 or n & (n - 1):
        raise ValueError("n must be a power of two >=2")
    if (not indices or len(set(indices)) != len(indices)
            or any(type(i) is not int or i < 0 or i >= n for i in indices)):
        raise ValueError("nonempty set of distinct in-range indices required")
    return tuple(sorted(indices))


def helper_indices(n: int, indices: Sequence[int]) -> tuple[int, ...]:
    """Exact standard binary multiproof frontier of a selected leaf set.

    Include siblings not themselves in the selected tree paths, across
    all levels; suppress overlaps and internal selected paths.
    """
    selected = {n + i for i in selection(n, indices)}
    helpers: set[int] = set()
    while selected != {1}:
        helpers.update({v ^ 1 for v in selected if v ^ 1 not in selected})
        selected = {v // 2 for v in selected}
    return tuple(sorted(helpers))


def prove(tree: Sequence[bytes], indices: Sequence[int]) -> dict[int, bytes]:
    n = len(tree) // 2
    if len(tree) != 2 * n or not tree[1]:
        raise ValueError("missing complete tree")
    return {i: tree[i] for i in helper_indices(n, indices)}


def reconstruct(n: int, indices: Sequence[int], values: Sequence[int],
                proof: Mapping[int, bytes]) -> tuple[bytes, int]:
    """Root from selected authenticated leaves and exactly required helpers.

    Returns computed root and number of SHA256 digests (leaves and internal).
    Helper digest verification happens via root equality, not by trusting
    their values or asserting information-theoretic collision freedom.
    """
    chosen = selection(n, indices)
    if len(chosen) != len(values):
        raise ValueError("index-value count mismatch")
    needed = set(helper_indices(n, chosen))
    if set(proof) != needed or any(type(i) is not int
                                  or type(h) is not bytes or len(h) != DIGEST_BYTES
                                  for i, h in proof.items()):
        raise ValueError("incomplete, extra or invalid multiproof helpers")
    objects = {n + i: leaf_digest(i, bit) for i, bit in zip(chosen, values)}
    objects.update(proof)
    hashes = len(chosen)
    while 1 not in objects:
        progress = False
        for p in sorted({i // 2 for i in objects if i > 1}, reverse=True):
            if p not in objects and 2 * p in objects and 2 * p + 1 in objects:
                objects[p] = parent_digest(objects[2 * p], objects[2 * p + 1])
                hashes += 1
                progress = True
        if not progress:
            raise AssertionError("proof cannot reconstruct root")
    return objects[1], hashes


@dataclass(frozen=True)
class Transition:
    root: bytes
    count: int
    no_effect: bool
    proof_hashes_transmitted: int
    verifier_hash_calls: int
    transmitted_bits_lower_bound: int


def authenticated_overwrite(
    n: int, trusted_old_root: bytes, trusted_old_count: int,
    threshold: int, edits: Sequence[tuple[int, int, int]],
    helper_hashes: Mapping[int, bytes]
) -> Transition:
    """Verify claim about old bits under old root, then commit new bits.

    The root+count must be authenticated at setup and updated together
    after every valid transition. The supplied 'old' bytes are UNTRUSTED
    until this check passes. The threshold count is NOT committed to by
    the Merkle root, so arbitrary caller-supplied counts are forbidden.
    """
    if (type(n) is not int or n < 2 or n & (n - 1)
            or type(trusted_old_root) is not bytes
            or len(trusted_old_root) != DIGEST_BYTES
            or type(trusted_old_count) is not int
            or not 0 <= trusted_old_count <= n
            or type(threshold) is not int or not 1 <= threshold <= n):
        raise ValueError("invalid trusted setup or threshold")
    if not edits or any(type(e) is not tuple or len(e) != 3
                        for e in edits):
        raise ValueError("nonempty triples required")
    idx = [x[0] for x in edits]
    chosen = selection(n, idx)
    old_by_index = {i: old for i, old, new in edits}
    new_by_index = {i: new for i, old, new in edits}
    if len(old_by_index) != len(edits):
        raise ValueError("duplicate updates must be rejected")
    old = [old_by_index[i] for i in chosen]
    new = [new_by_index[i] for i in chosen]
    recovered_old_root, old_cost = reconstruct(n, chosen, old, helper_hashes)
    if recovered_old_root != trusted_old_root:
        raise ValueError("old-bit claim or proof does not match trusted root")
    new_count = trusted_old_count + sum(b - a for a, b in zip(old, new))
    if not 0 <= new_count <= n:
        raise ValueError("count out of range: setup/count is inconsistent")
    new_root, new_cost = reconstruct(n, chosen, new, helper_hashes)
    index_bits = (n - 1).bit_length()
    # Counts index+old+new bits per changed index; key encoding/framing
    # and initial authenticated root+count are NOT included here.
    payload_bits = len(chosen) * (index_bits + 2) + 256 * len(helper_hashes)
    return Transition(
        root=new_root, count=new_count,
        no_effect=(trusted_old_count >= threshold) == (new_count >= threshold),
        proof_hashes_transmitted=len(helper_hashes),
        verifier_hash_calls=old_cost + new_cost,
        transmitted_bits_lower_bound=payload_bits,
    )


def compare_costs(n: int, indices: Sequence[int]) -> dict[str, int]:
    selected = selection(n, indices)
    k = len(selected)
    h = (n - 1).bit_length()
    helpers = helper_indices(n, selected)
    empty_proof = {j: b"\x00" * DIGEST_BYTES for j in helpers}
    # reconstruction hashes do not depend on helper contents; they're
    # accounting for the structural computation only.
    _, one_pass = reconstruct(n, selected, (0,) * k, empty_proof)
    return {
        "n": n, "updates": k,
        "direct_retained_bits": n,  # plus optional threshold count
        "threshold_count_bits": n.bit_length(),
        "trusted_merkle_root_bits": 256,
        "prover_full_tree_sha256_setup": 2 * n - 1,
        "prover_full_tree_stored_digest_bytes": (2 * n - 1) * 32,
        "independent_proof_digest_nodes": k * h,
        "batched_proof_digest_nodes": len(helpers),
        "independent_digest_bytes": 32 * k * h,
        "batched_digest_bytes": 32 * len(helpers),
        "verifier_batch_sha256_calls_old_and_new": 2 * one_pass,
        "transmitted_index_old_new_bits_lower_bound": k * (h + 2),
        "batched_minimum_unframed_bits": k * (h + 2) + 256 * len(helpers),
    }


def enumerate_costs(n: int) -> dict[str, object]:
    if n > 8:
        raise ValueError("only <=8 exhaustively enumerated")
    all_results = [
        compare_costs(n, chosen)
        for k in range(1, n + 1)
        for chosen in combinations(range(n), k)
    ]
    if len(all_results) != (1 << n) - 1:
        raise AssertionError("nonempty subset enumeration count")
    if any(s["batched_proof_digest_nodes"] >
           s["independent_proof_digest_nodes"] for s in all_results):
        raise AssertionError("SSZ multiproof cannot exceed independent proofs")
    return {
        "n": n, "exhaustive_nonempty_batches": len(all_results),
        "full_proof_storage_count": sum(s["batched_proof_digest_nodes"] for s in all_results),
        "independent_proof_storage_count": sum(s["independent_proof_digest_nodes"] for s in all_results),
        "batches_with_savings": sum(
            s["batched_proof_digest_nodes"] < s["independent_proof_digest_nodes"]
            for s in all_results
        ),
        "claim": "CLASSICAL_SSZ_STYLE_MULTIPROOF_COMPARATOR_NOT_NOVEL",
    }


def main() -> None:
    for n in (2, 4, 8):
        print("TOM003_D2_SSZ_FRONTIER_ENUM_PASS", enumerate_costs(n))
    initial = (1, 0, 1, 0, 0, 1, 0, 1)
    tree = complete_tree(initial)
    idx = (0, 1)
    proof = prove(tree, idx)
    result = authenticated_overwrite(
        8, tree[1], sum(initial), 5, ((0, 1, 0), (1, 0, 1)), proof
    )
    expected = list(initial)
    expected[0], expected[1] = 0, 1
    if (result.root != complete_tree(expected)[1]
            or result.count != sum(expected) or not result.no_effect):
        raise AssertionError("authenticated root/count replay failed")
    print("TOM003_D2_AUTHENTICATED_OVERWRITE_PASS")
    print("TOM003_D2_FULL_COST_NO_NOVELTY_GATE", compare_costs(8, idx))


if __name__ == "__main__":
    main()
