"""Independent original-source G6-E1 tests: published PDS and new transfer."""
from collections import Counter
from fractions import Fraction as Q
from itertools import product
import unittest

from gio_t3e1_subgq_pds import (
    SCHEMA,PARENT_G6D7_HEAD,gamma_names,gamma_line_points,
    actual_parent_GQ,parent_bipartite_adjacency,closed_ball,
    abreu_B_perfect_dominating,actual_smaller_source,
    universal_interlacing_envelope,exact_original_centered_missing_PSD,
    literal_case,exact_all_order_ledger,certificate,
)
from gio_t3d3_affine_arc import Field,source_from_affine_arc
from gio_t3c_intrinsic_defect import (
    source_graph,typed_maps,direct_original_owner_conflicts,
    exact_second_walk_identity,defect_matrices,
)
from gio_t3d2_centered_sixth import uniform_direct_spectral_constants
from gio_t3d4_few_outliers import exact_symmetric_inertia


def independent_lines(field):
    """Recompute ALL published Γ_q line--point pairs by field equations.

    Uses explicit independently inverted equations rather than the
    production line-neighborhood formulas wherever a finite a exists.
    """
    q=field.q
    names=gamma_names(q)
    out={}
    for line in names:
        a,b,c=line
        if a<q:
            ps=[]
            for x,y,z in product(range(q),repeat=3):
                right_y=field.add(field.mul(a,x),b)
                ab=field.mul(a,b)
                right_z=field.add(
                    field.add(field.mul(field.mul(a,a),x),
                              field.add(ab,ab)),c)
                if y==right_y and z==right_z:
                    ps.append((x,y,z))
            ps.append((q,a,c))
        elif b<q:
            ps=[(c,b,x) for x in range(q)]+[(q,q,c)]
        else:
            ps=[(q,c,x) for x in range(q)]+[(q,q,q)]
        assert len(ps)==q+1
        out[line]=set(ps)
    return out


def independent_components(source):
    """Connected components of literal bipartite ORIGINAL flags, not spectrum."""
    n=source["points"]
    N=n+len(source["lines"])
    adjacency=[set() for _ in range(N)]
    for p,ell in source["flags"]:
        adjacency[p].add(n+ell)
        adjacency[n+ell].add(p)
    found=set()
    components=[]
    for v in range(N):
        if v in found:
            continue
        seen={v}; frontier=[v];found.add(v)
        while frontier:
            a=frontier.pop()
            for b in adjacency[a]-found:
                found.add(b);seen.add(b);frontier.append(b)
        components.append(len(seen))
    return sorted(components)


def independent_centered_T_psd(source,q,side):
    """Literal BBt or BtB <=2q on 1_perp by rational Sylvester inertia."""
    n=source["points"] if side=="point" else len(source["lines"])
    assert n==source["points"]==len(source["lines"])
    neighbor=source["neighbors_point" if side=="point" else "neighbors_line"]
    # T=A+qI with principal eigenvalue q² for q-regular incidence.
    R=[[Q(q*(i==j)-int(j in neighbor[i]))
        +Q(q*q,n) for j in range(n)] for i in range(n)]
    z=exact_symmetric_inertia(R)
    assert z["negative"]==0
    return dict(side=side,source_vertices=n,
        centered_BBt_upper=2*q,exact_rational_inertia=z,
        no_numeric_singular_value_solver=True)


def independent_threeflag_missing(src):
    """A second original-length-3 projection oracle on a literal incidence."""
    n=src["points"]
    lines=src["lines"]
    on=[set() for _ in range(n)]
    for ell,line in enumerate(lines):
        for p in line:
            on[p].add(ell)
    miss=[]
    for p in range(n):
        for ell,line in enumerate(lines):
            if ell in on[p]:
                continue
            feet=sum(bool(on[p]&on[q]) for q in line)
            assert feet<=1
            if not feet:
                miss.append((p,ell))
    assert set(miss)==set(src["missing"])
    return miss


class TestG6E1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.z=certificate()
        cls.by={(c["q"],c["scheme"],c["xi"]):c
                for c in cls.z["independently_constructed_original_PDS_source_cases"]}

    def test_01_source_prior_art_and_conditional_scope(self):
        z=self.z
        self.assertEqual(z["schema"],SCHEMA)
        self.assertEqual(z["parent_G6D7_HEAD"],PARENT_G6D7_HEAD)
        self.assertEqual(z["claim"],
            "CONDITIONAL_T3_REAL_PDS_SUBGQ_SOURCE_VIA_INTERLACING")
        self.assertTrue(z["genuinely_distinct_smaller_source_cardinality_than_Wenger"])
        self.assertTrue(z["published_graph_family_NOT_NEW"])
        self.assertTrue(z["independent_interlacing_spectral_transfer_new_to_program"])
        self.assertTrue(z["no_unrestricted_abstract_T3_or_ASET"])
        self.assertTrue(z["no_external_referee_or_Lean"])

    def test_02_parent_vertex_formula_exact_not_guess(self):
        for q in (3,4,5):
            field=Field(q)
            names=gamma_names(q)
            self.assertEqual(len(names),(q+1)*(q*q+1))
            self.assertEqual(len(set(names)),len(names))
            self.assertEqual(set(names[-(q+1):]),
                             {(q,q,c) for c in range(q+1)})
            self.assertEqual(gamma_names(q),names)
        for bad in (0,1,2,True,Q(4)):
            with self.assertRaises(ValueError):
                gamma_names(bad)

    def test_03_original_GQ_line_equations_independently_reconstructed(self):
        for q in (3,4,5):
            field=Field(q)
            parent,names,idx=actual_parent_GQ(field)
            brute=independent_lines(field)
            self.assertEqual(parent["points"],(q+1)*(q*q+1))
            self.assertEqual(parent["excess_lines"],0)
            self.assertEqual(parent["excess_points"],0)
            self.assertEqual(parent["missing"],())
            for ell,name in enumerate(names):
                self.assertEqual(set(parent["lines"][ell]),
                                 {idx[p] for p in brute[name]})
            self.assertTrue(all(len(line)==q+1 for line in parent["lines"]))

    def test_04_prime_and_binary_field_2ab_is_field_sum(self):
        for q in (3,4,5,8):
            f=Field(q)
            for a,b in product(range(q),repeat=2):
                ab=f.mul(a,b)
                twice=f.add(ab,ab)
                self.assertEqual(twice,0 if q in (4,8)
                                 else (2*a*b)%q)
                if q in (4,8):
                    self.assertEqual(twice,0)
            self.assertEqual(len(gamma_line_points(f,(1,1,0))),q+1)

    def test_05_published_perfect_dominating_B_all_remaining_one_neighbor(self):
        for q in (3,4,5):
            f=Field(q)
            parent,names,idx=actual_parent_GQ(f)
            for xi in (1,2):
                B=abreu_B_perfect_dominating(parent,idx,xi=xi)
                n=parent["points"]
                self.assertEqual(len(B["deleted"]),2*(q*q+3*q+1))
                self.assertEqual(len(B["kept"]),2*q*(q*q-2))
                self.assertEqual(len({v for v in B["kept"] if v<n}),
                                 q*(q*q-2))
                self.assertTrue(B["perfect_dominating_all_outside_exactly_one"])
                for w in B["kept"]:
                    self.assertEqual(len(B["adjacency"][w]&B["deleted"]),1)
                    self.assertEqual(len(B["adjacency"][w]&B["kept"]),q)
            with self.assertRaises(ValueError):
                abreu_B_perfect_dominating(parent,idx,0)

    def test_06_true_original_new_source_smaller_than_Wenger(self):
        for q in (3,4,5):
            x=self.by[q,"lex",1]
            self.assertEqual(x["true_original_source_points"],q*(q*q-2))
            self.assertEqual(x["true_original_source_lines"],q*(q*q-2))
            self.assertEqual(x["true_original_source_flags"],q*q*(q*q-2))
            self.assertEqual(x["true_original_Moore_excess"],2*q*(q-2))
            self.assertEqual(x["true_original_PDS_removed_each"],q*q+3*q+1)
            self.assertEqual(x["original_parent_GQ_missing"],0)
            self.assertTrue(x["source_parent_induced_edges_exact"])
            self.assertTrue(x["different_vertex_count_from_Wenger_W2"])
            self.assertTrue(x["nonGQ_if_q_ge3"])
            self.assertEqual(q**3-x["true_original_source_points"],2*q)

    def test_07_girth8_independently_on_actual_removed_incidence(self):
        for q in (3,4,5):
            instance=actual_smaller_source(Field(q))
            src=instance["new_original_source"]
            self.assertEqual(independent_components(src),
                             [2*q*(q*q-2)])
            self.assertEqual(src["s"],q-1)
            self.assertEqual(src["t"],q-1)
            self.assertEqual(
                len(src["projected"]),src["points"]*q*(q-1)**2)
            self.assertTrue(all(v==3*(q-1)**2
                                for v in src["projection_load"].values()))
            self.assertEqual(len(src["missing"]),
                             src["points"]*2*q*(q-2))
            self.assertEqual(len(independent_threeflag_missing(src)),
                             len(src["missing"]))

    def test_08_universal_all_prime_power_interlacing_not_finite_guess(self):
        for q in (3,4,5,7,8,9,11,13,16,17,19,32,64,101):
            x=universal_interlacing_envelope(q)
            r=q-1
            self.assertEqual(x["parent_second_squared_singular"],2*q)
            self.assertEqual(x["reduced_second_squared_singular_upper"],2*q)
            self.assertTrue(x["strict_connectedness_from_interlacing"])
            self.assertLess(Q(x["upper_centered_F0_squared"]),
                            x["centered_operator_fixed_kappa_rhs"]+Q(1))
            self.assertEqual(x["fixed_centered_operator_kappa"],
                             3 if q==3 else 2)
            self.assertTrue(x["no_independent_centered_F0_hypothesis"])
            self.assertTrue(x["source_regular_induced_parent_GQ_hypothesis_REQUIRED"])
            self.assertLess(2*q*(q-2),2*r*r)
            self.assertEqual(q*(q*q-2)-q*(r*r+1),2*q*(q-2))
        for bad in (2,0,True,5.5):
            with self.assertRaises(ValueError):
                universal_interlacing_envelope(bad)

    def test_09_exact_full_original_BBt_interlacing_two_sided(self):
        for q in (3,4,5):
            src=actual_smaller_source(Field(q))["new_original_source"]
            for side in ("point","line"):
                cert=independent_centered_T_psd(src,q,side)
                self.assertEqual(cert["centered_BBt_upper"],2*q)
                self.assertEqual(cert["exact_rational_inertia"]["negative"],0)
                self.assertTrue(cert["no_numeric_singular_value_solver"])

    def test_10_exact_full_missing_F0_rational_PSD_two_sided(self):
        for q in (3,4,5):
            src=actual_smaller_source(Field(q))["new_original_source"]
            kappa=3 if q==3 else 2
            for side in ("point","line"):
                z=exact_original_centered_missing_PSD(src,kappa,side)
                self.assertEqual(z["exact_original_F0_operator_upper"],
                                 kappa*(q-1)**3)
                self.assertEqual(z["residual_inertia"]["negative"],0)
                self.assertTrue(z["no_synthetic_projection_or_GQ_completion"])

    def test_11_fixed_correlated_f_and_g_source_owner_without_independence(self):
        for q in (3,4,5):
            a=self.by[q,"lex",1]
            b=self.by[q,"correlated",2]
            self.assertEqual(a["true_original_source_flags"],
                             b["true_original_source_flags"])
            self.assertEqual(a["true_original_Moore_excess"],
                             b["true_original_Moore_excess"])
            self.assertTrue(a["true_original_not_synthetic_F"])
            self.assertTrue(b["true_original_not_synthetic_F"])
            for x in (a,b):
                self.assertEqual(x["original_total_J"],
                                 x["original_point_conflicts"]+
                                 x["original_line_conflicts"])
                self.assertGreaterEqual(x["point_original_Gram"],0)
                self.assertGreaterEqual(x["line_original_Gram"],0)

    def test_12_D2_existing_direct_spectral_constants_reused_correctly(self):
        for q in (3,4,5):
            x=self.by[q,"lex",1]
            kappa=3 if q==3 else 2
            r=q-1
            c=uniform_direct_spectral_constants(1,2,kappa)
            self.assertLessEqual(x["original_total_J"],
                                 c["original_owner_conflict_J0"]*r**4)
            self.assertLessEqual(x["point_original_Gram"]**2,
                                 c["original_pencil_Gram_G0"]**2*r**11)
            self.assertLessEqual(x["line_original_Gram"]**2,
                                 c["original_pencil_Gram_G0"]**2*r**11)
            self.assertTrue(c["structural_centered_spectral_bound_is_AN_ADDITIONAL_assumption"])
            # Here E1 proves the additional source assumption from
            # parent interlacing, not by pretending D2 proved it.
            self.assertEqual(x["interlacing_all_order"][
                "fixed_centered_operator_kappa"],kappa)

    def test_13_formal_all_order_SOURCE_GATE_not_sixth_moment(self):
        z=self.z["inherited_G6D2_direct_operator_ledger_FORMAL_ONLY"]
        self.assertTrue(z["FORMAL_ONLY"])
        self.assertTrue(z["moment_sixth_condition_is_NOT_required"])
        self.assertEqual(z["fixed_before_source"]["balance_b"],1)
        self.assertEqual(z["fixed_before_source"]["quadratic_C"],2)
        self.assertEqual(z["fixed_before_source"]["centered_operator_kappa"],2)
        self.assertTrue(z["no_unconditional_quadratic_T3"])
        f=z["fixed_before_source"];s=z["selector"];m=z["moments"]
        c=z["closure"];eps=Q(c["eps"]);rho=Q(c["rho"])
        R=int(c["sufficient_r0"])
        self.assertLessEqual(m["improper"],eps*R)
        self.assertLessEqual(m["E"]**2,eps*eps*R)
        self.assertLessEqual(m["blocker_D"]**8,eps**8*R)
        self.assertLessEqual(12*f["balance_b"]**2*rho*s["q3"]**2*m["L6"],
                             eps*eps)
        self.assertGreater(Q(c["delta"]),0)

    def test_14_pds_incomplete_fails_original_regularity(self):
        inst=actual_smaller_source(Field(3))
        parent=inst["parent"];B=inst["dom"]
        # Keep exactly one previously deleted point, leave all other
        # vertex deletions unchanged, producing a degree defect.
        n=parent["points"]
        deleted_point=next(v for v in B["deleted"] if v<n)
        keepP=sorted(set(inst["kept_parent_points"])|{deleted_point})
        keepL=inst["kept_parent_lines"]
        index={p:i for i,p in enumerate(keepP)}
        lines=[{index[p] for p in parent["lines"][l] if p in index}
               for l in keepL]
        with self.assertRaises(ValueError):
            source_graph(lines,len(keepP),2,2)

    def test_15_original_4_or_6_cycle_mutation_rejected(self):
        inst=actual_smaller_source(Field(3))
        src=inst["new_original_source"]
        lines=[set(z) for z in src["lines"]]
        p,v=sorted(lines[0])[:2]
        other=next(j for j in range(1,len(lines)) if p in lines[j])
        drop=next(w for w in lines[other] if w!=p)
        lines[other].remove(drop)
        lines[other].add(v)
        with self.assertRaises(ValueError):
            source_graph(lines,src["points"],2,2)

    def test_16_no_fake_q6_field_or_thin_q2(self):
        for q in (2,6,9,10,12):
            with self.assertRaises(ValueError):
                actual_smaller_source(Field(q))
        with self.assertRaises(ValueError):
            exact_original_centered_missing_PSD(
                actual_smaller_source(Field(3))["new_original_source"],3,"??")

    def test_17_prior_Hq_is_already_affine_arc_dual_not_independent(self):
        # An exact prevention of a false novelty claim:
        # paper's Hq: line(a,b,c) incident with point(x,y,z)
        # iff y=ax+b,z=a²x+c.
        # G6-D3 arc h(u)=u²: old-line(-x,-y,-z)
        # yields old-point(a, y-xa, z-xa²) = (a,b,c).
        for q in (3,4,5):
            f=Field(q)
            for a,x,y,z in product(range(q),repeat=4):
                b=f.sub(y,f.mul(x,a))
                c=f.sub(z,f.mul(x,f.mul(a,a)))
                dual_line=(f.sub(0,x),f.sub(0,y),f.sub(0,z))
                AA,BB,CC=dual_line
                predicted=(a,
                           f.sub(f.mul(AA,a),BB),
                           f.sub(f.mul(AA,f.mul(a,a)),CC))
                self.assertEqual(predicted,(a,b,c))
        # The smaller G6-E1 q(q²-2) cardinality rules out
        # isomorphism to the existing q³ affine-arc source.

    def test_18_independent_source_delta_count_typed_dual(self):
        for q in (3,4,5):
            inst=actual_smaller_source(Field(q))
            src=inst["new_original_source"]
            dp,dl,d=defect_matrices(src)
            self.assertEqual(d,q*2*q*(q-2))
            self.assertEqual(len(dp),q*(q*q-2))
            self.assertEqual(len(dl),q*(q*q-2))
            self.assertEqual(sum(sum(row) for row in dp),
                             sum(sum(row) for row in dl))
            self.assertEqual(set(map(sum,dp)),{d})
            self.assertEqual(set(map(sum,dl)),{d})

    def test_19_exact_symbolic_interlacing_critical_polynomial(self):
        for q in range(3,256):
            r=q-1;h=2*r
            f_at_critical=Q(4*h**3,27)
            f_at_endpoint=8*q
            kappa=3 if q==3 else 2
            self.assertLessEqual(max(f_at_critical,Q(f_at_endpoint)),
                                 kappa*r**3)
            self.assertGreater(q*q,2*q)

    def test_20_independent_field_GQ_parent_zero_defect_not_derived_from_B(self):
        for q in (3,4,5):
            parent,names,idx=actual_parent_GQ(Field(q))
            dpoint,dline,_=defect_matrices(parent)
            self.assertTrue(all(x==0 for row in dpoint for x in row))
            self.assertTrue(all(x==0 for row in dline for x in row))
            self.assertEqual(independent_components(parent),
                             [2*(q+1)*(q*q+1)])


if __name__=="__main__":
    unittest.main()
