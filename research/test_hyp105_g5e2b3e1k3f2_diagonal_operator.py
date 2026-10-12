"""Independent K3-F2 C4 diagonal operator and chord-to-motif falsifiers."""
from collections import Counter, defaultdict
from itertools import combinations
from math import comb, isqrt
import random
import unittest

from hyp105_g5e2b3e1k1_kikuchi_c6 import (
    gq_pair_model, kikuchi_graph, six_cycle_census,
)
from hyp105_g5e2b3e1k3c_book_packing import classify_c4_pair_overlaps
from hyp105_g5e2b3e1k3e_weighted_codegrees import mixed_weighted_profile
from hyp105_g5e2b3e1k3f2_diagonal_operator import (
    chorded_motif_extraction, mixed_pair, operator_tail_certificate,
    original_column_lut, weighted_cut_profile, weighted_diagonal_operator,
)
from test_hyp105_g5e2b3e1k3c_book_packing import independently_enumerated_c4


def independent_c4_diagonals(graph, a):
    """Construct W from exact C4 EDGE sets, not from graph codegrees."""
    diag=Counter()
    for sq in independently_enumerated_c4(graph):
        corners=sorted(set().union(*sq))
        for u,v in combinations(corners,2):
            if frozenset((u,v)) not in sq and mixed_pair(u,v,a):
                diag[(u,v)]+=1
    return diag


def independent_chorded_six_census(graph, model):
    """Quadratic C4-pair oracle without K3-C edge grouping."""
    sq=list(independently_enumerated_c4(graph))
    column={}
    a=model["a"]
    for i,(p,l) in enumerate(model["incidences"]):
        px,py=model["left_labels"][p]
        lx,ly=model["right_labels"][l]
        column[frozenset((px*a+lx,py*a+ly))]=i
        column[frozenset((px*a+ly,py*a+lx))]=i
    result=Counter()
    per_c6=Counter()
    for i,j in combinations(range(len(sq)),2):
        a1,a2=sq[i],sq[j]
        if len(a1&a2)!=1:
            continue
        common_vertices=set().union(*a1)&set().union(*a2)
        if len(common_vertices)!=2:
            continue
        six=a1^a2
        pts=set().union(*six)
        if len(six)!=6 or len(pts)!=6:
            raise AssertionError("independent H oracle malformed")
        cols=[column[e] for e in six]
        proper=(len({v//a for v in pts})==6
                and len({v%a for v in pts})==6)
        if proper:
            typ="proper"
        elif len(set(cols))==6:
            typ="distinct_improper"
        else:
            typ="repeated"
        result[typ]+=1
        per_c6[frozenset(six)]+=1
    return result,per_c6


class MixedDiagonalOperatorTests(unittest.TestCase):
    def test_opposite_diagonal_four_cycle_oracle_and_strength_wedge(self):
        for h,scheme,seed in ((1,"lex",None),
                              (1,"reverse-line",None),
                              (2,"random",20261011)):
            m=gq_pair_model(h,scheme,seed)
            graph=kikuchi_graph(m)
            w=weighted_diagonal_operator(m)
            diag=independent_c4_diagonals(graph,m["a"])
            self.assertEqual(sum(diag.values()),w["M2mixed"])
            self.assertEqual(sum(v*v for v in diag.values()),w["E2mixed"])
            for u in range(len(graph)):
                exact=Counter()
                for (x,y),count in diag.items():
                    if x==u:
                        exact[y]+=count
                    elif y==u:
                        exact[x]+=count
                self.assertEqual(dict(exact),w["rows"][u])
                self.assertEqual(sum(exact.values()),w["strength"][u])
                # Independent second oracle: each pair of neighbors b,c
                # of u generates one square for EACH OTHER common
                # neighbor v, with mixed-coordinate selection.
                wedge=0
                for b,c in combinations(graph[u],2):
                    for v in (graph[b]&graph[c])-{u}:
                        if mixed_pair(u,v,m["a"]):
                            wedge+=1
                self.assertEqual(wedge,w["strength"][u])

    def test_quadratic_form_cut_and_integer_frobenius(self):
        rng=random.Random(230372)
        for h,scheme,seed in ((1,"lex",None),
                              (2,"random",20261011)):
            model=gq_pair_model(h,scheme,seed)
            w=weighted_diagonal_operator(model)
            n=len(w["graph"])
            trial=[
                frozenset(),frozenset(range(n)),
                frozenset(u for u in range(n) if w["degree"][u]>=4)
            ]
            for _ in range(8):
                trial.append(frozenset(u for u in range(n)
                                       if rng.randrange(3)==0))
            independent=independent_c4_diagonals(w["graph"],model["a"])
            for selected in trial:
                r=weighted_cut_profile(w,selected)
                brute=sum(value for (u,v),value in independent.items()
                          if u in selected and v in selected)
                boundary=sum(value for (u,v),value in independent.items()
                             if (u in selected)!=(v in selected))
                self.assertEqual(r["Q_exact"],brute)
                self.assertEqual(r["weighted_boundary"],boundary)
                self.assertEqual(r["row_strength_sum"],2*brute+boundary)
                self.assertLessEqual(brute,r["operator_upper"])
                self.assertGreaterEqual(
                    r["Frobenius_integer_upper"]**2,
                    0,
                )
                self.assertGreaterEqual(
                    (r["Frobenius_integer_upper"]+1)**2,
                    len(selected)*(len(selected)-1)//2*w["E2mixed"]
                )

    def test_layered_operator_is_valid_but_not_new_universal_proof(self):
        for h,scheme,seed in ((1,"lex",None),
                              (1,"reverse-line",None),
                              (2,"lex",None),
                              (2,"random",20261011)):
            model=gq_pair_model(h,scheme,seed)
            r=operator_tail_certificate(model)
            k3e=mixed_weighted_profile(model)
            self.assertEqual(r["B_upper_K3E_exact_source_star"],
                             k3e["B_upper_source_star"])
            self.assertEqual(r["B_mixed"],k3e["B_mixed"])
            self.assertGreaterEqual(r["B_upper_F2_operator"],
                                    r["B_upper_K3E_exact_source_star"])
            self.assertFalse(r["all_h_Omega_s6_proved"])

    def test_independent_chord_extraction_and_accepted_proper_census(self):
        for h,scheme,seed in ((1,"lex",None),
                              (1,"reverse-line",None),
                              (2,"random",20261011)):
            model=gq_pair_model(h,scheme,seed)
            g=kikuchi_graph(model)
            r=chorded_motif_extraction(model)
            k3c=classify_c4_pair_overlaps(g,model=model)
            counts,multi=independent_chorded_six_census(g,model)
            self.assertEqual(r["H_proper"],counts["proper"])
            self.assertEqual(r["H_distinct_improper"],counts["distinct_improper"])
            self.assertEqual(r["H_repeated_original_columns"],counts["repeated"])
            self.assertEqual(r["H_chorded_total"],sum(counts.values()))
            self.assertEqual(r["H_chorded_total"],k3c["H_single_edge_only"])
            self.assertEqual(r["H_proper"],k3c["H_proper"])
            self.assertEqual(r["distinct_column_H_total"],
                             k3c["H_distinct_columns"])
            self.assertLessEqual(max(multi.values(),default=0),3)
            census=six_cycle_census(g,model["a"])
            self.assertLessEqual(r["D6_floor_by_chord_multiplicity"],
                                 census["proper_D6"])
            self.assertLessEqual(r["unique_chorded_proper_C6"],
                                 census["proper_D6"])
            self.assertFalse(r["branch_A_or_B_proved"])
            self.assertTrue(r["full_R3_is_not_seven_family_S"])

    def test_fail_closed_and_invalid_models(self):
        model=gq_pair_model(1,"lex")
        with self.assertRaises(RuntimeError):
            weighted_diagonal_operator(model,max_pairs=2)
        with self.assertRaises(RuntimeError):
            weighted_diagonal_operator(model,max_c4=0)
        with self.assertRaises(ValueError):
            weighted_diagonal_operator(model,max_pairs=True)
        with self.assertRaises(ValueError):
            chorded_motif_extraction(model,max_c4=-1)
        with self.assertRaises(RuntimeError):
            chorded_motif_extraction(model,max_incident_pairs=0)
        w=weighted_diagonal_operator(model)
        with self.assertRaises(ValueError):
            weighted_cut_profile(w,[len(w["rows"])])
        with self.assertRaises(ValueError):
            weighted_cut_profile(w,[True])
        with self.assertRaises(RuntimeError):
            weighted_cut_profile(w,range(len(w["rows"])),max_selected=0)
        self.assertEqual(weighted_cut_profile(w,[])["Q_exact"],0)


if __name__=="__main__":
    unittest.main()
