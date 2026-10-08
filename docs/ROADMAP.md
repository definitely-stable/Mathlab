# Mathlab roadmap

## LENT-001 — Locality–Entropy Trilemma

### G0 — Foundation

Status: **COMPLETE — FOUNDATION_PASS**

Completed:

- frozen deterministic exact additive-sketch model;
- claim labels and authority order;
- finite counting theorem recorded without novelty claim;
- exact big-integer checker;
- tiny exhaustive oracle for q in {2,3};
- machine-readable protocol;
- hosted CI;
- Lean plan.

The finite theorem remains the baseline impossibility framework, not the current novelty target.

### G1 — Prior-art closure and model correction

Status: **IN PROGRESS**

G1 has been split because the initial broad novelty map mixed several neighboring but non-equivalent models.

#### G1A — ASET model freeze

Status: **ACTIVE**

Primary object:

\[
A_q^{\mathrm{set}}(m,w,d),
\]

the maximum universe size for bounded-support vectors in \(\mathbb F_q^m\) whose subset sums for all sets of size at most \(d\) are distinct.

Required work:

1. prove the signed-relation equivalence with separate positive/negative side bounds;
2. freeze q=2 equivalence to small-column independence;
3. prove and test the q>2 separation from arbitrary-coefficient linear independence;
4. map Sidon / B_h / dissociated definitions exactly;
5. map update locality to update-efficient coding rather than LCC/LDC query locality;
6. record rate-compatible coding as a warning against a pure nestedness-tax conjecture;
7. record mixed-alphabet counting as a baseline derived result;
8. produce a source-to-claim matrix.

Exit is one of:

- G1A_CONTINUE_ASET;
- G1A_REDUCE_TO_KNOWN_OBJECT;
- G1A_SPLIT_Q3_QGT3;
- G1A_STOP_NOT_NOVEL.

#### G1B — sharp prior-art closure

Status: **BLOCKED ON G1A**

If G1A continues ASET, audit sharp known exponents/constructions for:

- sparse parity-check matrices over finite fields;
- k-dissociated / restricted signed-sum families;
- weak Sidon / B_h variants with distinct summands;
- bounded-weight / Hamming-ball constrained constructions.

Deliverable: source-to-claim matrix with theorem-level parameter maps.

#### G1C — secondary lanes

Status: **BLOCKED ON G1A**

Priority order:

1. nested prefixes + bounded update locality;
2. mixed/nonuniform cells;
3. computation only after an independent computational model is frozen.

Pure nestedness tax is deprioritized.

### G2 — ASET exact oracle and first finite lemmas

Status: **PLANNED / BLOCKED ON G1A**

If G1A exits with CONTINUE_ASET or SPLIT_Q3_QGT3:

- extend the oracle to q in {2,3,5};
- test ASET exactness, signed relations and full small-column independence separately;
- pin explicit q>2 separation witnesses;
- search a bounded q=3 box for separation/equivalence evidence;
- enumerate exact values of \(A_q^{\mathrm{set}}(m,w,d)\) for tiny parameters;
- compare exact values against LENT and sparse-linear baselines.

This stage produces EXACT NUMERICAL RESULT evidence, not an asymptotic novelty claim.

### G3 — baseline formalization

Status: **NOT STARTED**

Lean kernel target:

1. support of a finite sum is contained in the union of supports;
2. support cardinality is subadditive;
3. injectivity gives a cardinality lower bound;
4. Hamming-ball cardinality;
5. finite LENT theorem;
6. signed-relation equivalence for the ASET model.

Entropy approximations remain a separate later layer.

### G4 — new-math lane

Status: **BLOCKED ON G1/G2**

Preferred order:

#### G4A — ASET extremal theorem

Try to obtain a nontrivial bound for

\[
A_q^{\mathrm{set}}(m,w,d)
\]

that is not a direct sparse-parity-check corollary.

Strong success criteria include:

- a new asymptotic exponent;
- a matching upper/lower exponent in a nontrivial regime;
- a provable separation from arbitrary-coefficient sparse linear independence;
- a construction exploiting the restricted signed-relation model.

#### G4B — nested + update-locality tax

Study one common prefix family that must be near-optimal at several capacities while each universe element has bounded update support.

Do not target pure nestedness tax without locality.

#### G4C — mixed alphabets

After prior-art closure, optimize heterogeneous coordinate alphabets under a fixed bit budget and update-locality constraint.

#### G4D — computation tradeoff

Only after defining computation independently from update locality.

Possible models:

- decoding time;
- incremental decoding work;
- cell probes;
- memory probes.

### G5 — manuscript promotion

Status: **NOT STARTED**

A result enters preprints/ only when:

- theorem statement is stable;
- proof is reviewable;
- prior-art classification is complete enough to state novelty honestly;
- verification instructions reproduce;
- formalization status is declared accurately.

## Current priority

\[
\boxed{\text{G1A ASET model freeze} \rightarrow \text{G1B prior-art closure} \rightarrow \text{G2 exact oracle} \rightarrow \text{G4A sharp theorem}}
\]
