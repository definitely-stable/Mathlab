# UCT-005 D1-C0 — observational entropy of online SET histories and PIN versions

2026-10-11 · [D1-C research gate #302](https://github.com/definitely-stable/Mathlab/issues/302) · [slice #303](https://github.com/definitely-stable/Mathlab/issues/303) · [UCT root #105](https://github.com/definitely-stable/Mathlab/issues/105). **Classification: EXACT_CLASSICAL_HAMMING_OBSERVATION_COUNT / FINITE_BIJECTION / STOP_NOVELTY / F1_PHYSICAL_REDUCTION_NOT_PROVED**.

## Problem: pinned epochs are not independent random n-bit objects

In the restricted *observation-only projection* of the accepted F1 `SET(i,b)`, `RANGE_PARITY(l,r)`, `PIN_CURRENT(reader)`, `AS_OF(reader,t,l,r)`, each of H online SETs changes **zero or one** coordinate of an n-bit state. A SET which writes the previous value is a legal no-op and creates a new epoch.

Freeze public observed epoch labels `0≤t₀<...<tₖ≤H`; for each observed epoch, ALL singleton RANGE_PARITY queries (and hence all nonempty ranges) are available as truthful, complete binary outputs. This is only the **answer tuple alphabet**, not the authenticated protocol, public update-label transcripts, signatures, root freshness, threat model, proof/wire traffic, page allocations, or physical complexity. In particular, `t_j` is fixed and public; hiding epoch labels or allowing arbitrary independent state replacement changes the information accounting. Two offline readers may separately hold PIN0 and PIN2 and ask AS_OF at these epochs while the online author exposes LATEST epoch3; this valid two-reader case has observed times `(0,2,3)`.

Set `V(n,d)=Σ_{j=0}^{min(n,d)} binom(n,j)`. Then

```
K(n;t₀,...,tₖ) = 2^n × ∏_{j=1}^k V(n,t_j−t_{j−1})
minimum fixed encoding bits = ceil(log₂ K).
```

**Elementary proof:** The first named snapshot may be any n-bit word, including when t₀>0 (choose a legal prehistory). Over Δ SET steps, exactly every endpoint with Hamming distance ≤Δ from the first endpoint is reachable: flip each differing coordinate once, use legal no-op operations for unused steps. No endpoint outside the ball is reachable. The conditional number V(n,Δ) is constant for every starting word. Multiply the independent choices at successive intervals. Every snapshot bitmap is exactly recovered by singleton RANGE_PARITY, so each distinct tuple requires a distinct exact *observation-only representation*. Conversely, a finite publicly parameterized mixed-radix enumerative code records the first n-bit word and the **rank of each XOR difference inside its bounded Hamming ball**, reaching precisely `ceil(log₂ K)` fixed bits across all tuples (abstract static bit capacity; data structures/CPU to rank/unrank are not free in F1).

For all times `(0,1,...,H)`, Δ=1 and `V(n,1)=n+1`, so `K=2^n (n+1)^H`. The full update alphabet's multiple differently labelled no-op SETs produce identical **bitmaps**, not identical author receipts; those receipts and labels are intentionally excluded. This is a conditional compression **countermodel** to falsely treating historical bitmaps as independent, not a novel theorem.

| n=5, H=3 exact restricted history | Distinct answer tuples | Minimum fixed bits | Independent snapshot baseline |
| --- | ---: | ---: | ---: |
| PIN reader0 at 0, PIN reader1 at 2, LATEST 3 | 3,072 | 12 | 15 bits for three unrelated snapshots |
| Observe every epoch 0,1,2,3 | 6,912 | 13 | 20 bits for four unrelated snapshots |
| Publicly promised SET at epoch2 is a no-op; epochs 0,2,3 | 1,152 | 11 | 15 bits unrelated |

The third row is **a different transcript contract**. Observing the labels `(0,2,3)` without the no-op promise gives 3072 histories; treating the actual chosen benchmark no-op as publicly known and mandatory gives 1152, not 3072. This is why the full F1 transcript/author update information must not be silently discarded in any transfer.

## What changes if author SET labels are observed?

This is a **different observation contract** and must be accounted for separately. If epoch0 bits and every author `SET(i,b)` position-and-value label are part of the visible transcript, then the exact number of *labeled author histories* over H epochs is

```
K_labeled(n,H) = 2^n (2n)^H,
```

because each author step has n possible coordinates and two assigned values, regardless of whether the new value equals the old. Distinct `SET(i,b)` label histories are distinguishable as **author records** even when they produce exactly the same bitmap versions. This count is **not** the sum of cryptographic receipts, root generation/clock bytes or verifier/prover work. For example n=4,H=3 has `8192` (13-bit) initial+label histories but `2000` (11-bit) distinct full-bitmap observation sequences. Treating the label transcript as FREE state-dependent help is prohibited in F1. Treating that label entropy as mandatory bitmap-only storage is equally invalid if it is not in the observation contract.

The separate `independent_labeled_receipt_oracle` exhaustively enumerates **actual `SET(i,b)` operations** and checks both counts for n≤4,H≤3, rather than silently identifying update labels with canonical flip/no-op symbols. A formal F1 proof must explicitly specify whether it requires authenticated author labels/receipts, their public availability, and their transmission/storage units.

## Independent finite falsifier and exact coding

[Finite oracle](../../research/uct005_d1c0_observation_entropy.py) independently expands all `2^n (n+1)^H` legal *snapshot paths* for n≤5,H≤3 from canonical flip/no-op SET outcomes, projects each onto **every nonempty subset** of observed epochs and deduplicates exact output tuples. It checks closed-form counts against enumerated tuples and independently verifies the mixed-radix rank/unrank bijection. [Tests](../../research/test_uct005_d1c0_observation_entropy.py) also check all range/singleton parity equivalences, n=5 sparse gap rank space, arbitrary first-observed t₀, known no-op contract and incorrect/out-of-range epochs. Integer bit lengths avoid floating-point `log₂` rounding. The finite encoder uses explicit bounded Hamming mask enumeration (n≤12 only); the analytic count formula itself has no bounded-n claim.

**Important limitation:** A bit-efficient static representation does not imply small online update reads/writes, honest constant trusted scratch, bounded proof refresh, remote page-rounding or malicious SHA guarantee. The encoder may be expensive to update/query; it has no accepted F1 resource vector. Hence no physical `S\cdot U\cdot Q` or joint resource theorem follows from `ceil(log₂ K)`. A source-only delta transcript may require charged private/public update labels, per-epoch indexes, authenticated roots, crash fencing and provenance. Do not call the ∏V expression an asymptotically original PIN/GC theorem.

## Prior art, explicit STOP and next experiment

The direct combinatorial statement is standard Hamming-ball counting. For actual persistent data structures, Driscoll, Sarnak, Sleator and Tarjan, *Making Data Structures Persistent*, JCSS **38(1), 86–124 (1989)**, [DOI](https://doi.org/10.1016/0022-0000(89)90034-2), [author paper](https://www.cs.cmu.edu/~sleator/papers/making-data-structures-persistent.pdf), establishes efficient **non-authenticated** persistence for specified linked data structures. That result does not directly supply a fixed-P-byte SHA-authenticated multi-reader F1 model, but is an indispensable upper-bound/barrier. Modern source model gates in D1 #223 also include Fredman–Saks, Pătraşcu–Demaine, BKV memory checking, authenticated VC and SUNDR/COP. No transfer asserted without preserving adversary, trusted roots, input/output and units.

**D1-C0 verdict: `STOP_NOVELTY` as a candidate original root theorem; `ACCEPT` as a finite falsification of naive independent-history output entropy.** D1-C #302 is still an open root-benchmark gate. To progress beyond this slice, propose a *single quantified fully priced* bound on one natural F1 task that survives the log/bitmap COW/snapshot/replica uppers, exact PIN/history entropy, memory-checker source transfer and adversarial paid stage failures. Independently check n≤3,H≤3 before discussing a proof. Otherwise record D1 `STOP` rather than renaming the exact counting lemma.

GitHub-hosted full Research + dedicated F0 + INDEX/D1-A (if triggered) final-head required; root remains `OPEN_UNPROVED`.
