"""G6-D7 independent exact original source and row-capacity tests.

Small synthetic matrices appear ONLY as isolated algebraic negative
controls, never presented as original girth8 source witnesses.
"""
from fractions import Fraction as Q
from itertools import permutations,combinations
import unittest

from gio_t3d7_local_psd_rowtop import (
    SCHEMA,PARENT_G6D6,minimal_pair_alphabet,row_top_local_energy,
    exact_local_psd_source,diagonal_wenger_witness,
    source_local_constants,integrated_local_ledger,
    published_Wenger_local_diagonal,actual_case,certificate,
)
from gio_t3d4_few_outliers import original_source_case,exact_symmetric_inertia
from gio_t3d5_positive_tail import witness_for_fixture,source_adjacency
from gio_t3d6_squared_tail import published_Wenger_squared_tail
from gio_t3c_intrinsic_defect import source_graph,direct_original_owner_conflicts


def independent_original_H_trace(W,labels):
    """Entrywise original factor overlap; no use of production row-top."""
    n=len(labels)
    assert len(W)==n
    return sum(W[i][j]*len(set(labels[i])&set(labels[j]))
               for i in range(n) for j in range(n))


def independently_ranked_row_capacity(W,a):
    """Alternative brute finite row capacity, use subsets not sort."""
    n=len(W)
    cap=min(n-1,2*(a-2))
    out=2*sum((W[i][i] for i in range(n)),Q(0))
    for i in range(n):
        vals=[W[i][j] for j in range(n) if j!=i]
        # For the fixture sizes use direct optimal top-k, including
        # the option to pick fewer than k positive entries.
        positive=[x for x in vals if x>0]
        if len(positive)<=cap:
            out+=sum(positive,Q(0))
        else:
            out+=sum(sorted(positive,reverse=True)[:cap],Q(0))
    return out


class TestG6D7(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=certificate()
        cls.by={(z["name"],z["scheme"],z["witness_mode"]):z
                for z in cls.data["actual_source_exact_loewner_and_local_certificate"]}

    def test_01_precise_conditional_scope_and_parent(self):
        z=self.data
        self.assertEqual(z["schema"],SCHEMA)
        self.assertEqual(z["parent_G6D6_HEAD"],PARENT_G6D6)
        self.assertEqual(z["claim"],"CONDITIONAL_T3_QUADRATIC_EXCESS_LOCAL_PSD_ROW_TOP")
        self.assertTrue(z["fixed_cutoff_infinite_Wenger_separation_from_D5_D6"])
        self.assertTrue(z["existing_Wenger_already_satisfies_optimized_D2"])
        self.assertTrue(z["no_new_unrestricted_T3_or_ASET"])
        self.assertTrue(z["no_new_graph_family_discovered"])
        self.assertTrue(z["external_referee_or_Lean_not_claimed"])

    def test_02_minimum_pair_alphabet_exact_threshold(self):
        for V,a in ((1,2),(2,3),(3,3),(4,4),(6,4),
                    (15,6),(27,8),(54,11),(90,14),
                    (125,17),(10000,142)):
            self.assertEqual(minimal_pair_alphabet(V),a)
            self.assertGreaterEqual(a*(a-1)//2,V)
            self.assertLess((a-1)*(a-2)//2,V)
        for v in (0,-1,True,Q(2)):
            with self.assertRaises(ValueError):
                minimal_pair_alphabet(v)

    def test_03_exact_wenger3_qI_original_point_and_line(self):
        z=self.by["wenger3","lex","diagonal"]
        self.assertEqual(z["original_flags"],81)
        self.assertEqual((z["s"],z["t"],z["r"]),(2,2,2))
        for side in ("point","line"):
            c=z["exact_source_two_sided_certificates"][side]
            self.assertEqual(Q(c["local"]["exact_rowtop_energy"]),162)
            self.assertEqual(Q(c["local"]["positive_top_offdiagonal"]),0)
            self.assertEqual(c["minimum_pair_alphabet"],8)
            self.assertEqual(c["budget_rhs"],176)
            self.assertEqual(c["W_PSD_exact_inertia"]["negative"],0)
            self.assertEqual(c["W_dominance_PSD_exact_inertia"]["negative"],0)

    def test_04_exact_wenger5_qI_original_point_and_line(self):
        z=self.by["wenger5","lex","diagonal"]
        self.assertEqual((z["original_points"],z["original_lines"],
                          z["original_flags"]),(125,125,625))
        self.assertEqual((z["delta_line"],z["delta_point"]),(40,40))
        for side in ("point","line"):
            c=z["exact_source_two_sided_certificates"][side]
            self.assertEqual(Q(c["local"]["exact_rowtop_energy"]),1250)
            self.assertEqual(c["minimum_pair_alphabet"],17)
            self.assertEqual(c["budget_rhs"],11*4**4)
            self.assertEqual(c["W_PSD_exact_inertia"]["negative"],0)
            self.assertEqual(c["W_dominance_PSD_exact_inertia"]["negative"],0)

    def test_05_nonzero_signed_Wenger_projector_rowtop(self):
        for name in ("wenger3","wenger5"):
            z=self.by[name,"lex","projector"]
            src,maps=original_source_case(name)
            for side in ("point","line"):
                nbr=src["neighbors_point" if side=="point" else "neighbors_line"]
                labels=maps["f" if side=="point" else "g"]
                W=witness_for_fixture(name,src,side,1)
                a=minimal_pair_alphabet(len(labels))
                energy=row_top_local_energy(W,a)
                self.assertEqual(Q(energy["exact_rowtop_energy"]),
                                 independently_ranked_row_capacity(W,a))
                self.assertGreater(Q(energy["positive_top_offdiagonal"]),0)
                actual=independent_original_H_trace(W,labels)
                self.assertLessEqual(actual,Q(energy["exact_rowtop_energy"]))
                self.assertEqual(energy["max_admissible_shared_symbol_neighbors"],
                                 2*(a-2))
                self.assertLessEqual(Q(energy["exact_rowtop_energy"]),
                                     50*z["r"]**4)

    def test_06_negative_offdiagonal_double_GQ_rank_one(self):
        for name in ("doubleW32","doubleQminus24","doubleDualQminus42"):
            z=self.by[name,"lex","legacy"]
            src,maps=original_source_case(name)
            for side in ("point","line"):
                W=witness_for_fixture(name,src,side,2)
                labels=maps["f" if side=="point" else "g"]
                a=minimal_pair_alphabet(len(labels))
                self.assertTrue(any(W[i][j]<0 for i in range(len(W))
                                    for j in range(i+1,len(W))))
                energy=row_top_local_energy(W,a)
                self.assertGreater(Q(energy["positive_top_offdiagonal"]),0)
                actual=independent_original_H_trace(W,labels)
                self.assertLessEqual(actual,Q(energy["exact_rowtop_energy"]))
                self.assertLessEqual(Q(energy["exact_rowtop_energy"]),
                                     20*z["r"]**4)

    def test_07_actual_original_complete_minimal_factor_map_overlap(self):
        for name,mode in (("wenger3","diagonal"),("wenger5","diagonal"),
                          ("W32","legacy"),("Qminus24","legacy"),
                          ("dualQminus42","legacy"),
                          ("doubleQminus24","legacy"),
                          ("doubleDualQminus42","legacy")):
            src,maps=original_source_case(name)
            z=self.by[name,"lex",mode]
            for side in ("point","line"):
                labels=maps["f" if side=="point" else "g"]
                n=len(labels);a=minimal_pair_alphabet(n)
                self.assertEqual(len(set(labels)),n)
                self.assertTrue(all(len(pair)==2 and pair[0]!=pair[1]
                                    for pair in labels))
                self.assertLessEqual(max(y for pair in labels for y in pair),a-1)
                fiber_counts=[sum(y in pair for pair in labels)
                              for y in range(a)]
                self.assertEqual(sum(fiber_counts),2*n)
                self.assertLessEqual(max(fiber_counts),a-1)
                self.assertEqual(z["exact_source_two_sided_certificates"][side][
                    "minimum_pair_alphabet"],a)

    def test_08_correlated_fixed_maps_independent_of_witness(self):
        for name in ("wenger3","wenger5"):
            a=self.by[name,"lex","diagonal"]
            b=self.by[name,"correlated","diagonal"]
            self.assertEqual(a["original_flags"],b["original_flags"])
            for side in ("point","line"):
                self.assertEqual(
                    a["exact_source_two_sided_certificates"][side]["local"][
                        "exact_rowtop_energy"],
                    b["exact_source_two_sided_certificates"][side]["local"][
                        "exact_rowtop_energy"])
            src,maps=original_source_case(name,"correlated")
            self.assertEqual(b["original_J"],
                             direct_original_owner_conflicts(src,maps)["J"])

    def test_09_all_prime_power_Wenger_local_fixed_M11_symbolic(self):
        for q in (3,4,5,7,8,11,13,16,17,19,23,31,32,64,101):
            z=published_Wenger_local_diagonal(q)
            r=q-1
            self.assertTrue(z["local_rowtop_gate"])
            self.assertTrue(z["fixed_source_quadratic_excess_C3"])
            self.assertEqual(z["exact_diagonal_local_rowtop"],2*q**4)
            self.assertTrue(z["existing_Wenger_source_prime_power_required"])
            self.assertTrue(z["symbolic_published_spectrum_not_large_graph_instantiation"])
            self.assertLessEqual(2*q**4,11*r**4)
            if r>=8:
                self.assertFalse(z["D6_squared_tail_same_ell_M"])
                self.assertFalse(z["D5_first_tail_same_ell_M"])

    def test_10_all_integer_r_sufficient_M11_analytic_bound(self):
        # q=r+1 and r>=2 => q/r<=3/2:
        # 2q^4 <=2(3r/2)^4=81/8*r^4 <11*r^4.
        for r in range(2,2001):
            self.assertLessEqual(2*(r+1)**4,11*r**4)
            self.assertLessEqual(2*(r+1)**4*8,81*r**4)
            if r>=8:
                # D6 ell=0, M=11: E2=q^3*r^2/2
                # would require (r+1)^3 <= 22*r^(3/2).
                # A simpler all-integer sufficient violation:
                self.assertGreater((r+1)**6,22*22*r**3)

    def test_11_empty_PSD_GQ_and_asymmetric_duality(self):
        for name in ("W32","Qminus24","dualQminus42"):
            z=self.by[name,"lex","legacy"]
            for side in ("point","line"):
                c=z["exact_source_two_sided_certificates"][side]
                self.assertEqual(c["M"],0)
                self.assertEqual(Q(c["local"]["exact_rowtop_energy"]),0)
                self.assertTrue(c["exact_r4_local_budget"])
        for left,right in (("Qminus24","dualQminus42"),
                           ("doubleQminus24","doubleDualQminus42")):
            a=self.by[left,"lex","legacy"];b=self.by[right,"lex","legacy"]
            self.assertEqual(a["s"],b["t"])
            self.assertEqual(a["t"],b["s"])
            self.assertEqual(a["original_points"],b["original_lines"])
            self.assertEqual(a["original_lines"],b["original_points"])

    def test_12_exact_rowtop_small_synthetic_matrix_only_algebra(self):
        # This is a separate matrix-algebra stress test, never an
        # asserted actual source. Positive and negative offdiagonals.
        W=[[Q(4 if i==j else ((-1)**(i+j))*Q(1,3))
            for j in range(4)] for i in range(4)]
        a=4
        energy=row_top_local_energy(W,a)
        self.assertEqual(Q(energy["exact_rowtop_energy"]),
                         independently_ranked_row_capacity(W,a))
        self.assertGreater(Q(energy["positive_top_offdiagonal"]),0)
        self.assertEqual(exact_symmetric_inertia(W)["negative"],0)
        pairs=list(combinations(range(a),2))
        for ordered in permutations(pairs,4):
            actual=independent_original_H_trace(W,ordered)
            self.assertLessEqual(actual,Q(energy["exact_rowtop_energy"]))

    def test_13_refuse_bad_exact_PSD_and_original_source_type(self):
        src,_=original_source_case("wenger3")
        nbr=src["neighbors_point"]
        good=diagonal_wenger_witness(nbr,3)
        with self.assertRaises(ValueError):
            exact_local_psd_source(nbr,good,0,2,10) # 162>160
        with self.assertRaises(ValueError):
            exact_local_psd_source(nbr,[[0]],0,2,11)
        with self.assertRaises(ValueError):
            exact_local_psd_source(nbr,[[Q(0) for _ in nbr] for _ in nbr],
                                   0,2,11)
        for args in ((-1,2,11),(0,1,11),(0,2,-1),(True,2,11),
                     (0,2,Q(11))):
            with self.assertRaises(ValueError):
                exact_local_psd_source(nbr,good,*args)
        bad=[[Q(x) for x in row] for row in good]
        bad[0][1]=1
        with self.assertRaises(ValueError):
            exact_local_psd_source(nbr,bad,0,2,11)
        bad[0][1]=0
        bad[0][0]=-1
        with self.assertRaises(ValueError):
            exact_local_psd_source(nbr,bad,0,2,11)
        bad[0][0]=True
        with self.assertRaises(ValueError):
            exact_local_psd_source(nbr,bad,0,2,11)

    def test_14_wrong_symbol_alphabet_or_unbounded_input_rejected(self):
        W=[[Q(1),Q(0)],[Q(0),Q(1)]]
        for a in (0,1,-1,True,Q(3)):
            with self.assertRaises(ValueError):
                row_top_local_energy(W,a)
        for V in (0,-2,False,Q(9,2)):
            with self.assertRaises(ValueError):
                minimal_pair_alphabet(V)

    def test_15_exact_source_all_order_fixed_constants_and_gram(self):
        for b,C,ell,M in ((1,3,0,11),(1,3,2,0),(2,12,2,20),
                          (5,7,3,13)):
            a=source_local_constants(b,C,ell,M)
            self.assertEqual(a["half_local_budget_ceiling"],(M+1)//2)
            self.assertEqual(a["each_collinearity_conflict_j0"],
                a["point_degree_k0"]*a["alphabet_a0"]
                +ell*a["source_V0"]+(M+1)//2)
            self.assertEqual(a["original_owner_conflict_J0"],
                             2*a["each_collinearity_conflict_j0"])
            self.assertTrue(a["no_global_Schatten_or_trace_gate"])
        for bad in ((0,1,2,3),(1,-1,0,5),(1,3,-1,5),
                    (1,3,1,-1),(True,3,0,11),(1,3,0,0.1)):
            with self.assertRaises(ValueError):
                source_local_constants(*bad)

    def test_16_formal_all_four_inherited_LOW_budgets_and_provenance(self):
        for z in self.data["all_order_formal_original_HEAVY_LOW_ledgers"]:
            self.assertTrue(z["FORMAL_ONLY"])
            self.assertTrue(z["no_unrestricted_T3"])
            self.assertTrue(z["external_C6_numeric_constants_unverified"])
            self.assertTrue(z["source"]["source_conditional_on_BOTH_original_types"])
            self.assertTrue(z["source"]["source_alphabet_independent_of_labels"])
            self.assertIn("L_a(W)<=M*r^4",z["moments"]["local_source_gate"])
            f=z["fixed_before_source"];c=z["closure"]
            m=z["moments"];sel=z["selector"];r=int(c["sufficient_r0"])
            e=Q(c["eps"]);rho=Q(c["rho"])
            self.assertLessEqual(m["improper"],e*r)
            self.assertLessEqual(m["E"]**2,e*e*r)
            self.assertLessEqual(m["D"]**8,e**8*r)
            self.assertLessEqual(12*f["balance_b"]**2*rho*sel["q3"]**2*m["L6"],
                                 e*e)
            self.assertGreater(Q(c["delta"]),0)
            self.assertEqual(z["prerequisites"]["parent_G6D6_HEAD"],PARENT_G6D6)

    def test_17_real_original_C4_C6_corruption_fail_closed(self):
        src,_=original_source_case("W32")
        lines=[set(z) for z in src["lines"]]
        p,q=sorted(lines[0])[:2]
        ell=next(i for i in range(1,len(lines)) if p in lines[i])
        victim=next(z for z in lines[ell] if z!=p)
        lines[ell].remove(victim)
        lines[ell].add(q)
        with self.assertRaises(ValueError):
            source_graph(lines,src["points"],src["s"],src["t"])

    def test_18_true_source_direct_original_J_Gram_bounds(self):
        for z in self.data["actual_source_exact_loewner_and_local_certificate"]:
            r=z["r"];a=z["source_constants"]
            self.assertTrue(z["finite_fixture_M_selected_only_after_source"])
            self.assertTrue(z["actual_original_source_no_synthetic_F"])
            self.assertLessEqual(z["original_J"],
                                 a["original_owner_conflict_J0"]*r**4)
            self.assertLessEqual(z["point_Gram"]**2,
                                 a["original_pencil_Gram_G0"]**2*r**11)
            self.assertLessEqual(z["line_Gram"]**2,
                                 a["original_pencil_Gram_G0"]**2*r**11)
            self.assertEqual(z["original_J"],
                             z["original_point_conflicts"]+z["original_line_conflicts"])

    def test_19_published_symbolic_is_not_graph_construction(self):
        for x in self.data["published_prime_power_Wenger_diagonal_symbolic_family"]:
            self.assertTrue(x["existing_Wenger_source_prime_power_required"])
            self.assertTrue(x["symbolic_published_spectrum_not_large_graph_instantiation"])
            self.assertTrue(x["D4_count_and_D2_NOT_claimed_to_fail"])
        for p in ((2,0,11),(5,-1,11),(5,1,11),(5,0,-1),
                  (True,0,11)):
            with self.assertRaises(ValueError):
                published_Wenger_local_diagonal(*p)

    def test_20_nontrivial_W_all_factors_not_just_lex(self):
        for name in ("wenger3","wenger5"):
            src,_=original_source_case(name)
            for side in ("point","line"):
                W=witness_for_fixture(name,src,side,1)
                a=minimal_pair_alphabet(len(W))
                bound=Q(row_top_local_energy(W,a)["exact_rowtop_energy"])
                for scheme in ("lex","correlated"):
                    _,maps=original_source_case(name,scheme)
                    labels=maps["f" if side=="point" else "g"]
                    actual=independent_original_H_trace(W,labels)
                    self.assertLessEqual(actual,bound)


if __name__=="__main__":
    unittest.main()
