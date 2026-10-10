# UCT-005 D1-C2 — two-world freshness separation for offline immutable PIN and LATEST

2026-10-11 · [issue #311](https://github.com/definitely-stable/Mathlab/issues/311) · [D1-C #302](https://github.com/definitely-stable/Mathlab/issues/302) · [UCT root #105](https://github.com/definitely-stable/Mathlab/issues/105). Frozen F1 as specified in [D1-B0 model](UCT-005-G3-B2-D1B0-F1-MODEL.json); standalone [code](../../research/uct005_d1c2_pinned_freshness.py) and [independent adversarial tests](../../research/test_uct005_d1c2_pinned_freshness.py). **CLASSICAL_TWO_WORLD_LATEST_FRESHNESS_OBSTRUCTION / OLD_PIN_IMMUTABLE_UPPER / NO_ORIGINAL_NONFACTORIZING_LOWER / ROOT_OPEN_UNPROVED.**

## One service, two very different verification obligations

In F1 an honest serialized author issues `SET(i,b)` (including no-op creating an epoch), commits epoch and SHA digest to an ideal separately **paid** globally monotone anchor. Two independent readers may hold previously trusted per-reader PIN (epoch,root) tokens and offline history. A PIN is **atomically registered with trusted retention authority** so that honest GC cannot reclaim the epoch; the root alone has no retention authority. A Byzantine remote server can corrupt/omit/replay complete snapshot pages. F1 can ABORT on malicious withholding and does not guarantee Byzantine availability.

- `AS_OF_PINNED(reader,e,[l,r))`: authenticate **the immutable old epoch e** against the reader's already locally trusted PIN root (charged root storage, manifest/page proof transfer, verifier SHA and remote pages). It does not promise a current latest answer and therefore **needs no new LATEST anchor read** during the query.
- `LATEST_RANGE_PARITY(reader,[l,r))`: authenticate the version published at a fresh trusted-anchor linearization point. It must use a source of **new freshness** (F1 freezes the paid anchor read). A remote old digest, even if still fully SHA-valid for PIN e, cannot establish that epoch e remains latest after an unseen SET.

The public page-image comparator stores packed `ceil(n/8)` bytes per snapshot plus a separately aligned **48-byte epoch/length/digest manifest**. P-byte image counts are `S=ceil(ceil(n/8)/P)+ceil(48/P)`; every query reads S full remote pages and transmits 8-byte epoch address plus 48+ceil(n/8) bytes data/manifest. A PIN serializes a **41-byte trusted-authority registry record**, and client stores the separately paid old 40-byte (epoch,digest). A LATEST or PIN acquisition pays a trusted anchor request and 40-byte response, never a free shared clock.

## Restricted lemma D1-C2-T1 — classical two-world indistinguishability

Fix an initial x in {0,1}^n, known coordinate i and a reader with last authenticated PIN epoch e and root H(e,x). Consider:

- World W0: no SET since that PIN. Latest parity at [i,i+1) equals x_i.
- World W1: author committed `SET(i,1−x_i)` **before** a LATEST query; latest parity at the same singleton equals 1−x_i. Reader has no new trusted anchor/read/push/catch-up information.
- A replay-capable adversarial remote supplies **the same complete old epoch e, manifest and payload bytes** in W0 and W1. These are independently sound as **AS_OF** under the same pinned old root.

The reader state and untrusted remote transcript may be coupled identical, yet demanded LATEST answers differ. Therefore any deterministic protocol without ANY newer trusted freshness evidence that accepts the **same** LATEST answer in both worlds is incorrect in at least one world. Under a uniform random choice of worlds, a randomized common accepted output has conditional error at least 1/2. **ABORT is legal**, so this proves no guaranteed availability. One cannot infer that every real system needs exactly one HTTP request or one physical page: a *different, fully paid trusted freshness channel* could replace the F1 anchor. Within **this** frozen reference the authorizer calls anchor exactly once on each LATEST query, whereas AS_OF_PINNED invokes zero new anchor reads.

This is the classic fork/replay/indistinguishability observation, **not** an original joint space-update-query-history lower bound. For no-op SET the roots and epochs differ although the singleton parity remains the same; a no-op does not witness a different answer, so the hard two-world lemma correctly chooses a *flip* and tests no-op separately. An argument that root carries SHA-256 cryptographic binding indefinitely while lambda remains 256 as n→∞ is NOT made.

## Finite simulator and charged negative tests

[Oracle](../../research/uct005_d1c2_pinned_freshness.py) invokes the **accepted** `SnapshotF1Reference`. [Tests](../../research/test_uct005_d1c2_pinned_freshness.py) independently enumerate all 2^n words for n<=5, every coordinate i, P∈{1,2,64} for two-world attacks; for n<=4 they also enumerate every allowed SET(i,b) and ALL nonempty half-open intervals to assert old/new parities, exact anchor call differences, full remote pages, payload bytes, trusted registry writes, no-op roots and epoch semantics. Additional independent tests check two readers PINning the same old epoch, one-reader UNPIN not reclaiming the other's history, last UNPIN permitting exactly S old pages GC, GC directory scans separately paid, and withheld old pages causing AS_OF ABORT while LATEST still succeeds on current pages.

No Python dictionary key counts as unpriced server directory, and no byte of assumed trusted PIN/anchor state is deleted from the cost ledger. These reference tests do not certify real SHA cryptographic security, signed authority distribution, Byzantine liveness, physical SSD write amplification or crash/power-loss durability.

## Prior art and reason to STOP on this theorem

- Li–Krohn–Mazières–Shasha, *Secure Untrusted Data Repository (SUNDR)*, OSDI 2004, [USENIX](https://www.usenix.org/conference/osdi-04/secure-untrusted-data-repository-sundr). SUNDR uses **fork consistency** so that consistency violations can become detectable once clients see one another's updates; this is NOT the F1 separately trusted globally linearizable latest anchor. Our two-world argument is more elementary and cannot be claimed as a new general fork-consistency lower bound.
- Abusalah–Anthoine–Avitabile–Giunta, *Lower Bounding Update Frequency in Short Accumulators and Vector Commitments*, EUROCRYPT 2026, [publisher DOI](https://doi.org/10.1007/978-3-032-25330-9_7), [university primary abstract](https://openresearch.surrey.ac.uk/esploro/outputs/conferenceProceeding/Lower-Bounding-Update-Frequency-in-Short/991129195402346). This proves restrictions on **new/current additive accumulator and updatable VC membership proofs** at a constant-size digest; maintaining an OLD immutable PIN root/old proof across future updates is a different verification task. No assumption-preserving reduction to the latter is provided, and no full-paper theorem-by-theorem transfer has been completed.

**Decision:** `STOP_NOVELTY` for the restricted classical two-world freshness bound; `ACCEPT` as a precisely billed offline-historical-versus-online-freshness distinction. D1-C #302's strong fully priced *nonfactorizing* lower-bound question is **not** solved. No automatic formal replacement of SHA with VC. The next original hypothesis must explicitly couple freshness/retention/GC with simultaneous paid page, trusted state and adversarial proof-update costs for an infinite n family and survive these uppers/countermodels.

Organizing theorem-tree parent D1-C1 is an **input relationship**, not proof transfer. Research work is on a separate staged draft until #309 predecessor exact-head gates and merge, then clean main rebasing and D1-C2 exact-head focused + Research/INDEX/D1-A success. UCT-005 root **OPEN_UNPROVED**.
