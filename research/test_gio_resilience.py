"""Adversarial genuine-source falsifiers and exact universal error budget."""
import unittest
from fractions import Fraction as Q
from collections import Counter

from gio_resilience import (
    CAP, root_ledger, validate_asymptotic_budget, deletion_set, anchor_damage,
    model, source_first_d6, physical_d6, source_first_bbo, physical_bbo,
    greedy_pack, certificate, anchor_ids, dual_model, masks,
)


class TestGIOResilience(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cert=certificate()

    def test_01_exact_positive_uniform_deletion_budget(self):
        for z in self.cert["formal_ledgers"]:
            rho=Q(z["rho"]);delta=Q(z["delta"]);w=Q(z["walk_coefficient"])
            b=Q(z["error_budget_each"])
            self.assertGreater(rho,0)
            self.assertLessEqual(rho,CAP)
            self.assertGreater(delta,0)
            self.assertLessEqual(delta,Q(z["c0"])/z["R"]**6)
            self.assertLessEqual(delta,w/4)
            self.assertEqual(b,w/8)
            self.assertLessEqual(12*rho*z["q3"]**2*int(z["L6"]),b*b)

    def test_02_frozen_threshold_and_four_separate_errors(self):
        for z in self.cert["formal_ledgers"]:
            s=1<<z["sufficient_h0"];b=Q(z["error_budget_each"])
            T=int(z["T"]);E=int(z["E"]);D=int(z["D"])
            self.assertGreaterEqual(T,Q(17,2)*z["R"]**3*Q(z["C0"])**3)
            self.assertGreater(Q(z["core_coefficient"]),0)
            self.assertLessEqual(49*T,b*s)
            self.assertLessEqual(E**2,b*b*s)
            self.assertLessEqual(D**8,b**8*s)
            self.assertTrue(z["FORMAL_ONLY"])
            self.assertTrue(z["external_numeric_constants_unknown"])

    def test_03_invalid_constants_and_deletion_budget_rejected(self):
        for a,b in ((1,Q(1)),(Q(1),1),(Q(0),Q(1)),(Q(1),Q(0)),(Q(1),Q(2))):
            with self.assertRaises(ValueError):
                root_ledger(a,b)
        z=self.cert["formal_ledgers"][0]
        h=z["sufficient_h0"];s=1<<h
        cap=Q(z["rho"])*s**4
        n=cap.numerator//cap.denominator
        self.assertEqual(validate_asymptotic_budget(h,n,z),s)
        for d in (n+1,-1,(s+1)**2*(s*s+1),True):
            with self.assertRaises(ValueError):
                validate_asymptotic_budget(h,d,z)
        with self.assertRaises(ValueError):
            validate_asymptotic_budget(h-1,0,z)

    def test_04_singleton_exact_3s_squared_and_four_orientations(self):
        for s in (2,4):
            m=model(s,"lex","full")
            for i in (0,len(m["flags"])//2,len(m["flags"])-1):
                d,e=anchor_damage(m,[i])
                self.assertEqual(len(d),3*s*s)
                self.assertEqual(len(e),12*s*s)
                self.assertTrue(all(i in anchor_ids(m,q,r) for q,r in d))

    def test_05_original_flag_identity_fail_closed(self):
        m=model(2,"lex","full")
        for ids in ([0,0],[-1],[len(m["flags"])],[True]):
            with self.assertRaises(ValueError):
                deletion_set(m,ids)
        with self.assertRaises(ValueError):
            physical_bbo(m,frozenset(),frozenset({0}))
        with self.assertRaises(ValueError):
            source_first_bbo(m,frozenset(),frozenset({0}))
        with self.assertRaises(ValueError):
            greedy_pack([(0,1,2,3,4,4)])

    def test_06_all_masks_and_exact_independent_sets(self):
        for c in self.cert["finite_cases"]:
            self.assertTrue(c["duality_verified"])
            by={z["mask"]:z for z in c["masks"]}
            self.assertTrue({"empty","singleton","point_star","line_star",
                             "mixed_star_union","disconnected_pair","map_dependent",
                             "seeded_mask","delete_all_diagnostic"}<=set(by))
            for z in by.values():
                self.assertTrue(z["independent_exact_sets_agree"])
                self.assertEqual(z["damaged_ordered_endpoints"],4*z["damaged_projections"])
                self.assertLessEqual(z["damaged_ordered_endpoints"],z["deletion_endpoint_bound"])
                self.assertEqual(z["surviving"]+z["deleted"],c["original_flags"])
                self.assertLessEqual(z["D6"],c["full_D6"])
                self.assertLessEqual(z["produced_BBo"],c["full_produced_BBo"])
                self.assertLessEqual(z["smaller_core_produced_BBo"],z["produced_BBo"])
                self.assertLessEqual(6*z["greedy_disjoint_witnesses"],z["surviving"])
            self.assertEqual(by["singleton"]["damaged_ordered_endpoints"],12*c["s"]**2)
            self.assertEqual(by["mixed_star_union"]["deleted"],2*c["s"]+1)

    def test_07_delete_all_is_diagnostic_not_theorem(self):
        for c in self.cert["finite_cases"]:
            z=next(z for z in c["masks"] if z["mask"]=="delete_all_diagnostic")
            self.assertEqual(z["surviving"],0)
            self.assertEqual(z["D6"]+z["produced_BBo"]+z["greedy_disjoint_witnesses"],0)
            self.assertEqual(z["damaged_projections"],
                             ((c["s"]+1)*(c["s"]**2+1))*((c["s"]+1)*(c["s"]**2+1)-(c["s"]+1)))

    def test_08_known_parent_W32_regressions(self):
        c={z["scheme"]:z for z in self.cert["finite_cases"] if z["s"]==2}
        self.assertEqual((c["lex"]["full_D6"],c["lex"]["full_produced_BBo"]),(15,2))
        self.assertEqual((c["reverse"]["full_D6"],c["reverse"]["full_produced_BBo"]),(3,0))
        self.assertEqual((c["correlated"]["full_D6"],c["correlated"]["full_produced_BBo"]),(1,0))

    def test_09_anchor_only_deletion_kills_path_even_with_residual_core(self):
        m=model(2,"lex","full")
        A=frozenset(range(len(m["flags"])))
        all_b=source_first_bbo(m,A)
        ids=next(iter(all_b))
        f=[m["flags"][i] for i in ids]
        p=next(p for p,n in Counter(p for p,l in f).items() if n==2)
        l=next(l for l,n in Counter(l for p,l in f).items() if n==2)
        anchor={i for i in ids if p==m["flags"][i][0] or l==m["flags"][i][1]}
        middle=m["flag_to_id"][p,l];C=frozenset(set(ids)-anchor)
        self.assertEqual(len(anchor),3);self.assertEqual(len(C),3)
        self.assertIn(ids,physical_bbo(m,A,C))
        self.assertNotIn(ids,physical_bbo(m,A-{middle},C))
        self.assertNotIn(ids,source_first_bbo(m,A-{middle},C))

    def test_10_packing_and_independent_event_probability(self):
        for z in self.cert["formal_ledgers"]:
            s=1<<z["sufficient_h0"];rho=Q(z["rho"])
            m=int(z["packing_at_formal_h0"])
            self.assertLessEqual(6*(m-1),rho*s**4)
            self.assertGreater(6*m,rho*s**4)
            self.assertEqual(Q(z["independent_collision_probability_lower"]),Q(5175,51**6))
            self.assertEqual(Q(z["independent_collision_tail_exponent_per_witness"]),Q(5175,8*51**6))
        k=(0,1,2,3,4,5);j=(6,7,8,9,10,11)
        self.assertEqual(greedy_pack([k,j]),(k,j))
        self.assertEqual(greedy_pack([k,j],initial_deleted=[0]),(j,))

    def test_11_original_geometry_not_reconstructed_after_deletion(self):
        m=model(2,"lex","full")
        A=frozenset(range(len(m["flags"])))
        Z=frozenset([0,3,7])
        d=source_first_d6(m,A-Z)
        self.assertEqual(d,physical_d6(m,A-Z))
        b=source_first_bbo(m,A-Z)
        self.assertEqual(b,physical_bbo(m,A-Z))
        self.assertTrue(all(set(k).isdisjoint(Z) for k in {*d,*b}))
        self.assertEqual(len(m["projection"]),m["V"]*(m["V"]-m["s"]-1))

    def test_12_scope_no_finite_proof_no_external_acceptance(self):
        self.assertEqual(self.cert["claim"],"RESILIENCE_AND_PACKING_PROOF_CANDIDATE")
        self.assertEqual(self.cert["issue"],791)
        self.assertTrue(self.cert["finite_checks_not_all_order_proof"])
        self.assertFalse(self.cert["general_ASET_exponent"])
        self.assertFalse(self.cert["external_peer_review_received"])
        self.assertEqual({(z["s"],z["scheme"]) for z in self.cert["finite_cases"]},
            {(2,"lex"),(2,"reverse"),(2,"correlated"),(4,"lex"),(4,"correlated")})


if __name__=="__main__":
    unittest.main()
