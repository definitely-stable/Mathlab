"""Independent exhaustive tiny 4/6-original-ID transversal oracle."""
import unittest
from hyp105_original_event_cover import (
    normalize_edges,covers,verify_disjoint_packing,greedy_packing,
    greedy_cover,bounded_exact_cover,brute_force_min_cover,
    canonical_signed_partition)


class OriginalEventCoverTests(unittest.TestCase):
    def test_every_subfamily_against_different_brute_force(self):
        family=((0,1,2,3),(2,3,4,5),(4,5,6,7,8,9),
                (8,9,10,11),(0,10,12,13,2,8))
        for bits in range(1,1<<len(family)):
            edges=normalize_edges(e for j,e in enumerate(family)
                                  if bits & (1<<j))
            expected=brute_force_min_cover(edges)
            pack=greedy_packing(edges)
            result=bounded_exact_cover(edges,greedy_cover(edges),
                                       max_nodes=25000)
            self.assertEqual(result["status"],"EXACT")
            self.assertEqual((result["lower"],result["upper"]),
                             (len(expected),len(expected)))
            self.assertTrue(covers(edges,result["cover"]))
            self.assertEqual(verify_disjoint_packing(edges,pack),len(pack))
            self.assertLessEqual(len(pack),len(expected))

    def test_disjoint_source_pack_lower_and_trace_upper(self):
        e1=(0,1,2,3,4,5);e2=(6,7,8,9,10,11);e3=(0,1,2,3)
        edges=normalize_edges((e1,e2,e3))
        self.assertTrue(covers(edges,(0,6)))
        self.assertEqual(len(brute_force_min_cover(edges)),2)
        self.assertEqual(verify_disjoint_packing(edges,(e1,e2)),2)
        with self.assertRaises(AssertionError):
            verify_disjoint_packing(edges,(e1,e3))
        with self.assertRaises(AssertionError):
            verify_disjoint_packing(edges,(e1,e1))
        for malformed in (((0,1,2,2),),((0,1,2,3,4),),((0,1,2,-1),)):
            with self.assertRaises(ValueError):
                normalize_edges(malformed)

    def test_negative_signed_source_orientation(self):
        self.assertEqual(canonical_signed_partition(((0,1,2),(3,4,5)),3),
                         ((0,1,2),(3,4,5)))
        self.assertEqual(canonical_signed_partition(((0,1),(2,3)),2),
                         ((0,1),(2,3)))
        for v in (
            ((0,1,2),(2,3,4)), ((0,2,1),(3,4,5)),
            ((3,4,5),(0,1,2)), ((0,1,2),(3,4)),
            ((0,1,2),(3,4,-1))
        ):
            with self.assertRaises(ValueError):
                canonical_signed_partition(v,3)

    def test_small_budget_sound_bounds(self):
        edges=normalize_edges(((0,1,2,3),(4,5,6,7),(8,9,10,11),
                               (0,4,8,12),(1,5,9,13)))
        upper=greedy_cover(edges)
        result=bounded_exact_cover(edges,upper,max_nodes=1)
        self.assertIn(result["status"],("BOUNDED","EXACT"))
        self.assertLessEqual(result["lower"],result["upper"])
        self.assertTrue(covers(edges,result["cover"]))
        with self.assertRaises(ValueError):
            bounded_exact_cover(edges,(0,),max_nodes=10)
        with self.assertRaises(ValueError):
            bounded_exact_cover(edges,upper,max_nodes=0)

    def test_abstract_cover_does_not_certify_gf5_feasibility(self):
        edges=normalize_edges(((0,1,2,3,4,5),))
        self.assertTrue(covers(edges,(0,)))
        self.assertEqual(bounded_exact_cover(edges,(0,))["lower"],1)
        # No coefficient replacements were constructed in this oracle.


if __name__=="__main__":
    unittest.main()
