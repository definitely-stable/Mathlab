#!/usr/bin/env python3
"""UCT-005 C2-B2-B: file-page online COW SET, ideal durable-root admission.

The online author stores NODEs/roots/metadata as full-page file images;
only O(log n) Python call stack plus O(P) page buffers per operation.
Trusted monotone 40-byte root CAS and complete-image fsync barriers are
ASSUMPTIONS. Python TempFiles are not real cold-restart durable storage.
C2-B2-A GC is intentionally fenced out after an online epoch advance.
"""
from dataclasses import dataclass
from hashlib import sha256
import os
import struct
import tempfile

from uct005_g3b2b_range_tree import (
    AnchorValue, TreeWriter, _check_bit, _commit, _hash, _leaf,
)
from uct005_g3b2c2a_disk_gc import DiskGcArena, NODE, ROOT, PIN, NULL
from uct005_g3b2c2b1_pin_generation import Crash, Integrity, PinJournal

META_MAGIC = b"UCTB2B!!"
META = struct.Struct(">8sQQ32sQ32s")
META_DOMAIN = b"UCT005/C2B2B/META/"
CUTS = (None, "node_write", "node_flush", "bitmap_write",
        "bitmap_flush", "root_write", "root_flush", "meta_write",
        "meta_flush")


@dataclass(frozen=True)
class CowStage:
    epoch: int
    root_page: int
    digest: bytes
    previous_node_pages: int
    node_pages: int


class OnlineCowAuthor:
    """Honest single writer; permanently pinned roots paid by B1 journal.

    Must serialize SET with PIN/UNPIN/GC trusted publications. A previous
    DiskFencedGC instance becomes stale at every successful SET: see explicit
    frozen-forest rejection in C2-B2-A. Not a durable multi-process protocol.
    """
    def __init__(self, bits, page_bytes=4096, clients=2, key=b"uct005-c2b2b-author-owner-key-32bytes"):
        bits = tuple(bits)
        setup = TreeWriter(bits)  # setup-only unbounded initial memory
        self.n = len(bits)
        self.arena = DiskGcArena.from_writer(setup, page_bytes=page_bytes,
                                             clients=clients)
        self.journal = PinJournal(setup.epochs, key, clients=clients,
                                  page_bytes=page_bytes)
        self.page_bytes = page_bytes
        self.metadata = tempfile.TemporaryFile(mode="w+b", buffering=0)
        self.trusted = setup.anchor   # separately trusted monotone 40-byte CAS
        self.committed_nodes = self.arena.count
        self.stage = None
        self._needs_recover = False
        self.arena._uct005_writer_inflight = False
        self.io = dict.fromkeys((
            "node_reads", "node_writes", "root_reads", "root_writes",
            "meta_reads", "meta_writes", "bitmap_reads", "bitmap_writes",
            "pin_root_reads", "pin_slot_writes",
            "node_fsyncs", "root_fsyncs", "meta_fsyncs", "bitmap_fsyncs",
            "node_truncates", "root_truncates", "meta_truncates",
            "bitmap_truncates", "sha256_calls", "anchor_publications"), 0)
        root, digest = ROOT.unpack_from(self.arena._page(self.arena.roots, 0))
        if digest != self.trusted.digest:
            raise Integrity("setup authenticated root mismatch")
        self._write_meta(0, root, digest, self.committed_nodes)
        os.fsync(self.metadata.fileno())
        self.io["meta_fsyncs"] += 1
        self._setup_page_writes = self.arena.setup_page_writes + 1
        self._setup_sha = setup.setup_hash_calls

    @property
    def epoch(self):
        return self.trusted.epoch

    def _read(self, stream, page, key):
        if type(page) is not int or page < 0:
            raise Integrity("invalid physical page address")
        stream.seek(page * self.page_bytes)
        raw = stream.read(self.page_bytes)
        self.io[key] += 1
        if len(raw) != self.page_bytes:
            raise Integrity("missing committed or staged file page")
        return raw

    def _write(self, stream, page, raw, key):
        if len(raw) != self.page_bytes:
            raise ValueError("not a full-page canonical image")
        stream.seek(page * self.page_bytes)
        if stream.write(raw) != self.page_bytes:
            raise OSError("short full page write")
        self.io[key] += 1

    def _meta(self, epoch):
        page = self._read(self.metadata, epoch, "meta_reads")
        magic, recorded, root, digest, size, checksum = META.unpack_from(page)
        expected = sha256(META_DOMAIN + page[:META.size - 32]).digest()
        self.io["sha256_calls"] += 1
        if (magic != META_MAGIC or recorded != epoch
                or checksum != expected
                or page[META.size:] != bytes(self.page_bytes-META.size)):
            raise Integrity("untrusted/torn metadata page")
        return root, digest, size

    def _write_meta(self, epoch, root, digest, count):
        prefix = struct.pack(">8sQQ32sQ", META_MAGIC, epoch, root, digest, count)
        checksum = sha256(META_DOMAIN + prefix).digest()
        self.io["sha256_calls"] += 1
        self._write(self.metadata, epoch,
                    (prefix+checksum).ljust(self.page_bytes,b"\0"), "meta_writes")

    def _old_node(self, page, expected, length):
        if page >= self.committed_nodes:
            raise Integrity("attempted to read uncommitted or freed node")
        data = self._read(self.arena.nodes, page, "node_reads")
        left,right,span,bit,payload,digest = NODE.unpack_from(data)
        if (data[NODE.size:] != bytes(self.page_bytes-NODE.size)
                or bit not in (0,1) or span != length
                or digest != expected or
                _commit(span,bit,payload) != digest):
            raise Integrity("authenticated node image mismatch")
        self.io["sha256_calls"] += 1
        if left == NULL:
            if right != NULL or span != 1:
                raise Integrity("malformed leaf")
            leaf = _leaf(bit)
            self.io["sha256_calls"] += 2
            if leaf.payload != payload or leaf.digest != digest:
                raise Integrity("forged leaf")
        else:
            if right == NULL or span == 1 or left >= self.committed_nodes or right >= self.committed_nodes:
                raise Integrity("malformed child pointers")
        return left,right,span,bit,payload,digest

    def _append_node(self, left, right, span, parity, payload, digest):
        image = NODE.pack(left,right,span,parity,payload,digest)
        # Physical page IDs are allocated monotonically from file EOF.
        self.arena.nodes.seek(0,2)
        length = self.arena.nodes.tell()
        if length % self.page_bytes:
            raise Integrity("torn uncommitted append; recovery required")
        index = length // self.page_bytes
        self._write(self.arena.nodes, index, image.ljust(self.page_bytes,b"\0"),
                    "node_writes")
        return index

    def _replace(self, page, expected, lo, hi, position, bit):
        left,right,span,parity,payload,digest = self._old_node(
            page, expected, hi-lo+1)
        if lo == hi:
            new = _leaf(bit)
            self.io["sha256_calls"] += 2
            index = self._append_node(NULL,NULL,1,bit,new.payload,new.digest)
            return index, 1, bit, new.digest
        mid = (lo+hi)//2
        lraw = self._old_node(left, self._peek_digest(left), mid-lo+1)
        rraw = self._old_node(right, self._peek_digest(right), hi-mid)
        ld,rd=lraw[-1],rraw[-1]
        expected_payload = _hash(b"UCT005-G3B2B/PAIR\0"+ld+rd)
        self.io["sha256_calls"] += 1
        if parity != (lraw[3]^rraw[3]) or payload != expected_payload:
            raise Integrity("parent-child commitment mismatch")
        if position <= mid:
            nl,_,lp,ld = self._replace(left,ld,lo,mid,position,bit)
            nr,rp = right,rraw[3]
        else:
            nr,_,rp,rd = self._replace(right,rd,mid+1,hi,position,bit)
            nl,lp = left,lraw[3]
        new_parity = lp ^ rp
        new_payload = _hash(b"UCT005-G3B2B/PAIR\0"+ld+rd)
        new_digest = _commit(span,new_parity,new_payload)
        self.io["sha256_calls"] += 2
        index = self._append_node(nl,nr,span,new_parity,new_payload,new_digest)
        return index,span,new_parity,new_digest

    def _peek_digest(self, page):
        if page >= self.committed_nodes:
            raise Integrity("uncommitted child pointer")
        raw = self._read(self.arena.nodes,page,"node_reads")
        return NODE.unpack_from(raw)[-1]

    def _set_new_bits(self, start, end):
        # Node IDs start at first old EOF, are contiguous and all initialized.
        # Rewrites only affected full bitmap pages, preserving older GC liveness.
        for block in range(start//self.page_bytes,
                           (end-1)//self.page_bytes + 1):
            page_start = block*self.page_bytes
            self.arena.alive.seek(page_start)
            raw = self.arena.alive.read(self.page_bytes)
            self.io["bitmap_reads"] += 1
            if len(raw) == 0:
                raw = bytes(self.page_bytes)
            if len(raw) != self.page_bytes:
                raise Integrity("torn bitmap file image")
            bitmap = bytearray(raw)
            for k in range(max(start,page_start),min(end,page_start+self.page_bytes)):
                bitmap[k-page_start]=1
            self._write(self.arena.alive,block,bytes(bitmap),"bitmap_writes")

    def prepare(self, index, bit, fail_at=None):
        if fail_at not in CUTS:
            raise ValueError("unsupported failure cut before any side effects")
        if (type(index) is not int or index < 0 or index >= self.n):
            raise ValueError("invalid SET index")
        _check_bit(bit)
        if self._needs_recover or self.stage is not None:
            raise Integrity("unacknowledged stage: recover or publish first")
        if self.epoch >= 2**64-1:
            raise ValueError("epoch overflow")
        self._needs_recover = True
        # This is a process-local modeled serialized-actor lease. A real
        # reboot/independent-process fence is explicitly NOT established.
        self.arena._uct005_writer_inflight = True
        root, digest = ROOT.unpack_from(self._read(
            self.arena.roots,self.epoch,"root_reads"))
        if digest != self.trusted.digest:
            raise Integrity("committed root index disagrees with trusted anchor")
        self._old_node(root, digest,self.n)
        root_new,_,_,new_digest = self._replace(root,digest,0,self.n-1,index,bit)
        if fail_at=="node_write":
            raise Crash("COW pages written without node fsync")
        os.fsync(self.arena.nodes.fileno())
        self.io["node_fsyncs"] += 1
        if fail_at=="node_flush":
            raise Crash("COW node images flushed, no live bitmap/root")
        self.arena.nodes.seek(0,2)
        new_count=self.arena.nodes.tell()//self.page_bytes
        if new_count <= self.committed_nodes:
            raise Integrity("no immutable pages allocated by SET")
        self._set_new_bits(self.committed_nodes,new_count)
        if fail_at=="bitmap_write":
            raise Crash("bitmap written but not flushed")
        os.fsync(self.arena.alive.fileno())
        self.io["bitmap_fsyncs"] += 1
        if fail_at=="bitmap_flush":
            raise Crash("future node liveness flushed, no root publication")
        next_epoch=self.epoch+1
        self._write(self.arena.roots,next_epoch,
                    ROOT.pack(root_new,new_digest).ljust(self.page_bytes,b"\0"),
                    "root_writes")
        if fail_at=="root_write":
            raise Crash("future root written, not flushed")
        os.fsync(self.arena.roots.fileno())
        self.io["root_fsyncs"] += 1
        if fail_at=="root_flush":
            raise Crash("root index flushed but not trusted")
        self._write_meta(next_epoch,root_new,new_digest,new_count)
        if fail_at=="meta_write":
            raise Crash("future root metadata written, not flushed")
        os.fsync(self.metadata.fileno())
        self.io["meta_fsyncs"] += 1
        if fail_at=="meta_flush":
            raise Crash("metadata flushed but trusted root CAS pending")
        result=CowStage(next_epoch,root_new,new_digest,
                        self.committed_nodes,new_count)
        self.stage=result
        return result

    def publish(self, stage, fail_at=None):
        if fail_at not in (None,"publish_before","publish","ack"):
            raise ValueError("invalid publication crash cut")
        if not isinstance(stage,CowStage) or stage!=self.stage:
            raise Integrity("stale or unflushed COW transaction")
        if stage.epoch!=self.epoch+1 or stage.previous_node_pages!=self.committed_nodes:
            raise Integrity("stale root CAS predecessor")
        root,digest,count=self._meta(stage.epoch)
        actual_root,actual_digest=ROOT.unpack_from(
            self._read(self.arena.roots,stage.epoch,"root_reads"))
        if (root!=stage.root_page or actual_root!=root or digest!=stage.digest
                or actual_digest!=digest or count!=stage.node_pages):
            raise Integrity("forged untrusted root index or highwater")
        # Validate a new root under the expected canonical length before CAS.
        # Full-tree verification happens in the query oracle.
        if stage.root_page >= stage.node_pages:
            raise Integrity("root beyond committed file extent")
        raw=self._read(self.arena.nodes,stage.root_page,"node_reads")
        a,b,span,parity,payload,ndigest=NODE.unpack_from(raw)
        self.io["sha256_calls"] += 1
        if span!=self.n or ndigest!=stage.digest or _commit(span,parity,payload)!=ndigest:
            raise Integrity("COW root commitment invalid")
        if fail_at=="publish_before":
            raise Crash("all image barriers complete, trusted CAS not yet published")
        # Ideal *durable atomic* root CAS and serialized journal-catalog update.
        self.trusted=AnchorValue(stage.epoch,stage.digest)
        # Same ideal atomic trust transition: the GC may not keep using
        # its frozen forest after a committed but unacknowledged SET.
        self.arena.latest_trusted_checkpoint=self.trusted
        self.io["anchor_publications"]+=1
        self.stage=None
        if fail_at=="publish":
            raise Crash("trusted root committed, author acknowledgment lost")
        self.recover()
        return self.trusted

    def recover(self):
        """Ideal crash replay against an external trusted (epoch,digest) anchor.

        Models truncation of uncommitted tail and repair of bitmap padding.
        NOT a real process restart: owner key, trusted CAS and tempfiles live.
        """
        trusted_epoch=self.trusted.epoch
        root,digest,count=self._meta(trusted_epoch)
        if digest!=self.trusted.digest or root>=count or count<2*self.n-1:
            raise Integrity("trusted root metadata missing or corrupt")
        raw=self._read(self.arena.nodes,root,"node_reads")
        if NODE.unpack_from(raw)[-1]!=digest:
            raise Integrity("root node does not match trusted digest")
        self.arena.nodes.truncate(count*self.page_bytes)
        self.io["node_truncates"]+=1
        self.arena.roots.truncate((trusted_epoch+1)*self.page_bytes)
        self.io["root_truncates"]+=1
        self.metadata.truncate((trusted_epoch+1)*self.page_bytes)
        self.io["meta_truncates"]+=1
        blocks=(count+self.page_bytes-1)//self.page_bytes
        if count%self.page_bytes:
            page=self._read(self.arena.alive,blocks-1,"bitmap_reads")
            data=page[:count%self.page_bytes]+bytes(
                self.page_bytes-count%self.page_bytes)
            self._write(self.arena.alive,blocks-1,data,"bitmap_writes")
        self.arena.alive.truncate(blocks*self.page_bytes)
        self.io["bitmap_truncates"]+=1
        self.committed_nodes=count
        self.arena.count=count
        self.arena.epochs=trusted_epoch+1
        self.arena.latest_trusted_checkpoint=self.trusted
        self.arena._has_reclaimed = (self.arena._has_reclaimed or False)
        # Trusted root bulletin and historical trusted catalog are one
        # ideal serialized control actor here, not a deployed transaction.
        for epoch in range(len(self.journal.roots),trusted_epoch+1):
            r,d,c=self._meta(epoch)
            self.journal.roots[epoch]=d
        self.journal.latest=trusted_epoch
        self.journal.allowed.add(trusted_epoch)
        self.journal.crash_recover()
        self.stage=None
        self._needs_recover=False
        self.arena._uct005_writer_inflight = False
        return self.trusted

    def _sync_pin_slots(self):
        pins=self.journal.replay()
        for client in range(self.journal.clients):
            e=pins.get(client)
            if e is None:
                image=bytes(self.page_bytes)
            else:
                page=self._read(self.arena.roots,e,"pin_root_reads")
                root,digest=ROOT.unpack_from(page)
                if digest!=self.journal.roots[e]:
                    raise Integrity("journal PIN conflicts with attested root")
                image=PIN.pack(e,root,digest).ljust(self.page_bytes,b"\0")
            self._write(self.arena.pins,client,image,"pin_slot_writes")

    def query(self, epoch,left,right,checkpoint):
        if self._needs_recover or self.stage is not None:
            raise Integrity("no query during an incompletely published SET")
        if type(epoch) is not int or epoch not in self.journal.roots:
            raise ValueError("uncommitted historical epoch")
        if (checkpoint.epoch!=epoch or
                checkpoint.digest!=self.journal.roots[epoch]):
            raise Integrity("trusted historical root mismatch")
        self._sync_pin_slots()
        return self.arena.verify_range(epoch,left,right,checkpoint)

    def counters(self):
        reads=sum(self.io[k] for k in ("node_reads","root_reads","meta_reads",
                  "bitmap_reads","pin_root_reads"))
        writes=sum(self.io[k] for k in ("node_writes","root_writes","meta_writes",
                  "bitmap_writes","pin_slot_writes"))
        return {**self.io,"read_bytes":reads*self.page_bytes,
                "write_bytes":writes*self.page_bytes,
                "page_reads":reads,"page_writes":writes,
                "trusted_root_bytes":40*self.io["anchor_publications"],
                "setup_page_writes":self._setup_page_writes,
                "setup_sha256":self._setup_sha,
                "pin_cost":self.journal.c.as_dict(self.page_bytes),
                "mode":"IDEAL_ATOMIC_ROOT_CAS_TEMPFILE_NOT_PHYSICAL_CRASH_DURABLE"}

    def close(self):
        self.metadata.close()
        self.journal.close()
        self.arena.close()


def diagnostic():
    import json
    author=OnlineCowAuthor((0,0,1,0),page_bytes=256)
    try:
        before=author.trusted
        stage=author.prepare(1,1)
        after=author.publish(stage)
        assert author.query(1,0,3,after)==0
        assert before.epoch==0 and after.epoch==1
        return {"epoch":after.epoch,"digest":after.digest.hex(),
                "node_pages":author.committed_nodes,"charges":author.counters()}
    finally:
        author.close()


if __name__=="__main__":
    import json
    print(json.dumps(diagnostic(),sort_keys=True,indent=2))
