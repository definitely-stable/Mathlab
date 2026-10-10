#!/usr/bin/env python3
"""D1-B2-F1 independent paid offline reachability and PIN-retention oracle.

The page-image snapshot / COW systems remain conditional honest-author models.
This audit DOES NOT produce a free operational index: each authenticated root
and immutable COW node access charges additional offline audit page reads and
hash work. Its counters are not merged into routine F1 query/SET/GC pricing.
No full Pareto proof, crash durability, or real physical SSD TRIM inference.
"""
from __future__ import annotations

from collections import Counter
from itertools import product
import json

from uct005_d1b0_f1_reference import SnapshotF1Reference
from uct005_d1b2b_page_cow import (
    Abort as CowAbort, PageCowTree, NODE_BYTES, ROOT_BYTES, _ceil,
)
from uct005_d1b2b1_segmented_bitmap import SegmentedPageCowTree

CLASSIFICATION = "CONDITIONAL_PAID_OFFLINE_SHARED_PIN_RETENTION_NOT_FULL_F1_PARETO"
READER_IDS = (0, 1)


def _pins(m) -> dict[int, bytes]:
    """Return distinct independently trusted epoch root commitments."""
    if isinstance(m, SnapshotF1Reference):
        pin_registry = m.pin_registry
    else:
        pin_registry = m.authority_pins
    roots: dict[int, bytes] = {}
    for (reader, epoch), digest in pin_registry.items():
        if reader not in READER_IDS:
            raise AssertionError("unknown authority PIN owner")
        if epoch in roots and roots[epoch] != digest:
            raise CowAbort("inconsistent same-epoch trusted PINs")
        roots[epoch] = digest
    return roots


def _snapshot_roots(m: SnapshotF1Reference):
    expected = _pins(m)
    if m.epoch in expected and expected[m.epoch] != m.latest_root:
        raise ValueError("snapshot trusted PIN conflicts with latest root")
    expected[m.epoch] = m.latest_root
    return expected


def _cow_roots(m: PageCowTree):
    roots = _pins(m)
    if m.epoch in roots and roots[m.epoch] != m.latest_digest:
        raise CowAbort("PIN conflicts with trusted latest anchor")
    roots[m.epoch] = m.latest_digest
    return roots


def _cow_walk(m: PageCowTree, epoch: int, digest: bytes) -> set[int]:
    """Authenticated traversal without an unpriced stored node directory."""
    root_id, root_digest = m._root(epoch, digest, "retention_audit")
    nodes: set[int] = set()
    seen: dict[int, tuple[bytes, int, int]] = {}

    def visit(nid: int, expected_digest: bytes, lo: int, hi: int):
        previous = seen.get(nid)
        if previous is not None:
            if previous != (expected_digest, lo, hi):
                raise CowAbort("same node ID reused with conflicting authenticated interval")
            return
        rec = m._read_node(nid, expected_digest, hi-lo, "retention_audit")
        seen[nid] = (expected_digest, lo, hi)
        nodes.add(nid)
        if hi - lo == 1:
            if rec["kind"] != 0:
                raise CowAbort("retention audit encountered invalid leaf")
            return
        if rec["kind"] != 1:
            raise CowAbort("retention audit encountered invalid internal node")
        mid = (lo + hi)//2
        visit(rec["left"], rec["ld"], lo, mid)
        visit(rec["right"], rec["rd"], mid, hi)

    visit(root_id, root_digest, 0, m.n)
    return nodes


def _bitmap_audit(m: PageCowTree) -> int:
    """Charge every issued bitmap page; snapshot has no bitmap."""
    if isinstance(m, SegmentedPageCowTree):
        for kind in ("node", "epoch"):
            issued = m._max_index(kind)
            for i in range(issued // m.bits_per_segment + 1):
                m._get_page(kind, i, "retention_audit")
    else:
        m._read_bitmap("retention_audit")
    return m.bitmap_pages


def retention_audit(m) -> dict:
    """Offline audit of incremental PIN-retained pages over LATEST alone.

    Audit's own page/hash operations are explicitly in retention_audit_* ledger
    counters; this is not an online constant-cost operation and is not reused
    silently by the charged GC implementation.
    """
    before = {k:v for k,v in m.ledger.items()
              if k.startswith("retention_audit_")
              and not k.startswith("retention_audit_last_")}
    if isinstance(m, SnapshotF1Reference):
        trusted = _snapshot_roots(m)
        p = m.page_bytes
        per_epoch = m._pages_per_snapshot()
        for e, root in sorted(trusted.items()):
            # Public epoch slot address. The page-image dictionaries are
            # untrusted remote storage, NOT an authority lookup oracle.
            m.ledger["retention_audit_slot_page_reads"] += per_epoch
            m.ledger["retention_audit_request_bytes"] += 8
            m.ledger["retention_audit_response_bytes"] += per_epoch*p
            img = m.remote.get(e)
            manifest = m.remote_manifests.get(e)
            if img is None or manifest is None or len(img) != (m.n+7)//8:
                raise ValueError("withheld or malformed pinned snapshot")
            recomputed = m._digest(e,img)
            m.ledger["retention_audit_hash_calls"] += 1
            m.ledger["retention_audit_hash_input_bytes"] += (
                len(b"mathlab.F1.snapshot.v1\0") + len(img) + 16)
            if recomputed != root or manifest != m._manifest(e,img):
                raise ValueError("snapshot PIN root or manifest mismatch")
            m.ledger["retention_audit_hash_calls"] += 1
            m.ledger["retention_audit_hash_input_bytes"] += (
                len(b"mathlab.F1.snapshot.v1\0") + len(img) + 16)
        pinned = set(trusted) - {m.epoch}
        incremental = len(pinned)*per_epoch
        kept = len(trusted)*per_epoch
        latest_only_kept = per_epoch
        bitmap = 0
        overlap = 0
        latest_nodes = 0
        union_nodes = 0
        distinct_root_pages = len(trusted)*m._manifest_pages()
        audit_node_reads = 0
    elif isinstance(m, PageCowTree):
        trusted = _cow_roots(m)
        p = m.P
        root_pages = m.root_pages
        node_pages = m.node_pages
        # Read and check bitmap page images separately from the ordinary
        # mark pass. Their ordinary occupancy bits are advisory, never PINs.
        bitmap = _bitmap_audit(m)
        per_root = {
            epoch: _cow_walk(m, epoch, digest)
            for epoch, digest in sorted(trusted.items())
        }
        latest_set = per_root[m.epoch]
        union = set().union(*per_root.values())
        pinned = set(trusted) - {m.epoch}
        incremental = ((len(union)-len(latest_set))*node_pages
                       + len(pinned)*root_pages)
        kept = len(union)*node_pages + len(trusted)*root_pages + bitmap
        latest_only_kept = len(latest_set)*node_pages + root_pages + bitmap
        latest_nodes = len(latest_set)
        union_nodes = len(union)
        overlap = sum(len(x) for x in per_root.values())-len(union)
        distinct_root_pages = len(trusted)*root_pages
        audit_node_reads = sum(len(x) for x in per_root.values())*node_pages
        # No Python set allocation is free in a real GC. The frozen
        # fixed-u64-ID representation is a diagnostic only, NOT heap bytes.
    else:
        raise TypeError("unsupported reference")

    after = {k:v for k,v in m.ledger.items()
             if k.startswith("retention_audit_")
             and not k.startswith("retention_audit_last_")}
    new_cost = {k: after.get(k,0) - before.get(k,0)
                for k in set(before)|set(after)}
    if any(v<0 for v in new_cost.values()):
        raise AssertionError("audit counter went backward")
    return {
        "classification": CLASSIFICATION,
        "root_novelty": "OPEN_UNPROVED",
        "latest_epoch": m.epoch,
        "distinct_pinned_epochs": sorted(pinned),
        "active_pin_entries": len(m.pin_registry if isinstance(m, SnapshotF1Reference)
                                  else m.authority_pins),
        "incremental_PIN_remote_pages_over_latest": incremental,
        "latest_only_remote_pages_including_metadata": latest_only_kept,
        "authenticated_kept_remote_pages_including_metadata": kept,
        "bitmap_remote_pages_charged": bitmap,
        "root_slot_pages": distinct_root_pages,
        "latest_reachable_COW_nodes": latest_nodes,
        "union_reachable_COW_nodes": union_nodes,
        "shared_references_elided_by_COW": overlap,
        "offline_64bit_id_list_bytes_NOT_python_heap": 8*union_nodes,
        "offline_audit_charged": new_cost,
        "online_gc_price_reused_for_audit": False,
        "full_F1_pinned_retained_axis_proven": False,
    }


def _updated_words(initial):
    words=[tuple(initial)]
    n=len(initial)
    for j in range(3):
        next_word=list(words[-1])
        index=(0,min(1,n-1),n-1)[j]
        if j!=1:
            next_word[index]^=1
        words.append(tuple(next_word))
    return words


def exercise(n: int, p: int, initial: tuple[int,...] | None=None) -> dict:
    if type(n) is not int or not 1<=n<=2048 or type(p) is not int or not 1<=p<=4096:
        raise ValueError("bounded F1 retention oracle")
    bits=tuple(i&1 for i in range(n)) if initial is None else tuple(initial)
    if len(bits)!=n or any(type(x) is not int or x not in (0,1) for x in bits):
        raise ValueError("invalid bit word")
    words=_updated_words(bits)
    rows=[]
    models=(
        ("PAGE001_SNAPSHOT", SnapshotF1Reference),
        ("GLOBAL_BITMAP_COW", PageCowTree),
        ("SEGMENTED_BITMAP_COW", SegmentedPageCowTree),
    )
    for name, cls in models:
        m=cls(bits, page_bytes=p)
        if m.pin_current(0)!=0:
            raise AssertionError("PIN0 epoch")
        for j in range(1,4):
            idx=(0,min(1,n-1),n-1)[j-1]
            if m.set(idx, words[j][idx])!=j:
                raise AssertionError("wrong epoch")
            if j==2 and m.pin_current(1)!=2:
                raise AssertionError("PIN2 epoch")
        q = (m.latest if isinstance(m,SnapshotF1Reference) else m.query)
        for lo,hi in ((0,1),(0,n),(n-1,n)):
            for reader in READER_IDS:
                v=q(reader,lo,hi)
                if v!=(sum(words[3][lo:hi])&1):
                    raise AssertionError("latest parity changed")
            for rd,e in ((0,0),(1,2)):
                v=(m.as_of(rd,e,lo,hi) if isinstance(m, SnapshotF1Reference)
                   else m.query(rd,lo,hi,as_of=e))
                if v!=(sum(words[e][lo:hi])&1):
                    raise AssertionError("pinned parity changed")
        stages=[]
        for stage, revocation in (
            ("PIN0_PIN2", None),
            ("PIN2_ONLY", (0,0)),
            ("LATEST_ONLY", (1,2)),
        ):
            if revocation is not None:
                m.unpin(*revocation)
            pre=m.remote_pages
            info=retention_audit(m)
            audit_keys={k:v for k,v in m.ledger.items()
                        if k.startswith("retention_audit_")}
            freed=m.gc()
            actual=m.remote_pages
            if freed != pre-actual:
                raise AssertionError("GC pages freed mismatch actual resident page delta")
            if actual != info["authenticated_kept_remote_pages_including_metadata"]:
                raise AssertionError("retention root union did not predict post-GC pages")
            if (info["incremental_PIN_remote_pages_over_latest"] !=
                    actual - info["latest_only_remote_pages_including_metadata"]):
                raise AssertionError("PIN delta exceeds authenticated kept-root union")
            for k,v in audit_keys.items():
                if m.ledger[k]!=v:
                    raise AssertionError("GC mutated separately charged audit ledger")
            if (isinstance(m,SegmentedPageCowTree)
                    and not m.segment_matches_storage()):
                raise AssertionError("GC segmentation image corruption")
            stages.append({"stage":stage, "before_gc_remote_pages":pre,
                           "freed_logical_remote_pages":freed,
                           "after_gc_remote_pages":actual,
                           "PIN_incremental_pages":info["incremental_PIN_remote_pages_over_latest"],
                           "offline_audit":info})
        if stages[2]["PIN_incremental_pages"]!=0:
            raise AssertionError("remaining latest-only has nonzero PIN pages")
        if stages[2]["after_gc_remote_pages"]>stages[1]["after_gc_remote_pages"]:
            raise AssertionError("unpinning expanded retained storage")
        if stages[1]["after_gc_remote_pages"]>stages[0]["after_gc_remote_pages"]:
            raise AssertionError("unpinning expanded retained storage")
        rows.append({"model":name,"stages":stages})
    return {"n":n,"P":p,"status":CLASSIFICATION,
            "same_finite_F1_answers_verified": True,
            "root_novelty":"OPEN_UNPROVED","models":rows,
            "completed_full_F1_pareto":False}


def report():
    return {"status":CLASSIFICATION,"root_novelty":"OPEN_UNPROVED",
            "cases":[exercise(n,p) for n,p in
                     ((1,1),(5,2),(33,64),(257,4096))]}


if __name__=="__main__":
    print(json.dumps(report(),indent=2))
