"""INDEX-001 G2-B4-C2 independent dense state / exhaustive partition policy QA."""
import itertools
import math
import zlib
from fractions import Fraction
import unittest

from index001_variable_checkpoint import encode_snapshot, uvarint, decode_snapshot
from index001_adaptive_partition import (
    Limits, admissible, decode_image, directory_frame, framed_length,
    layout, lookup_cost, max_query, optimize_trace, partitions,
    read_directory, reset_certificate, report, transition,
)
from index001_priced_wal import assign


def independent_directory(n, lengths, pcs):
    serial=(b"IDR1"+uvarint(n)+uvarint(len(lengths))+
            b"".join(uvarint(a)+uvarint(p) for a,p in zip(lengths,pcs)))
    return serial+(zlib.crc32(serial)&0xffffffff).to_bytes(4,"little")


def independent_block_difference(a,b,B):
    changed=[]
    for idx in range((max(len(a),len(b))+B-1)//B):
        left=a[idx*B:idx*B+B].ljust(B,b"\x00")
        right=b[idx*B:idx*B+B].ljust(B,b"\x00")
        if left!=right:
            changed.append(idx)
    return changed


def enumerate_strategies(initial, updates, block, oldcuts, limits):
    """Independent full Cartesian partition words, no Bellman/dp call."""
    state=tuple(initial)
    states=[state]
    for op in updates:
        state=assign(state,op)
        states.append(state)
    allcuts=partitions(len(initial))
    initial_view=layout(states[0],oldcuts,block)
    if not admissible(initial_view,block,limits):
        raise ValueError("initial violates cap")
    best=None
    prefixes=[set() for _ in updates]
    for path in itertools.product(allcuts,repeat=len(updates)):
        previous=initial_view
        total=0
        valid=True
        for i,cut in enumerate(path):
            nxt=layout(states[i+1],cut,block)
            if not admissible(nxt,block,limits):
                valid=False;break
            before=previous["disk_bytes"]
            after=nxt["disk_bytes"]
            peak=max(before,after)
            bound=max(limits.cap(states[i],block),limits.cap(states[i+1],block))
            retired=max(0,(before-after)//block)
            changed=independent_block_difference(previous["image"],nxt["image"],block)
            if peak>bound or (limits.max_gc_pages is not None and
                              retired>limits.max_gc_pages):
                valid=False;break
            total+=(len(changed)+retired)*block
            prefixes[i].add(cut)
            previous=nxt
        if valid:
            candidate=(total,path)
            if best is None or candidate<best:
                best=candidate
    return {"feasible":best is not None,
            "min_modeled_write_plus_gc_bytes":None if best is None else best[0],
            "optimal_partitions":None if best is None else [list(t) for t in best[1]],
            "reachable_partition_counts":[len(s) for s in prefixes]}


class AdaptivePartitionTest(unittest.TestCase):
    def test_all_binary_maps_all_partitions_independent_frame_and_queries(self):
        for n in range(1,8):
            for state in itertools.product((0,1),repeat=n):
                for cuts in partitions(n):
                    B=16
                    view=layout(state,cuts,B)
                    decoded,backcuts=decode_image(view["image"],B)
                    self.assertEqual(decoded,state)
                    self.assertEqual(backcuts,cuts)
                    segments=[]
                    prev=0
                    for hi in cuts:
                        segments.append(state[prev:hi]);prev=hi
                    frames=[encode_snapshot(seg) for seg in segments]
                    count=tuple(math.ceil(len(f)/B) for f in frames)
                    expected=independent_directory(n,tuple(map(len,segments)),count)
                    self.assertEqual(view["directory"],expected)
                    self.assertEqual(view["disk_bytes"],
                        (math.ceil(len(expected)/B)+sum(count))*B)
                    self.assertEqual(view["ram_mirror_bits"],8*len(expected))
                    self.assertEqual(read_directory(view["image"],B)["lengths"],
                                     tuple(map(len,segments)))
                    self.assertGreaterEqual(view["disk_bytes"],(len(cuts)+1)*B)
                    for point in range(n):
                        disk=lookup_cost(view,point,"disk")
                        ram=lookup_cost(view,point,"mirrored")
                        self.assertEqual(disk["value"],state[point])
                        self.assertEqual(ram["value"],state[point])
                        self.assertEqual(disk["warm_pages"],disk["cold_pages"])
                        self.assertEqual(ram["warm_pages"]+view["directory_pages"],
                                         ram["cold_pages"])
                        self.assertGreaterEqual(ram["crc_verified_pages"],disk["warm_pages"])
                    self.assertEqual(max_query(view,"disk"),
                                     max(lookup_cost(view,p,"disk")["warm_pages"]
                                         for p in range(n)))

    def test_all_one_step_assignments_page_image_oracle(self):
        for n in range(1,6):
            combos=partitions(n)
            for before in itertools.product((0,1),repeat=n):
                for lo in range(n):
                    for hi in range(lo+1,n+1):
                        for bit in (0,1):
                            after=before[:lo]+(bit,)*(hi-lo)+before[hi:]
                            for c in (combos[0],combos[-1]):
                                old=layout(before,c,16)
                                for d in (combos[0],combos[-1]):
                                    new=layout(after,d,16)
                                    row=transition(old,new,16,Limits(
                                         alpha_n=20,beta=10,query_cap=8))
                                    self.assertEqual(row["changed_page_indices"],
                                      independent_block_difference(
                                        old["image"],new["image"],16))
                                    self.assertEqual(row["retired_pages"],
                                        max(0,(len(old["image"])-
                                               len(new["image"]))//16))
                                    self.assertEqual(row["written_model_bytes"],
                                        len(row["changed_page_indices"])*16)
                                    self.assertEqual(row["after_disk_bytes"],len(new["image"]))
                                    self.assertEqual(row["peak_bytes"],
                                        max(len(old["image"]),len(new["image"])))

    def test_zero_reset_certificate_and_strict_retirement_gate(self):
        z=reset_certificate()
        self.assertEqual((z["old_segments"],z["old_disk_bytes"]),(8,288))
        self.assertEqual(z["old_directory_bytes"],26)
        self.assertEqual(z["new_directory_bytes"],12)
        self.assertEqual(z["new_disk_bytes"],64)
        self.assertEqual(z["zero_snapshot_bytes"],12)
        self.assertEqual(z["zero_budget_bytes"],112)
        self.assertEqual(z["minimum_segment_eliminations"],6)
        self.assertEqual(z["minimum_retired_page_positions"],6)
        self.assertEqual(z["actual_retired_page_positions"],7)
        self.assertEqual(z["disk_only_worst_lookup_before"],2)
        self.assertEqual(z["mirrored_warm_worst_lookup_before"],1)
        self.assertEqual(z["mirror_ram_bits_before"],208)
        with self.assertRaises(ValueError):
            reset_certificate(limits=Limits(max_gc_pages=5))
        with self.assertRaises(ValueError):
            reset_certificate(limits=Limits(max_gc_pages=6))
        # Witness with one partition is different from theorem's lower bound;
        # a two-partition compressed new image requires 3 pages => 6 GC pages.
        initial=tuple(i%2 for i in range(64));zero=(0,)*64
        old=layout(initial,tuple(range(8,65,8)),32)
        new=layout(zero,(32,64),32)
        self.assertEqual(new["disk_bytes"],96)
        self.assertTrue(transition(old,new,32,Limits(max_gc_pages=6))["feasible"])
        self.assertEqual(transition(old,new,32,Limits(max_gc_pages=6))["retired_pages"],6)

    def test_ram_mirror_exact_limit_and_cold_vs_warm(self):
        original=tuple(i%2 for i in range(64))
        v=layout(original,tuple(range(8,65,8)),32)
        baseline=Limits(query_cap=2)
        self.assertTrue(admissible(v,32,baseline))
        self.assertFalse(admissible(v,32,Limits(query_cap=1)))
        mirror=Limits(query_cap=1,mode="mirrored",ram_cap_bits=208)
        self.assertTrue(admissible(v,32,mirror))
        self.assertFalse(admissible(v,32,Limits(
            query_cap=1,mode="mirrored",ram_cap_bits=207)))
        self.assertEqual(max_query(v,"disk"),2)
        self.assertEqual(max_query(v,"mirrored"),1)
        self.assertEqual(lookup_cost(v,63,"mirrored")["cold_pages"],2)
        self.assertEqual(lookup_cost(v,63,"mirrored")["crc_verified_pages"],2)
        self.assertFalse(admissible(v,32,Limits(query_cap=1,ram_cap_bits=999)))

    def test_independent_policy_cartesian_equals_dp_two_modes(self):
        for n in (3,4,5):
            for initial in ((0,)*n,tuple(i%2 for i in range(n))):
                ops=((0,n,1),(1,n,0)) if n>=2 else ((0,1,1),)
                first=tuple(range(1,n+1))
                for lim in (Limits(alpha_n=8,beta=4,query_cap=3),
                            Limits(alpha_n=8,beta=4,query_cap=1,
                                   mode="mirrored",ram_cap_bits=200),
                            Limits(alpha_n=8,beta=4,query_cap=3,max_gc_pages=1)):
                    dp=optimize_trace(initial,ops,16,first,lim)
                    brute=enumerate_strategies(initial,ops,16,first,lim)
                    self.assertEqual(dp,brute)
        # Three updates (n=4): genuine policy product, NOT just one-step.
        initial=(0,1,0,1)
        ops=((0,4,0),(2,3,1),(0,1,1))
        lim=Limits(alpha_n=8,beta=4,query_cap=3)
        self.assertEqual(optimize_trace(initial,ops,32,(1,2,3,4),lim),
                         enumerate_strategies(initial,ops,32,(1,2,3,4),lim))

    def test_crc_integrity_padded_geometry_fail_closed(self):
        v=layout((0,1,1,0),(2,4),16)
        dirty=bytearray(v["image"]);dirty[4]^=1
        with self.assertRaises(ValueError):
            decode_image(bytes(dirty),16)
        dirty=bytearray(v["image"]);dirty[v["directory_pages"]*16+3]^=1
        with self.assertRaises(ValueError):
            decode_image(bytes(dirty),16)
        dirty=bytearray(v["image"]);dirty[15]=1
        with self.assertRaises(ValueError):
            decode_image(bytes(dirty),16)
        dirty=bytearray(v["image"]);dirty[-1]=1
        with self.assertRaises(ValueError):
            decode_image(bytes(dirty),16)
        with self.assertRaises(ValueError):
            decode_image(v["image"][:-16],16)
        with self.assertRaises(ValueError):
            decode_image(v["image"]+bytes(16),16)
        with self.assertRaises(ValueError):
            read_directory(b"junk",16)
        with self.assertRaises(ValueError):
            layout((1,0),(1,1,2),16)
        with self.assertRaises(ValueError):
            layout((1,0),(1,),16)
        with self.assertRaises(ValueError):
            layout((1,0),(2,),3)

    def test_result_is_reproducible(self):
        row=report()
        self.assertEqual(row,report())
        self.assertTrue(row["no_ssd_nand_or_os_measurement"])
        self.assertTrue(row["working_memory_unbounded"])
        self.assertEqual(row["zero_reset"]["minimum_retired_page_positions"],6)


if __name__=="__main__":
    unittest.main()
