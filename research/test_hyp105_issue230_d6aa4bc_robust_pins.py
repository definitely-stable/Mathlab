"""AA4-BC: independent partial injection / full global remainder falsifiers."""
import unittest
from fractions import Fraction
from itertools import combinations, permutations

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4bc_robust_pins import (
    actual_original_pinned_completion_certificate,certified_robust_pins_envelope,
)
from hyp105_issue230_d6aa4bb_overlap_covariance import uniform_GOOD_variance_envelope
from hyp105_issue230_d6aa4az_quenched_good_opposite import (
    genuine_original_fixed_point_GOOD_source_potential, support_bad_clean_energy,
)


def independent_right_good_triples(E,a,locked_edges):
    """Direct full-support clean test, independent of rooted T formula."""
    occupied={tuple(sorted(e)) for e in E}
    misses=tuple(e for e in combinations(range(a),2) if e not in occupied)
    bad={v for v in range(a) if 16*sum(v in e for e in misses)>=a}
    free=[tuple(sorted(e)) for e in E if tuple(sorted(e)) not in locked_edges]
    count=0
    for e,x,y in permutations(free,3):
        if any(u in bad for f in (e,x,y) for u in f):
            continue
        left=set(e)&set(x)
        right=set(e)&set(y)
        if len(left)==len(right)==1 and left!=right:
            count+=1
    return count


def independent_source_pin_filter_W32(model,locked_lines):
    """Literal source flags + global POINT physical labels, no weighted helper."""
    inc=tuple(map(tuple,model["incidences"]))
    f=tuple(tuple(sorted(e)) for e in model["left_labels"])
    E_clean=set(support_bad_clean_energy(f,6)["clean_induced_occupied_edges"])
    count=0
    for p,l in inc:
        if l in locked_lines or f[p] not in E_clean:
            continue
        u,v=f[p]
        for q0,k0 in inc:
            if k0 in locked_lines or len({p,q0})!=2 or k0==l:
                continue
            if f[q0] not in E_clean or u not in f[q0] or v in f[q0]:
                continue
            for q1,k1 in inc:
                if k1 in locked_lines or len({p,q0,q1})!=3 or len({l,k0,k1})!=3:
                    continue
                if f[q1] in E_clean and v in f[q1] and u not in f[q1]:
                    count+=1
    return count


def actual_full_partial_completion_distribution(w,E,pins):
    """Exhaustively enumerate ALL remaining complete maps, not per-triple draws."""
    src=set(pins)
    srcfree=[j for j in range(len(E)) if j not in src]
    used={tuple(sorted(e)) for e in pins.values()}
    pool=[tuple(sorted(e)) for e in E if tuple(sorted(e)) not in used]
    if len(srcfree)!=len(pool):
        raise AssertionError("incompatible original source pin support")
    values=[]
    for assignment in permutations(pool):
        g=dict(pins)
        g.update(zip(srcfree,assignment))
        v=0
        for (l,k0,k1),cnt in w.items():
            if src&{l,k0,k1}:
                continue
            e,x,y=g[l],g[k0],g[k1]
            a,b=set(e)&set(x),set(e)&set(y)
            if len(a)==len(b)==1 and a!=b:
                v+=cnt
        values.append(v)
    return Fraction(sum(values),len(values))


class AA4BCRobustOriginalPinTests(unittest.TestCase):
    def test_01_exact_dyadic_all_h_worst_adversarial_pins_certification(self):
        for h in tuple(range(5,35))+(40,48,64,80):
            s=1<<h
            V=(s+1)*(s*s+1)
            for k in (0,1,V//1024):
                z=certified_robust_pins_envelope(s,k)
                self.assertGreaterEqual(z["conditional_mean_of_unpinned_GOOD_wedges_lower"],
                                        Fraction(s**6,512))
                self.assertLessEqual(z["conditional_relative_variance_upper"]*V,
                                     30000000000)
                self.assertTrue(z["existence_of_some_completion_with_GOOD_ge_s6_over512"])
                self.assertTrue(z["ALL_fully_fixed_g_or_six_ID_GF5_PROVED"] is False)
                self.assertTrue(z["eta_le_30000000000_over_V"])
            self.assertEqual(
                certified_robust_pins_envelope(s,0)["conditional_relative_variance_upper"],
                uniform_GOOD_variance_envelope(s)["relative_variance_upper"])

    def test_02_original_W32_exact_source_pin_and_independent_point_flags(self):
        for scheme in ("S68","S72","lex","reverse"):
            m=fixture(1,scheme)
            for line in (0,1):
                pin={line:tuple(m["right_labels"][(line+2)%15])}
                z=actual_original_pinned_completion_certificate(m,pin)
                self.assertEqual(z["original_clean_source_3flag_weight_avoiding_pins"],
                    independent_source_pin_filter_W32(m,{line}))
                self.assertEqual(z["physical_good_ordered_right_free_edge_triples"],
                    independent_right_good_triples(m["right_labels"],6,set(pin.values())))
                self.assertGreater(z["mean_unpinned_source_good_wedges"],0)

    def test_03_original_W34_incomplete_K14_holes_and_arbitrary_source_pins(self):
        for scheme in ("lex","random"):
            m=fixture(2,scheme)
            for line in (0,1):
                pin={line:tuple(m["right_labels"][(line+3)%85])}
                z=actual_original_pinned_completion_certificate(m,pin)
                self.assertEqual(z["V"],85)
                self.assertEqual(z["free"],84)
                self.assertTrue(z["bad_coordinates_depend_on_FULL_right_support_not_free_support"])
                self.assertGreater(z["relative_variance_unpinned_upper"],0)
            self.assertEqual(
                actual_original_pinned_completion_certificate(m,{})[
                    "mean_unpinned_source_good_wedges"],
                Fraction(genuine_original_fixed_point_GOOD_source_potential(m)[
                    "CLEAN_original_fixed_f_physical_point_opposite_true_source_3flag_count"])*
                Fraction(2*support_bad_clean_energy(m["right_labels"],14)[
                    "CLEAN_physical_two_opposite_port_root_energy"],85*84*83))

    def test_04_exact_all_120_GLOBAL_right_map_completions_under_fixed_one_pin(self):
        E=tuple(combinations(range(4),2))
        # Deliberately overlapping abstract positive source weights:
        # the exact permutation lemma does not assume a fake W3 source.
        w={(0,1,2):2,(2,3,4):3,(1,4,5):5,(3,0,5):7}
        pinned={0:E[1]}
        from hyp105_issue230_d6aa4bc_robust_pins import _falling
        free=[e for e in E if e!=E[1]]
        a=independent_right_good_triples(E,4,{E[1]})
        sourceB=sum(v for key,v in w.items() if 0 not in key)
        mean=Fraction(sourceB*a,_falling(len(free),3))
        self.assertEqual(actual_full_partial_completion_distribution(w,E,pinned),mean)
        self.assertEqual(len(list(permutations(free))),120)

    def test_05_global_line_pin_validation_and_domain_fail_closed(self):
        m=fixture(1,"lex")
        right=m["right_labels"]
        for malformed in ({0:(9,10)}, {0:right[0],1:right[0]}, {-1:right[0]},
                          {99:right[0]}):
            with self.assertRaises(ValueError):
                actual_original_pinned_completion_certificate(m,malformed)
        for s in (2,4,16):
            with self.assertRaises(ValueError):
                certified_robust_pins_envelope(s,0)
        for k in (-1,200):
            with self.assertRaises(ValueError):
                certified_robust_pins_envelope(32,k)

    def test_06_free_physical_bad_set_is_full_support_global_not_resampled(self):
        m=fixture(2,"random")
        E=tuple(map(tuple,m["right_labels"]))
        old=support_bad_clean_energy(E,14)["bad_coordinates"]
        self.assertGreaterEqual(len(old),0)
        pin={0:E[0],1:E[1]}
        z=actual_original_pinned_completion_certificate(m,pin)
        self.assertTrue(z["bad_coordinates_depend_on_FULL_right_support_not_free_support"])
        self.assertEqual(z["physical_good_ordered_right_free_edge_triples"],
            independent_right_good_triples(E,14,{E[0],E[1]}))


if __name__=="__main__":
    unittest.main()
