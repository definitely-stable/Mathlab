# Research index and authority order

## UCT-005 G3-B2-B — paid authenticated range frontier (2026-10-09)

[**Same-task F1 upper frontier, conditional proofs, accounting and novelty STOP gate**](UCT-005-G3-B2-B-UPPER-FRONTIER.md) · [tree](../../research/uct005_g3b2b_range_tree.py) · [replica/full snapshot](../../research/uct005_g3b2b_baselines.py) · [independent exhaustive tests](../../research/test_uct005_g3b2b_upper.py) · [#178](https://github.com/definitely-stable/Mathlab/issues/178). Three honest upper models for sequential SET/RANGE_PARITY with an explicitly paid monotone trusted epoch/root anchor. SHA-256 assumptions only, no computational-security reduction; byte counts apply only to frozen canonical JSON/reference anchor payloads, not physical I/O. G3-B2-C must prove a **genuinely new same-model nonfactorizing lower bound** or STOP_NOVELTY; UCT root remains OPEN.




## TKG-001 G0 — bitemporal fact/provenance DAG (2026-10-09)

[Exact as-of, 2^k witness expansion, recourse countermodels and prior-art barrier](TKG-001-G0-BITEMPORAL-PROVENANCE-AND-RECOURSE.md) · [issue #190](https://github.com/definitely-stable/Mathlab/issues/190) · [independent exhaustive test](../../research/test_tkg001_bitemporal.py). Distinct valid time and transaction epoch, alternative evidence, no uncharged freshness channel. **No new universal theorem or production code.**

## UCT-005 G3-B2-A — independent-reader freshness versus paid trusted root (2026-10-09)

[**Model, classical F0 indistinguishability proof, conditional F1 upper point and novelty barriers**](UCT-005-G3-B2-A-FRESHNESS-INDISTINGUISHABILITY.md) · [source identities](UCT-005-G3-B2-A-SOURCES.json) · [standalone exhaustive F0/F1 tests](../../research/test_uct005_g3b2a_freshness.py) · [G3-B2 #178](https://github.com/definitely-stable/Mathlab/issues/178). For signed full n-bit snapshots, two equal delivered historical transcripts can hide different latest range parities (F0): authentic past != globally latest. F1 adds independently trusted monotone epoch+seal publication, **bills every writer publication and reader trusted call**, and aborts if unavailable. Client persists only epoch+seal. Fork with conflicting signed siblings requires **author equivocation**; server-only forked views can be different authentic prefixes. CLASSICAL/NO NOVEL ROOT, symbolic signatures, not production crypto or byte-accurate I/O. Next G3-B2-B.



## HYP-105 G5-E2-B3.0 — six-edge factor forests / pair 2-core (2026-10-09)

[Proof and all-h bound](HYP-105-G5-E2-B3-FOREST-PROJECTION.md) · [finite exact checker](../../research/hyp105_g5e2b3_forests.py) · [independent tests](../../research/test_hyp105_g5e2b3_forests.py) · [issue #176](https://github.com/definitely-stable/Mathlab/issues/176). Classical finite weighted-simple-graph polynomial counts all 11 six-column projection profiles; 41,209 factor endpoint shapes, 11,663 surviving leafless factor-forest patterns; all-h **E_uniform-pair-label[R3]=O(s^6)** combined with previously established Omega(s^6) gives Theta(s^6) for independent random labels **only**. Does NOT yield R3=o(s^6), any individual-label lower, actual GF5 six-flow positivity, or new ASET power. B3.1/B3.2 remain open.

## HYP-105 G5-E2-B3.1-A — exact critical signed six-flow motifs (2026-10-09)

[Exact color-preserving signed GF5 2-factor census, all-h matching-risk floor](HYP-105-G5-E2-B3-B1-CRITICAL-FLOWS.md) · [stdlib finite graph oracle](../../research/hyp105_g5e2b3b1_critical_flows.py) · [independent GF5 MITM tests](../../research/test_hyp105_g5e2b3b1_critical_flows.py) · [issue #176](https://github.com/definitely-stable/Mathlab/issues/176). Full 70² × 10 leading **matching+6+6** colored signed configurations, reduced to 110 true colored-signed orbits by column-label stabilizers: 108 positive (48,900 labeled cases) and two zero (100 labeled cases); F>0 iff the six-column contracted graph is connected. Verified by exact prescribed-boundary flow IE and independent MITM. Explicit alternating C6 witness gives E_random-pair-label[R3]>=Omega(s^6) from the factor-matchings branch alone. No proof of a fixed-label or strict R3 power bound; no ASET promotion.

## UCT-005 G3-B1 — temporal trajectory packing theorem (2026-10-09)

[Full restricted proof and temporal novelty check](UCT-005-G3-B1-TEMPORAL-TRAJECTORY-PACKING.md) · [2026 published authenticated-state paper](UCT-005-G3-B1-SOURCES.json) · [issue #175](https://github.com/definitely-stable/Mathlab/issues/175) · [finite oracle](../../research/test_uct005_g3b1_trajectory.py). Realizable e=1, p=3 trajectory model: q=2, m=7, d=3, w=3 gives **2784 vs 3072** independent epoch bounds; a threefold repetition code actually attains 8 histories on three accessed cells. PROVED RESTRICTED CLASSICAL, **original UCT-005 root OPEN**; no authenticated freshness or physical updater read bound.

## INDEX-001 G2-B3-B — deterministic online checkpoint and finite adversary (2026-10-09)

[**Frozen reveal-before-recovery model, elementary ≤2 upper-bound proof and explicit rent-or-buy novelty STOP**](INDEX-001-G2-B3-B-ONLINE-ADVERSARY.md) · [issue #156](https://github.com/definitely-stable/Mathlab/issues/156) · [algorithm and bounded adversary](../../research/index001_online_checkpoint.py) · [independent adversarial tests](../../research/test_index001_online_checkpoint.py). The age threshold `ceil(S/E)` has an elementary component-wise ≤2 bound relative to the exact *clairvoyant* G2-B2-B oracle for **fixed-frame, no-hard-cap** accounting; this is NOT a novel universal lower bound, randomized/optimal online proof, device-NAND measurement or Rust engine. Finite restart-alphabet tests and exact POSIX write/read byte counter crosschecks; existing LIT-098 and current 2026 ski-rental source research explicitly mark prior art.


## UCT-005 G3-A — одна общая математическая конструкция (2026-10-09)

[**Robust Observable-State Reachability: формальная общая теорема, 3 точные специализации и проверяемая карта связей Mathlab**](UCT-005-G3-A-ROBUST-OBSERVABLE-STATE-THEOREM.md) · [корневая UCT-005 #105](https://github.com/definitely-stable/Mathlab/issues/105) · [G3 #164](https://github.com/definitely-stable/Mathlab/issues/164) · [независимые тесты](../../research/test_uct005_g3_robust.py). Joint dynamic state/update graph, trusted label H, remote q-ary Hamming locality d*w, t adaptive p-probe exact queries and e corrupted symbols: **K ≤ 2^H max_{s≤M} floor(V_q(s,dw+e)/V_q(s,e))**, **M=min(m,tΣ_{i<p}q^i)**. Sparse GF(q) counterpart = exclusion of signed *near trades* of syndrome weight ≤2e; temporal influence adds typed UCT-003 transversal. **SELF-CONTAINED_PROVED_CLASSICAL / ROOT ORIGINAL NOVELTY OPEN / NO RUST**; remote adversarial corruption ≠ cryptographic proof soundness.


## DAG-002 × ALG-001 G1-B — conditional adaptive-probe/write frontier and maintained GF(2) syndrome (2026-10-09)

[**Conditional joint H/B+G, P, W, c, N bound and its known coding limits**](DAG-002-ALG-001-G1-B-ADAPTIVE-DECISION-TREES.md) · [G1 #140](https://github.com/definitely-stable/Mathlab/issues/140) · [G1-B #157](https://github.com/definitely-stable/Mathlab/issues/157) · [independent exhaustive oracles](../../research/test_dag002_g1b_adaptive.py). Fixed prior physical history and K distinct successor answer vectors require `K ≤ 2^H V_c(M,W)`, `M=min(N,n Σ_{d=0}^{P−1}2^{cd})`; **elementary classical-style decision-tree counting**, NOT new UCT-005 proof. P=1 impossible in n=2,H=0,N=3,W=1, while classical Hamming parity-check syndrome admits P=2, one remote update read and one write per nonzero DELTA, all online histories. Target updates require additional charged reads. No cryptography, physical page bytes, novelty or Rust; G1-C remains OPEN.


## INDEX-001 G2-B3-A — two-slot snapshot/manifest crash-boundary research (2026-10-09)

[**Frozen two-generation manifest/LSN WAL checkpoint ordering, explicit fail-closed boundary and primary literature**](INDEX-001-G2-B3-A-GENERATION-COMMIT-PROTOCOL.md) · [issue #146](https://github.com/definitely-stable/Mathlab/issues/146) · [two-slot stdlib POSIX reference](../../research/index001_generations.py) · [crash/GC/dense-oracle tests](../../research/test_index001_generations.py) · [deterministic comparative audit](../../research/index001_generation_audit.py). Includes three source identities LIT-206..208 (PoWER OSDI 2025, Ferrite ASPLOS 2016, DIFFuzzer ISP RAS 2026); primary abstracts/identities checked, proofs NOT independently verified. **One writer; process-stop failpoint testing is NOT real power-loss proof**. Corrupt selected generation fails closed, prior snapshot is not automatically a valid fallback after WAL truncate. Hardware crash theorem and Rust API remain NO-GO.


## UCT-005 G2-B2 — exact multi-subscriber information broadcast (2026-10-09)

[**Restricted quotient theorem, rank-vs-one-hot falsifiers and finite independent coloring oracle**](UCT-005-G2-B2-EXACT-BROADCAST-QUOTIENT-AND-STOP.md) · [three original proof-labeling sources](UCT-005-G2-B2-SOURCES.json) · [executables](../../research/test_uct005_g2b2_broadcast.py) · [issue #151](https://github.com/definitely-stable/Mathlab/issues/151). Exact `b*=ceil(log2 |{A d : d in D}|)` for **deterministic synchronous zero-error shared messages without uncharged update side information**. Classical elementary communication result, **NOT a new cryptographic theorem or universal UCT-005 root**. Three papers indexed in typed source inventory; canonical numbering deferred behind PR #132 / issue #142.

## UCT-005 G2-B1 — semantic vs structural influence and online proof barriers (2026-10-09)

[**Exact odd-path influence in mutable XOR DAGs, proof/certificate structural dirty-set comparison and unbounded cancellation family**](UCT-005-G2-B1-DAG-SEMANTIC-STRUCTURAL-COUNTERMODELS.md) · [two new original primary publications plus LIT-068 and LIT-187 without duplication](UCT-005-G2-B1-SOURCES.json) · [exhaustive DAG and independent path-count tests](../../research/test_uct005_g2b1_dag_influence.py) · [issue #148](https://github.com/definitely-stable/Mathlab/issues/148). Restricted classical GF(2) lemma + conditional hash representation; **not original root theorem**, no computational security proof. Extra primary source identities pending canonical LIT numbering until issue #142/PR #132 resolution.

## DAG-002 × ALG-001 G1-A — priced remote probes, cells and sparse updates (2026-10-09)

[**Formal G1-A single-append write-state counting, exact covering-code prior-art barrier and falsifiers**](DAG-002-ALG-001-G1-A-PRICED-PROBE-WRITE-FRONTIER.md) · [issue #140](https://github.com/definitely-stable/Mathlab/issues/140) · [finite stdlib oracle](../../research/test_dag002_g1a_frontier.py). Fix input-independent old prefix and remote snapshot, local B+G bits, N c-bit remote cells, W final changed cells, P reads/query. Elementary necessary bound `2^(B+G) V_c(N,W)>=2^n`, independently proved but **NOT novel**; restricted XOR-delta one-bit-probe family is **known covering-code K(n,W)**, not a universal probe lower bound. The 2026 Young Kun Ko Multiphase paper and Cohen et al. 1986 covering code bound explicitly prohibit premature uniqueness claims. **G1-A MODEL_ONLY+FINITE EXACT / G1-B NONFACTORIZING OPEN / no Rust.**


## INDEX-001 G2-B2-B — exact offline checkpoint policy, recovery and tempfile lifecycle (2026-10-09)

[**Frozen fully-priced (write/recovery/storage byte-steps/peak) reference model, offline DP proof and adversarial controls**](INDEX-001-G2-B2-B-CHECKPOINT-POLICY.md) · [issue #143](https://github.com/definitely-stable/Mathlab/issues/143) · [policy, POSIX oracle and reporter](../../research/index001_checkpoint_policy.py) · [independent exhaustive policy+fault tests](../../research/test_index001_checkpoint_policy.py). **Mathlab research only**: DP has advance knowledge of restart events, solves a restricted fixed-image WAL protocol (not a new general theorem or online-competitive index); counts application byte lengths and on-disk file `stat()`, not physical SSD/NAND writes. Checks temporary snapshot orphan at interrupted checkpoint. G2-B parent #126 and stronger crash/online-theorem gates remain OPEN.


## INDEX-001 G2-B2-A — reproducible application-byte comparisons (2026-10-09)

[**Exact snapshot-vs-WAL frame-count equations, four deterministic range workloads and compaction thresholds 1/4/16**](INDEX-001-G2-B2-A-APPLICATION-IO.md) · [issue #137](https://github.com/definitely-stable/Mathlab/issues/137) · [stdlib reporter](../../research/index001_workload_io.py) · [independent tests](../../research/test_index001_workload_io.py). Counts actual returned `os.write` bytes + application `read_bytes` with exact restart-state oracle, NOT device physical NAND writes or a new general algorithmic theorem. Prior art LIT-098/175/176/182/184..186 reused without new source identity. G2-B2-A measured-model only / PHYSICAL_LOWER_BOUND_OPEN / NO_RUST.


## UCT-005 G2-B — 2D authenticated XOR: frozen model, adversarial replay and source STOP (2026-10-09)

[**Fully priced authenticated 2D parity model, explicit update/query transcript, finite adversarial oracle and quantitative non-novelty checks**](UCT-005-G2-B-VERIFIED-2D-PARITY-AND-NOVELTY-GATE.md) · [five original 2016–2026 source identities](UCT-005-G2-B-SOURCES.json) · [tests](../../research/test_uct005_g2b_auth_tree.py) · [issue #131](https://github.com/definitely-stable/Mathlab/issues/131). Published dynamic multidimensional query authentication and aggregate ADS defeat generic novelty claims. **G2-B evidence only; full-source proofs not reproduced, cryptographic security not proven, central UCT-005 theorem OPEN_UNPROVED.** Pending canonical LIT numbering while parallel HYP-105 PR #132 owns LIT-205.

## DAG-002 / ALG-001 G0 — immutable reachability and rank-sensitive output separation (2026-10-09)

[DAG-002 model, known SEA chain-top baseline and no-remote-probe information bound](DAG-002-G0-IMMUTABLE-REACHABILITY.md) · [ALG-001 rank-one coordinate-observation barrier, precise field/update types](ALG-001-G0-RANK-OBSERVATION.md) · issues [#133](https://github.com/definitely-stable/Mathlab/issues/133) and [#134](https://github.com/definitely-stable/Mathlab/issues/134). **RESTRICTED_ELEMENTARY_PROOF, KNOWN_PRIOR_ART, FINITE_EXACT_CHECKS, NO_NEW_ROOT_THEOREM, NO_RUST.** Canonical studies LIT-187/LIT-195 already indexed; no re-import and no modification of other research status.


## INDEX-001 G2-B0/B1 — durable WAL/checkpoint exact range-map reference (2026-10-09)

[**Frozen binary WAL/snapshot contract, CRC and linearization/fsync assumptions, explicit fault matrix**](INDEX-001-G2-B0-DURABILITY-PROTOCOL.md) · [issue #126](https://github.com/definitely-stable/Mathlab/issues/126) · [Python stdlib reference](../../research/index001_durable.py) · [independent dense/recovery tests](../../research/test_index001_durable.py). A deliberately inefficient one-writer full-snapshot baseline and append-WAL/checkpoint reference distinguish *application-level* returned read bytes and `os.write` bytes from physical disk/NAND bytes. G2-B1 is **POSIX RESEARCH REFERENCE ONLY**; no concurrent writers, fault-tolerant hardware proof, new asymptotic lower bound or Rust API. G2-B2 and physical proof gates OPEN; exact-head hosted CI required.


## UCT-005 G2-A — новые математические барьеры (2026-10-09)

[**Аудит семи источников, из которых шесть новых, и точные онлайн-контрмодели**](UCT-005-G2-A-NEW-FUNDAMENTAL-BARRIERS.md) · [issue #125](https://github.com/definitely-stable/Mathlab/issues/125) · [1D/2D oracle](../../research/test_uct005_g2a_models.py). В библиографии теперь **204 уникальных публикации** (новые LIT-199..204); STOC 2026 уже учтён как LIT-072. **G2-A: STOP простой 1D-корень; G2-B: 2D authenticated multi-query SCOUT; root novelty OPEN.**

## HYP-105 G5-C3-A — exact coordinate-gauge invariant and deterministic W32 label search (2026-10-09)

[Mathematical proofs and all-scale limitations](HYP-105-G5-C3-A-STRUCTURED-LABEL-SEARCH.md) · [certified bounded search code](../../research/hyp105_g5c3_label_search.py) · [independent regression](../../research/test_hyp105_g5c3_label_search.py) · [merged #122](https://github.com/definitely-stable/Mathlab/pull/122) · [hosted exact PR-head Research #1077 SUCCESS](https://github.com/definitely-stable/Mathlab/actions/runs/37896067333). Elementary all-field coordinate-gauge invariance, explicit S6×S6 class count (15!/6!)² for split K6 pair bijections; reproducible finite m12 W32 minimal T4:46→42 and T6:1722→1580, with 20 independently validated ASET columns before AND after. **No all-m density theorem, no exponent improvement, no original theorem novelty, no Rust.** Further work on [G5-C3 #119](https://github.com/definitely-stable/Mathlab/issues/119), [#106](https://github.com/definitely-stable/Mathlab/issues/106), [#95](https://github.com/definitely-stable/Mathlab/issues/95) remains OPEN: demand uniform algebraic pair label design and proved T4/T6 estimates.


## INDEX-001 G2-A — synthetic page-cost comparator and 2026 compaction novelty closure (2026-10-09)

[**Range overlay vs direct materialization: precise simulated cold page reads, journal/compaction writes, original 2025/26 prior-art audit**](INDEX-001-G2-A-PAGE-COST-AND-PRIOR-ART.md) · [issue #121](https://github.com/definitely-stable/Mathlab/issues/121) · [simulation module](../../research/index001_page_cost.py) · [independent finite tests](../../research/test_index001_page_cost.py). **LIT-183..186**, 182→186 canonical sources, attached SPIRE'24 preliminary identity to theoretical LIT-183, kept practical LIT-180 separate (no duplicate). G2-A MODEL_ONLY / physical lower bound OPEN / generic H2 adaptation novelty STOP / no Rust. No actual disk I/O or crash recovery implied.


## INDEX-001 G0/G1 (2026-10-09) — exact range-map elementary lemmas and original source barriers

[**Formal half-open latest-write-wins range-map model, elementary counting/boundary results, fully priced physical-cost roadmap and six new original publications**](INDEX-001-G0-RANGE-MAP-FOUNDATION.md) · [issue #117](https://github.com/definitely-stable/Mathlab/issues/117) · [independent finite oracle](../../research/test_index001.py) · [source provenance tests](../../research/test_index001_sources.py). LIT-177..182 expand imported corpus 176→**182**, without duplicating RASK LIT-175, competitive dynamization LIT-098, or UCT-005 sources. **L1/L2 elementary logical results only; PHYSICAL_LOWER_BOUND_OPEN, NOVELTY_UNPROVED, NO_RUST.** Research suite and source-index checks must pass on exact PR head; no false implication from interval stabbing or dictionary cell probes to write amplification.


## HYP-105 G5-C2 — exact trade density and random-labeling obstruction (2026-10-09)

[Conditional classical alteration frontier, exact finite W32 trade spectrum, proved expected six-trade Omega(m^4) random-label barrier](HYP-105-G5-C2-DENSITY-GATE.md) · [code](../../research/hyp105_g5c2_density.py) · [independent tests](../../research/test_hyp105_g5c2_density.py) · [merged PR #116](https://github.com/definitely-stable/Mathlab/pull/116) · [GitHub Research #989 SUCCESS](https://github.com/definitely-stable/Mathlab/actions/runs/37893926865). Correctly separates *conditional sufficient* trade count thresholds b4<52/15, b6<4 for GQ-style N~m^(8/3) alteration from *proved* expectation lower E_random_label[T6]=Omega(m^4). Exact m12 GQ 45-column subfamilies yield 19-20 independently verified ASET columns, with labels altering T4/T6 despite factor graph girth8; no finite exponent claim. **DERIVED_CLASSICAL / MODEL_SCOPED_NO_GO / NO_NEW_ASET_BOUND / NO_RUST.** G5-C [#106](https://github.com/definitely-stable/Mathlab/issues/106), parent [#95](https://github.com/definitely-stable/Mathlab/issues/95) remain OPEN. Next [G5-C3 #119](https://github.com/definitely-stable/Mathlab/issues/119): nonuniform/deterministic coordinate label designs or bounded STOP of random-first-moment track.


## UCT-005 G1 — первоисточники memory checking и vector commitments (2026-10-09)

[**Проверка условий классических теорем и границ переноса на UCT**](UCT-005-G1-MEMORY-CHECKING-AND-VC-PRIMARY-AUDIT.md) · [issue #113](https://github.com/definitely-stable/Mathlab/issues/113). **LIT-156..159**, всего **159** отдельных работ (журнальные/препринт версии не дублируются). Источники устанавливают существующие trade-offs доверенной памяти/удалённых обращений, covert soundness и динамических доказательств. **STOP** общая новизна таких комбинаций; строгая модель центральной теоремы и новая совместная граница пока **OPEN**. Проверки машинного каталога не означают независимого воспроизведения опубликованных доказательств.

## ROOT RESEARCH OBJECTIVE — UCT-005 (2026-10-09)

**[UCT-005 fundamental-root theorem program and typed research tree](UCT-005-ROOT-THEOREM-PROGRAM.md)** · [root issue #105](https://github.com/definitely-stable/Mathlab/issues/105). **OPEN / THEOREM NOT PROVED / NOVELTY NOT ESTABLISHED.** All earlier LENT/HYP/TOM/UCT work is classified as a proven foundation, proof ingredient, special case, adversarial countermodel or explicitly unreduced application; never invent theorem implications between different models. The target is ONE new, strictly nonfactorizing result for a fully priced online dynamic/verification task. Four urgent missing source-level barriers: online memory checking (1991), tight memory checking (2024), covert-secure checker (2025), and dynamic vector-commitment proof-refresh tradeoffs (2023). The historical UCT-002 capacity theorem is classical and **is not** the new root theorem.

## HYP-105 G5-B — exponent-tight graph-only relaxation is NOT an ASET construction (2026-10-09)

[**Exact bipartite graph-to-canonical-2+2-column embedding and generalized-quadrangle asymptotic NO-GO**](HYP-105-G5-B-GIRTH-RELAXATION.md) · [512 complete tiny graph embeddings plus independent symplectic W(3,2) 45-column tests](../../research/test_hyp105_g5b_graph_realization.py) · [issue #103](https://github.com/definitely-stable/Mathlab/issues/103) · [parent #95](https://github.com/definitely-stable/Mathlab/issues/95). Every bipartite graph on at most binom(a,2) and binom(b,2) vertices per part is realizable as the canonical first-two/last-two support-four **factor graph** (modulo isolates) on a+b coordinates. Existing girth-eight generalized quadrangles give **Theta(m^(8/3)) factor-graph edges**, so ordering constraints plus *only* forbidden C4/C6 cannot sharpen the G4 exponent. **But these columns are NOT necessarily ASET**: already W(3,2) on 12 coordinates has 45 columns and girth-eight factor graph with an explicit 2-vs-2 signed collision. Prior **LIT-136/148 reused**, current source corpus unchanged; this is derived classical NO-GO, not an improved ASET bound or original theorem. **Lefmann 2005 LIT-043 logarithmic correction:** the published lower is Ω_q(m^(12/5) (log m)^(1/5)) for k=6,r=4 (gcd(5,4)=1). Exponent interval [12/5,8/3] remains OPEN.

## HYP-105 G5-C0 — source-corrected weighted ASET/linear oracles (2026-10-09)

[**Strict model separation, four independent exact finite oracles, and Naor–Verstraëte 2008 Theorem 2.2 priority correction**](HYP-105-G5-C0-SIGNED-ORACLE-FOUNDATION.md) · [tests](../../research/test_hyp105_g5c_signed_oracles.py) · [merged PR #108](https://github.com/definitely-stable/Mathlab/pull/108) · [research CI #926 SUCCESS](https://github.com/definitely-stable/Mathlab/actions/runs/37889704751). Over GF5, exact support-four three-column ASET does **not** imply arbitrary-coefficient three-wise independence. Original 2008 Theorem 2.2 already yields the G4 ASET upper O_q(m^(8/3)); **not an original Mathlab exponent**. The genuine exponent window [12/5,8/3], with Lefmann logarithmic lower correction, remains OPEN. G5-C [#106](https://github.com/definitely-stable/Mathlab/issues/106) and parent [#95](https://github.com/definitely-stable/Mathlab/issues/95) stay OPEN; no ratio theorem or Rust claim. No bibliography duplicate.


## HYP-105 G5-B — exponent-tight graph-only relaxation is NOT an ASET construction (2026-10-09)

[**Exact bipartite graph-to-canonical-2+2-column embedding and generalized-quadrangle asymptotic NO-GO**](HYP-105-G5-B-GIRTH-RELAXATION.md) · [512 complete tiny graph embeddings plus independent symplectic W(3,2) 45-column tests](../../research/test_hyp105_g5b_graph_realization.py) · [issue #103](https://github.com/definitely-stable/Mathlab/issues/103) · [parent #95](https://github.com/definitely-stable/Mathlab/issues/95). Every bipartite graph on at most binom(a,2) and binom(b,2) vertices per part is realizable as the canonical first-two/last-two support-four **factor graph** (modulo isolates) on a+b coordinates. Existing girth-eight generalized quadrangles give **Theta(m^(8/3)) factor-graph edges**, so ordering constraints plus *only* forbidden C4/C6 cannot sharpen the G4 exponent. **But these columns are NOT necessarily ASET**: already W(3,2) on 12 coordinates has 45 columns and girth-eight factor graph with an explicit 2-vs-2 signed collision. Prior **LIT-136/148 reused**, current source corpus unchanged; this is derived classical NO-GO, not an improved ASET bound or original theorem. **Lefmann 2005 LIT-043 logarithmic correction:** the published lower is Ω_q(m^(12/5) (log m)^(1/5)) for k=6,r=4 (gcd(5,4)=1). Exponent interval [12/5,8/3] remains OPEN.

## UCT-004 G2-D — all-n nonlinear/adaptive proof bits, not exact κ (2026-10-09)

[Self-contained theorem and independent reconstruction of PPZ isolated-CNF lemma](UCT-004-G2-D-ALL-N-PPZ-PROOF-BITS.md) · [primary 1999/2022 source-model audit](UCT-004-G2-D-PPZ-PRIMARY-SOURCE-AUDIT.md) · [issue #98](https://github.com/definitely-stable/Mathlab/issues/98). **For every n,p** in the frozen G2-C game, `b_min(n,p)=ceil(n/p)-1` holds for *arbitrary nonlinear/adaptive*, private-coin sound proof verifiers with perfect completeness and any delta<1, independently of linear tests. Proof reduces each witness fiber to isolated width-p CNF and applies a self-contained derivation of the **classical PPZ 1999** lemma; matching block-parity construction. General exact κ remains OPEN when n/p is noninteger; do not infer κ power of two from b. Test `research/test_uct004_ppz_all_n.py`; 155 canonical sources (new LIT-154/155), 55 known/STOP records, 20 typed theorem nodes. **DERIVED_CLASSICAL, not an original global theorem; no Rust.**

## HYP-105 G5-A — exact signed-trade obstruction beyond pair-graph girth (2026-10-09)

[Six-column, 12-coordinate **matching** factor-graph with equal three-element sums in every characteristic; exact separated projection-kernel intersection criterion and 2026 union-free source audit](HYP-105-G5-A-TRADE-INTERSECTION.md) · [independent direct-sum/graph/kernel test oracles](../../research/test_hyp105_g5_trades.py) · [parent issue #95](https://github.com/definitely-stable/Mathlab/issues/95). This **refutes girth-eight sufficiency**, not its necessity from G4. Three-edge 4-uniform GF5 family is ASET but not union-free, confirming the exact source-model difference. Liu–Shangguan–Zhang 2026 revised v3 is **already LIT-005**; new proof explicitly checks (3,4) is excluded from the latest leading-constant theorem. Three other genuinely absent primary studies LIT-151..153 imported, corpus **153 works**. No new exponent/ratio, scientific originality or Rust claim; full [12/5,8/3] remains OPEN.

## UCT-004 G2-C — exact nonlinear parity proof-cover characterization (2026-10-09)

[Self-contained C1/C2/C3 equivalence, finite κ table and classical caveats](UCT-004-G2-C-NONLINEAR-PROOF-COVER.md) · [September 2026 certification and PCPP prior-art audit](UCT-004-G2-C-SOURCE-NOVELTY-AUDIT.md) · [issue #93](https://github.com/definitely-stable/Mathlab/issues/93). Perfect-completeness private-coin b-bit untrusted verification of n-bit parity with at most p adaptive data probes and **some** delta<1 exists iff both parity classes admit ≤2^b p-projection-separable sets covering all correct states. Exact b_min=ceil(log2 κ(n,p)); **PROVED_DERIVED_CLASSICAL** with potential exponential program description and weak soundness. Independent brute-force/minimum-set-cover tests for n≤5; κ matches the block bound on those finite cases, general equality still **OPEN**. LIT-149..150 primary-source imports, total **150**; anti-rediscovery **52**; typed brick graph **19 nodes**. No original-world novelty claim, Rust, crypto or production promise.

## HYP-105 G4 — sharp field characteristic and improved full weight-four upper (2026-10-09)

[Full theorem/counterexamples/primary-source audit](HYP-105-G4-CHARACTERISTIC-W4.md) · [independent finite checks](../../research/test_hyp105_g4_characteristic.py) · [issue #90](https://github.com/definitely-stable/Mathlab/issues/90). For *unit columns of a linear r-uniform hypergraph*, r>d and field characteristic p>d imply exact d-subset sums; coned grids refute extension to p=d, including the explicit GF3 size4 3-vs-3 collision; GF2 K6-minus-matching gives another. A complete **GF3 signed-set** census in linear 3graphs finds **10 five-edge, 70 six-edge** obstruction types among 531 certified G3 cores. Critically the full weight4 d3 ASET problem remains separate: splitting each support4 vector into two weighted pairs forces a bipartite **C4/C6-free** factor graph, giving the stronger all-fields **`A_set(q,m,4,3)=O_q(m^(8/3))`** rather than O(m³). With Lefmann's `A_lin(q,m,4,6)=Omega_q(m^(12/5))`, true growth and separation remain OPEN. Four primary works LIT-145..148 added atop existing **144** UCT-004 records; corpus **148**. No original scientific novelty/Rust claim.

## UCT-004 G2-A — private-coin sound witness, fractional packing and proof-length frontier (2026-10-09)

[Deductive theorem with two sharp constructions](UCT-004-G2-A-SOUND-WITNESS-PACKING.md) · [2026 and classical original primary-source barriers](UCT-004-G2-A-PRIMARY-SOURCE-AUDIT.md) · [issue #87](https://github.com/definitely-stable/Mathlab/issues/87). Soundness against every dishonest witness plus exact charged bit accesses yields data-probe p>=(1-alpha-delta)*nu-star for fractional packing of output-sensitive changed-code supports; with w=1 full parity p>=n(1-alpha-delta), tight at alpha=0. A **separately restricted** GF(2) one-check linear verifier has a sharp rank/cover witness-byte inequality b>=ceil(n/p)-1, achieved by block parity with delta=1-1/ceil(n/p). Independent finite nonlinear verifier oracle exposes that n=4,p=3 permits a six-state weight-two parity proof fiber, strictly exceeding the linear rank fiber cap four; this refutes only the **wrong transfer** of the rank proof to nonlinear tests, not the proven linear theorem. See `research/test_uct004_nonlinear_scope.py` and KR-051.

Independent finite exact test oracles; 144 canonical external sources (3 newly LIT-142..144), 51 known/STOP decisions (KR-048..051), typed 18-node theorem bricks. **DERIVED_CLASSICAL, not new original general theory**, fully priced online malicious-proof systems and arbitrary adaptive nonlinear verifiers remain OPEN. No Rust.

## HYP-105 G3 — six-column integer minor theorem and no-gap classification (2026-10-09)

[Complete core-model reduction and exact determinantal-divisor proof](HYP-105-G3-SIX-COLUMN-MINORS.md) · [exhaustive 531-core enumerator](../../research/hyp105_minor.py) · [modular and exact-arithmetic tests](../../research/test_hyp105_minor.py) · [issue #86](https://github.com/definitely-stable/Mathlab/issues/86). For a linear 3-uniform hypergraph with unit 0/1 incidence columns, **six-wise independence over every field of characteristic p≥5 iff no 3×3 grid**. All maximal-minor gcds of 531 complete incidence-core types are 0,1,2,3,4, with all ten singular types grids. Thus published dense grid-free graphs give A_lin(q,m,3,6)=A_set(q,m,3,3)=Theta_q(m²), **bounded ratio**, superseding G2's open denominator. Computer-assisted, originality unverified, no Rust/product claim. Source catalog LIT-137 (published 2022) reused, not duplicated.

## UCT-003 G1 — adaptive influence transversal and both sharp one-unit endpoints (2026-10-09)

[Deductive proof](UCT-003-G1-ADAPTIVE-INFLUENCE-THEOREM.md) · [prior-art barrier / G2 directions](UCT-003-G1-SOURCE-AND-GAP-AUDIT.md) · [issue #82](https://github.com/definitely-stable/Mathlab/issues/82). For exact deterministic bit-probe queries, affected old-state read paths must intersect changed stored cells. Theorem B completely characterizes p=1 Boolean function classes and writes; Theorem C proves complete hypercube unit-write rigidity and minimum deterministic decision-tree read depth, giving sharp opposite prefix-parity extremes (p=1 -> w>=n, w=1 -> p>=n). **DERIVED_CLASSICAL, NO worldwide novelty claim.** Fenwick falsifies w*p>=n for general p. Exhaustive finite tests `research/test_uct003_influence.py`, known/STOP **47** records (KR-045..047), newly imported static bit-probe original **LIT-141** (total bibliography **141**). Strong p>=2+fully priced sound-proof theorem remains OPEN.

## HYP-105 G2 — quadratic capacity of exact three-sums (2026-10-09)

[Self-contained **grid-free ⇔ subset-sum injection** proof for linear 3-uniform unit-incidence systems over char≥5, and derived (A_q^{set}(m,3,3)=\Theta_q(m^2))](HYP-105-G2-GRID-FREE-QUADRATIC.md) · [all 4096 AG(2,3) subfamilies with independent grid/sum oracles and characteristic-three counterexample](../../research/test_hyp105_grid.py) · [issue #84](https://github.com/definitely-stable/Mathlab/issues/84). Dense **grid-free** linear triple systems already existed in Gishboliner–Shapira (2022): mathematical consequence is DERIVED_CLASSICAL, **not original**. Six-wise-linear-independence denominator remains unresolved: `Omega(m^9/5) <= A_lin(m,3,6) <= O(m²)`; no unbounded ratio proved. External catalogue 136 -> **140**, LIT-137..140.

## HYP-105 G1 — weight-two d=3 asymptotic non-separation (2026-10-09)

[Self-contained graph girth proof with exact parameter scope](HYP-105-G1-W2D3-GIRTH8.md), [finite 30-vertex/45-edge symplectic quadrangle oracle](../../research/test_hyp105_girth.py), [issue #80](https://github.com/definitely-stable/Mathlab/issues/80). For **every fixed finite field** q, both A_set(q,m,2,3) and A_lin(q,m,2,6) are Theta_q(m^(4/3)). Hence proposed **unbounded** asymptotic ratio is refuted for w=2,d=3; original existential HYP-105 with other w/d is unresolved. The result derives from classical extremal girth/geometry, **NOT new scientific novelty**. Primary-source catalog expanded 134 -> **136** with Wenger 1991 and Abreu et al. 2011.

## UCT-002 — unified operational observation capacity (2026-10-09)

[Cross-domain master theorem](UCT-002-MASTER-THEOREM.md) · [16-node typed theorem-brick DAG](UCT-002-THEOREM-BRICKS.json) · [primary-source and model-transfer audit](UCT-002-PRIMARY-SOURCE-AND-BRICKS.md) · [issue #77](https://github.com/definitely-stable/Mathlab/issues/77). Joint q-ary update locality, maintained memory, annotated verifier communication, total adaptive source reads and finite-error Fano bound: **DERIVED_CLASSICAL, not an original unified scientific theorem**. Stronger nonfactorizing frontier remains OPEN. Eight additional deduplicated sources **LIT-127..134**, now **134** unique external identities; independent stdlib finite tests `research/test_uct002_joint_capacity.py`. The concurrent HYP-101 G1 source cohort LIT-123..126 is preserved.

## HYP-101 G1 — exact BLAKE3 leaf input phase/counter reuse audit (2026-10-09)

[Position-dependent leaf-input cache lemma, periodic counterexample, rigorous scope of applicability, source-to-theorem comparison](HYP-101-G1-PHASE-COUNTER-FRONTIER.md) · [independent exhaustive structural tests](../../research/test_hyp101_phase_counter.py), issue [#72](https://github.com/definitely-stable/Mathlab/issues/72). This is **PROVED_CLASSICAL_CACHE_COUNT / STOP_BROAD_UNCONDITIONAL / G2_MAINTAINED_MODEL_OPEN**, not an unconditional compression-oracle or BLAKE3 update-time lower bound. Imported LIT-123..126 (SODA 2018 dynamic strings; TCS 2026 FeST; normative C2SP BLAKE3 v1 spec; 2026 dynamic IPM) into the **126-work** source-index; historical UCT LIT-111..122 preserved. No Rust/G4 claim.

## UCT-001 — unified dynamic-information / distinguishability research (2026-10-08)

[UCT research program and four STOP/GO gates](UCT-001-PROGRAM.md) · [formal finite-state/observation baseline, self-contained Hamming-ball proof and triangle embedding counterexample](UCT-001-MODEL-AND-BASELINE.md) · [primary-source overlap and 12-work canonical LIT-111..122 import](UCT-001-PRIMARY-SOURCES.md), [issue #74](https://github.com/definitely-stable/Mathlab/issues/74). [2026 dynamic Boolean cell-probe Theorem 1.1/model-transfer audit](UCT-001-G1-2026-DYNAMIC-LOWER-BOUND-AUDIT.md). [Fixed-q TOM-006 generalization and exact small parse oracle](UCT-003-FIXED-Q-IMPOSSIBILITY.md) · Independent finite exhaustive oracle: `research/test_uct001_baseline.py`. **44-item known/STOP registry with UCT KR-041..044**; **DERIVED_CLASSICAL baseline; no original general theorem, no claim of source-proof verification, no Rust.**

## HYP-101 G0 — exact BLAKE3 multi-edit source barrier (2026-10-08)

[1994/1997 incremental cryptography primary-source audit, elementary one-shot lookup-table theorem and multi-edit model freeze](HYP-101-G0-INCREMENTAL-HASH-AUDIT.md), issue [#72](https://github.com/definitely-stable/Mathlab/issues/72). [Independent hash-agnostic test](../../research/test_hyp101_one_shot.py) uses SHA-256 solely as a standard-library deterministic digest comparator; no BLAKE3 implementation or cryptographic security is claimed. LIT-109/110 extend the unique bibliography from 108 to **110**. A one-shot Omega(n/1024) lower bound with free O(n)-bit preprocessing is disproved; exact BLAKE3 *multi-edit* complexity remains OPEN under a fully priced model.

## HYP-103 G0 — exact classical certificate reduction (2026-10-08)

[Complete old-root batch-overwrite probe model, proved minimum-hitting-set characterization, six source-level research constraints and stop decision](HYP-103-G0-CERTIFICATE-REDUCTION.md), [issue #70](https://github.com/definitely-stable/Mathlab/issues/70). An independent [all-Boolean-functions finite oracle](../../research/test_hyp103_certificates.py) is included in GitHub-hosted research CI. The earlier batch-DAG headline **STOP_CLASSICAL_CERTIFICATE_REDUCTION**: certificate complexity already covers the minimum-probe objective. Six further missing primary works LIT-103..108 expand the catalog from 102 to **108**; no publication novelty, G4 or Rust is claimed.

## TOM-007 — six cross-domain strong-hypothesis gates (2026-10-08)

[Source/model review, exact finite falsifiers and strict stop decisions](TOM-007-SIX-HYPOTHESIS-AUDIT.md), [issue #68](https://github.com/definitely-stable/Mathlab/issues/68), [independent small-instance oracles](../../research/test_tom007_hypotheses.py). Catalog expanded **95 → 102** genuinely distinct primary works (LIT-096..102) and reverse links regenerated. Existing papers already indexed (Bender/Chonkers/Lefmann/Differential Execution) were cross-referenced, **not** reimported. HYP-102/104/106 broad novelty is blocked; HYP-101/103/105 remain narrowly-scoped, NOT theorem-eligible and NOT Rust/product GO.

## TOM-006 — short source-only patch-bound kill gate

[Scoped proofs, fixed-short-q adversarial counterexample, literature overlap and STOP/GO conditions](TOM-006-EARLY-KILL-GATE.md) (issue #63). Elementary positional missing-q-gram bounds are **PROVED_MODEL_BASELINE**, NOT novelty-cleared. Fixed q<=2 has an arbitrarily large cost-floor gap. No real codec/CPU benchmark or Rust authorization; do not replay DeltaMeter M6 without an early workload-specific product gate. [Independent exhaustive oracles](../../research/test_tom006_floor.py) are included in research CI unittest discovery.

## STOP / already known — required pre-research gate

[**Known, proved, stopped and nontransferable research**](KNOWN-AND-STOPPED-RESEARCH.md) · [machine source](KNOWN-AND-STOPPED-RESEARCH.json). 33 source-linked records with scoped dispositions and strict reopening conditions. This **does not** establish an exhaustive global prior-art search, nor does STOP in one workload ban valid different assumptions. Validate with `python research/known_registry.py --check`.


## Seven cross-domain theorem proofs — TOM-005

[Proven A-G baseline theorems with exact assumptions, counterexamples and source matrix](TOM-005-SEVEN-THEOREM-AUDIT.md) · [independent finite regressions](../../research/test_tom005_models.py). Seven proofs are classical rather than novel results; no Rust authorization. The anti-rediscovery catalog is extended from 33 to **40** known/STOP/conditional items.

## Four-stage cross-project theorem/prior-art audit (THEOREM-GAP-004)

[Theorem-level transfer and source audit](THEOREM-GAP-004-FOUR-STAGE-AUDIT.md) · [machine-readable source-to-claim matrix](THEOREM-GAP-004-TRANSFER.json). Lefmann (2005) achieves the same *odd-field construction exponents* as HYP-001 and HYP-002 under a stronger four-wise independence condition; Mathlab ASET upper bounds are separate. DeltaMeter/DELSK recommendations preserve existing system STOP and unknown product headroom. This is an audit, not a new theorem.

## Supplemental 2026 breadth: 26 STOC/ICALP/EuroSys works beyond sketch

[RESEARCH-LITERATURE-003B: 26 complementary 2026 papers](RESEARCH-LITERATURE-003B-2026-STOC-ICALP-EUROSYS.md) supplements the prior [20-paper 2026 selection](catalog/LITERATURE-003-2026-OPPORTUNITY-AUDIT.md), yielding **95 unique primary literature references** across **14 topical research lanes**, including graph dynamics, proof complexity/certification, algebra, text indexing, sampling, and compression. No current proof or product decision changed.

## Verified external scholarly literature

[Primary literature catalog](catalog/LITERATURE.md) · [papers by research record](catalog/LITERATURE-BY-RESEARCH.md) · [source/model audit I](catalog/LITERATURE-001-AUDIT.md) · [source corrections and expansion II](catalog/LITERATURE-002-SOURCE-AUDIT.md) · [2026 nonsketch audit III](catalog/LITERATURE-003-2026-OPPORTUNITY-AUDIT.md) · [literature.json](catalog/literature.json).

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

## HYP-105 G5-E2-B3.2 — exact D_s coincident-cycle obstruction (2026-10-09)

[Theorem, finite results and next research gate](HYP-105-G5-E2-B3-B2-COINCIDENT-CYCLES.md) · [Python physical C6 join](../../research/hyp105_g5e2b3b2_coincident_cycles.py) · [independent oracle](../../research/test_hyp105_g5e2b3b2_coincident_cycles.py) · [issue #176](https://github.com/definitely-stable/Mathlab/issues/176). For EVERY fixed injective W(3,s) pair labeling R3>=**5643 D_s/51^6**; under uniform independent pair maps exact E[D_s]=60 M6 [(a)_6/(K)_6]^2. GF2 D=15/3/3; GF4 D=8481/8417/10602 in E2-A lex/reverse-line/coordinate-flag controls. Complete matching-C6 counting without C(N,6), NOT complete positive GF5 motif R3 upper, not a new ASET exponent. B3.2-B/B3.1-B pending.

## HYP-105 G5-E2-B3.3 — Hall-matched correlated label failure (2026-10-09)

[All-h restricted Omega(s^9) theorem](HYP-105-G5-E2-B3-B3-INCIDENCE-MATCHING-NOGO.md) · [finite exact verifier](../../research/hyp105_g5e2b3b3_incidence_nogo.py) · [independent GF2/GF4 tests](../../research/test_hyp105_g5e2b3b3_incidence_nogo.py) · [#176](https://github.com/definitely-stable/Mathlab/issues/176). Aligned map g(l)=f(pi(l)) with perfect incidence Hall matching pi forces D_s>=C6(f(P))=Omega(s^9), and R3>=5643 D_s/51^6=Omega(s^9). A **restricted method no-go only**; other correlated maps, ASET theorem and simultaneous risk targets remain open.

## HYP-105 G5-E2-B3.2-C — Plücker exterior geometry and nonaligned shifts (2026-10-09)

[All-h Plücker rank injection/nonalignment and finite controls](HYP-105-G5-E2-B3-C-PLUCKER-NONALIGNED.md) · [canonical bivectors, shift histograms, finite D_s](../../research/hyp105_g5e2b3c_plucker_shift.py) · [independent basis/Frobenius/brute oracles](../../research/test_hyp105_g5e2b3c_plucker_shift.py) · [#176](https://github.com/definitely-stable/Mathlab/issues/176). Proves Σ_t E_t=N and min_t E_t≤s+1, plus complete injectivity of classical Plücker exterior line ranks and physical pair rank map for all h; this exits only the restricted B3.3 incidence-perfect-aligned no-go. Explicit GF2/GF4 diagnostics DO NOT provide strict D_s/R3 upper or common R2. Classical Klein embedding source credited and no new ASET theorem.
