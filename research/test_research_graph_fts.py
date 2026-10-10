"""SQLite FTS5 incremental retrieval regressions: new, changed, deleted studies."""
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from research_graph_fts import sync, query


def record(ident, title, text, *, tags=None):
    return {
        "type": "node", "id": ident, "title": title, "aliases": [],
        "tags": tags or [], "summary": text, "limitations": "",
        "status": "OPEN_UNPROVED", "path": "docs/research/demo.md",
        "provenance": "test fixture"
    }


class IncrementalFTS5Tests(unittest.TestCase):
    def test_delta_update_delete_and_russian_query(self):
        with TemporaryDirectory() as folder:
            path = Path(folder)
            data = path / "items.jsonl"
            db = path / "retrieval.sqlite"
            first = [
                record("R:TEST001", "Наблюдаемость и графы", "проверяемая модель F1"),
                record("R:TEST002", "Signed trades", "GF5 six-motif obstructions"),
            ]
            data.write_text("".join(json.dumps(x, ensure_ascii=False) + "\n"
                                    for x in first), encoding="utf-8")
            a = sync(db, data)
            self.assertEqual((a["added"], a["total"]), (2, 2))
            self.assertEqual(sync(db, data)["unchanged"], 2)
            self.assertEqual(query(db, "графы", 5)["results"][0]["id"], "R:TEST001")
            self.assertEqual(query(db, "GF5", 5)["results"][0]["id"], "R:TEST002")
            second = [
                record("R:TEST001", "Наблюдаемость", "обновлённая версия", tags=["indexed"]),
                record("R:TEST003", "New graph study", "future citation records"),
            ]
            data.write_text("".join(json.dumps(x, ensure_ascii=False) + "\n"
                                    for x in second), encoding="utf-8")
            b = sync(db, data)
            self.assertEqual((b["added"], b["updated"], b["deleted"], b["total"]),
                             (1, 1, 1, 2))
            self.assertFalse(query(db, "GF5", 5)["results"])
            self.assertEqual(query(db, "indexed", 5)["results"][0]["id"], "R:TEST001")
            self.assertEqual(query(db, "future", 5)["results"][0]["id"], "R:TEST003")

    def test_fts_keeps_scoped_graph_backlinks_and_primary_identity(self):
        with TemporaryDirectory() as folder:
            path = Path(folder)
            data = path / "items.jsonl"
            pub = record("P:LIT-355", "Authenticated structures",
                         "primary work on authenticated updates")
            pub.update({
                "identity": "arxiv:2608.25206",
                "primary_url": "https://arxiv.org/abs/2608.25206",
                "full_proof_verified": False,
                "independent_reproduction": False,
                "neighbors_out": [
                    {"id": "R:ML-002", "relation": "MAPS_TO_RESEARCH",
                     "evidence_path": "docs/research/catalog/literature.json"},
                    {"id": "TAG:crypto", "relation": "TAGGED_WITH",
                     "evidence_path": "docs/research/catalog/literature.json"}
                ],
                "neighbors_in": []
            })
            data.write_text(json.dumps(pub, ensure_ascii=False) + "\n",
                            encoding="utf-8")
            sync(path / "index.sqlite", data)
            result = query(path / "index.sqlite", "Authenticated", 2)["results"][0]
            self.assertEqual(result["id"], "P:LIT-355")
            self.assertEqual(result["identity"], "arxiv:2608.25206")
            self.assertFalse(result["full_proof_verified"])
            self.assertEqual(len(result["neighbors_out"]), 1)
            self.assertEqual(result["neighbors_out"][0]["relation"],
                             "MAPS_TO_RESEARCH")
            self.assertEqual(result["neighbors_out"][0]["id"], "R:ML-002")

    def test_duplicate_id_rejected(self):
        with TemporaryDirectory() as folder:
            path = Path(folder)
            data = path / "items.jsonl"
            x = json.dumps(record("R:BAD", "test", "test"), ensure_ascii=False)
            data.write_text(x + "\n" + x + "\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "duplicate JSONL ID"):
                sync(path / "index.sqlite", data)

    def test_query_operators_are_lexically_escaped(self):
        with TemporaryDirectory() as folder:
            path = Path(folder)
            data = path / "items.jsonl"
            data.write_text(json.dumps(
                record("R:SAFE", "proof graph", "no new theorem"),
                ensure_ascii=False) + "\n", encoding="utf-8")
            sync(path / "index.sqlite", data)
            # Query parameters are treated as tokens, not executable FTS syntax.
            self.assertTrue(query(path / "index.sqlite", '"proof" OR graph*', 10)["results"])


if __name__ == "__main__":
    unittest.main()
