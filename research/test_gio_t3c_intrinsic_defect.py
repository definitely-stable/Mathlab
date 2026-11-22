"""Independent exact incidence/spectral falsifiers for #793 G6-C1."""
from collections import Counter, defaultdict
from itertools import combinations
from math import comb
import random
import unittest

from gio_generalized_gq import geometry
from gio_t3c_intrinsic_defect import (
    SCHEMA, BASE_MAIN, certificate, source_graph, defect_matrices,
    exact_second_walk_identity, typed_maps, typed_conflicts_and_gram,
    direct_original_owner_conflicts, spectral_cap, coarse_linear_excess_ledger,
    finite_case, doubled_gq, shortcycle_edit_from_gq,
    rainbow_c6_universal_source_inverse, ceil_sqrt,
)


def independent_collinearity_from_incidence(m):
    """Completely independent point adjacency from each original line."""
    rows=[set() for _ in range(m["points"])]
    for line in m["lines"]:
        for p in line:
            rows[p].update(set(line)-{p})
    return rows


def independent_missing_projections_from_all_threepaths(m):
    """Length-three source-walk oracle, no reuse of projected or missing."""
    on=[set() for _ in range(m["points"])]
    for ell,line in enumerate(m["lines"]):
        for p in line:
            on[p].add(ell)
    missing=set(); multiplicity=Counter()
    for q in range(m["points"]):
        for ell,line in enumerate(m["lines"]):
            if ell in on[q]:
                continue
            three_paths=set()
            for first in on[q]:
                for foot in m["lines"][first]:
                    if foot!=q and ell in on[foot]:
                        three_paths.add(((q,first),(foot,first),(foot,ell)))
            multiplicity[len(three_paths)]+=1
            if not three_paths:
                missing.add((q,ell))
    return missing,multiplicity


def independent_defect_from_common_neighbors(neighbors,s,t):
    """Recover D solely from A^2 and regular parameters, no geometry paths."""
    V=len(neighbors);k=s*(t+1);mu=t+1;theta=s-t-2
    return [[(k-mu)*(i==j)+theta*(j in neighbors[i])+mu
             -len(neighbors[i]&neighbors[j])
             for j in range(V)] for i in range(V)]


def rayleigh_exact_checks(neighbors, cap, seed):
    """Deterministic explicit integer zero-sum vector witnesses."""
    V=len(neighbors)
    vectors=[]
    for i,j in ((0,1),(0,V-1),(V//3,2*V//3)):
        if i!=j:
            x=[0]*V;x[i]=1;x[j]=-1
            vectors.append(x)
    rand=random.Random(seed)
    for _ in range(8):
        x=[rand.randint(-5,5) for _ in range(V)]
        total=sum(x)
        x=[V*y-total for y in x]
        vectors.append(x)
    for x in vectors:
        assert sum(x)==0
        lhs=sum(sum(x[j] for j in neighbors[i])**2 for i in range(V))
        rhs=cap**2*sum(y*y for y in x)
        if lhs>rhs:
            raise AssertionError(("spectral cap violated",lhs,rhs))
    return len(vectors)


class TestGIO003G6C(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.c=certificate()
        cls.by={x["kind"]+":"+x["scheme"]:x for x in cls.c["finite_cases"]}

    def test_01_independently_confirm_source_Moore_defect(self):
        for kind in ("W32","W33","Qminus24","dualQminus42",
                     "doubleW32","switchedDoubleW32"):
            if kind in ("doubleW32","switchedDoubleW32"):
                lines,P,s,t=doubled_gq("W32",kind=="switchedDoubleW32")
            else:
                g=geometry(kind);lines,s,t=g["lines"],g["s"],g["t"]
                P=(s+1)*(s*t+1)
            m=source_graph(lines,P,s,t)
            missing,mults=independent_missing_projections_from_all_threepaths(m)
            self.assertEqual(missing,set(m["missing"]))
            self.assertNotIn(2,mults)
            self.assertEqual(len(missing),P*m["excess_lines"])
            self.assertEqual(len(m["projected"]),P*(t+1)*s*t)
            self.assertEqual(set(m["projection_load"].values()),{3*s*t})
            self.assertEqual(independent_collinearity_from_incidence(m),
                             m["neighbors_point"])

    def test_02_true_point_and_dual_unequal_matrix_identity(self):
        for kind in ("W32","W33","Qminus24","dualQminus42",
                     "doubleW32","switchedDoubleW32"):
            z=self.by[kind+":lex"]
            if kind in ("doubleW32","switchedDoubleW32"):
                lines,P,s,t=doubled_gq("W32",kind=="switchedDoubleW32")
            else:
                g=geometry(kind);lines,s,t=g["lines"],g["s"],g["t"]
                P=(s+1)*(s*t+1)
            m=source_graph(lines,P,s,t)
            Dp,Dl,d=defect_matrices(m)
            self.assertEqual(Dp,independent_defect_from_common_neighbors(
                m["neighbors_point"],s,t))
            self.assertEqual(Dl,independent_defect_from_common_neighbors(
                m["neighbors_line"],t,s))
            self.assertEqual(d,(s+1)*m["excess_lines"])
            self.assertEqual(d,(t+1)*m["excess_points"])
            self.assertTrue(z["point_matrix"]["exact_identity"])
            self.assertTrue(z["line_matrix"]["exact_identity"])
            self.assertEqual(z["exact_common_defect_row"],d)

    def test_03_zero_defect_recovers_actual_GQ_srg_both_typed_graphs(self):
        for kind in ("W32","W33","Qminus24","dualQminus42"):
            z=self.by[kind+":lex"]
            self.assertEqual(z["source_excess_points"],0)
            self.assertEqual(z["source_excess_lines"],0)
            self.assertEqual(z["missing"],0)
            self.assertEqual(z["point_label"]["defect_correction"],0)
            self.assertEqual(z["line_label"]["defect_correction"],0)
            self.assertEqual(z["point_matrix"]["theta"],z["s"]-z["t"]-2)
            self.assertEqual(z["line_matrix"]["theta"],z["t"]-z["s"]-2)

    def test_04_large_excess_correction_not_silently_dropped(self):
        for kind in ("doubleW32","switchedDoubleW32"):
            z=self.by[kind+":lex"]
            self.assertEqual(z["source_excess_points"],15)
            self.assertEqual(z["source_excess_lines"],15)
            self.assertEqual(z["missing"],30*15)
            self.assertEqual(z["exact_common_defect_row"],45)
            self.assertTrue(z["point_label"]["repaired_gram_formula"])
            self.assertTrue(z["line_label"]["repaired_gram_formula"])
            self.assertGreater(z["point_label"]["defect_correction"]+
                               z["line_label"]["defect_correction"],0)
            # The naive GQ equality with D=0 MUST be false on this model.
            self.assertGreater(z["point_label"]["defect_correction"],0)

    def test_05_direct_original_owner_conflict_vs_collinearity(self):
        for kind in ("W32","W33","Qminus24","dualQminus42",
                     "doubleW32","switchedDoubleW32"):
            for scheme in ("lex","correlated"):
                if kind+":"+scheme in self.by:
                    z=self.by[kind+":"+scheme]
                elif kind=="W32":
                    z=finite_case(kind,scheme)
                else:
                    continue
                self.assertEqual(z["owner_conflicts"]["J"],
                    z["point_label"]["e_col"]+z["line_label"]["e_col"])
                self.assertEqual(z["owner_conflicts"]["via_line"],
                    z["point_label"]["e_col"])
                self.assertEqual(z["owner_conflicts"]["via_point"],
                    z["line_label"]["e_col"])

    def test_06_all_fixed_linear_excess_quantities_are_integer_safe(self):
        for z in self.c["finite_cases"]:
            led=z["spectral_and_conflict_ledger"]
            r=min(z["s"],z["t"])
            C=led["excess_multiplier"]
            self.assertLessEqual(z["source_excess_lines"],C*r)
            self.assertLessEqual(z["owner_conflicts"]["J"],
                led["exact_conflict_J_upper"])
            self.assertLessEqual(z["point_label"]["gram"]**2,
                led["exact_pencil_square_squared_upper"])
            self.assertLessEqual(z["line_label"]["gram"]**2,
                led["exact_pencil_square_squared_upper"])
            self.assertTrue(led["no_GQ_spectrum_assumed"])
            self.assertTrue(led["no_external_C6_input_used"])
            self.assertTrue(led["exact_one_sided_point_and_line_spectral_bound"])

    def test_07_exact_rayleigh_zero_sum_eigenvalue_cap(self):
        for kind in ("W32","W33","Qminus24","dualQminus42",
                     "doubleW32","switchedDoubleW32"):
            z=self.by[kind+":lex"]
            if kind in ("doubleW32","switchedDoubleW32"):
                lines,P,s,t=doubled_gq("W32",kind=="switchedDoubleW32")
            else:
                g=geometry(kind);lines,s,t=g["lines"],g["s"],g["t"]
                P=(s+1)*(s*t+1)
            m=source_graph(lines,P,s,t)
            self.assertGreaterEqual(
                rayleigh_exact_checks(m["neighbors_point"],
                    z["point_spectrum_upper"],73),10)
            self.assertGreaterEqual(
                rayleigh_exact_checks(m["neighbors_line"],
                    z["line_spectrum_upper"],97),10)

    def test_08_fail_closed_invalid_regular_girth_or_excess(self):
        g=geometry("W32");P=15
        with self.assertRaises(ValueError):
            source_graph((g["lines"][0],g["lines"][0])+g["lines"][1:],P,2,2)
        with self.assertRaises(ValueError):
            source_graph(g["lines"][:-1],P,2,2)
        with self.assertRaises(ValueError):
            source_graph(g["lines"],P,1,2)
        with self.assertRaises(ValueError):
            source_graph(g["lines"],P,2,1)
        from gio_t3c_intrinsic_defect import shortcycle_edit_from_gq
        edited,base,sw=shortcycle_edit_from_gq()
        rebuilt=[set() for _ in range(len(base["lines"]))]
        for p,l in edited:
            rebuilt[l].add(p)
        with self.assertRaises(ValueError):
            source_graph(rebuilt,15,2,2)

    def test_09_near_Moore_linear_threshold_is_not_quadratic_threshold(self):
        lines,P,s,t=doubled_gq("W32",True)
        m=source_graph(lines,P,s,t)
        maps=typed_maps(m)
        Dp,Dl,d=defect_matrices(m)
        pdata=typed_conflicts_and_gram(m,maps["f"],m["neighbors_point"],Dp,s,t)
        ldata=typed_conflicts_and_gram(m,maps["g"],m["neighbors_line"],Dl,t,s)
        point=exact_second_walk_identity(m["neighbors_point"],Dp,s,t)
        line=exact_second_walk_identity(m["neighbors_line"],Dl,t,s)
        for args in ((0,8),(1,0),(0,0),(1,-1),(1,7)):
            with self.assertRaises(ValueError):
                coarse_linear_excess_ledger(m,maps,point,line,pdata,ldata,*args)
        led=coarse_linear_excess_ledger(m,maps,point,line,pdata,ldata,1,8)
        self.assertEqual(led["excess_multiplier"],8)

    def test_10_universal_proper_physical_C6_inverse_on_actual_nonGQ_C4(self):
        v=self.c["physical_rainbow_C6_inverse"]
        self.assertTrue(v["non_GQ_C4"])
        self.assertTrue(v["physical_first_equals_source_first"])
        self.assertTrue(v["no_projection_or_GQ_hypothesis"])
        self.assertGreater(v["source_original_six_ID_D6"],0)
        self.assertEqual(v["real_physical_rainbow_C6"],
                         v["source_original_six_ID_D6"])
        self.assertEqual(v["edited_source_flags"],45)

    def test_11_critical_external_facts_not_asserted_by_certificate(self):
        c=self.c
        self.assertEqual(c["schema"],SCHEMA)
        self.assertEqual(c["frozen_base_main_sha"],BASE_MAIN)
        self.assertEqual(c["claim"],
            "PROVED_CONDITIONAL_INTRINSIC_A1_A2_A3_NOT_FULL_T3")
        self.assertTrue(c["fixed_balance_and_linear_excess_constants_must_precede_family"])
        self.assertTrue(c["existence_of_infinite_non_GQ_small_excess_family_not_claimed"])
        self.assertTrue(c["no_intrinsic_A4_A5_A6_mixed_book_or_BBo_supersaturation"])
        self.assertTrue(c["no_full_abstract_T3_theorem"])
        self.assertTrue(c["no_unrestricted_ASET_exponent"])
        self.assertTrue(c["no_external_referee_or_Lean_certificate"])

    def test_12_square_root_bound_is_exact_and_strongly_typed(self):
        for n in (0,1,2,3,4,15,16,17,48,49,50,10**9):
            k=ceil_sqrt(n)
            self.assertGreaterEqual(k*k,n)
            if k:
                self.assertLess((k-1)**2,n)
        for bad in (-1,1.5,True):
            with self.assertRaises(ValueError):
                ceil_sqrt(bad)
        for k,theta,mu,d in ((6,-2,3,45),(12,0,3,0),(10,-4,5,0)):
            x=spectral_cap(k,theta,mu,d)
            self.assertGreaterEqual(x*x-abs(theta)*x,k-mu+d)

    def test_14_defect_matrix_is_NOT_positive_semidefinite(self):
        # In disconnected double W32, every cross-component point pair
        # has exactly t+1 missing 3path line choices. Thus Dp has block
        # form [0,3*J;3*J,0], whose signed vector (1^15,-1^15) has
        # exact negative eigenvalue -45. Any proof using D>=0 in the
        # positive-semidefinite sense would be invalid.
        lines,P,s,t=doubled_gq("W32",False)
        m=source_graph(lines,P,s,t)
        Dp,Dl,d=defect_matrices(m)
        x=[1]*(P//2)+[-1]*(P//2)
        self.assertEqual(sum(x),0)
        self.assertEqual(d,45)
        self.assertEqual([sum(Dp[i][j]*x[j] for j in range(P))
                          for i in range(P)],[-d*z for z in x])
        self.assertEqual(
            sum(x[i]*Dp[i][j]*x[j] for i in range(P) for j in range(P)),
            -d*sum(z*z for z in x))
        self.assertTrue(all(y>=0 for row in Dp for y in row))

    def test_13_fixture_metadata_and_proper_alphabet_scales(self):
        expect={"W32":(15,15,45),"W33":(40,40,160),
                "Qminus24":(27,45,135),"dualQminus42":(45,27,135),
                "doubleW32":(30,30,90),"switchedDoubleW32":(30,30,90)}
        for name,(np,nl,ns) in expect.items():
            z=self.by[name+":lex"]
            self.assertEqual((z["points"],z["lines"],z["flags"]),(np,nl,ns))
            self.assertGreaterEqual(comb(z["point_label"]["alphabet"],2),np)
            self.assertGreaterEqual(comb(z["line_label"]["alphabet"],2),nl)


if __name__=="__main__":
    unittest.main()
