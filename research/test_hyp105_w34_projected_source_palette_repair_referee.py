"""Independent AA4-W34 source-preserving GF5 cross projection referee tests.

The principal adversarial property is exact:
    D3(with source i reassigned to t) - D3(old)
        == cross_histogram[t] - cross_histogram[old]
for ALL 51 source palettes t, checked by 51 FRESH W32 14,190-triple
GF5 sum enumerations, not a self-consistency test of the projection.

W34 genuine sources additionally check 24D projection decomposition,
full pair R2 baseline, source identity and fail-closed 12.6m budget.
"""
from itertools import combinations
from fractions import Fraction
import unittest

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_original_gf5_deterministic_extraction_referee import PALETTES
from hyp105_w32_complete_r3_triple_sum_referee import (
    committed_sevenclass_indices,
    _sums_by_cardinality,
    full_original_r3_triple_hash_census,
)
from hyp105_w34_external_triple_r3_referee import (
    BASE,DIGIT_POWERS,_add_four_digit_table,_packed_four_groups,
    exact_gf5_original_vectors,
    deterministic_original_checksum_palettes,
)
from hyp105_w34_projected_source_palette_repair_referee import (
    _subtract_to_gf5_palette,
    _real_original_source_support,
    _gf5_four_support_projection,
    _two_sum_collision_source_pairs,
    source_palette_51_exact_cross_histogram,
)


class OriginalW34ProjectedGF5SourceRepair(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.w32=pair_labeled_symplectic(1,"lex")
        cls.w34=pair_labeled_symplectic(2,"lex")
        cls.w32idx=committed_sevenclass_indices()["lex"]
        cls.w34idx=deterministic_original_checksum_palettes(
            cls.w34,seed=0)

    def test_original_source_GF5_four_coefficient_projection_is_bijective(self):
        for model,idx in ((self.w32,self.w32idx),
                          (self.w34,self.w34idx)):
            _,vectors=exact_gf5_original_vectors(model,idx)
            ng=model["m"]//4
            add=_add_four_digit_table()
            parts=_packed_four_groups(vectors)
            for source_id in (0,2,7,11,len(idx)-1):
                with self.subTest(s=model["s"],id=source_id):
                    out_lut,in_lut,out_coords,support=(
                        _gf5_four_support_projection(model,source_id))
                    self.assertEqual(len(out_coords),model["m"]-4)
                    self.assertEqual(len(set(support)),4)
                    self.assertEqual(support,
                                     _real_original_source_support(model,source_id))
                    self.assertEqual(len(out_lut),ng)
                    for triple in ((1,2,3),(10,11,12),(18,19,20)):
                        limbs=tuple(
                            add[BASE*add[BASE*parts[triple[0]][k]+
                                         parts[triple[1]][k]]+
                                parts[triple[2]][k]]
                            for k in range(ng))
                        outside=sum(out_lut[k][limbs[k]]
                                    for k in range(ng))
                        inside=sum(in_lut[k][limbs[k]]
                                   for k in range(ng))
                        direct=tuple(sum(vectors[j][d] for j in triple)%5
                                     for d in range(model["m"]))
                        expected_outside=sum(
                            direct[d]*5**k for k,d in enumerate(out_coords))
                        expected_inside=sum(
                            direct[d]*5**k for k,d in enumerate(support))
                        self.assertEqual(outside,expected_outside)
                        self.assertEqual(inside,expected_inside)

    def test_exact_original_GF5_51_palette_difference_reconstruction(self):
        subtract=_subtract_to_gf5_palette()
        self.assertEqual(len(subtract),625**2)
        bypattern={tuple(p):j for j,p in enumerate(PALETTES)}
        for x in range(625):
            for y in range(625):
                difference=tuple(((x//DIGIT_POWERS[k])%5-
                                  (y//DIGIT_POWERS[k])%5)%5
                                 for k in range(4))
                self.assertEqual(subtract[625*x+y],
                                 bypattern.get(difference,-1))

    def test_real_W32_FULL_all_51_candidate_delta_exact_independent(self):
        model=self.w32
        initial=self.w32idx
        oldvectors=exact_gf5_original_vectors(model,initial)[1]
        baseline=_sums_by_cardinality(oldvectors,3)[1]
        self.assertEqual(baseline,7)
        for source_id in (0,29):
            with self.subTest(source_id=source_id):
                projection=source_palette_51_exact_cross_histogram(
                    model,initial,source_id,max_other_triples=14190)
                self.assertEqual(projection["source_other_pair_count"],946)
                self.assertEqual(projection["source_other_triples_processed"],
                                 13244)
                self.assertEqual(
                    projection["cross_collision_count_current_palette"],
                    projection["all_51_exact_cross_counts"][initial[source_id]])
                self.assertEqual(len(projection["all_51_exact_cross_counts"]),51)
                self.assertTrue(projection["exact_full_source_no_sampling"])
                for t in range(51):
                    new=list(initial);new[source_id]=t
                    fresh=exact_gf5_original_vectors(model,new)[1]
                    full_independent=_sums_by_cardinality(fresh,3)[1]
                    expected=baseline+(
                        projection["all_51_exact_cross_counts"][t]-
                        projection["cross_collision_count_current_palette"])
                    self.assertEqual(
                        full_independent,expected,
                        msg=f"false exact local projection source {source_id}, palette {t}")

    def test_real_W34_original_425_flags_and_source_R2_pairs(self):
        model=self.w34
        self.assertEqual(model["N"],425)
        self.assertEqual(model["m"],28)
        self.assertEqual(len(set(model["incidences"])),425)
        self.assertEqual(len(self.w34idx),425)
        overlaps=_two_sum_collision_source_pairs(model,self.w34idx)
        self.assertEqual(len(overlaps),3)
        for left,right in overlaps:
            self.assertEqual(len(set(left+right)),4)
            self.assertTrue(all(0<=i<425 for i in left+right))
        # The real W34 R2 count is independent of source h=1 code.
        self.assertEqual(sum(1 for _ in combinations(range(425),2)),90100)
        self.assertEqual(sum(1 for _ in combinations(range(424),2)),89676)
        self.assertEqual(sum(1 for _ in combinations(range(424),3)),12614424)

    def test_source_partial_budget_and_illegal_IDs_fail_closed(self):
        model=self.w34
        indices=self.w34idx
        with self.assertRaises(ValueError):
            source_palette_51_exact_cross_histogram(
                model,indices,0,max_other_triples=14190)
        with self.assertRaises(ValueError):
            source_palette_51_exact_cross_histogram(
                model,indices,0,max_other_triples=-1)
        with self.assertRaises(ValueError):
            _real_original_source_support(model,425)
        with self.assertRaises(ValueError):
            _gf5_four_support_projection(model,425)


if __name__=="__main__":
    unittest.main()
