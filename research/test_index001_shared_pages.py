"""INDEX-001 C3: independent binary/partition/CRC/page and policy oracles."""
import itertools
from math import ceil
import unittest
import zlib

from index001_shared_pages import (
    SpaceReadLimits, PageReader, COUNTER_BYTES, admissible, bitset_layout,
    decode_shared, directory_frame, lookup_bitmap, lookup_shared,
    page_transition, partition_dp, report, shared_layout, zero_reset,
)
from index001_adaptive_partition import partitions
from index001_page_recourse import padded_pages
from index001_variable_checkpoint import encode_snapshot, uvarint
from index001_priced_wal import assign


def independent_frame(parts, n):
    lengths=[len(x) for x in parts]
    frames=[encode_snapshot(x) for x in parts]
    data=b"IPD1"+uvarint(n)+uvarint(len(parts))
    for logical,frame in zip(lengths,frames):
        data+=uvarint(logical)+uvarint(len(frame))
    data+=zlib.crc32(data).to_bytes(4,"little")
    return data,b"".join(frames)


def independent_page_changes(a,b,B):
    answer=[]
    for p in range(ceil(max(len(a),len(b))/B)):
        left=a[p*B:(p+1)*B].ljust(B,b"\0")
        right=b[p*B:(p+1)*B].ljust(B,b"\0")
        if left!=right:
            answer.append(p)
    return answer


def brute_policy(initial,ops,B,start,limits):
    truth=[tuple(initial)]
    for op in ops:
        truth.append(assign(truth[-1],op))
    feasible=[]
    stats=[set() for _ in ops]
    for cuts in itertools.product(partitions(len(initial)),repeat=len(ops)):
        cost=0
        prev=shared_layout(truth[0],start,B)
        if not admissible(prev,limits):
            raise ValueError("bad baseline")
        good=True
        for t,c in enumerate(cuts):
            nextview=shared_layout(truth[t+1],c,B)
            if not admissible(nextview,limits):
                good=False;break
            before=prev["image"];after=nextview["image"]
            moved=independent_page_changes(before,after,B)
            retired=max(0,(len(before)-len(after))//B)
            cost+=len(moved)+retired
            stats[t].add(c)
            prev=nextview
        if good:
            feasible.append((cost,cuts))
    optimal=min(feasible,default=None)
    return {"feasible":optimal is not None,
            "min_page_image_plus_retirement":None if optimal is None else optimal[0],
            "optimal_partitions":None if optimal is None else [list(x) for x in optimal[1]],
            "reachable":[len(x) for x in stats]}


class SharedPageTests(unittest.TestCase):
    def test_exhaustive_binary_partitions_crc_and_streaming_queries(self):
        samples=0
        for n in range(1,8):
            for state in itertools.product((0,1),repeat=n):
                for ends in partitions(n):
                    prev=0;parts=[]
                    for e in ends:
                        parts.append(state[prev:e]);prev=e
                    frame,data=independent_frame(parts,n)
                    for B in (16,32):
                        v=shared_layout(state,ends,B)
                        expected=(frame.ljust(ceil(len(frame)/B)*B,b"\0")+
                                  data.ljust(ceil(len(data)/B)*B,b"\0"))
                        self.assertEqual(v["directory"],frame)
                        self.assertEqual(v["image"],expected)
                        self.assertEqual(v["D"],len(expected))
                        self.assertEqual(v["payload_bytes"],len(data))
                        self.assertEqual(decode_shared(expected,B),(state,ends))
                        self.assertEqual(v["warm_cache_bits"],8*len(frame))
                        self.assertGreaterEqual(v["D"],B*(ceil(len(frame)/B)+
                                                             ceil(12*len(ends)/B)))
                        for i,x in enumerate(state):
                            cold=lookup_shared(v,i,"disk")
                            warm=lookup_shared(v,i,"mirror")
                            self.assertEqual(cold["value"],x)
                            self.assertEqual(warm["value"],x)
                            self.assertEqual(cold["Q_directory"],v["directory_pages"])
                            self.assertEqual(warm["Q_directory"],0)
                            self.assertEqual(cold["Q_payload"],warm["Q_payload"])
                            self.assertEqual(cold["Q"],cold["Q_payload"]+v["directory_pages"])
                            self.assertEqual(warm["Q"],warm["Q_payload"])
                            self.assertEqual(cold["working_RAM_bytes"],B+COUNTER_BYTES)
                            self.assertEqual(warm["working_RAM_bytes"],
                                             B+COUNTER_BYTES+len(frame))
                            self.assertFalse(cold["prefix_crc_verified"])
                        samples+=1
        self.assertEqual(samples,2*sum(2**n*2**(n-1) for n in range(1,8)))

    def test_one_step_exact_page_recensus_and_bitmap_control(self):
        for n in range(1,5):
            cuts=partitions(n)
            for before in itertools.product((0,1),repeat=n):
                for lo in range(n):
                    for hi in range(lo+1,n+1):
                        for value in (0,1):
                            after=before[:lo]+(value,)*(hi-lo)+before[hi:]
                            for old_end in (cuts[0],cuts[-1]):
                                old=shared_layout(before,old_end,16)
                                for new_end in (cuts[0],cuts[-1]):
                                    new=shared_layout(after,new_end,16)
                                    row=page_transition(old,new)
                                    independent=independent_page_changes(
                                        old["image"],new["image"],16)
                                    self.assertEqual(row["changed_pages"],len(independent))
                                    self.assertEqual(row["removed_pages"],
                                        max(0,(old["D"]-new["D"])//16))
                                    self.assertEqual(row["written_image_bytes"],16*len(independent))
                            oldb=bitset_layout(before,16)
                            newb=bitset_layout(after,16)
                            changed=independent_page_changes(oldb["image"],newb["image"],16)
                            self.assertEqual(page_transition(oldb,newb)["changed_pages"],
                                             len(changed))
                            for i,x in enumerate(after):
                                self.assertEqual(lookup_bitmap(newb,i)["value"],x)

    def test_two_pinned_shared_vs_independently_padded_vs_bitmap(self):
        for group,K,c2_bytes,shared_bytes,retire in [
            (4,16,576,352,9),(8,8,288,256,6)
        ]:
            obs=zero_reset(64,32,group)
            self.assertEqual(obs["K"],K)
            self.assertEqual(obs["shared_before_bytes"],shared_bytes)
            self.assertEqual(obs["shared_after_bytes"],64)
            self.assertEqual(obs["shared_removed_pages"],retire)
            self.assertEqual(obs["bitmap_before_bytes"],32)
            self.assertEqual(obs["bitmap_after_bytes"],32)
            self.assertEqual(obs["bitmap_removed_pages"],0)
            self.assertEqual(obs["bitmap_changed_pages"],1)
            self.assertEqual(obs["global_zero_ixr1_bytes"],12)
            self.assertLess(shared_bytes,c2_bytes)
            self.assertEqual(obs["working_ram_disk_bytes"],32+COUNTER_BYTES)
            self.assertEqual(obs["working_ram_mirror_bytes"],
                             32+COUNTER_BYTES+obs["shared_directory_bytes"])

    def test_crc_corruption_and_warm_cache_is_not_fresh_disk(self):
        view=shared_layout((0,1,0,1),(2,4),16)
        raw=bytearray(view["image"])
        raw[5]^=1
        with self.assertRaises(ValueError):
            decode_shared(bytes(raw),16)
        with self.assertRaises(ValueError):
            lookup_shared(dict(view,image=bytes(raw)),0,"disk")
        self.assertEqual(lookup_shared(dict(view,image=bytes(raw)),0,"mirror")["value"],0)
        badcache=bytearray(view["directory"]);badcache[5]^=1
        with self.assertRaises(ValueError):
            lookup_shared(dict(view,directory=bytes(badcache)),0,"mirror")
        # Change first segment's stored *symbol byte*: prefix observes corruption,
        # but a full IXR1 CRC verification rejects it.
        raw=bytearray(view["image"])
        pos=view["directory_pages"]*16
        raw[pos+7]^=1
        altered=dict(view,image=bytes(raw))
        self.assertNotEqual(lookup_shared(altered,0,"disk")["value"],0)
        with self.assertRaises(ValueError):
            decode_shared(bytes(raw),16)
        with self.assertRaises(ValueError):
            decode_shared(view["image"][:-16],16)
        with self.assertRaises(ValueError):
            decode_shared(view["image"]+bytes(16),16)
        with self.assertRaises(ValueError):
            shared_layout((0,1),(1,1,2),16)

    def test_exact_page_buffer_and_ram_fails_closed(self):
        state=(0,1,0,1,0,1,0,1)
        v=shared_layout(state,(2,4,6,8),16)
        self.assertTrue(admissible(v,SpaceReadLimits(R=16+COUNTER_BYTES,Q=10)))
        self.assertFalse(admissible(v,SpaceReadLimits(R=16+COUNTER_BYTES-1,Q=10)))
        self.assertTrue(admissible(v,SpaceReadLimits(R=16+COUNTER_BYTES+
                                len(v["directory"]),Q=10,mode="mirror")))
        self.assertFalse(admissible(v,SpaceReadLimits(R=16+COUNTER_BYTES+
                                len(v["directory"])-1,Q=10,mode="mirror")))
        with self.assertRaises(MemoryError):
            lookup_shared(v,0,"disk",Rmax=16+COUNTER_BYTES-1)
        with self.assertRaises(MemoryError):
            lookup_shared(v,0,"mirror",Rmax=16+COUNTER_BYTES)
        with self.assertRaises(MemoryError):
            lookup_bitmap(bitset_layout(state,16),0,Rmax=0)
        with self.assertRaises(ValueError):
            SpaceReadLimits(alpha_d=0)
        with self.assertRaises(ValueError):
            SpaceReadLimits(mode="unknown")

    def test_independent_finite_policy_product_matches_dp(self):
        for n in (3,4):
            for initial in ((0,)*n,tuple(i%2 for i in range(n))):
                ops=[(0,n,0),(1,n,1)]
                first=tuple(range(1,n+1))
                for limits in (
                    SpaceReadLimits(alpha_n=8,beta=4,Q=4,R=16+COUNTER_BYTES),
                    SpaceReadLimits(alpha_n=8,beta=4,Q=2,R=256,mode="mirror"),
                    SpaceReadLimits(alpha_n=2,beta=2,Q=2,R=256,mode="mirror"),
                ):
                    if not admissible(shared_layout(initial,first,16),limits):
                        continue
                    self.assertEqual(partition_dp(initial,ops,16,first,limits),
                                     brute_policy(initial,ops,16,first,limits))
        initial=(0,1,0,1)
        ops=[(0,4,0),(2,3,1),(0,1,1)]
        limits=SpaceReadLimits(alpha_n=8,beta=4,Q=4,R=16+COUNTER_BYTES)
        self.assertEqual(partition_dp(initial,ops,16,(1,2,3,4),limits),
                         brute_policy(initial,ops,16,(1,2,3,4),limits))

    def test_report_and_nonuniversal_stop(self):
        r=report()
        self.assertEqual(r,report())
        self.assertTrue(r["cold_point_read_one_page_scratch"])
        self.assertFalse(r["whole_process_bounded_ram"])
        self.assertFalse(r["nand_io_and_crash_safety_measured"])
        self.assertEqual(r["zero_reset_g4"]["shared_removed_pages"],9)
        self.assertEqual(r["zero_reset_g8"]["bitmap_removed_pages"],0)


if __name__=="__main__":
    unittest.main()
