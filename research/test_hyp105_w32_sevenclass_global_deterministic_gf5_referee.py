"""Independent actual W32 45-source-ID complete seven leading GF5 parity CSP tests."""
from collections import Counter
from fractions import Fraction
from pathlib import Path
import json
import unittest

from hyp105_original_gf5_deterministic_extraction_referee import PALETTES,DENOM
from hyp105_w32_sevenclass_global_deterministic_gf5_referee import (
    CLASSES,PINNED,_source_palette_by_id,
    true_original_w32_seven_hypergraph,
    independent_all_ten_exact_expected_risk,
    parity_sign_events,slow_direct_original_sign_events,
    hypergraph_direct_event_census,
    find_actual_global_sevenclass_zero_certificate,
    check_supplied_full_original_certificate,
)


class W32OriginalSevenFamilyDeterministic(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.models={s:true_original_w32_seven_hypergraph(s)
                    for s in ("lex","reverse-line")}

    def test_complete_true_original_source_sevenclass_hypergraph_and_overlap(self):
        for scheme,m in self.models.items():
            with self.subTest(scheme=scheme):
                self.assertEqual(m["physical_leading_candidates"],62370)
                self.assertEqual(m["all_45_original_flag_count"],45)
                self.assertEqual(len(m["source"]["incidences"]),45)
                self.assertEqual(len(set(m["source"]["incidences"])),45)
                self.assertEqual(tuple(m["counts"][k] for k in CLASSES),
                                 PINNED[scheme]["counts"])
                self.assertEqual(m["selected_original_sixsets"],
                                 259 if scheme=="lex" else 169)
                self.assertTrue(any(x>0 for x in
                    m["overlap_size_histogram"].values()))
                self.assertGreater(m["overlap_size_histogram"].get(1,0),0)
                self.assertEqual(sum(m["overlap_size_histogram"].values()),
                                 len(m["motifs"])*(len(m["motifs"])-1)//2)
                for q in m["motifs"]:
                    self.assertEqual(len(set(q["ids"])),6)
                    self.assertEqual(len(q["edges"]),12)
                    self.assertIn(q["kind"],CLASSES)

    def test_full_sevenclass_exact_GF5_expected_mass_independent_potential_oracle(self):
        # Expensive intentionally: every actual ORIGINAL selected sixset,
        # all ten balanced GF5 signs, independent 5^5 vertex potentials.
        for scheme,m in self.models.items():
            with self.subTest(scheme=scheme):
                r=independent_all_ten_exact_expected_risk(m)
                self.assertEqual(r["all_selected_original_sevenclass_signed_mass_numerator"],
                                 PINNED[scheme]["numerator"])
                self.assertEqual(tuple(r["exact_GF5_ten_sign_mass_by_class"][k]
                                       for k in CLASSES),PINNED[scheme]["sum_by_class"])
                self.assertEqual(r["exact_mean_signed_events"],
                                 Fraction(PINNED[scheme]["numerator"],DENOM))
                self.assertGreater(r["union_bound_probability_no_signed_events_at_least"],
                                   Fraction(999,1000))
                self.assertTrue(r["zero_exists_for_all_selected_sevenclass_sixsets"])
                self.assertTrue(r["not_full_R3"])

    def test_new_GF5_to_GF2_parity_signed_oracle_vs_physical_brute(self):
        for scheme,m in self.models.items():
            for style in ("all-ones",0,1,2):
                with self.subTest(scheme=scheme,style=style):
                    if style=="all-ones":
                        a={i:PALETTES[0] for i in range(45)}
                    else:
                        a={i:PALETTES[j] for i,j in enumerate(
                           _source_palette_by_id(scheme,style,45))}
                    r=hypergraph_direct_event_census(m,a,independent_parity=True)
                    self.assertEqual(r["number_sign_events_per_original_sixset_histogram"]
                                     .get(0,0)+r["colliding_original_sixset_count"],
                                     len(m["motifs"]))
                    self.assertEqual(sum(r["event_count_by_original_class"].values()),
                                     r["actual_ten_sign_event_count"])
                    self.assertTrue(r["exact_physical_parity_vs_brute_GF5_oracle_checked"])
                    if style=="all-ones":
                        self.assertGreater(r["actual_ten_sign_event_count"],0)
                    for q in m["motifs"]:
                        self.assertEqual(parity_sign_events(q,a),
                                         slow_direct_original_sign_events(q,a))

    def test_prove_real_complete_45_original_ID_witness_zero_every_class(self):
        for scheme,m in self.models.items():
            with self.subTest(scheme=scheme):
                certificate=find_actual_global_sevenclass_zero_certificate(
                    m,max_seeds=64)
                self.assertEqual(certificate["certified_original_flags"],45)
                self.assertLess(certificate["seed"],64)
                self.assertEqual(certificate["zero_selected_sevenclass_actual_signed_events"],0)
                self.assertGreater(certificate["all_ones_reference_actual_signed_events"],0)
                self.assertTrue(certificate["physical_SAT_parity_and_direct_GF5_fully_agree"])
                self.assertEqual(len(certificate["original_flag_palettes"]),45)
                self.assertEqual(len(set(certificate["original_flag_palettes"])),45)
                r=check_supplied_full_original_certificate(
                    m,certificate["original_flag_palette_indices"])
                self.assertEqual(r["actual_ten_sign_event_count"],0)
                self.assertEqual(r["colliding_original_sixset_count"],0)
                self.assertEqual(sum(r["event_count_by_original_class"].values()),0)
                # All-ones has TRUE events; reject fraudulent zero certificate.
                with self.assertRaises(ValueError):
                    check_supplied_full_original_certificate(
                        m,tuple(PALETTES.index((1,1,1,1)) for _ in range(45)))

    def test_committed_complete_45_original_source_certificate_is_independently_valid(self):
        path=Path(__file__).with_name(
            "hyp105_w32_sevenclass_original_45flag_certificates.json")
        payload=json.loads(path.read_text(encoding="utf-8"))
        self.assertTrue(payload["selected_family_only"])
        self.assertTrue(payload["not_full_R3"])
        self.assertFalse(payload["new_ASET_exponent_proved"])
        self.assertEqual(set(payload["certificates"]),set(self.models))
        for scheme,m in self.models.items():
            with self.subTest(scheme=scheme):
                cert=payload["certificates"][scheme]
                indices=tuple(cert["palette_indices_in_original_flag_ID_order"])
                self.assertEqual(cert["original_source_flag_count"],45)
                self.assertEqual(cert["selected_original_sixset_count"],
                                 len(m["motifs"]))
                self.assertEqual(len(indices),45)
                self.assertEqual(
                    indices,_source_palette_by_id(scheme,cert["deterministic_seed"],45))
                self.assertEqual(
                    Fraction(cert["exact_signed_event_mean"]),
                    Fraction(PINNED[scheme]["numerator"],DENOM))
                result=check_supplied_full_original_certificate(m,indices)
                self.assertEqual(result["actual_ten_sign_event_count"],0)
                self.assertEqual(result["colliding_original_sixset_count"],0)
                self.assertEqual(cert["exact_direct_signed_events"],0)
                self.assertGreater(cert["all_ones_signed_events"],0)

    def test_parity_rejects_illegal_G5_source_assignment_and_scope(self):
        m=self.models["lex"]
        q=m["motifs"][0]
        a={i:PALETTES[0] for i in range(45)}
        with self.assertRaises(ValueError):
            parity_sign_events(q,{})
        with self.assertRaises(ValueError):
            hypergraph_direct_event_census(m,{})
        with self.assertRaises(ValueError):
            check_supplied_full_original_certificate(m,tuple([0]*44))
        with self.assertRaises(ValueError):
            check_supplied_full_original_certificate(m,tuple([0]*44+[-1]))
        with self.assertRaises(ValueError):
            find_actual_global_sevenclass_zero_certificate(m,max_seeds=0)
        self.assertTrue(m["not_all_possible_six_source_ID_subsets"])
        self.assertTrue(DENOM>10**10)


if __name__=="__main__":
    unittest.main()
