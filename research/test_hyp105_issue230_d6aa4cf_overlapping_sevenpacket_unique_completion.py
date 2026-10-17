"""AA4-CF independent TRUE-original 7-packet overlap and 5-edge no-go tests."""
import unittest
from collections import Counter
from itertools import combinations
from fractions import Fraction

from hyp105_issue230_d6aa4cf_overlapping_sevenpacket_unique_completion import (
    PACKETS7, CUBE, FIVE_MASK, FAMILIES,
    original_shared_five_graph_unique_completion, _regular6,
    _lift_orientation, original_shared_five_graph_unique_completion,
    source_original_orientation_7, physical_overlapping_masks,
    mixed_pair_gram, source_families_W32, shared_twofamily_W32,
)
from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4bq_all_seven_reverse_switching import (
    apply_disjoint_factor_swaps,
)
from hyp105_issue230_d6aa4by_original_independent_2factor_kernel import (
    physical_right_is_six_vertex_two_regular,
)
from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked

K6_EDGES=tuple(combinations(range(6),2))


def both_live_physical_W32_g():
    """One TRUE full K6 original LINE image injection, both A/B physically nonzero.

    A selected C6: 01,12,23,34,45,05
    B selected C6: 01,12,23,35,45,04
    Each selected B edge originates from its OWN complete global packet.
    """
    a=((0,1),(1,2),(2,3),(3,4),(4,5),(0,5),(0,4))
    chosen_extra=(3,5)
    used=set(a)|{chosen_extra}
    rest=tuple(x for x in K6_EDGES if x not in used)
    assert len(rest)==7
    grouped=(
        (a[0],rest[0]), (a[1],rest[1]), (a[2],rest[2]),
        (a[3],chosen_extra), (a[4],rest[3]),
        (a[5],rest[4]),(a[6],rest[5]),
    )
    original_g=tuple(e for pair in grouped for e in pair)+(rest[6],)
    assert len(original_g)==15 and len(set(original_g))==15
    return original_g


class AA4CFOriginalSevenpacket(unittest.TestCase):
    def test_01_exhaustive_real_K6_five_edge_single_completion(self):
        # 3,003 genuine sets of five physical edges; independently try
        # ALL unordered pairs of distinct candidate sixth physical edges.
        # No Fourier code or source-Q classification is used here.
        checked=0;positive_completions=0
        for five in combinations(K6_EDGES,5):
            remaining=tuple(e for e in K6_EDGES if e not in five)
            for sixth1,sixth2 in combinations(remaining,2):
                a,b=original_shared_five_graph_unique_completion(
                    five,sixth1,sixth2)
                degree1=Counter(v for e in (*five,sixth1) for v in e)
                degree2=Counter(v for e in (*five,sixth2) for v in e)
                self.assertEqual(a,int(len(degree1)==6 and
                    set(degree1.values())=={2}))
                self.assertEqual(b,int(len(degree2)==6 and
                    set(degree2.values())=={2}))
                self.assertFalse(a and b)
                checked+=1
                positive_completions+=a+b
        self.assertEqual(checked,3003*45)
        self.assertGreater(positive_completions,0)
        with self.assertRaises(ValueError):
            original_shared_five_graph_unique_completion(
                K6_EDGES[:5], K6_EDGES[0], K6_EDGES[7])
        with self.assertRaises(ValueError):
            original_shared_five_graph_unique_completion(
                K6_EDGES[:4],K6_EDGES[5],K6_EDGES[7])
        print("AA4CF_K6_FINITE_EXHAUSTIVE",checked,positive_completions,
              flush=True)

    def test_02_two_LIVE_7packet_K6_physical_families_mixed_Gram(self):
        g=both_live_physical_W32_g()
        res=physical_overlapping_masks(g,PACKETS7)
        self.assertGreater(res["A_active"],0)
        self.assertGreater(res["B_active"],0)
        self.assertEqual(res["A"][0],1)
        self.assertEqual(res["B"][8],1)
        self.assertTrue(all(not(res["A"][x] and res["B"][x])
                            for x in range(CUBE)))
        gram=mixed_pair_gram(res)
        self.assertEqual(gram["J"][0][0],0)
        self.assertGreater(gram["J"][0][8],0)
        for t in range(64):
            for u in range(64):
                if (t&FIVE_MASK)==(u&FIVE_MASK):
                    self.assertEqual(gram["J"][t][u],0)
        # Completely distinct direct 7D physical raw graph oracle
        # against bitset-based mixed Gram for sampled translated offsets.
        for t,u in ((0,0),(0,8),(15,30),(37,7),(63,63),(8,0)):
            direct=0
            for x in range(CUBE):
                physical=[]
                for fam,local in (("A",t),("B",u)):
                    lifted=x^_lift_orientation(local,fam)
                    edges=tuple(res["edges"][j][(lifted>>j)&1]
                                for j in FAMILIES[fam])
                    physical.append(_regular6(edges))
                direct+=physical[0]*physical[1]
            self.assertEqual(direct,gram["J"][t][u])
        print("AA4CF_LIVE_K6",res["A_active"],res["B_active"],
              gram["positive_orientation_pair_count"],
              gram["max_joint_maps"],flush=True)

    def test_03_TRUE_original_W32_lex_S72_both_families_128_global_maps(self):
        for scheme,expectA in (("lex",351),("S72",301)):
            model=fixture(1,scheme)
            source=source_families_W32(model,PACKETS7)
            self.assertEqual(source["counts"]["A"],expectA)
            self.assertGreater(source["counts"]["B"],0)
            self.assertFalse({t[0] for t in source["Q"]["A"]} &
                             {t[0] for t in source["Q"]["B"]})
            r=shared_twofamily_W32(model,PACKETS7,verify_original=True)
            self.assertEqual(r["total_crossfamily_original_Q_pairs"],
                             source["counts"]["A"]*source["counts"]["B"])
            self.assertGreater(r["five_pins_same_source_Q_pairs_forbidden"],0)
            self.assertGreaterEqual(r["total_physically_forbidden_original_Q_pairs"],
                                    r["five_pins_same_source_Q_pairs_forbidden"])
            self.assertEqual(r["mixed_envelope_cross_moment_sum"],
                             r["mixed_envelope_cross_moment_by_Gram"])
            self.assertEqual(len(r["physical_family_envelope_A"]),CUBE)
            for fam in FAMILIES:
                self.assertEqual(len(r["historical_selected_Q_weighted_7cube"][fam]),CUBE)
                for x in range(CUBE):
                    self.assertLessEqual(r["historical_selected_Q_weighted_7cube"][fam][x],
                                         r["physical_family_envelope_"+fam][x])
            print("AA4CF_ORIGINAL",scheme,
                  "QA",source["counts"]["A"],"QB",source["counts"]["B"],
                  "A_live",r["physical_A_active"],"B_live",r["physical_B_active"],
                  "joint_all_pairs",r["total_crossfamily_original_Q_pairs"],
                  "same_five_forbidden",r["five_pins_same_source_Q_pairs_forbidden"],
                  "all_physical_forbidden",r["total_physically_forbidden_original_Q_pairs"],
                  "mixed_moment",r["mixed_envelope_cross_moment_sum"],flush=True)

    def test_04_NONVACUOUS_true_W32_both_live_and_literal_cross_Q_pairs(self):
        model=dict(fixture(1,"S72"),right_labels=both_live_physical_W32_g())
        r=shared_twofamily_W32(model,PACKETS7,verify_original=True)
        self.assertGreater(r["physical_A_active"],0)
        self.assertGreater(r["physical_B_active"],0)
        self.assertEqual(len(r["mixed_physical_Gram_J"]),64)
        self.assertGreater(r["physically_joint_possible_orientation_pairs"],0)
        self.assertGreater(r["five_pins_same_source_Q_pairs_forbidden"],0)
        # Pair count independent of 64-bin histogram multiplication:
        src=source_families_W32(model,PACKETS7)
        left=src["Q"]["A"];right=src["Q"]["B"]
        literal=0; forbidden=0
        J=r["mixed_physical_Gram_J"]
        for QA,tA,wa,tagA in left:
            for QB,tB,wb,tagB in right:
                if (tA&FIVE_MASK)==(tB&FIVE_MASK):
                    literal+=1
                if J[tA][tB]==0:
                    forbidden+=1
        self.assertEqual(literal,r["five_pins_same_source_Q_pairs_forbidden"])
        self.assertEqual(forbidden,r["total_physically_forbidden_original_Q_pairs"])
        self.assertGreaterEqual(forbidden,literal)
        print("AA4CF_REAL_BOTH_LIVE",r["original_source_Q_counts"],
              "A_live",r["physical_A_active"],"B_live",r["physical_B_active"],
              "same_five_forbidden",literal,
              "physical_forbidden",forbidden,
              "mixed_moment",r["mixed_envelope_cross_moment_sum"],flush=True)

    def test_05_g_adversarial_relabel_f_only_and_bad_inputs(self):
        model=fixture(1,"S72")
        original=source_families_W32(model,PACKETS7)
        altered=dict(model,right_labels=tuple(reversed(model["right_labels"])))
        reordered=source_families_W32(altered,PACKETS7)
        self.assertEqual(original["H"],reordered["H"])
        self.assertEqual(original["N"],reordered["N"])
        self.assertEqual(original["Q"],reordered["Q"])
        s,V,a,inc,f,g,_,_=_original_source(model)
        one=original["Q"]["B"][0][0]
        self.assertIn(source_original_orientation_7(
            one,inc,PACKETS7,V,"B"),range(CUBE))
        with self.assertRaises(ValueError):
            source_original_orientation_7(one,inc,PACKETS7,V,"no-family")
        with self.assertRaises(ValueError):
            source_original_orientation_7(one,inc,PACKETS7[:6],V,"B")
        with self.assertRaises(ValueError):
            physical_overlapping_masks(g,PACKETS7[:6])
        bad=list(g);bad[0]=bad[1]
        with self.assertRaises(ValueError):
            physical_overlapping_masks(bad,PACKETS7)
        with self.assertRaises(ValueError):
            physical_overlapping_masks(g,
                ((0,1),(1,2),(3,4),(5,6),(7,8),(9,10),(11,12)))


if __name__=="__main__":
    unittest.main()
