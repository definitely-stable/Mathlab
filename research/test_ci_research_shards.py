"""Guard the independent GitHub-hosted research CI shards from silent check loss."""
import re
import unittest
from pathlib import Path


WORKFLOW = Path(__file__).resolve().parents[1] / ".github/workflows/research.yml"
REQUIRED = {
    "lent-001-foundation": (
        "Research harness (G0 + G1A + G2A)",
        "Unit tests",
        "INDEX-001 G2-B4-C5A file-backed atomic-root pinned epoch and page allocator",
    ),
    "research-hyp105-foundation": (
        "HYP-105 G5-C2 deterministic signed-trade density report",
        "HYP-105 B3.2-E1-B1-A independent K14 missing-edge and W32 template tests",
    ),
    "research-hyp105-exact-census": (
        "HYP-105 B3.2-E1-A full W32 fixed-map 62370-candidate GF5 lower census",
        "HYP-105 E2-B3.2-D full four-motif and joint GF5 seven-column certificate",
    ),
    "research-catalog-and-primitives": (
        "External research literature identity and source validation",
        "Cross-repository research catalog validation",
        "TOM-003-D2 authenticated overwrite and multiproof cost gate",
    ),
}


def parse_jobs(raw):
    chunks = re.split(r"(?m)^  ([a-z][a-z0-9-]*):\s*$", raw.split("jobs:\n", 1)[1])
    return dict(zip(chunks[1::2], chunks[2::2]))


class ResearchWorkflowShardTests(unittest.TestCase):
    def test_all_shards_exist_and_require_hosted_setup(self):
        raw = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn("jobs:\n", raw)
        jobs = parse_jobs(raw)
        self.assertEqual(set(jobs), set(REQUIRED) | {"research-full-suite"})
        for name, body in jobs.items():
            self.assertIn("runs-on: ubuntu-latest", body, name)
            self.assertRegex(body, r"timeout-minutes: [1-9][0-9]*")
            if name in REQUIRED:
                self.assertIn("- uses: actions/checkout@v4", body, name)
                self.assertIn("- uses: actions/setup-python@v5", body, name)

    def test_no_silent_loss_or_duplicate_named_steps(self):
        raw = WORKFLOW.read_text(encoding="utf-8")
        jobs = parse_jobs(raw)
        all_names = []
        for name, body in jobs.items():
            if name == "research-full-suite":
                continue
            names = re.findall(r"(?m)^      - name: (.+)$", body)
            commands = re.findall(r"(?m)^        run: (.+)$", body)
            self.assertEqual(len(names), len(commands), name)
            for required in REQUIRED[name]:
                self.assertIn(required, names, name)
            all_names.extend(names)
        self.assertGreaterEqual(len(all_names), 77)
        self.assertEqual(len(all_names), len(set(all_names)))

    def test_aggregate_full_suite_depends_on_all_four_shards(self):
        jobs = parse_jobs(WORKFLOW.read_text(encoding="utf-8"))
        full = jobs["research-full-suite"]
        self.assertIn("if: ${{ always() }}", full)
        for required in REQUIRED:
            self.assertIn("      - " + required + "\n", full)
            self.assertIn("needs." + required + ".result", full)
        self.assertIn('"$result" != "success"', full)
        self.assertIn("exit 1", full)

    def test_heavy_census_is_not_in_ten_minute_foundation(self):
        jobs = parse_jobs(WORKFLOW.read_text(encoding="utf-8"))
        self.assertNotIn("62370-candidate", jobs["lent-001-foundation"])
        self.assertIn("62370-candidate", jobs["research-hyp105-exact-census"])
        self.assertIn("timeout-minutes: 90",
                      jobs["research-hyp105-exact-census"])


if __name__ == "__main__":
    unittest.main()
