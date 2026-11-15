"""Independent exact full-original W32 adversarial physical-tail falsifiers."""
from fractions import Fraction
import unittest
from hyp105_original_adversarial_B75_referee import (
    IDENTITY,REVERSE,_initial_labelings
)
from hyp105_original_full_w34_weighted_risk_referee import _source
from hyp105_original_pathwise_corner_charge_referee import (
    _physical_original_pathwise_charges
)
from hyp105_original_heavy_tail_adversarial_frontier_referee import (
    SCHEMA,STATUS,SEED,B75,THRESHOLDS,T,MESH,
    _genuine_original_complete_W32,_fast_original_degree_proxy_tail,
    _exact_genuine_original_tail,_deterministic_frontier,
)


class TestOriginalAdversarialPhysicalHeavyTail(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # One deterministic deliberately small additional CI scan, while
        # strict specialist JSON runs the full declared finite search.
        cls.report=_deterministic_frontier(trials=40,seed=SEED,shortlist=2)

    def test_scope_and_explicit_all_h_root_firewall(self):
        r=self.report
        self.assertEqual(r["schema"],SCHEMA)
        self.assertEqual(r["status"],STATUS)
        self.assertEqual(r["issue"],230)
        self.assertTrue(r["all_h_exact_original_layer_cake_tail_identity_proved"])
        self.assertTrue(r["all_h_finite_mesh_original_tail_sandwich_proved"])
        self.assertFalse(r["all_h_universal_P_2_over_3_below_quarter_PROVED"])
        self.assertFalse(r["all_h_original_B75_proved"])
        self.assertFalse(r["root_seven_six_motif_Omega_s6_PROVED"])
        self.assertFalse(r["ASET_exponent_claimed"])
        self.assertTrue(r["original_f_and_g_each_permute_all_15_pairs"])
        self.assertGreaterEqual(r["finite_float_only_proposals"],35)
        self.assertTrue(r["finite_search_nonproof_for_all_h"])

    def test_original_full_W32_true_physical_graph_two_separate_pair_bijections(self):
        c=_genuine_original_complete_W32(IDENTITY,REVERSE)
        parent=_source(2,"reverse","full")
        self.assertEqual(c["flags"],parent["flags"])
        self.assertEqual(c["f"],parent["f"])
        self.assertEqual(c["g"],parent["g"])
        self.assertEqual(c["ids"],parent["ids"])
        self.assertEqual(c["J"],parent["J"])
        self.assertEqual(c["owner"],parent["owner"])
        self.assertEqual(c["adj"],parent["adj"])
        self.assertEqual(len(c["flags"]),45)
        self.assertEqual(len(c["owner"]),90)
        self.assertEqual(len(set(c["f"])),15)
        self.assertEqual(len(set(c["g"])),15)

    def test_true_original_full_source_lex_reverse_frozen_exact_fraction(self):
        row=_exact_genuine_original_tail(IDENTITY,REVERSE)
        self.assertEqual(row["true_original_coordinate_proper_P3s"],1154)
        self.assertEqual(Fraction(row["exact_original_B_over_M"]),
                         Fraction(2197221736032,6861627242215))
        self.assertEqual(Fraction(row["exact_original_weighted_tail_P_2_over_3"]),
                         Fraction(816966722907,6861627242215))
        self.assertTrue(row["complete_true_original_source_not_sampling"])
        self.assertTrue(row["genuine_original_W32"])
        self.assertFalse(row["root_PROVED_A"])

    def test_finite_adversarial_exact_candidate_consistency_and_bounds(self):
        r=self.report
        x=r["exact_fraction_true_source_candidates"]
        self.assertGreaterEqual(len(x),2)
        for q in x:
            M=Fraction(q["exact_original_M"])
            G=Fraction(q["exact_original_G"])
            B=Fraction(q["exact_original_B"])
            P0=Fraction(q["exact_original_weighted_tail_P_0"])
            P1=Fraction(q["exact_original_weighted_tail_P_1_over_2"])
            P2=Fraction(q["exact_original_weighted_tail_P_2_over_3"])
            P3=Fraction(q["exact_original_weighted_tail_P_3_over_4"])
            L=Fraction(q["exact_original_tail_mesh32_lower"])
            U=Fraction(q["exact_original_tail_mesh32_upper"])
            self.assertTrue(M>0 and G>0 and B>=0 and M==G+B)
            self.assertEqual(q["named_original_flags"],45)
            self.assertEqual(q["owned_actual_physical_opposite_diagonals"],90)
            self.assertTrue(1>=P0>=P1>=P2>=P3>=0)
            self.assertEqual(Fraction(q["exact_original_tail_LayerCake_equals_B_over_M"]),B/M)
            self.assertTrue(0<=L<=B/M<=U<=1)
            self.assertLessEqual(U-L,Fraction(1,MESH))
            self.assertEqual(q["fixed_source_violates_auxiliary_P_2_over_3_below_1_over_4"],
                             P2>=Fraction(1,4))
            self.assertEqual(q["fixed_source_violates_global_B75"],B/M>=B75)
            self.assertEqual(len(set(q["f_pair_perm_indices"])),15)
            self.assertEqual(len(set(q["g_pair_perm_indices"])),15)
            self.assertFalse(q["root_PROVED_A"])

    def test_strict_adversarial_proxy_not_mislabeled_exact_priority(self):
        # Independent actual physical graph with pointwise FLOAT product
        # used ONLY as a proposal ranking, not to accept any tail theorem.
        z=_fast_original_degree_proxy_tail(IDENTITY,REVERSE)
        self.assertGreater(z["nonproof_float_proxy_P_2_over_3"],0)
        self.assertEqual(z["actual_original_P3_count"],1154)
        self.assertLess(z["nonproof_float_proxy_B_over_M"],1)

    def test_layer_cake_exact_from_abstract_two_atom_weighted_distribution(self):
        # Abstract positive-cone model, NOT a claim to be ORIGINAL GQ:
        # P_2/3>=1/4 does NOT imply B/M>=3/4.
        rows=[(Fraction(7,10),Fraction(2,5)),
              (Fraction(0),Fraction(3,5))]
        risk=sum((r*mass for r,mass in rows),Fraction(0))
        self.assertEqual(risk,Fraction(7,25))
        P23=sum((mass for r,mass in rows if r>Fraction(2,3)),Fraction(0))
        self.assertEqual(P23,Fraction(2,5))
        self.assertGreater(P23,Fraction(1,4))
        self.assertLess(risk,Fraction(3,4))
        grid=tuple(Fraction(k,MESH) for k in range(MESH+1))
        Pt={t:sum((mass for r,mass in rows if r>t),Fraction(0)) for t in grid}
        lower=sum((Pt[grid[k+1]] for k in range(MESH)),Fraction(0))/MESH
        upper=sum((Pt[grid[k]] for k in range(MESH)),Fraction(0))/MESH
        self.assertLessEqual(lower,risk)
        self.assertLessEqual(risk,upper)
        self.assertLessEqual(upper-lower,Fraction(1,MESH))

    def test_all_h_finite_mesh_sandwich_special_case_ATOMS(self):
        # Mixture of finite rational genuine-independent PRIORITY outcomes,
        # no original source claims; exact layer cake verifies the theorem.
        atoms=[(Fraction(1,2),Fraction(1,2)),
               (Fraction(1,3),Fraction(1,3)),
               (Fraction(0),Fraction(1,6))]
        M=sum((mass for _,mass in atoms),Fraction(0))
        self.assertEqual(M,1)
        exact=sum((r*mass for r,mass in atoms),Fraction(0))
        for n in (2,3,5,8,32):
            t=[Fraction(k,n) for k in range(n+1)]
            tail=lambda x:sum((v for r,v in atoms if r>x),Fraction(0))
            low=sum((tail(t[k+1]) for k in range(n)),Fraction(0))/n
            high=sum((tail(t[k]) for k in range(n)),Fraction(0))/n
            self.assertLessEqual(low,exact)
            self.assertLessEqual(exact,high)
            self.assertLessEqual(high-low,Fraction(1,n))


if __name__=="__main__":
    unittest.main()
