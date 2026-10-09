"""INDEX-001 G2-B4-C2 exact paid adaptive IXR1 segment partitions.

Models in-place same-offset *page images*, not POSIX/NAND/durable writes.
The entire directory is persisted; RAM-mirror costs exact bytes.
"""
from dataclasses import dataclass
from itertools import product
import argparse
import json
import zlib

from index001_variable_checkpoint import (
    encode_snapshot, decode_snapshot, parse_uvarint, uvarint,
)
from index001_page_recourse import page_difference, _prefix_lookup
from index001_priced_wal import assign, pages


def partitions(n):
    if type(n) is not int or n < 1:
        raise ValueError("positive universe")
    return tuple(tuple(i for i in range(1, n) if (mask >> (i-1)) & 1) + (n,)
                 for mask in range(1 << (n-1)))


def pieces(values, ends):
    values = tuple(values)
    n = len(values)
    if not n or not isinstance(ends, tuple) or not ends or ends[-1] != n or any(
        type(p) is not int or not (0 < p <= n) for p in ends
    ) or any(a >= b for a, b in zip(ends, ends[1:])):
        raise ValueError("nonempty ordered partition with final N required")
    starts = (0,) + ends[:-1]
    return tuple(values[lo:hi] for lo, hi in zip(starts, ends))


def framed_length(block):
    """Recover unpadded IXR1 frame length without a hidden length directory."""
    if not block.startswith(b"IXR1"):
        raise ValueError("bad segment magic")
    n, off = parse_uvarint(block, 4)
    k, off = parse_uvarint(block, off)
    if n < 1 or not 1 <= k <= n:
        raise ValueError("invalid segment header")
    for _ in range(k):
        length, off = parse_uvarint(block, off)
        if length < 1 or off >= len(block):
            raise ValueError("invalid segment run")
        off += 1
    if off+4 > len(block):
        raise ValueError("truncated CRC")
    return off+4


def directory_frame(n, lengths, pagecounts):
    if (not lengths or len(lengths)!=len(pagecounts) or
        any(type(x) is not int or x<1 for x in lengths+pagecounts) or
        sum(lengths)!=n):
        raise ValueError("invalid directory lengths/pages")
    body=bytearray(b"IDR1")
    body.extend(uvarint(n))
    body.extend(uvarint(len(lengths)))
    for ln, pc in zip(lengths,pagecounts):
        body.extend(uvarint(ln))
        body.extend(uvarint(pc))
    body.extend((zlib.crc32(body)&0xffffffff).to_bytes(4,"little"))
    return bytes(body)


def read_directory(data, block):
    if type(block) is not int or block<4 or not data.startswith(b"IDR1"):
        raise ValueError("bad directory magic/geometry")
    n, off=parse_uvarint(data,4)
    k, off=parse_uvarint(data,off)
    if n<1 or not 1<=k<=n:
        raise ValueError("bad partition count")
    lengths=[]; counts=[]
    for _ in range(k):
        a,off=parse_uvarint(data,off)
        b,off=parse_uvarint(data,off)
        if a<1 or b<1:
            raise ValueError("empty partition or page count")
        lengths.append(a);counts.append(b)
    end=off+4
    if end>len(data) or zlib.crc32(data[:off])&0xffffffff != int.from_bytes(data[off:end],"little"):
        raise ValueError("directory CRC invalid")
    if sum(lengths)!=n:
        raise ValueError("directory dimensions inconsistent")
    directory_pages=pages(end,block)
    if len(data)<directory_pages*block or any(data[end:directory_pages*block]):
        raise ValueError("noncanonical directory padding")
    return {"n":n,"lengths":tuple(lengths),"pagecounts":tuple(counts),
            "bytes":end,"pages":directory_pages}


def layout(values, ends, block=32):
    if type(block) is not int or block < 4:
        raise ValueError("B>=4")
    chunks=pieces(values,ends)
    frames=tuple(encode_snapshot(part) for part in chunks)
    lengths=tuple(map(len,chunks))
    pc=tuple(pages(len(frame),block) for frame in frames)
    directory=directory_frame(len(values),lengths,pc)
    dirpages=pages(len(directory),block)
    image=bytearray(directory.ljust(dirpages*block,b"\x00"))
    for frame,count in zip(frames,pc):
        image.extend(frame.ljust(count*block,b"\x00"))
    return {"image":bytes(image),"directory":directory,"directory_bytes":len(directory),
            "directory_pages":dirpages,"payload_pages":sum(pc),
            "segment_pages":pc,"ends":ends,"state":tuple(values),
            "disk_bytes":len(image),"ram_mirror_bits":8*len(directory)}


def decode_image(image, block=32):
    directory=read_directory(image,block)
    n=directory["n"]
    pos=directory["pages"]*block
    ends=[];output=[];running=0
    for ln,pc in zip(directory["lengths"],directory["pagecounts"]):
        region=image[pos:pos+pc*block]
        if len(region)!=pc*block:
            raise ValueError("truncated segment pages")
        actual=framed_length(region)
        if pages(actual,block)!=pc or any(region[actual:]):
            raise ValueError("wrong page count or padding")
        chunk=decode_snapshot(region[:actual])
        if len(chunk)!=ln:
            raise ValueError("directory segment mismatch")
        output.extend(chunk);running+=ln;ends.append(running)
        pos+=pc*block
    if pos!=len(image) or len(output)!=n:
        raise ValueError("noncanonical trailing pages")
    return tuple(output),tuple(ends)


def lookup_cost(view, pos, mode="disk"):
    """Parse the *persisted bytes*, not the dense oracle state.

    Mirrored mode models a full exact directory cached in RAM after preload,
    but no pre-decoded RAM index is assumed. The segment prefix is unverified.
    """
    if mode not in ("disk","mirrored") or type(pos) is not int:
        raise ValueError("invalid query")
    pages_total=view["directory_pages"]+view["payload_pages"]
    B=view["disk_bytes"]//pages_total
    # Warm mirror is a paid RAM copy; do NOT simulate a free directory disk
    # read. A cold lookup instead validates the persisted IDR1 pages.
    directory_raw = (view["directory"].ljust(view["directory_pages"]*B,b"\x00")
                     if mode=="mirrored" else view["image"])
    directory=read_directory(directory_raw,B)
    if not 0<=pos<directory["n"]:
        raise ValueError("point out of bounds")
    cellstart=0
    offset=directory["pages"]*B
    for ln,pc in zip(directory["lengths"],directory["pagecounts"]):
        if pos<cellstart+ln:
            raw=view["image"][offset:offset+pc*B]
            value,consumed=_prefix_lookup(raw,pos-cellstart)
            prefixpages=pages(consumed,B)
            return {"value":value,
                    "warm_pages":prefixpages if mode=="mirrored" else
                        directory["pages"]+prefixpages,
                    "cold_pages":directory["pages"]+prefixpages,
                    "crc_verified_pages":directory["pages"]+pc}
        offset+=pc*B
        cellstart+=ln
    raise AssertionError("directory missed valid point")


def max_query(view, mode):
    return max(lookup_cost(view,i,mode)["warm_pages"]
               for i in range(len(view["state"])))


@dataclass(frozen=True)
class Limits:
    alpha_n: int=4
    alpha_d: int=1
    beta: int=2
    query_cap: int=4
    ram_cap_bits: int=0
    mode: str="disk"
    max_gc_pages: int | None=None

    def __post_init__(self):
        if (any(type(x) is not int for x in (
            self.alpha_n,self.alpha_d,self.beta,self.query_cap,self.ram_cap_bits))
            or self.alpha_n<0 or self.alpha_d<=0 or self.beta<0 or
            self.query_cap<1 or self.ram_cap_bits<0 or
            self.mode not in ("disk","mirrored") or
            (self.max_gc_pages is not None and
             (type(self.max_gc_pages) is not int or self.max_gc_pages<0))):
            raise ValueError("invalid limits")

    def cap(self,state,block):
        return self.alpha_n*len(encode_snapshot(state))//self.alpha_d+self.beta*block


def admissible(view,block,limits):
    if view["disk_bytes"]>limits.cap(view["state"],block):
        return False
    if limits.mode=="mirrored" and view["ram_mirror_bits"]>limits.ram_cap_bits:
        return False
    return max_query(view,limits.mode)<=limits.query_cap


def transition(old,new,block,limits):
    if len(old["state"])!=len(new["state"]):
        raise ValueError("universe changes")
    image_delta=page_difference(old["image"],new["image"],block)
    gc=image_delta["pages_removed"]
    d0=old["disk_bytes"];d1=new["disk_bytes"]
    peak=max(d0,d1)
    fits= (admissible(new,block,limits) and
          peak<=max(limits.cap(old["state"],block),
                    limits.cap(new["state"],block)) and
          (limits.max_gc_pages is None or gc<=limits.max_gc_pages))
    return {"feasible":fits,"written_model_bytes":image_delta["modeled_page_image_bytes"],
            "retired_pages":gc,"allocated_pages":image_delta["pages_added"],
            "changed_page_indices":image_delta["changed_page_indices"],
            "before_disk_bytes":d0,"after_disk_bytes":d1,"peak_bytes":peak,
            "old_segments":len(old["ends"]),"new_segments":len(new["ends"]),
            "new_ram_mirror_bits":new["ram_mirror_bits"],
            "new_query_pages":max_query(new,limits.mode),
            "cold_query_pages":max_query(new,"disk")}


def optimize_trace(initial,updates,block,initial_ends,limits):
    """Finite exhaustive-candidate DP. Starting partition is fixed and charged."""
    prev=layout(initial,initial_ends,block)
    if not admissible(prev,block,limits):
        raise ValueError("initial layout not admitted")
    dp={initial_ends:(0,())}
    before=tuple(initial)
    candidates=partitions(len(before))
    step_counts=[]
    for operation in updates:
        after=assign(before,operation)
        choices={cuts:layout(after,cuts,block) for cuts in candidates}
        oldviews={cuts:layout(before,cuts,block) for cuts in dp}
        nxt={}
        for oldcuts,(cost,path) in dp.items():
            old=oldviews[oldcuts]
            for cuts,new in choices.items():
                row=transition(old,new,block,limits)
                if not row["feasible"]:
                    continue
                # The fixed optimization scalar *explicitly* charges modeled
                # changed page images plus one B per page retired.
                candidate=(cost+row["written_model_bytes"]+
                           row["retired_pages"]*block, path+(cuts,))
                if cuts not in nxt or candidate<nxt[cuts]:
                    nxt[cuts]=candidate
        dp=nxt
        step_counts.append(len(dp))
        before=after
    optimum=min(dp.values(),default=None)
    return {"feasible":optimum is not None,
            "min_modeled_write_plus_gc_bytes":None if optimum is None else optimum[0],
            "optimal_partitions":None if optimum is None else
                [list(x) for x in optimum[1]],
            "reachable_partition_counts":step_counts}


def reset_certificate(n=64,block=32,group=8,limits=Limits()):
    if type(n) is not int or n<2 or n%group:
        raise ValueError("N must be divisible by g")
    old=tuple(i%2 for i in range(n))
    oldcuts=tuple(range(group,n+1,group))
    after=(0,)*n
    oldv=layout(old,oldcuts,block)
    newv=layout(after,(n,),block)
    if not admissible(oldv,block,limits) or not admissible(newv,block,limits):
        raise ValueError("witness old/new layouts not admitted")
    change=transition(oldv,newv,block,limits)
    if not change["feasible"]:
        raise ValueError("reset peak or GC bound rejects witness")
    u=limits.cap(after,block)//block
    lower_removed=max(0,len(oldcuts)-u+1)
    lower_retired=max(0,oldv["disk_bytes"]//block-u)
    if len(oldcuts)-1<lower_removed or change["retired_pages"]<lower_retired:
        raise AssertionError("conditional lower-bound falsified")
    return {"N":n,"B":block,"g":group,"alpha_n":limits.alpha_n,
            "alpha_d":limits.alpha_d,"beta":limits.beta,
            "old_segments":len(oldcuts),"old_disk_bytes":oldv["disk_bytes"],
            "old_directory_bytes":oldv["directory_bytes"],
            "new_segments":1,"new_disk_bytes":newv["disk_bytes"],
            "new_directory_bytes":newv["directory_bytes"],
            "zero_snapshot_bytes":len(encode_snapshot(after)),
            "zero_budget_bytes":limits.cap(after,block),
            "minimum_segment_eliminations":lower_removed,
            "minimum_retired_page_positions":lower_retired,
            "actual_retired_page_positions":change["retired_pages"],
            "actual_changed_page_images":len(change["changed_page_indices"]),
            "disk_only_worst_lookup_before":max_query(oldv,"disk"),
            "mirrored_warm_worst_lookup_before":max_query(oldv,"mirrored"),
            "mirror_ram_bits_before":oldv["ram_mirror_bits"]}


def report():
    z=reset_certificate()
    return {"schema":"mathlab.index001.g2b4c2.adaptive-page.v1",
            "classification":"RESTRICTED_CONDITIONAL_PAGE_RECLAMATION_NOT_GENERAL_BOUND",
            "no_ssd_nand_or_os_measurement":True,
            "working_memory_unbounded":True,
            "zero_reset":z,
            "adaptive_policy_example":optimize_trace(
                (0,1,0,1,0),[(0,5,0),(2,3,1),(0,1,1)],
                32,(1,2,3,4,5),Limits(alpha_n=8,beta=4,query_cap=3))}
if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--json",action="store_true")
    args=parser.parse_args()
    result=report()
    if args.json:
        print(json.dumps(result,sort_keys=True,indent=2))
    else:
        z=result["zero_reset"]
        print("N={N} B={B} old_D={old_disk_bytes} new_D={new_disk_bytes} "
              "cap_zero={zero_budget_bytes} removed_pages={actual_retired_page_positions} "
              "lower_removed={minimum_retired_page_positions} "
              "directory_bits={mirror_ram_bits_before}".format(**z))
        print("INDEX001_G2B4C2_ADAPTIVE_PAGE_RECLAMATION_PASS")
