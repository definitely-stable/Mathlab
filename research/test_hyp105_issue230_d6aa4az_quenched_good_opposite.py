"""Independent AA4-AZ actual W32/W34 GOOD expected opposite threeflag falsifiers."""
import unittest
from itertools import combinations, permutations
from math import comb
from fractions import Fraction

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4az_quenched_good_opposite import (
    support_bad_clean_energy,
    genuine_original_fixed_point_GOOD_source_potential,
    quenched_genuine_original_GOOD_opposite_mean,
    universal_original_clean_twoport_support_floor,
)
from hyp105_issue230_d6aa4ar_good_wedges_port_balance import (
    exact_true_original_good_D_two_port_wedge_certificate,
    independent_original_literal_good_two_port_wedges,
)
from hyp105_issue230_d6aa4ay_quenched_allD_opposite_mean import (
    quenched_original_opposite_ALL_D_mean,
)


def literal_support_bad_and_clean_port_energy(support,a):
    """Fully independent missing edge from scratch, no parent helper."""
    total=set(combinations(range(a),2))
    E=set(tuple(sorted(e)) for e in support)
    assert len(E)==len(support)
    holes=total-E
    degree_miss={v:sum(v in edge for edge in holes) for v in range(a)}
    bad={v for v in range(a) if 16*degree_miss[v]>=a}
    clean={e for e in E if all(v not in bad for v in e)}
    degree={v:sum(v in edge for edge in clean) for v in range(a)}
    T=sum((degree[u]-1)*(degree[v]-1) for u,v in clean)
    return bad,clean,T


def literal_original_clean_point_triples(model):
    """Actual ORIGINAL source threeflag enumeration, without special Bgood algebra."""
    inc=tuple(tuple(x) for x in model["incidences"])
    f=tuple(tuple(sorted(x)) for x in model["left_labels"])
    s=model["s"]
    a=next(n for n in range(6,100) if comb(n,2)>=len(f))
    bad,clean,T=literal_support_bad_and_clean_port_energy(f,a)
    lines=[set() for _ in range(len(f))]
    for p,l in inc:lines[p].add(l)
    count=0
    for p,l in inc:
        if tuple(sorted(f[p])) not in clean:continue
        u,v=f[p]
        Q0=[q for q,e in enumerate(f)
            if q!=p and tuple(sorted(e)) in clean and u in e]
        Q1=[q for q,e in enumerate(f)
            if q!=p and tuple(sorted(e)) in clean and v in e]
        for q0 in Q0:
            for q1 in Q1:
                for k0 in lines[q0]:
                    if k0==l:continue
                    for k1 in lines[q1]:
                        if k1!=l and k1!=k0:
                            count+=1
    return count,T,bad


def literal_right_good_ordered_three_edge_probability(model):
    g=tuple(tuple(sorted(x)) for x in model["right_labels"])
    a=next(n for n in range(6,100) if comb(n,2)>=len(g))
    bad,clean,T=literal_support_bad_and_clean_port_energy(g,a)
    whole=len(g)*(len(g)-1)*(len(g)-2)
    successes=0
    for center in clean:
        u,v=center
        for first in clean:
            if first==center:continue
            for second in clean:
                if second==center or second==first:continue
                cp=set(center)&set(first)
                cq=set(center)&set(second)
                if len(cp)==len(cq)==1 and cp!=cq:
                    successes+=1
    return Fraction(successes,whole),T,bad


class TrueOriginalQuenchedGOODWedgeTests(unittest.TestCase):
    def test_01_exact_all_h_dyadic_clean_port_energy_and_s6_over128(self):
        for h in tuple(range(1,35))+(40,48,64,80):
            s=1<<h
            z=universal_original_clean_twoport_support_floor(s)
            self.assertEqual(z["root_230"],"OPEN_WITH_FORMAL_BLOCKER")
            self.assertFalse(z["accepted_original_7_GF5_six_ID_minimax_PROVED"])
            self.assertFalse(z["complete_FIXED_adversarial_original_right_g_minimax_PROVED"])
            if h>=5:
                self.assertTrue(z["uniform_clean_T_ge_V_squared_over_16_proved"])
                self.assertGreaterEqual(
                    z["uniform_original_GOOD_opposite_3flag_expected_lower"],
                    Fraction(s**6,128))
                self.assertGreaterEqual(
                    16*z["minimal_induced_clean_T_exact_deficit_floor"],z["V"]**2)
            else:
                self.assertFalse(z["uniform_clean_T_ge_V_squared_over_16_proved"])
        for v in (1,3,6,100):
            with self.assertRaises(ValueError):
                universal_original_clean_twoport_support_floor(v)

    def test_02_independent_W32_W34_physical_clean_bad_set_and_T(self):
        for h,name in ((1,"S68"),(1,"S72"),(1,"lex"),
                       (2,"lex"),(2,"random")):
            model=fixture(h,name)
            V=len(model["left_labels"])
            a=next(n for n in range(6,100) if comb(n,2)>=V)
            for kind in ("left_labels","right_labels"):
                val=tuple(model[kind])
                bad,edges,T=literal_support_bad_and_clean_port_energy(val,a)
                oracle=support_bad_clean_energy(val,a)
                self.assertEqual(bad,set(oracle["bad_coordinates"]))
                self.assertEqual(edges,set(oracle["clean_induced_occupied_edges"]))
                self.assertEqual(T,oracle["CLEAN_physical_two_opposite_port_root_energy"])
                self.assertLessEqual(len(bad),31)
                self.assertLessEqual(T,
                    len(val)*(a-2)**2)
        with self.assertRaises(ValueError):
            support_bad_clean_energy(((0,1),(1,0)),6)

    def test_03_genuine_W32_true_source_clean_point_opposite_triples(self):
        for name in ("S68","S72","lex","reverse"):
            m=fixture(1,name)
            z=genuine_original_fixed_point_GOOD_source_potential(m)
            direct,T,bad=literal_original_clean_point_triples(m)
            self.assertEqual(direct,z[
                "CLEAN_original_fixed_f_physical_point_opposite_true_source_3flag_count"])
            self.assertEqual(T,z["clean_point_physical_support"][
                "CLEAN_physical_two_opposite_port_root_energy"])
            self.assertGreaterEqual(direct,z["CLEAN_true_original_point_source_regular_degree_lower"])

    def test_04_genuine_W34_true_original_nononto_clean_source_triples(self):
        for name in ("lex","random"):
            m=fixture(2,name)
            z=genuine_original_fixed_point_GOOD_source_potential(m)
            direct,T,bad=literal_original_clean_point_triples(m)
            self.assertEqual(direct,z[
                "CLEAN_original_fixed_f_physical_point_opposite_true_source_3flag_count"])
            self.assertEqual(T,z["clean_point_physical_support"][
                "CLEAN_physical_two_opposite_port_root_energy"])

    def test_05_entire_W32_right_physical_ordered_clean_triple_space(self):
        for name in ("S68","S72","lex"):
            m=fixture(1,name)
            z=quenched_genuine_original_GOOD_opposite_mean(m)
            direct,T,bad=literal_right_good_ordered_three_edge_probability(m)
            self.assertEqual(direct,z[
                "exact_original_right_ordered_three_DISTINCT_line_edge_probability"])
            self.assertEqual(T,z["fixed_original_right_clean_support_port_energy"])
            self.assertEqual(z["exact_one_global_original_LINE_bijection_GOOD_opposite_wedge_mean"],
                z["fixed_original_POINT_side_TRUE_source_GOOD_opposite_triples"]*direct)
            self.assertLessEqual(z["exact_one_global_original_LINE_bijection_GOOD_opposite_wedge_mean"],
                                 quenched_original_opposite_ALL_D_mean(m)[
                                     "EXACT_quenched_uniform_ONE_full_global_original_LINE_map_ALL_D_opposite_mean"])

    def test_06_entire_real_W34_K14_holes_good_physical_ordered_triples(self):
        for name in ("lex","random"):
            m=fixture(2,name)
            z=quenched_genuine_original_GOOD_opposite_mean(m)
            direct,T,bad=literal_right_good_ordered_three_edge_probability(m)
            self.assertEqual(T,z["fixed_original_right_clean_support_port_energy"])
            self.assertEqual(direct,z[
                "exact_original_right_ordered_three_DISTINCT_line_edge_probability"])
            self.assertEqual(z["exact_one_global_original_LINE_bijection_GOOD_opposite_wedge_mean"],
                z["fixed_original_POINT_side_TRUE_source_GOOD_opposite_triples"]*direct)
            self.assertLessEqual(z["exact_one_global_original_LINE_bijection_GOOD_opposite_wedge_mean"],
                                 quenched_original_opposite_ALL_D_mean(m)[
                                     "EXACT_quenched_uniform_ONE_full_global_original_LINE_map_ALL_D_opposite_mean"])

    def test_07_TRUE_original_fixed_g_GOOD_opposite_vs_literal_flag_wedge(self):
        for h,name in ((1,"S68"),(1,"S72"),(1,"lex"),
                       (2,"lex"),(2,"random")):
            model=fixture(h,name)
            oracle=exact_true_original_good_D_two_port_wedge_certificate(model)
            literal=independent_original_literal_good_two_port_wedges(model)
            self.assertEqual(
                oracle["good_D_original_OPPOSITE_TWO_TYPED_port_wedges"],
                literal["actual_original_literal_two_type_opposite_wedges"])
            self.assertGreaterEqual(
                oracle["good_D_original_OPPOSITE_TWO_TYPED_port_wedges"],0)
            # No comparison of an adversarial fixed-g GOOD count to a
            # global-right random expectation is mathematically warranted.

    def test_08_global_original_line_swap_and_right_physical_vertex_gauge(self):
        for h,name in ((1,"S68"),(2,"lex"),(2,"random")):
            m=fixture(h,name)
            expected=quenched_genuine_original_GOOD_opposite_mean(m)
            labels=list(m["right_labels"])
            labels[0],labels[1]=labels[1],labels[0]
            perm=dict(m,right_labels=tuple(labels))
            self.assertEqual(expected["exact_one_global_original_LINE_bijection_GOOD_opposite_wedge_mean"],
                             quenched_genuine_original_GOOD_opposite_mean(perm)[
                                 "exact_one_global_original_LINE_bijection_GOOD_opposite_wedge_mean"])
            a=expected["a"]
            vperm=tuple((i+3)%a for i in range(a))
            newlabels=tuple(tuple(sorted(vperm[x] for x in e)) for e in m["right_labels"])
            relabeled=dict(m,right_labels=newlabels)
            self.assertEqual(expected["fixed_original_right_clean_support_port_energy"],
                             quenched_genuine_original_GOOD_opposite_mean(relabeled)[
                                 "fixed_original_right_clean_support_port_energy"])
            self.assertFalse(expected["given_FIXED_adversarial_original_f_g_GOOD_lower_PROVED"])

    def test_09_high_h_adversarial_missing_physical_star_or_matching(self):
        s=32
        V=(s+1)*(s*s+1)
        a=next(n for n in range(200,300) if comb(n,2)>=V)
        m=comb(a,2)-V
        all_e=set(combinations(range(a),2))
        for badshape in (
            set(combinations(range(a),2)) -set(list(sorted(all_e))[m:]),
            set(list(sorted(all_e))[:m]),
            {(0,j) for j in range(1,m+1)} if m<a else set(),
        ):
            holes=set(list(badshape)[:m])
            if len(holes)!=m:continue
            physical=tuple(sorted(all_e-holes))
            z=support_bad_clean_energy(physical,a)
            self.assertGreaterEqual(
                16*z["CLEAN_physical_two_opposite_port_root_energy"],V*V)
            self.assertLessEqual(len(z["bad_coordinates"]),31)


if __name__=="__main__":
    unittest.main()
