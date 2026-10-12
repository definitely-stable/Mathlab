"""Independent C4-weighted mixed-codegree K3-E falsifiers."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb
import random
import unittest

from hyp105_g5e2b3e1k1_kikuchi_c6 import gq_pair_model, kikuchi_graph
from hyp105_g5e2b3e1k3_local_collisions import star_degree_tensor
from hyp105_g5e2b3e1k3d_mixed_girth8 import global_mixed_book_certificate
from hyp105_g5e2b3e1k3e_weighted_codegrees import mixed_weighted_profile
from test_hyp105_g5e2b3e1k3c_book_packing import independently_enumerated_c4


def direct_cycle_diagonal_weights(graph,a):
    """Independent oriented-C4 walk oracle, then its two OPPOSITE pairs.

    Unlike the reference, no codegree intersection loops are used to
    construct the histogram. The counter of each diagonal pair is
    accumulated once per square edge set.
    """
    diagonal=Counter()
    for cyc in independently_enumerated_c4(graph):
        vertices=sorted(set().union(*cyc))
        for u,v in combinations(vertices,2):
            if frozenset((u,v)) in cyc:
                continue
            if u//a==v//a or u%a==v%a:
                continue
            diagonal[(u,v)]+=1
    return diagonal


class WeightedCodegreeTests(unittest.TestCase):
    def test_independent_four_cycle_weighted_histograms(self):
        specs=((1,"lex",None),(1,"reverse-line",None),
               (1,"random",230),(2,"random",20261011))
        for h,scheme,seed in specs:
            model=gq_pair_model(h,scheme,seed)
            g=kikuchi_graph(model)
            p=mixed_weighted_profile(model)
            opposite=direct_cycle_diagonal_weights(g,model["a"])
            hist=Counter()
            for (u,v),w in opposite.items():
                c=len(g[u]&g[v])
                self.assertEqual(w,c*(c-1)//2)
                hist[c]+=w
            expected={str(c):w for c,w in sorted(hist.items())}
            self.assertEqual(p["mixed_C4_weight_by_codegree"],expected)
            self.assertEqual(sum(opposite.values()),p["mixed_M2"])
            self.assertEqual(2*p["C4"],
                             p["mixed_M2"]+p["source_aligned_M2"])
            self.assertEqual(star_degree_tensor(model),tuple(map(len,g)))

    def test_independent_books_from_three_common_neighbors(self):
        for h,scheme,seed in ((1,"lex",None),(1,"random",37),
                              (2,"random",20261011)):
            model=gq_pair_model(h,scheme,seed)
            g=kikuchi_graph(model)
            a=model["a"]
            actual=0
            M2=0
            for u in range(len(g)):
                for v in range(u+1,len(g)):
                    if u//a==v//a or u%a==v%a:
                        continue
                    witnesses=list(g[u]&g[v])
                    M2+=len(list(combinations(witnesses,2)))
                    actual+=3*len(list(combinations(witnesses,3)))
            p=mixed_weighted_profile(model)
            self.assertEqual(actual,p["B_mixed"])
            self.assertEqual(M2,p["mixed_M2"])
            self.assertEqual(Fraction(actual,M2)+2,
                             Fraction(p["kappa_mixed_exact"]))
            self.assertEqual(sum(p["C4_weighted_tail"].values()),actual)
            self.assertEqual(sum(p["source_star_upper_tail"].values()),
                             p["B_upper_source_star"])

    def test_girth8_star_cap_is_sound_and_not_declared_as_theorem_A(self):
        models=((1,"lex",None),(1,"reverse-line",None),
                (2,"lex",None),(2,"random",20261011),(2,"random",230))
        for h,scheme,seed in models:
            model=gq_pair_model(h,scheme,seed)
            p=mixed_weighted_profile(model)
            prior=global_mixed_book_certificate(model)
            self.assertEqual(p["B_mixed"],prior["B_mixed"])
            self.assertEqual(p["mixed_M2"],prior["mixed_M2"])
            self.assertEqual(p["Cmax_girth8"],prior["universal_mixed_codegree_cap"])
            self.assertEqual(p["B_upper_global_girth8"],
                             prior["B_mixed_upper_via_second_moment"])
            self.assertLessEqual(p["B_mixed"],p["B_upper_source_star"])
            self.assertLessEqual(p["B_upper_source_star"],
                                 p["B_upper_global_girth8"])
            self.assertFalse(p["source_star_upper_is_uniform_o_s6"])
            self.assertFalse(p["branch_A_or_B_proved"])

    def test_exact_layer_cake_and_source_degree_tail(self):
        for h,scheme,seed in ((1,"lex",None),(2,"random",230)):
            model=gq_pair_model(h,scheme,seed)
            g=kikuchi_graph(model)
            p=mixed_weighted_profile(model)
            hist=p["mixed_codegree_pair_histogram"]
            cap=p["Cmax_girth8"]
            for k in range(3,cap+1):
                direct=sum(comb(int(c),2)*number for c,number in hist.items()
                           if int(c)>=k)
                self.assertEqual(direct,p["C4_weighted_tail"].get(str(k),0))
                self.assertLessEqual(direct,
                                     p["source_star_upper_tail"].get(str(k),0))
            self.assertEqual(Fraction(p["kappa_excess_exact"]),
                             Fraction(p["B_mixed"],p["mixed_M2"]))

    def test_fail_closed_budgets(self):
        model=gq_pair_model(1,"lex")
        with self.assertRaises(RuntimeError):
            mixed_weighted_profile(model,max_pairs=3)
        with self.assertRaises(RuntimeError):
            mixed_weighted_profile(model,max_c4=0)
        for kw in (dict(max_pairs=-2),dict(max_c4=-2),
                   dict(max_pairs=True),dict(max_c4=3.2)):
            with self.assertRaises(ValueError):
                mixed_weighted_profile(model,**kw)


if __name__=="__main__":
    unittest.main()
