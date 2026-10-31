"""Independent true W32/W34 audit of new all-map factor/coordinate transversal corollary."""
from fractions import Fraction
from itertools import combinations
import json
from pathlib import Path
import unittest

from hyp105_transversal_hierarchy import (
    validate_factor_and_physical_erasure,
    asymptotic_transversal_hierarchy,
    finite_accepted_genuine_two_class_motifs,
    greedy_maximal_packing_by_supports,
)
from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_full_physical_degree_tail import genuine_source
from hyp105_g5e2b3e1a_fixed_leading import selected_left_six
from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked
from hyp105_unconditional_original_deletion import (
    finite_true_original_sixset_deletion_certificate,
)


def independently_erased_original_flags(flags,f,g,P=(),L=(),X=(),Y=()):
    """Direct flag scan, NO factor-led exposure enumeration."""
    return frozenset(
        i for i,(p,ell) in enumerate(flags)
        if (p in P or ell in L or set(f[p]).intersection(X)
            or set(g[ell]).intersection(Y))
    )


def full_independent_historical_W32_supports(f,g,flags,source_model):
    """Original 62,370-incidence candidate GF5 classifier (not path oracle)."""
    result={}
    for six,_ in selected_left_six(source_model):
        tag=classify_seven_prechecked(six,f,g,flags)
        if tag not in ("D6","B/B-overlap"):
            continue
        ps=frozenset(flags[i][0] for i in six)
        ls=frozenset(flags[i][1] for i in six)
        xs=frozenset(x for p in ps for x in f[p])
        ys=frozenset(y for l in ls for y in g[l])
        if len(xs)!=6 or len(ys)!=6:
            raise AssertionError("bad historic true-source physical factor support")
        result[tuple(six)]=(ps,ls,xs,ys)
    return result


class TestOriginalFactorAndPhysicalCoordinateTransversal(unittest.TestCase):
    def test_algebraic_all_h_exact_fractional_hierarchy(self):
        for s in (2,4,8,16,64,128,1024,4096):
            for C,c in ((1,Fraction(1)),(2,Fraction(1,3))):
                with self.subTest(s=s,C=C):
                    x=asymptotic_transversal_hierarchy(s,C,c)
                    rho=(x["strict_lower_original_flag_disjoint_pack"]*6
                         /s**4)
                    self.assertTrue(rho>0)
                    self.assertEqual(
                        x["source_point_plus_line_factor_deletion_budget"],
                        (rho*s**4)//(s+1))
                    self.assertEqual(
                        x["left_plus_right_physical_symbol_deletion_budget"],
                        (rho*s**4)//((s+1)*(x["a"]-1)))
                    self.assertEqual(
                        x["strict_lower_original_point_and_line_factor_disjoint_pack"],
                        rho*s**4/(12*(s+1)))
                    self.assertEqual(
                        x["strict_lower_left_and_right_physical_symbol_disjoint_pack"],
                        rho*s**4/(12*(s+1)*(x["a"]-1)))
                    self.assertEqual(
                        x["strict_lower_original_flag_disjoint_pack"]/
                        x["strict_lower_original_point_and_line_factor_disjoint_pack"],
                        2*(s+1))
                    self.assertEqual(
                        x["strict_lower_original_point_and_line_factor_disjoint_pack"]/
                        x["strict_lower_left_and_right_physical_symbol_disjoint_pack"],
                        x["a"]-1)
                    self.assertFalse(x["root_branch_A_external_scientific_acceptance"])
                    self.assertTrue(x["parent_674_theorem_not_independently_reproved"])

    def test_nonvacuous_symbolic_s_at_formal_sufficient_threshold(self):
        # s is a HUGE symbolic dyadic integer; NO attempt is made to
        # construct the true W(3,s) or verify any all-h geometry.
        # The graph inputs C=c=1 are FORMAL and are NOT claimed to be
        # the actual Simonovits supersaturation constants.
        s=1<<1320
        q=asymptotic_transversal_hierarchy(s,1,Fraction(1))
        self.assertTrue(q["actual_s_meets_sufficient_threshold"])
        rho=(q["strict_lower_original_flag_disjoint_pack"]*6)/s**4
        self.assertGreater(q["original_flag_deletion_budget"],0)
        self.assertGreater(
            q["source_point_plus_line_factor_deletion_budget"],0)
        self.assertGreater(
            q["left_plus_right_physical_symbol_deletion_budget"],0)
        self.assertGreater(
            Fraction(q["left_plus_right_physical_symbol_deletion_budget"],
                     q["a"]),rho/3)
        self.assertLess(
            Fraction(q["left_plus_right_physical_symbol_deletion_budget"],
                     q["a"]),2*rho/3)
        self.assertLess(
            q["strict_lower_left_and_right_physical_symbol_disjoint_pack"],
            Fraction(q["a"],6))
        self.assertGreater(
            q["strict_lower_left_and_right_physical_symbol_disjoint_pack"],1)
        self.assertGreater(
            q["strict_lower_original_point_and_line_factor_disjoint_pack"],1)
        self.assertGreater(q["strict_lower_original_flag_disjoint_pack"],1)

    def test_true_original_geometry_physical_and_factor_exposure(self):
        for power in (1,2):
            m=pair_labeled_symplectic(power,"lex")
            s,V,flags=genuine_source(power)
            f,g=m["left_labels"],m["right_labels"]
            a=max(x for pair in f for x in pair)+1
            scenarios=[
                ((0,),(),(),()),
                ((),(0,),(),()),
                ((),(),(0,),()),
                ((),(),(),(0,)),
                ((0,1),(2,3),(0,1),(1,2)),
                (tuple(range(0,V,3)),tuple(range(1,V,7)),
                 tuple(range(0,a,2)),tuple(range(1,a,3))),
            ]
            for P,L,X,Y in scenarios:
                with self.subTest(s=s,p=len(P),l=len(L),x=len(X),y=len(Y)):
                    row=validate_factor_and_physical_erasure(
                        s,P,L,X,Y,point_labels=f,line_labels=g)
                    independent=independently_erased_original_flags(
                        flags,f,g,set(P),set(L),set(X),set(Y))
                    self.assertEqual(
                        frozenset(row["source_erasure_original_flag_ids"]),
                        independent)
                    self.assertLessEqual(
                        row["source_erasure_count"],
                        min(len(flags),row["combined_exposure_upper"]))
                    self.assertEqual(
                        row["point_factor_exposure_upper"],
                        (s+1)*(len(P)+len(L)))
                    self.assertEqual(
                        row["physical_coordinate_exposure_upper"],
                        (s+1)*(row["a"]-1)*(len(X)+len(Y)))
                    self.assertTrue(row["real_W3_geometry_not_sampled"])

    def test_independent_complete_W32_history_factor_coordinate_avoidance(self):
        # Five legal but DIFFERENT complete g original-line label injections.
        src=pair_labeled_symplectic(1,"lex")
        _,V,flags=genuine_source(1)
        f=tuple(src["left_labels"])
        for shift in (0,1,3,7,11):
            g=tuple(src["right_labels"][(i+shift)%V] for i in range(V))
            original=full_independent_historical_W32_supports(
                f,g,flags,src)
            self.assertTrue(original)
            for P,L,X,Y in (
                ((0,),(),(),()),
                ((),(1,),(),()),
                ((),(),(0,),()),
                ((),(),(),(1,)),
                ((0,2),(1,3),(0,2),(1,3))
            ):
                with self.subTest(shift=shift,erase=(P,L,X,Y)):
                    row=validate_factor_and_physical_erasure(
                        2,P,L,X,Y,point_labels=f,line_labels=g)
                    Z=set(row["source_erasure_original_flag_ids"])
                    accepted_after={
                        six for six in original
                        if not any(i in Z for i in six)
                    }
                    typed_after={
                        six for six,(ps,ls,xs,ys) in original.items()
                        if not ps.intersection(P) and not ls.intersection(L)
                        and not xs.intersection(X) and not ys.intersection(Y)
                    }
                    self.assertEqual(accepted_after,typed_after)
            # Pack from the full independent history, not only the
            # path-generator subfamily.
            for kind in ("factors","physical"):
                with self.subTest(shift=shift,kind=kind):
                    packing=greedy_maximal_packing_by_supports(original,kind)
                    self.assertGreater(packing["count"],0)
                    ids=packing["motif_six_original_incidence_IDs"]
                    i,j=(0,1) if kind=="factors" else (2,3)
                    self.assertEqual(len(ids),packing["count"])
                    self.assertTrue(all(
                        not (original[x][i]&original[y][i] or
                             original[x][j]&original[y][j])
                        for x,y in combinations(ids,2)
                    ))
                    # All actual accepted historical D6/BBo source
                    # motifs MUST hit the typed union of selected
                    # original factors or physical coordinates.
                    A=set(packing["covered_left_factor_or_coordinate_names"])
                    B=set(packing["covered_right_factor_or_coordinate_names"])
                    self.assertTrue(all(
                        original[x][i]&A or original[x][j]&B
                        for x in original))
                    if kind=="factors":
                        row=validate_factor_and_physical_erasure(
                            2,A,B,point_labels=f,line_labels=g)
                    else:
                        row=validate_factor_and_physical_erasure(
                            2,left_coordinates=A,right_coordinates=B,
                            point_labels=f,line_labels=g)
                    Z=set(row["source_erasure_original_flag_ids"])
                    self.assertFalse(
                        [six for six in original if not Z.intersection(six)]
                    )
                    # Independent PHYSICAL D6 DFS + source BBo
                    # projection corroboration under same hit set.
                    surviving=finite_true_original_sixset_deletion_certificate(
                        1,f,g,sorted(Z))
                    self.assertEqual(surviving["D6_avoid"],0)
                    self.assertEqual(
                        surviving["BBo_avoid_produced_source_subcount"],0)

    def test_true_W34_independent_accepted_path_subset_masks(self):
        fixture=json.loads(Path(__file__).with_name(
            "hyp105_w34_adversarial_certificate.json").read_text())
        f,g=fixture["f"],fixture["g"]
        s,V,flags=genuine_source(2)
        for P,L,X,Y in (
            ((0,),(),(),()),
            ((),(0,),(),()),
            ((),(),(0,),()),
            ((),(),(),(0,)),
            ((0,1),(2,3),(0,),(1,))
        ):
            with self.subTest(erasure=(P,L,X,Y)):
                mask=validate_factor_and_physical_erasure(
                    s,P,L,X,Y,point_labels=f,line_labels=g)
                Z=set(mask["source_erasure_original_flag_ids"])
                accepted=finite_accepted_genuine_two_class_motifs(
                    s,f,g,Z)
                for six,(ps,ls,xs,ys) in (
                    accepted["source_and_physical_supports"].items()):
                    self.assertFalse(ps.intersection(P))
                    self.assertFalse(ls.intersection(L))
                    self.assertFalse(xs.intersection(X))
                    self.assertFalse(ys.intersection(Y))
                    self.assertTrue(all(i not in Z for i in six))
                self.assertGreaterEqual(
                    accepted["accepted_genuine_GF5_two_class_subcount"],0)

    def test_fail_closed_original_typed_source_and_packing(self):
        m=pair_labeled_symplectic(1,"lex")
        f,g=m["left_labels"],m["right_labels"]
        for bad in ((True,),(-1,),(15,),(0,0)):
            with self.assertRaises(ValueError):
                validate_factor_and_physical_erasure(
                    2,left_point_ids=bad,
                    point_labels=f,line_labels=g)
        with self.assertRaises(ValueError):
            validate_factor_and_physical_erasure(
                2,left_coordinates=(6,),
                point_labels=f,line_labels=g)
        with self.assertRaises(ValueError):
            validate_factor_and_physical_erasure(
                2,left_point_ids=(0,),
                point_labels=f,line_labels=g[:-1])
        with self.assertRaises(ValueError):
            greedy_maximal_packing_by_supports({}, "unknown")
        with self.assertRaises(ValueError):
            asymptotic_transversal_hierarchy(3)

    def test_machine_readable_transversal_hierarchy(self):
        import json
        examples=[]
        for s in (4,64,4096):
            q=asymptotic_transversal_hierarchy(s)
            examples.append({
                "s":s,
                "a":q["a"],
                "source_original_flag_budget":q["original_flag_deletion_budget"],
                "source_point_line_budget":q[
                    "source_point_plus_line_factor_deletion_budget"],
                "physical_coordinate_both_half_budget":q[
                    "left_plus_right_physical_symbol_deletion_budget"],
                "all_three_packings_are_STRICT_rational_lower_bounds":True,
                "finite_s_passes_asymptotic_s0":
                    q["actual_s_meets_sufficient_threshold"]
            })
        print("HYP105_AA4_XPACK_CERTIFICATE="+json.dumps({
            "scope":"all-h mathematical consequence of scientific DRAFT #674",
            "original_source_flag_packing_scale":"Omega(s^4)",
            "original_point_line_factor_packing_scale":"Omega(s^3)",
            "physical_two_half_coordinate_packing_scale":"Omega(s^(3/2))",
            "external_SS6_constants_are_FORMAL_audit_placeholders":True,
            "no_small_dyadic_s_claim":True,
            "root_A_externally_accepted":False,
            "cases":examples,
        },sort_keys=True))


if __name__=="__main__":
    unittest.main()
