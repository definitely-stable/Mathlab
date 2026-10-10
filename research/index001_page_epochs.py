"""INDEX-001 G2-B4-C5A: explicit page-slot allocator and pinned epoch oracle.

Frozen failure model: pages are atomically written, data pages flush before
the atomic root page overwrite, single writer, volatile pins die on restart.
Real tempfile page reads/writes are counted; no fsync/NAND/durable guarantee.
Each data slot has a CRC32-validated 14-byte envelope (10-byte header and 4-
byte trailer), with opaque HYB4 bytes inside. Page 0 is a CRC root directory.
No RAM bound is claimed for the Python interpreter, oracle, or pin table.
"""
import argparse
import io
import json
import struct
import tempfile
import zlib
from dataclasses import dataclass

ROOT=b"R5IX"
DATA=b"D5IX"
FREE=b"F5IX"
END=0xffffffff
ROOT_HEAD="<4sIIIII"
PAGE_HEAD="<4sIH"


@dataclass(frozen=True)
class Epoch:
    epoch: int
    head: int
    count: int
    size: int
    checksum: int


class Arena:
    def __init__(self,B=64,backing=None,max_pages=None):
        if type(B) is not int or B<64 or B>1<<20:
            raise ValueError("B must be between 64 and 1MiB")
        self.B=B
        self.f=backing or tempfile.TemporaryFile(mode="w+b")
        self.max_pages=max_pages
        self.io={"reads":0,"writes":0,"payload_reads":0,"gc_page_writes":0}
        self.pins={}
        if self.npages()==0:
            self._put(0,self._root_page(Epoch(0,END,0,0,0)))
        else:
            self.root()

    @property
    def payload_capacity(self):
        return self.B-14

    def npages(self):
        self.f.seek(0,2)
        size=self.f.tell()
        if size%self.B:
            raise ValueError("partial physical page")
        return size//self.B

    def _get(self,p):
        if p<0 or p>=self.npages():
            raise ValueError("page out of bounds")
        self.f.seek(p*self.B)
        raw=self.f.read(self.B)
        if len(raw)!=self.B:
            raise ValueError("short physical read")
        self.io["reads"]+=1
        return raw

    def _put(self,p,raw,kind=None):
        if len(raw)!=self.B or p<0 or p>self.npages():
            raise ValueError("non-page-aligned write/physical gap")
        if self.max_pages is not None and p==self.npages() and p>=self.max_pages:
            raise MemoryError("physical disk page budget exceeded")
        self.f.seek(p*self.B)
        self.f.write(raw)
        self.f.flush()
        self.io["writes"]+=1
        if kind=="gc":
            self.io["gc_page_writes"]+=1

    def _root_page(self,e):
        raw=struct.pack(ROOT_HEAD,ROOT,e.epoch,e.head,e.count,e.size,e.checksum)
        raw+=struct.pack("<I",zlib.crc32(raw))
        return raw.ljust(self.B,b"\0")

    def root(self):
        raw=self._get(0)
        magic,epoch,head,count,size,checksum=struct.unpack(ROOT_HEAD,raw[:24])
        if magic!=ROOT or struct.unpack("<I",raw[24:28])[0]!=zlib.crc32(raw[:24]) or any(raw[28:]):
            raise ValueError("bad root CRC/padding")
        if (count==0)!=(head==END) or (count==0)!=(size==0):
            raise ValueError("root dimensions")
        if count and (head<1 or head>=self.npages()):
            raise ValueError("bad root pointer")
        return Epoch(epoch,head,count,size,checksum)

    def _frame(self,magic,following,part=b""):
        if magic not in (DATA,FREE) or len(part)>self.payload_capacity or following<0 or following>END:
            raise ValueError("invalid frame")
        if magic==FREE and (part or following!=END):
            raise ValueError("free page must be self contained")
        raw=struct.pack(PAGE_HEAD,magic,following,len(part))
        raw=(raw+part).ljust(self.B-4,b"\0")
        return raw+struct.pack("<I",zlib.crc32(raw))

    def _decode(self,raw):
        if len(raw)!=self.B or zlib.crc32(raw[:-4])!=struct.unpack("<I",raw[-4:])[0]:
            raise ValueError("data/free page CRC")
        magic,nxt,used=struct.unpack(PAGE_HEAD,raw[:10])
        if magic not in (DATA,FREE) or used>self.payload_capacity or any(raw[10+used:-4]):
            raise ValueError("bad page kind/extent/padding")
        if magic==FREE and (used or nxt!=END):
            raise ValueError("bad free page")
        return magic,nxt,raw[10:10+used]

    def verify(self,e=None,sink=None):
        """Stream page chain and CRC with one B-byte scratch page."""
        if e is None:e=self.root()
        if e.count==0:
            if e.size or e.checksum or e.head!=END:
                raise ValueError("invalid initial epoch")
            return 0
        cursor=e.head
        crc=0
        size=0
        for i in range(e.count):
            if cursor<1 or cursor>=self.npages():
                raise ValueError("chain out of range")
            magic,nextpage,payload=self._decode(self._get(cursor))
            if magic!=DATA or not payload:
                raise ValueError("bad data page")
            if i+1<e.count and nextpage==END:
                raise ValueError("premature end")
            if i+1==e.count and nextpage!=END:
                raise ValueError("unterminated chain")
            crc=zlib.crc32(payload,crc)
            size+=len(payload)
            if sink is not None:
                sink.write(payload)
            cursor=nextpage
        if size!=e.size or crc!=e.checksum:
            raise ValueError("chain size/payload CRC")
        return size

    def blob(self,e=None):
        sink=io.BytesIO()  # test helper; NOT a bounded-RAM query
        self.verify(e,sink)
        return sink.getvalue()

    def pin(self):
        e=self.root()
        self.verify(e)
        self.pins[e]=self.pins.get(e,0)+1
        return e

    def unpin(self,e):
        count=self.pins.get(e,0)
        if count<1:
            raise ValueError("unowned epoch pin")
        if count==1:del self.pins[e]
        else:self.pins[e]=count-1

    def _contains(self,e,slot):
        """O(B) scratch, scans rather than making a free reachability set."""
        cursor=e.head
        for _ in range(e.count):
            if cursor==slot:
                return True
            if cursor<1 or cursor>=self.npages():
                raise ValueError("invalid protected chain")
            magic,nextpage,_=self._decode(self._get(cursor))
            if magic!=DATA:
                raise ValueError("protected data overwritten")
            cursor=nextpage
        if cursor!=END:
            raise ValueError("protected cycle/corruption")
        return False

    def _protected(self,slot):
        roots=(self.root(),*self.pins.keys())
        return any(self._contains(e,slot) for e in roots if e.count)

    def sweep(self):
        """Reclaim only pages absent from active root and every volatile pin."""
        current=self.root()
        self.verify(current)
        for p in self.pins:
            self.verify(p)
        freed=0
        for slot in range(1,self.npages()):
            raw=self._get(slot)
            magic=raw[:4]
            if magic==FREE:
                self._decode(raw)
            elif magic==DATA:
                self._decode(raw)
                if not self._protected(slot):
                    self._put(slot,self._frame(FREE,END),kind="gc")
                    freed+=1
            else:
                raise ValueError("unknown page kind")
        return freed

    def _allocate(self):
        """Paid full scan: no invisible allocator directory/free list."""
        for slot in range(1,self.npages()):
            magic,nxt,_=self._decode(self._get(slot))
            if magic==FREE:
                return slot
        return self.npages()

    def publish(self,source,hook=None):
        """Source file bytes become new immutable chain, then root publication.

        Not transactional on Python/OS media: ordered flushed writes and an
        atomic root page are assumptions of the *finite crash model*.
        """
        before=self.root()
        self.verify(before)
        source.seek(0,2)
        length=source.tell()
        if not 0<length<1<<32:
            raise ValueError("opaque frame length outside range")
        # Fail closed on a malformed HYB4 payload BEFORE touching allocator
        # pages. The source preflight uses C4's page-streaming CRC validator
        # and semantic parser; its page reads are billed separately.
        from index001_hybrid_streaming import check as check_hyb4,scan as scan_hyb4
        source.seek(0)
        info=check_hyb4(source,self.B)
        if info["D"]!=length:
            raise ValueError("source frame allocation mismatch")
        semantic_io={"pages":0}
        for _ in scan_hyb4(source,self.B,info,semantic_io):
            pass
        self.io["source_preflight_pages"]=self.io.get("source_preflight_pages",0)+info["check_read_pages"]+semantic_io["pages"]
        source.seek(0)
        cursor=None
        first=END
        count=0
        crc=0
        while True:
            part=source.read(self.payload_capacity)
            if not part:break
            self.io["payload_reads"]+=1
            slot=self._allocate()
            if first==END:first=slot
            self._put(slot,self._frame(DATA,END,part))
            if hook:hook("stage",self)
            if cursor is not None:
                old=self._decode(self._get(cursor))
                if old[0]!=DATA or old[1]!=END:
                    raise ValueError("staging link collision")
                self._put(cursor,self._frame(DATA,slot,old[2]))
                if hook:hook("link",self)
            cursor=slot
            crc=zlib.crc32(part,crc)
            count+=1
        if count!=(length+self.payload_capacity-1)//self.payload_capacity:
            raise AssertionError("page count")
        after=Epoch(before.epoch+1,first,count,length,crc)
        self.verify(after)  # full staged validation before atomic root overwrite
        if hook:hook("ready",self)
        self._put(0,self._root_page(after))
        if hook:hook("publish",self)
        return after

    def snapshot(self):
        """Oracle-only full arena image, not part of the bounded page model."""
        self.f.seek(0)
        return self.f.read()

    @classmethod
    def recover(cls,image,B=64):
        file=tempfile.TemporaryFile(mode="w+b")
        file.write(image)
        file.flush()
        arena=cls(B,file)
        arena.verify()
        return arena

    def summary(self):
        root=self.root()
        live=sum(1 for i in range(1,self.npages()) if self._contains(root,i))
        pinned=sum(1 for i in range(1,self.npages()) if any(
            self._contains(p,i) for p in self.pins))
        free=0
        for i in range(1,self.npages()):
            if self._decode(self._get(i))[0]==FREE:
                free+=1
        dead=self.npages()-1-len({i for i in range(1,self.npages())
            if self._contains(root,i) or any(self._contains(p,i) for p in self.pins)})-free
        return {"epoch":root.epoch,"total_pages":self.npages(),
                "current_pages":live,"pinned_pages":pinned,
                "free_pages":free,"unreclaimed_dead_pages":dead,
                "retained_root_bytes":self.B,
                "volatile_pins":sum(self.pins.values()),
                "reads":self.io["reads"],"writes":self.io["writes"],
                "gc_writes":self.io["gc_page_writes"],
                "source_preflight_pages":self.io.get("source_preflight_pages",0)}


def report():
    from index001_hybrid_streaming import from_bits,update,check,read_all
    B=64
    a=Arena(B)
    initial=from_bits(tuple(i%2 for i in range(1024)),B,"B")
    first=a.publish(initial)
    pin=a.pin()
    zeros,out=update(initial,B,(0,1024,0),"U0")
    second=a.publish(zeros)
    if a.blob(pin)!=_readfile(initial) or a.blob()!=_readfile(zeros):
        raise AssertionError("pinned generation mismatch")
    blocked=a.sweep()
    if blocked:
        raise AssertionError("pinned pages prematurely freed")
    with_pin=a.summary()
    a.unpin(pin)
    freed=a.sweep()
    without_pin=a.summary()
    if freed!=first.count or without_pin["free_pages"]!=first.count:
        raise AssertionError("unpin reclaim")
    back=from_bits(tuple(i%2 for i in range(1024)),B,"B")
    third=a.publish(back)
    reused=a.summary()
    if reused["total_pages"] != without_pin["total_pages"]:
        raise AssertionError("free slots not reused")
    initial.close();zeros.close();back.close()
    return {"schema":"mathlab.index001.g2b4c5a.page-epoch.v1",
            "classification":"RESTRICTED_ATOMIC_ROOT_MODEL_PINNED_GENERATION_ORACLE",
            "root_page_atomic_assumption":True,
            "os_fsync_or_torn_page_proved":False,
            "whole_program_ram_bounded":False,
            "fixed_update_working_page_buffers_claimed":False,
            "page_size":B,"first_pages":first.count,
            "second_pages":second.count,"third_pages":third.count,
            "freed_after_unpin":freed,"pinned":with_pin,
            "after_unpin":without_pin,"after_reuse":reused}


def _readfile(f):
    f.seek(0)
    return f.read()


if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--json",action="store_true")
    args=p.parse_args()
    r=report()
    if args.json:print(json.dumps(r,sort_keys=True,indent=2))
    else:
        print("first=%d second=%d freed=%d total_after_reuse=%d" %
            (r["first_pages"],r["second_pages"],r["freed_after_unpin"],r["after_reuse"]["total_pages"]))
        print("INDEX001_G2B4C5A_ATOMIC_ROOT_PIN_ORACLE_PASS")
