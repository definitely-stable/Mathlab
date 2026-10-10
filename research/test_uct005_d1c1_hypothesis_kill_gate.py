"""D1-C1 independently check scoped falsification, physical ledgers, proof gates."""
from copy import deepcopy
import unittest

from uct005_d1c1_hypothesis_kill_gate import (
    EXPECTED, HonestFenwick, load_matrix, validate_matrix,
    fenwick_witness, observation_witness, one_pass_witness,
    changed_between_scans_witness, duplicate_pin_witness,
    failed_stage_witness, counting_witness, report,
)


class HypothesisGateTests(unittest.TestCase):
    def test_frozen_candidate_matrix_preserves_all_unknown_F1_axes(self):
        data=load_matrix()
        self.assertEqual(len(data["candidates"]),8)
        self.assertEqual(data["root_status"],"OPEN_UNPROVED")
        self.assertEqual([c["id"] for c in data["candidates"]],
                         [c[0] for c in EXPECTED])
        for candidate in data["candidates"]:
            self.assertIn(candidate["status"],{
                "REJECTED_SCOPED_F0","REJECTED_SCOPED_OBSERVATION",
                "REJECTED_SCOPED_F1_UPPER","STOP_NOVELTY_CLASSICAL",
                "OPEN_UNFORMULATED",
            })
            self.assertTrue(candidate["unpriced_f1_axes"])
            self.assertIsNot(candidate["novel_joint_f1_lower"],True)
        for source in data["primary_source_transfer"]:
            self.assertEqual(source["status"],"REDUCTION_REQUIRED")
            self.assertFalse(source["full_text_proof_transfer"])

    def test_frozen_schema_kills_false_promotion_missing_axes_bad_sources(self):
        good=load_matrix()
        def corrupt(f):
            tmp=deepcopy(good)
            f(tmp)
            with self.assertRaises(ValueError):
                validate_matrix(tmp)
        corrupt(lambda a:a.update(root_status="PROVED"))
        corrupt(lambda a:a["full_f1_axes"].remove("C_reader"))
        corrupt(lambda a:a["primary_source_transfer"][0].update(
            full_text_proof_transfer=True))
        corrupt(lambda a:a["primary_source_transfer"][0].update(
            status="APPLICABLE"))
        corrupt(lambda a:a["candidates"][0].update(status="PROVED_ROOT"))
        corrupt(lambda a:a["candidates"][0].update(
            status="REJECTED_SCOPED_F1_UPPER"))
        corrupt(lambda a:a["candidates"][0].update(
            unpriced_f1_axes=[]))
        corrupt(lambda a:a["candidates"][1].update(
            falsifier="unverified generic claim"))
        corrupt(lambda a:a["candidates"][1].update(
            novel_joint_f1_lower=True))
        corrupt(lambda a:a["candidates"][-1].update(
            novel_joint_f1_lower=False))
        corrupt(lambda a:a["candidates"][3].update(
            novel_joint_f1_lower=None))

    def test_actual_fenwick_bit_cell_bounds_not_mislabeled_as_authenticated_F1(self):
        witness=fenwick_witness()
        self.assertEqual(witness["n"],4096)
        self.assertEqual(witness["remote_raw_plus_tree_bit_cells"],8192)
        self.assertEqual(witness["worst_case_analytic_write_upper"],14)
        self.assertEqual(witness["worst_case_analytic_query_upper"],24)
        self.assertEqual(witness["analytic_product_upper"],336)
        self.assertLess(witness["analytic_product_upper"],witness["n"])
        self.assertFalse(witness["f1_authenticated_protocol"])
        for n in (2,4,8,16):
            m=HonestFenwick(n)
            bits=[0]*n
            for i in range(n):
                a,w=m.set(i,1)
                bits[i]=1
                self.assertEqual(a,1)
                self.assertGreater(w,0)
                for lo in range(n):
                    for hi in range(lo+1,n+1):
                        got,reads=m.parity(lo,hi)
                        self.assertEqual(got,sum(bits[lo:hi])&1)
                        self.assertLessEqual(reads,2*(n.bit_length()-1))
            self.assertEqual(m.set(0,1),(1,0))  # no-op also read charged
        with self.assertRaises(ValueError):
            HonestFenwick(3)
        with self.assertRaises(ValueError):
            HonestFenwick(2).parity(0,3)

    def test_real_two_PIN_observation_not_independent_and_author_receipts_differ(self):
        obs=observation_witness()
        self.assertEqual(obs["distinct_answer_tuples"],3072)
        self.assertEqual(obs["exact_minimum_fixed_bits"],12)
        self.assertEqual(obs["naive_independent_bits"],15)
        self.assertEqual(obs["distinct_labeled_SET_trajectories_n4_H3"],8192)
        self.assertEqual(obs["distinct_bitmap_paths_n4_H3"],2000)
        self.assertIsNone(obs["signed_author_receipts_and_physical_pages"])

    def test_real_authenticated_PIN_models_falsify_F3C_second_scan_necessity(self):
        q=one_pass_witness()
        self.assertEqual(q["P"],1)
        self.assertEqual(q["M"],5)
        self.assertEqual(q["F2_online_read_pages"],55)
        self.assertEqual(q["F3C_online_read_pages"],35)
        self.assertEqual(q["F3C_preauth_full_page_writes"],20)
        self.assertFalse(q["complete_crash_durability_or_SHA_reduction"])

    def test_F2_second_pass_changed_page_is_paid_on_abort(self):
        z=changed_between_scans_witness()
        self.assertEqual(z["F2_aborted_stage_page_writes"],5)
        self.assertEqual(z["F2_cleanup_drop_calls"],5)
        self.assertEqual(z["trusted_publications"],0)

    def test_two_readers_same_epoch_have_one_retained_snapshot_not_two(self):
        z=duplicate_pin_witness()
        self.assertEqual(z["PIN_entries"],2)
        self.assertEqual(z["distinct_retained_PIN_epochs"],1)
        self.assertGreater(z["offline_authenticated_audit_reads"],0)
        self.assertTrue(z["ideal_authority_and_local_PIN_roots_are_paid"])

    def test_invalid_old_SHA_falsifies_all_axis_onepass_dominance(self):
        z=failed_stage_witness()
        self.assertEqual(z["M"],5)
        self.assertEqual(z["F2_stage_page_writes"],0)
        self.assertEqual(z["F3C_stage_page_writes"],5)
        self.assertEqual(z["F3C_cleanup_drop_address_bytes"],40)
        self.assertIsNone(z["F2_and_F3C_full_system_Pareto"])

    def test_deferred_output_is_elementary_capacity_not_novel_UCT(self):
        z=counting_witness()
        self.assertEqual(z["minimal_post_auth_read_pages_without_stage"],8)
        self.assertEqual(z["minimal_post_auth_reads_with_eight_staged_pages"],0)
        self.assertTrue(z["only_classical_pigeonhole_injection"])
        self.assertFalse(z["novel_UCT_root"])

    def test_report_is_scoped_and_unresolved_candidate_stays_unknown(self):
        result=report()
        self.assertEqual(result["root_novelty"],"OPEN_UNPROVED")
        self.assertFalse(result["strict_novel_joint_lower_bound_proved"])
        self.assertFalse(result["primary_theorem_full_text_transfer"])
        self.assertEqual(len(result["candidates"]),8)
        for row in result["candidates"]:
            self.assertEqual(row["root_novelty"],"OPEN_UNPROVED")
            self.assertTrue(all(x is None for x in
                                row["unpriced_f1_axes"].values()))
        last=result["candidates"][-1]
        self.assertEqual(last["decision"],"OPEN_UNFORMULATED")
        self.assertIsNone(last["actual_finite_witness"]["quantified_joint_formula"])


if __name__=="__main__":
    unittest.main()
