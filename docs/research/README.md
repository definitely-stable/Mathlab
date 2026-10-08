# Research index and authority order

This directory is the canonical mathematical record.

## Authority order

For LENT-001, resolve conflicts in this order:

1. `LENT-001-PROTOCOL.md` — frozen G0 model and admissible claim changes;
2. `LENT-001-G1A-PROTOCOL.md` — active G1A ASET model-freeze protocol;
3. `LENT-001-CLAIMS.md` — current claim/status registry;
4. `LENT-001-G1-CORRECTIONS.md` — accepted corrections from the G1 review;
5. `LENT-001-FOUNDATION.md` — definitions, baseline proofs, derivations and caveats;
6. `LENT-001-PRIOR-ART.md` — novelty boundary and literature mapping;
7. `LENT-001-G1A-SOURCE-MATRIX.md` — source-by-source equivalence/implication audit;
8. `DECISIONS.md` — accepted research decisions;
9. `OPEN-QUESTIONS.md` — unresolved work;
10. older issue/discussion text.

Executable artifacts under `research/` validate finite cases and arithmetic. They do not override the mathematical model.

## Evidence classes

- **THEOREM**: general mathematical statement with a complete accepted proof. Lean may still be pending.
- **DERIVED RESULT**: follows from accepted theorem(s), with side conditions stated.
- **EXACT NUMERICAL RESULT**: exact finite computation or exhaustive enumeration.
- **ASYMPTOTIC RESULT**: asymptotic statement only.
- **EMPIRICAL RESULT**: sampled/benchmark/simulation evidence.
- **CONJECTURE**: open statement.
- **PRIOR-ART**: external known result or established mapping.

## Promotion rule

A result may be mathematically correct but still non-novel. Correctness and novelty are separate gates.

No file under `preprints/` should present LENT-001 or ASET as new until the relevant G1 prior-art gate closes.

## Active slice

`LENT-001-G1A` freezes the exact sparse subset-sum object

[
A_q^{\mathrm{set}}(m,w,d)
]

before any sharp theorem search.

The active planning marker is `G1A_MODEL_PLAN_PASS`.
