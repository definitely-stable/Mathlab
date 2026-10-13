"""Definition-level original six-incidence transfer gates for JPKC-004."""
import unittest
from collections import Counter

from hyp105_issue230_projection import ProjectionClosure, fixture
from hyp105_issue230_jpkc004_original_sixset_transport import (
    KINDS,STATES,_degrees,_two_regular,_closure_obstruction,
    transport_certificate,
)


class JPKC004Tests(unittest.TestCase):
    def test_true_W32_all_four_global_maps_reconcile_endpoint_collisions(self):
        expected={
            "lex":(786,1456,259),
            "reverse":(676,1060,169),
            "S68":(544,444,68),
            "S72":(600,624,72),
        }
        for scheme,(E,KE,S) in expected.items():
            with self.subTest(scheme=scheme):
                row=transport_certificate(fixture(1,scheme),compare_seven=True)
                self.assertEqual(row["endpoint_bad_original_path_count"],E)
                self.assertEqual(row["endpoint_bad_ordered_collisions"],KE)
                self.assertEqual(row["original_W32_true_seven_S"],S)
                self.assertEqual(sum(row["physical_collision_kinds"].values()),KE)
                self.assertEqual(sum(sum(rec.values()) for rec in
                                     row["original_sixset_provenance_partition"].values()),KE)
                self.assertTrue(row["J9_direct_GQ_closure_no_GF5_2reg"])
                self.assertTrue(row["JPKC003_endpoint_moment_independently_reconciled"])
                self.assertLessEqual(
                    row["max_disjoint_cycle_ordered_witnesses_per_original_sixset"],768)
                self.assertFalse(row["Root_A_PROVED"])
                self.assertIsNotNone(row["GF5_seven_W32_exact_accepted_witnesses"])

    def test_true_W34_lex_random_exact_source_transport_does_not_fake_GF5(self):
        for scheme,E,KE in (("lex",38020,128912),
                            ("random",30194,87996)):
            with self.subTest(scheme=scheme):
                row=transport_certificate(fixture(2,scheme))
                self.assertEqual(row["endpoint_bad_original_path_count"],E)
                self.assertEqual(row["endpoint_bad_ordered_collisions"],KE)
                self.assertIsNone(row["GF5_seven_W32_exact_accepted_witnesses"])
                self.assertFalse(row["GF5_seven_all_h_classifier_available"])
                self.assertEqual(sum(row["physical_collision_kinds"].values()),KE)
                self.assertLessEqual(
                    row["max_disjoint_cycle_ordered_witnesses_per_original_sixset"],768)

    def test_original_D4_true_spread_full_endpoint_transport(self):
        from hyp105_issue230_jpkc_spread_adversary import spread_adversary_model
        model,proof=spread_adversary_model(2)
        self.assertEqual(proof["M_f_original_exact"],259)
        row=transport_certificate(model)
        self.assertEqual(row["endpoint_bad_original_path_count"],35190)
        self.assertEqual(row["endpoint_bad_ordered_collisions"],116600)
        self.assertTrue(row["J9_direct_GQ_closure_no_GF5_2reg"])

    def test_J9_original_GQ_endpoint_shared_coordinate_forces_degree_three(self):
        # Checks all original nonincident projection anchors, without
        # ever sampling random sign patterns or independently redrawing maps.
        for scheme in ("lex","reverse","S68","S72"):
            c=ProjectionClosure(fixture(1,scheme))
            seen=0
            for (q,r),(p,l) in c.projection.items():
                L=bool(set(c.f[q]) & set(c.f[p]))
                R=bool(set(c.g[r]) & set(c.g[l]))
                if not (L or R):
                    continue
                anchor=(c.edge_id[q,l],c.edge_id[p,l],c.edge_id[p,r])
                left=_degrees(c,anchor,0)
                right=_degrees(c,anchor,1)
                if L:
                    self.assertGreaterEqual(max(left.values()),3)
                if R:
                    self.assertGreaterEqual(max(right.values()),3)
                seen+=1
            self.assertGreater(seen,0)

    def test_independent_source_witnesses_and_partition_fail_closed(self):
        row=transport_certificate(fixture(1,"lex"),compare_seven=True,
                                  include_witnesses=True)
        for kind in KINDS:
            self.assertEqual(sum(row["original_sixset_provenance_partition"][kind].values()),
                             row["physical_collision_kinds"][kind])
        for w in row["original_witness_examples"].values():
            ids=w["original_six"]
            self.assertTrue(len(ids)<=6)
            self.assertEqual(len(w["path1_original"]),3)
            self.assertEqual(len(w["path2_original"]),3)
            self.assertTrue(set(w["original_six"])<=
                            set(w["path1_original"]+w["path2_original"]))
        with self.assertRaisesRegex(ValueError,"path budget"):
            transport_certificate(fixture(1,"lex"),max_paths=1)
        with self.assertRaisesRegex(ValueError,"pair budget"):
            transport_certificate(fixture(1,"lex"),max_ordered_pairs=1)
        with self.assertRaisesRegex(ValueError,"cache budget"):
            transport_certificate(fixture(1,"lex"),max_unique_sixsets=1)
        with self.assertRaisesRegex(ValueError,"W32"):
            transport_certificate(fixture(2,"lex"),compare_seven=True)
        m=fixture(1,"lex")
        left=list(m["left_labels"]);left[0]=left[1]
        m["left_labels"]=tuple(left)
        with self.assertRaises(ValueError):
            transport_certificate(m)

    def test_J10_injective_two_diagonal_cap_and_j9_scope(self):
        # Each physical graph edge has ONE unique original incidence;
        # each original incidence creates exactly TWO graph edges.
        c=ProjectionClosure(fixture(1,"lex"))
        counts=Counter()
        for u,neighbors in enumerate(c.adj):
            for v,inc in neighbors:
                if u<v:
                    counts[inc]+=1
        self.assertEqual(set(counts),set(range(len(c.edges))))
        self.assertEqual(set(counts.values()),{2})
        self.assertEqual(12*(2**6),768)
        q,r=next(iter(c.projection))
        if (set(c.f[q])&set(c.f[c.projection[q,r][0]]) or
                set(c.g[r])&set(c.g[c.projection[q,r][1]])):
            _closure_obstruction(c,q,r,(0,1,2))
        else:
            with self.assertRaisesRegex(AssertionError,"endpoint-bad"):
                _closure_obstruction(c,q,r,(0,1,2))


if __name__=="__main__":
    unittest.main()
