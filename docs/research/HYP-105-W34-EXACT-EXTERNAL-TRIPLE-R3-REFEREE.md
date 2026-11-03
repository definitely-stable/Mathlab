# HYP-105 / #230 — AA4-W34EX: exact memory-budgeted full ORIGINAL GF(5) three-sum census on genuine W(3,4)

**Scientific next step:** independently audit full (R_3) on ALL 425
REAL ORIGINAL incidence-flag IDs of symplectic W(3,4), on
separately globally pair-injective fixed pair-coordinate maps
(f,g). No synthetic six-source IDs, re-labelling between tests,
assumed independence of overlapping collisions, or extrapolation
from W32's 45-column finite zero examples.

This Draft is STRICTLY stacked on frozen #712 HEAD
`e8cc133e2aeaf9ba21e6caf6a9194b3a8437dfc0`,
and never mutates parent/main or merges without approval.

## 1. Important correction about the size of the real research problem

For true W(3,4),
\[
 V=(4+1)(4^2+1)=85,\quad N=V(4+1)=425,\quad
 a=\min\{r:\binom r2\ge85\}=14,\quad m=2a=28.
\]

Each actual ORIGINAL flag `i=(p,ell)` has exactly one physical
support of four coordinates: the two sorted coordinates of f(p)
and the two sorted coordinates of g(ell), offset by 14. Source
columns are pairwise distinct because both factor maps are
globally pair-injective and the original incidence flags are distinct.
One legal checksum-4 GF5 coefficient palette from the exact
51-member nonzero palette is assigned to each ORIGINAL flag,
independently of whether it appears in many signed events.

There are exactly

- `C(425,1)=425` one-source sums;
- `C(425,2)=90,100` two-source sums;
- `C(425,3)=12,704,100` three-source sums.

An exhaustive direct sixset-sign scan would require
`C(425,6)*10` checks; that is unnecessary. Equal complete
GF5 three-sums count ALL balanced signed 3-vs-3 collisions,
regardless of coordinate multiplicity profile. This is the
exact theorem established on smaller W32 in #712.

## 2. NEW bounded-memory *lossless* exact external original-GF5 oracle

A vector in GF(5)^28 has a UNIQUE radix-five encoding
`S(c)=sum_{j=0}^{27} c_j 5^j`, with

`0<=S(c)<5^28=37,252,902,984,619,140,625<2^66`.

For three ORIGINAL source columns, sum the 28 components
separately modulo five, NEVER by ordinary integer addition
on base-five packed codes (which would introduce carries).
An independent reference encoder computes the sum from
physical coordinates and checks it against a new high-throughput
four-GF5-digit table:

- Represent each column as 7 groups of 4 actual GF5 digits,
  each group in `0..624`.
- Precompute all `625*625=390625` exact GF5^4 additions;
  each of the **12,704,100** triple sums then uses seven
  table lookups after reusing its original first-two-flag sum.
- The full 28-digit result is encoded in BASE 625 and
  retains the exact 66-bit original signed checksum
  signature. Neither digit information nor original
  column identity is discarded.

The canonical distinct source triple `0<=i<j<k<425` is
encoded as `(i*425+j)*425+k <425^3<2^27`. Thus combine
the exact GF5 signature S and source triple code U into

`record = (S<<27)|U`, which occupies **at most 93 bits**,
and is stored in EXACTLY **12 bytes**. No floating point,
modular fingerprint, 64-bit truncated hash, Bloom filter,
or probabilistic missed-collision assumption is used.

Partition all records into 256 deterministic external files
by a fixed XOR-folded function `bucket(S)`. This function
is not used for equality; **the full exact signature remains
present in every 12-byte record**. Crucial injectivity
invariant: if `S(T)=S(U)`, then
`bucket(S(T))=bucket(S(U))` and the two original triple
records MUST lie in the same file. Sorting each file's
complete exact records therefore finds EVERY equality.
The runtime rejects a bucket exceeding its explicitly
configured memory bound rather than returning a
partial census as though it were complete.

External spool size for full genuine W34:

`12,704,100 * 12 = 152,449,200 bytes`.

Peak sorted in-memory record count and actual bytes,
total processed source triples, total distinct exact
GF5^28 signatures and all pair counts are reported.
This is an explicit memory-controlled CI algorithm
on GitHub-hosted ubuntu-24.04 with NO user PC required.

## 3. NEW all-N exact O(k) signed-event intersection lemma

A group of `k` distinct ORIGINAL three-ID subsets with
the SAME GF5 sum contributes `C(k,2)` unordered
equal-three-sum pairs. Only those pairs with SIX DISTINCT
ORIGINAL source IDs contribute full signed R3.
A pair of distinct triples can share either ONE or TWO
source IDs (sharing all three would make them the same
triple, impossible in the canonical enumerator).

For each ORIGINAL flag ID i, let `d_i` be the number
of triples in this exact sum group containing i.
For each unordered pair (i,j), let `d_ij` be the
number of triples containing BOTH i,j. Apply
inclusion-exclusion over whether the two triples
share at least one original source ID:

\[
\boxed{
 R_{3,\text{group}}
 =\binom{k}{2}
  -\sum_i\binom{d_i}{2}
  +\sum_{i<j}\binom{d_{ij}}{2}.
}
\]

**Proof:** a pair sharing exactly one source ID is
subtracted once in the single-ID sum; a pair
sharing exactly two source IDs is subtracted twice,
then added back once in the pair-ID correction.
No pair shares three IDs. Every disjoint pair is
left untouched. The formula counts precisely all
unoriented balanced GF5 3+3 events in this group.
It is exact for arbitrary original source geometry,
arbitrary sixset overlap, and all h. Complexity is
linear in the number of triples in the group
(up to dictionary costs), rather than `O(k²)`
brute pair comparisons.

The program stores the full original 28-coordinate
GF5 vector sum and the six ORIGINAL source flag
IDs for any emitted collision witness, then
recomputes the entire vector equation independently.
A witness always includes its true source
point/line incidence factors and actual physical
coordinate multiplicity profiles.

## 4. Mathematical scope of the W34 experiment

This slice accepts the **complete legal** geometry and
original fixed maps generated by
`pair_labeled_symplectic(2,"lex")` (and a second
independent `reverse-line` control). The
deterministic source palette fixture is assigned
ONCE per original incidence flag using SHA-256
domain separation of scheme, original flag ID
and nonnegative seed; seed=0 is a control,
not a theorem that every seed has zero R3
nor a probabilistic independence assumption.

The exact source full k<=3 ASET status is
a direct consequence of zero 1/2/3 same-size
subset-sum equalities plus common nonzero
mod-five checksum4 for differing subset
cardinalities 0..3.

Independently verified **W32 regressions**:
- #711 complete seven-leading-class zero witnesses
  have REAL full-R3 signed counts 7 (lex) and
  4 (reverse-line), despite selected-leading zero;
- #712 modified full zero certificates have
  exact full source R3=0 for BOTH maps;
- the NEW 12-byte radix auditor must agree
  precisely with #712's independent historical
  Python-dictionary triple oracle on the same
  actual original source IDs, both for total
  signed events and omitted overlap pairs.

On W34, three separate 10-real-ORIGINAL-ID
subsets are checked against a wholly independent
direct `C(10,6)*10` sixset-sign enumeration
of ALL 28 physical GF5 coordinates, with no
use of the external sum bucket counter.
An algebraic synthetic *intersection formula
unit test* is separate from the REAL source
fixtures and is NEVER used as geometric data.

## 5. What a successful run proves, and what it cannot

After the hosted full-W34 audit actually completes,
the reported count is the exact full weighted
*deterministic signed-event count* for the
specified fixed original f,g and globally
fixed 425-source palette assignment. It is
NOT the **expected** GF5 risk over palettes
used in the all-h Branch A root inequality;
those are different quantities and must
not be mixed. Whether seed0 has zero, many
or no signed events is an empirical exact
finite result: no value should be invented
before the hosted full run is complete.

The research question left open is much harder:
does some ASSIGNMENT avoid full R3 on W34
for the SAME fixed f,g, and can one prove
anything UNIFORMLY in dyadic h? A
single fixed assignment with positive
signed-event count does NOT prove
nonexistence of a zero assignment.
Even a zero finite W34 assignment would
NOT by itself improve ASET exponents.

**Acceptance:** maintain HYP-105 root
`OPEN_WITH_FORMAL_BLOCKER`, no mergers,
and no automatic claim of a new asymptotic
ASET theorem. Frozen ancestors remain
unmodified.
