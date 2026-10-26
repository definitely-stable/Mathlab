"""AA4-TCN: rigorous genuine-source triple common-neighborhood / D6 transfer."""
import json
from itertools import combinations, product
from pathlib import Path
import unittest

from hyp105_b1_symplectic import symplectic_gq
from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_physical_degree_energy import _verify_typed_injections
from hyp105_triple_codegree_d6_compensation import (
    exact_coordinate_transversal_m3,
    greedy_matching_three_lower,
    true_source_triple_codegree_d6,
)


def _coherent_k44_source_witness():
    """Genuine source W34: four physical hubs x four diagonal free corners.

    Independently constructs a 16-edge original point/line matching,
    not a synthetic 16-edge source graph, and completes BOTH typed maps.
    """
    _,_,_,flags=symplectic_gq(2)
    by_point=[[] for _ in range(85)]
    for p,l in flags:
        by_point[p].append(l)
    owner={}
    def augment(p,used):
        for l in by_point[p]:
            if l in used:
                continue
            used.add(l)
            if l not in owner or augment(owner[l],used):
                owner[l]=p
                return True
        return False
    for p in range(16):
        if not augment(p,set()):
            raise AssertionError("cannot find 16 genuine source incidence matching")
    original=sorted((p,l) for l,p in owner.items())
    if len(original)!=16 or len({p for p,l in original})!=16 or (
            len({l for p,l in original})!=16):
        raise AssertionError("source factor matching not injective")
    f,g=[None]*85,[None]*85
    for (hub,free),(p,l) in zip(product(range(4),range(4,8)),
                                original):
        f[p]=(hub,free)
        g[l]=(hub,free)
    for labels in (f,g):
        occupied={pair for pair in labels if pair is not None}
        remaining=iter(e for e in combinations(range(14),2)
                       if e not in occupied)
        for i in range(85):
            if labels[i] is None:
                labels[i]=next(remaining)
    _verify_typed_injections(14,85,f,g)
    return f,g


class TestTripleCommonNeighborhoodD6(unittest.TestCase):
    def test_coordinate_matching_greedy_bound_on_small_bipartite_graphs(self):
        corners=tuple((i,i) for i in range(4))
        self.assertEqual(exact_coordinate_transversal_m3(corners),4)
        self.assertEqual(greedy_matching_three_lower(corners),24)
        star=tuple((0,j) for j in range(9))
        self.assertEqual(exact_coordinate_transversal_m3(star),0)
        self.assertEqual(greedy_matching_three_lower(star),0)
        for n in range(3,8):
            all_corners=tuple(product(range(n),repeat=2))
            for stride in (2,3,5):
                sample=all_corners[::stride]
                self.assertGreaterEqual(
                    6*exact_coordinate_transversal_m3(sample),
                    greedy_matching_three_lower(sample)
                )
        with self.assertRaises(ValueError):
            exact_coordinate_transversal_m3(((1,2),(1,2),(2,3)))
        with self.assertRaises(ValueError):
            greedy_matching_three_lower(((1,2),(1,2),(2,3)))

    def test_independent_W32_true_original_seven_GF5_D6_oracles(self):
        for scheme,sector,d6 in (("lex",6,15),("reverse-line",0,3)):
            with self.subTest(scheme=scheme):
                m=pair_labeled_symplectic(1,scheme)
                c=true_source_triple_codegree_d6(
                    1,m["left_labels"],m["right_labels"],
                    verify_gf5=True,verify_full_d6=True)
                self.assertEqual(c["accepted_original_D6_from_K33"],sector)
                self.assertEqual(c["all_accepted_original_D6"],d6)
                self.assertEqual(c["non_K33_accepted_original_D6"],d6-sector)
                self.assertEqual(c["unique_coordinate_transverse_K33"],
                                 sector//6)
                self.assertEqual(
                    3*c["oriented_transversal_three_matchings"],sector)
                self.assertLessEqual(
                    c["greedy_bound_two_times_D6_numerator"],2*sector)
                self.assertFalse(c["all_h_D6_Omega_s6_proved"])

    def test_W34_adversarial_has_D6_without_one_K33(self):
        cert=json.loads(Path(__file__).with_name(
            "hyp105_w34_adversarial_certificate.json"
        ).read_text(encoding="utf-8"))
        c=true_source_triple_codegree_d6(
            2,cert["f"],cert["g"],
            verify_gf5=True,verify_full_d6=True)
        self.assertEqual(c["unique_coordinate_transverse_K33"],0)
        self.assertEqual(c["accepted_original_D6_from_K33"],0)
        self.assertEqual(c["all_accepted_original_D6"],4972)
        self.assertEqual(c["non_K33_accepted_original_D6"],4972)

    def test_W34_real_original_K44_coherent_protected_96_D6(self):
        f,g=_coherent_k44_source_witness()
        c=true_source_triple_codegree_d6(
            2,f,g,verify_gf5=True,verify_full_d6=False)
        self.assertGreaterEqual(c["unique_coordinate_transverse_K33"],16)
        self.assertGreaterEqual(c["accepted_original_D6_from_K33"],96)
        self.assertEqual(
            c["accepted_original_D6_from_K33"],
            3*c["oriented_transversal_three_matchings"])
        self.assertEqual(
            c["accepted_original_D6_from_K33"],
            6*c["unique_coordinate_transverse_K33"])
        self.assertTrue(c["all_h_K33_to_D6_exact_subsector_proved"])
        self.assertIsNone(c["all_accepted_original_D6"])

    def test_coordinate_relabeling_preserves_K33_original_D6_subsector(self):
        m=pair_labeled_symplectic(1,"lex")
        f,g=m["left_labels"],m["right_labels"]
        base=true_source_triple_codegree_d6(
            1,f,g,verify_full_d6=False)
        shifted_f=[tuple(sorted(((5*u+1)%6,(5*v+1)%6))) for u,v in f]
        shifted_g=[tuple(sorted(((5*u+2)%6,(5*v+2)%6))) for u,v in g]
        perm=true_source_triple_codegree_d6(
            1,shifted_f,shifted_g,verify_full_d6=False)
        for key in ("oriented_transversal_three_matchings",
                    "unique_coordinate_transverse_K33",
                    "accepted_original_D6_from_K33",
                    "greedy_bound_two_times_D6_numerator"):
            self.assertEqual(base[key],perm[key])

    def test_no_synthetic_source_injection_or_unsupported_field(self):
        m=pair_labeled_symplectic(1,"lex")
        f,g=m["left_labels"],m["right_labels"]
        with self.assertRaises(ValueError):
            true_source_triple_codegree_d6(3,f,g)
        with self.assertRaises(ValueError):
            true_source_triple_codegree_d6(1,f[:-1],g)
        wrong=list(g);wrong[0]=wrong[1]
        with self.assertRaises(ValueError):
            true_source_triple_codegree_d6(1,f,wrong)


if __name__=="__main__":
    unittest.main()
