# LENT-001-G1A — first implementation plan

Status: **IMPLEMENTED / AWAITING CI ACCEPTANCE**

Issue: #3

## Objective

Independently test three properties on a tiny exact grid:

1. ASET subset-sum injectivity;
2. bounded signed-relation absence with separate positive/negative limits;
3. arbitrary-coefficient small-column independence.

## Implemented

- prime-field oracle scope q={2,3,5};
- independent \`signed_relation_witness\`;
- independent \`linear_dependency_witness\`;
- preserved G0 q={2,3} grid;
- q=2 equivalence assertions;
- q=3 pinned separation;
- q=5 pinned separation;
- d>=2 exhaustive G1A cases;
- ASET-but-not-full-linear counters and first witnesses;
- unit tests for signed equivalence, implication, separations and d=0;
- machine-readable protocol v2;
- proof note \`LENT-001-G1A-PROOF.md\`.

## Frozen execution grid

- q=2, m=4, d=2, w=2, max_v=4;
- q=3, m=3, d=2, w=2, max_v=4;
- q=5, m=3, d=2, w=1, max_v=4.

## Acceptance markers

\`G1A_SIGNED_EQUIV_PASS\`

\`G1A_Q2_EQUIV_PASS\`

\`G1A_Q3_SEPARATION_PASS\`

\`G1A_Q5_SEPARATION_PASS\`

\`G1A_ORACLE_PASS\`

## Non-goals

This slice does not:

- claim an asymptotic ASET theorem;
- claim publication novelty;
- implement GF(p^k) for k>1;
- optimize brute-force search;
- begin Lean formalization;
- revive pure nestedness tax.

## Next step after green CI

G1B primary-source closure for sparse parity-check,
k-dissociated, weak-Sidon/restricted-B_h and related bounded-support
families.

Only G1B can authorize a sharp novelty theorem target.
