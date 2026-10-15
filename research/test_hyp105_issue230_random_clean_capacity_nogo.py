"""EICE-003-L independent arithmetic/true-source randomized proof checks."""
from fractions import Fraction
from itertools import permutations
from math import comb, isqrt
import unittest

from hyp105_issue230_random_clean_capacity_nogo import (
    _falling, random_original_five_clean_certificate, report,
)
from hyp105_issue230_endpoint_energy import EndpointEnergy
from hyp105_issue230_projection import fixture
from hyp105_issue230_anchor_filtered_codegrees import (
    exact_original_anchor_middle_census,
    finite_original_anchor_cascade_report,
)


class OriginalCleanCapacityProbabilisticNoGoTests(unittest.TestCase):
    def test_L1_four_arm_random_injections_exact_without_replacement(self):
        # Enumerate all permutations of FOUR other point K6 physical
        # edge labels after the true original middle pair {0,1}.
        # Desired two arms meet x0 and two arms meet x1, ALL their
        # outside coordinates distinct, as in the all-h proof.
        a=6
        central=frozenset((0,1))
        edges=[frozenset((i,j)) for i in range(a) for j in range(i+1,a)]
        remaining=[e for e in edges if e!=central]
        accepted=0
        total=0
        for chosen in permutations(remaining,4):
            total+=1
            wanted=(0,0,1,1)
            if any(w not in chosen[i] for i,w in enumerate(wanted)):
                continue
            externals=tuple(next(iter(e-{wanted[i]}))
                            for i,e in enumerate(chosen))
            if len(set(externals))==4 and all(t not in central for t in externals):
                accepted+=1
        self.assertEqual(total,_falling(comb(a,2)-1,4))
        self.assertEqual(accepted,_falling(a-2,4))
        self.assertEqual(Fraction(accepted,total),
                         Fraction(_falling(a-2,4),_falling(comb(a,2)-1,4)))

    def test_L2_exact_all_h_probability_nonincident_clean_union_bound(self):
        for s in (64,128,256,512,1024,4096,65536):
            with self.subTest(s=s):
                row=random_original_five_clean_certificate(s)
                V,a,T,U=row["V"],row["a"],row["T"],row["U_unassigned_physical_pairs"]
                self.assertEqual(V,(s+1)*(s*s+1))
                self.assertEqual(T,comb(a,2))
                self.assertLess(comb(a-1,2),V)
                self.assertEqual(T-V,U)
                self.assertEqual(
                    Fraction(row["bad_missing_8_source_endpoint_labels"]),
                    Fraction(8*U,T-5))
                self.assertEqual(
                    Fraction(row["bad_original_GQ_incidence_geometry"]),
                    Fraction(56*(s+1),V-5))
                self.assertEqual(
                    Fraction(row[
                        "bad_exposed_original_anchor_intermediate_label_overlaps"]),
                    Fraction(16*(a-2),T-9))
                beta=Fraction(row["deferred_exposure_union_bound"])
                self.assertLess(beta,Fraction(1,4))
                self.assertEqual(Fraction(row[
                    "conditional_four_decoded_nonincident_clean_anchor_probability_lower"]),
                    1-beta)
                self.assertGreater(Fraction(row[
                    "expected_true_original_middle_four_clean_C_e_lower"]),
                    Fraction(s**4,1_000_000))
                self.assertTrue(row["REFUTED_universal_max_Ce_little_o_s4"])
                self.assertTrue(row["REFUTED_universal_sum_Ce_little_o_s8"])
                self.assertFalse(row["root_Branch_A_proved_or_refuted"])

    def test_L3_analytic_nonasymptotic_coarse_constant_proof_gates(self):
        # Independent elementary inequalities that yield s4 / 559872
        # from the lower exact probability formula for all s>=64.
        for s in (64,128,256,1024,8192,65536):
            with self.subTest(s=s):
                q=random_original_five_clean_certificate(s)
                a,T,V=q["a"],q["T"],q["V"]
                self.assertLessEqual(a*a,9*s**3)
                self.assertGreaterEqual(V,s**3)
                self.assertGreaterEqual(a,10)
                self.assertGreaterEqual(V-8,V//2)
                self.assertGreaterEqual(
                    Fraction(_falling(a-2,4),_falling(T-1,4)),
                    Fraction(1,a**4))
                beta=Fraction(q["deferred_exposure_union_bound"])
                # Exact rational beta and the elementary parameter
                # bounds are checked independently; the PDF-style
                # coarse inequality is proved symbolically in the note.
                self.assertLess(beta,Fraction(1,4))
                self.assertGreater(Fraction(q[
                    "expected_true_original_middle_four_clean_C_e_lower"]),
                    Fraction(s**4,1_000_000))
                self.assertGreater(Fraction(3,4*64*3**8),
                                   Fraction(1,1_000_000))

    def test_L4_true_original_five_source_matchings_lower_at_W32(self):
        # Independent actual ORIGINAL GQ matching count small finite
        # falsifier. Formula for ordered choices of four NEW sources
        # conservatively excludes each used original point and line.
        ctx=EndpointEnergy(fixture(1,"lex"))
        for middle in (0,10,44):
            usedP={ctx.inc[middle][0]}
            usedL={ctx.inc[middle][1]}
            tally=0
            def dfs(depth):
                nonlocal tally
                if depth==4:
                    tally+=1
                    return
                for p,l in ctx.inc:
                    if p in usedP or l in usedL:
                        continue
                    usedP.add(p)
                    usedL.add(l)
                    dfs(depth+1)
                    usedP.remove(p)
                    usedL.remove(l)
            dfs(0)
            lower=(ctx.s+1)**4
            for j in (1,2,3,4):
                lower*=ctx.v-2*j
            self.assertGreaterEqual(tally,lower)

    def test_L5_real_W34_two_global_original_label_maps_have_clean_templates(self):
        # Supporting finite actual ORIGINAL source evidence only:
        # neither those observations nor a single finite random
        # example establishes the all-h random-injection theorem.
        for scheme,total,max_e in (("lex",6421,129),("random",7968,133)):
            with self.subTest(scheme=scheme):
                model=fixture(2,scheme)
                data=finite_original_anchor_cascade_report(model)
                self.assertEqual(
                    data["all_original_source_stage_totals"][
                        "J_all_four_true_GQ_anchors_end_clean"],total)
                self.assertEqual(
                    data["largest_true_middle_stage_counts"][
                        "J_all_four_true_GQ_anchors_end_clean"],max_e)
                self.assertGreater(total,0)

    def test_L6_invalid_and_scope_negative_controls(self):
        for bad in (1,2,4,32,63,65,128.0,0):
            with self.subTest(s=bad):
                with self.assertRaisesRegex(ValueError,"s=2"):
                    random_original_five_clean_certificate(bad)
        with self.assertRaisesRegex(ValueError,"falling"):
            _falling(3,4)
        self.assertFalse(random_original_five_clean_certificate(64)[
            "positive_original_GF5_sixset_transfer_proved"])

    def test_L7_research_report_not_a_false_root_theorem(self):
        data=report()
        self.assertEqual(data["status"],"THEOREM_L_CLEAN_CAPACITY_NO_GO")
        self.assertEqual(data["root_A"],"OPEN")
        self.assertEqual(len(data["certificates"]),6)
        self.assertTrue(all(q["not_a_counterexample_to_H_e_little_o_s4"]
                            for q in data["certificates"]))


if __name__=="__main__":
    unittest.main()
