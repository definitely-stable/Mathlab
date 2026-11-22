"""Independent T3 boundary falsifiers; no reuse of GQ's structure() oracle."""
from collections import defaultdict
from fractions import Fraction
import unittest

from gio_generalized_gq import geometry
from gio_t3_axiom_boundary import (
    SCHEMA, BASE_MAIN, audit_incidence, certificate, deleted_projection_damage,
    disjoint_copies, remove_one_flag, exact_moore_gate, finite_case,
    regular_projection_excess_ledger, switched_connected_double, is_connected,
)


def independent_three_paths(lines, n):
    """Second oracle: construct all nonincident point->line length-3 walks."""
    on = [set() for _ in range(n)]
    for j, line in enumerate(lines):
        for p in line:
            on[p].add(j)
    out = {}
    for q in range(n):
        for r, line in enumerate(lines):
            if q in line:
                continue
            paths = set()
            for first_line in on[q]:
                for p in lines[first_line]:
                    if p != q and r in on[p]:
                        paths.add(((q, first_line), (p, first_line), (p, r)))
            out[q, r] = paths
    return out


class TestT3AxiomBoundary(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.c = certificate()
        cls.by = {row["kind"]: row for row in cls.c["cases"]}

    def test_01_exact_real_gq_fixtures_and_moore(self):
        for name in ("W32", "W33", "Qminus24", "dualQminus42"):
            row = self.by[name]
            self.assertTrue(row["moore"]["regular"])
            self.assertTrue(row["moore"]["exact_extremal_sizes"])
            self.assertTrue(row["moore"]["girth_at_least_eight"])
            self.assertTrue(row["moore"]["forces_full_unique_projection"])
            self.assertEqual(row["full"]["missing_pairs"], 0)
            self.assertEqual(row["full"]["multi_projection_pairs"], 0)

    def test_02_independent_all_three_walks_against_projection_oracle(self):
        for name in ("W32", "W33", "Qminus24", "dualQminus42"):
            g = geometry(name)
            a = audit_incidence(g["lines"], (g["s"]+1)*(g["s"]*g["t"]+1))
            second = independent_three_paths(g["lines"], a["points"])
            self.assertEqual(set(second), set(a["projected"]) | set(a["missing"]))
            for endpoint, paths in second.items():
                self.assertEqual(len(paths), 1)
                self.assertEqual(next(iter(paths)), a["projected"][endpoint])

    def test_03_two_distinct_projections_force_actual_six_cycle(self):
        lines = ((0,1),(1,2),(0,2))
        a = audit_incidence(lines, 3)
        self.assertFalse(a["girth_at_least_eight"])
        self.assertEqual(len(a["multiple"]), 3)
        self.assertEqual(len(a["missing"]), 0)
        v = a["cycle6_witness"]
        self.assertEqual(len(set(map(tuple, v["paths"][0])) |
                             set(map(tuple, v["paths"][1]))), 6)
        self.assertEqual(len(independent_three_paths(lines,3)[v["pair"]]), 2)

    def test_04_duplicate_edges_and_bad_ids_fail_closed(self):
        for lines, n in [(((0,0,1),),3),(((0,1),(0,1)),3),
                         (((0,2),),2),(((0,),),0)]:
            with self.assertRaises(ValueError):
                audit_incidence(lines,n)
        with self.assertRaises(ValueError):
            audit_incidence((), 2)

    def test_05_disjoint_double_preserves_biregularity_and_girth(self):
        for name in self.by:
            g=geometry(name)
            vp=(g["s"]+1)*(g["s"]*g["t"]+1)
            rows,n=disjoint_copies(g["lines"],vp)
            a=audit_incidence(rows,n)
            gate=exact_moore_gate(a,g["s"],g["t"])
            self.assertTrue(gate["regular"])
            self.assertFalse(gate["exact_extremal_sizes"])
            self.assertTrue(gate["girth_at_least_eight"])
            self.assertEqual(len(a["missing"]),2*vp*len(g["lines"]))
            self.assertEqual(len(a["projected"]),2*vp*(len(g["lines"])-(g["t"]+1)))

    def test_06_double_missing_exclusively_cross_component(self):
        g=geometry("W32")
        vp=(g["s"]+1)*(g["s"]*g["t"]+1)
        rows,n=disjoint_copies(g["lines"],vp)
        a=audit_incidence(rows,n)
        self.assertTrue(all((q<vp) != (ell<len(g["lines"]))
                            for q,ell in a["missing"]))
        self.assertEqual(Fraction(len(a["missing"]),
                           len(a["projected"])+len(a["missing"])),
                         Fraction(5,9))  # 2*15^2 / (4*15^2 - 2*45)

    def test_07_delete_one_flag_non_GQ_but_sparse_projection_defects(self):
        for name in self.by:
            g=geometry(name)
            vp=(g["s"]+1)*(g["s"]*g["t"]+1)
            shortened, removed=remove_one_flag(g["lines"])
            a=audit_incidence(shortened,vp)
            self.assertFalse(exact_moore_gate(a,g["s"],g["t"])["regular"])
            self.assertTrue(a["girth_at_least_eight"])
            self.assertEqual(len(a["missing"]),3*g["s"]*g["t"]+1)
            self.assertIn(removed,a["missing"])

    def test_08_exact_flag_load_and_adversarial_damage(self):
        for name in self.by:
            g=geometry(name);s,t=g["s"],g["t"]
            vp=(s+1)*(s*t+1)
            a=audit_incidence(g["lines"],vp)
            self.assertEqual(set(a["loads"]), set(a["flags"]))
            self.assertEqual(set(a["loads"].values()),{3*s*t})
            for z in (set(), {a["flags"][0]},
                      {a["flags"][0],a["flags"][-1]},
                      set(a["flags"][::max(1,len(a["flags"])//11)])):
                result=deleted_projection_damage(a,z)
                self.assertTrue(result["independent_inverse_exact"])
                self.assertLessEqual(result["affected_endpoints"],3*s*t*len(z))

    def test_09_independent_deletion_union_oracle(self):
        g=geometry("W32");a=audit_incidence(g["lines"],15)
        z={a["flags"][0],a["flags"][7],a["flags"][20]}
        # Different traversal: invert every source flag into its three-walk
        # end pairs and take the union in source-flag order.
        inverse=defaultdict(set)
        all_paths=independent_three_paths(g["lines"],15)
        for ends,paths in all_paths.items():
            for path in paths:
                for flag in path:
                    inverse[flag].add(ends)
        direct=set().union(*(inverse[x] for x in z))
        self.assertEqual(len(direct),
                         deleted_projection_damage(a,z)["affected_endpoints"])
        with self.assertRaises(ValueError):
            deleted_projection_damage(a,{(-1,-1)})

    def test_10_symbolic_fraction_tends_to_half(self):
        for s in (2,3,10,100,1000):
            v=(s+1)*(s*s+1)
            N=(s+1)*v
            fraction=Fraction(2*v*v,4*v*v-2*N)
            self.assertGreater(fraction,Fraction(1,2))
            self.assertLess(fraction,Fraction(3,5))
            self.assertEqual(fraction,Fraction(v,2*v-(s+1)))
        self.assertLess(Fraction((1000+1)*(1000**2+1),
                2*(1000+1)*(1000**2+1)-(1000+1))-Fraction(1,2),
                Fraction(1,100000))

    def test_12_biregular_girth8_exact_excess_not_just_moore(self):
        for name in self.by:
            g=geometry(name)
            vp=(g["s"]+1)*(g["s"]*g["t"]+1)
            a=audit_incidence(g["lines"],vp)
            base=regular_projection_excess_ledger(a,g["s"],g["t"])
            self.assertEqual(base["line_excess"],0)
            self.assertEqual(base["total_missing"],0)
            double_rows,double_pts=disjoint_copies(g["lines"],vp)
            twice=audit_incidence(double_rows,double_pts)
            led=regular_projection_excess_ledger(twice,g["s"],g["t"])
            self.assertEqual(led["line_excess"],len(g["lines"]))
            self.assertEqual(led["point_excess"],vp)
            self.assertEqual(led["total_missing"],2*vp*len(g["lines"]))
            self.assertEqual(led["exact_all_flag_projection_load"],3*g["s"]*g["t"])
            self.assertTrue(led["no_GQ_axiom_assumed"])

    def test_13_triple_copy_exact_excess_identity(self):
        g=geometry("W32");vp=15
        lines=tuple(g["lines"])+tuple(tuple(x+vp for x in L) for L in g["lines"]) + tuple(
            tuple(x+2*vp for x in L) for L in g["lines"])
        a=audit_incidence(lines,3*vp)
        led=regular_projection_excess_ledger(a,g["s"],g["t"])
        self.assertEqual(led["line_excess"],2*len(g["lines"]))
        self.assertEqual(len(a["missing"]),6*vp*len(g["lines"]))
        self.assertEqual(set(a["loads"].values()),{3*g["s"]*g["t"]})

    def test_15_connected_switched_double_preserves_girth_and_defect(self):
        for name in self.by:
            g=geometry(name);s,t=g["s"],g["t"]
            vp=(s+1)*(s*t+1)
            disjoined,n=disjoint_copies(g["lines"],vp)
            self.assertFalse(is_connected(audit_incidence(disjoined,n)))
            switched,n=switched_connected_double(g["lines"],vp)
            a=audit_incidence(switched,n)
            self.assertTrue(is_connected(a))
            self.assertTrue(a["girth_at_least_eight"])
            led=regular_projection_excess_ledger(a,s,t)
            self.assertEqual(led["total_missing"],2*vp*len(g["lines"]))
            self.assertEqual(led["exact_all_flag_projection_load"],3*s*t)
            self.assertEqual(led["point_excess"],vp)
            self.assertEqual(led["line_excess"],len(g["lines"]))
            self.assertTrue(self.by[name]["connected_switched_verified"])

    def test_16_switched_connected_literal_3walk_crosscheck(self):
        g=geometry("W32");rows,n=switched_connected_double(g["lines"],15)
        a=audit_incidence(rows,n)
        alt=independent_three_paths(rows,n)
        self.assertEqual(sum(not p for p in alt.values()),len(a["missing"]))
        self.assertEqual(sum(len(p)==1 for p in alt.values()),len(a["projected"]))
        self.assertEqual(sum(len(p)>1 for p in alt.values()),0)
        for flag in a["flags"][::5]:
            self.assertEqual(a["loads"][flag],3*g["s"]*g["t"])

    def test_14_regular_excess_gate_rejects_irregular_and_short_cycle(self):
        g=geometry("W32")
        shortened,_=remove_one_flag(g["lines"])
        with self.assertRaises(ValueError):
            regular_projection_excess_ledger(audit_incidence(shortened,15),2,2)
        with self.assertRaises(ValueError):
            regular_projection_excess_ledger(
                audit_incidence(((0,1),(1,2),(0,2)),3),1,1)

    def test_11_domain_guards_and_no_false_full_T3_claim(self):
        self.assertEqual(self.c["schema"],SCHEMA)
        self.assertEqual(self.c["frozen_base_main_sha"],BASE_MAIN)
        self.assertEqual(self.c["claim"],"PROVED_RESTRICTED_AXIOM_BOUNDARY_NOT_T3")
        self.assertTrue(self.c["no_full_abstract_T3_motif_theorem"])
        self.assertTrue(self.c["no_general_ASET_exponent"])
        self.assertTrue(self.c["no_external_referee"])
        with self.assertRaises(ValueError):
            exact_moore_gate(audit_incidence(((0,1),),2),0,1)
        self.assertEqual(set(self.by),{"W32","W33","Qminus24","dualQminus42"})


if __name__=="__main__":
    unittest.main()
