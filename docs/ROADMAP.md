# Mathlab roadmap

**No-repeat research gate (2026-10-08):** [40 source-linked already-known, proved, superseded and STOP entries](research/KNOWN-AND-STOPPED-RESEARCH.md) (and [JSON](research/KNOWN-AND-STOPPED-RESEARCH.json)) are normative before selecting any new theorem, reopening a paper claim or starting a Rust crate. DEFER and narrow prior-art overlap do not imply impossibility of all variants. Historical G2A/G2B descriptions below retain provenance; current G2 priority is REDUCE_TARGET, with no novel G4 claim or Rust product selected.


## TOM-005 — seven independent cross-domain proof kernels

**Seven of seven narrowly frozen general claims have self-contained mathematical proofs**, with independent finite exhaustive regression models, and closest published primary sources explicitly mapped. **Novel scientific theorem claims: ZERO.** The seven include interval stopping, Pareto pruning, shortest-path patch routing, optimal fail-fast check ordering, crash-safe immutable generation publication, exact fingerprint bit capacity, and output materialization fanout. See [TOM-005 proof and counterexample audit](research/TOM-005-SEVEN-THEOREM-AUDIT.md). Status pending exact GitHub-hosted CI acceptance at branch and final main. No crate permitted from elementary known results alone.

## LENT-001 — Sparse-Update State-Space Bounds for Exact Additive Set Sketches

### G0 — Foundation

Status: **COMPLETE — FOUNDATION_PASS**

Baseline state-space/Hamming-ball theorem and verification infrastructure are
established.

### G1 — model and prior-art closure

Status: **COMPLETE**

#### G1A — exact ASET model + oracle

Status: **COMPLETE — G1A_ORACLE_PASS**

#### G1B — primary-source novelty closure

Status: **COMPLETE — SPLIT_BY_CHARACTERISTIC**

Final classification:

- q=2: stop primary novelty lane;
- characteristic two q>2: secondary block-sparse coding lane;
- q=3: continue as odd-characteristic side-bound testbed;
- odd q>3: continue as primary hard-support lane.

Broad ASET/signature existence is known prior art. Only a theorem that uses
hard support \(w\) essentially remains eligible.

### G2 — odd-characteristic finite extremal evidence

Status: **GF5 FINITE EXACT ACCEPTED; G2_REDUCE_TARGET FOR NEW RUST PRIMITIVE — theorem novelty NOT AUTHORIZED**

Initial fields:

\[
q\in\{3,5,7\}.
\]

Initial capacity/support grid:

\[
d=2,\qquad w\in\{1,2,3\}.
\]

Phase A exact harness is accepted in issue #12. Decision: **G2_EXPAND_GRID**.

Phase-A warning: q=5,m=2,w=2 and q=7,m=2,w=2 have w=m, so those cases do
not exercise hard support. G2B must move to m>w before theorem selection.

G2B-A hosted evidence (run 37756386646):

1. q=3,m=4,d=2,w=2: **exact ASET maximum V=7**, certified exhaustive search;
2. q=5,m=3,d=2,w=2: **certified interval 10 <= V <= 15**; node-budget exhausted, exact maximum UNKNOWN;
3. q=7,m=3,d=2,w=2: deferred until solver review.

G2B-B1 proves **10<=A_5^set(3,2,2)<=11** using a classical weak-Sidon
odd-group inequality and the original independently checked 10-column
witness; G2B-A's [10,15] is historical. See
LENT-001-G2B-B1-WEAK-SIDON-BOUND.md and the machine protocol.

A frozen 10-witness cannot be grown to 11 by direct addition or
one-delete/two-add local exchange (50+12,750 exact finite trials).
This does **NOT** imply global 11-column infeasibility.

G2B-B2-A (issue #42) implements and freezes a **globally complete
single-anchor reduction**: any 11-vertex ASET family contains a
support-two column, and the 384-element coordinate-monomial
action can send it to (0,1,1). A dependency-free exact CNF
uses all 9,990 minimal forbidden edges and a fully reified
at-least-11 cardinality circuit. A separate verifier regenerates
the original ASET incidence; external SAT/UNSAT output can be
promoted only with independent witness/DRUP verification.
See LENT-001-G2B-B2-A-ANCHORED-SAT-PROTOCOL.md.

G2B-B2 is **COMPLETE** for GF5. The anchored eleven-column
CNF was UNSAT, and the full proof was independently checked using
pinned drat-trim on GitHub-hosted CI. Hence **A_5^set(3,2,2)=10**.
The source proof, complete CNF/model/DRAT hashes, reproducible
runner and independent checker are recorded in
docs/research/LENT-001-G2B-B2-EXACT10-CERTIFICATE.md.
This result is EXACT NUMERICAL RESULT (computer-assisted),
NOT a new general theorem or a novelty claim. The B1 interval
[10,11] is historical.

Next G2 decision: compare this finite exact value with classical
Sidon and sparse extremal structures before choosing
G2_SELECT_THEOREM/G2_REDUCE_TARGET/G2_NO_SIGNAL.

G2B-B **finite q=5 question is CLOSED** with exact maximum 10 and independent DRUP verification. The historical instructions above are provenance, not an active request to re-run the same search. Parent #14 remains open only for the G2 research disposition / prior-art gate. The valid signed-side model correction remains: a+b+c=0 with three positive terms is not by itself forbidden for d=2.

Tasks:

1. compute exact values or certified intervals for
   \(A_q^{set}(m,w,2)\) for the largest feasible small m;
2. persist extremal witness families;
3. compare against the finite Hamming-ball upper bound;
4. compare against stronger arbitrary-coefficient sparse-linear
   constructions/bounds only in valid directions;
5. detect whether q=3 and q≥5 show different exponent/structure;
6. choose one precise asymptotic theorem target.

G2 must terminate in either:

- G2_SELECT_THEOREM;
- G2_NO_SIGNAL;
- G2_REDUCE_TARGET;
- G2_STOP.

G2B-A supporting record: docs/research/LENT-001-G2B-A-PROTOCOL.md and
LENT-001-G2B-A-EVIDENCE.md. Phase-A acceptance markers do **not** close G2B.

### HYP-001/002 — locality-capacity theorem lane (separate research gate)

Status: **PHASE B / HYP-002 SHARP QUADRATIC EXPONENT DERIVED; NOVELTY NOT AUDITED**

- HYP-001 (#24): derived Theta_q(m^(3/2)) for odd primes, w=2, d=2.
  Complete definition-to-primary-source review of C4-free/Zarankiewicz
  bounds and projective constructions before promoting theorem originality.
- HYP-002 (#25): **Theta_q(m²) PROVED** for fixed odd field q, w=3,
  d=2, by explicit finite prefix-fiber C4-free upper bound and
  Steiner-triple quadratic lower bound. Old O_q(m^(5/2)) is superseded.
- Independent constructive finite checks: PG(2,2)/PG(2,3), STS(7),
  affine STS(9)/STS(27), plus GF(2) and C4 collision witnesses.
- Neither finite search nor elementary bounds license a novelty, Lean or
  Rust crate claim. Source: docs/research/HYP-001-002-LOCALITY-TRANSITION.md.
- Source: docs/research/HYP-002-B-QUADRATIC-THEOREM.md; finite check
  research/hyp002_quadratic.py, independent ASET regression.
- Next: broad exponent novelty **STOP/PRIOR-ART OVERLAP**; audit
  leading constants, compact decoder tradeoffs, or higher w separately.
  No original discovery, Lean completion, or Rust crate claimed.

### HYP-002-C — index-free affine two-ID decoder / product gate

Status: **PHASE A IMPLEMENTATION / CI-EVIDENCE GATE** (issue #34).

- The affine F3^r Steiner system yields a deterministic table-free
  decoder for <=2 DISTINCT active IDs, with O(m) dense scan and <=20
  candidate triple checks. This is a restricted correctness theorem.
- A fully explicit 3-distinct-line versus 2-line collision proves
  over-capacity cannot always be detected from a modulo-3 snapshot;
  naive raw arithmetic has NO unconditional membership safety.
- Storage: dense m trits is Theta(m) bits versus two canonical
  IDs needing O(log m) bits and no V-entry lookup.
- Compare Python checked transitions and direct-ID operations with
  non-gating diagnostic benchmarks on GitHub CI.
- Preliminary product decision: **STOP_STANDALONE_DENSE_TWO_ID**
  unless a different use case proves an end-to-end merge/algebraic
  workload advantage including additional metadata.
- Protocol/proof: docs/research/HYP-002-C-AFFINE-DECODER-PROTOCOL.md.
  Tests: research/test_affine_two_id.py; benchmark:
  research/bench_affine_two_id.py.

This lane **does not supersede** G2B-B (#14), which remains open.

### G2 exit decision — evidence-gated prioritization (2026-10-08)

**G2_REDUCE_TARGET** for the new Rust-product/theorem-program priority.
The finite GF(3)/GF(5) values and HYP-001/002 derived exponent bounds
remain mathematically valid research results. This is NOT the same as
proving there can never be a new hard-support theorem. Neither a new
leading-constant gap nor a production small primitive is validated.

- No new Rust crate or G4 preprint on known exponents, finite GF5 exact
  search or the rejected affine dense two-ID sketch.
- Issue #14 is a low-priority mathematical/prior-art disposition only.
  HYP #24/#25 still require a source-level equivalence audit, but no
  new general originality claim is allowed without that evidence.
- Cross-domain TOM-003 issue #49 starts a strictly separate O01
  falsification program. Its first result is a *classical* e-bit
  arbitrary-overwrite state minimum, contrasted with a conditional
  log(n+1)-bit externally trusted-old threshold counter. See
  docs/research/TOM-003-TRUST-BOUNDARY-PROTOCOL.md.
- Any future Rust GO requires an end-to-end workload, comparison with
  maintained exact state and validation costs, and a precise mathematical
  or performance advantage. Negative findings are first-class outcomes.

### G3 — formalization

Status: **NOT STARTED**

Lean priorities:

- finite Hamming-ball bound;
- ASET-SIGNED;
- binary equivalence;
- characteristic-two reduction/sandwich.

### G4 — theorem lane

Status: **BLOCKED ON G2**

Any G4 theorem must be support-sensitive and odd-characteristic unless G2
provides compelling contrary evidence.

### G5 — manuscript promotion

Status: **BLOCKED**

Requires theorem proof, theorem-level novelty re-audit, reproducible evidence
and explicit formalization status.

## TOM-001 — independent falsification-first theorem scouting

Status: **PHASE A/B/C COMPLETE; NO NOVEL THEOREM SELECTED** (issue #15).

- 14 ideas mapped at Phase A; O01/O02/O04/O06 audited against source models.
- O02 naive no-effect certificate conjunction refuted; broad O04 stopped as novelty.
- TOM-001-C exact one-edit/zero-probe certificate state quotient accepted as
  an elementary baseline, **STOP** as a novelty target.
- Any next O01 must charge input probes, metadata construction/maintenance,
  repeated updates, certificate size and fallback; independent from LENT G2B.

### TOM-003 — exact no-effect versus externally trusted old values

Status: **D1 CLASSICAL OVERWRITE LOWER BOUND; STANDALONE PRODUCT STOP**,
issue #49. In a no-probe deterministic model receiving only new values,
an exact f:{0,1}^n->{0,1} incremental machine needs exactly e
input-dependent state bits, e=number of essential input variables.
A threshold counter uses ceil(log2(n+1)) bits only with externally
verified old bits; validation and maintained membership are not free.
All n<=3 Boolean functions are independently tested by Moore
partition refinement. This is a classical automata corollary, not a
publication novelty claim or new Rust crate.

O01-D2 (issue #53) freezes a real, **externally authenticated**
root + count overwrite verifier and exact SSZ-style multiproof
comparator. Full bit/digest/hash setup/transmission/verification
cost ledger, exhaustive n<=8 helper/frontier tests and fail-closed
tampered/stale proof regressions. Existing Ethereum SSZ multiproofs
and transparency-dev compact ranges already cover the broad
constructions. **D2 decision: STOP_BROAD_MERKLE_CRATE**, no new
theorem or Rust artifact. See
docs/research/TOM-003-D2-AUTHENTICATED-OVERWRITE-AUDIT.md.

Any future O01-D3 must specify a genuinely different authenticated
update workload, demonstrate the model gap *at source level*, and
quantify advantage against the BEST trusted-bitmap/cached-Merkle
baseline before implementing another protocol.

## Current priority

1. Preserve exact G2B-B2 and full cryptographic proof provenance.
2. Preserve TOM-003 D1 and D2 exact trust-boundary and existing multiproof STOP gates.
3. Continue only source-grounded, narrower Rust-product scouting;
   no original theorem or crate has yet cleared the gate.
