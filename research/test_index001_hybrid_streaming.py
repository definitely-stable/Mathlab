"""INDEX-001 C4 independent exact modes, bounded file-stream pages and full policies."""
import itertools
import tempfile
import unittest
import zlib
from math import ceil
from index001_variable_checkpoint import encode_snapshot
from index001_page_recourse import page_difference
from index001_priced_wal import assign
from index001_hybrid_streaming import (
    MODES, REGISTER_BYTES, Reader, all_mode_images, candidates, check,
    characteristics, chosen_modes, from_bits, header, mode_policy_dp,
    read_all, recourse, report, reset_witness, update, view_image,
)


def independent_bitmap(bits):
    b=bytearray((len(bits)+7)//8)
    for i,v in enumerate(bits):
        if v:
            b[i//8]|=1<<(i%8)
    return bytes(b)


def independent_payload(bits,mode):
    if mode.startswith("U"):
        if any(bit != (mode=="U1") for bit in bits):
            raise ValueError("not uniform")
        return b""
    if mode=="B":
        return independent_bitmap(bits)
    from index001_variable_checkpoint import uvarint
    if mode.startswith("S"):
        value=0 if mode=="S0" else 1
        indices=[i for i,x in enumerate(bits) if x!=value]
        return uvarint(len(indices))+b"".join(uvarint(i) for i in indices)
    if mode=="R":
        runs=[]
        for v in bits:
            if runs and runs[-1][1]==v:
                runs[-1]=(runs[-1][0]+1,v)
            else:
                runs.append((1,v))
        return uvarint(len(runs))+b"".join(
            uvarint(length)+bytes((v,)) for length,v in runs)
    raise ValueError("unknown mode")


def independent_image(bits,B,mode):
    payload=independent_payload(bits,mode)
    h=header(len(bits),mode,len(payload))
    frame=h+payload
    frame+=zlib.crc32(frame).to_bytes(4,"little")
    return frame.ljust(ceil(len(frame)/B)*B,b"\0")


def independent_diff(a,b,B):
    changed=0
    for i in range(ceil(max(len(a),len(b))/B)):
        old=a[i*B:(i+1)*B].ljust(B,b"\0")
        new=b[i*B:(i+1)*B].ljust(B,b"\0")
        changed+=(old!=new)
    retired=max(0,len(a)//B-len(b)//B)
    return changed,retired


def brute_policies(initial,ops,B,initial_mode="B",alpha=4,beta=2,Qcap=4):
    states=[tuple(initial)]
    for op in ops:
        a=list(states[-1])
        a[op[0]:op[1]]=[op[2]]*(op[1]-op[0])
        states.append(tuple(a))
    options=[{
        mode:independent_image(bits,B,mode)
        for mode in MODES if not(mode=="U0" and any(bits)) and
        not(mode=="U1" and not all(bits))
    } for bits in states]
    counts=[set() for _ in ops]
    answers=[]
    for word in itertools.product(MODES,repeat=len(ops)):
        before=options[0][initial_mode]
        price=0;valid=True
        for step,mode in enumerate(word):
            if mode not in options[step+1]:
                valid=False;break
            after=options[step+1][mode]
            max_bytes=alpha*len(encode_snapshot(states[step+1]))+beta*B
            if len(after)>max_bytes or len(after)//B>Qcap:
                valid=False;break
            delta=independent_diff(before,after,B)
            price+=sum(delta)
            counts[step].add(mode)
            before=after
        if valid:
            answers.append((price,word))
    best=min(answers,default=None)
    return {"feasible":best is not None,
            "cost_page_images_plus_retirement":None if best is None else best[0],
            "mode_sequence":None if best is None else list(best[1]),
            "reachable_modes_by_step":[len(s) for s in counts]}


class HybridStreamingTest(unittest.TestCase):
    def test_all_binary_maps_all_eligible_encodings_match_independent_bytes(self):
        # Exact full distribution of maps up to n=7, multiple physical B sizes.
        verified=0
        for n in range(1,8):
            for bits in itertools.product((0,1),repeat=n):
                for B in (16,32):
                    fd=from_bits(bits,B,"B")
                    self.assertEqual(read_all(fd,B),bits)
                    self.assertEqual(view_image(fd),independent_image(bits,B,"B"))
                    for mode in MODES:
                        if mode=="U0" and any(bits):
                            continue
                        if mode=="U1" and not all(bits):
                            continue
                        changed,ledger=update(fd,B,(0,1,bits[0]),mode)
                        img=view_image(changed)
                        self.assertEqual(img,independent_image(bits,B,mode))
                        self.assertEqual(read_all(changed,B),bits)
                        self.assertEqual(check(changed,B)["mode"],mode)
                        self.assertEqual(ledger["D"],len(img))
                        self.assertEqual(ledger["writer_pages"],len(img)//B)
                        self.assertGreater(ledger["total_source_read_pages"],0)
                        self.assertEqual(ledger["source_passes"],3)
                        self.assertEqual(ledger["model_RAM_bytes"],2*B+REGISTER_BYTES)
                        verified+=1
                        changed.close()
                    fd.close()
        self.assertGreater(verified,2000)

    def test_all_short_range_updates_against_independent_dense_and_crc(self):
        for n in range(1,6):
            for bits in itertools.product((0,1),repeat=n):
                B=16
                for initial_mode in ("B","R","S0"):
                    source=from_bits(bits,B,initial_mode)
                    for l in range(n):
                        for r in range(l+1,n+1):
                            for val in (0,1):
                                op=(l,r,val)
                                new_bits=bits[:l]+(val,)*(r-l)+bits[r:]
                                for target_mode in ("B","R","S0","S1"):
                                    new,ledger=update(source,B,op,target_mode)
                                    independent=independent_image(new_bits,B,target_mode)
                                    self.assertEqual(view_image(new),independent)
                                    self.assertEqual(read_all(new,B),new_bits)
                                    payload=independent_payload(new_bits,target_mode)
                                    self.assertEqual(ledger["raw_bytes"],
                                        len(header(n,target_mode,len(payload)))+len(payload)+4)
                                    new.close()
                    source.close()

    def test_crc_tamper_and_format_invariants_fail_closed(self):
        source=from_bits((0,1,1,0,1),16,"R")
        good=view_image(source)
        for index in (0,4,8,len(good)-6):
            tampered=bytearray(good);tampered[index]^=1
            with tempfile.TemporaryFile(mode="w+b") as f:
                f.write(tampered);f.seek(0)
                with self.assertRaises(ValueError):
                    read_all(f,16)
        with tempfile.TemporaryFile(mode="w+b") as f:
            f.write(good[:-16]);f.seek(0)
            with self.assertRaises(ValueError):
                check(f,16)
        with tempfile.TemporaryFile(mode="w+b") as f:
            f.write(good+bytes(16));f.seek(0)
            with self.assertRaises(ValueError):
                check(f,16)
        with tempfile.TemporaryFile(mode="w+b") as f:
            b=bytearray(good);b[-1]=1;f.write(b);f.seek(0)
            with self.assertRaises(ValueError):
                check(f,16)
        source.close()
        bitmap=from_bits((1,0,1),16,"B")
        image=bytearray(view_image(bitmap))
        image[7]|=0x80  # bitmap high unused tail bit at payload offset 7
        frame=image[:]
        crc_at=8  # HYB4 + n + mode + payload-size + 1 payload byte
        frame[crc_at:crc_at+4]=zlib.crc32(frame[:crc_at]).to_bytes(4,"little")
        with tempfile.TemporaryFile(mode="w+b") as f:
            f.write(frame);f.seek(0)
            with self.assertRaises(ValueError):
                read_all(f,16)
        bitmap.close()

    def test_exact_ram_gate_and_all_io_passes(self):
        B=16
        f=from_bits((1,0,1,0,0),B,"S0")
        with self.assertRaises(MemoryError):
            update(f,B,(1,3,1),"R",Rcap=2*B+REGISTER_BYTES-1)
        z,ledger=update(f,B,(1,3,1),"R",Rcap=2*B+REGISTER_BYTES)
        self.assertEqual(read_all(z,B),(1,1,1,0,0))
        self.assertGreaterEqual(ledger["preflight_read_pages"],1)
        self.assertGreaterEqual(ledger["analysis_read_pages"],1)
        self.assertGreaterEqual(ledger["emit_source_read_pages"],1)
        self.assertEqual(ledger["total_source_read_pages"],
            ledger["preflight_read_pages"]+ledger["analysis_read_pages"]+
            ledger["emit_source_read_pages"])
        with self.assertRaises(ValueError):
            update(f,B,(0,6,1))
        with self.assertRaises(ValueError):
            update(f,B,(0,1,2))
        with self.assertRaises(ValueError):
            update(f,B,(0,0,1))
        with self.assertRaises(ValueError):
            update(f,B,(0,1,0),"U1")
        z.close();f.close()

    def test_switching_modes_and_distinct_page_recourse_objective(self):
        witness=reset_witness()
        self.assertEqual(witness["N"],257)
        self.assertEqual(witness["B"],32)
        self.assertEqual(witness["source_D"],64)
        self.assertEqual(witness["stay_D"],64)
        self.assertEqual(witness["min_D"],32)
        self.assertEqual(witness["min_mode"],"U0")
        self.assertEqual(witness["stay_recourse"]["changed_pages"],1)
        self.assertEqual(witness["stay_recourse"]["retired_pages"],0)
        self.assertEqual(witness["min_recourse"]["retired_pages"],1)
        self.assertGreater(
            witness["min_recourse"]["changed_pages"]+
            witness["min_recourse"]["retired_pages"],
            witness["stay_recourse"]["changed_pages"]+
            witness["stay_recourse"]["retired_pages"])
        self.assertEqual(witness["all_zero_canonical_ixr1_bytes"],
                         len(encode_snapshot((0,)*257)))

    def test_finite_mode_dp_equal_complete_cartesian_enumeration(self):
        for n in (2,3,4):
            for bits in itertools.product((0,1),repeat=n):
                operations=((0,n,0),(n-1,n,1),(0,1,1))
                for Qcap in (1,2,4):
                    optimized=mode_policy_dp(bits,operations,16,
                        initial_mode="B",Qcap=Qcap,Rcap=160)
                    independent=brute_policies(bits,operations,16,Qcap=Qcap)
                    self.assertEqual(optimized,independent)
        with self.assertRaises(MemoryError):
            mode_policy_dp((0,1),((0,1,1),),16,Rcap=159)

    def test_report_deterministic_and_scope(self):
        r=report()
        self.assertEqual(r,report())
        self.assertFalse(r["whole_python_rss_bounded"])
        self.assertFalse(r["durability_atomicity_proved"])
        self.assertFalse(r["allocator_metadata_fully_modeled"])
        self.assertEqual(r["classification"],
                         "MODEL_SCOPED_STREAMING_UPPER_AND_GREEDY_COUNTEREXAMPLE")


if __name__=="__main__":
    unittest.main()
