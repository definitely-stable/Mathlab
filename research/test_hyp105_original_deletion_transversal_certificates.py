"""Permanent true ORIGINAL W32 exact adversarial-deletion certificate replay.

Rebuild the original symplectic W32 45 genuine flag incidences, BOTH
complete global f/g maps, all 62,370 original left-positive sixsets,
both ORIGINAL D6/BBo accepted hypergraphs, exact integer min deletion
and MAX disjoint matching, and all C(45,k), k=0..4 deletion fronts,
then compare the ENTIRE permanent proof JSON with an independently
fresh reexecution. Negative edits never silently promote finite to all-h.

Do not parse exact >2^53 probability certificate integers through JS.
"""
import copy
from fractions import Fraction
from pathlib import Path
from math import comb
import json
import unittest

from hyp105_original_deletion_transversal_referee import (
    run, Q_TEN, _six_original_mask,
    exact_binomial_tail_under_ten_sign_union)

CERT=Path(__file__).with_name(
    "hyp105_original_deletion_transversal_certificates.json")


def check_permanent_original_W32_witness_consistency(x,*,full_replay=False):
    if (x.get("schema")!="mathlab.hyp105.original-W32-exact-deletion-research.v1"
        or x.get("root_230_status")!="OPEN_WITH_FORMAL_BLOCKER"
        or not x.get("allh_corollary_requires_independently_accepting_674")
        or not x.get("this_is_NOT_a_new_universal_D6_BBo_lower")
        or not x.get("binomial_tail_all_N_theorem_independent_of_674")
        or set(x.get("finite_schemes",{}))!={"lex","reverse-line"}):
        raise AssertionError("false root promotion or genuine W32 provenance drift")
    for name,expected in (("lex",(15,8,5,4)),
                          ("reverse-line",(3,7,3,3))):
        z=x["finite_schemes"][name]
        D,B,tau,nu=expected
        h=z["independent_full_original_sixset_ID_edges"]
        if (z.get("schema")!=
            "mathlab.hyp105.original-W32-exact-deletion-transversal-and-packing.v1"
            or z.get("true_original_incidence_flags")!=45
            or z.get("complete_original_physical_left_qualified_sixsets_audited")!=62370
            or z.get("accepted_true_original_D6_BBo_six_motifs")!=D+B
            or z.get("accepted_true_original_by_class")!={"D6":D,"B/B-overlap":B}
            or len(h)!=D+B
            or z.get("root_230_status")!="OPEN_WITH_FORMAL_BLOCKER"
            or z.get("root_allh_geom_branch_A_PROVED_HERE") is not False
            or z.get("claim_entire_W32_0_3_GF5_R3_exact_computed") is not False
            or z.get("general_allh_source_packing_requires_external_review_of_674")
            is not True):
            raise AssertionError("false/altered ORIGINAL finite source proof scope")
        e=[]
        for v in h:
            ids=v["original_source_IDs"]
            if (v["accepted_class"] not in ("D6","B/B-overlap")
                or ids!=sorted(set(ids))):
                raise AssertionError("not one true six-distinct-ID accepted source motif")
            e.append(_six_original_mask(ids,45))
        if len(set(e))!=len(e):
            raise AssertionError("source original hypergraph IDs duplicated")
        cover=z["exact_minimum_adversarial_original_ID_deletions"]
        match=z["exact_maximum_original_ID_disjoint_six_motif_packing"]
        if (cover["tau"]!=tau or
            cover["rejected_cardinality_at_tau_minus_1"] is not True
            or match["nu"]!=nu or
            match["exact_maximum_proved_by_include_exclude_DP"] is not True
            or len(cover["original_IDs"])!=tau
            or len(set(cover["original_IDs"]))!=tau
            or len(match["six_original_ID_sets"])!=nu):
            raise AssertionError("source deletion/minimum or packing cardinals drift")
        T=sum(1<<i for i in cover["original_IDs"])
        if any((T&edge)==0 for edge in e):
            raise AssertionError("original cardinality tau cover fails to hit an event")
        occupied=0
        for ids in match["six_original_ID_sets"]:
            mask=_six_original_mask(ids,45)
            if mask not in e or mask&occupied:
                raise AssertionError("not an ORIGINAL disjoint six-motif packing")
            occupied|=mask
        p=z["exhaustive_adversarial_original_ID_deletions_size_0_to_4"]
        expected_min=([23,15,9,5,2] if name=="lex"
                      else [10,5,1,0,0])
        expected_worst=([1,2,3,4,7] if name=="lex"
                        else [1,1,1,6,276])
        if len(p)!=5:
            raise AssertionError("lost exhaustive adversarial source Z sizes")
        for k,row in enumerate(p):
            if (row["deleted_original_ID_cardinality"]!=k
                or row["all_adversarial_deletion_subsets_exactly_enumerated"]!=comb(45,k)
                or row["minimum_surviving_true_original_six_motifs"]!=expected_min[k]
                or row["number_of_worst_adversarial_source_deletions"]!=expected_worst[k]
                or row["exact_total_survivor_events_over_all_deletions"]!=
                    (D+B)*comb(39,k)
                or row["independent_original_six_ID_double_count"]!=
                    (D+B)*comb(39,k)):
                raise AssertionError("complete original Z-deletion distribution altered")
            witness=row["lex_first_worst_source_deletion_IDs"]
            if k and (len(witness)!=k or len(set(witness))!=k or
                       sum(1 for edge in e
                           if not edge&sum(1<<i for i in witness))!=expected_min[k]):
                raise AssertionError("adversarial deletion worst witness false")
        if z["q10_complete_ten_sign_union_probability_min"]!=str(Q_TEN):
            raise AssertionError("true full GF5 ten-sign probability drift")
        b=z["stochastic_binomial_upper_clean_fraction_using_MAX_packing"]
        if Fraction(b["numerator"],b["denominator"])!=(
                exact_binomial_tail_under_ten_sign_union(nu,1)):
            raise AssertionError("exact MINIMUM Hamming distance binomial tail corrupted")
    if full_replay:
        # Independently RERUN all finite original model geometry and
        # exact source hypergraph proof calculations from saved source.
        actual=run()
        if actual!=x:
            raise AssertionError("permanent original W32 six-ID optimum proof differs")
    return True


class PermanentW32OriginalDeletionCertificate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.saved=json.loads(CERT.read_text(encoding="utf-8"))

    def test_all_original_W32_45_source_min_delete_max_pack_and_every_Z_full_replay(self):
        self.assertTrue(check_permanent_original_W32_witness_consistency(
            self.saved,full_replay=True))

    def test_mutating_original_5_cover_fails_closed(self):
        z=copy.deepcopy(self.saved)
        z["finite_schemes"]["lex"][
            "exact_minimum_adversarial_original_ID_deletions"]["original_IDs"]=[0,1,2,3,4]
        with self.assertRaises(AssertionError):
            check_permanent_original_W32_witness_consistency(z)

    def test_fake_five_original_deleted_when_three_kills_reverse_fails_closed(self):
        z=copy.deepcopy(self.saved)
        z["finite_schemes"]["reverse-line"][
            "exact_minimum_adversarial_original_ID_deletions"]["tau"]=5
        with self.assertRaises(AssertionError):
            check_permanent_original_W32_witness_consistency(z)

    def test_corrupt_any_full_adversarial_Z_distribution_fails_closed(self):
        z=copy.deepcopy(self.saved)
        z["finite_schemes"]["lex"][
            "exhaustive_adversarial_original_ID_deletions_size_0_to_4"][4][
                "minimum_surviving_true_original_six_motifs"]=0
        with self.assertRaises(AssertionError):
            check_permanent_original_W32_witness_consistency(z)

    def test_false_geometric_allh_claim_fails_closed(self):
        z=copy.deepcopy(self.saved)
        z["this_is_NOT_a_new_universal_D6_BBo_lower"]=False
        with self.assertRaises(AssertionError):
            check_permanent_original_W32_witness_consistency(z)

    def test_corrupt_full_GF5_binomial_rational_fails_closed(self):
        z=copy.deepcopy(self.saved)
        z["finite_schemes"]["lex"][
            "stochastic_binomial_upper_clean_fraction_using_MAX_packing"
        ]["numerator"]+=1
        with self.assertRaises(AssertionError):
            check_permanent_original_W32_witness_consistency(z)


if __name__=="__main__":
    unittest.main()
