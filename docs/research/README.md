# Research index and authority order

## Cross-repository evidence catalog (non-authoritative)

[Research index](catalog/INDEX.md) · [thematic navigator](catalog/THEMES.md) · [import review and cross-project discovery](catalog/IMPORT-002-REVIEW.md) · [metadata and maintenance](catalog/README.md) · [registry.json](catalog/registry.json).

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

## Current status

G1B is closed with \`SPLIT_BY_CHARACTERISTIC\`.

G2A exact evidence is accepted with decision `G2_EXPAND_GRID`.

G2B-A now has genuine m>w evidence: q=3,m=4,w=2 exact V=7 and
q=5,m=3,w=2 certified V in [10,15] (CI 37756386646). See
LENT-001-G2B-A-PROTOCOL.md and LENT-001-G2B-A-EVIDENCE.md.
G2B-B remains open until the q=5 gap is audited and a theorem-selection
decision is justified. No preprint novelty claim is authorized.

TOM-001-OPPORTUNITY-MAP.md and TOM-001-B/C audits remain separate
scouting/calibration artifacts; TOM-C is STOP as a novelty target.

Any theorem selected by G2 must receive a new theorem-specific prior-art
audit before promotion.
