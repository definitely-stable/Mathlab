"""Separate direct GF5 equations versus hosted C++ exhaustive frozen fibers.

True original W(3,2), 45 complete original flags, 12 GF5 physical
coordinates; freeze 11 genuine source IDs. Independently brute-force
all source-disjoint (1+2) and (2+3) pair/triple witnesses in the frozen
core for ALL 34 remaining original source IDs, ALL 51 legal patterns.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json
import subprocess
import tempfile
import unittest

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_original_gf5_deterministic_extraction_referee import PALETTES
from hyp105_w34_external_triple_r3_referee import (
    deterministic_original_checksum_palettes,exact_gf5_original_vectors)


def input_w32():
    model=pair_labeled_symplectic(1,"lex")
    indices=deterministic_original_checksum_palettes(model,seed=3)
    ids,columns=exact_gf5_original_vectors(model,indices)
    assert (model["s"],model["N"],model["m"])==(2,45,12)
    assert ids==tuple(range(45))
    a=model["a"]
    supports=[]
    for p,l in model["incidences"]:
        supports.append((model["left_labels"][p][0],
                         model["left_labels"][p][1],
                         a+model["right_labels"][l][0],
                         a+model["right_labels"][l][1]))
    edited=tuple(range(11,45))
    frozen=tuple(range(11))
    rows=[f"HYP105_FROZEN_CORE_V1 lex 45 12 {len(edited)}"]
    for i in range(45):
        rows.append(" ".join(map(str,(indices[i],*supports[i],*columns[i]))))
    rows.extend(" ".join(map(str,p)) for p in PALETTES)
    rows.append(" ".join(map(str,edited)))
    return "\n".join(rows)+"\n",columns,supports,edited,frozen


def direct_full_GF5_histogram(columns,support,edited_id,F):
    all_pal={}
    for idx,p in enumerate(PALETTES):
        v=[0]*len(columns[0])
        for pos,value in zip(support,p):
            v[pos]=value
        all_pal[tuple(v)]=idx
    count2=[0]*51
    count3=[0]*51
    m=len(columns[0])
    for k,hist in ((2,count2),(3,count3)):
        for pos in combinations(F,k-1):
            out=tuple(x for x in F if x not in pos)
            signed_A=tuple(sum(columns[i][j] for i in pos)%5
                           for j in range(m))
            for neg in combinations(out,k):
                needed=tuple((sum(columns[i][j] for i in neg)-
                              signed_A[j])%5 for j in range(m))
                index=all_pal.get(needed)
                if index is not None:hist[index]+=1
    return count2,count3


class RealOriginalFrozenCoreW32Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.directory=tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.root=Path(cls.directory.name)
        cpp=Path(__file__).with_name("hyp105_w34_frozen_core_palette.cpp")
        cls.exe=cls.root/"frozen-source"
        build=subprocess.run(
            ["g++","-O3","-std=c++17","-Wall","-Wextra",
             str(cpp),"-o",str(cls.exe)],
            capture_output=True,text=True,timeout=120)
        if build.returncode:
            raise AssertionError(build.stderr[-5000:])
        cls.input,cls.columns,cls.supports,cls.edited,cls.frozen=input_w32()
        cls.source=cls.root/"true-w32-input.txt"
        cls.output=cls.root/"w32-report.json"
        cls.source.write_text(cls.input,encoding="utf-8")
        run=subprocess.run([str(cls.exe),str(cls.source),
                            str(cls.output),"0","1"],
                           capture_output=True,text=True,timeout=100)
        if run.returncode:
            raise AssertionError(run.stderr[-5000:])
        cls.report=json.loads(cls.output.read_text(encoding="utf-8"))

    def test_complete_true_original_W32_fixed_core_direct_GF5_reference(self):
        z=self.report
        self.assertEqual(z["schema"],
                         "mathlab.hyp105.original-frozen-core-fibers.v1")
        self.assertEqual((z["scheme"],z["n"],z["m"]),("lex",45,12))
        self.assertEqual(z["edited_original_IDs"],list(self.edited))
        self.assertEqual(len(z["results"]),len(self.edited))
        self.assertEqual(z["frozen_original_ID_count"],len(self.frozen))
        for row in z["results"]:
            i=row["source_ID"]
            self.assertIn(i,self.edited)
            self.assertEqual(row["frozen_pairs_processed"],55)
            self.assertEqual(row["frozen_triples_processed"],165)
            left,right=direct_full_GF5_histogram(
                self.columns,self.supports[i],i,self.frozen)
            self.assertEqual(
                [v["R2_fixed_core_count"] for v in row["patterns"]],left)
            self.assertEqual(
                [v["R3_fixed_core_count"] for v in row["patterns"]],right)
            self.assertEqual(
                row["allowed_palettes"],
                [j for j in range(51) if not(left[j]+right[j])])
            self.assertEqual(row["blocked_count"],51-len(row["allowed_palettes"]))

    def test_every_emitted_witness_is_real_disjoint_full_GF5(self):
        for row in self.report["results"]:
            i=row["source_ID"]
            for p in row["patterns"]:
                forbidden=p["forbidden"]
                self.assertEqual(forbidden,
                    p["R2_fixed_core_count"]+p["R3_fixed_core_count"]>0)
                if not forbidden:continue
                k=p["witness_k"]
                plus=p["positive_original_IDs"]
                minus=p["negative_original_IDs"]
                self.assertEqual(plus[0],i)
                self.assertEqual(len(plus),k)
                self.assertEqual(len(minus),k)
                self.assertEqual(len(set(plus+minus)),2*k)
                self.assertTrue(set(plus[1:]+minus)<=set(self.frozen))
                replacement=list(self.columns[i])
                for at,value in zip(self.supports[i],PALETTES[p["palette"]]):
                    replacement[at]=value
                for j in range(12):
                    self.assertEqual(
                        (replacement[j]+sum(self.columns[v][j] for v in plus[1:]))%5,
                        sum(self.columns[v][j] for v in minus)%5)

    def test_invalid_original_physical_source_fails_closed(self):
        lines=self.input.splitlines()
        fields=lines[1].split()
        fields[5+int(fields[1])]="0"  # guaranteed nonzero original support
        lines[1]=" ".join(fields)
        bad=self.root/"corrupt.txt"
        bad.write_text("\n".join(lines)+"\n",encoding="utf-8")
        failure=subprocess.run([str(self.exe),str(bad),
                                str(self.root/"bad.json"),"0","1"],
                               capture_output=True,text=True,timeout=20)
        self.assertNotEqual(failure.returncode,0)


if __name__=="__main__":
    unittest.main()
