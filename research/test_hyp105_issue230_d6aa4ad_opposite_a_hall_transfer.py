"""Independent all-h physical 2factor/Hall and true original W32/W34 tests."""
import random
import unittest
from collections import Counter
from itertools import combinations,product

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ad_opposite_a_hall_transfer import (
    six_vertex_two_factors,pinned_twofactor_completions,
    _four_permanent_and_hall,opposite_physical_A_Hall_transfer,
    independent_W32_original_second_gate_census,
    analytic_physical_gate_counts,_W32_true_physical_C4_sources,
)


def _direct_original_assignment(model,side,pinned,q):
    """Independent actual-original four-line/point injection enumeration.
    Never constructs 2factors or calls the analytical Hall permanent.
    """
    flags=tuple(tuple(x) for x in model["incidences"])
    labels=tuple(model["right_labels" if side==0 else "left_labels"])
    v=len(model["left_labels"])
    neighbors=[set() for _ in range(v)]
    for p,l in flags:
        neighbors[(p,l)[side]].add((p,l)[1-side])
    frozen={flags[j][1-side] for j in pinned}
    Ai=[neighbors[x]-frozen for x in q]
    total=forest=0
    for assignments in product(*Ai):
        if len(set(assignments))<4:continue
        forest+=1
        all_six=tuple(frozen)+assignments
        degree=Counter(c for x in all_six for c in labels[x])
        if len(degree)==6 and set(degree.values())=={2}:
            total+=1
    return total,forest


class GenuineOriginalOppositePhysicalAHallTests(unittest.TestCase):
    def test_01_independent_six_coordinate_2factor_shapes(self):
        factors=six_vertex_two_factors()
        self.assertEqual(len(factors),70)
        seen=set()
        cycles=triangles=0
        for H in factors:
            self.assertEqual(len(H),6)
            degree=Counter(x for e in H for x in e)
            self.assertEqual(degree,{i:2 for i in range(6)})
            edges=frozenset(H)
            self.assertNotIn(edges,seen)
            seen.add(edges)
            stack=[0];visited=set()
            graph={i:set() for i in range(6)}
            for u,v in H:
                graph[u].add(v);graph[v].add(u)
            while stack:
                x=stack.pop()
                if x in visited:continue
                visited.add(x);stack.extend(graph[x]-visited)
            if len(visited)==6:cycles+=1
            else:triangles+=1
        self.assertEqual((cycles,triangles),(60,10))

    def test_02_all_ordered_K6_K7_K8_two_pinned_physical_pairs(self):
        for a in (6,7,8):
            all_pairs=list(combinations(range(a),2))
            for i,e0 in enumerate(all_pairs):
                for e1 in all_pairs[i+1:]:
                    H=pinned_twofactor_completions(e0,e1,a)
                    expected=(7*__import__("math").comb(a-3,3)
                              if len(set(e0)&set(e1)) else
                              14*__import__("math").comb(a-4,2))
                    self.assertEqual(len(H),expected)
                    self.assertEqual(len(set(H)),expected)
                    for h in H:
                        self.assertIn(e0,h);self.assertIn(e1,h)
                        degree=Counter(c for e in h for c in e)
                        self.assertEqual(len(degree),6)
                        self.assertEqual(set(degree.values()),{2})

    def test_03_Hall_and_permanent_all_four_source_row_patterns(self):
        self.assertEqual(_four_permanent_and_hall(({0,1,2,3},)*4),
                         (24,None))
        p,b=_four_permanent_and_hall(({0},{0},{2},{3}))
        self.assertEqual(p,0);self.assertIsNotNone(b)
        self.assertEqual(b["Hall_deficit"],1)
        self.assertEqual(_four_permanent_and_hall(({0},{1},{2},{3})),
                         (1,None))
        rng=random.Random(230507)
        for _ in range(300):
            rows=tuple(frozenset(j for j in range(4)
                                 if rng.randrange(3)==0)
                       for _ in range(4))
            p,w=_four_permanent_and_hall(rows)
            brute=sum(all(perm[i] in rows[i] for i in range(4))
                      for perm in __import__("itertools").permutations(range(4)))
            self.assertEqual(p,brute)
            self.assertEqual(w is None,brute>0)

    def test_04_TRUE_W32_S68_complete_270_physical_B_cohorts(self):
        z=independent_W32_original_second_gate_census("S68")
        self.assertEqual(z["full_original_GF5_S"],68)
        a=z["per_B_A_historical_GF5_tag"]
        self.assertEqual(a["B-left/A-right"]["accepted_actual_original_GF5_BA"],44)
        self.assertEqual(a["A-left/B-right"]["accepted_actual_original_GF5_BA"],21)
        self.assertEqual((a["B-left/A-right"]["source_only_distinct_original_flag_forests"],
                          a["A-left/B-right"]["source_only_distinct_original_flag_forests"]),
                         (6098,4740))
        for row in a.values():
            self.assertEqual(row["actual_original_B_root_two_flag_C4_cohorts"],135)
            self.assertEqual(row["independent_original_direct_four_choice_confirmations"],135)
            self.assertGreater(row["zero_accepted_cohorts"],0)
            self.assertEqual(row["zero_accepted_cohorts"],
                             row["Hall_zero_accepted_cohorts"])
            self.assertGreaterEqual(row["actual_two_factor_completions_passing_original_Hall"],1)

    def test_05_TRUE_W32_S72_complete_270_physical_B_cohorts(self):
        z=independent_W32_original_second_gate_census("S72")
        a=z["per_B_A_historical_GF5_tag"]
        self.assertEqual(z["full_original_GF5_S"],72)
        self.assertEqual((a["B-left/A-right"]["accepted_actual_original_GF5_BA"],
                          a["A-left/B-right"]["accepted_actual_original_GF5_BA"]),
                         (36,31))
        self.assertEqual((a["B-left/A-right"]["source_only_distinct_original_flag_forests"],
                          a["A-left/B-right"]["source_only_distinct_original_flag_forests"]),
                         (6098,4864))
        self.assertTrue(all(x["all_actual_original_Q_and_full_global_label_constraints_checked"]
                            for x in a.values()))

    def test_06_TRUE_W32_lex_reverse_independent_original_counts(self):
        for scheme,forests,accepted in (
            ("lex",(5000,5793),(98,110)),
            ("reverse",(5000,4428),(77,74))
        ):
            z=independent_W32_original_second_gate_census(scheme)
            x=z["per_B_A_historical_GF5_tag"]
            self.assertEqual(tuple(x[k]["source_only_distinct_original_flag_forests"]
                                   for k in ("B-left/A-right","A-left/B-right")),
                             forests)
            self.assertEqual(tuple(x[k]["accepted_actual_original_GF5_BA"]
                                   for k in ("B-left/A-right","A-left/B-right")),
                             accepted)

    def test_07_genuine_original_W34_incomplete_physical_Ka_transfer(self):
        model=fixture(2,"lex")
        a=model["a"]
        self.assertGreater(__import__("math").comb(a,2),
                           len(model["left_labels"]))
        inc=tuple(model["incidences"])
        for side in (0,1):
            b_labels=tuple(model["left_labels" if side==0 else "right_labels"])
            inverse={e:i for i,e in enumerate(b_labels)}
            root=0
            frozen=tuple(j for j,e in enumerate(inc) if e[side]==root)[:2]
            other=tuple(x for x in range(a) if x not in b_labels[root])
            candidate=None
            for verts in combinations(other,4):
                all_edges=set(combinations(verts,2))
                v0,v1,v2,v3=verts
                for omitted in (((v0,v1),(v2,v3)),
                                ((v0,v2),(v1,v3)),
                                ((v0,v3),(v1,v2))):
                    C4=tuple(sorted(all_edges-set(omitted)))
                    if all(e in inverse for e in C4):
                        candidate=tuple(inverse[e] for e in C4)
                        break
                if candidate is not None:break
            self.assertIsNotNone(candidate)
            row=opposite_physical_A_Hall_transfer(
                model,B_side=side,root=root,
                pinned_original_Q=frozen,four_sources=candidate)
            direct,forests=_direct_original_assignment(
                model,side,frozen,candidate)
            self.assertEqual(row["accepted_distinct_original_six_Q_through_permanents"],
                             direct)
            self.assertLessEqual(direct,forests)
            self.assertLessEqual(row["fully_occupied_opposite_physical_two_factors"],
                                 row["all_physical_two_factors_with_pinned_edges"])

    def test_08_negative_fake_original_or_noncomplete_maps(self):
        m=fixture(1,"S68")
        inc=tuple(m["incidences"])
        first=tuple(i for i,z in enumerate(inc) if z[0]==0)[:2]
        q=_W32_true_physical_C4_sources(tuple(m["left_labels"]),0)[0]
        with self.assertRaises(ValueError):
            opposite_physical_A_Hall_transfer(
                m,B_side=0,root=0,pinned_original_Q=first,
                four_sources=(0,)+q[1:])
        with self.assertRaises(ValueError):
            opposite_physical_A_Hall_transfer(
                m,B_side=0,root=0,pinned_original_Q=(first[0],first[0]),
                four_sources=q)
        with self.assertRaises(ValueError):
            opposite_physical_A_Hall_transfer(
                dict(m,incidences=m["incidences"][:-1]),B_side=0,
                root=0,pinned_original_Q=first,four_sources=q)
        with self.assertRaises(ValueError):
            opposite_physical_A_Hall_transfer(
                dict(m,right_labels=((0,1),)*15),B_side=0,
                root=0,pinned_original_Q=first,four_sources=q)
        with self.assertRaises(ValueError):
            opposite_physical_A_Hall_transfer(
                m,B_side=0,root=0,pinned_original_Q=first,
                four_sources=(q[0],)*4)
        with self.assertRaises(ValueError):
            pinned_twofactor_completions((0,1),(0,1),6)


if __name__=="__main__":
    unittest.main()
