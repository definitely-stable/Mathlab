"""Independent genuine GQ endpoint-overlap/label-correlation falsifiers."""
import unittest
from itertools import combinations
from math import comb
from hyp105_original_defect_factor_referee import genuine_symplectic_source, _cases
from hyp105_original_low_endpoint_overlap import (
    SCHEMA, canonical_certificate, exact_source_overlap, projection_oracle,
    outer_dual_oracles, label_endpoint_oracle,
)


def labels(s, reverse=False):
    V=(s+1)*(s*s+1)
    a=next(k for k in range(2,2*V+2) if comb(k,2)>=V)
    pairs=list(combinations(range(a),2))[:V]
    return pairs,list(reversed(pairs)) if reverse else pairs


class TestOriginalEndpointOverlap(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.gqs={s:genuine_symplectic_source(s) for s in (2,4)}

    def test_all_true_original_projection_oracles(self):
        for s,flags in self.gqs.items():
            for name,z in _cases(s,flags).items():
                with self.subTest(s=s,case=name):
                    local=exact_source_overlap(s,flags,z)
                    global_oracle=projection_oracle(s,flags,z)
                    px,ly=outer_dual_oracles(s,flags,z)
                    self.assertEqual(local['outer_overlap'],px)
                    self.assertEqual(px,ly)
                    self.assertEqual(px,global_oracle['outer'])
                    self.assertEqual(local['middle_only_defect'],global_oracle['middle_only'])
                    self.assertEqual(local['touched_projections'],global_oracle['union'])
                    self.assertEqual(local['physical_deleted_endpoint_upper'],4*global_oracle['union'])
                    self.assertLessEqual(local['physical_deleted_endpoint_upper'],local['old_defect_upper'])
                    self.assertLessEqual(local['old_defect_upper'],local['old_universal_upper'])
                    self.assertGreaterEqual(local['weighted_GQ_spectral_slack'],0)

    def test_singleton_is_worst_case_and_full_star_is_two_thirds(self):
        for s,flags in self.gqs.items():
            cases=_cases(s,flags)
            one=exact_source_overlap(s,flags,cases['single'])
            star=exact_source_overlap(s,flags,cases['point-star'])
            self.assertEqual(one['physical_deleted_endpoint_upper'],12*s*s)
            self.assertEqual(star['physical_deleted_endpoint_upper'],8*s*s*(s+1))
            self.assertEqual(star['middle_only_defect'],0)
            self.assertEqual(star['outer_overlap'],0)
            self.assertTrue(star['star_union'])

    def test_mixed_star_has_strict_new_outer_overlap(self):
        for s,flags in self.gqs.items():
            z=_cases(s,flags)['mixed-star']
            local=exact_source_overlap(s,flags,z)
            self.assertEqual(local['middle_only_defect'],0)
            self.assertGreater(local['outer_overlap'],0)
            self.assertLess(local['physical_deleted_endpoint_upper'],local['old_defect_upper'])

    def test_point_line_duality_and_original_flag_permutation(self):
        for s,flags in self.gqs.items():
            z=_cases(s,flags)['point-star-plus-one']
            old=exact_source_overlap(s,flags,z)
            dual=exact_source_overlap(s,tuple((l,p) for p,l in flags),z)
            rev=exact_source_overlap(s,flags[::-1],{len(flags)-1-i for i in z})
            for key in ('outer_overlap','middle_only_defect','touched_projections'):
                self.assertEqual(old[key],dual[key])
                self.assertEqual(old[key],rev[key])

    def test_all_990_genuine_W32_two_flag_subsets_degree_only_vs_two_dual_oracles(self):
        flags=self.gqs[2]
        self.assertEqual(len(flags),45)
        for z in combinations(range(len(flags)),2):
            local=exact_source_overlap(2,flags,z)
            first,last=outer_dual_oracles(2,flags,z)
            self.assertEqual(local['outer_overlap'],first)
            self.assertEqual(first,last)

    def test_full_correlated_f_g_endbad_and_Z_intersections(self):
        for s,flags in self.gqs.items():
            cases=_cases(s,flags)
            for reverse in (False,True):
                f,g=labels(s,reverse)
                for name in ('empty','single','point-star','mixed-star',
                             'point-star-plus-one','full-original-I'):
                    with self.subTest(s=s,reverse=reverse,name=name):
                        z=cases[name]
                        val=label_endpoint_oracle(s,flags,z,f,g)
                        loc=exact_source_overlap(s,flags,z)
                        self.assertEqual(val['Z'],loc['touched_projections'])
                        self.assertEqual(val['X'],2*s*val['original_collinear_point_collisions'])
                        self.assertEqual(val['Y'],2*s*val['original_collinear_line_collisions'])
                        self.assertEqual(
                            val['endbad_union'],val['X']+val['Y']-val['XY'])
                        self.assertEqual(
                            val['physical_good_endpoint_total']+
                            val['physical_bad_endpoint_total'],
                            val['physical_total_offcoordinate_endpoints'])
                        self.assertLessEqual(val['Z_and_endbad'],val['Z'])

    def test_reject_duplicate_or_missing_original_ids_and_wrong_labels(self):
        f=self.gqs[2]
        for bad in ((0,0),(-1,), (len(f),), (True,),('0',)):
            with self.subTest(bad=bad),self.assertRaises(ValueError):
                exact_source_overlap(2,f,bad)
        with self.assertRaises(ValueError):
            exact_source_overlap(2,f[:-1],())
        with self.assertRaises(ValueError):
            exact_source_overlap(2,tuple([f[0]]+list(f[1:-1])+[f[0]]),())
        x,y=labels(2)
        with self.assertRaises(ValueError):
            label_endpoint_oracle(2,f,(),x,x[:1]*len(x))

    def test_finite_certificate_cannot_promote_root(self):
        report=canonical_certificate()
        self.assertEqual(report['schema'],SCHEMA)
        self.assertEqual(report['parent_pr'],772)
        self.assertFalse(report['root_PROVED_A'])
        self.assertTrue(report['prior_748_equivalent_union_identity_acknowledged'])
        self.assertEqual(report['finite_verified_orders'],[2,4])
        self.assertGreaterEqual(len(report['rows']),20)
        self.assertTrue(any(x['outer']>0 for x in report['rows']))

if __name__=='__main__':
    unittest.main()
