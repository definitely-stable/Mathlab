"""Independent falsifiers for #793 G6-C3 shared selector + exact closure."""
from collections import Counter,defaultdict
from fractions import Fraction as Q
from itertools import product
import unittest

from gio_t3c3_integrated_low import (
    SCHEMA,PARENT_C1,PARENT_C2,certificate,closure_ledger,
    validate_ledger_domain,external_constants,owner_conflict_graph,
    frozen_heavy_low_core,actual_physical_degrees,counted_walks,
    trace_even,coordinate_returns,walk_and_selector_finite,
    exact_coherent_cut_path_probability,exact_d6_cut_probability,
)
from gio_t3c2_partial_books import make_model,selected_mask
from hyp105_aa4_branch_a_integrated_referee import actual_edges


def direct_walk_census(adj,order,proper):
    """Independent iterative global list-of-walks, no production recursion."""
    out=Counter()
    paths=[(u,) for u in adj]
    for _ in range(order):
        paths=[v+(n,) for v in paths for n in adj[v[-1]]]
    for path in paths:
        if proper and (len(set(z[0] for z in path))!=len(path)
                       or len(set(z[1] for z in path))!=len(path)):
            continue
        out[path[0],path[-1]]+=1
    return dict(out)


class TestG6C3(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.z=certificate()

    def test_01_certificate_claim_and_fixed_structural_scope(self):
        z=self.z
        self.assertEqual(z["schema"],SCHEMA)
        self.assertEqual(z["parent_G6C1_HEAD"],PARENT_C1)
        self.assertEqual(z["parent_G6C2_HEAD"],PARENT_C2)
        self.assertEqual(z["claim"],
          "CONDITIONAL_INTRINSIC_T3_LINEAR_EXCESS_HEAVY_LOW_CLOSED")
        for x in ("no_claim_external_C6_numeric_constants",
                  "no_infinite_nonGQ_linear_excess_existence",
                  "no_unrestricted_incidence_T3",
                  "no_general_ASET_exponent",
                  "no_external_human_referee_or_Lean"):
            self.assertTrue(z[x])

    def test_02_exact_algebraic_ledger_gates_and_all_error_exponents(self):
        for obj in self.z["exact_formal_ledgers"]:
            self.assertTrue(obj["FORMAL_ONLY"])
            self.assertTrue(obj["published_graph_numeric_constants_not_supplied"])
            K=obj["selector"]["K"];T=int(obj["selector"]["T"])
            r0=int(obj["closure"]["sufficient_integer_r0"])
            rho=Q(obj["closure"]["rho"]);delta=Q(obj["closure"]["delta"])
            e=Q(obj["closure"]["eps"]);w=Q(obj["selector"]["LOW_3walk_lower"])
            q3=obj["selector"]["cut_path_q3"]
            L6=obj["moment"]["L6"]
            self.assertGreater(rho,0);self.assertGreater(delta,0)
            self.assertLessEqual(rho,Q(1,32))
            self.assertEqual(obj["selector"]["cut_path_q2"],16*(K+1)**2)
            self.assertEqual(q3,64*(K+1)**3)
            self.assertLessEqual(12*(obj["fixed_before_source"]["balance_b"]**2)
                                 *rho*q3*q3*L6,e*e)
            self.assertLessEqual(obj["moment"]["improper_coefficient"],e*r0)
            self.assertLessEqual(obj["moment"]["endpoint_clean_E"]**2,e*e*r0)
            self.assertLessEqual(obj["moment"]["physical_fourblocker_D"]**8,
                                 e**8*r0)
            self.assertEqual(8*e,w)
            self.assertLessEqual(delta,w/4)
            self.assertEqual(obj["selector"]["one_global_owner_priority"],True)
            self.assertFalse(obj["selector"]["independent_reselection_per_path"])

    def test_03_quantifier_guards_and_fixed_c_before_source(self):
        for b,C in ((1,0),(1,1),(2,2),(3,5)):
            obj=closure_ledger(b,C,Q(1),Q(1))
            r0=int(obj["closure"]["sufficient_integer_r0"])
            self.assertTrue(validate_ledger_domain(r0,r0,0,0,obj))
            self.assertTrue(validate_ledger_domain(r0,r0,C*r0,0,obj))
            rho=Q(obj["closure"]["rho"])
            allowed=(rho*r0**4).__floor__()
            self.assertTrue(validate_ledger_domain(r0,r0,0,allowed,obj))
            for trial in ((r0-1,r0-1,0,0),
                          (r0,(b+1)*r0,0,0),
                          (r0,r0,C*r0+1,0),
                          (r0,r0,0,allowed+1),
                          (r0,r0,-1,0),(r0,r0,0,-1)):
                with self.assertRaises(ValueError):
                    validate_ledger_domain(*trial,obj)

    def test_04_external_graph_constants_not_fabricated(self):
        for bad in [(1,1), (Q(1),Q(0)),(Q(1),Q(2)),
                    (Q(1,2),Q(1)),(Q(1),0.2)]:
            with self.assertRaises(ValueError):
                closure_ledger(1,0,*bad)
        for b,C in ((0,0),(1,-1),(True,2),(2,1.5)):
            with self.assertRaises(ValueError):
                closure_ledger(b,C,Q(1),Q(1))

    def test_05_direct_proper_two_three_walks_vs_production(self):
        for name in ("W32","W33","Qminus24","switchedDoubleW32"):
            m=make_model(name)
            A,_=selected_mask(m,"mixed")
            a,_=actual_edges(m,A)
            for i in (2,3):
                self.assertEqual(counted_walks(a,i,True),
                                 direct_walk_census(a,i,True))
            self.assertEqual(trace_even(a,2),
                             sum(x*x for x in direct_walk_census(a,2,False).values()))
            self.assertEqual(trace_even(a,3),
                             sum(x*x for x in direct_walk_census(a,3,False).values()))

    def test_06_coordinate_return_exact_J_identity_in_four_structures(self):
        for name in ("W32","W33","Qminus24",
                     "dualQminus42","doubleW32",
                     "switchedDoubleW32"):
            m=make_model(name)
            A,_=selected_mask(m,"mixed")
            H,_=actual_edges(m,A)
            J=owner_conflict_graph(m,A)
            qx,qy=coordinate_returns(H)
            self.assertEqual(qx+qy,
                             8*len(A)+2*sum(map(len,J.values())))

    def test_07_jensen_ordered_all_threewalks_and_true_alphabet_product(self):
        for name in ("W32","W33","doubleW32","switchedDoubleW32"):
            m=make_model(name)
            A,_=selected_mask(m,"mixed")
            H,_=actual_edges(m,A)
            value=sum(len(H[u])*len(H[v]) for u in H for v in H[u])
            self.assertEqual(value,sum(counted_walks(H,3,False).values()))
            self.assertGreaterEqual(value*(m["aP"]*m["aL"])**2,
                                    (4*len(A))**3)

    def test_08_source_freezing_and_incidence_core_degree_gate(self):
        for name in ("W32","Qminus24","switchedDoubleW32"):
            m=make_model(name)
            A,_=selected_mask(m,"mixed")
            for thr,K in ((0,0),(2,3),(100,100)):
                c=frozen_heavy_low_core(m,A,thr,K)
                C=c["C"]
                self.assertTrue(C<=A)
                self.assertLessEqual(c["actual_CORE_max_physical_degree"],thr)
                self.assertLessEqual(c["actual_CORE_max_J"],K)
                self.assertLessEqual(
                    c["owners_removed_by_heavy"],
                    c["full_heavy_touching_edges"])
                self.assertGreaterEqual(
                    len(C),len(m["flags"])-(len(m["flags"])-len(A))
                    -c["full_heavy_touching_edges"]
                    -(2*c["FULL_source_owner_J_edges"]//(K+1)))
            self.assertEqual(
                frozen_heavy_low_core(m,A,100,100)["C"],A)

    def test_09_invalid_core_threshold_and_source_set(self):
        m=make_model("W32")
        A,_=selected_mask(m,"full")
        for t,K in ((-1,0),(0,-1),(1.5,0),(0,2.5)):
            with self.assertRaises(ValueError):
                frozen_heavy_low_core(m,A,t,K)
        with self.assertRaises(ValueError):
            frozen_heavy_low_core(m,{len(m["flags"])},2,3)

    def test_10_single_shared_global_selector_sampled_cycles_are_proper(self):
        all=self.z["finite_global_core_falsifiers"]
        self.assertTrue(all)
        for x in all:
            self.assertTrue(x["return_formula_exact"])
            self.assertTrue(x["exact_walk_Jensen_lower"])
            self.assertTrue(x["actual_inner_blocker_bound_four_positions"])
            self.assertTrue(x["source_partial_projection_not_completed"])
        # At least one ACTIVE core means we really checked a selector,
        # rather than only taking an empty CORE.
        explicit=walk_and_selector_finite("W32","lex","full",100,100)
        self.assertGreater(explicit["LOW_core"],0)
        self.assertTrue(explicit["shared_priority_and_two_global_cuts_checked"])

    def test_11_exact_global_typed_cut_length_two_and_three(self):
        d=self.z["local_coherent_cut_probability"]
        self.assertEqual(d["cut_probabilities"]["2"]["exact_probability"],"1/16")
        self.assertEqual(d["cut_probabilities"]["3"]["exact_probability"],"1/64")
        for p in d["cut_probabilities"].values():
            self.assertEqual(p["independent_owner_priority_success_probability"],"1")
            self.assertTrue(p["literal_original_distinct_owners"])
        self.assertTrue(d["full_global_selection_not_replaced_by_pathwise_cuts"])

    def test_12_six_distinct_owner_D6_cut_exactly_one_in_1024(self):
        d=self.z["local_D6_coherent_cut_probability"]
        self.assertEqual(d["exact_favorable_typed_cut_assignments"],4)
        self.assertEqual(d["exact_total_typed_cut_assignments"],4096)
        self.assertEqual(d["probability_reduced"],"1/1024")

    def test_13_nonGQ_true_source_moore_excess_preserved_without_template(self):
        d=walk_and_selector_finite("switchedDoubleW32","correlated","mixed",100,100)
        self.assertEqual(d["source_s"],2)
        self.assertEqual(d["source_t"],2)
        self.assertEqual(d["original_source_flags"],90)
        self.assertTrue(d["shared_priority_and_two_global_cuts_checked"])
        self.assertGreater(d["threewalks_all"],0)

    def test_14_empty_core_produces_no_fake_selected_moments(self):
        x=walk_and_selector_finite("W32","lex","empty_core",1,1)
        self.assertEqual(x["LOW_core"],0)
        self.assertEqual(x["threewalks_all"],0)
        self.assertEqual(x["actual_uncut_trace_A4"],0)
        self.assertFalse(x["shared_priority_and_two_global_cuts_checked"])

    def test_15_formal_external_inputs_independent_of_actual_finite_cases(self):
        x=self.z
        self.assertEqual(len(x["exact_formal_ledgers"]),4)
        self.assertGreaterEqual(len(x["finite_global_core_falsifiers"]),7)
        self.assertTrue(all(y["FORMAL_ONLY"] for y in x["exact_formal_ledgers"]))
        # No direct finite assertion of a giant universal r0 graph.
        self.assertTrue(x["no_infinite_nonGQ_linear_excess_existence"])
        self.assertTrue(x["no_unrestricted_incidence_T3"])


if __name__=="__main__":
    unittest.main()
