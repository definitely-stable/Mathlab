# UCT-005 G3-B2-D0 — primary-source import and causal-cut novelty gates

**Snapshot:** 2026-10-10. **Owners:** UCT-005 [#105](https://github.com/definitely-stable/Mathlab/issues/105), authenticated multi-epoch task [#178](https://github.com/definitely-stable/Mathlab/issues/178). **Baseline:** main `7044fb92fefbda32d615bda6319557f43622ae98`, merged [PR #219](https://github.com/definitely-stable/Mathlab/pull/219). **Scientific status:** PRIMARY_METADATA_AND_ABSTRACT_AUDIT / MODEL_FREEZE_PROPOSAL / NO_NEW_LOWER_BOUND / UCT_ROOT_OPEN_UNPROVED.

## 1. Imported originals — unique bibliographic identities, not new Mathlab theorems

This report records eight **missing canonical records**, all compared with the 347-record `literature.json` baseline by DOI/USENIX identity, title and URL. The publisher or primary institutional abstract was checked, not the entire primary proof. Publication dates below denote **original publication**, not discovery in 2026.

| ID | Original primary work | Source inspection | Importance / model transfer barrier |
| --- | --- | --- | --- |
| LIT-349 | Li, Krohn, Mazières, Shasha — **Secure Untrusted Data Repository (SUNDR)**, OSDI 2004, [USENIX](https://www.usenix.org/conference/osdi-04/secure-untrusted-data-repository-sundr) | Original venue abstract and author list | Fork consistency: clients that exchange observed changes may detect divergence. Does **not** provide guaranteed latest state to isolated readers without a separately trusted anchor; not a page-I/O lower bound |
| LIT-350 | Cachin, Ohrimenko — **Verifying the consistency of remote untrusted services with conflict-free operations**, Information and Computation 260 (2018), [DOI](https://doi.org/10.1016/j.ic.2018.03.004) | Publisher journal abstract/identity | COP: fork-linearizability against Byzantine service, honest-service linearizability; no direct F1 anchored-latest proof or `SET/RANGE_PARITY` lower bound |
| LIT-351 | Reinhart, Blass, Annighöfer — **SNARKs for stateful computations on authenticated data**, JISA 99 (2026) 104444, [DOI](https://doi.org/10.1016/j.jisa.2026.104444) | Publisher journal abstract / open-access paper listing | ADSC-SNARK supports authenticated data and consistent state across computation iterations; no independent global monotone freshness oracle, no already-proved page/write impossibility |
| LIT-352 | Larsen — **The Cell Probe Complexity of Dynamic Range Counting**, STOC 2012, [DOI](https://doi.org/10.1145/2213977.2213987) | Author's university archive with exact DOI, venue and theorem-level abstract | Epoch/cell-sampling technique and a strong `t_q` / `t_u` tradeoff for **weighted 2D orthogonal range counting** (logarithmic-bit weights). Not directly binary 1D point-SET parity or page-I/O with trusted anchors |
| LIT-353 | Yu — **Cell-probe lower bounds for dynamic problems via a new communication model**, STOC 2016, [DOI](https://doi.org/10.1145/2897518.2897556) | Publisher paper abstract, author, DOI | Nondeterministic communication game to dynamic interval union with insert/delete, and reductions to graph problems; not immediately applicable to `RANGE_PARITY` nor a Byzantine freshness bound |
| LIT-354 | Driscoll, Sarnak, Sleator, Tarjan — **Making data structures persistent**, JCSS 38(1) (1989), [DOI](https://doi.org/10.1016/0022-0000(89)90034-2) | Publisher plus author-hosted manuscript | Node-copying/path-copying persistence upper constructions. Counterweight to generic historical-retention lower-bound attempts; neither authenticated latest state nor media durability follows |
| LIT-355 | Shangguan, Yaish, Malkhi — **Authenticated Data Structures for Dynamic Workloads**, 2026 author preprint, [arXiv:2608.25206](https://arxiv.org/abs/2608.25206) | arXiv original metadata/abstract + author publication list | Huffman-Merkle Tree adaptive access-frequency layout with priced rebalancing/batched migrations. Useful **upper** comparator for weighted membership proof size and hash-update cost; not a universal worst-hard-range improvement nor independently fresh F1 state |
| LIT-356 | Taheri Boshrooyeh, Küpçü, Özkasap — **Integrita: A BFT distributed storage system**, Future Generation Computer Systems 166 (2025), [DOI](https://doi.org/10.1016/j.future.2024.107629) | Publisher original journal abstract/DOI | q-detectable view consistency under distributed-storage multi-server Byzantine assumptions. Does not automatically provide a single-server independently trusted latest anchor or a generic lower bound; cross-model comparison only |

**Identity discipline:** journal JCSS 1989 is the canonical DSST 1986 conference extension; do not create another entry for the STOC'86 version. 2026 JISA ADSC-SNARK is the published article; do not duplicate its eprint. HMT is an **author preprint** (not asserted peer-reviewed); Integrita appeared in journal volume 166 in **2025** even though its DOI contains 2024. No proof, crypto parameter security reduction, hardware measurements or reported benchmark values were independently reproduced.

## 2. Existing canonical papers — link, do not duplicate

These **already exist in canonical literature.json** and are deliberately not reimported:

- LIT-111: Fredman–Saks, *The cell probe complexity of dynamic data structures*, STOC 1989.
- LIT-112: Pătraşcu–Demaine, *Logarithmic Lower Bounds in the Cell-Probe Model*, SICOMP 2006.
- LIT-127: *Locally Updatable and Locally Decodable Codes*, 2014.
- LIT-129/131/132: annotated streaming and Merlin–Arthur communication/verification.
- LIT-156: Blum–Evans–Gemmell–Kannan–Naor, *Checking the Correctness of Memories*, FOCS 1991.
- LIT-157/158: Boyle–Komargodski–Vafa STOC 2024 / EUROCRYPT 2025 memory checking.
- LIT-159: Tas–Boneh, *Vector Commitments with Efficient Updates*, AFT 2023.
- LIT-068: updatable BARG/IVC, ITCS 2026.
- LIT-199/200: append-only accumulator witness / vector-commitment update-frequency lower bounds (2025/2026).
- LIT-206/207/208: crash-consistency testing, filesystem models and differential fuzzing.

**Critical:** LIT-157 already studies read/write tradeoffs; LIT-159, LIT-199 and LIT-200 already restrict updating succinct authenticated evidence. "First joint update/proof lower bound" would be an unverified and probably misleading claim. Existing theorem statements must be read at original proof level before any transfer.

## 3. Model freeze proposal for H1 — not a theorem

Pick a **single natural task** before calculating conjectured bounds. A sequential honest writer maintains `x in {0,1}^n`, each `SET(i,b)` advances the epoch (including no-ops), readers issue `RANGE_PARITY(l,r)`, and a Byzantine store may replay, omit or mutate remote pages and proofs. Two independently rejoining readers may pin authenticated historical roots. Each LATEST query uses an independently trusted (epoch, digest) anchor, with **every publication and retrieval paid**, and may ABORT under withholding. Computation is PPT with parameter `lambda`; separate this from information-theoretic perfect-error variants.

Explicit full resource vector:
`R=(s_trusted_bits, S_remote_pages, B_page, U_source_reads, U_full_page_writes, U_changed_cells, Q_page_reads, C_author_update_bytes, C_reader_catchup_bytes, B_proof_bytes, G_prover_work, V_verifier_work, A_anchor_messages, T_program_setup, H_epochs, lambda, epsilon_transcript)`.

- Distinguish **worst-case across hard/adaptive ranges** from an incorrect **for every range** lower bound (C1 already falsified `W_page*Q_page >= ceil(log2 n)` for a full-range query).
- Fix either `B_page` parametrically or a clearly nonasymptotic 4096B reference; 40B SHA256 roots do **not** imply negligible adversarial advantage uniformly as `n,H -> infinity` with fixed `lambda`.
- Account for actual memory updates, unchanged-but-written pages, proof creation, pinned-history retention, garbage collection and retry messages without double-counting old and new layouts.
- Do not conflate `SUNDR/COP` fork consistency (no global anchor) with `F1` independently anchored latest-state access.
- Do not equate separate authenticated COW upper constructions with a formal Byzantine-sound implementation.

## 4. Quantified falsification program, ordered by priority

**H1 — time-expanded causal information transfers.** Define a family `D_n` of operation distributions and adaptive hard-range queries. Let `U(I)` denote entropy injected by updates in epoch interval `I` not recoverable from charged trusted state; let `P(I,J)` be the genuinely paid retained/communicated symbols surviving from `I` to a future query block `J`. Explore an inequality relating `U(I)`, `P(I,J)`, physical reads/writes and verifier evidence. The standard data-processing entropy cut is a **classical lemma**, not original; novelty would require an irreducible multi-cut overlap/online-reuse penalty on one natural task.

**H2 — pinned-history recourse.** Search for a bound on physical page writes + retained pages + worst historical/current query reads for `r` simultaneous historical PINs, **after** testing DSST persistence, immutable path copying, snapshots, logs and multiproofs. Do not charge mere logical reachability as physical movement. If ordinary persistent-data-structure upper bounds saturate the proposed inequality, record `STOP_NOVELTY`.

**H3 — robust adaptive proof maintenance.** Match UCT G3-A/B1 q-ary error-correction assumptions against computational checking and dynamic commitments. No insertion of SHA collision resistance into an unconditional counting proof. Existing BKV, Tas–Boneh, lower-update-frequency and updatable BARG results are hard novelty barriers.

## 5. First deliverable and fail-fast acceptance

1. Publish exact `SET/RANGE_PARITY` operation, Byzantine server and trusted-anchor semantics for a fixed `H=poly(n)` family, with complete resource units; label every free oracle as **assumption**.
2. Compare **same-task** upper R (trusted replica), S (snapshot), T (authenticated tree), plus DSST-style persistent layouts, authenticated delta log and (conditionally) applicable VC/IVC constructions.
3. Before any proof, propose an explicit falsifiable `F_n(R) >= g(n,H,r,B,lambda)`, including clear min/max/average quantifiers. Reject vacuous formulas and those contradicted by the existing n=4096 cheap full-range counterexample.
4. Produce a publication-by-publication full-text *theorem and assumptions* matrix, with `APPLICABLE`, `REDUCTION_REQUIRED`, `NOT_APPLICABLE` and proof notes; current import is **only** primary abstract/metadata.
5. Execute independent small finite adversarial oracle and GitHub-hosted CI; pursue an asymptotic proof only if a strictly new resource region remains beyond conjunction of **legally transferable** bounds.
6. If no novelty separation survives, issue model-scoped `STOP_NOVELTY`; do not promote G3-A/B1 or this bibliography into the unproved UCT-005 central theorem.

**Forbidden claim:** importing eight sources is not proof of the root theorem. Root [#105](https://github.com/definitely-stable/Mathlab/issues/105) stays `OPEN_UNPROVED`.
