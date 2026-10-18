"""Independent AA4-CK exact original dual swap spectrum and original W32/W34/W38."""
import unittest
from collections import Counter
from fractions import Fraction

from hyp105_issue230_d6aa4ck_dual_cycle_transposition_spectral_energy import (
    N,DEGREE,TRANSPOSITIONS,ADJACENCY,CANONICAL_CYCLES,
    CYCLE_INDEX,transposed_original_dual,_cycle_from_order,
    exact_original_sixcycle_spectrum_certificate,
    exact_GF5_sixcycle_histogram_energy,
    original_true_sixpoint_fiber_spectral_energy,
    independent_original_GF5_full_factor_transposition_oracle,
    original_allh_maximal_named_D6_fan_energy,
)
from hyp105_issue230_d6aa4ci_dual_cycle_orbit_fiber_invariant import (
    original_B_C_D6_mixed_fixture,SIX_CYCLE,
)
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1b0_seven_signature import R3_CERTIFIED_FLOORS

W_D=R3_CERTIFIED_FLOORS["D6"]


class AA4CKTrueOriginalSpectralEnergy(unittest.TestCase):
    def test_01_integer_60cycle_spectral_polynomial_traces_and_sharp_real_extremizers(self):
        """60x60 exact P(A)=0 integer certificate and five trace powers.

        Abstract spectral sharpness checked by explicitly constructing
        5- and (-9)-adjacency eigenvectors via exact integer powers of
        the verified graph, not by applying floating-point eigensolvers.
        """
        c=exact_original_sixcycle_spectrum_certificate()
        self.assertEqual(c["adjacency_eigenvalues"],(15,5,0,-3,-9))
        self.assertEqual(c["eigen_multiplicities"],(1,18,16,20,5))
        self.assertEqual(c["laplacian_eigenvalues"],(0,10,15,18,24))
        self.assertEqual(c["integer_power_traces"],(60,0,1260,1440,96300))
        self.assertEqual(c["sharp_abstract_Adirichlet_ratio_bounds"],
                         (Fraction(4,3),Fraction(16,5)))
        self.assertEqual(c["sharp_abstract_centered_averaging_L2_operator_norm"],
                         Fraction(3,5))
        self.assertTrue(c["exact_integer_annihilating_polynomial_zero"])
        self.assertEqual(len(CANONICAL_CYCLES),60)
        self.assertEqual(sum(sum(row) for row in ADJACENCY),900)
        self.assertTrue(all(ADJACENCY[i][j]==ADJACENCY[j][i]
                            for i in range(N) for j in range(N)))
        self.assertEqual(sum(x*x for row in ADJACENCY for x in row),1260)
        # Independent literal combinatorial transposition on all 900
        # (C,tau) source column arrangements.
        overlap=Counter()
        seen_orbit=Counter()
        for k,c0 in enumerate(CANONICAL_CYCLES):
            outputs=Counter()
            for i,j in TRANSPOSITIONS:
                outcome=frozenset(frozenset(
                    j if v==i else i if v==j else v for v in e
                ) for e in c0)
                outputs[outcome]+=1
                self.assertNotEqual(outcome,c0)
                overlap[len(outcome&c0)]+=1
            self.assertEqual(dict(outputs),{
                c1:ADJACENCY[k][CYCLE_INDEX[c1]]
                for c1 in CANONICAL_CYCLES if ADJACENCY[k][CYCLE_INDEX[c1]]
            })
            self.assertEqual(len(outputs),12)
            self.assertEqual(Counter(outputs.values()),Counter({1:9,2:3}))
        self.assertEqual(overlap,Counter({4:720,2:180}))
        # Guard a negative and a degenerate H, no fabricated GF5.
        zero=exact_GF5_sixcycle_histogram_energy({},0)
        self.assertEqual(zero["exact_original_f_orbit_variance"],0)
        self.assertEqual(zero["exact_original_single_full_POINT_swap_mean_squared_GF5_delta"],0)
        for invalid in ({123:1},{CANONICAL_CYCLES[0]:-1}):
            with self.assertRaises(ValueError):
                exact_GF5_sixcycle_histogram_energy(invalid)
        with self.assertRaises(ValueError):
            exact_GF5_sixcycle_histogram_energy({},-1)
        with self.assertRaises(ValueError):
            transposed_original_dual(CANONICAL_CYCLES[0],0,0)
        with self.assertRaises(ValueError):
            _cycle_from_order((0,1,2,3,4,4))
        print("AA4CK_INTEGER_EXACT_SPECTRAL_CERTIFICATE",c,flush=True)

    def test_02_original_W32_lex_S72_full900_real_SOURCE_point_swaps(self):
        for scheme in ("lex","S72"):
            model=fixture(1,scheme)
            s,V,a,inc,f,g,_,_=_original_source(model)
            inv={tuple(e):i for i,e in enumerate(f)}
            points=tuple(inv[e] for e in SIX_CYCLE)
            c=independent_original_GF5_full_factor_transposition_oracle(model,points)
            self.assertEqual((c["s"],c["V"],c["a"]),(2,15,6))
            self.assertEqual(c["real_original_Q_in_fiber"],3**6)
            self.assertEqual(c["900_real_original_global_POINT_swaps_verified"],900)
            self.assertGreater(c["physically_right_eligible_original_Q"],0)
            cert=c["exact_spectral_certificate"]
            self.assertGreater(cert["exact_original_f_orbit_variance"],0)
            print("AA4CK_ORIGINAL_W32",scheme,
                "Q_right",c["physically_right_eligible_original_Q"],
                "variance",str(cert["exact_original_f_orbit_variance"]),
                "energy",str(c["actual_original_GF5_exact_energy"]),flush=True)

    def test_03_true_original_W34_rightBC_D6_900global_swaps(self):
        model,points,source=original_B_C_D6_mixed_fixture(2)
        z=independent_original_GF5_full_factor_transposition_oracle(model,points)
        self.assertEqual((z["s"],z["V"],z["a"]),(4,85,14))
        self.assertEqual(z["real_original_Q_in_fiber"],5**6)
        self.assertEqual(z["900_real_original_global_POINT_swaps_verified"],900)
        stat=z["exact_spectral_certificate"]
        self.assertEqual(stat["weighted_invariant_B_C_baseline"],403560)
        self.assertEqual(stat["histogram_original_sixflag_total"],1)
        self.assertEqual(stat["fixed_original_right_histogram_support"],1)
        self.assertEqual(stat["exact_original_f_orbit_variance"],
                         Fraction(59,3600)*W_D*W_D)
        self.assertEqual(stat["exact_original_single_full_POINT_swap_mean_squared_GF5_delta"],
                         Fraction(W_D*W_D,30))
        self.assertEqual(stat["exact_single_swap_averaging_variance"]<=
                         Fraction(9,25)*stat["exact_original_f_orbit_variance"],True)
        print("AA4CK_TRUE_W34","variance",str(stat["exact_original_f_orbit_variance"]),
              "energy",str(z["actual_original_GF5_exact_energy"]),
              "L2average",str(stat["exact_single_swap_averaging_variance"]),flush=True)

    def test_04_true_original_W38_and_allh_D6_fan_exact_energy(self):
        model,points,source=original_B_C_D6_mixed_fixture(3)
        z=independent_original_GF5_full_factor_transposition_oracle(model,points)
        self.assertEqual((z["s"],z["V"]),(8,585))
        self.assertEqual(z["real_original_Q_in_fiber"],9**6)
        self.assertEqual(z["900_real_original_global_POINT_swaps_verified"],900)
        stat=z["exact_spectral_certificate"]
        self.assertEqual(stat["weighted_invariant_B_C_baseline"],1087560)
        self.assertEqual(stat["histogram_original_sixflag_total"],32)
        self.assertEqual(stat["fixed_original_right_histogram_support"],13)
        self.assertGreater(stat["exact_original_f_orbit_variance"],0)
        self.assertGreater(stat["exact_original_single_full_POINT_swap_mean_squared_GF5_delta"],0)
        for h in (2,3):
            fan=original_allh_maximal_named_D6_fan_energy(h)
            m=(1<<h)+1
            self.assertEqual(fan["named_genuine_original_Q_count"],m)
            self.assertEqual(fan["symbolic_exact_orbit_variance"],
                             Fraction(59*W_D*W_D*m*m,3600))
            self.assertEqual(fan["symbolic_exact_single_global_POINT_swap_mean_squared_GF5_delta"],
                             Fraction(W_D*W_D*m*m,30))
            self.assertEqual(fan["squared_energy_to_variance_ratio"],Fraction(120,59))
        print("AA4CK_TRUE_W38","variance",str(stat["exact_original_f_orbit_variance"]),
              "energy",str(z["actual_original_GF5_exact_energy"]),
              "L2average",str(stat["exact_single_swap_averaging_variance"]),
              "fan_ratio",str(Fraction(120,59)),flush=True)


if __name__=="__main__":
    unittest.main()
