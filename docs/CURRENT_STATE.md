# CURRENT_STATE

Last verified baseline HEAD: main@db47787db396d5952e100a003cdcd01d383d3cbf (live snapshot during HYP-002-B work; always verify latest main)

Current milestone: LENT-001 / G2B and HYP-001/002 locality-capacity; independent TOM-001

Current slice: HYP-002-B sharp exponent proof and finite protocol; merge PR #32 after all CI gates; G2B-B remains open

Open issues: #1 LENT parent; #14 G2B-B; #15 TOM; #24 HYP-001 prior-art; #25 HYP-002 theorem novelty/constants audit. Additional research-catalog issues require live search

Open PR: #32 HYP-002-B at this documentation snapshot (verify live GitHub)

Last CI for HYP-002-B code+tests: GitHub research run 37765055502 — SUCCESS on 6e648f431c258f9cdf8f50776baab31b9f84f3c5; 64 unit tests, 51 curated research entries, G0/G1A/G2A/G2B/TOM/HYP-A gates passed

Acceptance: existing G0/G1A/G1B/G2A/G2B-A complete; HYP-001 two-cell derived Theta_q(m^(3/2)); HYP-002 three-cell Theta_q(m²) DERIVED THEOREM, claim novelty UNVERIFIED; TOM A/B/C exploratory only

Mathematical correction: HYP-002 O_q(m^(5/2)) upper bound superseded. For r=q-1 and any finite field q, the explicit bound is A_q^set(m,3,2) <= r*m+r²*C(m,2)+min(r³*C(m,3),r²*C(m,2)+C(r*m,2)). Steiner triple systems give matching Omega(m²) for any fixed odd-characteristic field; quadratic conjecture DISCHARGED.

Evidence: docs/research/HYP-002-B-QUADRATIC-THEOREM.md, docs/research/HYP-002-B-EVIDENCE.md, research/hyp002_quadratic.py, research/test_hyp002_quadratic.py

Known blockers: scientific novelty of broad HYP-002 exponent unlikely/unaudited; exact leading constant unknown; no decoder/resource cost; G2B GF(5) max remains certified 10..15, not exact; Lean not started; no Rust crate authorized

Next allowed action: finish HYP-002-B PR review/merge, then audit model-specific leading constants and decoder costs (or STOP_NOVELTY); independently continue G2B-B under #14

Last updated from repository: 2026-10-08
