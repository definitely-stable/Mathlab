#!/usr/bin/env python3
"""G2B-B2 optional hosted bounded solver for the anchored eleven-column CNF.

This is an optional discovery / proof-producing job. The standard library
model and tests have no SAT dependency. If a search hits its conflict limit,
the ONLY accepted result remains 10 <= max <= 11.

On SAT: verify an 11-column family with the original independent ASET oracle.
On UNSAT: write DRUP proof and label UNSAT_UNVERIFIED; never claim exact=10
until a second independent checker verifies that proof against the original
CNF and original ASET-model reduction.
"""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
import os
from pathlib import Path
import platform
import sys
from time import monotonic

from g2bb2_anchor_sat import (
    ANCHOR, build_atleast_cnf, formula_source_hash, verify_11_witness,
)
from lent_hypergraph import build_forbidden_hypergraph
from lent_weak_sidon import weak_sidon_upper_v


def decide(*, conflict_budget: int, artifact_dir: Path) -> dict[str, object]:
    if type(conflict_budget) is not int or conflict_budget < 1:
        raise ValueError("conflict_budget must be an integer >=1")
    try:
        from pysat.solvers import Glucose4
        import pysat
    except ImportError as exc:
        raise RuntimeError("Install pinned python-sat on GitHub-hosted CI") from exc
    graph = build_forbidden_hypergraph(5,3,2)
    cnf = build_atleast_cnf(graph,11,anchored=True)
    if weak_sidon_upper_v(5,3)!=11:
        raise AssertionError("rigorous upper bound regressed")
    artifact_dir.mkdir(parents=True,exist_ok=True)
    dimacs=cnf.dimacs()
    (artifact_dir/"problem.cnf").write_text(dimacs,encoding="ascii")
    started=monotonic()
    with Glucose4(bootstrap_with=cnf.clauses,with_proof=True) as solver:
        solver.conf_budget(conflict_budget)
        outcome=solver.solve_limited()
        elapsed=round(monotonic()-started,3)
        verdict="UNKNOWN"
        witness=None
        proof_digest=None
        proof_bytes=0
        proof_lines=0
        if outcome is True:
            model=solver.get_model()
            if model is None:
                raise AssertionError("SAT solver did not produce a model")
            chosen={lit-1 for lit in model if 1<=lit<=len(graph.columns)}
            # A >=11 satisfying assignment may contain >11 columns.
            if cnf.anchor not in chosen or len(chosen)<11:
                raise AssertionError("SAT model violated anchored/cardinality CNF")
            canonical_indices=[cnf.anchor]+sorted(chosen-{cnf.anchor})[:10]
            witness=verify_11_witness(canonical_indices,graph)
            if not cnf.satisfied_by(cnf.assignment_for(chosen)):
                raise AssertionError("SAT assignment failed independently reconstructed CNF")
            verdict="SAT_INDEPENDENT_WITNESS_EXACT_11"
            (artifact_dir/"witness.json").write_text(
                json.dumps({"q":5,"m":3,"w":2,"d":2,"V":11,
                            "columns":[list(v) for v in witness]},
                           sort_keys=True,indent=2)+"\n",encoding="utf-8"
            )
        elif outcome is False:
            proof=solver.get_proof()
            if not proof:
                raise AssertionError("solver reported UNSAT but omitted proof")
            proof_text="\n".join(proof)+"\n"
            (artifact_dir/"proof.drat").write_text(proof_text,encoding="ascii")
            proof_digest=sha256(proof_text.encode("ascii")).hexdigest()
            proof_bytes=len(proof_text.encode("ascii"))
            proof_lines=len(proof)
            verdict="UNSAT_UNVERIFIED_CERTIFICATE_REQUIRED"
        else:
            verdict="UNKNOWN_CONFLICT_BUDGET"

        details={
            "status":verdict,
            "q":5,"m":3,"w":2,"d":2,"target":11,
            "baseline_lower":10,"theorem_upper":11,
            "solver":"PySAT Glucose4 (CDCL DRUP output)",
            "pysat_version":getattr(pysat,"__version__","unreported"),
            "python_version":platform.python_version(),
            "github_sha":os.environ.get("GITHUB_SHA","not-provided"),
            "max_conflicts":conflict_budget,"elapsed_seconds":elapsed,
            "symmetry_anchor":list(ANCHOR),
            "source_sha256":formula_source_hash(graph),
            "cnf_sha256":sha256(dimacs.encode()).hexdigest(),
            "cnf_vars":cnf.var_count,
            "cnf_clauses":len(cnf.clauses),
            "witness_verified_independently":bool(witness),
            "proof_sha256":proof_digest,
            "proof_bytes":proof_bytes,
            "proof_lines":proof_lines,
            "unsat_proof_verified_independently":False,
            "exact_value":11 if witness else None,
        }
        (artifact_dir/"decision.json").write_text(
            json.dumps(details,sort_keys=True,indent=2)+"\n",encoding="utf-8"
        )
    print("G2BB2_BOUNDED_SAT_RUN_COMPLETE",json.dumps(details,sort_keys=True))
    if witness:
        print("G2BB2_EXACT_ELEVEN_INDEPENDENT_WITNESS_PASS")
    elif outcome is False:
        print("G2BB2_UNSAT_PENDING_INDEPENDENT_DRUP_VERIFICATION")
    else:
        print("G2BB2_UNKNOWN_NOT_AN_EXACTNESS_CLAIM")
    return details


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--conflicts",type=int,default=30000)
    parser.add_argument("--artifact-dir",type=Path,default=Path("/tmp/g2bb2-artifacts"))
    args=parser.parse_args()
    decide(conflict_budget=args.conflicts,artifact_dir=args.artifact_dir)
