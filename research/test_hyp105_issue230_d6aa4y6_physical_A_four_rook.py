"""Independent HYP-105 #230 Y6 genuine ORIGINAL GF5 physical-A 4-rook tests."""
import random
import unittest
from collections import Counter
from itertools import combinations, permutations, product

from hyp105_issue230_d6aa4y6_physical_A_four_rook import (
    original_four_by_four_incidence_permanent,
    exhaustive_four_by_four_K22_free_permanent_certificate,
    physical_2factor_containing_two_occupied_edges,
    original_all_h_two_pinned_physical_A_capacity,
    independent_historical_BA_rooted_gate,
    genuine_W32_BA_physical_gate_full,
    report,
)


def independent_matrix_permanent(rows):
    return sum(all(rows[i][perm[i]] for i in range(4))
               for perm in permutations(range(4)))


def independent_Ka_twofactor_count(a,e1,e2):
    """Brute enumerator fully independent of Y6's physical iterator:
    choose all occupied physical edge six-sets first and check
    coordinate degree-two on six different coordinate vertices."""
    edges=list(combinations(range(a),2))
    out=0
    for physical in combinations(edges,6):
        if e1 not in physical or e2 not in physical:
            continue
        degrees=Counter(v for edge in physical for v in edge)
        if len(degrees)==6 and set(degrees.values())=={2}:
            out+=1
    return out


class OriginalPhysicalAFourRookTests(unittest.TestCase):
    def test_001_exhaustive_65536_girth_four_matrix_permanent_le_three(self):
        result=exhaustive_four_by_four_K22_free_permanent_certificate()
        self.assertEqual(result["all_binary_4_by_4_matrices_exhausted"],65536)
        self.assertEqual(result["genuine_GQ_K22_free_4x4_matrices"],18521)
        self.assertEqual(result["permanent_histogram"],{0:11993,1:5688,2:744,3:96})
        self.assertEqual(result["maximum_permanent"],3)
        self.assertTrue(result["all_h_original_GQ_any_4_by_4_submatrix_PERMANENT_le_3_PROVED"])
        self.assertEqual(original_four_by_four_incidence_permanent(
            ({1,2,3},{0,3},{0,2},{0,1}),(0,1,2,3)),3)
        with self.assertRaises(ValueError):
            original_four_by_four_incidence_permanent(
                ({0,1},{0,1},{0},{0}),(0,1,2,3))
        with self.assertRaises(ValueError):
            original_four_by_four_incidence_permanent(
                ({0},{1},{2},{3}),(0,1,2,2))

    def test_002_independent_random_genuine_K22_free_permanent(self):
        rng=random.Random(505230)
        accepted=0
        for _ in range(700):
            bits=tuple(rng.randrange(16) for _ in range(4))
            if any((bits[i]&bits[j]).bit_count()>1
                   for i in range(4) for j in range(i+1,4)):
                continue
            rows=tuple({j for j in range(4) if bits[i]&(1<<j)}
                       for i in range(4))
            truth=independent_matrix_permanent(
                tuple(tuple(int(j in rows[i]) for j in range(4))
                      for i in range(4)))
            result=original_four_by_four_incidence_permanent(
                rows,(0,1,2,3))
            self.assertEqual(result,truth)
            self.assertLessEqual(result,3)
            accepted+=1
        self.assertGreater(accepted,80)

    def test_003_independent_full_physical_K6_K7_fixed_two_edges(self):
        for a in (6,7):
            for e1,e2 in (((0,1),(0,2)),((0,1),(2,3))):
                relation="adjacent" if set(e1)&set(e2) else "disjoint"
                reference=(
                    7*__import__("math").comb(a-3,3)
                    if relation=="adjacent"
                    else 14*__import__("math").comb(a-4,2))
                self.assertEqual(independent_Ka_twofactor_count(a,e1,e2),reference)
                self.assertEqual(
                    len(physical_2factor_containing_two_occupied_edges(a,e1,e2)),
                    reference)
        with self.assertRaises(ValueError):
            physical_2factor_containing_two_occupied_edges(8,(0,1),(2,3))
        with self.assertRaises(ValueError):
            physical_2factor_containing_two_occupied_edges(6,(0,1),(0,1))

    def test_004_all_h_sharp_source_physical_completion_bounds(self):
        for h in range(1,14):
            s=1<<h
            for relation in ("adjacent","disjoint"):
                c=original_all_h_two_pinned_physical_A_capacity(s,relation)
                self.assertTrue(c["original_source_GQ_girth_K22_permanent_at_most_3"])
                self.assertTrue(c["conditional_on_one_REALIZED_B_physical_C4"])
                self.assertEqual(
                    c["per_realized_B_root_C4_original_GF5_physical_A_upper"],
                    3*c["physical_2_regular_A_completion_patterns_full_Ka"])
                self.assertFalse(c["all_h_universal_seven_motif_lower_PROVED"])
        with self.assertRaises(ValueError):
            original_all_h_two_pinned_physical_A_capacity(2,"intersecting")

    def test_005_real_original_S68_rooted_independent_4rook(self):
        r=genuine_W32_BA_physical_gate_full("S68")
        self.assertEqual(r["scheme"],"S68")
        self.assertTrue(r["all_h_exact_BA_physical_2factor_x_original_4rook_identity_PROVED"])
        self.assertTrue(r["independent_4_by_4_GQ_no_K22_permanent_le_3_PROVED"])
        for tag,expected in (("B-left/A-right",44),("A-left/B-right",21)):
            row=r["per_historical_BA_tag"][tag]
            self.assertEqual(row["accepted_historical_GF5_by_exact_four_rook_2factor"],expected)
            self.assertEqual(row["rooted_cohorts_exhaustively_checked"],45)
            self.assertEqual(row["true_original_B_physical_C4_patterns_examined"],135)
            self.assertTrue(row["historical_GF5_independent_Y5_and_AA4Q_agree"])
            self.assertEqual(
                row["rooted_cohorts_with_zero_historical_GF5"]
                +row["rooted_cohorts_with_positive_historical_GF5"],45)
            self.assertTrue(set(row["nonzero_permanent_1_2_3_histogram"])=={"1","2","3"})

    def test_006_real_original_S72_rooted_independent_4rook(self):
        r=genuine_W32_BA_physical_gate_full("S72")
        for tag,expected in (("B-left/A-right",36),("A-left/B-right",31)):
            self.assertEqual(
                r["per_historical_BA_tag"][tag][
                    "accepted_historical_GF5_by_exact_four_rook_2factor"],expected)

    def test_007_independent_rooted_gate_hostile_fake_geometry_rejected(self):
        a=tuple(combinations(range(6),2))
        loops=physical_2factor_containing_two_occupied_edges(
            6,a[0],a[1])
        with self.assertRaises(ValueError):
            independent_historical_BA_rooted_gate(
                (1,1,2,3),(0,1),[set(range(15)) for _ in range(15)],
                a,loops)
        with self.assertRaises(ValueError):
            independent_historical_BA_rooted_gate(
                (1,2,3,4),(0,0),[set(range(15)) for _ in range(15)],
                a,loops)

    def test_008_report_does_not_claim_universal_lower(self):
        x=report()
        self.assertEqual(x["K22_free_four_by_four_certificate"]["maximum_permanent"],3)
        self.assertTrue(x["all_h_exact_rooted_BA_2factor_4rook_join_PROVED"])
        self.assertEqual(x["root_A"],"OPEN")
        self.assertEqual(x["root_B"],"OPEN")
        self.assertEqual(x["root_C"],"OPEN")


if __name__=="__main__":
    unittest.main()
