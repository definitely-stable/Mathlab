# UCT-005 G3-B2-D1-A — one-probe exact parity certificate and causal-resource falsifier

**10 October 2026** · root [#105](https://github.com/definitely-stable/Mathlab/issues/105), multi-epoch [#178](https://github.com/definitely-stable/Mathlab/issues/178), D1 [#223](https://github.com/definitely-stable/Mathlab/issues/223). Follows D0 [source import PR #222](https://github.com/definitely-stable/Mathlab/pull/222).

**Scientific state:** `RESTRICTED_CLASSICAL_EXACT_ONE_PROBE_LOWER / CONSTRUCTIVE_SHARPNESS / HONEST_FENWICK_FALSE_GLOBAL_PRODUCT / FINITE_INDEPENDENT_ORACLES / NO_NEW_ASYMPTOTIC_UCT_BOUND / NO_BYZANTINE_SECURITY / NO_PHYSICAL_PAGES / ROOT_OPEN_UNPROVED`.

## 1. Exact frozen F0 / *honest* bit-cell model, not F1

Let `n >= 1`, state space `X = {0,1}^n`, with independent binary coordinates. Public `SET(i,b)` overwrites coordinate `i`; each true change `FLIP(i)` is an admissible SET. Queries are **all** nonempty half-open intervals `RANGE_PARITY(l,r)`, returning XOR of `x_l,...,x_(r-1)`. An honest remote representation `E(x) in {0,1}^m` must work for **every** `x in X` and update edge. There are no free state-dependent public tables, query-dependent local persistent bits, proofs, downloaded transcript or trusted state; the query address depends only on the public interval. A one-probe decoder is an arbitrary Boolean function of its *one selected remote cell* and public interval; thus a constant, identity or complement. Charge **remote bit cells changed** for each SET and **remote bit cells read** for each query. Counting a changed bit is a LOWER bound on any implementation's actual remote writes, not a measurement of API calls or SSD bytes.

This is **not** the F1 authenticated service: malicious cells, SHA binding, published epochs, two offline reader PIN roots, full proof messages, setup programs, author source reads, persistent page allocation and crash semantics are not priced or protected here. Do not transfer the lemma to computational Byzantine security without a new explicitly paid construction/reduction.

## 2. Classical exact lower bound, sharp in its specified model

**Lemma D1A-T1.** Any such total exact deterministic 1-probe representation supporting all nonempty intervals requires

```
   m >= n(n+1)/2
   changed_remote_bits(FLIP(i)) >= (i+1)(n-i)   for i=0,...,n-1
   W_max >= floor((n+1)^2/4).
```

All three bounds are **simultaneously attained** by storing one parity bit per interval, in a fixed public order, and recomputing/toggling every interval containing `i` after a true bit change.

**Proof.** Every distinct interval defines a nonconstant linear Boolean function `f_(l,r): X -> {0,1}`. If two nonempty intervals are different, their GF(2) coefficient vectors differ, hence their functions cannot agree for all `x` or differ by a constant 1 for all `x` (evaluate both at zero). A single fixed remote cell `E_j(x)` plus the decoder's 1-bit output map can yield at most **one** nonconstant Boolean function up to complement; constants are not a valid query answer. Thus every interval requires its own distinct witness cell, giving `m >= n(n+1)/2`. Flipping input coordinate `i` toggles every interval-parity function covering `i`; their witness cells are distinct, so the encoding must change at least `(i+1)(n-i)` cells. Maximizing this concave integer quadratic over `i` gives `floor((n+1)^2/4)`. The explicit table construction achieves equality for every state and update, proving sharpness. QED.

**Novelty boundary:** this is an elementary information/decision-tree observation, not a new lower bound against general dynamic data structures or authenticated protocols. Its usefulness is to force correct query quantifiers and expose the exact `p=1` corner for later time-expanded proof attempts.

## 3. Overstrong resource conjecture: concrete false universal product

**Rejected claim H1-FALSE-1:** for *every* exact binary `SET/RANGE_PARITY` representation with no trusted bits, irrespective of its number of remote bit cells and read budget,

```
              W_max * Q_max >= n.
```

**Counterconstruction:** an honest remote `raw[0..n-1]` and binary Fenwick parity tree `tree[1..n]`. Every `SET` reads one charged raw bit to detect a no-op; on a change it overwrites one raw bit and at most `log2(n)+1` Fenwick cells. Every interval parity is a difference/XOR of two prefix-sum queries, each reading at most `log2(n)` Fenwick bits when `n=2^k`. Thus for power-of-two `n=2^k`,

```
     S_remote = 2n bits,
     U_read = 1 bit, W_max <= k+2, Q_max <= 2k,
     W_max * Q_max <= 2k(k+2).
```

For `n=4096, k=12`, the **explicit justified upper** gives `W_max<=14`, `Q_max<=24`, hence `W_max Q_max<=336 < 4096`. This strictly falsifies the universal product in this **honest remote bit-cell model**; the gap diverges with `n`. Tests implement actual one-bit SET and all interval queries, and verify the analytic envelope for small `n`. This is not a counterexample to *applicable known cell-probe tradeoffs*, which do not assert that false product. In particular, it does **not** give an F1 Byzantine protocol: a malicious server can lie about a Fenwick bit, and no proof/authenticated-root bytes or CPU are accounted for.

**Additional weak-quantifier failure:** if the task requires only full-range parity, a single parity bit updates in one remote cell and answers with one read, disproving any n-dependent lower bound that secretly substitutes one easy query for a uniform hard distribution over **all** ranges. A trusted n-bit client replica can eliminate remote query reads at the price of paid trusted state. These models must not be mixed.

## 4. Existing original sources — transfer matrix, with no invented full-text audit

| LIT | Work | What overlaps | Transfer into F1 authenticated SET/RANGE_PARITY? |
| --- | --- | --- | --- |
| 111/112 | Fredman–Saks / Pătraşcu–Demaine | Dynamic partial sums, cell-probe chronogram and sharp tradeoffs | `REDUCTION_REQUIRED`: bit/word size, delta alphabet, randomization, all-range hard quantifiers, external anchored checkpoint |
| 320/321 | Larsen 2012 / Yu 2016 | Cell sampling and communication-game information methods | `REDUCTION_REQUIRED`: weighted 2D range counts and dynamic interval union are not binary 1D SET parity |
| 156–158 | BEGKN / BKV memory checking | Trusted verifier memory, separated read/write and adversarial storage | `REDUCTION_REQUIRED`: arbitrary memory read/write semantics, full query proof, public author updates, trusted anchor and amortization |
| 159/199/200 | Tas–Boneh / accumulator update-frequency bounds | Succinct authenticated witnesses and paid updates | `REDUCTION_REQUIRED`: commitment/witness definition, setup, observer count and position-update information |
| 068/319 | Updatable BARG/IVC / ADSC-SNARK | State-consistent certified computation upper constructions | `UPPER_ONLY_CONDITIONAL`: no free independent-global latest anchor, setup/prover work and proof bytes must be charged |
| 317–318 (now 349–350) | SUNDR / COP | Fork consistency with untrusted server | `NOT_SAME_F1_TASK`: fork histories do not automatically guarantee independently verifiable LATEST |
| 322/323 (now 354/355) | DSST persistence / 2026 HMT | Historical versioning and dynamic-workload proof upper constructions | `UPPER_ONLY_CONDITIONAL`: page retention, rebalancing, proof bytes and memory charged |
| 324 (now 356) | Integrita BFT distributed storage | Multi-node view-consistency | `NOT_SAME_F1_TASK`: distributed Byzantine trust and q-detection are not independent single-anchor latest |

The overlap audit is **model-level**, based on primary bibliographic/abstract materials as recorded in D0. No source's precise full proof and all quantifiers have been re-derived here.

## 5. Independent oracle and next H1 discovery gate

- [Exhaustive deterministic checks](../../research/test_uct005_d1a_causal_falsifiers.py) compute all `2^n` binary words, their distinct interval truth tables *modulo complement*, all FLIP edges, exact changed witness counts and equality against a separately defined direct XOR oracle for `n<=6`.
- Independently instantiate paid honest raw+Fenwick SET and every interval for all `n<=8`, with no-op and changed-SET costs, plus logarithmic-product counterexamples at powers `k=7,8,10,12,16`.
- [Model and report](../../research/uct005_d1a_causal_falsifiers.py) output exact resource units and a non-promotion marker; GitHub-hosted unit CI is mandatory.

**NEXT D1-B:** move to one *truly joint* multi-epoch `F1` inequality with public honest author, trusted monotone anchor and adversarial proof channel. Before a theorem claim, derive full primary-paper same-model applicability for LIT-111/112/119/156–159/199–200/320/321/349–356, define an explicit hard adaptive range distribution and charge `(s,S,B,U_r,U_w,Q_r,B_pi,C,G,V,T,H,lambda,epsilon)`. Reject any bound collapsed to classical one-probe counting or falsified by Fenwick/snapshot/replica/VC/IVC points. If novelty fails, record `STOP_NOVELTY` for this task and preserve the correct restricted lemmas as independent components.

**The foundational UCT-005 root [#105](https://github.com/definitely-stable/Mathlab/issues/105) remains `OPEN_UNPROVED`.**
