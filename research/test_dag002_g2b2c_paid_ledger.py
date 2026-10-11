"""Common ledger: exact byte images, query correctness and no free-oracle claims."""
import unittest

from dag002_g2b2c_paid_ledger import (
    CommonLedger, PageImageStore, decode_label, decode_parents,
    encode_label, encode_parents, run_case,
)


class ChargedLedgerTests(unittest.TestCase):
    def test_page_transfer_counters_and_immutable_keys(self):
        for page in (16, 64, 4096):
            store = PageImageStore(page)
            self.assertEqual(store.write("x", b"a" * (page + 1)), 2)
            self.assertEqual(store.read("x"), b"a" * (page + 1))
            self.assertEqual(store.read_pages, 2)
            self.assertEqual(store.write_pages, 2)
            self.assertEqual(store.read_address_bytes, 16)
            self.assertEqual(store.write_payload_bytes, 2 * page)
            with self.assertRaises(ValueError):
                store.write("x", b"different")
            store.write("manifest", b"a", immutable=False)
            store.write("manifest", b"new", immutable=False)
            self.assertEqual(store.read("manifest"), b"new")

    def test_source_codec_validates_lengths(self):
        for parents in ((), (0,), (0, 2, 5)):
            self.assertEqual(decode_parents(encode_parents(parents)), parents)
        with self.assertRaises(ValueError):
            decode_parents(b"\x02\x00")
        with self.assertRaises(ValueError):
            decode_label(b"\0" * 21)

    def test_all_64_four_vertex_dags_three_modes_two_page_sizes(self):
        edges = [(u, v) for v in range(4) for u in range(v)]
        for mask in range(1 << len(edges)):
            trace = tuple(
                tuple(u for i, (u, dest) in enumerate(edges)
                      if dest == v and mask & (1 << i))
                for v in range(4))
            for page in (16, 64):
                rows = run_case(trace, page)
                self.assertEqual(set(rows), set(CommonLedger.MODES))
                for row in rows.values():
                    self.assertEqual(row["vertices"], 4)
                    self.assertEqual(row["source_parent_bytes"],
                                     sum(2 + 4 * len(p) for p in trace))
                    self.assertEqual(row["page_bytes"], page)
                    self.assertGreater(row["update_write_pages_charged"], 0)
                self.assertEqual(rows["bitmap"]["auxiliary_support_bytes"], 0)
                self.assertGreater(rows["felsner_power"]["auxiliary_support_bytes"], 0)
                self.assertTrue(rows["felsner_power"]["unpriced_update_ancestor_oracle"])

    def test_old_query_semantics_and_append_source_immutability(self):
        db = CommonLedger("felsner_power", 8, 16)
        for p in ((), (), (0,), (1,), (2, 3)):
            before = {k: v for k, v in db.store.images.items()
                      if k in db.store.immutable}
            db.append(p)
            for key, value in before.items():
                self.assertEqual(db.store.images[key], value)
        before_query = db.store.write_pages
        for u in range(5):
            for v in range(5):
                self.assertIsInstance(db.query(u, v)[0], bool)
        self.assertEqual(db.store.write_pages, before_query)
        self.assertEqual(db.report()["parent_input_bits"], 10)

    def test_query_cannot_access_hidden_reference_parent_lists(self):
        trace = ((), (), (0,), (1,), (2, 3))
        for mode in CommonLedger.MODES:
            db = CommonLedger(mode, len(trace), 64)
            for p in trace:
                db.append(p)
            db.parents = [()] * len(trace)  # query must use page images only
            self.assertTrue(db.query(0, 4)[0])
            self.assertTrue(db.query(1, 4)[0])
            self.assertFalse(db.query(4, 0)[0])

    def test_reports_do_not_claim_cross_model_physical_dominance(self):
        trace = ((), (), (0, 1), (2,), (2, 3))
        rows = run_case(trace)
        self.assertFalse(any(x["claims_physical_device_io"] for x in rows.values()))
        self.assertEqual(rows["felsner_power"]["verdict"],
                         "INCOMPLETE_COMPARATOR_IF_UNPRICED_ORACLE")
        self.assertEqual(rows["lazy"]["verdict"], "FULLY_BILLED_ABSTRACT_PAGE_IMAGES")
        self.assertEqual(rows["bitmap"]["verdict"], "FULLY_BILLED_ABSTRACT_PAGE_IMAGES")
        self.assertEqual(
            rows["felsner_power"]["total_live_logical_bytes"],
            sum(rows["felsner_power"][key] for key in (
                "source_parent_bytes", "index_label_bytes",
                "auxiliary_support_bytes", "mutable_manifest_bytes")))


if __name__ == "__main__":
    unittest.main()
