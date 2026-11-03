"""AA4-W34-ALL1 independently validate accelerated exhaustive source checker.

The C++ GF(5) full-source pair/triple projection is NEVER accepted
merely because it agrees with its own 51-way histogram. On true W32,
compare every source palette directly to 51 independently rebuilt
45-original-column complete GF(5) physical 990 pair and 14190 triple
collision censuses. Also validate the original 3+3 signed orientation
and source ID membership on each current true signed event.

The full W34 matrix and full candidate acceptance are independently
verified by its GitHub-hosted 16-worker / 2-aggregator scientific CI.
"""
from collections import Counter
from pathlib import Path
import json
import subprocess
import tempfile
import unittest

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_w32_complete_r3_triple_sum_referee import (
    committed_sevenclass_indices,full_original_r3_triple_hash_census,
)
from hyp105_w34_external_triple_r3_referee import (
    exact_full_original_external_r3,
)
from hyp105_w34_oneexchange_exhaustive_referee import (
    construct_exact_source_text,_derive_all_true_signed_original_degrees,
    _normalize_exact_shard_source,SCHEMA,
    frozen_complete_W34_sources,
)
from hyp105_w34_projected_source_palette_repair_referee import (
    _two_sum_collision_source_pairs,
)
from hyp105_w34_external_triple_r3_referee import (
    exact_gf5_original_vectors,
)
from hyp105_w34_direct_r3_palette_derivative_referee import (
    all_51_direct_R3_derivative,
)


class AcceleratedExhaustiveOriginalSourceOneExchange(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model=pair_labeled_symplectic(1,"lex")
        cls.indices=committed_sevenclass_indices()["lex"]
        cls.full=exact_full_original_external_r3(
            cls.model,cls.indices,max_triples=14190,max_witnesses=20)
        cls.expected=(
            cls.full["R2_signed_2v2_events_exact"],
            cls.full["equal_sum_pairs_of_distinct_ORIGINAL_triples"],
            cls.full[
                "FULL_six_distinct_original_ID_3v3_signed_event_count"])
        cls.degree=dict(_derive_all_true_signed_original_degrees(
            cls.full["verified_independent_true_source_witnesses"],
            cls.expected[2],45))
        cls.test_ids=(0,29)
        cls.tmp=tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.tmp.cleanup)
        cls.exe=Path(cls.tmp.name)/"hyp105-exact-oneexchange"
        cpp=Path(__file__).with_name("hyp105_w34_oneexchange_exact.cpp")
        subprocess.run(["g++","-O3","-std=c++17","-Wall","-Wextra",
                        "-pedantic",str(cpp),"-o",str(cls.exe)],
                       check=True,capture_output=True,text=True)
        cls.source_text=construct_exact_source_text(
            cls.model,cls.indices,cls.full,
            tuple((i,cls.degree.get(i,0)) for i in cls.test_ids))
        cls.input=Path(cls.tmp.name)/"true-W32-original.txt"
        cls.input.write_text(cls.source_text,encoding="utf-8")
        cls.output=Path(cls.tmp.name)/"true-W32-output.json"
        subprocess.run([str(cls.exe),str(cls.input),"0","1",
                        str(cls.output)],check=True,
                       capture_output=True,text=True)
        cls.report=json.loads(cls.output.read_text(encoding="utf-8"))

    def test_real_source_all_51_accurate_against_independent_original_full_census(self):
        p=self.report
        self.assertEqual(p["schema"],
                         "mathlab.hyp105.original-w34-active-oneexchange-v1")
        self.assertEqual(p["scheme"],"lex")
        self.assertEqual((p["n"],p["m"]),(45,12))
        self.assertEqual(tuple(p[k] for k in
                         ("original_D2","original_D3","original_R3")),
                         self.expected)
        self.assertEqual(len(p["results"]),2)
        for row in p["results"]:
            sid=row["source_ID"]
            with self.subTest(source_id=sid):
                self.assertIn(sid,self.test_ids)
                self.assertEqual(row["witness_degree"],
                                 self.degree.get(sid,0))
                self.assertEqual(row["current_palette"],
                                 self.indices[sid])
                self.assertEqual(len(row["H_R3_all_51"]),51)
                self.assertEqual(len(row["H_R2_all_51"]),51)
                self.assertEqual(row["current_true_R3_incidence"],
                                 self.degree.get(sid,0))
                for t in range(51):
                    altered=list(self.indices);altered[sid]=t
                    # A DIFFERENT unmodified exact full original GF5 3sum
                    # scanner independently checks the new C++ oracle.
                    fresh=full_original_r3_triple_hash_census(
                        self.model,tuple(altered),max_witnesses=0)
                    actual_r2=fresh["duplicate_equal_2_sum_pairs"]
                    actual_d3=fresh["duplicate_equal_3_sum_pairs"]
                    actual_r3=fresh[
                        "FULL_original_distinct_sixflag_3v3_signed_events"]
                    self.assertEqual(
                        self.expected[2]+row["H_R3_all_51"][t]-
                        row["H_R3_all_51"][self.indices[sid]],actual_r3)
                    self.assertEqual(
                        self.expected[0]+row["H_R2_all_51"][t]-
                        row["H_R2_all_51"][self.indices[sid]],actual_r2)
                    self.assertEqual(actual_d3,actual_r3+41*actual_r2)

    def test_python_all_51_projection_oracle_agrees_with_independent_CPP(self):
        for row in self.report["results"]:
            source=row["source_ID"]
            with self.subTest(source=source):
                old=all_51_direct_R3_derivative(
                    self.model,self.indices,source,
                    baseline_D2=self.expected[0],
                    baseline_D3=self.expected[1],
                    max_other_triples=13244)
                for t,prior in enumerate(old[
                        "exact_all_51_source_palette_candidates"]):
                    self.assertEqual(
                        prior["predicted_exact_true_R3"],
                        self.expected[2]+row["H_R3_all_51"][t]-
                        row["current_true_R3_incidence"])
                    self.assertEqual(
                        prior["predicted_exact_D2"],
                        self.expected[0]+row["H_R2_all_51"][t]-
                        row["current_R2_cross_incidence"])

    def test_real_source_full_signed_witness_degrees_and_inactive_prune(self):
        self.assertEqual(self.expected[2],7)
        self.assertEqual(sum(self.degree.values()),42)
        self.assertTrue(all(0<=i<45 and 0<d<=7
                            for i,d in self.degree.items()))
        for row in self.report["results"]:
            if row["witness_degree"]==0:
                # For every legal candidate, H_i(t)>=0, so a source
                # not in current events CANNOT strictly improve R3.
                self.assertGreaterEqual(min(row["H_R3_all_51"]),0)
                self.assertEqual(row["current_true_R3_incidence"],0)

    def test_permanent_all_519_active_original_sources_exact_CI_certificate(self):
        # Scientific review of the permanent independent CI-derived
        # FULL W34 source arrays, NOT a self-test of the fast C++
        # one-exchange projected algorithm or its original shard output.
        path=Path(__file__).with_name(
            "hyp105_w34_all_active_oneexchange_certificates.json")
        cert=json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(cert["scientific_parent_exact_SHA"],
                         "b2d848270980585904fe7c00676dc70bcf7001be")
        self.assertEqual(cert["full_hosted_run_id"],41647811306)
        self.assertEqual(cert["complete_artifact_id"],13236088070)
        self.assertEqual(cert["complete_artifact_sha256"],
                         "67b1443f83af8bbd6856afcac9ed3cb4ab7c479ef15ab9868ac0e5ec57871f51")
        self.assertEqual(cert["total_all_active_original_source_variables"],519)
        self.assertEqual(cert["total_all_51_exact_source_candidates"],26469)
        self.assertFalse(cert["root_all_h_mathematical_theorem_proved"])
        self.assertTrue(cert["all_425_true_original_flags_in_scope_per_scheme"])
        self.assertTrue(cert["no_source_pair_maps_changed"])
        self.assertEqual(set(cert["schemes"]),{"lex","reverse-line"})
        prior=frozen_complete_W34_sources()
        expected={
            "lex":((1,483,62),(1,479,58),247,372,(136,8,10),
                   {"1":158,"2":62,"3":18,"4":9},148),
            "reverse-line":((0,69,69),(0,65,65),272,414,(270,22,0),
                            {"1":168,"2":74,"3":22,"4":8},182),
        }
        for scheme,z in cert["schemes"].items():
            with self.subTest(scheme=scheme):
                initial,after,active,degree,edit,distribution,rejected=expected[scheme]
                old=tuple(z["frozen_original_GF5_before_source_palette_indices"])
                revised=tuple(z["full_original_425_GF5_after_source_palette_indices"])
                self.assertEqual(len(old),len(revised))
                self.assertEqual(len(old),425)
                self.assertEqual(old,tuple(prior["schemes"][scheme][
                    "all_425_ORIGINAL_ID_ordered_GF5_palette_indices"]))
                self.assertEqual(tuple(z["before_FULL_D2_D3_TRUE_R3"]),initial)
                self.assertEqual(tuple(z[
                    "after_independently_rehashed_FULL_D2_D3_TRUE_R3"]),after)
                self.assertEqual(z["all_active_original_IDs_examined"],active)
                self.assertEqual(z[
                    "total_original_signed_witness_source_incidence_degrees"],degree)
                self.assertEqual(z["strict_improving_active_source_count"],active)
                self.assertEqual(z[
                    "strict_R3_improvement_source_count_histogram"],distribution)
                self.assertEqual(sum(distribution.values()),active)
                self.assertEqual(z["R2_guarded_rejected_candidate_combinations"],
                                 rejected)
                self.assertTrue(z[
                    "all_51_palette_variants_per_active_ID_verified"])
                self.assertFalse(z["one_exchange_local_minimum_at_prior_source"])
                self.assertTrue(z["remaining_signed_original_R3_not_zero"])
                self.assertTrue(z[
                    "full_12704100_original_three_source_GF5_physical_census_independently_rechecked"])
                change=z["actual_one_source_edit"]
                self.assertEqual((
                    change["original_source_flag_ID"],
                    change["prior_legal_checksum4_palette_index"],
                    change["new_legal_checksum4_palette_index"]),edit)
                self.assertEqual(change["full_signed_R3_improvement"],4)
                self.assertEqual(
                    {i for i in range(425) if old[i]!=revised[i]}, {edit[0]})
                self.assertEqual((old[edit[0]],revised[edit[0]]),
                                 (edit[1],edit[2]))
                model=pair_labeled_symplectic(2,scheme)
                _,vec=exact_gf5_original_vectors(model,revised)
                self.assertEqual(len(set(vec)),425)
                self.assertTrue(all(len(x)==28 and sum(x)%5==4 and
                     sum(bool(v) for v in x)==4 for x in vec))
                self.assertEqual(
                    len(_two_sum_collision_source_pairs(model,revised)),after[0])
                # This independent referee NEVER invokes the optimized
                # C++ source-local exact candidate scanner. All
                # C(425,3)=12,704,100 physical GF5 triples are freshly
                # enumerated, with separate source-overlap exclusion.
                full=exact_full_original_external_r3(
                    model,revised,max_triples=12704100,max_witnesses=8)
                self.assertEqual((
                    full["R2_signed_2v2_events_exact"],
                    full["equal_sum_pairs_of_distinct_ORIGINAL_triples"],
                    full["FULL_six_distinct_original_ID_3v3_signed_event_count"]),
                    after)
                self.assertTrue(full[
                    "independent_original_R2_to_R3_overlap_identity_verified"])
                self.assertEqual(full[
                    "all_triples_exact_external_disk_records_processed"],
                    12704100)
                for witness in full[
                        "verified_independent_true_source_witnesses"]:
                    plus=tuple(witness["positive_ORIGINAL_three"])
                    minus=tuple(witness["negative_ORIGINAL_three"])
                    self.assertEqual(len(set(plus+minus)),6)
                    self.assertTrue(all(
                        sum(vec[i][j] for i in plus)%5==
                        sum(vec[i][j] for i in minus)%5
                        for j in range(28)))

    def test_bad_original_flag_context_fails_closed_before_any_output(self):
        wrong=Path(self.tmp.name)/"broken-original.txt"
        data=self.source_text.splitlines()
        first=data[1].split()
        first[0]="5"  # illegal original source GF5 physical digit
        data[1]=" ".join(first)
        wrong.write_text("\n".join(data)+"\n",encoding="utf-8")
        p=subprocess.run([str(self.exe),str(wrong),"0","1",
                          str(self.tmp.name+"/bad.json")],
                         capture_output=True,text=True)
        self.assertNotEqual(p.returncode,0)
        self.assertIn("FAIL CLOSED",p.stderr)
        with self.assertRaises(ValueError):
            construct_exact_source_text(
                self.model,self.indices[:-1],self.full,
                ((0,0),))


if __name__=="__main__":
    unittest.main()
