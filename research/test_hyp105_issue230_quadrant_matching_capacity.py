"""EICE-003-I: independent original source quadrant template/packing proofs."""
from fractions import Fraction
from itertools import combinations
import unittest

from hyp105_issue230_endpoint_energy import EndpointEnergy
from hyp105_issue230_projection import fixture
from hyp105_issue230_five_source_blocked_search import (
    FiveSourceSearch, exact_five_source_coherence
)
from hyp105_issue230_quadrant_matching_capacity import (
    original_midpoint_quadrants, valid_original_two_arm_pairs,
    exact_local_middle_capacity, true_five_source_middle_template,
    conditional_improved_source_packing, finite_quadrant_report,
    paired_five_source_component_certificate, report,
)
from hyp105_issue230_four_anchor_capacity import all_h_blocked_plaquette_reservoir


class TrueOriginalQuadrantPackingTests(unittest.TestCase):
    def test_I1_true_middle_all_four_quadrants_disjoint_and_complete(self):
        for h,scheme in ((1,"lex"),(1,"reverse"),(2,"lex"),(2,"random")):
            with self.subTest(h=h,scheme=scheme):
                ctx=EndpointEnergy(fixture(h,scheme))
                for e in range(ctx.N):
                    quads=original_midpoint_quadrants(ctx,e)
                    self.assertEqual(len(quads),4)
                    self.assertEqual(len(set(i for q in quads for i,_,_ in q)),
                                     sum(len(q) for q in quads))
                    p2,l2=ctx.inc[e]
                    for k,q in enumerate(quads):
                        for i,x,y in q:
                            p,l=ctx.inc[i]
                            self.assertNotEqual(p,p2)
                            self.assertNotEqual(l,l2)
                            self.assertNotIn(x,ctx.f[p2])
                            self.assertNotIn(y,ctx.g[l2])
                            xx=set(ctx.f[p])&set(ctx.f[p2])
                            yy=set(ctx.g[l])&set(ctx.g[l2])
                            self.assertEqual(len(xx),1)
                            self.assertEqual(len(yy),1)
                            a=0 if next(iter(xx))==ctx.f[p2][0] else 1
                            b=0 if next(iter(yy))==ctx.g[l2][0] else 1
                            self.assertEqual(k,a*2+b)

    def test_I2_strict_two_pair_disjointness_and_coherent_physical_diagonals_W32_W34(self):
        for h,scheme in ((1,"lex"),(2,"lex"),(2,"random")):
            with self.subTest(h=h,scheme=scheme):
                model=fixture(h,scheme)
                ctx=EndpointEnergy(model)
                validated=0
                for e in range(ctx.N):
                    result=exact_local_middle_capacity(
                        ctx,e,max_pair_comparisons=3_000_000,retain_families=True)
                    self.assertLessEqual(
                        result["unique_x_y_coordinate_disjoint_five_source_templates"],
                        result["pair_product_pre_cross_upper"])
                    ids_list=result["exact_families"]
                    self.assertEqual(len(ids_list),len(set(ids_list)))
                    for ids in ids_list[:2]:
                        self.assertTrue(true_five_source_middle_template(ctx,e,ids))
                        o=exact_five_source_coherence(model,ids,ctx=ctx)
                        self.assertIsNotNone(o)
                        shape=paired_five_source_component_certificate(o[0].ctx,e)
                        self.assertEqual(shape["oriented_two_by_two_plaquettes"],2)
                        self.assertEqual(shape["five_disconnected_paired_diagonals"],5)
                        self.assertTrue(shape["I3_all_h_original_middle_unique"])
                        proper=o[0].census(max_paths=2000,max_plaquettes=50)
                        self.assertGreater(proper["total_2x2_plaquettes"],0)
                        validated+=1
                self.assertGreater(validated,0)

    def test_I2_every_real_true_original_W34_blocked_five_source_middle_is_eligible(self):
        for scheme,expected in (("lex",467),("random",575)):
            with self.subTest(scheme=scheme):
                model=fixture(2,scheme)
                ctx=EndpointEnergy(model)
                data=FiveSourceSearch(model).census(
                    export_true_five_source_families=True)
                rows=data["TRUE_ORIGINAL_five_source_families"]
                self.assertEqual(len(rows),expected)
                for row in rows:
                    ids=tuple(row["original_incidence_ids"])
                    self.assertLessEqual(len(row["original_middle_source_ids"]),5)
                    for e in row["original_middle_source_ids"]:
                        self.assertTrue(true_five_source_middle_template(ctx,e,ids))
                self.assertEqual(sum(row[
                    "oriented_fourblock_multiplicity"] for row in rows),expected*2)

    def test_I3_each_five_source_supports_only_2_orientations_per_middle(self):
        for h,scheme in ((1,"lex"),(2,"lex"),(2,"random")):
            model=fixture(h,scheme)
            ctx=EndpointEnergy(model)
            total_checked=0
            for e in range(ctx.N):
                rows=exact_local_middle_capacity(
                    ctx,e,retain_families=True,max_pair_comparisons=3_000_000)
                for ids in rows["exact_families"][:3]:
                    o=exact_five_source_coherence(model,ids,ctx=ctx)
                    self.assertIsNotNone(o)
                    # A 5-ID true coordinate-proper source square anchored
                    # at this e has precisely one physical middle diagonal
                    # supporting two outer arms at BOTH endpoints, and its
                    # reverse oriented middle edge yields the other.
                    subset=o[0].ctx
                    physical_orientations=0
                    for u,neighbors in enumerate(subset.adj):
                        for v in neighbors:
                            if subset.provenance[tuple(sorted((u,v)))]!=e:
                                continue
                            A=neighbors-{v}
                            B=subset.adj[v]-{u}
                            if len(A)>=2 and len(B)>=2:
                                physical_orientations+=1
                    self.assertEqual(physical_orientations,2)
                    certificate=paired_five_source_component_certificate(subset,e)
                    self.assertEqual(certificate["active_physical_vertices"],16)
                    self.assertEqual(certificate["five_disconnected_paired_diagonals"],5)
                    self.assertEqual(certificate["unique_original_middle_source_id"],e)
                    total_checked+=1
            self.assertGreater(total_checked,0)

    def test_I4_sharp_conditional_all_h_five_family_and_heavy_middle_bounds(self):
        for s,theta in ((2**22,Fraction(1)),(2**26,Fraction(1,2)),
                        (2**26,Fraction(7,8))):
            prior=all_h_blocked_plaquette_reservoir(s,theta)
            P=Fraction(prior[
                "explicit_oriented_allblocked_true_GQ_plaquette_count_lower"])
            row=conditional_improved_source_packing(s,theta)
            N=(s+1)**2*(s*s+1)
            self.assertEqual(row[
                "max_oriented_plaquettes_per_fixed_middle_and_five_source_family"],2)
            self.assertEqual(row[
                "max_oriented_plaquettes_per_five_source_family_all_middles"],2)
            self.assertEqual(Fraction(row[
                "distinct_true_original_five_source_families_lower"]),P/2)
            self.assertEqual(Fraction(row[
                "at_least_one_middle_original_source_families_lower"]),P/(2*N))
            self.assertFalse(row["o_s4_capacity_or_GF5_transfer_proved"])
        with self.assertRaisesRegex(ValueError,"exact stationary"):
            conditional_improved_source_packing(16,Fraction(1))

    def test_I5_full_original_W34_capacity_audit_lex_random(self):
        for scheme,expected in (("lex",467),("random",575)):
            model=fixture(2,scheme)
            r=finite_quadrant_report(model,compare_sample=5)
            self.assertEqual(r["true_blocked_five_source_families"],expected)
            self.assertEqual(r["all_true_middle_source_incidences_audited"],425)
            self.assertTrue(r["full_true_middle_census"])
            self.assertGreaterEqual(r["largest_single_middle_exact_template_capacity"],
                                    r["largest_observed_true_blocked_family_count_per_middle"])
            self.assertGreater(r["independent_both_diagonals_proper_square_template_validations"],0)
            self.assertFalse(r["uniform_o_s4_true_blocking_capacity_proved"])

    def test_abstract_two_arm_matching_counts_and_fail_closed_budgets(self):
        source=((1,10,20),(2,10,21),(3,11,20),(4,12,22))
        valid=valid_original_two_arm_pairs(source)
        self.assertEqual(len(valid),4)
        self.assertEqual(len(valid_original_two_arm_pairs(((1,10,20),))),0)
        with self.assertRaisesRegex(ValueError,'exactly five'):
            paired_five_source_component_certificate(
                EndpointEnergy(fixture(1,'lex'),selected=[0]),0)
        ctx=EndpointEnergy(fixture(2,'lex'))
        with self.assertRaisesRegex(ValueError,'nonnegative exact'):
            exact_local_middle_capacity(ctx,0,max_pair_comparisons=-1)
        # A zero-comparison budget must fail closed on a real e with
        # at least one pair-product source candidate.
        candidate=next(e for e in range(ctx.N) if
            exact_local_middle_capacity(ctx,e,exact_cross=False)[
                'pair_product_pre_cross_upper']>0)
        with self.assertRaisesRegex(ValueError,'compatibility budget'):
            exact_local_middle_capacity(ctx,candidate,max_pair_comparisons=0)
        self.assertFalse(true_five_source_middle_template(ctx,0,(0,0,1,2,3)))
        self.assertFalse(true_five_source_middle_template(ctx,0,(1,2,3,4,5)))

    def test_report_true_original_all_maps_no_GF5_promotion(self):
        r=report()
        self.assertEqual(r["status"],"RESTRICTED_THEOREM_I")
        self.assertEqual(r["root_A"],"OPEN")
        self.assertEqual(len(r["maps"]),6)
        self.assertEqual(r["maps"][4]["true_blocked_five_source_families"],467)
        self.assertEqual(r["maps"][5]["true_blocked_five_source_families"],575)
        self.assertTrue(all(not x["root_Branch_A_proved"] for x in r["maps"]))


if __name__=="__main__":
    unittest.main()
