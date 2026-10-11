"""Independent HYP-105 K3-D girth-eight GQ incidence and cubic-book tests."""
from collections import Counter
from itertools import combinations
from math import comb
import random
import unittest

from hyp105_g5e2b3e1k1_kikuchi_c6 import gq_pair_model, kikuchi_graph
from hyp105_g5e2b3e1k3_local_collisions import star_codegree_tensor
from hyp105_g5e2b3e1k3c_book_packing import book_moments
from hyp105_g5e2b3e1k3d_mixed_girth8 import (
    c4_free_edge_cap, girth8_moore_edge_cap, global_mixed_book_certificate,
    mixed_compatibility, source_inverses,
)


def brute_double_incidence(model, u, v):
    """Original incidence rows reconstructed WITHOUT inverse-pair dictionaries.

    Costly oracle: scan the ORIGINAL ordered incidences directly for each
    candidate z,t. No call to the production Kikuchi adjacency constructor.
    """
    a = model["a"]
    x,y=divmod(u,a)
    xx,yy=divmod(v,a)
    inc=set(model["incidences"])
    rows={}
    for z in range(a):
        if z==x or z==xx:
            continue
        zs=set()
        for t in range(a):
            if t==y or t==yy:
                continue
            original_p=[p for p,phys in enumerate(model["left_labels"])
                        if set(phys)=={x,z}]
            original_pp=[p for p,phys in enumerate(model["left_labels"])
                         if set(phys)=={xx,z}]
            original_l=[l for l,phys in enumerate(model["right_labels"])
                        if set(phys)=={y,t}]
            original_ll=[l for l,phys in enumerate(model["right_labels"])
                         if set(phys)=={yy,t}]
            if (len(original_p)==1 and len(original_pp)==1
                    and len(original_l)==1 and len(original_ll)==1
                    and (original_p[0],original_l[0]) in inc
                    and (original_pp[0],original_ll[0]) in inc):
                zs.add(t)
        rows[z]=frozenset(zs)
    return rows


def independent_no_short_even_cycles(rows):
    """Exhaustively enumerate 4- and 6-cycles in a bipartite source graph."""
    left=sorted(rows)
    right=sorted(set().union(*rows.values()))
    adj={("L",z):set() for z in left}
    adj.update({("R",t):set() for t in right})
    for z,ts in rows.items():
        for t in ts:
            adj[("L",z)].add(("R",t))
            adj[("R",t)].add(("L",z))
    for target_len in (4,6):
        for start in adj:
            def walk(path):
                if len(path)==target_len:
                    return start in adj[path[-1]]
                return any(w not in path and walk(path+[w])
                           for w in adj[path[-1]])
            if walk([start]):
                return False
    return True


def brute_three_path_endpoints(rows):
    left=tuple(rows)
    right=set().union(*rows.values())
    reverse={t:set() for t in right}
    for z,ts in rows.items():
        for t in ts:
            reverse[t].add(z)
    by_end=Counter()
    for z0 in left:
        for t1 in rows[z0]:
            for z2 in reverse[t1]:
                if z2==z0:
                    continue
                for t3 in rows[z2]:
                    if t3==t1:
                        continue
                    by_end[(z0,t3)]+=1
                    if t3 in rows[z0]:
                        raise AssertionError("short four-cycle induced by length-3 path")
    return by_end


class MixedGirthTests(unittest.TestCase):
    def test_exact_integer_c4_free_capacity(self):
        for r in range(1,75):
            bound=c4_free_edge_cap(r)
            self.assertLessEqual(bound*(bound-r),r*r*(r-1))
            self.assertGreater((bound+1)*(bound+1-r),r*r*(r-1))
        for bad in (0,-3,2.5,True):
            with self.assertRaises(ValueError):
                c4_free_edge_cap(bad)

    def test_girth8_moore_integer_cap_regimes(self):
        for r in range(1,101):
            bound=girth8_moore_edge_cap(r)
            self.assertLessEqual(bound,r*r)
            self.assertGreaterEqual(bound,min(3*r-1,r*r))
            if bound>=3*r:
                self.assertLessEqual(bound*((bound-r)**2+r*r),r**4)
            if bound+1<=r*r and bound+1>=3*r:
                self.assertGreater((bound+1)*((bound+1-r)**2+r*r),r**4)
        self.assertEqual(c4_free_edge_cap(12),46)
        self.assertEqual(girth8_moore_edge_cap(12),35)
        self.assertLess(girth8_moore_edge_cap(33),c4_free_edge_cap(33))
        for invalid in (-2,0,True,3.0):
            with self.assertRaises(ValueError):
                girth8_moore_edge_cap(invalid)

    def test_true_w32_compatibility_exhaustive_and_girth(self):
        for scheme in ("lex","reverse-line"):
            model=gq_pair_model(1,scheme)
            graph=kikuchi_graph(model)
            a=model["a"]
            for u in range(a*a):
                for v in range(u+1,a*a):
                    if u//a==v//a or u%a==v%a:
                        continue
                    witness=mixed_compatibility(model,u,v)
                    oracle=brute_double_incidence(model,u,v)
                    self.assertEqual(witness["rows"],oracle)
                    self.assertEqual(witness["m"],len(graph[u]&graph[v]))
                    self.assertEqual(witness["m"],star_codegree_tensor(model,u,v))
                    self.assertTrue(independent_no_short_even_cycles(oracle))
                    per_end=brute_three_path_endpoints(oracle)
                    self.assertLessEqual(max(per_end.values(),default=0),1)
                    self.assertEqual(sum(per_end.values()),
                                     witness["path3_left_to_right"])

    def test_true_s4_seeded_larger_witnesses(self):
        model=gq_pair_model(2,"random",20261011)
        graph=kikuchi_graph(model)
        a=model["a"]
        rng=random.Random(230368)
        pairs=[(u,v) for u in range(a*a)
                    for v in range(u+1,a*a)
                    if u//a!=v//a and u%a!=v%a
                    and len(graph[u]&graph[v])>=3]
        samples=list(pairs)
        samples.extend(tuple(sorted(rng.sample(range(a*a),2)))
                       for _ in range(15))
        tested=0
        for u,v in samples:
            if u//a==v//a or u%a==v%a:
                continue
            result=mixed_compatibility(model,u,v)
            oracle=brute_double_incidence(model,u,v)
            self.assertEqual(result["rows"],oracle)
            self.assertEqual(result["m"],len(graph[u]&graph[v]))
            self.assertTrue(independent_no_short_even_cycles(oracle))
            endpoints=brute_three_path_endpoints(oracle)
            self.assertTrue(all(v==1 for v in endpoints.values()))
            self.assertEqual(sum(endpoints.values()),
                             result["path3_left_to_right"])
            tested+=1
        self.assertGreater(tested,15)

    def test_aggregate_moments_and_old_k3c_books(self):
        expectations={("lex",None,1):(90,9),
                      ("reverse-line",None,1):(21,3),
                      ("random",20261011,2):(333,54)}
        for (scheme,seed,power),(mixed_book,aligned_book) in expectations.items():
            model=gq_pair_model(power,scheme,seed)
            result=global_mixed_book_certificate(model)
            self.assertEqual(result["B_mixed"],mixed_book)
            self.assertEqual(result["B_aligned"],aligned_book)
            self.assertEqual(result["B_total"],mixed_book+aligned_book)
            self.assertEqual(result["mixed_M1"]+result["aligned_M1"],
                             result["total_codegree_M1_from_original_stars"])
            self.assertGreaterEqual(result["B_mixed_upper_via_first_moment"],
                                    result["B_mixed"])
            self.assertLessEqual(result["universal_mixed_codegree_cap"],
                                 result["C4_free_cap"])
            self.assertGreaterEqual(result["book_witnesses_checked_against_original_GQ"],1)
            books=book_moments(kikuchi_graph(model),model["a"])
            self.assertEqual(books["book_mixed"],mixed_book)

    def test_all_h_bound_is_not_claimed_and_budget_is_fail_closed(self):
        model=gq_pair_model(1,"lex")
        r=global_mixed_book_certificate(model)
        self.assertFalse(r["uniform_o_s6_proved"])
        self.assertFalse(r["branch_A_or_B_proved"])
        with self.assertRaises(RuntimeError):
            global_mixed_book_certificate(model,max_pairs=3)
        with self.assertRaises(RuntimeError):
            global_mixed_book_certificate(model,max_book_witnesses=0)
        with self.assertRaises(ValueError):
            mixed_compatibility(model,0,0)
        with self.assertRaises(ValueError):
            mixed_compatibility(model,0,1)
        with self.assertRaises(ValueError):
            mixed_compatibility(model,0,True)
        with self.assertRaises(ValueError):
            source_inverses(dict(model,left_labels=((0,1),(0,1))))
        with self.assertRaises(ValueError):
            global_mixed_book_certificate(model,max_book_witnesses=-1)


if __name__=="__main__":
    unittest.main()
