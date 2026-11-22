"""Independent G6-C2 mixed FULL/CORE and partial projection exact tests."""
from collections import Counter, defaultdict
from itertools import combinations
import unittest

from gio_t3c2_partial_books import (
    SCHEMA,PARENT_G6C1,make_model,selected_mask,
    full_core_book,manual_produced_bbo,inverse_certificate,
    original_source_conflict_degrees,endpoint_mask,
    source_finite_case,certificate,typed_e_col,
)
from gio_t3c_intrinsic_defect import source_graph,doubled_gq
from hyp105_aa4_branch_a_integrated_referee import (
    actual_edges,historical_bbo,source_bbo_inverse,
)
from gio_resilience import physical_bbo,source_first_bbo


def independent_book_bruteforce(m,A,C,side):
    """Count literal (j,x,k,p,q,aflag,cflag,y) source tuples by flags.

    Intentionally does NOT call the new aggregated K_AC, F1/F2,
    source-book or physical-degree implementations.
    """
    factors=m["f"] if side=="point" else m["g"]
    other=m["g"] if side=="point" else m["f"]
    neighbors=m["neighbors_point"] if side=="point" else m["neighbors_line"]
    source=m["flags"] if side=="point" else tuple((l,p) for p,l in m["flags"])
    terms=set()
    for ac in A:
        p,r=source[ac]
        for cc in C:
            j,h=source[cc]
            ys=set(other[r])&set(other[h])
            for y in ys:
                for x,k in (factors[j],factors[j][::-1]):
                    if k not in factors[p]:
                        continue
                    for q in neighbors[p]:
                        if x in factors[q]:
                            term=(j,x,k,p,q,ac,cc,y)
                            assert term not in terms
                            terms.add(term)
    return terms


def independent_endpoint_mask(m,A):
    """Exact domain partition by original endpoint names and anchors."""
    classes=Counter()
    for fp in combinations(range(m["aP"]),2):
        for gl in combinations(range(m["aL"]),2):
            q=m["point_by_pair"].get(fp)
            r=m["line_by_pair"].get(gl)
            if q is None or r is None:
                k="unlabelled"
            elif (q,r) in m["flag_to_id"]:
                k="incident"
            elif (q,r) not in m["projection"]:
                k="unprojected"
            else:
                p,ell=m["projection"][q,r]
                if (set(m["f"][q])&set(m["f"][p])
                    or set(m["g"][r])&set(m["g"][ell])):
                    k="factor_overlap"
                elif not set((m["flag_to_id"][q,ell],
                              m["flag_to_id"][p,ell],
                              m["flag_to_id"][p,r]))<=A:
                    k="deleted_anchors"
                else:
                    k="good"
            classes[k]+=4
    return classes


def independent_middle_path_owner_balance(m,A,C):
    """Independent physical H FULL/CORE weighted corner-count identity."""
    dA=Counter();dC=Counter()
    for i in A:
        p,l=m["flags"][i]
        for x in m["f"][p]:
            for y in m["g"][l]:
                dA[x,y]+=1
    for i in C:
        p,l=m["flags"][i]
        for x in m["f"][p]:
            for y in m["g"][l]:
                dC[x,y]+=1
    return sum(dA[v]*dC[v] for v in dA),max(dC.values(),default=0)


class TestGIO003C2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=certificate()
        cls.items={(x["kind"],x["scheme"],x["mask"]):x
                   for x in cls.data["selected_cases"]}

    def test_01_all_exact_certificate_entries_and_strict_scope(self):
        d=self.data
        self.assertEqual(d["schema"],SCHEMA)
        self.assertEqual(d["parent_G6C1_HEAD"],PARENT_G6C1)
        self.assertEqual(d["claim"],
           "PROVED_INTRINSIC_A5_BOOK_AND_PARTIAL_A6_INVERSE_NOT_FULL_T3")
        self.assertTrue(d["no_abstract_T3_full_obstruction_claim"])
        self.assertTrue(d["no_intrinsic_A4_LOW_sixset_supersaturation"])
        self.assertTrue(d["no_unrestricted_ASET_exponent"])
        self.assertTrue(d["no_Lean_or_external_independent_referee"])

    def test_02_independent_literal_full_core_source_books(self):
        for name,scheme,mask in [
            ("W32","lex","full"),("W32","lex","mixed"),
            ("W32","correlated","mixed"),
            ("Qminus24","lex","mixed"),
            ("doubleW32","lex","full"),
            ("switchedDoubleW32","lex","mixed")]:
            m=make_model(name,scheme)
            A,C=selected_mask(m,mask)
            for side in ("point","line"):
                b=full_core_book(m,A,C,side)
                independently=independent_book_bruteforce(m,A,C,side)
                self.assertEqual(b["book_keys"],independently)
                self.assertEqual(b["source_book"],len(independently))
                self.assertLessEqual(b["source_book"]**2,
                                     b["exact_source_book_squared_bound"])

    def test_03_independent_theta_and_degree_plus_Cauchy(self):
        for name in ("W32","W33","Qminus24","switchedDoubleW32"):
            m=make_model(name)
            A,C=selected_mask(m,"mixed")
            theta,D=independent_middle_path_owner_balance(m,A,C)
            for side in ("point","line"):
                x=full_core_book(m,A,C,side)
                self.assertEqual(x["source_full_core_theta"],theta)
                self.assertEqual(x["physical_max_degree_core"],D)
                self.assertLessEqual(x["source_book"]**2,x["F1"]*x["F2"])
                self.assertLessEqual(x["F1"],2*x["G"])
                self.assertLessEqual(x["source_full_core_theta"],
                                      4*len(A)*D)

    def test_04_partial_source_produced_BBo_inverse_independent_three_way(self):
        for name in ("W32","W33","Qminus24","dualQminus42",
                     "doubleW32","switchedDoubleW32"):
            m=make_model(name)
            A,C=selected_mask(m,"mixed")
            manual=manual_produced_bbo(m,A,C)
            self.assertEqual(manual,physical_bbo(m,A,C))
            self.assertEqual(manual,source_first_bbo(m,A,C))
            for k,paths in manual.items():
                self.assertEqual(len(set(k)),6)
                self.assertTrue(historical_bbo(m,k))
                self.assertEqual(source_bbo_inverse(m,k),paths)

    def test_05_missing_source_projections_are_not_filled_in(self):
        for name in ("doubleW32","switchedDoubleW32"):
            m=make_model(name)
            self.assertEqual(m["excess_lines"],15)
            self.assertEqual(len(m["missing"]),m["points"]*15)
            self.assertEqual(len(m["projection"]),len(m["projected"]))
            A,C=selected_mask(m,"full")
            result=inverse_certificate(m,A,C)
            self.assertTrue(result["missing_projections_not_completed"])
            self.assertTrue(result["exact_original_six_ID_nontrivial_inverse"])
            self.assertFalse(any(qr in m["projection"] for qr in m["missing"]))

    def test_06_frozen_source_anchors_not_in_CORE_need_only_in_FULL(self):
        m=make_model("W32")
        A,C=selected_mask(m,"mixed")
        self.assertTrue(C<A)
        for k in manual_produced_bbo(m,A,C):
            self.assertTrue(set(k)<=A)
        # C is independent of anchor storage; smaller C cannot be used
        # as a replacement for FULL in the original projection condition.
        self.assertEqual(physical_bbo(m,C,C),source_first_bbo(m,C,C))
        self.assertLessEqual(len(physical_bbo(m,C,C)),
                             len(physical_bbo(m,A,C)))

    def test_07_exact_endpoint_partition_separate_raw_orientations(self):
        for name,mask in (("W32","mixed"),("W33","mixed"),
                          ("Qminus24","mixed"),("doubleW32","mixed"),
                          ("switchedDoubleW32","mixed")):
            m=make_model(name)
            A,C=selected_mask(m,mask)
            e=endpoint_mask(m,A)
            other=independent_endpoint_mask(m,A)
            self.assertEqual(e["parts"],
               {k:other.get(k,0) for k in e["parts"]})
            self.assertEqual(e["total_bad"],sum(e["parts"].values()))
            self.assertLessEqual(e["total_bad"],e["total_conservative_cap"])
            self.assertEqual(e["total_bad"]+other["good"],
                             m["aP"]*(m["aP"]-1)*m["aL"]*(m["aL"]-1))

    def test_08_moore_hole_is_explicit_not_GQ_automatically(self):
        m=make_model("switchedDoubleW32")
        A,C=selected_mask(m,"full")
        result=endpoint_mask(m,A)
        self.assertEqual(result["parts"]["unprojected"],
                         4*m["points"]*m["excess_lines"])
        self.assertEqual(result["parts"]["unprojected"],4*30*15)
        self.assertGreater(result["parts"]["unprojected"],0)
        self.assertEqual(result["parts"]["deleted_anchors"],0)

    def test_09_deliberate_deleted_anchor_endpoint_charge(self):
        m=make_model("W32")
        full,C=selected_mask(m,"full")
        valid=manual_produced_bbo(m,full,C)
        self.assertGreater(len(valid),0)
        first=next(iter(sorted(valid)))
        six=[m["flags"][i] for i in first]
        p=next(q for q,n in Counter(q for q,ell in six).items() if n==2)
        ell=next(l for l,n in Counter(l for q,l in six).items() if n==2)
        central=m["flag_to_id"][p,ell]
        self.assertIn(central,first)
        A=full-{central}
        base=endpoint_mask(m,full)
        after=endpoint_mask(m,A)
        self.assertEqual(base["parts"]["deleted_anchors"],0)
        # A genuine produced endpoint with clean outer symbols has been
        # selected, so deleting its central anchor MUST create damage.
        self.assertGreater(after["parts"]["deleted_anchors"],0)
        self.assertLessEqual(after["parts"]["deleted_anchors"],
                             12*m["s"]*m["t"]*1)

    def test_10_source_book_rejects_CORE_outside_FULL(self):
        m=make_model("W32");A,C=selected_mask(m,"full")
        with self.assertRaises(ValueError):
            full_core_book(m,A-{0},{0})
        with self.assertRaises(ValueError):
            manual_produced_bbo(m,A-{0},C)
        with self.assertRaises(ValueError):
            full_core_book(m,A,A,"not-typed")
        with self.assertRaises(ValueError):
            selected_mask(m,"nonsense")

    def test_11_point_dual_books_are_both_proved_not_symmetry_assumed(self):
        for name in ("Qminus24","dualQminus42"):
            m=make_model(name)
            A,C=selected_mask(m,"full")
            p=full_core_book(m,A,C)
            l=full_core_book(m,A,C,"line")
            self.assertEqual(p["side"],"point")
            self.assertEqual(l["side"],"line")
            self.assertEqual(p["N_full"],l["N_full"])
            self.assertEqual(p["source_full_core_theta"],
                             l["source_full_core_theta"])
            self.assertTrue(p["exact_F1_le_2G"])
            self.assertTrue(l["exact_F1_le_2G"])

    def test_12_zero_CORE_implies_zero_books_and_no_BBo(self):
        m=make_model("W32")
        A,C=selected_mask(m,"empty_core")
        for side in ("point","line"):
            z=full_core_book(m,A,C,side)
            self.assertEqual(z["source_book"],0)
            self.assertEqual(z["source_full_core_theta"],0)
            self.assertEqual(z["physical_max_degree_core"],0)
        self.assertEqual(manual_produced_bbo(m,A,C),{})
        self.assertEqual(physical_bbo(m,A,C),{})

    def test_13_manual_physical_inverse_is_anchor_consistent(self):
        m=make_model("W32")
        A,C=selected_mask(m,"full")
        result=manual_produced_bbo(m,A,C)
        self.assertGreater(len(result),0)
        for k,paths in result.items():
            self.assertEqual(len(paths),2)
            p=next(p for p,n in Counter(m["flags"][i][0] for i in k).items()
                   if n==2)
            ell=next(l for l,n in Counter(m["flags"][i][1] for i in k).items()
                   if n==2)
            self.assertIn((p,ell),[m["flags"][i] for i in k])
            self.assertTrue(set(k)<=A)
            for path in paths:
                self.assertEqual(len({x for x,y in path}),4)
                self.assertEqual(len({y for x,y in path}),4)

    def test_14_sample_gf5_closed_sign_is_not_a_full_T3_claim(self):
        z=self.data
        self.assertTrue(z["source_first_equals_physical_first_for_partial_nonGQ"])
        self.assertTrue(z["full_A_core_C_never_conflated"])
        self.assertTrue(z["exact_mixed_book_Cauchy_and_Theta_bound"])
        self.assertTrue(z["no_abstract_T3_full_obstruction_claim"])

    def test_15_old_projection_mask_keeps_true_biregular_source_only(self):
        for name in ("W32","Qminus24","doubleW32",
                     "switchedDoubleW32"):
            m=make_model(name)
            mask=endpoint_mask(m,frozenset(range(len(m["flags"]))))
            self.assertEqual(mask["parts"]["deleted_anchors"],0)
            self.assertEqual(mask["parts"]["unprojected"],
                             4*m["points"]*m["excess_lines"])
            self.assertTrue(mask["all_nonincident_projections_unique_where_present"])


if __name__=="__main__":
    unittest.main()
