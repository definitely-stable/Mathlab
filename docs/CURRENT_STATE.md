# CURRENT_STATE

Last verified main snapshot: 2787900cdd7259de363fd73147fa57927dd60afd (HYP-002-C PR #35 merged; always re-read live main)

Current milestone: LENT-001 / G2B; HYP-001/002 capacity; TOM; curated cross-repo research

Current slice: HYP-002-C index-free affine decoder Phase A ACCEPTED; narrow STOP_STANDALONE_DENSE_TWO_ID product decision. Issue #34 CLOSED/completed; G2B-B #14 separately OPEN

Open issues: #1 LENT parent; #14 G2B-B; #15 TOM; #24 HYP-001 prior art; #25 HYP-002 leading constant/novelty. Check live GitHub for changes

Open PR: none at this checkpoint

Last CI: HYP-002-C branch run 37768308956 SUCCESS (77 tests and all decoder, alias, G2B/TOM/catalog gates; registry 61); post-merge main run 37768418282 (verify live conclusion)

Acceptance: G0/G1A/G1B/G2A/G2B-A previous gates; HYP-001 derived Theta_q(m^(3/2)); HYP-002-B derived Theta_q(m²), novelty UNVERIFIED; HYP-002-C exhaustive promised-state decoder PASS with STOP_STANDALONE_DENSE_TWO_ID; TOM A/B/C scouting only

HYP-002-C exact evidence: all 2,79,6904 promised states for ranks 1,2,3; explicit 3-DISTINCT-to-2-ID alias in affine F3²; canonical index-free decoder O(m) dense scan + <=20 algebraic candidate checks; checked update O(m); Python tuple-copy raw update O(m)

Memory gate: m=27, V=117 uses 54 bits with 2-bit packed trits vs 22 bits direct canonical two IDs including occupancy; m=243, V=9801 uses 486 vs 34 bits. Theoretical payload numbers, not heap benchmarks

Authoritative docs: docs/research/HYP-002-C-AFFINE-DECODER-PROTOCOL.md and docs/research/HYP-002-C-EVIDENCE.md. Code: research/affine_two_id.py, test_affine_two_id.py, bench_affine_two_id.py

Known blockers: arbitrary duplicate/overcapacity update histories not reconstructible from trit-only state; no competitive standalone two-ID product; theorem novelty still unknown; G2B GF(5) exact max still 10..15; Lean not started

Next allowed action: return to #14 G2B-B for tight exact proof, or open a separately scoped application-level composable-state / reliable bounds research lane with explicit comparator, not a Rust crate

Last updated from repository: 2026-10-08
