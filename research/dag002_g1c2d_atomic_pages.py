#!/usr/bin/env python3
"""DAG-002 G1-C2-D: deterministic append-DAG crash-prefix page oracle.

Single atomic page writes, ordered persistence, single writer, no GC,
readers/pins, Byzantine freshness or real device guarantees.
"""
from dataclasses import dataclass
import struct
import zlib

MAGIC=b'DGR1'
DIR=b'DIR1'
EMPTY=0xffffffff

def page_count(length,page_bytes):
    if type(length) is not int or length<0 or type(page_bytes) is not int or page_bytes<32:
        raise ValueError("invalid pages")
    return (length+page_bytes-1)//page_bytes

@dataclass(frozen=True)
class Root:
    generation:int
    directory:int
    directory_pages:int
    next_free:int
    vertices:int

@dataclass(frozen=True)
class Plan:
    previous:Root
    new:Root
    writes:tuple
    parent_input_bits:int
    preparation_reads:int
    workspace_bytes:int

class AtomicAppendPages:
    def __init__(self,page_bytes=32,capacity=128,ram_limit=1<<20):
        if type(page_bytes) is not int or not 32<=page_bytes<=4096:
            raise ValueError("page bytes outside range")
        if type(capacity) is not int or not 2<=capacity<EMPTY:
            raise ValueError("invalid capacity")
        if type(ram_limit) is not int or ram_limit<0:
            raise ValueError("invalid RAM")
        self.P,self.capacity,self.ram_limit=page_bytes,capacity,ram_limit
        self.read_pages=self.data_write_pages=self.root_write_pages=0
        self.max_workspace_bytes=self.total_parent_input_bits=0
        self.initialization_pages=2
        self.disk={0:self._root_bytes(Root(0,EMPTY,0,2,0)),1:bytes(self.P)}

    def _root_bytes(self,r):
        header=struct.pack('<4sIIIII',MAGIC,r.generation,r.directory,
                           r.directory_pages,r.next_free,r.vertices)
        return (header+struct.pack('<I',zlib.crc32(header))).ljust(self.P,b'\0')

    def _decode_root(self,image):
        if len(image)!=self.P or image[:4]!=MAGIC:
            return None
        raw=image[:24]
        if zlib.crc32(raw)!=struct.unpack('<I',image[24:28])[0]:
            return None
        _,gen,start,count,nxt,n=struct.unpack('<4sIIIII',raw)
        if not (2<=nxt<=self.capacity and n<=1000000 and (
              (n==0 and start==EMPTY and count==0) or
              (n>0 and start>=2 and count>=1 and start+count<=nxt))):
            return None
        return Root(gen,start,count,nxt,n)

    def _read(self,address):
        if address not in self.disk or not 0<=address<self.capacity:
            raise ValueError("missing committed page")
        page=self.disk[address]
        if len(page)!=self.P:
            raise ValueError("invalid image")
        self.read_pages+=1
        return page

    def recover(self):
        roots=[]
        for slot in (0,1):
            r=self._decode_root(self._read(slot))
            if r is not None:
                roots.append((r.generation,slot,r))
        if not roots:
            raise ValueError("unrecoverable roots")
        return max(roots)[2]

    def _directory(self,r):
        if not r.vertices:
            return ()
        raw=b''.join(self._read(r.directory+i) for i in range(r.directory_pages))
        if raw[:4]!=DIR or struct.unpack('<I',raw[4:8])[0]!=r.vertices:
            raise ValueError("directory/header disagreement")
        if page_count(8+8*r.vertices,self.P)!=r.directory_pages:
            raise ValueError("noncanonical directory length")
        result=tuple(struct.unpack('<II',raw[8+8*i:16+8*i])
                     for i in range(r.vertices))
        for i,(addr,pages) in enumerate(result):
            if pages!=page_count((i+7)//8,self.P):
                raise ValueError("invalid extent count")
            if pages and (addr<2 or addr+pages>r.next_free):
                raise ValueError("invalid extent address")
        return result

    def _read_label(self,index,records):
        addr,n=records[index]
        return b''.join(self._read(addr+i) for i in range(n))

    def prepare_append(self,parents=()):
        initial_reads=self.read_pages
        r=self.recover()
        v=r.vertices
        if v>=255:
            raise ValueError("finite reference bound")
        selected=tuple(parents)
        if any(type(x) is not int or x<0 or x>=v for x in selected) or len(set(selected))!=len(selected):
            raise ValueError("invalid parent tuple")
        old=self._directory(r)
        mask=0
        for p in selected:
            mask|=1<<p
            mask|=int.from_bytes(self._read_label(p,old),'little')
        label_bytes=(v+7)//8
        label_pages=page_count(label_bytes,self.P)
        dir_pages=page_count(8+8*(v+1),self.P)
        if r.next_free+label_pages+dir_pages>self.capacity:
            raise MemoryError("no free append-only pages; no GC")
        workspace=r.directory_pages*self.P+sum(old[p][1]*self.P for p in selected)+(label_pages+dir_pages+2)*self.P
        if workspace>self.ram_limit:
            raise MemoryError("logical working-set cap")
        self.max_workspace_bytes=max(self.max_workspace_bytes,workspace)
        label_addr=r.next_free
        dir_addr=label_addr+label_pages
        records=old+((label_addr if label_pages else EMPTY,label_pages),)
        labels=mask.to_bytes(label_bytes,'little')
        directory=DIR+struct.pack('<I',v+1)+b''.join(
            struct.pack('<II',a,n) for a,n in records)
        writes=[]
        for addr,raw,n in ((label_addr,labels,label_pages),(dir_addr,directory,dir_pages)):
            for i in range(n):
                writes.append((addr+i,raw[i*self.P:(i+1)*self.P].ljust(self.P,b'\0')))
        updated=Root(r.generation+1,dir_addr,dir_pages,dir_addr+dir_pages,v+1)
        writes.append(((r.generation+1)&1,self._root_bytes(updated)))
        return Plan(r,updated,tuple(writes),v,self.read_pages-initial_reads,workspace)

    def apply_prefix(self,plan,completed_writes):
        """Atomic page writes; no externally observable partial page images."""
        if type(completed_writes) is not int or not 0<=completed_writes<=len(plan.writes):
            raise ValueError("invalid crash cut")
        for addr,image in plan.writes[:completed_writes]:
            if not 0<=addr<self.capacity or len(image)!=self.P:
                raise ValueError("invalid planned write")
            self.disk[addr]=image
            if addr<2:
                self.root_write_pages+=1
            else:
                self.data_write_pages+=1

    def append(self,parents=()):
        plan=self.prepare_append(parents)
        self.apply_prefix(plan,len(plan.writes))
        self.total_parent_input_bits+=plan.parent_input_bits
        assert self.recover()==plan.new
        return plan.new.vertices-1

    def query(self,ancestor,target):
        r=self.recover()
        if any(type(x) is not int or not 0<=x<r.vertices for x in (ancestor,target)):
            raise ValueError("query vertex outside committed prefix")
        if ancestor==target:
            return True
        if ancestor>target:
            return False
        addr,_=self._directory(r)[target]
        raw=self._read(addr+ancestor//(8*self.P))
        return bool(raw[(ancestor//8)%self.P]&(1<<(ancestor%8)))

    def clone(self):
        other=AtomicAppendPages(self.P,self.capacity,self.ram_limit)
        other.disk=dict(self.disk)
        other.total_parent_input_bits=self.total_parent_input_bits
        return other

    def ledger(self):
        r=self.recover()
        return dict(generation=r.generation,next_free=r.next_free,
            charged_page_reads=self.read_pages,data_page_writes=self.data_write_pages,
            root_page_writes=self.root_write_pages,
            initialization_pages=self.initialization_pages,
            uncommitted_tail_pages=sum(addr>=r.next_free for addr in self.disk),
            max_workspace_bytes=self.max_workspace_bytes,
            read_bytes=self.read_pages*self.P,
            write_bytes=(self.data_write_pages+self.root_write_pages)*self.P,
            parent_input_bits=self.total_parent_input_bits,
            page_request_address_bytes=4*(self.read_pages+self.data_write_pages+self.root_write_pages))

def report():
    s=AtomicAppendPages()
    for parents in ((),(0,),(0,),(1,2)):
        plan=s.prepare_append(parents)
        for cut in range(len(plan.writes)+1):
            x=s.clone()
            x.apply_prefix(plan,cut)
            assert x.recover()==(plan.new if cut==len(plan.writes) else plan.previous)
        s.append(parents)
    assert s.query(0,3)
    assert s.ledger()['root_page_writes']==4
    print("DAG_G1C2D_ALL_ATOMIC_PAGE_CRASH_CUTS_PASS")
    print("DAG_G1C2D_PAID_HIGH_WATERMARK_ALLOCATOR_PASS")
    print("NOVELTY_UNPROVED_RESTRICTED_COW_PUBLICATION")

if __name__=="__main__":
    report()
