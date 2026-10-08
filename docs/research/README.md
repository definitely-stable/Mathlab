# Research index and authority order

## Cross-repository evidence catalog (non-authoritative)

[OM-116/OM-140 theorem transfer audit](TOM-002-OM116-OM140-THEOREM-AUDIT.md) · [Research index](catalog/INDEX.md) · [thematic navigator](catalog/THEMES.md) · [import review and cross-project discovery](catalog/IMPORT-002-REVIEW.md) · [OpenAI Math source audit](catalog/IMPORT-003-OPENAI-PRIMARY-AUDIT.md) · [metadata and maintenance](catalog/README.md) · [registry.json](catalog/registry.json).

The catalog indexes selected, commit-pinned results from Mathlab, Shift-lab/DELSK, DeltaMeter and openai/math. It is **a navigator, not a new proof authority**: the source-specific protocols and decisions below remain canonical. External author claims are not independently validated.


This directory is the canonical mathematical record.

Terminology: \`LENT-001\` is a stable historical ID. Public-facing work uses
**Sparse-Update State-Space Bounds for Exact Additive Set Sketches**.

## Authority order

1. \`LENT-001-PROTOCOL.md\`
2. \`LENT-001-G1A-PROTOCOL.md\`
3. \`LENT-001-CLAIMS.md\`
4. \`LENT-001-G1B-AUDIT-03-FINAL.md\` — final G1B decision
5. \`LENT-001-G1B-SOURCE-MATRIX.md\`
6. \`LENT-001-G1A-PROOF.md\`
7. \`LENT-001-G1A-EVIDENCE.md\`
8. \`LENT-001-G1B-CHAR2-REDUCTION.md\`
9. \`LENT-001-G1B-CHAR2-BOUNDS.md\`
10. \`LENT-001-PRIOR-ART.md\`
11. \`DECISIONS.md\`
12. \`OPEN-QUESTIONS.md\`
15. older audit/issues/discussion text.

Executable artifacts verify finite mathematics; they do not establish
publication novelty.

## HYP-001/002 locality-capacity research (independent G2 lane)

[Mathematical claim ledger, derivations, adversarial tests and prior-art map](HYP-001-002-LOCALITY-TRANSITION.md)
tracks HYP-001 issue #24 and HYP-002 issue #25. HYP-001 has a derived
Theta_q(m^(3/2)) proof based on classical C4-free graphs. HYP-002
now has a **DERIVED sharp Theta_q(m²) theorem** via a finite prefix-fiber
C4-free bound; see [Phase B correction](HYP-002-B-QUADRATIC-THEOREM.md).
The old O(m^(5/2)) upper is superseded, and the quadratic CONJECTURE
has been discharged. Novelty of either exponent has NOT been established.

The finite evidence is recorded in
[HYP-001-002-PHASE-A-EVIDENCE.md](HYP-001-002-PHASE-A-EVIDENCE.md)
(CI #37762380556: 49 tests, valid projective/Steiner witnesses).
The machine-frozen finite test protocol is
`research/lent-001/hyp001-002-protocol.json`. The finite construction
oracle is `research/locality_transition.py`.

## HYP-002-C — bounded two-ID affine decoder / cost audit

[Affine two-ID proof, overload counterexample and product gate](HYP-002-C-AFFINE-DECODER-PROTOCOL.md)
(issue #34) demonstrates O(m) table-free decoding under the strict
<=2 distinct-active-ID promise, but also a 3-versus-2 exact collision
that makes overload detection impossible from the trits alone.
Physical dense-state costs must be compared against directly storing
two canonical IDs. No new Rust crate or originality is implied.

## G2B-B2 — globally sound eleven-column decision reduction

[Single-anchor complete reduction, Tseitin cardinality proof and
SAT/DRAT audit](LENT-001-G2B-B2-A-ANCHORED-SAT-PROTOCOL.md)
for issue #42. Every hypothetical 11-family is isomorphic under a
verified GF(5) coordinate-monomial action to one containing (0,1,1);
the 384 group actions are exhaustively tested. The 60-variable
forbidden-hypergraph model and at-least-11 CNF are regenerated and
independently checked, with **no solver-verdict promotion on timeout**.

## Current status

G1B is closed with \`SPLIT_BY_CHARACTERISTIC\`.

G2A exact evidence is accepted with decision `G2_EXPAND_GRID`.

G2B-A now has genuine m>w evidence: q=3,m=4,w=2 exact V=7 and
q=5,m=3,w=2 originally certified V in [10,15] (CI 37756386646).
The **G2B-B1 classical weak-Sidon reduction** now rigorously tightens
this to **[10,11]**; see [proof and source audit](LENT-001-G2B-B1-WEAK-SIDON-BOUND.md)
and [GitHub-hosted 84-test evidence](LENT-001-G2B-B1-EVIDENCE.md)
and [G2B-A historical evidence](LENT-001-G2B-A-EVIDENCE.md).
The exact q=5 optimum remains UNPROVED; local 10-witness extension
failure cannot establish global infeasibility of V=11.
G2B-B remains open until the q=5 gap is audited and a theorem-selection
decision is justified. No preprint novelty claim is authorized.

TOM-001-OPPORTUNITY-MAP.md and TOM-001-B/C audits remain separate
scouting/calibration artifacts; TOM-C is STOP as a novelty target.

Any theorem selected by G2 must receive a new theorem-specific prior-art
audit before promotion.
