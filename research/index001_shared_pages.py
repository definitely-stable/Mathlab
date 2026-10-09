"""INDEX-001 G2-B4-C3: shared-page exact CRC-RLE fragments + packed-bitset control.

Finite *logical page-image* model; disk bytes referenced by Python oracle are
a stand-in for storage, not proof that Python itself has bounded process RAM.
Cold point-read parser explicitly uses one B-byte page scratch buffer plus a
fixed-width counter budget. Update/optimal-policy builders are NOT bounded RAM.
"""
from dataclasses import dataclass
from itertools import product
import argparse
import json
import zlib

from index001_variable_checkpoint import encode_snapshot, decode_snapshot, uvarint
from index001_adaptive_partition import partitions, pieces
from index001_page_recourse import page_difference
from index001_priced_wal import pages, assign

MAGIC=b"IPD1"
COUNTER_BYTES=96  # declared allowance for up to 12 64-bit cursor/CRC counters
MAX_VAR_BYTES=9    # only <2^63 canonical uvarints


def directory_frame(n, logical_lengths, physical_lengths):
    if (type(n) is not int or n<1 or not logical_lengths or
        len(logical_lengths)!=len(physical_lengths) or
        any(type(x) is not int or x<1 for x in logical_lengths+physical_lengths) or
        sum(logical_lengths)!=n):
        raise ValueError("invalid directory dimensions")
    data=bytearray(MAGIC)
    data+=uvarint(n)+uvarint(len(logical_lengths))
    for logical,physical in zip(logical_lengths,physical_lengths):
        data+=uvarint(logical)+uvarint(physical)
    data+=zlib.crc32(data).to_bytes(4,"little")
    return bytes(data)


def shared_layout(values,ends,B):
    if type(B) is not int or B<4:
        raise ValueError("B>=4 required")
    blocks=pieces(values,ends)
    frames=tuple(encode_snapshot(p) for p in blocks)
    directory=directory_frame(len(values),tuple(map(len,blocks)),tuple(map(len,frames)))
    payload=b"".join(frames)
    image=directory.ljust(pages(len(directory),B)*B,b"\0")+payload.ljust(pages(len(payload),B)*B,b"\0")
    return {"kind":"shared","N":len(values),"B":B,"state":tuple(values),
            "ends":ends,"directory":directory,"directory_bytes":len(directory),
            "directory_pages":pages(len(directory),B),"payload_bytes":len(payload),
            "payload_pages":pages(len(payload),B),"image":image,
            "D":len(image),"warm_cache_bits":8*len(directory),
            "segment_lengths":tuple(map(len,frames))}


def bitset_layout(values,B):
    if type(B) is not int or B<4 or not values or any(x not in (0,1) for x in values):
        raise ValueError("bad geometry or values")
    n=len(values)
    data=bytearray((n+7)//8)
    for i,x in enumerate(values):
        if x:
            data[i//8] |= 1 << (i%8)
    return {"kind":"bitmap","N":n,"B":B,"state":tuple(values),
            "image":bytes(data).ljust(pages(len(data),B)*B,b"\0"),
            "payload_bytes":len(data),"D":pages(len(data),B)*B,
            "directory_bytes":0,"directory_pages":0,"warm_cache_bits":0,
            "ends":(n,)}


def decode_shared(image,B):
    """Independently whole-image CRC decode; *not* streaming RAM bound."""
    from index001_variable_checkpoint import parse_uvarint
    if not image.startswith(MAGIC):
        raise ValueError("invalid magic")
    n,pos=parse_uvarint(image,4)
    k,pos=parse_uvarint(image,pos)
    if n<1 or k<1 or k>n:
        raise ValueError("invalid header")
    lengths=[];byte_counts=[]
    for _ in range(k):
        x,pos=parse_uvarint(image,pos)
        y,pos=parse_uvarint(image,pos)
        if x<1 or y<1:
            raise ValueError("zero segment")
        lengths.append(x);byte_counts.append(y)
    if pos+4>len(image) or zlib.crc32(image[:pos]) != int.from_bytes(image[pos:pos+4],"little"):
        raise ValueError("directory CRC")
    end=pos+4
    dpages=pages(end,B)
    if sum(lengths)!=n or any(image[end:dpages*B]):
        raise ValueError("noncanonical directory")
    offset=dpages*B
    answer=[];ends=[];reached=0
    for length,byte_count in zip(lengths,byte_counts):
        frame=image[offset:offset+byte_count]
        if len(frame)!=byte_count:
            raise ValueError("truncated frame")
        seg=decode_snapshot(frame)
        if len(seg)!=length:
            raise ValueError("wrong logical size")
        answer+=seg
        reached+=length
        ends.append(reached)
        offset+=byte_count
    if (offset>len(image) or any(image[offset:]) or
            len(image)!=(dpages+pages(sum(byte_counts),B))*B):
        raise ValueError("payload padding/length mismatch")
    return tuple(answer),tuple(ends)


class PageReader:
    """One-page buffer, no saved prior-page cache. Tracks *unique* read pages."""
    def __init__(self,data,B,backing="disk"):
        self.data=data  # backing store, NOT charged resident emulator memory
        self.B=B
        self.backing=backing
        self.index=-1
        self.scratch=b""
        self.pages=set()

    def byte(self,off):
        if off<0 or off>=len(self.data):
            raise ValueError("read past frame")
        p=off//self.B
        if self.index!=p:
            self.scratch=self.data[p*self.B:(p+1)*self.B]
            self.index=p
            if self.backing=="disk":
                self.pages.add(p)
        return self.scratch[off-p*self.B]


class Cursor:
    def __init__(self,reader,at=0):
        self.reader=reader
        self.at=at
        self.crc=0

    def take(self,crc=False):
        b=self.reader.byte(self.at)
        self.at+=1
        if crc:
            self.crc=zlib.crc32(bytes((b,)),self.crc)
        return b

    def var(self,crc=False):
        shift=0
        number=0
        for used in range(1,MAX_VAR_BYTES+1):
            byte=self.take(crc)
            number |= (byte&127)<<shift
            if not byte&128:
                if len(uvarint(number))!=used:
                    raise ValueError("noncanonical varint")
                return number
            shift+=7
        raise ValueError("too-long varint")


def lookup_shared(view,point,mode="disk",Rmax=None):
    """Reads IPD1 + exact segment-prefix bytes through a page cursor.

    RAM limit models a B-byte page buffer, fixed 96-byte registers, plus the
    exact paid mirrored directory bytes in warm mode. No unpriced directory
    list, decoded state, or persistent page cache is consulted.
    """
    if (view["kind"]!="shared" or mode not in ("disk","mirror") or
            type(point) is not int or not 0<=point<view["N"]):
        raise ValueError("invalid point/mode")
    B=view["B"]
    resident=B+COUNTER_BYTES+(len(view["directory"]) if mode=="mirror" else 0)
    if Rmax is not None and resident>Rmax:
        raise MemoryError("declared query scratch+mirror bytes exceed Rmax")
    # Warm directory is read from an exact paid RAM copy; not the disk.
    directory_store=(view["directory"] if mode=="mirror" else view["image"])
    directory_reader=PageReader(directory_store,B,"ram" if mode=="mirror" else "disk")
    d=Cursor(directory_reader)
    if bytes(d.take(True) for _ in range(4))!=MAGIC:
        raise ValueError("magic")
    n=d.var(True);k=d.var(True)
    if n!=view["N"] or not 1<=k<=n:
        raise ValueError("directory identity")
    logical=0;byte_prefix=0
    chosen=None
    for _ in range(k):
        ln=d.var(True);size=d.var(True)
        if ln<1 or size<1:
            raise ValueError("invalid entry")
        if logical<=point<logical+ln:
            chosen=(point-logical,ln,byte_prefix,size)
        logical+=ln;byte_prefix+=size
    check=int.from_bytes(bytes(d.take() for _ in range(4)),"little")
    if d.crc!=check or logical!=n:
        raise ValueError("directory checksum")
    dlen=d.at
    dir_pages=pages(dlen,B)
    if dir_pages!=view["directory_pages"] or chosen is None:
        raise ValueError("bad directory length or missing group")
    if mode=="disk" and any(view["image"][dlen:dir_pages*B]):
        raise ValueError("directory padding")
    local,segment_n,prefix,segment_size=chosen
    start=dir_pages*B+prefix
    segment=Cursor(PageReader(view["image"],B),start)
    if bytes(segment.take() for _ in range(4))!=b"IXR1":
        raise ValueError("segment magic")
    n_segment=segment.var();runs=segment.var()
    if segment_n!=n_segment or not 1<=runs<=n_segment:
        raise ValueError("segment n/count")
    reached=0;previous=None;value=None
    for _ in range(runs):
        ln=segment.var();v=segment.take()
        if ln<1 or v not in (0,1) or v==previous or reached+ln>segment_n:
            raise ValueError("invalid run")
        if local<reached+ln:
            value=v
            break
        reached+=ln;previous=v
    if value is None or segment.at-start>segment_size:
        raise ValueError("segment prefix invalid")
    read_pages=len(directory_reader.pages | segment.reader.pages)
    # They address disjoint byte regions and thus count additively.
    return {"value":value,"Q":read_pages,"Q_directory":len(directory_reader.pages),
            "Q_payload":len(segment.reader.pages),"working_RAM_bytes":resident,
            "mirrored_directory_bits":8*view["directory_bytes"] if mode=="mirror" else 0,
            "prefix_crc_verified":False}


def lookup_bitmap(view,point,Rmax=None):
    if view["kind"]!="bitmap" or type(point) is not int or not 0<=point<view["N"]:
        raise ValueError("out of range")
    resident=view["B"]+COUNTER_BYTES
    if Rmax is not None and resident>Rmax:
        raise MemoryError("bounded scratch")
    reader=PageReader(view["image"],view["B"])
    bit=(reader.byte(point//8)>>(point%8))&1
    return {"value":bit,"Q":len(reader.pages),"working_RAM_bytes":resident}


def page_transition(old,new):
    if old["N"]!=new["N"] or old["B"]!=new["B"]:
        raise ValueError("geometry")
    delta=page_difference(old["image"],new["image"],old["B"])
    return {"changed_pages":delta["changed_page_positions"],
            "removed_pages":delta["pages_removed"],
            "allocated_pages":delta["pages_added"],
            "written_image_bytes":delta["modeled_page_image_bytes"],
            "Dold":old["D"],"Dnew":new["D"]}


def zero_reset(n=64,B=32,g=4):
    if type(n) is not int or type(g) is not int or n<1 or g<1 or n%g:
        raise ValueError("requires integral split")
    bits=tuple(i&1 for i in range(n));zeros=(0,)*n
    cuts=tuple(range(g,n+1,g))
    old=shared_layout(bits,cuts,B)
    after=shared_layout(zeros,(n,),B)
    bitmap_old=bitset_layout(bits,B)
    bitmap_new=bitset_layout(zeros,B)
    rec=page_transition(old,after)
    return {"N":n,"B":B,"g":g,"K":len(cuts),
            "shared_before_bytes":old["D"],"shared_after_bytes":after["D"],
            "shared_directory_bytes":old["directory_bytes"],
            "shared_removed_pages":rec["removed_pages"],
            "shared_changed_pages":rec["changed_pages"],
            "shared_max_Q_disk":max(lookup_shared(old,i,"disk")["Q"] for i in range(n)),
            "shared_max_Q_mirror":max(lookup_shared(old,i,"mirror")["Q"] for i in range(n)),
            "working_ram_disk_bytes":B+COUNTER_BYTES,
            "working_ram_mirror_bytes":B+COUNTER_BYTES+old["directory_bytes"],
            "bitmap_before_bytes":bitmap_old["D"],
            "bitmap_after_bytes":bitmap_new["D"],
            "bitmap_removed_pages":page_transition(bitmap_old,bitmap_new)["removed_pages"],
            "bitmap_changed_pages":page_transition(bitmap_old,bitmap_new)["changed_pages"],
            "global_zero_ixr1_bytes":len(encode_snapshot(zeros))}


def report():
    return {"schema":"mathlab.index001.g2b4c3.shared-pages.v1",
            "classification":"C2_PER_SEGMENT_PAGE_BOUND_FALSIFIED_IN_SHARED_LAYOUT",
            "claim_scope":"static snapshot exact finite model with eager in-place image replacement",
            "whole_process_bounded_ram":False,
            "cold_point_read_one_page_scratch":True,
            "nand_io_and_crash_safety_measured":False,
            "zero_reset_g4":zero_reset(64,32,4),
            "zero_reset_g8":zero_reset(64,32,8)}
if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--json",action="store_true")
    args=parser.parse_args()
    result=report()
    if args.json:
        print(json.dumps(result,indent=2,sort_keys=True))
    else:
        for key in ("zero_reset_g4","zero_reset_g8"):
            w=result[key]
            print(f"{key} K={w['K']} D_shared={w['shared_before_bytes']} "
                  f"D_bitset={w['bitmap_before_bytes']} "
                  f"shared_removed={w['shared_removed_pages']} "
                  f"bitset_removed={w['bitmap_removed_pages']} "
                  f"cold_Q={w['shared_max_Q_disk']} warm_Q={w['shared_max_Q_mirror']}")
        print("INDEX001_G2B4C3_SHARED_PAGE_COUNTERMODEL_PASS")
