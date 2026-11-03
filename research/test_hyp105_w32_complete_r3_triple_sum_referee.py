"""AA4-FULLR3: exhaustive-in-principle true ORIGINAL GF5 triple sum audit.

All C(45,3)=14,190 original triples, paired by exact GF5^12 sum;
covers ALL C(45,6)=8,145,060 possible six-original-flag choices.
Small control independently enumerates actual sixsets x ten balanced signs.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json
import unittest

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_original_gf5_deterministic_extraction_referee import PALETTES
from hyp105_w32_sevenclass_global_deterministic_gf5_referee import (
    true_original_w32_seven_hypergraph,
    hypergraph_direct_event_census,
    _source_palette_by_id,
)
from hyp105_w32_complete_r3_triple_sum_referee import (
    N_FLAGS,N_TRIPLES,N_SEXTUPLES,_field_sum,
    _sums_by_cardinality,_direct_signed_six_column_check,
    _sextuple_degree_profile,
    committed_sevenclass_indices,true_original_source_vectors,
    full_original_r3_triple_hash_census,
    independent_small_universe_brute_3v3,
    independent_small_universe_hash_3v3,
)


class IndependentCompleteOriginalW32R3(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.seven={scheme:true_original_w32_seven_hypergraph(scheme)
                   for scheme in ("lex","reverse-line")}
        cls.saved=committed_sevenclass_indices()

    def test_exact_all_six_original_flag_universe_and_saved_palettes(self):
        self.assertEqual(N_FLAGS,45)
        self.assertEqual(N_TRIPLES,14190)
        self.assertEqual(N_SEXTUPLES,8145060)
        self.assertEqual(len(PALETTES),51)
        for scheme,family in self.seven.items():
            with self.subTest(scheme=scheme):
                self.assertEqual(len(self.saved[scheme]),45)
                vectors=true_original_source_vectors(
                    family["source"],self.saved[scheme])
                self.assertEqual(len(set(vectors)),45)
                self.assertEqual(len(vectors),45)
                self.assertTrue(all(len(v)==12 and
                    sum(v)%5==4 and
                    sum(bool(x) for x in v)==4 for v in vectors))
                self.assertEqual(len(family["source"]["incidences"]),45)
                self.assertEqual(len(set(family["source"]["incidences"])),45)
                self.assertEqual(sum(1 for _ in combinations(range(45),6)),
                                 8145060)

    def test_seven_zero_is_independently_preserved_but_full_is_recomputed(self):
        for scheme,family in self.seven.items():
            with self.subTest(scheme=scheme):
                leading={m["ids"] for m in family["motifs"]}
                result=full_original_r3_triple_hash_census(
                    family["source"],self.saved[scheme],
                    leading_original_sixsets=leading)
                r=hypergraph_direct_event_census(family,{
                    i:PALETTES[t] for i,t in enumerate(self.saved[scheme])
                },independent_parity=True)
                self.assertEqual(result[
                    "actual_signed_events_in_seven_leading_family"],
                    r["actual_ten_sign_event_count"])
                self.assertEqual(r["actual_ten_sign_event_count"],0)
                self.assertEqual(result["source_flag_count"],45)
                self.assertEqual(result["all_original_three_subset_count"],14190)
                self.assertEqual(result[
                    "all_original_distinct_sixsets_implicitly_covered"],8145060)
                self.assertEqual(result[
                    "FULL_original_distinct_sixflag_3v3_signed_events"],
                    result["actual_signed_events_OUTSIDE_seven_family"])
                self.assertGreaterEqual(result[
                    "duplicate_equal_3_sum_pairs"],
                    result["FULL_original_distinct_sixflag_3v3_signed_events"])
                self.assertEqual(
                    result["all_45_original_source_0_to_3_subset_sums_unique"],
                    not any(result[k] for k in (
                        "duplicate_equal_1_sum_pairs",
                        "duplicate_equal_2_sum_pairs",
                        "duplicate_equal_3_sum_pairs",
                    )))
                for witness in result["sample_true_original_signed_event_witnesses"]:
                    plus=tuple(witness["positive_three_original_IDs"])
                    minus=tuple(witness["negative_three_original_IDs"])
                    self.assertTrue(_direct_signed_six_column_check(
                        true_original_source_vectors(
                            family["source"],self.saved[scheme]),plus,minus))
                    self.assertEqual(len(set(plus+minus)),6)
                    self.assertTrue(all(1 not in profile for profile in
                                      witness["original_coordinate_degree_profiles"]))

    def test_all_ones_positive_control_and_nonleading_profile_completeness(self):
        for scheme,family in self.seven.items():
            with self.subTest(scheme=scheme):
                all_ones=(PALETTES.index((1,1,1,1)),)*45
                leading={m["ids"] for m in family["motifs"]}
                result=full_original_r3_triple_hash_census(
                    family["source"],all_ones,
                    leading_original_sixsets=leading)
                accepted=hypergraph_direct_event_census(
                    family,{i:(1,1,1,1) for i in range(45)},
                    independent_parity=True)
                self.assertEqual(
                    result["actual_signed_events_in_seven_leading_family"],
                    accepted["actual_ten_sign_event_count"])
                self.assertEqual(
                    accepted["actual_ten_sign_event_count"],
                    96 if scheme=="lex" else 11)
                self.assertGreaterEqual(
                    result["FULL_original_distinct_sixflag_3v3_signed_events"],
                    accepted["actual_ten_sign_event_count"])
                self.assertEqual(result[
                    "actual_signed_events_OUTSIDE_seven_family"],
                    sum(result[
                        "other_coordinate_multiplicity_signed_event_profiles"].values()))

    def test_independent_direct_small_12_id_sixsets_vs_triple_hash(self):
        for scheme,family in self.seven.items():
            for kind,idx in (
                ("saved",self.saved[scheme]),
                ("all-ones",(PALETTES.index((1,1,1,1)),)*45),
                ("other-seed",_source_palette_by_id(scheme,7,45)),
            ):
                with self.subTest(scheme=scheme,kind=kind):
                    vec=true_original_source_vectors(family["source"],idx)
                    first_motif=next(m["ids"] for m in family["motifs"]
                                     if m["kind"]=="D6")
                    chosen=tuple(sorted(set(first_motif)
                           |set(i for i in range(45) if i not in first_motif) ))
                    # Exactly twelve distinct ORIGINAL IDs, guaranteed
                    # to contain a complete accepted source D6 motif.
                    universe=tuple(sorted(
                        set(first_motif)|set(
                            i for i in range(45) if i not in first_motif
                        ).intersection(set(range(45)))
                    ))[:12]
                    # A proper canonical selection of twelve that
                    # retains all six D6 owner IDs.
                    universe=tuple(sorted(first_motif+
                        tuple(i for i in range(45) if i not in first_motif)[:6]))
                    self.assertEqual(len(universe),12)
                    brute=independent_small_universe_brute_3v3(vec,universe)
                    hashed=independent_small_universe_hash_3v3(vec,universe)
                    self.assertEqual(brute,hashed)

    def test_historical_45_w32_weighted_witness_by_separate_full_triple_oracle(self):
        # Pre-existing G5-D 45-column full ASET witness is an INDEPENDENT
        # historical control; we do NOT misrepresent that existence as new.
        path=Path(__file__).with_name("hyp105_g5d_w32_45_witness.json")
        old=json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(len(old["columns"]),45)
        vectors=[]
        for col in old["columns"]:
            s=tuple(col["support"]);w=tuple(col["coefficients"])
            self.assertEqual(len(set(s)),4)
            self.assertEqual(len(w),4)
            self.assertEqual(sum(w)%5,4)
            v=[0]*12
            for i,value in zip(s,w):v[i]=value
            vectors.append(tuple(v))
        for k in (1,2,3):
            buckets,duplicates=_sums_by_cardinality(vectors,k)
            self.assertEqual(duplicates,0)
            self.assertEqual(len(buckets),(45,990,14190)[k-1])

    def test_bad_original_signature_and_malformed_signed_indices_rejected(self):
        m=self.seven["lex"]["source"]
        with self.assertRaises(ValueError):
            true_original_source_vectors(m,(0,)*44)
        with self.assertRaises(ValueError):
            true_original_source_vectors(m,(0,)*44+(-1,))
        vec=true_original_source_vectors(m,(0,)*45)
        with self.assertRaises(ValueError):
            _direct_signed_six_column_check(vec,(1,2),(3,4))
        with self.assertRaises(ValueError):
            _direct_signed_six_column_check(vec,(1,2,3),(3,4,5))
        with self.assertRaises(ValueError):
            full_original_r3_triple_hash_census(m,(0,)*45,max_witnesses=-1)


if __name__=="__main__":
    unittest.main()
