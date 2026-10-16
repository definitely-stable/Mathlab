"""AA4-AN independent true-original D-pair physical/Hall/7-GF5 port funnel."""
import unittest
from collections import Counter
from itertools import combinations,combinations_with_replacement

from hyp105_issue230_d6aa4an_port_completion_hall_funnel import (
    _pattern_edges,all_h_port_completion_count,
    true_original_D_physical_ports,physical_D_pair_half_patterns,
    exact_original_D_pair_six_Q_funnel,original_Q_D_anchor_residual_kind)
from hyp105_issue230_d6aa4am_genuine_pair_sixcharge import (
    original_D_pair_index,six_Q_anchored_D_pairs,
    exact_W32_original_seven_pair_extension_certificate)
from hyp105_issue230_d6aa4al_global_original_coordinate_transport import (
    _actual_strict_original_transport)
from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import (
    zero_split_original_W32)
from hyp105_g5e2b3e1b0_seven_signature import seven_census
from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ab_minimax_orbit_normalform import (
    symplectic_transvection_source,transform_model)


def independently_enumerate_port_degree_profiles(a):
    """Independent brute multigraphs, no P5/triangle/double template code."""
    ports=(0,1,2)
    assert a>=6
    allowed=[v for v in range(a) if v!=0]
    edges=tuple(combinations(allowed,2))
    result=set()
    for four in combinations_with_replacement(edges,4):
        degrees=Counter(v for e in four for v in e)
        if degrees[1]!=1 or degrees[2]!=1 or len(degrees)!=5:
            continue
        if any(degrees[v]!=2 for v in degrees if v not in (1,2)):
            continue
        if 0 in degrees:continue
        result.add(tuple(four))
    return result


class OriginalPortCompletionHall(unittest.TestCase):
    def test_01_all_h_exact_three_physical_topology_numbers(self):
        for h in (1,2,3,4,8,19,25,50):
            s=1<<h
            z=all_h_port_completion_count(s)
            n=z["physical_new_coordinate_triples"]
            self.assertEqual(z["physical_P5_paths"],6*n)
            self.assertEqual(z["physical_K2_plus_C3"],n)
            self.assertEqual(z["physical_P3_plus_parallel_K2"],3*n)
            self.assertEqual(z["physical_all_one_typed_residual_completions"],10*n)
            self.assertEqual(z["physical_all_two_typed_candidate_pairs_before_original_Hall"],100*n*n)
            self.assertTrue(z["physical_pattern_capacity_is_NOT_an_original_six_Q_lower"])
        for bad in (0,3,True,-2):
            with self.assertRaises(ValueError):
                all_h_port_completion_count(bad)

    def test_02_independent_bruteforce_all_K6_K7_K8_port_multigraphs(self):
        for a in (6,7,8):
            brute=independently_enumerate_port_degree_profiles(a)
            constructive=set()
            tag_count=Counter()
            for new in combinations(tuple(range(3,a)),3):
                for tag,edges in _pattern_edges((0,1,2),new):
                    self.assertNotIn(edges,constructive)
                    constructive.add(edges);tag_count[tag]+=1
            self.assertEqual(brute,constructive)
            n=a-3
            self.assertEqual(len(brute),10*(n*(n-1)*(n-2)//6))
            self.assertEqual(tag_count["P5"],6*(n*(n-1)*(n-2)//6))
            self.assertEqual(tag_count["K2+C3"],n*(n-1)*(n-2)//6)
            self.assertEqual(tag_count["P3+2K2"],3*n*(n-1)*(n-2)//6)

    def test_03_complete_original_W32_5_global_maps_D_first_exact_Q_extensions(self):
        maps=[("dual_zero",zero_split_original_W32())]+[
            (scheme,fixture(1,scheme)) for scheme in ("lex","reverse","S68","S72")]
        for name,m in maps:
            D=original_D_pair_index(m)
            historical=seven_census(m,independent_checks=False,witness_sets=True)["sets"]
            expected=exact_W32_original_seven_pair_extension_certificate(m)
            E=0;C=0
            source_matched=0;aa_rejected=0
            zero_hall_pairs=0;zero_selected_pairs=0
            hist=Counter();selected_types=Counter()
            for pair in sorted(D):
                result=exact_original_D_pair_six_Q_funnel(m,pair)
                self.assertEqual(result["point_side_occupied_physical_pattern_count"],10)
                self.assertEqual(result["line_side_occupied_physical_pattern_count"],10)
                self.assertEqual(result["physical_double_completion_candidate_pairs"],100)
                expected_Q={Q:tag for Q,tag in historical.items() if set(pair).issubset(Q)}
                self.assertEqual(result["selected_ORIGINAL_six_incidence_ID_Q_tags"],
                                 expected_Q)
                n=len(expected_Q)
                E+=n
                C+=bool(n)
                source_matched+=result[
                    "actual_original_six_Q_both_leafless_physical_projections"]
                aa_rejected+=result["actual_original_six_Q_unaligned_AA_rejected"]
                zero_hall_pairs+=int(result[
                    "actual_original_six_Q_both_leafless_physical_projections"]==0)
                zero_selected_pairs+=int(n==0)
                hist[n]+=1
                selected_types.update(result["actual_original_positive_seven_GF5_by_tag"])
            self.assertEqual(E,expected["E_original_extension_incidences"])
            self.assertEqual(C,expected["D_covered_by_at_least_one_selected_original_six_Q"])
            self.assertEqual(zero_selected_pairs,
                 expected["D_UNCOVERED_by_ALL_SEVEN_selected_six_Q"])
            self.assertEqual(E,sum(selected_types.values()))
            self.assertEqual(sum(hist.values()),len(D))
            self.assertGreater(zero_selected_pairs,0)
            print("AA4AN_W32",name,"D",len(D),"E",E,"covered",C,
                  "uncovered",zero_selected_pairs,"zero_original_Hall",zero_hall_pairs,
                  "source_both_projection_Q_charge",source_matched,
                  "unaligned_AA_Q_charge",aa_rejected,
                  "original_seven_tags_by_D_charge",dict(selected_types),
                  "D_extension_hist",dict(sorted(hist.items())))

    def test_04_physical_occupied_partial_W34_source_ports_and_local_Q_membership(self):
        from test_hyp105_issue230_d6aa4am_genuine_pair_sixcharge import (
            independent_true_original_W34_selected_local_BA)
        from hyp105_issue230_d6aa4af_rootpair_robust_quench import (
            occupied_root_C4_source_factors)
        touched=set()
        for scheme in ("lex","random"):
            m=fixture(2,scheme)
            s,V,d,a,left,right,inc,np,nl=_actual_strict_original_transport(m)
            self.assertEqual((s,V,a),(4,85,14))
            D=original_D_pair_index(m)
            checked=0
            for side in (0,1):
                for root,off in ((0,0),(1,1),(5,2)):
                    for four in occupied_root_C4_source_factors(
                            m,side=side,root=root)[:2]:
                        genuine=independent_true_original_W34_selected_local_BA(
                            m,side,root,off,four)
                        for Q in genuine:
                            kset=six_Q_anchored_D_pairs(Q,inc,left,right)
                            for pair in kset:
                                self.assertIn(pair,D)
                                for typed in (0,1):
                                    tag=original_Q_D_anchor_residual_kind(
                                        m,pair,Q,side=typed)
                                    self.assertIn(tag,("P5","K2+C3","P3+2K2"))
                                    key=(scheme,tag)
                                    touched.add(key)
                                checked+=1
            # Half-occupied pattern lists under non-surjective K14
            for pair in tuple(sorted(D))[:2]:
                sides=[physical_D_pair_half_patterns(m,pair,side=j) for j in (0,1)]
                self.assertTrue(all(x["physical_formal_total"]==1650 for x in sides))
                self.assertTrue(all(0<=x["physical_occupied_total"]<=1650
                                    for x in sides))
                self.assertTrue(all(x["physical_global_injection_missing_reject"]>=0
                                    for x in sides))
            print("AA4AN_W34",scheme,"actual_Q_D_anchor_pairs_checked",checked)
        self.assertTrue(touched)

    def test_05_genuine_original_source_symplectic_and_typed_physical_invariance(self):
        m=zero_split_original_W32()
        p,l=symplectic_transvection_source(m,1)
        relabeled=transform_model(
            m,point_sources=p,line_sources=l,
            point_coordinates=tuple(reversed(range(6))),
            line_coordinates=tuple((i+2)%6 for i in range(6)))
        for model in (m,relabeled):
            D=original_D_pair_index(model)
            selected=seven_census(model,independent_checks=False,witness_sets=True)["sets"]
            e=0;covered=0
            for pair in D:
                z=exact_original_D_pair_six_Q_funnel(model,pair,retain_selected=False)
                e+=z["actual_original_positive_seven_GF5_six_Q_extensions"]
                covered+=bool(z["actual_original_positive_seven_GF5_six_Q_extensions"])
            self.assertEqual(e,164)
            self.assertEqual(covered,115)
            self.assertEqual(len(D),277)

    def test_06_strict_true_original_incidence_and_wrong_support_falsifiers(self):
        m=zero_split_original_W32()
        s,V,d,a,left,right,inc,np,nl=_actual_strict_original_transport(m)
        good=sorted(original_D_pair_index(m))[0]
        with self.assertRaises(ValueError):
            true_original_D_physical_ports(inc,left,right,(-1,1))
        with self.assertRaises(ValueError):
            true_original_D_physical_ports(inc,left,right,(good[1],good[0]))
        with self.assertRaises(ValueError):
            true_original_D_physical_ports(inc,left,right,(0,0))
        with self.assertRaises(ValueError):
            physical_D_pair_half_patterns(m,good,side=2)
        with self.assertRaises(ValueError):
            exact_original_D_pair_six_Q_funnel(
                dict(m,left_labels=((0,1),)*15),good)
        with self.assertRaises(ValueError):
            original_Q_D_anchor_residual_kind(m,good,(0,1,2),side=0)


if __name__=="__main__":
    unittest.main()
