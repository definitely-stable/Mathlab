"""Independent C4 holes inclusion-exclusion and true original GQ P3 referees."""
from itertools import combinations
from math import comb
from random import Random
import unittest

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4cq_original_macro_path_cut_gate import _validated_original
from hyp105_issue230_d6aa4cr_exact_BBo_three_matching_transfer import (
    c4_completions_from_single_and_doubled,
    original_nonincident_threepath,
)
from hyp105_issue230_d6aa4cs_uniform_disjoint_original_source_cut import (
    original_disjoint_3path_cut_certificate,
)
from hyp105_issue230_d6aa4ct_dense_physical_c4_reservoir import (
    physical_graph, c4_count_via_holes, dense_side_certificate,
    all_h_dense_c4_arithmetic, original_cut_dense_c4_certificate,
)


def independent_c4_path_count(e, d, edges, a):
    """Independently enumerate FOUR vertex cycles as physical edges."""
    u, v = sorted(e)
    free = sorted(set(range(a)) - set(e) - set(d))
    count = 0
    for z in free:
        for w in free:
            if z == w:
                continue
            if all(frozenset(edge) in edges for edge in ((u, z), (z, w), (w, v))):
                count += 1
    return count


class AA4CTDenseOriginalC4Reservoir(unittest.TestCase):
    def test_01_adversarial_star_holes_disprove_each_anchor_positive(self):
        for a in (16, 24, 32):
            # Exactly a-2 holes, all around u=0, while e=(0,1)
            # remains occupied. The original physical left C4 count
            # is ZERO although the entire graph is K_a minus <a edges.
            holes = {frozenset((0,j)) for j in range(2,a)}
            labels = [(u,v) for u in range(a) for v in range(u+1,a)
                      if frozenset((u,v)) not in holes]
            edges, missing, degrees = physical_graph(labels,a)
            self.assertEqual(missing,holes)
            self.assertEqual(len(missing),a-2)
            self.assertEqual(2*sum(degrees),4*len(holes))
            self.assertEqual(independent_c4_path_count((0,1),(2,3),edges,a),0)
            z=dense_side_certificate((0,1),(2,3),edges,missing,degrees,a)
            self.assertEqual(z["occupied_C4_source_triples"],0)
            self.assertFalse(z["single_endpoint_no_heavy"])
            self.assertTrue(z["full_C4_templates"]>0)

    def test_02_adversarial_holes_formula_vs_independent_cycle_walker(self):
        random=Random(230619)
        for a in (16,17,24,35):
            universe=[(u,v) for u in range(a) for v in range(u+1,a)]
            for H in (0,1,a//2,a-2):
                for trial in range(5):
                    missing=set(random.sample(universe,H))
                    labels=[uv for uv in universe if uv not in missing]
                    edges,holes,degrees=physical_graph(labels,a)
                    heavy={v for v in range(a) if 16*degrees[v]>=a}
                    self.assertLessEqual(len(heavy),31)
                    self.assertLessEqual(sum(degrees),2*(a-2))
                    samples=0
                    for e in universe:
                        if frozenset(e) not in edges:
                            continue
                        for d in universe:
                            if len(set(e+d))!=4 or frozenset(d) not in edges:
                                continue
                            z=dense_side_certificate(e,d,edges,holes,degrees,a)
                            direct=independent_c4_path_count(e,d,edges,a)
                            self.assertEqual(z["occupied_C4_source_triples"],direct)
                            if not (set(e)&heavy):
                                self.assertGreaterEqual(2*direct,(a-4)*(a-5))
                            samples+=1
                            if samples>=7:
                                break
                        if samples>=7:
                            break
                    self.assertEqual(samples,7)

    def test_03_true_original_W32_W34_W38_C4_triples_are_real_complete_maps(self):
        for power,schemes in ((1,("lex","S72")),
                              (2,("lex","random")),
                              (3,("lex","random"))):
            for scheme in schemes:
                model=fixture(power,scheme)
                s,V,a,f,g,pl,lp=_validated_original(model)
                point_graph=physical_graph(f,a)
                line_graph=physical_graph(g,a)
                p_inverse={tuple(sorted(e)):i for i,e in enumerate(f)}
                l_inverse={tuple(sorted(e)):i for i,e in enumerate(g)}
                checked=0
                for p in range(min(V,12)):
                    for l in range(V):
                        if l in pl[p]:
                            continue
                        Q=original_nonincident_threepath(p,l,pl,lp)
                        q,l0=Q[1][0],Q[0][1]
                        if set(f[p])&set(f[q]) or set(g[l])&set(g[l0]):
                            continue
                        for single,double,graph,inverse in (
                            (f[p],f[q],point_graph,p_inverse),
                            (g[l],g[l0],line_graph,l_inverse)):
                            cert=dense_side_certificate(single,double,*graph,a)
                            old=c4_completions_from_single_and_doubled(
                                single,double,inverse,a)
                            self.assertEqual(cert["occupied_C4_source_triples"],len(old))
                            self.assertEqual(cert["occupied_C4_source_triples"],
                                independent_c4_path_count(single,double,graph[0],a))
                        checked+=1
                        if checked>=8:
                            break
                    if checked>=8:
                        break
                self.assertEqual(checked,8)
                print("AA4CT_REAL_ORIGINAL_C4",s,scheme,"a",a,
                      "point_holes",len(point_graph[1]),"line_holes",
                      len(line_graph[1]),"genuine_paths_checked",checked,
                      flush=True)

    def test_04_exact_large_h_minimal_physical_alphabet_certificate(self):
        for h in range(1,27):
            z=all_h_dense_c4_arithmetic(h)
            a,V,m=z["a"],z["V"],z["m"]
            self.assertLess(comb(a-1,2),V)
            self.assertGreaterEqual(comb(a,2),V)
            if h>=14:
                B=32*(a-1)
                self.assertGreaterEqual(m,8*B)
                self.assertGreaterEqual(8*m,V)
                self.assertGreaterEqual(256*m*m,V*V)
                self.assertGreaterEqual((a-4)*(a-5),8*(a-2))
            print("AA4CT_ALLH_NUMERIC_FALSIFIER",h,"a",a,
                  "m",m,"B",z["max_heavy_occupied_endpoint_edges_per_typed_map"],
                  flush=True)

    def test_05_true_original_3path_cut_nonheavy_source_fiber_census(self):
        for power,scheme in ((1,"lex"),(1,"S72"),(2,"lex"),(2,"random"),
                             (3,"lex"),(3,"random")):
            model=fixture(power,scheme)
            a=_validated_original(model)[2]
            k=a//2
            cuts=((tuple(range(k)),tuple(range(a-k,a))),
                  (tuple(range(a-k,a)),tuple(range(k))))
            for X,Y in cuts:
                old=original_disjoint_3path_cut_certificate(model,X,Y)
                z=original_cut_dense_c4_certificate(model,X,Y,sample_limit=5)
                self.assertEqual(z["true_original_P3_cut"],
                                 old["actual_original_nonincident_source_3paths_T"])
                self.assertEqual(z["double_disjoint_P3"],
                                 old["both_physically_disjoint_source_3paths"])
                self.assertLessEqual(z["double_disjoint_nonheavy_P3"],
                                     z["double_disjoint_P3"])
                self.assertLessEqual(z["point_heavy_vertices"],31)
                self.assertLessEqual(z["line_heavy_vertices"],31)
                for original, left, right in z["C4_samples_original_p_l_q_l0_left_right"]:
                    self.assertEqual(len(original),4)
                    self.assertTrue(left["single_endpoint_no_heavy"])
                    self.assertTrue(right["single_endpoint_no_heavy"])
                    if a>=16:
                        self.assertGreaterEqual(
                            2*left["occupied_C4_source_triples"],
                            left["full_C4_templates"])
                        self.assertGreaterEqual(
                            2*right["occupied_C4_source_triples"],
                            right["full_C4_templates"])
                print("AA4CT_REAL_ORIGINAL_NONHEAVY_CUT",
                      power,scheme,"a",a,"P3",z["true_original_P3_cut"],
                      "both_disjoint",z["double_disjoint_P3"],
                      "nonheavy",z["double_disjoint_nonheavy_P3"],
                      flush=True)

    def test_06_invalid_graph_source_mapping_and_cut_fail_closed(self):
        with self.assertRaises(ValueError):
            physical_graph(((0,1),(1,0)),16)
        with self.assertRaises(ValueError):
            physical_graph(((0,0),),16)
        with self.assertRaises(ValueError):
            physical_graph(((0,True),),16)
        with self.assertRaises(ValueError):
            all_h_dense_c4_arithmetic(0)
        model=fixture(1,"lex")
        with self.assertRaises(ValueError):
            original_cut_dense_c4_certificate(model,X=(0,0,1))
        with self.assertRaises(ValueError):
            original_cut_dense_c4_certificate(model,sample_limit=-1)
        fake=dict(model)
        ll=list(model["left_labels"])
        ll[1]=ll[0]
        fake["left_labels"]=tuple(ll)
        with self.assertRaises(ValueError):
            original_cut_dense_c4_certificate(fake)


if __name__=="__main__":
    unittest.main()
