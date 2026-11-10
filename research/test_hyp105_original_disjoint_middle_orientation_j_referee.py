"""HYP-105 AA4-DMID: independent all-h orientation theorem / true original J risk."""
from fractions import Fraction
from itertools import combinations
from collections import Counter
import unittest

from hyp105_original_disjoint_middle_orientation_j_referee import (
    SCHEMA,STATUS,CAUSES,OVERLAPS,FULL_CASES,MIDDLE_CHANNEL,
    _all_orientation_compatibility_matrix,
    _minimal_three_by_three_typed_compatible,
    _all_full_original_source_compatibility_matrix,
    _min_three_by_three_full_original_compatible,
    _physical_endpoint_J_collision,
    _physical_only_disjoint_middle_compatibility,
    _independent_true_middle_orientation_pair,
    _full_exact_case,
    canonical_report
)
from hyp105_original_full_w34_weighted_risk_referee import (
    _source,_true_original_proper_P3,_pair_bad
)


class TestOriginalDisjointMiddleOrientationAndJ(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result=canonical_report()
        cls.rows=cls.result["complete_true_original_source_W32_W34_exact_disjoint_middle_census"]

    def test_all_h_scientific_stop_and_source_contract(self):
        r=self.result
        self.assertEqual(r["schema"],SCHEMA)
        self.assertEqual(r["status"],STATUS)
        self.assertEqual(r["issue"],230)
        self.assertFalse(r["root_PROVED_A"])
        self.assertFalse(r["all_h_GLOBAL_B_over_M_below_three_quarters_proved"])
        self.assertFalse(r["infinite_correlated_counterfamily_claimed"])
        self.assertFalse(r["ASET_exponent_claimed"])
        self.assertFalse(r["numeric_external_graph_C6_constants_claimed"])
        for key in ("all_h_original_disjoint_middle_direct_source_J_edge_impossible",
                    "all_h_original_zero_both_overlap_typed_obstruction_impossible",
                    "all_h_four_by_four_source_oriented_diagonal_compatibility_exact",
                    "all_h_sharp_three_by_three_typed_compatibility_counts",
                    "all_h_disjoint_middle_J_midouter_outerouter_and_nonJ_typed_exact_partition"):
            self.assertTrue(r[key])

    def test_exact_all_h_four_oriented_middle_by_four_census(self):
        expected={"00":16,"10":8,"01":8,"11":4}
        for overlap,target in expected.items():
            A=_all_orientation_compatibility_matrix(int(overlap[0]),int(overlap[1]))
            self.assertEqual(len(A),4)
            self.assertTrue(all(len(row)==4 for row in A))
            self.assertEqual(sum(map(sum,A)),target)
            self.assertEqual(self.result["orientation_compatibility_certificates"][overlap]["full_four_by_four_typed_compatible_count"],target)

    def test_all_h_exact_sharp_three_by_three_orientation_minima(self):
        expected={"00":9,"10":4,"01":4,"11":2}
        for overlap,target in expected.items():
            x=int(overlap[0]);y=int(overlap[1])
            self.assertEqual(_minimal_three_by_three_typed_compatible(x,y),target)
            self.assertEqual(self.result["orientation_compatibility_certificates"][overlap]["worst_case_actual_three_by_three_orientation_subsets_typed_compatible_min"],target)

    def test_NEW_all_h_full_J_and_typed_original_4x4_16_0_0_2(self):
        expected={"00":16,"10":0,"01":0,"11":2}
        for overlap,n in expected.items():
            ox=int(overlap[0]);oy=int(overlap[1])
            matrix=_all_full_original_source_compatibility_matrix(ox,oy)
            self.assertEqual(len(matrix),4)
            self.assertTrue(all(len(r)==4 for r in matrix))
            self.assertEqual(sum(map(sum,matrix)),n)
            self.assertEqual(self.result["orientation_compatibility_certificates"][overlap][
                "full_four_by_four_original_J_plus_typed_compatible_count"],n)
        self.assertTrue(self.result[
            "all_h_FULL_original_J_plus_typed_4x4_compatibility_counts_16_0_0_2"])

    def test_NEW_sharp_full_original_3x3_minimum_9_0_0_0(self):
        expected={"00":9,"10":0,"01":0,"11":0}
        for o,val in expected.items():
            x,y=map(int,o)
            self.assertEqual(_min_three_by_three_full_original_compatible(x,y),val)
            self.assertEqual(self.result["orientation_compatibility_certificates"][o][
                "minimum_three_by_three_full_original_J_plus_typed_compatible_count"],val)

    def test_new_all_h_outer_source_J_endpoint_vertex_test_independent(self):
        self.assertTrue(self.result[
            "all_h_proper_same_end_original_J_only_first_first_or_last_last"])
        for s,sch,core in FULL_CASES[:3]:
            c=_source(s,sch,core)
            byend={}
            for p,os in _true_original_proper_P3(c):
                byend.setdefault((p[0],p[-1]),[]).append((p,os))
            for group in byend.values():
                for (p,os),(q,ot) in combinations(group,2):
                    f1=c["flags"][os[1]];f2=c["flags"][ot[1]]
                    if f1[0]==f2[0] or f1[1]==f2[1]:continue
                    j1,j2=_physical_endpoint_J_collision(p,q)
                    expected_J=any(ot[y] in c["J"][os[x]]
                                   for x in range(3) for y in range(3))
                    self.assertEqual(j1 or j2,expected_J)
                    for x,y in ((0,2),(2,0),(1,0),(1,2),(0,1),(2,1)):
                        self.assertNotIn(ot[y],c["J"][os[x]])

    def test_new_full_original_compatibility_physical_only_every_W32_source_pair(self):
        for sch,core in (("lex","full"),("reverse","full"),("shift","Z17")):
            c=_source(2,sch,core)
            byend={}
            for p,os in _true_original_proper_P3(c):
                byend.setdefault((p[0],p[-1]),[]).append((p,os))
            for group in byend.values():
                for (p,os),(q,ot) in combinations(group,2):
                    f1=c["flags"][os[1]];f2=c["flags"][ot[1]]
                    if f1[0]==f2[0] or f1[1]==f2[1]:continue
                    ox=len(set(c["f"][f1[0]]) & set(c["f"][f2[0]]))
                    oy=len(set(c["g"][f1[1]]) & set(c["g"][f2[1]]))
                    phys=_physical_only_disjoint_middle_compatibility(p,q,ox,oy)
                    self.assertEqual(phys,_pair_bad(p,os,q,ot,c["J"])=="compatible")
        self.assertTrue(self.result[
            "all_h_disjoint_middle_full_compatibility_physical_only_vertex_test"])

    def test_reject_non_boolean_overlap(self):
        for x,y in ((2,0),(0,2),(-1,0),(1,3)):
            with self.assertRaises(ValueError):
                _all_orientation_compatibility_matrix(x,y)

    def test_no_middle_middle_source_J_on_disjoint_original_flags_all_8_cases(self):
        for s,sch,core in FULL_CASES:
            c=_source(s,sch,core)
            for i in c["ids"]:
                p,l=c["flags"][i]
                for j in c["J"][i]:
                    q,m=c["flags"][j]
                    self.assertTrue(p==q or l==m)

    def test_all_eight_original_source_complete_full_paths(self):
        self.assertEqual(len(self.rows),8)
        self.assertEqual([(x["original_s"],x["original_fixed_scheme"],x["original_CORE"])
                          for x in self.rows],list(FULL_CASES))
        self.assertEqual([r["true_proper_directed_physical_P3_count"] for r in self.rows],
                         [1346,1154,838,83892,82846,79404,9966,66418])
        for r in self.rows:
            self.assertTrue(r["full_source_complete_census"])
            self.assertEqual(r["real_paired_physical_edges"],2*r["retained_original_flags"])
            self.assertGreater(r["original_source_priority_triples_exact"],0)
            self.assertGreater(r["true_original_ordered_physical_endpoint_bins"],0)

    def test_four_source_J_middle_outer_and_outer_outer_typed_partition_each_case(self):
        for r in self.rows:
            ledger=r["disjoint_middle_true_J_vs_typed_bad_mass_exact"]
            count=r["disjoint_middle_true_J_vs_typed_bad_pair_counts"]
            self.assertEqual(tuple(ledger),CAUSES)
            self.assertEqual(tuple(count),CAUSES)
            self.assertEqual(
               sum((Fraction(ledger[name]) for name in CAUSES),Fraction(0)),
               Fraction(r["disjoint_middle_actual_incompatible_weight"]))
            self.assertEqual(
               sum((count[name] for name in CAUSES)),sum(
                  v for k,v in r["disjoint_middle_complete_four_overlap_by_cause_integer_counts"].items()
                  if not k.endswith("/compatible")))
            self.assertTrue(all(Fraction(ledger[name])>=0 and count[name]>=0
                                for name in CAUSES))

    def test_complete_joint_signature_compatibility_and_bad_pair_conservation(self):
        for r in self.rows:
            c=r["disjoint_middle_complete_four_overlap_by_cause_integer_counts"]
            w=r["disjoint_middle_complete_four_overlap_by_cause_exact_mass"]
            self.assertEqual(set(c),set(w))
            self.assertEqual(sum(c.values()),r["disjoint_middle_both_point_line_actual_ordered_path_pairs"])
            self.assertEqual(sum((Fraction(v) for v in w.values()),Fraction(0)),
                 Fraction(r["disjoint_middle_actual_incompatible_weight"])+
                 Fraction(r["disjoint_middle_actual_compatible_weight"]))
            self.assertEqual(sum(v for k,v in c.items() if k.endswith("/compatible")),
                 sum(v for k,v in c.items())-sum(r["disjoint_middle_true_J_vs_typed_bad_pair_counts"].values()))

    def test_no_typed_only_incompatibility_when_both_true_middle_pairs_disjoint(self):
        for r in self.rows:
            for name in CAUSES[2:]:
                self.assertEqual(r["disjoint_middle_complete_four_overlap_by_cause_integer_counts"].get("00/"+name,0),0)
                self.assertEqual(Fraction(r["disjoint_middle_complete_four_overlap_by_cause_exact_mass"].get("00/"+name,"0")),0)
            self.assertEqual(Fraction(r["disjoint_middle_actual_incompatible_weight"]),
                 sum((Fraction(x) for x in r["disjoint_middle_actual_bad_overlap_signature_mass"].values()),
                     Fraction(0)))

    def test_expected_original_W32_W34_full_source_baselines_source_masks(self):
        for r in self.rows:
            self.assertEqual(sum(r["disjoint_middle_true_J_vs_typed_bad_pair_counts"].values())+
                             sum(v for k,v in r["disjoint_middle_complete_four_overlap_by_cause_integer_counts"].items()
                                 if k.endswith("/compatible")),
                             r["disjoint_middle_both_point_line_actual_ordered_path_pairs"])
            self.assertGreater(r["disjoint_middle_both_point_line_actual_ordered_path_pairs"],0)

    def test_actual_original_zero_pair_label_overlap_source_J_only_witness(self):
        for r in self.rows:
            a=r["first_true_original_zero_both_label_overlap_J_only_bad_witness"]
            self.assertIsNone(a)
            self.assertEqual(Fraction(r["disjoint_middle_actual_bad_overlap_signature_mass"]["00"]),0)
        self.assertTrue(self.result[
            "all_h_disjoint_middle_BAD_requires_at_least_one_middle_label_overlap"])

    def test_full_original_source_physical_only_Fraction_ledger_equals_J_graph(self):
        for r in self.rows:
            self.assertEqual(
                Fraction(r["independent_physical_only_full_compatibility_source_weight"]),
                Fraction(r["disjoint_middle_actual_compatible_weight"]))
            self.assertEqual(
                Fraction(r["independent_physical_only_full_incompatibility_source_weight"]),
                Fraction(r["disjoint_middle_actual_incompatible_weight"]))
            self.assertEqual(Fraction(r["disjoint_middle_true_J_vs_typed_bad_mass_exact"][
                "source_J_middle_to_outer"]),0)
            self.assertEqual(r["disjoint_middle_true_J_vs_typed_bad_pair_counts"][
                "source_J_middle_to_outer"],0)
            for sig in ("10","01"):
                self.assertEqual(r[
                    "disjoint_middle_complete_four_overlap_by_cause_integer_counts"].get(
                    sig+"/compatible",0),0)

    def test_true_single_overlap_same_depth_outer_J_actual_witness(self):
        observed=0
        for r in self.rows:
            w=r["first_true_original_single_label_overlap_same_depth_J_witness"]
            if w is None:continue
            observed+=1
            c=_source(r["original_s"],r["original_fixed_scheme"],r["original_CORE"])
            p=tuple(map(tuple,w["path_a"]))
            q=tuple(map(tuple,w["path_b"]))
            os=w["original_flag_owners_a"];ot=w["original_flag_owners_b"]
            self.assertEqual((p[0],p[-1]),(q[0],q[-1]))
            ox,oy,cause,xbad,ybad,jmo,joo=(
                _independent_true_middle_orientation_pair(p,os,q,ot,c))
            self.assertNotEqual(ox,oy)
            self.assertTrue(joo)
            self.assertFalse(jmo)
            self.assertFalse(xbad or ybad)
            self.assertEqual(cause,"source_J_outer_to_outer_only")
            self.assertTrue(any(_physical_endpoint_J_collision(p,q)))
        self.assertGreater(observed,0)

    def test_new_all_h_source_middle_group_kernel_00_and_shared_corner_11(self):
        self.assertTrue(self.result[
            "all_h_exact_compressed_original_middle_source_label_and_shared_corner_good_kernel"])
        self.assertTrue(self.result[
            "all_h_full_G_lower_by_source_physical_diagonal_plus_disjoint_mid_good"])
        for r in self.rows:
            g00=Fraction(r["exact_compressed_original_middle_source_good_00_weight"])
            g11=Fraction(r["exact_compressed_original_middle_source_good_11_sharedcorner_weight"])
            g=Fraction(r["exact_compressed_original_middle_source_good_total"])
            b=Fraction(r["exact_compressed_original_middle_source_bad_total"])
            m=Fraction(r["exact_compressed_original_middle_source_pair_total"])
            self.assertEqual(g00+g11,g)
            self.assertEqual(b+g,m)
            self.assertGreaterEqual(g00,0)
            self.assertGreaterEqual(g11,0)
            self.assertEqual(g,Fraction(r["disjoint_middle_actual_compatible_weight"]))
            self.assertEqual(b,Fraction(r["disjoint_middle_actual_incompatible_weight"]))
            self.assertEqual(g00,Fraction(r[
                "disjoint_middle_complete_four_overlap_by_cause_exact_mass"].get("00/compatible","0")))
            self.assertEqual(g11,Fraction(r[
                "disjoint_middle_complete_four_overlap_by_cause_exact_mass"].get("11/compatible","0")))
            self.assertGreater(r["compressed_original_source_middle_flag_pairs_examined"],0)

    def test_all_h_positive_good_diagonal_plus_compressed_mid_mass(self):
        for r in self.rows:
            D=Fraction(r["exact_physical_path_diagonal_from_compressed_mid_source"])
            good=Fraction(r["exact_compressed_original_middle_source_good_total"])
            cert=Fraction(r["exact_full_source_G_lower_by_diagonal_plus_disjoint_middle_good"])
            self.assertGreater(D,0)
            self.assertGreaterEqual(good,0)
            self.assertEqual(cert,D+good)
            self.assertGreater(cert,0)

    def test_disjoint_source_middle_group_exact_kernel_vs_ORIGINAL_W32_direct(self):
        # Separate direct W32 path-pair geometry test already constructs source
        # compatibility without J. Compare that exact full good with compressed
        # middle-source weights from one full actual symplectic fixture.
        for r in self.rows[:3]:
            self.assertEqual(
                Fraction(r["exact_compressed_original_middle_source_good_total"]),
                Fraction(r["independent_physical_only_full_compatibility_source_weight"]))
            self.assertEqual(
                Fraction(r["exact_compressed_original_middle_source_bad_total"]),
                Fraction(r["independent_physical_only_full_incompatibility_source_weight"]))

    def test_real_two_overlap_shared_corner_source_compatible_witness(self):
        observed=0
        for r in self.rows:
            w=r["first_true_original_two_overlap_shared_corner_compatible_witness"]
            if w is None:continue
            observed+=1
            c=_source(r["original_s"],r["original_fixed_scheme"],r["original_CORE"])
            p=tuple(map(tuple,w["path_a"]))
            q=tuple(map(tuple,w["path_b"]))
            os=w["original_flag_owners_a"];ot=w["original_flag_owners_b"]
            self.assertTrue(p[1]==q[1] or p[2]==q[2])
            self.assertEqual(_pair_bad(p,os,q,ot,c["J"]),"compatible")
            self.assertEqual(
                _independent_true_middle_orientation_pair(p,os,q,ot,c)[:3],
                (1,1,"compatible"))
        self.assertGreater(observed,0)

    def test_actual_original_typed_only_middle_overlap_witness(self):
        witnessed=0
        for r in self.rows:
            a=r["first_true_original_typed_only_bad_witness"]
            if a is None:continue
            witnessed+=1
            self.assertIn(a["typed_only_obstruction_cause"],CAUSES[2:])
            self.assertGreater(Fraction(a["exact_original_pair_weight"]),0)
            c=_source(r["original_s"],r["original_fixed_scheme"],r["original_CORE"])
            p=tuple(map(tuple,a["path_a"]))
            q=tuple(map(tuple,a["path_b"]))
            os=a["original_flag_owners_a"]
            ot=a["original_flag_owners_b"]
            x=_independent_true_middle_orientation_pair(p,os,q,ot,c)
            self.assertNotEqual(x[:2],(0,0))
            self.assertEqual(x[2],a["typed_only_obstruction_cause"])
            self.assertIn(_pair_bad(p,os,q,ot,c["J"]),
                          ("first_typed_opposite_depth","second_typed_opposite_depth"))
        self.assertGreater(witnessed,0)

    def test_direct_original_GQ_middle_owner_correlation_per_real_path(self):
        c=_source(2,"lex","full")
        checked=0
        byend={}
        for path,os in _true_original_proper_P3(c):
            byend.setdefault((path[0],path[-1]),[]).append((path,os))
        for group in byend.values():
            for (p,os),(q,ot) in combinations(group,2):
                mi=c["flags"][os[1]];mj=c["flags"][ot[1]]
                if mi[0]!=mj[0] and mi[1]!=mj[1]:
                    x,y,cause,xb,yb,jmo,joo=(
                        _independent_true_middle_orientation_pair(p,os,q,ot,c))
                    self.assertEqual((cause in CAUSES),_pair_bad(p,os,q,ot,c["J"])!="compatible")
                    self.assertFalse(xb and x==0)
                    self.assertFalse(yb and y==0)
                    checked+=1
        self.assertGreater(checked,0)

    def test_genuine_original_source_scarcity_full_W34_obstruction_type_nonzero(self):
        for r in self.rows[3:6]:
            x=r["disjoint_middle_true_J_vs_typed_bad_mass_exact"]
            self.assertGreater(Fraction(x[CAUSES[0]])+Fraction(x[CAUSES[1]]),0)
            self.assertGreater(Fraction(x[CAUSES[2]])+Fraction(x[CAUSES[3]]),0)

    def test_pure_orientation_sharp_three_by_three_proof_witnesses(self):
        # Missing ONE of the four orientations on each side leaves:
        # no overlap 9/9 compatible, exactly one overlap 4 or 5,
        # two overlaps (perfect matching) 2 or 3.
        for o in OVERLAPS:
            A=_all_orientation_compatibility_matrix(int(o[0]),int(o[1]))
            values=[sum(A[i][j] for i in range(4) if i!=a
                          for j in range(4) if j!=b)
                    for a in range(4) for b in range(4)]
            self.assertEqual(min(values),_minimal_three_by_three_typed_compatible(int(o[0]),int(o[1])))
            self.assertEqual(len(values),16)

    def test_source_status_not_promoted_by_finite_disjoint_middle_data(self):
        r=self.result
        self.assertFalse(r["all_h_GLOBAL_B_over_M_below_three_quarters_proved"])
        self.assertFalse(r["infinite_correlated_counterfamily_claimed"])
        self.assertEqual(len(r["complete_true_original_source_W32_W34_exact_disjoint_middle_census"]),8)


if __name__=="__main__":
    unittest.main()
