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

## 3A. NEW universal exact R2-to-R3 overlap identity

The first full source W34 hosted census produced a surprising precise
consistency check: of all equal-GF5 triple-sum pairs, exactly `1263`
(lex) and `421` (reverse-line) share an original source ID.
This is NOT an arbitrary empirical coincidence.

**New all-N identity:** provided all ORIGINAL weighted source columns
`c_i` are DISTINCT, let `D_2` be the number of distinct unordered
pairs of two-source subsets whose exact GF5 vector sums agree,
and let `D_3` be the number of distinct unordered pairs of
three-source subsets whose exact GF5 vector sums agree.
Let `R_3^{det}` be the number of unordered signed 3+3
collisions on six DISTINCT ORIGINAL source IDs, counted with
all ten balanced partitions. Then

\[
\boxed{D_3=R_3^{det}+(N-4)D_2.}
\]

**Proof.** Partition equal-sum pairs of distinct ORIGINAL
triples by the cardinality of their intersection.
With ZERO common source IDs, the equality is exactly
one genuine six-distinct-source-ID 3+3 signed event.
With ONE shared flag ID i, cancel the same c_i
on both sides. This is exactly one pair of DISJOINT
original two-source subsets A,B of the other four
IDs with equal sums, plus a choice of shared
source flag i among the remaining N-4 original IDs.
Every such pair of original 2-subsets can be lifted
in EXACTLY N-4 ways; no double count because the
intersection singleton i is uniquely identified.
With TWO shared original IDs, cancellation would
force two DIFFERENT remaining original columns
to have equal full GF5 vectors, impossible because
all columns are distinct. Intersection size THREE
would make the two triples IDENTICAL and is excluded
from D3. This is a bijective classification. QED.

Any pair of distinct original 2-subsets with
equal sums and ONE shared source ID likewise
forces two original columns equal, which is
impossible; therefore D2 itself consists
precisely of genuine original 2+2 signed
events for this true globally injected model.

This second theorem provides an **independent
exact cross-check** on the external bucket
triple intersection IE: the code counts D2
via an entirely separate original two-subset
sum table, and asserts the identity for
every complete W32 and W34 source audit.
It is also computationally useful: if one
has exact D2 and D3, no source-triple
pairwise intersection analysis is needed
to obtain the true six-distinct-ID R3.

## 3B. Actual completed exhaustive W(3,4) ORIGINAL results

GitHub-hosted dedicated [run #41603089629](https://github.com/definitely-stable/Mathlab/actions/runs/41603089629),
on the same exact frozen source SHA `050d5e9f4f0dfabb439a953e7aa90069fe39b8d6`,
completed SUCCESS on two separate Ubuntu-24.04
full 425-source workers plus one independent
W32/W34 validation worker.

For both true W34 fixed `f,g` schemes the source
palette `omega_i` was deterministically
assigned ONCE per original flag ID from the
domain-separated SHA256 seed **0**. The exact
FULL **12,704,100** original triple sums and
all 1/2 source subset sums were processed
without a missing-source or partial-coverage
exception.

| Observed exact ORIGINAL statistic | W34 lex | W34 reverse-line |
|---|---:|---:|
| True ORIGINAL source flags | 425 | 425 |
| Source GF5 physical coordinates | 28 | 28 |
| All original GF5 triple sums processed | 12,704,100 | 12,704,100 |
| Distinct complete triple-sum signatures | 12,702,751 | 12,703,583 |
| **D2: equal two-subset sum pairs** | **3** | **1** |
| D3: equal three-subset sum pairs | 1,349 | 517 |
| Of D3: pairs sharing at least one source ID | 1,263 | 421 |
| **Full six-distinct-original-flag 3+3 events** | **86** | **96** |
| Is seed0 a full 0..3 GF5 ASET? | **No** | **No** |
| Exact disk records written (bytes) | 152,449,200 | 152,449,200 |
| Peak one sorted bucket payload (bytes) | 605,208 | 605,040 |

The independently derived all-N identity matches both
full-source runs EXACTLY, since N-4=421:

\[
 1349=86+421\cdot3,\qquad
 517=96+421\cdot1.
\]

Thus the **86/96 positive full R3 findings**
are NOT 1349/517 events counted
with source intersections; the latter are
unqualified equal-triple-sum pair counts.
The original ID overlap correction is
essential and was checked using BOTH
the new linear-time source-incidence
intersection formula and the independent
full original R2-based identity.

**Permanent source-controlled exact evidence:**
`research/hyp105_w34_full_425flag_r3_seed0_certificates.json`
stores the full hosted output for both
W34 schemes, exact source counts, R2/R3
values, actual peak bucket size and
**eight distinct-source-ID signed 28D physical
witnesses per scheme**. A second set of tests
loads these STATIC records, regenerates
the unchanged original f,g and the exact
seed0 GF5 source palette for all 425 IDs,
and independently verifies every one of
these sixteen witness equations using
the full 28 physical coordinates and the
real point/line source flags.

**Scope of this negative result:** positive
R2/R3 for THESE TWO fixed seed0 assignments
does NOT prove that no alternate coefficient
assignment (possibly via exact local repair)
can make the full 425-source ASET valid.
It does not contradict the previous finite
45-column zero examples, the older G5-D
constructive source, nor large-s Branch A's
lower bound on EXPECTED random signed R3.
There is no mathematically valid new
asymptotic exponent claim here.

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
