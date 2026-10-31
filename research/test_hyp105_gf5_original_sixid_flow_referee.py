"""Independent finite GF5/51-column and genuine ORIGINAL six-ID referee."""
from collections import Counter
from itertools import combinations, product
import unittest

from hyp105_gf5_original_sixid_flow_referee import (
    SIGNS, c4_edge_sets, bb_overlap_templates, coincident_c6_template,
    gf5_flow_inclusion_exclusion, gf5_flow_spanning_tree,
    complete_bb_overlap_census, planted_original_bb_overlap,
    planted_original_d6, original_projected_column_edges,
)
from hyp105_full_physical_degree_tail import genuine_source


class OriginalGF5SixIdReferee(unittest.TestCase):
    def test_original_full_palette_is_exactly_51(self):
        # Raw 4-coordinate coefficient vectors; no repo palette helper.
        palette=tuple(w for w in product(range(1,5),repeat=4)
                      if sum(w)%5==4)
        self.assertEqual(len(palette),51)
        self.assertEqual(len(set(palette)),51)
        self.assertTrue(all(len(w)==4 and all(0<x<5 for x in w)
                            for w in palette))

    def test_complete_90_signed_BBo_dual_profiles(self):
        x=complete_bb_overlap_census(direct_crosscheck=True)
        self.assertEqual(len(x["profiles"]),9)
        self.assertEqual(x["signed_cases"],90)
        self.assertEqual(x["positive_cases"],90)
        self.assertEqual((x["min"],x["max"]),(5175,5535))
        self.assertEqual(x["total_all_nine_and_ten"],482670)
        self.assertTrue(x["all_positive"])
        self.assertEqual(
            sorted(Counter(p["total"] for p in x["profiles"]).items()),
            [(53526,6),(53838,3)])
        for p in x["profiles"]:
            self.assertEqual(len(p["signed_flows"]),10)
            self.assertGreaterEqual(min(p["signed_flows"]),5175)
            self.assertGreaterEqual(sum(p["signed_flows"]),51750)

    def test_coincident_C6_positive_alternating_5643(self):
        x=coincident_c6_template()
        self.assertEqual(len(x),12)
        results=tuple(gf5_flow_inclusion_exclusion(x,s) for s in SIGNS)
        self.assertEqual(len(results),10)
        self.assertEqual((min(results),max(results)),(5265,5643))
        self.assertEqual(results[5],5643)  # {0,2,4} alternating
        self.assertEqual(gf5_flow_spanning_tree(x,SIGNS[5]),5643)
        self.assertTrue(all(x>0 for x in results))

    def test_true_original_W32_W34_BB_overlap_full_labels(self):
        for power in (1,2):
            with self.subTest(power=power):
                m=planted_original_bb_overlap(power)
                s,V,flags=genuine_source(power)
                self.assertEqual((m["s"],m["V"]),(s,V))
                self.assertEqual(len(m["ids"]),6)
                self.assertEqual(len(set(m["ids"])),6)
                self.assertEqual(len(m["f"]),V)
                self.assertEqual(len(set(m["f"])),V)
                self.assertEqual(len(m["g"]),V)
                self.assertEqual(len(set(m["g"])),V)
                physical=original_projected_column_edges(
                    flags,m["ids"],m["f"],m["g"])
                self.assertEqual(physical,m["edges"])
                flows=tuple(gf5_flow_inclusion_exclusion(physical,sig)
                            for sig in SIGNS)
                self.assertGreaterEqual(min(flows),5175)
                self.assertGreaterEqual(sum(flows),51750)
                for pos in (0,5,9):
                    self.assertEqual(gf5_flow_spanning_tree(physical,SIGNS[pos]),
                                     flows[pos])

    def test_true_original_W32_W34_matching_D6_full_labels(self):
        for power in (1,2):
            with self.subTest(power=power):
                m=planted_original_d6(power)
                s,V,flags=genuine_source(power)
                self.assertEqual(m["s"],s)
                self.assertEqual(len(m["ids"]),6)
                self.assertEqual(len(set(m["ids"])),6)
                self.assertEqual(len(set(m["f"])),V)
                self.assertEqual(len(set(m["g"])),V)
                self.assertEqual(m["edges"],original_projected_column_edges(
                    flags,m["ids"],m["f"],m["g"]))
                self.assertEqual(gf5_flow_inclusion_exclusion(m["edges"],SIGNS[5]),5643)
                self.assertEqual(gf5_flow_spanning_tree(m["edges"],SIGNS[5]),5643)

    def test_signed_column_relabel_and_physical_coordinate_conservation(self):
        e=next(iter(bb_overlap_templates()))
        base=tuple(gf5_flow_inclusion_exclusion(e,s) for s in SIGNS)
        permutation=(3,5,0,2,4,1)
        relabeled=tuple(tuple(sorted((permutation[u],permutation[v])))
                        for u,v in e)
        for i,plus in enumerate(SIGNS):
            renamed=frozenset(permutation[v] for v in plus)
            # Sign-complement to keep ID 0 in the 3+3 representative.
            if 0 not in renamed:
                renamed=frozenset(set(range(6))-renamed)
            self.assertEqual(gf5_flow_inclusion_exclusion(relabeled,renamed),base[i])
        self.assertEqual(len(c4_edge_sets((0,1,2,3))),3)

    def test_genuine_id_and_leaf_fail_closed(self):
        m=planted_original_bb_overlap(1)
        with self.assertRaises(ValueError):
            original_projected_column_edges(m["flags"],m["ids"][:5],m["f"],m["g"])
        with self.assertRaises(ValueError):
            original_projected_column_edges(
                m["flags"],(m["ids"][0],)*6,m["f"],m["g"])
        with self.assertRaises(ValueError):
            original_projected_column_edges(
                m["flags"],(*m["ids"][:5],len(m["flags"])),m["f"],m["g"])
        with self.assertRaises(ValueError):
            planted_original_bb_overlap(3)
        with self.assertRaises(ValueError):
            planted_original_d6(0)
        with self.assertRaises(ValueError):
            gf5_flow_inclusion_exclusion(coincident_c6_template()[:-1],SIGNS[5])
        with self.assertRaises(ValueError):
            gf5_flow_spanning_tree(coincident_c6_template(),frozenset((0,1)))
        with self.assertRaises(ValueError):
            gf5_flow_inclusion_exclusion(tuple((0,0) for _ in range(12)),SIGNS[5])


if __name__=="__main__":
    unittest.main()
