# CURRENT_STATE

Last verified main HEAD: d11c339e957dd6496edacf0f3b45b02f3af3199c (PR #40 merged on 2026-10-08; re-read live main on next turn)

Current milestone: LENT-001 / G2B sparse ASET exact finite research; independent HYP and TOM

Current slice: G2B-B1 weak-Sidon upper bound ACCEPTED, merged; G2B-B2 global GF5 11-column decision NEXT

Open issues: #14 LENT G2B continuation; #1 parent; #15 TOM; #24 HYP-001 novelty; #25 HYP-002 audit (verify live GitHub)

Open PR: none at this post-merge snapshot; verify live on future turns

Last CI: main research run 37771443375 — SUCCESS on d11c339e957dd6496edacf0f3b45b02f3af3199c. PR head run 37771326021 — SUCCESS (91 unit tests, cross-repo catalog 61 entries, all existing G0/G1A/G2B/HYP/TOM and new G2B-B1 gates)

Mathematical result: **10<=A_5^set(3,2,2)<=11**, q5,m3,w2,d2; q=5 field has 125 states. Classical Roth-Seroussi weak-Sidon inequality applied to S={0} union ASET C gives V<=11. Frozen ten-column ASET witness independently valid; old [10,15] is superseded. **Exact maximum 10 or 11 is NOT known**.

Finite evidence: 60 candidates, 9990 minimal forbidden hyperedges, 25000-node B&B limit, search_exhausted=False, exact=False; [10,11] rigorous by an external mathematical upper. 50 direct additions and 12750 one-delete/two-add attempts around original ten-column witness failed, but this is **local-only**, not a global impossibility certificate.

Proof: docs/research/LENT-001-G2B-B1-WEAK-SIDON-BOUND.md. CI artifact: docs/research/LENT-001-G2B-B1-EVIDENCE.md. Programs: research/lent_weak_sidon.py, research/lent_g2bb_neighborhood.py, research/test_lent_weak_sidon.py and updated research/lent_hypergraph.py.

Known blockers: GF5 global V=11 feasibility unresolved; G2B-B2 requires independently auditable global proof, not timer-based assumption; HYP-001/002 exponents overlap prior art, Lean not started, Rust crate not authorized.

Next allowed action: G2B-B2 frozen independent 11-column SAT/CP/exhaustive feasibility protocol. Success via any independently validated exact 11 witness; failure only via globally complete, independently checked impossibility certificate. All CI on GitHub-hosted runners, preserve TOM/catalog changes.

Last updated from repository: 2026-10-08
