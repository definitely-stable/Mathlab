"""Independent genuine-original W32 full-GF5 2-editable source falsifier.

Unlike the indexed C++ binary oracle, this oracle directly enumerates
every fixed 2/3-subset signed vector equation on full physical GF5^12
and all 51^2 legal pairs, using actual original symplectic W(3,2) source
incidences. Small selected W32 subproblem; other original IDs are
deliberately not part of this finite local fixed-core control.
"""
from itertools import combinations,product
from pathlib import Path
from collections import Counter
import json
import subprocess
import tempfile
import unittest

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_original_gf5_deterministic_extraction_referee import PALETTES
from hyp105_w34_external_triple_r3_referee import (
    deterministic_original_checksum_palettes,exact_gf5_original_vectors)
from hyp105_w34_twoedit_binary_csp import exact_ac3


def source_control():
    model=pair_labeled_symplectic(1,"lex")
    indices=deterministic_original_checksum_palettes(model,seed=3)
    ids,columns=exact_gf5_original_vectors(model,indices)
    assert (model["s"],model["N"],model["m"])==(2,45,12)
    a=model["a"]
    supports=tuple((model["left_labels"][p][0],model["left_labels"][p][1],
                    a+model["right_labels"][ell][0],
                    a+model["right_labels"][ell][1])
                   for p,ell in model["incidences"])
    # Choose real original flags with distinct k=1/2/3 F-subset sums.
    # This is only a small *physical W32* subproblem, not claimed all W32.
    F=[]
    for i in range(45):
        trial=F+[i]
        valid=True
        for k in (1,2,3):
            signatures=set()
            for ids in combinations(trial,k):
                sig=tuple(sum(columns[t][j] for t in ids)%5 for j in range(12))
                if sig in signatures:
                    valid=False;break
                signatures.add(sig)
            if not valid:break
        if valid:F.append(i)
        if len(F)==8:break
    if len(F)!=8:raise AssertionError("no 8 true frozen original W32 IDs")
    T=tuple(i for i in range(45) if i not in F)[:2]
    assert set(T).isdisjoint(F)
    lines=[f"HYP105_BINARY_ORIGINAL_V1 lex 45 12 2 {len(F)}"]
    for i in range(45):
        lines.append(" ".join(map(str,(indices[i],*supports[i],*columns[i]))))
    lines.extend(" ".join(map(str,p)) for p in PALETTES)
    lines.append(" ".join(map(str,T)))
    lines.append(" ".join(map(str,F)))
    lines.extend([str((1<<51)-1)]*2)
    return "\n".join(lines)+"\n",tuple(columns),supports,T,tuple(F)


def direct_full_signed_W32_binary_forbidden(columns,supports,T,F,p,q):
    changed={}
    for i,v in zip(T,(p,q)):
        col=list(columns[i])
        for at,digit in zip(supports[i],PALETTES[v]):
            col[at]=digit
        changed[i]=tuple(col)
    def vector(i):
        return changed.get(i,columns[i])
    def same(X,Y):
        return all(sum(vector(i)[j] for i in X)%5==
                   sum(vector(i)[j] for i in Y)%5 for j in range(12))
    i,j=T
    # Exhaust EVERY source-DISJOINT original 2v2 and 3v3 event with
    # exactly these 2 editable ORIGINAL source IDs.
    for k in (2,3):
        for a in range(k+1):
            b=2-a
            if a>k or b>k:continue
            # For canonical orientation include i always on the positive
            # side; the second editable j is on positive or negative.
            if a==2:
                posE=(i,j);negE=()
            elif a==1:
                posE=(i,);negE=(j,)
            else:
                continue
            for posF in combinations(F,k-len(posE)):
                for negF in combinations(tuple(v for v in F if v not in posF),
                                         k-len(negE)):
                    if same(posE+posF,negE+negF):
                        return True
    return False


class GenuineOriginalW32BinaryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp=tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.tmp.cleanup)
        cls.root=Path(cls.tmp.name)
        source,cls.columns,cls.supports,cls.T,cls.F=source_control()
        inp=cls.root/"true-original-w32-subscope.txt"
        out=cls.root/"all-51x51-binary.json"
        exe=cls.root/"w32-binary"
        inp.write_text(source,encoding="utf-8")
        cpp=Path(__file__).with_name("hyp105_w34_twoedit_binary.cpp")
        c=subprocess.run(["g++","-O3","-std=c++17","-Wall","-Wextra",
                          "-pedantic",str(cpp),"-o",str(exe)],
                         capture_output=True,text=True,timeout=120)
        if c.returncode:
            raise AssertionError(c.stderr[-4500:])
        run=subprocess.run([str(exe),str(inp),str(out),"0","1"],
                           capture_output=True,text=True,timeout=90)
        if run.returncode:
            raise AssertionError(run.stderr[-4500:])
        cls.result=json.loads(out.read_text(encoding="utf-8"))
        cls.exe=exe
        cls.source=source

    def test_all_51x51_true_original_2v2_3v3_full_physical_equations(self):
        r=self.result
        self.assertEqual((r["n"],r["m"],r["scheme"]),(45,12,"lex"))
        self.assertEqual(r["edited_original_source_IDs"],list(self.T))
        self.assertEqual(r["frozen_original_source_IDs"],list(self.F))
        self.assertEqual(r["all_frozen_pairs"],28)
        self.assertEqual(r["all_frozen_triples"],56)
        self.assertEqual(len(r["results"]),1)
        row=r["results"][0]
        self.assertEqual(row["total_domain_pairs"],51*51)
        allowed=set(tuple(x) for x in row["allowed_pairs"])
        rejected={(x["p"],x["q"]):x for x in row["forbidden"]}
        self.assertEqual(len(allowed)+len(rejected),2601)
        for p,q in product(range(51),repeat=2):
            forbidden=direct_full_signed_W32_binary_forbidden(
                self.columns,self.supports,self.T,self.F,p,q)
            self.assertEqual(forbidden,(p,q) in rejected,
                             "true original W32 two-editable GF5 discrepancy")
            self.assertEqual(not forbidden,(p,q) in allowed)

    def test_every_forbidden_record_is_true_full_12D_GF5_signed_event(self):
        r=self.result["results"][0]
        for w in r["forbidden"]:
            i,j=self.T
            changes={}
            for source,p in ((i,w["p"]),(j,w["q"])):
                v=list(self.columns[source])
                for at,digit in zip(self.supports[source],PALETTES[p]):
                    v[at]=digit
                changes[source]=tuple(v)
            pos=w["positive_original_IDs"]
            neg=w["negative_original_IDs"]
            self.assertEqual(len(pos),w["k"])
            self.assertEqual(len(neg),w["k"])
            self.assertEqual(len(set(pos+neg)),2*w["k"])
            self.assertEqual(set(pos+neg)&set(self.T),set(self.T))
            for coord in range(12):
                l=sum(changes.get(x,self.columns[x])[coord] for x in pos)%5
                rr=sum(changes.get(x,self.columns[x])[coord] for x in neg)%5
                self.assertEqual(l,rr)

    def test_invalid_original_source_checksum_fails_closed(self):
        rows=self.source.splitlines()
        data=rows[1].split()
        at=int(data[1])
        data[5+at]="0"
        rows[1]=" ".join(data)
        bad=self.root/"invalid-actual-source.txt"
        bad.write_text("\n".join(rows)+"\n",encoding="utf-8")
        p=subprocess.run([str(self.exe),str(bad),
                          str(self.root/"bad.json"),"0","1"],
                         capture_output=True,text=True,timeout=30)
        self.assertNotEqual(p.returncode,0)

    def test_arc_consistency_negative_and_full_support(self):
        # Independently verify that a deleted value has NO support
        # in one neighbor, while retention alone proves no solution.
        T=(0,1,2)
        D={0:(0,1),1:(0,1),2:(0,1)}
        r={(0,1):((0,0),),(0,2):((1,1),),(1,2):((0,0),(1,1))}
        result=exact_ac3(T,D,r)
        self.assertTrue(result["empty_ids"])
        self.assertGreater(len(result["removals"]),0)
        full={(0,1):tuple(product(D[0],D[1])),
              (0,2):tuple(product(D[0],D[2])),
              (1,2):tuple(product(D[1],D[2]))}
        self.assertFalse(exact_ac3(T,D,full)["empty_ids"])


if __name__=="__main__":
    unittest.main()
