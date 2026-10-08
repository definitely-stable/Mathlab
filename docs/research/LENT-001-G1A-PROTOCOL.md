# LENT-001-G1A — ASET model-freeze protocol

Status: **FROZEN FOR PLANNING**

Issue: #3

Baseline branch point:

\[
\texttt{main@f89a8db71b50a3c504643464b391f8414ebc2244}
\]

## 1. Objective

Freeze the exact mathematical object and its nearest prior-art boundaries before attempting a sharp bound or novelty theorem.

Primary object:

\[
A_q^{\mathrm{set}}(m,w,d).
\]

No publication novelty is claimed in G1A.

## 2. Exact model

Let \(q\) be a prime power and let

\[
a_1,\ldots,a_V\in\mathbb F_q^m.
\]

Each column satisfies

\[
|\operatorname{supp}(a_i)|\le w.
\]

For a set \(S\subseteq[V]\), define

\[
\Phi(S)=\sum_{i\in S}a_i.
\]

The family is \((q,m,w,d)\)-ASET-exact when

\[
S\ne T,\quad |S|,|T|\le d
\implies
\Phi(S)\ne\Phi(T).
\]

Define \(A_q^{\mathrm{set}}(m,w,d)\) as the maximum \(V\) for which such a family exists.

## 3. Signed-relation form

ASET-exactness is equivalent to the nonexistence of a nonzero vector

\[
\varepsilon\in\{-1,0,1\}^V
\]

such that

\[
\sum_i\varepsilon_i a_i=0,
\]

with

\[
n_+(\varepsilon)\le d,\qquad n_-(\varepsilon)\le d.
\]

The proof must explicitly preserve the two side bounds.

## 4. Boundary with sparse parity-check matrices

Define the stronger property LIN-\(2d\):

every set of at most \(2d\) distinct columns is linearly independent over \(\mathbb F_q\).

Then

\[
\text{LIN-}2d
\Longrightarrow
\text{ASET-exact}.
\]

### q=2

For \(q=2\),

\[
\text{LIN-}2d
\Longleftrightarrow
\text{ASET-exact}.
\]

This equivalence is a baseline and not a novelty claim.

### q>2

Do not claim equivalence.

Required separation witness:

\[
q=5,\quad m=1,\quad d=1,\quad
a_1=1,\quad a_2=2.
\]

ASET-exactness holds for sets of size at most one, while the two columns are linearly dependent.

### q=3

Do not infer equivalence merely because \(\mathbb F_3^\*=\{\pm1\}\).

The ASET condition retains the separate constraints on the number of positive and negative coefficients.

G1A must either provide a proof of an exact equivalence under additional hypotheses or record a counterexample.

## 5. Boundary with Sidon / B_h families

A source-to-definition map must record, for every compared paper:

- whether repeated summands are allowed;
- whether exactly \(h\) or all sizes up to \(h\) are controlled;
- whether cross-cardinality collisions are controlled;
- whether coefficients are all \(+1\), signed, or arbitrary field elements;
- whether ambient vectors have bounded support;
- whether the ambient operation is field addition, group addition, OR, or another operation.

No row is allowed to say "equivalent" unless all relevant coordinates of this map agree or a reduction is proved.

## 6. Locality boundary

Mathlab update locality is

\[
w=\max_i |\operatorname{supp}(a_i)|.
\]

It is a write/change locality.

It must not be identified with:

- LDC query locality;
- LCC repair/query locality;
- decoding locality;
- sparse parity-check row weight.

The nearest coding-theory comparator is update efficiency / sparse generator-row structure.

## 7. Nested boundary

Pure nestedness tax is not a G1A target.

The retained candidate is one common family of prefixes that is simultaneously close to the pointwise information bound while preserving bounded update locality.

A future protocol may use a competitive ratio

\[
\rho(D)=
\max_{d\in D}
\frac{m_d\log_2 q}{\log_2 N_d(V)}.
\]

No lower bound on \(\rho(D)\) beyond pointwise LENT is claimed here.

## 8. Mixed alphabets

For coordinate alphabets of sizes \(q_1,\ldots,q_m\), the baseline reachable-state count is

\[
B_{\mathbf q}(m,r)
=
\sum_{\substack{J\subseteq[m]\\|J|\le r}}
\prod_{j\in J}(q_j-1).
\]

Thus

\[
N_d(V)\le B_{\mathbf q}(m,dw).
\]

Status: DERIVED BASELINE / NOVELTY NOT CLAIMED.

## 9. G1A execution plan

### G1A-1 — model proof

Produce a short proof note for:

1. subset-sum injectivity \(\Longleftrightarrow\) signed-relation condition;
2. q=2 equivalence to small-column independence;
3. q>2 implication direction and explicit separation;
4. exact handling of \(d=0\), \(w=0\), \(m=0\), and \(V=0\).

### G1A-2 — executable oracle

Extend the research harness so that for tiny parameters it can separately test:

- ASET-exactness;
- signed-relation absence;
- arbitrary-coefficient small-column independence.

Required fields: \(q=2,3,5\).

The oracle must reproduce the q=5 separation witness and search for the smallest q=3 separation or certify none in the searched finite box.

### G1A-3 — source-to-claim matrix

Audit primary sources in four clusters:

1. sparse parity-check matrices over finite fields;
2. dissociated / k-dissociated / weak Sidon / B_h families;
3. update-efficient codes / sparse generator matrices;
4. rate-compatible/nested codes and mixed-alphabet bounds.

Every source gets:

- exact definition;
- parameter map;
- implication direction;
- theorem imported, if any;
- whether bounded support appears;
- novelty effect on Mathlab.

### G1A-4 — decision gate

Allowed exits:

- G1A_CONTINUE_ASET;
- G1A_REDUCE_TO_KNOWN_OBJECT;
- G1A_SPLIT_Q3_QGT3;
- G1A_STOP_NOT_NOVEL.

Nested/locality and mixed-alphabet lanes remain secondary until this gate closes.

## 10. Acceptance

Planning acceptance requires:

- issue #3 exists;
- correction note exists;
- this protocol exists;
- ROADMAP, CLAIMS, DECISIONS, OPEN-QUESTIONS and PRIOR-ART are synchronized;
- CI is green on the PR head.

Planning marker:

G1A_MODEL_PLAN_PASS.
