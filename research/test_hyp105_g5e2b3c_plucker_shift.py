"""Independent Pluecker-basis, GF(2^h) Frobenius and D_s model audits."""
from itertools import combinations
from collections import Counter
import unittest

from hyp105_b1_symplectic import GF2Power, symplectic_gq
from hyp105_g5e2b3c_plucker_shift import (
    plucker_wedge, exact_isotropic_klein_check, canonical_line_pluckers,
    incidence_shift_histogram, rank_labels, plucker_shift_model, SCHEMES,
)
from hyp105_g5e2b3b2_coincident_cycles import (
    exact_coincident_c6, independent_brute_small_incidence,
)


class PluckerShiftTests(unittest.TestCase):
    def test_wedge_changes_of_basis_and_isotropic_equations(self):
        for h in (1,2):
            field,points,lines,incidence=symplectic_gq(h)
            keys=canonical_line_pluckers(field,points,lines)
            self.assertEqual(len(set(keys)),len(lines))
            for line,key in zip(lines,keys):
                self.assertTrue(exact_isotropic_klein_check(key,field))
                for i,j in combinations(line,2):
                    self.assertEqual(
                        plucker_wedge(points[i],points[j],field),key)
                self.assertEqual(key[1],key[4]) # W(3,q) symplectic condition
                frob=tuple(field.mul(w,w) for w in key)
                self.assertTrue(exact_isotropic_klein_check(frob,field))
            self.assertEqual(len(set(keys)),len(points))

    def test_plucker_rejects_dependent_and_invalid(self):
        field=GF2Power(2)
        with self.assertRaises(ValueError):
            plucker_wedge((0,0,0,0),(0,0,0,1),field)
        with self.assertRaises(ValueError):
            plucker_wedge((1,0,0,0),(1,0,0,0),field)
        with self.assertRaises(ValueError):
            plucker_wedge((1,0,0,0),(4,1,0,0),field)
        with self.assertRaises(ValueError):
            rank_labels(field,[(1,0,0,0)],[(0,)],[],SCHEMES[0])

    def test_minimum_incidence_shift_is_pigeonhole_theorem(self):
        # Independent 7x7 degree-three circulant regular bipartite fixture.
        n=7
        points=tuple(range(n))
        line_order=(3,1,6,0,5,2,4)
        line_rank={v:i for i,v in enumerate(line_order)}
        edges=tuple((p,l) for p in points for l in (
            p,(p+1)%n,(p+3)%n))
        hist=incidence_shift_histogram(
            points,tuple(line_rank[i] for i in range(n)),edges)
        self.assertEqual(sum(hist),21)
        self.assertLessEqual(min(hist),3)
        for k in range(n):
            direct=sum(1 for p,l in edges
                       if p==(line_rank[l]+k)%n)
            self.assertEqual(hist[k],direct)
        with self.assertRaises(ValueError):
            incidence_shift_histogram((0,0,1),(0,1,2),())

    def test_all_original_incidence_equality_matches_selected_shift(self):
        for h in (1,2):
            field,points,lines,incidences=symplectic_gq(h)
            for scheme in SCHEMES:
                model=plucker_shift_model(h,scheme)
                ranks=rank_labels(field,points,lines,incidences,scheme)
                histogram=ranks["shift_histogram"]
                self.assertEqual(sum(histogram),model["N"])
                exact=sum(
                    model["left_labels"][p]==model["right_labels"][l]
                    for p,l in incidences)
                self.assertEqual(exact,model["actual_incidence_pair_equalities"])
                self.assertEqual(exact,histogram[model["plucker_shift"]])
                self.assertEqual(len(set(model["left_labels"])),model["v"])
                self.assertEqual(len(set(model["right_labels"])),model["v"])
                self.assertEqual(len(set(model["supports"])),model["N"])
                self.assertEqual(model["N"],model["v"]*(model["s"]+1))
                if scheme.endswith("-mincollision"):
                    self.assertTrue(model["all_h_nonalignment_theorem_proved"])
                    self.assertTrue(model["no_incidence_aligned_perfect_matching"])
                    self.assertLessEqual(exact,model["s"]+1)
                    self.assertLess(exact,model["v"])
                else:
                    self.assertFalse(model["all_h_nonalignment_theorem_proved"])
                    self.assertTrue(model["no_incidence_aligned_perfect_matching"])
                self.assertFalse(model["all_h_R2_bound_proved"])
                self.assertFalse(model["all_h_R3_upper_bound_proved"])

    def test_Gf2_actual_D_s_with_independent_small_subset_brute(self):
        for scheme in SCHEMES:
            model=plucker_shift_model(1,scheme)
            full=exact_coincident_c6(model)
            witnesses=full["witness_column_ids_in_canonical_left_cycle_order"]
            if witnesses:
                indices=list(witnesses[0])
                indices += [i for i in range(model["N"])
                            if i not in indices][:7]
            else:
                indices=list(range(13))
            sub=dict(model)
            sub["incidences"]=tuple(model["incidences"][i] for i in indices)
            sub["N"]=len(indices)
            optimized=exact_coincident_c6(sub)
            independent=independent_brute_small_incidence(sub)
            self.assertEqual(
                optimized["exact_coincident_C6_factor_matchings_D"],
                independent["D"])
            self.assertEqual(full["left_physical_C6_cycles_examined"],60)
            self.assertFalse(full["strict_R3_exponent_proved"])

    def test_Gf4_one_candidate_full_true_GF5_event_witness(self):
        model=plucker_shift_model(2,SCHEMES[0])
        result=exact_coincident_c6(model)
        self.assertEqual(result["left_physical_C6_cycles_examined"],121320)
        self.assertEqual(result["exact_coincident_C6_factor_matchings_D"],9190)
        self.assertEqual(model["plucker_shift"],29)
        self.assertEqual(model["actual_incidence_pair_equalities"],1)
        for witness in result["witness_column_ids_in_canonical_left_cycle_order"]:
            self.assertEqual(len(set(witness)),6)
            coord=[0]*model["m"]
            for j,col in enumerate(witness):
                p,l=model["incidences"][col]
                for x in model["left_labels"][p]:
                    coord[x] += 1 if j%2==0 else -1
                for x in model["right_labels"][l]:
                    coord[model["a"]+x] += 1 if j%2==0 else -1
            self.assertTrue(all(v%5==0 for v in coord))
        self.assertFalse(result["new_ASET_exponent_proved"])

    def test_exact_Gf4_plucker_controls_falsify_incidence_as_risk_proxy(self):
        frob=plucker_shift_model(2,"plucker-frobenius-mincollision")
        zero=plucker_shift_model(2,"plucker-lex-zero")
        self.assertEqual((frob["plucker_shift"],
                          frob["actual_incidence_pair_equalities"]),(15,1))
        self.assertEqual((zero["plucker_shift"],
                          zero["actual_incidence_pair_equalities"]),(0,9))
        frob_D=exact_coincident_c6(frob)[
            "exact_coincident_C6_factor_matchings_D"]
        zero_D=exact_coincident_c6(zero)[
            "exact_coincident_C6_factor_matchings_D"]
        self.assertEqual(frob_D,9109)
        self.assertEqual(zero_D,9103)
        # First scheme proved (min E=1, D=9190) in the GF4 witness test:
        # fewer aligned factor incidences can have MORE forbidden cycles.
        self.assertLess(1,zero["actual_incidence_pair_equalities"])
        self.assertLess(zero_D,9190)
        self.assertFalse(zero["all_h_R3_upper_bound_proved"])
        self.assertFalse(frob["all_h_R2_bound_proved"])

    def test_fail_closed_power_invalid_scheme(self):
        with self.assertRaises(ValueError):
            plucker_shift_model(3,SCHEMES[0])
        with self.assertRaises(ValueError):
            plucker_shift_model(1,"fake")


if __name__=="__main__":
    unittest.main()
