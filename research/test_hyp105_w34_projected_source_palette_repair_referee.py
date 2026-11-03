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
from pathlib import Path
import json
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

    def test_saved_full_W34_425_original_source_repair_certificates(self):
        # FROZEN independent full 12,704,100-triple CI results, not just
        # desired local improvement or source-projection self-consistency.
        path=Path(__file__).with_name(
            "hyp105_w34_r2first_repaired_source_certificates.json")
        payload=json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(payload["true_ORIGINAL_flags"],425)
        self.assertEqual(payload["physical_GF5_coordinates"],28)
        self.assertEqual(payload["full_source_triples_checked_per_scheme"],12704100)
        self.assertTrue(payload["source_original_geometry_unchanged"])
        self.assertFalse(payload["new_asymptotic_exponent_proved"])
        self.assertFalse(payload["full_0to3_ASET_found"])
        self.assertEqual(set(payload["schemes"]),{"lex","reverse-line"})
        expected={
            "lex":{"prior":(3,1349,86),"after":(1,507,86),"ids":(45,143)},
            "reverse-line":{"prior":(1,517,96),"after":(0,96,96),"ids":(184,)},
        }
        for scheme,c in payload["schemes"].items():
            with self.subTest(scheme=scheme):
                want=expected[scheme]
                self.assertEqual(
                    (c["original_full_D2_before"],c["original_full_D3_before"],
                     c["original_full_signed_R3_before"]),want["prior"])
                self.assertEqual(
                    (c["new_exact_full_source_R2"],c["new_exact_full_source_D3"],
                     c["new_exact_full_source_signed_R3"]),want["after"])
                self.assertEqual(
                    tuple(x["original_source_id"] for x in
                          c["accepted_true_original_source_changes"]),
                    want["ids"])
                self.assertEqual(c["evaluated_original_source_IDs"],
                                 list(want["ids"]))
                self.assertTrue(c[
                    "all_12_704_100_original_triples_independently_rechecked"])
                self.assertFalse(c["full_0_to_3_ASET_success"])
                self.assertEqual(len(c["all_425_ORIGINAL_flag_palette_indices"]),425)
                self.assertEqual(c["new_exact_full_source_D3"]-421*
                                 c["new_exact_full_source_R2"],
                                 c["new_exact_full_source_signed_R3"])
                # Do NOT falsely equate a strict D3 improvement to R3:
                # here all improvement came from lifted R2 overlap pairs.
                self.assertEqual(
                    c["original_full_D3_before"]-c["new_exact_full_source_D3"],
                    421*(c["original_full_D2_before"]-
                         c["new_exact_full_source_R2"]))
                model=pair_labeled_symplectic(2,scheme)
                original=deterministic_original_checksum_palettes(
                    model,seed=0)
                revised=tuple(c["all_425_ORIGINAL_flag_palette_indices"])
                differing=tuple(i for i,(x,y) in enumerate(zip(original,revised))
                                if x!=y)
                self.assertEqual(set(differing),set(want["ids"]))
                self.assertEqual(len(_two_sum_collision_source_pairs(
                    model,revised)),want["after"][0])
                _,vec=exact_gf5_original_vectors(model,revised)
                self.assertEqual(len(vec),425)
                self.assertEqual(len(set(vec)),425)
                self.assertTrue(all(sum(v)%5==4 and
                                    sum(bool(x) for x in v)==4 for v in vec))
                # Independent direct 28-coordinate verification of
                # actual six distinct ORIGINAL source witnesses.
                for sample in c["full_original_exact_signed_witnesses"]:
                    pos=tuple(sample["six_distinct_ORIGINAL_flag_IDs"])
                    plus=tuple(sample["positive_ORIGINAL_three"])
                    minus=tuple(sample["negative_ORIGINAL_three"])
                    self.assertEqual(tuple(sorted(plus+minus)),pos)
                    self.assertEqual(len(set(pos)),6)
                    left=tuple(sum(vec[i][k] for i in plus)%5
                               for k in range(28))
                    right=tuple(sum(vec[i][k] for i in minus)%5
                                for k in range(28))
                    self.assertEqual(left,right)
                    self.assertEqual(left,tuple(
                        sample["complete_GF5_physical_sum"]))

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
