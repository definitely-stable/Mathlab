# TOM-006 — early proof, prior-art and product kill gate

Date: 2026-10-08 · [issue #63](https://github.com/definitely-stable/Mathlab/issues/63).
Scope: Mathlab research only. No Rust crate, patch encoder, codec claim or other-repository changes.

## Disposition (do not overclaim)

- **PROVED_MODEL_BASELINE**: a positional absent-q-gram inequality, plus elementary block/packing variants, have direct deductive proofs below.
- **NOT_NOVELTY_CLEARED**: reference-only dictionary parsing, greedy phrase optimality and string-attractor/boundary covering predate this note. Their abstracts/definitions are checked, but no full theorem-level equivalence has been certified.
- **EARLY_NEGATIVE_WITNESS**: for every fixed short q-budget of {1,2}, the inequality can yield cost floor 2 while the exact minimum patch cost tends to infinity even after enforcing the source-length constraint.
- **PRODUCT_NOT_MEASURED / NO-GO_FOR_STANDALONE_q<=2**: no end-to-end speed or actual wire-byte benefit has been measured; **do not** conclude impossibility of other q, indexed workloads or new algorithms.
- **G4/RUST BLOCKED** pending definition-level novelty review and preregistered comparator performance on real workloads.

This study is deliberately smaller than the original TOM-006 A/B/C program. Its purpose is to avoid replaying DeltaMeter M6's multi-stage optimization before a plausible product win exists.

## Frozen model and cost

Let B,T be finite byte strings, n=|T|, m=|B|. A valid parse is a finite concatenation of **nonempty**:
- ADD(x), appending literal bytes x, for |x|>0; its bytes exactly match the corresponding target positions;
- COPY(offset,length), copying the contiguous B[offset:offset+length] with length>0, 0<=offset and offset+length<=m.

No RUN, copy from emitted target, compressor, cross-window shifts or VCDIFF-style context-sensitive address/size encoding. The target is produced exactly. Empty T uses the empty parse. Let L be the total ADD payload bytes, C the number of COPY instructions, A the number of maximal contiguous ADD regions (distinct from raw ADD instruction count), J the number of adjacent COPY|COPY boundaries. Set U_q(B,T) to the **number of target starting positions** i with T[i:i+q] absent as a contiguous substring of B, not the number of distinct missing q-gram values. q is a positive integer; for q>n, U_q=0.

For independent fixed-charge toy tests, let K(P)=L + (#ADD instructions) + 2C, in abstract byte units: each literal is charged 1, each nonempty ADD instruction has overhead 1, each COPY has overhead 2. These are **not** real VCDIFF wire bytes. A fixed header is excluded uniformly. No unpaid empty commands.

## Theorem A1 (model-scoped, positional)

For every q>=1 and valid parse:

    U_q(B,T) <= q L + (q-1) max(C-1,0).

**Proof.** Fix a target q-window absent from B. If it contains a literal ADD byte, charge it to one such byte. A given byte is contained in at most q target q-windows, hence at most qL windows can be charged this way (overcounting is allowed). Otherwise the window consists entirely of COPY-produced bytes. It cannot lie within a single COPY, because that would make it a substring of B. It therefore crosses a boundary between *adjacent* COPY instructions. For each boundary, at most q-1 windows cross it. There are at most max(C-1,0) such boundaries. Taking the union bound on counted windows proves the inequality. q=1 is included, and if q>n the left side is zero. Empty source/target are handled by the valid-parse definition. QED.

**Remark.** Do not call a generic absent substring/window boundary counting argument a new theorem.

## Theorem A2 (block-level strengthening, model-scoped)

With A maximal literal regions and J adjacent COPY|COPY boundaries:

    U_q(B,T) <= L + (q-1)(A+J).

**Proof.** An ADD region of length ell>0 intersects at most ell+q-1 target q-windows. Over all A regions, at most L+(q-1)A windows meet literals. Every remaining missing window must cross an adjacent COPY|COPY boundary, accounting for at most (q-1)J more. QED.

When L>0, A<=L; always J<=max(C-1,0). Thus A2 is no weaker than A1 for the same actual parse. No originality claimed.

## Theorem A3 (disjoint-window packing)

Let P_q be the maximum cardinality of a family of pairwise position-disjoint, absent target q-windows. Then:

    P_q(B,T) <= L+J.

**Proof.** Each selected absent window either contains a literal byte or crosses an adjacent COPY|COPY boundary. Disjoint target windows cannot share an interior byte or boundary point, so assign a distinct literal byte or COPY|COPY boundary to each selected window. QED.

## Safe toy lower-bound computation

For all q in 1..min(n,qmax), compute positional U_q. Enumerate nonnegative integers L,C satisfying:
- 0<=L<=n, C<=n-L (COPY instructions are nonempty);
- if C=0 then L=n; if C>0 then m>0;
- C*m >= n-L (each source COPY moves at most m bytes);
- A1 simultaneously for every selected q.

For each retained pair charge the optimistic cost L + [L>0] + 2C and take the minimum (zero for n=0). This is a **relaxation**: it need not describe any realizable parse, and [L>0] charges at most one ADD instruction even when multiple are necessary. It is therefore a *lower* bound on the exact minimum K*, never an upper bound. No production API and no actual wire-cost claim. q-gram index/scanning work is entirely excluded from K and **must be charged separately** in a product benchmark.

## Adversarial theorem: arbitrarily weak fixed {1,2} certificate

For m>=2 put B_m = a^m bb a^m and T_m=(ab)^m. Every 1-gram and 2-gram of T_m occurs in B_m. Thus U_1=U_2=0. Since |B_m|=2m+2 >= |T_m|=2m, the relaxation accepts L=0,C=1 and returns floor 2.

But the only 3-grams of T_m are aba and bab, neither present in B_m. Hence every COPY phrase in a valid parse has length at most 2. A COPY costs 2 and an ADD costs at least its literal payload, so K(P)>=|T_m|=2m. Conversely, m copies of the source substring ab generate T_m at cost exactly 2m. Thus **K*=2m, LB_{q<=2}=2**, with arbitrarily large absolute and multiplicative gaps. The source-length structural constraint does not repair this example.

This *falsifies useful tightness of this bounded-q relaxation on this family*; it does not refute A1 or prove a general fast-certificate impossibility. q=3 observes missing grams and changes the outcome.

## Pre-registered early product gate

Baseline competitors: direct exact source-only parsing (including a longest-match/relative-LZ-style baseline), a cheap full encode attempt, and a build/reuse-aware q-gram certificate. Measure actual output bytes, B/T reads, preprocessing and index updates, query CPU, retained memory, proof size, and trial count. Two separate cohorts: fresh B used once, and maintained B reused across many targets. Hold-out workloads (including periodic/repeated/adversarial strings) must be frozen before choosing q/index parameters.

**GO only if** no false reject under the exact model; source-specific certificate net CPU/bytes is better than a cheap reference on the frozen cohort after counting setup, and it avoids >=1 complete encode. Otherwise stop the standalone product track. No data currently satisfy this gate. In particular do not infer benefit from a fast Python micro-example or a math-only inequality.

## Direct primary-source overlap (not an originality certificate)

| Source | Verified overlap | Important non-equivalence / verification level |
| --- | --- | --- |
| [RFC 3284 (2002)](https://www.rfc-editor.org/rfc/rfc3284.html) | ADD/COPY/RUN and address/instruction compression | Source-only toy format is **not** general VCDIFF. RFC text/definitions inspected. |
| [Kuruppu–Puglisi–Zobel (SPIRE 2010)](https://doi.org/10.1007/978-3-642-16321-0_20) | Relative Lempel–Ziv parses against a reference | Reference compression predates TOM-006; source metadata/abstract inspected, not full proof transfer. |
| [Crochemore–Langiu–Mignosi (TCS 2014)](https://doi.org/10.1016/j.tcs.2014.01.013) | Greedy phrase-count optimality for suffix-closed dictionaries | Phrase count differs from K, especially variable address costs. Journal abstract inspected. |
| [Kosolobov–Shur (IPL 2019)](https://doi.org/10.1016/j.ipl.2018.09.005) | Relations between LZ77 parsing models with/without overlap | LZ77's earlier-target pointers differ from fixed-source COPY. Abstract/intro inspected. |
| [Kempa–Prezza (STOC 2018)](https://arxiv.org/abs/1710.10964) and [Kempa et al. (ESA 2018)](https://doi.org/10.4230/LIPIcs.ESA.2018.52) | Substring-covering and phrase-boundary/attractor viewpoint | Related combinatorics, not a verified theorem-level exact equality with A1–A3. Abstracts/definitions inspected. |

Additional issue #63 prior-art references (Gańczorz CPM 2019; Boneh–Golan–Kraus SODA 2026) remain mandatory if the stronger theorem track is ever reopened. A DOI/abstract is not a verified full source proof. Avoid both false-newness and false-exhaustive equivalence claims.

## Reopen / exit decision

A1–A3: **PROVED_MODEL_BASELINE / NOT_NOVELTY_CLEARED**. Standalone fixed short-q certificate: **NO-GO_FOR_STANDALONE_q<=2**. Generic codec/product: **UNTESTED**, *not* global NO-GO. TOM-006-B/C is permitted only after a specific workload, wire format, reusable-index provenance and cheap comparator are preregistered; otherwise record this negative witness and move on to a distinct Mathlab theorem opportunity. No separate Rust crate or G4 announcement.
