# UCT-001 — primary literature, solved overlap and transfer barriers

Date: 2026-10-08. Parent: [#74](https://github.com/definitely-stable/Mathlab/issues/74). **Source status:** original publisher/arXiv/ECCC landing page metadata and abstracts checked, **not** independently reproved whole articles. `UCT-SRC-*` are local temporary scope IDs, not new canonical `LIT-*` and not claims of new mathematics. Canonical external registry before this work has 110 works.

## Primary sources checked for UCT (bibliographic import into Mathlab research)
| Local ID | Primary identity (authors; year) | Exact model / contribution reflected in available primary source | UCT transfer restriction |
|---|---|---|---|
| **UCT-SRC-01** | [Fredman & Saks 1989, ACM STOC, DOI:10.1145/73007.73040](https://doi.org/10.1145/73007.73040) | Cell-probe dynamic structures, updates/queries, tradeoffs between reads and writes; chronogram technique. | Arbitrary cell writes and sizes vs per-coordinate q-ary Hamming locality: cannot assert a new joint write/query bound by rephrasing their theorem. |
| **UCT-SRC-02** | [Pătraşcu & Demaine 2006, SIAM J. Computing, DOI:10.1137/S0097539705447256](https://doi.org/10.1137/S0097539705447256) | Randomized amortized cell-probe lower bounds, partial sums, dynamic connectivity, query/update tradeoffs, word size. | Cell-probe model, amortized bounds and operation distributions must be mapped exactly. |
| **UCT-SRC-03** | [Yi & Zhang, SODA 2010, DOI:10.1137/1.9781611973075.12](https://doi.org/10.1137/1.9781611973075.12) | Dynamic membership lower bound with a cache of free cells; upper limits on reducing amortized updates via large block writes. | Free cache fundamentally changes resource accounting; do not present independent Hamming-ball result as their lower bound. |
| **UCT-SRC-04** | [On dynamic bit-probe complexity, Theoretical Computer Science 2007, DOI:10.1016/j.tcs.2007.02.058](https://doi.org/10.1016/j.tcs.2007.02.058) | Lower bounds for dynamic membership and partial sums in bit/cell-probe models; extension of chronogram reasoning. | A 1-bit write is not equal to 1 physical byte/word write; normalize exactly. |
| **UCT-SRC-05** | [New amortized cell-probe lower bounds for dynamic problems, TCS 2019, DOI:10.1016/j.tcs.2019.01.043](https://doi.org/10.1016/j.tcs.2019.01.043) | Amortized update/query lower-bound framework for dynamic polynomial evaluation and online matrix-vector multiplication. | Specific hard problems; does not imply a bound for every evolving observable. |
| **UCT-SRC-06** | [Slepian & Wolf, IEEE TIT 1973, DOI:10.1109/TIT.1973.1055037](https://doi.org/10.1109/TIT.1973.1055037) | Distributed lossless source coding under statistical correlation. | Asymptotic correlated *random sources* vs finite worst-case source-only COPY/ADD patch; not the same cost or guarantee. |
| **UCT-SRC-07** | [A Library for Self-Adjusting Computation, ENTCS 2006, DOI:10.1016/j.entcs.2005.11.043](https://doi.org/10.1016/j.entcs.2005.11.043) | Change propagation with modifiable references and memoization; incremental convex-hull example. | Performance demonstrations and programming invariants do not prove universal update lower bounds. |
| **UCT-SRC-08** | [Lower Bounds for Adaptive Locally Decodable Codes, Random Structures & Algorithms 2005, DOI:10.1002/rsa.20069](https://doi.org/10.1002/rsa.20069) | Query locality for error-correcting codes with adaptive decoding. | **READ locality** on corrupted codewords is not LENT's per-update **WRITE locality**. |
| **UCT-SRC-09** | [An Omega((log n / log log n)^2) Cell-Probe Lower Bound for Dynamic Boolean Data Structures, ECCC TR26-047, 2026](https://eccc.weizmann.ac.il/report/2026/047/) | Author-reported unconditional dynamic Boolean lower-bound advance, original 2026 technical-report landing page, revision #1 dated 2026-10-07; the authors introduce a 2.5-round Multiphase Communication Game with a verification round. The asserted Omega((log n/log log n)^2) lower bound concerns the stated Multiphase problem, not all dynamic Boolean structures. | **ABSTRACT-ONLY REVIEW**: numerical exponent and exact assumptions must be checked in manuscript before theorem use. |
| **UCT-SRC-10** | [Hardt & Woodruff, STOC 2013, arXiv:1211.1056](https://arxiv.org/abs/1211.1056) | Attacks on Euclidean-norm linear sketches for adaptively selected inputs. | A negative result for specified linear sketches cannot be lifted to every DeltaMeter estimator. **ALREADY CANONICAL `LIT-100` — do not reimport.** |
| **UCT-SRC-11** | [Wang & Yin, 2014, arXiv:1404.5743](https://arxiv.org/abs/1404.5743) | Static cell-probe certificate complexity and lower-bound methods. | Static data-structure certificates are not complete costed online authenticated batch-update protocols. **ALREADY CANONICAL `LIT-041` — do not reimport.** |

## Existing Mathlab results: direct overlap matrix
| Existing primary Mathlab model | UCT reuse | Decision |
|---|---|---|
| [LENT-001 foundation](LENT-001-FOUNDATION.md), **KR-001** | Reachable Hamming-ball capacity when states are bounded-size subsets with sparse additive signatures. | **DERIVED_CLASSICAL**, no novelty. |
| [LENT-001 G2B GF(5) certificate](LENT-001-G2B-B2-EXACT10-CERTIFICATE.md), **KR-009** | Finite extremal constructions / reproducibility only. | **EXACT_NUMERICAL**, not generic joint bound. |
| [TOM-003](TOM-003-TRUST-BOUNDARY-PROTOCOL.md) and [HYP-103 G0](HYP-103-G0-CERTIFICATE-REDUCTION.md) | Trusted delta vs untrusted overwrite; certified old-root batch verifier. | **STOP_BROAD**, classical state minimization and certificate complexity; cryptographic helper proofs not free. |
| [TOM-005](TOM-005-SEVEN-THEOREM-AUDIT.md) | Interval stop, Pareto, dynamic routing, test ordering, crash safety, exact fingerprints, materialized fanout. | Seven separate **DERIVED_CLASSICAL** kernels; objectives cannot be combined without compatible shared cost. |
| [TOM-006](TOM-006-EARLY-KILL-GATE.md) | Missing-q-gram COPY/ADD lower bounds, explicit cheap-q adversarial separation. | Weak bounded-q relaxation; no competitive certificate theorem. |
| [TOM-007](TOM-007-SIX-HYPOTHESIS-AUDIT.md) | Existing HYP-101..106 novelty scouting incl. adaptive cardinality & shared DAG certificates. | No automatic UCT novelty; exact existing STOP rules still apply. |
| [DeltaMeter](https://github.com/definitely-stable/deltameter) | Ideal finite-sample one-sided statistical vs keyed deterministic pseudorandom-oracle guarantees. | Guarantee transfer requires distinguishing statistical, computational and adaptive threat models. |
| [DELSK](https://github.com/definitely-stable/Shift-lab) | Real best-base/patch objective and baseline separation. | Ranking oracle/selector measurements are not a theorem about optimal compression. |
| [openai/math](https://github.com/openai/math) | Selected mathematical manuscripts as *candidate* proof techniques, preserving pinned identities and individual proof status. | Source-reported manuscript claims ≠ independently validated theorem; no blanket transfer. |

## Prior-art disposition for four new program lanes
**UCT-A:** BROAD KNOWN. Dynamic time–space and update/read lower bounds established. A single exact compatible model could still permit a sharper joint result; none shown.

**UCT-B:** BROAD KNOWN / STOP simple witness. HYP-103 old-input probes exactly promise-domain certificate complexity. Costs for access, prover work, auth and persistent state remain unsolved in any proposed stronger joint statement.

**UCT-C:** BROAD KNOWN. Correlated coding and parsing are classical, but the specific *bounded-preprocessing, source-only, verifiable patch lower-bound service* requires direct prior-art comparisons and adversarial benchmarking. TOM-006 already disproves usefulness of q<=2 relaxation.

**UCT-D:** BROAD KNOWN / MODEL OPEN. Standard simultaneous union bound applies only to a fixed family with stated marginal bounds over the *same sample space*; adaptive selection changes the query distribution. Computational PRF assumptions do not transform automatically into unconditional finite-sample guarantees.

## Canonical catalog import gate
The above **nine new-to-current-catalog identities** (UCT-SRC-01..09) are recorded and source-linked in this review; existing LIT-041/LIT-100 are linked without duplication. The existing `docs/research/catalog/literature.json` and generated indexes are deliberately not hand-edited in this slice: import to canonical numbered LIT records must atomically update machine registry, deterministic `research/literature_catalog.py` generated forward/reverse indexes and CI, after model/scope QA. Until then do **not** report total canonical literature count as increased. This is a staged primary research import, not a claim that the canonical catalog has changed.

## Required next source audit
- Read full theorem statements/proofs for UCT-SRC-01/02/03/04/05/09; map word size, free preprocessing, randomized/amortized vs exact guarantees.
- Read full Slepian–Wolf assumptions and distinguish side-information availability/conditional distribution from worst-case patch parsing.
- Check strongest results on fully persistent/strongly history-independent dynamic structures before stating a new representation theorem.
- Inspect papers' actual theorem hypotheses independently of abstracts; assert source identity only as verified above.
