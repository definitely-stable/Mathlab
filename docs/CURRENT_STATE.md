# CURRENT_STATE

Last verified baseline main HEAD: faac82888596573d49609279f5b012fe87e5a583 (before G2B-B1 branch; re-read live main after merge)

Current milestone: LENT-001 / G2B sparse ASET exact finite research; HYP-001/002 and TOM remain separate

Current slice: G2B-B1 verified classical weak-Sidon upper-bound integration; G2B-B2 remains open

Issue: #14 LENT-G2B ongoing; #1 parent. Do not close G2B until globally exact q5 value or a decision to stop the theorem lane

Open PR: verify live GitHub before continuing (B1 branch research/lent-g2bb-weak-sidon-bound)

Last branch CI: research run 37770881915 SUCCESS (84 tests, catalog 61 entries, all existing G0/G1A/G2B/TOM/HYP stages); repeat on final branch head / merged main

Mathematical result: **10<=A_5^set(3,2,2)<=11**, derived using original 10-column witness and Roth-Seroussi classical weak-Sidon inequality s(s-3)+1<=|F_5^3|=125 with s=V+1. Previous Hamming-ball upper 15 is superseded for this case. GF5 max remains **unknown: 10 or 11**.

Finite result: q3,m4,w2 exact optimum 7 unaffected. q5,m3,w2 has 60 candidates, 9990 forbidden hyperedges, and a 25000-node budget-limited B&B run. Witness from G2B-A independently checked by original ASET oracle. New difference-multiplicity audit passed.

Local-only research: the frozen q5 ten-column witness has no valid eleven-column extension by one addition (50 checks) or deleting one and adding two (12750 checks). This **does not prove that no other eleven-column family exists**.

Proof and evidence: docs/research/LENT-001-G2B-B1-WEAK-SIDON-BOUND.md; docs/research/LENT-001-G2B-B1-EVIDENCE.md; research/lent_weak_sidon.py; research/lent_g2bb_neighborhood.py; research/test_lent_weak_sidon.py

Other accepted decisions: HYP-001 derived theta(m^(3/2)), HYP-002 derived theta(m²) both no novelty claim, HYP-002-C standalone dense two-ID STOP_PRODUCT, Lean not started. Catalog of Mathlab/DELSK/DeltaMeter/openai/math retained

Known blockers: exact GF5 optimum still 10 or 11; G2B-B2 independent global proof or 11 witness required. No scientific novelty or Rust crate authorized

Next allowed action: a separately frozen GF5 11-column existence/infeasibility search with reproducible, independently checkable global certificate; if 11 witness is found independently verify full ASET and close, otherwise do not claim exactness. Remain within GitHub-hosted CI resource constraints

Last updated from repository: 2026-10-08
