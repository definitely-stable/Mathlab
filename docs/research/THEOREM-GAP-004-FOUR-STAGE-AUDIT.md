# THEOREM-GAP-004 — Four-stage prior-art and model-transfer audit

Date: **2026-10-08** · Issue: [#51](https://github.com/definitely-stable/Mathlab/issues/51)  
Status: **SOURCE-THEOREM-SCOPE AUDITED / NOVEL EXPONENT NO-GO / CROSS-PRODUCT TRANSFER NOT AUTHORIZED**  
Mathlab HEAD at branch creation `fa5998c7aa42879945a3254998f9343e1183eed4`.  
Pinned DELSK `e1ee235fe08c7cc1f6e8ec8884b65439435adf92`; DeltaMeter `862579643fb44bfd3df3b65a863bfdc90b998611`.  
This is **not** a 2026 survey proving global literature completeness. Primary abstracts and selected original source text are checked; full proofs are **not** independently rechecked, Lean **not** run. No new Rust crate, changes to G2B-B2 or product performance claim.

## Stage 1 — HYP-001/002 theorem-level prior art

### Exact ASET definition (unchanged)

For fixed finite field `F_q`, dimension m, column weight w and activity d=2: distinct nonzero columns `a_i∈F_q^m`, each with at most w nonzero coordinates, have injective `S→Σ_{i∈S} a_i` over distinct subsets `S` with `|S|≤2`. The original ASET definition **does not allow** arbitrary field coefficients or repeated indices.

### [LIT-043: Lefmann (2005)](https://doi.org/10.1017/S0963548304006625) — the missing direct exponent baseline

Author/publisher abstract: [*Sparse Parity-Check Matrices over GF(q)*](https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/abs/sparse-paritycheck-matrices-over-gfq/1C4D3DC9839C5DBA0677E3FF698084D4). It maximizes the number `N_q(m,k,r)` of columns with **≤r nonzeros per column**, requiring every k columns to be linearly independent over GF(q). For odd characteristic, the published abstract explicitly states:

`N_q(m,4,r)=Theta(m^{ceil(4r/3)/2})` for fixed q and r.

Therefore `r=2 → Theta(m^(3/2))` and `r=3 → Theta(m²)` are **already achieved by a stronger construction criterion**. This directly affects our HYP-001 `Theta_q(m^(3/2))` and HYP-002 `Theta_q(m²)` lower-bound/nonnovelty assessments.

**DERIVED ELEMENTARY LEMMA (Mathlab; independent short argument):** if every subset of **at most four distinct** columns is linearly independent over GF(q), the columns form an ASET-exact-through-2 family. Indeed distinct subsets S,T of size ≤2 produce a zero relation `Σ_{i∈S\T} a_i − Σ_{i∈T\S} a_i=0`, involving between one and four distinct columns, each nonzero coefficient ±1 (or ±1=1 in characteristic two). Independence forbids it. Independence of any *exactly four* columns only implies all smaller subfamilies independent when `V≥4`; no vacuous inference for `V<4`.

**CONVERSE IS FALSE.** In `F_5^1`, the two columns `(1),(2)` are ASET-exact (subset sums `0,1,2,3` all distinct), yet they are linearly dependent (`2·(1)−(2)=0`). This is a concrete obstruction to transferring **upper bounds** for general 4-wise independent code families to **all** ASET families. Likewise two non-identical supports do not imply arbitrary coefficient independence.

**Decision:** The broad exponents of HYP-001/002 are **NOT ORIGINAL AS CONSTRUCTION/LOWER-BOUND EXPONENTS**: older stronger parity-check families achieve them. The Mathlab *upper-bound proofs* remain self-contained, valid deductions in the ASET model; this source does **not** itself establish their exact ASET bounds or make the proofs textually identical. Precise paper-level uniqueness of upper bounds and constants remains **UNRESOLVED**. Do not label either exponent a newly discovered asymptotic phenomenon.

### [LIT-044: Bshouty–Mazzawi (2015)](https://doi.org/10.1137/120881129)

[SIAM original abstract](https://epubs.siam.org/doi/10.1137/120881129) states a binary-entry `t_p(n,k)×n` parity-check matrix where any k columns are independent over `Z_p`; `t_p(n,k)=O(k + k log(n/k)/log(min{k,p}))` for prime p. Thus it establishes a powerful **non-sparse** finite-field signature baseline, and the preceding lemma gives set identification through d when the required independent-cardinality threshold covers 2d. **But no ≤w nonzeros-per-column guarantee is part of this abstract.** Its upper on the number of rows cannot be plugged into ASET's **fixed w** capacity. Also do not confuse the paper's parameter k (independence) with the Mathlab number m (coordinates).

### [LIT-003: Blackburn (2015)](https://arxiv.org/abs/1505.02597), [LIT-004: Cheng et al. (2015)](https://arxiv.org/abs/1507.00954)

Publisher/arXiv source explicitly uses **barred-`t` separability**, written `overline{t}`; ordinary t-separability and barred-t are not interchangeable. Blackburn cites Gao–Ge length-n barred-2 upper bounds and studies barred-`t` existence, including a special regime for t=2. Cheng's paper is **barred-3**, NOT "ordinary 3-separable"; its result cannot be cited as a theorem directly proving Mathlab ASET for two active IDs.

In an intentionally restricted, unit-entry, 3-partite model with integer-coordinate count maps, equality of complete additive count vectors is stronger/different from equality of **descendant sets** (coordinatewise sets of *symbols*, losing multiplicities). Any claimed equivalence needs a case-by-case proof, and must also handle empty and singleton subsets. Hence we retain this literature as close neighborhood, *not an automatic upper bound on weighted non-tripartite ASET*.

### [LIT-036: constant-weight binary B₂](https://arxiv.org/abs/2303.12990) and [LIT-005: union-free hypergraphs](https://arxiv.org/abs/2605.11949)

Sima et al. count real-valued sums of **distinct pairs** of binary columns at constant Hamming weight `ω∝m`, not GF(q) sums of **0,1,2-element subsets** under fixed hard `w=2 or 3`. Union-free hypergraphs distinguish **unions** of edges, which erase multiplicity that remains present in odd-field incidence sums. Neither carries an ASET `w=2/3` capacity upper bound without reduction.

### Stage 1 decision

- `GO`: retain elementary ASET proofs and existing finite exact G2B result as repository evidence.
- `NO_GO_NOVEL_EXPONENT`: HYP-001/002 broad exponents match a stronger 2005 construction result.
- `OPEN_UNPROVEN_NOVELTY`: a precise **leading constant**, restriction-sensitive finite inequality, characterization of the ASET-vs-4-independent gap, or efficient bounded-write encoder after further source-specific search.
- Absolutely **no** claim that the entire mathematical theory of ASET is solved by Lefmann, and no claim that the new Mathlab upper bound was explicitly published verbatim.

## Stage 2 — DeltaMeter against external streaming/reconciliation models

Source snapshots: [M6-D13B system evidence](https://github.com/definitely-stable/deltameter/blob/862579643fb44bfd3df3b65a863bfdc90b998611/docs/M6-D13B-SYSTEM-EVIDENCE.md), [D13B frozen comparison](https://github.com/definitely-stable/deltameter/blob/862579643fb44bfd3df3b65a863bfdc90b998611/docs/M6-D13B-SYSTEM-COMPARISON.md), [D2 RIBLT scope](https://github.com/definitely-stable/deltameter/blob/862579643fb44bfd3df3b65a863bfdc90b998611/docs/M6-D2-RIBLET-COMPARATOR.md).

| Source / question | Main mathematical promise | Operational cost scope | Allowed comparison | Forbidden transfer |
| --- | --- | --- | --- | --- |
| [Wang F-PCSA, LIT-023](https://arxiv.org/abs/2310.14977) | Asymptotic estimator for generalized turnstile finite-field counting | Rows, levels, hash randomness | ParityDeltaMeter's M2 baseline | No strict one-sided finite-sample high-confidence capacity |
| [Simple Set Sketching, LIT-026](https://arxiv.org/abs/2211.03683) | With high probability, recover set using three independently repeated XOR tables below occupancy ≈0.81 | Lookup storage, hashes, O(n) successful decode | An exact-on-success recoverer | Not unconditional adversarial success or an unbiased cardinality oracle |
| [IBLT listing, LIT-040](https://arxiv.org/abs/2212.13812) | Deterministic worst-case listing for sets below a chosen bound in a **special construction** | Table/map memory, listing time | Bounded-capacity exact retrieval objective | Does not bestow worst-case guarantee on random ordinary IBLT |
| [XYZ-Sketch, LIT-042](https://arxiv.org/abs/2609.14442) | **Author claim** for sufficiently large d: ~`(1+ε)d` communicated **elements**, O(1) insertion, O(d log V) decode; wider fixed-support optimality **conditional on an open conjecture** | Input universe size V, transmitted elements and memory are different metrics | Conjecture-scoped static/fixed-support research comparison | Neither unconditional universal rateless optimum nor wire bytes/RSS/RTT |
| [Rateless IBLT, LIT-027](https://doi.org/10.1145/3651890.3672219) | Progressive coded-symbol transmission as difference size becomes apparent | Wire encoded Symbol/Hash/Count, headers, fallback | Unknown-d reconciliation protocol | Can't equate 1 coded symbol to 8 bytes |

**Frozen DeltaMeter empirical decision:** D13B (5 independent hosted timing workers; 3,900 observations / 360 modeled cells) produced `STOP_SYSTEM_PRODUCT`: **0** qualifying cells for D11 and **0** for even the optimistic RIBLT streaming lower-bound. This is **not** a lower bound for all reconciliation protocols, and no author abstract (even XYZ-Sketch) reverses it. Production/public ExactSmallDelta remains NO-GO. D13B pricing included verification traffic and end-to-end amortization that paper-level `(1+ε)d` does not include.

**Product gate:** a new comparator must specify wire serialization (elements, checksums and framing), state maintenance, fallback, verification cost and source import/rebuild, identical independent workloads, and pre-registered break-even criteria. Until then: **do not reopen STOP_SYSTEM_PRODUCT**.

## Stage 3 — DELSK: delta utility is old; cost-structured headroom remains empirical

Pinned [literature](https://github.com/definitely-stable/Shift-lab/blob/e1ee235fe08c7cc1f6e8ec8884b65439435adf92/.work/research/literature-review.md), [claims and exact sections](https://github.com/definitely-stable/Shift-lab/blob/e1ee235fe08c7cc1f6e8ec8884b65439435adf92/.work/research/claim-matrix.md), [baseline update](https://github.com/definitely-stable/Shift-lab/blob/e1ee235fe08c7cc1f6e8ec8884b65439435adf92/.work/research/DELSK-PRIOR-ART-UPDATE-2026-10.md).

| Source | Already established contribution | DELSK-specific unresolved costed question |
| --- | --- | --- |
| [Finesse FAST'19](https://www.usenix.org/conference/fast19/presentation/zhang) | Content subchunk features + super-features for fast resemblance matching | Does codec-conditioned directionality improve **actual retained patch bytes** under identical CPU/index budget? |
| [DeepSketch FAST'22](https://www.usenix.org/conference/fast22/presentation/park) | Learned block sketch, ANN and *delta compression ratio-informed* clustering | Can a compact CPU-only description beat learned/reimplemented baseline when maintenance and query are priced? |
| [Palantir ASPLOS'24](https://doi.org/10.1145/3620665.3640353) | Hierarchical SF and bad-delta filtering | Is directional scoring incremental after a codec-aware gain filter at fixed R_K trial encodes? |
| [CARD 2021](https://arxiv.org/abs/2106.01273) | Neighbor-context + neural feature extraction | Can cheap non-neural context features preserve performance under shifts, after excluding data leakage? |
| [SpeedSketch ICPP'25](https://doi.org/10.1145/3754598.3754628) | Sketch and encoder acceleration jointly, so pipeline optimization already known | Separate reference ranking gains from encoder savings and CDC/fingerprint amortization |
| [Broder 1997](https://doi.org/10.1109/SEQUEN.1997.666900) | Asymmetric resemblance/containment already known | New direction alone is not novel; require measurable codec-conditioned benefit |
| [Git path-walk, Git 2.49/2.51](https://github.blog/open-source/git/highlights-from-git-2-51/) | Cheap practical path/name/size hints already strongly deployed | Compare to previous-version/size-closest/git-like window at identical query cost |

**Engineering recommendation:** do *not* invent a Delsk science advantage. For future external DELSK (not Mathlab code) evaluation, freeze a pairwise instance universe, independent held-out family, encoder `xdelta3,zstd --patch-from` profiles, candidate budget `K`, metadata bytes, query CPU, build/update CPU, `R_K` trial calls, byte regret vs oracle and fallback penalties. Report a multiobjective **Pareto frontier**, not an averaged gain dominated by a single workload. Each proposed new scorer must have a falsification scenario where cheap trial-encode/lineage baseline is expected to win; otherwise it's merely generic similarity matching.

**Decision:** `NO_GO_GENERIC_DESCRIPTOR_NOVELTY`; `EXPERIMENTAL_GO_CONDITIONAL` only after existing DELSK G3 baseline protocol identifies a real costed region where a proposed new scorer could dominate. No change to Shift-lab product gates or repository artifacts in this work.

## Stage 4 — explicit claim-to-source and transfer matrix

The normative executable complement is [THEOREM-GAP-004-TRANSFER.json](THEOREM-GAP-004-TRANSFER.json), checked by [research/test_theorem_gap.py](../../research/test_theorem_gap.py). It makes assertions about allowed/forbidden implication direction, source IDs, model assumptions, status and cross-repo provenance; it does **not** run third-party code or purportedly machine-check the Lefmann, XYZ-Sketch or systems papers.

| Candidate scientific statement | Status after steps 1–3 | What can still be original (requires further proofs) |
| --- | --- | --- |
| HYP-001 `A_q^set(m,2,2)=Θ_q(m^{3/2})` | `PROVED_LOCAL / PRIOR_ART_EXPONENT_OVERLAP` | Sharp support-sensitive coefficient, extremal structure, simpler exact upper |
| HYP-002 `A_q^set(m,3,2)=Θ_q(m²)` | `PROVED_LOCAL / PRIOR_ART_EXPONENT_OVERLAP` | Weighted/non-partite leading constant or exact finite characterization |
| G2B-B2 `A_5^set(3,2,2)=10` | `EXACT_NUMERICAL_ALREADY_CLOSED` | **Out of scope**; computer-assisted certificate remains authoritative |
| TOM O01 certificate lower bounds | `CLASSICAL/NEGATIVE MODEL GATE` | Frozen external verifier workload with trust-boundary accounting, if any |
| DeltaMeter finite parity strict coverage | `UNPROVEN / PRIOR ART F-PCSA ASYMPTOTIC` | A *new* rigorous finite concentration theorem, if not contradicted by previous NO-GO |
| DeltaMeter maintained system reconciliation | `STOP_SYSTEM_PRODUCT` | New system protocol with independent end-to-end cost evidence (not selected) |
| DELSK codec-conditioned delta scorer | `UNPROVEN PRODUCT IMPROVEMENT` | Pareto improvement beyond cheap previous-version/trial encode under independent held-out corpus |

### Publication and product policy

- Do not call an exponent scientifically new because our derivation is elementary: Lefmann 2005 already provides the same exponents in a stronger subfamily.
- Do not call different sources equivalent unless there is a written formula-level reduction in the correct direction.
- Do not promote source author abstracts to fully verified theorems or hosted benchmarks.
- No Rust crate is justified by HYP exponent similarity or raw XYZ-Sketch headline.
- G2B-B2 closed exact finite result is preserved, untouched.
