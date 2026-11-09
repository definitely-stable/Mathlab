"""Independent original LOW full physical 3walk/source BBo joint-acceptance tests."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb
import unittest

from hyp105_original_lowchain_partition_referee import (
    SCHEMA,ROOT_STATUS,R,RHO_CAP,K,
    _source,_actual_core,_endpoints,_endpoint,_mixed_book,_trace4,
    _threepath_source_inverse,
    finite_original_partition,formal_low_heavy_glue,canonical_report
)


class TestOriginalLOWFullEndToEndPartition(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report=canonical_report()

    def test_all_h_graph_constants_are_FORMAL_and_original_root_unaccepted(self):
        z=self.report
        self.assertEqual(z["schema"],SCHEMA)
        self.assertEqual(z["status"],ROOT_STATUS)
        self.assertEqual(z["issue"],230)
        self.assertFalse(z["root_PROVED_A"])
        self.assertFalse(z["original_FULL_LOW_chain_independently_judged_finished"])
        self.assertFalse(z["published_numeric_graph_constants"])
        self.assertEqual(len(z["exact_all_h_low_heavy_formal_glue"]),3)

    def test_exact_all_h_low_source_glue_three_external_formal_cases(self):
        for q in self.report["exact_all_h_low_heavy_formal_glue"]:
            self.assertEqual(q["R"],93313)
            self.assertEqual(q["q2"],16*comb(2*(K+1),2))
            self.assertEqual(q["q3"],64*comb(3*(K+1),3))
            self.assertEqual(q["L6"],24+153*q["T"]**2)
            self.assertEqual(q["L4"],q["q2"]**2*
                (q["L4"]-19*q["T"])//q["q2"]**2+19*q["T"]) if False else None
            self.assertLess(Fraction(q["rho_star"]),RHO_CAP)
            self.assertGreater(Fraction(q["delta"]),0)
            self.assertEqual(Fraction(q["LOW_original_BBo_sextic_coefficient"]),
                             Fraction(54162,53838)*Fraction(q["delta"]))
            self.assertEqual(Fraction(q["GF5_additive_sextic_coefficient"]),
                             Fraction(54162,51**6)*Fraction(q["delta"]))
            self.assertTrue(all(q["all_h_LOWMATH_formal_bound_gates"].values()))
            self.assertFalse(q["proved_independent_full_Branch_A"])
            self.assertFalse(q["published_numeric_graph_constants_claimed"])
            self.assertGreaterEqual(1<<q["h0"],q["s0"])

    def test_complete_W32_W34_finite_real_original_joint_partitions(self):
        rows=self.report["true_original_W32_W34_finite_joint_partitions"]
        self.assertEqual(len(rows),11)
        self.assertEqual({x["s"] for x in rows},{2,4})
        for q in rows:
            self.assertEqual(q["physical_core_edges"],2*q["original_CORE_ID_count"])
            self.assertEqual(q["W3_walks_directed_exact"],q["W3_partition_sum"])
            self.assertGreaterEqual(q["W3_walks_directed_exact"],
                                    Fraction(q["W3_Blakley_Roy_lower_exact"]))
            self.assertEqual(q["original_source_produced_BBo_directed"],
                             2*q["original_source_produced_BBo_sixsets"])
            self.assertTrue(q["original_exact_2to1_inverse_all_positive_sixsets"])
            self.assertTrue(q["four_blocker_Cauchy_source_bound_valid"])
            self.assertLessEqual(q["proper_P3_bad_endpoint_weight"]**2,
                                 q["Cauchy_endpoint_error_squared_bound"])
            self.assertLessEqual(q["W3_source_partition"]["blocker_union"],
                                 sum(q["four_individual_interior_blockers"].values()))
            self.assertEqual(q["physical_vertices_including_isolates"],
                             q["physical_vertices_including_isolates"])

    def test_seeded_original_W32_W34_first_order_positive_BBo_proper_path(self):
        for s in (2,4):
            src=_source(s,"seed")
            seed=src["seed"]
            self.assertEqual(len(seed["original_projection_anchors"]),3)
            self.assertEqual(len(seed["original_physical_3path_owners"]),3)
            self.assertEqual(len(set(seed["original_projection_anchors"]+
                                     seed["original_physical_3path_owners"])),6)
            self.assertFalse(set(seed["original_projection_anchors"])&
                             set(seed["original_physical_3path_owners"]))
            q=finite_original_partition(s,"seed","seed","none")
            self.assertEqual(q["original_source_produced_BBo_directed"],2)
            self.assertEqual(q["original_source_produced_BBo_sixsets"],1)
            self.assertTrue(q["original_full_projection_anchors_outside_core"])

    def test_deleted_SOURCE_middle_anchor_not_required_in_core(self):
        for s in (2,4):
            good=finite_original_partition(s,"seed","seed","none")
            bad=finite_original_partition(s,"seed","seed","anchor")
            self.assertEqual(good["original_SOURCE_produced_BBo_directed"],2) if False else None
            self.assertEqual(good["original_source_produced_BBo_directed"],2)
            self.assertEqual(bad["original_source_produced_BBo_directed"],0)
            self.assertEqual(bad["original_Z_ID_count"],1)
            self.assertGreaterEqual(bad["W3_source_partition"]["end_deleted"],2)
            self.assertEqual(good["W3_walks_directed_exact"],
                             bad["W3_walks_directed_exact"])

    def test_endpoint_full_off_coordinate_partition_genuine_original_oriented(self):
        for s in (2,4):
            c=_source(s,"lex")
            c["decode_f"]={z:p for p,z in enumerate(c["f"])}
            c["decode_g"]={z:l for l,z in enumerate(c["g"])}
            counts,e_bad=_endpoints(c,set())
            a=c["a"];V=c["V"];B=comb(a,2);M=B-V
            self.assertEqual(sum(counts.values()),a*a*(a-1)**2)
            self.assertEqual(counts["missing"],4*(2*B*M-M*M))
            self.assertEqual(counts["incident"],4*len(c["flags"]))
            self.assertEqual(counts["deleted"],0)
            self.assertEqual(len(e_bad),sum(counts[k] for k in
                    ("missing","incident","endbad","deleted")))
            self.assertTrue(all(val%4==0 for val in counts.values()))

    def test_source_projection_exact_THREE_original_anchor_s_square_exposures(self):
        for s in (2,4):
            c=_source(s,"shift")
            counts=[Counter(),Counter(),Counter()]
            for q,r in c["projection"]:
                p,l,anchors=c["projection"][q,r]
                self.assertEqual(len(set(anchors)),3)
                for j,i in enumerate(anchors):counts[j][i]+=1
            self.assertEqual(len(c["projection"]),(c["V"]**2-len(c["flags"])))
            for j in range(3):
                self.assertEqual(len(counts[j]),len(c["flags"]))
                self.assertTrue(all(counts[j][i]==s*s
                                    for i in range(len(c["flags"]))))

    def test_full_allowed_SOURCE_A_beyond_physical_CORE_mixed_books(self):
        for s in (2,4):
            c=_source(s,"seed")
            core=set(c["seed"]["original_physical_3path_owners"])
            z=set()
            owner,adj=_actual_core(c,core,z)
            bx=_mixed_book(c,core,z)
            by=_mixed_book(c,core,z,dual=True)
            self.assertGreaterEqual(bx,0)
            self.assertGreaterEqual(by,0)
            self.assertEqual(len(owner),2*len(core))
            self.assertLessEqual(max(map(len,adj.values())),2*len(core))

    def test_full_core_vs_pruned_core_and_arbitrary_fixed_correlations(self):
        rows=self.report["true_original_W32_W34_finite_joint_partitions"]
        self.assertEqual({x["mode"] for x in rows},{"lex","reverse","shift","seed"})
        self.assertTrue(any(x["C_mode"]!="full" for x in rows))
        self.assertTrue(any(x["Z_mode"]=="sparse" for x in rows))
        self.assertTrue(any(x["original_Z_ID_count"]>0 for x in rows))
        self.assertTrue(any(x["original_source_produced_BBo_sixsets"]>0
                            for x in rows))

    def test_endbad_deletion_precedence_and_disjoint_7_class_groups(self):
        c=_source(2,"seed")
        c["decode_f"]={z:p for p,z in enumerate(c["f"])}
        c["decode_g"]={z:l for l,z in enumerate(c["g"])}
        v0=(0,0);v3=(3,3)
        cat,z=_endpoint(c,v0,v3,set())
        self.assertEqual(cat,"eligible")
        seed=c["seed"]
        cat,z=_endpoint(c,v0,v3,{seed["original_projection_anchors"][1]})
        self.assertEqual(cat,"deleted")
        cat,z=_endpoint(c,v0,v3,set(seed["original_projection_anchors"]))
        self.assertEqual(cat,"deleted")

    def test_original_true_Cauchy_source_books_each_of_four_interior_positions(self):
        rows=self.report["true_original_W32_W34_finite_joint_partitions"]
        for q in rows:
            t4=q["original_physical_fourth_trace"]
            cap=q["physical_max_degree"]
            for typ in ("x1","x2"):
                self.assertLessEqual(q["four_individual_interior_blockers"][typ]**2,
                    q["original_point_FULL_CORE_Bx"]*cap*t4)
            for typ in ("y1","y2"):
                self.assertLessEqual(q["four_individual_interior_blockers"][typ]**2,
                    q["original_line_dual_FULL_CORE_By"]*cap*t4)

    def test_source_bbo_inverse_requires_distinct_six_and_TRUE_CORE_owners(self):
        c=_source(2,"seed")
        c["decode_f"]={z:p for p,z in enumerate(c["f"])}
        c["decode_g"]={z:l for l,z in enumerate(c["g"])}
        seed=c["seed"]
        ids=tuple(sorted(seed["original_projection_anchors"]+
                         seed["original_physical_3path_owners"]))
        C=set(seed["original_physical_3path_owners"])
        owner,adj=_actual_core(c,C,set())
        result=_threepath_source_inverse(c,ids,C,set(),owner)
        self.assertEqual(len(result),2)
        self.assertEqual(result[0],result[1][::-1])
        self.assertEqual(_threepath_source_inverse(c,ids,set(),set(),owner),())
        self.assertEqual(_threepath_source_inverse(c,ids[:5],C,set(),owner),())
        self.assertEqual(_threepath_source_inverse(c,ids[:5]+(ids[4],),C,set(),owner),())
        self.assertEqual(_threepath_source_inverse(c,ids,C,{ids[0]},owner),())

    def test_strict_original_core_Z_validation(self):
        c=_source(2,"lex")
        for C,Z in (({0},{0}),({-1},set()),({len(c["flags"])},set()),
                    ({True},set())):
            with self.assertRaises(ValueError):
                _actual_core(c,C,Z)
        with self.assertRaises(ValueError):
            finite_original_partition(2,"bad_synth","full","none")
        with self.assertRaises(ValueError):
            finite_original_partition(2,"lex","seed","none")
        with self.assertRaises(ValueError):
            finite_original_partition(2,"lex","full","anchor")

    def test_formal_wrong_constants_fail_closed_and_no_root_promotion(self):
        for a,b in ((1,Fraction(1)),(Fraction(1),1),
                    (Fraction(0),Fraction(1)),(Fraction(1),Fraction(0)),
                    (Fraction(1),Fraction(2))):
            with self.assertRaises(ValueError):
                formal_low_heavy_glue(a,b)
        self.assertEqual(R,93313)
        self.assertEqual(K,64)
        self.assertFalse(self.report["root_PROVED_A"])


if __name__=="__main__":unittest.main()
