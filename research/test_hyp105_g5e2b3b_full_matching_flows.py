"""Independent all-six factor-matching GF5 exhaustive-template falsifiers."""
import unittest
from collections import Counter
from itertools import combinations, product

from hyp105_g5e2b3b_full_matching_flows import (
    N, SIGNS, projection_types, validate_profile,
    signed_stabilizer_group, transform_profile,
    nonzero_coordinate_options, half_checksum_histogram,
    matching_signed_orbit_representatives, exact_pair_GF5_flow,
    supports_for_profiles, exhaustive_matching_census,
)
from hyp105_g5e2b3b1_critical_flows import (
    exact_nowherezero_signed_flow, connected_contracted_column_graph,
)
from hyp105_g5e2b1_energy import single_signed_trade_mitm


def contracted_edges(profile):
    """Independent bit-intersection translation when EVERY mask has degree2."""
    edges=[]
    for mask in profile:
        ids=tuple(i for i in range(N) if mask>>i&1)
        if len(ids)!=2:
            raise ValueError("6/6 degree-two case only")
        edges.append(ids)
    return tuple(sorted(edges))


def coordinate_direct_count(mask):
    ids=tuple(i for i in range(N) if mask>>i&1)
    return sum(sum(SIGNS[i]*w for i,w in zip(ids,coeff))%5==0
               for coeff in product(range(1,5),repeat=len(ids)))


class CompleteMatchingFlowTests(unittest.TestCase):
    def test_all_injective_6edge_projection_catalog(self):
        rows=projection_types()
        self.assertEqual(len(rows),610)
        self.assertEqual(Counter(map(len,rows)),{4:30,5:510,6:70})
        self.assertEqual(len(set(rows)),len(rows))
        for row in rows:
            self.assertTrue(validate_profile(row))
            self.assertEqual(sum(mask.bit_count() for mask in row),12)
            self.assertEqual(len(supports_for_profiles(row,row)),6)
        with self.assertRaises(ValueError):
            validate_profile((3,3,3,3))
        with self.assertRaises(ValueError):
            validate_profile((1,3,7,15))
        with self.assertRaises(ValueError):
            validate_profile((3,5,6,8))
        with self.assertRaises(ValueError):
            transform_profile(rows[0],(0,1,2,3,4,4))

    def test_GF5_single_coordinate_constraint_vs_full_brute(self):
        for mask in (0b000011,0b000111,0b001011,0b001111,
                     0b111000,0b101011):
            direct=coordinate_direct_count(mask)
            constructed=nonzero_coordinate_options(mask)
            self.assertEqual(len(constructed),direct)
            self.assertEqual(len(set(constructed)),len(constructed))
            for assignment in constructed:
                self.assertEqual(sum(SIGNS[i]*w for i,w in assignment)%5,0)
                self.assertTrue(all(1<=w<=4 for i,w in assignment))
        with self.assertRaises(ValueError):
            nonzero_coordinate_options(1)

    def test_half_conservation_and_explicit_4D_small_brute(self):
        for profile in (projection_types()[0],
                        next(x for x in projection_types() if len(x)==5),
                        next(x for x in projection_types() if len(x)==6)):
            h=half_checksum_histogram(profile)
            self.assertTrue(h)
            self.assertEqual(sum(h.values()),__import__("math").prod(
                coordinate_direct_count(m) for m in profile))
            self.assertTrue(all(
                sum(sign*z for sign,z in zip(SIGNS,sig))%5==0
                for sig in h))
        self.assertLessEqual(len(h),5**5)

    def test_six_matching_color_signed_orbit_group_mass(self):
        reps=matching_signed_orbit_representatives()
        self.assertEqual(len(reps),5486)
        self.assertEqual(sum(weight for _,_,weight in reps),3721000)
        self.assertEqual(len(signed_stabilizer_group()),72)
        self.assertEqual(len(set(signed_stabilizer_group())),72)
        # Normalized projection types form EXACTLY 20 orbits under signed H.
        self.assertEqual(len(set(
            min(transform_profile(x,p) for p in signed_stabilizer_group())
            for x in projection_types())),20)
        self.assertEqual(sum(weight for left,right,weight in reps
                             if len(left)==len(right)==6),49000)

    def test_two_independent_full_GF5_oracles_across_all_core_sizes(self):
        reps=matching_signed_orbit_representatives()
        pairs={(len(left),len(right)):(left,right)
               for left,right,_ in reversed(reps)}
        for shape in ((4,4),(4,5),(4,6),(5,4),(5,5),(5,6),
                      (6,4),(6,5),(6,6)):
            left,right=pairs[shape]
            direct=exact_pair_GF5_flow(left,right)
            supports=supports_for_profiles(left,right)
            independently=single_signed_trade_mitm(
                supports,(1,1,1,-1,-1,-1),len(left)+len(right))
            self.assertEqual(direct,independently["weighted_flow_count"])
            self.assertEqual(independently["total_assignments"],51**6)
            self.assertGreater(direct,0)

    def test_independent_classical_12_edge_flow_for_entire_6_6_subcase(self):
        relevant=((left,right,weight)
                  for left,right,weight in
                  matching_signed_orbit_representatives()
                  if len(left)==len(right)==6)
        seen=Counter()
        for left,right,mass in relevant:
            old=exact_nowherezero_signed_flow(
                contracted_edges(left),contracted_edges(right),0b000111)
            new=exact_pair_GF5_flow(left,right)
            self.assertEqual(old,new)
            self.assertEqual(old>0,connected_contracted_column_graph(
                contracted_edges(left),contracted_edges(right)))
            seen["positive" if old else "zero"]+=mass
        self.assertEqual(seen,{"positive":48900,"zero":100})

    def test_all_profile_orbits_exact_positive_flow_falsifier(self):
        results=exhaustive_matching_census()
        self.assertEqual(results["projection_types_total"],610)
        self.assertEqual(results["all_labeled_signed_templates"],3721000)
        self.assertEqual(results["signed_color_preserving_orbits"],5486)
        self.assertEqual(results["zero_labeled_signed_templates"],100)
        self.assertEqual(results["positive_labeled_signed_templates"],3720900)
        self.assertEqual(results["min_positive_GF5_weight_assignments"],4806)
        self.assertEqual(results["max_positive_GF5_weight_assignments"],135001)
        self.assertFalse(results["fixed_label_full_R3_upper_proved"])
        self.assertFalse(results["all_11663_factor_forest_shapes_classified"])
        self.assertFalse(results["new_ASET_exponent_proved"])
        by_key=results["labeled_signed_by_vleft_vright_status"]
        self.assertEqual(by_key["6/6/zero"],100)
        self.assertEqual(by_key["5/5/positive"],2601000)
        self.assertEqual(by_key["4/4/positive"],9000)
        self.assertEqual(set(k for k in by_key if k.endswith("/zero")),
                         {"6/6/zero"})


if __name__=="__main__":
    unittest.main()
