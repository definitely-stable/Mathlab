"""AA4-AT independent source GQ forest Hall 0/1 and true original audits."""
import unittest
from collections import Counter
from itertools import combinations

from hyp105_issue230_d6aa4at_original_forest_unique_hall import (
    all_h_original_threeflag_forest_unique_certificate,
    unique_original_threeflag_forest_Hall,
    exact_original_wedge_forest_Hall_audit)
from hyp105_issue230_d6aa4as_threeflag_hall_frontier import (
    original_opposite_wedge_context,
    _original_threeflag_Hall_completions,
    exact_original_opposite_threeflag_six_Q_funnel)
from hyp105_issue230_d6aa4aq_colored_original_D_cycle import (
    exact_original_rainbow_D6_cycle_transfer)
from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import (
    zero_split_original_W32)
from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ab_minimax_orbit_normalform import (
    symplectic_transvection_source,transform_model)


def literal_source_good_opposite_wedges(context):
    """Independent actual original centered D-neighbor list traversal."""
    for center,row in enumerate(context["good_neighbors"]):
        for (i,pc,lc),(k,pd,ld) in combinations(row,2):
            if pc!=pd and lc!=ld:
                yield (center,)+tuple(sorted((i,k)))


def _old_permutation_source_hall(inc,point,line):
    return _original_threeflag_Hall_completions(
        inc,(0,1,2),("A",tuple(point),()),("A",tuple(line),()))


class OriginalGQThreeflagForestHall(unittest.TestCase):
    def test_01_all_h_symbolic_original_source_unique_hall_capacity(self):
        for h in tuple(range(1,27))+(32,40,50,60):
            z=all_h_original_threeflag_forest_unique_certificate(1<<h)
            a=z["a"]
            self.assertEqual(z["T_formal_one_typed_residual_templates"],
                             (a-3)*(a-4)*(a-5)//6)
            self.assertEqual(z["P_formal_one_typed_residual_templates"],
                             3*(a-4)*(a-5)//2)
            self.assertEqual(z["TP_formal_two_typed_capacity"],
                             z["T_formal_one_typed_residual_templates"]*
                             z["P_formal_one_typed_residual_templates"])
            self.assertEqual(z["max_original_three_new_flag_Hall_Q_PER_OCCUPIED_PAIR"],1)
            self.assertTrue(z["original_induced_six_source_factor_graph_is_forest"])
            self.assertTrue(z["forest_uniqueness_holds_with_doubled_source_factors"])
            self.assertTrue(z["no_uniform_positive_seven_GF5_coverage_proved"])
        for invalid in (0,3,True,-2):
            with self.assertRaises(ValueError):
                all_h_original_threeflag_forest_unique_certificate(invalid)

    def test_02_independent_literal_girth8_forests_repeated_factor_degree_demand(self):
        # Purely small INPUT degree forests illustrating mechanics;
        # these are NOT falsely asserted to be a full original GQ.
        # Mathematical theorem uses the induced acyclicity of genuine
        # W(3,s) source incidence graph for global correctness.
        examples=[
            ({(0,0):10,(1,1):11,(2,2):12},(0,1,2),(0,1,2),
             (0,1,2,10,11,12)),
            ({(0,0):10,(0,1):11,(1,0):12},(0,0,1),(0,1,0),
             (0,1,2,10,11,12)),
            ({(0,0):10,(0,1):11,(1,0):12},(0,0,1),(0,0,1),
             (0,1,2,10,11,12)),
            ({(0,0):10,(1,1):11},(0,0,1),(0,0,1),None),
            ({(0,0):10,(0,1):11,(1,0):12},(0,1,2),(0,1,2),None),
        ]
        for inc,left,right,expected in examples:
            f=("A",left,())
            g=("A",right,())
            cert=unique_original_threeflag_forest_Hall(
                inc,(0,1,2),f,g,with_certificate=True)
            self.assertEqual(cert["unique_genuine_original_six_incidence_Q"],expected)
            brute=_old_permutation_source_hall(inc,left,right)
            self.assertEqual(brute,set() if expected is None else {expected})
            self.assertTrue(cert["original_three_new_source_flag_Hall_unique_0_or_1"])
        # One physically repeated original point factor/line factor
        # cannot count the SAME genuine original point-line flag twice:
        repeated={(0,0):10,(1,1):11}
        self.assertIsNone(unique_original_threeflag_forest_Hall(
            repeated,(0,1,2),("B",(0,0,1),()),("B",(0,0,1),())))
        # Excluding a pinned source flag can kill the only candidate.
        forest={(0,0):0,(1,1):10,(2,2):11}
        self.assertIsNone(unique_original_threeflag_forest_Hall(
            forest,(0,1,2),("A",(0,1,2),()),("A",(0,1,2),())))

    def test_03_reject_nonoriginal_source_four_or_six_incidence_cycles(self):
        K22={(0,0):10,(0,1):11,(1,0):12,(1,1):13,(2,2):14}
        C6={(0,0):10,(0,1):11,(1,1):12,(1,2):13,
            (2,2):14,(2,0):15}
        for invalid_source in (K22,C6):
            with self.assertRaisesRegex(ValueError,"not a genuine GQ residual forest"):
                unique_original_threeflag_forest_Hall(
                    invalid_source,(0,1,2),
                    ("A",(0,1,2),()),("A",(0,1,2),()))
        for left,right in (((0,1),(0,1,2)),((0,1,2),(0,1,2,3))):
            with self.assertRaises(ValueError):
                unique_original_threeflag_forest_Hall(
                    {(0,0):10},(0,1,2),("A",left,()),("A",right,()))
        with self.assertRaises(ValueError):
            unique_original_threeflag_forest_Hall(
                {(0,0):10},(0,1,1),("A",(0,0,1),()),("A",(0,1,1),()))

    def test_04_all_five_real_original_W32_global_f_g_every_opposite_good_wedge(self):
        expected={
            "dual_zero":(870,5328,150,40),
            "lex":(1105,7233,505,237),
            "reverse":(1013,6351,232,68),
            "S68":(697,4041,46,6),
            "S72":(750,4386,85,11),
        }
        for name,m in [("dual_zero",zero_split_original_W32())]+[
                (scheme,fixture(1,scheme)) for scheme in ("lex","reverse","S68","S72")]:
            context=original_opposite_wedge_context(m)
            all_wedges=tuple(literal_source_good_opposite_wedges(context))
            wedge_orig_Q=0
            occupied=0
            nonzero=0
            for wedge in all_wedges:
                a=exact_original_wedge_forest_Hall_audit(
                    m,wedge,context=context,require_good=True,
                    crosscheck_permutation=True)
                count=a["unique_genuine_original_six_ID_Q_count"]
                wedge_orig_Q+=count
                occupied+=a["globally_occupied_two_typed_residual_template_pairs"]
                nonzero+=bool(count)
                self.assertEqual(
                    a["globally_occupied_two_typed_residual_template_pairs"],
                    a["original_forest_Hall_zero_occupied_template_pairs"]+
                    a["original_forest_Hall_positive_occupied_template_pairs"])
                self.assertEqual(count,
                    a["original_forest_Hall_positive_occupied_template_pairs"])
            self.assertEqual((len(all_wedges),occupied,wedge_orig_Q),
                             expected[name][:3])
            # Source Hall stage cannot be promoted to GF5 selected:
            # this number is genuine ORIGINAL source Q Hall incidence
            # charge, while 4th number is accepted sevenclass charge.
            self.assertGreaterEqual(wedge_orig_Q,expected[name][3])
            print("AA4AT_GENUINE_W32",name,
                  "true_original_opposite_good_wedges",len(all_wedges),
                  "globally_occupied_residual_template_pairs",occupied,
                  "original_source_forest_boolean_Hall_true_pairs",wedge_orig_Q,
                  "wedge_at_least_one_original_Hall_Q",nonzero,
                  "seven_GF5_positive_Q_wedge_charge_independent",expected[name][3])

    def test_05_true_original_W34_witness_source_forest_Hall_vs_seven_Q(self):
        for name in ("lex","random"):
            m=fixture(2,name)
            sample=exact_original_rainbow_D6_cycle_transfer(
                m,roots=(0,1,2),max_rainbow_sixcycles=1)
            Q,cycle=next(iter(
                sample["exact_true_original_six_ID_D6_Q_to_unique_cycle"].items()))
            wedge=(cycle[0],)+tuple(sorted((cycle[1],cycle[-1])))
            ctx=original_opposite_wedge_context(m)
            cert=exact_original_wedge_forest_Hall_audit(
                m,wedge,context=ctx,require_good=False)
            historic=exact_original_opposite_threeflag_six_Q_funnel(
                m,wedge,context=ctx)
            self.assertEqual(
                cert["unique_genuine_original_six_ID_Q_count"],
                historic["genuine_original_both_leafless_three_additional_flag_Hall_Q_count"])
            self.assertIn(Q,cert["original_Hall_Q_to_physical_template_kind"])
            self.assertEqual(cert["source_point_threeflag_shape"],"P")
            self.assertEqual(cert["source_line_threeflag_shape"],"P")
            self.assertIn(Q,historic["selected_true_original_six_incidence_ID_Q_tags"])
            self.assertEqual(historic["selected_true_original_six_incidence_ID_Q_tags"][Q],"D6")
            print("AA4AT_GENUINE_W34_PARTIAL",name,
                  "wedge",wedge,"actual_original_D6_Q",Q,
                  "unique_forest_true_source_Hall",cert[
                      "unique_genuine_original_six_ID_Q_count"],
                  "original_physically_occupied_residual_pairs",cert[
                      "globally_occupied_two_typed_residual_template_pairs"])

    def test_06_true_original_symplectic_invariance_and_forged_source_rejection(self):
        from hyp105_issue230_d6aa4at_original_forest_unique_hall import (
            _genuine_source_forest_degree_problem)
        m=zero_split_original_W32()
        p,l=symplectic_transvection_source(m,1)
        t=transform_model(m,point_sources=p,line_sources=l,
                          point_coordinates=tuple(reversed(range(6))),
                          line_coordinates=tuple((i+2)%6 for i in range(6)))
        counts=[]
        for model in (m,t):
            ctx=original_opposite_wedge_context(model)
            a=Counter()
            for wedge in literal_source_good_opposite_wedges(ctx):
                result=exact_original_wedge_forest_Hall_audit(
                    model,wedge,context=ctx)
                a[(result["source_point_threeflag_shape"],
                   result["source_line_threeflag_shape"])]+=result[
                       "unique_genuine_original_six_ID_Q_count"]
            counts.append(a)
        self.assertEqual(counts[0],counts[1])
        for corrupted in (dict(m,left_labels=((0,1),)*15),
                          dict(m,right_labels=((0,1),)*15),
                          dict(m,incidences=m["incidences"][:-1])):
            with self.assertRaises((ValueError,AssertionError)):
                original_opposite_wedge_context(corrupted)


if __name__=="__main__":
    unittest.main()
