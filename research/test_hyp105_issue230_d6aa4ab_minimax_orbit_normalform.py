"""Independent HYP-105 AA4-AB-SYM adversarial *global* orbit falsifiers."""
import random
import unittest
from itertools import combinations
from math import factorial

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4q_two_sided_seven_join import (
    exact_two_sided_original_seven_join,
)
from hyp105_issue230_d6aa4ab_minimax_orbit_normalform import (
    anchored_pair_normal_form,
    edge_to_zero_one_permutation,
    finite_W32_symmetry_certificate,
    local_original_seven_tag,
    normalized_search_cardinality,
    symplectic_transvection_source,
    transform_model,
    translate_six_original_ids,
)


class ExactAdversarialOrbitNormalFormTests(unittest.TestCase):
    def test_01_all_h_two_complete_global_anchored_search_counts(self):
        for s in (2,4,8,16,32,64):
            z = normalized_search_cardinality(s)
            k,v = z["K"],z["V"]
            self.assertEqual(z["unanchored_per_side"],
                             k*z["anchored_per_side"])
            self.assertEqual(z["two_sided_exact_search_reduction_factor"],k*k)
            self.assertEqual(z["anchored_both_side_candidate_count"],
                             z["anchored_per_side"]**2)
            self.assertTrue(z["all_h_exact_anchor_normal_form"])
            self.assertFalse(z["root_A_proved"])
        self.assertEqual(normalized_search_cardinality(2)["anchored_per_side"],
                         factorial(14))
        self.assertEqual(normalized_search_cardinality(2)[
            "two_sided_exact_search_reduction_factor"],225)

    def test_02_independent_physical_coordinate_action_and_normalization(self):
        m = fixture(1,"S68")
        cp=(5,4,3,2,1,0)
        cl=(1,2,3,4,5,0)
        changed=transform_model(m,point_coordinates=cp,line_coordinates=cl)
        self.assertEqual(changed["incidences"],m["incidences"])
        self.assertEqual(len(set(changed["left_labels"])),15)
        self.assertEqual(len(set(changed["right_labels"])),15)
        normal=anchored_pair_normal_form(changed,3,7)
        self.assertEqual(normal["left_labels"][3],(0,1))
        self.assertEqual(normal["right_labels"][7],(0,1))
        for a in range(6):
            for b in range(a+1,6):
                perm=edge_to_zero_one_permutation((a,b),6)
                self.assertEqual(tuple(sorted((perm[a],perm[b]))),(0,1))

    def test_03_true_original_symplectic_W32_W34_transvections(self):
        for h in (1,2):
            model=fixture(h,"lex")
            for seed in (0,3):
                p,l=symplectic_transvection_source(model,seed)
                v=len(p)
                self.assertEqual(len(set(p)),v)
                self.assertEqual(len(set(l)),v)
                self.assertEqual(tuple(p[p[i]] for i in range(v)),tuple(range(v)))
                self.assertEqual(tuple(l[l[i]] for i in range(v)),tuple(range(v)))
                inc=set(model["incidences"])
                self.assertEqual({(p[a],l[b]) for a,b in inc},inc)
                z=transform_model(model,point_sources=p,line_sources=l)
                self.assertEqual(z["incidences"],model["incidences"])

    def test_04_W32_full_TRUE_seven_GF5_global_join_and_weight_invariant(self):
        cert=finite_W32_symmetry_certificate("S68")
        self.assertEqual(cert["S"],68)
        self.assertEqual(cert["D6"],0)
        self.assertEqual(sum(cert["all_seven_GF5_tags"].values()),68)
        self.assertTrue(cert["true_original_global_coherence_checked"])
        self.assertGreater(cert["historical_51_palette_weighted_numerator"],0)

    def test_05_W32_independent_original_per_Q_oracle_all_accepted_motifs(self):
        model=fixture(1,"S72")
        base=exact_two_sided_original_seven_join(
            model, independent_history=False, collect=True)
        self.assertEqual(base["accepted_seven_GF5_original_S"],72)
        self.assertEqual(base["physical_A_A_genuine_D6_only"],0)
        self.assertEqual(len(base["selected_ORIGINAL_Q_tags"]),72)
        p,l=symplectic_transvection_source(model,3)
        moved=transform_model(model,point_sources=p,line_sources=l,
                              point_coordinates=(1,2,3,4,5,0),
                              line_coordinates=(5,4,3,2,1,0))
        direct=0
        for Q,tag in base["selected_ORIGINAL_Q_tags"].items():
            self.assertEqual(local_original_seven_tag(model,Q),tag)
            transported=translate_six_original_ids(model,Q,p,l)
            self.assertEqual(local_original_seven_tag(moved,transported),tag)
            direct+=1
        self.assertEqual(direct,72)

    def test_06_W34_source_geom_and_coordinate_joint_action_sample(self):
        model=fixture(2,"random")
        p,l=symplectic_transvection_source(model,7)
        m=transform_model(model,point_sources=p,line_sources=l,
                          point_coordinates=tuple(reversed(range(model["a"]))),
                          line_coordinates=tuple(range(1,model["a"]))+(0,))
        rng=random.Random(105230)
        inc=list(range(len(model["incidences"])))
        for _ in range(1200):
            Q=tuple(sorted(rng.sample(inc,6)))
            tag=local_original_seven_tag(model,Q)
            Qt=translate_six_original_ids(model,Q,p,l)
            self.assertEqual(tag,local_original_seven_tag(m,Qt))
        normal=anchored_pair_normal_form(m,4,11)
        self.assertEqual(normal["left_labels"][4],(0,1))
        self.assertEqual(normal["right_labels"][11],(0,1))

    def test_07_fail_closed_invalid_nonautomorphism_and_injection(self):
        model=fixture(1,"S68")
        p=list(range(15));p[0],p[1]=p[1],p[0]
        with self.assertRaises(ValueError):
            transform_model(model,point_sources=p)
        with self.assertRaises(ValueError):
            transform_model(model,point_sources=(0,)*15)
        bad=dict(model,left_labels=((0,1),)*15)
        with self.assertRaises(ValueError):
            anchored_pair_normal_form(bad)
        bad2=dict(model,incidences=model["incidences"][:-1])
        with self.assertRaises(ValueError):
            symplectic_transvection_source(bad2,0)
        with self.assertRaises(ValueError):
            edge_to_zero_one_permutation((1,1),6)
        with self.assertRaises(ValueError):
            local_original_seven_tag(model,(0,0,1,2,3,4))

    def test_08_no_fake_all_h_exhaustion_or_unverified_geometry(self):
        self.assertFalse(normalized_search_cardinality(2)["root_C_closed"])
        self.assertTrue(normalized_search_cardinality(4)[
            "still_astronomical_not_full_minimax_enumeration"])
        model=fixture(1,"S68")
        with self.assertRaises(ValueError):
            transform_model(model,point_coordinates=(0,)*6)
        with self.assertRaises(ValueError):
            anchored_pair_normal_form(model,-1,0)


if __name__=="__main__":
    unittest.main()
