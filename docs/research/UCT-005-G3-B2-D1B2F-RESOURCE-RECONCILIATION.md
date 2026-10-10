# UCT-005 D1-B2-F — same-history F1 resource-ledger reconciliation

**2026-10-10** · [Issue #262](https://github.com/definitely-stable/Mathlab/issues/262) · Parent [#223](https://github.com/definitely-stable/Mathlab/issues/223) · [D1-B2-A #243](https://github.com/definitely-stable/Mathlab/pull/243) · [D1-B2-B #248](https://github.com/definitely-stable/Mathlab/pull/248) · [D1-B2-B1 #258](https://github.com/definitely-stable/Mathlab/pull/258).

**Classification:** \`PARTIAL_COST_RECONCILIATION_NO_FULL_PARETO_NO_NOVEL_LOWER_BOUND\`.

**Root:** \`OPEN_UNPROVED\`. **Not** a new lower bound, **not** a filesystem benchmark, **not** a physical SSD durability cost measurement, and **not** a claim of complete F1 Pareto domination.

## 1. Problem and audit correction

Earlier B2-A compared a byte-conserving snapshot with two conditional logical comparators and correctly declined to rank any fully priced Pareto point. B2-B now provides a second authenticated, byte-record COW tree; B2-B1 further provides an explicitly page-backed *segmented* allocation bitmap. But no scientifically valid global Pareto ordering follows from its locally efficient bitmap-update coordinate. The COW and snapshot designs have unequal **trust composition** (writer n-bit replica vs trusted node/epoch highwater), **GC conventions**, **proof bytes**, **CAS/PIN communication framing**, and **crash-durability assumptions**. Merely reporting \`SET bitmap pages\` or even \`SET total page writes\` cannot close the theorem.

The implementation [\`uct005_d1b2f_resource_reconciliation.py\`](../../research/uct005_d1b2f_resource_reconciliation.py) freezes the observation workflow and maps explicitly paid counters to shared units. It maintains a **partial** cost record, plus independently traced provenance and reasons for each missing coordinate. No unknown is zero-filled.

## 2. Frozen workload

- Same binary initial word of length \`1 <= n <= 2048\`, same \`P\` full-byte page size, same single honest writer and two independent readers, same ideal linearizable root/PIN authority assumption.
- \`PIN(reader=0,e=0)\`; \`SET(0,~bit0)\`; \`SET(min(1,n-1),same bit)\` with a **new no-op epoch 2**; \`PIN(reader=1,e=2)\`; \`SET(n-1,~latest)\` giving epoch 3.
- For each common half-open interval \`[l,r)\`: two mandatory \`LATEST\` reads, one independently authenticated \`AS_OF(e=0)\`, and one \`AS_OF(e=2)\`. Exact interval-parity answers must match separately retained GF(2) states, including n=1.
- Run GC retaining epochs {0,2,3}; UNPIN e0 and GC retaining {2,3}; UNPIN e2 and GC retaining {3}. The same protected history and operation count are verified in each comparator.
- \`representative\` query profile uses the existing B2-A interval set, so the legacy Tree and Replica+Log controls can independently check **the same representative interval answers**. Their legacy reader1 performs an additional catch-up query before PIN2; consequently the legacy **physical operation transcript is not identical** and their entire physical price vector is left `null`, with an explicitly distinct service label. \`all_intervals\` enumerates every interval and omits these legacy controls, which **were not run over that larger query set**.

Reference model meanings: S is the PAGE-001 full snapshot with a charged n-bit trusted writer copy. T0 is a byte-authenticated immutable COW tree with an allocation bitmap fully rewritten on each SET. T1 is the same COW tree with separate fixed-address, page-sized node-ID and epoch bitmap segments, rewritten once per touched segment on SET. R/T legacy controls remain *logical* and do **not** magically become byte-conserving just because they share logical answers.

## 3. Comparable coordinates and explicitly unknown costs

The shared \`PRICE_AXES\` are inherited from accepted D1-B2-A. Only source-accounted and unit-consistent axes are populated: \`peak_remote_pages\`, \`set_remote_page_writes\`, \`query_remote_page_reads\`, \`proof_payload_bytes\` (remote response payload, excluding network framing), \`gc_remote_reads\` (model-specific charged scans), and \`author_upload_bytes\` (SET padded payloads).

Even these numbers **do not establish full cross-model Pareto**; interpretation requires the source counter map, the same \`P\` and workload, and the admission that author/server I/O conventions differ. In particular, \`gc_remote_reads\` reflects each model's *recorded* GC scan cost, not a cryptographically uniform GC correctness protocol.

The remaining axes are **always \`null\`** rather than fabricated zero:

| Axis | Missing proof or accounting |
|---|---|
| \`trusted_bits\` | Declared reference-owned trust peak omits transient GC reachability and different writer setup |
| \`pinned_retained_pages\` | COW shares data across retained roots; a separately charged physical retained-history decomposition is missing |
| \`gc_remote_writes\` | Snapshot counts deleted manifests while COW counts rewritten allocation pages; logical free calls are not physical flash erase |
| \`anchor_bytes\` | Ideal linearizable central PIN+root publication/CAS wire and durability framing incomplete |
| \`prover_work\`, \`verifier_work\` | SHA byte inputs/CPU, proof traversal, historical lookups not measured to identical operation units |
| \`setup_bytes\` | Remote padded upload known, but author trusted setup, transient memory and authority anchoring not jointly priced |
| \`durability_barriers\` | Page-image reference has no verified fsync/crash consistency, transport proof or real SSD measurements |

Separately exposed **diagnostics** include \`peak_trusted_bits_declared\`, \`setup_remote_page_writes\`, \`set_remote_page_reads\`, \`gc_remote_page_writes_observed\`, \`gc_logical_pages_freed\`, \`authority_pin_page_writes\` and original raw ledger counters. The label \`gc_logical_pages_freed\` must not be translated to hardware TRIM without an independent physical implementation.

The existing strict dominance gate \`candidate_dominates(a,b)\` must return **\`None\` for every actual candidate pair**, because every model's status remains partial and critical axes are \`null\`. A favorable known-coordinate inequality is insufficient to change that decision.

## 4. Falsification before theoretical promotion

The independent [tests](../../research/test_uct005_d1b2f_resource_reconciliation.py) enumerate every initial word at n=1..5 and P=1/2/64, every half-open nonempty range, both readers and historical PINs, three GC runs, no-op epoch 2 and exact page-to-padded-upload conservation. Legacy R/T controls are run on the representative-profile case only; their cost vector is uniformly \`null\` because missing physical accounting cannot be transferred from another backend.

As an **illustrative bounded comparator**, \`n=257,P=1\` yields lower SET write pages for segmented COW versus global-bitmap COW, but the 122-byte node records still make segmented COW more expensive than a full packed snapshot for that coordinate. Conversely B2-B1's separate symbolic \`n=2^20,P=4096\` model bounds total remote COW SET page writes by 25 vs 33 for snapshot. That is a *single-coordinate* best-case bound; it omits query latency and proof, PIN communication, authority setup and GC. Both witnesses are deliberate stops against universal non-conditional Pareto statements.

## 5. Next mathematical gate

Before any new H1+H2 lower bound or complete Pareto theorem, the program must reconcile:
(1) the full byte grammar of central anchor/PIN authority transactions and crash-safe root publication; (2) COW shared physical PIN retention, issue-slot scan cost, GC peak working memory and durable page reuse/deletion; (3) CPU and exact prover/verifier proof-network cost under one adversary and client trust model; (4) complete Replica+Log page/GC extension or a formal exclusion from the comparison; and (5) source-level prior-art theorem hypothesis audit.

**STOP:** This is an evidence-backed *partial* upper-comparator corpus. UCT-005 root remains **OPEN_UNPROVED**.
