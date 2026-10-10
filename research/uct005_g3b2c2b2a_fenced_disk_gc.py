#!/usr/bin/env python3
"""UCT-005 C2-B2-A: authenticated PIN-fenced, disk-buffered GC data plane.

Combines C2-A disk FIFO/mark/bitmap collector with C2-B1 HMAC PIN journal,
ideal monotone GC fence, and a staged immutable on-disk generation.
No unrestricted in-RAM reachability map or generation-wide Python bitmap
in this adapter. The B2-B writer/exporter and B1 attested root catalog DO
still use O(H+n) Python RAM; NOT an end-to-end bounded-RAM server.
TemporaryFile/fsync/CAS are a modeled durability ordering, not crash proof.
"""
from dataclasses import dataclass
from hashlib import sha256
import hmac
import os
import struct
import tempfile

from uct005_g3b2c2a_disk_gc import PIN, ROOT, DiskGcArena, Cost
from uct005_g3b2c2b1_pin_generation import (
    GENHEAD, MAGIC, ZERO, Crash, Integrity, PinJournal, PinFence, GcFence,
)

DOMAIN = b"UCT005/C2B2A/GEN/"
CUTS = (None, "copy", "mark", "write", "flush", "publish_before",
        "publish", "trim")


@dataclass(frozen=True)
class FencedStage:
    generation: int
    pin_fence: PinFence
    digest: bytes
    collector_cost: Cost
    total_nodes: int


class DiskFencedGC:
    """Serialized honest control actor, bounded explicit *GC data-plane* pages.

    Root attestations and MAC owner key are trusted inputs; B1 PinJournal has
    an unbounded historical-root map, so a whole-system O(1)-RAM claim would
    be false. Untrusted storage cannot serve as a trusted monotone anchor.
    """
    COLLECTOR_BUFFERS = 6

    def __init__(self, arena: DiskGcArena, journal: PinJournal):
        if not isinstance(arena, DiskGcArena) or not isinstance(journal, PinJournal):
            raise TypeError("disk arena and authentic PIN journal required")
        if journal.clients != arena.clients or journal.page_bytes != arena.page_bytes:
            raise ValueError("incompatible client/page configurations")
        if arena.latest != journal.latest:
            raise ValueError("root epoch history differs")
        if getattr(arena, "_uct005_writer_inflight", False):
            raise Integrity("cannot open GC during in-flight COW writer")
        self.arena = arena
        self.journal = journal
        self.page_bytes = arena.page_bytes
        self.count = arena.count
        self.frozen_epoch = arena.latest
        self.frozen_digest = arena.latest_trusted_checkpoint.digest
        self.blocks = (self.count + self.page_bytes - 1) // self.page_bytes
        self.pages_per_gen = 1 + self.blocks
        # No all-epochs reachability set; compare attestations one at a time.
        self.setup_root_page_reads = 0
        for epoch in range(arena.epochs):
            root, digest = ROOT.unpack_from(arena._page(arena.roots, epoch))
            self.setup_root_page_reads += 1
            if journal.roots[epoch] != digest:
                raise Integrity("root catalog mismatch with authentic checkpoint")
        self.generations = tempfile.TemporaryFile(mode="w+b", buffering=0)
        self.anchor = GcFence(0, 0, ZERO)
        self.durable_bytes = 0
        self.staged = None
        self.io = {
            "source_bitmap_reads": 0, "candidate_bitmap_writes": 0,
            "pin_root_reads": 0, "pin_slot_writes": 0,
            "generation_bitmap_reads": 0, "generation_page_writes": 0,
            "generation_page_reads": 0, "resident_bitmap_reads": 0,
            "resident_bitmap_writes": 0, "metadata_fsyncs": 0,
            "metadata_truncates": 0, "gc_anchor_publications": 0,
            "sha256_digests": 0, "logical_trim_commands": 0,
        }

    def _assert_forest_frozen(self):
        # A live COW author can increase both node count and epoch. A GC
        # instance constructed for the previous forest must FAIL CLOSED:
        # its bitmap cardinality and generation digest format are stale.
        if (getattr(self.arena, "_uct005_writer_inflight", False) or
                self.arena.count != self.count or
                self.arena.latest != self.frozen_epoch or
                self.arena.latest_trusted_checkpoint.epoch != self.frozen_epoch or
                self.journal.latest != self.frozen_epoch or
                self.arena.latest_trusted_checkpoint.digest != self.frozen_digest):
            raise Integrity("GC instance frozen to an earlier writer/root epoch")

    def _offset(self, generation):
        if type(generation) is not int or generation < 1:
            raise ValueError("invalid immutable generation")
        return (generation-1) * self.pages_per_gen * self.page_bytes

    def _page_read(self, f, index, key):
        f.seek(index * self.page_bytes)
        data = f.read(self.page_bytes)
        self.io[key] += 1
        if len(data) != self.page_bytes:
            raise Integrity("missing/truncated physical bitmap image")
        return data

    def _page_write(self, f, index, data, key):
        if len(data) != self.page_bytes:
            raise ValueError("noncanonical physical bitmap write")
        f.seek(index * self.page_bytes)
        if f.write(data) != self.page_bytes:
            raise OSError("short full-page write")
        self.io[key] += 1

    def _pin_slots(self, expected):
        """Derive *every* untrusted C2-A pin slot from published HMAC prefix."""
        pins = self.journal.replay()
        if self.journal.tip != expected:
            raise Integrity("PIN tip changed while constructing snapshot")
        p = self.page_bytes
        for client in range(self.journal.clients):
            epoch = pins.get(client)
            if epoch is None:
                image = bytes(p)
            else:
                root_page = self._page_read(
                    self.arena.roots, epoch, "pin_root_reads")
                root, digest = ROOT.unpack_from(root_page)
                if digest != self.journal.roots[epoch]:
                    raise Integrity("pinned DAG root conflicts with trusted checkpoint")
                image = PIN.pack(epoch, root, digest).ljust(p, b"\0")
            self._page_write(self.arena.pins, client, image, "pin_slot_writes")
        if self.journal.tip != expected:
            raise Integrity("PIN tip changed during slot preparation")
        return pins

    def _digest_start(self, generation, fence):
        h = sha256()
        h.update(DOMAIN)
        h.update(generation.to_bytes(8, "big"))
        h.update(fence.seq.to_bytes(8, "big"))
        h.update(fence.tag)
        return h

    def prepare(self, fail_at=None):
        if fail_at not in CUTS:
            raise ValueError("unknown crash cut before any mutation")
        self._assert_forest_frozen()
        if self.staged is not None:
            raise Integrity("unpublished candidate must be recovered/discarded first")
        fence = self.journal.tip
        self._pin_slots(fence)
        candidate = tempfile.TemporaryFile(mode="w+b", buffering=0)
        try:
            # Explicit full-image clone; C2-A GC will only mutate candidate.
            for block in range(self.blocks):
                page = self._page_read(self.arena.alive, block,
                                       "source_bitmap_reads")
                self._page_write(candidate, block, page,
                                 "candidate_bitmap_writes")
                del page
            if fail_at == "copy":
                raise Crash("candidate clone cut, active pages unmodified")
            original_live = self.arena.alive
            original_flag = self.arena._has_reclaimed
            try:
                self.arena.alive = candidate
                gc_cost = self.arena.collect(self.arena.latest)
            finally:
                self.arena.alive = original_live
                self.arena._has_reclaimed = original_flag
            if fail_at == "mark":
                raise Crash("candidate completed but uncommitted")
            # Stage a generation as [authenticated header][bitmap page images].
            # Stream bitmap digest with O(P) explicit page-buffer workspace.
            generation = self.anchor.generation + 1
            header_pos = self._offset(generation)
            digest = self._digest_start(generation, fence)
            remaining = self.count
            for block in range(self.blocks):
                page = self._page_read(candidate, block,
                                       "generation_bitmap_reads")
                valid = min(remaining, self.page_bytes)
                if (any(v not in (0, 1) for v in page[:valid])
                        or page[valid:] != bytes(self.page_bytes-valid)):
                    raise Integrity("invalid candidate live-bitmap padding/data")
                digest.update(page[:valid])
                remaining -= valid
                del page
            image_digest = digest.digest()
            self.io["sha256_digests"] += 1
            head = GENHEAD.pack(MAGIC, generation, fence.seq,
                                fence.tag, image_digest).ljust(self.page_bytes, b"\0")
            first_page = header_pos // self.page_bytes
            self._page_write(self.generations, first_page, head,
                             "generation_page_writes")
            for block in range(self.blocks):
                page = self._page_read(candidate, block,
                                       "generation_bitmap_reads")
                self._page_write(self.generations, first_page+1+block, page,
                                 "generation_page_writes")
                del page
            if fail_at == "write":
                raise Crash("GC generation written but not fsync'ed")
            os.fsync(self.generations.fileno())
            self.io["metadata_fsyncs"] += 1
            self.durable_bytes = header_pos + self.pages_per_gen*self.page_bytes
            if fail_at == "flush":
                raise Crash("GC generation fsync'ed but not published")
            result = FencedStage(generation, fence, image_digest,
                                 gc_cost, self.count)
            self.staged = result
            return result
        finally:
            candidate.close()

    def _verify_generation(self, expected):
        """Full streaming authentication *before any* destructive write."""
        pos = self._offset(expected.generation) // self.page_bytes
        image = self._page_read(self.generations, pos,
                                "generation_page_reads")
        magic, gen, seq, tag, digest = GENHEAD.unpack_from(image)
        if (magic != MAGIC or gen != expected.generation
                or seq != expected.pin_seq or digest != expected.digest
                or image[GENHEAD.size:] != bytes(self.page_bytes-GENHEAD.size)):
            raise Integrity("generation header inconsistent with trusted CAS")
        # A future journal tip is permitted: new PINs are limited to retained
        # historical roots or current latest at prior generation publication.
        _, trusted_tag = self.journal._prefix(seq)
        if not hmac.compare_digest(tag, trusted_tag):
            raise Integrity("GC fence refers to unauthenticated PIN history")
        hasher = self._digest_start(gen, PinFence(seq, tag))
        remaining = self.count
        for block in range(self.blocks):
            page = self._page_read(
                self.generations, pos+1+block, "generation_page_reads")
            used = min(self.page_bytes, remaining)
            if (any(v not in (0, 1) for v in page[:used])
                    or page[used:] != bytes(self.page_bytes-used)):
                raise Integrity("noncanonical generation bitmap")
            hasher.update(page[:used])
            remaining -= used
            del page
        self.io["sha256_digests"] += 1
        if not hmac.compare_digest(hasher.digest(), digest):
            raise Integrity("GC image tampered or torn")
        return pos

    def publish(self, stage, fail_at=None):
        if fail_at not in (None, "publish_before", "publish", "trim"):
            raise ValueError("invalid publication crash cut")
        self._assert_forest_frozen()
        if not isinstance(stage, FencedStage) or self.staged != stage:
            raise Integrity("only currently staged immutable generation can publish")
        if stage.generation != self.anchor.generation+1:
            raise Integrity("stale generation number")
        if self.journal.tip != stage.pin_fence:
            raise Integrity("PIN changed between mark and GC commit")
        required_end = self._offset(stage.generation)+self.pages_per_gen*self.page_bytes
        if self.durable_bytes < required_end:
            raise Integrity("GC bitmap lacks a modeled fsync barrier")
        proposed = GcFence(stage.generation, stage.pin_fence.seq, stage.digest)
        self._verify_generation(proposed)
        if fail_at == "publish_before":
            raise Crash("GC stage durable, trusted anchor unchanged")
        # Ideal atomic trusted CAS, serialized against PIN/UNPIN publication.
        if self.journal.tip != stage.pin_fence:
            raise Integrity("concurrent PIN invalidated GC candidate")
        pins = self.journal.replay()
        self.anchor = proposed
        self.io["gc_anchor_publications"] += 1
        self.journal.allowed = {self.journal.latest} | set(pins.values())
        self.staged = None
        if fail_at == "publish":
            raise Crash("trusted GC fence published, logical bitmap not yet trimmed")
        return self.recover(fail_at="trim" if fail_at == "trim" else None)

    def recover(self, fail_at=None):
        if fail_at not in (None, "trim"):
            raise ValueError("unknown recovery crash cut")
        self._assert_forest_frozen()
        self.journal.crash_recover()
        self.generations.truncate(self.durable_bytes)
        self.io["metadata_truncates"] += 1
        self.staged = None
        if self.anchor.generation == 0:
            return 0
        first = self._verify_generation(self.anchor)
        # Retention policy derives from the EXACT journal prefix observed
        # at publication, not a mutable/stale replay of an untrusted pin slot.
        retained, _ = self.journal._prefix(self.anchor.pin_seq)
        # A later authorized PIN could only target one of these retained roots
        # or the newest epoch; journal.allowed is frozen by trust after commit.
        self.journal.allowed = {self.journal.latest} | set(retained.values())
        deleted = 0
        remaining = self.count
        for block in range(self.blocks):
            desired = self._page_read(
                self.generations, first+1+block, "generation_page_reads")
            actual = self._page_read(self.arena.alive, block,
                                     "resident_bitmap_reads")
            used = min(remaining, self.page_bytes)
            next_bytes = bytearray(actual)
            changed = False
            for i in range(used):
                if desired[i] > actual[i]:
                    raise Integrity("GC attempted to resurrect a freed page")
                if actual[i] and not desired[i]:
                    next_bytes[i] = 0
                    deleted += 1
                    self.io["logical_trim_commands"] += 1
                    changed = True
            if changed:
                self._page_write(self.arena.alive, block, bytes(next_bytes),
                                 "resident_bitmap_writes")
                self.arena._has_reclaimed = True
                if fail_at == "trim":
                    raise Crash("interrupted post-publish logical bit-flip")
            remaining -= used
            del desired, actual, next_bytes
        return deleted

    def query(self, epoch, left, right, checkpoint):
        """Reference full-tree query, NOT optimized or bounded-CPU query."""
        self._assert_forest_frozen()
        if type(epoch) is not int or epoch not in self.journal.roots:
            raise ValueError("invalid authenticated epoch")
        if self.journal.roots[epoch] != checkpoint.digest or epoch != checkpoint.epoch:
            raise Integrity("checkpoint not from trusted author root catalog")
        self._pin_slots(self.journal.tip)
        return self.arena.verify_range(epoch, left, right, checkpoint)

    def cost(self):
        page_reads = sum(self.io[k] for k in (
            "source_bitmap_reads", "pin_root_reads", "generation_bitmap_reads",
            "generation_page_reads", "resident_bitmap_reads"))
        page_writes = sum(self.io[k] for k in (
            "candidate_bitmap_writes", "pin_slot_writes",
            "generation_page_writes", "resident_bitmap_writes"))
        return {
            **self.io, "page_reads": page_reads, "page_writes": page_writes,
            "read_bytes": page_reads*self.page_bytes,
            "write_bytes": page_writes*self.page_bytes,
            "trusted_gc_anchor_bytes": 48*self.io["gc_anchor_publications"],
            "external_pin_journal_cost": self.journal.c.as_dict(self.page_bytes),
            "setup_root_page_reads": self.setup_root_page_reads,
            "page_size": self.page_bytes,
            "gc_explicit_page_buffers": self.COLLECTOR_BUFFERS,
            "scope": "DATA_PLANE_GC_ONLY_NO_POWERLOSS_OR_ONLINE_SET_PROOF",
        }

    def close(self):
        self.generations.close()


def diagnostic():
    import json
    from uct005_g3b2b_range_tree import TreeWriter
    w = TreeWriter((0,)*8)
    w.set(0, 1)
    w.set(3, 1)
    arena = DiskGcArena.from_writer(w, page_bytes=4096, clients=2)
    journal = PinJournal(w.epochs, b"owner-secret-UCT005-C2B2A-32-bytes", clients=2)
    service = DiskFencedGC(arena, journal)
    try:
        journal.event("PIN", 0, w.epochs[0])
        stage = service.prepare()
        gc_freed = service.publish(stage)
        assert service.query(w.anchor.epoch, 0, 7, w.anchor) == 0
        return {"freed": gc_freed, "staged": stage.generation,
                "page_gc": stage.collector_cost.__dict__,
                "cost": service.cost(),
                "status": "CONTROL_DATA_PLANE_JOIN_IDEAL_CAS_AND_FSYNC"}
    finally:
        service.close()
        journal.close()
        arena.close()


if __name__ == "__main__":
    import json
    print(json.dumps(diagnostic(), sort_keys=True, indent=2))
