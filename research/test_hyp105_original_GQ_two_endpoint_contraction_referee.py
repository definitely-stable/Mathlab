"""Independent genuine ORIGINAL W32/W34 two-endpoint source contraction tests."""
from collections import defaultdict
from fractions import Fraction
from itertools import islice
import unittest

from hyp105_original_GQ_two_endpoint_contraction_referee import (
    SCHEMA,ROOT_STATUS,CASES,_oriented_source_pair_star,
    _true_source_two_endpoint_shadow_one_bin,
    _independent_direct_physical_orientation_source_shadow,
    _full_original_source_two_endpoint_case,canonical_report
)
from hyp105_original_full_w34_weighted_risk_referee import (
    _source,_true_original_proper_P3
)


class TestOriginalGQTwoEndpointSourceContraction(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report=canonical_report()
        cls.rows=cls.report["eight_complete_genuine_ORIGINAL_W32_W34_two_endpoint_spectral_cases"]

    def test_scientific_scope_and_frozen_root_nonacceptance(self):
        z=self.report
        self.assertEqual(z["schema"],SCHEMA)
        self.assertEqual(z["issue"],230)
        self.assertEqual(z["status"],ROOT_STATUS)
        for key in (
            "classical_GQ_real_incidence_spectrum_not_claimed_novel",
            "all_h_original_CORRELATED_two_endpoint_GQ_incidence_weighted_projection_contraction",
            "all_h_all_source_retained_and_full_GQ_shadow_ordering",
            "all_h_original_weighted_centered_GQ_two_endpoint_spectral_upper",
            "all_h_original_two_endpoint_physical_coupling_defect_nonnegative",
            "all_h_original_P3_endpoint_count_square_Frobenius_shadow_upper"
        ):
            self.assertTrue(z[key])
        for key in ("all_h_root_GLOBAL_original_P3_B75_proved",
                    "all_h_root_original_six_motif_S_s_floor_proved",
                    "original_HEAVY_LOW_GF5_complete_claimed",
                    "ASET_exponent_claimed","root_PROVED_A"):
            self.assertFalse(z[key])

    def test_complete_true_original_finite_source_census_not_sampled(self):
        self.assertEqual(len(self.rows),8)
        self.assertEqual([(r["original_s"],r["original_label_scheme"],
                           r["original_retained_CORE"]) for r in self.rows],list(CASES))
        self.assertEqual([r["exact_TRUE_original_proper_directed_P3s"] for r in self.rows],
                         [1346,1154,838,83892,82846,79404,9966,66418])
        self.assertEqual(
            [r["max_original_true_proper_P3s_same_endpoint_bin"] for r in self.rows],
            [9,7,8,16,21,17,6,14])
        for row in self.rows:
            self.assertEqual(row["original_actual_physical_edges"],
                             2*row["original_named_retained_CORE_flags"])
            self.assertTrue(row["true_source_GQ_full_core_retained_proper_path_conservation"])

    def test_all_h_two_coordinate_orientation_vector_exact_cases(self):
        pairs=((0,1),(0,2),(1,2),(2,3),(3,4))
        self.assertEqual(
            _oriented_source_pair_star(pairs,{1,2,3},{1,2,3},5,6),
            (2,2,2,2,0))
        self.assertEqual(
            _oriented_source_pair_star(pairs,{0,2},{1,3},4,5),
            (1,0,1,1,0))
        self.assertEqual(
            _oriented_source_pair_star(pairs,{0,2},{1,3},3,3),
            (0,0,0,0,0))
        self.assertEqual(
            _oriented_source_pair_star(pairs,{0,2},{1,3},0,5),
            (0,0,0,0,0))

    def test_every_source_all_h_exact_inequality_chain(self):
        for row in self.rows:
            z=row["max_real_original_P3_endpoint_witness"]
            self.assertGreater(z["actual_proper_P3"],0)
            self.assertLessEqual(z["actual_proper_P3"],
                z["source_retained_CORE_projection_orientation_shadow"])
            self.assertLessEqual(z["source_retained_CORE_projection_orientation_shadow"],
                z["source_full_GQ_projection_orientation_shadow"])
            self.assertLessEqual(z["source_full_GQ_projection_orientation_shadow"],
                z["source_WEIGHTED_centered_GQ_spectral_shadow_upper"])
            self.assertLessEqual(z["actual_proper_P3"],
                z["source_endpoint_actual_degree_product_upper"])
            self.assertEqual(z["source_full_shadow_to_retained_deleted_incidence_gap"],
                z["source_full_GQ_projection_orientation_shadow"]-
                z["source_retained_CORE_projection_orientation_shadow"])
            self.assertEqual(z["source_retained_shadow_to_true_physical_coupling_defect"],
                z["source_retained_CORE_projection_orientation_shadow"]-
                z["actual_proper_P3"])
            self.assertGreaterEqual(z["source_weighted_GQ_mixing_squared_slack"],0)
            self.assertTrue(z["all_h_source_orientation_phi_psi_range_0_to_2"])

    def test_every_SOURCE_all_h_true_two_endpoint_shadow_Frobenius_moment(self):
        for r in self.rows:
            m=r["exact_full_two_endpoint_source_moments"]
            n2=r["exact_original_proper_P3_endpoint_count_square"]
            self.assertEqual(m["source_actual_proper_path_count_square"],n2)
            self.assertEqual(m["source_actual_proper_path_count"],
                             r["exact_TRUE_original_proper_directed_P3s"])
            for key in ("degree_product_upper_square_sum",
                        "retained_middle_projection_upper_square_sum",
                        "spectral_middle_projection_upper_square_sum",
                        "degree_and_retained_upper_square_sum",
                        "degree_and_spectral_upper_square_sum"):
                self.assertGreaterEqual(m[key],n2)
            self.assertEqual(
                m["source_full_GQ_projection_orientation_shadow"],
                m["source_retained_CORE_projection_orientation_shadow"]+
                m["source_full_shadow_to_retained_deleted_incidence_gap"])
            self.assertEqual(
                m["source_retained_CORE_projection_orientation_shadow"],
                m["source_actual_proper_path_count"]+
                m["source_retained_shadow_to_true_physical_coupling_defect"])

    def test_independent_every_original_W32_middle_orientation_shadow_and_real_P3(self):
        # Independent DIRECT every ORIGINAL named middle incidence flag
        # and all FOUR physically directed diagonals on every W32 endpoint
        # with nonzero proper paths. Does NOT call phi/psi source moments.
        for s,sch,core in CASES[:3]:
            c=_source(s,sch,core)
            byend=defaultdict(int)
            for p,owners in _true_original_proper_P3(c):
                byend[(p[0],p[-1])]+=1
            for ends,n in byend.items():
                orient,real=_independent_direct_physical_orientation_source_shadow(c,ends)
                z=_true_source_two_endpoint_shadow_one_bin(c,ends,n)
                self.assertEqual(orient,z[
                    "source_retained_CORE_projection_orientation_shadow"])
                self.assertEqual(real,n)

    def test_independent_W34_all_three_full_schemes_orientation_physical(self):
        # Deterministic true original endpoint corpus, including the
        # maximum-family witness from each source, not synthetic owners.
        for r in self.rows[3:6]:
            c=_source(4,r["original_label_scheme"],"full")
            byend=defaultdict(int)
            for p,owners in _true_original_proper_P3(c):
                byend[(p[0],p[-1])]+=1
            worst=r["max_real_original_P3_endpoint_witness"]
            w=tuple(map(tuple,worst["ordered_physical_endpoints"]))
            chosen=set(islice(sorted(byend),80))|{w}
            for ends in chosen:
                raw,exact=_independent_direct_physical_orientation_source_shadow(c,ends)
                z=_true_source_two_endpoint_shadow_one_bin(c,ends,byend[ends])
                self.assertEqual(raw,z[
                    "source_retained_CORE_projection_orientation_shadow"])
                self.assertEqual(exact,byend[ends])

    def test_inclusion_real_full_vs_retained_original_pruning_source(self):
        for r in self.rows:
            m=r["exact_full_two_endpoint_source_moments"]
            self.assertGreaterEqual(m["source_full_shadow_to_retained_deleted_incidence_gap"],0)
            if r["original_retained_CORE"]=="full":
                self.assertEqual(m["source_full_shadow_to_retained_deleted_incidence_gap"],0)
            else:
                # Pruning of actual original incidence sources MAY not
                # hit the projected endpoint labels, but these fixtures do.
                self.assertGreater(m["source_full_shadow_to_retained_deleted_incidence_gap"],0)
            self.assertGreaterEqual(m["source_retained_shadow_to_true_physical_coupling_defect"],0)

    def test_exact_WEIGHTED_integer_GQ_centered_mixing_squared_oracle(self):
        for r in self.rows:
            z=r["max_real_original_P3_endpoint_witness"]
            V=(r["original_s"]+1)*(r["original_s"]**2+1)
            s=r["original_s"]
            a=z["source_phi_sum"];b=z["source_psi_sum"]
            X=z["source_phi_square_sum"];Y=z["source_psi_square_sum"]
            e=z["source_full_GQ_projection_orientation_shadow"]
            d=V*e-(s+1)*a*b
            rad=2*s*(V*X-a*a)*(V*Y-b*b)
            self.assertLessEqual(d*d,rad)
            self.assertEqual(z["source_weighted_GQ_mixing_deviation"],d)
            self.assertEqual(z["source_weighted_GQ_mixing_squared_slack"],rad-d*d)
            self.assertEqual(z["source_WEIGHTED_centered_GQ_spectral_shadow_upper"],
                ((s+1)*a*b+__import__("math").isqrt(rad))//V)

    def test_real_source_two_endpoint_strict_or_not_informative_is_not_invented(self):
        for r in self.rows:
            counts=r["counts"]
            bins=counts["nonempty_ordered_physical_proper_P3_endpoint_bins"]
            self.assertGreater(bins,0)
            self.assertLessEqual(
                counts.get("bins_retained_source_shadow_strictly_beats_degree_product",0),bins)
            self.assertLessEqual(
                counts.get("bins_spectral_GQ_shadow_strictly_beats_degree_product",0),bins)
            self.assertLessEqual(
                counts.get("bins_with_NONZERO_original_two_endpoint_projection_coupling_defect",0),bins)
            self.assertEqual(r["max_original_true_proper_P3s_same_endpoint_bin"],
                             r["max_real_original_P3_endpoint_witness"]["actual_proper_P3"])
            z=r["max_absolute_ORIGINAL_shadow_vs_degree_improvement_witness"]
            self.assertGreaterEqual(z["absolute_improvement"],0)

    def test_real_TRUE_source_witness_degree_shadow_improvements_nonnegative(self):
        for r in self.rows:
            z=r["max_absolute_ORIGINAL_shadow_vs_degree_improvement_witness"]
            d=z["source_endpoint_actual_degree_product_upper"]
            shadow=z["source_retained_CORE_projection_orientation_shadow"]
            self.assertEqual(z["absolute_improvement"],max(0,d-shadow))
            self.assertLessEqual(z["source_two_endpoint_min_degree_and_shadow_upper"],d)
            self.assertLessEqual(z["source_two_endpoint_min_degree_and_shadow_upper"],shadow)
            self.assertGreaterEqual(z["source_two_endpoint_min_degree_and_shadow_upper"],z["actual_proper_P3"])

    def test_source_strict_fail_closed_same_endpoints_invalid(self):
        c=_source(2,"lex","full")
        u=next(iter(c["adj"]))
        with self.assertRaises(AssertionError):
            _true_source_two_endpoint_shadow_one_bin(c,(u,u),0)

    def test_GQ_orientation_shadow_not_path_priority_independence(self):
        # Source output proves count/support bounds ONLY, no claim that
        # individual proper P3 selector events are independent.
        for r in self.rows:
            self.assertFalse(r["all_h_ROOT_two_endpoint_weighted_B75_proved"])
            self.assertFalse(r["root_PROVED_A"])
            self.assertLessEqual(r["max_original_true_proper_P3s_same_endpoint_bin"],
                                 r["max_original_actual_endpoint_degree_product"])
            self.assertEqual(r["original_actual_physical_edges"],
                             2*r["original_named_retained_CORE_flags"])

if __name__=="__main__":
    unittest.main()
