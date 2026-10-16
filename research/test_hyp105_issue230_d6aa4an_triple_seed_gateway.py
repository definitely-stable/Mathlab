"""HYP-105 AA4-AN adversarial independent all-seven physical seed gate tests."""
import unittest
from collections import Counter
from itertools import combinations, combinations_with_replacement

from hyp105_issue230_d6aa4an_triple_seed_gateway import (
    canonical_edge, falling3, minimal_physical_parameters,
    sharp_all_global_crowded_triple_floor, balanced_missing_edges,
    count_original_distinct_source_crowded_triples,
    complete_three_physical_edges_to_six_2regular, verify_balanced_sharpness,
    joint_physically_eligible_original_matching_triple_floor,
    exact_original_matching_uncrowded_triples,
)
from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import zero_split_original_W32
from hyp105_g5e2b3e1b0_seven_signature import seven_census


def _physical_full6_multisets(a):
    """Independent literal brute 6-edge degree-2 multigraphs on exactly 6 coords.

    This is NOT the completion algorithm under review; enumerates all
    K6-with-repetition six-multisets once, lifts to every six-subset K_a.
    """
    k6=list(combinations(range(6),2))
    templates=[]
    for H in combinations_with_replacement(k6,6):
        D=Counter(v for e in H for v in e)
        if len(D)==6 and set(D.values())=={2}:
            templates.append(H)
    assert len(templates)==130
    for vertices in combinations(range(a),6):
        for H in templates:
            yield tuple(sorted(canonical_edge(vertices[u],vertices[v])
                               for u,v in H))


class GenuineOriginalTriplePhysicalSeed(unittest.TestCase):
    def test_01_exhaustive_K6_K7_K8_multiset_completion_iff_maxdegree2(self):
        for a in (6,7,8):
            K=list(combinations(range(a),2))
            can_complete=set()
            for H in _physical_full6_multisets(a):
                for indices in combinations(range(6),3):
                    can_complete.add(tuple(sorted(H[i] for i in indices)))
            self.assertEqual(len(can_complete)>0,True)
            for E in combinations_with_replacement(K,3):
                D=Counter(v for e in E for v in e)
                eligible=max(D.values())<=2
                actual=complete_three_physical_edges_to_six_2regular(E,a)
                self.assertEqual(eligible,E in can_complete,(a,E))
                self.assertEqual(eligible,actual is not None,(a,E))
                if actual is not None:
                    X=Counter(v for e in actual for v in e)
                    self.assertEqual((len(actual),len(X),set(X.values())),
                                     (6,6,{2}))
                    self.assertFalse(Counter(E)-Counter(actual))

    def test_02_sharp_extremal_global_missing_graph_achievability(self):
        for s in (2,4,8,16,32,64):
            V,a,m=minimal_physical_parameters(s)
            self.assertTrue(verify_balanced_sharpness(s))
            M=balanced_missing_edges(a,m)
            self.assertEqual(len(M),m)
            degrees=Counter(v for e in M for v in e)
            self.assertLessEqual(max(degrees.values(),default=0)-
                min(degrees.get(i,0) for i in range(a)),1)
            R=sharp_all_global_crowded_triple_floor(s)
            self.assertEqual(R["V"],V)
            self.assertEqual(R["a"],a)

    def test_03_all_h_exact_integer_discrete_Jensen_s9_no_lift(self):
        for h in range(1,73):
            s=1<<h
            z=sharp_all_global_crowded_triple_floor(s)
            self.assertGreaterEqual(
                z["exact_minimum_ordered_distinct_original_source_point_triples"],
                z["coarse_all_maps_original_source_triple_lower"])
            self.assertGreaterEqual(
                9*z["exact_minimum_ordered_distinct_original_source_point_triples"],
                s**9)
            self.assertTrue(z["seven_GF5_positive_extension_from_crowded_triple_IMPOSSIBLE"])
            self.assertTrue(z["root_issue230_Branch_A_B_C_NOT_PROVED"])

    def test_04_original_W32_direct_flag_triples_vs_physical_degrees(self):
        for model in (zero_split_original_W32(),fixture(1,"lex"),
                      fixture(1,"S68"),fixture(1,"S72")):
            inc=tuple(tuple(e) for e in model["incidences"])
            for side in (0,1):
                images=tuple(tuple(e) for e in model[
                    "left_labels" if side==0 else "right_labels"])
                direct=0
                for i,j,k in combinations(range(len(inc)),3):
                    ids=(inc[i][side],inc[j][side],inc[k][side])
                    if len(set(ids)) != 3:
                        continue
                    if set(images[ids[0]]) & set(images[ids[1]]) & set(images[ids[2]]):
                        direct+=6
                expected=count_original_distinct_source_crowded_triples(
                    images,model["s"]+1)
                self.assertEqual(direct,expected)
                # Physical K6 source-factor map is bijective on W32.
                self.assertEqual(direct,9720)

    def test_05_original_W34_W38_global_holes_direct_degree_count(self):
        for h in (2,3):
            for scheme in ("lex","random"):
                model=fixture(h,scheme)
                for side in (0,1):
                    images=tuple(tuple(e) for e in model[
                        "left_labels" if side==0 else "right_labels"])
                    count=count_original_distinct_source_crowded_triples(
                        images,h and (1<<h)+1)
                    bound=sharp_all_global_crowded_triple_floor(1<<h)
                    self.assertGreaterEqual(count,bound[
                        "exact_minimum_ordered_distinct_original_source_point_triples"])
                    self.assertEqual(len(images),bound["V"])

    def test_06_all_seven_original_GF5_W32_classes_no_degree3_triples(self):
        for model in (zero_split_original_W32(),fixture(1,"S68")):
            selected=seven_census(model,witness_sets=True,independent_checks=False)
            tags=selected["sets"]
            self.assertEqual(len(tags),selected["S_seven"])
            inc=tuple(tuple(e) for e in model["incidences"])
            for Q in tags:
                self.assertEqual(len(Q),6)
                for side in (0,1):
                    imgs=tuple(tuple(e) for e in model[
                        "left_labels" if side==0 else "right_labels"])
                    phys=[imgs[inc[i][side]] for i in Q]
                    deg=Counter(v for e in phys for v in e)
                    self.assertEqual(len(deg),6)
                    self.assertEqual(set(deg.values()),{2})
                    for triple in combinations(phys,3):
                        self.assertLessEqual(max(Counter(
                            v for e in triple for v in e).values()),2)

    def test_07_missing_edge_graph_extrema_small_adversarial(self):
        # For every actual K6 physical injection missing m<=4, independently
        # enumerate complement choices and check near-balanced optimum.
        for a in (6,7):
            K=tuple(combinations(range(a),2))
            for m in range(a-1):
                q,r=divmod(a*(a-1)-2*m,a)
                sharp=(a-r)*falling3(q)+r*falling3(q+1)
                witness=balanced_missing_edges(a,m)
                global_witness=tuple(e for e in K if e not in witness)
                self.assertEqual(count_original_distinct_source_crowded_triples(
                    global_witness,1),sharp)
                for missing in combinations(K,m):
                    chosen=tuple(e for e in K if e not in missing)
                    self.assertGreaterEqual(
                        count_original_distinct_source_crowded_triples(chosen,1),
                        sharp)

    def test_08_explicit_rejections_and_type_boundaries(self):
        for bad in (0,3,6,True,16.0):
            with self.assertRaises(ValueError):
                sharp_all_global_crowded_triple_floor(bad)
        for e in (((0,1),(0,1),(0,1)),
                  ((0,1),(0,2),(0,3))):
            self.assertIsNone(complete_three_physical_edges_to_six_2regular(e,6))
        for edges in (((0,1),(1,2),(2,0)),
                      ((0,1),(0,1),(2,3)),
                      ((0,1),(1,2),(2,3)),
                      ((0,1),(2,3),(4,5))):
            self.assertIsNotNone(
                complete_three_physical_edges_to_six_2regular(edges,6))
        with self.assertRaises(ValueError):
            count_original_distinct_source_crowded_triples(
                [(0,1),(0,1)],3)
        with self.assertRaises(ValueError):
            balanced_missing_edges(6,5)
        with self.assertRaises(ValueError):
            complete_three_physical_edges_to_six_2regular(
                ((0,1),(1,2),(2,6)),6)

    def test_09_all_global_original_source_matching_3by3_uncrowded_omega_s12(self):
        for h in range(1,73):
            s=1<<h
            z=joint_physically_eligible_original_matching_triple_floor(s)
            self.assertGreaterEqual(3*z[
                "all_global_ordered_true_original_3_by_3_uncrowded_triples_lower"],
                z["n_true_original_flags"]**3)
            self.assertGreaterEqual(3*z[
                "all_global_ordered_true_original_3_by_3_uncrowded_triples_lower"],
                s**12)
            self.assertTrue(z["same_original_six_flag_GF5_completion_NOT_PROVED"])
            if h>=2:
                self.assertGreaterEqual(4*z[
                    "all_global_ordered_true_original_3_by_3_uncrowded_triples_lower"],
                    3*z["n_true_original_flags"]**3)

    def test_10_real_original_uncrowded_not_joint_GF5_extendible_W32(self):
        for model in (zero_split_original_W32(),fixture(1,"lex"),
                      fixture(1,"S68"),fixture(1,"S72")):
            source=exact_original_matching_uncrowded_triples(model)
            minbound=joint_physically_eligible_original_matching_triple_floor(2)
            good=source["unordered_physically_both_types_uncrowded_original_triples"]
            self.assertGreaterEqual(6*good,minbound[
                "all_global_ordered_true_original_3_by_3_uncrowded_triples_lower"])
            seven=seven_census(model,witness_sets=True,independent_checks=False)
            accepted=seven["S_seven"]
            # Each selected ORIGINAL six-incidence Q has <=20 three-subsets.
            # This lower quantifies physical joint-palette feasibility
            # WITHOUT actual source/GF5 six-Q extension.
            cannot_extend_lower=good-20*accepted
            self.assertGreater(cannot_extend_lower,0)
            print("AA4AN_TRUE_ORIGINAL_UNCROWDED",model["s"],good,
                  "selected_seven",accepted,"unextendible_at_least",
                  cannot_extend_lower)


if __name__ == "__main__":
    unittest.main()
