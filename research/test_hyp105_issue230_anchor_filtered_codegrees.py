"""EICE-003-J independent true original GF(5)-agnostic four-anchor cascade."""
from collections import Counter
from itertools import combinations
from fractions import Fraction
import unittest

from hyp105_issue230_endpoint_energy import EndpointEnergy
from hyp105_issue230_projection import fixture
from hyp105_issue230_quadrant_matching_capacity import (
    original_midpoint_quadrants, valid_original_two_arm_pairs,
    exact_local_middle_capacity,
)
from hyp105_issue230_anchor_filtered_codegrees import (
    two_arm_matching_count, independent_original_anchor_status,
    exact_original_anchor_middle_census, finite_original_anchor_cascade_report,
    STAGES, FILTERS, report,
)
from hyp105_issue230_source_plaquettes import status_of_cell
from hyp105_issue230_five_source_blocked_search import FiveSourceSearch


def independent_direct_quadruple_count(ctx,e,max_checks=3_000_000):
    """Brute physical 2x2 original path endpoint status, no codegree algebra."""
    groups=original_midpoint_quadrants(ctx,e)
    counts=[0]*len(STAGES)
    checked=0
    for qa,qb in ((0,3),(1,2)):
        for a,b in combinations(groups[qa],2):
            if a[1]==b[1] or a[2]==b[2]:
                continue
            for c,d in combinations(groups[qb],2):
                checked+=1
                if checked>max_checks:
                    raise ValueError("true GQ independent enumeration budget exceeded")
                if c[1]==d[1] or c[2]==d[2]:
                    continue
                if (a[1] in (c[1],d[1]) or b[1] in (c[1],d[1]) or
                        a[2] in (c[2],d[2]) or b[2] in (c[2],d[2])):
                    continue
                status=[independent_original_anchor_status(
                    ctx,e,w[1]*ctx.a+w[2],z[1]*ctx.a+z[2])[0]
                    for w,z in ((a,c),(a,d),(b,c),(b,d))]
                for k,allowed in enumerate(FILTERS):
                    if all(v in allowed for v in status):
                        counts[k]+=1
    return tuple(counts)


class OriginalFourAnchorCodegreeTests(unittest.TestCase):
    def test_J1_formula_exhaustive_abstract_binary_partner_grids(self):
        # A quadrant is a simple bipartite original arm graph on
        # outer physical x/y. Validate exact two-edge matching count.
        for n in range(1,9):
            records=[(i,(3*i+2)%5,(7*i+1)%7) for i in range(n)]
            if len({(a[1],a[2]) for a in records})!=n:
                continue
            actual=sum(a[1]!=b[1] and a[2]!=b[2]
                       for a,b in combinations(records,2))
            self.assertEqual(two_arm_matching_count(records),actual)
        self.assertEqual(two_arm_matching_count([(1,3,7),(2,3,8),(3,4,7)]),1)
        with self.assertRaisesRegex(ValueError,"distinct true ORIGINAL"):
            two_arm_matching_count([(1,3,7),(1,4,8)])
        with self.assertRaisesRegex(ValueError,"distinct original arm"):
            two_arm_matching_count([(1,3,7),(2,3,7)])

    def test_J2_real_W32_ALL_middle_direct_original_quadruple_comparison(self):
        for scheme in ("lex","reverse","S68","S72"):
            with self.subTest(scheme=scheme):
                ctx=EndpointEnergy(fixture(1,scheme))
                totals=[0]*len(STAGES)
                for e in range(ctx.N):
                    got=exact_original_anchor_middle_census(ctx,e)
                    expected=independent_direct_quadruple_count(ctx,e)
                    self.assertEqual(got[
                        "cumulative_all_four_corner_source_counts"],expected)
                    from_i=exact_local_middle_capacity(ctx,e)
                    self.assertEqual(expected[0],from_i[
                        "unique_x_y_coordinate_disjoint_five_source_templates"])
                    self.assertEqual(sum(got[
                        "all_four_blocker_channels"].values()),expected[-1])
                    totals=[a+b for a,b in zip(totals,expected)]
                self.assertEqual(totals[-1],0)
                self.assertGreater(totals[0],0)

    def test_J2_real_W34_sampled_middle_direct_ORIGINAL_four_anchor_oracle(self):
        for scheme in ("lex","random"):
            with self.subTest(scheme=scheme):
                ctx=EndpointEnergy(fixture(2,scheme))
                for e in (0,10,26,45,126,206,ctx.N-1):
                    got=exact_original_anchor_middle_census(ctx,e)
                    direct=independent_direct_quadruple_count(ctx,e)
                    self.assertEqual(got[
                        "cumulative_all_four_corner_source_counts"],direct)
                    self.assertEqual(got[
                        "cumulative_all_four_corner_source_counts"][0],
                        exact_local_middle_capacity(ctx,e)[
                            "unique_x_y_coordinate_disjoint_five_source_templates"])

    def test_J3_real_W34_entire_global_cascade_matches_independent_physical_G(self):
        for scheme,expected in (("lex",467),("random",575)):
            with self.subTest(scheme=scheme):
                model=fixture(2,scheme)
                data=finite_original_anchor_cascade_report(model)
                self.assertEqual(data[
                    "original_allblocked_five_source_family_count"],expected)
                self.assertEqual(data[
                    "all_original_source_stage_totals"][STAGES[0]],
                    251962 if scheme=="lex" else 212905)
                self.assertEqual(data[
                    "largest_true_middle_stage_counts"][STAGES[-1]],
                    18 if scheme=="lex" else 13)
                counts=list(data["all_original_source_stage_totals"].values())
                self.assertTrue(all(x>=y for x,y in zip(counts,counts[1:])))
                self.assertEqual(sum(data[
                    "original_blocker_mask_channels"].values()),expected)
                self.assertEqual(sum(data[
                    "allblocked_original_GQ_4x4_cross_histogram"].values()),expected)
                self.assertTrue(all(int(k)<=8 for k in data[
                    "allblocked_original_GQ_4x4_cross_histogram"]))
                self.assertTrue(data["full_independent_G_source_crosscheck"])
                self.assertFalse(data["o_s4_real_source_capacity_proved"])
                self.assertFalse(data["original_GF5_positive_sixset_transfer_proved"])

    def test_J4_exact_source_stages_not_an_unproved_asymptotic_capacity(self):
        for scheme in ("lex","random"):
            ctx=EndpointEnergy(fixture(2,scheme))
            e=10
            result=exact_original_anchor_middle_census(
                ctx,e,retain_allblocked_source_sets=True)
            stages=result["cumulative_all_four_corner_source_counts"]
            self.assertEqual(stages[0],exact_local_middle_capacity(ctx,e)[
                "unique_x_y_coordinate_disjoint_five_source_templates"])
            self.assertEqual(len(result[
                "allblocked_true_original_five_source_ids"]),stages[-1])
            self.assertEqual(sum(result[
                "first_failed_source_filter_counts"]),stages[0]-stages[-1])
            self.assertTrue(result["J_true_source_codegree_formula_exact"])
            self.assertFalse(result["uniform_o_s4_four_anchor_capacity_proved"])

    def test_negative_budget_and_independent_source_status_controls(self):
        ctx=EndpointEnergy(fixture(1,"lex"))
        with self.assertRaisesRegex(ValueError,"nonnegative"):
            exact_original_anchor_middle_census(ctx,0,max_source_pair_checks=-1)
        with self.assertRaisesRegex(ValueError,"nonnegative"):
            exact_original_anchor_middle_census(ctx,0,max_blocked_expansions=-1)
        with self.assertRaisesRegex(ValueError,"distinct true ORIGINAL"):
            two_arm_matching_count([(1,2,3),(1,4,5)])
        # True actual G source paths are proper only after coordinate
        # quartet validation. Independent original status must refuse
        # loops rather than silently classify them as missing.
        with self.assertRaisesRegex(AssertionError,"coordinate-proper"):
            independent_original_anchor_status(ctx,0,0,0)
        with self.assertRaisesRegex(ValueError,"budget"):
            nonzero=next(e for e in range(ctx.N) if
                exact_local_middle_capacity(ctx,e)[
                "pair_product_pre_cross_upper"]>0)
            exact_original_anchor_middle_census(ctx,nonzero,max_source_pair_checks=0)

    def test_research_report_all_true_original_source_maps_no_branch_A(self):
        data=report()
        self.assertEqual(data["status"],"RESTRICTED_THEOREM_J")
        self.assertEqual(data["root_A"],"OPEN")
        self.assertEqual(len(data["maps"]),6)
        self.assertEqual(data["maps"][4][
            "original_allblocked_five_source_family_count"],467)
        self.assertEqual(data["maps"][5][
            "original_allblocked_five_source_family_count"],575)
        self.assertTrue(all(not r["root_Branch_A_proved"] for r in data["maps"]))


if __name__=="__main__":
    unittest.main()
