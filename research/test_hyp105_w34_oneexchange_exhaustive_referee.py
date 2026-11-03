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
