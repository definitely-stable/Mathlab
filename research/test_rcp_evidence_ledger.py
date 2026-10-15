"""RCP-001-C: adversarial cross-ledger, escrow and no-go falsifier tests."""
from __future__ import annotations

from copy import deepcopy
import hashlib
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from urllib.parse import unquote

from research.rcp.evidence_ledger import (
    RegistryError, expected_blobs, git_blob_sha, load_ledgers,
    relative_archive_path, validate_ledgers, verify_archives,
    verify_originals, index_markdown,
)

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCE = REPO_ROOT / "research/rcp/hyp105"


class EvidenceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.project_root = Path(self.temp.name)
        self.root = self.project_root / "research/rcp/hyp105"
        shutil.copytree(SOURCE, self.root)

    def modify(self, collection, name, func):
        path = self.root / collection / (name + ".json")
        obj = json.loads(path.read_text(encoding="utf-8"))
        func(obj)
        path.write_text(json.dumps(obj, indent=2), encoding="utf-8")

    def fail(self, message):
        with self.assertRaisesRegex(RegistryError, message):
            validate_ledgers(self.root)

    def test_registered_seven_claims_full_receipt_coverage(self):
        x = validate_ledgers(self.root)
        self.assertEqual(x["claim_count"], 7)
        self.assertEqual(x["evidence_count"], 5)
        self.assertEqual(x["no_go_count"], 5)
        self.assertEqual(x["archived_blob_count"], 17)
        self.assertEqual(len(x["archive_paths"]), 17)

    def test_sha_escrow_all_seventeen_real_pinned_blobs(self):
        x = verify_archives(self.root, self.project_root)
        self.assertEqual(len(x), 17)
        self.assertTrue(all(len(row["sha256"]) == 64 for row in x))
        self.assertTrue(any("capacity_results.json" in row["archive"] for row in x))

    def test_git_hash_includes_blob_header_not_raw_sha1(self):
        b = b"hello\n"
        self.assertEqual(git_blob_sha(b),
                         hashlib.sha1(b"blob 6\0" + b).hexdigest())
        self.assertNotEqual(git_blob_sha(b), hashlib.sha1(b).hexdigest())

    def test_corrupt_archived_fixture_detected(self):
        p = self.project_root / (
            "research/rcp/hyp105/archive/PR466/fixtures/capacity_results.json"
        )
        p.write_bytes(p.read_bytes() + b"\n")
        with self.assertRaisesRegex(RegistryError, "archive Git blob mismatch"):
            verify_archives(self.root, self.project_root)

    def test_missing_archived_proof_fails_closed(self):
        p = self.project_root / (
            "research/rcp/hyp105/archive/PR455/proof.md"
        )
        p.unlink()
        with self.assertRaisesRegex(RegistryError, "archive bytes unavailable"):
            verify_archives(self.root, self.project_root)

    def test_fake_claim_id_cannot_create_evidence(self):
        self.modify("evidence", "HYP105-EV-AA4N",
                    lambda e: e["claim_ids"].append("HYP105-NOT-REAL"))
        self.fail("missing or duplicate claims")

    def test_evidence_source_cannot_swap_proof(self):
        self.modify("evidence", "HYP105-EV-AA4N",
                    lambda e: e["source"].update(
                        proof_blob_sha="b" * 40))
        self.fail("differs from registered claim")

    def test_evidence_source_cannot_swap_commit(self):
        self.modify("evidence", "HYP105-EV-AA4O",
                    lambda e: e["source"].update(commit="c" * 40))
        self.fail("differs from registered claim")

    def test_missing_test_oracle_fails(self):
        self.modify("evidence", "HYP105-EV-JPKC015",
                    lambda e: e.update(artifacts=[e["artifacts"][0]]))
        self.fail("missing source/oracle/test artifacts")

    def test_fake_test_blob_rejected_by_escrow(self):
        self.modify("evidence", "HYP105-EV-AA4O",
                    lambda e: e["artifacts"][1].update(
                        git_blob_sha="f" * 40))
        validate_ledgers(self.root)
        with self.assertRaisesRegex(RegistryError, "archive Git blob mismatch"):
            verify_archives(self.root, self.project_root)

    def test_no_fake_replay_execution(self):
        self.modify("evidence", "HYP105-EV-EICE003K",
                    lambda e: e["reproduction"].update(
                        execution_status="CI_PASS"))
        self.fail("replay must be explicit")

    def test_no_promotion_ci_to_proof(self):
        self.modify("evidence", "HYP105-EV-LOCAL",
                    lambda e: e["ci"].update(status="MATHEMATICS_PROVED"))
        self.fail("CI is not a mathematical certificate")

    def test_no_go_root_must_remain_open(self):
        self.modify("no_go", "HYP105-NG-LOCAL-P3",
                    lambda n: n.update(root_status="PROVED_A"))
        self.fail("may not silently close root")

    def test_no_go_unrelated_evidence_fails(self):
        self.modify("no_go", "HYP105-NG-LOCAL-P3",
                    lambda n: n.update(evidence_ids=["HYP105-EV-AA4O"]))
        self.fail("evidence unrelated")

    def test_no_go_requires_precise_not_refuted_scope(self):
        self.modify("no_go", "HYP105-NG-ANCHOR-MARGINAL",
                    lambda n: n.update(does_not_refute=[]))
        self.fail("must explicitly delimit")

    def test_no_go_reopen_conditions_required(self):
        self.modify("no_go", "HYP105-NG-QUENCHED-POINTWISE",
                    lambda n: n.update(reopen_only_if=""))
        self.fail("missing reopen_only_if")

    def test_no_go_legacy_decision_link_required(self):
        self.modify("no_go", "HYP105-NG-SWAP-OPTIMUM",
                    lambda n: n.update(prior_registry_ref="removed"))
        self.fail("existing no-rediscovery registry")

    def test_broken_replay_commit_rejected(self):
        self.modify("evidence", "HYP105-EV-AA4N",
                    lambda e: e["reproduction"].update(
                        checkout_commit="0" * 40))
        self.fail("replay must be explicit")

    def test_deterministic_paths_and_index(self):
        rows = expected_blobs(self.root)
        self.assertEqual(len(rows), 17)
        self.assertEqual(rows, sorted(rows))
        report = verify_archives(self.root, self.project_root)
        _, ng = load_ledgers(self.root)
        assert set(x["id"] for x in ng) == {
            "HYP105-NG-LOCAL-P3", "HYP105-NG-ANCHOR-MARGINAL",
            "HYP105-NG-QUENCHED-POINTWISE", "HYP105-NG-SWAP-OPTIMUM",
            "HYP105-NG-ENSEMBLE-WORST"}
        md = index_markdown(report, sorted(ng, key=lambda x: x["id"]),
                            validate_ledgers(self.root))
        self.assertIn("Does NOT refute", md)
        self.assertIn("Root #230: OPEN_WITH_FORMAL_BLOCKER", md)

    def test_remote_pinned_source_mock_same_bytes(self):
        expected = {}
        for rel, _, commit, source in expected_blobs(self.root):
            expected[(commit, source)] = (
                self.project_root / rel).read_bytes()
        def fake_get(url):
            before, commit = url.split("?ref=", 1)
            source = unquote(before.split("/contents/", 1)[1])
            return expected[(commit, source)]
        self.assertEqual(len(verify_originals(self.root, get=fake_get)), 17)

    def test_remote_corruption_is_not_success(self):
        with self.assertRaisesRegex(RegistryError, "remote pinned origin"):
            verify_originals(self.root, get=lambda url: b"wrong")

    def test_fixture_escrow_is_not_full_global_counterexample(self):
        _, no_gos = load_ledgers(self.root)
        local = next(n for n in no_gos if n["id"] == "HYP105-NG-LOCAL-P3")
        self.assertEqual(local["kind"], "SCOPED_COUNTEREXAMPLE")
        self.assertEqual(local["root_status"], "OPEN_WITH_FORMAL_BLOCKER")
        self.assertIn("sparse", local["witness_scope"])
        self.assertTrue(any("full" in x.lower() for x in
                            local["does_not_refute"]))

if __name__ == "__main__":
    unittest.main()
