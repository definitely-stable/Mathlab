"""HYP-105 C3: independent GQ witness and missing-star finite falsifiers."""
from collections import Counter
from fractions import Fraction
from itertools import combinations,product
from math import comb
import unittest

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_g5e2b3e1a_fixed_leading import validated_small_model
from hyp105_g5e2b3e1c1_gq_concurrency import (
    physical_four_cycles_on_other_coordinates,
    original_right_line_concurrency,
)
from hyp105_g5e2b3e1c3_wedge_alignment import (
    max_occupied_physical_adjacency,actual_occupied_physical_adjacency,
    universal_wedge_alignment,original_W32_distinguished_right_pair_source,
    finite_W32_distinguished_pair_report,
)


def independent_wedge_pair_mass(model):
    """Second original-incidence algorithm: by p, four-cycle, and neighbors.

    Does not call the production selected_left_six() constructor or
    C3's witness enumeration. The 10935 B candidate count is independent.
    """
    physical,_,original,_=validated_small_model(model)
    reverse={edge:p for p,edge in enumerate(physical)}
    incident=[set() for _ in physical]
    for p,l in original:
        incident[p].add(l)
    result=Counter()
    candidates=0
    for p,edge in enumerate(physical):
        for square in physical_four_cycles_on_other_coordinates(edge,6):
            singles=tuple(reverse[e] for e in square)
            for u,v in combinations(sorted(incident[p]),2):
                for rest in product(*(incident[q] for q in singles)):
                    candidates+=1
                    if len({u,v,*rest})==6:
                        result[frozenset((u,v))]+=1
    if candidates!=10935:
        raise AssertionError("independent B candidate count invalid")
    return result


class WitnessPairAlignmentTests(unittest.TestCase):
    def test_missing_star_sharp_physical_adjacency(self):
        for a,max_missing in ((6,3),(7,4)):
            alphabet=tuple(combinations(range(a),2))
            for missing_count in range(max_missing+1):
                bound=max_occupied_physical_adjacency(
                    a,len(alphabet)-missing_count)
                observed=[]
                for missed in combinations(alphabet,missing_count):
                    value=actual_occupied_physical_adjacency(a,missed)
                    self.assertLessEqual(
                        value,bound["max_occupied_physical_adjacent_pair_count"])
                    observed.append(value)
                self.assertEqual(max(observed),
                                 bound["max_occupied_physical_adjacent_pair_count"])
                star=tuple((0,i) for i in range(1,missing_count+1))
                self.assertEqual(actual_occupied_physical_adjacency(a,star),
                                 bound["max_occupied_physical_adjacent_pair_count"])
        for a,n in ((5,10),(6,0),(6,16),(6,6.0),(True,10)):
            with self.assertRaises(ValueError):
                max_occupied_physical_adjacency(a,n)

    def test_gq_all_h_sharp_finite_bounds_and_asymptotic_gate(self):
        fractions=[]
        for s in (2,4,8,16,32,64,128,256,512,1024):
            c=universal_wedge_alignment(s)
            a,K,V=c["a"],c["K"],c["V"]
            self.assertLess(K-V,a)
            self.assertEqual(
                c["source_witness_multiplicity_each_pair_upper"],
                3*comb(a-2,4)*(s+1)**4)
            self.assertEqual(
                c["occupied_physical_adjacency_upper"],
                K*(a-2)-2*(K-V)*(a-2)+comb(K-V,2))
            self.assertEqual(c["original_concurrent_pair_count"],
                             V*s*(s+1)//2)
            self.assertEqual(c["physically_disjoint_distinguished_pair_source_mass_lower"],
                max(0,c["source_mass_lower"]
                    -c["concurrent_pairs_mapped_physically_adjacent_upper"]
                    *c["source_witness_multiplicity_each_pair_upper"]))
            self.assertFalse(c["positive_all_correlated_sixset_overlap_proved"])
            self.assertFalse(c["all_seven_motifs_omega_s6_proved"])
            if s>=16:
                self.assertGreater(
                    c["physically_disjoint_distinguished_pair_source_mass_lower"],0)
            if s>=128:
                fractions.append(c["source_mass_disjoint_fraction_lower"])
        self.assertTrue(all(a<b for a,b in zip(fractions,fractions[1:])))
        self.assertGreater(fractions[0],Fraction(7,10))
        self.assertGreater(fractions[-1],Fraction(9,10))
        for bad in (0,1,3,True):
            with self.assertRaises(ValueError):
                universal_wedge_alignment(bad)

    def test_real_GQ_W32_independent_original_wedge_source(self):
        for scheme in ("lex","reverse-line"):
            model=pair_labeled_symplectic(1,scheme)
            w,by_six=original_W32_distinguished_right_pair_source(model)
            independent=independent_wedge_pair_mass(model)
            self.assertEqual(independent,w)
            self.assertEqual(sum(w.values()),5000)
            self.assertEqual(len(by_six),3076)
            self.assertEqual(max(by_six.values()),6)
            gamma=original_right_line_concurrency(model)
            self.assertTrue(all(j in gamma[i] for pair in w
                                for i,j in (tuple(sorted(pair)),)))
            cert=universal_wedge_alignment(2)
            self.assertLessEqual(max(w.values()),
                                 cert["source_witness_multiplicity_each_pair_upper"])
            diagnostic=finite_W32_distinguished_pair_report(model)
            self.assertEqual(
                diagnostic["physically_disjoint_witness_mass"]+
                diagnostic["physically_adjacent_witness_mass"],5000)
            self.assertEqual(diagnostic["distinct_original_concurrent_witness_pairs"],
                             len(w))
            self.assertFalse(diagnostic["actual_complete_BA_six_target_lower_claim"])

    def test_every_real_W32_original_line_swap_witness_mass_conserved(self):
        model=pair_labeled_symplectic(1,"reverse-line")
        original_source,_=original_W32_distinguished_right_pair_source(model)
        labels=tuple(model["right_labels"])
        signatures=set()
        for changed in (None,)+tuple(combinations(range(15),2)):
            phys=list(labels)
            if changed is not None:
                i,j=changed
                phys[i],phys[j]=phys[j],phys[i]
            observed=finite_W32_distinguished_pair_report(
                model,right_labels=phys)
            independent=sum(weight for pair,weight in original_source.items()
                            if set(phys[next(iter(pair))])
                            &set(phys[next(iter(pair-{next(iter(pair))}))]))
            self.assertEqual(observed["physically_adjacent_witness_mass"],
                             independent)
            self.assertEqual(observed["physically_disjoint_witness_mass"],
                             5000-independent)
            signatures.add(independent)
        self.assertGreater(len(signatures),1)

    def test_invalid_missing_images_fail_closed(self):
        with self.assertRaises(ValueError):
            actual_occupied_physical_adjacency(6,((0,1),(0,1)))
        with self.assertRaises(ValueError):
            actual_occupied_physical_adjacency(6,((0,6),))
        with self.assertRaises(ValueError):
            actual_occupied_physical_adjacency(False,())
        model=pair_labeled_symplectic(1,"lex")
        with self.assertRaises(ValueError):
            finite_W32_distinguished_pair_report(
                model,right_labels=[(0,1)]*15)


if __name__=="__main__":
    unittest.main()
