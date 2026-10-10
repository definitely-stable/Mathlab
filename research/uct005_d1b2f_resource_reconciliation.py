#!/usr/bin/env python3
"""UCT-005 D1-B2-F: same-transcript normalized, *partial* F1 cost ledger.

No completed resource-vector/Pareto theorem. The three page-image references
have differing trusted-state, GC and proof/CPU accounting. Missing coordinates
are explicit None, never free zero. Legacy Replica+Log uses the shared B2-A
transcript on the representative-range profile only; physical cost stays NULL.
"""
from __future__ import annotations

from collections import Counter
from itertools import product
import json

from uct005_d1b0_f1_reference import SnapshotF1Reference, validate_contract
from uct005_d1b2b_page_cow import PageCowTree
from uct005_d1b2b1_segmented_bitmap import SegmentedPageCowTree
from uct005_d1b2a_partial_pareto import (
    PRICE_AXES, candidate_dominates, exercise as legacy_exercise, ranges,
)

SERVICE = "F1_TWO_READER_THREE_SET_PIN0_PIN2_LATEST_ASOF_GC"
PAGE_API = "FINITE_IDEAL_PAGE_IMAGE_FIXED_SLOTS_NOT_SSD"
STATUS = "PARTIAL_COST_RECONCILIATION_NO_FULL_PARETO_NO_NOVEL_LOWER_BOUND"
MODELS = (
    ("S_BYTE_SNAPSHOT", SnapshotF1Reference),
    ("T_GLOBAL_BITMAP_COW", PageCowTree),
    ("T_SEGMENTED_BITMAP_COW", SegmentedPageCowTree),
)
ALIASES = {
    "setup_remote_page_writes": "setup pages with explicit padded byte transfer",
    "set_remote_page_reads": "reads charged by each model on SET, no cache assumption",
    "set_remote_page_writes": "page-image API writes on the same three SETs",
    "query_remote_page_reads": "page-image API reads for the same issued queries",
    "query_reply_payload_bytes": "remote proof/full-image bytes without network framing",
    "gc_remote_page_reads": "model-specific mark and full highwater directory/bitmap reads",
    "gc_remote_page_writes_observed": "different GC deletion/accounting conventions; not a Pareto axis",
    "gc_logical_pages_freed": "logical free-page calls, NOT device trim or secure erase",
    "authority_pin_page_writes": "separate ideal trusted authority page-image writes",
    "peak_trusted_bits_declared": "incomplete reference-owned trusted state, excludes CPU transient state",
    "peak_remote_pages": "live remote page-image pages including metadata",
    "set_remote_upload_bytes": "padded page-image bytes sent by author on three SETs",
}


# Exact raw ledgers underlying every published diagnostic. Missing Counter
# keys are NOT interpreted as a free 0; a future refactor that stops charging
# an operation must fail the reproducible gate instead.
SOURCE_COUNTERS = {
    "S_BYTE_SNAPSHOT": {
        "setup_remote_page_writes": ("setup_full_page_writes",),
        "set_remote_page_reads": ("set_full_page_reads",),
        "set_remote_page_writes": ("set_full_page_writes",),
        "query_remote_page_reads": ("query_full_page_reads",),
        "query_reply_payload_bytes": ("query_remote_payload_bytes",),
        "gc_remote_page_reads": ("gc_directory_page_reads",),
        "gc_remote_page_writes_observed": ("gc_manifest_page_writes",),
        "gc_logical_pages_freed": ("gc_logical_pages_freed",),
        "authority_pin_page_writes": ("pin_control_full_page_writes",),
        "peak_trusted_bits_declared": ("@trusted_bits",),
        "peak_remote_pages": ("peak_remote_pages",),
        "set_remote_upload_bytes": ("author_remote_upload_bytes",),
    },
    "T_GLOBAL_BITMAP_COW": {},
    "T_SEGMENTED_BITMAP_COW": {},
}
_COW_COUNTERS = {
    "setup_remote_page_writes": (
        "setup_node_page_writes", "setup_root_page_writes",
        "setup_bitmap_page_writes"),
    "set_remote_page_reads": (
        "set_node_page_reads", "set_root_page_reads", "set_bitmap_page_reads"),
    "set_remote_page_writes": (
        "set_node_page_writes", "set_root_page_writes", "set_bitmap_page_writes"),
    "query_remote_page_reads": ("query_node_page_reads", "query_root_page_reads"),
    "query_reply_payload_bytes": ("query_proof_payload_bytes",),
    "gc_remote_page_reads": (
        "gc_node_page_reads", "gc_root_page_reads",
        "gc_bitmap_page_reads", "gc_node_slot_scan_page_reads",
        "gc_root_slot_scan_page_reads"),
    "gc_remote_page_writes_observed": ("gc_bitmap_page_writes",),
    "gc_logical_pages_freed": ("gc_logical_pages_freed",),
    "authority_pin_page_writes": ("authority_pin_page_writes",),
    "peak_trusted_bits_declared": ("@trusted_bits",),
    "peak_remote_pages": ("peak_remote_pages",),
    "set_remote_upload_bytes": ("set_remote_upload_bytes",),
}
for _name in ("T_GLOBAL_BITMAP_COW", "T_SEGMENTED_BITMAP_COW"):
    SOURCE_COUNTERS[_name] = dict(_COW_COUNTERS)


def _audit_raw_sources(model: str, m, observed: dict,
                       captured_peak_trusted_bits: int) -> dict[str, list[str]]:
    if set(SOURCE_COUNTERS[model]) != set(ALIASES):
        raise AssertionError("incomplete diagnostic-source map")
    source = SOURCE_COUNTERS[model]
    for axis, keys in source.items():
        if not keys:
            raise AssertionError("empty raw provenance")
        if keys == ("@trusted_bits",):
            # PIN/UNPIN have already released history after the trace.
            # The declared peak was captured while both PINs were live.
            value = captured_peak_trusted_bits
        else:
            if any(k not in m.ledger for k in keys):
                raise AssertionError(
                    f"missing explicitly charged {model}/{axis}: {keys}")
            value = sum(m.ledger[k] for k in keys)
        if observed[axis] != value:
            raise AssertionError(
                f"provenance drift {model}/{axis}: {observed[axis]} != {value}")
    return {k: list(v) for k, v in source.items()}


def _add(ledger: Counter, *keys: str) -> int:
    return sum(ledger[k] for k in keys)


def _snapshot_costs(m: SnapshotF1Reference, trusted_peak: int) -> dict:
    l = m.ledger
    return {
        "setup_remote_page_writes": l["setup_full_page_writes"],
        "set_remote_page_reads": l["set_full_page_reads"],
        "set_remote_page_writes": l["set_full_page_writes"],
        "query_remote_page_reads": l["query_full_page_reads"],
        "query_reply_payload_bytes": l["query_remote_payload_bytes"],
        "gc_remote_page_reads": l["gc_directory_page_reads"],
        "gc_remote_page_writes_observed": l["gc_manifest_page_writes"],
        "gc_logical_pages_freed": l["gc_logical_pages_freed"],
        "authority_pin_page_writes": l["pin_control_full_page_writes"],
        "peak_trusted_bits_declared": trusted_peak,
        "peak_remote_pages": l["peak_remote_pages"],
        "set_remote_upload_bytes": l["author_remote_upload_bytes"],
    }


def _cow_costs(m: PageCowTree, trusted_peak: int) -> dict:
    l = m.ledger
    return {
        "setup_remote_page_writes": _add(
            l, "setup_node_page_writes", "setup_root_page_writes",
            "setup_bitmap_page_writes"),
        "set_remote_page_reads": _add(
            l, "set_node_page_reads", "set_root_page_reads",
            "set_bitmap_page_reads"),
        "set_remote_page_writes": _add(
            l, "set_node_page_writes", "set_root_page_writes",
            "set_bitmap_page_writes"),
        "query_remote_page_reads": _add(
            l, "query_node_page_reads", "query_root_page_reads"),
        "query_reply_payload_bytes": l["query_proof_payload_bytes"],
        "gc_remote_page_reads": _add(
            l, "gc_node_page_reads", "gc_root_page_reads",
            "gc_bitmap_page_reads", "gc_node_slot_scan_page_reads",
            "gc_root_slot_scan_page_reads"),
        "gc_remote_page_writes_observed": l["gc_bitmap_page_writes"],
        "gc_logical_pages_freed": l["gc_logical_pages_freed"],
        "authority_pin_page_writes": l["authority_pin_page_writes"],
        "peak_trusted_bits_declared": trusted_peak,
        "peak_remote_pages": l["peak_remote_pages"],
        "set_remote_upload_bytes": l["set_remote_upload_bytes"],
    }


def _partial_vector(observed: dict, model: str) -> tuple[dict, dict]:
    """Every populated axis has same page-image unit and counter provenance.

    Full Pareto is forbidden: ghost setup state, storage GC semantics,
    authority framing, cryptographic proof and durability remain unpriced.
    """
    costs = {axis: None for axis in PRICE_AXES}
    provenance: dict[str, str] = {}
    supported = {
        "peak_remote_pages": "peak_remote_pages",
        "set_remote_page_writes": "set_remote_page_writes",
        "query_remote_page_reads": "query_remote_page_reads",
        "proof_payload_bytes": "query_reply_payload_bytes",
        "gc_remote_reads": "gc_remote_page_reads",
        "author_upload_bytes": "set_remote_upload_bytes",
    }
    for axis, field in supported.items():
        costs[axis] = observed[field]
        provenance[axis] = field
    # Even when source references return a plausible value, these axes
    # are not total comparable model costs.
    caveats = {
        "trusted_bits": "Declared peak excludes transient COW/GC reachability and differing author setup",
        "pinned_retained_pages": "COW sharing needs a separately paid reachable-history accounting pass",
        "gc_remote_writes": "Snapshot charges deleted manifests; COW charges updated bitmap, free-page semantics differ",
        "anchor_bytes": "Ideal global CAS/PIN authority framing and durability not fully serialized",
        "prover_work": "Hash and node traversal CPU units not normalized across references",
        "verifier_work": "SHA digest inputs and parity extraction operations not normalized",
        "setup_bytes": "Only remote page upload charged; author setup CPU/ram, trust publication incomplete",
        "durability_barriers": "Ideal page-image API; no fsync/atomic crash protocol",
    }
    for k in PRICE_AXES:
        if costs[k] is None and k not in caveats:
            caveats[k] = "Requires further independent source-level audit"
    if set(costs) != set(PRICE_AXES) or (set(caveats) | set(provenance)) != set(PRICE_AXES):
        raise AssertionError("invalid full reconciliation axis registry")
    if any(type(v) is not int or v < 0 for v in costs.values() if v is not None):
        raise AssertionError("nonconserving or negative comparable cost")
    return costs, {"sources": provenance, "unknown_reasons": caveats}


def _intervals(n: int, profile: str) -> tuple[tuple[int, int], ...]:
    if profile == "representative":
        return ranges(n)
    if profile == "all_intervals":
        return tuple((i, j) for i in range(n) for j in range(i+1, n+1))
    raise ValueError("unknown bounded query profile")


def _updated_words(initial: tuple[int, ...]):
    words = [initial]
    n = len(initial)
    for k in range(3):
        word = list(words[-1])
        i = (0, min(1, n - 1), n - 1)[k]
        b = word[i] if k == 1 else 1 ^ word[i]
        word[i] = b
        words.append(tuple(word))
        yield k+1, i, b, tuple(word)


def _query(m, kind, reader, lo, hi, epoch=None):
    if kind == "snapshot":
        return m.latest(reader, lo, hi) if epoch is None else m.as_of(reader, epoch, lo, hi)
    return m.query(reader, lo, hi, as_of=epoch)


def reconcile(n: int, p: int, initial: tuple[int, ...] | None = None,
              profile: str = "representative", legacy: bool = True) -> dict:
    validate_contract()
    if type(n) is not int or not 1 <= n <= 2048 or type(p) is not int or not 1 <= p <= 4096:
        raise ValueError("finite F1 bounds")
    word = tuple(i & 1 for i in range(n)) if initial is None else tuple(initial)
    if len(word) != n or any(type(x) is not int or x not in (0, 1) for x in word):
        raise ValueError("invalid GF2 initial word")
    chosen = _intervals(n, profile)
    words = [word] + [row[3] for row in _updated_words(word)]
    if words[2] != words[1] or words[0] == words[1] or words[2] == words[3]:
        raise AssertionError("missing no-op or changing update")
    comparators = []
    for name, factory in MODELS:
        m = factory(word, page_bytes=p)
        kind = "snapshot" if name.startswith("S_") else "cow"
        if m.pin_current(0) != 0:
            raise AssertionError("expected reader0 PIN e0")
        for e, i, b, expected in _updated_words(word):
            if m.set(i,b) != e:
                raise AssertionError("wrong epoch/no-op transcript")
            if e == 2 and m.pin_current(1) != 2:
                raise AssertionError("expected reader1 PIN e2")
        if m.epoch != 3 or m.ledger["set_changed_logical_bits"] != 2:
            raise AssertionError("incorrect common GF2 changes")
        peaks = m.trusted_bits
        remote_peak = m.remote_pages
        # Same query count and same exact [left,right) range selection in all models.
        for lo, hi in chosen:
            cases = [(0, None, words[3]), (1, None, words[3]),
                     (0, 0, words[0]), (1, 2, words[2])]
            for reader, as_of, expected in cases:
                actual = _query(m, kind, reader, lo, hi, as_of)
                if actual != (sum(expected[lo:hi]) & 1):
                    raise AssertionError("query returned wrong exact GF2 parity")
        if m.gc() < 0:
            raise AssertionError("negative reclaimed pages")
        roots_after_first_gc = set(m.remote) if kind == "snapshot" else set(m.roots)
        if roots_after_first_gc != {0, 2, 3}:
            raise AssertionError("GC reclaimed independent PIN")
        m.unpin(0, 0)
        m.gc()
        roots_after_unpin0 = set(m.remote) if kind == "snapshot" else set(m.roots)
        if roots_after_unpin0 != {2, 3}:
            raise AssertionError("GC reclaimed retained PIN2")
        m.unpin(1, 2)
        m.gc()
        roots_after_unpin2 = set(m.remote) if kind == "snapshot" else set(m.roots)
        if roots_after_unpin2 != {3}:
            raise AssertionError("GC did not reclaim unpinned versions")
        if m.trusted_bits >= peaks:
            # Trusted state may include latest writer; both PINs should be gone.
            raise AssertionError("PIN authority/reader trusted memory not released")
        if m.ledger["peak_remote_pages"] < remote_peak:
            raise AssertionError("remote peak lost")
        if name.startswith("T_SEGMENTED") and not m.segment_matches_storage():
            raise AssertionError("remote bitmap no longer matches physical pages")
        observed = _snapshot_costs(m, peaks) if kind == "snapshot" else _cow_costs(m, peaks)
        if observed["set_remote_page_writes"] * p != observed["set_remote_upload_bytes"]:
            raise AssertionError("remote SET byte-to-page nonconservation")
        if observed["setup_remote_page_writes"] * p != m.ledger["setup_remote_upload_bytes"]:
            raise AssertionError("remote SETUP byte-to-page nonconservation")
        if observed["set_remote_page_writes"] <= 0 or observed["query_remote_page_reads"] <= 0:
            raise AssertionError("zero but mandatory I/O cost")
        raw_sources = _audit_raw_sources(name, m, observed, peaks)
        if (observed["query_reply_payload_bytes"]
                > observed["query_remote_page_reads"] * p):
            raise AssertionError("query payload exceeds full read page images")
        priced, audit = _partial_vector(observed, name)
        audit["raw_counter_sources"] = raw_sources
        row = {"name": name, "service": SERVICE, "cost_model": PAGE_API,
               "status": "PARTIAL_PRICING_NO_FULL_PARETO",
               "costs": priced, "audit": audit,
               "observed": observed, "source_ledger": dict(m.ledger)}
        comparators.append(row)
    if legacy and profile == "representative":
        old = legacy_exercise(n, p, word)
        if not old["all_honest_answers_verified"] or old["history"]["epochs"] != 3:
            raise AssertionError("legacy transcript was not independently checked")
        for baseline in old["comparators"][1:]:
            nulls = {a: None for a in PRICE_AXES}
            comparators.append({"name": baseline["name"],
                                # B2-A's reader1 performs an extra catch-up
                                # query before PIN2: not an identical physical
                                # request transcript to the PAGE-001 models.
                                "service": "LEGACY_B2A_LOGICAL_TRACE_WITH_CATCHUP",
                                "cost_model": baseline["cost_model"],
                                "status": "LEGACY_LOGICAL_ONLY_NOT_PAGE_PRICED",
                                "costs": nulls,
                                "audit": {"sources": {},
                                          "unknown_reasons": {k:"legacy logical model includes reader catch-up and lacks full page/CAS/GC price" for k in PRICE_AXES},
                                          "operation_trace_identical": False},
                                "observed": {}, "source_ledger": {}})
    if any(candidate_dominates(a,b) is not None for a in comparators for b in comparators):
        raise AssertionError("incomplete F1 Pareto was spuriously decided")
    all_writes = {x["name"]: x["observed"]["set_remote_page_writes"]
                  for x in comparators if "set_remote_page_writes" in x["observed"]}
    return {"status": STATUS, "root_novelty": "OPEN_UNPROVED",
            "F1_proof_of_joint_lower_bound": False, "n":n, "P":p,
            "workload": {"profile":profile,"SET_epochs":3,"no_op_epochs":[2],
                         "PIN_epochs":{"reader0":0,"reader1":2},
                         "ranges":list(chosen), "range_query_count_per_model":4*len(chosen),
                         "GC_runs":3,"UNPIN_calls":2},
            "byte_conserving":True,
            "comparators":comparators,"remote_SET_page_writes":all_writes,
            "pareto":"UNDECIDABLE_MISSING_AXES", "fully_priced_models":0}


def report():
    cases=[reconcile(n,p,legacy=True) for n,p in ((1,1),(5,2),(33,2),(64,64),(257,4096))]
    return {"status":STATUS,"cases":cases,"root_novelty":"OPEN_UNPROVED"}


if __name__ == "__main__":
    print(json.dumps(report(),indent=2))
