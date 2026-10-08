# CURRENT_STATE

Last verified main SHA: 49e1df287eee6ed179e4e4b4d64bc568eaaef066 (PR #45 merged, two post-merge CI suites SUCCESS; recheck live HEAD on subsequent turns)

Current milestone: LENT-001 finite odd-field exact sparse ASET research; G2 finite GF5 case completed; G2 theorem/novelty selection PENDING. TOM, HYP and curated external literature remain independent research tracks.

Current slice: G2B-B2 **ACCEPTED EXACT NUMERICAL RESULT**, issue #42 CLOSED/completed; parent #14 OPEN for theorem selection.

Exact results: **A_3^set(4,2,2)=7** (G2B-A) and **A_5^set(3,2,2)=10** (G2B-B2 independently checked full SAT refutation). Earlier GF5 intervals [10,15] and [10,11] are historical and superseded.

GF5 exact proof: 60 nonzero support<=2 candidate columns in F5^3; 9990 minimal forbidden configurations derived from equal 0/1/2 subset sums. Any 11-column family has some support-two vector (each axis supports <=2 one-sparse), and the 384-element coordinate-monomial symmetry group transforms it to (0,1,1). The anchored >=11 exact CNF has 665 variables and 12341 clauses, and the complete DRUP UNSAT refutation was accepted by an independently built pinned drat-trim verifier. Original independent G1A oracle verifies a 10-column witness. This is a computer-assisted **finite** proof only, not an asymptotic theorem or novelty claim.

Frozen source SHA256: d045919f0410c1272ea9a2d86196cfd0b1b8a8acbeae0040ca88a0e99cef3829; CNF SHA256: 548645e741ad29e948670608216e48bbf3ca306b42b049783c89e35569032b5a; complete proof SHA256: ffbc5fabb0900acf52e72c41304572eea22f9a5d8c6bd19c2377a038d6e2f748 (24,388,999 bytes, 500,980 lines).

Last merged CI: standard research #37775586881 — SUCCESS (112 tests, 61-entry cross-repo catalog, new source-literature schema checks, all prior G0/G1A/G2B/HYP/TOM gates). Independent solver + full DRAT proof checker #37775586858 — SUCCESS. Both tested exact merged main SHA 49e1df287eee6ed179e4e4b4d64bc568eaaef066. Complete proof artifact has finite retention; pinned GitHub-hosted workflow regenerates it and verifies the certificate on main.

Canonical evidence: docs/research/LENT-001-G2B-B2-EXACT10-CERTIFICATE.md. Machine result: research/lent-001/g2bb2-exact10-result.json. Frozen protocol: research/lent-001/g2bb2-sat-protocol.json. Independent model/verifier: research/g2bb2_anchor_sat.py, research/g2bb2_verify.py; optional solver research/g2bb2_decide.py.

Open issues at snapshot: #1 LENT parent; #14 G2 theorem-level decision; #15 TOM, #24/#25 HYP originality. Issue #42 is CLOSED. Verify live GitHub for concurrent work.

Open PR: none at the exact-proof merge snapshot; current docs follow-up PR is pending until its CI and merge.

Next allowed action: perform claim-to-primary-source audit for genuinely original support-sensitive theorem candidates, or decide G2_REDUCE_TARGET/G2_NO_SIGNAL. Do NOT infer q7 optimum from q5, assert a new asymptotic theorem, launch a Rust crate, or claim Lean completion.

Last updated from repository: 2026-10-08
