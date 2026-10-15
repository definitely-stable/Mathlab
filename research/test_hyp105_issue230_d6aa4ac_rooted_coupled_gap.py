"""Independent real-GQ AA4-AC 2-anchor minimax / rooted BA-AB identities."""
from itertools import combinations
from math import factorial
import unittest

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4q_two_sided_seven_join import (
    exact_two_sided_original_seven_join,
)
from hyp105_issue230_d6aa4ab_minimax_orbit_normalform import (
    symplectic_transvection_source,transform_model,
)
from hyp105_issue230_d6aa4ac_rooted_coupled_gap import (
    normalize_two_physical_edges,two_edge_physical_orbit,
    normalize_two_anchors,all_h_second_anchor_sectors,
    all_h_repeated_source_root_universe,
    true_W32_root_gap_certificate,root_gap_hamming_theorem,
)


class RealOriginalTwoAnchorRootGapTests(unittest.TestCase):
    def test_01_all_K6_and_K7_ordered_distinct_edge_orbits(self):
        for a in (6,7):
            allpairs=list(combinations(range(a),2))
            freq={"adjacent":0,"disjoint":0}
            for e0 in allpairs:
                for e1 in allpairs:
                    if e0==e1:continue
                    z=normalize_two_physical_edges(e0,e1,a)
                    perm=z["permutation"]
                    self.assertEqual(set(perm),set(range(a)))
                    self.assertEqual(
                        tuple(sorted(perm[x] for x in e0)),(0,1))
                    self.assertEqual(
                        tuple(sorted(perm[x] for x in e1)),
                        (0,2) if z["relation"]=="adjacent" else (2,3))
                    self.assertEqual(two_edge_physical_orbit(e0,e1,a),
                                     z["relation"])
                    freq[z["relation"]]+=1
            K=len(allpairs)
            self.assertEqual(freq["adjacent"],K*2*(a-2))
            self.assertEqual(freq["disjoint"],K*(a-2)*(a-3)//2)
            self.assertEqual(sum(freq.values()),K*(K-1))

    def test_02_exact_all_h_four_sectors_and_true_W32_factor(self):
        for h in range(1,5):
            s=1<<h
            z=all_h_second_anchor_sectors(s)
            K,V=z["K"],z["V"]
            expected_per=factorial(K-2)//factorial(K-V)
            self.assertEqual(z["per_canonical_orbit_sector_assignments"],
                             expected_per**2)
            self.assertEqual(z["four_canonical_sector_assignments_total"],
                             4*expected_per**2)
            self.assertEqual(z["unanchored_global_two_map_assignments"],
                             (factorial(K)//factorial(K-V))**2)
            self.assertEqual(
                z["unanchored_global_two_map_assignments"]//
                z["four_canonical_sector_assignments_total"],
                z["exact_search_assignment_reduction_factor"])
            self.assertFalse(z["all_h_universal_adversarial_lower_PROVED"])
        w32=all_h_second_anchor_sectors(2)
        self.assertEqual(w32["exact_search_assignment_reduction_factor"],11025)
        self.assertEqual(w32["per_canonical_orbit_sector_assignments"],
                         factorial(13)**2)
        self.assertEqual(set(w32["sector_cardinalities"]),{
            "point_adjacent__line_adjacent",
            "point_adjacent__line_disjoint",
            "point_disjoint__line_adjacent",
            "point_disjoint__line_disjoint"})

    def test_03_all_four_genuine_W32_two_sided_sectors_preserve_seven(self):
        for name,S in (("S68",68),("S72",72)):
            model=fixture(1,name)
            base=exact_two_sided_original_seven_join(
                model,independent_history=False)
            self.assertEqual(base["accepted_seven_GF5_original_S"],S)
            point_pairs={}
            line_pairs={}
            for key,allpairs in (("point",point_pairs),("line",line_pairs)):
                labels=model["left_labels" if key=="point" else "right_labels"]
                for j in range(1,15):
                    orbit=two_edge_physical_orbit(labels[0],labels[j],6)
                    allpairs.setdefault(orbit,(0,j))
            self.assertEqual(set(point_pairs),{"adjacent","disjoint"})
            self.assertEqual(set(line_pairs),{"adjacent","disjoint"})
            for po in ("adjacent","disjoint"):
                for lo in ("adjacent","disjoint"):
                    p=point_pairs[po];l=line_pairs[lo]
                    z=normalize_two_anchors(model,p,l)
                    transformed=z["model"]
                    self.assertEqual((z["point_orbit"],z["line_orbit"]),(po,lo))
                    check=exact_two_sided_original_seven_join(
                        transformed,independent_history=False)
                    for field in ("accepted_seven_GF5_original_Q_by_tag",
                                  "accepted_seven_GF5_original_S",
                                  "physical_A_A_genuine_D6_only",
                                  "selected_GF5_51palette_certified_numerator"):
                        self.assertEqual(base[field],check[field])

    def test_04_true_original_W32_independent_root_BA_AB_gap_S68(self):
        z=true_W32_root_gap_certificate(fixture(1,"S68"))
        self.assertEqual(z["accepted_original_B_left_A_right"],44)
        self.assertEqual(z["accepted_original_A_left_B_right"],21)
        self.assertEqual(z["accepted_two_BA_AB_classes"],65)
        self.assertEqual(z["true_original_root_source_universe"],111132)
        self.assertEqual(
            z["B/A_A/B_selected_51palette_certified_numerator"],45600*65)
        for rows in z["root_rows_by_GF5_tag"].values():
            self.assertEqual(len(rows),15)
            self.assertEqual([q["source_root_id"] for q in rows],list(range(15)))
            self.assertEqual(sum(q["root_coupled_overlap_excess_above_Frechet"]
                                 for q in rows),
                             sum(q["joint_original_SIX_Q_positive"] for q in rows))
            self.assertTrue(all(q["root_Frechet_lower"]==0 for q in rows))

    def test_05_true_original_W32_S72_shared_f_and_dual_charge(self):
        x=true_W32_root_gap_certificate(fixture(1,"S68"))
        y=true_W32_root_gap_certificate(fixture(1,"S72"))
        self.assertEqual(y["accepted_original_B_left_A_right"],36)
        self.assertEqual(y["accepted_original_A_left_B_right"],31)
        self.assertEqual(y["accepted_two_BA_AB_classes"],67)
        for tag in ("B-left/A-right","A-left/B-right"):
            px=x["root_rows_by_GF5_tag"][tag]
            py=y["root_rows_by_GF5_tag"][tag]
            # S68/S72 use the IDENTICAL original global point f.
            self.assertEqual([q["first_side_half_support"] for q in px],
                             [q["first_side_half_support"] for q in py])
            self.assertNotEqual([q["joint_original_SIX_Q_positive"] for q in px],
                                [q["joint_original_SIX_Q_positive"] for q in py])

    def test_06_true_original_W32_joint_sp4_and_two_physical_orbits(self):
        m=fixture(1,"S68")
        reference=true_W32_root_gap_certificate(m)
        p,l=symplectic_transvection_source(m,4)
        changed=transform_model(
            m,point_sources=p,line_sources=l,
            point_coordinates=tuple(reversed(range(6))),
            line_coordinates=(1,2,3,4,5,0))
        anchored=normalize_two_anchors(changed,(2,5),(3,7))["model"]
        z=true_W32_root_gap_certificate(anchored)
        for tag in ("B-left/A-right","A-left/B-right"):
            old=reference["root_rows_by_GF5_tag"][tag]
            new=z["root_rows_by_GF5_tag"][tag]
            t=p if tag=="B-left/A-right" else l
            for i in range(15):
                for field in ("first_side_half_support",
                              "second_side_half_support",
                              "joint_original_SIX_Q_positive",
                              "symmetric_difference_gap"):
                    self.assertEqual(old[i][field],new[t[i]][field])

    def test_07_exact_source_reservoir_all_h_and_purely_symbolic_gap(self):
        for s in (2,4,8,16):
            source=all_h_repeated_source_root_universe(s)
            V=source["V"]
            self.assertEqual(
                source["source_B/A_total"],
                V*source["original_source_B/A_Q_per_repeated_point_root"])
            self.assertEqual(source["source_B/A_total"],source["source_A/B_total"])
            statement=root_gap_hamming_theorem(s)
            self.assertTrue(statement["BA_plus_AB_exact_root_global_identity"])
            self.assertFalse(statement["full_seven_positive_S_lower_NOT_PROVED"] is False)

    def test_08_real_W32_invalid_global_sources_and_second_anchors(self):
        m=fixture(1,"S68")
        with self.assertRaises(ValueError):
            normalize_two_physical_edges((0,1),(0,1),6)
        with self.assertRaises(ValueError):
            normalize_two_physical_edges((1,0),(0,2),6)
        with self.assertRaises(ValueError):
            normalize_two_anchors(m,(1,1),(0,1))
        with self.assertRaises(ValueError):
            normalize_two_anchors(m,(0,15),(0,1))
        with self.assertRaises(ValueError):
            normalize_two_anchors(m,(0,1),(0,0))
        bad=dict(m,incidences=m["incidences"][:-1])
        with self.assertRaises(ValueError):
            true_W32_root_gap_certificate(bad)
        bad2=dict(m,right_labels=((0,1),)*15)
        with self.assertRaises(ValueError):
            true_W32_root_gap_certificate(bad2)


if __name__=="__main__":
    unittest.main()
