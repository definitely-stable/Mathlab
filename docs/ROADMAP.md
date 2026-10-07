# Mathlab roadmap

## LENT-001 — Locality–Entropy Trilemma

### G0 — Foundation

Status: **IN PROGRESS**

Deliverables:

- frozen additive-sketch model;
- claim labels and authority order;
- finite counting theorem recorded without novelty claim;
- exact big-integer checker;
- tiny exhaustive oracle for `q in {2,3}`;
- machine-readable protocol;
- hosted CI;
- Lean plan.

Exit: `FOUNDATION_PASS`.

### G1 — Prior-art closure

Status: **BLOCKED ON G0**

Required audits:

1. binary sparse parity-check matrices / bounded column weight;
2. bounded-weight Sidon / B_h / separable-set formulations;
3. q-ary restricted `{-1,0,1}` dependencies;
4. locally updatable codes/sketches;
5. PinSketch/Minisketch model mapping;
6. Stuffed IBLT randomized model mapping;
7. nested/rate-compatible reconciliation literature.

Exit is one of:

- `STOP_NOT_NOVEL`;
- `BASELINE_ONLY`;
- `CONTINUE_QARY`;
- `CONTINUE_NESTED`;
- `CONTINUE_JOINT_LOWER_BOUND`.

### G2 — Proof package

Status: **NOT STARTED**

Targets:

- complete finite proof with all degenerate cases;
- q-ary entropy corollary with exact side conditions;
- fixed-alphabet near-optimal locality lower bound;
- carefully stated alphabet-growth consequence;
- prefix/nested corollary under a frozen prefix-locality definition.

### G3 — Formalization

Status: **NOT STARTED**

Lean kernel target:

1. support of a finite sum is contained in the union of supports;
2. support cardinality is subadditive;
3. injectivity gives a cardinality lower bound;
4. Hamming-ball cardinality;
5. finite LENT theorem.

Entropy approximations are a separate later layer.

### G4 — Extremal/new-math lane

Status: **NOT STARTED**

Do not default to the binary extremal function: it substantially overlaps known sparse parity-check-matrix work.

Candidate directions only after G1:

- q-ary restricted-coefficient extremal function;
- sharp nested-prefix lower bound;
- nonuniform-cell alphabet/locality theorem;
- matching construction for a genuinely unclaimed regime;
- computation + communication + locality lower bound under a frozen decoder model.

### G5 — Manuscript promotion

Status: **NOT STARTED**

A result enters `preprints/` only when:

- theorem statement is stable;
- proof is reviewable;
- prior-art classification is complete enough to state novelty honestly;
- verification instructions reproduce;
- formalization status is declared accurately.
