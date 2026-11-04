"""AA4-MULTI: bounded, sound counterexample-guided ORIGINAL GF5 source CSP.

Proof scope: all-N equivalence between full original 0-to-3 ASET and
satisfaction of ALL signed 2v2 / 3v3 original-source nogoods. Every
learned clause follows from a DIRECT physical complete-GF5 equality
using only immutable F and selected editable source IDs T. A bounded
incomplete search NEVER proves no possible original source assignment.

The hosted true W34 experiment:
  exact parent source f,g, true minimum source covers 25/26;
  complete frozen-core 51-palette D_i(F) from #722;
  complete exact binary R_ij source tables from #723;
  cached frozen original F 90k/10.5m pair/triple physical sums;
  incremental complete dynamic original 2/3-subset-sum oracle;
  native long-lived physical tester and Python independently verified
  exact source-ID signed event --> necessary finite-domain nogood;
  brute-force independent final full 12,704,100-triple GF5 auditor
  REQUIRED before any constructive success promotion.
"""
import argparse
from collections import Counter,defaultdict
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path
import random
import subprocess

from hyp105_frozen_core_fiber import real_source
from hyp105_w34_twoedit_binary_csp import (
    _read_domains,validate_shard,binary_source_text)
from hyp105_w34_external_triple_r3_referee import (
    exact_full_original_external_r3,exact_gf5_original_vectors)
from hyp105_w34_zero_incidence_erasure_referee import (
    _two_sum_collision_source_pairs)
from hyp105_original_gf5_deterministic_extraction_referee import PALETTES

ROOT=Path(__file__).parent
PARENT_723="bd81ccade8dc7f6306174d3fe8104f22927abc15"
ROOT_OPEN="OPEN_WITH_FORMAL_BLOCKER"
PERMANENT_BINARY=ROOT/"hyp105_w34_twoedit_binary_csp_certificates.json"
FULL_ZERO_PARENT=ROOT/"hyp105_w34_zero_incidence_erasure_certificates.json"


def load_exact_binary(scheme,frozen_dir,binary_dir):
    model,old,columns,supports,T,D=_read_domains(scheme,frozen_dir)
    cert=json.loads(PERMANENT_BINARY.read_text(encoding="utf-8"))
    if (cert["root_230_status"]!=ROOT_OPEN
        or cert["scientific_parent_722_exact_SHA"]!=
           "10958b04a2bd62f258b95e22f294ea222622a292"
        or cert["all_h_root_A_B_C_proved"]
        or cert["joint_true_Gf5_zero_ASET_from_binary_only"]):
        raise AssertionError("wrong frozen true ORIGINAL binary CSP parent")
    expected=cert["schemes"][scheme]["source_pairwise_relation_sizes"]
    edges={}
    shard_ids=set()
    for path in sorted(binary_dir.glob(f"{scheme}-binary-*-of-4.json")):
        data=json.loads(path.read_text(encoding="utf-8"))
        shard=data["shard"]
        if shard in shard_ids or shard not in range(4):
            raise AssertionError("duplicate/invalid 4-shard source physics")
        validate_shard(scheme,frozen_dir,data,shard=shard,shards=4)
        shard_ids.add(shard)
        for e in data["results"]:
            i,j=e["source_i"],e["source_j"]
            if (i,j) in edges:
                raise AssertionError("duplicate physical source pair CSP")
            compatible=set(tuple(x) for x in e["allowed_pairs"])
            if len(compatible)!=expected[str(i)+","+str(j)]:
                raise AssertionError("source compatibility result differs from #723")
            edges[(i,j)]=compatible
    if (shard_ids!=set(range(4)) or
        set(edges)!=set(combinations(T,2))):
        raise AssertionError("incomplete physical original W34 pair matrix")
    return model,old,columns,supports,T,D,edges


def verify_full_source_event(event,T,assign,columns,supports):
    """Independent 28D physical arithmetic and exact source-ID proof."""
    k=event["k"]
    pos=tuple(event["positive_original_IDs"])
    neg=tuple(event["negative_original_IDs"])
    if (k not in (2,3) or len(pos)!=k or len(neg)!=k
        or len(set(pos+neg))!=2*k
        or tuple(sorted(pos))!=pos or tuple(sorted(neg))!=neg
        or not pos<neg
        or any(not 0<=x<len(columns) for x in pos+neg)):
        raise AssertionError("false original signed 2v2/3v3 event")
    changed=tuple(sorted(set(pos+neg)&set(T)))
    if changed!=tuple(event["edited_original_IDs"]) or not changed:
        raise AssertionError("false original edited source-ID provenance")
    for c in range(len(columns[0])):
        def coeff(i):
            if i not in assign:return columns[i][c]
            p=assign[i]
            support=supports[i]
            return PALETTES[p][support.index(c)] if c in support else 0
        if sum(coeff(i) for i in pos)%5!=sum(coeff(i) for i in neg)%5:
            raise AssertionError("not a real complete-GF5 ORIGINAL source equality")
    return tuple((i,assign[i]) for i in changed)


def checked_cegar_clause(event,T,assign,columns,supports):
    """A true source-event witness forbids this EXACT T-intersection tuple."""
    clause=verify_full_source_event(event,T,assign,columns,supports)
    if not clause:
        raise AssertionError("no original editable variable in source conflict")
    return clause


class FiniteSourceCSP:
    """Finite-domain exhaustive backtracker bounded by explicit node budget.

    Parent R_ij exact physical tables are STATIC necessary constraints.
    Learned clauses are independently verified exact full-GF5 source
    witness nogoods. An incomplete search reports INCOMPLETE not UNSAT.
    """
    def __init__(self,T,D,binary):
        self.T=tuple(T)
        self.D={i:tuple(D[i]) for i in T}
        if (set(self.D)!=set(T) or
            set(binary)!=set(combinations(self.T,2))):
            raise ValueError("not complete independent binary source CSP")
        self.R={}
        for (i,j),pairs in binary.items():
            rel=set(pairs)
            self.R[(i,j)]=rel
            self.R[(j,i)]={(b,a) for a,b in rel}
        self.nogoods=set()
        self.by_var={i:set() for i in T}
        self.physical_reason={}
    def add_nogood(self,clause,physical_witness):
        clause=tuple(sorted(clause))
        if not clause or len(set(i for i,_ in clause))!=len(clause):
            raise AssertionError("invalid source proof nogood")
        if any(i not in self.D or p not in self.D[i] for i,p in clause):
            raise AssertionError("not the exact original 51-pattern domain")
        if clause in self.nogoods:return False
        self.nogoods.add(clause)
        self.physical_reason[clause]=physical_witness
        for i,_ in clause:self.by_var[i].add(clause)
        return True
    def _consistent(self,i,p,assigned):
        for j,q in assigned.items():
            if (p,q) not in self.R[(i,j)]:
                return False
        for clause in self.by_var[i]:
            if all((id==i and v==p) or
                   (id in assigned and assigned[id]==v)
                   for id,v in clause):
                return False
        return True
    def search(self,*,preferred=None,seed=0,node_budget=200000):
        rng=random.Random(seed)
        priority={i:len(self.by_var[i]) for i in self.T}
        order=tuple(sorted(self.T,
            key=lambda i:(len(self.D[i]),-priority[i],i)))
        chosen={}
        stats={"visited_nodes":0,"incomplete":False}
        def dfs(depth):
            if depth==len(order):
                return dict(chosen)
            i=order[depth]
            options=list(self.D[i])
            rng.shuffle(options)
            if preferred is not None and preferred.get(i) in options:
                p=preferred[i]
                options.remove(p)
                options.insert(0,p)
            for p in options:
                stats["visited_nodes"]+=1
                if stats["visited_nodes"]>node_budget:
                    stats["incomplete"]=True
                    return None
                if not self._consistent(i,p,chosen):
                    continue
                chosen[i]=p
                found=dfs(depth+1)
                if found is not None:
                    return found
                chosen.pop(i)
                if stats["incomplete"]:
                    return None
            return None
        result=dfs(0)
        return result,stats


class OriginalPhysicalOracle:
    """Persistent native physical checker caches 10.5m F-only triple sums."""
    def __init__(self,binary,source_file,max_witnesses=24):
        self.process=subprocess.Popen(
            [str(binary),str(source_file),str(max_witnesses)],
            stdin=subprocess.PIPE,stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,text=True,bufsize=1)
        line=self.process.stdout.readline().strip()
        if not line.startswith("ORIGINAL_CEGAR_READY "):
            raise AssertionError("native GF5 source oracle did not initialize: "+line+
                                 " / "+self.process.stderr.read()[-2500:])
        self.ready=line
        self.max_witnesses=max_witnesses
    def audit(self,assign,T):
        self.process.stdin.write(" ".join(str(assign[i]) for i in T)+"\n")
        self.process.stdin.flush()
        raw=self.process.stdout.readline().strip()
        if not raw.startswith("ORIGINAL_CEGAR_RESULT "):
            raise AssertionError("native original physical GF5 source oracle failed: "+
                                 raw+" / "+self.process.stderr.read()[-2500:])
        result=json.loads(raw[len("ORIGINAL_CEGAR_RESULT "):])
        if result["assigned_palettes"]!=[assign[i] for i in T]:
            raise AssertionError("physical source audit not for submitted coefficient vector")
        if (result["zero"] and (not result["full_scan"] or result["events"])):
            raise AssertionError("false complete zero-ASET source claim")
        if not result["zero"] and not result["events"]:
            raise AssertionError("nonzero original physical risk without a signed witness")
        return result
    def close(self):
        if self.process.poll() is None:
            self.process.stdin.write("QUIT\n")
            self.process.stdin.flush()
            self.process.stdin.close()
            self.process.wait(timeout=20)
        if self.process.returncode:
            raise AssertionError("native physical source oracle failed: "+
                                 self.process.stderr.read()[-3500:])


def independent_final_all_original_w34(scheme,before,final):
    """Independent physical 425 ORIGINAL pair + all 12.7m triple verifier."""
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
    model=pair_labeled_symplectic(2,scheme)
    ids,vectors=exact_gf5_original_vectors(model,final)
    if ids!=tuple(range(425)) or len(set(vectors))!=425:
        raise AssertionError("not injective 425 ORIGINAL physical source columns")
    risks=exact_full_original_external_r3(
        model,final,max_triples=12_704_100,max_witnesses=2)
    if not (risks["all_triples_exact_external_disk_records_processed"]
            ==12_704_100 and
            risks["all_source_triple_count"]==12_704_100 and
            (risks["R2_signed_2v2_events_exact"],
             risks["equal_sum_pairs_of_distinct_ORIGINAL_triples"],
             risks["FULL_six_distinct_original_ID_3v3_signed_event_count"])
             ==(0,0,0) and
            not _two_sum_collision_source_pairs(model,final)):
        raise AssertionError("native zero candidate fails independent complete original GF5")
    return {"independent_full_original_12_704_100_triples":True,
            "independent_full_original_90_100_pairs":True,
            "all_true_original_GF5_0_to_3_collision_counts":[0,0,0]}


def run_cegar(scheme,frozen,binary_dir,source_file,oracle_binary,
              *,max_rounds=64,node_budget=100000,seed=7123):
    model,old,columns,supports,T,D,relations=load_exact_binary(
        scheme,frozen,binary_dir)
    if sha256(source_file.read_bytes()).hexdigest()!=sha256(
            binary_source_text(scheme,frozen).encode()).hexdigest():
        raise AssertionError("source input changed from parent actual f,g")
    cs=FiniteSourceCSP(T,D,relations)
    parent=json.loads(FULL_ZERO_PARENT.read_text(encoding="utf-8"))
    if (parent["root_230_status"]!=ROOT_OPEN or
        parent["all_h_theorem_proved"]):
        raise AssertionError("false parent source proof scope")
    after=parent["scheme_results"][scheme][
        "exact_source_425_GF5_legal_palette_indices_after"]
    # Genuine zero-to-three #719 parent is a HEURISTIC warm start ONLY.
    preferred={i:(after[i] if after[i] in D[i] else D[i][0]) for i in T}
    logs=[]
    best=1_000_000
    candidate=None
    last_result=None
    state="BOUND_NO_FEASIBILITY_OR_UNSAT_CLAIM"
    independent=None
    oracle=OriginalPhysicalOracle(oracle_binary,source_file,max_witnesses=32)
    try:
        for step in range(max_rounds):
            assignment,stats=cs.search(
                preferred=preferred,seed=seed+step*7919,
                node_budget=node_budget)
            if assignment is None:
                state=("SEARCH_BUDGET_EXHAUSTED_NO_UNSAT_PROOF"
                       if stats["incomplete"] else
                       "COMPLETE_NECESSARY_CSP_UNSAT_FOR_THIS_SPECIFIC_T")
                logs.append({"iteration":step,"search_nodes":stats[
                    "visited_nodes"],"search_status":state})
                break
            exact=oracle.audit(assignment,T)
            witnesses=[]
            fresh=0
            for event in exact["events"]:
                clause=checked_cegar_clause(
                    event,T,assignment,columns,supports)
                if len(clause)<3:
                    # With complete frozen D_i and exact R_ij, ANY
                    # <=2 edit source event is a REAL inconsistency.
                    raise AssertionError(
                        "source oracle contradicted full 0/1/2-variable parent")
                if cs.add_nogood(clause,event):
                    fresh+=1
                    witnesses.append({"literals":[list(x) for x in clause],
                                      "signed_event":event})
            if exact["zero"]:
                if not exact["full_scan"]:
                    raise AssertionError("partial 12.7m original triple audit passed as zero")
                final=list(old)
                for i,p in assignment.items():final[i]=p
                independent=independent_final_all_original_w34(
                    scheme,old,final)
                state="CONSTRUCTIVE_FULL_ORIGINAL_GF5_ZERO_ASET_VERIFIED"
                candidate={"edited_original_IDs":list(T),
                           "palettes_on_T":[assignment[i] for i in T],
                           "complete_425_original_GF5_palettes":final}
                logs.append({"iteration":step,"search_nodes":stats[
                    "visited_nodes"],"zero":True,
                    "full_original_dynamic_triples_checked":exact[
                        "dynamic_triples_checked"]})
                break
            if not fresh:
                raise AssertionError("source oracle returned only already-excluded clauses")
            best=min(best,len(exact["events"]))
            logs.append({
                "iteration":step,
                "search_nodes":stats["visited_nodes"],
                "physical_scan_complete":exact["full_scan"],
                "physical_witnesses":len(exact["events"]),
                "new_verified_original_signed_nogoods":fresh,
                "witnesses":witnesses,
                "source_assigned_palettes":[assignment[i] for i in T],
                "dynamic_original_pairs_examined":exact["dynamic_pairs_checked"],
                "dynamic_original_triples_examined":exact["dynamic_triples_checked"]})
            # Preserve a near-neighbor preference until its current
            # true signed GF5 event clause forces a legal change.
            preferred=assignment
        else:
            state="BOUND_NO_FEASIBILITY_OR_UNSAT_CLAIM"
    finally:
        oracle.close()
    report={
        "schema":"mathlab.hyp105.original-W34-multiedit-cegar.v1",
        "scheme":scheme,
        "scientific_parent_723_exact_SHA":PARENT_723,
        "root_230_status":ROOT_OPEN,
        "original_W34_source_flags":425,
        "physical_GF5_coordinates":28,
        "candidate_original_source_IDs":list(T),
        "fixed_original_source_count":425-len(T),
        "complete_original_source_parent_sha256":
            sha256(source_file.read_bytes()).hexdigest(),
        "exact_complete_binary_original_source_pairs":len(relations),
        "complete_one_editable_legal_palette_sum":sum(len(v) for v in D.values()),
        "bound_iterations":max_rounds,
        "solver_per_candidate_node_budget":node_budget,
        "seed":seed,
        "run_status":state,
        "physical_native_oracle_cached_frozen_source_header":oracle.ready,
        "learning_rounds":len(logs),
        "learned_true_physical_signed_nogoods":len(cs.nogoods),
        "best_bounded_witness_sample_size":
            (best if best!=1_000_000 else None),
        "steps":logs,
        "accepted_full_original_zero_source":candidate,
        "independent_complete_original_pair_triple_audit":independent,
        "does_not_prove_any_other_minimum_T_unsat":True,
        "does_not_prove_all_h_seven_motif_conjecture":True,
    }
    return report


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--scheme",required=True,
                   choices=("lex","reverse-line"))
    p.add_argument("--frozen",type=Path,required=True)
    p.add_argument("--binary",type=Path,required=True)
    p.add_argument("--source",type=Path,required=True)
    p.add_argument("--native",type=Path,required=True)
    p.add_argument("--out",type=Path,required=True)
    p.add_argument("--max-rounds",type=int,default=64)
    p.add_argument("--node-budget",type=int,default=100000)
    a=p.parse_args()
    report=run_cegar(a.scheme,a.frozen,a.binary,a.source,a.native,
                     max_rounds=a.max_rounds,node_budget=a.node_budget)
    a.out.parent.mkdir(parents=True,exist_ok=True)
    a.out.write_text(json.dumps(report,indent=2,sort_keys=True)+"\n",
                     encoding="utf-8")
    print("AA4_MULTIEDIT_CEGAR_RESULT="+json.dumps({
        k:v for k,v in report.items() if k not in ("steps",)},
        sort_keys=True,separators=(",",":")),flush=True)
    for row in report["steps"]:
        print("AA4_MULTIEDIT_CEGAR_STEP="+json.dumps({
            k:v for k,v in row.items() if k not in
                ("witnesses","source_assigned_palettes")},
            sort_keys=True,separators=(",",":")),flush=True)
    print("AA4_ROOT_230_STILL_OPEN_WITH_FORMAL_BLOCKER",flush=True)
if __name__=="__main__":
    main()
