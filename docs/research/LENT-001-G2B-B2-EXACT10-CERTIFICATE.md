# LENT-001 G2B-B2 — exact GF(5) sparse ASET maximum 10

**Result class:** EXACT NUMERICAL RESULT / COMPUTER-ASSISTED PROOF.
**Date:** 2026-10-08. **Mathematical novelty:** NOT CLAIMED.
**Status:** EXPLICIT UNSAT CERTIFICATE ACCEPTED by an independent DRAT
checker on GitHub-hosted CI. Lean formalization: NOT PERFORMED.
Issue #42, parent #14.

## Final theorem (finite instance only)

For the ASET d=2 model over prime field GF(5), with m=3
coordinate counters and each distinct nonzero candidate vector
supported on <=2 coordinates, the exact maximum universe size is

    A_5^set(3,2,2) = 10.

This is a **finite exact value**. It is NOT a new asymptotic
theorem, a theorem about arbitrary q/m/w/d, or an original
coding-theoretic construction.

## 1. Lower-bound witness (10)

An independently exact 10-column family, preserved from G2B-A:

    (0,1,1) (0,1,2) (0,1,3) (0,3,1) (1,0,2)
    (1,3,0) (2,0,4) (2,4,0) (3,0,0) (4,0,0)

Every vector has support <=2. The original independent G1A
oracle verifies pairwise distinct modular sums for all
index subsets of cardinality 0,1,2. Thus V>=10.

## 2. Exhaustiveness of the single-anchor reduction

Any valid 11-column family has at most two support-one
columns on each of the three axes: 3 on one axis would
have 1+3+C(3,2)=7 required different subset sums in
only 5 possible one-coordinate field states.

Thus any valid 11-column family must contain a support-two
vector. The 384-element monomial group S3 acting by
coordinate permutations and the 4^3 independent nonzero
coordinate multipliers preserves all model constraints.
Every support-two vector is in the orbit of (0,1,1).

Therefore existence of ANY 11-column family is equivalent
to existence of one containing the anchor (0,1,1).
The proof does not rely on random search, a heuristic,
or a false use of projective scaling on each column
independently.

The runner tested the complete 384-element action set
and its 48-element support-two orbit against the
original ASET oracle.

## 3. Finite CNF and full checked UNSAT refutation

The source model consists of 60 distinct admissible
nonzero columns. Enumerate all 0/1/2-element index
subsets, bucket their sums, and retain the
inclusion-minimal symmetric differences from each
collision: exactly 9,990 forbidden hyperedges.
No relations with three positive elements alone
are incorrectly declared forbidden.

The exact SAT formula uses:
- 60 Boolean candidate selections;
- a fixed positive unit clause for anchor (0,1,1);
- for each minimal forbidden edge E, the negative
  clause OR_(i in E) NOT x_i;
- fully bi-implicated prefix count wires
  t[i,k] <-> t[i-1,k] OR (x_i AND t[i-1,k-1]);
- final positive unit requiring >=11 selected.

**Frozen formula:** 665 variables; 12,341 clauses.

Both directions of the cardinality recurrence are
encoded, avoiding spurious or lost feasible assignments.
The source model is independently regenerated from
the original prime-field subset sum definition by
research/g2bb2_verify.py, not copied from the solver's
hyperedge builder.

**Result:** PySAT Glucose4 returned UNSAT on this exact
normalized formula. Crucially, a separate
drat-trim checker accepted the resulting COMPLETE
DRUP/DRAT derivation against the regenerated DIMACS
formula. The result was NOT accepted merely from
the solver's status.

Therefore no 11-column family exists. Combined with
the verified 10-column witness, the exact value is 10.

## 4. Cryptographic provenance and reproducibility

The proof-producing hosted run:
https://github.com/definitely-stable/Mathlab/actions/runs/37774499932

Source revision for the first independently verified proof:
704a35937de1bf6cc486aa7307f241efb778790d

The audit at that run printed:
- G2BB2_INDEPENDENT_9990_EDGE_SOURCE_PASS
- G2BB2_INDEPENDENT_UNSAT_PROOF_ACCEPTED
- G2BB2_CERTIFIED_EXACT_10
- G2BB2_VERIFIED_VERDICT EXACT_10

Pinned dataset/model hashes (SHA-256):

    model_source_sha256:
    d045919f0410c1272ea9a2d86196cfd0b1b8a8acbeae0040ca88a0e99cef3829

    problem.cnf sha256:
    548645e741ad29e948670608216e48bbf3ca306b42b049783c89e35569032b5a

Pinned later hosted proof metadata from run 37774701667
(identical source/CNF and verified by independent DRAT checker):

    proof.drat sha256:
    ffbc5fabb0900acf52e72c41304572eea22f9a5d8c6bd19c2377a038d6e2f748
    proof bytes: 24,388,999
    proof lines: 500,980

Solver for the above certificate: python-sat==1.9.dev15,
PySAT Glucose4, Python 3.12, deterministic conflict budget
5,000,000, UNSAT reached inside that budget.
Second implementation: drat-trim source revision
2e3b2dc0ecf938addbd779d42877b6ed69d9a985.
The complete DRUP file is uploaded with the original
DIMACS and decision.json to GitHub Actions as a ZIP
artifact. GitHub artifacts have finite retention and
are NOT claimed permanently archived.

**Reproducibility:** the pinned
.github/workflows/g2bb2-decision.yml regenerates the
problem, calls the pinned solver, independently rebuilds
and bytewise matches the DIMACS/source hashes, and
verifies the entire proof against a pinned source
build of drat-trim. The workflow is configured for both
research branch runs and merged main. The exact proof
and checker result are uploaded as an Actions artifact.
The currently retained certified proof artifact can
be regenerated by rerunning this workflow after expiry.

The mandatory dependency-free research CI separately
checks all original G0/G1A/G2A/G2B/HYP/TOM/catalog
gates and the full anchor protocol. A failed or
interrupted optional solver must retain UNKNOWN and
NEVER remove the independent mathematical result
based on previously verified certificates.

## 5. Distinguish the claims

THEOREM/PROVEN FACT (classical): odd-order weak-Sidon
bound from Roth–Seroussi, 1996. The initial q5 [10,11]
interval was its direct consequence.

DERIVED LEMMA: an 11-column exact ASET family
would have a representative containing (0,1,1).
This is a short elementary group-action argument.

EXACT NUMERICAL RESULT: A_5^set(3,2,2)=10, established
via independently checked UNSAT certificate plus
independent 10-column witness.

HEURISTIC/EMPIRICAL (not proof): earlier incomplete
25,000-node solver runs, SCIP/HiGHS probes and
12,800 local exchanges around one witness. None is
used to justify global infeasibility.

CONJECTURE / NOVELTY: no new general claim follows
from this finite solution. Source-to-model prior-art
audit and G2 theorem selection are separate.

## 6. Next research and engineering actions

- Close G2B-B2 issue #42 ONLY after merged-main
  certificate CI passes; report exact result to #14.
- Preserve historical G2B-A [10,15] and B1 [10,11]
  as provenance, but mark them SUPERSEDED.
- Do not infer analogous q=7, m=3, w=2 value.
- Examine small-case extremal geometry or leading
  constants ONLY against documented prior art.
- Choose G2_SELECT_THEOREM / G2_REDUCE_TARGET /
  G2_NO_SIGNAL explicitly before pursuing G4.
- No release or Rust crate from this result alone.
