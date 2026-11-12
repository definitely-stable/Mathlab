"""Independent exact genuine ORIGINAL HYP-105 middle overlap neighborhood referee."""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
import unittest

from hyp105_original_middle_neighborhood_charge_referee import (
    SCHEMA,STATUS,CASES,_one_true_source_endpoint_charge,
    _one_full_original_source_case,canonical_report
)
from hyp105_original_full_w34_weighted_risk_referee import (
    _source,_true_original_proper_P3,_rank_probability3,_pair_bad
)
from hyp105_original_symbol_secondmoments_referee import (
    _full_exact_symbol_moments_one_bin,_potential_original_middle_label_overlap_degree_bound
)


class TestTrueOriginalMiddleNeighborhoodCharge(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.doc=canonical_report()
        cls.rows=cls.doc["true_original_W32_W34_full_source_neighborhood_censuses"]

    def test_all_h_scientific_scope_and_source_status(self):
        c=self.doc
        self.assertEqual(c["schema"],SCHEMA)
        self.assertEqual(c["status"],STATUS)
        self.assertEqual(c["issue"],230)
        for z in ("all_h_source_closed_overlap_neighborhood_exact_postings_and_symbol_moment_mass",
                  "all_h_original_point_line_source_pair_label_overlap_degree_capacity",
                  "all_h_weighted_neighborhood_Laplacian_variance_and_spectral_upper",
                  "all_h_strict_local_BAD_B75_forces_one_heavy_original_middle_neighborhood",
                  "all_h_global_BAD_B75_forces_some_local_heavy_original_middle_neighborhood"):
            self.assertTrue(c[z])
        self.assertTrue(c["this_does_NOT_claim_all_h_uniform_75_percent_good_mass"])
        self.assertFalse(c["root_PROVED_A"])
        self.assertFalse(c["all_h_global_B_over_M_below_three_quarters_PROVED"])
        self.assertFalse(c["ASET_exponent_claimed"])
        self.assertFalse(c["infinite_correlated_counterfamily_claimed"])

    def test_true_original_all_eight_complete_source_path_counts(self):
        self.assertEqual(len(self.rows),8)
        self.assertEqual([(q["original_s"],q["original_scheme"],q["original_CORE"])
                          for q in self.rows],list(CASES))
        self.assertEqual([q["counts"]["full_real_original_proper_directed_P3s"]
                          for q in self.rows],
                         [1346,1154,838,83892,82846,79404,9966,66418])
        for q in self.rows:
            self.assertTrue(q["complete_original_actual_path_census"])
            self.assertEqual(q["actual_source_real_physical_diagonal_edges"],
                             2*q["source_retained_CORE_original_flags"])
            self.assertGreater(q["source_priority_original_triple_sets"],0)

    def test_all_h_global_original_M_G_B_exact_conservation(self):
        for r in self.rows:
            M=Fraction(r["total_M"]);G=Fraction(r["total_G"])
            B=Fraction(r["total_B"]);m={k:Fraction(v) for k,v in r["moments"].items()}
            self.assertGreater(M,0)
            self.assertGreater(G,0)
            self.assertGreaterEqual(B,0)
            self.assertEqual(M,G+B)
            self.assertEqual(M,m["M"])
            self.assertEqual(G,m["G"])
            self.assertEqual(B,m["B"])
            self.assertEqual(B,m["R"]-m["D"]-m["G11"])
            self.assertEqual(Fraction(r["exact_B_over_M"]),B/M)
            self.assertEqual(Fraction(r["original_neighborhood_overlap_R_over_M"]),m["R"]/M)

    def test_independent_previous_exact_W32_W34_ratios(self):
        expected=[
            Fraction(6455794325016624278974180549344,34112625017517015558762952579019),
            Fraction(1112181511961691267640954528608,5419443488794004529193758698293),
            Fraction(38485044924066111819475664,193743221070784284041268159)
        ]
        self.assertEqual(
            [Fraction(z["exact_B_over_M"]) for z in self.rows[3:6]],expected)
        self.assertEqual(Fraction(self.rows[0]["exact_B_over_M"]),
                         Fraction(395498199363009600,1190067603581473393))

    def test_all_h_original_neighborhood_graph_exact_Laplacian(self):
        for row in self.rows:
            m={k:Fraction(v) for k,v in row["moments"].items()}
            self.assertEqual(m["R"],
                m["source_weighted_degree_square_energy"]-
                m["source_laplacian_nonnegative_variance"])
            self.assertGreaterEqual(m["source_laplacian_nonnegative_variance"],0)
            self.assertGreaterEqual(m["source_weighted_degree_square_energy"],m["R"])
            self.assertGreaterEqual(m["source_spectral_degree_R_upper"],m["R"])
            self.assertGreaterEqual(m["source_top_degree_R_upper"],m["R"])
            self.assertGreaterEqual(m["source_max_single_group_R_upper"],m["R"])
            self.assertGreaterEqual(m["source_max_neighbor_R_upper"],m["R"])

    def test_all_h_TRUE_GQ_minimal_alphabet_degree_capacity_vs_active_source_degree(self):
        for row in self.rows:
            z=row["source_overlap_all_h_minimal_alphabet_capacity"]
            self.assertEqual(z["actual_alphabet"],row["original_minimal_alphabet"])
            self.assertEqual(z["s"],row["original_s"])
            self.assertGreater(z["unweighted_source_middle_pair_overlap_max_degree_cap"],0)
            self.assertLessEqual(row["max_occupied_middle_original_flag_overlap_closed_degree"],
                1+z["unweighted_source_middle_pair_overlap_max_degree_cap"])
            self.assertGreaterEqual(row["max_occupied_middle_original_flag_overlap_closed_degree"],1)

    def test_all_h_exact_weighted_heavy_neighborhood_B75_OBSTRUCTION(self):
        for row in self.rows:
            M=Fraction(row["total_M"]);B=Fraction(row["total_B"])
            c=Fraction(row["source_heavy_neighborhood_candidate_M_share"])
            safe=Fraction(row["source_max_neighborhood_strict_SAFE_M_share"])
            actual=Fraction(row["actual_source_strict_local_bad_M_share"])
            degsafe=Fraction(row["source_weighted_degree_strict_SAFE_M_share"])
            topsafe=Fraction(row["source_top_degree_strict_SAFE_M_share"])
            self.assertEqual(c+safe,1)
            self.assertTrue(0<=actual<=c<=1)
            self.assertTrue(0<=degsafe<=1)  # degree-energy and max-neighbor bounds are incomparable
            self.assertTrue(0<=topsafe<=safe<=1)
            self.assertLessEqual(actual+safe,1)
            self.assertLessEqual(actual+degsafe,1)
            self.assertLessEqual(actual+topsafe,1)
            self.assertLess(B/M,Fraction(3,4))

    def test_real_TRUE_original_bad_bin_source_neighborhood_witness(self):
        found=0
        for row in self.rows:
            w=row["first_actual_bad_real_original_source_neighborhood_witness"]
            if w is None:continue
            found+=1
            self.assertGreater(Fraction(w["B_over_M"]),Fraction(3,4))
            self.assertGreater(Fraction(w["max_neighborhood_relative_weight"]),
                               Fraction(w["necessary_relative_threshold"]))
            self.assertGreater(w["witness_neighborhood_original_flag_count"],0)
            self.assertIn(w["witness_original_middle_flag"],w["witness_source_flag_ids"])
            self.assertEqual(len(w["witness_middle_f_label"]),2)
            self.assertEqual(len(w["witness_middle_g_label"]),2)
            self.assertLessEqual(w["witness_neighborhood_original_flag_count"],
                                len(w["witness_source_flag_ids"]))
        self.assertGreater(found,0)

    def test_IND_W32_complete_original_pathpair_source_label_overlap_direct(self):
        # Independently iterate EVERY same-endpoint ordered pair of genuine
        # W32 original paths and compare the sum of pairwise middle source
        # label overlap products with the new posting+symbol formula.
        for scheme,core in (("lex","full"),("reverse","full"),("shift","Z17")):
            c=_source(2,scheme,core)
            bins=defaultdict(list);rank={}
            for path,owners in _true_original_proper_P3(c):
                k=tuple(sorted(owners))
                if k not in rank:rank[k]=_rank_probability3(k,c["J"])/64
                bins[(path[0],path[-1])].append((path,owners,rank[k]))
            directR=Fraction(0);postR=Fraction(0)
            for group in bins.values():
                zz=_one_true_source_endpoint_charge(group,c)
                source_R=Fraction(0)
                for p,os,wp in group:
                    pi,li=c["flags"][os[1]]
                    for q,ot,wq in group:
                        pj,lj=c["flags"][ot[1]]
                        x=bool(set(c["f"][pi])&set(c["f"][pj]))
                        y=bool(set(c["g"][li])&set(c["g"][lj]))
                        if x or y:source_R+=wp*wq
                self.assertEqual(source_R,zz["R"])
                postR+=zz["R"];directR+=source_R
            self.assertEqual(postR,directR)
            rr=next(row for row in self.rows if row["original_s"]==2
                and row["original_scheme"]==scheme and row["original_CORE"]==core)
            self.assertEqual(postR,Fraction(rr["moments"]["R"]))

    def test_IND_exact_new_neighborhood_oracle_vs_parent_symbol_moments_full_W34(self):
        # Independent parent source formula is computed by disjoint source
        # square-moment algebra; new one uses postings and overlap incidence.
        for scheme in ("lex","reverse","shift"):
            c=_source(4,scheme,"full")
            bins=defaultdict(list);rank={}
            for physical,owners in _true_original_proper_P3(c):
                key=tuple(sorted(owners))
                if key not in rank:rank[key]=_rank_probability3(key,c["J"])/64
                bins[(physical[0],physical[-1])].append((physical,owners,rank[key]))
            for group in bins.values():
                a=_one_true_source_endpoint_charge(group,c)
                b=_full_exact_symbol_moments_one_bin(group,c)
                self.assertEqual(a["M"],b["M"])
                self.assertEqual(a["G"],b["G"])
                self.assertEqual(a["B"],b["B"])
                self.assertEqual(a["D"],b["D"])
                self.assertEqual(a["G11"],b["G11"])
                self.assertEqual(a["R"],b["net_middle_label_union_overlap"])
                self.assertEqual(a["R_middle_symbol_second_moments"],b["net_middle_label_union_overlap"])

    def test_source_group_quadratic_and_diagonal_relationship(self):
        for r in self.rows:
            m={k:Fraction(v) for k,v in r["moments"].items()}
            Q=m["Q_original_middle_flag_group_energy"]
            self.assertGreater(Q,0)
            self.assertGreaterEqual(Q,m["D"])
            self.assertLessEqual(Q,3*m["D"])
            self.assertGreaterEqual(m["R"],Q)
            self.assertLessEqual(m["R"],m["M"])
            self.assertGreaterEqual(m["G"],m["D"])

    def test_full_W34_scientific_STOP_scope_not_promoted(self):
        for r in self.rows[3:6]:
            self.assertFalse(r["root_PROVED_A"])
            self.assertFalse(r["all_h_global_B_over_M_below_three_quarters_PROVED"])
            self.assertGreater(r["counts"]["real_physical_ordered_endpoints"],0)

    def test_invalid_empty_ORIGINAL_endpoints_and_source_weight_fail_closed(self):
        c=_source(2,"lex","full")
        with self.assertRaises(ValueError):
            _one_true_source_endpoint_charge([],c)
        path,owners=next(iter(_true_original_proper_P3(c)))
        for v in (Fraction(0),Fraction(-1),1):
            with self.assertRaises(AssertionError):
                _one_true_source_endpoint_charge([(path,owners,v)],c)

    def test_full_source_true_original_singleton_has_closed_neighborhood(self):
        c=_source(2,"lex","full")
        p,owners=next(iter(_true_original_proper_P3(c)))
        w=_rank_probability3(tuple(sorted(owners)),c["J"])/64
        x=_one_true_source_endpoint_charge([(p,owners,w)],c)
        self.assertEqual(x["R"],w*w)
        self.assertEqual(x["M"],w*w)
        self.assertEqual(x["G"],x["D"])
        self.assertEqual(x["B"],0)
        self.assertEqual(x["G11"],0)
        self.assertEqual(x["weighted_source_neighbor_max_fraction"],1)
        self.assertEqual(x["delta_occupied_original_middle_flag_overlap_closed_degree"],1)
        self.assertEqual(x["source_laplacian_nonnegative_variance"],0)

    def test_ALL_h_manual_nonuniform_source_weights_stress_algebra(self):
        # Algebra-only adversarial reweighting. These are NOT claimed as
        # actual original selector marginals; used to falsify any hidden
        # equal-weight assumption in source neighborhood charge.
        c=_source(2,"lex","full")
        binmap=defaultdict(list)
        for path,os in _true_original_proper_P3(c):
            binmap[(path[0],path[-1])].append((path,os))
        group=next(z for z in binmap.values() if len(z)>=3)
        modified=[(p,os,Fraction((i+1)*(i+2),11))
                  for i,(p,os) in enumerate(group)]
        a=_one_true_source_endpoint_charge(modified,c)
        self.assertEqual(a["G"]+a["B"],a["M"])
        self.assertEqual(a["R"],a["R_middle_symbol_second_moments"])
        self.assertEqual(
            a["source_weighted_degree_square_energy"]-a["source_laplacian_nonnegative_variance"],
            a["R"])

    def test_root_global_bad_witness_dichotomy_no_unproven_promotion(self):
        # Global weighted B/M>=.75 would have SOME bin at least .75
        # and hence SOME source neighbor carrying >= .75+(D+G11)/M
        # of that bin's middle group source mass. The finite source
        # ratio can be safe without refuting that conditional theorem.
        total=Fraction(0);part=Fraction(0)
        for r in self.rows:
            total+=Fraction(r["total_M"])
            part+=Fraction(r["total_B"])
            self.assertGreaterEqual(r["counts"].get(
                "source_heavy_neighborhood_candidate_endpoint_bins",0),
                r["counts"].get("actual_local_strict_bad_endpoint_bins",0))
        self.assertLess(part/total,Fraction(3,4))


if __name__=="__main__":
    unittest.main()
