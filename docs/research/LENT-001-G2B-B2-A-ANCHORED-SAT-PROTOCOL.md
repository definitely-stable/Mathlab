# G2B-B2-A — global 11-column GF(5) ASET SAT decision protocol

**Date:** 2026-10-08. **Status:** MODEL / CERTIFICATE FOUNDATION, not exact optimum.
Issue #42, parent issue #14. Baseline: 10 <= A_5^set(3,2,2) <= 11,
from a 10-column exact witness and the classical weak-Sidon bound.

## 1. Critical distinction: witness versus refutation

**SAT proof:** one valid 11-column family (11 distinct nonzero GF5^3
vectors, support <=2, all subset sums for 0,1,2 distinct), checked
against the independent original G1A oracle, proves exact optimum 11.

**UNSAT proof:** an externally reported no-solution verdict is NOT
evidence of exact optimum 10. It must be accompanied by a complete
machine-checkable DRAT/DRUP refutation of the *full normalized*
11-column CNF, accepted by an independent verifier whose input CNF
is checked against the precise original ASET model. Timed-out solver,
failed hillclimber, exhausted *local* one-exchange neighborhood or
unchecked CP-SAT/MILP status cannot establish impossibility.

**UNKNOWN:** maintain [10,11] and explicitly label exactness unresolved.

## 2. Proof of an exhaustive single-anchor reduction

There are exactly 60 nonzero vectors with support <=2 in GF5^3:
12 supported on one coordinate axis, and 48 supported on two.

**Lemma 1 (per-axis cap).** In an ASET-exact d=2 family, no
three vectors can be supported entirely on the SAME coordinate
axis: they alone would require 1+3+C(3,2)=7 distinct subset
sums but have only q=5 possible scalar states on that axis.
Therefore each axis contains <=2 selected columns, and all
support-one columns together number at most 6.

**Lemma 2 (transitivity).** The group H of coordinate permutations
and independent multiplication of each output coordinate by
an element of GF(5)^* has 3!*4^3=384 elements. All actions are
invertible diagonal/permutation linear maps and preserve
coordinate support, field addition, collisions of admissible
subset sums, and family cardinality.

Every support-two vector is in the H-orbit of (0,1,1):
move its two nonzero coordinate positions to 1,2 and
scale their nonzero coefficients to 1.

**Corollary.** Any hypothetical exact family of 11 columns
must include a support-two vector by Lemma 1; applying Lemma 2
produces an isomorphic valid family containing the **single
canonical anchor a=(0,1,1)**. Therefore a *globally exhaustive*
feasibility search can fix selection variable x_a=1. This is
not a heuristic restriction and never excludes the only
possible witness or a proof of UNSAT.

**Non-symmetries:** adding a fixed translation, mixing
coordinates by arbitrary GL(3,5), or identifying projective
scalar multiples of distinct columns is NOT authorized.
The executable tests audit the full orbit (48 points), all
384 actions, and preservation of the original G1A oracle
on a valid 10-column family.

## 3. Exact model and CNF encoding

Let x_i be Boolean for each lexicographically ordered candidate
column i. Enumerate all index sets A of size 0,1,2, including empty;
whenever distinct A and B have equal modular vector sums, the
symmetric difference E=A XOR B is a forbidden hyperedge.
Keep only inclusion-minimal E; the frozen target contains 9,990
edges and 60 vertices. Never forbid the legal all-positive
GF7 relation 1+2+4=0 in the d=2 model.

Every forbidden hyperedge contributes

    OR_(i in E) NOT(x_i).

The anchor adds unit clause x_(0,1,1). Enforce count(x)>=11
using the exact prefix-threshold recurrence

    t[i,k] <=> (t[i-1,k] OR (x_i AND t[i-1,k-1])),

with t[i,0]=TRUE and t[0,k>=1]=FALSE and final unit t[60,11].
All gates use *full bi-implication Tseitin clauses*, not a
one-way cardinality relaxation. For every assignment of the 60
original choices there is precisely one correct auxiliary
extension, and the CNF is satisfiable iff that assignment
contains the anchor, includes >=11 vectors, and avoids every
forbidden edge. Reducing a larger selected family to any
11-element subfamily including the anchor is safe because
ASET exactness is hereditary.

Small grid CNF truth tables are exhaustively compared against
the independent original ASET oracle. The independent verifier
also enumerates the q=5 full 60-vector forbidden incidence
from the modular states without importing the hypergraph
builder. A solver result is not its own verifier.

## 4. Three-stage evidence and integrity

1. **Mandatory standard-library CI:** generate the pinned CNF,
   check all 384 actions, anchor orbit and exhaustive small model
   equivalence; independently reconstruct all 9,990 forbidden edges;
   reject modified SAT/UNSAT/UNKNOWN payloads.
2. **Optional GitHub-hosted SAT experiment:** install pinned PySAT
   Glucose4, run a bounded conflict budget with proof logging,
   emit a JSON manifest with solver version, budget, GitHub SHA,
   exact source hash, exact DIMACS hash and status. Only SAT,
   UNSAT or UNKNOWN are permitted.
3. **Independent decision verifier:** a SAT result is checked
   twice using original G1A subset sums and a separate direct
   state-set enumerator. An UNSAT result is NOT promoted unless
   the complete original CNF is bytewise regenerated and an
   independent drat-trim verifier accepts the emitted proof.
   Missing verifier, truncated proof, or timeouts fail closed.

The optional solver may consume many conflicts without solving
the problem. Such an outcome is still a valid complete *protocol
slice*, not a mathematical exactness milestone.

## 5. Reproducible artifacts

- research/g2bb2_anchor_sat.py — symmetry + exact standard-library
  CNF builder and canonical DP threshold extension
- research/g2bb2_decide.py — optional proof-producing bounded PySAT
  solver (not a claim of completion on timeout)
- research/g2bb2_verify.py — independent incidence replay and
  SAT witness/UNSAT DRAT fail-closed verifier
- research/test_g2bb2_anchor_sat.py — exhaustive small CNF
  truth tables and all coordinate-monomial transformations
- research/test_g2bb2_certificate.py — independent source construction,
  fake SAT/UNSAT and UNKNOWN tampering regressions
- research/lent-001/g2bb2-sat-protocol.json — frozen machine scope
- .github/workflows/g2bb2-decision.yml — GitHub-hosted optional
  bounded SAT; no self-hosted runner or local action by user

**Prior art / tooling:** Roth–Seroussi, Location-correcting
codes (1996), DOI 10.1109/18.485724. The external proof-producing
solver interface and conflict-budget semantics are documented in
PySAT: https://pysathq.github.io/docs/api/solvers.html .
Independent DRAT checker: https://github.com/marijnheule/drat-trim .
None of these are Mathlab's scientific novelty claims.

## 6. Decision gate

B2-A passes when standard-library symmetry/cardinality tests
and independent full-source reconstruction pass in GitHub CI.
The optional solver must report its exact achieved status.

B2-B is complete ONLY after:
- SAT: 11 vectors independently checked, hence exact 11; or
- UNSAT: independently validated complete proof, hence exact 10.

If neither happens, **retain 10 <= A_5^set(3,2,2) <= 11**,
keep issue #42 OPEN, and assess structural/difference-count
constraints or symmetry-stabilized orbit partitions instead.
No new theorem novelty, Lean result, G4 selection or Rust
crate is authorized by an unfinished SAT experiment.
