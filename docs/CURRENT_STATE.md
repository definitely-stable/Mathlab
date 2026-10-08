# CURRENT_STATE

Last verified HEAD: `main@5f168b26020de61f1b229585d143ab5d05dc4538`

Current milestone: LENT-001 / G1B — hard-support novelty closure

Current slice: Audit 02 — direct BCC/signature-code prior art + characteristic-two block reduction

Implementation branch: `research/lent-001-g1b-audit-02`

Open issue: #6 — LENT-001-G1B: primary-source novelty closure for A_q^set

Open PR: pending

Last CI: main research run `37726769100` — SUCCESS on Audit-01 merge commit

Acceptance: G0 = FOUNDATION_PASS; G1A = G1A_ORACLE_PASS; G1B remains OPEN

Audit-02 result: unconstrained binary ASET is BCC prior art; finite-field bounded-active signature identification is established; characteristic-two ASET reduces exactly to a block-sparse binary short-dependency problem

Primary novelty candidate: sharp zero-error finite-field signature coding under the hard per-signature support bound `|supp(a_i)| <= w`

Known blockers: block-sparse BCC/parity-check asymptotics, exact sparse finite-field/mod-q signatures, bounded-column-weight detecting matrices, support-constrained q-ary B_h/signed-sum families, and fixed-(d,w) sharp results remain unclosed

Next allowed action: merge Audit 02 after latest-head CI, then execute G1B Audit 03 over the remaining hard-support-specific source classes before choosing a v2 G1B exit

Last updated from repository: 2026-10-08
