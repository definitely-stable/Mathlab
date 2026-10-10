"""HYP-105 C13: independent incidence/both-physical-side orbit falsifiers."""
from itertools import combinations
from math import factorial
import unittest

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_g5e2b3e1b0_seven_signature import seven_census
from hyp105_g5e2b3e1c12_physical_orbits import physical_coordinate_actions
from hyp105_g5e2b3e1c13_joint_orbits import (
    w32_original_sp4_automorphisms,original_incidence_pair_orbits,
    joint_transport_W32,joint_fixed_pair_stabilizer_W32,
    canonical_joint_pair_key_W32,W32_joint_orbit_report,
)


class C13JointGQDoubleOrbitTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.A=w32_original_sp4_automorphisms()
        cls.model=pair_labeled_symplectic(1,"reverse-line")
        cls.H=physical_coordinate_actions(
            6,tuple(combinations(range(6),2))
        )["distinct_occupied_edge_actions"]

    def test_entire_GQ_sp4_group_incidence_preserved(self):
        self.assertEqual(len(self.A),720)
        inc=set(self.model["incidences"])
        for p,l in self.A:
            self.assertEqual(set(p),set(range(15)))
            self.assertEqual(set(l),set(range(15)))
            self.assertEqual({(p[i],l[j]) for i,j in inc},inc)

    def test_original_point_line_flags_and_antiflags_not_conflated(self):
        r=original_incidence_pair_orbits(self.A)
        self.assertEqual(r["orbit_cardinalities"],(45,180))
        self.assertEqual(r["original_incidence_flags"],45)
        self.assertEqual(r["original_nonincident_antiflags"],180)
        for _,size,stabilizer in r["point_line_pair_orbits"]:
            self.assertEqual(size*stabilizer,720)

    def test_joint_stabilizer_exact_orbit_size(self):
        cert=joint_fixed_pair_stabilizer_W32(self.model,self.A,self.H,self.H)
        self.assertEqual(cert["full_joint_group_order"],720**3)
        self.assertGreaterEqual(cert["stabilizer_size_of_actual_pair_f_g"],1)
        self.assertEqual(cert["joint_orbit_cardinality"]*
                         cert["stabilizer_size_of_actual_pair_f_g"],720**3)
        for p,l in cert["stabilizer_original_collineations"]:
            self.assertIn((p,l),self.A)

    def test_independent_seven_class_census_under_joint_transport(self):
        original=seven_census(self.model,independent_checks=False)
        ident=tuple(range(15))
        options=(self.A[1],self.A[len(self.A)//2],self.A[-1])
        sample=(self.H[5],self.H[-3])
        for i,geo in enumerate(options):
            candidate=joint_transport_W32(
                self.model,geo,sample[i%2],sample[(i+1)%2])
            new=seven_census(candidate,independent_checks=False)
            self.assertEqual(original["seven_class_motif_counts"],
                             new["seven_class_motif_counts"])
            self.assertEqual(original["S_seven"],new["S_seven"])
            self.assertEqual(original["GF5_seven_lower_numerator"],
                             new["GF5_seven_lower_numerator"])
            self.assertEqual(candidate["N"],45)
            self.assertEqual(len(set(candidate["supports"])),45)

    def test_exact_joint_canonical_key_independent_nontrivial_transforms(self):
        base=canonical_joint_pair_key_W32(self.model,self.A,self.H)
        ident=tuple(range(15))
        geo=next(t for t in self.A if t!=(ident,ident))
        changed=joint_transport_W32(self.model,geo,self.H[7],self.H[-7])
        another=canonical_joint_pair_key_W32(changed,self.A,self.H)
        self.assertEqual(base["canonical_pair_key"],
                         another["canonical_pair_key"])
        self.assertEqual(base["physical_normalizations_exhausted"],1036800)

    def test_invalid_non_incidence_original_relabeling_fail_closed(self):
        ident=tuple(range(15))
        # Only permuting ORIGINAL points while leaving original lines
        # fixed cannot be silently treated as an automorphism of GQ.
        wrong=list(ident)
        wrong[0],wrong[1]=wrong[1],wrong[0]
        with self.assertRaises(ValueError):
            joint_transport_W32(self.model,(tuple(wrong),ident),ident,ident)
        with self.assertRaises(ValueError):
            canonical_joint_pair_key_W32(
                self.model,self.A,self.H,max_physical_normalizations=1036799)

    def test_whole_GQ_and_GF5_scope_report(self):
        report=W32_joint_orbit_report()
        self.assertEqual(report["original_sp4_order"],720)
        self.assertEqual(report["joint_group_order"],720**3)
        self.assertEqual(report["original_point_line_orbits"],(45,180))
        self.assertEqual(report["same_map_seven_original_S"],
                         report["same_map_transformed_S"])
        self.assertEqual(report["same_map_seven_original_S"],169)
        self.assertTrue(report["canonical_joint_pair_key_invariant_under_nontrivial_triple"])
        self.assertFalse(report["joint_orbit_all_f_g_exhausted"])
        self.assertFalse(report["all_h_uniform_seven_class_lower_proved"])


if __name__=="__main__":
    unittest.main()
