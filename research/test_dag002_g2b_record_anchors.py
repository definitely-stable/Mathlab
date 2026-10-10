"""Independent finite oracles for DAG-002 G2-B1."""
import unittest
from dag002_g2b_record_anchors import IndexedDAG, demo, fan_in_comparison, source_reach


class RecordAnchorTests(unittest.TestCase):
    def test_every_five_vertex_dag_and_published_old_labels(self):
        pairs = [(u, v) for v in range(5) for u in range(v)]
        for bits in range(1 << len(pairs)):
            parents = tuple(tuple(u for k, (u, t) in enumerate(pairs)
                                  if t == v and bits & (1 << k))
                            for v in range(5))
            for cap in (1, 3, 8, None):
                db = IndexedDAG(page_bytes=16, horizon=16, depth_cap=cap)
                old_images = []
                for v, parent_set in enumerate(parents):
                    db.append(parent_set)
                    self.assertEqual(db.records[:v], old_images)
                    old_images = db.records.copy()
                    for u in range(v + 1):
                        for t in range(v + 1):
                            actual, pages = db.query(u, t)
                            self.assertEqual(actual, source_reach(parents, u, t),
                                             (bits, cap, u, t))
                            self.assertGreaterEqual(pages, 0)
                if cap is not None:
                    self.assertLessEqual(db.report()["max_anchor_depth"], cap)

    def test_fan_in_countermodel(self):
        d = fan_in_comparison()
        plain, anchored = d["no_anchor"], d["record_anchor_D3"]
        self.assertEqual(plain["vertices"], anchored["vertices"])
        self.assertEqual(plain["chains"], anchored["chains"])
        self.assertLess(anchored["label_pages"], plain["label_pages"])
        self.assertGreater(anchored["total_update_page_reads"],
                           plain["total_update_page_reads"])
        self.assertLess(anchored["total_update_page_writes"],
                        plain["total_update_page_writes"])

    def test_chain_antichain_diamond(self):
        d = demo()
        self.assertEqual(d["chain"]["vertices"], 160)
        self.assertEqual(d["chain"]["chains"], 1)
        self.assertEqual(d["antichain"]["chains"], 160)
        self.assertEqual(d["diamond"]["vertices"], 4)

    def test_parent_validation_and_query_range(self):
        db = IndexedDAG(horizon=3)
        with self.assertRaises(ValueError):
            db.append((0,))
        db.append(())
        for bad in ((0, 0), (-1,), (1,), (1, 0)):
            with self.assertRaises(ValueError):
                db.append(bad)
        with self.assertRaises(ValueError):
            db.query(0, 1)

    def test_scores_immutable_and_anchor_depth(self):
        db = IndexedDAG(seed=73, horizon=32, depth_cap=4)
        for p in ((), (), (0,), (0, 1), (2, 3)):
            db.append(p)
        before = tuple(db.records)
        db.append((4,))
        self.assertEqual(tuple(db.records[:-1]), before)
        for v, rec in enumerate(db.records):
            if rec.anchor >= 0:
                self.assertGreater(db.score(rec.anchor), db.score(v))

    def test_exact_page_address_ledgers(self):
        db = IndexedDAG(page_bytes=16, horizon=32, depth_cap=4)
        for p in ((), (0,), (1,), (0, 2), (3,)):
            db.append(p)
        self.assertEqual(sum(c.label_pages for c in db.update_log),
                         db.total_label_pages)
        for c in db.update_log:
            self.assertEqual(c.update_address_bytes,
                             (c.update_page_reads + c.update_page_writes) * (1 + 2*db.d))
            self.assertEqual(c.update_page_writes, c.label_pages + c.manifest_pages)
            self.assertGreater(c.workspace_bytes_bound, 0)


if __name__ == "__main__":
    unittest.main()
