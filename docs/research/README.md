# Research index and authority order

## STOP / already known — required pre-research gate

[**Known, proved, stopped and nontransferable research**](KNOWN-AND-STOPPED-RESEARCH.md) · [machine source](KNOWN-AND-STOPPED-RESEARCH.json). 33 source-linked records with scoped dispositions and strict reopening conditions. This **does not** establish an exhaustive global prior-art search, nor does STOP in one workload ban valid different assumptions. Validate with `python research/known_registry.py --check`.


## Four-stage cross-project theorem/prior-art audit (THEOREM-GAP-004)

[Theorem-level transfer and source audit](THEOREM-GAP-004-FOUR-STAGE-AUDIT.md) · [machine-readable source-to-claim matrix](THEOREM-GAP-004-TRANSFER.json). Lefmann (2005) achieves the same *odd-field construction exponents* as HYP-001 and HYP-002 under a stronger four-wise independence condition; Mathlab ASET upper bounds are separate. DeltaMeter/DELSK recommendations preserve existing system STOP and unknown product headroom. This is an audit, not a new theorem.

## Verified external scholarly literature

[Primary literature catalog](catalog/LITERATURE.md) · [papers by research record](catalog/LITERATURE-BY-RESEARCH.md) · [source/model audit I](catalog/LITERATURE-001-AUDIT.md) · [source corrections and expansion II](catalog/LITERATURE-002-SOURCE-AUDIT.md) · [literature.json](catalog/literature.json).

This is a distinct DOI/arXiv-based bibliography of sources cited by or mathematically intersecting Mathlab, DELSK and DeltaMeter, not a theorem authority. LENT G2B-B2 is independently handled under issue #42 and is unchanged by these imports.

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

## G2B-B2 — exact q5 maximum 10, independently checked computer-assisted proof

[Exact GF5 result and full UNSAT certificate provenance](LENT-001-G2B-B2-EXACT10-CERTIFICATE.md).
The complete normalized 11-column SAT formula was refuted by Glucose4,
and the full refutation was accepted by an independently pinned drat-trim
checker. The original 10-column G1A witness is still exact.
**A_5^set(3,2,2)=10: EXACT NUMERICAL RESULT, scientific novelty NOT claimed.**
The former [10,11] interval is now HISTORICAL.

## G2B-B2 — globally sound eleven-column decision reduction (source protocol)

[Single-anchor complete reduction, Tseitin cardinality proof and
SAT/DRAT audit](LENT-001-G2B-B2-A-ANCHORED-SAT-PROTOCOL.md)
for issue #42. Every hypothetical 11-family is isomorphic under a
verified GF(5) coordinate-monomial action to one containing (0,1,1);
the 384 group actions are exhaustively tested. The 60-variable
forbidden-hypergraph model and at-least-11 CNF are regenerated and
independently checked, with **no solver-verdict promotion on timeout**.

## TOM-003 — overwrite-vs-trusted-delta memory boundary

[Source-aware selection and exact finite automata proof](TOM-003-TRUST-BOUNDARY-PROTOCOL.md), issue #49. The classical e-essential-coordinate overwrite lower bound and the conditional log(n+1)-bit trusted-old counter are checked for every n<=3 Boolean function and adversarial invalid-old examples. A false old bit is not detectable from the count alone; external validation is not free. O01-D1 is **STOP as standalone Rust**, O01-D2 remains audit-only. No publication novelty is claimed.

## TOM-003 D2 — authenticated old values and proof reuse cost audit

[Protocol, primary-source matrix and cost accounting](TOM-003-D2-AUTHENTICATED-OVERWRITE-AUDIT.md)
(issue #53). A Merkle root does not authenticate a separately
provided threshold count; both require trusted setup. The standard
SSZ batch helper frontier and recomputation of a new Merkle root
are known. The new dependency-free finite oracle checks exact
structural savings *against naive independent proofs*, and
adversarial stale/corrupt proofs, **not** original mathematical
novelty or improvement over standard SSZ.

## Current status

G1B is closed with \`SPLIT_BY_CHARACTERISTIC\`.

G2A exact evidence is accepted with decision `G2_EXPAND_GRID`.

G2B-A now has genuine m>w evidence: q=3,m=4,w=2 exact V=7 and
q=5,m=3,w=2 originally certified V in [10,15] (CI 37756386646).
The **G2B-B1 classical weak-Sidon reduction** now rigorously tightens
this to **[10,11]**; see [proof and source audit](LENT-001-G2B-B1-WEAK-SIDON-BOUND.md)
and [GitHub-hosted 84-test evidence](LENT-001-G2B-B1-EVIDENCE.md)
and [G2B-A historical evidence](LENT-001-G2B-A-EVIDENCE.md).
The B1 [10,11] interval and local-only obstruction were historical;
B2's complete independently checked UNSAT refutation now rigorously proves
the global exact value V=10 (see the B2 certificate linked above).
G2B-B2 finite q5 exactness is COMPLETE; G2 theorem-selection and
source-level originality audit remain separate. No preprint novelty claim is authorized.

TOM-001-OPPORTUNITY-MAP.md and TOM-001-B/C audits remain separate
scouting/calibration artifacts; TOM-C is STOP as a novelty target.

Any theorem selected by G2 must receive a new theorem-specific prior-art
audit before promotion.
