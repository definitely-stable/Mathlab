"""INDEX-001 G2-B4-B: independent dense, page-diff and prefix-read oracles."""
import itertools
import math
import random
import unittest

from index001_variable_checkpoint import encode_snapshot, decode_snapshot, uvarint
from index001_page_recourse import (
    alternating_flip_witness, analyze_transition, build_report,
    image_for, lookup_page_probe, page_difference, padded_pages, raw_image,
    runs_and_boundaries, segmented_image, slot_capacity,
    verified_snapshot_pages,
)


def dense_runs(values):
    boundaries = [0]+[i for i in range(1,len(values)) if values[i]!=values[i-1]]+[len(values)]
    return [(boundaries[t+1]-boundaries[t],values[boundaries[t]])
            for t in range(len(boundaries)-1)]


def independent_offset(values, query):
    """Compute run-offset by direct dense scanning, no production prefix parser."""
    runs=dense_runs(values)
    end=4+len(uvarint(len(values)))+len(uvarint(len(runs)))
    completed=0
    for length,bit in runs:
        end+=len(uvarint(length))+1
        if query<completed+length:
            return end
        completed+=length
    raise AssertionError("missing run")


def independent_pages(old,new,b):
    """Independent block comparison: missing bytes compare as zero."""
    result=[]
    for i in range((max(len(old),len(new))+b-1)//b):
        start=i*b
        first=old[start:start+b]+bytes(max(0,b-len(old[start:start+b])))
        second=new[start:start+b]+bytes(max(0,b-len(new[start:start+b])))
        if first!=second:
            result.append(i)
    return result


def expected_prefix_pages(layout,values,point,group,b):
    if layout=="raw":
        return [point//b]
    if layout=="packed":
        start=0
        end=independent_offset(values,point)
    else:
        group_no=point//group
        start=group_no*slot_capacity(group,b)
        lo=group_no*group
        sub=values[lo:min(lo+group,len(values))]
        end=independent_offset(sub,point-lo)
    return list(range(start//b,(start+end-1)//b+1))


class Index001G2B4BTests(unittest.TestCase):
    def test_canonical_all_binary_states_and_page_count(self):
        for n in range(1,9):
            for state in itertools.product((0,1),repeat=n):
                self.assertEqual(decode_snapshot(encode_snapshot(state)),state)
                self.assertEqual(len(runs_and_boundaries(state))+1,len(dense_runs(state)))
                for b in (8,16,32):
                    g=min(3,n)
                    slot=segmented_image(state,g,b)
                    self.assertEqual(len(slot),(n+g-1)//g*slot_capacity(g,b))
                    for block_id,lo in enumerate(range(0,n,g)):
                        sample=state[lo:lo+g]
                        capacity=slot_capacity(g,b)
                        block=slot[block_id*capacity:(block_id+1)*capacity]
                        encoded=encode_snapshot(sample)
                        self.assertEqual(block[:len(encoded)],encoded)
                        self.assertEqual(block[len(encoded):],bytes(capacity-len(encoded)))
                        self.assertEqual(decode_snapshot(block[:len(encoded)]),sample)
                    self.assertEqual(raw_image(state),bytes(state))
                    for typ in ("packed","segmented","raw"):
                        data=image_for(typ,state,g,b)
                        self.assertEqual(len(padded_pages(data,b)),(len(data)+b-1)//b)
                        for at in range(n):
                            answer=lookup_page_probe(typ,state,at,g,b)
                            self.assertEqual(answer["value"],state[at])
                            self.assertEqual(answer["page_indices"],
                                             expected_prefix_pages(typ,state,at,g,b))
                            self.assertFalse(answer["verified_crc"])
                        if typ!="raw":
                            actual=verified_snapshot_pages(typ,state,g,b)
                            if typ=="packed":
                                self.assertEqual(actual,(len(data)+b-1)//b)
                            else:
                                self.assertLessEqual(actual,slot_capacity(g,b)//b)

    def test_all_binary_assignments_against_dense_independent_page_oracle(self):
        for n in range(1,6):
            actions=((lo,hi,bit) for lo in range(n)
                     for hi in range(lo+1,n+1) for bit in (0,1))
            actions=tuple(actions)
            for before in itertools.product((0,1),repeat=n):
                for lo,hi,bit in actions:
                    after=before[:lo]+(bit,)*(hi-lo)+before[hi:]
                    removed=set(runs_and_boundaries(before))-set(runs_and_boundaries(after))
                    added=set(runs_and_boundaries(after))-set(runs_and_boundaries(before))
                    for b in (8,16,32):
                        g=min(3,n)
                        result=analyze_transition(before,after,b,g)
                        self.assertEqual(result["logical_boundary_edits"],
                                         len(removed)+len(added))
                        for typ in ("packed","segmented","raw"):
                            row=result["strategies"][typ]
                            old=image_for(typ,before,g,b)
                            new=image_for(typ,after,g,b)
                            oracle=independent_pages(old,new,b)
                            self.assertEqual(row["changed_page_indices"],oracle)
                            self.assertEqual(row["changed_page_positions"],len(oracle))
                            self.assertEqual(row["modeled_page_image_bytes"],len(oracle)*b)
                            self.assertEqual(row["pages_added"],
                                             max(0,math.ceil(len(new)/b)-math.ceil(len(old)/b)))
                            self.assertEqual(row["pages_removed"],
                                             max(0,math.ceil(len(old)/b)-math.ceil(len(new)/b)))
                            for p in range(n):
                                probe=lookup_page_probe(typ,after,p,g,b)
                                self.assertEqual(probe["value"],after[p])
                                self.assertEqual(probe["page_indices"],
                                                 expected_prefix_pages(typ,after,p,g,b))

    def test_adversarial_single_boundary_recourse_amplification(self):
        for n in (3,5,31,129,511):
            for b in (8,16,32):
                row=alternating_flip_witness(n,b,8)
                packed=row["strategies"]["packed"]
                self.assertEqual(row["logical_boundary_edits"],1)
                self.assertGreaterEqual(packed["shared_changed_pages"],
                                        row["full_suffix_pages_lower_bound"])
                h=4+2*len(uvarint(n))
                self.assertEqual(row["full_suffix_pages_lower_bound"],
                                max(0,(h+2*n-2)//b-(h+2+b-1)//b))
            block=alternating_flip_witness(n,32,8)["strategies"]["segmented"]
            self.assertEqual(block["changed_page_positions"],1)
            self.assertEqual(block["max_point_query_prefix_pages_after"],1)
            self.assertEqual(block["max_crc_verified_frame_pages_after"],1)
        self.assertGreater(alternating_flip_witness(511,32)["strategies"]["packed"]["shared_changed_pages"],20)

    def test_excluded_varint_width_edge_and_capacity_boundaries(self):
        for n in (128,16384):
            if n==128:
                with self.assertRaises(ValueError):
                    alternating_flip_witness(n)
        for group in (1,2,3,7,8,16,32,129):
            for b in (8,16,32):
                capacity=slot_capacity(group,b)
                self.assertEqual(capacity%b,0)
                # Check three extremal encodings: uniform zero, alternating,
                # and a sparse boundary perturbation.
                for bits in (tuple(0 for _ in range(group)),
                             tuple(i%2 for i in range(group)),
                             tuple(1 if i==group//2 else 0 for i in range(group))):
                    self.assertLessEqual(len(encode_snapshot(bits)),capacity)
        self.assertEqual(slot_capacity(8,32),32)
        self.assertGreater(slot_capacity(32,32),32)

    def test_variable_page_layout_does_not_prove_universal_lower_bound(self):
        n=511
        zero=(0,)*n
        packed=len(encode_snapshot(zero))
        slots=len(segmented_image(zero,8,32))
        self.assertLess(packed,20)
        self.assertGreater(slots,packed*20)
        changed=(1,)+zero[1:]
        result=analyze_transition(zero,changed,32,8)
        self.assertLessEqual(result["strategies"]["segmented"]["changed_page_positions"],1)
        self.assertLessEqual(result["strategies"]["raw"]["changed_page_positions"],1)
        self.assertEqual(result["strategies"]["raw"]["disk_bytes_after"],n)
        self.assertEqual(result["strategies"]["segmented"]["disk_bytes_after"],
                         32*math.ceil(n/8))
        with self.assertRaises(ValueError):
            lookup_page_probe("unknown",zero,0,8,32)

    def test_reproducible_report_and_restrictions(self):
        a=build_report()
        self.assertEqual(a,build_report())
        self.assertEqual(len(a["witnesses"]),5)
        self.assertEqual(a["actual_syscalls"],"NOT_MEASURED")
        self.assertEqual(a["physical_nand_bytes"],"NOT_MEASURED")
        self.assertEqual(a["crc_prefix_queries"],"NOT_VERIFIED_PER_QUERY")
        for n in (0,-1,8):
            if n==8:
                with self.assertRaises(ValueError):
                    alternating_flip_witness(n)
            else:
                with self.assertRaises(ValueError):
                    alternating_flip_witness(n)
        with self.assertRaises(ValueError):
            slot_capacity(0,32)
        with self.assertRaises(ValueError):
            page_difference(b"",b"",0)


if __name__=="__main__":
    unittest.main()
