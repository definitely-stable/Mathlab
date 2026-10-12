"""Independent GQ anchor projection, cardinalities and weighted Jcross oracle."""
from collections import Counter
from itertools import combinations
import unittest

from hyp105_g5e2b3e1k1_kikuchi_c6 import gq_pair_model
from hyp105_g5e2b3e1k3g2b_origin_pair_kernel import inc_tables
from hyp105_g5e2b3e1k3g2c_projection_fibers import (
    projection_pair_certificate, theoretical_pair_capacities,
    CLASSES7,
)

def independent_projection_by_original_paths(P,L,side,anchor):
    """Follow actual original GQ incidences, not shared-line set intersection."""
    origins=P if side=="line" else L
    opposite=L if side=="line" else P
    anchor_set=opposite[anchor]
    foot={}
    for q in range(len(origins)):
        if q in anchor_set:
            foot[q]=q
        else:
            found=[]
            for opposite_id in origins[q]:
                for possible in opposite[opposite_id]:
                    if possible in anchor_set:
                        found.append(possible)
            if len(found)!=1:
                raise AssertionError("original GQ projection missing/not unique")
            foot[q]=found[0]
    return foot

def independent_class(q,r,projection,on,P_or_L):
    q_on=q in on
    r_on=r in on
    if q_on and r_on:
        return "both_on_anchor"
    if q_on!=r_on:
        marked=q if q_on else r
        remote=r if q_on else q
        return "one_on_projected" if projection[remote]==marked else "one_on_other"
    same=projection[q]==projection[r]
    collinear=False
    # Independently enumerate original incidence instead of set intersection.
    for original in P_or_L[q]:
        if original in P_or_L[r]:
            collinear=True
            break
    if same:
        return "off_samefoot_collinear" if collinear else "off_samefoot_noncollinear"
    return "off_differentfoot_collinear" if collinear else "off_differentfoot_noncollinear"

def independent_closure_by_third_physical_coordinate(model,side,P,L):
    labels=model["right_labels"] if side=="line" else model["left_labels"]
    source=L if side=="line" else P
    inv={frozenset(edge):i for i,edge in enumerate(labels)}
    buckets=[Counter() for _ in labels]
    for anchor,(x,y) in enumerate(labels):
        for t in range(model["a"]):
            if t==x or t==y:
                continue
            j=inv.get(frozenset((x,t)))
            k=inv.get(frozenset((y,t)))
            if j is None or k is None:
                continue
            common=source[j]&source[k]
            if len(common)>1:
                raise AssertionError("two original GQ source intersections")
            for q in common:
                buckets[anchor][q]+=1
    return buckets

def independent_kernel_count(physq,physr,anchor_physical):
    """Count through actual original anchor incidence labels, no pair-set join."""
    total=0
    for x,y in anchor_physical:
        total+=int((x in physq and y in physr) or
                   (x in physr and y in physq))
    return total

class K3G2CProjectionTests(unittest.TestCase):
    def test_independent_all_original_pair_population_both_dual_sides(self):
        for h,scheme,seed in ((1,"lex",None),(2,"random",20261011)):
            model=gq_pair_model(h,scheme,seed)
            P,L=inc_tables(model)
            V=len(P)
            expected=theoretical_pair_capacities(model["s"])
            self.assertEqual(sum(expected.values()),V*(V-1)//2)
            for side in ("line","point"):
                on_anchor=L if side=="line" else P
                pencil=P if side=="line" else L
                for anchor,on in enumerate(on_anchor):
                    foot=independent_projection_by_original_paths(P,L,side,anchor)
                    self.assertEqual(set(foot.values()),set(on))
                    self.assertTrue(all(sum(foot[q]==t for q in range(V))==
                                        model["s"]**2+1 for t in on))
                    observed=Counter(
                        independent_class(q,r,foot,on,pencil)
                        for q,r in combinations(range(V),2))
                    for cls in CLASSES7:
                        self.assertEqual(observed[cls],expected[cls])

    def test_independent_weighted_refinement_of_entire_cross_kernel(self):
        for h,scheme,seed in ((1,"lex",None),(1,"reverse-line",None),
                              (2,"lex",None),(2,"random",20261011)):
            m=gq_pair_model(h,scheme,seed)
            P,L=inc_tables(m)
            report=projection_pair_certificate(m)
            for side in ("line","point"):
                on_anchor=L if side=="line" else P
                origin_pencil=P if side=="line" else L
                physical=m["left_labels"] if side=="line" else m["right_labels"]
                T=independent_closure_by_third_physical_coordinate(m,side,P,L)
                bins=Counter()
                raw=Counter()
                direct_same=0
                foot_pair_mass=Counter()
                for anchor,on in enumerate(on_anchor):
                    projection=independent_projection_by_original_paths(
                        P,L,side,anchor)
                    anchor_phys=[physical[q] for q in on]
                    for q,t in T[anchor].items():
                        if q in on:
                            direct_same+=t*t
                    for q,r in combinations(sorted(T[anchor]),2):
                        klass=independent_class(q,r,projection,on,origin_pencil)
                        mass=T[anchor][q]*T[anchor][r]
                        raw[klass]+=mass
                        foot_pair_mass[projection[q]==projection[r]]+=mass
                        bridges=independent_kernel_count(physical[q],physical[r],
                                                         anchor_phys)
                        bins[klass]+=bridges*mass
                for klass in CLASSES7:
                    self.assertEqual(bins[klass],
                        report[side]["seven_class_weighted"][klass])
                    self.assertEqual(raw[klass],
                        report[side]["seven_class_source_pair_products"][klass])
                self.assertEqual(direct_same,report[side]["total_same"])
                self.assertEqual(foot_pair_mass[True],
                    report[side]["same_foot_source_pair_products"])
                self.assertEqual(foot_pair_mass[False],
                    report[side]["different_foot_source_pair_products"])
                self.assertEqual(sum(bins.values()),report[side]["total_cross"])
            self.assertFalse(report["all_h_Jcross_o_s6_proved"])

    def test_projection_exact_minimal_example_and_invalid_budgets(self):
        m=gq_pair_model(1,"lex")
        r=projection_pair_certificate(m)
        self.assertEqual(r["line"]["complete_projection_fiber_size"],5)
        self.assertEqual(r["point"]["complete_projection_fiber_size"],5)
        with self.assertRaises(RuntimeError):
            projection_pair_certificate(m,max_pairs=0)
        with self.assertRaises(RuntimeError):
            projection_pair_certificate(m,max_geometry_pairs=0)
        with self.assertRaises(ValueError):
            projection_pair_certificate(m,max_pairs=True)
        with self.assertRaises(ValueError):
            projection_pair_certificate(m,max_geometry_pairs=-1)
        with self.assertRaises(ValueError):
            theoretical_pair_capacities(True)

if __name__=="__main__":
    unittest.main()
