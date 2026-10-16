"""AA4-BD: true original wider arbitrary line pins and whole-global orbit checks."""
import unittest
from fractions import Fraction
from itertools import combinations,permutations

from hyp105_issue230_d6aa4bd_strong_robust_pins_orbits import (
    strengthened_original_robust_pin_envelope,
    simultaneously_robust_whole_global_completions,
    fully_deranged_two_original_completions_all_large_h)
from hyp105_issue230_d6aa4bc_robust_pins import (
    certified_robust_pins_envelope,
    actual_original_pinned_completion_certificate)
from hyp105_issue230_d6aa4az_quenched_good_opposite import (
    support_bad_clean_energy)
from hyp105_issue230_d6aa4ar_good_wedges_port_balance import (
    exact_true_original_good_D_two_port_wedge_certificate)
from hyp105_issue230_projection import fixture


def independent_actual_original_W32_point_clean_pinned_line_triples(model,locked):
    """Literal genuine ORIGINAL W32 45 incidence flag triple enumeration.

    No source weighted-triple helper; counts original source ordering
    (center,outer-point-port-0,outer-point-port-1) exactly.
    """
    inc=tuple(tuple(x) for x in model["incidences"])
    f=tuple(tuple(sorted(e)) for e in model["left_labels"])
    bad=set(support_bad_clean_energy(f,6)["bad_coordinates"])
    out=0
    for p,l in inc:
        if l in locked or any(u in bad for u in f[p]):
            continue
        c0,c1=f[p]
        for q,k in inc:
            if (k in locked or q==p or k==l or
                any(u in bad for u in f[q]) or
                len(set(f[q])&{c0,c1})!=1 or c0 not in f[q]):
                continue
            for r,m in inc:
                if (m in locked or r in (p,q) or m in (l,k) or
                    any(u in bad for u in f[r])):
                    continue
                if c1 in f[r] and c0 not in f[r]:
                    out+=1
    return out


def independent_real_physical_clean_ordered_triples(E,a,removed):
    """Whole ORIGINAL physical occupied edge support defines CLEAN;
    then explicitly omit arbitrarily removed pinned physical edges.
    """
    occupied={tuple(sorted(e)) for e in E}
    missing=[e for e in combinations(range(a),2) if e not in occupied]
    bad={c for c in range(a)
         if 16*sum(c in edge for edge in missing)>=a}
    free=[e for e in occupied if e not in removed
          and not any(c in bad for c in e)]
    ans=0
    for e in free:
        c0,c1=e
        outer0=[x for x in free if c0 in x and c1 not in x]
        outer1=[x for x in free if c1 in x and c0 not in x]
        # Physical favorable counts are ORDERED source-line image triples:
        # the two opposite outer physical edges can swap source LINE IDs.
        ans+=2*len(outer0)*len(outer1)
    return ans


class StrongerOriginalLinePinsAndRobustOrbits(unittest.TestCase):
    def test_01_all_h5_to80_fourfold_more_arbitrary_real_original_line_pins(self):
        for h in tuple(range(5,35))+(40,48,64,80):
            s=1<<h;V=(s+1)*(s*s+1)
            for k in sorted({0,1,V//1024,V//512,V//384,V//320,V//256}):
                x=strengthened_original_robust_pin_envelope(s,k)
                self.assertEqual(x["arbitrary_pinned_actual_original_LINE_factor_limit"],V//256)
                self.assertTrue(x["original_GOOD_mean_universal_s6_over1024"])
                self.assertGreaterEqual(x[
                    "exact_rational_uniform_conditional_GOOD_mean_lower"],
                    Fraction(25,16384)*s**6)
                self.assertGreaterEqual(x[
                    "exact_rational_uniform_conditional_GOOD_mean_lower"],
                    Fraction(s**6,1024))
                self.assertLessEqual(x[
                    "exact_rational_conditional_GOOD_relative_variance_upper"]*V,
                    30000000000)
                self.assertEqual(x["parent_exact_overlap_checked"],k<=V//1024)
                self.assertFalse(x["ALL_fully_fixed_g_or_six_ID_GF5_PROVED"]
                                 if "ALL_fully_fixed_g_or_six_ID_GF5_PROVED" in x
                                 else not x["no_original_six_ID_seven_GF5_lower"])
            print("AA4BD_ALLH_4X_TRUE_ORIGINAL_PINS",h,
                  "V",V,"k_new",V//256,"k_old",V//1024,
                  "new_mean_ratio_s6",str(x[
                      "exact_rational_uniform_conditional_GOOD_mean_lower"]/s**6),
                  "eta_times_V",str(x[
                      "exact_rational_conditional_GOOD_relative_variance_upper"]*V))
        for invalid in (0,3,True,-4):
            with self.assertRaises(ValueError):
                strengthened_original_robust_pin_envelope(invalid,0)
        V=(33)*(1025)
        for invalid in (-1,V//256+1,True,0.5):
            with self.assertRaises(ValueError):
                strengthened_original_robust_pin_envelope(32,invalid)

    def test_02_exact_parent_same_source_same_full_right_support_common_k_subset(self):
        for h in (5,6,8,12,20,32):
            s=1<<h;V=(s+1)*(s*s+1)
            for k in (0,1,V//1024):
                old=certified_robust_pins_envelope(s,k)
                new=strengthened_original_robust_pin_envelope(s,k)
                self.assertEqual(old["conditional_mean_of_unpinned_GOOD_wedges_lower"],
                                 new["exact_rational_uniform_conditional_GOOD_mean_lower"])
                self.assertEqual(old["conditional_relative_variance_upper"],
                                 new["exact_rational_conditional_GOOD_relative_variance_upper"])
                self.assertTrue(new["parent_exact_overlap_checked"])

    def test_03_any_preselected_global_whole_free_physical_edge_permutation_orbit(self):
        for h in (5,6,9,11,12,13,14,15,20,40,80):
            s=1<<h;V=(s+1)*(s*s+1)
            k=V//256
            base=simultaneously_robust_whole_global_completions(s,k,1)
            self.assertEqual(base["s"],s)
            self.assertTrue(base["strict_original_f_g_global_no_redraw"])
            if h>=13:
                pair=fully_deranged_two_original_completions_all_large_h(s,k)
                self.assertEqual(pair[
                    "original_source_LINE_image_Hamming_distance_between_two_maps"],
                                 V-k)
                self.assertTrue(pair["Hamming_changes_EVERY_free_original_LINE_factor"])
                self.assertTrue(pair[
                    "two_fully_globally_injected_original_LINE_maps_extend_same_adversarial_pins"])
                self.assertGreater(pair["success_base_completions_fraction_lower"],0)
                orbit=simultaneously_robust_whole_global_completions(s,k,2)
                self.assertEqual(pair["success_base_completions_fraction_lower"],
                                 orbit["analytic_GOOD_whole_map_fraction_lower"])
                # Different predefined WHOLE physical-free-edge
                # transformations: union bound, no per-wedge redraw.
                more=simultaneously_robust_whole_global_completions(
                    s,k,max(2,V//1000000000000))
                self.assertIn("analytic_GOOD_whole_map_fraction_lower",more)
            else:
                with self.assertRaises(ValueError):
                    fully_deranged_two_original_completions_all_large_h(s,k)
        for invalid in (-1,0,1.5,True):
            with self.assertRaises(ValueError):
                simultaneously_robust_whole_global_completions(1<<13,0,invalid)

    def test_04_genuine_original_W32_adversarial_pinned_source_and_clean_physical_independent(self):
        for scheme in ("S68","S72","lex","reverse"):
            m=fixture(1,scheme)
            for j in (0,1,2):
                assigned={j:tuple(m["right_labels"][(j+5)%15])}
                x=actual_original_pinned_completion_certificate(m,assigned)
                self.assertEqual(x[
                    "original_clean_source_3flag_weight_avoiding_pins"],
                    independent_actual_original_W32_point_clean_pinned_line_triples(
                        m,set(assigned)))
                self.assertEqual(x[
                    "physical_good_ordered_right_free_edge_triples"],
                    independent_real_physical_clean_ordered_triples(
                        m["right_labels"],6,{tuple(sorted(v)) for v in assigned.values()}))
                self.assertTrue(x[
                    "bad_coordinates_depend_on_FULL_right_support_not_free_support"])
        print("AA4BD_TRUE_ORIGINAL_W32_GLOBAL_LABELS","four schemes, three arbitrary fixed complete right support image pins, independent original actual flag and physical CLEAN ordered triples")

    def test_05_true_original_W34_nononto_K14_full_support_pinned_edge_clean_invariant(self):
        for scheme in ("lex","random"):
            m=fixture(2,scheme)
            V=len(m["right_labels"])
            self.assertEqual(V,85)
            for pinned in ({0:tuple(m["right_labels"][4])},
                           {0:tuple(m["right_labels"][4]),
                            1:tuple(m["right_labels"][7])}):
                x=actual_original_pinned_completion_certificate(m,pinned)
                # Independent direct physical K14 occupied triples
                # compatible with FULL-support BAD coordinates; false
                # reclassifying the free support would change theorem.
                actual=independent_real_physical_clean_ordered_triples(
                    m["right_labels"],14,{tuple(sorted(e)) for e in pinned.values()})
                self.assertEqual(x[
                    "physical_good_ordered_right_free_edge_triples"],actual)
                self.assertEqual(x["free"],V-len(pinned))
                self.assertTrue(x[
                    "bad_coordinates_depend_on_FULL_right_support_not_free_support"])

    def test_06_actual_original_W32_two_hamming_disjoint_full_global_extensions_preserve_pins(self):
        # FINITE ORIGINAL symplectic W32 demonstration ONLY; the new
        # h>=13 theorem is certified symbolically and NOT extrapolated
        # from tiny W32. One full point f remains fixed. Nine genuine
        # original source LINE IDs fixed and six FREE right physical
        # pair images rotated AS A WHOLE; no event-level resampling.
        m=fixture(1,"S68")
        original_right=tuple(tuple(e) for e in m["right_labels"])
        pinned=set(range(9))
        free=tuple(range(9,15))
        successes=[]
        for shift in range(6):
            labels=list(original_right)
            for idx,j in enumerate(free):
                labels[j]=original_right[free[(idx+shift)%6]]
            model=dict(m,right_labels=tuple(labels))
            z=exact_true_original_good_D_two_port_wedge_certificate(model)
            successes.append(z[
                "good_D_original_OPPOSITE_TWO_TYPED_port_wedges"])
            self.assertEqual(tuple(model["right_labels"][j] for j in pinned),
                             tuple(original_right[j] for j in pinned))
            self.assertEqual(len(set(model["right_labels"])),15)
            if shift:
                self.assertTrue(all(model["right_labels"][j]!=original_right[j]
                                    for j in free))
        self.assertTrue(all(v>0 for v in successes))
        print("AA4BD_REAL_W32_S68_6_WHOLE_COMPLETIONS",
              "pinned_original_LINE_count",9,
              "every_NONZERO_rotation_changes_ALL_SIX_free_original_LINE_images",
              "R_GOOD_by_rotation",successes)
