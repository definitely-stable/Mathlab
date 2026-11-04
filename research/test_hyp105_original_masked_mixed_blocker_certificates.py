"""Independent final-head permanent original Z-masked mixed FULL/CORE referee.

The permanent immutable host certificate is checked against source
reconstruction and literal full ORIGINAL physical coordinate degrees,
every signed original p,q,r source record, independent physical endpoint
source triple, all six original positive GF5 B/B-overlap IDs and exact
two-oriented-path multiplicity. No all-h geometric conclusion follows.
"""
import copy
from pathlib import Path
import json
import unittest

from hyp105_original_masked_mixed_blocker import (
    canonical_true_original_W32_W34_masked_mixed_certificate,
)

CERT=Path(__file__).with_name(
    "hyp105_original_masked_mixed_blocker_certificates.json")


def verify_original_masked_mixed_permanent_certificate(z,*,replay=False):
    expected=[
        (2,"lex",44,1,980,21,2023,2,0),
        (2,"reverse-line",30,5,578,58,1214,0,0),
        (4,"lex",165,14,6658,216,19754,541,1022),
        (4,"reverse-line",177,15,6826,220,20184,449,834),
    ]
    if (z.get("schema")!="mathlab.hyp105.original-masked-FULL-CORE-mixed-blocker.v1"
        or z.get("root_230_status")!="OPEN_WITH_FORMAL_BLOCKER"
        or z.get("full_allh_Branch_A_proved_here") is not False
        or len(z.get("cases",()))!=4):
        raise AssertionError("not complete accepted original source proof scope")
    for x,ground in zip(z["cases"],expected):
        s,scheme,core,removed,theta,delta,B,BB,noncore=ground
        six=x.get("source_original_G7_full_nonZ_certificate",{})
        if ((x.get("s"),x.get("scheme"),
             x.get("original_paired_core_source_count"),
             len(x.get("deleted_original_IDs",[])),
             x.get("exact_theta_allowed"),
             x.get("exact_theta_removed_by_original_owner"),
             x.get("source_B_masked_exact"),
             six.get("accepted_true_original_BBo_sixsets"),
             six.get("unblocked_BBo_source_path_anchor_outside_core"))!=ground
            or x.get("root_230_status")!="OPEN_WITH_FORMAL_BLOCKER"
            or x.get("universal_allh_mixed_blocker_exponent_claimed_newly") is not False
            or not x.get("source_masked_mixed_identity_exact")
            or not x.get("fullcore_deletion_sensitivity_identity_all_N")
            or not x.get("all_source_first_physical_masked_triples_match")
            or not x.get("physical_weighted_blocker_W2_le_BDeltaTr4")
            or not six.get("historical_full_GF5_BBo_positive_class_verified")
            or not six.get("each_original_6set_all_six_flags_avoid_Z")
            or not six.get("two_directed_paths_per_original_BBo_source_sixset")):
            raise AssertionError("true W32/W34 original source Z-masked physical proof mismatch")
        z_owner=x["deleted_owner_weighted_cell_degree_contributions"]
        if (len(z_owner)!=removed
            or sum(z_owner.values())!=delta
            or x["exact_theta_full"]-theta!=delta
            or B!=x["physical_original_source_records_exact"]
            or x["original_admissible_first_internal_blocker_triples_exact"]>B
            or x["masked_K_max"]>x["masked_core_R_max_scaled_by_2d"]
            or x["original_masked_F2"]>x["masked_K_max"]*theta
            or B**2>x["source_collinearity_Cauchy_factor_F1"]*
                        x["original_masked_F2"]):
            raise AssertionError("exact original full/core masked source inequality corrupted")
        W=x["first_core_mixed_blocker_weighted_two_step_completions"]
        Delta=x["physical_core_Delta"]
        tr4=x["physical_core_trace_A4"]
        if W*W>B*Delta*tr4:
            raise AssertionError("physical 4-step source blocker weighted bound corrupted")
        ids=six.get("original_BBo_sixset_IDs",[])
        removed_IDs=set(x["deleted_original_IDs"])
        if (len(ids)!=BB or
            six["unblocked_source_disjoint_original_six_ID_directed_paths"]!=2*BB
            or len(set(tuple(row) for row in ids))!=BB
            or any(len(row)!=6 or len(set(row))!=6 or
                   set(row)&removed_IDs or
                   any(type(i) is not int or not 0<=i<x["original_source_flags"] for i in row)
                   for row in ids)):
            raise AssertionError("not true six DISTINCT surviving ORIGINAL source ID motifs")
    if replay:
        # Rebuild BOTH original W32 and W34 geometries and recalculate
        # every physical core edge, 2-step blocker and 3-step GF5 BBo
        # source event from independently regenerated original source.
        regenerated=canonical_true_original_W32_W34_masked_mixed_certificate()
        regenerated=json.loads(json.dumps(regenerated,sort_keys=True))
        if regenerated!=z:
            raise AssertionError("stored original physical masked proof does not replay")
    return True


class PermanentOriginalMaskFullCoreTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.saved=json.loads(CERT.read_text(encoding="utf-8"))

    def test_independent_full_original_W32_W34_source_and_physical_proof_replay(self):
        self.assertTrue(
            verify_original_masked_mixed_permanent_certificate(
                self.saved,replay=True))

    def test_tamper_mixed_fullcore_theta_owner_fails_closed(self):
        z=copy.deepcopy(self.saved)
        z["cases"][2]["exact_theta_removed_by_original_owner"]+=1
        with self.assertRaises(AssertionError):
            verify_original_masked_mixed_permanent_certificate(z)

    def test_tamper_original_six_ID_accepted_class_provenance_fails_closed(self):
        z=copy.deepcopy(self.saved)
        z["cases"][2]["source_original_G7_full_nonZ_certificate"][
            "original_BBo_sixset_IDs"][0][0]=999
        with self.assertRaises(AssertionError):
            verify_original_masked_mixed_permanent_certificate(z)

    def test_tamper_anchor_outside_core_under_deletion_fails_closed(self):
        z=copy.deepcopy(self.saved)
        z["cases"][3]["source_original_G7_full_nonZ_certificate"][
            "unblocked_BBo_source_path_anchor_outside_core"]=0
        with self.assertRaises(AssertionError):
            verify_original_masked_mixed_permanent_certificate(z)

    def test_tamper_actual_mixed_source_book_record_fails_closed(self):
        z=copy.deepcopy(self.saved)
        z["cases"][0]["source_B_masked_exact"]+=1
        with self.assertRaises(AssertionError):
            verify_original_masked_mixed_permanent_certificate(z)

    def test_falsely_claim_universal_geometric_root_proof_fails_closed(self):
        z=copy.deepcopy(self.saved)
        z["full_allh_Branch_A_proved_here"]=True
        with self.assertRaises(AssertionError):
            verify_original_masked_mixed_permanent_certificate(z)


if __name__=="__main__":
    unittest.main()
