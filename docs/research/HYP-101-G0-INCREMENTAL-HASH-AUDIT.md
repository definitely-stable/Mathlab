# HYP-101 G0 — Incremental cryptography prior art and one-shot exact-digest barrier

Date: 2026-10-08. [Issue #72](https://github.com/definitely-stable/Mathlab/issues/72). Parent: [TOM-007 #68](https://github.com/definitely-stable/Mathlab/issues/68). Baseline: main `1a083fc89fbee8d994146b50e68e3582ce24d620`.

**Status: PRIOR_ART_BROAD + PROVED_ELEMENTARY_ONESHOT_COUNTERMODEL / MULTI_EDIT_THEOREM_OPEN.** No scientific novelty, actual BLAKE3 cryptanalytic conclusion, new Rust crate, or production change is claimed.

## The crucial distinction

1. **New incremental cryptographic hash** under a claimed collision-resistance assumption is a well-established research direction, not new: Bellare–Goldreich–Goldwasser CRYPTO 1994, and Bellare–Micciancio EUROCRYPT 1997 including MuHASH/AdHASH/LtHASH (see primary sources below).
2. **Exactly the standard BLAKE3-256 digest after arbitrary byte insertion/deletion** is a different contract. Replacing standard BLAKE3 by another incremental hash is *not* a solution of this contract. Official BLAKE3 specification fixes the tree/content/chunk structure; overwrite-only and insertion/edit-shift cases are not interchangeable.
3. The earlier candidate `T_update=Omega(n/1024)` for even one arbitrary insertion, given *O(n) additional preprocessed bits*, is **false as stated** if preprocessing cost and constants are not charged. It does not establish that there is an efficient or inefficient sequence-maintaining exact BLAKE3 data structure.

## Theorem G0-A: one-shot exact-output table (elementary countermodel)

Let `H:{0,1}^* -> {0,1}^h` be any deterministic fixed-output hashing function, including the real standard BLAKE3 truncated to h=256 bits. Let `B` be a fixed n-byte source, and let the permitted single update insert exactly one byte `c` from alphabet `Sigma` at any of the n+1 positions.

In preprocessing construct the table

    Table[i,c] = H(B[:i] || c || B[i:]), for 0<=i<=n and c in Sigma.

It has exactly `(|Sigma|*(n+1))` digests, using at most `h*|Sigma|*(n+1)` **digest payload bits** plus optional address/header overhead. After preprocessing, `Table[i,c]` equals the exact updated standard digest and needs zero online hash/compression calls (O(1) lookup in a direct-address representation).

**Proof.** Each allowable query is explicitly indexed by a pair (i,c) for which preprocessing evaluated precisely the corresponding modified message. Determinism makes the cached digest exactly equal to a fresh invocation. There are `|Sigma|(n+1)` such pairs. QED.

For fixed byte alphabet `|Sigma|=256` and h=256 the table stores `65536(n+1)` digest bits = `8192(n+1)` bytes plus metadata: **linear in n, but at a very large constant factor**. It can require superlinear preprocessing CPU/reads (e.g. naively `Theta(|Sigma|*n^2)` processed message bytes), and **cannot be reused directly as an up-to-date answer table for a second edit**. There is no contradiction with BLAKE3's fixed-block implementation; this is a one-shot exhaustive memoization countermodel, not a fast practical update algorithm.

**Consequent falsification.** The unconditional statement "all arbitrary single-byte insertions require Omega(n/1024) *new* BLAKE3 compression-oracle calls even if arbitrary O(n)-bit auxiliary preprocessing is free" is false in the above exact computational model. Do not infer any multi-edit lower bound from this fact.

## G0-B: meaningful strong theorem would require a much narrower contract

Freeze all of the following before a conjecture about update cost:
- Exact output must be the bytewise standardized BLAKE3-256 digest, not an alternative incremental hash with a different digest.
- Long, consecutive adaptive insert/delete/overwrite operations versus one-shot offline queries.
- Precise auxiliary-state budget **in bytes with constants**, total preprocessing/work to build the state, incremental maintenance and cache invalidations.
- Memory/register/cell-probe model and whether bytes, BLAKE3 compression invocations, SHA/CV parent calls, raw IO and allocations are charged; a compression-oracle abstraction must avoid falsely equating the ideal oracle to BLAKE3.
- Query adversary: oblivious/adaptive, update lengths and positions, retained versions, and whether a full digest is mandatory after every mutation.
- Explicit comparators: rehash from scratch, cached full BLAKE3 subtree CVs for in-place overwrite, precomputed alignment/offset caches, and a maintained dynamic-tree/rope implementation (the latter's digest is NOT automatically standard BLAKE3).
- External source-theorem audit before considering a genuinely new lower bound. A BLAKE3 paper's assertion about chunk-alignment costs is not itself an oracle lower-bound theorem.

## Primary-source audit and catalog

| Source | Directly established relevance | No invalid transfer |
| --- | --- | --- |
| [Bellare, Goldreich, Goldwasser, CRYPTO 1994](https://doi.org/10.1007/3-540-48658-5_22), **LIT-109**; [author record](https://www.wisdom.weizmann.ac.il/~oded/annot/node70.html) | Formal incremental hashing/signing as a cryptographic research problem already existed in 1994 | Does not construct an updater for the exact later standardized BLAKE3 digest. |
| [Bellare, Micciancio, EUROCRYPT 1997](https://doi.org/10.1007/3-540-69053-0_13), **LIT-110**; [author abstract](https://cseweb.ucsd.edu/~daniele/papers/IncHash.html) | Incremental collision-resistant constructions MuHASH, AdHASH and LtHASH | Different digest constructions and assumptions; cannot be substituted for exact BLAKE3. |
| [Official BLAKE3 specification](https://github.com/BLAKE3-team/BLAKE3-specs/blob/master/blake3.tex) | Fixed chunk size, tree structure, parent chaining values and implementation update semantics | Does not establish an unconditional cost lower bound against all auxiliary representations. |

Source levels: official publisher/author abstracts/bibliography and published algorithm descriptions, NOT independently checked entire paper proofs. No import of the normative BLAKE3 repository as an invented publication record.

## Reproducibility

`research/test_hyp101_one_shot.py` independently compares every tiny table entry against a direct re-hash using standard-library SHA-256 as a **stand-in deterministic digest**. The algebraic countermodel proof applies to *any deterministic H*, including actual BLAKE3, without importing a hash package. Test shows that table reuse for two consecutive mutations is invalid in general. This is **not** a test of BLAKE3 implementation, collision resistance, or a multi-edit lower bound.

## Decision

- HYP-101-BROAD "first incremental cryptographic hash": **STOP_PRIOR_ART**.
- HYP-101-ONESHOT `Omega(n/1024)` under free O(n)-bit preprocessing: **COUNTEREXAMPLE** in the frozen one-shot model.
- HYP-101-MAINTAINED exact BLAKE3 after repeated arbitrary byte edits: **SCOUT_ONLY / MODEL_OPEN**; a meaningful trade-off requires full state/preprocessing maintenance costs, exact hash semantics, and independent proof-level source audit.
- No Rust, G4 novelty, library announcement or change in other repositories. Only research index and source catalog updates authorized.
