"""Independent exact source-factor edit support / hitting-set falsifiers."""
import unittest
from itertools import combinations

from hyp105_issue230_d6aa4c_edit_transversal import (
    V32, MIXED_RADIUS, incidence_cover_bits, genuine_original_positive_hypergraph,
    scan_supports, source_hypergraph_report, survivor_certificate)
from hyp105_issue230_d6aa_positional_tensor import classify_original_six,WEIGHTS
from hyp105_issue230_projection import fixture


class OriginalFactorTransversalContract(unittest.TestCase):
    def test_small_unweighted_and_weighted_exhaustive_independent_support(self):
        fake=[
            {"typed_support_bitmask":(1<<0)|(1<<3),"certified_GF5_numerator":7},
            {"typed_support_bitmask":(1<<1)|(1<<3),"certified_GF5_numerator":11},
            {"typed_support_bitmask":(1<<2)|(1<<4),"certified_GF5_numerator":13},
        ]
        bits,weights,allmask=incidence_cover_bits(fake)
        result=scan_supports(bits,weights,allmask,range(5),radius=5)
        self.assertEqual(result["number_exact_supports_checked"],32)
        self.assertEqual(result["minimum_transversal_size"],2)
        for row in result["by_exact_edit_support_size"]:
            k=row["edit_support_size"]
            naive=[]
            for block in combinations(range(5),k):
                survivors=[f for f in fake
                           if not any(f["typed_support_bitmask"]&(1<<v)
                                      for v in block)]
                naive.append((len(survivors),
                              sum(f["certified_GF5_numerator"] for f in survivors)))
            self.assertEqual(row["min_unchanged_original_positive_sixsets"],
                             min(a for a,b in naive))
            self.assertEqual(row["min_unchanged_certified_GF5_numerator"],
                             min(b for a,b in naive))
            self.assertEqual(row["number_source_support_transversals"],
                             sum(a==0 for a,b in naive))
        self.assertEqual(survivor_certificate(bits,weights,allmask,(3,4))[:2],(0,0))
        with self.assertRaises(ValueError):
            survivor_certificate(bits,weights,allmask,(len(bits),))
        with self.assertRaises(ValueError):
            scan_supports(bits,weights,allmask,(0,0,1),radius=2)
        with self.assertRaises(ValueError):
            scan_supports(bits,weights,allmask,range(5),radius=6)

    def test_actual_original_W32_unchanged_motifs_survive_arbitrary_two_type_swaps(self):
        model=fixture(1,"S68")
        source=genuine_original_positive_hypergraph(model)
        self.assertEqual((source["S"],source["Y"]),(68,3112510))
        E=tuple(model["incidences"])
        L=list(model["left_labels"])
        R=list(model["right_labels"])
        # Simultaneously change TWO ORIGINAL points and TWO ORIGINAL lines.
        L[0],L[1]=L[1],L[0]
        R[0],R[1]=R[1],R[0]
        self.assertEqual(len(set(L)),15)
        self.assertEqual(len(set(R)),15)
        block={0,1,V32,V32+1}
        untouched=0
        weighted=0
        for row in source["records"]:
            if any(row["typed_support_bitmask"]&(1<<v) for v in block):
                continue
            six=tuple(E[i] for i in row["original_incidence_ids"])
            self.assertEqual(classify_original_six(six,L,R),row["tag"])
            self.assertEqual(WEIGHTS[row["tag"]],row["certified_GF5_numerator"])
            untouched+=1
            weighted+=row["certified_GF5_numerator"]
        bits,weights,allmask=incidence_cover_bits(source["records"])
        self.assertEqual(survivor_certificate(bits,weights,allmask,sorted(block))[:2],
                         (untouched,weighted))

    def test_genuine_original_W32_S68_full_single_type_and_mixed_up_to_five(self):
        x=source_hypergraph_report("S68")
        self.assertTrue(x["true_original_W32"])
        self.assertEqual(x["original_positive_sixsets"],68)
        self.assertEqual(x["original_GF5_certified_numerator"],3112510)
        self.assertTrue(x["all_62370_original_left_candidates_checked"])
        a=x["typed_original_factor_coverage"]
        for side in ("point_only","line_only"):
            self.assertEqual(a[side]["number_exact_supports_checked"],1<<15)
            self.assertTrue(a[side]["minimum_transversal_is_exact"])
            self.assertGreaterEqual(a[side]["minimum_transversal_size"],1)
        self.assertEqual(a["mixed_both_types"]["max_edit_radius_exhaustively_checked"],
                         MIXED_RADIUS)
        self.assertEqual(a["mixed_both_types"]["number_exact_supports_checked"],
                         sum(__import__("math").comb(30,k) for k in range(MIXED_RADIUS+1)))
        self.assertLessEqual(x["AA4B_pinned_block_unchanged_positive_S"],68)
        self.assertLessEqual(x["AA4B_pinned_block_unchanged_GF5_numerator"],3112510)

    def test_reject_invalid_model_and_scope(self):
        model=fixture(1,"S68")
        malformed=dict(model)
        malformed["s"]=4
        with self.assertRaises(ValueError):
            genuine_original_positive_hypergraph(malformed)
        with self.assertRaises(ValueError):
            source_hypergraph_report("unknown")


if __name__=="__main__":
    unittest.main()
