"""HYP-105 AA4-REFGATE: mutation-based scope/proof DAG stress tests."""
from dataclasses import replace
from fractions import Fraction
from pathlib import Path
from itertools import combinations
from math import comb
import json
import unittest

from hyp105_branch_a_external_referee_proof_obligation_gate import (
    CLAIMS,TRANSFERS,BRIDGE_IDS,FORBIDDEN_PROMOTIONS,
    validate_manifest,validate_scope_transfers,audit_repository,json_report,
)
from hyp105_original_selector_sixwalk_joint_root_gate import (
    exact_root_ablation_grid, EPSILON, HEAVY_BETA,
)
from hyp105_full_physical_degree_tail import genuine_source


REPO=Path(__file__).resolve().parents[1]


class OriginalHYP105ExternalReviewerGate(unittest.TestCase):
    def test_all_13_original_source_claim_documents_have_exact_scoped_evidence(self):
        got=audit_repository(REPO)
        self.assertEqual(got["source_objects_scoped"],13)
        self.assertEqual(len(got["topological_dependency_order"]),13)
        self.assertEqual(got["scientific_acceptance"],"OPEN_WITH_FORMAL_BLOCKER")
        self.assertFalse(got["external_qualified_review_completed"])
        self.assertFalse(got["real_published_graph_constants_numeric_available"])
        self.assertFalse(got["formal_proof_assistant_verification"])
        self.assertEqual({x["claim"] for x in got["claim_documents"]},
                         {x.id for x in CLAIMS})
        self.assertEqual(
            sum(x["source_markers_verified"] for x in got["claim_documents"]),
            sum(len(x.must_contain) for x in CLAIMS))
        self.assertEqual(next(x for x in got["claim_documents"] if x["claim"]=="SS6")[
            "evidence_type"],"EXTERNAL_PUBLISHED_EXISTENTIAL_CONSTANTS")
        order=list(got["topological_dependency_order"])
        for claim in CLAIMS:
            for parent in claim.needs:
                self.assertLess(order.index(parent),order.index(claim.id))
        self.assertLess(order.index("ROOT"),order.index("GF5"))
        payload=json.loads(json_report(REPO))
        self.assertEqual(payload["scientific_acceptance"],
                         got["scientific_acceptance"])
        self.assertTrue(payload["human_referee_needed"])

    def test_external_primary_theorem_is_scoped_to_ordinary_c6_and_unknown_constants(self):
        claim=next(x for x in CLAIMS if x.id=="SS6")
        src=(REPO/claim.document).read_text(encoding="utf8").casefold()
        self.assertIn("10.1017/s0963548320000206",src)
        self.assertIn("existential",src)
        self.assertIn("ordinary",src)
        self.assertIn("c6",src)
        self.assertNotIn("C_graph=1 is proved by jiang".casefold(),src)

    def test_every_required_original_full_core_gf5_transfer_is_indispensable(self):
        for b in BRIDGE_IDS:
            with self.subTest(removed=b):
                with self.assertRaises(ValueError):
                    validate_scope_transfers(set(BRIDGE_IDS)-{b})
        good=validate_scope_transfers()
        self.assertEqual(good["mandatory_source_transfers"],8)
        for invalid in FORBIDDEN_PROMOTIONS:
            with self.subTest(illegal=invalid):
                with self.assertRaises(ValueError):
                    validate_scope_transfers(set(BRIDGE_IDS)|{invalid})

    def test_manipulated_scientific_dependency_graph_rejected_not_cosmetically_passed(self):
        validate_manifest()
        root=next(c for c in CLAIMS if c.id=="ROOT")
        gf5=next(c for c in CLAIMS if c.id=="GF5")
        ss6=next(c for c in CLAIMS if c.id=="SS6")
        cases=[
            tuple(c for c in CLAIMS if c.id!="ROOT"),
            CLAIMS+(root,),
            tuple(replace(c,needs=tuple(x for x in c.needs if x!="SS6"))
                  if c.id=="ROOT" else c for c in CLAIMS),
            tuple(replace(c,needs=("ROOT",)) if c.id=="GQ" else c
                  for c in CLAIMS),
            tuple(replace(c,source="ANY_GRAPH_AND_ANY_H") if c.id=="ROOT"
                  else c for c in CLAIMS),
            tuple(replace(c,document="../fake-proof.md") if c.id=="D6"
                  else c for c in CLAIMS),
            tuple(replace(c,evidence_type="NUMERIC_PUBLISHED_GRAPH_CONSTANTS")
                  if c.id=="SS6" else c for c in CLAIMS),
        ]
        for fake in cases:
            with self.subTest(fake_len=len(fake)):
                with self.assertRaises(ValueError):
                    validate_manifest(fake)

    def test_forged_transfer_drop_source_and_duplicate_bridge_rejected(self):
        with self.assertRaises(ValueError):
            validate_manifest(CLAIMS,TRANSFERS[:-1])
        with self.assertRaises(ValueError):
            validate_manifest(CLAIMS,TRANSFERS+(TRANSFERS[0],))
        with self.assertRaises(ValueError):
            validate_manifest(CLAIMS,TRANSFERS[:-1]+(
                ("BAD_SOURCE","GF5",BRIDGE_IDS[-1]),))

    def test_actual_W32_W34_original_incidence_requires_both_diagonal_edges(self):
        for power in (1,2):
            s,V,flags=genuine_source(power)
            self.assertEqual(len(flags),(s+1)*V)
            self.assertEqual(len(set(flags)),len(flags))
            self.assertEqual(V,(s+1)*(s*s+1))
            points=[0]*V
            lines=[0]*V
            for p,l in flags:
                points[p]+=1
                lines[l]+=1
            self.assertEqual(set(points),{s+1})
            self.assertEqual(set(lines),{s+1})
            self.assertEqual(2*len(flags),2*(s+1)**2*(s*s+1))
            a=2
            while comb(a,2)<V:a+=1
            self.assertGreaterEqual(comb(a,2),V)
            self.assertLess(comb(a-1,2),V)

    def test_real_merged_root_gate_is_still_conditional_on_unknown_SS6_constants(self):
        z=exact_root_ablation_grid(1,1)
        self.assertEqual(z["gain_in_dyadic_h"],18)
        self.assertEqual(z["same_original_heavy_T"],39352331442479)
        self.assertEqual(
            [z["four_matched_runs"][k]["joint_certified_dyadic_h"] for k in
             ("baseline_702","sixwalk_only_703",
              "selector_only_679","joint_679_703")],
            [684,682,668,666])
        self.assertEqual(z["same_root_delta"],
                         min(Fraction(1,8),
                             (HEAVY_BETA/32)**6))
        self.assertTrue(z["no_genuine_numeric_C_graph_c_graph_claim"])
        self.assertEqual(audit_repository(REPO)["scientific_acceptance"],
                         "OPEN_WITH_FORMAL_BLOCKER")

    def test_proof_dossier_genuine_external_review_question_bank_is_nonempty(self):
        dossier=(REPO/"docs/research/HYP-105-BRANCH-A-EXTERNAL-REFEREE-DOSSIER.md"
                 ).read_text(encoding="utf-8")
        for label in (
            "R1 — Original source provenance",
            "R2 — Heavy branch",
            "R3 — Core pruning",
            "R4 — Selector and moments",
            "R5 — FULL/CORE mixed blockers",
            "R6 — Original six-ID inverse",
            "R7 — Signed GF(5)",
            "R8 — Global quantifiers",
            "ACCEPTANCE: OPEN_WITH_FORMAL_BLOCKER",
            "C_graph", "c_graph", "Jiang", "Yepremyan",
            "No fabricated numerical h0",
            "How to reproduce",
        ):
            self.assertIn(label,dossier)
        self.assertIn("DO NOT merge",dossier)


if __name__=="__main__":
    unittest.main()
