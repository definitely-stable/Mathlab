# LENT-001-G1A — first implementation plan

Status: **READY AFTER PR REVIEW**

Issue: #3

This is the first executable slice after the G1A documentation/model correction.

## Objective

Extend the existing tiny exhaustive oracle so that it distinguishes three properties that were previously conflated:

1. ASET exact subset-sum injectivity;
2. absence of bounded signed relations with separate positive/negative side limits;
3. arbitrary-coefficient small-column linear independence.

The slice is finite, exact, deterministic, and intended to falsify bad equivalence assumptions before any asymptotic proof work.

## Existing code to reuse

Current implementation already provides:

- sparse nonzero vector generation;
- exact subset-sum collision detection;
- q=2 small-dependency checking;
- exhaustive family enumeration;
- exact finite LENT bound checks;
- unit-test coverage for the binary equivalence.

No production/library API exists; this is research-only code.

## Planned code changes

### 1. Generalize the finite-field grid to prime q in {2,3,5}

File:

research/lent_exhaustive.py

The current arithmetic is coordinate-wise modulo q and is valid for prime q.

For G1A, explicitly allow only:

\[
q\in\{2,3,5\}.
\]

Do not silently generalize to non-prime prime powers until a proper finite-field representation exists.

### 2. Add an independent signed-relation oracle

Add a function conceptually equivalent to:

signed_relation_witness(columns, q, d)

It must search nonzero

\[
\varepsilon\in\{-1,0,1\}^V
\]

subject to

\[
n_+(\varepsilon)\le d,
\qquad
n_-(\varepsilon)\le d
\]

and return a witness when

\[
\sum_i\varepsilon_i a_i=0.
\]

This checker must be independent from collision_witness rather than deriving one result from the other, so CI can test the equivalence itself.

Required invariant:

\[
\text{ASET exact}
\Longleftrightarrow
\text{no signed witness}.
\]

### 3. Add arbitrary-coefficient small-column dependency checking

Add a prime-field checker conceptually equivalent to:

linear_dependency_witness(columns, q, max_size)

For every subset of at most max_size distinct columns, enumerate nonzero coefficients

\[
c_i\in\mathbb F_q^\*
\]

and test whether the linear combination is zero.

This is deliberately brute force: G1A uses only tiny finite cases.

Required relationship:

\[
\text{no arbitrary dependency up to }2d
\Longrightarrow
\text{ASET exact}.
\]

For q=2, CI must verify equivalence.

For q=3 and q=5, CI must contain explicit separation regressions.

### 4. Pin minimal separation regressions

#### q=3

\[
m=1,\quad d=1,\quad a_1=(1),\quad a_2=(2).
\]

Expected:

- ASET exact: true;
- signed bounded relation: absent for d=1;
- arbitrary dependency of size <=2: present because \(1+2=0\).

#### q=5

\[
m=1,\quad d=1,\quad a_1=(1),\quad a_2=(2).
\]

Expected:

- ASET exact: true;
- signed bounded relation: absent for d=1;
- arbitrary dependency of size <=2: present, e.g. \(2a_1-a_2=0\).

These witnesses are model-separation tests, not novelty claims.

### 5. Add nontrivial d>=2 search cases

The machine-readable G1A grid should include small cases that can finish quickly in GitHub-hosted CI.

Initial candidates:

- q=2, m=4, d=2, w=2;
- q=3, m=3, d=2, w=2;
- q=5, m=2 or 3, d=2, w=1 or 2.

The exact max_v values must be chosen after measuring combinatorial cost.

Do not enlarge the grid until the CI runtime is observed.

### 6. Exact result schema

Each exhaustive result should report at least:

- q, m, d, w, V;
- number of candidate columns;
- number of ASET-exact families;
- number of full-linear-independent families;
- number of ASET-but-not-full-linear families;
- first separation witness, if any;
- finite LENT bound status.

This creates evidence that can later be promoted as EXACT NUMERICAL RESULT.

## Unit tests

Extend research/test_lent.py with:

1. signed-relation equivalence on a bounded q=2/3/5 grid;
2. q=2 exactness <-> no dependency <=2d;
3. q=3 pinned separation;
4. q=5 pinned separation;
5. implication:
   no full dependency <=2d => ASET exact;
6. adversarial relation with too many positive coefficients to ensure side bounds are respected;
7. empty family / d=0 edge cases if the frozen API admits them.

## Proof note

Before or with the code PR, add a compact theorem note proving:

### ASET-SIGNED

\[
\Phi(S)=\Phi(T)
\]

iff, after cancelling the intersection, there exists a signed relation whose positive and negative supports each have size at most d.

### ASET-BINARY

For q=2, exactness up to d iff no nonempty dependency exists among at most 2d distinct columns.

### ASET-QGT2-SEPARATION

The q=3 and q=5 pinned singleton examples show that arbitrary-coefficient independence is strictly stronger than ASET exactness.

Status of all three in this slice:

DERIVED RESULT / BASELINE; NOVELTY NOT CLAIMED.

## CI acceptance

Required markers:

G1A_SIGNED_EQUIV_PASS

G1A_Q2_EQUIV_PASS

G1A_Q3_SEPARATION_PASS

G1A_Q5_SEPARATION_PASS

G1A_ORACLE_PASS

## Non-goals

Do not in this slice:

- prove an asymptotic ASET exponent;
- claim novelty;
- implement general GF(p^k);
- optimize the brute-force oracle;
- start Lean formalization;
- revive pure nestedness tax;
- define computation complexity.

## Exit

When all exact tests pass and the proof note is reviewed, the next allowed action is G1B:

primary-source closure for k-dissociated / weak Sidon / B_h / sparse parity-check objects using the source-to-claim matrix.

Only after G1B may Mathlab choose a sharp ASET theorem target.
