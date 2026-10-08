# CURRENT_STATE

Last verified HEAD: main@8027bc64af5c3dcc908b90fd8ec1670526a3b39b

Current milestone: LENT-001 / G2A — exact odd-characteristic extremal lab

Current slice: exact branch-and-bound for q={3,5,7}, d=2, hard support w={1,2}

Implementation branch: research/lent-001-g2a-extremal

Open issue: #12 — LENT-001-G2A: exact odd-characteristic extremal lab

Open PR: pending

Last CI: post-G1B merge run 37745969955 — SUCCESS

Acceptance: G0 = FOUNDATION_PASS; G1A = G1A_ORACLE_PASS; G1B = SPLIT_BY_CHARACTERISTIC; G2A requires all five G2A acceptance markers on latest head

Frozen Phase-A expected maxima: q3/m3/w2 ASET=5 vs linear=3 vs LENT upper=6; q5/m2/w2 ASET=5 vs linear=2 vs LENT upper=6; q7/m2/w2 ASET=7 vs linear=2 vs LENT upper=9

Additional exact baseline: for d=2,w=1, A_q^set(m,1,2)=m*A_q^set(1,1,2), giving m,2m,3m for q=3,5,7

Known constraint: these are exact finite results, not an asymptotic or novelty theorem

Next allowed action: obtain green G2A CI, persist exact witnesses/evidence, then choose G2_SELECT_THEOREM or expand/reduce the grid

Last updated from repository: 2026-10-08
