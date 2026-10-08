# LENT-001-G1A — first implementation plan

Status: **IMPLEMENTED / PR-HEAD ACCEPTED**

Issue: #3

## Objective

Independently test:

1. ASET subset-sum injectivity;
2. bounded signed-relation absence with separate positive/negative limits;
3. arbitrary-coefficient small-column independence.

## Implemented

- prime-field oracle scope q={2,3,5};
- independent \`signed_relation_witness\`;
- independent \`linear_dependency_witness\`;
- preserved G0 q={2,3} grid;
- q=2 equivalence assertions;
- q=3 and q=5 pinned separations;
- d>=2 exhaustive G1A grid;
- ASET-but-not-full-linear counters and witnesses;
- 11 unit tests;
- machine-readable protocol v2;
- \`LENT-001-G1A-PROOF.md\`;
- \`LENT-001-G1A-EVIDENCE.md\`.

## Frozen execution grid

- q=2, m=4, d=2, w=2, max_v=4;
- q=3, m=3, d=2, w=2, max_v=4;
- q=5, m=3, d=2, w=1, max_v=4.

## Acceptance

PR run \`37724834067\` completed successfully and emitted:

- \`G1A_SIGNED_EQUIV_PASS\`;
- \`G1A_Q2_EQUIV_PASS\`;
- \`G1A_Q3_SEPARATION_PASS\`;
- \`G1A_Q5_SEPARATION_PASS\`;
- \`G1A_ORACLE_PASS\`.

All 11 unit tests passed.

The final evidence-only head must also stay green before merge.

## Next step

After merge, enter G1B primary-source closure for sparse parity-check,
k-dissociated, weak-Sidon/restricted-B_h and bounded-support additive
families.

Only G1B can authorize a sharp novelty theorem target.
