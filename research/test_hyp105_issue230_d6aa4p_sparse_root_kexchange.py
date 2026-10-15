"""AA4-P independent physical C4 root and complete source-point k-exchange tests."""
from collections import Counter
from itertools import combinations
from math import comb
import random
import unittest

from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1b0_seven_signature import seven_census
from hyp105_issue230_d6aa4o_quintic_adversarial_swap import (
    true_original_W32_fixed_g_weighted_tensor,exact_original_BA_energy,
    exact_swap_gradient)
from hyp105_issue230_d6aa4p_sparse_root_kexchange import (
    _C4_edges_for_four_coordinates,
    exact_physically_active_source_B_supports,
    exact_sparse_original_BA_energy,
    all_coordinate_orbit_images,
    exact_distance_k_derangement_frontier,
    exact_W32_original_kexchange_report,
)


class GenuineOriginalGF5SparsePointRootTests(unittest.TestCase):
    def test_001_independent_all_W32_physical_B_supports_brute_full_5factor(self):
        rng=random.Random(2300499)
        edges=list(combinations(range(6),2))
        for scheme in ("lex","reverse","S68","S72"):
            model=fixture(1,scheme)
            f=tuple(tuple(x) for x in model["left_labels"])
            sparse=exact_physically_active_source_B_supports(f,6)
            self.assertEqual(len(sparse),45)
            for point in range(15):
                self.assertEqual(sum(ids[0]==point for ids in sparse),3)
            # Brute choose all source point four-tuples by the original
            # left-source root p, not from the new physical C4 enumeration.
            brute=set()
            for p in range(15):
                for q in combinations((u for u in range(15) if u!=p),4):
                    selected=[f[u] for u in q]
                    coords={c for e in selected for c in e}
                    degree=Counter(c for e in selected for c in e)
                    if (len(coords)==4 and all(k==2 for k in degree.values())
                            and not coords.intersection(f[p])):
                        brute.add((p,)+q)
            self.assertEqual(set(sparse),brute)
            self.assertEqual(len(brute),45)
            t=true_original_W32_fixed_g_weighted_tensor(model)
            self.assertEqual(exact_sparse_original_BA_energy(t,f),
                             exact_original_BA_energy(t,f))
            for _ in range(4):
                rng.shuffle(edges)
                x=tuple(edges)
                self.assertEqual(len(exact_physically_active_source_B_supports(x)),45)
                self.assertEqual(exact_sparse_original_BA_energy(t,x),
                                 exact_original_BA_energy(t,x))

    def test_002_true_original_all_right_GQ_same_g_K6_coordinate_symmetry(self):
        for scheme in ("S68","S72"):
            m=fixture(1,scheme)
            t=true_original_W32_fixed_g_weighted_tensor(m)
            source=tuple(tuple(e) for e in m["left_labels"])
            x=all_coordinate_orbit_images(source,6)
            self.assertEqual(len(x),720)
            self.assertEqual(len(set(x)),720)
            baseline=exact_original_BA_energy(t,source)
            self.assertTrue(all(exact_sparse_original_BA_energy(t,y)==baseline for y in x))
            self.assertEqual(m["right_labels"],fixture(1,scheme)["right_labels"])

    def test_003_every_105_exact_complete_permutation_2exchange_independent(self):
        for scheme in ("S68","S72"):
            m=fixture(1,scheme)
            t=true_original_W32_fixed_g_weighted_tensor(m)
            f=tuple(tuple(e) for e in m["left_labels"])
            f2=exact_distance_k_derangement_frontier(t,f,2)
            self.assertEqual(f2["number_of_complete_globally_injective_point_maps_checked"],105)
            self.assertEqual(f2["exact_min_delta"],min(
                exact_swap_gradient(t,f,p,q)
                for p,q in combinations(range(15),2)))
            self.assertEqual(f2["best_neighborhood_BA_internal_charge"],
                             f2["original_BA_internal_charge"]+f2["exact_min_delta"])
            self.assertTrue(f2["global_original_all_15_factor_assignment_minimum_NOT_proved"])

    def test_004_S72_genuine_45support_k2_k3_k4_exhaustive_full_injection(self):
        m=fixture(1,"S72")
        t=true_original_W32_fixed_g_weighted_tensor(m)
        f=tuple(tuple(e) for e in m["left_labels"])
        result=[exact_distance_k_derangement_frontier(t,f,k) for k in (2,3,4)]
        self.assertEqual([r["number_of_complete_globally_injective_point_maps_checked"]
                          for r in result],[105,910,12285])
        self.assertEqual(result[0]["original_BA_internal_charge"],23)
        self.assertGreaterEqual(result[0]["best_neighborhood_BA_internal_charge"],23)
        self.assertEqual(result[0]["strictly_improving_full_maps"],0)
        self.assertEqual(sum(r["number_of_complete_globally_injective_point_maps_checked"]
                             for r in result),13300)
        for r in result:
            self.assertGreaterEqual(r["best_neighborhood_BA_internal_charge"],0)
            self.assertTrue(r["full_exact_k_permutation_neighborhood_checked"])
            self.assertEqual(len({tuple(e) for e in r["best_global_point_labels"]}),15)
            self.assertEqual(len(r["best_changed_original_source_point_IDs"]),
                             r["exact_support_changed_source_points"])
            self.assertEqual(
                sum(tuple(a)!=tuple(b) for a,b in zip(f,r["best_global_point_labels"])),
                r["exact_support_changed_source_points"])
            self.assertEqual(exact_original_BA_energy(t,r["best_global_point_labels"]),
                             r["best_neighborhood_BA_internal_charge"])
            self.assertEqual(sum(r[key] for key in (
                "strictly_improving_full_maps","equal_cost_full_maps","worse_full_maps")),
                r["number_of_complete_globally_injective_point_maps_checked"])

    def test_005_original_historical_62370_seven_GF5_vs_every_k_neighborhood_winner(self):
        for scheme in ("S68","S72"):
            x=exact_W32_original_kexchange_report(scheme)
            self.assertEqual(x["scheme"],scheme)
            self.assertTrue(x["original_right_g_UNCHANGED_across_all_complete_point_maps"])
            self.assertEqual(x["physical_B_supports_per_complete_K6_point_map"],45)
            self.assertEqual(x["source_root_C4_candidates_per_actual_original_point"],3)
            self.assertEqual(x["all_source_coordinate_S6_orbit_size"],720)
            self.assertEqual(x["source_coordinate_action_exact_BA_charge_invariance"],"PASS")
            self.assertEqual(x["baseline_full_original_positive_GF5_seven_S"],
                             {"S68":68,"S72":72}[scheme])
            self.assertEqual(len(x["exact_distances_2_3_4_full_injection_neighborhood"]),3)
            self.assertTrue(x["all_13300_nonidentity_k_le_4_full_injections_checked"])
            self.assertFalse(x["all_15_source_global_minimum_certified"])
            rows=x["exact_distances_2_3_4_full_injection_neighborhood"]
            self.assertEqual([r["best_neighborhood_BA_internal_charge"] for r in rows][1:],
                             {"S68":[25,22],"S72":[21,17]}[scheme])
            self.assertEqual(rows[1]["strictly_improving_full_maps"],
                             {"S68":129,"S72":3}[scheme])
            self.assertEqual(rows[2]["strictly_improving_full_maps"],
                             {"S68":1446,"S72":29}[scheme])
            self.assertEqual(rows[2]["historical_full_original_seven_GF5_positive_Q_at_k_frontier"],
                             {"S68":91,"S72":92}[scheme])
            self.assertEqual(x["minimum_improving_source_exchange_support_size_within_2_3_4"],
                             {"S68":2,"S72":3}[scheme])
            for q in x["exact_distances_2_3_4_full_injection_neighborhood"]:
                self.assertEqual(q["full_dense_5_source_quintic_oracle"],"PASS")
                self.assertEqual(q["full_original_62370_sixset_GF5_oracle"],"PASS")
                self.assertGreaterEqual(q["historical_full_original_seven_GF5_positive_Q_at_k_frontier"],1)

    def test_006_all_h_physical_C4_predicate_counterexample_rejections(self):
        self.assertEqual(len(_C4_edges_for_four_coordinates((0,1,2,3))),3)
        for c in _C4_edges_for_four_coordinates((0,1,2,3)):
            self.assertEqual(len(c),4)
            self.assertEqual(len(set(c)),4)
            for v in range(4):
                self.assertEqual(sum(v in edge for edge in c),2)
        for bad in ((0,1,1,2),(2,1,3,4),(-1,2,3,4)):
            with self.assertRaises(ValueError):
                _C4_edges_for_four_coordinates(bad)
        m=fixture(1,"S72")
        with self.assertRaises(ValueError):
            exact_physically_active_source_B_supports(
                tuple(m["left_labels"])[:-1]+(m["left_labels"][0],))
        with self.assertRaises(ValueError):
            exact_physically_active_source_B_supports(m["left_labels"],5)
        with self.assertRaises(ValueError):
            exact_physically_active_source_B_supports(m["left_labels"][:-1]+
                                                      ((3,3),))
        t=true_original_W32_fixed_g_weighted_tensor(m)
        with self.assertRaises(ValueError):
            exact_distance_k_derangement_frontier(t,m["left_labels"],5)
        with self.assertRaises(ValueError):
            exact_distance_k_derangement_frontier(t,m["left_labels"],True)


if __name__=="__main__":
    unittest.main()
