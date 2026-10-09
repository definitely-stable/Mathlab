"""INDEX-001 G2-B4-C4: paid hybrid formats and two-pass disk-file updater.

Research-only, no crash/durability/physical NAND result. Real temporary files
are used for old/new images, and explicit page transfer counts are recorded.
The *algorithmic* source-reader/output-writer use one B-byte buffer each,
plus 128 bytes of fixed-register allowance. Python heap/RSS, runtime and
tempfile metadata are NOT proven bounded; use only as a page-I/O oracle.
"""
from dataclasses import dataclass
from itertools import product
import argparse
import json
import tempfile
import zlib

from index001_variable_checkpoint import encode_snapshot, uvarint
from index001_priced_wal import pages, assign
from index001_page_recourse import page_difference

MAGIC=b"HYB4"
MODES=("U0","U1","S0","S1","R","B")
MODENUM={m:i for i,m in enumerate(MODES)}
REGISTER_BYTES=128
MAX_VAR=9
LIMIT=1 << 63


def positive_n(n):
    if type(n) is not int or not 1 <= n < LIMIT:
        raise ValueError("universe outside 1..2^63-1")
    return n


def header(n,mode,payload_len):
    positive_n(n)
    if mode not in MODENUM or type(payload_len) is not int or not 0 <= payload_len < LIMIT:
        raise ValueError("bad header")
    return MAGIC+uvarint(n)+bytes((MODENUM[mode],))+uvarint(payload_len)


class Reader:
    """File-backed, one B-byte resident block, counted B-byte read requests."""
    def __init__(self,fd,B):
        self.fd=fd;self.B=B
        self.page=-1;self.buffer=b"";self.reads=0

    def get(self,offset):
        if offset<0:
            raise ValueError("negative read")
        page=offset//self.B
        if page!=self.page:
            self.fd.seek(page*self.B)
            self.buffer=self.fd.read(self.B)
            self.page=page;self.reads+=1
        p=offset%self.B
        if p>=len(self.buffer):
            raise ValueError("truncated read")
        return self.buffer[p]


class Cursor:
    def __init__(self,reader,offset=0):
        self.r=reader;self.pos=offset

    def byte(self):
        x=self.r.get(self.pos);self.pos+=1
        return x

    def var(self):
        value=0
        for shift in range(0,MAX_VAR*7,7):
            b=self.byte()
            value|=(b&127)<<shift
            if not (b&128):
                if value>=LIMIT or len(uvarint(value)) != (shift//7+1):
                    raise ValueError("noncanonical/oversized varint")
                return value
        raise ValueError("unterminated varint")


class Writer:
    """B-byte staging buffer; no source payload held in RAM."""
    def __init__(self,fd,B):
        self.fd=fd;self.B=B;self.buf=bytearray();self.writes=0
        self.payload_crc=0;self.bytes=0

    def put(self,b,crc=True):
        if not 0<=b<=255:
            raise ValueError("bad byte")
        self.buf.append(b);self.bytes+=1
        if crc:
            self.payload_crc=zlib.crc32(bytes((b,)),self.payload_crc)
        if len(self.buf)==self.B:
            self.fd.write(self.buf);self.writes+=1;self.buf.clear()

    def data(self,data,crc=True):
        for b in data:
            self.put(b,crc)

    def pad(self):
        while self.buf:
            self.put(0,False)

    def finish(self):
        if self.buf:
            self.fd.write(self.buf);self.writes+=1;self.buf.clear()
        self.fd.flush()


def check(fd,B):
    """CRC covers canonical header + payload; padding must be zero."""
    r=Reader(fd,B);c=Cursor(r)
    if bytes(c.byte() for _ in range(4))!=MAGIC:
        raise ValueError("bad HYB4 magic")
    n=positive_n(c.var())
    mode_index=c.byte()
    if mode_index>=len(MODES):
        raise ValueError("unknown encoding")
    mode=MODES[mode_index]
    length=c.var();start=c.pos
    total=start+length+4
    if total>=LIMIT:
        raise ValueError("overlong frame")
    fd.seek(0,2);file_size=fd.tell()
    if file_size!=pages(total,B)*B:
        raise ValueError("noncanonical allocation/trailing garbage")
    crc=0
    for i in range(start+length):
        crc=zlib.crc32(bytes((r.get(i),)),crc)
    expected=sum(r.get(start+length+j)<<(8*j) for j in range(4))
    if crc!=expected:
        raise ValueError("payload/header CRC mismatch")
    for i in range(total,file_size):
        if r.get(i)!=0:
            raise ValueError("nonzero alignment padding")
    if mode.startswith("U") and length!=0:
        raise ValueError("bad uniform payload")
    if mode=="B" and length!=(n+7)//8:
        raise ValueError("bad bitmap payload size")
    return {"n":n,"mode":mode,"payload_len":length,"payload_at":start,
            "D":file_size,"crc_ok":True,"check_read_pages":r.reads}


def scan(fd,B,info,telemetry=None):
    """Read exactly N cells in O(B+fixed registers), canonical validation."""
    n=info["n"];mode=info["mode"];start=info["payload_at"]
    end=start+info["payload_len"]
    r=Reader(fd,B);c=Cursor(r,start)
    if mode in ("U0","U1"):
        for _ in range(n):
            yield MODENUM[mode]
    elif mode=="B":
        octet=0
        for i in range(n):
            if i%8==0:
                octet=c.byte()
            yield (octet>>(i%8))&1
        if n%8 and octet>>(n%8):
            raise ValueError("bitmap high bits not zero")
    elif mode in ("S0","S1"):
        default=0 if mode=="S0" else 1
        count=c.var()
        if count>n:
            raise ValueError("too many sparse positions")
        next_pos=c.var() if count else n
        prev=-1
        for i in range(n):
            if i==next_pos:
                if i<=prev:
                    raise ValueError("unsorted positions")
                yield 1-default
                prev=i;count-=1
                next_pos=c.var() if count else n
                if count and not prev<next_pos<n:
                    raise ValueError("duplicate/invalid sparse position")
            else:
                if next_pos<i:
                    raise ValueError("unsorted sparse position")
                yield default
        if count:
            raise ValueError("incomplete sparse sequence")
    elif mode=="R":
        runs=c.var()
        if not 1<=runs<=n:
            raise ValueError("bad run count")
        prior=None;total=0
        for _ in range(runs):
            run=c.var();v=c.byte()
            if run<1 or v not in (0,1) or v==prior or total+run>n:
                raise ValueError("invalid maximal run")
            for _ in range(run):
                yield v
            total+=run;prior=v
        if total!=n:
            raise ValueError("run coverage error")
    if c.pos!=end:
        raise ValueError("noncanonical payload/undecoded bytes")
    if telemetry is not None:
        telemetry["pages"]+=r.reads


def modified(fd,B,info,operation,telemetry=None):
    lo,hi,val=operation
    if not (type(lo) is int and type(hi) is int and
            type(val) is int and 0<=lo<hi<=info["n"] and val in (0,1)):
        raise ValueError("bad update")
    for i,old in enumerate(scan(fd,B,info,telemetry)):
        yield val if lo<=i<hi else old


def characteristics(fd,B,info,op):
    n=info["n"]
    ones=0;zeros=0;length0=0;length1=0
    nruns=0;runbytes=0;last=None;runlen=0
    telemetry={"pages":0}
    for i,x in enumerate(modified(fd,B,info,op,telemetry)):
        if x:
            ones+=1;length1+=len(uvarint(i))
        else:
            zeros+=1;length0+=len(uvarint(i))
        if last is None:
            last=x;nruns=1;runlen=1
        elif x!=last:
            runbytes+=len(uvarint(runlen))+1
            nruns+=1;runlen=1;last=x
        else:
            runlen+=1
    runbytes+=len(uvarint(runlen))+1
    lengths={"B":(n+7)//8,
             "R":len(uvarint(nruns))+runbytes,
             "S0":len(uvarint(ones))+length1,
             "S1":len(uvarint(zeros))+length0}
    if zeros==n:lengths["U0"]=0
    if ones==n:lengths["U1"]=0
    return {"n":n,"ones":ones,"zeros":zeros,"runs":nruns,
            "payload":lengths,"analysis_read_pages":telemetry["pages"]}


def candidates(stats,B):
    n=stats["n"]
    return {m:{"payload":size,
               "raw_bytes":len(header(n,m,size))+size+4,
               "D":pages(len(header(n,m,size))+size+4,B)*B}
            for m,size in stats["payload"].items()}


def chosen_modes(stats,B):
    v=candidates(stats,B)
    return sorted(v,key=lambda m:(v[m]["D"],v[m]["raw_bytes"],MODENUM[m]))


def payload_bytes(fd,B,info,op,mode,stats,telemetry=None):
    n=stats["n"]
    if mode.startswith("U"):
        return
    if mode=="B":
        pending=0
        for i,v in enumerate(modified(fd,B,info,op,telemetry)):
            pending|=v<<(i%8)
            if i%8==7:
                yield pending;pending=0
        if n%8:
            yield pending
    elif mode in ("S0","S1"):
        polarity=0 if mode=="S0" else 1
        count=stats["ones"] if polarity==0 else stats["zeros"]
        yield from uvarint(count)
        for i,v in enumerate(modified(fd,B,info,op)):
            if v!=polarity:
                yield from uvarint(i)
    elif mode=="R":
        yield from uvarint(stats["runs"])
        last=None;runlen=0
        for v in modified(fd,B,info,op,telemetry):
            if last is None:
                last=v;runlen=1
            elif v==last:
                runlen+=1
            else:
                yield from uvarint(runlen)
                yield last
                last=v;runlen=1
        yield from uvarint(runlen)
        yield last
    else:
        raise ValueError("unknown output mode")


def update(fd,B,operation,mode="min",Rcap=None):
    """Two scans + CRC preflight. Source and result are *file descriptors*.

    Counts physical B-byte read()/write() requests made by the source reader
    and output writer, excluding the independent validation/oracle readback.
    The caller owns and closes the returned TemporaryFile.
    """
    if type(B) is not int or B<4 or B>1<<20:
        raise ValueError("invalid B")
    R=2*B+REGISTER_BYTES
    if Rcap is not None and R>Rcap:
        raise MemoryError("insufficient modeled two-buffer update RAM")
    info=check(fd,B)
    stats=characteristics(fd,B,info,operation)
    opts=candidates(stats,B)
    if mode=="min":
        mode=chosen_modes(stats,B)[0]
    if mode not in opts:
        raise ValueError("inadmissible output mode")
    size=opts[mode]["payload"]
    output=tempfile.TemporaryFile(mode="w+b")
    writer=Writer(output,B)
    writer.data(header(info["n"],mode,size))
    produced=0
    payload_io={"pages":0}
    for byte in payload_bytes(fd,B,info,operation,mode,stats,payload_io):
        writer.put(byte);produced+=1
    if produced!=size:
        output.close()
        raise AssertionError("two-pass encoded byte length mismatch")
    crc=writer.payload_crc
    writer.data(crc.to_bytes(4,"little"),False)
    raw=writer.bytes
    writer.pad()
    writer.finish()
    if output.tell()!=opts[mode]["D"]:
        output.close()
        raise AssertionError("aligned total differs from prior count")
    output.seek(0)
    return output,{"mode":mode,"n":info["n"],"old_D":info["D"],
                   "D":opts[mode]["D"],"raw_bytes":raw,
                   "preflight_read_pages":info["check_read_pages"],
                   "analysis_read_pages":stats["analysis_read_pages"],
                   "emit_source_read_pages":payload_io["pages"],
                   "total_source_read_pages":info["check_read_pages"]+stats["analysis_read_pages"]+payload_io["pages"],
                   "writer_pages":writer.writes,
                   "model_RAM_bytes":R,"source_passes":2 if mode.startswith("U") else 3,
                   "all_mode_bytes":{k:v["D"] for k,v in opts.items()}}


def from_bits(bits,B,mode="min"):
    """Test fixture encoder only; dense input sits in host memory."""
    bits=tuple(bits)
    if not bits or any(type(x) is not int or x not in (0,1) for x in bits):
        raise ValueError("binary input required")
    # Uniform source is a constant logical stream; fixture emits bits through
    # a canonical RLE source using existing baseline snapshot run iterator.
    # Build an exact HYB4 bitmap directly (fixture construction not bounded).
    octets=bytearray((len(bits)+7)//8)
    for i,v in enumerate(bits):
        octets[i//8]|=v<<(i%8)
    frm=header(len(bits),"B",len(octets))+octets
    frm+=zlib.crc32(frm).to_bytes(4,"little")
    fd=tempfile.TemporaryFile(mode="w+b")
    fd.write(frm.ljust(pages(len(frm),B)*B,b"\0"));fd.flush();fd.seek(0)
    if mode=="B":
        return fd
    op=(0,1,bits[0])
    result,_=update(fd,B,op,mode)
    fd.close()
    return result


def read_all(fd,B):
    info=check(fd,B)
    return tuple(scan(fd,B,info))


def view_image(fd):
    """Debug/oracle only: image RAM not included in streaming RAM bound."""
    fd.seek(0);return fd.read()


def recourse(a,b,B):
    left=view_image(a);right=view_image(b)
    result=page_difference(left,right,B)
    return {"changed_pages":result["changed_page_positions"],
            "retired_pages":result["pages_removed"],
            "allocated_pages":result["pages_added"],
            "modeled_page_write_bytes":result["modeled_page_image_bytes"]}



def all_mode_images(bits,B):
    """EXHAUSTIVE policy oracle only, not memory-bounded updating."""
    source=from_bits(bits,B,"B")
    options={}
    op=(0,1,bits[0])  # semantically idempotent, to preserve target bits
    info=check(source,B)
    stats=characteristics(source,B,info,op)
    for mode in stats["payload"]:
        candidate,ledger=update(source,B,op,mode)
        options[mode]=view_image(candidate)
        candidate.close()
    source.close()
    return options


def mode_policy_dp(initial,ops,B,initial_mode="B",alpha=4,beta=2,
                   Qcap=4,Rcap=None):
    """Finite offline mode-selection oracle, FULL CRC lookup equal for modes.

    All images materialized by the oracle: this is *not* the streaming updater.
    Q=D/B represents a *single-pass abstract full-CRC-and-decode scanner*,
    possible with B-sized sequential page reads and fixed counters. The actual
    test helpers call check() followed by scan() and can make more read calls;
    DO NOT quote Q as observed tempfile reads or hardware I/O.
    """
    if Rcap is None:
        Rcap=2*B+REGISTER_BYTES
    if Rcap<2*B+REGISTER_BYTES:
        raise MemoryError("bounded updater cannot participate")
    states=[tuple(initial)]
    for op in ops:
        states.append(assign(states[-1],op))
    images=[all_mode_images(bits,B) for bits in states]
    if initial_mode not in images[0]:
        raise ValueError("invalid initial mode")
    def admitted(bits,image):
        return len(image)<=alpha*len(encode_snapshot(bits))+beta*B and len(image)//B<=Qcap
    if not admitted(states[0],images[0][initial_mode]):
        raise ValueError("initial image violates budget")
    dp={initial_mode:(0,())}
    history=[]
    for i in range(1,len(states)):
        next_step={}
        for source_mode,(cost,path) in dp.items():
            old=images[i-1][source_mode]
            for mode,new in images[i].items():
                if not admitted(states[i],new):
                    continue
                # Independent same-offset byte-page comparison is in the tests.
                diff=page_difference(old,new,B)
                weight=diff["changed_page_positions"]+diff["pages_removed"]
                value=(cost+weight,path+(mode,))
                if mode not in next_step or value<next_step[mode]:
                    next_step[mode]=value
        dp=next_step
        history.append(len(dp))
    best=min(dp.values(),default=None)
    return {"feasible":best is not None,
            "cost_page_images_plus_retirement":None if best is None else best[0],
            "mode_sequence":None if best is None else list(best[1]),
            "reachable_modes_by_step":history}

def reset_witness(n=257,B=32):
    initial=(0,)*(n-1)+(1,)
    src=from_bits(initial,B,"B")
    sticky,sticky_ledger=update(src,B,(n-1,n,0),"B")
    smallest,min_ledger=update(src,B,(n-1,n,0),"min")
    before=read_all(src,B)
    if before!=initial or read_all(sticky,B)!=(0,)*n or read_all(smallest,B)!=(0,)*n:
        raise AssertionError("reset truth")
    stay=recourse(src,sticky,B)
    switch=recourse(src,smallest,B)
    result={"N":n,"B":B,"source_mode":"B",
            "source_D":len(view_image(src)),"stay_mode":"B",
            "stay_D":sticky_ledger["D"],"stay_recourse":stay,
            "min_mode":min_ledger["mode"],"min_D":min_ledger["D"],
            "min_recourse":switch,
            "source_mode_not_globally_smallest":True,
            "source_bits_have_one_last_bit":True,
            "all_zero_canonical_ixr1_bytes":len(encode_snapshot((0,)*n)),
            "page_oracle_not_hardware":True}
    src.close();sticky.close();smallest.close()
    return result


def report():
    return {"schema":"mathlab.index001.g2b4c4.hybrid.v1",
            "classification":"MODEL_SCOPED_STREAMING_UPPER_AND_GREEDY_COUNTEREXAMPLE",
            "buffer_bound_bytes_formula":"2*B+128 (emulated I/O buffers only)",
            "whole_python_rss_bounded":False,
            "durability_atomicity_proved":False,
            "allocator_metadata_fully_modeled":False,
            "bitmap_vs_minimum_bytes":reset_witness()}


if __name__=="__main__":
    cli=argparse.ArgumentParser()
    cli.add_argument("--json",action="store_true")
    args=cli.parse_args()
    z=report()
    if args.json:
        print(json.dumps(z,indent=2,sort_keys=True))
    else:
        w=z["bitmap_vs_minimum_bytes"]
        print("N=%d B=%d bitmap %d->%d mode_min=%s D_min=%d image_pages_stay=%d image_pages_min=%d retired_stay=%d retired_min=%d" %
              (w["N"],w["B"],w["source_D"],w["stay_D"],w["min_mode"],w["min_D"],
               w["stay_recourse"]["changed_pages"],w["min_recourse"]["changed_pages"],
               w["stay_recourse"]["retired_pages"],w["min_recourse"]["retired_pages"]))
        print("INDEX001_G2B4C4_HYBRID_STREAMING_PASS")
