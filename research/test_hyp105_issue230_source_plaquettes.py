"""EICE-003-E: true ORIGINAL W32/W34 plaquettes and independent girth audits."""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
import unittest

from hyp105_issue230_endpoint_energy import EndpointEnergy
from hyp105_issue230_nb_rectangles import OriginalNBRectangle
from hyp105_issue230_paired_gstar import paired_gstar
from hyp105_issue230_projection import fixture
from hyp105_issue230_source_plaquettes import (
    STATUS, OriginalPlaquette, all_four_count, report,
    source_girth_four_by_four, status_of_cell,
)


class OriginalPlaquetteTests(unittest.TestCase):
    def source(self,power,scheme):
        model=fixture(power,scheme)
        paired=paired_gstar(model,verify_paths=True)
        return model,paired,OriginalPlaquette(
            model,paired['original_incidence_ids'],
            paired['colors_left'],paired['colors_right'])

    def test_four_true_W32_schemes_exact_status_partition_with_prior_path_oracle(self):
        for scheme in ('lex','reverse','S68','S72'):
            with self.subTest(scheme=scheme):
                model,paired,oracle=self.source(1,scheme)
                row=oracle.census(independent_paths=True,independent_plaquettes=True)
                old=OriginalNBRectangle(
                    model,paired['original_incidence_ids'],
                    paired['colors_left'],paired['colors_right']).census()
                self.assertEqual(Fraction(row['internally_blocked_end_clean_weight']),
                                 Fraction(old['theta_internal_only']))
                self.assertEqual(Fraction(row['missing_original_endpoint_weight']),
                                 Fraction(old['D5_either_original_endpoint_absent_mass']))
                self.assertEqual(sum((Fraction(v) for v in
                    row['original_nb_path_status_weight'].values()),Fraction()),1)
                self.assertEqual(
                    Fraction(row['original_nb_path_status_weight'][STATUS[3]])+
                    Fraction(row['original_nb_path_status_weight'][STATUS[4]]),
                    Fraction(old['eligible_end_clean_mass']))
                self.assertFalse(row['source_gf5_sixset_from_cross_pairs_proved'])
                self.assertFalse(row['universal_branch_A_proved'])
                self.assertLessEqual(row['original_endpoint_complete_plaquettes'],
                                     row['total_2x2_plaquettes'])
                self.assertEqual(sum(row['original_cross_incidence_histogram'].values()),
                                 row['original_endpoint_complete_plaquettes'])
                self.assertTrue(all(int(k)<=8 for k in
                                    row['original_cross_incidence_histogram']))

    def test_original_W34_lex_random_and_strict_first_source_provenance(self):
        for scheme in ('lex','random'):
            with self.subTest(scheme=scheme):
                model,paired,oracle=self.source(2,scheme)
                row=oracle.census(max_paths=500_000,max_plaquettes=100_000)
                self.assertEqual(row['N'],425)
                self.assertEqual(row['original_middle_source_count'],
                                 paired['final_original_count'])
                self.assertEqual(row['physical_edges'],2*paired['final_original_count'])
                self.assertLessEqual(row['original_endpoint_complete_plaquettes'],
                                     row['total_2x2_plaquettes'])

    def test_sharp_grid_plaquette_missing_original_pair_incidence_charge(self):
        # Pure combinatorial grid witness: one undefined source label
        # removes exactly (r-1)(c-1) out of C(r,2)*C(c,2) squares.
        r,c=5,6
        grid=[[4]*c for _ in range(r)]
        total=r*(r-1)//2*c*(c-1)//2
        self.assertEqual(all_four_count(grid,{4}),total)
        grid[0][0]=0
        self.assertEqual(all_four_count(grid,{4}),total-(r-1)*(c-1))
        self.assertGreaterEqual(Fraction(all_four_count(grid,{4}),total),
                                1-Fraction(4,r*c))
        self.assertEqual(all_four_count([[3,3],[3,3]],{3}),1)
        self.assertEqual(all_four_count([[4,3],[4,3]],{3}),0)
        with self.assertRaisesRegex(ValueError,'nonrectangular'):
            all_four_count([[3,4],[3]],{3})

    def test_TRUE_original_W32_girth8_eight_cycle_attains_eight_cross_edges(self):
        # Find a GQ incidence C8, not an ordinary physical K4 square.
        ctx=EndpointEnergy(fixture(1,'lex'))
        found=None
        for p0 in range(ctx.v):
            if found:break
            for l0,l3 in permutations(sorted(ctx.point_lines[p0]),2):
                if found:break
                for p1 in sorted(ctx.line_points[l0]-{p0}):
                    if found:break
                    for l1 in sorted(ctx.point_lines[p1]-{l0,l3}):
                        if found:break
                        for p2 in sorted(ctx.line_points[l1]-{p0,p1}):
                            if found:break
                            for l2 in sorted(ctx.point_lines[p2]-{l0,l1,l3}):
                                if found:break
                                for p3 in sorted(ctx.line_points[l2]-{p0,p1,p2}):
                                    if l3 in ctx.point_lines[p3]:
                                        found=(p0,p1,p2,p3),(l0,l1,l2,l3)
                                        break
        self.assertIsNotNone(found)
        geom=source_girth_four_by_four(*found,ctx.edge_id)
        self.assertEqual(geom['original_cross_incidence_count'],8)
        self.assertEqual(geom['original_cross_nonincidence_count'],8)

    def test_original_four_by_four_girth_tight_and_forbidden_C4_C6(self):
        pts=range(4)
        lines=range(4)
        eight={(0,0),(1,0),(1,1),(2,1),
               (2,2),(3,2),(3,3),(0,3)}
        out=source_girth_four_by_four(pts,lines,eight)
        self.assertEqual(out['original_cross_incidence_count'],8)
        with self.assertRaisesRegex(AssertionError,'four-cycle|six-cycle'):
            source_girth_four_by_four(pts,lines,eight|{(0,1)})
        with self.assertRaisesRegex(AssertionError,'four-cycle'):
            source_girth_four_by_four(pts,lines,
                                     {(0,0),(0,1),(1,0),(1,1)})
        with self.assertRaisesRegex(ValueError,'DISTINCT'):
            source_girth_four_by_four([0,0,2,3],lines,eight)

    def test_count_complete_plaquette_cross_incidence_cap_independent_girth_logic(self):
        # Exhaust all 2^16 potential ORIGINAL bipartite 4x4 incidence
        # patterns, using a separate direct C4/C6 detector.
        max_girth8=0
        max_girth6=0
        witnessed=0
        for mask in range(1<<16):
            n=mask.bit_count()
            if n<8:
                continue
            rows=[(mask>>(4*i))&15 for i in range(4)]
            c4=any((rows[i]&rows[j]).bit_count()>=2
                   for i,j in combinations(range(4),2))
            if c4:
                continue
            max_girth6=max(max_girth6,n)
            c6=False
            for p0,p1,p2 in combinations(range(4),3):
                for l0,l1,l2 in permutations(range(4),3):
                    if all(rows[p]&(1<<l) for p,l in
                           ((p0,l0),(p0,l1),(p1,l1),
                            (p1,l2),(p2,l2),(p2,l0))):
                        c6=True
                        break
                if c6:break
            if not c6:
                max_girth8=max(max_girth8,n)
                witnessed+=1
        self.assertEqual(max_girth6,9)   # C4-free alone insufficient!
        self.assertEqual(max_girth8,8)   # ORIGINAL GQ has girth >=8
        self.assertGreater(witnessed,0)

    def test_invalid_source_and_budgets_fail_closed(self):
        model,paired,oracle=self.source(1,'lex')
        with self.assertRaisesRegex(ValueError,'path budget'):
            oracle.census(max_paths=0)
        with self.assertRaisesRegex(ValueError,'plaquette budget'):
            oracle.census(max_plaquettes=-1)
        with self.assertRaisesRegex(ValueError,'complete ORIGINAL NB path budget'):
            oracle.census(max_paths=1)
        with self.assertRaisesRegex(ValueError,'bichromatic'):
            OriginalPlaquette(model,paired['original_incidence_ids'],
                              [0]*model['a'],paired['colors_right'])
        bad=fixture(1,'lex')
        bad['right_labels']=list(bad['right_labels'])
        bad['right_labels'][0]=bad['right_labels'][1]
        with self.assertRaisesRegex(ValueError,'global injective'):
            OriginalPlaquette(bad,paired['original_incidence_ids'],
                              paired['colors_left'],paired['colors_right'])

    def test_report_research_only_no_GQ_to_GF5_leap(self):
        data=report()
        self.assertEqual(data['status'],'RESTRICTED_THEOREM_C')
        self.assertEqual(data['root_A'],'OPEN')
        self.assertEqual(len(data['rows']),4)
        self.assertTrue(all(not row.get('universal_branch_A_proved',False)
                            for row in data['rows']))


if __name__=='__main__':
    unittest.main()
