"""Permanent signed GF5 original W32 physical source sixset packing audit.

The authoritative 51^6 count/independence certificates are exact
JSON integers (not floating point). Independently rerun both original
W32 complete six-motif censuses and 2 different full-51-pattern GF5
sign oracles, compare every original source-ID packing and rational
product with the PERMANENT fixed frozen certificate.
"""
import copy
from fractions import Fraction
import json
from pathlib import Path
import unittest

from hyp105_original_random_palette_distance import (
    run,Q,check_disjoint_original_sixset_packing,
    exact_independent_failure_distribution)

PERMANENT=Path(__file__).with_name(
    "hyp105_original_random_palette_distance_certificates.json")


def verify_permanent_cert(data):
    fresh=run()
    if data!=fresh:
        raise AssertionError("signed ORIGINAL sixset certified 51-palette exact rational result changed")
    if (data["root_230_status"]!="OPEN_WITH_FORMAL_BLOCKER"
        or data["allh_geometric_obstruction_proved_here"]
        or not data["allh_corollary_depends_on_674_EXTERNAL_ACCEPTANCE"]):
        raise AssertionError("root proof promotion / conditional antecedent lost")
    for scheme in ("lex","reverse-line"):
        z=data["schemes"][scheme]
        raw=z["original_source_signed_sixset_witnesses"]
        parsed=check_disjoint_original_sixset_packing(45,raw)
        if (len(parsed)!=3 or
            z["six_source_distinct_packing_size"]!=3 or
            z["full_true_original_W32_accepted_D6"]!=(
                15 if scheme=="lex" else 3) or
            z["full_true_original_W32_accepted_BB_overlap"]!=(
                8 if scheme=="lex" else 7)):
            raise AssertionError("true original frozen W32 source packing changed")
        distribution=exact_independent_failure_distribution(
            tuple(x["chosen_signed_GF5_legal_assignments"] for x in raw))
        expected=Fraction(z[
            "exact_probability_NO_chosen_3v3_source_event"]["numerator"],
            z["exact_probability_NO_chosen_3v3_source_event"]["denominator"])
        if distribution[0]!=expected or expected>(1-Q)**len(raw):
            raise AssertionError("original full-GF5 probability product incorrect")
        if (z["root_all_h_branch_A_proved_here"] or
            not z["does_NOT_equate_chosen_event_zero_with_full_ASET_zero"]):
            raise AssertionError("invalid accepted all-h theorem promotion")
    return True


class PermanentTrueOriginalGF5PaletteDistance(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.saved=json.loads(PERMANENT.read_text(encoding="utf-8"))

    def test_full_actual_source_signed_physical_palette_certificate_replay(self):
        self.assertTrue(verify_permanent_cert(self.saved))

    def test_a_false_GF5_probability_fraction_cannot_survive(self):
        changed=copy.deepcopy(self.saved)
        changed["schemes"]["lex"][
            "exact_probability_NO_chosen_3v3_source_event"]["numerator"]+=1
        with self.assertRaises(AssertionError):
            verify_permanent_cert(changed)

    def test_an_original_source_flag_collision_cannot_survive(self):
        changed=copy.deepcopy(self.saved)
        rows=changed["schemes"]["reverse-line"][
            "original_source_signed_sixset_witnesses"]
        rows[1]["original_source_IDs"][0]=rows[0]["original_source_IDs"][0]
        with self.assertRaises((AssertionError,ValueError)):
            verify_permanent_cert(changed)

    def test_false_root_allh_completion_cannot_survive(self):
        changed=copy.deepcopy(self.saved)
        changed["allh_geometric_obstruction_proved_here"]=True
        with self.assertRaises(AssertionError):
            verify_permanent_cert(changed)


if __name__=="__main__":
    unittest.main()
