"""B1-C2 independent exact-rational falsifiers (two different oracles)."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb
import unittest

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_g5e2b3e1c0_weighted_overlap import (
    source_weighted_BA_hypergraph, exact_BA_overlap,
)
from hyp105_g5e2b3e1c2_johnson_gate import (
    target_degree_two_data, target_order_three_data,
    physical_three_edge_type, source_johnson_energy,
    exact_overlap_decomposition, is_target_sixset,
)


def independently_enumerated_T6():
    """All 5005 physical sextets; no C2 target implementation used."""
    physical=tuple(combinations(range(6),2))
    target=set()
    for R in combinations(range(15),6):
        d=Counter(v for i in R for v in physical[i])
        if len(d)==6 and set(d.values())=={2}:
            target.add(frozenset(R))
    return target


class ExactJohnsonC2Tests(unittest.TestCase):
    def test_target_two_point_johnson_projection_complete_K6(self):
        palette=tuple(combinations(range(6),2))
        N=comb(15,6)
        target=independently_enumerated_T6()
        self.assertEqual(len(target),70)
        oracle=target_degree_two_data(6)
        self.assertEqual(oracle["target_w2_norm_squared"],Fraction(42,11))
        self.assertEqual(oracle["target_w_ge3_norm_squared"],Fraction(9324,143))
        third=target_order_three_data(6)
        self.assertEqual(third["target_w3_norm_squared"],Fraction(710,1001))
        self.assertEqual(third["target_w_ge4_norm_squared"],Fraction(4966,77))
        self.assertEqual(oracle["johnson_lambda2"],330)
        pair_marginal=Counter()
        for R in target:
            for pair in combinations(sorted(R),2):
                pair_marginal[pair]+=1
        self.assertEqual(
            {pair_marginal[(i,j)] for i,j in combinations(range(15),2)
             if set(palette[i]) & set(palette[j])}, {7})
        self.assertEqual(
            {pair_marginal[(i,j)] for i,j in combinations(range(15),2)
             if not set(palette[i]) & set(palette[j])}, {14})
        # Construct the exact W2 projection over all 5005 physical sixsets,
        # independently from the analytic target norm formula.
        vector={}
        for R in combinations(range(15),6):
            residual=Fraction(0)
            for i,j in combinations(R,2):
                residual+=Fraction(pair_marginal[(i,j)]-10,330)
            vector[frozenset(R)]=residual
        self.assertEqual(sum(x*x for x in vector.values()),Fraction(42,11))
        for i in range(15):
            # W2 is orthogonal to all degree-one columns.
            self.assertEqual(sum(x for R,x in vector.items() if i in R),0)
        self.assertEqual(sum(vector.values()),0)
        self.assertEqual(sum(
            (int(R in target)-Fraction(70,N)-vector[R])**2
            for R in vector),Fraction(9324,143))

    def test_all_a_target_type_gate_and_vacuity(self):
        for a in (6,9,14,20):
            t=target_order_three_data(a)
            self.assertEqual(
                t["target_w0_norm_squared"]
                +t["target_w2_norm_squared"]
                +t["target_w_ge3_norm_squared"],t["T"])
            self.assertEqual(t["target_w1_norm_squared"],0)
            self.assertEqual(t["target_w2_zero"], a==9)
            self.assertGreater(t["target_w_ge3_norm_squared"],0)
            self.assertGreaterEqual(t["target_w3_norm_squared"],0)
            self.assertGreater(t["target_w_ge4_norm_squared"],0)
            self.assertEqual(t["target_w3_norm_squared"]+t["target_w_ge4_norm_squared"],t["target_w_ge3_norm_squared"])
            if a==9:
                self.assertEqual(t["target_w2_norm_squared"],0)
            else:
                self.assertGreater(t["target_w2_norm_squared"],0)
        for bad in (0,5,True,6.0):
            with self.assertRaises(ValueError):
                target_degree_two_data(bad)

    def test_independent_K6_complete_W3_target_energy(self):
        """Enumerate 455 triples and 5005 sextets without C2 W3 generator."""
        T=independently_enumerated_T6()
        palette=tuple(combinations(range(6),2))
        triple_marg=Counter()
        pair_marg=Counter()
        for R in T:
            for tr in combinations(sorted(R),3):
                triple_marg[tr]+=1
            for p in combinations(sorted(R),2):
                pair_marg[p]+=1
        data=target_order_three_data(6)
        obs=Counter()
        r3={}
        for tr in combinations(range(15),3):
            physical=tuple(palette[i] for i in tr)
            kind=physical_three_edge_type(physical)
            obs[kind]+=1
            q2sum=sum(Fraction(pair_marg[p]-10,330)
                      for p in combinations(tr,2))
            r3[tr]=(Fraction(triple_marg[tr])
                    -comb(12,3)*Fraction(70,5005)
                    -comb(10,3)*q2sum)
            self.assertEqual(
                r3[tr],data["target_three_harmonic_residual"][kind])
        self.assertEqual(
            dict(obs),{kind:v[0] for kind,v in data["target_three_orbits"].items()})
        self.assertEqual(sum(x*x for x in r3.values())/84,
                         Fraction(710,1001))
        projections={}
        for R in combinations(range(15),6):
            t2=sum(Fraction(pair_marg[p]-10,330)
                   for p in combinations(R,2))
            t3=sum(r3[tr] for tr in combinations(R,3))/84
            projections[frozenset(R)]=(t2,t3)
        self.assertEqual(sum(z[1]*z[1] for z in projections.values()),
                         Fraction(710,1001))
        self.assertEqual(sum(
            (int(R in T)-Fraction(70,5005)-v[0]-v[1])**2
            for R,v in projections.items()),Fraction(4966,77))
        for pair in combinations(range(15),2):
            self.assertEqual(sum(v[1] for R,v in projections.items()
                                 if set(pair)<=R),0)

    def test_source_projection_against_brute_5005_vector(self):
        model=pair_labeled_symplectic(1,"lex")
        weights=source_weighted_BA_hypergraph(model)
        x=source_johnson_energy(weights,15)
        self.assertEqual(x["M"],5000)
        self.assertEqual(x["N"],5005)
        self.assertEqual(sum(x["degree_vector"]),6*5000)
        self.assertEqual(sum(x["pair_marginals"].values()),15*5000)
        m0=Fraction(5000,5005)
        beta=x["w1_betas"]
        r=x["w2_pair_residuals"]
        squared={"w0":Fraction(0),"w1":Fraction(0),
                 "w2":Fraction(0),"w3":Fraction(0),"wge3":Fraction(0),"wge4":Fraction(0)}
        for R in combinations(range(15),6):
            y0=m0
            y1=sum(beta[i] for i in R)
            y2=sum(r[p] for p in combinations(R,2))/330
            y3=sum(x["w3_triple_residuals"][tr] for tr in combinations(R,3))/84
            yge3=Fraction(weights.get(frozenset(R),0))-y0-y1-y2
            y4=yge3-y3
            squared["w0"]+=y0*y0
            squared["w1"]+=y1*y1
            squared["w2"]+=y2*y2
            squared["w3"]+=y3*y3
            squared["wge3"]+=yge3*yge3
            squared["wge4"]+=y4*y4
        for name,attr in (("w0","w0_norm_squared"),
                          ("w1","w1_norm_squared"),
                          ("w2","w2_norm_squared"),
                          ("w3","w3_norm_squared"),
                          ("wge3","w_ge3_norm_squared"),
                          ("wge4","w_ge4_norm_squared")):
            self.assertEqual(squared[name],x[attr])
        self.assertEqual(squared["w0"]+squared["w1"]+squared["w2"]+squared["w3"]+squared["wge4"],x["source_norm_squared"])

    def test_W32_all_105_original_right_line_swaps_exact_identity(self):
        model=pair_labeled_symplectic(1,"reverse-line")
        weights=source_weighted_BA_hypergraph(model)
        labels=list(model["right_labels"])
        reference=independently_enumerated_T6()
        palette=tuple(combinations(range(6),2))
        indices={edge:i for i,edge in enumerate(palette)}
        expected_mass=5000
        saw_nonzero_higher=False
        for swap in (None,)+tuple(combinations(range(15),2)):
            perm=list(labels)
            if swap is not None:
                i,j=swap
                perm[i],perm[j]=perm[j],perm[i]
            observed=exact_overlap_decomposition(
                weights,perm,a=6,with_source_norms=False,
                with_third_order=swap in (None,(4,13),(0,1),(7,8)))
            mapped=tuple(indices[e] for e in perm)
            independent=sum(w for R,w in weights.items()
                if frozenset(mapped[i] for i in R) in reference)
            self.assertEqual(observed["overlap_exact"],independent)
            self.assertEqual(observed["source_mass"],expected_mass)
            self.assertEqual(
                observed["uniform_injection_mean"]
                +observed["correlated_degree2_contribution"]
                +observed["degree_ge3_contribution"],independent)
            self.assertEqual(observed["uniform_injection_mean"],
                             Fraction(5000*2,143))
            saw_nonzero_higher |= (
                observed["degree_ge3_contribution"]!=0)
            if swap in (None,(4,13),(0,1),(7,8)):
                self.assertEqual(observed["uniform_injection_mean"]+observed["correlated_degree2_contribution"]+observed["correlated_degree3_contribution"]+observed["degree_ge4_contribution"],independent)
                self.assertTrue(observed["johnson_identity_degree3_exact"])
            if swap == (4,13):
                self.assertEqual(independent,57)
            if swap is None:
                self.assertEqual(independent,77)
        self.assertTrue(saw_nonzero_higher)
        exact=exact_overlap_decomposition(weights,labels,a=6)
        self.assertTrue(exact["square_bound_checked"])
        self.assertTrue(exact["johnson_identity_degree3_exact"])
        self.assertGreater(exact["target_w_ge4_norm_squared"],0)
        self.assertFalse(exact["universal_all_correlated_positive_lower_proved"])

    def test_non_surjective_injection_and_higher_only_trade(self):
        # Original K6 3-cube trade proves degree <=2 cannot determine
        # overlap, including with identical mass and actual image g.
        shared=(0,1,6)
        flips=((2,11),(3,12),(13,14))
        even,odd={},{}
        for n in range(8):
            R=frozenset(shared+tuple(pair[(n>>j)&1]
                              for j,pair in enumerate(flips)))
            (even if n.bit_count()%2==0 else odd)[R]=1
        right=tuple(combinations(range(6),2))
        e=exact_overlap_decomposition(even,right,a=6)
        o=exact_overlap_decomposition(odd,right,a=6)
        self.assertEqual(e["overlap_exact"],0)
        self.assertEqual(o["overlap_exact"],1)
        self.assertEqual(e["uniform_injection_mean"],o["uniform_injection_mean"])
        self.assertEqual(e["correlated_degree2_contribution"],
                         o["correlated_degree2_contribution"])
        self.assertTrue(e["johnson_identity_degree3_exact"])
        self.assertTrue(o["johnson_identity_degree3_exact"])
        self.assertEqual(
            o["degree_ge3_contribution"]-e["degree_ge3_contribution"],1)
        # All 15 old vertices embed into 36 physical pair labels at a=9.
        # The physical target has W2=0 for *every* right injection.
        padded=exact_overlap_decomposition(even,right,a=9)
        self.assertEqual(padded["correlated_degree2_contribution"],0)
        self.assertTrue(padded["johnson_identity_exact"])
        self.assertTrue(padded["square_bound_checked"])

    def test_invalid_injections_and_weights_fail_closed(self):
        R=frozenset(range(6))
        labels=tuple(combinations(range(6),2))
        for invalid in ({R:-1},{R:True},{frozenset(range(5)):1},
                        {frozenset((0,1,2,3,4,15)):1}):
            with self.assertRaises(ValueError):
                exact_overlap_decomposition(invalid,labels,a=6)
        with self.assertRaises(ValueError):
            exact_overlap_decomposition({R:1},labels[:5],a=6)
        with self.assertRaises(ValueError):
            exact_overlap_decomposition({R:1},[labels[0]]*15,a=6)
        with self.assertRaises(ValueError):
            exact_overlap_decomposition({R:1},labels,a=True)


if __name__=="__main__":
    unittest.main()
