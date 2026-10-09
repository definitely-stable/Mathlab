# UCT-005 G3-B2-C2-B1 — Authenticated PIN journal and generation-fenced GC

**10 October 2026.** [Research #178](https://github.com/definitely-stable/Mathlab/issues/178), foundational [#105](https://github.com/definitely-stable/Mathlab/issues/105); predecessor [C2-A disk collector](UCT-005-G3-B2-C2-A-DISK-WORKSPACE-GC.md).

**Classification:** `FROZEN_ACTOR_IDEAL_BARRIER_PIN_JOURNAL_AND_GC_GENERATION` / `EXPLICIT_CRASH_PREFIX_ORACLE` / `NO_REAL_POWER_LOSS_PROOF` / `NOT_BOUNDED_WORKSPACE_END_TO_END` / `NO_NEW_LOWER_BOUND` / `UCT_ROOT_OPEN`.

## 1. The concrete retention race we fix

C2-A's old-version PIN/UNPIN updates are independent full-page file writes. During a loss of power, the file may contain a partially updated PIN slot, or a server may claim a stale set of pins. Reconstructing reachability from such a slot without a trusted acknowledgment order can reclaim data still owed to a previously acknowledged offline reader.

C2-B1 therefore distinguishes a **committed, authenticated retention history** from merely written file images and serializes PIN/UNPIN and GC publication through separate ideal trusted control operations.

* `PinJournal` emits one fixed-size, HMAC-SHA256 authenticated full-page event per PIN/UNPIN, chained by the preceding record's MAC; events include sequence number, operation, client slot, authenticated epoch and root digest. `PinFence(seq, tag)` is a **separately paid trusted monotone tip**, not untrusted file content. Replay verifies every record, MAC, padding, sequence, parent tag and the tip; it fails closed on corruption, truncation, rollback or replay. The owner signing key must remain outside the untrusted store.
* PIN accepts a distinct already-authenticated historical `(epoch,digest)` checkpoint, and only for epochs still allowed by the last published GC; release requires an existing pin. The service currently serializes two fixed reader slots (general configurable count) and never infers current freshness from an old historical commitment.
* Record order is **write complete full image → os.fsync → ideal trusted monotone compare-and-swap (publish fence) → acknowledge**. Writes that lack the trusted publication are ignored on recovery, including writes already flushed. A lost acknowledgment after publication is distinguishable by rereading the trusted tip. Unknown failure-injection values are rejected *before* side effects; partial I/O is not treated as successful.
* For GC, construct a new **copy-on-write generation** consisting of a full page header and ceil(N/P) full-page live bitmap images. The header binds the generation number, current PIN fence sequence and full MAC, and the SHA256 digest of the complete live bitmap. After `fsync`, GC checks the PIN fence did not change, checks each still-pinned root's reachability, verifies the staged immutable bytes, and publishes a second independently trusted `GcFence(generation,pin_seq,digest)`.
* **Only after GC anchor publication** may logical TRIM invalidate pages in the local resident bitmap. Crash during the invalidation is retryable: replay latest authenticated generation before resuming logical TRIM; no fresh pin for a dropped historical epoch is allowed after commit. Intermediate untrusted generations never justify freeing pages.

[Reference protocol](../../research/uct005_g3b2c2b1_pin_generation.py) · [independent tests](../../research/test_uct005_g3b2c2b1_pin_generation.py).

## 2. Restricted failure safety statement

Let `Roots[e]` be an immutable, correct authenticated node-page reachability set for each epoch, `L` be the **published** PIN-event prefix, and `T(L)` the set of currently pinned epochs in that prefix. The publication actor is single-writer and serializes all trusted PIN and GC transitions. The per-generation bitmask contains only members of

`Roots[latest] ∪ ⋃_{e∈T(L)} Roots[e]`

that have not been invalidated by a prior committed generation. A candidate bitmap is staged and flushed before any new trusted GC anchor is published.

**Safety lemma (conditional):** Assuming (A1) immutable complete node images, (A2) roots and checkpoint attestations issued by an independent trusted authority, (A3) secret and binding HMAC key with SHA-256 collision resistance, (A4) an atomic, monotonic and independently durable trusted PIN/GC publication order, (A5) an idealized `fsync` barrier making complete image writes persistent before publication, (A6) a serialized actor excluding simultaneous unmediated PIN/UNPIN or SET, and (A7) no torn/tampered committed images accepted by replay, a GC cannot logically reclaim a page reachable from any successfully published PIN or from the latest authoritative root.

**Proof outline:** Authentication and sequence checks make the published PIN prefix unique under A2–A4. Every retained epoch is present in its replayed prefix. Publishing GC with a different PIN fence is rejected. The staged bitmap is derived from the union of latest/pinned roots and explicitly checked for retained-root inclusion immediately before publishing its independent anchor. No reclamation occurs before this anchor, and recovery validates this published immutable bitmask and the referenced journal prefix before proceeding. Post-publication PIN excludes unretained historical roots, so no later accepted PIN can require an already reclaimed page. The lemma proves preservation for this *frozen ideal actor model*, **not** filesystem durability or an original lower bound.

The trusted roots, trusted PIN tip and trusted GC anchor are supplied **outside the untrusted store**. Both monotone CAS order and synchronization are modeled, not constructed. This is why the implementation can test ordering and invariants but cannot establish practical crash safety on an SSD merely by invoking `os.fsync` in Python.

## 3. Reproducible crash and adversary matrix

The independent unit tests enumerate journal cuts at `WRITE / FLUSH / PUBLISH / ACK` for PIN and UNPIN; GC cuts at `STAGE_WRITE / STAGE_FLUSH / PREPUBLISH / POSTPUBLISH / PARTIAL_TRIM`. A crash preserves only idealized flushed complete file-page prefixes; published fences survive independently. On restart, replay truncates uncommitted tails and rejects missing, forged or replayed committed prefixes rather than silently disregarding acknowledged retention. Tests also cover two offline historical readers, forged root credentials, HMAC-key substitution, journal-record replay, torn committed pages, stale staged generations invalidated by a new PIN, GC bitmap tampering before and after anchor publication, idempotent logical trim, and cross-checks against reachability independently extracted from C2-A's disk-node DAG for small n. Invalid cut names must have zero publication and zero file-write side effects.

Exact I/O counters report fixed page image reads/writes, explicit `fsync` calls, HMAC/SHA256 calls, trusted PIN publications (40-byte logical checkpoint) and GC publications (48-byte logical checkpoint), **separate file `truncate` calls during recovery**, and logical TRIM commands. `truncate` calls are charged as operations, **not** as a known device-byte movement cost; their filesystem metadata and garbage-collection costs are still unmeasured. These are **logical program operations**; actual SSD page writes, FTL amplification, directory-fsync ordering, network retries, registration messages, metadata wear, compaction and transaction coordination are **unmeasured**. The conceptual trusted-anchor transport frame is not an actual wire protocol.

## 4. Important remaining gaps (not silently promoted)

**No end-to-end bounded-RAM GC here.** The `GenerationalGC` oracle is a Python dictionary of all epoch reachability sets and constructs an in-RAM bitmap. This is a deliberate *control-plane model*, distinct from C2-A's separately proved **six-page-buffer collector**. Joining both without free server RAM, retaining authentication and recomputing a complete generation under I/O accounting remains future work. The source B2-B SET writer and reference RANGE_PARITY verifier are also still in-memory or O(n).

**Not actual crash durability.** Temporary files + `os.fsync` and a simulated `durable_pages` prefix cannot model torn sectors, drive flush caches, file naming/rename, directory metadata, open-file descriptors lost after process restart, power-loss order anomalies, malicious rollback of both journals, independent atomic service availability or time-of-check-to-time-of-use races across unsynchronized actors. A real protocol must add explicit failure domains, persistent named files, checkpoint stores, CAS/lease and replay idempotency semantics. Tests of *injected* crashes are only evidence in the ideal-barrier model.

**No general Byzantine proof.** HMAC-SHA256 and root hashing are conditional cryptographic assumptions; no security reduction or measured computational advantage is given. The signed author and the monotone CAS are trusted. Byzantine readers/owners, stale authority responses and network forks require a separate threat model.

**No hard-query lower bound.** The all-ranges page-write × page-read inequality was already falsified by C1. C2-B1 adds a restricted upper protocol/operational invariant, **not** a strict gap over applicable dynamic partial-sums or memory-checker lower bounds. Prior source hypotheses remain untransferred: [Fredman–Saks LIT-111](https://doi.org/10.1145/73007.73040), [Pătraşcu–Demaine LIT-112](https://doi.org/10.1137/S0097539705447256), [Boyle–Komargodski–Vafa LIT-157](https://doi.org/10.1145/3618260.3649686). Do not claim these theorems automatically transfer to a binary SET/RANGE_PARITY service with an independent trusted latest-root bulletin.

## 5. Exact next gate: C2-B2

1. Merge the C2-A disk-backed mark traversal **with** B1 trusted epoch-prefix snapshots using page-buffered, independently authenticated root/pin records, without an all-epochs Python set or unpriced retention-memory oracle; quantify per-generation I/O, pin message, bitmap initialization and hash/verify costs.
2. Add true online author SET and durable root publication protocol. Enumerate crash prefixes for SET→new-root publication, pin publication and mark→sweep, including reader vs writer races and old-root retention.
3. State a falsifiable worst-case or hard-distribution `F_n(R) ≥ g(n)` with matching resource dimensions and explicit valid reduction to prior literature, otherwise mark the proposed service `STOP_NOVELTY`. The overall UCT root remains `OPEN_UNPROVED`.

Neither Rust/product implementation nor claims of real filesystem crash durability are authorized by B1.
