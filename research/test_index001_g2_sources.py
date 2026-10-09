"""INDEX-001 G2-A original compaction publications and version-coalescing tests."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "docs/research/INDEX-001-G2-A-PAGE-COST-AND-PRIOR-ART.md"
JSON = ROOT / "docs/research/catalog/literature.json"

EXPECTED = {
    "LIT-183": ("doi:10.1007/s00224-025-10229-8",
                "(Worst-case) Optimal Adaptive Dynamic Bitvectors"),
    "LIT-184": ("doi:10.1016/j.future.2026.108425",
                "C2LSM: A configuration paradigm for efficient compaction in LSM-tree-based key-value stores"),
    "LIT-185": ("doi:10.14778/3796195.3796208",
                "ArceKV: Towards Workload-driven LSM-compactions for Key-Value Store Under Dynamic Workloads"),
    "LIT-186": ("doi:10.1109/ICDE65706.2026.00194",
                "RangeReduce: Query-Driven LSM Compactions"),
}


class G2ASources(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(JSON.read_text(encoding="utf-8"))
        cls.by = {e["id"]: e for e in cls.data["entries"]}

    def test_four_new_canonical_primary_identities_and_committed_note(self):
        self.assertEqual(len(self.by), 205)
        for key, (ident, title) in EXPECTED.items():
            e = self.by[key]
            self.assertEqual(e["identity"], ident)
            self.assertEqual(e["title"], title)
            self.assertEqual(e["mentioned_in"], [{
                "repo": "MATHLAB",
                "path": "docs/research/INDEX-001-G2-A-PAGE-COST-AND-PRIOR-ART.md",
                "kind": "model_overlap",
                "source_sha": "c04acfe345d941eeaf1f9aa447f65c8eca2bb4cb"
            }])
            self.assertFalse(e["full_proof_verified"])
            self.assertFalse(e["independent_reproduction"])

    def test_no_version_splitting_or_rask_duplication(self):
        self.assertEqual(self.by["LIT-180"]["identity"], "doi:10.1002/spe.3433")
        self.assertNotIn("alternate_identities", self.by["LIT-180"])
        self.assertIn("doi:10.1007/978-3-031-72200-4_16",
                      self.by["LIT-183"]["alternate_identities"])
        self.assertIn("arxiv:2405.15088", self.by["LIT-183"]["alternate_identities"])
        self.assertEqual(self.by["LIT-175"]["identity"], "usenix:fast26:zhao")
        self.assertEqual(self.by["LIT-098"]["identity"], "arxiv:2011.02615")
        self.assertEqual(len({e["identity"] for e in self.by.values()}), 205)

    def test_page_model_explicitly_avoids_physical_proof_claim(self):
        audit = AUDIT.read_text(encoding="utf-8")
        for token in ("STOP", "Verbin", "NO", "compaction", "WAL",
                      "cold", "SSD", "RangeReduce", "ArceKV"):
            self.assertIn(token.lower(), audit.lower())
        self.assertNotIn("NEW ORIGINAL UNIVERSAL LOWER BOUND PROVED", audit.upper())


if __name__ == "__main__":
    unittest.main()
