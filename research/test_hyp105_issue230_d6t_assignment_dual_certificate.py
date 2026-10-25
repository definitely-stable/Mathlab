"""D6-T independent exact global injection dual, Hungarian and GQ tests.

The root all-label theorem remains OPEN. A locally feasible certificate
MUST be checked against every injective local assignment and against
the global Hungarian optimum; finite true W32 controls fix left f and
all but three original right factors, not the full 15! or all h.
"""
from fractions import Fraction
from itertools import permutations,product
import unittest

from hyp105_issue230_d6t_assignment_dual_certificate import (
    DUAL_SCALE, integer_injective_assignment_min,
    verified_projected_marginal_dual,
    complete_true_original_W32_three_factor_tables,
    local_factor_objective,
    frozen_W32_assignment_dual_report,
    physical_non_two_regular_star_witness,
)
from hyp105_issue230_d6p_seven_cylinder_swap_audit import (
    cylinder_census, R3_CERTIFIED_FLOORS,
)
from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1b0_seven_signature import seven_census


def independent_brute_assignment_min(matrix):
    n=len(matrix)
    return min((sum(matrix[i][p[i]] for i in range(n)),p)
               for p in permutations(range(len(matrix[0])),n))


def independent_brute_global_two_side_min(factors,nL,mL,nR,mR):
    candidatesL=list(permutations(range(mL),nL))
    candidatesR=list(permutations(range(mR),nR))
    result=None
    for x,y in product(candidatesL,candidatesR):
        value=sum(f["costs"][(
                tuple(x[v] for v in f["L"]),
                tuple(y[v] for v in f["R"]))]
                  for f in factors)
        if result is None or value<result:
            result=value
    return result


class GlobalProjectedAssignmentDualTests(unittest.TestCase):
    def test_independent_rectangular_Hungarian_against_every_injection(self):
        matrices=[
            [[4,2,1],[2,0,5]],
            [[10,-3,-7],[-2,8,1],[6,-4,9]],
            [[5,3,3,2],[0,4,7,2],[1,5,2,3]],
            [[12]],[[1,1,1,1],[1,1,1,1]],
            [[100,-10],[30,7]],
        ]
        for matrix in matrices:
            with self.subTest(matrix=matrix):
                actual,assignment=integer_injective_assignment_min(matrix)
                brute=min(independent_brute_assignment_min(matrix)[0],
                          min(sum(matrix[i][p[i]] for i in range(len(matrix)))
                              for p in permutations(
                                  range(len(matrix[0])),len(matrix))))
                self.assertEqual(actual,brute)
                self.assertEqual(len(set(assignment)),len(matrix))
                self.assertEqual(
                    actual,sum(matrix[i][j] for i,j in enumerate(assignment)))
        self.assertEqual(integer_injective_assignment_min([]),(0,()))

    def test_actual_global_injectivity_recovers_positive_sum_of_zero_min_factors(self):
        """Three singleton factors all individually have minimum zero.

        Their sum is exactly 1 for every COMPLETE right bijection:
        exactly one right original factor receives image 0. A solver
        ignoring the physical image all-different constraint reports
        the unsound value zero. Hungarian forces 1.
        """
        factors=[]
        for i in range(3):
            factors.append({
                "L":(),"R":(i,),
                "costs":{((),(e,)):int(e==0) for e in range(3)}
            })
        dual=verified_projected_marginal_dual(
            (),0,(0,1,2),3,factors)
        self.assertEqual(dual["local_independent_minima_sum"],0)
        self.assertEqual(dual["global_assignment_dual_lower"],"1")
        self.assertEqual(dual["global_assignment_dual_integer_floor"],1)
        self.assertEqual(
            dual["minimum_right_injective_assignment_potential_scaled"],
            DUAL_SCALE)
        self.assertEqual(independent_brute_global_two_side_min(
            factors,0,0,3,3),1)
        self.assertTrue(dual["complete_local_truth_tables_required"])
        self.assertTrue(dual["globally_injective_both_factor_sides"])

    def test_exact_dual_honestly_misses_parity_third_order_frustration(self):
        """Proof-scope NO-GO: one-site projection cannot capture parity.

        One third-order term charges odd permutations and a second
        charges even permutations; sum is identically 1 globally, but
        every one-site projection minimum of each factor is 0.
        """
        all_perm=list(permutations(range(3)))
        def parity(p):
            return sum(p[i]>p[j] for i in range(3)
                       for j in range(i+1,3))%2
        factors=[
            {"L":(),"R":(0,1,2),"costs":{
                ((),p): int(parity(p)==flag) for p in all_perm}}
            for flag in (0,1)
        ]
        dual=verified_projected_marginal_dual(
            (),0,(0,1,2),3,factors)
        self.assertEqual(dual["global_assignment_dual_lower"],"0")
        self.assertEqual(dual["max_single_site_potential_scaled"],0)
        self.assertEqual(independent_brute_global_two_side_min(
            factors,0,0,3,3),1)
        self.assertLess(Fraction(
            dual["global_assignment_dual_lower"]),1)

    def test_both_original_factor_sides_are_independent_injections(self):
        factors=[]
        for side in ("L","R"):
            for original_id in range(2):
                factors.append({
                    "L":(original_id,) if side=="L" else (),
                    "R":(original_id,) if side=="R" else (),
                    "costs":{
                        ((e,),()) if side=="L" else ((),(e,)):int(e==0)
                        for e in range(2)},
                })
        dual=verified_projected_marginal_dual(
            (0,1),2,(0,1),2,factors)
        self.assertEqual(dual["global_assignment_dual_lower"],"2")
        self.assertEqual(independent_brute_global_two_side_min(
            factors,2,2,2,2),2)
        self.assertEqual(
            dual["minimum_left_injective_assignment_potential_scaled"],
            DUAL_SCALE)
        self.assertEqual(
            dual["minimum_right_injective_assignment_potential_scaled"],
            DUAL_SCALE)
        self.assertEqual(dual["local_truth_rows_verified"],8)

    def test_constructive_all_h_original_two_sided_one_site_dual_no_go(self):
        """Every site projection has a zero via the OPPOSITE side.

        Check actual W32 original incidences with physical A/B/C left
        types. The construction is valid for arbitrary h with a>=6.
        This invalidates sitewise-only global certification, NOT Branch A.
        """
        from hyp105_g5e2b3e1a_fixed_leading import selected_left_six
        for scheme in ("lex","S68"):
            model=fixture(1,scheme)
            chosen={}
            for ids,kind in selected_left_six(model):
                if kind not in chosen:
                    chosen[kind]=ids
                if len(chosen)==3:
                    break
            self.assertEqual(set(chosen),{"A","B","C"})
            for kind,ids in chosen.items():
                original_points=tuple(model["incidences"][i][0]
                                      for i in ids)
                original_lines=tuple(model["incidences"][i][1]
                                     for i in ids)
                for side,indices in (("left",original_points),
                                     ("right",original_lines)):
                    with self.subTest(scheme=scheme,kind=kind,side=side):
                        for a in (6,14,35):
                            witness=physical_non_two_regular_star_witness(
                                indices,a)
                            self.assertTrue(witness[
                                "all_seven_GF5_classes_on_this_side_impossible"])
                            degrees=witness["physical_degree_multiset"]
                            self.assertFalse(len(degrees)==6 and
                                             all(d==2 for d in degrees))
                            self.assertEqual(
                                witness["root_two_sided_single_site_projection_min"],
                                "ZERO")
        with self.assertRaises(ValueError):
            physical_non_two_regular_star_witness((0,1),6)
        with self.assertRaises(ValueError):
            physical_non_two_regular_star_witness((0,1,2,3,4,5),5)

    def test_full_truth_table_verification_is_fail_closed(self):
        valid={
            "L":(),"R":(0,1),
            "costs":{((),p):i for i,p in enumerate(
                permutations(range(3),2))}
        }
        def solve(factors):
            return verified_projected_marginal_dual(
                (),0,(0,1,2),3,factors)
        self.assertGreaterEqual(
            Fraction(solve([valid])["global_assignment_dual_lower"]),0)
        missing=dict(valid)
        missing["costs"]=dict(valid["costs"])
        del missing["costs"][next(iter(missing["costs"]))]
        with self.assertRaises(ValueError):
            solve([missing])
        negative=dict(valid);negative["costs"]=dict(valid["costs"])
        negative["costs"][((),(0,1))]=-1
        with self.assertRaises(ValueError):
            solve([negative])
        invalid=dict(valid);invalid["costs"]=dict(valid["costs"])
        del invalid["costs"][((),(0,1))]
        invalid["costs"][((),(1,1))]=0
        with self.assertRaises(ValueError):
            solve([invalid])
        with self.assertRaises(ValueError):
            verified_projected_marginal_dual(
                (),0,(0,1,2),3,[valid],max_local_truth_rows=5)
        with self.assertRaises(ValueError):
            verified_projected_marginal_dual(
                (),0,(0,1,2),2,[valid])
        with self.assertRaises(ValueError):
            integer_injective_assignment_min([[1,2],[3]])
        with self.assertRaises(ValueError):
            integer_injective_assignment_min([[1],[2]])

    def test_true_original_W32_all_six_local_suborbit_costs_and_dual_sound(self):
        for scheme,T in (("S68",(3,11,12)),("S72",(1,7,9))):
            with self.subTest(scheme=scheme):
                model=fixture(1,scheme)
                triple,labels,image,compiled,factors_S,factors_GF5=(
                    complete_true_original_W32_three_factor_tables(model,T))
                self.assertEqual(compiled["original_left_sixsets"],62370)
                self.assertEqual(len(factors_S),len(factors_GF5))
                self.assertLessEqual(len(factors_S),8)
                dual_S=verified_projected_marginal_dual(
                    (),0,triple,3,factors_S)
                dual_GF5=verified_projected_marginal_dual(
                    (),0,triple,3,factors_GF5)
                orbit=[]
                for phi in permutations(range(3)):
                    changed=list(labels)
                    for orig,e in zip(triple,phi):
                        changed[orig]=image[e]
                    self.assertEqual(len(set(changed)),15)
                    actual=cylinder_census(compiled,changed)
                    S=local_factor_objective(factors_S,triple,phi)
                    Y=local_factor_objective(factors_GF5,triple,phi)
                    self.assertEqual((S,Y),(
                        actual["S_seven"],
                        actual["GF5_seven_lower_numerator"]))
                    orbit.append((S,Y,phi))
                self.assertEqual(
                    min(z[0] for z in orbit),68)
                nonidentity_min=min(
                    z[0] for z in orbit if z[2]!=(0,1,2))
                if scheme=="S68":
                    self.assertGreater(nonidentity_min,68)
                else:
                    self.assertEqual(nonidentity_min,68)
                self.assertLessEqual(
                    Fraction(dual_S["global_assignment_dual_lower"]),68)
                self.assertLessEqual(
                    Fraction(dual_GF5["global_assignment_dual_lower"]),
                    min(z[1] for z in orbit))
                source=seven_census(model,independent_checks=False)
                self.assertEqual(
                    local_factor_objective(factors_S,triple,(0,1,2)),
                    source["S_seven"])
                self.assertEqual(
                    local_factor_objective(factors_GF5,triple,(0,1,2)),
                    source["GF5_seven_lower_numerator"])

    def test_independent_true_original_S72_72_to_68_conditioned_witness(self):
        model=fixture(1,"S72")
        triple,labels,image,compiled,factors_S,factors_GF5=(
            complete_true_original_W32_three_factor_tables(model,(1,7,9)))
        # Reverse orientation: u<-old(w),v<-old(u),w<-old(v)
        reverse=(2,0,1)
        changed=list(labels)
        for orig,e in zip(triple,reverse):
            changed[orig]=image[e]
        newer=dict(model);newer["right_labels"]=tuple(changed)
        baseline=seven_census(model,independent_checks=False)
        witnessed=seven_census(newer,independent_checks=False)
        self.assertEqual(
            (baseline["S_seven"],witnessed["S_seven"]),(72,68))
        self.assertEqual(
            witnessed["GF5_seven_lower_numerator"]-
            baseline["GF5_seven_lower_numerator"],-179530)
        self.assertEqual(
            local_factor_objective(factors_S,triple,reverse),68)
        self.assertEqual(
            local_factor_objective(factors_GF5,triple,reverse),
            witnessed["GF5_seven_lower_numerator"])


if __name__=="__main__":
    unittest.main()
