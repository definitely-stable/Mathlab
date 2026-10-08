# Mathlab roadmap

## LENT-001 — Sparse-Update State-Space Bounds for Exact Additive Set Sketches

### G0 — Foundation

Status: **COMPLETE — FOUNDATION_PASS**

Baseline exact model, finite Sparse-Update Hamming-Ball Bound, exact checker,
hosted CI and verification discipline are established.

### G1 — model correction and prior-art closure

Status: **IN PROGRESS**

#### G1A — ASET model + exact relation oracle

Status: **COMPLETE — G1A_ORACLE_PASS**

Merged as:

\[
\texttt{e435b72fbf7b94f3f514a3f5fbbae88070876525}.
\]

Established:

- exact ASET definition;
- ASET-SIGNED equivalence;
- q=2 equivalence to small-column GF(2) independence;
- q=3/q=5 strict finite separation;
- exact q={2,3,5} comparison oracle;
- exact finite evidence;
- no novelty claim.

#### G1B — primary-source novelty closure

Status: **ACTIVE — AUDIT 01 COMPLETE**

Issue: #6.

Audit 01 verified:

1. Lefmann q-ary sparse parity-check boundary;
2. dissociated/free/h-free terminology;
3. Sidon / \(B_h^*\) / weak-distinct-summand conventions;
4. q=3 Sidon/2-cap mismatch;
5. binary constant-weight \(B_2\) literature;
6. signature/detecting/adder-code literature;
7. additive/quantitative group-testing separability under standard arithmetic.

Audit 02 must close:

1. bounded-column-weight quantitative/additive group testing;
2. finite-field/mod-q bounded-active-user signature codes;
3. q-ary bounded-support Sidon/\(B_h\)/dissociated systems;
4. two-sided h-free / both-side-bounded signed relations;
5. q=3 distinct-summand variants;
6. characteristic-two q>2 behavior.

Allowed exit:

- CONTINUE_ASET;
- REDUCE_TO_KNOWN_OBJECT;
- SPLIT_Q3_QGT3;
- STOP_NOT_NOVEL.

G1B is the publication-novelty gate.

#### G1C — secondary lanes

Status: **BLOCKED ON G1B**

Priority:

1. nested prefixes + bounded update locality;
2. mixed/nonuniform cells;
3. computation only after a separate cost model is frozen.

### G2 — finite ASET extremal evidence

Status: **BLOCKED ON G1B**

If G1B continues ASET:

- enumerate exact small \(A_q^{\mathrm{set}}\) values or intervals;
- persist extremal witness families;
- compare against valid sparse-linear baselines;
- identify the smallest regimes with a provable extremal gap;
- use exact evidence to choose a theorem target.

### G3 — baseline formalization

Status: **NOT STARTED**

Lean targets include the finite Hamming-ball bound, ASET-SIGNED and the
binary equivalence.

### G4 — new-math lane

Status: **BLOCKED ON G1B/G2**

Primary candidate: a sharp theorem for

\[
A_q^{\mathrm{set}}(m,w,d)
\]

in a regime left open by G1B.

Secondary candidates remain nested+locality and mixed alphabets.

### G5 — manuscript promotion

Status: **NOT STARTED**

Requires a stable theorem, reviewable proof, closed novelty boundary,
reproducible evidence and explicit formalization status.

## Current priority

\[
\boxed{
\text{G1B primary-source closure}
\rightarrow
\text{G2 finite extremal evidence}
\rightarrow
\text{G4A sharp theorem}
}
\]
