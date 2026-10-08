# CURRENT_STATE

Last verified HEAD: `main@15c1bf7bb47c5edb3727fd50b27c4044daf4813f`

Current milestone: LENT-001 / G1A — exact ASET relation oracle

Current slice: independently verify ASET exactness, legal signed relations, and arbitrary-coefficient small-column dependence over q={2,3,5}

Implementation branch: `research/lent-001-g1a-oracle`

Open PR: pending

Last CI: merged G1A planning/terminology PR #4 was green; implementation-head CI pending

Acceptance: G0 = FOUNDATION_PASS; G1A planning = G1A_MODEL_PLAN_PASS; G1A execution requires G1A_ORACLE_PASS plus unit tests on latest PR head

Known blockers: publication novelty is still blocked on G1B prior-art closure; general GF(p^k) is intentionally outside the tiny oracle; no sharp asymptotic ASET theorem is authorized yet

Next allowed action: obtain green CI for the exact oracle, review the exact q=3/q=5 separation evidence, then enter G1B source-level novelty closure

Last updated from repository: 2026-10-08
