# Research index and authority order

This directory is the canonical mathematical record.

## Authority order

Terminology: `LENT-001` is a historical stable ID, not an acronym that
should be expanded in new material. Public-facing work uses
**Sparse-Update State-Space Bounds for Exact Additive Set Sketches**.

For LENT-001, resolve conflicts in this order:

1. `LENT-001-PROTOCOL.md` — frozen G0 model;
2. `LENT-001-G1A-PROTOCOL.md` — frozen active G1A execution protocol;
3. `LENT-001-CLAIMS.md` — current claim/status registry;
4. `LENT-001-G1A-PROOF.md` — model-level derived proofs;
5. `LENT-001-G1A-EVIDENCE.md` — exact finite G1A evidence;
6. `LENT-001-G1-CORRECTIONS.md` — accepted G1 corrections;
7. `LENT-001-FOUNDATION.md` — baseline theorem and derivations;
8. `LENT-001-PRIOR-ART.md` — novelty boundary;
9. `LENT-001-G1A-SOURCE-MATRIX.md` — source-by-source mapping;
10. `DECISIONS.md`;
11. `OPEN-QUESTIONS.md`;
12. older issue/discussion text.

Executable artifacts under `research/` validate finite cases and arithmetic.
They do not override the mathematical model.

## Evidence classes

- **THEOREM**: general statement with a complete accepted proof.
- **DERIVED RESULT**: follows from accepted theorem(s) with side conditions.
- **EXACT NUMERICAL RESULT**: exact finite computation/exhaustive enumeration.
- **ASYMPTOTIC RESULT**: asymptotic statement only.
- **EMPIRICAL RESULT**: sampled/benchmark/simulation evidence.
- **CONJECTURE**: open statement.
- **PRIOR-ART**: external known result or established mapping.

## Promotion rule

Correctness and novelty are independent gates.

No file under `preprints/` may present ASET as new until G1B prior-art
closure authorizes a novelty target.

## Active transition

G1A exact model/oracle work is implemented and has passed the code-head PR
CI. The evidence commit must remain green before merge.

The next research gate after merge is G1B primary-source novelty closure.
