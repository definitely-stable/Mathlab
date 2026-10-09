# UCT-005 G3-B2-C1 — latest-only versus pinned-AS_OF retention, charged GC, and candidate rejection

**9 October 2026.** Parent [#178](https://github.com/definitely-stable/Mathlab/issues/178), [UCT root #105](https://github.com/definitely-stable/Mathlab/issues/105), baseline [G3-B2-B](UCT-005-G3-B2-B-UPPER-FRONTIER.md), physical [G3-B2-C0](UCT-005-G3-B2-C0-PAGE-IMAGE-FRONTIER.md).

**Decision:** RESTRICTED_EXACT_GC_REACHABILITY_AND_COST / CONDITIONAL_LATEST_VS_AS_OF_SAFETY / ONE_QUANTIFIED_FALSE_CANDIDATE / PRIOR_ART_TRANSFER_GATE / NO_NEW_LOWER_BOUND / PHYSICAL_SYSTEM_MODEL_INCOMPLETE / ROOT_OPEN.

## 1. Why C0 did not establish a durable physical frontier

C0 counts copy-on-write pages for every update but retains all historical roots indefinitely. Therefore its space versus update claims exclude reclamation, offline-reader retention and liveness under root deletion. A complete theorem about costs must count **retention and GC**, and distinguish one *latest* query from historical *as-of* access. G3-B2-B's latest verifier checks the externally trusted **current** root, not whether the server retained every old version.

We freeze exactly the previous single-honest-author binary SET(i,b) and inclusive RANGE_PARITY(a,b). Every SET advances epoch, including no-ops. Multiple independently offline readers obtain current (epoch,32B commitment) from a separately trusted atomic monotone anchor (1B request / 40B response), or abort if anchor unavailable. The untrusted store may withhold and tamper. This remains the F1 **conditional trusted-author/anchor/hash** setting, NOT a real cryptographic reduction. Every author root publication is charged 40B. The bounded server page cache has 1 physical page by default and is *not* the client's 40-byte checkpoint.

## 2. Precisely separate two contracts

**LATEST:** client may hold an older durable 40-byte checkpoint, and on reconnection asks only for the newest range aggregate at the independently anchored latest epoch. Under the B2-B verifier with an honest anchor, it can jump directly to the current authenticated root without retaining the old version's page images: the reader's own checkpoint is used for monotonic anti-rollback, not as a remote storage pin. A server can always deny availability, so this does **not** guarantee progress against a Byzantine withholding adversary.

**AS_OF:** to query a historical epoch e, a reader must already possess an independently authenticated historical (e,digest) token and expressly register a retention pin BEFORE that version is swept. The service contract includes retention metadata and must charge publication/pin/renew/release transport and persistence in a real implementation. Current C1 pins are trusted scheduler inputs and their delivery/persistence are **not implemented**, so historical safety is conditional. AS_OF verification uses the *historical* previously obtained token; falsely presenting it as a currently trusted latest root would break the threat model. Expired/unpinned AS_OF queries are rejected rather than silently substituted with the newest epoch.

These are not interchangeable: retaining many AS_OF versions is more expensive than supporting only LATEST, and a universal cost lower bound that fails to quantify which contract it covers is ill-typed.

## 3. Frozen page and collection model

Code: [mark/sweep and falsifiers](../../research/uct005_g3b2c1_gc_frontier.py) · [independent reference tests](../../research/test_uct005_g3b2c1_gc_frontier.py).

The physical addresses of 4-KiB images are exactly those emitted by the C0 immutable authenticated tree. Every path update allocates new packed data pages and one new root directory page; all old shared subtrees point to the same physical page IDs. The GC chooses the most recent root plus any authenticated historical epochs currently pinned, and traces all recursively reachable node images. It frees **only pages absent from the union** of these roots, not individual nodes within pages. There is no page compaction or relocation, so shared mixed pages can remain partially occupied indefinitely. An allocated image not reachable from any retained root has no future read in this fixed-version immutable execution graph.

All physical image bytes are charged at P=4096. Mark traversal reads each node's page using a cold LRU of one page. The logical free-space bitmap uses one bit per **allocated page address including holes** and occupies M=ceil(A/[8(P-header)]) full physical images, where A is the high-water allocation ID. Every collection charges M page-image reads and M page-image rewrites for that bitmap, plus mark traversal page faults; the number of released pages is counted as individual TRIM/UNMAP **logical commands**, and reclaimed storage capacity is recorded separately (freed pages × P). TRIM is NOT a physical erase guarantee and has **zero charged payload bytes but nonzero command count** in this model.

**Important incompleteness:** the executable simulator uses a Python set to materialize page reachability, a stand-in for a disk bitmap. The bitmap I/O prices are declared and charged, but an actual bounded-RAM incremental marking algorithm, its metadata allocation/init/update traffic, page-by-page marking spills, parallel mutation fences, pin persistence, and GC crash recovery remain open. Only the server *page cache* is bounded here; no claim is made that the reference Python process has bounded total RAM. A complete physical-I/O lower-bound model MUST close this gap first. The 40-byte trusted checkpoint does not include the trusted pin scheduling service.

## 4. Elementary exact safety lemma — model-scoped, classical

Let P be the set of all page IDs allocated by the C0 ledger, let R_e be the set of images reachable by the authentic immutable root for epoch e, including its epoch-directory page, and let E be {latest} union active authenticated AS_OF pins. Define K = union of R_e for all e in E and G = P_resident minus K. A stop-the-world mark/sweep which atomically removes exactly G satisfies:

1. Every page used by any retained authorized LATEST or pinned-AS_OF proof remains resident, because all its traversed page IDs belong to one R_e subset of K.
2. No reclaimed page can be required by these proofs, by definition of set difference.
3. Page-ID reuse is forbidden: no freed page may be overwritten under an old immutable authenticated pointer. The high-water page ID increases on subsequent SETs.
4. Collection recovers exactly |G| × P *logical page-image capacity* and pays a mark traversal, bitmap metadata I/O and |G| TRIM commands; returned capacity is not a negative disk-write byte count.

**Proof:** set inclusion for (1)–(2); the allocator is monotone for (3); the counters implement exactly the chosen frozen image/bitmap accounting for (4). This is a classical reachability/garbage-collection invariant, NOT an original joint read/write lower bound. The tests independently construct reachable page sets from the B2-B node graph rather than invoking the GC implementation's graph traversal.

The proof presumes no concurrent publication or pin changes while marking/sweeping. A stale expected epoch is rejected; a real protocol additionally requires durable pin registration, an atomic free bitmap swap, and crash recovery before any physical TRIM. The C0 ordered WRITE_DATA → FLUSH_DATA → WRITE_DIRECTORY → FLUSH_DIRECTORY → PUBLISH_ANCHOR → ACK_COMMIT condition remains required for new roots. It is not an SSD/fsync guarantee.

## 5. Concrete candidate H_C1 that FAILS

Test an explicit (deliberately too strong) joint conjecture:


\[
H_{\mathrm{C1}}:\quad
\forall n=2^h\ge 4096,\ \forall\ \mathrm{F1\ schemes}\ (s\le 40\ \mathrm B),\
\forall\ 0\le a\le b<n:\quad
U_{\mathrm{page\,writes}}(n)\,Q_{\mathrm{page\,reads}}(n,a,b)\ge h.
\]

All 40-byte roots must be independently anchored, page size fixed at 4096B and F1 trust assumptions held. For the existing T tree with n=4096, any binary SET copies k=13 nodes into one packed new data page plus one directory page: U=2. The full-range query a=0,b=n-1 needs only the root node page and directory: Q=2 under the one-page cold LRU. Therefore U×Q=4, while h=12. It violates H_C1. This counterexample has 40B client checkpoint and 4096B server page cache. No asymptotic result is proved merely by enumerating this witness. In fact for all n=2^h with 12<=h<=24, k=h+1<=25, so U=2 and full-range Q=2; H_C1 fails for every such h>4 under C0's fixed record assumptions.

**Critical quantifier correction:** this does NOT reject a bound on **max over queries** or on adversarial average over a prescribed hard range distribution. The full-range parity is a *single easy query*. The existing point is not a counterexample to Fredman–Saks / Pătraşcu–Demaine, which address worst-case/amortized families of dynamic partial sums with specified word size and δ updates. Moreover, SET versus increment/flip, changing update information, security assumptions, and trusted F1 anchor oracle all require explicit reduction charges.

Other unsafe ideas already falsified in C0: W_pages >= number of logical changed nodes; every query must touch Ω(log n) pages; a fully current trusted n-bit replica requires an untrusted data read for each query. New C1 rejects a **zero-charge GC** policy because sweeping an unbounded version log must at least account for its own metadata operations in this frozen policy; this is NOT a theorem requiring every possible GC algorithm to perform those exact operations.

## 6. Closest primary-source theorem barriers (existing canonical LIT IDs)

| Identity | Verified primary source | Why C1 cannot simply adopt it |
| --- | --- | --- |
| LIT-111 Fredman–Saks, STOC 1989 | [ACM DOI 10.1145/73007.73040](https://doi.org/10.1145/73007.73040) | Dynamic partial sums; quantifiers, word size and update operation model must match; a cheap full-range query does not contradict hard prefix queries |
| LIT-112 Pătraşcu–Demaine, SICOMP 2006 | [Publisher DOI 10.1137/S0097539705447256](https://doi.org/10.1137/S0097539705447256) | Published amortized randomized and external-memory lower bounds plus tradeoffs for partial sums, under exact δ/b hypotheses; the δ=1 binary case is NOT automatically δ=Ω(b); no free transfer of an Ω(log n) statement to F1 with a trusted root oracle |
| LIT-157 Boyle–Komargodski–Vafa, STOC 2024 | [MIT original published-version abstract](https://dspace.mit.edu/entities/publication/540979d8-2b5e-4c4c-9fa4-a9cd71533bc4) | Computational memory checking with trusted local storage p, separate read/write costs and completeness/soundness. Arbitrary memory-checker Read(i)/Write(i) and arbitrary range parity are different service families; do not multiply independent lower bounds |

Full-text theorem hypotheses, proof techniques and input/state update transformations are **NOT** independently reverified in this slice; primary publisher/author abstracts and the canonical identities were verified. In particular, the Pătraşcu–Demaine δ=Ω(b) versus δ=o(b) split forbids claiming their strongest formula in the one-bit delta model without a careful source-level reading. No duplicate LIT entries introduced.

Other non-transferable comparators remain SUNDR/COP fork consistency, authenticated-state ADSC-SNARK (which does NOT furnish trusted independent freshness), existing UCT G3-A/B1 classical packing, and finite INDEX page-layout evidence. Never combine unrelated formulas as if their hypotheses held simultaneously.

## 7. Gate result and next research slice

**What C1 proves:** deterministic exact mark/sweep preservation and capacity recovery in one immutable page DAG with explicitly pinned historical checkpoints; priced bitmap/mark/trim upper protocol; finite (n=2..4) independent correctness oracles after GC; one explicit falsified multi-resource inequality; preservation of latest-only response despite old-client checkpoints. This is an actionable negative finding and a classical infrastructure improvement.

**What C1 does not prove:** novel general lower bound, complete bounded-RAM GC, true page writes including metadata creation, reliable PIN/UNPIN/expiry delivery, multi-writer support, recovery of torn/failed fsync writes, crypto soundness, SNARK costs, or unbounded-family novelty.

**C2 decision gate:** Either (A) complete the physical model with a real bounded-workspace mark-and-sweep algorithm, durable epoch pin/GC bitmap publication, crash and compaction probes, then formulate a new lower bound for a **hard query distribution** or max-query cost and verify full LIT-111/112/157 quantifier transfer; or (B) set STOP_NOVELTY for the present natural task and pivot UCT-005 to another genuinely nonfactorizing theorem candidate. Root #105 remains **OPEN_UNPROVED**, issue #178 remains OPEN until explicit accepted decision.

No production Rust or service API is authorized by this model.
