"""Independent genuine W32 original-source full 2/3 subset-sum CEGAR falsifiers.

A DIFFERENT Python implementation enumerates every actual signed
original equal-subset sum over a real symplectic W(3,2) 12-source
subproblem; its result must equal the cached native GF5 source events.
This is not a synthetic GF5 graph or a full-W32 theorem.
"""
from collections import defaultdict
from itertools import combinations,product
from pathlib import Path
import copy
import json
import random
import subprocess
import tempfile
import unittest

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_original_gf5_deterministic_extraction_referee import PALETTES
from hyp105_w34_external_triple_r3_referee import (
    deterministic_original_checksum_palettes,exact_gf5_original_vectors)
from hyp105_frozen_core_fiber import real_source
from hyp105_w34_multiedit_cegar import (
    OriginalPhysicalOracle,FiniteSourceCSP,checked_cegar_clause,
    verify_full_source_event)

ROOT=Path(__file__).parent


def true_w32_fixture():
    model=pair_labeled_symplectic(1,"lex")
    src=deterministic_original_checksum_palettes(model,seed=3)
    ids,cols=exact_gf5_original_vectors(model,src)
    assert (model["N"],model["m"])==(45,12)
    a=model["a"]
    support=tuple((model["left_labels"][p][0],
                   model["left_labels"][p][1],
                   a+model["right_labels"][line][0],
                   a+model["right_labels"][line][1])
                  for p,line in model["incidences"])
    F=[]
    # Genuine physical fixed-source triples must have UNIQUE signatures.
    for i in range(45):
        trial=F+[i]
        good=True
        for k in (1,2,3):
            seen=set()
            for xs in combinations(trial,k):
                sig=tuple(sum(cols[v][j] for v in xs)%5
                          for j in range(12))
                if sig in seen:
                    good=False
                    break
                seen.add(sig)
            if not good:break
        if good:F.append(i)
        if len(F)>=8:break
    if len(F)!=8:raise AssertionError("no real W32 collision-free fixed subset")
    T=tuple(i for i in range(45) if i not in F)[:4]
    assert len(T)==4 and set(T).isdisjoint(F)
    s=[f"HYP105_BINARY_ORIGINAL_V1 lex 45 12 4 {len(F)}"]
    for id in range(45):
        s.append(" ".join(map(str,(src[id],*support[id],*cols[id]))))
    s.extend(" ".join(map(str,p)) for p in PALETTES)
    s.append(" ".join(map(str,T)))
    s.append(" ".join(map(str,F)))
    s.extend([str((1<<51)-1)]*len(T))
    return "\n".join(s)+"\n",cols,support,T,tuple(F)


def direct_w32_signed_events(columns,support,T,F,assigned):
    selected=sorted(set(T)|set(F))
    def physical(i):
        if i not in assigned:return columns[i]
        p=assigned[i]
        v=list(columns[i])
        for pos,x in zip(support[i],PALETTES[p]):v[pos]=x
        return tuple(v)
    col={i:physical(i) for i in selected}
    events=set()
    for k in (2,3):
        by_sig=defaultdict(list)
        for source in combinations(selected,k):
            sig=tuple(sum(col[i][j] for i in source)%5
                      for j in range(12))
            for earlier in by_sig[sig]:
                a=tuple(x for x in source if x not in earlier)
                b=tuple(x for x in earlier if x not in source)
                if len(a)!=len(b):
                    raise AssertionError("direct physical W32 ID equality broken")
                if len(a) not in (2,3):
                    continue
                pair=tuple(sorted((tuple(sorted(a)),tuple(sorted(b)))))
                events.add((len(a),*pair))
            by_sig[sig].append(source)
    return events


class GenuineW32PhysicalCounterexampleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp=tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.tmp.cleanup)
        cls.folder=Path(cls.tmp.name)
        cls.src,cls.columns,cls.support,cls.T,cls.F=true_w32_fixture()
        cls.input=cls.folder/"W32-real-subproblem.txt"
        cls.input.write_text(cls.src,encoding="utf-8")
        cls.exe=cls.folder/"native-original-cegar"
        cpp=ROOT/"hyp105_w34_multiedit_cegar_oracle.cpp"
        built=subprocess.run(["g++","-O3","-std=c++17","-Wall",
                              "-Wextra","-pedantic",str(cpp),"-o",
                              str(cls.exe)],
                             capture_output=True,text=True,timeout=120)
        if built.returncode:
            raise AssertionError(built.stderr[-5500:])

    def test_exact_physical_GF5_W32_against_different_all_subsets_oracle(self):
        audit=OriginalPhysicalOracle(self.exe,self.input,max_witnesses=4096)
        try:
            rng=random.Random(8842)
            # Fixed old, globally uniformly random physical legal patterns,
            # and deliberately repeated-check to validate native cache reuse.
            first={i:next(p for p,v in enumerate(PALETTES)
                          if tuple(self.columns[i][s] for s in self.support[i])==v)
                   for i in self.T}
            assignments=[first]
            assignments.extend({i:rng.randrange(51) for i in self.T}
                               for _ in range(12))
            assignments.append(first)
            for selected in assignments:
                with self.subTest(assigned=selected):
                    x=audit.audit(selected,self.T)
                    self.assertTrue(x["full_scan"])
                    self.assertEqual(x["dynamic_pairs_checked"],38)
                    self.assertEqual(x["dynamic_triples_checked"],164)
                    physical=direct_w32_signed_events(
                        self.columns,self.support,self.T,self.F,selected)
                    native=set()
                    for ev in x["events"]:
                        verify_full_source_event(
                            ev,self.T,selected,self.columns,self.support)
                        native.add((ev["k"],
                                    tuple(ev["positive_original_IDs"]),
                                    tuple(ev["negative_original_IDs"])))
                    self.assertEqual(physical,native)
                    self.assertEqual(x["zero"],not physical)
        finally:
            audit.close()

    def test_false_original_witness_is_rejected(self):
        _,old,columns,supports,T=real_source("lex")
        all_events=json.loads((ROOT/
            "hyp105_w34_original_event_cover_certificates.json"
        ).read_text(encoding="utf-8"))["schemes"]["lex"][
            "initial_R3_true_original_signed_partitions"]
        a,b=all_events[0]
        altered=tuple(sorted(set(a+b)))
        current={i:old[i] for i in altered}
        witness={"k":3,"positive_original_IDs":list(a),
                 "negative_original_IDs":list(b),
                 "edited_original_IDs":list(altered)}
        clause=checked_cegar_clause(witness,altered,current,columns,supports)
        self.assertEqual(len(clause),6)
        fake=copy.deepcopy(witness)
        fake["negative_original_IDs"][0]=fake["positive_original_IDs"][0]
        with self.assertRaises(AssertionError):
            checked_cegar_clause(fake,altered,current,columns,supports)

    def test_finite_sound_learned_nogood_and_complete_unsat(self):
        T=(0,1,2)
        D={i:(0,1,2) for i in T}
        pairs={k:set(product(D[k[0]],D[k[1]]))
               for k in combinations(T,2)}
        s=FiniteSourceCSP(T,D,pairs)
        m,stats=s.search(preferred={0:0,1:1,2:2})
        self.assertEqual(m,{0:0,1:1,2:2})
        self.assertTrue(s.add_nogood(((0,0),(1,1),(2,2)),{"valid":"fixture"}))
        m,_=s.search(preferred={0:0,1:1,2:2},node_budget=10000)
        self.assertIsNotNone(m)
        self.assertNotEqual(m,{0:0,1:1,2:2})
        for p in D[0]:
            self.assertTrue(s.add_nogood(((0,p),),{"valid":"fixture"}))
        m,stats=s.search(node_budget=10000)
        self.assertIsNone(m)
        self.assertFalse(stats["incomplete"])
        m,stats=s.search(node_budget=1)
        self.assertIsNone(m)
        self.assertTrue(stats["incomplete"])

    def test_corrupted_original_physical_source_fails_closed(self):
        rows=self.src.splitlines()
        fields=rows[1].split()
        coord=int(fields[1])
        fields[5+coord]="0"
        rows[1]=" ".join(fields)
        f=self.folder/"bad.txt"
        f.write_text("\n".join(rows)+"\n",encoding="utf-8")
        result=subprocess.run([str(self.exe),str(f),"20"],
                              input="",text=True,capture_output=True,timeout=30)
        self.assertNotEqual(result.returncode,0)


if __name__=="__main__":
    unittest.main()
