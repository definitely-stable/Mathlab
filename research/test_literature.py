"""RESEARCH-LITERATURE-001: deterministic primary-source metadata checks."""
import copy
import json
import re
import unittest
from literature import DATA, INTERNAL, INDEX, REVERSE, valid, render, render_reverse


class LiteratureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(DATA.read_text(encoding="utf-8"))
        cls.catalog = json.loads(INTERNAL.read_text(encoding="utf-8"))

    def test_real_collection_has_no_metadata_errors(self):
        self.assertEqual(valid(self.data, self.catalog), [])

    def test_import006_distinct_works_and_eighteen_lanes(self):
        entries = self.data["entries"]
        self.assertEqual(len(entries), 347)
        self.assertEqual(len({e["identity"].lower() for e in entries}), 347)
        self.assertEqual(len({e["id"] for e in entries}), 347)
        self.assertEqual(({f"LIT-{i:03d}" for i in range(1, 205)} |
                          {"LIT-206", "LIT-207", "LIT-208", "LIT-209", "LIT-210", "LIT-211", "LIT-212", "LIT-213"} | {f"LIT-{i:03d}" for i in range(214, 349)}),
                         {e["id"] for e in entries})
        self.assertEqual(len({e["track"] for e in entries}), 21)


    def test_import006_graph_rag_memory_primary_metadata(self):
        cohort = {e["id"]: e for e in self.data["entries"]
                  if "LIT-214" <= e["id"] <= "LIT-242"}
        self.assertEqual(len(cohort), 29)
        self.assertEqual(len({e["identity"] for e in cohort.values()}), 29)
        self.assertEqual({e["track"] for e in cohort.values()},
                         {"graph-rag", "agent-memory", "graph-reasoning", "graph-algorithms"})
        self.assertEqual(sum(e["year"] == 2026 for e in cohort.values()), 14)
        self.assertEqual(sum(e["year"] == 2025 for e in cohort.values()), 10)
        self.assertTrue(all(not e["full_proof_verified"]
                            and not e["independent_reproduction"] for e in cohort.values()))
        self.assertTrue(all(e["mentioned_in"] == [{
            "repo": "MATHLAB",
            "path": "docs/research/RESEARCH-LITERATURE-006-GRAPHS-DAG-GRAPHRAG-MEMORY-2025-2026.md",
            "kind": "model_overlap",
            "source_sha": "72ec2a72c0a47cefbbb2c36275080f2d433f304c",
        }] for e in cohort.values()))
        self.assertEqual(cohort["LIT-221"]["identity"], "arxiv:2506.05690")
        self.assertEqual(cohort["LIT-220"]["identity"], "doi:10.1609/aaai.v40i36.40278")
        self.assertEqual(cohort["LIT-239"]["identity"], "doi:10.14778/1920841.1920879")
        altered = copy.deepcopy(self.data)
        next(e for e in altered["entries"] if e["id"] == "LIT-230")["title"] = "Wrong new title"
        self.assertTrue(any("primary source title mismatch" in err
                            for err in valid(altered, self.catalog)))


    def test_import006b_september_2026_primary_source_and_negative_control(self):
        cohort = {e["id"]: e for e in self.data["entries"]
                  if "LIT-243" <= e["id"] <= "LIT-251"}
        self.assertEqual(len(cohort), 9)
        self.assertEqual({e["year"] for e in cohort.values()}, {2026})
        self.assertEqual(cohort["LIT-243"]["identity"], "arxiv:2609.38353")
        self.assertEqual(cohort["LIT-244"]["identity"], "arxiv:2609.40118")
        self.assertIn("BM25", cohort["LIT-243"]["limits_ru"])
        self.assertEqual({e["track"] for e in cohort.values()},
                         {"graph-rag", "agent-memory"})
        self.assertTrue(all(not e["full_proof_verified"]
                            and not e["independent_reproduction"] for e in cohort.values()))
        self.assertTrue(all(e["mentioned_in"] == [{
            "repo": "MATHLAB",
            "path": "docs/research/RESEARCH-LITERATURE-006B-FRESH-GRAPHRAG-AGENT-MEMORY-2026.md",
            "kind": "model_overlap",
            "source_sha": "f8f17c77fb2556f518feafe3f7c2a0372c8127f1",
        }] for e in cohort.values()))
        tampered = copy.deepcopy(self.data)
        next(e for e in tampered["entries"] if e["id"] == "LIT-244")["title"] = "Wrong ReCAP title"
        self.assertTrue(any("primary source title mismatch" in x
                            for x in valid(tampered, self.catalog)))


    def test_tkg001_six_canonical_source_identities(self):
        cohort = {e["id"]: e for e in self.data["entries"] if "LIT-252" <= e["id"] <= "LIT-257"}
        self.assertEqual(len(cohort), 6)
        self.assertEqual(cohort["LIT-252"]["identity"], "doi:10.1145/1265530.1265535")
        self.assertEqual(cohort["LIT-254"]["identity"], "doi:10.1007/978-3-032-26220-2_18")
        self.assertEqual(cohort["LIT-256"]["identity"], "arxiv:2510.13590")
        self.assertTrue(all(not e["full_proof_verified"] and
                            not e["independent_reproduction"] for e in cohort.values()))
        self.assertTrue(all(e["mentioned_in"] == [{
            "repo": "MATHLAB", "kind": "model_overlap",
            "path": "docs/research/TKG-001-G0-BITEMPORAL-PROVENANCE-AND-RECOURSE.md",
            "source_sha": "e34d725bb17e39e144d5d2d4b857bf205a574d59"
        }] for e in cohort.values()))
        altered = copy.deepcopy(self.data)
        next(e for e in altered["entries"] if e["id"] == "LIT-255")["title"] = "wrong"
        self.assertTrue(any("primary source title mismatch" in x
                            for x in valid(altered, self.catalog)))


    def test_import007_temporal_graphs_and_agent_memory_cohort(self):
        cohort = {e["id"]: e for e in self.data["entries"]
                  if "LIT-259" <= e["id"] <= "LIT-280"}
        self.assertEqual(len(cohort), 22)
        self.assertEqual(sum(e["year"] == 2026 for e in cohort.values()), 18)
        self.assertEqual(sum(e["year"] == 2025 for e in cohort.values()), 3)
        self.assertEqual(len({e["identity"].lower() for e in cohort.values()}), 22)
        self.assertEqual(cohort["LIT-260"]["identity"], "doi:10.4230/LIPIcs.SAND.2026.5")
        self.assertEqual(cohort["LIT-270"]["identity"], "doi:10.4230/LIPIcs.ESA.2026.122")
        self.assertEqual(cohort["LIT-277"]["identity"], "arxiv:2603.00026")
        self.assertEqual(cohort["LIT-279"]["identity"], "doi:10.1016/j.ic.2021.104862")
        self.assertTrue(all(e["mentioned_in"] == [{
            "repo": "MATHLAB",
            "path": "docs/research/RESEARCH-LITERATURE-007-TEMPORAL-DYNAMIC-GRAPHS-2026.md",
            "kind": "model_overlap",
            "source_sha": "732dcc116d02ee2639eafe4580f009f6a6b9aefc"
        }] for e in cohort.values()))
        self.assertTrue(all(not e["full_proof_verified"] and
                            not e["independent_reproduction"] for e in cohort.values()))
        for victim in ("LIT-260", "LIT-275", "LIT-277"):
            changed = copy.deepcopy(self.data)
            next(e for e in changed["entries"] if e["id"] == victim)["title"] = "fabricated"
            self.assertTrue(any("primary source title mismatch" in x
                                for x in valid(changed, self.catalog)))


    def test_import008_graph_15_pinned_primary_sources(self):
        cohort = {e["id"]: e for e in self.data["entries"]
                  if "LIT-283" <= e["id"] <= "LIT-297"}
        self.assertEqual(len(cohort), 15)
        self.assertEqual(sum(e["year"] == 2026 for e in cohort.values()), 14)
        self.assertEqual(sum(e["year"] == 2025 for e in cohort.values()), 1)
        self.assertEqual(len({e["identity"].lower() for e in cohort.values()}), 15)
        self.assertEqual(cohort["LIT-287"]["identity"], "doi:10.4230/LIPIcs.ESA.2026.59")
        self.assertEqual(cohort["LIT-288"]["identity"], "doi:10.4230/LIPIcs.ESA.2026.108")
        self.assertEqual(cohort["LIT-292"]["identity"], "doi:10.4230/LIPIcs.ICALP.2026.105")
        self.assertEqual(cohort["LIT-294"]["identity"], "arxiv:2609.23315")
        self.assertEqual(cohort["LIT-295"]["identity"], "arxiv:2608.08055")
        self.assertEqual(cohort["LIT-297"]["identity"], "arxiv:2510.13614")
        self.assertTrue(all(e["mentioned_in"] == [{
            "repo": "MATHLAB",
            "path": "docs/research/RESEARCH-LITERATURE-008-GRAPH-DAG-MEMORY-2026.md",
            "kind": "model_overlap",
            "source_sha": "200bc81a779cd0bb1f766e9168e794964c103e0d"
        }] for e in cohort.values()))
        self.assertTrue(all(not e["full_proof_verified"] and
                            not e["independent_reproduction"] for e in cohort.values()))
        self.assertEqual(len({e["identity"].lower() for e in self.data["entries"]}),
                         len(self.data["entries"]))
        for victim in ("LIT-287", "LIT-292", "LIT-295"):
            changed = copy.deepcopy(self.data)
            next(e for e in changed["entries"] if e["id"] == victim)["title"] = "fabricated"
            self.assertTrue(any("primary source title mismatch" in x
                                for x in valid(changed, self.catalog)))


    def test_import009_dag_reachability_and_graph_memory_primary_identities(self):
        cohort = {e["id"]: e for e in self.data["entries"]
                  if "LIT-298" <= e["id"] <= "LIT-316"}
        self.assertEqual(len(cohort), 19)
        self.assertEqual(sum(e["year"] == 2026 for e in cohort.values()), 12)
        self.assertEqual(sum(e["year"] == 2025 for e in cohort.values()), 4)
        self.assertEqual(len({e["identity"].lower() for e in cohort.values()}), 19)
        self.assertEqual(cohort["LIT-298"]["identity"], "doi:10.1137/24M1638215")
        self.assertEqual(cohort["LIT-298"]["year"], 2025)  # SIAM online; issue 2026
        self.assertEqual(cohort["LIT-302"]["identity"], "arxiv:2607.21390")
        self.assertEqual(cohort["LIT-307"]["identity"], "doi:10.1109/ICDE65706.2026.00177")
        self.assertEqual(cohort["LIT-308"]["identity"], "doi:10.1109/ICDE65706.2026.00179")
        self.assertEqual(cohort["LIT-316"]["alternate_identities"], ["arxiv:2512.03413"])
        self.assertTrue(all(e["mentioned_in"] == [{
            "repo": "MATHLAB",
            "path": "docs/research/RESEARCH-LITERATURE-009-DAG-REACHABILITY-PROVENANCE-2025-2026.md",
            "kind": "model_overlap",
            "source_sha": "1503899bfba204ed5e0bfc6d245440b20c92db3d",
        }] for e in cohort.values()))
        self.assertTrue(all(not e["full_proof_verified"] and
                            not e["independent_reproduction"] for e in cohort.values()))
        self.assertEqual(len({e["identity"].lower() for e in self.data["entries"]}),
                         len(self.data["entries"]))
        for victim in ("LIT-298", "LIT-300", "LIT-302", "LIT-314"):
            altered = copy.deepcopy(self.data)
            next(e for e in altered["entries"] if e["id"] == victim)["title"] = "fabricated"
            self.assertTrue(any("primary source title mismatch" in x
                                for x in valid(altered, self.catalog)))


    def test_import010_bio_dna_three_new_catalog_tracks(self):
        cohort = {e["id"]: e for e in self.data["entries"]
                  if "LIT-317" <= e["id"] <= "LIT-348"}
        self.assertEqual(len(cohort), 32)
        self.assertEqual(len({e["identity"].lower() for e in cohort.values()}), 32)
        self.assertEqual({e["track"] for e in cohort.values()},
                         {"agent-memory", "genomic-graphs", "biological-memory",
                          "molecular-dna-storage"})
        self.assertEqual(sum(e["track"] == "genomic-graphs" for e in cohort.values()), 16)
        self.assertEqual(sum(e["track"] == "biological-memory" for e in cohort.values()), 10)
        self.assertEqual(sum(e["track"] == "molecular-dna-storage" for e in cohort.values()), 4)
        self.assertEqual(cohort["LIT-317"]["identity"], "arxiv:2405.14831")
        self.assertEqual(cohort["LIT-321"]["identity"], "doi:10.1186/s13059-020-02135-8")
        self.assertEqual(cohort["LIT-329"]["identity"], "doi:10.1038/s41586-025-09603-w")
        self.assertEqual(cohort["LIT-345"]["identity"], "doi:10.1126/science.aaj2038")
        self.assertEqual(cohort["LIT-347"]["identity"], "doi:10.1093/bioinformatics/btaf618")
        self.assertTrue(all(e["mentioned_in"] == [{
            "repo": "MATHLAB",
            "path": "docs/research/RESEARCH-LITERATURE-010-DNA-PANGENOME-BIOLOGICAL-GRAPH-MEMORY.md",
            "kind": "model_overlap",
            "source_sha": "8c9bd7948f0cb9fc5a40c99964b96e71cbd74128"
        }] for e in cohort.values()))
        self.assertTrue(all(not e["full_proof_verified"] and
                            not e["independent_reproduction"] for e in cohort.values()))
        for victim in ("LIT-317", "LIT-321", "LIT-329", "LIT-338", "LIT-347"):
            mutated = copy.deepcopy(self.data)
            next(e for e in mutated["entries"] if e["id"] == victim)["title"] = "false"
            self.assertTrue(any("primary source title mismatch" in x
                                for x in valid(mutated, self.catalog)))


    def test_import004_after_uct005_g1_sources_are_disjoint_and_pinned(self):
        records = {e["id"]: e for e in self.data["entries"]}
        uct = {f"LIT-{i:03d}" for i in range(156, 160)}
        group = {f"LIT-{i:03d}" for i in range(160, 177)}
        self.assertTrue(uct | group <= records.keys())
        self.assertEqual(len(group), 17)
        self.assertEqual(sum(records[i]["year"] == 2025 for i in group), 10)
        self.assertEqual(sum(records[i]["year"] == 2026 for i in group), 7)
        for i in group:
            entry = records[i]
            self.assertFalse(entry["full_proof_verified"])
            self.assertFalse(entry["independent_reproduction"])
            self.assertEqual(entry["mentioned_in"], [{
                "repo": "MATHLAB",
                "path": "docs/research/RESEARCH-LITERATURE-004-CACHING-GRAPHS-2025-2026.md",
                "kind": "model_overlap",
                "source_sha": "cce55aa0eb28e369eef3e032e01d3fce79304c1d",
            }])
        for i in uct:
            self.assertEqual(records[i]["mentioned_in"][0]["path"],
                             "docs/research/UCT-005-G1-MEMORY-CHECKING-AND-VC-PRIMARY-AUDIT.md")
        self.assertEqual(sum(e["year"] == 2025 for e in records.values()), 57)
        self.assertEqual(sum(e["year"] == 2026 for e in records.values()), 171)
        bad = copy.deepcopy(self.data)
        next(e for e in bad["entries"] if e["id"] == "LIT-160")["title"] = "Incorrect paging paper"
        self.assertTrue(any("primary source title mismatch" in x for x in valid(bad, self.catalog)))


    def test_import005_after_index001_g2_source_isolation(self):
        refs = {e["id"]: e for e in self.data["entries"]}
        original = {f"LIT-{i:03d}" for i in range(183, 187)}
        cohort = {f"LIT-{i:03d}" for i in range(187, 199)}
        self.assertTrue((original | cohort).issubset(refs))
        self.assertEqual(len(cohort), 12)
        self.assertEqual(sum(refs[i]["year"] == 2025 for i in cohort), 5)
        self.assertEqual(sum(refs[i]["year"] == 2026 for i in cohort), 7)
        for key in original:
            self.assertEqual(refs[key]["mentioned_in"][0]["path"],
                             "docs/research/INDEX-001-G2-A-PAGE-COST-AND-PRIOR-ART.md")
        for key in cohort:
            paper = refs[key]
            self.assertFalse(paper["full_proof_verified"])
            self.assertFalse(paper["independent_reproduction"])
            self.assertEqual(paper["mentioned_in"], [{
                "repo": "MATHLAB",
                "path": "docs/research/RESEARCH-LITERATURE-005-DYNAMIC-ALGEBRA-GRAPHS-2025-2026.md",
                "kind": "model_overlap",
                "source_sha": "399e1db43a1b1847de1855261b1da9c145068e4a",
            }])
        bad = copy.deepcopy(self.data)
        next(p for p in bad["entries"] if p["id"] == "LIT-195")["title"] = "Wrong dynamic rank paper"
        self.assertTrue(any("primary source title mismatch" in e for e in valid(bad, self.catalog)))
        self.assertEqual(sum(p["year"] == 2025 for p in refs.values()), 57)
        self.assertEqual(sum(p["year"] == 2026 for p in refs.values()), 171)

    def test_uct_2026_primary_import_is_deduplicated_and_not_proof_promoted(self):
        lookup = {e["id"]: e for e in self.data["entries"]}
        expected = {f"LIT-{i:03d}" for i in range(111, 123)}
        self.assertTrue(expected.issubset(lookup))
        self.assertEqual(len({lookup[k]["identity"].lower() for k in expected}), 12)
        self.assertEqual(lookup["LIT-119"]["identity"], "publisher:eccc:tr26-047")
        self.assertEqual(lookup["LIT-119"]["verification"],
                         "publisher_full_text_spotchecked")
        for key in expected:
            paper = lookup[key]
            self.assertFalse(paper["full_proof_verified"])
            self.assertFalse(paper["independent_reproduction"])
            self.assertTrue(all(m["kind"] == "model_overlap"
                                for m in paper["mentioned_in"]))
            self.assertIn("docs/research/UCT-001-PRIMARY-SOURCES.md",
                          [m["path"] for m in paper["mentioned_in"]])
        self.assertEqual(lookup["LIT-041"]["identity"], "arxiv:1404.5743")
        self.assertEqual(lookup["LIT-100"]["identity"], "arxiv:1211.1056")

    def test_uct002_eight_source_identities_and_proof_limits(self):
        lookup = {e["id"]: e for e in self.data["entries"]}
        expected = {f"LIT-{i:03d}" for i in range(127, 135)}
        self.assertTrue(expected.issubset(lookup))
        self.assertEqual(len({lookup[k]["identity"] for k in expected}), 8)
        self.assertEqual(lookup["LIT-127"]["identity"], "doi:10.1007/978-3-642-54242-8_21")
        self.assertEqual(lookup["LIT-131"]["identity"], "doi:10.4230/LIPIcs.ITCS.2024.53")
        self.assertEqual(lookup["LIT-134"]["identity"], "doi:10.1214/aoms/1177729032")
        for k in expected:
            self.assertFalse(lookup[k]["full_proof_verified"])
            self.assertFalse(lookup[k]["independent_reproduction"])
            self.assertEqual(lookup[k]["mentioned_in"][0]["kind"], "model_overlap")

    def test_uct003_viola_source_dedup_and_proof_boundaries(self):
        paper = next(e for e in self.data["entries"] if e["id"] == "LIT-141")
        self.assertEqual(paper["identity"], "doi:10.1137/090766619")
        self.assertEqual(paper["title"], "Bit-Probe Lower Bounds for Succinct Data Structures")
        self.assertFalse(paper["full_proof_verified"])
        self.assertFalse(paper["independent_reproduction"])
        self.assertEqual(paper["mentioned_in"][0]["kind"], "model_overlap")

    def test_uct004_certificate_adversary_sources_have_proof_limits(self):
        lookup = {e["id"]: e for e in self.data["entries"]}
        wanted = {"LIT-142": "doi:10.1016/j.jcss.2007.06.020",
                  "LIT-143": "doi:10.1145/3442357",
                  "LIT-144": "arxiv:2609.15063"}
        for code, identity in wanted.items():
            self.assertEqual(lookup[code]["identity"], identity)
            self.assertFalse(lookup[code]["full_proof_verified"])
            self.assertFalse(lookup[code]["independent_reproduction"])
            self.assertEqual(lookup[code]["mentioned_in"][0]["kind"],
                             "model_overlap")
            self.assertEqual(lookup[code]["mentioned_in"][0]["path"],
                             "docs/research/UCT-004-G2-A-PRIMARY-SOURCE-AUDIT.md")

    def test_uct004_g2c_operational_certification_and_pcpp_scope(self):
        lookup = {e["id"]: e for e in self.data["entries"]}
        self.assertEqual(lookup["LIT-149"]["identity"], "arxiv:2609.26757")
        self.assertEqual(lookup["LIT-150"]["identity"],
                         "doi:10.1145/1595391.1595394")
        for key in ("LIT-149", "LIT-150"):
            self.assertFalse(lookup[key]["full_proof_verified"])
            self.assertFalse(lookup[key]["independent_reproduction"])
            self.assertEqual(lookup[key]["mentioned_in"][0]["path"],
                             "docs/research/UCT-004-G2-C-SOURCE-NOVELTY-AUDIT.md")

    def test_uct004_g2d_ppz_1999_and_mfcs_2022_source_scope(self):
        index = {e["id"]: e for e in self.data["entries"]}
        for code, identity, title in [
            ("LIT-154", "doi:10.4086/cjtcs.1999.011", "Satisfiability Coding Lemma"),
            ("LIT-155", "doi:10.4230/LIPIcs.MFCS.2022.47", "CNF Encodings of Parity"),
        ]:
            source = index[code]
            self.assertEqual(source["identity"], identity)
            self.assertEqual(source["title"], title)
            self.assertEqual(source["verification"], "publisher_full_text_spotchecked")
            self.assertFalse(source["full_proof_verified"])
            self.assertFalse(source["independent_reproduction"])
            self.assertEqual(source["mentioned_in"][0]["path"],
                             "docs/research/UCT-004-G2-D-PPZ-PRIMARY-SOURCE-AUDIT.md")

    def test_2026_report_links_match_bibliographic_identities(self):
        """Check real publisher URLs (part A) and internal anchors (part B)."""
        research = DATA.parent.parent
        reports = (
            DATA.parent / "LITERATURE-003-2026-OPPORTUNITY-AUDIT.md",
            research / "RESEARCH-LITERATURE-003B-2026-STOC-ICALP-EUROSYS.md",
        )
        registry = {e["id"]: e for e in self.data["entries"]}
        for report, expected in zip(reports, (20, 26)):
            with self.subTest(report=report.name):
                raw = report.read_text(encoding="utf-8")
                self.assertEqual(
                    self._check_report_paper_links(raw, registry), expected)

    @staticmethod
    def _check_report_paper_links(content, registry):
        """Match each visible paper ID to its exact canonical source."""
        pattern = re.compile(
            r"\[[^\]\n]*?\b(LIT-\d{3})\b[^\]\n]*?\]"
            r"\(([^)\s]+)\)",
            re.IGNORECASE,
        )
        links = list(pattern.finditer(content))
        for link in links:
            visible, target_url = link.group(1).upper(), link.group(2)
            paper = registry.get(visible)
            if paper is None:
                raise AssertionError(f"missing bibliographic work: {visible}")
            if target_url.startswith("https://"):
                if target_url != paper["primary_url"]:
                    raise AssertionError(
                        f"wrong bibliographic primary URL: {visible} -> "
                        f"{target_url}, expected {paper['primary_url']}")
            else:
                match = re.fullmatch(
                    r"(?:catalog/)?LITERATURE\.md#lit-(\d{3})",
                    target_url, re.IGNORECASE)
                if match is None:
                    raise AssertionError(
                        f"unknown bibliographic destination: {target_url}")
                target = "LIT-" + match.group(1)
                if target not in registry:
                    raise AssertionError(
                        f"missing bibliographic work: {visible} -> {target}")
                if visible != target:
                    raise AssertionError(
                        f"wrong bibliographic anchor: {visible} -> {target}")
        return len(links)

    def test_report_link_mismatch_is_rejected(self):
        registry = {e["id"]: e for e in self.data["entries"]}
        with self.assertRaisesRegex(AssertionError, "wrong bibliographic anchor"):
            self._check_report_paper_links(
                "[LIT-072](catalog/LITERATURE.md#lit-052)", registry)
        with self.assertRaisesRegex(AssertionError, "missing bibliographic work"):
            self._check_report_paper_links(
                "[LIT-999](catalog/LITERATURE.md#lit-999)", registry)
        with self.assertRaisesRegex(AssertionError,
                                    "wrong bibliographic primary URL"):
            self._check_report_paper_links(
                "[LIT-063](https://doi.org/10.1145/wrong)", registry)

    def test_forward_and_reverse_indices_are_exactly_reproducible(self):
        self.assertEqual(render(self.data), INDEX.read_text(encoding="utf-8"))
        self.assertEqual(render_reverse(self.data, self.catalog),
                         REVERSE.read_text(encoding="utf-8"))

    def test_research_anchors_are_pinned_and_do_not_claim_novelty(self):
        for e in self.data["entries"]:
            self.assertTrue(e["mentioned_in"])
            self.assertTrue(e["maps_to"])
            self.assertFalse(e["full_proof_verified"])
            self.assertFalse(e["independent_reproduction"])
            self.assertIn(e["verification"],
                          {"primary_abstract_checked", "publisher_abstract_checked",
                           "publisher_bibliography_checked", "publisher_full_text_spotchecked",
                           "author_paper_or_bibliography_checked"})

    def test_26_new_venue_sources_are_broad_and_nonreconciliation(self):
        new = [e for e in self.data["entries"]
               if "LIT-070" <= e["id"] <= "LIT-095"]
        self.assertEqual(len(new), 26)
        self.assertGreaterEqual(len({e["track"] for e in new}), 8)
        self.assertFalse(any(e["track"] == "streaming-reconciliation"
                             for e in new))
        self.assertEqual({e["year"] for e in new}, {2026})
        self.assertEqual({e["venue"] for e in new},
                         {"STOC 2026", "ICALP 2026", "EuroSys 2026"})
        self.assertEqual(len({e["identity"] for e in new}), 26)
        self.assertEqual(len([e for e in self.data["entries"]
                              if e["id"] <= "LIT-069"]), 69)
        self.assertTrue(all(e["publication_stage"] == "peer_reviewed_proceedings"
                            and not e["full_proof_verified"]
                            and not e["independent_reproduction"]
                            for e in new))

    def test_2026_venue_identity_and_year_falsifications(self):
        d = copy.deepcopy(self.data)
        target = next(e for e in d["entries"] if e["id"] == "LIT-070")
        target["source_listing_url"] = "https://example.com/spurious"
        target["year"] = 2025
        errors = valid(d, self.catalog)
        self.assertTrue(any("primary 2026 listing/identity mismatch" in x
                            for x in errors))
        self.assertTrue(any("venue-2026 cohort has non-2026 work" in x
                            for x in errors))

    def test_2026_source_cannot_be_promoted_to_independent_proof(self):
        d = copy.deepcopy(self.data)
        target = next(e for e in d["entries"] if e["id"] == "LIT-095")
        target["verification"] = "publisher_full_text_spotchecked"
        target["full_proof_verified"] = True
        errors = valid(d, self.catalog)
        self.assertTrue(any("unsupported 2026 full-text verification" in x
                            for x in errors))
        self.assertTrue(any("unsupported proof/reproduction promotion" in x
                            for x in errors))

    def test_concurrent_2026_primary_cohorts_are_both_preserved(self):
        original = {e["id"] for e in self.data["entries"]}
        self.assertTrue({f"LIT-{i:03d}" for i in range(50, 96)} <= original)
        self.assertTrue({f"LIT-{i:03d}" for i in range(1, 96)} <= original)
        self.assertEqual(len(self.data["entries"]), 347)
        all_ids = [e["identity"].lower() for e in self.data["entries"]]
        self.assertEqual(len(all_ids), len(set(all_ids)))

    def test_tom007_seven_source_identity_and_provenance_are_retained(self):
        expected = {
            "LIT-096": "arxiv:1503.07792",
            "LIT-097": "arxiv:1407.3008",
            "LIT-098": "arxiv:2011.02615",
            "LIT-099": "doi:10.4230/LIPIcs.CPM.2026.20",
            "LIT-100": "arxiv:1211.1056",
            "LIT-101": "publisher:pmlr:cohen25c",
            "LIT-102": "usenix:atc22:curtsinger",
        }
        selected = {e["id"]: e for e in self.data["entries"]
                    if "LIT-096" <= e["id"] <= "LIT-102"}
        self.assertEqual(set(selected), set(expected))
        for key, identity in expected.items():
            with self.subTest(paper=key):
                paper = selected[key]
                self.assertEqual(paper["identity"], identity)
                self.assertEqual(paper["mentioned_in"], [{
                    "repo": "MATHLAB",
                    "path": "docs/research/TOM-007-SIX-HYPOTHESIS-AUDIT.md",
                    "kind": "model_overlap",
                }])
                self.assertFalse(paper["full_proof_verified"])
                self.assertFalse(paper["independent_reproduction"])
        self.assertEqual(len([e for e in self.data["entries"]
                              if e["id"] <= "LIT-095"]), 95)
        # A false/changed primary title cannot pass the metadata authority.
        changed = copy.deepcopy(self.data)
        next(e for e in changed["entries"] if e["id"] == "LIT-101")["title"] = "Adaptive Sketches"
        self.assertTrue(any("primary source title mismatch" in problem
                            for problem in valid(changed, self.catalog)))

    def test_hyp103_six_primary_source_identities_and_old_cohorts(self):
        expected = {
            "LIT-103": "doi:10.4230/LIPIcs.MFCS.2024.46",
            "LIT-104": "doi:10.4230/LIPIcs.ESA.2020.2",
            "LIT-105": "doi:10.4230/LIPIcs.ITCS.2020.56",
            "LIT-106": "publisher:eccc:tr26-206",
            "LIT-107": "arxiv:2602.01042",
            "LIT-108": "doi:10.1016/S0304-3975(01)00144-X",
        }
        rows = {e["id"]: e for e in self.data["entries"]
                if "LIT-103" <= e["id"] <= "LIT-108"}
        self.assertEqual(set(rows), set(expected))
        for key, identity in expected.items():
            with self.subTest(primary=key):
                row = rows[key]
                self.assertEqual(row["identity"], identity)
                self.assertEqual(row["mentioned_in"], [{
                    "repo": "MATHLAB",
                    "path": "docs/research/HYP-103-G0-CERTIFICATE-REDUCTION.md",
                    "kind": "model_overlap",
                }])
                self.assertFalse(row["full_proof_verified"])
                self.assertFalse(row["independent_reproduction"])
        self.assertEqual(
            {f"LIT-{i:03d}" for i in range(1, 103)},
            {e["id"] for e in self.data["entries"] if e["id"] <= "LIT-102"})
        modified = copy.deepcopy(self.data)
        next(e for e in modified["entries"] if e["id"] == "LIT-106")["title"] = "Misattributed result"
        self.assertTrue(any("primary source title mismatch" in x
                            for x in valid(modified, self.catalog)))

    def test_hyp101_crypto_origins_are_new_without_dropping_108_works(self):
        expected = {
            "LIT-109": "doi:10.1007/3-540-48658-5_22",
            "LIT-110": "doi:10.1007/3-540-69053-0_13",
        }
        rows = {e["id"]: e for e in self.data["entries"]
                if e["id"] in expected}
        self.assertEqual(set(rows), set(expected))
        for key, identity in expected.items():
            self.assertEqual(rows[key]["identity"], identity)
            self.assertEqual(rows[key]["mentioned_in"], [{
                "repo": "MATHLAB",
                "path": "docs/research/HYP-101-G0-INCREMENTAL-HASH-AUDIT.md",
                "kind": "model_overlap",
            }])
            self.assertFalse(rows[key]["full_proof_verified"])
        self.assertEqual({f"LIT-{i:03d}" for i in range(1, 109)},
                         {e["id"] for e in self.data["entries"]
                          if e["id"] <= "LIT-108"})
        changed = copy.deepcopy(self.data)
        next(e for e in changed["entries"] if e["id"] == "LIT-110")["title"] = "Unknown hashing"
        self.assertTrue(any("primary source title mismatch" in problem
                            for problem in valid(changed, self.catalog)))

    def test_hyp101_g1_four_source_identities_and_122_paper_retention(self):
        expected = {
            "LIT-123": "doi:10.1137/1.9781611975031.99",
            "LIT-124": "doi:10.1016/j.tcs.2026.115746",
            "LIT-125": "publisher:c2sp:blake3-v1-0-0",
            "LIT-126": "doi:10.1007/s00224-026-10266-x",
        }
        lookup = {e["id"]: e for e in self.data["entries"]}
        self.assertEqual(
            {f"LIT-{i:03d}" for i in range(1, 123)},
            {e["id"] for e in self.data["entries"] if e["id"] <= "LIT-122"})
        for id_, identity in expected.items():
            with self.subTest(record=id_):
                row = lookup[id_]
                self.assertEqual(row["identity"], identity)
                self.assertEqual(row["mentioned_in"], [{
                    "repo": "MATHLAB",
                    "path": "docs/research/HYP-101-G1-PHASE-COUNTER-FRONTIER.md",
                    "kind": "model_overlap",
                }])
                self.assertFalse(row["full_proof_verified"])
                self.assertFalse(row["independent_reproduction"])
        self.assertIn("техническая спецификация", lookup["LIT-125"]["limits_ru"])
        copy_data = copy.deepcopy(self.data)
        copy_lookup = {e["id"]: e for e in copy_data["entries"]}
        copy_lookup["LIT-125"]["title"] = "Rebranded third-party specification"
        self.assertTrue(any("primary source title mismatch" in x
                            for x in valid(copy_data, self.catalog)))

    def test_hyp105_g1_girth_sources_and_historical_134_retention(self):
        expected = {
            "LIT-135": "doi:10.1016/0095-8956(91)90097-4",
            "LIT-136": "arxiv:1111.3279",
        }
        lookup = {paper["id"]: paper for paper in self.data["entries"]}
        self.assertEqual({f"LIT-{i:03d}" for i in range(1, 135)},
                         {paper["id"] for paper in self.data["entries"]
                          if paper["id"] <= "LIT-134"})
        for ref, identity in expected.items():
            paper = lookup[ref]
            self.assertEqual(paper["identity"], identity)
            self.assertEqual(paper["mentioned_in"], [{
                "repo": "MATHLAB",
                "path": "docs/research/HYP-105-G1-W2D3-GIRTH8.md",
                "kind": "model_overlap",
            }])
            self.assertFalse(paper["full_proof_verified"])
            self.assertFalse(paper["independent_reproduction"])
        altered = copy.deepcopy(self.data)
        next(e for e in altered["entries"] if e["id"] == "LIT-136")["title"] = "Invented different paper"
        self.assertTrue(any("primary source title mismatch" in problem
                            for problem in valid(altered, self.catalog)))

    def test_hyp105_g2_grid_and_sparse_sources_preserve_first_136(self):
        expected = {
            "LIT-137": "doi:10.1090/proc/15673",
            "LIT-138": "doi:10.1109/ISIT.2005.1523645",
            "LIT-139": "arxiv:2508.09841",
            "LIT-140": "doi:10.37236/14115",
        }
        self.assertEqual(
            {f"LIT-{i:03d}" for i in range(1, 137)},
            {e["id"] for e in self.data["entries"] if e["id"] <= "LIT-136"},
        )
        lookup = {e["id"]: e for e in self.data["entries"]}
        for ref, identity in expected.items():
            row = lookup[ref]
            self.assertEqual(row["identity"], identity)
            self.assertEqual(row["mentioned_in"], [{
                "repo": "MATHLAB",
                "path": "docs/research/HYP-105-G2-GRID-FREE-QUADRATIC.md",
                "kind": "model_overlap",
            }])
            self.assertFalse(row["full_proof_verified"])
            self.assertFalse(row["independent_reproduction"])
        d = copy.deepcopy(self.data)
        next(e for e in d["entries"] if e["id"] == "LIT-137")["title"] = "Wrong source"
        self.assertTrue(any("primary source title mismatch" in p
                            for p in valid(d, self.catalog)))

    def test_g4_all_four_sources_and_uct004_historical_144_retention(self):
        expected = {
            "LIT-145": "arxiv:2602.14716",
            "LIT-146": "doi:10.1016/j.disc.2022.113025",
            "LIT-147": "doi:10.1016/j.disc.2024.114029",
            "LIT-148": "doi:10.1006/jctb.2002.2123",
        }
        rows = {e["id"]: e for e in self.data["entries"]}
        self.assertEqual(
            {f"LIT-{i:03d}" for i in range(1, 145)},
            {e["id"] for e in self.data["entries"] if e["id"] <= "LIT-144"})
        for key, identity in expected.items():
            self.assertEqual(rows[key]["identity"], identity)
            self.assertEqual(rows[key]["mentioned_in"], [{
                "repo": "MATHLAB",
                "path": "docs/research/HYP-105-G4-CHARACTERISTIC-W4.md",
                "kind": "model_overlap",
            }])
            self.assertFalse(rows[key]["full_proof_verified"])
            self.assertFalse(rows[key]["independent_reproduction"])
        altered = copy.deepcopy(self.data)
        next(e for e in altered["entries"] if e["id"] == "LIT-148")["title"] = "Bad source"
        self.assertTrue(any("primary source title mismatch" in message
                            for message in valid(altered, self.catalog)))

    def test_hyp105_g5_new_primary_identity_and_no_reimport_of_old_2026_paper(self):
        expected = {
            "LIT-151": "doi:10.1137/20M1325769",
            "LIT-152": "doi:10.1007/s00493-008-2195-2",
            "LIT-153": "arxiv:2609.39680",
        }
        rows = {e["id"]: e for e in self.data["entries"]}
        self.assertEqual(
            {f"LIT-{i:03d}" for i in range(1, 151)},
            {e["id"] for e in self.data["entries"] if e["id"] <= "LIT-150"},
        )
        # Already indexed arXiv 2605.11949 under the original v1 title.
        self.assertEqual(rows["LIT-005"]["identity"], "arxiv:2605.11949")
        self.assertEqual(
            sum(e["identity"] == "arxiv:2605.11949"
                for e in self.data["entries"]), 1)
        for key, identity in expected.items():
            paper = rows[key]
            self.assertEqual(paper["identity"], identity)
            self.assertEqual(paper["mentioned_in"], [{
                "repo": "MATHLAB",
                "path": "docs/research/HYP-105-G5-A-TRADE-INTERSECTION.md",
                "kind": "model_overlap",
            }])
            self.assertFalse(paper["full_proof_verified"])
            self.assertFalse(paper["independent_reproduction"])
        tampered = copy.deepcopy(self.data)
        next(e for e in tampered["entries"] if e["id"] == "LIT-153")["title"] = "Wrong article"
        self.assertTrue(any("primary source title mismatch" in err
                            for err in valid(tampered, self.catalog)))

    def test_original_sedd_arxiv_identity_is_not_misattributed(self):
        e = next(x for x in self.data["entries"] if x["id"] == "LIT-022")
        self.assertEqual(e["identity"], "arxiv:2501.01046")
        self.assertTrue(e["title"].startswith("SEDD:"))
        self.assertNotIn("FED:", e["title"])
        d = copy.deepcopy(self.data)
        next(x for x in d["entries"] if x["id"] == "LIT-022")["title"] = "FED: Fast Dataset Deduplication"
        self.assertTrue(any("primary source title mismatch" in x
                            for x in valid(d, self.catalog)))

    def test_2026_broad_selection_is_not_sketch_centric(self):
        selected = [e for e in self.data["entries"]
                    if 50 <= int(e["id"][4:]) <= 69]
        self.assertEqual(len(selected), 20)
        self.assertEqual({e["year"] for e in selected}, {2026})
        self.assertEqual(len({e["track"] for e in selected}), 7)
        self.assertFalse({"streaming-reconciliation", "sparse-coding"} &
                         {e["track"] for e in selected})
        self.assertEqual(sum(e["track"] == "proof-certification"
                             for e in selected), 7)
        self.assertEqual(sum(e["track"] == "compressed-indexing"
                             for e in selected), 5)
        self.assertEqual(sum(e["publication_stage"] ==
                             "peer_reviewed_proceedings" for e in selected), 16)
        self.assertEqual(sum(e["publication_stage"] ==
                             "author_preprint" for e in selected), 4)
        self.assertTrue(all(e["mentioned_in"][0]["kind"] == "model_overlap"
                            for e in selected))

    def test_2026_year_stage_and_priority_mislabeling_is_rejected(self):
        for key, value, diagnostic in (
            ("year", 2025, "non-2026 cohort entry"),
            ("publication_stage", "peer_reviewed_proceedings", "proceedings DOI missing"),
            ("selection_priority", "publication accepted", "missing 2026 selection priority"),
        ):
            d = copy.deepcopy(self.data)
            target = next(x for x in d["entries"] if x["id"] == "LIT-063")
            target[key] = value
            self.assertTrue(any(diagnostic in x for x in valid(d, self.catalog)),
                            f"{key} must fail on mismatched source identity")

    def test_2026_source_and_classification_guardrails(self):
        d = copy.deepcopy(self.data)
        x = next(x for x in d["entries"] if x["id"] == "LIT-055")
        x["mentioned_in"][0]["kind"] = "cited"
        self.assertTrue(any("invented existing citation" in problem
                            for problem in valid(d, self.catalog)))
        d = copy.deepcopy(self.data)
        x = next(x for x in d["entries"] if x["id"] == "LIT-052")
        x["title"] = "FSST Fast Random Access"
        self.assertTrue(any("primary source title mismatch" in problem
                            for problem in valid(d, self.catalog)))

    def test_cross_identifier_alias_collision_is_rejected(self):
        d = copy.deepcopy(self.data)
        target = next(x for x in d["entries"] if x["id"] == "LIT-039")
        self.assertIn("doi:10.1109/ALLERTON.2011.6120248",
                      target["alternate_identities"])
        wrong = next(x for x in d["entries"] if x["id"] == "LIT-040")
        wrong["alternate_identities"] = list(target["alternate_identities"])
        self.assertTrue(any("duplicate canonical identity" in x
                            for x in valid(d, self.catalog)))

    def test_identity_alias_is_never_reported_as_a_second_work(self):
        d = copy.deepcopy(self.data)
        riblt = next(x for x in d["entries"] if x["id"] == "LIT-027")
        self.assertIn("arxiv:2402.02668", riblt["alternate_identities"])
        self.assertEqual(sum("arxiv:2402.02668" in [e["identity"]] +
                             e.get("alternate_identities", []) for e in
                             d["entries"]), 1)

    def test_bibliography_expansion_covers_three_projects(self):
        entries = self.data["entries"]
        self.assertEqual(len({e["id"] for e in entries}), 347)
        tracks = {e["track"] for e in entries}
        self.assertEqual(len(tracks), 18)
        self.assertTrue({"LIT-043", "LIT-044", "LIT-047"}.issubset(
            {e["id"] for e in entries}))
        self.assertTrue({"MATHLAB", "DELSK", "DELTAMETER"}.issubset(
            {origin["repo"] for e in entries for origin in e["mentioned_in"]}))

    def test_duplicate_doi_is_rejected(self):
        d = copy.deepcopy(self.data)
        d["entries"][1]["identity"] = d["entries"][0]["identity"]
        self.assertTrue(any("duplicate canonical identity" in err
                            for err in valid(d, self.catalog)))

    def test_missing_internal_research_link_is_rejected(self):
        d = copy.deepcopy(self.data)
        d["entries"][0]["maps_to"].append("ML-999")
        self.assertTrue(any("dangling research link" in err
                            for err in valid(d, self.catalog)))

    def test_unpinned_origin_and_invalid_sha_are_rejected(self):
        d = copy.deepcopy(self.data)
        d["source_snapshots"]["DELSK"]["sha"] = "main"
        self.assertTrue(any("invalid snapshot SHA" in err
                            for err in valid(d, self.catalog)))
        d = copy.deepcopy(self.data)
        d["entries"][1]["mentioned_in"][0]["path"] = "../escape.md"
        self.assertTrue(any("origin path unsafe" in err
                            for err in valid(d, self.catalog)))

    def test_promotion_to_independent_theorem_is_rejected(self):
        d = copy.deepcopy(self.data)
        d["entries"][0]["full_proof_verified"] = True
        d["entries"][0]["independent_reproduction"] = True
        self.assertTrue(any("unsupported proof/reproduction promotion" in err
                            for err in valid(d, self.catalog)))

    def test_non_equivalence_boundaries_are_documented(self):
        lookup = {e["id"]: e for e in self.data["entries"]}
        self.assertIn("overline{3}", lookup["LIT-004"]["limits_ru"])
        self.assertIn("GF(q)", lookup["LIT-005"]["limits_ru"])
        self.assertIn("байтам", lookup["LIT-027"]["limits_ru"])
        self.assertIn("finite-sample", lookup["LIT-023"]["limits_ru"])

    def test_distinguish_explicit_citation_from_model_overlap(self):
        r = next(e for e in self.data["entries"] if e["id"] == "LIT-031")
        self.assertEqual(r["mentioned_in"][0]["kind"], "model_overlap")
        self.assertIn("model_overlap", render(self.data))


if __name__ == "__main__":
    unittest.main()
