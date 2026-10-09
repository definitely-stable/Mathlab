# HYP-101 G1 — Phase/counter reuse frontier for *exact* standard BLAKE3

Date: 2026-10-09 · [HYP-101 issue #72](https://github.com/definitely-stable/Mathlab/issues/72).
Source main: `45f7ff750e25d67d08a56713462cc8abc9f8cf33`. This is a **model-scoped source audit + elementary cache-counterexample**, NOT a general time/space lower bound, hash-security claim, optimized implementation, or new theorem.
Prior record: [HYP-101-G0](HYP-101-G0-INCREMENTAL-HASH-AUDIT.md), [UCT program](UCT-001-PROGRAM.md), [Mathlab anti-rediscovery registry](KNOWN-AND-STOPPED-RESEARCH.md).

## Key primary-source facts, verified at specification/source level

The [C2SP BLAKE3 v1.0.0 normative specification](https://c2sp.org/BLAKE3@v1.0.0) splits messages into **1024-byte chunks** and 64-byte compression blocks. Every compression block in a leaf receives **the chunk's zero-based index** as its 64-bit counter (C2SP §4.2). Parent compression always uses counter 0, distinct PARENT and possibly ROOT flags (§4.3). The canonical digest is **not** the root of an arbitrary locally balanced rope: BLAKE3 prescribes the layout and flags of the root.

The [original BLAKE3 research specification](https://github.com/BLAKE3-team/BLAKE3-specs/blob/master/blake3.tex), §6.5, already explicitly states that in-place overwrite can update leaf paths but insertion/deletion in the middle can force suffix recomputation. Therefore **'BLAKE3 byte insertions may invalidate suffix chunks' is published prior art**.

**Critical correction:** "insertion necessarily changes *every* suffix CV" is FALSE even in the canonical model for highly periodic inputs. An `a` insertion into `a^n` produces `a^(n+1)` independently of insertion position; any correct algorithm may exploit canonical target equality. Additionally repeated blocks can have the same position-and-payload canonical leaf *input* after an edit.

## Frozen structural-CV-cache model

This audit counts only whether a cached **canonical leaf computation may be reused without changing its compression input**; no cryptographic collision assumption is needed. Let `b=1024` (toy tests may use b=2,3,4). For a byte string S define

    key_i(S) := (i, S[i*b : min((i+1)*b, |S|)]),

where i runs over all nonempty canonical chunks. For the exactly empty message BLAKE3 has an exceptional empty root chunk that is deliberately OUTSIDE this toy definition. The key records index *and the exact bytes*, and is sufficient to identify the corresponding **leaf input parameters** for a non-root chunk: chunk counter, fixed length/CHUNK_START/CHUNK_END pattern and byte blocks under a fixed hash mode/key. **For a single-chunk message, BLAKE3 uses a distinct ROOT-flagged final compression, so these signatures by themselves do NOT imply full root-output reuse.** Our cache equivalence represents separately available non-ROOT leaf CVs when there are at least two chunks; small-length test cases below check signature equality only and do not assert a valid BLAKE3 root reuse.

Let `K(S)` be the set of all canonical leaf keys of S. If the cache holds only full canonical leaf results from a previous S, the **number of new leaf-input keys** for a new T is

    miss_b(S,T) = | K(T) \ K(S) |.

This is an exact identity for *canonical leaf-input-key misses*, not a lower bound on all possible hash algorithms; arbitrary precomputed other keys, internal-state caches, direct final digest tables, cryptanalytic shortcuts and alternative representations are excluded. If the only cached results are keyed by `key_i(S)`, a missing canonical input must be recomputed to obtain its leaf CV (or provided by a separate method, outside this cache model).

## G1-A: aligned whole-chunk insertion, exact restricted-cache count

Let S consist of m>=2 full length-b chunks `C_0,...,C_(m-1)`. Suppose `C_j != C_(j+1)` for all adjacent old chunks, and insert an entire new full chunk `X` at canonical boundary k (0<=k<=m), with `X != C_k` when k<m.

Then

    miss_b(S, S[:k*b] || X || S[k*b:]) = m-k+1.

**Proof:** The first k canonical input keys are unchanged. At index k, the new key holds X and is different from the old key at k (or is beyond its old domain when k=m). For every k<j<m, the new index-j chunk is C_(j-1), which differs from the old C_j by hypothesis, and the counter stays j; hence the old canonical leaf key at j cannot be reused. The final new index m has no old same-index key. There are exactly m-k+1 missing input keys. QED.

This is *not* an `Omega(m-k)` compression-query lower bound in an unrestricted RAM/oracle model. It is an exact statement for **strict previously-materialized canonical-leaf reuse**. The result follows immediately from position-dependent chunk inputs and is not claimed as scientifically new.

**Counterexample to an unconditional suffix-miss claim:** if all C_j = X = a^b, then inserting X at boundary k<m leaves every existing index-j full chunk payload identical, so the old m canonical keys all remain valid; only the newly appended index m lacks a cached input. Thus `miss_b=1`, even though the byte insertion occurred at the beginning. This also demonstrates why "bytes physically moved" and "canonical hash inputs changed" are not interchangeable.

## G1-B: offset insertion and two independent obstacles

For a non-b-aligned insertion the canonical leaf payloads may be reshuffled across the suffix. In addition to payload-phase change, `key_i` always includes the index. But **phase shift does not imply a high miss count for all messages**: periodic and repeated bytes can match old same-index inputs.

Even for b-aligned whole-chunk insertion, the content of old suffix chunks can remain intact while their new canonical indices differ. A content-only cache with signatures of the form `digest(chunk_payload)` cannot, by itself, substitute for the exact BLAKE3 leaf inputs because the compression *also includes the chunk counter*. It is **not** sound to accept such a substitute without recomputation or a proved transformation of the counter-dependent compression.

## G1-C: exact expected strict-cache misses under IID uniform bytes

A separate **average-case / source-distribution** statement is possible, without a cryptographic idealization.

Let S contain m>=2 full b-byte chunks, with each byte independently uniform over an alphabet of size q>=2. Fix any one-byte value c and insert it **at the start** of S. Then the new message has m full canonical chunks plus one final one-byte chunk. In the above position-indexed leaf-input cache model:

    E[miss_b(S, c || S)] = (m+1) - m*q^(-b).

Moreover, the probability that **all m existing full same-index leaf inputs are invalidated** is at least:

    Pr[miss_b(S,c||S)=m+1] >= max(0,1 - m*q^(-b)).

**Proof.** For index j=0, its new full b-byte chunk equals the old one iff all b original bytes equal c. This event has probability q^-b. For each 1<=j<m, the new full chunk is the b-byte window shifted backward by exactly one byte; equality with the old window iff the b+1 bytes spanning those adjacent windows are identical. Under IID uniform symbols, that has probability q^-b. The fresh final one-byte index j=m is always missing. Linearity of expectation therefore gives one mandatory miss plus m*(1-q^-b) expected misses. The probability at least one old full index remains a cache hit is at most m*q^-b by union bound; complement gives the stated inequality. Independence **between individual hit events is not assumed**. QED.

For standard b=1024, q=256, the per-position old-leaf hit probability is 256^-1024 under this *artificially uniform independent-byte distribution*. This quantifies why a strict old-leaf CV cache can be weak on high-entropy data; it is **not** a realistic workload assumption, not an unrestricted lower bound on compression calls, and not a theorem about BLAKE3 collision probabilities.

The result is elementary expectation + union bound, so **NOT scientific novelty**. Its utility is a falsification/calibration gate. Independent exhaustive enumeration of tiny finite alphabets in `research/test_hyp101_phase_counter.py` compares the exact rational expectation with this formula.

## G1-D: source-to-claim comparator matrix (new literature)

| Source | Actual established result | Cannot transfer as exact BLAKE3 theorem |
| --- | --- | --- |
| [Optimal Dynamic Strings, Gawrychowski et al., SODA 2018](https://doi.org/10.1137/1.9781611975031.99), new **LIT-123** | Randomized dynamic string split/concat and compare/LCP, O(log n) w.h.p. operations, matching logarithmic tradeoff in its own equality model | Equality and LCP certificates **do not provide exact standardized BLAKE3-256 digest** after every edit; do not call their `Omega(log n)` result our compression lower bound. |
| [A Textbook Solution for Dynamic Strings, Lipták–Masillo–Navarro, TCS 2026](https://doi.org/10.1016/j.tcs.2026.115746), new **LIT-124** | FeST enhanced splay trees, amortized logarithmic updates, probabilistically correct substring comparison and more transformations | Position-independent rolling/fingerprint representations do not automatically compute exact BLAKE3 compression with global chunk counters/ROOT flags. |
| [The BLAKE3 Hashing Framework, C2SP BLAKE3@v1.0.0](https://c2sp.org/BLAKE3@v1.0.0), new **LIT-125** **normative specification, not a research article** | Source-of-truth for BLAKE3 v1 tree, chunks, flags and index-dependent compression | Specification demonstrates structural behavior, **not** an algorithmic unrestricted lower bound or cryptographic collision resistance proof. |
| [Logarithmic-Time Internal Pattern Matching Queries in Compressed and Dynamic Texts, Duyster–Kociumaka, 2026](https://doi.org/10.1007/s00224-026-10266-x), new **LIT-126** | Dynamic/compressed string IPM, O(log n) queries on recompression RLSLP, including a proof-of-concept Rust implementation | This is a *different* query (pattern matches), different probabilistic guarantees, and not BLAKE3 digest compatibility. |
| [Incremental Cryptography, CRYPTO 1994](https://doi.org/10.1007/3-540-48658-5_22), existing LIT-109; [Incrementality at Reduced Cost, EUROCRYPT 1997](https://doi.org/10.1007/3-540-69053-0_13), existing LIT-110 | Existing incremental cryptographic hash construction schemes | Original MuHASH/AdHASH/LtHASH output != exact BLAKE3-256; no new incremental-hashing headline. |

These new sources supplement—not replace—the 12 UCT-001 imported works (LIT-111..122) and existing HYP-101 G0 LIT-109/110. The model-transfer result is based on the cited source definitions/theorem abstracts. It is **not a full literature completeness proof or independent re-verification of every cited theorem**.

## Hypothesis falsification and proper next step

The earlier broad candidate

    "Any arbitrary insertion requires Omega(number_of_suffix_chunks) fresh BLAKE3 calls"

is false for (1) precomputed one-shot digest tables (G0), (2) periodic target-equality witnesses even under canonical chunks, and (3) counting only strict leaf misses does not preclude algorithms using other state or precomputation.

**HYP-101 G2 is conditional:** only a *maintained, multi-edit* model requiring exact standardized digest after **every** operation, with explicit initial preprocessing P, total auxiliary bits S (including alignment/counter caches), internal compression-oracle queries Q, read/write work, and adaptive edit sequence may admit a new meaningful S–P–Q tradeoff. Distinguish S measured in bits vs bytes and do not confuse big-O with an economically feasible constant. Need a concrete lower-bound proof *in an oracle abstraction whose primitive inputs match the actual BLAKE3 tree*, or a matching faster construction and an audited source/model mismatch.

A valid G2 experiment first implements a **source-based canonical leaf-miss census** (not a hash accelerator), repeats inserts/deletes/substitutions with held-out periodic, adversarial distinct, and realistic files, then compares (a) standard full rehash; (b) cached canonical CV with overwrite fast path; (c) any alternative precomputed phase-counter caches, fully charging preprocessing. This step is a research feasibility comparator, not a Rust crate/product commitment.

**Decision at this gate:** `PROVED_CLASSICAL_CACHE_COUNT / STOP_BROAD_UNCONDITIONAL / G2_MAINTAINED_MODEL_OPEN`. Do not open a Rust implementation, do not call an `Omega(n)` unrestricted lower bound, and do not modify DELSK/DeltaMeter/ChunkShift.
