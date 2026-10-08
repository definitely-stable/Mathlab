# LENT-001-G2A — exact Phase-A evidence

Status: **EXACT NUMERICAL RESULT**

Decision: **G2_EXPAND_GRID**

Novelty status: **NOT CLAIMED**

GitHub-hosted CI:

- run: \`37746812318\`
- conclusion: SUCCESS
- unit tests: 14 passed

Acceptance markers observed:

- \`G2A_ASET_EXACT_PASS\`
- \`G2A_LINEAR_BASELINE_PASS\`
- \`G2A_W1_PASS\`
- \`G2A_WITNESS_PASS\`
- \`G2A_PHASE_A_PASS\`

## 1. Exact d=2, w=2 cases

| q | m | w | candidate columns | exact ASET max | exact stronger linear max | LENT upper |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | 3 | 2 | 18 | **5** | 3 | 6 |
| 5 | 2 | 2 | 24 | **5** | 2 | 6 |
| 7 | 2 | 2 | 48 | **7** | 2 | 9 |

The branch-and-bound search exhausted:

- 4,161 nodes for q=3,m=3,w=2;
- 24,336 nodes for q=5,m=2,w=2;
- 5,079,636 nodes for q=7,m=2,w=2.

Every extremal witness was independently rechecked by the pre-existing ASET
oracle.

## 2. Persisted ASET witnesses

### q=3, m=3, w=2, V=5

\[
(0,0,1),\;
(0,1,0),\;
(0,2,2),\;
(1,0,1),\;
(2,2,0).
\]

### q=5, m=2, w=2, V=5

\[
(0,1),\;
(0,2),\;
(1,0),\;
(2,0),\;
(4,4).
\]

### q=7, m=2, w=2, V=7

\[
(0,1),\;
(0,2),\;
(1,0),\;
(1,3),\;
(2,5),\;
(4,2),\;
(5,6).
\]

## 3. Stronger arbitrary-linear baseline

The exact maxima under the stronger requirement "no arbitrary-coefficient
dependency among at most four columns" are:

\[
3,\;2,\;2
\]

for the three frozen cases respectively.

Thus finite odd-characteristic ASET can be substantially larger than the
stronger sparse-linear baseline.

This is a model-gap result, not an asymptotic theorem.

## 4. Critical interpretation: only one w=2 case is genuinely sparse

The q=5 and q=7 Phase-A cases have

\[
m=w=2.
\]

Therefore every nonzero vector in \(\mathbb F_q^2\) already satisfies the
support constraint.

These cases test the restricted-relation model, but **not** the hard-support
frontier.

The q=3 case has

\[
m=3>w=2
\]

and is the only Phase-A w=2 case where the support constraint removes
candidate columns.

Therefore Phase A is insufficient for theorem selection.

## 5. Exact w=1 theorem baseline

G2A proves:

\[
A_q^{set}(m,1,2)
=
m A_q^{set}(1,1,2).
\]

For the frozen fields:

\[
A_3^{set}(m,1,2)=m,
\]

\[
A_5^{set}(m,1,2)=2m,
\]

\[
A_7^{set}(m,1,2)=3m.
\]

The CI-checked instances were:

- q=3,m=4: exact value 4; LENT upper 7;
- q=5,m=3: exact value 6; LENT upper 10;
- q=7,m=3: exact value 9; LENT upper 15.

This shows that the general Hamming-ball bound is not sharp even in the
simplest hard-support lane.

The w=1 theorem is useful as a calibration result but is too elementary /
too close to one-dimensional distinct-sum theory to serve as the main G4
target without a separate novelty audit.

## 6. Phase-A decision

\[
\boxed{\texttt{G2\_EXPAND\_GRID}}
\]

Reasons:

1. exact odd-characteristic model separation is real;
2. only q=3,m=3,w=2 currently tests nontrivial hard support;
3. q=5/q=7 must be moved to \(m>w\);
4. the LENT upper bound has visible slack;
5. theorem selection now requires at least one additional sparse scaling point.

## 7. G2B target

Priority cases:

1. q=3,m=4,d=2,w=2 — small enough for an improved exact search;
2. q=5,m=3,d=2,w=2 — first genuinely sparse q=5 case;
3. q=7,m=3,d=2,w=2 — only after solver/certificate improvements.

G2B must improve the solver rather than silently increasing CI runtime.

A theorem may be selected only after at least q=3 and q=5 have genuine
\(m>w\) evidence.
