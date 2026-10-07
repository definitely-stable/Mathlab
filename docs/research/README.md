# Research index and authority order

This directory is the canonical mathematical record.

## Authority order

For LENT-001, resolve conflicts in this order:

1. `LENT-001-PROTOCOL.md` — frozen model and admissible claim changes;
2. `LENT-001-CLAIMS.md` — current claim/status registry;
3. `LENT-001-FOUNDATION.md` — definitions, proofs, derivations, caveats;
4. `LENT-001-PRIOR-ART.md` — novelty boundary and literature mapping;
5. `DECISIONS.md` — accepted research decisions;
6. `OPEN-QUESTIONS.md` — unresolved work;
7. older issue/discussion text.

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

No file under `preprints/` should present LENT-001 as new until the G1 prior-art audit closes.
