"""Independent aggregate end-energy oracle, retaining true nonincidence."""
import json
from itertools import combinations, permutations, product
from pathlib import Path
import unittest

from hyp105_end_energy_tail_difference import end_energy_tail_difference
from hyp105_end_posting_subfield import paired_subfield_w34_witness
from hyp105_b1_symplectic import symplectic_gq
from hyp105_sixflag_pair_collision import source_sixflag_collision_census
from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked
from hyp105_physical_degree_energy import _verify_typed_injections
from hyp105_weighted_variance_transfer import witness_maps


class TestEndEnergyTailDifference(unittest.TestCase):
    def test_original_source_witnesses_match_separate_orbit_index(self):
        certificate = json.loads((Path(__file__).with_name(
            "hyp105_w34_adversarial_certificate.json"
        )).read_text(encoding="utf-8"))
        f,g,_ = paired_subfield_w34_witness()
        for power,left,right,expected in (
            (1,*witness_maps(41),201),
            (1,*witness_maps(91),126),
            (2,certificate["f"],certificate["g"],8805),
            (2,f,g,20468),
        ):
            with self.subTest(power=power,expected=expected):
                c = end_energy_tail_difference(power,left,right)
                self.assertEqual(c["C1_end"],expected)
                self.assertLessEqual(c["C1_end"],c["unmasked_envelope"])
                self.assertFalse(c["root_sevenclass_proved"])

    def test_injections_and_supported_finite_scope_fail_closed(self):
        f,g = witness_maps(41)
        with self.assertRaises(ValueError):
            end_energy_tail_difference(3,f,g)
        with self.assertRaises(ValueError):
            end_energy_tail_difference(1,[f[1],*f[1:]],g)
        with self.assertRaises(ValueError):
            end_energy_tail_difference(1,f,g[:-1])

    def test_coordinate_permutations_preserve_tail_energy(self):
        f,g = witness_maps(91)
        f2 = [tuple(sorted(((5*u+1)%6,(5*v+1)%6))) for u,v in f]
        g2 = [tuple(sorted(((5*u+2)%6,(5*v+2)%6))) for u,v in g]
        self.assertEqual(end_energy_tail_difference(1,f,g),
                         end_energy_tail_difference(1,f2,g2))

    def test_packed_family_parameter_sanity_not_an_asymptotic_fit(self):
        for k in (3,4,5,10,32,128,1024):
            t = 1 << k
            s = t*t
            n = (t+1)*(t*t+1)
            e = n*(t+1)
            V = (s+1)*(s*s+1)
            pockets = n//256
            with self.subTest(k=k):
                self.assertLess(2*n*n,4*V)
                self.assertGreaterEqual(512*pockets,n)
                self.assertLessEqual(8*(16*(pockets-1)+4),n)
                self.assertLess((n+2*pockets)*(n+2*pockets-1),2*V)
                self.assertLess(16,t*t+1)
                self.assertGreaterEqual(n,20)
                self.assertGreaterEqual(n*e**3,t**15)

    def test_genuine_nonincident_tails_with_large_proper_common_join(self):
        f,g,w = paired_subfield_w34_witness()
        _,_,_,flags = symplectic_gq(2)
        original = set(flags)
        points = w["subfield_points"]
        J = {0,5,6,10,22,26}
        K = (1,2,9,21,25)
        sigma = dict(zip(K,(9,21,1,25,2)))
        g2 = list(g)
        for l in K:
            g2[w["line_permutation"][sigma[l]]] = g[w["line_permutation"][l]]
        common = [(p,l) for p,l in flags if p in points and l in J]
        tail_flags = [(p,l) for p,l in flags if p in points and l in K]
        tails = [(p,l) for p,l in tail_flags if (p,sigma[l]) not in original]
        self.assertEqual((len(common),len(tail_flags),len(tails)),(15,13,12))
        occupancies = [sum(p2 != p for p2,l2 in common) for p,l in tails]
        self.assertEqual(min(occupancies),13)
        self.assertEqual(sum(k*(k-1)//2 for k in occupancies),1110)
        for p,l in tails:
            self.assertNotIn((w["point_permutation"][p],
                              w["line_permutation"][sigma[l]]),original)
        c = end_energy_tail_difference(2,f,g2)
        self.assertEqual(c["C1_end"],20255)
        self.assertEqual(c["C1_end"],
                         source_sixflag_collision_census(2,f,g2)["C1_end"])

    def test_three_hubs_give_six_accepted_original_D6_sets(self):
        _,_,_,flags = symplectic_gq(2)
        used_points,used_lines = set(),set()
        matching = []
        for i,(p,l) in enumerate(flags):
            if p not in used_points and l not in used_lines:
                matching.append((i,p,l))
                used_points.add(p)
                used_lines.add(l)
                if len(matching) == 9:
                    break
        self.assertEqual(len(matching),9)
        f,g = [None]*85,[None]*85
        grid = {}
        for (hub,free),(flag_id,p,l) in zip(product(range(3),range(3,6)),matching):
            f[p] = g[l] = (hub,free)
            grid[hub,free] = flag_id
        for labels in (f,g):
            occupied = {pair for pair in labels if pair is not None}
            available = iter(pair for pair in combinations(range(14),2)
                             if pair not in occupied)
            for i in range(85):
                if labels[i] is None:
                    labels[i] = next(available)
        _verify_typed_injections(14,85,f,g)
        sixsets = set()
        for permutation in permutations(range(3,6)):
            omitted = {(hub,permutation[hub]) for hub in range(3)}
            ids = tuple(sorted(flag_id for pair,flag_id in grid.items()
                               if pair not in omitted))
            self.assertEqual(classify_seven_prechecked(ids,f,g,flags),"D6")
            sixsets.add(ids)
        self.assertEqual(len(sixsets),6)


if __name__ == "__main__":
    unittest.main()
