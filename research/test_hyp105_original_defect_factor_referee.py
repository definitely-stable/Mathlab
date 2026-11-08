"""Independent factorization, iff classification and genuine GQ adversarial falsifiers."""
from fractions import Fraction
from itertools import combinations
import unittest

from hyp105_original_defect_factor_referee import (
    SCHEMA, _cases, degree_defect, genuine_symplectic_source,
    projection_defect, canonical_certificate,
)


class TestOriginalGQDegreeFactor(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sources={s:genuine_symplectic_source(s) for s in (2,4)}

    def test_independent_finite_symplectic_GQ_source_cardinality(self):
        for s, flags in self.sources.items():
            V=(s+1)*(s*s+1)
            self.assertEqual(len(flags),V*(s+1))
            self.assertEqual(len(set(flags)),len(flags))
            self.assertEqual(len({p for p,l in flags}),V)
            self.assertEqual(len({l for p,l in flags}),V)

    def test_all_structured_and_seeded_adversarial_source_cases_two_oracles(self):
        for s, flags in self.sources.items():
            for case,Z in _cases(s,flags).items():
                with self.subTest(s=s,case=case):
                    deg=degree_defect(s,flags,Z)
                    geo=projection_defect(s,flags,Z)
                    self.assertEqual(deg['D_local'],geo['D_projection'])
                    self.assertLessEqual(geo['M_projection'],deg['M_upper_from_local_D'])
                    self.assertEqual(geo['M_projection'],8*s*s*len(Z)+4*(
                        geo['D_projection']-geo['H']-geo['F']))
                    self.assertEqual(deg['D_local']==0,
                                     deg['union_of_complete_point_line_stars'])
                    self.assertEqual(deg['kappa'],str(Fraction(
                        deg['D_local'],s*s*len(Z))) if Z else '0')
                    self.assertTrue(geo['three_roles_s2'])

    def test_ZERO_defect_if_and_ONLY_if_full_point_line_star_union(self):
        for s,flags in self.sources.items():
            cases=_cases(s,flags)
            for name in ('empty','point-star','line-star','mixed-star',
                         'mixed-nonincident-stars','full-original-I'):
                d=degree_defect(s,flags,cases[name])
                self.assertEqual(d['D_local'],0)
                self.assertTrue(d['union_of_complete_point_line_stars'])
                self.assertEqual(d['uncovered_original_IDs'],())
            for name in ('single','incomplete-point-star','point-star-plus-one'):
                d=degree_defect(s,flags,cases[name])
                self.assertGreater(d['D_local'],0)
                self.assertFalse(d['union_of_complete_point_line_stars'])
                self.assertTrue(d['uncovered_original_IDs'])

    def test_single_original_deleted_ID_saturates_old_bound(self):
        for s,flags in self.sources.items():
            d=degree_defect(s,flags,{0})
            geo=projection_defect(s,flags,{0})
            self.assertEqual(d['D_local'],s*s)
            self.assertEqual(geo['H'],0)
            self.assertEqual(geo['F'],0)
            self.assertEqual(geo['M_projection'],12*s*s)
            self.assertEqual(d['kappa'],'1')

    def test_broken_full_star_plus_one_extra_degree_formula_beats_coarse_e(self):
        for s,flags in self.sources.items():
            Z=_cases(s,flags)['point-star-plus-one']
            d=degree_defect(s,flags,Z)
            self.assertGreater(d['D_local'],0)
            self.assertLess(d['D_local'],s*s)
            self.assertLess(Fraction(d['D_local'],s*s*len(Z)),Fraction(1,len(Z)))
            self.assertLess(d['M_upper_from_local_D'],d['original_universal_M_upper'])

    def test_degree_contributions_sum_and_each_term_is_actual_two_choice_product(self):
        for s,flags in self.sources.items():
            Z=_cases(s,flags)['incomplete-point-star']
            d=degree_defect(s,flags,Z)
            self.assertEqual(sum(v for i,v in d['contributions']),d['D_local'])
            self.assertTrue(all(0<=v<=s*s for i,v in d['contributions']))
            self.assertTrue(all(v>0 for i,v in d['contributions']))

    def test_original_source_ID_permutation_and_point_line_duality(self):
        for s,flags in self.sources.items():
            Z=_cases(s,flags)['point-star-plus-one']
            d=degree_defect(s,flags,Z)
            self.assertEqual(d['D_local'],degree_defect(s,
                tuple((l,p) for p,l in flags),Z)['D_local'])
            reversed_flags=flags[::-1]
            reverse_Z={len(flags)-1-i for i in Z}
            other=degree_defect(s,reversed_flags,reverse_Z)
            self.assertEqual(d['D_local'],other['D_local'])
            self.assertEqual(d['kappa'],other['kappa'])
            self.assertEqual(d['union_of_complete_point_line_stars'],
                             other['union_of_complete_point_line_stars'])

    def test_w32_all_two_original_ID_deletions_local_and_sample_projection(self):
        flags=self.sources[2]
        pairs=list(combinations(range(len(flags)),2))
        self.assertEqual(len(pairs),990)
        for j,Z in enumerate(pairs):
            d=degree_defect(2,flags,Z)
            if j%37==0:
                self.assertEqual(d['D_local'],projection_defect(2,flags,Z)['D_projection'])
            self.assertEqual(d['D_local']==0,d['union_of_complete_point_line_stars'])

    def test_negative_fake_source_flag_IDs_duplicates_bad_degrees_and_bool(self):
        f=self.sources[2]
        for invalid in ((0,0),(-1,), (len(f),),(True,), (1.5,),('0',)):
            with self.subTest(ids=invalid),self.assertRaises(ValueError):
                degree_defect(2,f,invalid)
        with self.assertRaises(ValueError):
            degree_defect(2,f[:-1],(0,))
        with self.assertRaises(ValueError):
            degree_defect(2,tuple([f[0]]+list(f[1:-1])+[f[0]]),(0,))
        with self.assertRaises(ValueError):
            genuine_symplectic_source(8)

    def test_strict_canonical_certificate_no_root_proof_promotion(self):
        report=canonical_certificate()
        self.assertEqual(report['schema'],SCHEMA)
        self.assertEqual(report['issue'],230)
        self.assertEqual(report['status'],'OPEN_WITH_FORMAL_BLOCKER')
        self.assertFalse(report['new_root_A_PROVED'])
        self.assertFalse(report['new_ASET_exponent'])
        self.assertEqual(report['finite_verified_orders'],[2,4])
        self.assertEqual(len(report['independent_cases']),33)
        self.assertTrue(all(x['original_GQ_roles_s2'] for x in report['independent_cases']))


if __name__=='__main__':
    unittest.main()
