"""Independent finite-optimality guards for true W34 source certificates.

The specialized hosted workflow separately runs full 12,704,100
ORIGINAL triple GF5 census BEFORE and AFTER for each source map;
these fast tests independently check exact signed geometry, lower
transversal refutation, source labels and malicious-certificate rejection.
"""
from itertools import combinations
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import hyp105_w34_minimum_recolor_referee as referee
from hyp105_w34_minimum_recolor_referee import (
    checked_inputs,verify_minimum_theorem,pair_sum_collisions_direct)
from hyp105_original_gf5_deterministic_extraction_referee import PALETTES


class W34ExactMinimumLegalGF5Recolors(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.saved=json.loads(referee.MAIN_CERT.read_text(encoding="utf-8"))

    def test_both_exact_minimum_recolor_theorems_direct_initial_GF5_and_cover(self):
        for name,tau,prior,r2,d3,r3 in (
            ("lex",25,27,1,475,54),("reverse-line",26,29,0,61,61)):
            with self.subTest(name=name):
                result=verify_minimum_theorem(name)
                self.assertEqual(result["new_constructive_source_edits"],tau)
                self.assertEqual(result[
                    "independently_reproven_universal_to_this_fixed_source_min_changes"],tau)
                self.assertEqual(result["before_original_R2_D3_true_R3"],
                                 [r2,d3,r3])
                self.assertEqual(result["all_90_100_final_original_pairs_independently_collision_free"],True)
                self.assertEqual(result["root_230_status"],
                                 "OPEN_WITH_FORMAL_BLOCKER")

    def test_no_hidden_original_source_recolor_or_changed_global_f_g(self):
        for name in referee.EXPECTED:
            with self.subTest(name=name):
                model,before,after,v_before,v_after,parent,optimal,T=checked_inputs(name)
                self.assertEqual(len(before),425)
                self.assertEqual(len(after),425)
                self.assertEqual(set(T),
                                 {i for i in range(425) if before[i]!=after[i]})
                self.assertEqual(len(T),optimal["exact_minimal_original_source_changes"])
                self.assertEqual([after[i] for i in T],
                                 optimal["edited_legal_palettes_on_support"])
                self.assertEqual(len(set(model["incidences"])),425)
                self.assertEqual(len(set(v_after)),425)
                self.assertEqual(
                    [sum(x for x in v)%5 for v in v_after],[4]*425)

    def test_tamper_one_of_425_palette_entries_fails_closed(self):
        name="lex"
        corrupted=json.loads(referee.MAIN_CERT.read_text(encoding="utf-8"))
        assignment=corrupted["schemes"][name]["exact_425_original_GF5_after_palettes"]
        self.assertNotIn(0,corrupted["schemes"][name]["minimum_support_original_IDs"])
        assignment[0]=(assignment[0]+1)%51
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"wrong-physical-source-optimum.json"
            p.write_text(json.dumps(corrupted),encoding="utf-8")
            with patch.object(referee,"MAIN_CERT",p):
                with self.assertRaises(AssertionError):
                    checked_inputs(name)

    def test_false_asymptotic_ASET_proof_claim_fails_closed(self):
        altered=json.loads(referee.MAIN_CERT.read_text(encoding="utf-8"))
        altered["all_h_existence_or_asymptotic_exponent_claimed"]=True
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"unsupported-all-h-claim.json"
            p.write_text(json.dumps(altered),encoding="utf-8")
            with patch.object(referee,"MAIN_CERT",p):
                with self.assertRaises(AssertionError):
                    checked_inputs("reverse-line")

    def test_single_actual_palette_mutation_does_not_preserve_existing_certificate(self):
        name="reverse-line"
        altered=json.loads(referee.MAIN_CERT.read_text(encoding="utf-8"))
        changed=altered["schemes"][name]["minimum_support_original_IDs"]
        idx=changed[0]
        after=altered["schemes"][name]["exact_425_original_GF5_after_palettes"]
        old=after[idx]
        after[idx]=(old+1)%51
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"altered-legal-pattern.json"
            p.write_text(json.dumps(altered),encoding="utf-8")
            with patch.object(referee,"MAIN_CERT",p):
                with self.assertRaises(AssertionError):
                    checked_inputs(name)


if __name__=="__main__":
    unittest.main()
