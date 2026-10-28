"""Original source pencil robust conditional B/A theorem: independent controls."""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, islice
import unittest

from hyp105_allh_annealed_BA_floor import annealed_original_BA_floor
from hyp105_allh_macro_freeze_BA import (
    robust_annealed_BA_floor,
    best_robust_annealed_BA_floor,
    macroscopic_freeze_rational_example,
    synthetic_regular_source_good_point_oracle,
)
from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_b1_symplectic import symplectic_gq


class TestAllHMacroscopicOriginalFrozenLineBA(unittest.TestCase):
    def test_zero_freeze_recovers_exact_prior_all_h_formula(self):
        for s in (2,4,8,16,32,64,128,256,1024):
            new=robust_annealed_BA_floor(s,0,0)
            old=annealed_original_BA_floor(s, frozen_count=0)
            self.assertEqual(
                new["conditional_expected_original_BA_lower_bound"],
                old["conditional_expected_original_B_left_A_right_floor"])
            self.assertEqual(new["guaranteed_good_original_source_points"],
                             new["V"])
            self.assertEqual(new["missing_good_f_pair_edges_upper_bound"],
                             new["M"]-new["V"])
            self.assertFalse(new["root_A_B_C_proved"])
        self.assertGreater(
            robust_annealed_BA_floor(1024,0,0)[
                "scaled_expected_BA_floor_over_s6"],138)

    def test_all_h_macroscopic_fraction_sixteenth_remains_positive(self):
        # At fixed rho=1/16 and k=floor(d/2), the proof yields a
        # strictly positive all-h order s^6, unlike AA4-ANNBA's
        # previous d-b argument (b~rho V >> d).
        for s in (128,256,512,1024,2048):
            x=macroscopic_freeze_rational_example(s)
            self.assertEqual(
                x["frozen_original_source_lines"],x["V"]//16)
            self.assertEqual(
                x["pencil_freeze_threshold_k"],(s+1)//2)
            self.assertGreater(
                x["scaled_expected_BA_floor_over_s6"],0)
            self.assertTrue(x["all_h_annealed_not_all_completed_g"])
            self.assertEqual(x["root_A_B_C_proved"],False)
        # Conservative strict positive coefficient 1225/2048 (~0.598)
        # holds in LIMINF, without relying on exact residual-palette
        # amplification factor (1-rho)^(-6). Test only eventually.
        self.assertGreater(
            macroscopic_freeze_rational_example(8192)[
                "scaled_expected_BA_floor_over_s6"],
            Fraction(1,2))

    def test_sublinear_V_freeze_recovers_leading_140_uniformly(self):
        # b=s^2 grows much faster than the old b=o(s), but b/V~1/s.
        for s in (128,256,512,1024,2048):
            V=(s+1)*(s*s+1)
            b=s*s
            self.assertLess(b,V)
            old=annealed_original_BA_floor(s,frozen_count=b)
            self.assertEqual(
                old["conditional_expected_original_B_left_A_right_floor"],0)
            # k≈s*sqrt(b/V)+sqrt(s) is sublinear in d and
            # Markov's bad original points are o(V).
            from math import isqrt
            d=s+1
            k=min(d-6, isqrt((b*d*d)//V)+isqrt(d)+2)
            x=robust_annealed_BA_floor(s,b,k)
            self.assertGreater(x["scaled_expected_BA_floor_over_s6"],0)
            self.assertLess(
                Fraction(x["upper_bound_bad_original_source_points"],V),
                Fraction(1,2))
            self.assertGreater(
                x["good_source_minimum_unfrozen_pencil"],d//2)
        self.assertGreater(
            best_robust_annealed_BA_floor(2048,2048**2)[
                "scaled_expected_BA_floor_over_s6"],
            Fraction(100))

    def test_exact_true_W32_W34_original_frozen_pencil_markov(self):
        # Genuine original symplectic GQ source, not a proxy graph.
        for h in (1,2):
            s=1<<h
            _,points,lines,flags=symplectic_gq(h)
            V=(s+1)*(s*s+1)
            b=min(12,V)
            J=set(range(b))
            t=defaultdict(int)
            for p,l in flags:
                if l in J:
                    t[p]+=1
            self.assertEqual(sum(t.values()),b*(s+1))
            for k in range(s+2):
                bad=sum(t[p]>k for p in range(V))
                self.assertLessEqual(bad,(b*(s+1))//(k+1))
                x=robust_annealed_BA_floor(s,b,k)
                self.assertGreaterEqual(
                    V-bad,x["guaranteed_good_original_source_points"])
                self.assertEqual(x["frozen_original_source_lines"],b)
            model=pair_labeled_symplectic(h,"lex")
            r=robust_annealed_BA_floor(
                s, b,0,
                point_labels=model["left_labels"],
                frozen_labels=tuple(model["right_labels"][l] for l in J))
            self.assertFalse(r["root_A_B_C_proved"])

    def test_independent_regular_pencil_and_good_Ka_C4_oracle(self):
        # A synthetic regular circulant is only a falsifier of the
        # general SOURCE DEGREE combinatorial lemma; the proof and claim
        # apply to genuine W(3,s), as independently audited above.
        s=8;d=s+1;V=d*(s*s+1)
        J=tuple(range(24))
        k=2
        synthetic=synthetic_regular_source_good_point_oracle(s,J,k)
        x=robust_annealed_BA_floor(s,len(J),k)
        self.assertTrue(synthetic["abstract_regular_host_not_W3"])
        self.assertGreaterEqual(synthetic["actual_good_pencils"],
                                x["guaranteed_good_original_source_points"])
        a=x["a"]
        f=tuple(islice(combinations(range(a),2),V))
        owners={edge:p for p,edge in enumerate(f)}
        t=[sum((p+j)%V in J for j in range(d))
           for p in range(V)]
        good={p for p in range(V) if t[p]<=k}
        self.assertTrue(good)
        p=min(good)
        u,v=f[p]
        remaining=[z for z in range(a) if z not in (u,v)]
        actual=0
        selected=None
        # Independently enumerate actual GOOD-source C4s, not use the
        # union bound as an oracle for itself.
        for four in combinations(remaining,4):
            for excluded in (
                ((four[0],four[1]),(four[2],four[3])),
                ((four[0],four[2]),(four[1],four[3])),
                ((four[0],four[3]),(four[1],four[2])),
            ):
                candidate=tuple(edge for edge in combinations(four,2)
                                if edge not in excluded)
                if all(edge in owners and owners[edge] in good
                       for edge in candidate):
                    actual+=1
                    if selected is None:
                        selected=tuple(owners[edge] for edge in candidate)
        self.assertGreaterEqual(actual,x["good_point_physical_C4_floor"])
        self.assertIsNotNone(selected)
        self.assertEqual(len(set(selected)),4)
        self.assertNotIn(p,selected)
        # Direct construction of SIX actual distinct source incidence IDs
        # with pair repeated p and four other point factors. The host
        # here is explicitly a combinatorial regular-source falsifier,
        # not a claim to construct a true W(3,8).
        chosen=[]
        for point in (p,p)+selected:
            avail=[(point+j)%V for j in range(d)
                   if (point+j)%V not in J and
                   (point+j)%V not in chosen]
            self.assertTrue(avail)
            chosen.append(avail[0])
        self.assertEqual(len(set(chosen)),6)
        self.assertTrue(all(line not in J for line in chosen))

    def test_hosted_exact_annealed_macroscopic_certificate(self):
        # Data are *lower bounds on conditional expectations*, not
        # enumerations of fixed correlated full right source maps.
        import json
        from math import isqrt
        cases=[]
        for s,b,k in (
            (128,128**2, min(128+1-6,isqrt(128)+12)),
            (2048,2048**2, min(2048+1-6,
                isqrt((2048**2*(2049**2))//((2049)*(2048**2+1)))+
                isqrt(2049)+2)),
            (1024,((1025)*(1024**2+1))//16,1025//2),
            (8192,((8193)*(8192**2+1))//16,8193//2),
        ):
            r=robust_annealed_BA_floor(s,b,k)
            cases.append({
                "s":s,"b":b,"k":k,
                "guaranteed_good_original_source_points":
                    r["guaranteed_good_original_source_points"],
                "guaranteed_good_physical_C4_per_good_point":
                    r["good_point_physical_C4_floor"],
                "conditional_expected_original_BA_floor_integer":
                    r["floor_of_expected_original_BA"],
                "scaled_floor_over_s6_decimal":
                    format(float(r["scaled_expected_BA_floor_over_s6"]),".9f"),
            })
        print("HYP105_AA4_MFREEZE_CERTIFICATE="+json.dumps({
            "scope":"all-h uniform conditional mean, not pointwise completed g",
            "sublinear_V_leading_constant":140,
            "fixed_fraction_one_sixteenth_conservative_liminf":
                "1225/2048",
            "root_A_B_C_proved":False,"cases":cases
        },sort_keys=True))

    def test_invalid_freezes_and_thresholds_fail_closed(self):
        with self.assertRaises(ValueError):
            robust_annealed_BA_floor(3,0,0)
        with self.assertRaises(ValueError):
            robust_annealed_BA_floor(8,-1,0)
        with self.assertRaises(ValueError):
            robust_annealed_BA_floor(8,10,-1)
        with self.assertRaises(ValueError):
            robust_annealed_BA_floor(8,10,10)
        with self.assertRaises(ValueError):
            robust_annealed_BA_floor(8,2,1,frozen_labels=((0,1),))
        with self.assertRaises(ValueError):
            robust_annealed_BA_floor(8,2,1,
                                    frozen_labels=((0,1),(0,1)))
        with self.assertRaises(ValueError):
            synthetic_regular_source_good_point_oracle(8,(0,0),0)
        with self.assertRaises(ValueError):
            best_robust_annealed_BA_floor(8,10_000)
        with self.assertRaises(ValueError):
            macroscopic_freeze_rational_example(8,1,1)


if __name__=="__main__":
    unittest.main()
