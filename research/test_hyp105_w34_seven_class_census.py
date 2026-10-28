"""Independent exact original W32/W34 seven-class census regression."""
import json
import os
import subprocess
import tempfile
from pathlib import Path
import unittest

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_g5e2b3e1b0_seven_signature import seven_census
from hyp105_w34_seven_class_census import (
    build_census_binary,
    certified_model_seven_counts,
    true_W34_positive_zero_all_seven_census,
)


class TestOriginalSevenClassW34Census(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tempdir = tempfile.TemporaryDirectory(prefix="hyp105-seven-test-")
        cls.binary = build_census_binary(Path(cls.tempdir.name)/"source-original-seven")

    @classmethod
    def tearDownClass(cls):
        cls.tempdir.cleanup()

    def test_true_W32_lex_and_reverse_against_independent_historical_census(self):
        for scheme in ("lex", "reverse-line"):
            with self.subTest(scheme=scheme):
                model = pair_labeled_symplectic(1, scheme)
                historic = seven_census(model, independent_checks=True)
                new = certified_model_seven_counts(
                    self.binary, 1, model["left_labels"],
                    model["right_labels"], model["incidences"],
                    J=range(5))
                self.assertEqual(new["all_seven_original_GF5_classes"],
                                 historic["seven_class_motif_counts"])
                self.assertEqual(new["global_S_seven"], historic["S_seven"])
                self.assertEqual(
                    new["GF5_seven_necessary_R3_floor_numerator"],
                    historic["GF5_seven_lower_numerator"])
                self.assertTrue(
                    new["native_original_BC"][
                        "native_historical_GF5_witnesses_verified"])
                self.assertGreater(
                    new["native_original_BC"][
                        "exhaustive_B_original_sixset_candidates_both_axes"], 0)
                self.assertGreater(
                    new["native_original_BC"][
                        "exhaustive_C_original_sixset_candidates_both_axes"], 0)
                self.assertFalse(new["root_universal_Omega_s6_proved"])

    def test_native_rejects_repeated_source_flag_and_noninjective_pair_map(self):
        m = pair_labeled_symplectic(1, "lex")
        f = list(m["left_labels"])
        f[0] = f[1]
        with self.assertRaises(ValueError):
            certified_model_seven_counts(
                self.binary, 1, f, m["right_labels"], m["incidences"])
        from hyp105_w34_seven_class_census import _model_text
        text = _model_text(1, m["left_labels"], m["right_labels"],
                           m["incidences"])
        lines = text.splitlines()
        # Repeating an actual original flag is rejected by native source guard.
        lines[-1] = lines[-2]
        child = subprocess.run(
            [str(self.binary)], input="\n".join(lines) + "\n",
            text=True, capture_output=True, timeout=20)
        self.assertNotEqual(child.returncode, 0)
        self.assertIn("HYP105_EXACT_SEVEN_FAIL_CLOSED", child.stderr)

    @unittest.skipUnless(os.environ.get("HYP105_FULL_W34_SEVEN") == "1",
                         "full exhaustive W34 runs only in dedicated hosted CI")
    def test_TRUE_W34_POS_ZERO_all_seven_exhaustive_source_census(self):
        result = true_W34_positive_zero_all_seven_census()
        self.assertTrue(result["all_seven_classes_finite_W34_exhaustive"])
        # Exact independently hosted W34 source-ID certificate, not a fit.
        self.assertEqual(
            result["positive"]["all_seven_original_GF5_classes"],
            {
                "D6": 7567,
                "B-left/A-right": 177564,
                "A-left/B-right": 173412,
                "C/A": 22122,
                "C/B": 4070,
                "B/B-overlap": 22802,
                "B/B-disjoint": 21921,
            })
        self.assertEqual(
            result["zero"]["all_seven_original_GF5_classes"],
            {
                "D6": 8110,
                "B-left/A-right": 170578,
                "A-left/B-right": 168080,
                "C/A": 21349,
                "C/B": 4336,
                "B/B-overlap": 23262,
                "B/B-disjoint": 19827,
            })
        self.assertEqual(
            (result["positive"]["global_S_seven"],
             result["zero"]["global_S_seven"]),
            (429458, 415542))
        self.assertEqual(result["global_S_seven_zero_minus_positive"],
                         -13916)
        self.assertEqual(
            (result["positive"]["GF5_seven_necessary_R3_floor_numerator"],
             result["zero"]["GF5_seven_necessary_R3_floor_numerator"]),
            (19371832431, 18722310780))
        self.assertEqual(
            result["certified_GF5_R3_floor_numerator_zero_minus_positive"],
            -649521651)
        # Falsifies monotone local-M or global-D6 proxies for the actual
        # same-model seven-family S and its GF5 weighted necessary floor.
        self.assertGreater(
            result["zero"]["all_seven_original_GF5_classes"]["D6"],
            result["positive"]["all_seven_original_GF5_classes"]["D6"])
        self.assertLess(result["zero"]["global_S_seven"],
                        result["positive"]["global_S_seven"])
        self.assertEqual(
            result["zero_minus_positive_by_historical_GF5_class"]["D6"],
            543)
        self.assertEqual(
            result["positive"]["all_seven_original_GF5_classes"]["D6"],
            7567)
        self.assertEqual(
            result["zero"]["all_seven_original_GF5_classes"]["D6"],
            8110)
        for key in ("positive", "zero"):
            entry = result[key]
            self.assertEqual(
                sum(entry["all_seven_original_GF5_classes"].values()),
                entry["global_S_seven"])
            self.assertEqual(
                len(entry["all_seven_original_GF5_classes"]), 7)
            self.assertGreaterEqual(
                entry["global_S_seven"],
                entry["all_seven_original_GF5_classes"]["D6"])
        self.assertEqual(
            result["global_S_seven_zero_minus_positive"],
            result["zero"]["global_S_seven"] -
            result["positive"]["global_S_seven"])
        self.assertFalse(
            result["positive"]["full_GF5_R3_computed"])
        self.assertTrue(result["no_all_h_root_A_or_B_claim"])
        print("HYP105_AA4_SEVEN34_CERTIFICATE=" +
              json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    unittest.main()
