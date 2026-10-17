"""AA4-CE: independent tests for original shared physical sixpacket Q coupling."""
import unittest
from collections import Counter
from itertools import combinations
from fractions import Fraction
from hyp105_issue230_d6aa4ce_shared_sixpacket_xor_coupling import (
    N, fwht64, xor_convolution64, autocorrelation64,
    physical_right_mask_for_packets, physical_cross_Q_certificate,
    orientation_of_true_original_Q, source_orientation_histogram_W32,
    shared_sixpacket_W32_certificate, DEFAULT_PACKETS,
)
from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4bq_all_seven_reverse_switching import (
    apply_disjoint_factor_swaps,
)
from hyp105_issue230_d6aa4by_original_independent_2factor_kernel import (
    physical_right_is_six_vertex_two_regular,
)
from hyp105_issue230_d6aa4cb_original_physical_parity_code import syndrome


class AA4CESharedSourceOrientation(unittest.TestCase):
    def test_01_64_integer_Walsh_vs_independent_direct_XOR_convolution(self):
        a=tuple((7*x*x+11*x+13)%199 for x in range(N))
        b=tuple((x*x+5*x+1)%17 for x in range(N))
        self.assertEqual(fwht64(fwht64(a)),tuple(N*v for v in a))
        c=xor_convolution64(a,b)
        literal=tuple(sum(a[t]*b[x^t] for t in range(N)) for x in range(N))
        self.assertEqual(c,literal)
        impulse=tuple(int(x==19) for x in range(N))
        self.assertEqual(xor_convolution64(impulse,b),
                         tuple(b[x^19] for x in range(N)))
        for bad in (tuple([0]*63),tuple([0]*63+[-1])):
            with self.assertRaises(ValueError):xor_convolution64(bad,b)
        with self.assertRaises(ValueError):fwht64((1.0,)*N)

    def test_02_independent_physical_K6_translations_and_pair_autocorrelation(self):
        full=tuple(combinations(range(6),2))
        base=tuple((i,(i+1)%6) for i in range(6))
        occupied={tuple(sorted(z)) for z in base}
        alternate=tuple(z for z in full if z not in occupied)[:6]
        chosen=tuple((base[i],alternate[i]) for i in range(6))
        # Six actual pairs of distinct original physical unordered images.
        # One complete 12-edge globally injected image map is used.
        g=tuple(z for pair in chosen for z in pair)
        pairs=DEFAULT_PACKETS
        z=physical_right_mask_for_packets(g,pairs)
        R=z["mask"]
        self.assertEqual(R[0],1)
        self.assertGreaterEqual(z["rank"],2)
        self.assertEqual(len(set(g)),12)
        direct_ac=tuple(sum(R[x]*R[x^d] for x in range(N))
                        for d in range(N))
        self.assertEqual(autocorrelation64(R),direct_ac)
        for t,u in ((0,0),(1,12),(7,42),(63,16)):
            c=physical_cross_Q_certificate(R,t,u,z["columns"])
            literal=sum(R[x^t]*R[x^u] for x in range(N))
            self.assertEqual(c["joint_possible_complete_right_maps"],literal)
            self.assertEqual(c["joint_physical_probability"],Fraction(literal,N))
            if syndrome(z["columns"],t^u):
                self.assertEqual(literal,0)
        # Independently reconstruct all 64 2factor masks after xor translation:
        for t in (1,3,13,32,63):
            for x in range(N):
                edges=tuple(chosen[i][((x^t)>>i)&1] for i in range(6))
                degree=Counter(v for edge in edges for v in edge)
                physical=int(len(degree)==6 and all(d==2 for d in degree.values()))
                self.assertEqual(physical,R[x^t])

    def test_03_real_original_W32_full_sixflag_Q_one_global_g(self):
        for scheme,expected_Q,expected_rank in (
            ("lex",351,4),("S72",301,5)
        ):
            model=fixture(1,scheme)
            z=shared_sixpacket_W32_certificate(
                model,DEFAULT_PACKETS,verify_all_Q=True)
            self.assertEqual(z["original_s"],2)
            self.assertEqual(z["original_source_Q_count"],expected_Q)
            self.assertEqual(z["global_right_parity_rank"],expected_rank)
            self.assertEqual(sum(z["source_histogram_H"]),z["source_total_weight"])
            self.assertEqual(z["uniform_mean_B"],z["expected_mean_B"])
            self.assertEqual(z["pair_autocorrelation"][0],
                             z["right_physical_active_states"])
            self.assertEqual(len(z["xor_convolution_upper_B"]),64)
            self.assertEqual(z["xor_convolution_upper_B"][0],
                             z["center_physical_upper_B0"])
            self.assertEqual(z["uniform_second_moment_B"],
                             Fraction(sum(x*x for x in z["xor_convolution_upper_B"]),64))
            score=z["true_original_six_touch_weighted_GF5_scores"]
            self.assertTrue(all(0<=v<=z["xor_convolution_upper_B"][i]
                                for i,v in enumerate(score)))
            if scheme=="lex":
                self.assertEqual(z["right_physical_active_states"],0)
                self.assertEqual(z["xor_convolution_upper_B"],(0,)*64)
            else:
                self.assertGreater(z["right_physical_active_states"],0)
                self.assertGreater(sum(z["xor_convolution_upper_B"]),0)
            print("AA4CE_ORIGINAL",scheme,"Q",expected_Q,"rank",
                  expected_rank,"R_active",z["right_physical_active_states"],
                  "H_total",z["source_total_weight"],
                  "orientations",sum(bool(x) for x in z["source_histogram_H"]),
                  "nonzero_syndrome_groups",len(z["weighted_source_parity_groups"]),
                  "B0",z["center_physical_upper_B0"],
                  "B_mean",z["uniform_mean_B"],
                  "B2",z["uniform_second_moment_B"],flush=True)

    def test_04_source_H_independent_of_global_g_and_bad_source_rejected(self):
        model=fixture(1,"S72")
        original=source_orientation_histogram_W32(model,DEFAULT_PACKETS)
        changed=dict(model,right_labels=tuple(reversed(model["right_labels"])))
        altered=source_orientation_histogram_W32(changed,DEFAULT_PACKETS)
        self.assertEqual(original["orientation_mass"],altered["orientation_mass"])
        self.assertEqual(original["source_Q"],altered["source_Q"])
        s,V,a,inc,f,g,_,_=_original_source(model)
        oneQ=original["source_Q"][0][0]
        t=orientation_of_true_original_Q(oneQ,inc,DEFAULT_PACKETS,V)
        self.assertIn(t,range(64))
        with self.assertRaises(ValueError):
            orientation_of_true_original_Q(oneQ,inc,DEFAULT_PACKETS[:5],V)
        with self.assertRaises(ValueError):
            orientation_of_true_original_Q(oneQ,inc,
                ((0,1),(1,2),(3,4),(5,6),(7,8),(9,10)),V)
        bad_g=list(g);bad_g[0]=bad_g[1]
        with self.assertRaises(ValueError):
            physical_right_mask_for_packets(bad_g,DEFAULT_PACKETS)
        with self.assertRaises(ValueError):
            physical_right_mask_for_packets(g,DEFAULT_PACKETS[:5])

if __name__=="__main__":
    unittest.main()
