"""AA4-AY independent true source incidence and physical right-triple falsifiers."""
import unittest
from itertools import permutations,combinations
from math import comb
from fractions import Fraction
from collections import Counter

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ay_quenched_allD_opposite_mean import (
    physical_edge_port_energy,exact_original_source_point_opposite_potential,
    quenched_original_opposite_ALL_D_mean,
    dyadic_every_original_spectral_free_quenched_certificate,
    actual_original_ALL_D_opposite_wedges_direct,
)
from hyp105_issue230_d6aa4av_global_source_aa_good_wedges import (
    exact_original_corrected_two_type_four_bin_transport,
)


def independent_right_triple_assignment_probability(E):
    """Physical brute count over ALL ordered 3-edge images, not formula."""
    total=0
    for central,left,right in permutations(E,3):
        cu,cv=central
        a=set(central)&set(left)
        b=set(central)&set(right)
        if len(a)==len(b)==1 and a!=b:
            total+=1
    return Fraction(total,len(E)*(len(E)-1)*(len(E)-2))


def independent_original_source_threeflag_point_opposite(model):
    """LITERAL source triple, no source theorem potential helper called."""
    inc=tuple(tuple(v) for v in model["incidences"])
    f=tuple(tuple(x) for x in model["left_labels"])
    val=0
    for p,l in inc:
        u,v=f[p]
        port0=[];port1=[]
        for q,k in inc:
            if p==q or l==k:
                continue
            if len({p,q})!=2:
                raise AssertionError("not genuinely distinct original point factors")
            edge=set(f[q])
            if u in edge:port0.append((q,k))
            elif v in edge:port1.append((q,k))
        for q0,k0 in port0:
            for q1,k1 in port1:
                if q0!=q1 and k0!=k1:
                    val+=1
    return val


class ExactTrueOriginalQuenchedOppositeALLDTests(unittest.TestCase):
    def test_01_all_h_integer_physical_energy_lower_and_s6_over2(self):
        for h in tuple(range(1,36))+(40,48,64,80):
            z=dyadic_every_original_spectral_free_quenched_certificate(1<<h)
            self.assertGreaterEqual(
                z["uniform_original_ALL_D_opposite_physical_threeflag_expectation_lower"],
                Fraction((1<<h)**6,2))
            self.assertTrue(z["given_adversarial_FIXED_g_minimax_NOT_PROVED"])
            self.assertTrue(z["physical_port_GOOD_subset_mean_NOT_PROVED"])
            self.assertTrue(z["accepted_historical_seven_GF5_six_ID_NOT_PROVED"])
            self.assertEqual(z["root_230"],"OPEN_WITH_FORMAL_BLOCKER")
            if h>1:
                self.assertGreaterEqual(
                    2*z["universal_occupied_physical_port_edge_energy_lower"],
                    z["original_point_and_line_source_factor_count"]**2)
        for s in (1,3,6,12):
            with self.assertRaises(ValueError):
                dyadic_every_original_spectral_free_quenched_certificate(s)

    def test_02_all_original_W32_literal_three_flag_potential_independent(self):
        for scheme in ("S68","S72","lex","reverse"):
            model=fixture(1,scheme)
            x=exact_original_source_point_opposite_potential(model)
            direct=independent_original_source_threeflag_point_opposite(model)
            self.assertEqual(x["point_opposite_centered_3distinct_original_source_incidence_triples"],direct)
            self.assertEqual(x["actual_original_source_center_incidence_flag_count"],45)
            self.assertEqual(len(x["per_actual_original_center_incidence_ID_candidate_counts"]),45)
            self.assertGreaterEqual(direct,x["point_opposite_triples_source_only_genuine_lower"])

    def test_03_true_original_W34_nononto_source_threeflag_potential(self):
        for scheme in ("lex","random"):
            model=fixture(2,scheme)
            x=exact_original_source_point_opposite_potential(model)
            direct=independent_original_source_threeflag_point_opposite(model)
            self.assertEqual(x["point_opposite_centered_3distinct_original_source_incidence_triples"],direct)
            self.assertEqual(x["actual_original_source_center_incidence_flag_count"],425)
            self.assertEqual((x["a"],x["m"]),(14,6))
            self.assertGreaterEqual(direct,x["point_opposite_triples_source_only_genuine_lower"])

    def test_04_all_W32_K6_physical_ordered_triples_exact_probability(self):
        for scheme in ("S68","S72","lex"):
            model=fixture(1,scheme)
            z=quenched_original_opposite_ALL_D_mean(model)
            e=tuple(model["right_labels"])
            exact=independent_right_triple_assignment_probability(e)
            self.assertEqual(exact,z["two_opposite_right_physical_ports_joint_probability"])
            self.assertEqual(
                z["EXACT_quenched_uniform_ONE_full_global_original_LINE_map_ALL_D_opposite_mean"],
                exact*z["original_point_global_f_specific_source_threeflag_potential"])
            self.assertTrue(z["uniform_in_both_adversarial_supports_R_ALL_D_mean_lower"]>=
                            Fraction(2**6,2))

    def test_05_W34_K14_with_six_holes_independent_all_right_triples(self):
        for scheme in ("lex","random"):
            model=fixture(2,scheme)
            z=quenched_original_opposite_ALL_D_mean(model)
            self.assertEqual(len(model["right_labels"]),85)
            prob=independent_right_triple_assignment_probability(tuple(model["right_labels"]))
            self.assertEqual(prob,z["two_opposite_right_physical_ports_joint_probability"])
            self.assertEqual(
                z["EXACT_quenched_uniform_ONE_full_global_original_LINE_map_ALL_D_opposite_mean"],
                prob*z["original_point_global_f_specific_source_threeflag_potential"])
            self.assertGreaterEqual(z["uniform_in_both_adversarial_supports_R_ALL_D_mean_lower"],
                                    Fraction(4**6,2))

    def test_06_actual_fixed_original_g_ALL_D_opposite_vs_independent_transport(self):
        for h,scheme in ((1,"S68"),(1,"S72"),(1,"lex"),(2,"lex"),(2,"random")):
            model=fixture(h,scheme)
            direct=actual_original_ALL_D_opposite_wedges_direct(model)
            historic=exact_original_corrected_two_type_four_bin_transport(model)
            self.assertEqual(
                direct,historic["genuine_original_ALL_D_two_typed_physically_opposite_wedges"])
            self.assertGreaterEqual(direct,0)

    def test_07_fully_injected_physical_edge_deletion_adversarial_extremes(self):
        for a,m in ((6,0),(10,8),(14,6),(18,16)):
            K=comb(a,2)
            total=list(combinations(range(a),2))
            for holes in (total[:m],total[-m:] if m else [],
                          [(0,i) for i in range(2,m+2)] if m<=a-2 else []):
                e=tuple(x for x in total if x not in set(holes))
                V=len(e)
                if comb(a,2)-V!=m:
                    continue
                observed=physical_edge_port_energy(e,a)
                lower=V*(a-2)**2-2*m*(a-1)*(a-2)
                self.assertGreaterEqual(observed,lower)
                if a>=14:
                    self.assertGreaterEqual(2*observed,V*V)
        with self.assertRaises(ValueError):
            physical_edge_port_energy(((0,1),(1,0)),4)

    def test_08_exact_original_W32_W34_fixed_g_vs_quenched_mean_REGRESSION(self):
        certified=(
            (1,"S68",697,Fraction(87056,91),Fraction(23040,91)),
            (1,"S72",750,Fraction(87056,91),Fraction(23040,91)),
            (1,"lex",1105,Fraction(88992,91),Fraction(23040,91)),
            (2,"lex",49742,Fraction(471930840,9877),Fraction(214990848,9877)),
            (2,"random",46996,Fraction(131596825,2822),Fraction(214990848,9877)),
        )
        for h,scheme,observed,mean,bound in certified:
            m=fixture(h,scheme)
            r=quenched_original_opposite_ALL_D_mean(m)
            self.assertEqual(actual_original_ALL_D_opposite_wedges_direct(m),observed)
            self.assertEqual(
                r["EXACT_quenched_uniform_ONE_full_global_original_LINE_map_ALL_D_opposite_mean"],mean)
            self.assertEqual(
                r["uniform_in_both_adversarial_supports_R_ALL_D_mean_lower"],bound)
            self.assertNotEqual(
                r["EXACT_quenched_uniform_ONE_full_global_original_LINE_map_ALL_D_opposite_mean"],
                Fraction(observed))
            self.assertFalse(r["all_global_FIXED_RIGHT_original_g_minimax_PROVED"])

    def test_09_original_RIGHT_full_global_permutation_and_typed_gauge_invariance(self):
        for h,scheme in ((1,"S68"),(2,"lex")):
            model=fixture(h,scheme)
            old=quenched_original_opposite_ALL_D_mean(model)
            g=tuple(model["right_labels"])
            # One legal COMPLETE globally correlated swap over actual
            # original source LINE factors, not per-incidence redraw.
            changed=list(g)
            changed[0],changed[1]=changed[1],changed[0]
            new=dict(model,right_labels=tuple(changed))
            self.assertEqual(
                old["EXACT_quenched_uniform_ONE_full_global_original_LINE_map_ALL_D_opposite_mean"],
                quenched_original_opposite_ALL_D_mean(new)[
                    "EXACT_quenched_uniform_ONE_full_global_original_LINE_map_ALL_D_opposite_mean"])
            a=old["a"]
            physical=tuple((x+3)%a for x in range(a))
            changed2=tuple(tuple(sorted(physical[v] for v in edge)) for edge in g)
            new2=dict(model,right_labels=changed2)
            self.assertEqual(
                old["original_right_occupied_physical_pair_support_energy"],
                quenched_original_opposite_ALL_D_mean(new2)[
                    "original_right_occupied_physical_pair_support_energy"])
            self.assertFalse(old["original_port_GOOD_only_mean_lower_PROVED"])


if __name__=="__main__":
    unittest.main()
