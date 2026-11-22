"""Exact independent tests for GIO-003/T3-B edit-stable GQ-template theorem."""
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations
import unittest

from gio_generalized_gq import model
from gio_resilience import source_first_d6, source_first_bbo
from hyp105_aa4_branch_a_integrated_referee import source_d6, historical_bbo
from gio_t3b_edit_transfer import (
    SCHEMA, BASE_MAIN, certificate, finite_case, verify_edit,
    switch_with_forced_four_cycle, literal_historical_class, typed_adjacency,
    is_six_cycle, independent_signature_check, symbolic_transfer_ledger,
    actual_missing_projections,
)


def direct_four_cycles(source_flags):
    """Independent four-cycle oracle from point-pair -> common lines."""
    lines = {}
    for p,l in source_flags:
        lines.setdefault(l,set()).add(p)
    found = []
    for l1,l2 in combinations(sorted(lines),2):
        shared = sorted(lines[l1]&lines[l2])
        for p,q in combinations(shared,2):
            found.append((p,q,l1,l2))
    return found


class TestGIO003T3B(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.c = certificate()
        cls.by = {z["kind"]:z for z in cls.c["finite_examples"]}

    def test_01_real_geometries_have_certified_non_gq_edit(self):
        expect = {"W32":(2,2,45),"W33":(3,3,160),
                  "Qminus24":(2,4,135),"dualQminus42":(4,2,135)}
        for kind,(s,t,n) in expect.items():
            z=self.by[kind]
            self.assertEqual((z["s"],z["t"],z["original_flags"]),(s,t,n))
            self.assertEqual(z["edited_flags"],n)
            self.assertTrue(z["point_and_line_degrees_preserved"])
            self.assertTrue(z["new_geometry_has_four_cycle"])
            self.assertEqual(len(z["switch_removed"]),2)
            self.assertEqual(len(z["switch_added"]),2)
            m=model(kind)
            sw=switch_with_forced_four_cycle(m)
            edited=verify_edit(m,sw["removed"],sw["added"])["edited"]
            assert direct_four_cycles(edited)
            self.assertTrue(set(sw["four_cycle"])<=edited)
            self.assertFalse(direct_four_cycles(m["flags"]))

    def test_02_historical_lex_original_counts_and_original_class_preservation(self):
        expect={"W32":(15,2),"W33":(653,530),
                "Qminus24":(466,378),"dualQminus42":(466,378)}
        for kind,(d,b) in expect.items():
            z=self.by[kind]
            self.assertEqual((z["original_D6"],z["original_produced_BBo"]),(d,b))
            self.assertLessEqual(z["edited_certified_D6"],d)
            self.assertLessEqual(z["edited_certified_BBo"],b)
            self.assertTrue(z["literal_and_independent_historical_classifier_agree"])

    def test_03_source_ids_preserved_when_new_flags_recoded(self):
        for kind in ("W32","Qminus24"):
            m=model(kind)
            e=switch_with_forced_four_cycle(m)
            edited=verify_edit(m,e["removed"],e["added"])["edited"]
            D=source_first_d6(m,frozenset(range(len(m["flags"]))))
            B=source_first_bbo(m,frozenset(range(len(m["flags"]))))
            for cls,motifs in (("D6",D),("BBo_historical",B)):
                for k in motifs:
                    if all(m["flags"][x] in edited for x in k):
                        self.assertTrue(independent_signature_check(m,edited,k,cls))

    def test_04_independent_port_graph_equivalence_on_true_source_motifs(self):
        for kind in ("W32","W33","Qminus24","dualQminus42"):
            m=model(kind)
            D=source_first_d6(m,frozenset(range(len(m["flags"]))))
            B=source_first_bbo(m,frozenset(range(len(m["flags"]))))
            for k in D:
                named=tuple(m["flags"][x] for x in k)
                self.assertEqual(literal_historical_class(named,m["f"],m["g"]),"D6")
                self.assertIsNotNone(source_d6(m,k))
            for k in B:
                named=tuple(m["flags"][x] for x in k)
                self.assertEqual(literal_historical_class(named,m["f"],m["g"]),
                                 "BBo_historical")
                self.assertTrue(historical_bbo(m,k))

    def test_05_deletion_after_edit_is_exact_named_source_intersection(self):
        for z in self.by.values():
            for item in z["post_edit_masks"]:
                self.assertGreaterEqual(item["surviving_D6"],0)
                self.assertGreaterEqual(item["surviving_certified_BBo"],0)
                self.assertLessEqual(item["greedy_original_disjoint_packing"]*6,
                                     z["original_flags"])
            self.assertEqual(
                next(x for x in z["post_edit_masks"] if x["mask"]=="new_only")["surviving_D6"],
                z["edited_certified_D6"])
            self.assertEqual(
                next(x for x in z["post_edit_masks"] if x["mask"]=="new_only")["surviving_certified_BBo"],
                z["edited_certified_BBo"])

    def test_06_arbitrary_source_insertions_preserve_all_old_motifs(self):
        m=model("W32"); old=set(m["flags"])
        all_extra={(p,l) for p in range(m["Vp"])
                   for l in range(m["Vl"]) if (p,l) not in old}
        e=verify_edit(m,(),all_extra)
        self.assertEqual(len(e["edited"]),m["Vp"]*m["Vl"])
        self.assertEqual(e["deleted_GQ_flags"],0)
        self.assertEqual(e["added_flags"],m["Vp"]*m["Vl"]-len(old))
        D=source_first_d6(m,frozenset(range(len(m["flags"]))))
        B=source_first_bbo(m,frozenset(range(len(m["flags"]))))
        for cls,motifs in (("D6",D),("BBo_historical",B)):
            for k in motifs:
                self.assertTrue(independent_signature_check(m,e["edited"],k,cls))

    def test_07_correlated_maps_still_preserve_original_signatures(self):
        for kind in ("W32","Qminus24"):
            z=finite_case(kind,"correlated")
            self.assertTrue(z["literal_and_independent_historical_classifier_agree"])
            self.assertTrue(z["new_geometry_has_four_cycle"])

    def test_08_untyped_and_invalid_edits_are_rejected(self):
        m=model("W32");old=set(m["flags"]);bad=next(x for x in
          ((p,l) for p in range(m["Vp"]) for l in range(m["Vl"])) if x not in old)
        for deletion,additions in [
            ({bad},set()),(set(),{m["flags"][0]}),
            (set(),{(-1,0)}),(set(),{(m["Vp"],0)}),
            (set(),{(0,m["Vl"])}),
        ]:
            with self.assertRaises(ValueError):
                verify_edit(m,deletion,additions)
        bad_map=dict(m,f=tuple(m["f"][:-1])+(m["f"][0],))
        with self.assertRaises(ValueError):
            verify_edit(bad_map,(),())
        bad_alphabet=dict(m,aP=m["aP"]+1)
        with self.assertRaises(ValueError):
            verify_edit(bad_alphabet,(),())

    def test_09_invalid_sixsets_do_not_fake_accepted_historical_class(self):
        m=model("W32")
        k=tuple(m["flags"][:6])
        self.assertIsNone(literal_historical_class(k[:5],m["f"],m["g"]))
        self.assertIsNone(literal_historical_class((k[0],)*6,m["f"],m["g"]))
        self.assertIsNone(typed_adjacency([(0,1)]*5))
        self.assertFalse(is_six_cycle(((0,1),)*6))
        self.assertFalse(is_six_cycle(None))

    def test_10_symbolic_edited_radius_and_probability(self):
        for b in (1,2,3):
            z=symbolic_transfer_ledger(b)
            self.assertTrue(z["FORMAL_ONLY"])
            self.assertTrue(z["external_C6_numeric_constants_unknown"])
            self.assertEqual(2*Q(z["edited_source_deletion_radius_eta"]),
                             Q(z["inherited_GQ_rho"]))
            self.assertGreater(Q(z["surviving_lower_delta"]),0)
            self.assertGreater(Q(z["iid_GF5_sign_probability_min"]),0)
            self.assertTrue(z["all_insertions_allowed_without_new_spectral_claim"])
            r0=int(z["sufficient_non_GQ_two_switch_r0"])
            self.assertGreaterEqual(r0,int(z["r0"]))
            self.assertGreaterEqual(Q(z["edited_source_deletion_radius_eta"])*r0**4,2)
            self.assertIn("W(3,2^h)",z["explicit_infinite_family"])

    def test_11_positive_lower_asymptotic_not_claimed_for_small_fixture(self):
        self.assertEqual(self.c["schema"],SCHEMA)
        self.assertEqual(self.c["base_main_sha"],BASE_MAIN)
        self.assertTrue(self.c["no_non_template_T3_theorem"])
        self.assertTrue(self.c["no_general_ASET_improvement"])
        self.assertTrue(self.c["no_external_human_referee"])
        self.assertEqual(self.c["GF5"]["palette"],51)
        self.assertEqual(self.c["GF5"]["D6_sign"],5643)
        self.assertEqual(self.c["GF5"]["BBo_min_sign"],5175)
        for z in self.c["formal_ledgers"]:
            self.assertTrue(z["FORMAL_ONLY"])

    def test_13_direct_missing_projection_budget_in_edited_graph(self):
        for kind in self.by:
            m=model(kind); sw=switch_with_forced_four_cycle(m)
            edit=verify_edit(m,sw["removed"],sw["added"])
            absent=actual_missing_projections(edit["edited"],m["Vp"],m["Vl"])
            self.assertEqual(len(absent),self.by[kind]["switched_missing_projections"])
            self.assertLessEqual(len(absent),(3*m["s"]*m["t"]+1)*2)
            self.assertEqual(self.by[kind]["switched_missing_3st_plus_one_bound"],
                             (3*m["s"]*m["t"]+1)*2)
            for row in self.by[kind]["post_edit_masks"]:
                self.assertTrue(row["bounded_by_3st_plus_one"])
                self.assertLessEqual(
                    row["actual_missing_projections"],
                    (3*m["s"]*m["t"]+1)*row["removed_original_GQ_flags_total"])

    def test_14_unlimited_insertions_cannot_create_missing_projection(self):
        m=model("W32")
        old=set(m["flags"])
        extra={(p,l) for p in range(m["Vp"]) for l in range(m["Vl"])
               if (p,l) not in old}
        self.assertEqual(actual_missing_projections(old,m["Vp"],m["Vl"]),set())
        self.assertEqual(
            actual_missing_projections(old|extra,m["Vp"],m["Vl"]),set())
        self.assertEqual(
            actual_missing_projections(set(),m["Vp"],m["Vl"]),
            set((p,l) for p in range(m["Vp"]) for l in range(m["Vl"])))

    def test_15_independent_three_path_endpoint_census(self):
        m=model("W32"); sw=switch_with_forced_four_cycle(m)
        available=verify_edit(m,sw["removed"],sw["added"])["edited"]
        byp={}
        byline={}
        for p,l in available:
            byp.setdefault(p,set()).add(l)
            byline.setdefault(l,set()).add(p)
        alt_missing=set()
        for p in range(m["Vp"]):
            for ell in range(m["Vl"]):
                if ell in byp.get(p,()):
                    continue
                found=False
                for mid in byp.get(p,()):
                    for foot in byline[mid]:
                        if foot!=p and ell in byp.get(foot,()):
                            found=True
                if not found:
                    alt_missing.add((p,ell))
        self.assertEqual(alt_missing,
             actual_missing_projections(available,m["Vp"],m["Vl"]))

    def test_16_post_edit_adversarial_factor_relabeling_same_template(self):
        m=model("W32")
        sw=switch_with_forced_four_cycle(m)
        # Physical label permutation is deliberately chosen FROM the edit,
        # rather than independently or before it.
        changed=verify_edit(m,sw["removed"],sw["added"])["edited"]
        points=sorted({p for p,l in sw["added"]})
        lines=sorted({l for p,l in sw["added"]})
        f=list(m["f"]); g=list(m["g"])
        self.assertEqual(len(points),2)
        self.assertEqual(len(lines),2)
        f[points[0]],f[points[1]]=f[points[1]],f[points[0]]
        g[lines[0]],g[lines[1]]=g[lines[1]],g[lines[0]]
        updated=dict(m,f=tuple(f),g=tuple(g),
                     point_by_pair={z:i for i,z in enumerate(f)},
                     line_by_pair={z:i for i,z in enumerate(g)})
        self.assertEqual(len(set(updated["f"])),updated["Vp"])
        self.assertEqual(len(set(updated["g"])),updated["Vl"])
        edit=verify_edit(updated,sw["removed"],sw["added"])
        self.assertEqual(edit["edited"],changed)
        D=source_first_d6(updated,frozenset(range(len(m["flags"]))))
        B=source_first_bbo(updated,frozenset(range(len(m["flags"]))))
        self.assertFalse(set(D)&set(B))
        alive={i for i,x in enumerate(m["flags"]) if x in changed}
        for cls,inventory in (("D6",D),("BBo_historical",B)):
            for key in inventory:
                if set(key)<=alive:
                    self.assertTrue(independent_signature_check(updated,changed,key,cls))

    def test_12_literal_source_profiles_not_an_edited_projection_claim(self):
        m=model("W32")
        sw=switch_with_forced_four_cycle(m)
        e=verify_edit(m,sw["removed"],sw["added"])
        self.assertEqual(len(sw["four_cycle"]),4)
        self.assertEqual(len(e["witness_to_edited"]),len(m["flags"])-2)
        self.assertEqual(len(e["added"]),2)
        # New GQ projection is not assumed unique, old one certifies only
        # preserved old sixsets. An inserted flag has no GQ source witness.
        self.assertTrue(all(x not in m["flag_to_id"] for x in e["added"]))


if __name__=="__main__":
    unittest.main()
