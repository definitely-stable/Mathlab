"""Genuine-source falsifiers for the quadratic end-posting construction."""
from itertools import combinations, product
import unittest

from hyp105_b1_symplectic import symplectic_gq, symplectic
from hyp105_end_posting_subfield import paired_subfield_w34_witness
from hyp105_physical_degree_energy import minimal_alphabet, _verify_typed_injections
from hyp105_sixflag_pair_collision import source_sixflag_collision_census


class TestEndPostingSubfield(unittest.TestCase):
    def test_source_translate_and_complete_injections(self):
        f,g,w = paired_subfield_w34_witness()
        field,points,lines,flags = symplectic_gq(2)
        _verify_typed_injections(14,85,f,g)
        pp,ll = w["point_permutation"],w["line_permutation"]
        self.assertEqual(set(pp),set(range(85)))
        self.assertEqual(set(ll),set(range(85)))
        for u,v in combinations(range(85),2):
            self.assertEqual(
                symplectic(points[u],points[v],field) == 0,
                symplectic(points[pp[u]],points[pp[v]],field) == 0,
            )
        self.assertEqual({(pp[p],ll[l]) for p,l in flags},set(flags))
        self.assertEqual(w["source_overlap"],(3,2))
        self.assertEqual(w["retained_subfield_flags"],28)
        self.assertIn(tuple(w["alpha"]),set(flags))
        self.assertNotIn(tuple(w["endpoint"]),set(flags))

    def test_target_posting_by_original_incidence_products(self):
        f,g,w = paired_subfield_w34_witness()
        _,_,_,flags = symplectic_gq(2)
        original = set(flags)
        fi = {pair:p for p,pair in enumerate(f)}
        gi = {pair:l for l,pair in enumerate(g)}
        # For (0,0)--(1,1)--(z,Z)--(2,2), each free corner
        # is one reversal orbit, with both flags checked in the source.
        retained = [(z,Z) for z,Z in product(range(3,14),repeat=2)
                    if (fi[1,z],gi[1,Z]) in original
                    and (fi[2,z],gi[2,Z]) in original]
        self.assertEqual(len(retained),28)
        self.assertGreater(len(retained),4)
        alpha = tuple(w["alpha"])
        q,r = w["endpoint"]
        self.assertEqual((f[alpha[0]],g[alpha[1]]),((0,1),(0,1)))
        self.assertEqual((f[q],g[r]),((0,2),(0,2)))

    def test_full_source_collision_census(self):
        f,g,_ = paired_subfield_w34_witness()
        c = source_sixflag_collision_census(2,f,g)
        self.assertEqual(tuple(c[k] for k in (
            "P","Q","C0","C1","C1_middle","C1_end",
            "max_middle_flag_occupancy","max_end_flag_occupancy",
            "max_corner_degree","max_N3",
        )),(73840,1143472,103619,20855,387,20468,3,28,32,84))
        self.assertFalse(c["root_GF5_sevenclass_proved"])

    def test_exact_parameter_sanity_separate_from_all_h_proof(self):
        for k in (2,3,4,5,10,32,128,1024):
            t = 1 << k
            s = t*t
            n = (t+1)*(t*t+1)
            V = (s+1)*(s*s+1)
            with self.subTest(k=k):
                self.assertLess(2*n*n,4*V)
                self.assertLessEqual(n+3,minimal_alphabet(V))
                self.assertGreater(V,4*n)
                self.assertGreater(V-2*n-1,s+1)
                self.assertGreaterEqual((n-3)*(t+1),s*s)


if __name__ == "__main__":
    unittest.main()
