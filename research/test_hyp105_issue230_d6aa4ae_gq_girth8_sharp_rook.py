"""Independent true ORIGINAL W3s girth-eight four-rook exact tests."""
import unittest
from itertools import combinations,permutations

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ae_gq_girth8_sharp_rook import (
    PERMS4,true_gq_four_rook,
    all_65536_four_binary_gq_certificates,
    original_opposite_four_factor_cycle_census,
    full_original_W32_all_four_schemes_girth8_report,
)
from hyp105_issue230_d6aa4ab_minimax_orbit_normalform import (
    symplectic_transvection_source,transform_model,
)
from hyp105_issue230_d6aa4q_two_sided_seven_join import (
    exact_two_sided_original_seven_join,
)


def independent_gq_local_cycle_check(rows):
    """Graph-theoretic search separate from row-pair C4/C6 criterion."""
    graph={i:[] for i in range(8)}
    for i in range(4):
        for j in range(4):
            if rows[i]&(1<<j):
                graph[i].append(j+4)
                graph[j+4].append(i)
    found={4:False,6:False,8:False}
    def walk(first,node,visited,path):
        for nxt in graph[node]:
            if nxt==first and len(path) in found and len(path)>=4:
                found[len(path)]=True
            if nxt in visited or len(path)>=8:
                continue
            walk(first,nxt,visited|{nxt},path+[nxt])
    for i in range(8):
        walk(i,i,{i},[i])
    return found


def independent_direct_permanent(rows):
    return sum(all(rows[i]&(1<<p[i]) for i in range(4))
               for p in permutations(range(4)))


class GenuineOriginalGirthEightFourRookTests(unittest.TestCase):
    def test_01_all_65536_binary_four_by_four_C4_C6_classification(self):
        z=all_65536_four_binary_gq_certificates()
        self.assertEqual(z["all_binary_four_by_four_matrices"],65536)
        self.assertEqual(z["maximum_PERMANENT_for_valid_true_GQ_local_matrix"],2)
        self.assertGreater(z["C4free_but_C6_forbidden_non_GQ_matrices"],0)
        hist=z["girth_at_least_eight_local_matrix_histogram"]
        self.assertEqual(set(hist),{0,1,2})
        self.assertGreater(hist[2],0)
        self.assertEqual(sum(hist.values())+
                         z["C4_forbidden_non_GQ_matrices"]+
                         z["C4free_but_C6_forbidden_non_GQ_matrices"],65536)
        self.assertEqual(
            true_gq_four_rook(z["K22_free_PERMANENT_3_NON_GQ_due_to_SOURCE_C6_rows"])[
                "true_original_four_rook_permanent"],3)

    def test_02_explicit_original_source_C8_iff_permanent_two(self):
        C8=(0b1001,0b0011,0b0110,0b1100)
        z=true_gq_four_rook(C8)
        self.assertEqual(z["true_original_four_rook_permanent"],2)
        self.assertTrue(z["gq_girth_eight_eligible"])
        self.assertTrue(z["exactly_two_perfect_matchings_implies_original_C8"])
        self.assertEqual(independent_gq_local_cycle_check(C8),
                         {4:False,6:False,8:True})
        self.assertEqual(independent_direct_permanent(C8),2)
        changed=(C8[0]|2,C8[1],C8[2],C8[3])
        invalid=true_gq_four_rook(changed)
        self.assertFalse(invalid["gq_girth_eight_eligible"])
        self.assertTrue(invalid["original_C4_forbidden_observed"] or
                        invalid["original_C6_forbidden_observed"])

    def test_03_girth_SIX_forbidden_even_if_K22_free(self):
        non_gq=(14,9,5,3)
        z=true_gq_four_rook(non_gq)
        self.assertFalse(z["original_C4_forbidden_observed"])
        self.assertTrue(z["original_C6_forbidden_observed"])
        self.assertFalse(z["gq_girth_eight_eligible"])
        self.assertEqual(z["true_original_four_rook_permanent"],3)
        cycle=independent_gq_local_cycle_check(non_gq)
        self.assertFalse(cycle[4]);self.assertTrue(cycle[6])

    def test_04_independent_short_cycles_sparse_exhaustive_samples(self):
        for n in range(0,65536,19):
            rows=tuple((n>>(4*i))&15 for i in range(4))
            z=true_gq_four_rook(rows)
            chk=independent_gq_local_cycle_check(rows)
            self.assertEqual(z["original_C4_forbidden_observed"],chk[4])
            self.assertEqual(z["gq_girth_eight_eligible"],
                             not(chk[4] or chk[6]))
            self.assertEqual(z["true_original_four_rook_permanent"],
                             independent_direct_permanent(rows))
            self.assertEqual(z["exactly_two_perfect_matchings_implies_original_C8"],
                             z["gq_girth_eight_eligible"] and
                             z["true_original_four_rook_permanent"]==2)

    def test_05_original_W32_S68_S72_true_six_incidence_join(self):
        for scheme,values in (("S68",(44,21)),("S72",(36,31))):
            z=full_original_W32_all_four_schemes_girth8_report(scheme)
            self.assertEqual(z["true_original_W32_GF5_S"],
                             68 if scheme=="S68" else 72)
            for tag,expected in zip(
                ("B-left/A-right","A-left/B-right"),values):
                row=z["per_GF5_BA_tag"][tag]
                self.assertEqual(row["exact_accepted_true_original_GF5_BA"],expected)
                self.assertEqual(row["actual_original_B_C4_cohorts_examined"],135)
                self.assertEqual(row["induced_original_C8_double_permanent_patterns"],0)
                self.assertEqual(row["Hall_positive_true_original_GQ_completions"],expected)
                self.assertEqual(row["positive_permanent_multiset_histogram"],{1:expected})

    def test_06_original_W32_lex_reverse_C8_double_witness(self):
        for scheme,accepted in (
            ("lex",(98,110)),("reverse",(77,74))
        ):
            z=full_original_W32_all_four_schemes_girth8_report(scheme)
            for tag,value in zip(
                ("B-left/A-right","A-left/B-right"),accepted):
                row=z["per_GF5_BA_tag"][tag]
                self.assertEqual(row["exact_accepted_true_original_GF5_BA"],value)
                if scheme=="lex" and tag=="A-left/B-right":
                    self.assertEqual(row["induced_original_C8_double_permanent_patterns"],1)
                    self.assertEqual(row["Hall_positive_true_original_GQ_completions"],109)
                    self.assertEqual(row["positive_permanent_multiset_histogram"],
                                     {1:108,2:1})
                    witness=row["first_true_original_induced_C8_witness"]
                    self.assertIsNotNone(witness)
                    self.assertEqual(independent_gq_local_cycle_check(
                        witness["true_original_incidence_row_masks"]),
                        {4:False,6:False,8:True})
                else:
                    self.assertEqual(row["induced_original_C8_double_permanent_patterns"],0)
                    self.assertIsNone(row["first_true_original_induced_C8_witness"])

    def test_07_genuine_W34_global_nononto_physical_source(self):
        model=fixture(2,"lex")
        for side in (0,1):
            z=original_opposite_four_factor_cycle_census(
                model,side=side,roots=(0,),max_cohorts=5)
            self.assertEqual(z["s"],4)
            self.assertEqual(z["actual_original_B_C4_cohorts_examined"],5)
            self.assertEqual(
                z["Hall_positive_true_original_GQ_completions"]+
                z["induced_original_C8_double_permanent_patterns"],
                z["exact_accepted_true_original_GF5_BA"])
            self.assertTrue(z["full_global_injective_maps_used_same_in_every_original_Q"])

    def test_08_true_original_source_automorphism_invariance_BA_C8(self):
        model=fixture(1,"lex")
        reference=original_opposite_four_factor_cycle_census(model,side=1)
        p,l=symplectic_transvection_source(model,4)
        changed=transform_model(
            model,point_sources=p,line_sources=l,
            point_coordinates=tuple(reversed(range(6))),
            line_coordinates=(1,2,3,4,5,0))
        alternate=original_opposite_four_factor_cycle_census(changed,side=1)
        for key in (
            "fully_occupied_physical_A_2factor_completions",
            "Hall_positive_true_original_GQ_completions",
            "induced_original_C8_double_permanent_patterns",
            "exact_accepted_true_original_GF5_BA",
            "positive_permanent_multiset_histogram",
        ):
            self.assertEqual(reference[key],alternate[key])

    def test_09_invalid_false_source_or_bad_binary_four_matrix(self):
        for rows in ((0,),(1,2,3,4,5),(-1,2,3,4),(0.0,0,0,0),
                     (16,1,1,0)):
            with self.assertRaises(ValueError):
                true_gq_four_rook(rows)
        model=fixture(1,"S68")
        with self.assertRaises(ValueError):
            original_opposite_four_factor_cycle_census(
                model,side=0,roots=(0,0))
        with self.assertRaises(ValueError):
            original_opposite_four_factor_cycle_census(
                model,side=3,roots=(0,))
        with self.assertRaises(ValueError):
            original_opposite_four_factor_cycle_census(
                dict(model,right_labels=((0,1),)*15),side=0,roots=(0,))
        with self.assertRaises(ValueError):
            original_opposite_four_factor_cycle_census(
                dict(model,incidences=tuple(model["incidences"])[:-1]),
                side=0,roots=(0,))

    def test_10_non_GQ_C6_matrix_independently_rejected(self):
        non_gq=(14,9,5,3)
        self.assertEqual(independent_direct_permanent(non_gq),3)
        # Prior Y6 K2,2-free-only abstract bound allows THREE,
        # but the true source GQ cannot contain this row matrix.
        z=true_gq_four_rook(non_gq)
        self.assertFalse(z["gq_girth_eight_eligible"])
        self.assertTrue(z["original_C6_forbidden_observed"])


if __name__=="__main__":
    unittest.main()
