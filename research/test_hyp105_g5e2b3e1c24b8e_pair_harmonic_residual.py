"""Independent small-K6 enumeration of B8-E Gram and projection identities."""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
import unittest

from hyp105_g5e2b3e1c24b8e_pair_harmonic_residual import (
    exact_pair_gram_parameters,exact_gram_entry,
    exact_pair_projection,evaluate_projection,exact_residual_witness,
)


def brute_four_lines():
    """Completely independent 15P4 global injection marginal enumeration."""
    edges=tuple(combinations(range(6),2))
    pairs=tuple(combinations(range(4),2))
    counts=Counter()
    zz=Counter()
    score_z=Counter()
    N=0
    for images in permutations(edges,4):
        z={e:int(bool(set(images[e[0]])&set(images[e[1]]))) for e in pairs}
        # Deliberately nonlinear physical-invariant score; NOT HYP-105 S.
        score=2*z[(0,1)]*z[(2,3)]+3*z[(0,2)]
        N+=1
        counts["score"]+=score
        counts["score_squared"]+=score*score
        for e in pairs:
            counts[e]+=z[e]
            score_z[e]+=score*z[e]
            for h in pairs:
                zz[(e,h)]+=z[e]*z[h]
    return N,pairs,counts,score_z,zz


class PairHarmonicResidualTests(unittest.TestCase):
    def test_all_h_gram_eigenvalues_and_zero_modes(self):
        par=exact_pair_gram_parameters(6,15)
        self.assertEqual(par["p_adj"],Fraction(4,7))
        self.assertEqual(par["variance"],Fraction(12,49))
        self.assertEqual(par["eigenvalues"],(0,0,Fraction(2,7)))
        self.assertEqual(par["multiplicities"],(1,14,90))
        self.assertEqual(par["rank"],90)
        self.assertEqual(exact_pair_gram_parameters(6,14)["rank"],90)
        self.assertEqual(exact_pair_gram_parameters(6,13)["rank"],78)
        self.assertEqual(exact_pair_gram_parameters(7,8)["rank"],28)
        self.assertEqual(exact_gram_entry(6,15,(0,1),(0,1)),Fraction(12,49))
        self.assertEqual(exact_gram_entry(6,15,(0,1),(0,2)),-Fraction(12,637))
        self.assertEqual(exact_gram_entry(6,15,(0,1),(2,3)),Fraction(2,637))

    def test_independent_enumerated_k6_p4_all_cross_covariances(self):
        N,pairs,counts,score_z,zz=brute_four_lines()
        self.assertEqual(N,32760)
        p=Fraction(4,7)
        mean=Fraction(counts["score"],N)
        variance=Fraction(counts["score_squared"],N)-mean**2
        v=p*(1-p)
        b={}
        for e in pairs:
            self.assertEqual(Fraction(counts[e],N),p)
            b[e]=Fraction(score_z[e],N)-mean*p
            for h in pairs:
                brute=Fraction(zz[(e,h)],N)-p*p
                self.assertEqual(brute,exact_gram_entry(6,4,e,h))
        I={e:b[e]/v for e in pairs}
        projection=exact_pair_projection(I,6,4)
        gamma=projection["coefficients"]
        self.assertTrue(projection["exact_orthogonality_all_pair_features"])
        second=Fraction(0)
        for e in pairs:
            predicted=sum((gamma[h]*(Fraction(zz[(e,h)],N)-p*p)
                           for h in pairs),Fraction(0))
            self.assertEqual(predicted,b[e])
            for h in pairs:
                second+=gamma[e]*gamma[h]*(Fraction(zz[(e,h)],N)-p*p)
        self.assertEqual(second,projection["projected_variance"])
        self.assertGreater(variance-second,0)
        sample=tuple(combinations(range(6),2))[:4]
        score_at_sample=(2*int(bool(set(sample[0])&set(sample[1])))
                         *int(bool(set(sample[2])&set(sample[3])))
                         +3*int(bool(set(sample[0])&set(sample[2]))))
        witness=exact_residual_witness(projection,mean,score_at_sample,sample,6)
        self.assertEqual(
            witness["nonlinear_pair_feature_residual_at_g"],
            Fraction(score_at_sample)-mean-evaluate_projection(projection,sample,6))

    def test_full_and_one_slack_host_singular_gram_valid_canonical(self):
        edges=tuple(combinations(range(6),2))
        for n in (14,15):
            pairs=tuple(combinations(range(n),2))
            # Score is precisely the original pair adjacency Z_01.
            b={e:exact_gram_entry(6,n,e,(0,1)) for e in pairs}
            v=exact_pair_gram_parameters(6,n)["variance"]
            projection=exact_pair_projection({e:b[e]/v for e in pairs},6,n)
            self.assertEqual(projection["projected_variance"],v)
            self.assertEqual(evaluate_projection(projection,edges[:n],6),
                             int(bool(set(edges[0])&set(edges[1])))-Fraction(4,7))
        bad={e:Fraction(0) for e in combinations(range(15),2)}
        bad[(0,1)]=Fraction(1)
        with self.assertRaisesRegex(ValueError,"zero-variance"):
            exact_pair_projection(bad,6,15)

    def test_fail_closed_inputs(self):
        with self.assertRaises(ValueError):
            exact_pair_gram_parameters(5,4)
        with self.assertRaises(ValueError):
            exact_pair_gram_parameters(6,16)
        with self.assertRaises(ValueError):
            exact_pair_projection({},6,4)
        with self.assertRaises(ValueError):
            exact_gram_entry(6,4,(1,0),(1,2))
        base={e:Fraction(0) for e in combinations(range(4),2)}
        projection=exact_pair_projection(base,6,4)
        with self.assertRaises(ValueError):
            evaluate_projection(projection,((0,1),)*4,6)
        with self.assertRaises(ValueError):
            exact_residual_witness(projection,Fraction(0),-1,
                                   tuple(combinations(range(6),2))[:4],6)


if __name__=="__main__":
    unittest.main()
