# CURRENT_STATE

Last verified baseline main: eee8e89e1d844bca9f418587d4c8ddba731c2673 (before G2B-B2 PR; verify live main after merge)

Current milestone: LENT-001 G2 finite extremal research and theorem-selection audit; HYP-001/002, TOM and cross-repo catalog remain independent

Current slice: G2B-B2 — EXACT GF5 maximum 10 independently verified via complete SAT refutation; merge/provenance checkpoint in progress

G2B finite results: A_3^set(4,2,2)=7 (exact G2B-A); **A_5^set(3,2,2)=10** (computer-assisted EXACT NUMERICAL RESULT, independently checked full DRAT proof). Historical GF5 intervals [10,15] (G2B-A) and [10,11] (G2B-B1) are SUPERSEDED.

GF5 proof: 60 candidate support<=2 nonzero vectors, 9990 minimal hyperedges from genuine admissible d=2 subset-sum collisions; exact >=11 CNF normalized with anchor (0,1,1) by 384 coordinate-monomial actions, 665 SAT variables, 12341 clauses. Complete Glucose4 UNSAT proof independently verified by drat-trim at pinned commit 2e3b2dc0ecf938addbd779d42877b6ed69d9a985. Original 10-column family independently checked by G1A.

Proof provenance: source SHA256 d045919f0410c1272ea9a2d86196cfd0b1b8a8acbeae0040ca88a0e99cef3829; CNF SHA256 548645e741ad29e948670608216e48bbf3ca306b42b049783c89e35569032b5a; first pinned full proof SHA256 ffbc5fabb0900acf52e72c41304572eea22f9a5d8c6bd19c2377a038d6e2f748 (24388999 bytes, 500980 lines). Archived original hosted-run evidence: Actions #37774499932 and #37774701667, SUCCESS for independent refutation acceptance.

Canonical report: docs/research/LENT-001-G2B-B2-EXACT10-CERTIFICATE.md. Machine record: research/lent-001/g2bb2-exact10-result.json. Frozen protocol: research/lent-001/g2bb2-sat-protocol.json. Pure-stdlib generator: research/g2bb2_anchor_sat.py; independent verifier: research/g2bb2_verify.py. Separate workflow .github/workflows/g2bb2-decision.yml regenerates proof on research/* and main, uploads SHA-pinned artifacts with finite retention.

Open issues until postmerge check: #42 G2B-B2 exact result closure; #14 parent G2 theorem-level decision; #1 LENT parent; #15 TOM; #24/#25 HYP prior-art audit. Verify live GitHub state.

Open PR: G2B-B2 branch research/g2bb2-anchored-global-sat, verify live GitHub.

Known blockers: general asymptotic theorem ORIGINALITY not established; Lean not started; q7/m3/w2 exact value not investigated; Rust library not authorized. No generalized conclusion from a single finite GF5 exact maximum.

Next allowed action: ensure main CI and independent solver workflow pass on exact merged SHA; close issue #42 with certificate links; then G2 theorem selection based on prior art and product usefulness, not automatic Rust implementation.

Last updated from repository: 2026-10-08
