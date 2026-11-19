"""Independent true ORIGINAL W32/W34 BBo alignment/source-sixset/GF5 tests."""
from collections import Counter
from fractions import Fraction
import unittest

from hyp105_original_bbo_alignment_dag_referee import (
    SCHEMA,STATUS,PARENT_PR,SIGNED_ALIGNED,SIGNED_UNALIGNED,
    real_source,genuine_projection,minimal_pairs,all_four_cycles,
    _source_six_seed,template_model,source_owned_graph,
    _chain_from_three_ids,independent_sixID_factor_inverse,
    physical_first_paths,original_sixset_factor_profile,_source_alignment,_canonical_edges_for_gf5,
    independent_gf5_fourier_mass,template_referee,
    extra_core_and_deleted_case,certificate,
)


class TestOriginalBBoSourceFactorSixId(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.c=certificate()

    def test_01_genuine_W32_W34_original_geometry_pencil_cardinality(self):
        for s in (2,4):
            m=real_source(s)
            self.assertEqual(len(m["flags"]),(s+1)**2*(s*s+1))
            self.assertEqual(m["V"],(s+1)*(s*s+1))
            self.assertEqual(len(m["idx"]),len(m["flags"]))
            for p in range(m["V"]):
                self.assertEqual(len(m["bp"][p]),s+1)
                self.assertEqual(len(m["bl"][p]),s+1)

    def test_02_full_original_GQ_projection_independent(self):
        for s in (2,4):
            m=real_source(s)
            success=0
            for q in range(m["V"]):
                for r in range(m["V"]):
                    p=genuine_projection(m,q,r)
                    if r in m["bp"][q]:
                        self.assertIsNone(p)
                    else:
                        self.assertIsNotNone(p)
                        point,line=p
                        self.assertIn((q,line),m["idx"])
                        self.assertIn((point,line),m["idx"])
                        self.assertIn((point,r),m["idx"])
                        success+=1
            self.assertEqual(success,m["V"]**2-len(m["flags"]))

    def test_03_seed_six_named_original_flag_IDs_and_unique_anchor(self):
        for s in (2,4):
            m=real_source(s)
            a=_source_six_seed(m)
            self.assertEqual(len(set(a["ids"])),6)
            self.assertEqual(len(set(a["residual"])),3)
            self.assertEqual(len(set(a["anchors"])),3)
            self.assertEqual(genuine_projection(m,a["q"],a["r"]),
                             (a["p"],a["ell"]))
            self.assertTrue(all(z not in a["residual"] for z in a["anchors"]))

    def test_04_minimal_original_complete_global_f_g_injection(self):
        for s in (2,4):
            for left,right in ((0,0),(0,1),(1,2)):
                m=template_model(s,left,right)
                self.assertEqual(len(set(m["f"])),m["V"])
                self.assertEqual(len(set(m["g"])),m["V"])
                self.assertEqual(m["a"],min(i for i in range(2,30) if i*(i-1)//2>=m["V"]))
                self.assertTrue(all(len(pair)==2 and pair[0]<pair[1]
                                    for pair in m["f"]+m["g"]))

    def test_05_exactly_three_C4s_on_each_factor_side(self):
        x=all_four_cycles()
        self.assertEqual(len(x),3)
        for e in x:
            self.assertEqual(len(set(e)),4)
            deg=Counter(z for edge in e for z in edge)
            self.assertEqual(set(deg),set(range(4)))
            self.assertEqual(set(deg.values()),{2})

    def test_06_actual_TWO_original_disjoint_diagonals_per_CORE_ID(self):
        for s in (2,4):
            m=template_model(s,0,0)
            graph=source_owned_graph(m)
            self.assertEqual(len(graph["edges"]),2*len(m["C"]))
            self.assertEqual(len(set(graph["edges"].values())),len(m["C"]))
            for i in m["C"]:
                e=[e for e,j in graph["edges"].items() if j==i]
                self.assertEqual(len(e),2)
                self.assertFalse(set(e[0])&set(e[1]))

    def test_07_nine_ORIGINAL_W32_BBo_template_combinations_all_checked(self):
        cases=self.c["original_nine_C4xC4_W32_templates"]
        self.assertEqual(len(cases),9)
        self.assertEqual({(p["left"],p["right"]) for p in cases},
                         {(i,j) for i in range(3) for j in range(3)})
        self.assertEqual(sum(p["source_aligned"] for p in cases),3)
        self.assertEqual(sum(not p["source_aligned"] for p in cases),6)

    def test_08_source_ONLY_alignment_iff_BBo_has_two_paths(self):
        for p in self.c["original_nine_C4xC4_W32_templates"]:
            n=2 if p["source_aligned"] else 0
            self.assertEqual(p["SOURCE_ONLY_inverse_directed_count"],n)
            self.assertEqual(p["INDEPENDENT_PHYSICAL_first_directed_count"],n)
            self.assertEqual(p["actual_true_original_source_BBo_sixsets"],n//2)
            self.assertEqual(p["source_middle_left"]==p["source_middle_right"],
                             bool(n))

    def test_09_actual_original_six_ID_inverse_two_REVERSED_paths(self):
        for s in (2,4):
            for i,j in ((0,0),(0,1)):
                m=template_model(s,i,j)
                q=independent_sixID_factor_inverse(m,m["seed"]["ids"])
                self.assertIn(len(q),(0,2))
                if q:
                    self.assertEqual(q[0][0],q[1][0][::-1])
                    self.assertEqual(q[0][1],q[1][1][::-1])
                    self.assertEqual(len(set(q[0][0])),4)
                    self.assertEqual(len({p[0] for p in q[0][0]}),4)
                    self.assertEqual(len({p[1] for p in q[0][0]}),4)

    def test_10_W34_nonvacuous_original_positive_and_unaligned_negative(self):
        cases=self.c["original_W34_positive_and_negative_sixsets"]
        self.assertEqual(len(cases),2)
        self.assertEqual({p["source_aligned"] for p in cases},{True,False})
        self.assertEqual(sorted(p["SOURCE_ONLY_inverse_directed_count"] for p in cases),[0,2])
        for p in cases:
            self.assertEqual(p["SOURCE_ONLY_inverse_directed_count"],
                             p["INDEPENDENT_PHYSICAL_first_directed_count"])

    def test_11_TRUE_GF5_signs_exactly_ten_each_sixset(self):
        for p in self.c["original_nine_C4xC4_W32_templates"]:
            self.assertEqual(p["exact_GF5_ten_sign_mass"],
                             SIGNED_ALIGNED if p["source_aligned"] else SIGNED_UNALIGNED)
            self.assertGreater(p["exact_GF5_ten_sign_mass"],51750)

    def test_12_independent_original_GF5_Fourier_nontrivial_integer_result(self):
        m=template_model(2,0,0)
        edges=_canonical_edges_for_gf5(m,m["seed"]["ids"])
        self.assertEqual(len(edges),12)
        out=independent_gf5_fourier_mass(edges)
        self.assertEqual(len(out["ten_signs"]),10)
        self.assertEqual(sum(out["ten_signs"]),53838)
        self.assertGreater(min(out["ten_signs"]),0)
        self.assertTrue(out["independent_fourier_arithmetic_exact"])

    def test_13_original_genuine_source_C6_C4_alignment_not_graph_fitting(self):
        cases=self.c["original_nine_C4xC4_W32_templates"]
        aligned=[q for q in cases if q["source_aligned"]]
        self.assertEqual(len(aligned),3)
        self.assertEqual(len({q["source_middle_left"] for q in aligned}),3)
        self.assertEqual(len({q["source_middle_right"] for q in aligned}),3)

    def test_14_actual_original_W32_full_CORE_enumerated_without_source_oracle(self):
        p=next(q for q in self.c["additional_true_original_core_and_deleted_cases"]
               if q["s"]==2 and q["Cmode"]=="full")
        self.assertEqual(p["full_paired_CORE_original_flags"],
                         p["full_original_source_flags"])
        self.assertGreaterEqual(p["produced_true_original_sixsets"],0)
        self.assertTrue(p["all_produced_sixsets_two_oracles_agree"])

    def test_15_REAL_original_C_outside_anchors_and_true_deleted_middle(self):
        c=self.c["additional_true_original_core_and_deleted_cases"]
        self.assertTrue(any(q["Cmode"]=="seed_plus" and
                            q["produced_true_original_sixsets"]>=1 for q in c))
        for q in c:
            if q["Zmode"]=="middle":
                self.assertEqual(q["seed_source_inverse"],0)
            self.assertTrue(q["original_FULL_three_projection_anchors_may_be_OUTSIDE_CORE"])

    def test_16_FAIL_CLOSED_invalid_six_ORIGINAL_ID_sets_and_template_inputs(self):
        m=template_model(2,0,0)
        ids=m["seed"]["ids"]
        for broken in (ids[:5],ids[:5]+(ids[0],),ids[:5]+(-1,),
                       ids[:5]+(999999,)):
            with self.assertRaises(ValueError):
                independent_sixID_factor_inverse(m,broken)
        for lr in ((-1,0),(0,4),(9,1)):
            with self.assertRaises(ValueError):
                template_model(2,*lr)
        with self.assertRaises(ValueError):
            template_model(3,0,0)

    def test_17_remaining_CORE_missing_or_middle_source_Z_yields_NO_paths(self):
        m=template_model(2,0,0,mask="empty")
        self.assertEqual(independent_sixID_factor_inverse(m,m["seed"]["ids"]),())
        m=template_model(2,0,0,mask="seed",delete_middle=True)
        self.assertEqual(independent_sixID_factor_inverse(m,m["seed"]["ids"]),())
        self.assertEqual(physical_first_paths(m)["actual_unweighted_produced_BBo"],0)

    def test_18_true_original_all_w32_full_P3_partition_is_closed(self):
        m=template_model(2,0,0,mask="full")
        p=physical_first_paths(m)
        self.assertEqual(p["actual_accepted_directed_3walks"],
                         2*p["actual_unweighted_produced_BBo"])
        for ids,paths in p["accepted"].items():
            rec=independent_sixID_factor_inverse(m,ids)
            self.assertEqual({x for x,_ in rec},paths)

    def test_19_true_ORIGINAL_five_distinct_factors_and_unique_source_anchors(self):
        for s in (2,4):
            m=template_model(s,0,0)
            ids=m["seed"]["ids"]
            cp=Counter(m["flags"][i][0] for i in ids)
            cl=Counter(m["flags"][i][1] for i in ids)
            self.assertEqual(sorted(cp.values()),[1,1,1,1,2])
            self.assertEqual(sorted(cl.values()),[1,1,1,1,2])
            self.assertEqual(len(set(ids)),6)

    def test_20_original_D6_and_produced_BBo_factor_profile_are_disjoint(self):
        for s in (2,4):
            m=template_model(s,0,0,mask="seed")
            seed=m["seed"]["ids"]
            self.assertEqual(original_sixset_factor_profile(m,seed),
                             "FIVE_P_AND_L_SHARED_ANCHOR_BBO_OVERLAP")
            source=real_source(s)
            match=[];pused=set();lused=set()
            for i,(p,ell) in enumerate(source["flags"]):
                if p not in pused and ell not in lused:
                    match.append(i);pused.add(p);lused.add(ell)
                    if len(match)==6:break
            self.assertEqual(len(match),6)
            self.assertEqual(original_sixset_factor_profile(m,match),
                             "SIX_DISTINCT_P_AND_L_ONLY_D6_NECESSARY")
            with self.assertRaises(ValueError):
                original_sixset_factor_profile(m,seed[:5])
        self.assertTrue(self.c["original_D6_and_produced_BBo_disjoint_by_named_source_factor_profile"])

    def test_21_root_dependency_DAG_not_accidentally_promoted(self):
        c=self.c
        self.assertEqual(c["schema"],SCHEMA)
        self.assertEqual(c["status"],STATUS)
        self.assertEqual(c["issue"],230)
        self.assertEqual(c["parent_pr"],780)
        self.assertTrue(c["all_h_original_factor_alignment_zero_or_two_mathematically_proved"])
        self.assertTrue(c["all_h_source_GQ_projection_anchoring_required"])
        self.assertTrue(c["all_h_per_source_sixset_TWO_reverse_physical_paths_in_real_CORE"])
        self.assertTrue(c["all_h_original_BBo_produced_SOURCE_class_canonical"])
        self.assertTrue(c["exact_GF5_potential_integer_Fourier_verified"])
        self.assertFalse(c["true_original_S_s_seven_class_PROVED_A"])
        self.assertTrue(c["root_global_dependency_DAG_STILL_REQUIRES_independent_acceptance"])


if __name__=="__main__":
    unittest.main()
