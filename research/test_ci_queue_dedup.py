"""CI-QUEUE-001: regression guard for fail-closed GitHub-hosted queue policy.

No YAML dependency is needed: this checks the actual event blocks and concurrency
expressions, not a simulated workflow scheduler. Existing suite guards separately
verify named Research steps and the exact full-suite dependency closure.
"""
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
GENERAL_WORKFLOWS = (
    "research.yml",
    "index001-c5-page-epochs.yml",
    "dag002-g1c-online.yml",
    "dag002-g2a-source-gate.yml",
    "dag002-g2b2-felsner.yml",
    "dag002-g2b2c-paid-ledger.yml",
    "dag002-g2b-record-anchors.yml",
    "dag002-g2b2-power-anchors.yml",
)
CONCURRENCY_GROUP = (
    "group: ${{ github.workflow }}-${{ github.event_name == 'pull_request' "
    "&& format('pr-{0}', github.event.pull_request.number) || github.run_id }}"
)
PR_ONLY_CANCEL = "cancel-in-progress: ${{ github.event_name == 'pull_request' }}"


def events_of(raw):
    # Only the pre-jobs header is inspected; job and step YAML is out of scope.
    header = raw.split("\njobs:", 1)[0]
    on_section = header.split("\non:\n", 1)[1].split("\npermissions:", 1)[0]
    on_section = on_section.split("\nconcurrency:", 1)[0]
    sections = re.split(r"(?m)^  ([a-z_]+):\s*$", on_section)
    return dict(zip(sections[1::2], sections[2::2]))


class CIQueueDedupPolicyTests(unittest.TestCase):
    def test_global_workflows_are_pr_or_main_only_with_manual_dispatch(self):
        for filename in GENERAL_WORKFLOWS:
            with self.subTest(workflow=filename):
                raw = (ROOT / ".github" / "workflows" / filename).read_text(
                    encoding="utf-8"
                )
                events = events_of(raw)
                self.assertIn("push", events)
                self.assertIn("pull_request", events)
                self.assertIn("workflow_dispatch", events)
                branch_lines = events["push"].split("    paths:", 1)[0]
                inline = re.search(r"(?m)^    branches:\s*\[([^]]+)\]\s*$", branch_lines)
                if inline:
                    branches = [s.strip().strip("'\"") for s in inline.group(1).split(",")]
                else:
                    branches = re.findall(r"(?m)^      - (.+)$", branch_lines)
                    branches = [s.strip().strip("'\"") for s in branches]
                self.assertEqual(branches, ["main"])
                self.assertNotIn("research/**", branch_lines)

    def test_supersession_cancels_pr_only_and_preserves_all_job_bodies(self):
        for filename in GENERAL_WORKFLOWS:
            with self.subTest(workflow=filename):
                raw = (ROOT / ".github" / "workflows" / filename).read_text(
                    encoding="utf-8"
                )
                header, sep, jobs = raw.partition("\njobs:\n")
                self.assertTrue(sep)
                self.assertIn(CONCURRENCY_GROUP, header)
                self.assertIn(PR_ONLY_CANCEL, header)
                self.assertIn("runs-on: ubuntu-latest", jobs)
                self.assertNotIn("runs-on: self-hosted", jobs)


if __name__ == "__main__":
    unittest.main()
