"""Permanent true ORIGINAL 24C6+72mDelta² sixth moment and 47/8 replay.

The exact full symbolic/formal ledger is recomputed independently from
both genuine W32/W34 physical priority+color selector graphs, and
full integer-safe (not float) analytic constants. This does not assume
actual numeric balanced-C6 supersaturation constants nor all-h Branch A.
"""
import copy
from fractions import Fraction
import json
from pathlib import Path
import unittest

from hyp105_original_selector_symbolic_ledger import (
    canonical_original_selector_symbolic_ledger,
)

FROZEN=Path(__file__).with_name(
    "hyp105_original_selector_symbolic_ledger_certificates.json")


def verify_true_original_selector_analytic_ledger(cert,*,replay=False):
    if (cert.get("schema")!="mathlab.hyp105.original-selector-analytic-47over8-checks.v1"
        or cert.get("root_230_status")!="OPEN_WITH_FORMAL_BLOCKER"
        or cert.get("no_new_allh_geometric_proof_claimed") is not True
        or len(cert.get("formal_parameter_pairs",()))!=4
        or len(cert.get("true_original_bipartite_source_graph_cases",()))!=6):
        raise AssertionError("analytic selector root proof scope or evidence lost")
    expected_formal=((0,1),(2,3),(8,10),(64,2**65))
    for x,(K,T) in zip(cert["formal_parameter_pairs"],expected_formal):
        if ((x.get("formal_original_core_max_conflict_degree_K"),
             int(x.get("formal_original_physical_max_degree_parameter_T","0"))
            )!=(K,T)
            or x.get("all_N_sharp_Young_trA6_upper_24C6_plus_72mDeltaSquared") is not True
            or x.get("all_N_bipartite_simple_closed6_to_C6_plus_Delta_A4_proved") is not True
            or x.get("conservative_parent_trA6_upper_24C6_plus_144mDeltaSquared") is not True
            or int(x["original_L6_tighter_24plus288T2"])!=24+288*T*T
            or int(x["original_parent_L6_24plus576T2"])!=24+576*T*T
            or int(x["exact_original_sigma2_inverse"])!=64*(K+1)**2
            or int(x["exact_original_sigma3_inverse"])!=64*27*(K+1)**3
            or Fraction(x["original_mixed_source_B_exponent"])!=Fraction(23,4)
            or Fraction(x["original_internal_blocking_exponent"])!=Fraction(47,8)
            or Fraction(x["strict_gap_to_six"])!=Fraction(1,8)
            or x.get("allh_prior_graph_CHUNK_supersaturation_requires_external_acceptance") is not True
            or x.get("this_is_NOT_new_allh_geometric_Branch_A_proof") is not True):
            raise AssertionError("false independent tight source moment bound or all-h claim")
        if (int(x["original_L4_tighter_SAFE_integer_envelope"])>
            int(x["original_L4_parent_SAFE_integer_envelope"]) or
            int(x["original_internal_I47over8_tighter_SAFE_integer_envelope"])>
            int(x["original_internal_I47over8_parent_SAFE_integer_envelope"])):
            raise AssertionError("tight original symbolic source moment no longer stronger")
    expected_graphs=((2,"lex",0,2,4,0,8),
                     (2,"lex",1,4,8,0,28),
                     (2,"reverse-line",0,3,6,0,12),
                     (2,"reverse-line",3,4,8,0,28),
                     (4,"lex",0,23,46,0,488),
                     (4,"reverse-line",1,20,40,0,266))
    for graph,expect in zip(cert["true_original_bipartite_source_graph_cases"],
                            expected_graphs):
        if ((graph.get("s"),graph.get("scheme"),graph.get("seed"),
             graph.get("selected_ORIGINAL_core_flags"),
             graph.get("selected_source_physical_edges"),
             graph.get("selected_source_physical_C6"),
             graph.get("selected_source_physical_trace_A6"))!=expect
            or graph.get("root_230_status")!="OPEN_WITH_FORMAL_BLOCKER"
            or graph.get("actual_trace6_le_24C6_plus_72mDelta2") is not True
            or graph.get("actual_trace6_le_12C6_plus_6Delta_trace4") is not True
            or graph.get("all_selected_source_physical_edges_bichromatic") is not True):
            raise AssertionError("actual original bipartite source selector graph drift")
        X=graph["selected_source_physical_trace_A6"]
        C=graph["selected_source_physical_C6"]
        Delta=graph["selected_source_physical_max_degree"]
        m=graph["selected_source_physical_edges"]
        T4=graph["selected_source_physical_trace_A4"]
        if X>12*C+6*Delta*T4 or X>24*C+72*m*Delta**2:
            raise AssertionError("original physical selected graph exact trace6 false")
    if replay:
        reconstructed=canonical_original_selector_symbolic_ledger()
        if json.loads(json.dumps(reconstructed,sort_keys=True))!=cert:
            raise AssertionError("permanent ALL source selectors + symbolic ledger not replayable")
    return True


class PermanentTighterSelectorL6Ledger(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cert=json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_original_six_actual_physical_selectors_and_full_symbolic_replay(self):
        self.assertTrue(verify_true_original_selector_analytic_ledger(
            self.cert,replay=True))

    def test_corrupted_first_original_eigenmoment_bound_fails_closed(self):
        bad=copy.deepcopy(self.cert)
        bad["true_original_bipartite_source_graph_cases"][0][
            "selected_source_physical_trace_A6"]+=1
        with self.assertRaises(AssertionError):
            verify_true_original_selector_analytic_ledger(bad)

    def test_false_tight_original_72_to_144_claim_fails_closed(self):
        bad=copy.deepcopy(self.cert)
        bad["formal_parameter_pairs"][2][
            "all_N_sharp_Young_trA6_upper_24C6_plus_72mDeltaSquared"]=False
        with self.assertRaises(AssertionError):
            verify_true_original_selector_analytic_ledger(bad)

    def test_wrong_original_source_L6_exact_finite_T_fails_closed(self):
        bad=copy.deepcopy(self.cert)
        bad["formal_parameter_pairs"][3][
            "original_L6_tighter_24plus288T2"]="777"
        with self.assertRaises(AssertionError):
            verify_true_original_selector_analytic_ledger(bad)

    def test_falsely_improved_47over8_exponent_fails_closed(self):
        bad=copy.deepcopy(self.cert)
        bad["formal_parameter_pairs"][0]["original_internal_blocking_exponent"]="23/4"
        with self.assertRaises(AssertionError):
            verify_true_original_selector_analytic_ledger(bad)

    def test_false_new_allh_branch_A_acceptance_fails_closed(self):
        bad=copy.deepcopy(self.cert)
        bad["no_new_allh_geometric_proof_claimed"]=False
        with self.assertRaises(AssertionError):
            verify_true_original_selector_analytic_ledger(bad)

    def test_arbitrary_external_supersaturation_coefficients_not_claimed(self):
        for x in self.cert["formal_parameter_pairs"]:
            self.assertTrue(
                x["allh_prior_graph_CHUNK_supersaturation_requires_external_acceptance"])
            self.assertTrue(
                x["allh_full_original_mixed_source_collinearity_assumed_not_proved_here"])


if __name__=="__main__":
    unittest.main()
