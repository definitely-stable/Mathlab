#!/usr/bin/env python3
"""Independent G2B-B2 result verification, including optional DRAT/DRUP.

Fail-closed states:
- SAT witness => independently re-evaluate all ASET subset sums.
- UNKNOWN => no exactness claim.
- UNSAT => only accept if the stored CNF matches regenerated source
  and an independent drat-trim checker accepts the complete proof.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from hashlib import sha256
from itertools import combinations, product
import json
from pathlib import Path
import shutil
import subprocess

from g2bb2_anchor_sat import ANCHOR, build_atleast_cnf, formula_source_hash
from lent_hypergraph import build_forbidden_hypergraph
from lent_exhaustive import is_exact_family


def independently_enumerated_graph():
    """Second source enumeration: no hypergraph builder reuse."""
    universe=tuple(x for x in product(range(5),repeat=3)
                   if 1<=sum(t!=0 for t in x)<=2)
    buckets:dict[tuple[int,...],list[int]]=defaultdict(list)
    buckets[(0,0,0)].append(0)
    for i,vec in enumerate(universe):
        buckets[vec].append(1<<i)
    for i,j in combinations(range(len(universe)),2):
        v=tuple((universe[i][t]+universe[j][t])%5 for t in range(3))
        buckets[v].append((1<<i)|(1<<j))
    invalid={
        a^b
        for bucket in buckets.values()
        for a,b in combinations(bucket,2)
        if a!=b
    }
    # A subset-mask is a minimal invalid family iff deleting any
    # nonempty included column makes it ASET exact independently.
    minimal=[]
    for mask in sorted(invalid,key=lambda v:(v.bit_count(),v)):
        if mask.bit_count()<2 or mask.bit_count()>4:
            raise AssertionError("inadmissible forbidden mask size")
        if any(mask&edge==edge for edge in minimal):
            continue
        minimal.append(mask)
    return universe,tuple(minimal)


def verify_model_source() -> tuple[str,str]:
    graph=build_forbidden_hypergraph(5,3,2)
    cols,forbidden=independently_enumerated_graph()
    if cols!=graph.columns or forbidden!=graph.edges:
        raise AssertionError("independent forbidden incidence disagreement")
    cnf=build_atleast_cnf(graph,11,anchored=True)
    if not (len(cols)==60 and len(forbidden)==9990
            and ANCHOR in cols and cnf.anchor==cols.index(ANCHOR)):
        raise AssertionError("source model contract drift")
    return formula_source_hash(graph),cnf.dimacs()


def independently_validate_witness(payload:dict) -> None:
    if any(payload.get(k)!=v for k,v in (
        ("q",5),("m",3),("w",2),("d",2),("V",11))):
        raise AssertionError("wrong witness domain")
    raw=payload.get("columns")
    if not isinstance(raw,list) or len(raw)!=11:
        raise AssertionError("need 11 candidate columns")
    cols=[]
    for row in raw:
        if not isinstance(row,list) or len(row)!=3 or any(
            type(x) is not int or not 0<=x<5 for x in row
        ) or not 1<=sum(v!=0 for v in row)<=2:
            raise AssertionError("malformed witness column")
        cols.append(tuple(row))
    if len(set(cols))!=11 or ANCHOR not in cols:
        raise AssertionError("invalid duplicate or unanchored family")
    if not is_exact_family(cols,5,2):
        raise AssertionError("independent G1A sum check failed")
    seen=set()
    for group in [()] + [(i,) for i in range(11)] + list(combinations(range(11),2)):
        state=tuple(sum(cols[i][j] for i in group)%5 for j in range(3))
        if state in seen:
            raise AssertionError("separate explicit 0/1/2 subset sum collision")
        seen.add(state)
    if len(seen)!=1+11+55:
        raise AssertionError("distinct cardinality states count")
    print("G2BB2_ELEVEN_WITNESS_DOUBLE_ORACLE_PASS")


def verify_artifacts(path:Path, drat_trim:str|None=None)->str:
    report=json.loads((path/"decision.json").read_text(encoding="utf-8"))
    source_hash,dimacs=verify_model_source()
    if source_hash!=report.get("source_sha256"):
        raise AssertionError("source provenance mismatch")
    if sha256(dimacs.encode()).hexdigest()!=report.get("cnf_sha256"):
        raise AssertionError("CNF provenance mismatch")
    if (path/"problem.cnf").read_text(encoding="ascii")!=dimacs:
        raise AssertionError("CNF bytes differ from regenerated formula")
    status=report.get("status")
    if status=="SAT_INDEPENDENT_WITNESS_EXACT_11":
        independently_validate_witness(
            json.loads((path/"witness.json").read_text(encoding="utf-8")))
        if report.get("exact_value")!=11:
            raise AssertionError("SAT claimed wrong exact value")
        print("G2BB2_CERTIFIED_EXACT_11")
        return "EXACT_11"
    if status=="UNKNOWN_CONFLICT_BUDGET":
        if report.get("exact_value") is not None or (
            (path/"witness.json").exists() or (path/"proof.drat").exists()):
            raise AssertionError("UNKNOWN cannot contain proof or exactness")
        print("G2BB2_UNKNOWN_SAFE_STATUS_PASS")
        return "UNKNOWN"
    if status=="UNSAT_UNVERIFIED_CERTIFICATE_REQUIRED":
        if report.get("exact_value") is not None:
            raise AssertionError("UNSAT remains unverified at decision stage")
        proof=path/"proof.drat"
        if not proof.exists() or not proof.stat().st_size:
            raise AssertionError("empty or absent DRUP proof")
        complete_proof=proof.read_bytes()
        if report.get("proof_sha256") != sha256(complete_proof).hexdigest():
            raise AssertionError("proof SHA256 mismatch")
        if report.get("proof_bytes") != len(complete_proof):
            raise AssertionError("incomplete proof byte count")
        if report.get("proof_lines") != complete_proof.count(b"\\n"):
            raise AssertionError("incomplete proof line count")
        executable=drat_trim or shutil.which("drat-trim")
        if not executable:
            raise RuntimeError("drat-trim required to validate UNSAT; exactness NOT claimed")
        result=subprocess.run(
            [executable,str(path/"problem.cnf"),str(proof)],
            capture_output=True,text=True,timeout=480,check=False,
        )
        if result.returncode!=0 or "VERIFIED" not in (
            result.stdout+result.stderr).upper():
            raise AssertionError(
                f"independent DRAT checker rejected refutation: "
                f"exit={result.returncode}; last output="
                f"{(result.stdout+result.stderr)[-1500:]}"
            )
        (path/"verified-result.json").write_text(
            json.dumps({
                "verdict": "EXACT_10",
                "q": 5, "m": 3, "w": 2, "d": 2,
                "model_source_sha256": source_hash,
                "cnf_sha256": sha256(dimacs.encode()).hexdigest(),
                "proof_sha256": report["proof_sha256"],
                "independent_checker": "drat-trim, source pinned in workflow",
                "solver": report["solver"],
                "github_sha": report["github_sha"],
            }, sort_keys=True, indent=2)+"\\n", encoding="utf-8",
        )
        print("G2BB2_PROOF_HASH_AND_LENGTH_PASS")
        print("G2BB2_INDEPENDENT_UNSAT_PROOF_ACCEPTED")
        print("G2BB2_CERTIFIED_EXACT_10")
        return "EXACT_10"
    raise AssertionError(f"unknown decision status {status!r}")


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--artifact-dir",type=Path,required=True)
    parser.add_argument("--drat-trim",default=None)
    args=parser.parse_args()
    result=verify_artifacts(args.artifact_dir,args.drat_trim)
    print("G2BB2_VERIFIED_VERDICT",result)


if __name__=="__main__":
    main()
