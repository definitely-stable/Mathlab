"""D1-B2-A negative Pareto decision gates and independent historic XOR oracle."""
import itertools
import unittest
from uct005_d1b2a_partial_pareto import PRICE_AXES, exercise, candidate_dominates, ranges

class PartialParetoTests(unittest.TestCase):
    def test_cross_protocol_one_history_n1_to_8_and_small_pages(self):
        for n in range(1, 9):
            for word in itertools.product((0,1), repeat=n):
                # Covers no-op, genesis/latest/PIN epoch correctness for
                # every initial word, two readers, all distinct edge ranges.
                result=exercise(n, 1+(n%3), word)
                self.assertTrue(result["all_honest_answers_verified"])
                self.assertEqual(result["root_novelty"],"OPEN_UNPROVED")
                self.assertEqual(result["history"]["epochs"],3)
                self.assertEqual(result["history"]["set_noop_count"],1)
                self.assertEqual(result["pareto"],["UNDECIDABLE_PARTIAL_PRICING"]*3)
                self.assertEqual(len(result["comparators"]),3)

    def test_page001_witness_correct_full_manifest_48_bytes(self):
        row=exercise(33,2)
        snap=row["comparators"][0]["costs"]
        # 5 packed data bytes -> 3 pages, manifest 48B -> 24 pages
        self.assertEqual(snap["peak_remote_pages"],4*27)
        self.assertEqual(snap["set_remote_page_writes"],3*27)
        self.assertEqual(snap["pinned_retained_pages"],2*27)
        self.assertEqual(snap["author_upload_bytes"],3*54)
        self.assertGreater(snap["trusted_bits"],33+320)
        self.assertEqual(len(row["comparators"]),3)

    def test_pareto_never_computes_with_unknown_axis_or_model(self):
        cases=exercise(8,2)["comparators"]
        for x in cases:
            for y in cases:
                self.assertIsNone(candidate_dominates(x,y))
        complete={x:1 for x in PRICE_AXES}
        richer={x:2 for x in PRICE_AXES}
        a={"service":"S","cost_model":"reference-P","status":"FULLY_PRICED","costs":complete}
        b={"service":"S","cost_model":"reference-P","status":"FULLY_PRICED","costs":richer}
        self.assertTrue(candidate_dominates(a,b))
        self.assertFalse(candidate_dominates(b,a))
        self.assertFalse(candidate_dominates(a,a))
        self.assertIsNone(candidate_dominates(a,{**b,"status":"PARTIAL"}))
        self.assertIsNone(candidate_dominates(a,{**b,"cost_model":"different"}))
        self.assertIsNone(candidate_dominates(a,{**b,"costs":{**richer,"setup_bytes":None}}))

    def test_half_open_range_adapter_and_bad_input(self):
        for n in range(1,30):
            self.assertEqual(len(set(ranges(n))),len(ranges(n)))
            self.assertTrue(all(0<=l<r<=n for l,r in ranges(n)))
        for bits,n in [((1,2),2),((1,),2),((True,),1)]:
            with self.assertRaises(ValueError):
                exercise(n,2,bits)
        with self.assertRaises(ValueError):
            exercise(0,2)
        with self.assertRaises(ValueError):
            exercise(9,0)

if __name__=="__main__":
    unittest.main()
