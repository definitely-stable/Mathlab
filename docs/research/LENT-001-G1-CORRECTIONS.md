# LENT-001 — G1 correction pass

Status: **ACTIVE / G1A INPUT**

Date: 2026-10-08

This note records the critical corrections produced after reviewing the external deep-research report supplied for G1. The report is treated as secondary evidence and a research lead, not as an authority. This document separates:

- claims supported by the report;
- corrections derived from direct model analysis;
- prior-art conclusions that still require source-level closure.

## 1. What survives unchanged

The finite LENT counting theorem remains valid in the frozen deterministic exact additive-sketch model:

\[
N_d(V)=\sum_{i=0}^{d}\binom{V}{i}
\le
B_q(m,dw)
=
\sum_{j=0}^{\min(dw,m)}\binom{m}{j}(q-1)^j.
\]

No publication novelty is claimed for this counting statement.

Its role is unchanged: it is the baseline information/locality impossibility bound from which sharper model-specific questions are derived.

## 2. Primary correction: the q-ary problem is not ordinary small-column independence

Let

\[
\Phi(S)=\sum_{i\in S} a_i,
\qquad a_i\in\mathbb F_q^m,
\qquad |\operatorname{supp}(a_i)|\le w.
\]

Exactness on all sets of cardinality at most \(d\) means that for distinct \(S,T\),

\[
|S|,|T|\le d
\implies
\Phi(S)\ne\Phi(T).
\]

After cancelling \(S\cap T\), a collision is equivalent to a relation

\[
\sum_i \varepsilon_i a_i=0
\]

with

\[
\varepsilon_i\in\{-1,0,1\},
\qquad
n_+(\varepsilon)\le d,
\qquad
n_-(\varepsilon)\le d,
\]

where \(n_+\) and \(n_-\) count positive and negative coefficients.

The separate side bounds are part of the model. Merely saying "a relation of length at most \(2d\)" loses information.

### Consequence for q=2

Since \(-1=1\) in characteristic two, every nonempty dependency on at most \(2d\) distinct columns can be split into two parts, each of size at most \(d\).

Therefore, for \(q=2\), exact-set injectivity is equivalent to the absence of a nonempty GF(2) dependency among at most \(2d\) columns.

This is why the binary extremal lane directly overlaps sparse parity-check-matrix literature.

### Consequence for q>2

Sparse parity-check results such as Lefmann's \(N_q(m,k,r)\) prohibit arbitrary nonzero field coefficients in a short linear dependence.

That condition is stronger than Mathlab's signed subset-sum condition.

Therefore the safe relation is:

\[
\text{arbitrary-coefficient small-column independence}
\Longrightarrow
\text{exact set-sum injectivity},
\]

not equivalence.

A trivial separation already occurs for \(q=5,m=1,d=1\):

\[
a_1=1,\qquad a_2=2.
\]

The states \(0,1,2\) are distinct, so the set sketch is exact for \(d=1\). But two nonzero columns in a one-dimensional vector space are linearly dependent.

For \(q=3\), all nonzero coefficients are \(\pm1\), but the separate constraints \(n_+\le d\) and \(n_-\le d\) still prevent a blanket equivalence with arbitrary short linear dependence.

## 3. New primary extremal object

Define

\[
A_q^{\mathrm{set}}(m,w,d)
\]

to be the maximum \(V\) for which there are columns

\[
a_1,\ldots,a_V\in\mathbb F_q^m
\]

with column support at most \(w\) and with all subset sums of sets of size at most \(d\) distinct.

This object is the preferred G1/G4 target.

It deliberately avoids the ambiguous phrase "q-ary restricted dependencies".

The current inclusion picture is:

\[
N_q^{\mathrm{lin}}(m,2d,w)
\le
A_q^{\mathrm{set}}(m,w,d)
\le
A_q^{\mathrm{LENT}}(m,w,d),
\]

where:

- the left term denotes a stronger arbitrary-coefficient small-column-independence problem of the sparse parity-check type;
- the right term denotes the maximum \(V\) allowed by the finite LENT Hamming-ball count.

The exact gap between the two is not yet classified as new.

## 4. Sidon / B_h correction

The external report correctly identifies additive-combinatorial proximity, but "direct equivalence" must not be used without a definition map.

Mathlab differs from classical formulations along several axes:

- sets contain distinct universe elements;
- some \(B_h\) definitions permit repeated summands;
- Mathlab requires all cardinalities \(0,\ldots,d\), not only exactly \(h\);
- cross-cardinality collisions must also be excluded;
- vectors are constrained to have support at most \(w\);
- arithmetic is inside a specified finite field/vector space.

For \(d=2\), Mathlab is best described as a restricted/weak-Sidon-like problem with cross-cardinality uniqueness and bounded support until a theorem-level equivalence is proved under one exact convention.

## 5. Nested-prefix correction

The pure claim

\[
\text{nestedness alone forces a positive asymptotic size tax}
\]

is no longer a preferred conjecture.

Rate-compatible coding literature gives strong evidence that good nested families can asymptotically approach ordinary coding bounds in neighboring models.

That does not solve Mathlab because the source family, exactness requirement and sparse-update constraint differ.

The preferred target is therefore:

\[
\boxed{\text{nestedness + bounded update locality}}
\]

rather than pure nestedness.

A useful quantity is a simultaneous competitive ratio such as

\[
\rho=
\max_{d\in D}
\frac{m_d\log_2 q}
{\log_2 N_d(V)}.
\]

The research question is whether requiring one common nested family with bounded column support forces \(\rho\) away from one in a regime where independent pointwise families need not.

## 6. Update locality correction

LCC/LDC query locality is not the same as Mathlab update locality.

- LDC locality: how many encoded symbols are read to recover one message symbol.
- LCC locality: how many encoded symbols are read to repair/recover a corrupted codeword symbol.
- Mathlab update locality: how many sketch coordinates change when one universe element is added or removed.

For a linear/additive representation, Mathlab update locality is structurally closer to sparse generator rows / update-efficient codes.

Therefore no LCC/LDC query lower bound may be imported as an update-locality theorem without a formal reduction.

## 7. Computation correction

The phrase "communication-locality-computation trilemma" is not yet a mathematical model.

If computation means only update arithmetic, then an update touching \(w\) coordinates already has \(O(w)\)-scale work and the parameter may collapse into locality.

Before any joint computation theorem, one of the following must be frozen independently:

- decoding time;
- incremental decoding work;
- cell probes;
- memory probes;
- preprocessing time;
- another explicit machine model.

Until then, LENT-JOINT is deferred.

## 8. Mixed/nonuniform alphabets

If coordinate \(j\) has alphabet size \(q_j\), a direct counting extension is

\[
N_d(V)
\le
\sum_{\substack{J\subseteq[m]\\|J|\le dw}}
\prod_{j\in J}(q_j-1).
\]

This is recorded as a derived baseline, not as a novelty theorem.

The potentially interesting question is the sharp optimization of heterogeneous \(q_j\) under a fixed bit budget and locality constraint, after mixed-alphabet coding prior art is mapped.

## 9. IBLT boundary

IBLT-style sketches are additive/composable but randomized and decoding can fail.

They are therefore useful comparators for the engineering frontier, but they are not deterministic exact instances of the frozen LENT model unless a fixed construction is injective for every admissible input.

## 10. Revised research ranking

1. **Priority 1:** \(A_q^{\mathrm{set}}(m,w,d)\) — bounded-support exact subset-sum families.
2. **Priority 2:** nested-prefix + bounded update locality.
3. **Priority 3:** mixed/nonuniform cells after a mixed-alphabet prior-art map.
4. **Deferred:** joint computation lower bound until the computational model is frozen.
5. **Deprioritized:** pure nestedness tax.
6. **Stopped as novelty target:** ordinary binary sparse parity-check extremal problem.

## 11. G1A gate

No new theorem search starts until G1A freezes:

- the exact \(A_q^{\mathrm{set}}\) definition;
- the signed-relation equivalence;
- q=2 equivalence and q>2 strict-separation logic;
- Sidon/B_h definition map;
- update-locality definition map;
- a source-to-claim matrix.

Acceptance marker: G1A_MODEL_PLAN_PASS.
