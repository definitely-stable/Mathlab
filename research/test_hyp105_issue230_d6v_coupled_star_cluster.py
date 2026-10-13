"""HYP-105 D6-V independent local-to-global star and coupled cluster audit."""
import unittest
from itertools import combinations, permutations, product
from collections import Counter

from hyp105_issue230_d6v_coupled_star_cluster import (
    star_zero_family,exact_cluster_min,coupled_partition_certificate,
    frozen_original_W32_coupling_report,
)
from hyp105_issue230_projection import fixture
from hyp105_issue230_proof_audit import parameters
from hyp105_issue230_d6t_assignment_dual_certificate import (
    complete_true_original_W32_three_factor_tables, local_factor_objective,
)
from hyp105_g5e2b3e1a_fixed_leading import selected_left_six
from hyp105_issue230_d6p_seven_cylinder_swap_audit import (
    _signature_for_original_sixset, cylinder_seven_class,
)


def independent_deg_bad(incidences, side, labels):
    deg=Counter(c for pair in incidences for c in labels[pair[side]])
    return len(deg)!=6 or any(v!=2 for v in deg.values())


def brute_primal(factors, nL,mL,nR,mR):
    optimum=None
    for f,g in product(permutations(range(mL),nL),
                       permutations(range(mR),nR)):
        total=sum(factor["costs"][(
             tuple(f[i] for i in factor["L"]),
             tuple(g[i] for i in factor["R"]))]
             for factor in factors)
        optimum=total if optimum is None or total<optimum else optimum
    return optimum


class D6VCoupledStarTests(unittest.TestCase):
    def test_star_constructs_global_two_sided_injections_s2_s4_s8(self):
        for h,cluster_count in ((1,1),(2,2),(3,5)):
            model=fixture(h,"lex")
            p=parameters(2**h)
            edges=tuple(tuple(x) for x in model["incidences"])
            self.assertEqual(len(edges),p["V"]*(p["s"]+1))
            if h == 1:
                # At a=6 the star has five edges: use a true ORIGINAL
                # B-left sixset with exactly five distinct left sites.
                ids=next(ids for ids,kind in selected_left_six(model) if kind=="B")
                cluster=(tuple(edges[i] for i in ids),)
            else:
                cluster=tuple(tuple(edges[k*6:k*6+6])
                              for k in range(cluster_count))
            w=star_zero_family(2**h,cluster)
            self.assertEqual(w["star_side"],"left")
            self.assertEqual(len(w["complete_left_injection"]),p["V"])
            self.assertEqual(len(w["complete_right_injection"]),p["V"])
            for labels in (w["complete_left_injection"],
                           w["complete_right_injection"]):
                self.assertEqual(len(set(labels)),p["V"])
                self.assertTrue(all(0<=x<y<p["a"] for x,y in labels))
            for Q in cluster:
                self.assertTrue(independent_deg_bad(
                    Q,0,w["complete_left_injection"]))
            self.assertTrue(w["all_seven_GF5_contributions_zero"])
            self.assertTrue(w["selected_nonnegative_GF5_numerator_zero"])
            if h>=2:
                self.assertGreaterEqual(p["a"]-1,6*cluster_count)
            else:
                self.assertEqual(w["union_original_points"],5)

    def test_real_W32_two_B_original_sixsets_share_five_original_points(self):
        model=fixture(1,"S68")
        incidence=tuple(model["incidences"])
        found={}
        pair=None
        for ids,kind in selected_left_six(model):
            if kind!="B":
                continue
            Q=tuple(incidence[i] for i in ids)
            support=tuple(sorted({p for p,l in Q}))
            self.assertEqual(len(support),5)
            if support in found:
                pair=(found[support],Q)
                break
            found[support]=Q
        self.assertIsNotNone(pair)
        self.assertNotEqual(set(pair[0]),set(pair[1]))
        w=star_zero_family(2,pair)
        self.assertEqual(w["union_original_points"],5)
        self.assertEqual(w["original_sixsets_count"],2)
        self.assertTrue(all(independent_deg_bad(Q,0,w["complete_left_injection"])
                            for Q in pair))
        # This explicitly preserves the ORIGINAL incidence columns and physical
        # pair labels for the right side, rather than projecting factor sets.
        for Q in pair:
            self.assertEqual(len(Q),6)
            self.assertEqual(len(set(Q)),6)

    def test_adversarial_right_side_star_and_scope_failure(self):
        # Family has >a-1 ORIGINAL points but <=a-1 ORIGINAL lines.
        Q=(
            ((0,0),(1,0),(2,0),(3,1),(4,1),(5,1)),
            ((6,2),(7,2),(8,2),(9,3),(10,3),(11,3)),
        )
        w=star_zero_family(2,Q)
        self.assertEqual(w["star_side"],"right")
        self.assertTrue(all(independent_deg_bad(q,1,w["complete_right_injection"])
                            for q in Q))
        with self.assertRaises(ValueError):
            star_zero_family(2,[])
        with self.assertRaises(ValueError):
            star_zero_family(2,(tuple((i,i) for i in range(6)),))
        with self.assertRaises(ValueError):
            star_zero_family(2,(tuple((16,i) for i in range(6)),))
        # Both typed unions >5 and valid as six-edge forests.
        Qa=tuple((i,i) for i in range(6))
        Qb=tuple((6+i,6+i) for i in range(6))
        with self.assertRaisesRegex(ValueError,"both factor unions"):
            star_zero_family(2,(Qa,Qb))

    def test_independent_synthetic_coupled_parity_frustration(self):
        # Every factor individually has 0 minimum, but their SUM is 1.
        permutations3=list(permutations(range(3)))
        def parity(p):
            return sum(p[i]>p[j] for i in range(3)
                       for j in range(i+1,3))%2
        factors=[{"L":(),"R":(0,1,2),
                  "costs":{((),p):int(parity(p)==bit)
                           for p in permutations3}} for bit in (0,1)]
        singleton=coupled_partition_certificate(factors,0,0,3,3,
                                                max_cluster_size=1)
        coupled=coupled_partition_certificate(factors,0,0,3,3,
                                              max_cluster_size=2)
        self.assertEqual(singleton["exact_coupled_cluster_lower"],0)
        self.assertEqual(coupled["exact_coupled_cluster_lower"],1)
        self.assertEqual(coupled["strict_gain_over_singletons"],1)
        self.assertEqual(brute_primal(factors,0,0,3,3),1)
        self.assertEqual(exact_cluster_min(factors,(0,1),0,3)[0],1)

    def test_two_sided_independent_cluster_bound_finite_exact(self):
        # Costs couple BOTH ORIGINAL typed alphabets.
        factors=[
            {"L":(0,),"R":(0,), "costs":{
                ((i,),(j,)):int(i==j) for i in range(2) for j in range(2)}},
            {"L":(0,),"R":(0,), "costs":{
                ((i,),(j,)):int(i!=j) for i in range(2) for j in range(2)}},
            {"L":(1,),"R":(1,), "costs":{
                ((i,),(j,)):int(i==j) for i in range(2) for j in range(2)}},
        ]
        baseline=coupled_partition_certificate(factors,2,2,2,2,
                                               max_cluster_size=1)
        tight=coupled_partition_certificate(factors,2,2,2,2,
                                            max_cluster_size=2)
        exact=brute_primal(factors,2,2,2,2)
        self.assertGreaterEqual(tight["exact_coupled_cluster_lower"],
                                baseline["exact_coupled_cluster_lower"])
        self.assertLessEqual(tight["exact_coupled_cluster_lower"],exact)
        self.assertEqual(tight["exact_coupled_cluster_lower"],1)
        self.assertEqual(exact,1)

    def test_fail_closed_on_incomplete_or_invalid_coupled_tables(self):
        f={"L":(),"R":(0,1),"costs":{
            ((),a):1 for a in permutations(range(3),2)}}
        def run(factor):
            return coupled_partition_certificate(
                [factor],0,0,2,3,max_cluster_size=1)
        self.assertEqual(run(f)["exact_coupled_cluster_lower"],1)
        for bad in ("missing","extra","negative","bool"):
            altered={**f,"costs":dict(f["costs"])}
            if bad=="missing":
                altered["costs"].pop(next(iter(altered["costs"])))
            elif bad=="extra":
                altered["costs"][((),(0,0))]=0
            elif bad=="negative":
                altered["costs"][((),(0,1))]=-1
            else:
                altered["costs"][((),(0,1))]=True
            with self.assertRaises(ValueError):
                run(altered)
        with self.assertRaises(ValueError):
            coupled_partition_certificate(
                [f],0,0,2,3,max_cluster_size=2)
        with self.assertRaises(ValueError):
            coupled_partition_certificate(
                [f],0,0,2,3,max_cluster_size=1,max_rows=5)

    def test_genuine_ORIGINAL_W32_complete_right_3_permutation_cluster_orbits(self):
        results=frozen_original_W32_coupling_report()
        self.assertEqual([r["scheme"] for r in results],["S68","S72"])
        for r in results:
            self.assertEqual(r["true_original_left_sixsets"],62370)
            self.assertEqual(r["right_permutations"],6)
            for objective in r["objectives"].values():
                self.assertTrue(objective["all_right_outside_triple_frozen"])
                lower=[objective["orders"][str(k)]["exact_coupled_cluster_lower"]
                       for k in (1,2,3)]
                exact=objective["exact_full_three_permutation_min"]
                self.assertTrue(0<=lower[0]<=lower[1]<=lower[2]<=exact)
                self.assertEqual(
                    objective["orders"]["1"]["exact_singleton_minima_sum"],
                    lower[0])
                for k in (1,2,3):
                    z=objective["orders"][str(k)]
                    self.assertEqual(sum(z["local_cluster_joint_minima"]),
                                     z["exact_coupled_cluster_lower"])
                    self.assertEqual(sorted(i for group in z["partition"]
                                            for i in group),
                                     list(range(z["factors_verified"])))
            self.assertEqual(r["objectives"]["S_seven"][
                "exact_full_three_permutation_min"],68)


if __name__=="__main__":
    unittest.main()
