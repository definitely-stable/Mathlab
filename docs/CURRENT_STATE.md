# CURRENT_STATE

Reference baseline before TOM-003-D2 branch: main fa5998c7aa42879945a3254998f9343e1183eed4 (PR #50 merged on 2026-10-08).
This branch documentation is PRE-MERGE; verify live main/CI before claiming acceptance.

Current priority: falsification-first product/theorem selection. LENT G2 is G2_REDUCE_TARGET for new Rust crate and theorem originality; its finite results are preserved.

Accepted LENT numerical results: A_3^set(4,2,2)=7 and A_5^set(3,2,2)=10. GF5 complete DRUP proof hash ffbc5fabb0900acf52e72c41304572eea22f9a5d8c6bd19c2377a038d6e2f748; the GitHub-hosted independently checked proof workflow remains active on main.

Accepted TOM-003 D1 (#49 CLOSED): classical Moore-state necessary/sufficient retained e-bit result under unconditional overwrites and no external reads; trusted-old threshold-count memory saves space only by charging external validation. STOP_STANDALONE_UNTRUSTED_NO_EFFECT.

TOM-003 D2 (#53 IN REVIEW): externally authenticated old Merkle root **and initial count**, hashed indexed Boolean leaves, exact k-leaf shared helper frontier, verification of old root before applying edits, recomputation of new root/count. Compare trusted bitmap, k independent proofs and standard SSZ-style shared multiproof, and charge setup/retained digests/hash calls/wire fields. Adversarial stale proof/false old/false count tests are mandatory. All primary mechanisms are established; preliminary decision STOP_STANDALONE_MERKLE_UPDATE_CRATE. Independent GitHub CI validation and review/merge required.

Code: research/tom_authenticated_overwrite.py and research/test_tom_authenticated_overwrite.py.
Protocol: docs/research/TOM-003-D2-AUTHENTICATED-OVERWRITE-AUDIT.md.
Parent research: #15. D1 #49 closed, D2 #53 open pending CI.
No original theorem, Lean completion, Rust crate or demonstrated production speedup.

Next: independently complete CI/review/merge, then STOP this broad Merkle primitive direction, retaining the conditional auth cost model as a baseline. Future D3 only after a sharply different operation and verified source gap.

Last updated from GitHub: 2026-10-08.
