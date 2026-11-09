"""AA4-DICHOTOMY: true ORIGINAL all-h quantitative endpoint covariance scope."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
import unittest

from hyp105_original_compatible_path_covariance_referee import (
    SCHEMA,ROOT_STATUS,actual_source,true_proper_p3,
    _source_priority_exact,_constraint_rank,_probability,pair_dichotomy,
    endpoint_pair_audit,canonical_report
)


class TestOriginalCompatibleCovarianceDichotomy(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report=canonical_report()
        cls.c=actual_source(2,"lex","full")
        cls.paths=true_proper_p3(cls.c)
        cls.full=cls.report["independent_original_full_W32_and_sample_W34_cases"][0]

    def test_root_not_promoted_and_all_h_scope_is_explicit(self):
        q=self.report
        self.assertEqual(q["schema"],SCHEMA)
        self.assertEqual(q["status"],ROOT_STATUS)
        self.assertEqual(q["issue"],230)
        self.assertFalse(q["root_PROVED_A"])
        self.assertTrue(q["same_endpoint_factor_four_all_h_THEOREM"])
        self.assertTrue(q["negative_iff_SOURCE_or_TYPED_odd_cycle_all_h_THEOREM"])
        self.assertIn("all dyadic",q["source_quantifiers"])

    def test_exact_full_W32_genuine_original_geometry(self):
        c=self.c
        self.assertEqual(len(c["flags"]),45)
        self.assertEqual(len(c["ids"]),45)
        self.assertEqual(len(c["owner"]),90)
        self.assertEqual(len(self.paths),1346)
        self.assertLessEqual(c["source_max_J"],64)
        self.assertEqual(len(c["Z"]),0)
        for i in c["ids"]:
            self.assertEqual(sum(j==i for j in c["owner"].values()),2)
            for j in c["J"][i]:
                self.assertIn(i,c["J"][j])

    def test_true_original_source_owner_pair_conflict_free_per_path(self):
        c=self.c
        for vs,owners in self.paths:
            self.assertEqual(len(vs),4)
            self.assertEqual(len(set(owners)),3)
            self.assertEqual(len({v[0] for v in vs}),4)
            self.assertEqual(len({v[1] for v in vs}),4)
            self.assertFalse(any(j in c["J"][i] for i,j in combinations(owners,2)))

    def test_exact_all_physical_same_endpoint_W32_classification(self):
        r=self.full
        self.assertTrue(r["complete_true_original_P3_and_joint_pairs"])
        self.assertEqual(r["proper_directed_P3_scanned"],1346)
        self.assertEqual(r["physical_ordered_endpoint_bins"],624)
        self.assertEqual(r["same_end_ordered_path_pairs_audited"],4370)
        self.assertEqual(r["same_end_ordered_path_pair_classes"],{
            "compatible":2386,
            "original_J_conflict":1348,
            "original_first_factor_odd_cycle":464,
            "original_second_factor_odd_cycle":172
        })

    def test_full_W32_exact_second_moment_is_previous_independent_value(self):
        r=self.full
        self.assertEqual(Fraction(r["exact_selected_P3_second_moment"]),
                         Fraction(2464778346891846823,3826102303457280000))
        self.assertEqual(Fraction(r["exact_mean_selected_P3_norm2"]),
                         Fraction(170009657654496199,164130319761408000000))
        self.assertEqual(Fraction(r["independently_summed_original_pair_covariances"]),
                         Fraction(5489586524019325126911803,8535269018552500224000000))

    def test_full_W32_compatible_fourfold_integrated_second_floor(self):
        r=self.full
        p=Fraction(r["weighted_compatible_marginal_product"])
        broken=Fraction(r["weighted_incompatible_marginal_product"])
        tot=Fraction(r["exact_mean_selected_P3_norm2"])
        selected=Fraction(r["exact_selected_P3_second_moment"])
        self.assertEqual(p+broken,tot)
        self.assertGreater(p,0)
        self.assertGreater(broken,0)
        self.assertGreaterEqual(selected,4*p)
        self.assertEqual(Fraction(r["quantitative_color_rank_lower4"]),4*p)

    def test_true_original_three_distinct_negative_mechanism_witnesses(self):
        w=self.full["true_original_first_witnesses"]
        self.assertEqual(set(w),{"compatible","original_J_conflict",
                       "original_first_factor_odd_cycle",
                       "original_second_factor_odd_cycle"})
        for cause in ("original_J_conflict","original_first_factor_odd_cycle",
                      "original_second_factor_odd_cycle"):
            x=w[cause]
            self.assertEqual(x["cause"],cause)
            self.assertEqual(Fraction(x["joint"]),0)
            self.assertGreater(Fraction(x["marginal_a"]),0)
            self.assertGreater(Fraction(x["marginal_b"]),0)
            self.assertEqual(Fraction(x["covariance"]),
                -Fraction(x["marginal_a"])*Fraction(x["marginal_b"]))

    def test_true_original_compatible_source_witness_positive_and_fourfold(self):
        w=self.full["true_original_first_witnesses"]["compatible"]
        self.assertGreater(Fraction(w["joint"]),0)
        self.assertGreater(Fraction(w["covariance"]),0)
        self.assertGreaterEqual(Fraction(w["joint"]),
            4*Fraction(w["marginal_a"])*Fraction(w["marginal_b"]))
        self.assertGreaterEqual(Fraction(w["rank_priority_ratio"]),1)
        self.assertLessEqual(w["rank_first"],5)
        self.assertLessEqual(w["rank_second"],5)

    def test_W32_full_color_boost_distribution_contains_factor_four_or_more(self):
        hist=self.full["compatible_extra_physical_color_boost_histogram"]
        self.assertEqual(sum(hist.values()),2386)
        self.assertTrue(all(int(boost)>=1 for boost in hist))
        self.assertTrue(all(int(boost)&(int(boost)-1)==0 for boost in hist))

    def test_all_W32_full_same_end_path_pairs_have_priority_positive_association(self):
        c=self.c
        byend=defaultdict(list)
        for p in self.paths:
            byend[(p[0][0],p[0][-1])].append(p)
        observed=0
        for arr in byend.values():
            for a,b in combinations(arr,2):
                r=pair_dichotomy(a,b,c)
                if r["cause"]=="compatible":
                    self.assertGreaterEqual(r["original_priority_ratio"],1)
                    self.assertGreaterEqual(r["joint"],4*r["p_a"]*r["p_b"])
                    self.assertGreaterEqual(r["covariance"],3*r["p_a"]*r["p_b"])
                    observed+=1
        self.assertGreater(observed,0)

    def test_explicit_quantitative_factor_four_requires_same_endpoint(self):
        a=self.paths[0]
        b=next(x for x in self.paths if (x[0][0],x[0][-1])!=
               (a[0][0],a[0][-1]))
        with self.assertRaises(ValueError):
            pair_dichotomy(a,b,self.c)

    def test_original_priority_separate_from_compatible_color_gain(self):
        w=self.full["true_original_first_witnesses"]["compatible"]
        owners_a=tuple(w["original_owner_ids_a"])
        owners_b=tuple(w["original_owner_ids_b"])
        S=tuple(sorted(set(owners_a+owners_b)))
        self.assertGreaterEqual(
            _source_priority_exact(S,self.c["J"]),
            _source_priority_exact(owners_a,self.c["J"])*
            _source_priority_exact(owners_b,self.c["J"]))
        self.assertLessEqual(_constraint_rank(S,self.c,"x"),5)
        self.assertLessEqual(_constraint_rank(S,self.c,"y"),5)

    def test_complete_W32_reverse_and_adversarial_deletion_are_not_samples(self):
        arr=self.report["independent_original_full_W32_and_sample_W34_cases"]
        self.assertEqual(len(arr),6)
        for r in arr[:3]:
            self.assertEqual(r["s"],2)
            self.assertTrue(r["complete_true_original_P3_and_joint_pairs"])
            self.assertGreater(r["same_end_ordered_path_pairs_audited"],0)
            self.assertEqual(sum(r["same_end_ordered_path_pair_classes"].values()),
                             r["same_end_ordered_path_pairs_audited"])
            self.assertGreaterEqual(
                Fraction(r["exact_selected_P3_second_moment"]),
                Fraction(r["quantitative_color_rank_lower4"]))
            self.assertEqual(
                Fraction(r["exact_selected_P3_second_moment"])-
                Fraction(r["exact_mean_selected_P3_norm2"]),
                Fraction(r["independently_summed_original_pair_covariances"]))
        self.assertGreater(arr[2]["original_deleted_Z_ID_count"],0)

    def test_W34_true_original_finite_sample_adversarial_mappings(self):
        arr=self.report["independent_original_full_W32_and_sample_W34_cases"]
        for r in arr[3:]:
            self.assertEqual(r["s"],4)
            self.assertFalse(r["complete_true_original_P3_and_joint_pairs"])
            self.assertEqual(r["same_end_ordered_path_pairs_audited"],160)
            self.assertEqual(sum(r["same_end_ordered_path_pair_classes"].values()),160)
            self.assertGreaterEqual(
                Fraction(r["exact_selected_P3_second_moment"]),
                Fraction(r["quantitative_color_rank_lower4"]))
            self.assertTrue(r["actual_paired_original_physical_edges"]==
                            2*r["original_CORE_ID_count"])

    def test_genuine_source_odd_factor_not_equivalent_to_J_conflict(self):
        w=self.full["true_original_first_witnesses"]
        for name in ("original_first_factor_odd_cycle",
                     "original_second_factor_odd_cycle"):
            v=w[name]
            S=tuple(v["original_owner_ids_a"]+v["original_owner_ids_b"])
            self.assertFalse(any(j in self.c["J"][i]
                for i,j in combinations(sorted(set(S)),2)))
            self.assertGreater(_source_priority_exact(S,self.c["J"]),0)
        x=w["original_first_factor_odd_cycle"]
        self.assertIsNone(_constraint_rank(
            x["original_owner_ids_a"]+x["original_owner_ids_b"],self.c,"x"))
        y=w["original_second_factor_odd_cycle"]
        self.assertIsNone(_constraint_rank(
            y["original_owner_ids_a"]+y["original_owner_ids_b"],self.c,"y"))

    def test_independent_previous_pairrank_source_crosscheck_selected_genuine(self):
        # PREVIOUS routine is TEST-ONLY, never imported by new all-h implementation.
        from hyp105_original_selector_pair_covariance_referee import (
            true_source,exact_joint
        )
        older=true_source(2,"lex","full")
        for w in self.full["true_original_first_witnesses"].values():
            A=tuple(w["original_owner_ids_a"])
            B=tuple(w["original_owner_ids_b"])
            self.assertEqual(_probability(A,self.c),exact_joint(A,older))
            self.assertEqual(_probability(B,self.c),exact_joint(B,older))
            self.assertEqual(_probability(A+B,self.c),exact_joint(A+B,older))

    def test_invalid_nonoriginal_geometry_and_deleted_core_fail_closed(self):
        for s in (0,1,3,8):
            with self.assertRaises(ValueError):actual_source(s)
        with self.assertRaises(ValueError):actual_source(2,"invented")
        with self.assertRaises(ValueError):actual_source(2,"lex","clones")

    def test_original_probabilities_fraction_and_categorical_bound_exact(self):
        for w in self.full["true_original_first_witnesses"].values():
            a=tuple(w["original_owner_ids_a"])
            b=tuple(w["original_owner_ids_b"])
            p1=_probability(a,self.c)
            p2=_probability(b,self.c)
            p12=_probability(a+b,self.c)
            self.assertIsInstance(p12,Fraction)
            self.assertEqual(p1,Fraction(w["marginal_a"]))
            self.assertEqual(p2,Fraction(w["marginal_b"]))
            self.assertEqual(p12,Fraction(w["joint"]))
            if w["cause"]=="compatible":
                self.assertGreaterEqual(p12,4*p1*p2)
            else:
                self.assertEqual(p12,0)


if __name__=="__main__":unittest.main()
