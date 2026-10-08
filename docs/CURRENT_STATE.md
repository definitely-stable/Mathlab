# CURRENT_STATE

Last verified HEAD: main@ea4793d64ec73236b20c9a24167d870d8218587d (HYP-001/002 source/evidence merge snapshot; update the SHA from live main on each new status check)

Current milestone: LENT-001 exact sparse additive-set capacity; HYP-001/002 locality-transition research; independent TOM-001

Current slice: G2B-A accepted; G2B-B outstanding; HYP-001/002 Phase A merged (#26)

Open issues: #1 LENT parent; #14 G2B-B; #15 TOM; #24 HYP-001 theorem novelty audit; #25 HYP-002 quadratic exponent conjecture

Open PR: 0 as of HYP-001/002 source merge snapshot (verify live GitHub)

Last CI: research run 37762657184 — SUCCESS on merged main ea4793d64ec73236b20c9a24167d870d8218587d; 49 unit tests, existing G0/G1A/G2A/G2B/TOM gates, 26-entry research catalog, five HYP-001/002 markers

Acceptance: G0 FOUNDATION_PASS; G1A G1A_ORACLE_PASS; G1B SPLIT_BY_CHARACTERISTIC; G2A G2_EXPAND_GRID; G2B-A G2B_PHASE_A_PASS; HYP-001/002 finite construction evidence PASS; TOM A/B/C scouting only

Mathematical results: HYP-001 odd-prime w=2,d=2 has a self-contained derived Theta_q(m^(3/2)) argument using C4-free graph bounds and classical projective incidence; scientific novelty NOT audited. HYP-002 odd-prime w=3,d=2 has derived Omega(m²) and O_q(m^(5/2)) brackets; Theta_q(m²) is an UNPROVEN CONJECTURE.

Finite evidence: PG(2,2) (m14,V21), PG(2,3) (m26,V52), Fano STS(7), affine STS(9) (m9,V12), affine STS(27) (m27,V117); GF(2) Pasch and nonlinear/cycle counterexamples. See docs/research/HYP-001-002-LOCALITY-TRANSITION.md and HYP-001-002-PHASE-A-EVIDENCE.md.

Known blockers: q=5 G2B-B exact optimum unresolved (certified 10..15); HYP-002 quadratic upper unproven; HYP-001/HYP-002 novelty unknown; Lean not started; no Rust crate authorized

Next allowed action: HYP-002 primary-source model-equivalence audit and sharper three-cell upper or superquadratic construction; in parallel G2B-B independent certified search under #14. Keep research gates separate.

Last updated from repository: 2026-10-08
