# Mathlab roadmap

## LENT-001 — Sparse-Update State-Space Bounds for Exact Additive Set Sketches

### G0 — Foundation

Status: **COMPLETE — FOUNDATION_PASS**

The finite Sparse-Update Hamming-Ball Bound, exact model, arithmetic checker,
CI discipline and formalization plan are established.

### G1 — model correction and prior-art closure

Status: **IN PROGRESS**

#### G1A — exact ASET model + oracle

Status: **COMPLETE — G1A_ORACLE_PASS**

Established exact signed-relation semantics, q=2 equivalence, q=3/q=5 model
separations and exact q={2,3,5} evidence.

#### G1B — primary-source novelty closure

Status: **ACTIVE — AUDIT 03 STARTED**

Issue: #6.

Audit 01 established the sparse parity-check, dissociated/free, Sidon/B_h,
constant-weight B2, ordinary signature/detecting and additive group-testing
neighborhood.

Audit 02 adds two decisive results:

1. **unconstrained binary ASET is already Bounded-Contention Coding**;
2. **finite-field bounded-active identity recovery from signature sums is
   already established signature-code prior art**.

It also proves the structural reduction

\[
q=2^s
\quad\Longrightarrow\quad
\text{block-sparse binary BCC/parity-check formulation}.
\]

Therefore G1B no longer asks whether ASET-like coding is new. It asks whether
the **hard support-constrained sharp frontier** is already known.

Audit 03 is frozen as the final source gate and must close:

1. block-sparse BCC/parity-check extremal results;
2. zero-error hard-sparse finite-field/mod-q signature codes;
3. bounded-column-weight additive/quantitative detecting matrices;
4. support-constrained q-ary \(B_h\)/signed-sum families;
5. fixed-\((d,w)\) sharp asymptotics.

Characteristic two carries the valid sandwich

\[
A_2(m,w,d)
\le
A_{2^s}^{\mathrm{set}}(m,w,d)
\le
A_2(sm,sw,d).
\]

Any characteristic-two novelty target must therefore sharpen or exploit the
block structure beyond ordinary binary sparse-code baselines.

Allowed G1B v2 exits:

- CONTINUE_SPARSE_ASET;
- REDUCE_TO_KNOWN_SPARSE_SIGNATURE;
- SPLIT_BY_CHARACTERISTIC;
- STOP_NOT_NOVEL.

#### G1C — secondary lanes

Status: **BLOCKED ON G1B**

Nested+update-locality and mixed alphabets remain secondary. Computation
remains deferred until independently modeled.

### G2 — finite hard-support extremal evidence

Status: **BLOCKED ON G1B**

If G1B keeps a sparse frontier alive:

- enumerate small exact \(A_q^{set}(m,w,d)\) values or intervals;
- persist extremal support-constrained witness families;
- compare against the strongest valid BCC/parity-check/signature baselines;
- separate characteristic-two and odd-characteristic regimes;
- use exact evidence to choose a theorem target.

### G3 — baseline formalization

Status: **NOT STARTED**

Lean targets include the Hamming-ball theorem, ASET-SIGNED, binary
equivalence, and characteristic-two block reduction.

### G4 — new-math lane

Status: **BLOCKED ON G1B/G2**

A future G4A theorem must be explicitly support-sensitive. A theorem about
bounded-active identification that does not use \(w\) essentially is no
longer a valid novelty target.

### G5 — manuscript promotion

Status: **NOT STARTED**

Requires stable theorem, reviewable proof, closed novelty boundary,
reproducible evidence, and explicit formalization status.

## Current priority

\[
\boxed{
\text{G1B Audit 03: hard-support closure}
\rightarrow
\text{G2 finite sparse extremal evidence}
\rightarrow
\text{G4A support-sensitive theorem}
}
\]
