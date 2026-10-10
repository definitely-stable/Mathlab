# IMPORT-011 — external Deep Research PDF scientific audit and cross-program correction gates

**Date:** 2026-10-10. **Baseline:** Mathlab main `19c3842f1ef8ad989e7a8f78f3cf5ec608887c1c`; 355 canonical works (`LIT-001..356`, historical missing `LIT-205`). The two *user-provided* reports are evidence to scrutinize, not trusted primary papers: `От пробелов в литературе к новым теоремам` (31 pages) and `Фундаментальные математические связи, пробелы покрытия и междисциплинарное расширение исследовательской программы Mathlab` (30 pages). The PDFs themselves are **not** imported as primary literature.

**Authority hierarchy:** original DOI/publisher/arXiv landing page > historical bibliography > external AI-generated synthesis. A reported theorem is only an *author-reported result* until its full proof is independently checked. This import changes **literature and scientific scoping**, not theorem status, algorithm implementations or acceptance of product releases.

## 1. Important 2026 fine-grained update — NOT an excuse to discard every lower bound

- **Alman & Vassilevska Williams**, *Truly Subquadratic 3SUM and Truly Subcubic APSP via Triangles in Sparse Lopsided Graphs*, [arXiv:2610.06783](https://arxiv.org/abs/2610.06783), submitted 2026-10-05: author-claimed deterministic `O(n^1.9992)` 3SUM (polynomial-size integers) and `O(n^2.9995)` APSP (polynomially bounded integer edge weights), with real-valued variants addressed using reductions. **Status: AUTHOR_PREPRINT / AUTHOR_THEOREM_STATEMENT_CHECKED / INDEPENDENT_PROOF_NOT_VERIFIED.** The classical universal fine-grained 3SUM and APSP conjectures are refuted by these author-stated algorithms; earlier conditional lower bounds depending *essentially* on these precise hypotheses require retraction/retargeting. This does not negate *unconditional* cell-probe bounds, arbitrary dynamic online lower bounds, OV/SETH assumptions, or hardness statements proved in a different model. Audit each dependency arrow one by one; do not globally delete conditional evidence.
- The first PDF cites [arXiv:2610.10904](https://arxiv.org/abs/2610.10904) as Ko et al. with an asserted `t_u*t_q=Omega(n^2/w)`; identity and same-model theorem were **not** verified in this audit. This is **QUARANTINE_NOT_IMPORTED**, not authority for UCT-005.

## 2. External-report errors requiring corrections

| Report statement | Evidence-based correction | Gate |
| --- | --- | --- |
| Memory Checking Requires Logarithmic Overhead by Boyle, Komargodski, **Lin**, JACM `10.1145/3716616`, universal `Omega(log n)` | Already `LIT-157`, by Boyle, Komargodski, **Vafa**, STOC 2024 [DOI 10.1145/3618260.3649686](https://doi.org/10.1145/3618260.3649686). Exact local-memory, computational-soundness and operation assumptions matter; [covert-security follow-up `LIT-158`](https://doi.org/10.1007/978-3-031-91092-0_11) describes `Omega(log n/log log n)` in a scoped setting. A universal `Omega(log n)` penalty for all authenticated protocols is unsupported. | UCT-005 prior-art |
| Transitive reduction by Henzinger/Kosinas/Papadopoulos/Parotsidis at `O(n^1.528 + m)` | Already `LIT-164`: Goranci, Karczmarz, Momeni, Parotsidis, ICALP 2025 [DOI](https://doi.org/10.4230/LIPIcs.ICALP.2025.92); `O(m+n log n)` amortized and `O(m+n^1.585)` worst case, for *fully dynamic general directed* graphs. DAG-002 immutable labels/new-sink append are different models. | DAG-002 |
| Hypergraph linear-cycle arXiv:2609.38772 by Nie/Spyro/Xu/Yang | Actual authors Balogh, Garcia, Methuku; main theorem counts linear-cycle-free r-uniform hypergraphs. Container machinery **cannot** be applied to GF(5) signed trades without an incidence hypergraph, supersaturation and signed-coefficient comparison. | HYP-105 |
| Cauchyproofs DOI `10.1109/SP61156.2025.00115` | Official IEEE S&P 2025 program and dblp: Luo/Jia/Ospina Gracia/Kate, DOI [10.1109/SP61157.2025.00247](https://doi.org/10.1109/SP61157.2025.00247). KZG/Cauchy algebra applies under commitment setup and crypto assumptions, not unrestricted information-theoretic verification. | UCT-005/TKG-001 |
| Largest Sidon subsets in weak Sidon sets = arXiv:2502.04510; lower `c|A|^{1/2}` | Actual work by Ma/Tang: [arXiv:2602.23282](https://arxiv.org/abs/2602.23282), current abstract gives `g(n)=ceil((n+1)/2)` for **real weak Sidon sets**. Not directly ASET's GF(5) signed subset sum. | LENT-001/HYP-105 |
| Singer construction 2026 by Riblet et al., prime fields only | [arXiv:2605.03274](https://arxiv.org/abs/2605.03274) lists Hulak, Ramos, de Queiroz; 2026 May version covers **prime powers** q. Reusable formalization; no validated HYP-105 GF(5) full exponent. | LENT-001/formal |
| Semantic contradiction detection by persistent homology | Topological cycles/holes **do not imply** semantic inconsistency; two contradictory labels on one edge can exist in acyclic graphs, and harmless cycles may be consistent. Need exact logical semantics, provenance and independent counterexamples. | TKG-001 |
| Dynamic GBWT indexes all DAG reachability in `O(L)` and indel-code Levenshtein distance equals GF(5) signed trade size | A haplotype/path-set index indexes **represented paths**, not arbitrary graph reachability without a reduction. Indel edit metric is not the GF(5) restricted subset-sum collision predicate; claimed isomorphism/equality unproved. | DAG-002/INDEX-001/LENT-001 |
| Cryptographic root alone proves freshness, semantic validity and fork freedom | Binding/inclusion depends on authentication assumptions; freshness needs independent monotone root or bulletin; semantic truth needs independent factual/causal semantics. CRDT join does not automatically preserve acyclicity for arbitrary concurrent edges. | UCT-005/TKG-001 |
| Generic jointly priced inequalities `t_u*pi+t_q*M>=Omega(N log N)`, `t_u log n+t_q pi>=...`, signed-container asymptotics and TKG causal iff mutual information | PDF supplies no same-model proof or quantitative reduction. **HYPOTHESIS_ONLY**; do not label THEOREM. Model dimensions, resources, threat model, static vs dynamic, authentication assumptions and explicit baselines must be frozen first. | All |

## 3. Canonical import candidates (source identity/source abstract checked; no proof reproduction)

| Candidate | Verified primary identity | Correct scope / model transfer |
| --- | --- | --- |
| Alman–Vassilevska Williams, fine-grained breakthrough | [arXiv:2610.06783](https://arxiv.org/abs/2610.06783) | Retire false 3SUM/APSP conditional premises **only** where the exact reductions depend on the refuted hypotheses. |
| Luo et al., *Cauchyproofs* | [DOI 10.1109/SP61157.2025.00247](https://doi.org/10.1109/SP61157.2025.00247) | KZG vector-commitment proof maintenance, not a data-structure cell-probe lower bound. |
| Guruswami–Lyu–Yuan, *Cell-Probe Lower Bounds via Semi-Random CSP Refutation: Simplified and the Odd-Locality Case* | [arXiv:2507.22265](https://arxiv.org/abs/2507.22265) | Static local-circuit/CSP lower bounds, not a turnkey dynamic verification theorem. |
| Balogh–Garcia–Methuku, *Counting hypergraphs without linear cycles of fixed length* | [arXiv:2609.38772](https://arxiv.org/abs/2609.38772) | Linear-cycle-free hypergraphs, not GF(5) signed hypergraphs. |
| Ni–Cheng–Wang–Kang, *Spectral Turán Problems for Expanded hypergraphs* | [arXiv:2603.00428](https://arxiv.org/abs/2603.00428) | Forbidden graph expansions, not automatic signed-trade bounds. |
| Ma–Tang, *Largest Sidon subsets in weak Sidon sets* | [arXiv:2602.23282](https://arxiv.org/abs/2602.23282) | Weak-vs-strong Sidon in real numbers, not GF(5) restricted signed sums. |
| Hulak–Ramos–de Queiroz, *Formalizing Singer Sidon Constructions and Sidon Set Infrastructure in Lean 4* | [arXiv:2605.03274](https://arxiv.org/abs/2605.03274) | Mechanized classical prime-power Singer constructions; not a HYP-105 proof. |
| Li et al., *LycheeMemory V2* | [arXiv:2608.12990](https://arxiv.org/abs/2608.12990) | Empirical LLM segment-based consolidation; does not confer cryptographic/causal guarantees. |
| Press et al., *HEDGES error-correcting code for DNA storage corrects indels and allows sequence constraints* | [DOI 10.1073/pnas.2004821117](https://doi.org/10.1073/pnas.2004821117) | DNA insertion/deletion/substitution recovery plus outer code, not exact ASET equivalence. |

**Already present — do NOT duplicate:** `LIT-157` memory checking; `LIT-158` covert checking; `LIT-159` efficient vector commitments; `LIT-164` fully dynamic transitive reduction; `LIT-201` FSS/dynamic DS; `LIT-212` compressed fully indexable dictionaries; `LIT-298` Larsen–Yu dynamic graph cell-probe; `LIT-321` Bifrost; `LIT-328` pangenome graph indexing. Existing `LIT-317..348` cover substantial DNA/pangenome/biological-memory prior art and supersede the PDFs' premise that no genomic material has been imported.

## 4. Program-level changes required before a claim can be promoted

- **UCT-005:** scope 3SUM/APSP hypothesis break, do not generalize memory-checker lower bounds, preserve time-horizon/adaptive error/independent trust/fork fencing, distinguish bit/cell accesses from proof bytes and verifier CPU; comparison must use same task. `ROOT_OPEN` remains.
- **HYP-105:** signed two-sided support constraints are not ordinary girth or unweighted cycle avoidance. Freeze GF(5), w=4, d=3 and prove source-model-preserving container supersaturation before claiming any improved exponent.
- **DAG-002:** transitive reduction for general fully dynamic graphs is a distinct operation from append-new-sink immutable-old-label reachability. GBWT indexes declared paths, not arbitrary semantic DAG reachability. Keep page and label rewrite charges.
- **INDEX-001:** dynamic compressed string/graph indexes require their own page/write, RAM, WAL/GC, scan and crash metrics; `O(L)` in an algorithmic index does not imply `O(L)` persistent SSD reads.
- **TKG-001:** separate evidence authenticity, semantic truth, complete provenance, bi-temporal validity and independent freshness. No cycle => contradiction theorem; causal intervention and timestamps do not prove data origin.
- **LENT-001:** DNA edit-distance/indel recovery is a useful separate metric, not automatically an additive GF(q) collision-free code. Sidon/Singer methods need exact predicate reductions.

## 5. Further tasks (no invented novelty)

1. Audit every Mathlab theorem/issue dependent on standard 3SUM/APSP hardness with a machine-readable model/conditional-dependency matrix; preserve unconditional boundaries.
2. UCT-005: add a source-to-theorem comparison for Cauchyproofs and the 2024 memory-checker + 2025 covert models; falsify any broad `Omega(log n)` claim outside its assumptions.
3. HYP-105: formalize the signed-trade incidence hypergraph `H_trades`; test minimal overlap/codegree and balance-supersaturation conditions before importing container theorem consequences.
4. DAG-002/INDEX-001: specify a path-set vs full-reachability test matrix (chain, layered DAG, arbitrary edge insertions, dynamic deletion, page recourse) and compare compressed genomic path indexes only on shared legal operations.
5. TKG-001: exact semantic contradiction counterexamples, Byzantine authenticity, trusted freshness and independent source retraction; evaluate LycheeMemory only as an empirical baseline.

## 6. Acceptance

Only metadata+abstract/title was source-checked. All `full_proof_verified=false`, `independent_reproduction=false`. Run `python research/literature.py --check`, `python -m unittest research.test_literature`, and repository-wide GitHub-hosted research CI. Do not merge on syntactic validity alone: verify source identity, exact main/PR HEAD, no duplicate alias and no model-laundered scientific claims.
