"""AA4-BD independent adversarial 10%-pin true source and K_a CLEAN falsifiers."""
import unittest
from fractions import Fraction
from itertools import combinations
from math import comb

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4bd_tenth_pins import (
    sharp_clean_all_support_floor, tenth_pinned_GOOD_completion,
    actual_true_original_tenth_pins_certificate,
)
from hyp105_issue230_d6aa4bc_robust_pins import (
    actual_original_pinned_completion_certificate, certified_robust_pins_envelope,
)
from hyp105_issue230_d6aa4az_quenched_good_opposite import (
    support_bad_clean_energy,
)
from hyp105_issue230_d6aa4ay_quenched_allD_opposite_mean import (
    _params, physical_edge_port_energy,
)


def fresh_supports_for_s32():
    s=32
    V,a,_,m=_params(s)
    edges=tuple(combinations(range(a),2))
    lex=edges[:V]
    # Spread the m missing edges across a matching instead of clustering
    # physical bad coordinates at the last large-degree vertex.
    holes=set((2*i,2*i+1) for i in range(m))
    spread=tuple(e for e in edges if e not in holes)
    assert len(spread)==V
    return ((a,lex),(a,spread))


def independently_count_right_free_good_center_ports(E,a,pinned_edges):
    """Independent direct physical degree pair convolution on ORIGINAL clean set.

    Does not call parent's physical_edge_port_energy and keeps FULL-E bad set.
    """
    E={tuple(sorted(e)) for e in E}
    holes=[e for e in combinations(range(a),2) if e not in E]
    bad={u for u in range(a)
         if 16*sum(u in e for e in holes)>=a}
    free={e for e in E if e not in pinned_edges and not any(u in bad for u in e)}
    degrees=[0]*a
    for u,v in free:
        degrees[u]+=1
        degrees[v]+=1
    return 2*sum((degrees[u]-1)*(degrees[v]-1) for u,v in free)


class AA4BDTenthAdversarialOriginalLinePins(unittest.TestCase):
    def test_01_exact_all_dyadic_h5_to80_without_fit(self):
        for h in tuple(range(5,36))+(40,48,64,80):
            s=1<<h
            V=(s+1)*(s*s+1)
            for k in (0,1,V//10):
                p=tenth_pinned_GOOD_completion(s,k)
                self.assertEqual(p["adversarial_original_LINE_pin_capacity"],V//10)
                self.assertGreaterEqual(
                    p["conditional_mean_unpinned_original_GOOD_lower"],
                    Fraction(s**6,80))
                self.assertLessEqual(
                    p["conditional_relative_variance_upper"]*V,50000000)
                self.assertTrue(
                    p["some_complete_g_extending_all_adversarial_line_pins_GOOD_ge_s6_over80"])
                self.assertFalse(p["ALL_fully_fixed_g_or_six_original_ID_GF5_PROVED"])
                self.assertEqual(p["root_230"],"OPEN_WITH_FORMAL_BLOCKER")

    def test_02_polynomial_all_h_clean_9over8_floor_and_real_s32_extremes(self):
        for s in (32,64,128,256,4096,1<<80):
            x=sharp_clean_all_support_floor(s)
            self.assertGreater(x["nonnegative_polynomial_all_t_ge_230"],0)
            self.assertGreaterEqual(x["symbolic_universal_lower_from_a"],
                                    Fraction(9*x["V"]**2,8))
        for a,E in fresh_supports_for_s32():
            whole=support_bad_clean_energy(E,a)
            T=whole["CLEAN_physical_two_opposite_port_root_energy"]
            self.assertGreaterEqual(T,Fraction(9*len(E)**2,8))
            self.assertGreaterEqual(T,sharp_clean_all_support_floor(32)[
                "symbolic_universal_lower_from_a"])

    def test_03_10percent_actual_K261_right_adversarial_edges(self):
        V,a,_,m=_params(32)
        k=V//10
        for a,E in fresh_supports_for_s32():
            # Worst-looking concentrated and distributed frozen image sets,
            # all are real physical edges of the complete occupied support E.
            pins=[
                set(E[:k]),
                set(E[::10][:k]),
                set(sorted(E,key=lambda e:(e[0]+e[1])%17)[:k]),
            ]
            for frozen in pins:
                A=independently_count_right_free_good_center_ports(E,a,frozen)
                floor=tenth_pinned_GOOD_completion(32,k)[
                    "right_good_ordered_free_edge_3tuples_floor"]
                self.assertGreaterEqual(A,floor)
                self.assertGreaterEqual(A,V*V)
                fixed_clean=set(support_bad_clean_energy(E,a)[
                    "clean_induced_occupied_edges"])
                free_clean=tuple(e for e in E if e not in frozen and e in fixed_clean)
                self.assertEqual(A,2*physical_edge_port_energy(free_clean,a))

    def test_04_genuine_original_symplectic_W32_W34_pin_oracles(self):
        for h,schemes in ((1,("S68","S72","lex","reverse")),
                          (2,("lex","random"))):
            for scheme in schemes:
                model=fixture(h,scheme)
                V=len(model["right_labels"])
                for k in (0,1,V//10):
                    # Actual original LINE IDs, corresponding arbitrary
                    # FIXED yet non-identity occupied right pair images.
                    pins={j:tuple(model["right_labels"][(j+3)%V])
                          for j in range(k)}
                    x=actual_true_original_tenth_pins_certificate(model,pins)
                    y=actual_original_pinned_completion_certificate(model,pins)
                    self.assertEqual(x,y)
                    self.assertEqual(x["pinned"],k)
                    self.assertTrue(x[
                        "bad_coordinates_depend_on_FULL_right_support_not_free_support"])
                    self.assertGreaterEqual(
                        x["mean_unpinned_source_good_wedges"],0)

    def test_05_64times_larger_fraction_and_fail_closed(self):
        s=32
        V=(s+1)*(s*s+1)
        self.assertGreaterEqual(V//10,100*(V//1024))
        self.assertEqual(
            certified_robust_pins_envelope(s,V//1024)[
                "arbitrary_pinned_source_LINE_factor_limit"],V//1024)
        self.assertGreater(
            tenth_pinned_GOOD_completion(s,V//10)[
                "conditional_mean_unpinned_original_GOOD_lower"],0)
        for bad in (-1,V//10+1,V,True,Fraction(1,10)):
            with self.assertRaises(ValueError):
                tenth_pinned_GOOD_completion(s,bad)
        for invalid in (0,2,4,16,24,33,48):
            with self.assertRaises(ValueError):
                sharp_clean_all_support_floor(invalid)
        self.assertGreater(
            tenth_pinned_GOOD_completion(32,0)[
                "conditional_mean_unpinned_original_GOOD_lower"],
            certified_robust_pins_envelope(32,0)[
                "conditional_mean_of_unpinned_GOOD_wedges_lower"])


if __name__=="__main__":
    unittest.main()
