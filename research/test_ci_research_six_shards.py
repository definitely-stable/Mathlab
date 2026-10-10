"""Lossless six-shard GitHub-hosted Research CI regression contract.

Frozen 121 exact (name, run) pairs preserve the 107 scientific-branch commands,
plus two explicit C16, six C17-C19 and two C20 commands. No old check lost. Any
future command edits/additions must update the independent fingerprint
AND explain the change in the CI documentation. No removed checks,
name-only surrogates or hidden duplicates silently pass this guard.
"""
import re
import unittest
from pathlib import Path

WORKFLOW = Path(__file__).resolve().parents[1] / ".github/workflows/research.yml"
SHARDS = {
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
    "research-hyp105-coupled-low": (
        "HYP-105 C1 GQ concurrence theorem and independent W32 wedge oracle",
        "HYP-105 C10 symbolic all-h three-pin relaxation zero certificate",
    ),
    "research-hyp105-coupled-exact": (
        "HYP-105 C11 independent shared-prefix second-moment and W32 four-line falsifiers",
        "HYP-105 C15 compare three verified BnB modes on the W32 36 full joint map box",
        "HYP-105 C16 independent original two-sided source membership and hierarchy tests",
        "HYP-105 C16 full genuine W32 two-sided 36-pair certificate report",
        "HYP-105 C17 original W32 factor-local versus full-joint report",
        "HYP-105 C18 all-h star zero original W32 A B C report",
        "HYP-105 C19 genuine original W32 nine-point joint-left 62370 census report",
        "HYP-105 C20 all-h physical missing-edge C6 and real W32 global-left tests",
        "HYP-105 C20 43740 real original W32 Hamilton source global relabel report",
    ),
}
# Independently frozen on the 121 exact (name,run) pairs: the full
# 117-command C20 six-shard suite plus two explicit C21 checks.
FROZEN_FNV1A64 = 0x0BAEB6BDD0C8839B
FROZEN_COMMANDS = 121


def jobs_from_source(raw):
    if "jobs:\n" not in raw:
        raise ValueError("Research workflow lost jobs")
    chunks = re.split(r"(?m)^  ([a-z][a-z0-9-]*):\s*$",
                      raw.split("jobs:\n", 1)[1])
    return dict(zip(chunks[1::2], chunks[2::2]))


def pairs_for_job(body):
    names = re.findall(r"(?m)^      - name: (.+)$", body)
    runs = re.findall(r"(?m)^        run: (.+)$", body)
    if len(names) != len(runs):
        raise AssertionError("unequal script names and inline run commands")
    return list(zip(names, runs))


def fnv1a64(items):
    """Stable byte-wise digest; these frozen commands are UTF-8 source."""
    h = 0xCBF29CE484222325
    mask = (1 << 64) - 1
    for name, run in sorted(items):
        # All 121 current source names and commands are ASCII.
        for byte in (name + "\x00" + run).encode("utf-8") + b"\n":
            h = ((h ^ byte) * 0x100000001B3) & mask
    return h


class ResearchSixShardsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw = WORKFLOW.read_text(encoding="utf-8")
        cls.jobs = jobs_from_source(cls.raw)

    def test_six_hosted_independently_configured_shards(self):
        self.assertEqual(set(self.jobs), set(SHARDS) | {"research-full-suite"})
        for name, body in self.jobs.items():
            self.assertIn("runs-on: ubuntu-latest", body, name)
            self.assertRegex(body, r"timeout-minutes: [1-9][0-9]*")
            if name in SHARDS:
                self.assertIn("- uses: actions/checkout@v4", body)
                self.assertIn("- uses: actions/setup-python@v5", body)
                self.assertIn('python-version: "3.x"', body)
            else:
                self.assertNotIn("actions/checkout", body)

    def test_exact_lossless_frozen_named_commands(self):
        pairs = []
        for name in SHARDS:
            sub = pairs_for_job(self.jobs[name])
            for required in SHARDS[name]:
                self.assertIn(required, [step for step, _ in sub], name)
            pairs.extend(sub)
        self.assertEqual(len(pairs), FROZEN_COMMANDS)
        self.assertEqual(len(pairs), len(set(pairs)))
        self.assertEqual(len({name for name, _ in pairs}), len(pairs))
        self.assertEqual(fnv1a64(pairs), FROZEN_FNV1A64)

    def test_exact_all_shards_aggregate_fail_closed(self):
        aggregate = self.jobs["research-full-suite"]
        self.assertIn("if: ${{ always() }}", aggregate)
        self.assertIn('if [ "$result" != "success" ]; then', aggregate)
        self.assertIn("exit 1", aggregate)
        for name in SHARDS:
            self.assertIn("      - " + name + "\n", aggregate)
            self.assertIn("needs." + name + ".result", aggregate)
        self.assertIn('"$COUPLED_LOW"', aggregate)
        self.assertIn('"$COUPLED_EXACT"', aggregate)

    def test_heavy_steps_have_separate_hosted_budgets(self):
        self.assertIn("timeout-minutes: 90", self.jobs["research-hyp105-exact-census"])
        self.assertIn("timeout-minutes: 90", self.jobs["research-hyp105-coupled-exact"])
        self.assertNotIn("62370-candidate", self.jobs["lent-001-foundation"])
        self.assertNotIn("C16 full genuine W32", self.jobs["lent-001-foundation"])
        self.assertNotIn("C16 full genuine W32", self.jobs["research-hyp105-coupled-low"])
        self.assertIn("C16 full genuine W32", self.jobs["research-hyp105-coupled-exact"])
        self.assertIn("C19 genuine original W32", self.jobs["research-hyp105-coupled-exact"])


if __name__ == "__main__":
    unittest.main()
