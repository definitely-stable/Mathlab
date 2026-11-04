"""Final-head permanent exact ten-sign source GF5 certificate source replay.

Do NOT use floats: stored JSON contains exact rational counts far above
IEEE-754 integer accuracy. Independently rebuild both complete genuine
original W(3,2) source maps, source-disjoint sixsets, exact full 51^6
signed-flow probabilities, and both separate 4096/4^7 GF5 oracles for
ALL ten signs per chosen source sixset, then compare the ENTIRE structure.
"""
import copy
from fractions import Fraction
import json
from pathlib import Path
import unittest

from hyp105_original_ten_sign_exclusive import run,Q_TEN

FROZEN=Path(__file__).with_name(
    "hyp105_original_ten_sign_exclusive_certificates.json"
)


def independently_verify_frozen_ten_sign_source_certificate(z):
    expected=run()
    if z!=expected:
        raise AssertionError("complete true ORIGINAL ten-sign union source certificate drift")
    if (z["schema"]!="mathlab.hyp105.original-W32-ten-sign-exclusive-distance.v1"
        or z["original_root_230_status"]!="OPEN_WITH_FORMAL_BLOCKER"
        or z["new_root_allh_geometric_obstruction_proved"]
        or not z["conditional_allh_requires_674_external_scientific_acceptance"]
        or not z["full_original_sixset_signs_not_falsely_independent"]
        or set(z["source_original_W32_schemes"])!={"lex","reverse-line"}):
        raise AssertionError("false geometric or risk promotion")
    d=z["signed_uniform_GF5_51_to_6_union_probability_min"]
    if Fraction(d["numerator"],d["denominator"])!=Q_TEN:
        raise AssertionError("full 10-sign GF5 union floor corrupted")
    for scheme,src in z["source_original_W32_schemes"].items():
        motifs=src["source_original_sixset_witnesses"]
        if (src["source_disjoint_sixset_packing_size"]!=3
            or len(motifs)!=3
            or not src["all_ten_signs_mutually_EXCLUSIVE_for_each_original_motif"]
            or not src["original_motif_sign_sets_are_INDEPENDENT_ACROSS_disjoint_sixsets"]
            or src["root_allh_accepted_here"]):
            raise AssertionError("not accepted ORIGINAL W32 three-sixset packing")
        ids=[i for motif in motifs for i in motif["original_source_IDs"]]
        if len(ids)!=18 or len(set(ids))!=18:
            raise AssertionError("not six-disjoint ORIGINAL incidence flags")
        p_no=Fraction(1)
        flows=[]
        for m in motifs:
            c=m["ten_sign_GF5_full_51_palette_audit"]
            flow=c["source_ten_sign_union_favorable_palette_assignments_exact"]
            if (c["source_four_flag_dual_closed_subsets"]
                or not c["all_ten_signs_are_MUTUALLY_EXCLUSIVE_not_independent"]
                or len(c["all_ten_original_signed_flow_counts"])!=10
                or sum(c["all_ten_original_signed_flow_counts"])!=flow):
                raise AssertionError("uncertified nonoverlapping 10-original-sign family")
            p_no*=1-Fraction(flow,51**6)
            flows.append(flow)
        if flows!=[54162,54162,53526]:
            raise AssertionError("real W32 original 10-sign exact counts changed")
        cert=src["exact_independent_NO_motif_with_ANY_of_ten_signs_probability"]
        if p_no!=Fraction(cert["numerator"],cert["denominator"]):
            raise AssertionError("invalid independent sixset probability rational product")
        if p_no>(1-Q_TEN)**3:
            raise AssertionError("uniform q10 anti-concentration violated")
    return True


class PermanentOriginalTenSignGF5Certificates(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.z=json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_independent_complete_genuine_W32_all_ten_original_sign_source_replay(self):
        self.assertTrue(independently_verify_frozen_ten_sign_source_certificate(self.z))

    def test_mutated_large_rational_numerator_fails_closed(self):
        z=copy.deepcopy(self.z)
        z["source_original_W32_schemes"]["lex"][
            "exact_independent_NO_motif_with_ANY_of_ten_signs_probability"
        ]["numerator"]+=1
        with self.assertRaises(AssertionError):
            independently_verify_frozen_ten_sign_source_certificate(z)

    def test_false_root_allh_geometric_claim_fails_closed(self):
        z=copy.deepcopy(self.z)
        z["new_root_allh_geometric_obstruction_proved"]=True
        with self.assertRaises(AssertionError):
            independently_verify_frozen_ten_sign_source_certificate(z)

    def test_shared_original_source_flag_fails_closed(self):
        z=copy.deepcopy(self.z)
        motifs=z["source_original_W32_schemes"]["reverse-line"][
            "source_original_sixset_witnesses"]
        motifs[1]["original_source_IDs"][0]=motifs[0]["original_source_IDs"][0]
        with self.assertRaises(AssertionError):
            independently_verify_frozen_ten_sign_source_certificate(z)

    def test_falsely_independent_ten_signs_in_one_sixset_fails_closed(self):
        z=copy.deepcopy(self.z)
        motif=z["source_original_W32_schemes"]["lex"][
            "source_original_sixset_witnesses"][0]
        motif["ten_sign_GF5_full_51_palette_audit"][
            "all_ten_signs_are_MUTUALLY_EXCLUSIVE_not_independent"]=False
        with self.assertRaises(AssertionError):
            independently_verify_frozen_ten_sign_source_certificate(z)


if __name__=="__main__":
    unittest.main()
