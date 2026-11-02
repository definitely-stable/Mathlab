"""AA4-R6ALIGN independent all-h source template and third GF5 Fourier tests."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb
import unittest

from hyp105_full_physical_degree_tail import genuine_source
from hyp105_original_aligned_bbo_gf5_fourier_referee import (
    PALETTE_SIX, SIGNED_ALIGNED_BBO, SIGNED_UNALIGNED_BBO,
    SIGNS, _cycles, _opposite, aligned_template_types,
    gf5_fourier_potential_oracle, source_six_original_ids,
    lift_template, classify_original_six_alignment,
    source_coordinate_edges, count_actual_physical_owner_paths,
    exact_aligned_signed_certificate, sharpened_original_r3_floor,
)
from hyp105_gf5_original_sixid_flow_referee import (
    gf5_flow_inclusion_exclusion, gf5_flow_spanning_tree,
)


class OriginalAlignedBBoR6Referee(unittest.TestCase):
    def test_all_nine_named_typed_template_structures_and_middle_owner_bijection(self):
        templates=aligned_template_types()
        self.assertEqual(len(templates),9)
        self.assertEqual(len({x["left"] for x in templates}),3)
        self.assertEqual(len({x["right"] for x in templates}),3)
        self.assertEqual(Counter(x["aligned"] for x in templates),
                         Counter({True:3,False:6}))
        for typ in templates:
            self.assertEqual(typ["aligned"],
                             typ["left_middle_owner"]==typ["right_middle_owner"])
            self.assertIn(typ["left_middle_owner"],(3,4,5))
            self.assertIn(typ["right_middle_owner"],(3,4,5))
            self.assertEqual(len(typ["edges"]),12)
            self.assertEqual(Counter(typ["edges"])[(0,1)],2)
            self.assertEqual(Counter(typ["edges"])[(0,2)],2)

    def test_independent_integer_fourier_vs_both_historical_gf5_oracles(self):
        # All 90 genuinely distinct 3+3 masks independently checked with
        # the historic edge-IE implementation; selected tree-current
        # witnesses provide a second unrelated validation of the new method.
        distribution=Counter()
        for idx,typ in enumerate(aligned_template_types()):
            vec=[]
            for si,sign in enumerate(SIGNS):
                actual=gf5_fourier_potential_oracle(typ["edges"],sign)
                self.assertEqual(actual,
                                 gf5_flow_inclusion_exclusion(typ["edges"],sign))
                if si in (0,5,9):
                    self.assertEqual(actual,
                                     gf5_flow_spanning_tree(typ["edges"],sign))
                self.assertGreater(actual,0)
                vec.append(actual)
            distribution[typ["aligned"],sum(vec)]+=1
            self.assertEqual(sum(vec),
                             53838 if typ["aligned"] else 53526)
        self.assertEqual(distribution,Counter({(True,53838):3,(False,53526):6}))

    def test_real_true_original_W32_W34_all_18_lifts_full_injections_and_0_or_2(self):
        for power in (1,2):
            with self.subTest(power=power):
                results=exact_aligned_signed_certificate(power)
                self.assertEqual(len(results),9)
                self.assertEqual(Counter((r["aligned"],r["exact_signed_mass"])
                                         for r in results),
                                 Counter({(True,53838):3,(False,53526):6}))
                self.assertEqual(Counter(r["original_produced_directed_paths"]
                                         for r in results),
                                 Counter({2:3,0:6}))
                for typ in aligned_template_types():
                    s,v,flags,ids,f,g=lift_template(power,typ)
                    self.assertEqual(v,(s+1)*(s*s+1))
                    self.assertEqual(len(set(f)),v)
                    self.assertEqual(len(set(g)),v)
                    self.assertEqual(len(set(ids)),6)
                    p,ell=flags[ids[0]]
                    self.assertEqual(flags[ids[1]][0],p)
                    self.assertEqual(flags[ids[2]][1],ell)
                    # Same anchored source sixset, but 3 anchor ORIGINAL
                    # flags are intentionally OUTSIDE the retained CORE.
                    self.assertFalse(set(ids[:3]) & set(ids[3:]))
                    self.assertEqual(count_actual_physical_owner_paths(
                        flags,ids,f,g),2 if typ["aligned"] else 0)
                    self.assertEqual(Counter(source_coordinate_edges(
                        flags,ids,f,g)),Counter(typ["edges"]))
                    # Arbitrary permutation of same unordered ORIGINAL IDs
                    # cannot affect canonical source provenance classification.
                    perm=ids[::-1]
                    c=classify_original_six_alignment(flags,perm,f,g)
                    self.assertEqual(c["ordered_original_ids"],ids)
                    self.assertEqual(c["aligned"],typ["aligned"])

    def test_improved_original_risk_floor_uses_aligned_only_without_double_count(self):
        self.assertEqual(sharpened_original_r3_floor(0,1),
                         Fraction(53838,51**6))
        self.assertEqual(sharpened_original_r3_floor(1,1,1),
                         Fraction(54162+53838+53526,51**6))
        self.assertEqual(sharpened_original_r3_floor(0,1)-
                         Fraction(53526,51**6),Fraction(312,51**6))
        self.assertEqual(SIGNED_ALIGNED_BBO-SIGNED_UNALIGNED_BBO,312)
        self.assertEqual(PALETTE_SIX,51**6)
        for vals in ((-1,0,0),(0,-1,0),(0,0,-1),(1.0,1,1)):
            with self.assertRaises(ValueError):
                sharpened_original_r3_floor(*vals)

    def test_fourier_rejects_bad_six_column_source_profiles(self):
        typ=aligned_template_types()[0]
        with self.assertRaises(ValueError):
            gf5_fourier_potential_oracle(typ["edges"][:-1],SIGNS[0])
        with self.assertRaises(ValueError):
            gf5_fourier_potential_oracle(typ["edges"],frozenset((1,2,3)))
        with self.assertRaises(ValueError):
            gf5_fourier_potential_oracle(typ["edges"][:11]+((0,0),),SIGNS[0])
        with self.assertRaises(ValueError):
            _cycles((1,1,2,3))
        with self.assertRaises(ValueError):
            _opposite(((0,1),(1,2),(0,2),(3,4)),2)


if __name__=="__main__":
    unittest.main()
