# Mathlab roadmap

## LENT-001 — Sparse-Update State-Space Bounds for Exact Additive Set Sketches

### G0 — Foundation

Status: **COMPLETE — FOUNDATION_PASS**

Baseline state-space/Hamming-ball theorem and verification infrastructure are
established.

### G1 — model and prior-art closure

Status: **COMPLETE**

#### G1A — exact ASET model + oracle

Status: **COMPLETE — G1A_ORACLE_PASS**

#### G1B — primary-source novelty closure

Status: **COMPLETE — SPLIT_BY_CHARACTERISTIC**

Final classification:

- q=2: stop primary novelty lane;
- characteristic two q>2: secondary block-sparse coding lane;
- q=3: continue as odd-characteristic side-bound testbed;
- odd q>3: continue as primary hard-support lane.

Broad ASET/signature existence is known prior art. Only a theorem that uses
hard support \(w\) essentially remains eligible.

### G2 — odd-characteristic finite extremal evidence

Status: **ACTIVE — G2A COMPLETE / G2B-A HOSTED EVIDENCE ACCEPTED / G2B-B OPEN**

Initial fields:

\[
q\in\{3,5,7\}.
\]

Initial capacity/support grid:

\[
d=2,\qquad w\in\{1,2,3\}.
\]

Phase A exact harness is accepted in issue #12. Decision: **G2_EXPAND_GRID**.

Phase-A warning: q=5,m=2,w=2 and q=7,m=2,w=2 have w=m, so those cases do
not exercise hard support. G2B must move to m>w before theorem selection.

G2B-A hosted evidence (run 37756386646):

1. q=3,m=4,d=2,w=2: **exact ASET maximum V=7**, certified exhaustive search;
2. q=5,m=3,d=2,w=2: **certified interval 10 <= V <= 15**; node-budget exhausted, exact maximum UNKNOWN;
3. q=7,m=3,d=2,w=2: deferred until solver review.

G2B-B is still OPEN. Shrink/close the q=5 gap through independently audited exact search or certificate. Keep the mathematical model correction: a+b+c=0 is not by itself forbidden for d=2; only collisions of admissible subsets generate forbidden hyperedges.

Tasks:

1. compute exact values or certified intervals for
   \(A_q^{set}(m,w,2)\) for the largest feasible small m;
2. persist extremal witness families;
3. compare against the finite Hamming-ball upper bound;
4. compare against stronger arbitrary-coefficient sparse-linear
   constructions/bounds only in valid directions;
5. detect whether q=3 and q≥5 show different exponent/structure;
6. choose one precise asymptotic theorem target.

G2 must terminate in either:

- G2_SELECT_THEOREM;
- G2_NO_SIGNAL;
- G2_REDUCE_TARGET;
- G2_STOP.

G2B-A supporting record: docs/research/LENT-001-G2B-A-PROTOCOL.md and
LENT-001-G2B-A-EVIDENCE.md. Phase-A acceptance markers do **not** close G2B.

### G3 — formalization

Status: **NOT STARTED**

Lean priorities:

- finite Hamming-ball bound;
- ASET-SIGNED;
- binary equivalence;
- characteristic-two reduction/sandwich.

### G4 — theorem lane

Status: **BLOCKED ON G2**

Any G4 theorem must be support-sensitive and odd-characteristic unless G2
provides compelling contrary evidence.

### G5 — manuscript promotion

Status: **BLOCKED**

Requires theorem proof, theorem-level novelty re-audit, reproducible evidence
and explicit formalization status.

## TOM-001 — independent falsification-first theorem scouting

Status: **PHASE A/B/C COMPLETE; NO NOVEL THEOREM SELECTED** (issue #15).

- 14 ideas mapped at Phase A; O01/O02/O04/O06 audited against source models.
- O02 naive no-effect certificate conjunction refuted; broad O04 stopped as novelty.
- TOM-001-C exact one-edit/zero-probe certificate state quotient accepted as
  an elementary baseline, **STOP** as a novelty target.
- Any next O01 must charge input probes, metadata construction/maintenance,
  repeated updates, certificate size and fallback; independent from LENT G2B.

## Current priority

\[
\boxed{
\text{G2 odd-characteristic exact extremal evidence}
\rightarrow
\text{specific theorem selection}
\rightarrow
\text{G4 proof}
}
\]
