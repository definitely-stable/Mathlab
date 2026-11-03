"""AA4-W34EX independent lossless 12-byte GF5 triple radix source tests.

W32 controls re-prove frozen FULL true original risk 7/4 and zero
for two genuinely repaired 45-source certificates. W34 selected
original source IDs compare the new external radix exact 3-sum
algorithm against direct ALL six-ID x TEN sign equations on 28
physical GF5 coordinates.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json
import math
import unittest

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_w34_external_triple_r3_referee import (
    _add_four_digit_table,_packed_four_groups,
    _signature_from_grouped_add,_gf5_encoded,
    _write_bucket_id,_bucket_disjoint_pair_census,
    _decode_record_triple,_write_exact_original_triple_records,
    exact_gf5_original_vectors,exact_full_original_external_r3,
    deterministic_original_checksum_palettes,
    RECORD_BYTES,ORIGINAL_TRIPLE_CODE_BITS,W34_TRIPLES
)
from hyp105_w32_complete_r3_triple_sum_referee import (
    committed_sevenclass_indices,
    true_original_source_vectors,
    full_original_r3_triple_hash_census,
)


class ExactOriginalW34RadixReferee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.w32={s:pair_labeled_symplectic(1,s) for s in
                 ("lex","reverse-line")}
        cls.w34=pair_labeled_symplectic(2,"lex")

    def test_true_source_n_a_m_and_all_triple_space_capacity(self):
        m=self.w34
        self.assertEqual(m["s"],4)
        self.assertEqual(m["v"],85)
        self.assertEqual(m["N"],425)
        self.assertEqual(m["a"],14)
        self.assertEqual(m["m"],28)
        self.assertEqual(math.comb(425,3),12_704_100)
        self.assertEqual(W34_TRIPLES,12_704_100)
        self.assertEqual((5**28).bit_length(),66)
        self.assertLess((5**28)<<ORIGINAL_TRIPLE_CODE_BITS,1<<(RECORD_BYTES*8))
        ids,vec=exact_gf5_original_vectors(
            m,deterministic_original_checksum_palettes(m,seed=0))
        self.assertEqual(len(ids),425)
        self.assertEqual(len(set(m["incidences"])),425)
        self.assertEqual(len(vec),425)
        self.assertTrue(all(len(x)==28 and sum(x)%5==4 and
                            sum(bool(z) for z in x)==4 for x in vec))

    def test_original_lossless_packed_GF5_four_digit_12byte_roundtrip(self):
        for power,source in ((1,self.w32["lex"]),(2,self.w34)):
            with self.subTest(power=power):
                ids,v=exact_gf5_original_vectors(
                    source,deterministic_original_checksum_palettes(
                        source,seed=13),
                    source_ids=tuple(range(10)))
                parts=_packed_four_groups(v)
                add=_add_four_digit_table()
                self.assertEqual(len(parts),10)
                for trip in combinations(range(10),3):
                    left=_signature_from_grouped_add(
                        tuple(add[625*parts[trip[0]][q]+parts[trip[1]][q]]
                              for q in range(len(parts[0]))),
                        parts[trip[2]],add)
                    right=tuple(sum(v[i][q] for i in trip)%5
                                for q in range(source["m"]))
                    self.assertEqual(left,_gf5_encoded(right))
                    self.assertTrue(0<=_write_bucket_id(left)<256)
                    code=(trip[0]*10+trip[1])*10+trip[2]
                    record=(left<<ORIGINAL_TRIPLE_CODE_BITS)|code
                    self.assertEqual(len(record.to_bytes(12,"big")),12)
                    self.assertEqual(_decode_record_triple(record&(
                        (1<<ORIGINAL_TRIPLE_CODE_BITS)-1),10),trip)

    def test_exact_intersection_IE_includes_double_ID_overlap(self):
        n=7
        examples=((0,1,2),(0,1,3),(0,4,5),(3,4,6))
        codes=tuple((a*n+b)*n+c for a,b,c in examples)
        total,shared,disjoint=_bucket_disjoint_pair_census(codes,n)
        self.assertEqual(total,6)
        self.assertEqual(disjoint,1)
        self.assertEqual(shared,5)
        with self.assertRaises(AssertionError):
            _bucket_disjoint_pair_census((codes[0],codes[0]),n)

    def test_w32_old_seven_zero_does_not_prove_full_and_w32_new_full_zero(self):
        old=committed_sevenclass_indices()
        payload=json.loads(Path(__file__).with_name(
            "hyp105_w32_full_r3_original_45flag_certificates.json"
        ).read_text(encoding="utf-8"))
        for scheme,model in self.w32.items():
            with self.subTest(scheme=scheme):
                for indices,wanted in (
                    (old[scheme],7 if scheme=="lex" else 4),
                    (tuple(payload["schemes"][scheme][
                        "source_flag_ID_order_palette_indices"]),0),
                ):
                    ext=exact_full_original_external_r3(
                        model,indices,max_triples=14190,
                        max_bucket_bytes=2_000_000,max_witnesses=5)
                    history=full_original_r3_triple_hash_census(model,indices)
                    self.assertEqual(ext["source_legal_ORIGINAL_flag_ID_count"],45)
                    self.assertEqual(ext["all_source_triple_count"],14190)
                    self.assertEqual(ext["FULL_six_distinct_original_ID_3v3_signed_event_count"],
                                     wanted)
                    self.assertEqual(ext["FULL_six_distinct_original_ID_3v3_signed_event_count"],
                                     history["FULL_original_distinct_sixflag_3v3_signed_events"])
                    self.assertEqual(ext["equal_triples_sharing_original_ID_not_signed_R3"],
                                     history["overlapping_equal_triple_pairs_excluded_from_R3"])
                    self.assertEqual(ext["equal_sum_pairs_of_distinct_ORIGINAL_triples"],
                                     history["duplicate_equal_3_sum_pairs"])
                    self.assertEqual(ext["complete_source_GF5_zero_to_three_ASET"],
                                     history["all_45_original_source_0_to_3_subset_sums_unique"])
                    self.assertEqual(ext["all_source_sixsets_implicitly_covered"],
                                     math.comb(45,6))
                    self.assertEqual(ext["all_triples_exact_external_disk_records_processed"],
                                     14190)

    def test_W34_real_10_source_subsets_vs_independent_brute_3v3(self):
        model=self.w34
        all_indices=deterministic_original_checksum_palettes(model,seed=4)
        for source_ids in (tuple(range(10)),tuple(range(125,135)),
                           tuple(range(410,425))[:10]):
            with self.subTest(source_ids=source_ids):
                global_ids,v=exact_gf5_original_vectors(
                    model,all_indices,source_ids=source_ids)
                n=len(v)
                brute=0
                for six in combinations(range(n),6):
                    for plus_tail in combinations(six[1:],2):
                        pos=(six[0],)+plus_tail
                        neg=tuple(z for z in six if z not in pos)
                        if all((sum(v[z][q] for z in pos)
                                -sum(v[z][q] for z in neg))%5==0
                               for q in range(28)):
                            brute+=1
                ext=exact_full_original_external_r3(
                    model,all_indices,source_ids=source_ids,
                    max_triples=120,max_bucket_bytes=2_000_000)
                self.assertEqual(ext["FULL_six_distinct_original_ID_3v3_signed_event_count"],
                                 brute)
                self.assertEqual(ext["all_source_triple_count"],120)
                self.assertFalse(ext["all_425_original_flags_in_scope"])
                self.assertEqual(ext["all_source_sixsets_implicitly_covered"],
                                 math.comb(10,6))

    def test_allN_exact_R2_to_R3_shared_triple_identity_on_genuine_source(self):
        # For distinct full original columns:
        # equal triple pairs = genuine R3 + (N-4)*genuine R2.
        # This is a completely separate source-2sum census: it
        # crosschecks the duplicate-pair IE correction on real data.
        for scheme,m in self.w32.items():
            source=committed_sevenclass_indices()[scheme]
            z=exact_full_original_external_r3(
                m,source,max_triples=14190,
                max_bucket_bytes=2_000_000)
            self.assertTrue(z[
                "independent_original_R2_to_R3_overlap_identity_verified"])
            self.assertEqual(
                z["equal_sum_pairs_of_distinct_ORIGINAL_triples"],
                z["FULL_six_distinct_original_ID_3v3_signed_event_count"]+
                41*z["R2_signed_2v2_events_exact"])
        saved=json.loads(Path(__file__).with_name(
            "hyp105_w34_full_425flag_r3_seed0_certificates.json"
        ).read_text(encoding="utf-8"))
        self.assertEqual(saved["source_ORIGINAL_flag_count"],425)
        self.assertEqual(saved["true_original_triple_count"],12704100)
        self.assertEqual(saved["external_lossless_bytes"],152449200)
        self.assertFalse(saved["new_asymptotic_exponent_proved"])
        self.assertEqual(set(saved["schemes"]),{"lex","reverse-line"})
        expected={"lex":(86,3,1349,1263),"reverse-line":(96,1,517,421)}
        for scheme in expected:
            with self.subTest(scheme=scheme):
                R=saved["schemes"][scheme]["exact_complete_source_risk"]
                actual=(R["FULL_six_distinct_original_ID_3v3_signed_event_count"],
                        R["all_original_1_2_source_sum_checks"][
                            "two_source_sum_collisions"],
                        R["equal_sum_pairs_of_distinct_ORIGINAL_triples"],
                        R["equal_triples_sharing_original_ID_not_signed_R3"])
                self.assertEqual(actual,expected[scheme])
                self.assertEqual(actual[2],actual[0]+421*actual[1])
                self.assertEqual(actual[3],421*actual[1])
                self.assertEqual(R["peak_one_sorted_external_bucket_bytes"]<1_000_000,True)
                self.assertFalse(R["complete_source_GF5_zero_to_three_ASET"])
                self.assertTrue(R["all_425_original_flags_in_scope"])
                self.assertEqual(R["all_source_triple_count"],12704100)
                self.assertEqual(R["all_triples_exact_external_disk_records_processed"],
                                 12704100)

    def test_saved_real_W34_signed_witnesses_independently_satisfy_all_28_equations(self):
        stored=json.loads(Path(__file__).with_name(
            "hyp105_w34_full_425flag_r3_seed0_certificates.json"
        ).read_text(encoding="utf-8"))
        for scheme in ("lex","reverse-line"):
            with self.subTest(scheme=scheme):
                model=pair_labeled_symplectic(2,scheme)
                idx=deterministic_original_checksum_palettes(model,seed=0)
                ids,v=exact_gf5_original_vectors(model,idx)
                self.assertEqual(len(ids),425)
                samples=stored["schemes"][scheme][
                    "exact_complete_source_risk"][
                    "verified_independent_true_source_witnesses"]
                self.assertEqual(len(samples),8)
                for witness in samples:
                    pos=tuple(witness["positive_ORIGINAL_three"])
                    neg=tuple(witness["negative_ORIGINAL_three"])
                    six=tuple(witness["six_distinct_ORIGINAL_flag_IDs"])
                    self.assertEqual(tuple(sorted(pos+neg)),six)
                    self.assertEqual(len(set(six)),6)
                    self.assertEqual(
                        tuple(model["incidences"][z] for z in six),
                        tuple(tuple(x) for x in witness[
                            "actual_original_point_line_incidence_flags"]))
                    a=tuple(sum(v[z][k] for z in pos)%5 for k in range(28))
                    b=tuple(sum(v[z][k] for z in neg)%5 for k in range(28))
                    self.assertEqual(a,b)
                    self.assertEqual(a,tuple(witness[
                        "complete_GF5_physical_sum"]))
                    profiles=[]
                    for side,labels in ((0,model["left_labels"]),
                                        (1,model["right_labels"])):
                        degree=Counter(q for z in six
                                     for q in labels[model["incidences"][z][side]])
                        profiles.append(tuple(sorted(degree.values(),reverse=True)))
                    self.assertEqual(tuple(profiles),tuple(
                        tuple(x) for x in witness[
                        "two_original_physical_coordinate_profiles"]))
                    self.assertNotIn(1,profiles[0])
                    self.assertNotIn(1,profiles[1])

    def test_fail_closed_w34_and_never_return_partial_exact_risk(self):
        m=self.w34
        idx=deterministic_original_checksum_palettes(m)
        with self.assertRaises(ValueError):
            exact_gf5_original_vectors(m,idx[:-1])
        with self.assertRaises(ValueError):
            exact_gf5_original_vectors(m,idx,source_ids=(0,0))
        with self.assertRaises(ValueError):
            exact_full_original_external_r3(m,idx,max_triples=14190)
        with self.assertRaises(ValueError):
            exact_full_original_external_r3(
                m,idx,source_ids=tuple(range(10)),
                max_triples=120,max_bucket_bytes=11)
        with self.assertRaises(ValueError):
            deterministic_original_checksum_palettes(m,seed=-1)


if __name__=="__main__":
    unittest.main()
