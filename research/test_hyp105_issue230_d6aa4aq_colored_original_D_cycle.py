"""AA4-AQ: genuine original two-typed rainbow six-cycle D6 certificates."""
import unittest
from fractions import Fraction

from hyp105_issue230_d6aa4aq_colored_original_D_cycle import (
    original_bicolored_D_flag_graph,
    original_D_arc_transition_spectral_audit,
    exact_original_rainbow_D6_cycle_transfer,
    all_h_abstract_plain_C6_edgecount_nogo,
    _plain_any_six_cycle)
from hyp105_issue230_d6aa4am_genuine_pair_sixcharge import (
    original_D_pair_index, six_Q_anchored_D_pairs)
from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import (
    zero_split_original_W32)
from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1b0_seven_signature import seven_census
from hyp105_issue230_d6aa4q_two_sided_seven_join import (
    _column_physical_dual,_is_single_6cycle_on_incidence_positions,
    independent_joint_classify)
from hyp105_issue230_d6aa4ab_minimax_orbit_normalform import (
    symplectic_transvection_source, transform_model)


class TrueOriginalColoredD6(unittest.TestCase):
    def test_01_full_original_W32_all_five_global_maps_independent_D6_sixQ(self):
        known={"dual_zero":(277,1),"lex":(307,15),"reverse":(300,3),
               "S68":(257,0),"S72":(261,0)}
        for name,m in [("dual_zero",zero_split_original_W32())]+[
                (name,fixture(1,name)) for name in ("lex","reverse","S68","S72")]:
            graph=original_bicolored_D_flag_graph(m)
            cert=exact_original_rainbow_D6_cycle_transfer(m)
            historical=seven_census(m,independent_checks=False,witness_sets=True)
            historic_D6={Q for Q,tag in historical["sets"].items() if tag=="D6"}
            graph_D=len(graph["D_edges"])
            self.assertEqual((graph_D,len(historic_D6)),known[name])
            self.assertEqual(set(cert["exact_true_original_six_ID_D6_Q_to_unique_cycle"]),
                             historic_D6)
            self.assertEqual(cert["double_rainbow_D6_original_Q_count"],
                             known[name][1])
            self.assertTrue(cert["global_root_scan_complete"])
            self.assertFalse(cert["scan_truncated_by_explicit_witness_budget"])
            self.assertEqual(graph_D,len(original_D_pair_index(m)))
            for Q,cyc in cert["exact_true_original_six_ID_D6_Q_to_unique_cycle"].items():
                self.assertEqual(set(Q),set(cyc))
                self.assertEqual(cyc[0],min(Q))
                self.assertLess(cyc[1],cyc[-1])
                self.assertEqual(len(six_Q_anchored_D_pairs(
                    Q,tuple(m["incidences"]),m["left_labels"],m["right_labels"])),6)
                self.assertEqual(independent_joint_classify(
                    Q,"A","A",tuple(m["incidences"]),
                    m["left_labels"],m["right_labels"]),"D6")
                # Independent previously accepted AA4-Q positional oracle,
                # without consulting the new D-cycle color algorithm.
                dualP=_column_physical_dual(
                    Q,tuple(m["incidences"]),m["left_labels"],0)
                dualL=_column_physical_dual(
                    Q,tuple(m["incidences"]),m["right_labels"],1)
                self.assertEqual(dualP,dualL)
                self.assertTrue(_is_single_6cycle_on_incidence_positions(dualP))
            print("AA4AQ_ORIGINAL_W32",name,"D_pairs",graph_D,
                  "selected_exact_D6",len(historic_D6),
                  "rainbow_paths_examined",cert["examined_D_flag_path_extensions"])

    def test_02_real_original_W32_S68_S72_ordinary_sixcycle_without_D6(self):
        # This falsifies the proposed weaker step:
        # "one ordinary C6 in the true D compatibility graph forces
        # one selected original positive D6". Missing TWO-COLOR rainbow
        # vertex/edge constraints are essential.
        for scheme in ("S68","S72"):
            m=fixture(1,scheme)
            graph=original_bicolored_D_flag_graph(m)
            ordinary=_plain_any_six_cycle(graph)
            self.assertIsNotNone(ordinary)
            self.assertEqual(len(ordinary),6)
            self.assertEqual(len(set(ordinary)),6)
            for i in range(6):
                e=tuple(sorted((ordinary[i],ordinary[(i+1)%6])))
                self.assertIn(e,graph["D_edges"])
            cert=exact_original_rainbow_D6_cycle_transfer(m)
            self.assertEqual(cert["double_rainbow_D6_original_Q_count"],0)
            print("AA4AQ_TRUE_W32_ORDINARY_NONRAINBOW",scheme,
                  "ordinary_flag_cycle",ordinary,
                  "D_edge_count",len(graph["D_edges"]))

    def test_03_genuine_original_W32_W34_two_typed_source_cell_spectral_transition(self):
        for name,m in (("dual_zero",zero_split_original_W32()),
                       ("S68",fixture(1,"S68")),
                       ("W34_lex",fixture(2,"lex")),
                       ("W34_random",fixture(2,"random"))):
            z=original_D_arc_transition_spectral_audit(m)
            self.assertEqual(z["directed_original_D_arc_count"],
                             2*len(original_D_pair_index(m)))
            self.assertEqual(sum(z[
                "forward_original_typed_legal_port_count_histogram"].values()),
                z["directed_original_D_arc_count"])
            self.assertLessEqual(z[
                "maximum_valid_original_two_typed_one_step"],
                z["classical_original_source_incidence_cell_upper"])
            self.assertTrue(z["AA4_AP_good_D_lower_not_promoted_to_D6"])
            print("AA4AQ_SOURCE_TYPED_PORT_TRANSITIONS",name,
                  "maximum_forward_step",z[
                      "maximum_valid_original_two_typed_one_step"],
                  "source_spectral_K",str(z[
                      "classical_original_source_incidence_cell_upper"]))

    def test_04_true_original_W34_partial_rooted_rainbow_certificate(self):
        # Explicitly PARTIAL root slice. Every returned candidate
        # independently classified as REAL source D6; no full W34
        # D6 census or source-Hall lower is claimed.
        for name in ("lex","random"):
            m=fixture(2,name)
            z=exact_original_rainbow_D6_cycle_transfer(
                m,roots=(0,1,2),max_rainbow_sixcycles=3)
            self.assertEqual(z["s"],4)
            self.assertFalse(z["global_root_scan_complete"])
            self.assertLessEqual(z["double_rainbow_D6_original_Q_count"],3)
            for Q,cyc in z["exact_true_original_six_ID_D6_Q_to_unique_cycle"].items():
                self.assertEqual(len(Q),6)
                self.assertEqual(set(Q),set(cyc))
                self.assertEqual(independent_joint_classify(
                    Q,"A","A",tuple(m["incidences"]),
                    m["left_labels"],m["right_labels"]),"D6")
            print("AA4AQ_PARTIAL_REAL_ORIGINAL_W34",name,
                  "rainbow_D6_sampled",z["double_rainbow_D6_original_Q_count"],
                  "partial",not z["global_root_scan_complete"])

    def test_05_original_source_symplectic_and_two_typed_physical_relabels(self):
        m=zero_split_original_W32()
        p,l=symplectic_transvection_source(m,1)
        transformed=transform_model(
            m,point_sources=p,line_sources=l,
            point_coordinates=tuple(reversed(range(6))),
            line_coordinates=tuple((i+2)%6 for i in range(6)))
        r0=exact_original_rainbow_D6_cycle_transfer(m)
        r1=exact_original_rainbow_D6_cycle_transfer(transformed)
        self.assertEqual(r0["double_rainbow_D6_original_Q_count"],1)
        self.assertEqual(r1["double_rainbow_D6_original_Q_count"],1)
        for name in ("D_original_undirected_pair_count",
                     "original_source_flag_vertices",
                     "double_rainbow_D6_original_Q_count"):
            self.assertEqual(r0[name],r1[name])

    def test_06_abstract_girth_eight_edgecount_no_go_for_h48_to_80(self):
        for h in (48,49,50,51,60,64,75,80):
            s=1<<h
            z=all_h_abstract_plain_C6_edgecount_nogo(s)
            self.assertGreaterEqual(
                z["abstract_C6_free_incidence_graph_edges"],s**5)
            self.assertLessEqual(
                z["abstract_generalized_quadrangle_incidence_graph_vertices"],
                z["original_source_flag_vertex_budget"])
            self.assertFalse(z["has_any_ordinary_C6"])
            self.assertTrue(z["NOT_an_actual_original_D_f_g_compatibility_graph"])
            self.assertTrue(z["no_all_map_D6_counterexample_proved"])
        for wrong in (0,3,-4,True,2**47):
            with self.assertRaises(ValueError):
                all_h_abstract_plain_C6_edgecount_nogo(wrong)

    def test_07_invalid_original_inputs_full_domain_and_partial_scope(self):
        m=zero_split_original_W32()
        for bad in (dict(m,left_labels=((0,1),)*15),
                    dict(m,right_labels=((0,1),)*15),
                    dict(m,incidences=m["incidences"][:-1])):
            with self.assertRaises((ValueError,AssertionError)):
                original_bicolored_D_flag_graph(bad)
        with self.assertRaises(ValueError):
            exact_original_rainbow_D6_cycle_transfer(m,roots=(-1,))
        with self.assertRaises(ValueError):
            exact_original_rainbow_D6_cycle_transfer(m,roots=(0,0))
        with self.assertRaises(ValueError):
            exact_original_rainbow_D6_cycle_transfer(m,max_rainbow_sixcycles=0)
        with self.assertRaises(ValueError):
            exact_original_rainbow_D6_cycle_transfer(fixture(2,"lex"))


if __name__=="__main__":
    unittest.main()
