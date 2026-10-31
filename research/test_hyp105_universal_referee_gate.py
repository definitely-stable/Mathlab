"""Independent scientific adversarial referee gates for HYP-105 #672-#674.

A finite source-native falsifier, not an all-h automated proof or
a human/external referee. Covers complete *correlated* globally injected
pair maps that are NOT the historical frozen lex/reverse examples.
"""
from fractions import Fraction
from math import comb, isqrt
import unittest

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_g5e2b3e1a_fixed_leading import selected_left_six
from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked
from hyp105_unconditional_original_deletion import (
    finite_true_original_sixset_deletion_certificate,
    exact_unconditional_constants,
)
from hyp105_full_physical_degree_tail import (
    genuine_source, physical,
)


def independent_genuine_W32_accepted_two_classes(f, g, flags, left_candidates):
    """Full exhaustive 62,370 left-source candidates; NO physical path DFS.

    This is an independent historical ORIGINAL incidence GF5 classifier,
    not any of the new #672/#674 path reconstruction code.
    """
    D=set()
    B=set()
    for six,kind in left_candidates:
        tag=classify_seven_prechecked(six,f,g,flags)
        if tag=="D6":
            D.add(six)
        elif tag=="B/B-overlap":
            B.add(six)
    if D & B:
        raise AssertionError("historical GF5 accepted source classes overlap")
    return D,B


def deterministic_right_label_permutations(original_right):
    """Legal full globally injected right maps NOT all conjugate by K6.

    Physically permuting each right coordinate leaves structural counts
    unchanged; we instead reassign the 15 DISTINCT K6 edges to DIFFERENT
    actual original source-line factor IDs, disrupting cross-map
    source correlations while maintaining exact globally typed injection.
    """
    v=len(original_right)
    for shift in (0,1,3,7,11):
        yield shift, tuple(original_right[(i+shift)%v] for i in range(v))


def greedy_maximal_original_flag_sixset_matching(candidates):
    """Select maximal disjoint SIX original incidence-ID sets.

    This gives a hitting-set certificate (union of chosen source sets),
    NOT a numerical lower bound on matching number at small h.
    """
    chosen=[]
    used=set()
    for six in sorted(candidates):
        if not used.intersection(six):
            chosen.append(six)
            used.update(six)
    assert len(used)==6*len(chosen)
    assert all(set(six)&used for six in candidates), (
        "maximal-original-ID matching's union is not a hitting set"
    )
    return tuple(chosen),frozenset(used)


class ScientificRefereeUniversalSource(unittest.TestCase):
    def test_adversarial_globally_reassigned_g_W32_finite_D6_and_BBo(self):
        source=pair_labeled_symplectic(1,"lex")
        s,V,flags=genuine_source(1)
        self.assertEqual(V,15)
        left=tuple(source["left_labels"])
        source_candidates=tuple(selected_left_six(source))
        self.assertEqual(len(source_candidates),62370)
        for shift,g in deterministic_right_label_permutations(
                source["right_labels"]):
            # Five legally globally injected, generally correlated g,
            # with a fixed ORIGINAL source f and original flags.
            self.assertEqual(len(set(g)),V)
            D,B=independent_genuine_W32_accepted_two_classes(
                left,g,flags,source_candidates)
            for Z in ((),(0,),(0,1,2),tuple(range(0,45,7))):
                with self.subTest(shift=shift,Z=len(Z)):
                    rem=set(Z)
                    D_remaining={six for six in D if not rem.intersection(six)}
                    B_remaining={six for six in B if not rem.intersection(six)}
                    result=finite_true_original_sixset_deletion_certificate(
                        1,left,g,Z)
                    self.assertEqual(result["D6_avoid"],len(D_remaining))
                    self.assertLessEqual(
                        result["BBo_avoid_produced_source_subcount"],
                        len(B_remaining))
                    self.assertLessEqual(
                        result["two_disjoint_historical_GF5_class_sixset_lower"],
                        len(D_remaining)+len(B_remaining))

    def test_true_source_hitting_set_after_maximal_all_six_ID_packing(self):
        source=pair_labeled_symplectic(1,"lex")
        _,_,flags=genuine_source(1)
        left=tuple(source["left_labels"])
        candidates=tuple(selected_left_six(source))
        for shift,g in deterministic_right_label_permutations(
                source["right_labels"]):
            D,B=independent_genuine_W32_accepted_two_classes(
                left,g,flags,candidates)
            selected,Z=greedy_maximal_original_flag_sixset_matching(D|B)
            self.assertEqual(len(Z),6*len(selected))
            self.assertTrue(all(len(six)==6 and
                                len(set(six))==6 for six in selected))
            self.assertFalse(any(set(six).isdisjoint(Z) for six in D|B))
            # The two ACTUAL independent source-backed physical oracles
            # must both return ZERO after removing a hitting set of all
            # historical ORIGINAL D6 and BBo classes.
            post=finite_true_original_sixset_deletion_certificate(
                1,left,g,sorted(Z))
            self.assertEqual(post["D6_avoid"],0)
            self.assertEqual(post["BBo_avoid_produced_source_subcount"],0)

    def test_symbolic_high_tail_and_low_tail_complete_error_budget(self):
        """Independent exact power algebra from cited #659/#672/#673."""
        for C,c in ((1,Fraction(1)),(2,Fraction(1,5)),
                    (9,Fraction(1,13))):
            q=exact_unconditional_constants(C,c)
            T=q["heavy_degree_cap_T"]
            K=q["source_conflict_degree_cap_K"]
            rho=q["allowed_original_flag_deletion_density_rho"]
            delta=q["accepted_sixset_all_map_floor_delta"]
            eps=Fraction(1,8)
            beta=(eps/2)**2/Fraction(128)
            self.assertEqual(beta,eps**2/Fraction(512))
            self.assertEqual(T,2**20*C**3*beta.denominator**3//
                                 beta.numerator**3)
            self.assertEqual(c*(beta/Fraction(32))**6,
                             c/Fraction(2**120))
            self.assertLessEqual(2*rho,eps/2)
            self.assertGreaterEqual(1-eps-Fraction(3,32)-rho,
                                    Fraction(3,4))
            self.assertEqual(delta,c/Fraction(2**120))
            s0=q["sufficient_s0_integer"]
            LEupper=200*q["selected_sigma3_inverse"]*T
            L4coefficient=140*q["selected_sigma2_inverse"]**2+56
            rt=isqrt(L4coefficient)
            ceiling=rt+(rt*rt<L4coefficient)
            LBupper=24*ceiling*T*T
            self.assertGreaterEqual(s0,1008*T)
            self.assertGreaterEqual(s0,(12*LEupper)**2)
            self.assertGreaterEqual(s0,(48*LBupper)**8)
            # All three normalized path errors <=s^6/24 exactly.
            self.assertLessEqual(Fraction(42*T,s0),Fraction(1,24))
            self.assertLessEqual(Fraction(LEupper**2,4*s0),
                                 Fraction(1,24**2))
            self.assertLessEqual(Fraction(LBupper**8,s0),
                                 Fraction(1,48**8))
            self.assertLessEqual(
                12*rho*q["endpoint_proper_third_path_Frobenius_bound_squared_M3"],
                Fraction(1,64))
            self.assertGreaterEqual(Fraction(1,16),delta)

    def test_true_W32_physical_provenance_is_unique_before_and_after_deletion(self):
        for scheme in ("lex","reverse-line"):
            model=pair_labeled_symplectic(1,scheme)
            _,_,flags=genuine_source(1)
            f,g=model["left_labels"],model["right_labels"]
            full,owner=physical(range(45),flags,f,g)
            self.assertEqual(len(owner),90)
            self.assertEqual(sum(map(len,full.values())),180)
            for Z in (set(),{0},{0,1,2},set(range(0,45,7))):
                sub,subowners=physical(
                    (i for i in range(45) if i not in Z),flags,f,g)
                self.assertEqual(len(subowners),90-2*len(Z))
                self.assertEqual(
                    {e for e,i in owner.items() if i not in Z},
                    set(subowners))
                self.assertTrue(
                    all(subowners[e]==owner[e] for e in subowners))


if __name__=="__main__":
    unittest.main()
