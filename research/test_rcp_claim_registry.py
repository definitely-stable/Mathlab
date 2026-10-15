"""Independent adversarial checks for the RCP-001-B claim registry."""
from __future__ import annotations
from copy import deepcopy
import json
from pathlib import Path
import shutil
import tempfile
import unittest

from research.rcp.claim_registry import (
    RegistryError, read_registry, validate_registry, verify_pinned_sources
)

SOURCE = Path(__file__).parent / "rcp" / "hyp105"
J = "HYP105-JPKC015-D6-ENSEMBLE"
N_ID = "HYP105-AA4N-QUENCHED-IDENTITY"
N_LOW = "HYP105-AA4N-QUENCHED-LOWER"
O = "HYP105-AA4O-QUINTIC-IDENTITY"
SWAP = "HYP105-AA4O-SWAP-IDENTITY"


class RegistryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "hyp105"
        shutil.copytree(SOURCE, self.root)

    def change(self, cid, operation):
        path = self.root / "claims" / (cid + ".json")
        item = json.loads(path.read_text(encoding="utf-8"))
        operation(item)
        path.write_text(json.dumps(item, indent=2), encoding="utf-8")

    def assert_invalid(self, needle):
        with self.assertRaisesRegex(RegistryError, needle):
            validate_registry(self.root)

    def test_seven_referenced_draft_claims_metadata_valid(self):
        result = validate_registry(self.root)
        self.assertGreaterEqual(result["claims"], 7)
        self.assertEqual(result["models"], 8)
        self.assertEqual(result["status"],
                         "METADATA_VALIDATED_NOT_MATHEMATICALLY_VERIFIED")

    def test_conditional_mean_cannot_drop_expectation(self):
        self.change(N_LOW, lambda c: c["quantifiers"].pop())
        self.assert_invalid("conditional expectation")

    def test_conditional_mean_cannot_swap_sampling_and_forall(self):
        self.change(N_LOW, lambda c: c["quantifiers"].reverse())
        self.assert_invalid("genuine s=2\\^h domain")

    def test_ensemble_cannot_be_mislabeled_worst_case(self):
        self.change(J, lambda c: c.update(mode="DETERMINISTIC_BOUND"))
        self.assert_invalid("cannot hide sampling")

    def test_fake_proof_status_from_ci_rejected(self):
        self.change(O, lambda c: c.update(mathematical_status="REVIEWED"))
        self.assert_invalid("cannot promote claim")

    def test_forged_root_proof_rejected(self):
        self.change(N_LOW, lambda c: c.update(root_impact="ROOT_A_PROVED"))
        self.assert_invalid("root proof cannot be inferred from CI")

    def test_missing_proof_blob_hash_rejected(self):
        self.change(O, lambda c: c["source"].update(proof_blob_sha="missing"))
        self.assert_invalid("missing pinned proof blob")

    def test_parent_path_traversal_rejected(self):
        self.change(O, lambda c: c["source"].update(proof_path=
                   "docs/research/../../unsafe.md"))
        self.assert_invalid("unsafe/missing proof path")

    def test_missing_model_rejected(self):
        self.change(J, lambda c: c["model_ids"].append("MODEL-FAKE"))
        self.assert_invalid("unknown/duplicate model")

    def test_omitted_global_map_model_rejected(self):
        self.change(J, lambda c: c["model_ids"].remove(
                    "MODEL-TYPED-GLOBAL-INJECTION"))
        self.assert_invalid("original geometry or global injection")

    def test_unknown_claim_dependency_rejected(self):
        self.change(SWAP, lambda c: c["depends_on_claims"].append("HYP105-UNKNOWN"))
        self.assert_invalid("unknown claim")

    def test_dependency_cycle_rejected(self):
        self.change(N_ID, lambda c: c["depends_on_claims"].append(SWAP))
        self.assert_invalid("dependency cycle")

    def test_self_dependency_rejected(self):
        self.change(O, lambda c: c["depends_on_claims"].append(O))
        self.assert_invalid("self-dependency")

    def test_renamed_claim_file_rejected(self):
        src = self.root / "claims" / (J + ".json")
        src.rename(self.root / "claims" / "HYP105-RENAMED.json")
        self.assert_invalid("filename must equal immutable ID")

    def test_model_duplicate_rejected(self):
        path = self.root / "models.json"
        doc = json.loads(path.read_text(encoding="utf-8"))
        doc["models"].append(deepcopy(doc["models"][0]))
        path.write_text(json.dumps(doc), encoding="utf-8")
        self.assert_invalid("duplicate model id")

    def test_nogo_limitations_cannot_be_empty(self):
        self.change(O, lambda c: c.update(limitations=[]))
        self.assert_invalid("missing non-implication limitations")

    def test_source_shas_pinned_and_unique(self):
        _, claims = read_registry(self.root)
        sources = {c["source"]["commit"] for c in claims}
        self.assertGreaterEqual(len(sources), 5)
        self.assertTrue(all(len(s) == 40 for s in sources))
        self.assertEqual(sum(1 for c in claims if c["source"]["pr"] == 470
                             and c["mode"] == "CONDITIONAL_EXPECTATION"), 2)
        self.assertGreaterEqual(sum(1 for c in claims if
                                    c["mode"] == "CONDITIONAL_EXPECTATION"), 2)

    def test_verified_source_blobs_match_pinned_hash(self):
        _, claims = read_registry(self.root)
        expected = {(c["source"]["commit"], c["source"]["proof_path"]):
                    c["source"]["proof_blob_sha"] for c in claims}
        def mock_get(url):
            part, sha = url.split("?ref=")
            path = part.split("/contents/", 1)[1]
            blob = expected[(sha, path)]
            return {"type": "file", "sha": blob}
        self.assertEqual(len(verify_pinned_sources(self.root, get=mock_get)), len(expected))

    def test_source_hash_mismatch_fails_closed(self):
        with self.assertRaisesRegex(RegistryError, "pinned source mismatch"):
            verify_pinned_sources(self.root, get=lambda url: {
                "type": "file", "sha": "0" * 40
            })

    def test_source_absence_fails_closed(self):
        with self.assertRaisesRegex(RegistryError, "pinned source mismatch"):
            verify_pinned_sources(self.root, get=lambda url: {})

    def test_local_counterexample_is_not_root_counterfamily(self):
        models, claims = read_registry(self.root)
        local = next(x for x in claims if x["mode"] == "LOCAL_CONSTRUCTION")
        self.assertIn("MODEL-SELECTED-LOCAL-PATTERN", local["model_ids"])
        self.assertEqual(local["root_impact"], "ROOT_BRANCHES_OPEN")
        self.assertEqual([q["op"] for q in local["quantifiers"]],
                         ["forall", "exists"])
        self.assertTrue(any("full-model" in x for x in local["limitations"]))


if __name__ == "__main__":
    unittest.main()
