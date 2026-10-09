#!/usr/bin/env python3
"""UCT-005 G3-B2-C2-B1: pinned versions and generation-fenced GC.

Executable *ideal-barrier* protocol using temporary files, explicit os.fsync
calls, HMAC-authenticated append-only page records and two independent ideal
trusted control anchors. This is NOT a proof of power-loss-safe filesystem
behavior or an implementation of a bounded-RAM online writer/collector.
"""
from dataclasses import dataclass
from hashlib import sha256
import hmac
import os
import struct
import tempfile

MAGIC = b"UCTC2B1!"
EVENT = struct.Struct(">8sQBIQ32s32s")
GENHEAD = struct.Struct(">8sQQ32s32s")
ZERO = bytes(32)


def _integer(v, low=0):
    if type(v) is not int or v < low:
        raise ValueError("invalid integer")
    return v


def _digest(data):
    return sha256(data).digest()


class Crash(RuntimeError):
    pass


class Integrity(ValueError):
    pass


@dataclass(frozen=True)
class PinFence:
    seq: int
    tag: bytes


@dataclass(frozen=True)
class GcFence:
    generation: int
    pin_seq: int
    digest: bytes


@dataclass(frozen=True)
class Stage:
    generation: int
    pin_fence: PinFence
    bitmask: bytes
    digest: bytes


class Counters:
    """Logical program I/O; not device IOPS, and flush is not a crash proof."""
    def __init__(self):
        self.page_reads = 0
        self.page_writes = 0
        self.flushes = 0
        self.sha_calls = 0
        self.mac_calls = 0
        self.pin_publications = 0
        self.gc_publications = 0
        self.trim_commands = 0

    def as_dict(self, page_size):
        return {**vars(self), "read_bytes": self.page_reads*page_size,
                "write_bytes": self.page_writes*page_size,
                "pin_anchor_bytes": self.pin_publications*40,
                "gc_anchor_bytes": self.gc_publications*48}


class PinJournal:
    """Authenticated one-full-page-per-event log and independently trusted tip.

    Trust includes the owner's secret HMAC key (NOT on untrusted storage),
    the independently monotone PinFence, authorized root attestations, and a
    single serialized actor for all PIN/UNPIN/GC control transitions.
    File contents alone never grant version freshness or anti-rollback.
    """
    def __init__(self, roots, key, clients=2, page_bytes=4096):
        if type(page_bytes) is not int or page_bytes < max(256, EVENT.size+32):
            raise ValueError("invalid full-image size")
        _integer(clients, 1)
        if not isinstance(key, bytes) or len(key) < 16:
            raise ValueError("owner key required")
        if not roots:
            raise ValueError("attested root history required")
        self.roots = {}
        for checkpoint in roots:
            if type(checkpoint.epoch) is not int or checkpoint.epoch != len(self.roots):
                raise ValueError("contiguous attested epoch roots required")
            self.roots[checkpoint.epoch] = checkpoint.digest
        self.latest = max(self.roots)
        self.clients = clients
        self.key = key
        self.page_bytes = page_bytes
        self.file = tempfile.TemporaryFile(mode="w+b", buffering=0)
        self.tip = PinFence(0, ZERO)  # simulated independent durable authority
        self.durable_pages = 0  # test oracle: only fsync'ed images survive cut
        self.allowed = set(self.roots)  # before first generation publish
        self.c = Counters()

    def _read(self, seq):
        self.file.seek((seq-1)*self.page_bytes)
        raw = self.file.read(self.page_bytes)
        self.c.page_reads += 1
        if len(raw) != self.page_bytes:
            raise Integrity("trusted fence references a missing journal image")
        return raw

    def _encode(self, seq, op, client, epoch, digest, previous):
        base = EVENT.pack(MAGIC, seq, op, client, epoch, digest, previous)
        mac = hmac.new(self.key, b"UCT005/C2B1/PIN/" + base, sha256).digest()
        self.c.mac_calls += 1
        return (base + mac).ljust(self.page_bytes, b"\0"), mac

    def _prefix(self, upto=None):
        if upto is None:
            upto = self.tip.seq
        _integer(upto)
        if upto > self.tip.seq:
            raise Integrity("requested journal future beyond trusted authority")
        prev = ZERO
        current = {}
        for seq in range(1, upto+1):
            raw = self._read(seq)
            base = raw[:EVENT.size]
            mac = raw[EVENT.size:EVENT.size+32]
            if raw[EVENT.size+32:] != bytes(self.page_bytes-EVENT.size-32):
                raise Integrity("noncanonical journal padding")
            magic, actual, op, client, epoch, digest, parent = EVENT.unpack(base)
            expected = hmac.new(
                self.key, b"UCT005/C2B1/PIN/" + base, sha256).digest()
            self.c.mac_calls += 1
            if (magic != MAGIC or actual != seq or parent != prev
                    or not hmac.compare_digest(mac, expected)):
                raise Integrity("forged/replayed/rollback journal record")
            if client >= self.clients:
                raise Integrity("invalid client slot")
            if op == 1:
                if self.roots.get(epoch) != digest or client in current:
                    raise Integrity("invalid PIN event/root")
                current[client] = epoch
            elif op == 2:
                if (digest != ZERO or epoch != 0 or client not in current):
                    raise Integrity("invalid UNPIN event")
                del current[client]
            else:
                raise Integrity("invalid PIN operation")
            prev = mac
        if upto == self.tip.seq and not hmac.compare_digest(prev, self.tip.tag):
            raise Integrity("journal tip disagrees with independent anchor")
        return current, prev

    def replay(self):
        return self._prefix()[0]

    def event(self, op, client, checkpoint=None, fail_at=None):
        if fail_at not in (None, "write", "flush", "publish", "ack"):
            raise ValueError("unknown failure cut before any PIN side effect")
        if op not in ("PIN", "UNPIN") or type(client) is not int or not 0 <= client < self.clients:
            raise ValueError("invalid journal command")
        current = self.replay()  # fail closed if previous pages disappeared
        if op == "PIN":
            if checkpoint is None or checkpoint.epoch not in self.roots:
                raise ValueError("independent authenticated root required")
            epoch, digest = checkpoint.epoch, checkpoint.digest
            if (self.roots[epoch] != digest or epoch not in self.allowed
                    or client in current):
                raise ValueError("unavailable or duplicate pin")
            kind = 1
        else:
            if client not in current:
                raise ValueError("cannot release absent pin")
            epoch, digest, kind = 0, ZERO, 2
        seq = self.tip.seq+1
        raw, tag = self._encode(seq, kind, client, epoch, digest, self.tip.tag)
        self.file.seek((seq-1)*self.page_bytes)
        if self.file.write(raw) != self.page_bytes:
            raise OSError("short journal image write")
        self.c.page_writes += 1
        if fail_at == "write":
            raise Crash("unflushed PIN log image")
        os.fsync(self.file.fileno())
        self.c.flushes += 1
        self.durable_pages = seq
        if fail_at == "flush":
            raise Crash("flushed but unpublished PIN record")
        # Ideal trusted atomic compare-and-swap. No untrusted filesystem
        # operation can mutate this separately trusted monotone state.
        self.tip = PinFence(seq, tag)
        self.c.pin_publications += 1
        if fail_at == "publish":
            raise Crash("published PIN, acknowledgement lost")
        return self.tip

    def crash_recover(self):
        """Idealized discard of data not behind an fsync barrier."""
        self.file.truncate(self.durable_pages*self.page_bytes)
        state = self.replay()
        return state

    def close(self):
        self.file.close()


class GenerationalGC:
    """Immutable COW metadata generations, fenced by the PIN journal tip.

    Graph reachability is supplied by an independent complete *oracle map*:
    epoch -> set of node page IDs. This oracle is UNBOUNDED in memory and is
    NOT C2-A's page-buffer collector. It prevents false claims of a complete
    bounded-RAM + concurrent-storage GC implementation.
    """
    def __init__(self, journal, reachable_by_epoch, total_nodes):
        _integer(total_nodes, 1)
        if set(reachable_by_epoch) != set(journal.roots):
            raise ValueError("all attested epoch root sets required")
        if any(any(type(v) is not int or v < 0 or v >= total_nodes
                   for v in members) for members in reachable_by_epoch.values()):
            raise ValueError("invalid reachable node ID")
        self.journal = journal
        self.roots = {k:frozenset(v) for k,v in reachable_by_epoch.items()}
        self.total_nodes = total_nodes
        self.page_bytes = journal.page_bytes
        self.pages_per_gen = 1 + (total_nodes+self.page_bytes-1)//self.page_bytes
        self.metadata = tempfile.TemporaryFile(mode="w+b", buffering=0)
        self.anchor = GcFence(0, 0, ZERO)  # another independent trusted pointer
        self.metadata_durable_bytes = 0
        self.resident = bytearray(b"\1"*total_nodes)
        self.c = Counters()

    def _offset(self, gen):
        return (gen-1)*self.pages_per_gen*self.page_bytes

    def _candidate(self, pins):
        required = set(self.roots[self.journal.latest])
        for epoch in pins.values():
            required.update(self.roots[epoch])
        for v in required:
            if not self.resident[v]:
                raise Integrity("required authenticated page was deleted")
        # Every previously dead node stays dead; no resurrection.
        return bytes(int(bool(self.resident[i]) and i in required)
                     for i in range(self.total_nodes))

    def stage(self, fail_at=None):
        if fail_at not in (None, "write", "flush", "publish", "trim"):
            raise ValueError("unknown failure cut before any GC stage write")
        pins = self.journal.replay()
        tip = self.journal.tip
        data = self._candidate(pins)
        gen = self.anchor.generation+1
        digest = _digest(b"UCT005/C2B1/GEN/" + gen.to_bytes(8,"big")
                         + tip.seq.to_bytes(8,"big")+tip.tag+data)
        self.c.sha_calls += 1
        header = GENHEAD.pack(MAGIC,gen,tip.seq,tip.tag,digest)
        at = self._offset(gen)
        self.metadata.seek(at)
        if self.metadata.write(header.ljust(self.page_bytes,b"\0")) != self.page_bytes:
            raise OSError("short GC generation header image")
        self.c.page_writes += 1
        for j in range(0,self.total_nodes,self.page_bytes):
            if self.metadata.write(data[j:j+self.page_bytes].ljust(self.page_bytes,b"\0")) != self.page_bytes:
                raise OSError("short GC generation bitmap image")
            self.c.page_writes += 1
        if fail_at == "write":
            raise Crash("unflushed GC generation")
        os.fsync(self.metadata.fileno())
        self.c.flushes += 1
        self.metadata_durable_bytes = at + self.pages_per_gen*self.page_bytes
        if fail_at == "flush":
            raise Crash("durable but unpublished GC generation")
        return Stage(gen,tip,data,digest)

    def _read_committed(self):
        if self.anchor.generation == 0:
            return bytes([1])*self.total_nodes, None
        self.metadata.seek(self._offset(self.anchor.generation))
        header = self.metadata.read(self.page_bytes)
        self.c.page_reads += 1
        if len(header) != self.page_bytes:
            raise Integrity("published GC header missing")
        magic,gen,seq,tag,digest = GENHEAD.unpack_from(header)
        if (magic != MAGIC or gen != self.anchor.generation
                or seq != self.anchor.pin_seq or digest != self.anchor.digest
                or header[GENHEAD.size:] != bytes(self.page_bytes-GENHEAD.size)):
            raise Integrity("rollback/corruption of published GC header")
        data = bytearray()
        for i in range(self.pages_per_gen-1):
            page = self.metadata.read(self.page_bytes)
            self.c.page_reads += 1
            if len(page) != self.page_bytes:
                raise Integrity("published GC bitmap missing")
            data.extend(page)
        if any(data[self.total_nodes:]) or any(v not in (0,1) for v in data[:self.total_nodes]):
            raise Integrity("noncanonical live bitmap")
        content = bytes(data[:self.total_nodes])
        calc = _digest(b"UCT005/C2B1/GEN/"+gen.to_bytes(8,"big")
                       +seq.to_bytes(8,"big")+tag+content)
        self.c.sha_calls += 1
        if not hmac.compare_digest(calc,digest):
            raise Integrity("GC bitmap digest mismatch")
        earlier, proof = self.journal._prefix(seq)
        if proof != tag:
            raise Integrity("PIN chain mismatches published GC generation")
        return content, earlier

    def publish(self, stage, fail_at=None):
        if fail_at not in (None, "publish_before", "publish", "trim"):
            raise ValueError("unknown failure cut before GC anchor update")
        if (not isinstance(stage,Stage)
                or stage.generation != self.anchor.generation+1
                or stage.pin_fence != self.journal.tip):
            raise Integrity("stale GC stage: PIN/UNPIN raced with publication")
        if self.metadata_durable_bytes < (
                self._offset(stage.generation)+self.pages_per_gen*self.page_bytes):
            raise Integrity("metadata has not been flushed")
        # Verify actual immutable staged bytes BEFORE trusted publication.
        at = self._offset(stage.generation)
        self.metadata.seek(at)
        raw = self.metadata.read(self.pages_per_gen*self.page_bytes)
        self.c.page_reads += self.pages_per_gen
        if len(raw) != self.pages_per_gen*self.page_bytes:
            raise Integrity("truncated staged metadata")
        hd = GENHEAD.pack(MAGIC,stage.generation,stage.pin_fence.seq,
                          stage.pin_fence.tag,stage.digest)
        expected = hd.ljust(self.page_bytes,b"\0")+b"".join(
            stage.bitmask[j:j+self.page_bytes].ljust(self.page_bytes,b"\0")
            for j in range(0,self.total_nodes,self.page_bytes))
        if raw != expected:
            raise Integrity("staged metadata modified")
        if fail_at == "publish_before":
            raise Crash("stage durable but anchor not published")
        pins = self.journal.replay()
        if stage.pin_fence != self.journal.tip:
            raise Integrity("PIN changed during commit")
        for epoch in {self.journal.latest}|set(pins.values()):
            if any(not stage.bitmask[v] for v in self.roots[epoch]):
                raise Integrity("GC would reclaim retained root")
        self.anchor = GcFence(stage.generation,stage.pin_fence.seq,stage.digest)
        self.c.gc_publications += 1
        # Pins created after publish cannot resurrect deleted historical roots.
        self.journal.allowed = {self.journal.latest}|set(pins.values())
        if fail_at == "publish":
            raise Crash("published GC anchor, TRIM not yet run")
        return self.recover(fail_at=fail_at)

    def recover(self, fail_at=None):
        if fail_at not in (None, "trim"):
            raise ValueError("unknown recovery cut before any mutation")
        self.metadata.truncate(self.metadata_durable_bytes)
        self.journal.crash_recover()
        live,pins = self._read_committed()
        if pins is None:
            return 0
        self.journal.allowed = {self.journal.latest}|set(pins.values())
        released = 0
        for i,v in enumerate(live):
            if self.resident[i] and not v:
                self.resident[i]=0
                released+=1
                self.c.trim_commands += 1
                if fail_at == "trim":
                    raise Crash("GC anchor visible, logical trim interrupted")
        return released

    def close(self):
        self.metadata.close()


def diagnostic():
    from uct005_g3b2b_range_tree import TreeWriter
    w=TreeWriter((0,0,0,0))
    w.set(0,1)
    j=PinJournal(w.epochs,b"K"*32)
    gc=GenerationalGC(j,{0:{0,1,2},1:{2,3,4}},6)
    try:
        j.event("PIN",0,w.epochs[0])
        s=gc.stage()
        removed=gc.publish(s)
        return {"removed":removed,"remaining":sum(gc.resident),
                "journal_tip":j.tip.seq,"generation":gc.anchor.generation,
                "pin_io":j.c.as_dict(j.page_bytes),
                "gc_io":gc.c.as_dict(gc.page_bytes),
                "scientific_status":"IDEAL_FSYNC_CAS_MODEL_NO_REAL_CRASH_PROOF"}
    finally:
        gc.close()
        j.close()


if __name__=="__main__":
    import json
    print(json.dumps(diagnostic(),sort_keys=True,indent=2))
