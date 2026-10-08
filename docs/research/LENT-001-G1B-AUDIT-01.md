# LENT-001-G1B — primary-source audit 01

Status: **PRIMARY-SOURCE VERIFIED / PARTIAL G1B**

Date: 2026-10-08

This tranche audits the closest definition-level neighbors discovered before
attempting a sharp ASET theorem.

It does not close G1B.

## 1. Sparse parity-check matrices: Lefmann 2005

Primary source:

Hanno Lefmann, *Sparse Parity-Check Matrices over GF(q)*,
Combinatorics, Probability and Computing 14 (2005), 147–169.

DOI:
https://doi.org/10.1017/S0963548304006625

Author PDF:
https://www.tu-chemnitz.de/informatik/ThIS/downloads/publications/sp_mat47_long.pdf

The paper defines \(N_q(m,k,r)\) as the maximum number of columns in an
\(m\)-row matrix over \(GF(q)\), with at most \(r\) nonzero entries in each
column, such that every \(k\) columns are linearly independent.

Relevant reported results include:

\[
N_q(m,k,r)
=
\Omega\!\left(m^{kr/(2(k-1))}\right)
\]

for even \(k\ge2\), matching orders in specified \(k=2^i\)/gcd regimes, and
for \(k=4\), characteristic \(>2\),

\[
N_q(m,4,r)
=
\Theta\!\left(m^{\lceil 4r/3\rceil/2}\right).
\]

### ASET relation

Lefmann forbids every short dependence with arbitrary nonzero coefficients
from \(GF(q)\).

ASET forbids only relations

\[
\sum_i\varepsilon_i a_i=0,
\qquad
\varepsilon_i\in\{-1,0,1\},
\]

with the two independent side bounds

\[
n_+\le d,\qquad n_-\le d.
\]

Therefore:

\[
\text{Lefmann LIN-}2d
\Longrightarrow
\text{ASET}_d.
\]

For \(q=2\), G1A proves equivalence.

For \(q>2\), G1A proves strict finite separation.

**Transfer rule:** Lefmann constructions are valid ASET construction/lower
baselines after the parameter map \(k=2d,r=w\). Lefmann upper bounds do not
automatically upper-bound ASET for \(q>2\).

Novelty effect: **binary STOP / q>2 GAP REMAINS**.

## 2. "k-dissociated" is an overloaded and dangerous term

Primary source:

I. D. Shkredov, *Additive dimension and growth of sets*,
arXiv:2205.07296.

https://arxiv.org/abs/2205.07296

Shkredov defines a set \(\Lambda\) to be \(k\)-dissociated when every
relation

\[
\sum_{\lambda\in\Lambda}\varepsilon_\lambda\lambda=0
\]

with

\[
|\varepsilon_\lambda|\le k
\]

is trivial.

Thus the parameter \(k\) bounds **coefficient magnitude**, not the number of
participating terms.

For \(k=1\), this gives the standard dissociated condition: no nontrivial
\(\{-1,0,1\}\) relation of any order.

### ASET relation

Full dissociation is stronger than bounded-capacity ASET:

\[
\text{dissociated}
\Longrightarrow
\text{ASET}_d
\quad\text{for every finite }d.
\]

But the phrase "\(k\)-dissociated" in this source must not be used as a
synonym for "no signed relation on at most \(k\) terms".

Novelty effect: **definition corrected; bounded-order ASET gap remains**.

## 3. Free, h-free and B_h^*: very close, but not equal to ASET

Primary source:

Jaroslav Nešetřil, Vojtěch Rödl, and Marcelo Sales,
*On Pisier Type Theorems*, Combinatorica (2024).

DOI:
https://doi.org/10.1007/s00493-024-00115-1

The paper uses:

- **free / quasi-independent**: different finite subsets have different
  subset sums;
- **h-free**: the subset-sum inequality is required when one of the two
  index sets has size at most \(h\), while the other side is not restricted
  in the same way;
- \(B_h^*\): uniqueness of sums of \(h\) distinct elements.

### Relation map

In the same ambient additive structure:

\[
\text{free}
\Longrightarrow
\text{h-free}
\Longrightarrow
\text{ASET}_h.
\]

The second implication holds because ASET only asks that **both** colliding
sets have size at most \(h\).

Also,

\[
\text{ASET}_d
\Longrightarrow
B_h^*
\quad\text{for every }h\le d,
\]

because equal-cardinality distinct-summand collisions are a subset of the
collisions excluded by ASET.

The converses are not automatic:

- \(B_h^*\) only controls one fixed cardinality;
- it does not by itself control singleton-vs-pair or other
  cross-cardinality collisions;
- h-free is stronger because the opposite side may be arbitrarily large.

The cited paper is formulated over integers/additive settings, not as the
bounded-support finite-field extremal problem.

Novelty effect: **strong conceptual neighbor; no equivalence; GAP REMAINS**.

## 4. Classical and weak B_h conventions

Primary source:

Imre Z. Ruzsa-related direction represented here by
Gergely Kiss and Csaba Sándor,
*Generalized Sidon sets of perfect powers*,
arXiv:2006.02783.

https://arxiv.org/abs/2006.02783

The paper explicitly distinguishes representation functions for:

- \(h\) **distinct** terms;
- \(h\) nondecreasing terms, hence repetitions allowed.

This reinforces that "\(B_h\)" cannot be imported into ASET without first
freezing the repeated/distinct-summand convention.

ASET uses distinct universe elements and all cardinalities through \(d\).

Novelty effect: **fixed-cardinality neighbor only**.

## 5. Sidon / 2-cap in F_3^n does not equal ASET d=2

Primary source:

Yixuan Huang, Michael Tait, Robert Won,
*Sidon sets and 2-caps in \(\mathbb F_3^n\)*,
arXiv:1809.05117, Involve 12 (2019), 995–1003.

https://arxiv.org/abs/1809.05117

DOI:
https://doi.org/10.2140/involve.2019.12.995

The paper identifies 2-caps in \(\mathbb F_3^n\) with Sidon sets and obtains,
for even \(n\), maximum size \(3^{n/2}\).

Its Sidon condition also excludes repeated-summand equations such as

\[
a+a=b+c,
\]

not only four-distinct-element pair collisions.

### ASET relation

ASET is based on subsets, so the same universe element cannot be selected
twice in one source set.

ASET \(d=2\) additionally requires uniqueness across cardinalities
\(0,1,2\).

Consequently the standard Sidon condition used here and ASET \(d=2\) are
not definitionally equal.

A particularly important characteristic-three phenomenon is

\[
a+b+c=0
\iff
a+b=c+c.
\]

Thus a three-positive relation can violate this Sidon condition while still
being legal under ASET \(d=2\) if there is no collision with both sides of
size at most two. G1A found such examples exactly.

Therefore the \(3^{n/2}\) Sidon maximum is **not automatically an ASET
upper bound**.

Novelty effect: **q=3 remains open after standard Sidon comparison**.

## 6. Constant-weight B_2 sequences: bounded-weight prior art exists

Primary source:

Jin Sima, Yun-Han Li, Ilan Shomorony, Olgica Milenkovic,
*On Constant-Weight Binary \(B_2\)-Sequences*,
arXiv:2303.12990.

https://arxiv.org/abs/2303.12990

A binary \(B_2\)-sequence in this paper is a collection of binary strings
whose **real-valued sums of all distinct pairs** are distinct.

The paper additionally imposes constant Hamming weight \(\omega\) and gives
entropy-style upper bounds and constructive lower bounds. Its main asymptotic
regime has \(\omega\) scaling linearly with the vector length.

### ASET relation

This is the first verified source in G1B showing that a
**Hamming-weight-constrained additive uniqueness problem is already a
developed research object**.

It still differs from ASET:

- ordinary/real addition versus \(GF(q)\) addition;
- exactly two distinct summands versus all subset sizes through \(d\);
- no ASET cross-cardinality condition;
- constant exact weight versus ASET weight at most \(w\);
- the main asymptotic weight regime differs from fixed \(w\).

For binary columns, a modular ASET collision-free family is also
ordinary-integer pair-sum collision-free, because equality over the integers
would imply equality modulo two. Thus compatible upper bounds for the
integer \(B_2\) super-class can be necessary ASET bounds when parameter
regimes match.

Constructions do not transfer in the reverse direction automatically.

Novelty effect: **bounded-support/weight territory is not untouched; exact
ASET regime still unresolved**.

## 7. Signature and detecting codes

### 7.1 q-ary signature codes over integer addition

Primary source:

Gökberk Erdoğan, Georg Maringer, Nikita Polyanskii,
*Signature Codes for a Noisy Adder Multiple Access Channel*,
arXiv:2206.10735.

https://arxiv.org/abs/2206.10735

The q-ary signature-code model requires that a subset of codewords be
recoverable from the coordinatewise sum **over the integers**.

This is all-subset ordinary-sum uniqueness, not finite-field modular ASET.

### 7.2 constant-weight t-signature codes

Primary source:

Jinping Fan, Yujie Gu, Masahiro Hachimori, Ying Miao,
*Signature codes for weighted binary adder channel and multimedia
fingerprinting*, IEEE TIT 67 (2021).

arXiv:
https://arxiv.org/abs/1905.10180

DOI:
https://doi.org/10.1109/TIT.2020.3033445

The paper defines extremal quantities for \(t\)-signature codes and for
constant-weight \(t\)-signature codes, derives upper bounds, and for some
\(t=2\), low-weight regimes determines exact values.

This is a major prior-art warning: "signature code + constant weight" is a
real extremal literature.

The weighted binary adder-channel identification property is nevertheless
not the same as ASET's finite-field modular subset-sum property.

### 7.3 classical sum-distinct / detecting vectors

Primary sources:

- Bernt Lindström, *On a Combinatorial Problem in Number Theory*,
  Canadian Mathematical Bulletin (1965),
  DOI https://doi.org/10.4153/CMB-1965-034-2
- Sanja Jevtić, *On Families of Sets of Integral Vectors Whose
  Representatives form Sum-Distinct Sets*, SIAM J. Discrete Math. (1995),
  DOI https://doi.org/10.1137/S0895480194265623

These belong to the older detecting/sum-distinct integer-vector line.
The special case \(\{0,x_i\}\) is all-subset ordinary-sum uniqueness.

Novelty effect: **new mandatory G1B source cluster; arithmetic mismatch
prevents automatic reduction to modular ASET**.

## 8. Additive / quantitative group testing

Primary source:

Fei-Huang Chang, Hong-Bin Chen, Jun-Yi Guo, Yu-Pei Huang,
*Multi-Group Testing for Items with Real-Valued Status under Standard
Arithmetic*, IEEE TIT 61(2), 2015.

arXiv:
https://arxiv.org/abs/1303.6020

DOI:
https://doi.org/10.1109/TIT.2014.2384012

The paper defines an additive \((D,d)\)-separable matrix by requiring
different \(d\)-sparse input vectors from \(D^n\) to produce different
measurement vectors under **standard arithmetic**.

For \(D=\{0,1\}\), this is the ordinary-arithmetic analogue of injectivity on
sets of size at most \(d\).

### Relation to modular ASET

Fix integer representatives of the matrix entries.

If two source sets have the same ordinary integer measurement, then they
also have the same measurement modulo \(q\).

Therefore:

\[
\text{mod-}q\ \text{ASET}_d
\Longrightarrow
\text{standard-arithmetic additive separability}_d
\]

for the same measurement matrix/input domain.

Hence a compatible upper bound for standard-arithmetic separability can be
a necessary ASET upper bound.

The reverse implication is false in general because two unequal integer
sums can become equal modulo \(q\).

The Chang et al. paper focuses on q-ary additive disjunct constructions and
decoding under standard arithmetic; it does not, by itself, close the
support-\(w\) modular ASET extremal problem.

Novelty effect: **direct comparator; quantitative/additive group testing
must be a mandatory G1B cluster**.

## 9. Provisional effect on G1B

This audit changes the novelty map in two directions.

### The ASET lane remains alive

No verified source in this tranche simultaneously matches:

1. finite-field/modular addition;
2. distinct subset elements;
3. all subset sizes through \(d\);
4. both collision sides bounded by \(d\);
5. per-generator Hamming support at most \(w\).

### But the neighborhood is much denser than the initial map suggested

In particular, existing literature already covers significant subsets of
the design space:

- arbitrary-coefficient sparse linear independence;
- all-order signed independence;
- h-free and \(B_h^*\) uniqueness;
- finite-field Sidon/2-cap systems;
- constant-weight \(B_2\) sequences;
- constant-weight signature codes;
- sum-distinct/detecting vectors;
- additive \(d\)-sparse standard-arithmetic group testing.

Therefore **CONTINUE_ASET is not yet authorized**.

## 10. Required audit 02

Before G1B can decide, the next tranche must search specifically for:

1. finite-field or modulo-\(q\) **bounded-active-user signature codes**;
2. quantitative/additive group-testing matrices with explicit bounded
   column weight;
3. bounded-support q-ary Sidon/\(B_h\)/dissociated families inside Hamming
   balls;
4. "two-sided h-free" or equivalent relations with both
   \(n_+,n_-\le d\);
5. q=3 distinct-summand variants that omit the repeated-summand Sidon
   restriction;
6. characteristic-two \(q>2\) behavior.

Until those are closed:

**G1B STATUS = OPEN.**
