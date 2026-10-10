# UCT-005 G3-B2-D1-B0 — F1 authenticated two-reader temporal service: cost and trust freeze

**2026-10-10.** Parent [#223](https://github.com/definitely-stable/Mathlab/issues/223), root [#105](https://github.com/definitely-stable/Mathlab/issues/105); predecessor [D1-A](UCT-005-G3-B2-D1A-ONE-PROBE-AND-CAUSAL-FALSIFICATION.md). Authoritative, machine-checked resource contract: [F1-MODEL.json](UCT-005-G3-B2-D1B0-F1-MODEL.json). Finite adversarial snapshot comparator: [reference](../../research/uct005_d1b0_f1_reference.py); [independent tests](../../research/test_uct005_d1b0_f1_reference.py).

**Status:** F1_MODEL_FROZEN / FINITE_CLASSICAL_UPPER / NO_NONFACTORIZING_LOWER_BOUND / SOURCE_FULL_TEXT_TRANSFER_PENDING / ROOT_OPEN_UNPROVED. Neither an original theorem nor a real-file durability claim.

## 1. Exactly one task, three security claims that must not be conflated

An honest *sequential* author maintains a logical word `x in {0,1}^n`. Each authorized `SET(i,b)`, including an unchanged bit, creates a fresh integer epoch `e+1` with a separately authenticated commitment to that epoch's entire logical state. A remote server is Byzantine. Two independent readers have distinct authenticated persistent states and can go offline.

1. `LATEST RANGE_PARITY([l,r))` must use a separately trusted, paid, globally monotone `(epoch,root)` anchor read at its **linearization point**; return XOR with respect to that observed root or safely `ABORT`. A writer publication **after** the anchor read is not part of this freshness claim. The server may indefinitely refuse service; no Byzantine availability guarantee.
2. `PIN_CURRENT(reader)` obtains the trusted current epoch/root and **atomically registers retention** with a trusted root/PIN authority that serializes PIN, UNPIN and GC decisions. A merely local unsignaled PIN does not protect against deletion. `AS_OF_PINNED(reader,e,[l,r))` may check against this particular reader's *previously trusted* root without a fresh LATEST anchor call. It may `ABORT` on server withholding or lawful deletion after UNPIN.
3. `UNPIN(reader,e)` authoritatively revokes only that reader's token. GC can reclaim a version iff it is neither latest nor pinned by **any** reader. Shared immutable DAG pages require reachability rather than a naïve per-epoch deletion criterion. A PIN racing the collector is an explicit synchronization obligation.

Canonical queries are **half-open** `0 <= l < r <= n`. Older code implementing an inclusive range `[l,r]` is adapted by `[l,r+1)`, without changing semantics or hiding any program/work charges. Failure to separate these conventions invalidates finite comparisons.

### Trust firewall

Trusted author, authentic bootstrap, correct locally stored reader roots, trusted monotone anchor and trusted serialized PIN authority are **assumptions**, not derived from untrusted snapshots. The trusted root alone is *not* an oracle for forgotten historical roots. PIN of arbitrary old epochs requires an independently authenticated historical retrieval channel, charged in full; this first slice implements `PIN_CURRENT` only. Readers have no free gossip, state-dependent tables or trusted replica unless included in `s`.

Correctness is conditional on collision/second-preimage binding, epoch/domain-separation and canonical encoding. `lambda=256` in finite SHA-256 tests is **not** a uniform asymptotic security argument; for family `n→∞` use explicitly varying `lambda(n)`, computational assumptions and error `epsilon(lambda)`. All authorization/key distribution, signatures and network overhead not simulated by the reference remain outstanding charges, not zero-price resources.

## 2. Resource vector and units

`R=(n,H,lambda,epsilon,P,s,S,U_r,U_w,U_delta,Q_r,B_pi,C_author,C_reader,G,V,A,T,M,GC_r,GC_w,GC_free,F)`.

Definitions are normative in [F1-MODEL.json](UCT-005-G3-B2-D1B0-F1-MODEL.json). In particular:

- `s` is total persistent trusted **bits** across the author, each of the two readers, anchor and PIN registry; account for retained historical roots and advice. A fully trusted n-bit author or reader replica is a legal comparator, not an implicit exception.
- `S` is peak **complete remote pages**, including data, roots, metadata, indexes, WAL and retention; `P` is bytes per page. `U_r/U_w/Q_r/GC_r/GC_w` are distinct **full page API operations**, not changed bits nor measured SSD transactions. Both `U_delta` and `U_w` must be exposed even for a no-op.
- `M` is PIN-reachable historic *remote pages* and must count page-sharing correctly; `GC_free` denotes logically reclaimed pages, not TRIM or SSD write amplification. Crash barriers `F`, copies, bitmap traversal, root publication and generation migration are not free.
- `B_pi` is remote proof/data **bytes**; `C_author` and `C_reader` separately include server/control-plane messages, catch-up and retries. `A` includes trusted root publication, retrieval, PIN-registration and revocation. `G/V` count prover/verifier operations and hashed **bytes**, not just hash invocations. `T` counts program bits and setup/preprocessing.
- For theorems, specify whether each budget is per operation worst-case, amortized over `H=poly(n)`, or an expectation under a **stated hard adaptive distribution**. Do not substitute an average for a worst-case statement.

The reference model counts complete logical snapshot images with one full manifest page per version, compact bit-packed payloads, root pub/read wire bytes and trusted PIN copies. It counts `GC_free` as logical page reclamation and `GC_r` as directory scan, **not** fsync, real storage compaction, measured SSD writes, CAS network round trips, or total Python RSS. It cannot by itself justify a physical page-I/O lower bound.

## 3. Upper-frontier baselines and anti-novelty counterconstructions

All candidate inequalities must survive these **same-task** points (with explicit pricing and/or failure declarations):

| Comparator | Fundamental resource escape | Present verification state |
| --- | --- | --- |
| Paid trusted replica + log | `s >= n` bits eliminates many per-query remote probes after charged catch-up | G3-B2-B classical upper; crash and root registry still conditional |
| Full independently anchored snapshots | `S,M,U_w,B_pi` can be linear, but `V,Q_r` easily implementable | D1-B0 finite oracle; complete page images counted |
| Merkle range aggregate tree | `O(log n)` update path, authenticated frontier proof at paid hash/proof cost | G3-B2-B upper; physical allocator/GC separate |
| DSST/path-copy persistent trees | History can be made immutable with copy-on-write nodes and nonconstant retained space | Canonical LIT-354, theorem transfer not audited |
| Authenticated WAL/LSM/generations | Delays materialization/compaction at cost of logs, catch-up and read amplification | G3-B2-C predecessors provide scoped upper and stale-GC controls |
| VC, Cauchyproofs, IVC/SNARK | May shrink evidence but increases preprocessing, witness updates or prover complexity | Conditional proposals only; no same-task priced reduction yet |

A hypothetical `U_w * Q_r >= n` is already false in the honest F0 logical bit-cell model by the D1-A Fenwick example; that does **not** refute F1. A hypothetical positive bound on every individual range fails on the full-range-parity-only case unless the query universe/hard distribution is fixed. Any H1+H2 lower bound must also survive paid trusted replicas and retained snapshots. Historic provenance is *not* automatically irreducible given these upper families.

## 4. Negative oracle and next proof gate

An ideal serialized authority stores a current 40-byte epoch/root and active PINs; the honest writer stores `n` charged trusted bits. Immutable remote full snapshots commit the epoch and packed word. Two readers PIN different epochs, rejoin, request both LATEST and AS_OF; tests corrupt bytes, replay older images, withhold/reclaim unpinned versions, perform no-op SET, and ensure an independently pinned epoch survives GC. The non-adversarial independent XOR answer is checked for all short words/updates/ranges. The reference includes a root prefix and epoch in the hash, so a repeated logical word at a different epoch has a different commitment.

**What has NOT been established:** SHA security under an unbounded adversary, real global consensus/anchor implementation, durable write barriers, physical SSD page movement, PIN-versus-GC distributed transaction correctness, any new asymptotic or lower bound, or complete prover/VC/IVC frontier. These are not repaired by a finite test.

**Next D1-B1:** inspect full primary theorem and proof hypotheses for canonical LIT-111/112/119/156–159/199–200/349–359, then issue a signed `APPLICABLE/REDUCTION_REQUIRED/NOT_APPLICABLE` transfer table for this *exact* F1 task. LIT-359 (Guruswami–Lyu–Yuan, [arXiv:2507.22265](https://arxiv.org/abs/2507.22265)) is static semi-random-CSP/cell-probe methodology, **not** a directly transferred authenticated dynamic range theorem. The bibliography corpus already contains the identifiers; do not duplicate them. D1-B2 should then enumerate same-task Pareto points, D1-B3 must state **one quantified falsifiable H1+H2 formula**, and D1-B4 must either prove a novel strict Pareto gap or record a scoped `STOP_NOVELTY`.

**UCT-005 root remains `OPEN_UNPROVED`.**


## 2026-10-10 D1-B0-F1-PAGE-001 byte conservation correction

**Issue #240.** Corrects an incorrect single-page manifest and implicit epoch-to-snapshot lookup in merged PR #235. Logical PIN/GC, the ideal anchor and UCT ROOT_OPEN_UNPROVED remain unchanged.

### Exact frozen reference layout

Each integer epoch e in [0,2^64) has one immutable, independently page-aligned sparse fixed-stride slot. Its public layout uses n logical bits and page size P bytes:
\[
B_d=\lceil n/8\rceil,\quad B_m=8_{\rm epoch}+8_{\rm length}+32_{\rm digest}=48\ \text{bytes},
\]
\[
P_d=\lceil B_d/P\rceil,\quad P_m=\lceil48/P\rceil,\quad
P_{\rm slot}=P_d+P_m,\quad {\rm first\_page}(e)=eP_{\rm slot}.
\]
Remote manifest wire grammar: big-endian uint64 epoch || big-endian uint64 payload length || 32-byte domain-separated SHA256 digest. This is a physically stored 48-byte manifest, **not** a free pointer to a digest; the 40-byte epoch+digest in the *separately trusted* linearizable anchor remains independently charged. Manifest and payload are separately page-aligned (rounding waste included).

All remote data/proof reads use the public arithmetic slot, verify manifest epoch, length and digest, and compare to the reader's trusted latest root or PIN. The Python dictionaries only simulate presence of physical pages in public fixed-stride slots: no unpriced dynamic remote lookup B-tree or epoch-to-object directory. Old slots are never relocated or reused in this restricted upper construction; reclaiming them leaves sparse address holes. Space measures *allocated live pages*, not largest virtual byte offset. The archive is an abstract page-image machine, not a real file, filesystem hole punch, mmap, NAND or crash-safe SSD claim.

Per snapshot update, charge P_slot full-page remote writes and P*P_slot padded upload bytes. Exact server query payload is 48 manifest bytes plus B_d image bytes, with an additional 8-byte epoch request. Charge P_slot full-page remote reads and 16+B_d verifier-hash input bytes. For GC, enumerate **every issued epoch**, including reclaimed sparse holes, and charge (e+1)*P_m manifest-region page fetch attempts; remote deletion/reclaim page ledger remains separate. Thus using a Python dictionary to simulate extant payloads does not confer a free epoch-directory oracle.

The separately trusted authoritative PIN registry stores 1-byte reader ID + 8-byte epoch + 32-byte digest = 41 bytes per active record, additionally to the 40-byte PIN kept by the independent reader. PIN/UNPIN persistence charges ceil(41/P) **trusted-authority** page writes, not remote S/U_w. Trusted state s counts writer's n bits, latest 40-byte root, every reader PIN root and each 41-byte registry record. Actual separate anchor, network authentication, retry framing, durable fsync and cryptographic security reductions remain unimplemented/assumed.

### Corrected finite witness

At n=33, P=2, a 5-byte packed payload uses 3 data pages; the 48-byte manifest uses 24 pages. Exact total is **27** remote pages per snapshot and **54** padded upload bytes, rather than the earlier incorrect 4 pages and 8 upload bytes. The independent regression covers P in {1,2,8,40,64}, n in {1,33,65}, no-op epoch binding, two independent PINs, latest and historical reads, GC holes, replay, manifest tampering and truncation. A full Research CI pass and exact-head focused workflow are prerequisites to acceptance.

Do not infer any original lower bound, cryptographic security proof, bounded-address-space optimality, OS fsync guarantee or real SSD physical write amplification from this byte-conserving reference comparator.
