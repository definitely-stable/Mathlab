# UCT-005 G1 — four source-level lower-bound barriers and model-transfer matrix

**Date:** 2026-10-09. **Parent:** [UCT-005 root #105](https://github.com/definitely-stable/Mathlab/issues/105); **G1 issue:** [#113](https://github.com/definitely-stable/Mathlab/issues/113). **Status:** SOURCE-THEOREM-STATEMENT-AUDIT / ROOT_NOVELTY_OPEN / NO NEW THEOREM. No product or Rust implementation.

## 1. What G1 establishes — and what it does NOT

Four original publication identities, author/publisher pages, and critical source theorem statements were compared against UCT-005's candidate model. **The bibliography alone and any existing author's proof are not independently reproved**. No universal resource inequality is certified by this audit; the central root theorem is still OPEN. Distinguish **publisher abstract checked**, **PDF exact theorem text spotchecked** and **full paper proof independently verified** (NONE for these imported works).

A theorem applies to UCT-005 only if a typed reduction preserves a fully specified operation semantics, online transcript, adversary/error condition, counted resources (including unit!), update legality and trust context. Merely using words "verification", "locality", or "proof" is insufficient.

## 2. Four new canonical primary sources

### LIT-156 — Blum–Evans–Gemmell–Kannan–Naor (FOCS 1991; Algorithmica 1994)

- Canonical first publication [FOCS DOI 10.1109/SFCS.1991.185352](https://doi.org/10.1109/SFCS.1991.185352); 1994 journal expansion [Algorithmica DOI 10.1007/BF01185212](https://doi.org/10.1007/BF01185212). [Publisher-author abstract](https://research.ibm.com/publications/checking-the-correctness-of-memories). Not two independent discoveries.
- **Source statement at publisher/author abstract level:** online sequence of reads and writes against untrusted external memory, small reliable local storage, probabilistic failure detection; prove `log n` trusted-memory lower bounds **under various assumptions** and time-space tradeoffs for RAM memory checking.
- **Do not infer:** unconditional `p >= log n` for *all* UCT encodings; the paper distinguishes protocols/models. The 1992 author-hosted PDF has difficult legacy text extraction and its individual lower-bound proof conditions were **not independently checked** in this slice. Mark `publisher_abstract_checked`.
- **UCT impact:** complete STOP on the claim "we first study dynamic integrity against unreliable memory".

### LIT-157 — Boyle–Komargodski–Vafa, STOC 2024, JACM 2025

- Canonical conference [STOC DOI 10.1145/3618260.3649686](https://doi.org/10.1145/3618260.3649686), original [ECCC TR24-014 PDF](https://eccc.weizmann.ac.il/report/2024/014/download). Later journal [JACM DOI 10.1145/3707202](https://doi.org/10.1145/3707202) is **an alternate identity of the same research, NOT a second catalog paper**.
- **Paper §1.1 Theorem 1 (informal, formal Theorem 5):** for a computationally-secure RAM memory checker with `n` logical blocks, local *reliable* storage `p` and *total number of remote accesses per logical operation* `q`,
  `p >= n / (log n)^{O(q)}`.
  For `p <= n^{1-epsilon}` constant epsilon>0, `q=Omega(log n/log log n)`. The source explicitly handles randomized/adaptive constructions with private local state. Its stated theorem uses completeness 2/3 and inverse-polynomial soundness; do not equate this with *covert* constant-risk security.
- **Paper §1.1 Theorem 3 (informal, formal Theorem 5):** separates remote **read operation** cost `q_r` and remote **write operation** cost `q_w`:
  `p >= n / (q_r q_w log n)^{O(q_r)}` in the printed informal statement. Thus for `q_r=O(1)` and `p<=n^{1-Omega(1)}`, necessarily `q_w=n^{Omega(1)}`. The paper itself notes that the converse constant-write/general-adaptive direction is not resolved by the same theorem.
- **Crucial model mismatch:** these `q_r,q_w` are remote **probe counts** for logical reads/writes, whereas LENT/UCT-003 `w` counts **physically changed encoded coordinates**. There is no free conversion `q_w=w`: an update can read many cells yet change one, or touch cells without changing content. An abstract annotated prover with unpriced work is not automatically a RAM checker.
- **UCT impact:** `STOP_GENERIC_DYNAMIC_MEMORY_QUERY_UPDATE_LOWER_BOUND` as scientific headline. Classify `publisher_full_text_spotchecked`; full original formal proof not independently reproduced.

### LIT-158 — Boyle–Komargodski–Vafa, EUROCRYPT 2025

- [Springer DOI 10.1007/978-3-031-91092-0_11](https://doi.org/10.1007/978-3-031-91092-0_11); author-publication record [IACR ePrint 2025/358](https://eprint.iacr.org/2025/358).
- **Publisher and author abstract:** strengthens the preceding checker lower-bound program to **covert security** (adversary may risk being caught with constant probability), maintaining `Omega(log n/loglog n)` overhead under the **read-only reads** property (logical reads must not modify remote or trusted memory); randomized/adaptive protocols and crypto/random-oracle assumptions covered under this model.
- An indexed original-paper excerpt labels **Theorem 3 (Main Theorem)** and displays a more explicit dependence on `n,m,w,q_r,q_w,p` with `w` the **physical word size**, not update-support; assumptions include one-bit logical words, read-only reads, completeness 99/100 and soundness error 1/3. Because official publisher site exposes the abstract and the full text was not retrievable as a stable searchable PDF here, this G1 slice **does not assert independent inspection of the formal theorem proof or exact general constants**. `publisher_abstract_checked` is the safe metadata status.
- **UCT impact:** constant-probability cheating detection **alone** is NOT a scientifically novel explanation for better fully-online checking. Do not infer that the BKV 2024 inverse-polynomial-soundness theorem by itself covers this relaxed model.

### LIT-159 — Ertem Nusret Tas–Dan Boneh, AFT 2023

- Official publication [DOI 10.4230/LIPIcs.AFT.2023.29](https://doi.org/10.4230/LIPIcs.AFT.2023.29) and [23-page proceedings PDF](https://drops.dagstuhl.de/storage/00lipics/lipics-vol282-aft2023/LIPIcs.AFT.2023.29/LIPIcs.AFT.2023.29.pdf); full author preprint [arXiv 2307.04085](https://arxiv.org/abs/2307.04085) describes **the same work**.
- **Publication Section 6, Definition 4 and Theorem 5:** under the specific `proof-binding` dynamic vector commitment property (stronger/different from mere position-binding), cryptographic security assumptions, and `g_2(k)=O(k^{1-nu})` *per-user proof refresh work*, necessarily auxiliary update-information complexity `g_1(k)=Omega(k^nu)` for `nu in (0,1)`. Exact theorem statement on publisher PDF p.29:21; the full proof is referred to a longer author version, **not reproduced here**.
- **Important cost accounting:** the publisher explicitly **excludes public updated positions and message differences from U**. `|U|` is only *extra update information*. Replacing `C_total` in UCT with this `|U|` is invalid without adding the public-diff traffic. Public parameter/preprocessing cost can also affect practical implementations; paper's asymptotic construction is not automatically cheaper than Verkle at concrete workloads.
- **UCT impact:** `STOP_GENERIC_PROOF_UPDATE_MESSAGE_VS_RUNTIME_LOWER_BOUND`. Do not claim the same inequality for all dynamic certificates that are not proof-binding or for every security regime.

## 3. Transfer/novelty classification

| Source | UCT resource dimension | Proven source scope / necessary conditions | Transfer into ROOT |
|---|---|---|---|
| BEGKN91 | trusted space, online reads/writes, sound checking | online RAM memory-checker abstraction, specific assumptions for information-theoretic lower bounds | **KNOWN_BROAD / RESTRICTED_ONLY** |
| BKV24 | trusted p, remote q, q_r, q_w | computationally-secure RAM simulation, per-logical-operation remote probes, specified completeness/soundness | **DIRECT PRIOR-ART BARRIER** when a model-preserving checker reduction exists |
| BKV25 | p, q_r, q_w, memory size/word size, covert soundness | *read-only reads* + covert adversary + source-specific security parameters | **DIRECT PRIOR-ART BARRIER** only for the properly restricted scenario |
| Tas–Boneh23 | proof update time, *extra* update broadcast | dynamic proof-binding VC with public diffs not included in U | **DIRECT PRIOR-ART BARRIER** for proof-binding VC branch |

The 2024/2025 works use `p` for local **trusted memory**, while G2-D uses `p` for data-bit **probe budget**; `w` is physical word size in BKV25 and sparse write support in LENT. Keep all notation qualified, especially in automated hypothesis comparisons. Information-theoretic lower-bound *proof techniques* do not magically extend an information-theoretic security guarantee to computational cryptography; nor do computationally secure schemes imply zero error or unbounded adversary security.

## 4. Explicit STOP decision and a narrower G2 hypothesis-selection test

**STOP NOW:** (1) "first general local-state/online checking tradeoff"; (2) "first simultaneous read/write lower bound"; (3) "first constant-risk checker lower bound"; (4) "first sublinear broadcast/proof-update tradeoff"; (5) multiplying UCT-002's capacity estimate with BKV/Tas–Boneh inequalities from *different* resource models.

**REMAINING OPEN, no novelty claim:** choose one natural *online multi-query derived service* (e.g. authenticated prefix functions or bounded-fanout incremental DAG outputs) with:
- trusted local state and **all** remote reads/writes physically counted;
- maintenance of proofs across batches and *multiple successive adversarial queries*;
- fully charged prover creation/maintenance and total public-diff + auxiliary broadcasting;
- fixed data/word model, client-prover interaction, adaptive soundness horizon and setup/public parameters.

Then map the service to the **best known RAM checker, vector commitment and online-annotation schemes** with unit-preserving reductions. Propose a concrete lower bound **only after** showing `R_n in B_known(T_n) \ Ach(T_n)` for some asymptotic family, or a matching construction. All general claims of a new worldwide theorem are **OPEN_UNPROVED**.

## 5. Reproducibility / evidence tiers

- Machine-readable literature: `LIT-156..159`; one canonical DOI per paper plus journal/preprint aliases, none separately re-counted. Author list and publication titles linked to publisher.
- Deterministic source-hypothesis matrix tests: `research/test_uct005_g1_sources.py`. Their purpose is provenance/false-claim prevention, NOT deduction of an asymptotic theorem.
- Hosted CI: `python -m unittest discover -s research -p 'test_*.py'`, `python research/literature.py --check`, other existing workflows; exact PR HEAD and post-merge main necessary.
- **State:** `G1_SOURCE_STATEMENTS_AUDITED` when CI green, `G1_PROOF_OVERLAP_PARTIAL` (not all full paper proofs independently checked), `UCT005_ROOT_OPEN`.
