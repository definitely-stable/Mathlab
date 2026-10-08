# LENT-001 — prior-art audit

Status: **G1 OPEN / G1A ACTIVE**.

This document records the current source-level boundary between Mathlab and neighboring literature. It is deliberately conservative: mathematical correctness and publication novelty are separate questions.

## 1. Sparse parity-check matrices

### Binary overlap

Lefmann, Pudlák and Savický (1996) and later Naor–Verstraete study sparse parity-check matrices with bounded column weight and small-set column independence.

For the frozen Mathlab model at \(q=2\), exact subset-sum injectivity for all sets of size at most \(d\) is equivalent to the absence of a nonempty GF(2) dependency among at most \(2d\) columns.

Therefore the sharp binary extremal lane is not a clean novelty target.

References:

- Lefmann, Pudlák, Savický, "On sparse parity check matrices" (1996), LNCS 1090.
- DOI: https://doi.org/10.1007/3-540-61332-3_137
- Naor, Verstraete, "Improved bounds on the size of sparse parity check matrices" (ISIT 2005).
- DOI: https://doi.org/10.1109/ISIT.2005.1523645

### Nonbinary arbitrary-coefficient result

Hanno Lefmann, "Sparse Parity-Check Matrices over GF(q)", Combinatorics, Probability and Computing 14 (2005), 147–169.

Primary source:
https://doi.org/10.1017/S0963548304006625

Lefmann defines \(N_q(m,k,r)\) using \(m\)-row matrices with at most \(r\) nonzero entries per column and the requirement that any \(k\) columns are linearly independent over \(GF(q)\).

Reported results include:

- for even \(k\ge2\),
  \[
  N_q(m,k,r)=\Omega\!\left(m^{kr/(2(k-1))}\right);
  \]
- for certain \(k=2^i\) / gcd regimes, matching \(\Theta\)-orders;
- for \(k=4\) and \(\operatorname{char}(GF(q))>2\),
  \[
  N_q(m,4,r)=\Theta\!\left(m^{\lceil4r/3\rceil/2}\right);
  \]
- in characteristic two for that \(k=4\) statement, the source records only the corresponding upper bound.

### Critical Mathlab boundary

Lefmann's property forbids arbitrary nonzero field coefficients in a short linear dependence.

Mathlab ASET exactness forbids only collision relations

\[
\sum_i \varepsilon_i a_i=0
\]

with

\[
\varepsilon_i\in\{-1,0,1\},
\qquad n_+(\varepsilon)\le d,
\qquad n_-(\varepsilon)\le d.
\]

Thus for \(q>2\) Lefmann gives a stronger sufficient condition, not an established equivalence.

This distinction is now a first-class G1A requirement. It already separates at q=3: with m=1,d=1 and columns 1 and 2=-1, ASET singleton states are distinct while the two columns satisfy 1+2=0.

## 2. ASET / dissociated / Sidon / B_h boundary

The primary Mathlab object is now

\[
A_q^{\mathrm{set}}(m,w,d),
\]

the largest universe size admitting support-\(w\) vectors in \(\mathbb F_q^m\) whose subset sums for all sets of size at most \(d\) are distinct.

A collision is a bounded signed relation. This makes dissociated / bounded-order dissociated sets a natural prior-art cluster.

Sidon and \(B_h\) families are also nearby, but no blanket equivalence is recorded because conventions differ on:

- repeated summands;
- distinct summands;
- exactly \(h\) versus all sizes up to \(h\);
- collisions between different cardinalities;
- bounded support / Hamming-ball restrictions;
- ambient operation.

G1A/G1B must build a definition-by-definition source matrix before importing an exponent or claiming a gap.

## 3. Update-efficient coding — direct locality neighbor

Mazumdar, Chandar and Wornell, "Update-Efficiency and Local Repairability Limits for Capacity Approaching Codes", IEEE Journal on Selected Areas in Communications 32(5), 2014, 976–988.

Primary manuscript:
https://dspace.mit.edu/entities/publication/3cee62d1-5b96-4b1a-8f23-8a9113b1f389

They study how many encoded bits must change when a single information bit changes. In their capacity-approaching BEC/BSC setting, nontrivial rate with vanishing error requires logarithmic update-efficiency scaling in block length, and matching capacity-achieving constructions are discussed.

This is substantially closer to Mathlab update locality than LDC/LCC query locality.

However the models are still different:

- coding uses the full message space;
- Mathlab restricts inputs to a sparse Hamming ball / bounded set size;
- coding includes a noisy-channel reliability objective;
- Mathlab uses deterministic exact injectivity on the admissible input family.

Therefore this literature is a strong prior-art neighbor, not an automatic proof of LENT/ASET bounds.

## 4. LCC/LDC boundary

LCC/LDC query or repair locality measures how many encoded symbols are read to recover information or repair a symbol.

Mathlab update locality measures how many sketch coordinates change when one universe element is inserted or deleted.

No LCC/LDC query lower bound is to be imported as an update-locality lower bound without a formal reduction.

The earlier broad G1 report overstated this analogy; G1A records the correction.

## 5. Rate-compatible / nested codes

Pengfei Huang, Yi Liu, Xiaojie Zhang, Paul H. Siegel and Erich F. Haratsch, "Syndrome-Coupled Rate-Compatible Error-Correcting Codes: Theory and Application", IEEE Transactions on Information Theory 66(4), 2020, 2311–2330.

Author publication page:
https://cmrr-star.ucsd.edu/psiegel/publications/

This is relevant evidence that good rate-compatible/nested code families can exist in a neighboring coding model.

It weakens a naive conjecture that nestedness alone must impose a positive asymptotic constant tax.

It does not settle Mathlab because ASET has:

- a sparse source family rather than a full message space;
- deterministic exact injectivity;
- bounded per-element update support.

**Decision:** deprioritize pure nestedness tax; retain nestedness + bounded update locality.

## 6. Mixed alphabets

Yehezkeally, Al Kim, Puchinger and Wachter-Zeh, "Bounds on Mixed Codes with Finite Alphabets", arXiv:2212.09314.

Reference:
https://arxiv.org/abs/2212.09314

The work generalizes several classical coding bounds to finite mixed alphabets.

Therefore Mathlab must not treat heterogeneous coordinate alphabets as an untouched area.

The direct LENT counting extension

\[
N_d(V)
\le
\sum_{\substack{J\subseteq[m]\\|J|\le dw}}
\prod_{j\in J}(q_j-1)
\]

is a derived baseline. Sharp optimization under bit-budget plus update-locality constraints remains a separate prior-art question.

## 7. PinSketch / Minisketch

Minisketch is an optimized BCH-based implementation of PinSketch-style set reconciliation.

Primary project:
https://github.com/bitcoin-core/minisketch

Mathematical overview:
https://github.com/bitcoin-core/minisketch/blob/master/doc/math.md

Relevance:

- practical large-alphabet/algebraic comparator;
- sketches combine linearly to represent symmetric difference;
- does not provide constant support locality as capacity grows.

Therefore it motivates the LENT frontier but is not a counterexample.

## 8. Stuffed IBLTs

Jonas Klausen, Rasmus Pagh, Stefan Walzer,
"Stuffed IBLTs: Optimal Linear Multiset Sketches" (2026).

Preprint:
https://arxiv.org/abs/2609.17487

The construction is relevant to the practical frontier of near-optimal space and cheap updates under randomized/high-probability guarantees.

Mathlab classification:

**RANDOMIZED / ADDITIVE COMPARATOR**, not a deterministic exact ASET instance by default.

## 9. External deep-research report — retained and rejected parts

A deep-research report supplied on 2026-10-08 was useful for identifying adjacent areas, but several conclusions are not accepted as repository authority.

Retained:

- q-ary sparse dependence literature is relevant;
- rate-compatible coding must be included in nested analysis;
- update-efficient coding must be included in locality analysis;
- mixed alphabets need their own prior-art pass.

Rejected or corrected:

- generic q-ary small-column independence is not "exactly" the ASET model for \(q>2\);
- pure nestedness tax is not currently the strongest novelty target;
- LCC/LDC query locality is not directly Mathlab update locality;
- "computation" is not yet a frozen independent parameter;
- IBLTs are not deterministic exact ASET examples.

The detailed correction record is in LENT-001-G1-CORRECTIONS.md.

## 10. Current novelty verdict

- finite LENT counting theorem: **BASELINE / NOVELTY NOT CLAIMED**;
- binary sharp extremal problem: **STOP AS PRIMARY NOVELTY TARGET**;
- \(A_q^{\mathrm{set}}(m,w,d)\): **PRIMARY G1 CANDIDATE / NOVELTY UNRESOLVED**;
- pure nestedness tax: **DEPRIORITIZED**;
- nestedness + update locality: **SECONDARY CANDIDATE**;
- mixed alphabets: **BASELINE KNOWN NEIGHBOR / SHARP QUESTION OPEN**;
- communication + locality + computation: **DEFERRED UNTIL MODEL FREEZE**.

G1 is not closed.
