# CURRENT_STATE

Last verified main snapshot: 76da0af1c7739e2bf6851cc10f6c1ea79609e438 (PR #32 merged; refresh live main before subsequent work)

Current milestone: LENT-001 exact sparse additive-set capacity / HYP-001/002 / independent TOM and cross-repo research catalog

Current slice: HYP-002-B sharp quadratic exponent DERIVED + MERGED; remaining issue #25 is novelty/constants audit. G2B-B issue #14 remains open

Open issues: #1 LENT parent; #14 G2B-B; #15 TOM; #24 HYP-001 novelty; #25 HYP-002 novelty/constants; plus independent catalog issues (verify live list)

Open PR: none at post-merge snapshot (verify live GitHub)

Last CI: PR head research run 37765274674 SUCCESS (68 tests, 61 catalog entries, G0/G1A/G2A/G2B/TOM/HYP-A/HYP-B gates); main post-merge run 37765381532 (verify its live conclusion)

Acceptance: G0 FOUNDATION_PASS; G1A ORACLE_PASS; G1B SPLIT_BY_CHARACTERISTIC; G2A G2_EXPAND_GRID; G2B-A PASS; HYP-001 two-cell derived Theta_q(m^(3/2)); HYP-002 three-cell derived Theta_q(m²); TOM A/B/C exploratory only

Mathematical correction: HYP-002 three-cell quadratic conjecture DISCHARGED. For any finite field q>=2, r=q-1, explicit upper A_q^set(m,3,2) <= r*m+r²*C(m,2)+min[r³*C(m,3),r²*C(m,2)+C(r*m,2)]. For fixed odd q, Steiner triple systems yield matching lower Omega(m²). Previous O_q(m^(5/2)) proof is valid but strictly weaker.

Evidence: docs/research/HYP-002-B-QUADRATIC-THEOREM.md, docs/research/HYP-002-B-EVIDENCE.md, research/hyp002_quadratic.py, research/test_hyp002_quadratic.py, research/lent-001/hyp002-b-protocol.json

Novelty: broad exponent strongly overlaps classical C4-free/2-separable literature; scientific originality NOT established; Lean NOT STARTED; a Rust primitive is NOT authorized without explicit decoder/memory product proof

Known blockers: exact G2B-B q5 optimum still only 10..15; HYP-002 finite leading constants/structure unknown; indexed encoder/decoder worst-case costs unknown; research-specific novelty audit outstanding

Next allowed action: HYP-002-B leading constant/source audit (or STOP_NOVELTY) and efficient bounded-ID decoder feasibility; independently continue G2B-B under #14

Last updated from repository: 2026-10-08
