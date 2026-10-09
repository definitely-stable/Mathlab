"""HYP-105 E2-B1: independent exact GF5 signed energy/flow cross-oracles."""
from fractions import Fraction
from itertools import combinations, product
import unittest

from hyp105_g5e2b1_energy import (
    DEFAULT_PALETTE, add_gf5_vectors, checked_palette,
    disjoint_energy_mobius, risk_from_energy_finite,
    risk_from_pair_energy, single_signed_trade_mitm,
    vector_for_support,
)
from hyp105_g5e0_boundary_flows import exact_nonzero_trade_flow
from hyp105_g5d_affine_weights import w32_supports
from hyp105_g5c2_density import collision_spectrum, w32_columns


def real_unit_trade(k):
    """Find genuine signed orientations by independently adding GF5 vectors."""
    conflicts = collision_spectrum(w32_columns())[0 if k==2 else 1]
    ids = [i for i in range(45) if conflicts[0] & (1<<i)]
    assert len(ids) == 2*k
    columns=w32_columns()
    for plus in combinations(ids,k):
        minus=tuple(i for i in ids if i not in plus)
        if all(sum(columns[i][j] for i in plus)%5 ==
               sum(columns[i][j] for i in minus)%5
               for j in range(12)):
            supports=w32_supports()
            return tuple(supports[i] for i in plus+minus), (1,)*k+(-1,)*k
    raise AssertionError("published W32 minimal t4/t6 trade has no true orientation")


def direct_disjoint_moment(histograms,k):
    """Completely independent O(#k-tuples^2) exact weighted matching sum."""
    total=0
    tuples=list(histograms.items())
    for i,(a,ha) in enumerate(tuples):
        for b,hb in tuples[i+1:]:
            if set(a).isdisjoint(b):
                total+=sum(c*hb.get(sig,0) for sig,c in ha.items())
    return total


class E2B1ExactAdditiveEnergyTests(unittest.TestCase):
    def test_general_mobius_inversion_exhaustive_small_synthetic(self):
        # Trivial exact signature distributions deliberately have huge
        # intersections, repeated sum values, and nonuniform multiplicities.
        for k in (2,3):
            for n in (2*k, 2*k+1):
                hist={}
                for subset in combinations(range(n),k):
                    hist[subset] = {
                        bytes([sum(subset)%3]):sum(subset)+1,
                        bytes([3]):2,
                    }
                self.assertEqual(disjoint_energy_mobius(hist,k),
                                 direct_disjoint_moment(hist,k))
        with self.assertRaises(ValueError):
            disjoint_energy_mobius({(0,0):{b"a":1}},2)
        with self.assertRaises(ValueError):
            disjoint_energy_mobius({(0,1):{b"a":-1}},2)
        with self.assertRaises(ValueError):
            disjoint_energy_mobius({},4)

    def test_real_full_51_palette_R2_agrees_with_all_three_flow_events(self):
        s, signs=real_unit_trade(2)
        result=risk_from_pair_energy(s,12)
        self.assertEqual(result["n"],4)
        self.assertEqual(result["local_weighted_pair_samples"],6*51**2)
        self.assertGreater(result["R2"],0)
        independent_sum=Fraction(0)
        # 4 distinct columns have exactly 3 unordered 2-vs-2 partitions.
        ids=tuple(range(4))
        events=0
        for a in combinations(ids,2):
            b=tuple(i for i in ids if i not in a)
            if a>=b:
                continue
            picked=tuple(s[i] for i in a+b)
            f=exact_nonzero_trade_flow(picked,(1,1,-1,-1))
            independent_sum+=f["exact_probability"]
            mm=single_signed_trade_mitm(picked,(1,1,-1,-1),12)
            self.assertEqual(mm["exact_probability"],f["exact_probability"])
            self.assertEqual(mm["weighted_flow_count"],
                             f["number_of_nonzero_GF5_weight_assignments"])
            self.assertLessEqual(f["exact_probability"],f["rank_upper"])
            events+=1
        self.assertEqual(events,3)
        self.assertEqual(result["R2"],independent_sum)
        self.assertGreaterEqual(result["R2"],Fraction(1,51**4))

    def test_general_risk_R3_inclusion_exclusion_matches_true_GF5_brute(self):
        s,signs=real_unit_trade(3)
        palette=((1,1,1,1),(1,2,3,3))
        report=risk_from_energy_finite(s,12,3,palette)
        self.assertEqual(report["signature_assignments"],20*2**3)
        self.assertGreater(report["Rk"],0)
        all_sum_risk=0
        # Enumerate ALL 10 distinct unordered 3-vs-3 partitions and
        # ALL 2^6 real GF5 assignments, without using moment identities.
        for plus in combinations(range(6),3):
            minus=tuple(i for i in range(6) if i not in plus)
            if plus>=minus:
                continue
            for weights in product(palette, repeat=6):
                columns=[vector_for_support(s[i], weights[i],12)
                         for i in range(6)]
                a=bytes(12)
                b=bytes(12)
                for i in plus:
                    a=add_gf5_vectors(a,columns[i])
                for i in minus:
                    b=add_gf5_vectors(b,columns[i])
                all_sum_risk+=(a==b)
        self.assertEqual(report["Rk"],Fraction(all_sum_risk,2**6))
        # The unit-coefficient choice is a direct positive witness.
        self.assertGreaterEqual(all_sum_risk,1)

    def test_real_t6_full_51_exact_risk_computed_without_2_to_24_flow_loop(self):
        s,signs=real_unit_trade(3)
        r=single_signed_trade_mitm(s,signs,12)
        self.assertEqual(r["t"],6)
        self.assertEqual(r["total_assignments"],51**6)
        self.assertGreaterEqual(r["weighted_flow_count"],1)
        self.assertGreater(r["plus_distinct_sums"],0)
        self.assertEqual(r["exact_probability"],
                         single_signed_trade_mitm(
                             tuple(reversed(s)),
                             tuple(reversed(signs)),12)["exact_probability"])

    def test_invalid_field_and_resource_budget_handled(self):
        self.assertEqual(len(DEFAULT_PALETTE),51)
        with self.assertRaises(ValueError):
            checked_palette(((1,1,1,1),)*2)
        with self.assertRaises(ValueError):
            checked_palette(((1,1,1,2),))
        with self.assertRaises(ValueError):
            risk_from_pair_energy(w32_supports()[:12],12)
        with self.assertRaises(ValueError):
            risk_from_energy_finite(w32_supports()[:6],12,3,
                                    DEFAULT_PALETTE)
        with self.assertRaises(ValueError):
            single_signed_trade_mitm(w32_supports()[:6],
                                     (1,1,1,-1,-1,-1),12,
                                     max_side_assignments=100)
        with self.assertRaises(ValueError):
            risk_from_pair_energy((w32_supports()[0],)*4,12)
        with self.assertRaises(ValueError):
            single_signed_trade_mitm(w32_supports()[:4],
                                     (1,1,1,-1),12)


if __name__=="__main__":
    unittest.main()
