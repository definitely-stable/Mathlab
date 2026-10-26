"""AA4-CWNO: packed coherent-return C6 completion no-go and true W34 template."""
import json
from math import comb, isqrt
import unittest

from hyp105_coherent_wedge_completion_obstruction import (
    coherent_packet_completion_lower,
    protected_three_hub_source_witness_w34,
)
from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked
from hyp105_b1_symplectic import symplectic_gq
from hyp105_physical_degree_energy import minimal_alphabet


class TestCoherentWedgeCompletionNoGo(unittest.TestCase):
    def test_all_k_packed_subfield_constants_exact_integers(self):
        # No huge geometry is constructed here. These test the all-h
        # inequalities used AFTER PR #651's infinite existence lemma,
        # including very large k where an O(sqrt V) search is impossible.
        for k in (4,5,6,8,10,16,32,64,128):
            with self.subTest(k=k):
                x=coherent_packet_completion_lower(k)
                t=x["t"]
                s=x["s"]
                n=x["n"]
                e=x["e"]
                d=x["d"]
                R=x["R"]
                self.assertGreaterEqual(R,3)
                self.assertGreaterEqual(512*R,n)
                self.assertGreaterEqual(8*e,5*e)
                self.assertGreaterEqual(5*d,8)
                self.assertGreaterEqual(5*e,4*e)
                self.assertGreaterEqual(
                    x["W2x_lower_numerator"] * (2**33),
                    x["W2x_lower_denominator"] * t**18
                )
                self.assertLessEqual(
                    x["universal_Jx_spectral_integer_upper"],
                    x["universal_Jx_coarse_upper"]
                )
                self.assertEqual(x["universal_Jx_coarse_upper"],9*s**4)
                # The target universal mean O(s^2) cannot follow
                # from the pair of opposite asymptotic inequalities.
                self.assertGreaterEqual(
                    x["mean_comp_lower_numerator"] * 9*(2**33),
                    x["mean_comp_lower_denominator"] * s**5
                )
                self.assertTrue(
                    x["all_h_mean_O_s2_falsified_conditional_on_PR651_packing"]
                )
                self.assertFalse(x["pr651_packing_independently_reproved_here"])
                self.assertFalse(x["root_GF5_sevenclass_disproved"])

    def test_true_w34_protected_genuine_incidence_returning_template(self):
        witness=protected_three_hub_source_witness_w34()
        self.assertEqual((witness["s"],witness["V"],witness["a"]),
                         (4,85,14))
        self.assertGreaterEqual(
            witness["actual_kernel_completion_count_at_hub0"],2
        )
        self.assertEqual(len(witness["protected_cycles"]),2)
        self.assertEqual(
            len({frozenset(ids) for ids in
                 witness["six_actual_original_source_flag_IDs_per_cycle"]}),
            2
        )
        _,_,_,flags=symplectic_gq(2)
        f=[None]*85
        g=[None]*85
        from itertools import combinations
        for j,(p,q,l1,l2,l3) in enumerate(
                witness["protected_source_packets"]):
            f[p]=(j,3)
            f[q]=(j,4)
            g[l1]=(j,5)
            g[l2]=(j,6)
            g[l3]=(j,7)
        pairs=list(combinations(range(14),2))
        for labels in (f,g):
            existing={z for z in labels if z is not None}
            missing=iter(edge for edge in pairs if edge not in existing)
            for k in range(85):
                if labels[k] is None:
                    labels[k]=next(missing)
        for ids in witness["six_actual_original_source_flag_IDs_per_cycle"]:
            self.assertEqual(len(set(ids)),6)
            self.assertIsNone(
                classify_seven_prechecked(tuple(sorted(ids)),f,g,flags)
            )
        self.assertTrue(
            witness["both_protected_cycles_have_six_distinct_original_flags"]
        )
        self.assertFalse(witness["root_sevenclass_disproved"])
        self.assertFalse(witness["infinite_subfield_packing_instantiated"])

    def test_lower_bound_strengthens_quintic_mean(self):
        previous=None
        for k in (4,5,6,7,8,10):
            x=coherent_packet_completion_lower(k)
            # certificate mean/s^2 lower diverges along dyadic widths.
            ratio=x["mean_comp_lower_numerator"] / (
                x["mean_comp_lower_denominator"]*x["s"]**2
            )
            if previous is not None:
                self.assertGreater(ratio,previous)
            previous=ratio

    def test_reject_inadmissible_subfield_widths(self):
        for k in (0,1,2,3,-1,4.0,True):
            with self.subTest(k=k),self.assertRaises(ValueError):
                coherent_packet_completion_lower(k)
        self.assertEqual(
            coherent_packet_completion_lower(4)["a"],
            minimal_alphabet((257)*(256**2+1)),
        )


if __name__=="__main__":
    unittest.main()
