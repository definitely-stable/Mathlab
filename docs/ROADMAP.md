# Mathlab roadmap

## LENT-001 — Sparse-Update State-Space Bounds for Exact Additive Set Sketches

### G0 — Foundation

Status: **COMPLETE — FOUNDATION_PASS**

Completed:

- deterministic exact additive-sketch model;
- finite Sparse-Update Hamming-Ball Bound;
- exact arithmetic checker;
- original q={2,3} exhaustive grid;
- claim/evidence discipline;
- GitHub-hosted CI;
- Lean plan.

The finite theorem is a baseline impossibility framework; publication
novelty is not claimed.

Terminology policy: \`LENT-001\` is a stable historical ID. The former
public label "Locality–Entropy Trilemma" is deprecated.

### G1 — model correction and prior-art closure

Status: **IN PROGRESS**

#### G1A — ASET model + exact relation oracle

Status: **IMPLEMENTED / AWAITING LATEST-HEAD CI**

Primary object:

\[
A_q^{\mathrm{set}}(m,w,d).
\]

G1A contains:

1. exact ASET definition;
2. ASET-SIGNED proof with separate positive/negative side bounds;
3. q=2 equivalence with small-column GF(2) independence;
4. q=3 and q=5 strict model-separation witnesses;
5. independent exact checkers for ASET, signed relations and arbitrary
   small-column dependencies;
6. frozen q={2,3,5} exhaustive grid;
7. source-to-claim prior-art matrix.

Acceptance marker:

\`G1A_ORACLE_PASS\`

After acceptance, no asymptotic theorem is started yet.

#### G1B — sharp prior-art closure

Status: **BLOCKED ON G1A ACCEPTANCE**

Audit primary sources for:

- sparse parity-check matrices over finite fields;
- k-dissociated / bounded-order signed-relation families;
- weak Sidon / restricted B_h families with distinct summands;
- bounded-weight / Hamming-ball constrained constructions;
- update-efficient coding where needed for the locality boundary.

G1B must decide exactly one:

- CONTINUE_ASET;
- REDUCE_TO_KNOWN_OBJECT;
- SPLIT_Q3_QGT3;
- STOP_NOT_NOVEL.

This is the actual novelty gate.

#### G1C — secondary lanes

Status: **BLOCKED ON G1B**

Priority order:

1. nested prefixes + bounded update locality;
2. mixed/nonuniform cells;
3. computation only after an independent cost model is frozen.

Pure nestedness tax remains deprioritized.

### G2 — finite ASET extremal evidence

Status: **BLOCKED ON G1B**

If G1B continues ASET:

- enumerate exact small values or lower/upper intervals for
  \(A_q^{\mathrm{set}}(m,w,d)\);
- record extremal witness families;
- compare ASET counts with arbitrary-coefficient sparse-linear baselines;
- identify the smallest parameter regimes where the extremal quantities
  genuinely diverge;
- use exact results to choose a plausible asymptotic theorem.

G2 produces EXACT NUMERICAL RESULT evidence, not a novelty claim by itself.

### G3 — baseline formalization

Status: **NOT STARTED**

Lean targets:

1. support of a finite sum is contained in the union of supports;
2. support cardinality is subadditive;
3. injectivity gives a cardinality lower bound;
4. Hamming-ball cardinality;
5. finite Sparse-Update Hamming-Ball Bound;
6. ASET-SIGNED equivalence;
7. binary small-dependency equivalence.

### G4 — new-math lane

Status: **BLOCKED ON G1B/G2**

#### G4A — sharp ASET theorem

Preferred target if G1B/G2 support it:

\[
A_q^{\mathrm{set}}(m,w,d).
\]

Strong outcomes include:

- a new asymptotic exponent;
- matching upper/lower exponents in a nontrivial regime;
- a sharp provable gap from arbitrary-coefficient sparse linear
  independence;
- a construction that exploits restricted signed relations.

#### G4B — nested + update-locality tax

Study simultaneous near-optimality of one prefix family under bounded
update support.

Do not target pure nestedness tax without locality.

#### G4C — mixed alphabets

Study sharp heterogeneous-cell optimization only after the mixed-alphabet
prior-art map is closed.

#### G4D — computation tradeoff

Only after computation is defined independently from update locality.

### G5 — manuscript promotion

Status: **NOT STARTED**

Promotion requires:

- stable theorem;
- reviewable proof;
- closed novelty boundary;
- reproducible verification;
- explicit formalization status.

## Current priority

\[
\boxed{
\text{G1A oracle acceptance}
\rightarrow
\text{G1B prior-art closure}
\rightarrow
\text{G2 finite extremal evidence}
\rightarrow
\text{G4A sharp theorem}
}
\]
