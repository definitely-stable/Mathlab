"""Independent exact GF5 miniature falsifiers and immutable W34 trace checks."""
import json
from pathlib import Path
import unittest

from hyp105_palette_fiber_transversal import (
    PALETTES, legal_replacements, local_palette_fibers,
    signed_events, predicted_remaining, exact_hitting_number,
    greedy_disjoint_witness_lower_bound,
)

ROOT = Path(__file__).parent
INDICES = (23, 5, 31, 12, 37, 20)


class PaletteFiberTransversalTests(unittest.TestCase):
    def source(self):
        return tuple(PALETTES[t] for t in INDICES)

    def test_exact_51_nonzero_checksum4_full_support(self):
        self.assertEqual(len(PALETTES), 51)
        self.assertTrue(all(len(p)==4 and all(1<=v<=4 for v in p)
                            and sum(p)%5==4 for p in PALETTES))
        out = legal_replacements(7,(0,2,4,6))
        self.assertEqual(len(out),51)
        self.assertTrue(all(sum(bool(x) for x in v)==4
                            and sum(v)%5==4 and v[1]==v[3]==v[5]==0 for v in out))
        for s in ((0,0,1,2), (0,1,2,7), (0,1,2), (0,1,2,3,4)):
            with self.assertRaises(ValueError):
                legal_replacements(7,s)

    def test_every_palette_against_independent_full_event_census(self):
        source = self.source()
        self.assertEqual(len(signed_events(source,3)), 1)
        self.assertEqual(len(signed_events(source,2)), 0)
        report = local_palette_fibers(source, 0, (0,1,2,3))
        self.assertEqual(report["old_palette"],23)
        self.assertEqual(report["bad_r3"],frozenset((9,16,22,23)))
        self.assertEqual(report["bad_r1"],frozenset((5,12,20,31,37)))
        self.assertEqual(report["bad_r2"],frozenset((2,3,13,20,27,36,44,45,47)))
        self.assertEqual(report["safe_exact_count"],34)
        self.assertEqual(report["safe_union_lower_bound"],33)
        base_r2 = signed_events(source,2)
        base_r3 = signed_events(source,3)
        for t, value in enumerate(report["legal_columns"]):
            new = list(source)
            new[0] = value
            current_r2 = signed_events(new,2)
            current_r3 = signed_events(new,3)
            h2 = sum(0 in a or 0 in b for a,b in current_r2)
            h3 = sum(0 in a or 0 in b for a,b in current_r3)
            self.assertEqual(report["h2"][t], h2)
            self.assertEqual(report["h3"][t], h3)
            expected_safe = (h3==0 and len(current_r2)<=len(base_r2)
                             and len(set(new))==len(new))
            self.assertEqual(t in report["safe"], expected_safe)
            self.assertEqual(
                len(current_r2)-len(base_r2),
                report["h2"][t]-report["h2"][23])
            self.assertEqual(
                len(current_r3)-len(base_r3),
                report["h3"][t]-report["h3"][23])
            if expected_safe:
                self.assertEqual(current_r3,
                    predicted_remaining(base_r3, (0,)))

    def test_two_consecutive_clean_edits_order_independent_event_set(self):
        original = self.source()
        initial = signed_events(original,3)
        one = list(original)
        one[0] = PALETTES[0]
        self.assertEqual(signed_events(one,3),predicted_remaining(initial,(0,)))
        r = local_palette_fibers(one,1,(0,1,2,3))
        self.assertNotIn(0,r["safe"])  # duplicate singleton with source ID 0
        self.assertIn(1,r["safe"])
        two = one[:]
        two[1] = PALETTES[1]
        self.assertEqual(signed_events(two,3),
                         predicted_remaining(initial,(0,1)))
        self.assertEqual(len(signed_events(two,2)),0)
        self.assertNotEqual(signed_events(original,3),signed_events(one,3))
        contaminated = list(original)
        contaminated[0] = PALETTES[9]
        self.assertGreater(len(signed_events(contaminated,3)),0)
        self.assertNotIn(9,local_palette_fibers(original,0,(0,1,2,3))["safe"])

    def test_conditional_cover_and_disjoint_edge_lower_bound(self):
        e1=((0,1,2),(3,4,5))
        e2=((6,7,8),(9,10,11))
        e3=((0,1),(2,3))
        self.assertEqual(exact_hitting_number((e1,e2)),2)
        self.assertEqual(greedy_disjoint_witness_lower_bound((e1,e2)),2)
        self.assertEqual(exact_hitting_number((e1,e3)),1)
        self.assertEqual(predicted_remaining((e1,e2),(0,)),frozenset((e2,)))
        self.assertEqual(predicted_remaining((e1,e2),(0,6)),frozenset())
        self.assertEqual(predicted_remaining((e1,e2),(0,6,6)),frozenset())
        with self.assertRaises(ValueError):
            exact_hitting_number(((
                tuple(range(10)),tuple(range(10,19))
            ),))

    def test_real_w34_saved_erasure_trace_necessary_partition(self):
        cert=json.loads((ROOT/"hyp105_w34_zero_incidence_erasure_certificates.json").read_text())
        self.assertEqual(cert["exact_frozen_parent_SHA"],
                         "b0be049a0899ec653a36956d363c43eb762426a2")
        expected={"lex":(27,1,54),"reverse-line":(29,0,61)}
        for name,(edits,start_r2,start_r3) in expected.items():
            z=cert["scheme_results"][name]
            trace=z["exact_global_source_palette_edit_trace"]
            self.assertEqual(len(trace),edits)
            self.assertEqual(tuple(z["starting_full_original_D2_D3_TRUE_R3"])[::2],
                             (start_r2,start_r3))
            self.assertEqual(sum(e["exact_original_signed_R3_events_removed"]
                                 for e in trace),start_r3)
            ids=[e["original_source_flag_ID"] for e in trace]
            self.assertEqual(len(set(ids)),edits)
            self.assertTrue(all(0<=i<425 for i in ids))
            self.assertTrue(all(e["exact_new_signed_six_ID_R3_events_introduced"]==0
                                for e in trace))
            self.assertEqual(tuple(z[
                "final_independently_exact_rehashed_full_original_D2_D3_TRUE_R3"
            ]),(0,0,0))
            # This checks exact trace partition arithmetic, not the separate
            # 12,704,100-triple W34 physical referee.
            remaining=start_r3
            for edit in trace:
                remaining-=edit["exact_original_signed_R3_events_removed"]
                self.assertEqual(remaining,
                    edit["complete_source_risk_after_D2_D3_R3"][2])
            self.assertEqual(remaining,0)

    def test_not_a_root_all_h_claim(self):
        source = self.source()
        with self.assertRaises(ValueError):
            local_palette_fibers(source,7,(0,1,2,3))
        with self.assertRaises(ValueError):
            local_palette_fibers(source,0,(0,0,2,3))
        modified=list(source)
        modified[0]=(0,0,0,0)
        with self.assertRaises(ValueError):
            local_palette_fibers(modified,0,(0,1,2,3))


if __name__=="__main__":
    unittest.main()
