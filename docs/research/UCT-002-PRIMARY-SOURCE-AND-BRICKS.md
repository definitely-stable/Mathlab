# UCT-002 — wider cross-domain source audit and theorem bricks

2026-10-09 · [issue #77](https://github.com/definitely-stable/Mathlab/issues/77) · **full original-source landing-page/abstract verification; no independent full-paper proof validation.** This bibliography *expands* the scope from LENT, source-only patch bounds and estimator sketches to information theory, interactive proofs, dynamic error-correcting codes, statistical decision theory, and online verification. For the central baseline see [UCT-002 master theorem](UCT-002-MASTER-THEOREM.md). Titles/identities below are pinned into the canonical literature index where novel.

## Precisely relevant original works
| Source identity | What the original authors actually study | UCT role and mathematical transfer |
|---|---|---|
| **10.1007/978-3-642-54242-8_21**, Chandran, Kanukurthi & Ostrovsky, *Locally Updatable and Locally Decodable Codes*, TCC 2014 | Local *physical writes* plus *local reads* in noisy/adversarial codewords; prefix-Hamming corruption model; also dynamic proofs of retrievability. [Publisher/author record](https://www.microsoft.com/en-us/research/publication/locally-updatable-and-locally-decodable-codes/) · [author manuscript](https://eprint.iacr.org/2013/520.pdf). | **DIRECT STRONG PRIOR ART.** Existing read/write locality coding is not new. UCT's uncorrupted q-ary state model is weaker and MUST NOT claim novel local-decoding tradeoffs. |
| **arxiv:1305.3224**, Mazumdar, Chandar & Wornell, *Update-Efficiency and Local Repairability Limits for Capacity Approaching Codes* (2013) | Update-efficient error-correcting codes near channel capacity with strong per-symbol update/repair tradeoffs. [Original preprint](https://arxiv.org/abs/1305.3224). | **DIRECT PRIOR ART / DIFFERENT CHANNEL:** channel capacity/noisy recovery is an extra resource not in UCT-002 exact ball counting. |
| **doi:10.1145/2636924**, Chakrabarti, Cormode, McGregor & Thaler, *Annotations in Data Streams* (2014) | Strong communication/proof annotation vs verifier space tradeoffs; prover is **UNTRUSTED**. [Publisher DOI](https://doi.org/10.1145/2636924). | **STRONGEST CHECK ON UCT's PROOF CLAIM:** counting b honest witness bits is necessary but not sufficient for online soundness, and nonlinear annotation-space lower bounds exist. |
| **arxiv:1304.3816**, Chakrabarti, Cormode, Goyal & Thaler, *Annotations for Sparse Data Streams* (2013) | Online Merlin–Arthur/annotated streams; construction with costs sublinear in actual sparse update length and separations between online proof models. [Original preprint](https://arxiv.org/abs/1304.3816). | **DIRECT ONLINE PRIOR ART:** query order, annotation publication time, verifier storage and prover soundness determine attainable tradeoffs. |
| **doi:10.4230/LIPIcs.ITCS.2024.53**, Ghosh & Shah, *New Lower Bounds in Merlin-Arthur Communication and Graph Streaming Verification* (ITCS 2024) | Strong separations for **non-trivial online MA** vs ordinary one-way protocols; lower bounds for annotated graph streams and distinct elements. [Official LIPIcs](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2024.53). | **FALSIFIER:** untrusted advice cannot be treated as universal free communication or guaranteed improvement; one proof family can be worse than direct computation. |
| **doi:10.1016/j.ic.2014.12.011**, *Arthur–Merlin streaming complexity* (2015) | Randomized proof/stream verification with annotation-space tradeoffs and lower bounds (e.g., Distinct Elements). [Publisher](https://doi.org/10.1016/j.ic.2014.12.011). | **PRIOR ART:** heterogeneous statistical, soundness and annotation guarantees are formal separate proof systems, not automatically composable. |
| **doi:10.1016/j.ic.2019.05.001**, *Tight upper and lower bounds for leakage-resilient, locally decodable and updatable non-malleable codes* (2019) | Simultaneous cryptographic security, local decoding, updates and leakage resilience, with strong lower/upper locality bounds. [Publisher](https://doi.org/10.1016/j.ic.2019.05.001). | **PRIOR ART:** any proposed *generic* storage+write+read+security frontier must compare this precise security model. |
| **doi:10.1214/aoms/1177729032**, Blackwell, *Equivalent Comparisons of Experiments* (1953) | Statistical decision-theoretic ordering of experiments (informativeness/garbling) and decision risks. [Journal DOI](https://doi.org/10.1214/aoms/1177729032). | **PROOF-TRANSFER FOUNDATION:** one information source simulates another only after explicitly specifying its decision/kernel relation. Not a byte-probe lower bound. |

## Foundational already indexed / non-duplicated
- Fredman–Saks 1989 / Pătraşcu–Demaine 2006 / dynamic bit-probes 2007: **LIT-111/112/114**. These already concern update/query tradeoffs. Must normalize cell reads+writes vs q-ary *changed* code coordinates.
- Ko 2026 Multiphase communication verified source statement: **LIT-119**, [Mathlab theorem/model audit](UCT-001-G1-2026-DYNAMIC-LOWER-BOUND-AUDIT.md). Verification round is a lower-bound communication-game device, NOT a dynamic signed certificate.
- Hardt–Woodruff linear sketches/adaptivity **LIT-100**; Wang–Yin static cell-probe certificates **LIT-041**. Their error/interaction contracts differ from UCT-B and UCT-D; no new duplicate identities.
- Shannon/Fano converse and data-processing: classical source-level [MIT Information Theory lectures](https://ocw.mit.edu/courses/6-441-information-theory-spring-2010/pages/lecture-notes/) (lecture 2/13); historical origin Fano 1953/1961. This **supports proof logic**, not originality. No invented canonical DOI.
- Slepian–Wolf distributed source coding **LIT-116**, not a source-only zero-error worst-case patch lower bound.
- TOM-003/Myhill–Nerode and HYP-103 are not fully recovered by the capacity bound: future distinguishability vs current answer and pointwise certificate complexity are stronger, separately formulated notions.

## Typed claim-dependency DAG ("bricks", not free equivalences)

| Brick | Master role | Required bridge to reach a new theorem |
|---|---|---|
| LENT-001 sparse additive states + UCT-001 graph bound | **SPECIAL_CASE**: ball capacity for exact reachability; fixed public query suite | Need access/coding/construction constraint beyond elementary volume |
| TOM-003 old-state minimization | **REDUCTION_ONLY**: future-labeled-output equivalence is stronger than current observables | Need transition congruence and old bit access policy |
| HYP-103 minimum certificate | **LOWER_BOUND_COMPONENT**, not equality with sphere count | Need paid authenticated old probes, proof soundness and query-set structure |
| UCT-003 patch q-gram counterexample | **FALSIFIER**, not corollary: small observed feature sets can be insufficient | Need formal reduction from source-only parsing to service query model |
| DeltaMeter exact/asymptotic/adaptive guarantee | **NONTRANSFER / THREAT MODEL** | Need conditional error probability, sample/collision distribution and PRF reduction |
| TOM-005 efficient candidate stop / routing | **ADDITIONAL COST LEMMAS** | Need exact common objective, context-closure and no hidden setup share |
| Locally updatable codes + LRC | **PRIOR ART** on update+read+error tradeoff | Distinctive online witness and exact operation family |
| Annotated stream/OMA + 2024 separation | **PRIOR ART** on side messages+verifier memory+soundness | Joint dynamic locality, adversarial annotation and interactive cost |
| Blackwell/Fano | **PROOF TOOL** for approximate observation, statistical decision | Do not transfer ideal-average error to adaptive or cryptographic guarantees |
| Ko/FS/PD dynamic probes | **PRIOR ART** on cell accesses/time | Prove *new* resource coupling, beyond all same-model known inequalities |

## Ambitious theorem selection (NOT YET PROVED)

**A. Strong dynamic coding + verification theorem:** select one exact online membership/index/partial-sum workload under bounded physical writes, external read probes and adversarial untrusted annotation; derive a **nonfactorizing** joint lower bound vs published LULDC and OMA.

**B. Trusted-state substitution theorem:** characterize which observation/certificate contexts admit replacing an authenticated old state with a smaller maintained proof without an uncharged oracle; use TOM-003 + HYP-103 + Blackwell as components. Note this may collapse to classical machine minimization / decision theory.

**C. Cross-application structural lower bound:** an explicit source-delta/patch and repeated query service whose unique legal transformations force cost beyond UCT-003's absent-q gram count; require exact resource-preserving reduction from source matching to dynamic observation.

**D. Adaptive reliability conservation:** a transcript-dependent error theorem under a single named ideal process, with a **separate cryptographic reduction** for any practical PRF. Challenge Hardt–Woodruff/Cohen-Stemmer boundaries rather than asserting all adaptive protocols fail.

### Stop/reopen
**Baseline (A/B in master theorem) PROVED_DERIVED_CLASSICAL;** **novel nonfactorizing theorem OPEN.** No blanket combination of heterogeneous models, no claim that many proofs + new terminology = original theorem, and no Rust authorization. Publication claims require exact theorem-level reading of the closest sources, proof, independent finite falsification, and an improvement/separation beyond them.
