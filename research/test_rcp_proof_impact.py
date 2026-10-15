"""RCP-001-E: independent impact, compatibility, and structured Markdown tests."""
from __future__ import annotations
from copy import deepcopy
import json
from pathlib import Path
import tempfile
import unittest

from research.rcp.claim_registry import RegistryError
from research.rcp.context_builder import digest, seal_snapshot
from research.rcp.proof_impact import (
    proof_graph, descendants, compatibility_review, impact_report, md, main as impact_main,
)
from research.rcp.structured_docs import render_all, read_formulas, main as docs_main
from research.test_rcp_context import build, altered

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "research/rcp/hyp105"
QID = "HYP105-AA4N-QUENCHED-IDENTITY"
LOWER = "HYP105-AA4N-QUENCHED-LOWER"
O = "HYP105-AA4O-QUINTIC-IDENTITY"
SWAP = "HYP105-AA4O-SWAP-IDENTITY"


def find(items, id):
    return next(x for x in items if x["id"] == id)


def rehash_claim(claim):
    claim["fingerprint"] = digest({k: v for k, v in claim.items()
                                  if k not in ("fingerprint", "evidence_ids",
                                               "no_go_ids", "proof_url",
                                               "source_pr_current")})


class ImpactTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = build()

    def test_exact_pilot_dependencies(self):
        _, children, edges = proof_graph(self.base)
        self.assertEqual(len(edges), 3)
        self.assertEqual(descendants(children, QID),
                         sorted([LOWER, O, SWAP]))
        self.assertEqual(descendants(children, O), [SWAP])

    def test_empty_baseline_has_no_fabricated_change(self):
        r = impact_report(self.base)
        self.assertEqual(len(r["possibly_impacted_claim_ids"]), 0)
        self.assertIsNone(r["previous_snapshot_sha256"])
        self.assertIn("REGISTERED_CLAIMS_ONLY", r["coverage"])
        self.assertEqual(r["diagnosed_contradictions"],
                         "NONE_ESTABLISHED_AUTOMATICALLY")

    def test_parent_claim_change_marks_all_transitive_dependents(self):
        def change(s):
            c = find(s["research"]["claims"], QID)
            c["statement"] += " audited future revision"
            rehash_claim(c)
        x = altered(self.base, change)
        out = impact_report(x, self.base)
        self.assertEqual(out["possibly_impacted_claim_ids"],
                         sorted([QID, LOWER, O, SWAP]))
        seed = next(z for z in out["transitive_impact"]
                    if z["seed_claim"] == QID)
        self.assertEqual(seed["transitive_dependents"], sorted([LOWER, O, SWAP]))

    def test_model_change_targets_model_users_and_downstream(self):
        def change(s):
            s["research"]["models"]["MODEL-BA-INTERNAL-CHARGE"][
                "definition"] += " new condition"
        r = impact_report(altered(self.base, change), self.base)
        self.assertIn(QID, r["possibly_impacted_claim_ids"])
        self.assertIn(SWAP, r["possibly_impacted_claim_ids"])
        self.assertEqual(r["diagnosed_contradictions"],
                         "NONE_ESTABLISHED_AUTOMATICALLY")

    def test_no_go_revision_impacts_related_claims(self):
        def change(s):
            n = find(s["research"]["no_go"], "HYP105-NG-QUENCHED-POINTWISE")
            n["rejected_inference"] += " clarified"
            n["fingerprint"] = digest(n)
        r = impact_report(altered(self.base, change), self.base)
        self.assertIn(QID, r["possibly_impacted_claim_ids"])
        self.assertIn(LOWER, r["possibly_impacted_claim_ids"])
        self.assertIn(SWAP, r["possibly_impacted_claim_ids"])

    def test_receipt_change_impacts_both_related_claims(self):
        def change(s):
            e = find(s["research"]["evidence"], "HYP105-EV-AA4N")
            e["limitations"].append("future review needed")
            e["fingerprint"] = digest(e)
        r = impact_report(altered(self.base, change), self.base)
        self.assertIn(QID, r["possibly_impacted_claim_ids"])
        self.assertIn(LOWER, r["possibly_impacted_claim_ids"])

    def test_escrow_changed_triggers_claim_associated_with_pr(self):
        def change(s):
            e = next(x for x in s["research"]["escrow"]
                     if "PR470/" in x["archive"])
            e["sha256"] = "0" * 64
        r = impact_report(altered(self.base, change), self.base)
        self.assertIn(QID, r["possibly_impacted_claim_ids"])
        self.assertIn(LOWER, r["possibly_impacted_claim_ids"])

    def test_source_head_advance_is_operational_not_math_claim_change(self):
        def change(s):
            c = find(s["research"]["claims"], O)
            c["source_pr_current"]["head"] = "f" * 40
            pr = next(x for x in s["inventory"]["open_prs"]
                      if x["number"] == 471)
            pr["head_sha"] = "f" * 40
        r = impact_report(altered(self.base, change), self.base)
        self.assertEqual(r["possibly_impacted_claim_ids"], [])
        self.assertGreater(r["observed_operational_events"], 0)

    def test_scope_difference_is_a_review_not_a_contradiction(self):
        warnings = compatibility_review(self.base)
        self.assertTrue(any(w["kind"] ==
                            "EXPECTATION_TO_DETERMINISTIC_BRIDGE_REVIEW"
                            for w in warnings))
        self.assertTrue(all(w["decision"].startswith("UNREVIEWED")
                            for w in warnings))

    def test_missing_dependency_fails_closed(self):
        s = deepcopy(self.base)
        find(s["research"]["claims"], SWAP)["depends_on_claims"] = ["MISSING"]
        with self.assertRaisesRegex(RegistryError, "missing claim dependency"):
            proof_graph(s)

    def test_cycle_fails_closed(self):
        s = deepcopy(self.base)
        find(s["research"]["claims"], QID)["depends_on_claims"] = [SWAP]
        with self.assertRaisesRegex(RegistryError, "dependency cycle"):
            proof_graph(s)

    def test_unknown_model_fails_closed(self):
        s = deepcopy(self.base)
        find(s["research"]["claims"], O)["model_ids"].append("FAKE-MODEL")
        with self.assertRaisesRegex(RegistryError, "unknown mathematical model"):
            proof_graph(s)

    def test_new_claim_add_is_candidate_only(self):
        def change(s):
            c = deepcopy(find(s["research"]["claims"], LOWER))
            c["id"] = "HYP105-NEW-TEST"
            c["depends_on_claims"] = [QID]
            c["fingerprint"] = digest(c)
            s["research"]["claims"].append(c)
        r = impact_report(altered(self.base, change), self.base)
        self.assertIn("HYP105-NEW-TEST", r["possibly_impacted_claim_ids"])
        self.assertEqual(r["acceptance"],
                         "CANDIDATE_REVIEW_NOT_MATHEMATICAL_CONTRADICTION")

    def test_model_change_does_not_erase_old_dependency_edges(self):
        def change(s):
            find(s["research"]["claims"], O)["depends_on_claims"] = []
            rehash_claim(find(s["research"]["claims"], O))
        r = impact_report(altered(self.base, change), self.base)
        seed = next(v for v in r["transitive_impact"] if v["seed_claim"] == O)
        self.assertIn(SWAP, seed["transitive_dependents"])

    def test_only_timestamp_changed_zero_research_impact(self):
        s = altered(self.base, lambda d: d.update(
            observed_at_utc="2026-10-15T10:00:00Z"))
        out = impact_report(s, self.base)
        self.assertEqual(out["possibly_impacted_claim_ids"], [])

    def test_impact_markdown_has_explicit_caveats(self):
        report = impact_report(self.base)
        markdown = md(report)
        self.assertIn("not automatically", markdown.lower())
        self.assertIn("Registered dependency DAG", markdown)
        self.assertIn("compatibility", markdown.lower())

    def test_cli_two_snapshots_writes_json_and_markdown(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            first, later, dest = p/"a.json", p/"b.json", p/"output"
            first.write_text(json.dumps(self.base), encoding="utf-8")
            later.write_text(json.dumps(self.base), encoding="utf-8")
            self.assertEqual(impact_main(["--snapshot", str(later),
                                          "--previous", str(first),
                                          "--output", str(dest)]), 0)
            x = json.loads((dest/"impact.json").read_text(encoding="utf-8"))
            self.assertEqual(x["possibly_impacted_claim_ids"], [])
            self.assertTrue((dest/"impact.md").is_file())


class StructuredDocsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.docs = render_all(REGISTRY)

    def test_all_five_structured_documents_rendered(self):
        self.assertEqual(set(self.docs), {
            "RESULTS.md", "FORMULAS.md", "PROOF-GRAPH.md",
            "PROTOCOLS.md", "RESEARCH-MATRIX.md"})

    def test_seven_explicit_scoped_original_formulas(self):
        x = read_formulas(REGISTRY, {c["id"] for c in
                          __import__("research.rcp.claim_registry",
                                     fromlist=["read_registry"]).read_registry(REGISTRY)[1]})
        self.assertEqual(len(x), 7)
        self.assertIn("\\mathbb E_f", self.docs["FORMULAS.md"])
        self.assertIn("\\chi_B", self.docs["FORMULAS.md"])
        self.assertIn("\\frac{16}{3}", self.docs["FORMULAS.md"])

    def test_all_results_have_exact_pinned_proof_source(self):
        text = self.docs["RESULTS.md"]
        for pr in (455, 466, 469, 470, 471):
            self.assertIn("PR #" + str(pr), text)
        self.assertIn("DOCUMENTED_IN_DRAFT", text)
        self.assertIn("Ordered quantifiers", text)

    def test_protocols_do_not_assert_automated_science_review(self):
        txt = self.docs["PROTOCOLS.md"]
        self.assertIn("mathematical review", txt)
        self.assertIn("No averaging-to-adversarial-minimum", txt)
        self.assertIn("GitHub", txt)

    def test_no_go_matrix_covers_all_five(self):
        txt = self.docs["RESEARCH-MATRIX.md"]
        self.assertEqual(txt.count("| HYP105-NG-"), 5)
        self.assertIn("Revisit only if", txt)

    def test_formula_unknown_claim_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            import shutil
            shutil.copytree(REGISTRY, target/"reg")
            p = target/"reg/formulas.json"
            data = json.loads(p.read_text())
            data["formulas"][0]["claim_ids"] = ["BAD-NONEXISTENT"]
            p.write_text(json.dumps(data), encoding="utf-8")
            with self.assertRaisesRegex(RegistryError, "unknown scoped claim"):
                render_all(target/"reg")

    def test_duplicate_formula_id_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            import shutil
            shutil.copytree(REGISTRY, target/"reg")
            p = target/"reg/formulas.json"
            data = json.loads(p.read_text())
            data["formulas"][1]["id"] = data["formulas"][0]["id"]
            p.write_text(json.dumps(data), encoding="utf-8")
            with self.assertRaisesRegex(RegistryError, "duplicate/invalid formula"):
                render_all(target/"reg")

    def test_document_generation_and_stale_file_detection(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)/"docs"
            self.assertEqual(docs_main(["--destination", str(target),
                                        "--write"]), 0)
            self.assertEqual(docs_main(["--destination", str(target),
                                        "--check"]), 0)
            p = target/"FORMULAS.md"
            p.write_text(p.read_text() + "\nFAKE FORMULA", encoding="utf-8")
            with self.assertRaisesRegex(RegistryError, "stale structured Markdown"):
                docs_main(["--destination", str(target), "--check"])


if __name__ == "__main__":
    unittest.main()
