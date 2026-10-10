#!/usr/bin/env python3
"""D1-B2-A: same-logical-transcript upper comparator with explicit unknown axes.

This is NOT a complete F1 physical Pareto frontier. Only the corrected PAGE-001
snapshot carries byte-conserving remote page accounting; legacy tree/replica
are conditional logical-node/log controls, not fully priced historical GC.
"""
from __future__ import annotations

import json
from math import ceil

from uct005_d1b0_f1_reference import SnapshotF1Reference, validate_contract
from uct005_g3b2b_range_tree import (
    Reader, TreeWriter, checked_query, _wire,
)
from uct005_g3b2b_baselines import (
    ReplicaReader, ReplicaWriter, replica_query,
)


PRICE_AXES = ("trusted_bits", "peak_remote_pages", "set_remote_page_writes",
              "query_remote_page_reads", "proof_payload_bytes",
              "pinned_retained_pages", "gc_remote_reads", "gc_remote_writes",
              "author_upload_bytes", "anchor_bytes", "prover_work",
              "verifier_work", "setup_bytes", "durability_barriers")
SCIENTIFIC_STATUS = "PARTIAL_SAME_TRANSCRIPT_UPPER_NO_FULL_PARETO_NO_NOVEL_LOWER_BOUND"


def candidate_dominates(a: dict, b: dict) -> bool | None:
    """Refuse ranking when cost axis or trust/operation semantics incomplete.

    Returns None unless all axes have comparable numerical values *and*
    both candidates declare full identical F1 semantics and physical layout.
    This prevents cherry-picking only measured dimensions.
    """
    if a.get("service") != b.get("service") or a.get("cost_model") != b.get("cost_model"):
        return None
    if a.get("status") != "FULLY_PRICED" or b.get("status") != "FULLY_PRICED":
        return None
    x = a.get("costs", {})
    y = b.get("costs", {})
    if (set(x) != set(PRICE_AXES) or set(y) != set(PRICE_AXES)
            or any(type(x[k]) is not int or type(y[k]) is not int
                   or x[k] < 0 or y[k] < 0 for k in PRICE_AXES)):
        return None
    return all(x[k] <= y[k] for k in PRICE_AXES) and any(
        x[k] < y[k] for k in PRICE_AXES)


def ranges(n: int) -> tuple[tuple[int, int], ...]:
    if n <= 0:
        raise ValueError("n must be positive")
    return tuple(sorted({(0, 1), (0, n), (n - 1, n),
                         (0, min(2, n))}))


def _check_tree(writer: TreeWriter, epoch: int, lo: int, hi: int,
                pinned_anchor) -> tuple[int, int]:
    response, reads = writer.serve(epoch, lo, hi - 1)  # legacy inclusive
    # An AS_OF read relies on the previously trusted PIN, not on a new
    # anchor query; checked_query's internal anchor cost is not reused.
    outcome = checked_query(Reader(pinned_anchor), writer.n, lo, hi - 1,
                            response, reads, pinned_anchor)
    if outcome.status != "ACCEPT":
        raise AssertionError(f"tree rejected valid pinned root: {outcome.status}")
    return outcome.value, len(response)


def exercise(n: int, page_bytes: int) -> dict:
    validate_contract()  # PAGE-001 layout must be integrated in this branch
    if not 1 <= n <= 2048 or not 1 <= page_bytes <= 4096:
        raise ValueError("bounded finite reference only")
    bits = tuple(i & 1 for i in range(n))
    snapshot = SnapshotF1Reference(bits, page_bytes=page_bytes)
    tree = TreeWriter(bits)
    log = ReplicaWriter(bits)
    replicas = [ReplicaReader(bits, log.genesis) for _ in range(2)]
    versions = [bits]
    total_tree_upload_logical_nodes = 0
    total_tree_proof_bytes = 0
    total_replica_response_bytes = 0

    # Two independently pinned historical states. R's local pinned copies
    # are counted as trusted state, T's roots are retained without priced GC.
    pin0 = snapshot.pin_current(0)
    if pin0 != 0:
        raise AssertionError("genesis epoch mismatch")
    tree_pin0 = tree.epochs[0]
    log_pin0 = (replicas[0].bits, replicas[0].checkpoint.digest)

    updates = ((0, bits[0] ^ 1),
               (min(1, n - 1), (bits[0] ^ 1) if n == 1 else bits[1]),
               (n - 1, None))
    # The middle SET is necessarily a no-op. The final SET toggles newest
    # state at n-1; there are three epochs even with no-op.
    for j, (pos, desired) in enumerate(updates):
        current = list(versions[-1])
        bit = current[pos] ^ 1 if desired is None else desired
        epoch = snapshot.set(pos, bit)
        tc = tree.set(pos, bit)
        log.set(pos, bit)
        total_tree_upload_logical_nodes += tc.remote_node_writes
        current[pos] = bit
        versions.append(tuple(current))
        if (epoch != j + 1 or tree.anchor.epoch != epoch
                or log.anchor.epoch != epoch):
            raise AssertionError("failed epoch/no-op alignment")
        if j == 1:
            # Independent reader1 must catch up from genesis before PIN.
            q = replica_query(replicas[1], log, 0, n - 1)
            if q.status != "ACCEPT":
                raise AssertionError("reader1 not authenticated before PIN")
            total_replica_response_bytes += q.cost.untrusted_response_bytes
            if snapshot.pin_current(1) != 2:
                raise AssertionError("second reader PIN wrong epoch")
            tree_pin2 = tree.epochs[2]
            log_pin2 = (replicas[1].bits, replicas[1].checkpoint.digest)

    expected = (len(bits) + 7) // 8
    expected_pages = ceil(expected / page_bytes) + ceil(48 / page_bytes)
    if snapshot._pages_per_snapshot() != expected_pages:
        raise AssertionError("PAGE-001 physical manifest was not applied")
    if snapshot.remote_pages != 4 * expected_pages:
        raise AssertionError("missing four pre-GC versions")

    for lo, hi in ranges(n):
        current = sum(versions[3][lo:hi]) & 1
        historic0 = sum(versions[0][lo:hi]) & 1
        historic2 = sum(versions[2][lo:hi]) & 1
        for reader in (0, 1):
            if snapshot.latest(reader, lo, hi) != current:
                raise AssertionError("snapshot LATEST incorrect")
            seen, wire = _check_tree(tree, 3, lo, hi, tree.anchor)
            total_tree_proof_bytes += wire
            if seen != current:
                raise AssertionError("tree LATEST incorrect")
            rr = replica_query(replicas[reader], log, lo, hi - 1)
            if rr.status != "ACCEPT" or rr.value != current:
                raise AssertionError("replica LATEST incorrect")
            total_replica_response_bytes += rr.cost.untrusted_response_bytes
        if snapshot.as_of(0, 0, lo, hi) != historic0:
            raise AssertionError("snapshot AS_OF(0) incorrect")
        if snapshot.as_of(1, 2, lo, hi) != historic2:
            raise AssertionError("snapshot AS_OF(2) incorrect")
        a0, w0 = _check_tree(tree, 0, lo, hi, tree_pin0)
        a2, w2 = _check_tree(tree, 2, lo, hi, tree_pin2)
        total_tree_proof_bytes += w0 + w2
        if (a0, a2) != (historic0, historic2):
            raise AssertionError("tree historical proof incorrect")
        # R AS_OF: paid trusted n-bit pinned *replicas*, no remote proof.
        if ((sum(log_pin0[0][lo:hi]) & 1) != historic0
                or (sum(log_pin2[0][lo:hi]) & 1) != historic2):
            raise AssertionError("replica historic cache incorrect")

    snapshot.gc()
    if set(snapshot.remote) != {0, 2, 3}:
        raise AssertionError("GC illegally discarded independent PIN")
    retained_before = snapshot.retained_pinned_pages
    snapshot.unpin(0, 0)
    snapshot.gc()
    if set(snapshot.remote) != {2, 3}:
        raise AssertionError("GC did not reclaim unpinned snapshot")
    snapshot.unpin(1, 2)
    snapshot.gc()
    if set(snapshot.remote) != {3}:
        raise AssertionError("GC did not reclaim unpinned epoch 2")

    base_costs = {key: None for key in PRICE_AXES}
    base_costs.update({
        "trusted_bits": snapshot.trusted_bits,
        "peak_remote_pages": snapshot.ledger["peak_remote_pages"],
        "set_remote_page_writes": snapshot.ledger["set_full_page_writes"],
        "query_remote_page_reads": snapshot.ledger["query_full_page_reads"],
        "proof_payload_bytes": snapshot.ledger["query_remote_payload_bytes"],
        "pinned_retained_pages": retained_before,
        "gc_remote_reads": snapshot.ledger["gc_directory_page_reads"],
        "gc_remote_writes": snapshot.ledger["gc_manifest_page_writes"],
        "author_upload_bytes": snapshot.ledger["author_remote_upload_bytes"],
    })
    snap={"name": "S_BYTE_CONSERVING_SNAPSHOT",
          "service": "F1_two_reader_SET_LATEST_ASOF_PIN_GC",
          "cost_model": "PAGE001_reference_API_page_images",
          "status": "PARTIAL_PRICE_SETUP_DURABILITY_AND_TRANSPORT_MISSING",
          "costs": base_costs}
    tcost={key: None for key in PRICE_AXES}
    tcost.update({"proof_payload_bytes":total_tree_proof_bytes})
    t={"name":"T_IMMUTABLE_AUTHENTICATED_TREE",
       "service":snap["service"], "cost_model":"legacy_logical_nodes",
       "status":"NO_PRICED_HISTORICAL_GC_OR_PAGES",
       "costs":tcost,
       "charged_logical_node_writes":total_tree_upload_logical_nodes}
    rcost={key:None for key in PRICE_AXES}
    rcost.update({"proof_payload_bytes":total_replica_response_bytes})
    rep={"name":"R_FULL_TRUSTED_REPLICA_AND_LOG",
         "service":snap["service"],"cost_model":"legacy_remote_log",
         "status":"NO_PRICED_HISTORICAL_GC_OR_PAGES",
         "costs":rcost,
         "minimum_reader_replica_bits":2 * n,
         "additional_pinned_copy_bits":2 * n}
    return {
        "n":n, "page_bytes":page_bytes,
        "status":SCIENTIFIC_STATUS,
        "history":{"epochs":3,"set_noop_count":1,"pin0":0,"pin1":2,
                   "queries_per_reader":len(ranges(n))},
        "comparators":[snap,t,rep],
        "pareto":["UNDECIDABLE_PARTIAL_PRICING"] * 3,
        "all_honest_answers_verified":True,
        "root_novelty":"OPEN_UNPROVED",
    }


def report() -> dict:
    cases=[exercise(n,p) for n,p in ((1,1),(8,2),(33,2),(64,64),(257,4096))]
    if any(candidate_dominates(a,b) is not None for row in cases
           for a in row["comparators"] for b in row["comparators"]):
        raise AssertionError("a partial Pareto verdict was made")
    return {"status":SCIENTIFIC_STATUS,"cases":cases,
            "proof_of_new_lower_bound":False}


if __name__=="__main__":
    print(json.dumps(report(),indent=2))
