# UCT-005 — fundamental root theorem program and typed research tree

**As-of:** 2026-10-09; baseline `main` `e0b24b0c6185a19b5075cfaac155f0158d60704a`; **root issue:** [#105](https://github.com/definitely-stable/Mathlab/issues/105).
**Scientific status: ROOT OPEN / NO ORIGINAL UNIFIED THEOREM PROVED / NO PRODUCT OR RUST RELEASE.**

## 1. The target is ONE theorem, not a collection of named elementary lemmas

Central question: **for a system with evolving state, how do limited update locality, persisted memory, access to original information, verifier/prover work, proof communication, trust and adaptive error constrain the *same online service*?**

The target is a *new nonfactorizing asymptotic impossibility or sharp frontier* in one explicitly frozen natural task family, with valid special-case consequences. UCT-002's classical master capacity `K <= V_q(m,dw) * 2^b * s^P` is an important existing lemma, but cannot serve as a novel root law: auxiliary information and oracles can be freely state-dependent in its sharp example, program/prover/update work is not priced, and its global observation is not a real per-query read budget. [UCT-002](UCT-002-MASTER-THEOREM.md).

No universal product `w*p >= n`, no universal `Omega(log n)` update cost for all commitments, and no claim of cryptographic security from information-theoretic counting. Query and update models may differ sharply (see Fenwick and [UCT-003](UCT-003-G1-ADAPTIVE-INFLUENCE-THEOREM.md)).

## 2. Mathematical skeleton (to be frozen into a single model at G1)

For each n let `T_n=(X_n,E_n,J_n,f_n)`: states X_n, **publicly labelled** allowed online updates E_n and public query indices J_n with responses f_n(x,j). An online transcript contains updates, stateful storage transitions, certificate maintenance and adversarial queries. A verifier may hold a bounded *trusted* state; the large store and arbitrary prover-generated messages may be adversarial. Distinguish physical cells actually written from address/data probes and CPU work.

The complete resource vector is

```text
R=(S_trusted, S_untrusted, U_read, U_write, Q_probe,
   B_proof, C_total, G_prover, V_verifier,
   T_program, T_preprocess, R_random, epsilon, security_parameter).
```

Precise unit (bit/word), worst-case or amortized semantics, charged setup, update-prover timing, query suite vs individual query, first vs repeated use, public/private coins, fresh/reused secret randomness, crash/rollback model, honest completeness, and untrusted-prover soundness must be fixed **before** inequalities.

Let `Ach(T_n)` denote the **feasible resource region**: every tuple R for which an online protocol exists meeting *all* of the above semantics. For each published applicable theorem i, let `B_i(T_n)` be the allowed tuples after an explicit assumption- and unit-preserving transfer. The comparison region is `B_known(T_n) = intersection_i B_i(T_n)`. Always `Ach(T_n) subseteq B_known(T_n)` if the published bounds and transfers are valid.

**Central nonfactorization target:** prove a quantified family of tuples `R_n in B_known(T_n) \ Ach(T_n)` for one natural task family T_n, ideally with an **unbounded quantitative margin** in a fixed scalar resource while all other costs are explicitly bounded; or characterize `Ach(T_n)` sharply with matching constructive protocols. This distinguishes a genuinely new joint constraint from a mere juxtaposition of existing inequalities. Importantly `B_known` is limited to *audited* transferable bounds and changes when prior art is imported: no claims of global completeness. Proving the strict inclusion for just a finite toy task does not itself make a fundamental asymptotic theorem.

An equivalent eventual theorem may state an explicit `F_{T_n}(R) >= g(n)`, but **F and g must be specified and tested rather than inserted as placeholders and announced as results**. This is a theorem search specification, NOT a proved theorem or currently formulated true conjecture.

For each proposed result freeze a concrete numerical expression `F`, an explicit `T_n`, and a named adversarial experiment. Publish simple competing upper constructions and exact small countermodels BEFORE investing in an asymptotic proof.

## 3. Typed tree: what each old theorem contributes

```text
ROOT UCT-005: online, fully priced, verifiable dynamic observability [OPEN]
├── GEOMETRY / INFORMATION FOUNDATION
│   ├── LENT-001: reachable-ball / sparse additive set capacity [SPECIAL_CASE]
│   ├── HYP-001 / HYP-002 / HYP-105: support-sensitive finite-field
│   │   extremal constructions [RESTRICTED_SPECIAL_CASE / OPTIONAL]
│   └── UCT-001 & UCT-002: transition/observation capacity [CLASSICAL BRICKS]
├── OPERATIONS AND TEMPORAL SEMANTICS
│   ├── TOM-003: future-trace distinction, old-state trust [PROOF_INGREDIENT]
│   ├── UCT-003 G1: adaptive read/write influence, p=1/w=1 endpoints
│   │   [PROOF_INGREDIENT; CLASSICAL]
│   └── HYP-101: canonical incremental hash re-use [APPLICATION / COUNTERMODEL]
├── CERTIFICATION AND SECURITY
│   ├── HYP-103 / TOM-003 D2: verification certificates [PROOF_INGREDIENT]
│   ├── UCT-004 G2-C/G2-D: proof covers, PPZ witness-bit bound
│   │   [STATIC WEAK-SOUNDNESS BASELINE; CLASSICAL]
│   └── Memory-checking, vector commitments, annotated streams
│       [EXTERNAL PRIOR-ART BARRIERS]
├── DYNAMIC RELIABILITY
│   └── DeltaMeter adaptive/statistical/computational boundaries
│       [THREAT-MODEL ANALOGY ONLY UNTIL FORMAL REDUCTION]
├── INCREMENTAL TRANSFORMS
│   └── TOM-005 / TOM-006 and source delta/patch tasks
│       [APPLICATION ONLY UNTIL A MODEL-PRESERVING REDUCTION]
└── OPTIONAL INDEPENDENT MATHEMATICS
    ├── HYP-105 G5-B true four-support 3-sum exponent [SEPARATE OPEN]
    └── κ(n,p) exact integer cover for nondivisible n/p [SEPARATE OPEN]
```

The **[UCT-005 machine-readable theorem tree](UCT-005-THEOREM-TREE.json)** freezes 23 uniquely identified nodes and 22 parent-child edges, with source paths, status, edge roles, and strict single-parent acyclic organization; [metadata integrity tests](../../research/test_uct005_tree.py) run in the GitHub-hosted research workflow. They certify the catalog topology only, **not the truth or novelty of any mathematical claim**. The tree's arrows are *typed*: SPECIAL_CASE, PROOF_INGREDIENT, COUNTERMODEL, THREAT_MODEL, APPLICATION, OPEN_REDUCTION or NONTRANSFER. These are **not all logical implications**. Do not force HYP-105, source delta or a DeltaMeter estimator into a theorem if the reduction loses the operational assumptions. Existing [machine-readable 20-node UCT-002 DAG](UCT-002-THEOREM-BRICKS.json) remains valid as historical typed bricks; this document identifies the research root above it.

## 4. One leading candidate, one explicitly allowed alternative

**Lead (G1-C1): online authenticated multi-query range parity / indexed-memory service.** Coordinate updates chosen adversarially, repeated public queries, small trusted state, untrusted bulk storage, maintained evidence, explicit per-operation costs and constant `epsilon<=1/3` under a specified adaptive horizon. Baselines: identity/raw store, materialized prefix values, Fenwick, Merkle proofs and multiproofs, dynamic vector commitments, and best memory checker. Essential novelty question: is there a *joint* tradeoff of verifier probes/proof maintenance/trusted storage/communication that is not already a memory-checker or cell-probe theorem? If no, **STOP** and choose another task.

**Fallback (G1-C2): online incrementally certified DAG or compressed transformation service** with nontrivial shared recomputation and batch updates. Charge preprocessing, prover recomputation, verifier queries, annotation publication and authentication. No free trusted old value, no source-only q-gram false tightness, no elementary Pareto/shortest-path theorem as the headline.

Do NOT use the already closed weak-soundness parity equality `b_min(n,p)=ceil(n/p)-1` as evidence of a breakthrough. G2-E [#102](https://github.com/definitely-stable/Mathlab/issues/102) notes constant soundness makes the unit-write raw parity read barrier linear even with long untrusted witnesses; exact κ is interesting but not the central goal.

## 5. New indispensable original-source gaps (as of 155-entry index)

These *four works were not found by exact title/identity in the merged `catalog/literature.json` at the baseline HEAD*. Their abstracts/original landing pages were checked in this planning slice; **full hypotheses/proofs and possible exact overlap remain to be read independently and canonically imported, with duplicate prevention**.

| Reference | Why it may make our headline already known |
|---|---|
| Blum–Evans–Gemmell–Kannan–Naor, *Checking the Correctness of Memories*, FOCS 1991 / Algorithmica 1994 ([DOI](https://doi.org/10.1109/SFCS.1991.185352)) | Adversarial online remote memory, small reliable client memory, verification and information-theoretic bounds |
| Boyle–Komargodski–Vafa, *Memory Checking Requires Logarithmic Overhead*, STOC 2024 / JACM ([DOI](https://doi.org/10.1145/3707202), [ECCC](https://eccc.weizmann.ac.il/report/2024/014/)) | A strong known general computational-secure memory-checker lower-bound barrier |
| Boyle–Komargodski–Vafa, *The Complexity of Memory Checking with Covert Security*, EUROCRYPT 2025 ([ePrint](https://eprint.iacr.org/2025/358)) | Explicit constant-risk/covert soundness and read-only-read model; cannot advertise constant-error online checker tradeoff as wholly new |
| Tas–Boneh, *Vector Commitments with Efficient Updates*, AFT 2023 ([DOI](https://doi.org/10.4230/LIPIcs.AFT.2023.29)) | Published *information-theoretic lower bound* on joint update-publication size vs opening-proof refresh time, plus matching construction |

Already catalogued but still *must compare theorem-to-theorem*: Fredman–Saks, Pătraşcu–Demaine, Pătraşcu–Tarniţă, Ko ECCC TR26-047, Chandran–Kanukurthi–Ostrovsky LULDC 2014, annotated streams 2014, Ghosh–Shah 2024, PPZ 1999, Emdin et al. MFCS 2022, Kayal et al. 2026. Source title/abstract similarity alone does not establish an equivalence. See [UCT-002 source matrix](UCT-002-PRIMARY-SOURCE-AND-BRICKS.md) and [G2-D prior-art audit](UCT-004-G2-D-PPZ-PRIMARY-SOURCE-AUDIT.md).

## 6. G0→G5 gates and fatal counterexamples

| Gate | Required deliverable | STOP condition |
|---|---|---|
| G0 | Typed research root, status inventory, unchanged proofs/IDs | Rebranding known master counting as discovery |
| G1 | Four source-level import/audit records; frozen task, resource units, trust boundary and competitor schemes | Task already exactly covered by a stronger published theorem |
| G2 | Small independent brute-force/falsification oracle and explicit `n`-parameter counterexamples; all resource costs paid | Universal inequality falsified by systematic/Fenwick/fast commitment or free-state channel |
| G3 | Named new **quantified** inequality beyond same-model results and at least one proof method | Only independent old bounds were added/multiplied |
| G4 | Full mathematical proof, upper construction or separation, independent adversarial review and hosted CI | No theorem-level proof / no model-preserving reduction |
| G5 | Formalizable kernel, reproducible paper and independent novelty review | Only finite testing and source abstracts available |

Threat-model kill gates: wrong-state prover may adapt to prior accept/reject outputs; a state-dependent root, proof cache, public parameter table, communication and random seed are never free. `delta<1` is not interchangeable with constant soundness; perfect correctness, statistical guarantees and computational binding are separate objects. A 12-state sharp UCT-002 star blocks a universal stronger capacity factor; a Fenwick representation blocks universal `w*p>=n`. Dynamic commitments and memory checker literature may kill a new broad online-verification law.

## 7. Repository hygiene to implement separately

- Link this root above UCT-002 as a research **objective**, not as an accepted theorem.
- [#98](https://github.com/definitely-stable/Mathlab/issues/98) G2-D remains OPEN despite merged [PR #101](https://github.com/definitely-stable/Mathlab/pull/101): close or explain only after checklist audit.
- The source-count/status text in historical documents (33/40/51/52 vs current 55 known-stop entries; 150/153 vs 155 literature items) is snapshot provenance, not live authority. Add a generated status header rather than globally rewrite historical records.
- `lean/` is currently only a plan/README, not a formal proof of the central theorem.
- Do not release a Rust crate, claim publication novelty or merge an unreviewed speculative theorem.

**Next allowed action:** G1 original-publication theorem/model import, then fully costed task selection. This file constitutes governance/model planning, **not G1 scientific acceptance**.

## 8. G1 source-barrier discovery and import (2026-10-09)

[Four-source formal-statement/mismatch audit](UCT-005-G1-MEMORY-CHECKING-AND-VC-PRIMARY-AUDIT.md) · [issue #113](https://github.com/definitely-stable/Mathlab/issues/113) catalogs canonical **LIT-156..159** without duplicate conference/journal identities. Early G0 source gaps in section 5 are now **cataloged and partially theorem-statement checked** (BKV24 and Tas–Boneh PDFs), but not independently proof-reproduced; BEGKN91 and covert BKV25 formal theorem proof hypotheses need further full-text inspection. This closes the **generic-memory-checker** and **generic-proof-update-broadcast** novelty headlines, NOT the UCT-005 program. G2 must seek an explicit natural task and novel same-model quantitative separation. Root remains **OPEN_UNPROVED**.

## 9. G2-A: new fundamental primary-source barriers and exact honest countermodels (2026-10-09)

[Seven-source audit with six new canonical publications](UCT-005-G2-A-NEW-FUNDAMENTAL-BARRIERS.md) · [issue #125](https://github.com/definitely-stable/Mathlab/issues/125) · [oracle](../../research/test_uct005_g2a_models.py). LIT-199..204 imported; STOC natural-proofs paper already LIT-072. Honest 1D Fenwick disproves universal unscoped `w*p >= n` for dynamic parity; this is NOT a counterexample to UCT-004 weak-soundness certificate theorem. Dynamic 2D transcript-adaptive authenticated range parity remains a nonfrozen G2-B candidate. All theorem novelty **OPEN_UNPROVED**.

## 10. G2-B: frozen adaptive 2D parity authentication, quantitative novelty barrier (2026-10-09)

[Formal statement and cost ledger](UCT-005-G2-B-VERIFIED-2D-PARITY-AND-NOVELTY-GATE.md) · [five additional primary source identities](UCT-005-G2-B-SOURCES.json) · [independent executable small-instance oracle](../../research/test_uct005_g2b_auth_tree.py) · [issue #131](https://github.com/definitely-stable/Mathlab/issues/131). Research fixture: owner keeps trusted digest and epoch; a malicious remote server produces domain-separated XOR-quadtree proofs/updates. Construction tests honest completeness and rejection of stale, truncated and wrong-aggregate proofs, **not SHA-256 collision resistance or a cryptographic reduction**. Dynamic multi-dimensional authenticated queries and aggregate ADS are already prior art (IET 2016, IEEE Access 2019, PVLDB 2025; dynamic skewed Merkle 2026 preprint). One numerical G2B-H0 lower-bound candidate overlaps known memory-checker barriers; an `Omega(lambda*N)` universal range-proof claim is falsified by full-grid aggregate proof. **No same-model novel asymptotic inequality, ROOT OPEN_UNPROVED.** New canonical bibliography IDs allocated only after PR #132 LIT-205 collision resolved.

## 11. G2-B1: authenticated DAG semantic cancellation vs certificate invalidation (2026-10-09)

[Formal classic GF(2) path-parity derivation and unbounded diamond fanout countermodels](UCT-005-G2-B1-DAG-SEMANTIC-STRUCTURAL-COUNTERMODELS.md) · [new primary sources and canonical deduplication](UCT-005-G2-B1-SOURCES.json) · [finite independent oracle](../../research/test_uct005_g2b1_dag_influence.py) · [issue #148](https://github.com/definitely-stable/Mathlab/issues/148). The number of changed materialized XOR outputs `h_s` is the number of **odd** s→v paths, while the number of recomputed node commitments in the specified eager Merkle-DAG follows structural reachability `r_s`. A K-terminal diamond produces `h_s=3`, `r_s=K+3`: an arbitrarily large divergence but NOT a general lower bound on all authenticated data structures. Larsen–Yu's dynamic DAG reachability lower bound and ITCS 2026 UpBARG IVC already bar overly broad originality claims; their models do not transfer without proofs. **STOP generic online authenticated XOR and DAG certificate novelty; root OPEN_UNPROVED.** Canonical IDs of new sources remain pending #142.
