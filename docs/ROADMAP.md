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

Status: **ACTIVE — G2A COMPLETE / G2B REQUIRED**

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

G2B priority:

1. q=3,m=4,d=2,w=2;
2. q=5,m=3,d=2,w=2;
3. q=7,m=3,d=2,w=2 only after solver improvement.

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
