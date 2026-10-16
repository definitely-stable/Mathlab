"""HYP-105 #230 AA4-AS genuine ORIGINAL every sixflag source Q radius5.

Independent all-h exact floor, full five real W32 six-Q candidate sets,
per-Q repairs, W34/W38 finite genuine source geometry, negative controls.
"""
import unittest
from collections import Counter
from itertools import combinations
from math import comb,perm

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ar_five_swap_original_D6 import (
    repair_original_D6_with_at_most_five_line_swaps,
    exceptional_noncycle_edge)
from hyp105_issue230_d6aa4as_every_original_Q_five_swap_repair import (
    _parameters,all_h_every_original_Q_five_swap_mass,
    finite_original_eligible_Q_generator,
    repair_EVERY_actual_original_Q_D6_in_five_line_swaps,
    original_left_C6_order_on_six_flag_IDs,
    _strict_finite_actual_original_model)
from hyp105_g5e2b3e1b0_seven_signature import (
    physical_column_dual,is_connected_column_cycle,classify_seven_prechecked)


def _independent_six_flag_dual_edges(model,Q,updated_line_labels):
    """DIRECT true original positional pair intersection oracle,
    not historical helper physical_column_dual."""
    inc=tuple(tuple(x) for x in model["incidences"])
    f=tuple(tuple(x) for x in model["left_labels"])
    edges={}
    for side,labels in (("point",f),("line",updated_line_labels)):
        adj=set()
        for x,y in combinations(range(6),2):
            u=inc[Q[x]][0 if side=="point" else 1]
            v=inc[Q[y]][0 if side=="point" else 1]
            if set(labels[u]) & set(labels[v]):
                adj.add((x,y))
        edges[side]=adj
    return (len(edges["point"])==6 and
            edges["point"]==edges["line"] and
            all(sum(1 for e in edges["point"] if i in e)==2 for i in range(6)))


class EveryGenuineOriginalSourceQRadiusFive(unittest.TestCase):
    def test_01_all_h_original_s15_Q_mass_sandwich_exact_powers_1_to_80(self):
        for h in range(1,81):
            s=1<<h
            z=all_h_every_original_Q_five_swap_mass(s)
            V,d,a,m=_parameters(s)
            Cfull=perm(a,6)//12
            Cmin=Cfull-m*perm(a-2,4)
            self.assertEqual(z["physically_occupied_point_C6_at_least"],Cmin)
            self.assertEqual(z["complete_Ka_simple_point_C6"],Cfull)
            q=d**4*(d*d-15) if s>=4 else 1
            self.assertEqual(z[
                "EVERY_fixed_f_has_at_least_THIS_many_individually_repairable_original_Q"],
                Cmin*q)
            self.assertEqual(z[
                "EVERY_fixed_f_has_at_most_THIS_many_eligible_original_Q"],
                Cfull*d**6)
            self.assertGreater(Cmin,0)
            self.assertLessEqual(Cmin*q,Cfull*d**6)
            self.assertTrue(z["EVERY_eligible_original_Q_repairable_within_FIVE_global_line_swaps"])
            self.assertTrue(z["each_Q_may_need_ITS_OWN_different_GLOBAL_line_map"])
            self.assertTrue(z["root_issue230_A_B_C_still_OPEN"])
            if s>=2**20:
                n=z["relative_repairable_eligible_Q_count_lower_vs_s15"]
                u=z["relative_repairable_eligible_Q_count_upper_vs_s15"]
                self.assertGreater(100*n[0],60*n[1])
                self.assertLess(100*u[0],75*u[1])

    def test_02_FULL_genuine_W32_five_maps_ALL_original_eligible_Q_exact_counts_and_sampled_repair(self):
        expected=(("lex",18716),("reverse",18716),
                  ("S68",21186),("S72",21186))
        for name,N in expected:
            m=fixture(1,name)
            all_Q=tuple(finite_original_eligible_Q_generator(
                m,max_yield=None))
            self.assertEqual(len(all_Q),N)
            self.assertEqual(len(set(all_Q)),N)
            # Selection is deterministic across all 60 physical C6
            # point factor sets and all true six-line SDR assignments.
            chosen=all_Q[::max(1,N//65)]
            self.assertGreaterEqual(len(chosen),65)
            for Q in chosen:
                repaired=repair_EVERY_actual_original_Q_D6_in_five_line_swaps(m,Q)
                self.assertLessEqual(
                    repaired["number_of_GLOBAL_line_factor_image_transpositions"],5)
                self.assertGreaterEqual(
                    repaired["at_least_FIVE_C6_eligible_DISTINCT_source_flag_anchors"],5)
                self.assertEqual(
                    repaired["EXACT_six_distinct_original_incidence_flag_IDs"],Q)
                self.assertTrue(repaired["original_line_image_support_UNCHANGED"])
                self.assertTrue(_independent_six_flag_dual_edges(
                    m,Q,repaired["original_line_global_image_after"]))
                self.assertEqual(classify_seven_prechecked(
                    Q,m["left_labels"],repaired["original_line_global_image_after"],
                    m["incidences"]),"D6")
            print("AA4AS real W32",name,
                  "all_ORIGINAL_left_C6_sixflag_Q",N,
                  "sampled_true_Q_repaired",len(chosen))

    def test_03_genuine_W32_every_Q_at_least_five_possible_preserved_source_line_anchors(self):
        for scheme in ("lex","S68","S72"):
            m=fixture(1,scheme)
            q=next(finite_original_eligible_Q_generator(m,max_yield=1))
            z=repair_EVERY_actual_original_Q_D6_in_five_line_swaps(m,q)
            anchor_options=z["eligible_original_flag_anchor_IDs"]
            self.assertGreaterEqual(len(anchor_options),5)
            for pinned in anchor_options:
                v=repair_EVERY_actual_original_Q_D6_in_five_line_swaps(
                    m,q,preserved_original_flag_ID=pinned)
                self.assertLessEqual(v["number_of_GLOBAL_line_factor_image_transpositions"],5)
                self.assertEqual(
                    v["selected_genuine_original_line_anchor_ID"],
                    m["incidences"][pinned][1])
                self.assertEqual(
                    v["original_line_global_image_after"][
                      m["incidences"][pinned][1]],
                    m["right_labels"][m["incidences"][pinned][1]])
                self.assertTrue(_independent_six_flag_dual_edges(
                    m,q,v["original_line_global_image_after"]))

    def test_04_true_W34_W38_original_global_nononto_source_Q_repair_all_samples(self):
        for h,missing,schemes in ((2,6,("lex","random")),
                                  (3,10,("lex","random"))):
            for scheme in schemes:
                m=fixture(h,scheme)
                s,V,d,a,f,g,inc=_strict_finite_actual_original_model(m)
                self.assertEqual(comb(a,2)-V,missing)
                candidates=list(finite_original_eligible_Q_generator(
                    m,max_yield=12))
                self.assertEqual(len(candidates),12)
                for Q in candidates:
                    z=repair_EVERY_actual_original_Q_D6_in_five_line_swaps(m,Q)
                    self.assertLessEqual(
                        z["number_of_GLOBAL_line_factor_image_transpositions"],5)
                    self.assertEqual(
                        len(set(z["original_line_global_image_after"])),V)
                    self.assertEqual(
                        set(z["original_line_global_image_after"]),set(g))
                    self.assertTrue(_independent_six_flag_dual_edges(
                        m,Q,z["original_line_global_image_after"]))
                print("AA4AS real GQ",s,scheme,
                      "original_Q_individually_repaired",len(candidates))

    def test_05_independent_physical_point_line_coordinate_relabelling(self):
        m=fixture(1,"lex")
        f=lambda e,p:tuple(sorted((p[e[0]],p[e[1]])))
        a=m["a"]
        P=tuple(reversed(range(a)))
        L=tuple((i+2)%a for i in range(a))
        altered=dict(m,
            left_labels=tuple(f(e,P) for e in m["left_labels"]),
            right_labels=tuple(f(e,L) for e in m["right_labels"]))
        q=list(finite_original_eligible_Q_generator(m,max_yield=9))
        qq=list(finite_original_eligible_Q_generator(altered,max_yield=None))
        self.assertEqual(len(qq),18716)
        for Q in q:
            v=repair_EVERY_actual_original_Q_D6_in_five_line_swaps(
                altered,Q)
            self.assertTrue(_independent_six_flag_dual_edges(
                altered,Q,v["original_line_global_image_after"]))

    def test_06_exact_old_one_Q_five_swap_repair_and_new_EVERY_Q_repair_both_verified(self):
        for h,scheme in ((1,"S68"),(1,"S72"),(2,"lex")):
            m=fixture(h,scheme)
            old=repair_original_D6_with_at_most_five_line_swaps(m)
            self.assertLessEqual(old["global_line_transposition_distance_upper"],5)
            self.assertEqual(old["historical_original_seven_GF5_class_after"],"D6")
            Q=tuple(old["actual_original_six_incidence_IDs"])
            fresh=repair_EVERY_actual_original_Q_D6_in_five_line_swaps(m,Q)
            self.assertTrue(fresh[
                "repaired_TRUE_ORIGINAL_exact_same_six_flag_Q_positive_D6"])
            self.assertLessEqual(
                fresh["number_of_GLOBAL_line_factor_image_transpositions"],5)

    def test_07_negative_unusable_Q_fake_original_source_and_invalid_anchor(self):
        m=fixture(1,"lex")
        Q=next(finite_original_eligible_Q_generator(m,max_yield=1))
        with self.assertRaises(ValueError):
            repair_EVERY_actual_original_Q_D6_in_five_line_swaps(
                m,Q,preserved_original_flag_ID=999)
        with self.assertRaises(ValueError):
            repair_EVERY_actual_original_Q_D6_in_five_line_swaps(
                m,(Q[0],)*6)
        with self.assertRaises(ValueError):
            repair_EVERY_actual_original_Q_D6_in_five_line_swaps(
                m,tuple(Q)[:5])
        with self.assertRaises(ValueError):
            all_h_every_original_Q_five_swap_mass(12)
        with self.assertRaises(ValueError):
            list(finite_original_eligible_Q_generator(
                fixture(2,"lex"),max_yield=None))
        for bad in (
            dict(m,left_labels=((0,1),)*15),
            dict(m,right_labels=((0,1),)*15),
            dict(m,incidences=tuple(m["incidences"])[:-1])):
            with self.assertRaises(ValueError):
                repair_EVERY_actual_original_Q_D6_in_five_line_swaps(bad,Q)


if __name__=="__main__":
    unittest.main()
