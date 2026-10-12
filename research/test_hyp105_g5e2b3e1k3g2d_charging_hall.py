"""Independent finite Hall/mincut and original six-column charging falsifiers."""
from collections import Counter
from itertools import product
import unittest
from hyp105_g5e2b3e1k1_kikuchi_c6 import (
    gq_pair_model,kikuchi_graph,six_cycle_census,proper_six_cycles_pruned
)
from hyp105_g5e2b3e1k3g2d_charging_hall import (
    _maxflow_with_cut,edge_source_index,proper_d6_supports,cross_witnesses,
    finite_charging_certificate,HEAVY
)
from hyp105_g5e2b3e1k3g2c_projection_fibers import projection_pair_certificate


def brute_capacity_assignment(adjacency,right_count,capacity):
    """Small independent exhaustive assignment oracle, NO maxflow reused."""
    if not adjacency:
        return 0
    best=0
    for picks in product(range(right_count+1),repeat=len(adjacency)):
        used=[0]*right_count
        size=0
        valid=True
        for i,k in enumerate(picks):
            if k==right_count:
                continue
            if k not in adjacency[i] or used[k]>=capacity:
                valid=False
                break
            used[k]+=1
            size+=1
        if valid and size>best:
            best=size
    return best


def simple_original_column_counter(model):
    """Independent graph-edge physical pair reconstruction."""
    labels=model["left_labels"]
    lines=model["right_labels"]
    a=model["a"]
    mapping={}
    for p,l in model["incidences"]:
        x,xx=labels[p]
        y,yy=lines[l]
        for pair in ((x*a+y,xx*a+yy),(x*a+yy,xx*a+y)):
            key=frozenset(pair)
            if key in mapping:
                raise AssertionError("nonunique original physical incidence")
            mapping[key]=(p,l)
    return mapping


class K3G2DChargingTests(unittest.TestCase):
    def test_capacity_flow_and_exact_dual_mincut_bruteforce(self):
        examples=(
            ([],2),
            ([()],2),
            ([(0,)],1),
            ([(0,),(0,)],1),
            ([(0,1),(1,),(0,)],2),
            ([(0,),(0,),(0,),(1,)],2),
            ([(0,1),(1,2),(2,)],3),
            ([(0,1),(0,1),(0,1)],2)
        )
        for adj,right in examples:
            for capacity in (1,2,3):
                exact=_maxflow_with_cut(adj,right,capacity)
                brute=brute_capacity_assignment(adj,right,capacity)
                self.assertEqual(exact["matched"],brute)
                self.assertEqual(exact["min_cut_capacity"],brute)
                self.assertEqual(exact["unmatched"],len(adj)-brute)
                self.assertEqual(exact["all_witnesses_charged"],brute==len(adj))
        with self.assertRaises(ValueError):
            _maxflow_with_cut([(0,)],1,0)
        with self.assertRaises(ValueError):
            _maxflow_with_cut([(2,)],2,1)

    def test_proper_cycles_all_six_source_columns(self):
        for scheme in ("lex","reverse-line"):
            model=gq_pair_model(1,scheme)
            support=proper_d6_supports(model)
            g=kikuchi_graph(model)
            expected={"lex":15,"reverse-line":3}[scheme]
            self.assertEqual(len(support),expected)
            self.assertEqual(len(support),proper_six_cycles_pruned(g,model["a"]))
            self.assertEqual(len(support),six_cycle_census(g,model["a"])["proper_D6"])
            self.assertTrue(all(len(s)==6 for s in support))
            independent=simple_original_column_counter(model)
            edges=edge_source_index(model,g)
            self.assertEqual({frozenset(k):v for k,v in edges.items()},independent)

    def test_cross_witness_independent_seven_bins_and_no_unit_injection(self):
        # Finite, fully quantified model-specific NO-GO to a bijective
        # charging of ALL Jcross witnesses into accepted proper D6.
        for scheme,expected in (
            ("lex",{"Jcross":36,"D6":15,"heavy":18,"capacity_floor":3}),
            ("reverse-line",{"Jcross":28,"D6":3,"heavy":6,"capacity_floor":10}),
        ):
            model=gq_pair_model(1,scheme)
            rows=cross_witnesses(model)
            cert=finite_charging_certificate(model)
            c=projection_pair_certificate(model)
            self.assertEqual(len(rows),expected["Jcross"])
            self.assertEqual(cert["J_cross_exact"],expected["Jcross"])
            self.assertEqual(cert["proper_D6_exact"],expected["D6"])
            self.assertEqual(sum(r["class"]==HEAVY for r in rows),expected["heavy"])
            self.assertEqual(cert["heavy_witness_count"],expected["heavy"])
            self.assertEqual(cert["all_cross_anchor_local_charge"]["global_counting_floor"],
                             expected["capacity_floor"])
            self.assertTrue(cert["unit_injection_global_no_go"])
            self.assertGreater(cert["all_cross_anchor_local_charge"]["unmatched"],0)
            self.assertGreater(cert["heavy_anchor_local_charge"]["unmatched"],0)
            for side,part in (("line","line"),("point","point")):
                for cls,n in c[part]["seven_class_weighted"].items():
                    self.assertEqual(sum(x["side"]==side and x["class"]==cls
                                         for x in rows),n)

    def test_invalid_budgets_fail_closed(self):
        model=gq_pair_model(1,"lex")
        with self.assertRaises(RuntimeError):
            cross_witnesses(model,max_witnesses=0)
        with self.assertRaises(RuntimeError):
            proper_d6_supports(model,max_cycles=0)
        with self.assertRaises(ValueError):
            cross_witnesses(model,max_witnesses=True)
        with self.assertRaises(ValueError):
            proper_d6_supports(model,max_cycles=-1)

if __name__=="__main__":
    unittest.main()
