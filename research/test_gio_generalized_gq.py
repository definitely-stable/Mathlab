"""Fail-closed axiomatic GQ(s,t) and unequal-geometry original source falsifiers."""
from fractions import Fraction as Q
from math import comb
import unittest

from gio_generalized_gq import (
    SCHEMA, balanced_ledger, validate_asymptotic_domain, symplectic_prime,
    elliptic_minus_24, dual_geometry, geometry, structure,
    strongly_regular_data, model, collinearity_conflict_certificate,
    adversarial_anchor_damage, finite_case, certificate,
)
from gio_resilience import source_first_d6, source_first_bbo, physical_bbo
from hyp105_aa4_branch_a_integrated_referee import physical_d6


class TestGIO003(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.c=certificate()
        cls.by={x["kind"]:x for x in cls.c["finite_cases"]}

    def test_01_real_structures_even_odd_and_unequal(self):
        expect={"W32":(2,2,15,15,45),"W33":(3,3,40,40,160),
                "Qminus24":(2,4,27,45,135),
                "dualQminus42":(4,2,45,27,135),
                "W34":(4,4,85,85,425)}
        for name,(s,t,vp,vl,n) in expect.items():
            z=self.by[name]
            self.assertEqual((z["s"],z["t"],z["structural"]["points"],
                              z["structural"]["lines"],z["original_flags"]),
                             (s,t,vp,vl,n))
            self.assertTrue(z["structural"]["both_source_SRG_checked_directly"])

    def test_02_unequal_true_point_and_line_srg_parameters(self):
        for name in ("Qminus24","dualQminus42"):
            z=self.by[name];s=z["s"];t=z["t"]
            self.assertEqual(z["structural"]["point_parameters"],
                             [(s+1)*(s*t+1),s*(t+1),s-1,t+1])
            self.assertEqual(z["structural"]["line_parameters"],
                             [(t+1)*(s*t+1),t*(s+1),t-1,s+1])
            self.assertNotEqual(s-t-2,-2)
            self.assertEqual(z["structural"]["distinct_nonincident_projections"],
                             (s+1)*(s*t+1)*((t+1)*(s*t+1)-t-1))

    def test_03_independent_odd_GF3_projective_construction(self):
        g=symplectic_prime(3)
        self.assertEqual((g["s"],g["t"],len(g["lines"])),(3,3,40))
        self.assertEqual(len(structure(g)["flags"]),160)

    def test_04_independent_elliptic_minus_quadric_geometry(self):
        g=elliptic_minus_24();d=dual_geometry(g)
        self.assertEqual((len(g["lines"]),len(d["lines"])),(45,27))
        self.assertEqual((g["s"],g["t"]), (2,4))
        self.assertEqual((d["s"],d["t"]), (4,2))
        self.assertEqual(len(structure(g)["projection"]),27*40)
        self.assertEqual(len(structure(d)["projection"]),45*24)

    def test_05_falsify_fake_SRGS_and_broken_incidence(self):
        g=geometry("W32")
        bad=dict(g,lines=g["lines"][:-1])
        with self.assertRaises(AssertionError):
            structure(bad)
        g=geometry("Qminus24")
        L=list(g["lines"]);L[0]=(L[0][0],L[0][0],L[0][1])
        with self.assertRaises(AssertionError):
            structure(dict(g,lines=tuple(L)))

    def test_06_separate_minimal_pair_alphabets_and_injectivity(self):
        for kind in self.by:
            m=model(kind)
            self.assertGreaterEqual(comb(m["aP"],2),m["Vp"])
            self.assertLess(comb(m["aP"]-1,2),m["Vp"])
            self.assertGreaterEqual(comb(m["aL"],2),m["Vl"])
            self.assertLess(comb(m["aL"]-1,2),m["Vl"])
            self.assertEqual(len(set(m["f"])),m["Vp"])
            self.assertEqual(len(set(m["g"])),m["Vl"])
            if kind=="Qminus24":
                self.assertEqual((m["aP"],m["aL"]),(8,10))
            if kind=="dualQminus42":
                self.assertEqual((m["aP"],m["aL"]),(10,8))

    def test_07_literal_J_equals_typed_collinearity_and_unequal_gram(self):
        for z in self.by.values():
            m=model(z["kind"],z["scheme"])
            r=collinearity_conflict_certificate(m)
            self.assertEqual(r["J"],r["e_col_point"]+r["e_col_line"])
            self.assertTrue(r["unequal_typed_Gram_identity_checked"])
            self.assertEqual(r,z["spectral"])

    def test_08_single_deleted_flag_has_exact_3st_damage(self):
        for kind in self.by:
            m=model(kind)
            for idx in (0,len(m["flags"])//2,len(m["flags"])-1):
                n,k=adversarial_anchor_damage(m,{idx})
                self.assertEqual(n,3*m["s"]*m["t"])
                self.assertEqual(k,12*m["s"]*m["t"])

    def test_09_arbitrary_targeted_deletion_no_independence(self):
        for z in self.by.values():
            m=model(z["kind"],z["scheme"])
            for x in z["masks"]:
                self.assertTrue(x["independent_censuses_agree"])
                self.assertEqual(x["damaged_oriented_endpoint_pairs"],
                                 4*x["damaged_nonincident_projections"])
                self.assertLessEqual(x["damaged_oriented_endpoint_pairs"],
                                     12*m["s"]*m["t"]*x["removed"])
                self.assertLessEqual(x["surviving_D6"],z["D6"])
                self.assertLessEqual(x["surviving_produced_BBo"],z["produced_BBo"])
                self.assertLessEqual(6*x["disjoint_packing"],m["Vp"]*(m["t"]+1))

    def test_10_distinct_original_source_sixsets_in_two_dfs(self):
        for name in ("W32","W33","Qminus24","dualQminus42"):
            m=model(name)
            A=frozenset(range(len(m["flags"])))
            left=source_first_d6(m,A)
            right=physical_d6(m,A)
            self.assertEqual(left,right)
            self.assertTrue(all(len(k)==len(set(k))==6 for k in left))

    def test_11_source_vs_physical_produced_BBo_with_surviving_anchors(self):
        for name in ("W32","W33","Qminus24","dualQminus42"):
            m=model(name);A=frozenset(range(len(m["flags"])))
            a=source_first_bbo(m,A);b=physical_bbo(m,A)
            self.assertEqual(a,b)
            self.assertTrue(all(len(k)==6 for k in a))
            Z={0}
            a2=source_first_bbo(m,A-Z);b2=physical_bbo(m,A-Z)
            self.assertEqual(a2,b2)
            self.assertEqual(a2,{k:v for k,v in a.items() if not (set(k)&Z)})

    def test_12_known_genuine_W32_regression(self):
        z=self.by["W32"]
        self.assertEqual((z["D6"],z["produced_BBo"]),(15,2))
        self.assertEqual(z["scheme"],"lex")

    def test_13_at_least_one_nonvacuous_odd_or_unequal_finite_witness(self):
        self.assertTrue(any(self.by[k]["D6"]+self.by[k]["produced_BBo"]>0
                            for k in ("W33","Qminus24","dualQminus42")))
        self.assertTrue(all(z["all_source_first_physical_first_equal"]
                            for z in self.by.values()))

    def test_14_fixed_balance_quantifiers_and_literal_positivity(self):
        for led in self.c["formal_ledgers"]:
            self.assertEqual(led["schema"],SCHEMA)
            self.assertGreater(Q(led["rho"]),0)
            self.assertGreater(Q(led["delta"]),0)
            self.assertLessEqual(Q(led["rho"]),Q(led["rho_cap"]))
            self.assertLessEqual(Q(led["delta"]),Q(led["c0"])/led["R"]**6)
            self.assertTrue(led["FORMAL_ONLY"])
            self.assertTrue(led["external_numeric_constants_unknown"])
            self.assertFalse(led["geometric_characteristic_assumed"])

    def test_15_all_four_Low_errors_paid_after_frozen_T(self):
        for z in self.c["formal_ledgers"]:
            eps=Q(z["error_budget_each"]);rho=Q(z["rho"])
            R0=int(z["sufficient_integer_r0"]);B=z["balance_upper"]
            self.assertLessEqual(12*B*B*rho*z["q3"]**2*int(z["L6"]),eps**2)
            self.assertLessEqual(int(z["improper_coefficient"]),eps*R0)
            self.assertLessEqual(int(z["E"])**2,eps**2*R0)
            self.assertLessEqual(int(z["D"])**8,eps**8*R0)
            self.assertLessEqual(8*z["N_upper"]*z["R"]**3*Q(z["C0"])**3,int(z["T"]))
            self.assertGreater(R0,2**31)
            self.assertEqual(Q(z["core_lower"]),Q(1,2))

    def test_16_invalid_external_constants_fail_closed(self):
        for args in ((0,Q(1),Q(1)),(1,1,Q(1)),(1,Q(1),1),
                     (1,Q(0),Q(1)),(1,Q(1),Q(0)),(1,Q(1),Q(2))):
            with self.assertRaises(ValueError):
                balanced_ledger(*args)
        with self.assertRaises(ValueError):
            geometry("FAKE_GQ")

    def test_17_balance_and_deletion_domain_rejection(self):
        z=balanced_ledger(2)
        r=int(z["sufficient_integer_r0"])
        maxZ=int(Q(z["rho"])*r**4)
        self.assertEqual(validate_asymptotic_domain(r,2*r,maxZ,z),r)
        for s,t,k in ((r-1,r-1,0),(r,2*r+1,0),
                      (r,r,maxZ+1),(r,r,-1),(r,2*r,True)):
            with self.assertRaises(ValueError):
                validate_asymptotic_domain(s,t,k,z)

    def test_18_Gf_Gg_unequal_sign_and_exact_formula(self):
        for kind in ("Qminus24","dualQminus42"):
            m=model(kind,"correlated")
            d=collinearity_conflict_certificate(m)
            self.assertGreater(d["G_point"],0)
            self.assertGreater(d["G_line"],0)
            self.assertEqual(d["J"],d["e_col_point"]+d["e_col_line"])

    def test_19_GF5_model_independent_of_characteristic(self):
        v=self.c["independent_GF5"]
        self.assertEqual(v["palette"],51)
        self.assertEqual(v["d6_alternating"],5643)
        self.assertEqual(len(v["bbo_sign_counts"]),10)
        self.assertGreaterEqual(min(v["bbo_sign_counts"]),5175)

    def test_21_actual_produced_BBo_signed_topology_odd_and_unequal(self):
        from hyp105_aa4_branch_a_integrated_referee import (
            actual_bbo_flow_topology, flow_catalog,
        )
        flow=flow_catalog()
        self.assertGreaterEqual(min(flow["bbo_sign_counts"]),5175)
        for kind in ("W33","Qminus24","dualQminus42"):
            m=model(kind)
            A=frozenset(range(len(m["flags"])))
            b=source_first_bbo(m,A)
            self.assertGreater(len(b),0)
            keys=sorted(b)
            for ids in keys[::max(1,len(keys)//15)][:15]:
                self.assertEqual(len(b[ids]),2)
                path=next(iter(b[ids]))
                self.assertTrue(actual_bbo_flow_topology(m,ids,path))
                self.assertEqual(len(ids),6)

    def test_22_naive_equal_order_minus_four_srg_term_is_false(self):
        from collections import Counter
        for kind in ("Qminus24","dualQminus42"):
            m=model(kind)
            d=collinearity_conflict_certificate(m)
            s,t=m["s"],m["t"]
            V=m["Vp"]
            fibre=Counter(x for pair in m["f"] for x in pair)
            naive=2*V*(s-1)*(t+1)-4*d["e_col_point"]+(t+1)*sum(n*n for n in fibre.values())
            self.assertEqual(d["G_point"]-naive,2*(s-t)*d["e_col_point"])
            self.assertNotEqual(d["G_point"],naive)

    def test_20_explicit_nonimplications_and_program_scope(self):
        self.assertEqual(self.c["issue"],793)
        self.assertEqual(self.c["claim"],"BALANCED_GQ_RESILIENCE_PROOF_CANDIDATE_T1_T2")
        self.assertTrue(self.c["finite_checks_are_not_all_order_proof"])
        self.assertTrue(self.c["no_existence_claim_for_arbitrary_s_t"])
        self.assertTrue(self.c["no_T3_abstract_incidence_theorem"])
        self.assertTrue(self.c["no_unrestricted_ASET_improvement"])
        self.assertFalse(self.c["external_peer_review_received"])


if __name__=="__main__":
    unittest.main()
