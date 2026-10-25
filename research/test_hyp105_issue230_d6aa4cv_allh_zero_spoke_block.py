"""AA4-CV: independent true original GQ all-h projected-energy ZERO witness."""
from itertools import combinations,permutations
from math import comb
import unittest

from hyp105_b1_symplectic import symplectic_gq
from hyp105_issue230_proof_audit import parameters
from hyp105_issue230_d6aa4cr_exact_BBo_three_matching_transfer import (
    c4_completions_from_single_and_doubled, original_nonincident_threepath,
)
from hyp105_issue230_d6aa4cu_exterior_matching_energy import incidence_minor3_det
from hyp105_issue230_d6aa4cv_allh_zero_spoke_block import (
    allh_zero_spoke_arithmetic,
    complete_zero_anchor_source_pairmaps,
    verify_combinatorial_zero_without_enumerating_quartic_pairs,
)


def independent_permanent3(P,L,pl):
    return sum(all(line in pl[point] for point,line in zip(P,perm))
               for perm in permutations(L))


def independent_zero_energy_adversarial_spoke_test(w,pl,lp,limit=30):
    """Independent old C4 triple enumeration + actual original determinant/permanent.

    No shared use of the CV no-cross proof except validation of real GQ
    input and explicit f/g maps. Check nontrivial diverse samples from
    the exact occupied source triple families on SAME full global maps.
    """
    s,V,a=w["s"],w["V"],w["a"]
    p,l=w["anchor"]
    (p0,l0),(q,l1),(q1,l2)=original_nonincident_threepath(p,l,pl,lp)
    assert (p0,q1,l0,l1,l2)==(p,q,l0,l0,l)
    f,g=w["point_labels"],w["line_labels"]
    fi={pair:i for i,pair in enumerate(f)}
    gi={pair:i for i,pair in enumerate(g)}
    left=c4_completions_from_single_and_doubled(f[p],f[q],fi,a)
    right=c4_completions_from_single_and_doubled(g[l],g[l0],gi,a)
    N=(a-4)*(a-5)
    assert len(left)==len(right)==N
    source_p_spoke=set(w["source_POINT_spokes"])
    source_l_spoke=set(w["source_LINE_spokes"])
    assert all(len(set(P)&source_p_spoke)==2 for P in left)
    assert all(len(set(L)&source_l_spoke)==2 for L in right)
    step=max(1,N//limit)
    checked=0
    for P in left[::step]:
        for L in right[::step]:
            det=incidence_minor3_det(P,L,pl)
            per=independent_permanent3(P,L,pl)
            assert (det,per)==(0,0)
            checked+=1
    assert checked>=limit*limit//4
    return {"s":s,"a":a,"left_C4_real_source_triples":len(left),
            "right_C4_real_source_triples":len(right),
            "all_physical_completion_pairs":len(left)*len(right),
            "true_original_3x3_distinct_sampled":checked,
            "all_checked_real_incidence_minors_zero":True}


class AA4CVActualOriginalSpokeNoGo(unittest.TestCase):
    def test_01_all_dyadic_h_budget_and_algebraic_no_go(self):
        for h in range(1,27):
            z=allh_zero_spoke_arithmetic(h)
            s,V,a,H,t,N=(z[k] for k in
                ("s","V","a","H","spoke_source_factors_per_side","C4_completions_each_side"))
            self.assertEqual(V,(s+1)*(s*s+1))
            self.assertLess(comb(a-1,2),V)
            self.assertGreaterEqual(comb(a,2),V)
            self.assertEqual(H,comb(a,2)-V)
            self.assertEqual(N,(a-4)*(a-5))
            if h>=4:
                self.assertGreaterEqual(V-2-t*(s+1),t)
                self.assertLessEqual(H,2*(a-4))
                self.assertLess(4*(a-2)**2,9*s**3)
                self.assertTrue(z["constructive_local_zero_thm_all_h_ge_4"])
            else:
                self.assertFalse(z["constructive_local_zero_thm_all_h_ge_4"])
        print("AA4CV_ALLH_INTEGER_ARITHMETIC_1_TO_26_PASS",flush=True)

    def test_02_original_W316_complete_true_symplectic_witness(self):
        # REAL symplectic W(3,16) has 4369 original POINT and LINE
        # factors and 74273 actual incidence IDs. Independent source
        # geometry generator, no synthetic adjacency or probabilistic
        # approximation and NO checking 64m candidate pairs by sampling.
        field,points,lines,incidences=symplectic_gq(4)
        s=field.q
        self.assertEqual(s,16)
        V=(s+1)*(s*s+1)
        self.assertEqual((len(points),len(lines),len(incidences)),(V,V,V*(s+1)))
        pl=[set() for _ in range(V)]
        lp=[set() for _ in range(V)]
        for p,l in incidences:
            pl[p].add(l)
            lp[l].add(p)
        self.assertTrue(all(len(x)==s+1 for x in pl+lp))
        p=0
        l=next(l for l in range(V) if l not in pl[p])
        w=complete_zero_anchor_source_pairmaps(s,pl,lp,p,l)
        self.assertEqual(w["all_physical_C4_completions_per_side"],8010)
        self.assertEqual(w["all_physical_C4_pairs"],64160100)
        self.assertEqual((w["V"],w["a"],w["H"]),(4369,94,2))
        self.assertEqual(len(w["source_POINT_spokes"]),180)
        self.assertEqual(len(w["source_LINE_spokes"]),180)
        self.assertEqual(len(set(w["point_labels"])),V)
        self.assertEqual(len(set(w["line_labels"])),V)
        z=verify_combinatorial_zero_without_enumerating_quartic_pairs(w,pl)
        self.assertEqual(z["all_physical_pairs_with_zero_true_source_permanent"],64160100)
        independently=independent_zero_energy_adversarial_spoke_test(w,pl,lp,limit=42)
        self.assertEqual(independently["all_physical_completion_pairs"],64160100)
        self.assertTrue(independently["all_checked_real_incidence_minors_zero"])
        # Distinct REAL flag IDs and full typed maps retained.
        flagset=set(incidences)
        self.assertEqual(len(flagset),V*(s+1))
        self.assertTrue(all(flag in flagset for flag in w["true_original_source_P3"]))
        print("AA4CV_GENUINE_W316_ALLH_CONSTRUCTION",
              "a",94,"physical_C4_each",8010,
              "zero_minors_entire_cartesian_product",64160100,
              "independently_sampled_source_minors",
              independently["true_original_3x3_distinct_sampled"],flush=True)

    def test_03_abstract_free_source_spoke_matching_cover_is_impossible(self):
        # Combinatorial zero mechanism independent of W geometry.
        # Any 3+3 bipartite graph with 2 distinguished 'spokes' in
        # each triple and NO incidence in the 2x2 spoke rectangle
        # has zero perfect matching regardless of the other FIVE cells.
        count=0
        for mask in range(1<<9):
            mat=[[bool(mask&(1<<(3*i+j))) for j in range(3)] for i in range(3)]
            if any(mat[i][j] for i in (0,1) for j in (0,1)):
                continue
            self.assertEqual(sum(all(mat[i][p[i]] for i in range(3))
                                 for p in permutations(range(3))),0)
            count+=1
        self.assertEqual(count,1<<5)
        print("AA4CV_ALL_POSSIBLE_NON_SPOKE_3X3_ADVERSARIAL_MATRICES",count,flush=True)

    def test_04_fail_closed_dyadic_budget_and_invalid_original_inputs(self):
        for h in (0,-1,1.5,True):
            with self.assertRaises(ValueError):
                allh_zero_spoke_arithmetic(h)
        for s in (2,4,8,0,-1,12,True):
            with self.assertRaises(ValueError):
                complete_zero_anchor_source_pairmaps(s,(),(),0,0)
        z=allh_zero_spoke_arithmetic(4)
        V=z["V"]
        fake=[tuple() for _ in range(V)]
        with self.assertRaises(ValueError):
            complete_zero_anchor_source_pairmaps(16,fake,fake,0,1)
        print("AA4CV_FAIL_CLOSED_NON_ORIGINAL_INVALID_INPUT_PASS",flush=True)


if __name__=="__main__":unittest.main()
