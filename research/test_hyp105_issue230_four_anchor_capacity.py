"""EICE-003-F finite source-oracle falsifiers and known quartic C4 lower."""
from fractions import Fraction
from itertools import product, combinations
import unittest

from hyp105_issue230_endpoint_energy import EndpointEnergy
from hyp105_issue230_four_anchor_capacity import (
    FourAnchorCapacity, blocked_checkerboard_or_adjacent,
    find_true_nonvacuous_w32, original_closure, quartic_c4_lower,
    all_h_blocked_plaquette_reservoir, report,
)
from hyp105_issue230_source_plaquettes import OriginalPlaquette, status_of_cell
from hyp105_issue230_paired_gstar import paired_gstar
from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1b0_seven_signature import (
    seven_census, classify_seven_prechecked, R3_CERTIFIED_FLOORS,
)


def direct_four_count(grid):
    r=len(grid)
    c=len(grid[0])
    return sum(all(grid[ii][jj] for ii,jj in
                   ((i,j),(i,l),(k,j),(k,l)))
               for i,k in combinations(range(r),2)
               for j,l in combinations(range(c),2))


class FourAnchorTests(unittest.TestCase):
    def test_F2_all_three_to_the_four_blocker_signatures(self):
        adjacency=((0,1),(0,2),(1,3),(2,3))
        checkerboard=0
        for masks in product((1,2,3),repeat=4):
            cls=blocked_checkerboard_or_adjacent(masks)
            self.assertEqual(len(cls["signature"]),4)
            direct=tuple((i,j) for i,j in adjacency if masks[i]&masks[j])
            self.assertEqual(cls["adjacent_same_side_edges"],direct)
            self.assertEqual(cls["shared_anchor_side"],bool(direct))
            if not direct:
                checkerboard+=1
                self.assertTrue(cls["strict_checkerboard"])
                self.assertIn(masks,((1,2,2,1),(2,1,1,2)))
            else:
                self.assertFalse(cls["strict_checkerboard"])
        self.assertEqual(checkerboard,2)
        with self.assertRaisesRegex(ValueError,"four nonempty"):
            blocked_checkerboard_or_adjacent((1,0,3,2))

    def test_F4_quartic_supersaturation_ALL_binary_small_grids(self):
        for r,c in ((2,2),(2,3),(3,3),(3,4)):
            tot=r*c
            denom=Fraction(r*(r-1)*c*(c-1),4)
            for bitset in range(1<<tot):
                grid=[[bool(bitset&(1<<(i*c+j))) for j in range(c)]
                      for i in range(r)]
                ones=bitset.bit_count()
                actual=Fraction(direct_four_count(grid),denom)
                low=quartic_c4_lower(r,c,ones)
                self.assertLessEqual(low,actual)
                self.assertGreaterEqual(low,0)
        self.assertEqual(quartic_c4_lower(2,2,0),0)
        with self.assertRaisesRegex(ValueError,"valid binary"):
            quartic_c4_lower(2,3,7)

    def test_F5_exact_all_h_omega_s8_to_conditional_s6_transfer(self):
        # Numeric Fraction tests for the independently proved symbolic
        # EICE-002 density/degree + EICE-003-E orientation sampling lemma.
        # Absolutely no assumption that a GF5 transfer actually exists.
        delta=Fraction(1,1_000_000)
        for s in (2**22,2**23,2**26):
            row=all_h_blocked_plaquette_reservoir(s,Fraction(1))
            expected=delta**4*Fraction(s**8,1_280_000)
            self.assertEqual(
                Fraction(row["explicit_oriented_allblocked_true_GQ_plaquette_count_lower"]),
                expected)
            self.assertFalse(row["universal_four_anchor_transfer_proved"])
            self.assertFalse(row["unconditional_positive_GF5_sixset_lower_proved"])
            if s==2**22:
                # This is a PURE HYPOTHETICAL mapping with at most 7*s²
                # preimages per actual positive original six-incidence set.
                only_if=all_h_blocked_plaquette_reservoir(
                    s,Fraction(1),proposed_transfer_K=7)
                self.assertEqual(
                    Fraction(only_if["ONLY_IF_TRANSFER_EXISTS_S_lower"]),
                    expected/(7*s*s))
                self.assertFalse(only_if["universal_four_anchor_transfer_proved"])
        for theta in (Fraction(),Fraction(1,2),Fraction(3,4)):
            row=all_h_blocked_plaquette_reservoir(2**22,theta)
            self.assertEqual(Fraction(
                row["explicit_oriented_allblocked_true_GQ_plaquette_count_lower"]),0)
        near=all_h_blocked_plaquette_reservoir(2**22,Fraction(7,8))
        self.assertEqual(Fraction(
            near["uniform_oriented_square_allblocked_probability_lower"]),Fraction(1,2))
        # At fixed positive theta, F6 becomes positive once active
        # degree is sufficiently high, unlike 4*theta-3.
        s=2**26
        moderate=all_h_blocked_plaquette_reservoir(s,Fraction(1,2))
        floor=Fraction(1,16)-Fraction(2,delta*s-1)
        self.assertGreater(floor,0)
        self.assertEqual(Fraction(moderate["F6_C4_Jensen_quartic_lower"]),floor)
        self.assertEqual(Fraction(moderate[
            "uniform_oriented_square_allblocked_probability_lower"]),floor)
        self.assertEqual(Fraction(moderate[
            "explicit_oriented_allblocked_true_GQ_plaquette_count_lower"]),
            floor*delta**4*s**8/Fraction(1_280_000))
        self.assertEqual(Fraction(moderate["F5_four_union_lower"]),0)
        with self.assertRaisesRegex(ValueError,"exact stationary"):
            all_h_blocked_plaquette_reservoir(64,Fraction(1))
        with self.assertRaisesRegex(ValueError,"hypothetical transfer"):
            all_h_blocked_plaquette_reservoir(2**22,Fraction(1),proposed_transfer_K=0)

    def test_true_W32_four_canonical_Gstar_scopes_and_status(self):
        for scheme in ("lex","reverse","S68","S72"):
            with self.subTest(scheme=scheme):
                model=fixture(1,scheme)
                p=paired_gstar(model)
                F=FourAnchorCapacity(
                    model,p["original_incidence_ids"],
                    p["colors_left"],p["colors_right"])
                row=F.census(independent=True)
                self.assertEqual(row["status"],"RESTRICTED_THEOREM_C")
                self.assertFalse(row["universal_four_anchor_capacity_proved"])
                self.assertFalse(row["bounded_multiplicity_GF5_transfer_proved"])
                self.assertFalse(row["root_Branch_A_proved"])
                self.assertEqual(row["true_original_2x2_plaquettes"],0)
                self.assertEqual(row["all_four_blocked_plaquettes"],0)
                self.assertEqual(row["F4_known_quartic_lower"],None)

    def test_true_W34_two_globally_injected_original_source_maps(self):
        for scheme in ("lex","random"):
            with self.subTest(scheme=scheme):
                model=fixture(2,scheme)
                p=paired_gstar(model)
                row=FourAnchorCapacity(
                    model,p["original_incidence_ids"],
                    p["colors_left"],p["colors_right"]).census(
                        max_paths=400_000,max_plaquettes=90_000)
                self.assertEqual(row["N"],425)
                self.assertFalse(row["frozen_W32_seven_classifier_available"])
                self.assertEqual(row["canonical_path_seven_classes"],{})
                self.assertLessEqual(row["all_four_blocked_plaquettes"],
                                     row["all_four_end_clean_plaquettes"])
                self.assertTrue(row["F4_quartic_is_standard_C4_supersaturation"])

    def test_nonvacuous_true_W32_five_source_and_W32_seven_index(self):
        model=fixture(1,"lex")
        witness=find_true_nonvacuous_w32(model)
        self.assertEqual(len(witness["selected"]),5)
        self.assertGreater(witness["plaquettes"],0)
        audit=FourAnchorCapacity(model,witness["selected"],
                                 witness["colors_left"],
                                 witness["colors_right"])
        row=audit.census(exact_W32_GF5_index=True,independent=True)
        self.assertGreater(row["true_original_2x2_plaquettes"],0)
        self.assertTrue(row["frozen_W32_seven_classifier_available"])
        self.assertGreater(row["all_endpoint_complete_plaquettes"],0)
        self.assertTrue(all(int(x)<=17 for x in row[
            "allblocked_original_scope_sizes"]))
        self.assertEqual(sum(row["observed_blocker_signatures"].values()),
                         row["all_four_blocked_plaquettes"])
        self.assertGreater(
            row["complete_source_plaquettes_verified_against_W32_index"],0)
        # The first genuine coherent 5-source square need not contain
        # any nonincident endpoint anchor, so there may be ZERO LOCAL
        # sixset subsets to compare. Never manufacture GF5 evidence.
        self.assertGreaterEqual(
            row["independent_W32_full_seven_index_comparisons"],0)
        self.assertEqual(row["all_four_blocked_plaquettes"],0)
        self.assertEqual(row["observed_scope_seven_hits"],{})
        # Any accepted motif on a merely endpoint-complete plaquette is
        # diagnostic and MUST NOT be counted as blocked-square transfer.
        self.assertIsInstance(
            row["complete_source_scope_seven_hits_NOT_compensation"],dict)
        independent=seven_census(model,independent_checks=False,
                                 witness_sets=True)
        # These are REAL GLOBAL W32 six-incidence witnesses used as
        # independent POSITIVE classifier controls, not compensation
        # witnesses attached to the five-source plaquette.
        for tag,ids in independent["witnesses"].items():
            self.assertEqual(classify_seven_prechecked(
                ids,tuple(model["left_labels"]),
                tuple(model["right_labels"]),
                tuple(model["incidences"])),tag)
            self.assertIn(tag,R3_CERTIFIED_FLOORS)

    def test_true_original_canonical_six_source_closure_and_overlap(self):
        model=fixture(1,"lex")
        ctx=EndpointEnergy(model)
        found=False
        for (w,u,v,z),_ in ctx._iter_nb(200_000):
            mid=ctx.provenance[tuple(sorted((u,v)))]
            st,q,r=status_of_cell(ctx,mid,w,z)
            if st not in (3,4):
                continue
            first=ctx.provenance[tuple(sorted((w,u)))]
            last=ctx.provenance[tuple(sorted((v,z)))]
            closure=original_closure(ctx,(first,mid,last),q,r)
            self.assertEqual(len(closure["path_source_ids"]),3)
            self.assertEqual(len(closure["anchor_source_ids"]),3)
            self.assertEqual(len(set(closure["distinct_original_incidences"])),
                             closure["source_union_size"])
            self.assertEqual(set(closure["anchor_source_ids"]),
                             {ctx.edge_id[(q,ctx.anchor[q,r][1])],
                              ctx.edge_id[ctx.anchor[q,r]],
                              ctx.edge_id[(ctx.anchor[q,r][0],r)]})
            if closure["certified_seven_class"]:
                self.assertEqual(closure["source_union_size"],6)
                self.assertIn(closure["certified_seven_class"],R3_CERTIFIED_FLOORS)
            found=True
            break
        self.assertTrue(found)
        with self.assertRaisesRegex(AssertionError,"three distinct"):
            original_closure(ctx,(0,0,1),q,r)

    def test_strict_genuine_source_rejections_and_termination_budgets(self):
        model=fixture(1,"lex")
        p=paired_gstar(model)
        with self.assertRaisesRegex(ValueError,"finite ORIGINAL source budgets"):
            FourAnchorCapacity(
                model,p["original_incidence_ids"],
                p["colors_left"],p["colors_right"]).census(max_plaquettes=-1)
        with self.assertRaisesRegex(ValueError,"W32 true source"):
            find_true_nonvacuous_w32(model,max_candidates=0)
        with self.assertRaisesRegex(ValueError,"bichromatic"):
            FourAnchorCapacity(model,p["original_incidence_ids"],
                               [0]*model["a"],p["colors_right"])
        with self.assertRaisesRegex(ValueError,"global injective"):
            corrupt=fixture(1,"lex")
            corrupt["left_labels"]=list(corrupt["left_labels"])
            corrupt["left_labels"][0]=corrupt["left_labels"][1]
            FourAnchorCapacity(corrupt,p["original_incidence_ids"],
                               p["colors_left"],p["colors_right"])
        with self.assertRaisesRegex(ValueError,"global seven-class witness"):
            m4=fixture(2,"lex")
            q=paired_gstar(m4)
            FourAnchorCapacity(m4,q["original_incidence_ids"],
                               q["colors_left"],q["colors_right"]).census(
                exact_W32_GF5_index=True)

    def test_research_report_no_false_transfer(self):
        data=report()
        self.assertEqual(data["status"],"RESTRICTED_THEOREM_C")
        self.assertEqual(data["root_A"],"OPEN")
        self.assertEqual(len(data["models"]),5)
        self.assertGreater(data["models"][-1]["true_original_2x2_plaquettes"],0)


if __name__=="__main__":
    unittest.main()
