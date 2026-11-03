# HYP-105 / issue #230 — AA4-W34-R3DERIV: exact source-local direct FULL signed R3 derivative for ALL 51 legal GF(5) palettes

**Scientific milestone:** direct original-six-DISTINCT-ID GF5 signed R3 optimisation on genuine full W(3,4), with globally fixed ORIGINAL incidence flags, fixed separately pair-injective physical maps f,g and real source-wide 51-checksum4 nonzero GF5 coefficient templates.

Strict scientific Draft child stacked on #714 frozen exact HEAD
`1494c9ff320bc3b169ffe97843ee3b0fbdd93302`.
No parent/main mutations, merges, scientific result-promotions without CI or closure of #230.

## 1. Why optimizing D3 alone demonstrably fails

Previous #714 proved exact 24+4 original source local projection, and verified in COMPLETE W34 full R3 rehashes that its R2-first local D3 descent
produced:

| Source | D2 after #714 | D3 after #714 | TRUE original six-ID R3 after #714 |
|---|---:|---:|---:|
| lex | 1 | 507 | **86** |
| reverse-line | 0 | 96 | **96** |

The score D3 mixes true six-distinct ORIGINAL flag 3v3 events
with equal triple-sum pairs that share one ORIGINAL flag.
The independently proved all-N exact identity for any N
DISTINCT physical source columns is

\[
 D_3 = R_3^{det}+(N-4)D_2.
\]

For W34, N=425 and N-4=421. Both previous improvements removed
ONLY the 421-fold shadows of 2v2 source collisions. The mathematical
goal is therefore MINIMIZE TRUE R3 DIRECTLY, subject to nonincrease
of genuine source R2, instead of optimizing D3 as a surrogate.

## 2. NEW all-N exact 51-candidate R2 projection lemma

Fix one ORIGINAL source ID i with physical support of exactly four
GF5 coordinates S_i. All other source palettes and all physical
point/line pair maps f,g remain unchanged.

Consider equal two-subset sums, i.e. pairs of ORIGINAL pairs.
Split 2-subsets into U (do NOT contain i) and A_i (DO contain i).
The number of equal-sum pairs within U/U is invariant under
changing source palette c_i; within A_i/A_i the common
c_i cancels, and for two DISTINCT ORIGINAL source IDs j≠k
the equality `c_i+c_j=c_i+c_k` would force `c_j=c_k`,
impossible because true physical source columns are distinct.
Thus the ONLY palette-dependent contribution to FULL D2 is
from U/A_i cross-equality.

For each other original pair P={a,b}, each other original
single source j, both avoiding i, require

\[
c_i+c_j=c_a+c_b.
\]

Decompose original physical coordinates into
`outside_i` (all m-4 coordinates not in S_i) and
`inside_i` (exactly the four true support coordinates).
Because c_i is identically ZERO outside S_i, the equality
can hold only if

\[
outside_i(c_j)=outside_i(c_a+c_b),
\]

in which case the full four-coordinate palette is
uniquely FORCED to be

\[
c_i|_{S_i} =inside_i(c_a+c_b)-inside_i(c_j)
            \pmod 5.
\]

This forced pattern is either one of the 51 legal
all-nonzero checksum4 GF5 patterns, or the equality
is impossible under any legal candidate. All 51 source
palette cross-collision counts are therefore computable
EXACTLY with one indexed lookup of the N-1 real
ORIGINAL singleton sums and one pass over C(N-1,2)
other-original pair sums, with physical complete
24-dimensional outside keys. No truncated hashes,
independence assumptions, fabricated columns,
or 51 full D2 scans.

For true W(3,4) there are exactly **424 real
other-source singles** and **89,676 real
other-source pairs**. The exact 625×625
GF5 four-digit difference table determines
the unique original legal palette for each
matched outside projection.

## 3. NEW exact direct ORIGINAL R3 51-way derivative theorem

#714's preceding original source-local
24D pair/triple projection computes EXACTLY
\(\Delta D_3(t)\) for every legal candidate
t with one full **12,614,424**
other-source triple pass and an index of
all 89,676 other-source original pair sums.

This PR computes **both**
\(\Delta D_2(t)\) and
\(\Delta D_3(t)\) exactly on the SAME
real globally fixed physical source assignment.
For every one of 51 candidates, because
the all-N identity holds before and after
the source change, subtraction proves

\[
\boxed{
\Delta R_3^{det}(t)
=\Delta D_3(t)-(N-4)\Delta D_2(t).
}
\]

This is NOT a derived expectation or leading-family proxy.
It is the EXACT change in the number of all actual
3-positive/3-negative collisions on six
DISTINCT ORIGINAL source flag IDs, regardless
of physical coordinate multiplicity.

The referee records all 51 candidates'
signed R3, D2 and D3 exact predicted absolute
costs and chooses lexicographically first
candidate minimizing TRUE R3 among candidates
with **D2 nonincrease**. It accepts a source
change ONLY on STRICT TRUE R3 reduction.
A legitimate D3 increase can be accepted
if it reduces six-distinct-ID signed R3
without increasing R2, because D3 is not
the target of this slice.

**Non-negativity safeguard:** a candidate
with predicted negative D2, D3, or R3
means the algebraic derivative or true
source membership is wrong and is rejected
as an assertion failure. The unchanged
palette candidate must reproduce the
trusted exact initial D2,D3,R3.

## 4. Source hotspot selection and independent acceptance

Start from the ACTUAL immutable #714
static 425-flag repaired source arrays:
lex `(D2,D3,R3)=(1,507,86)` and
reverse-line `(0,96,96)`.
Never alter the original f,g or geometry,
never independently resample a shared source palette.

For EACH round, FIRST execute a COMPLETE
independent 12,704,100-original-triple
GF5^28 external radix census (#713) with
at least 256 physical witness capacity,
enough to enumerate all current 86/96
actual six-original-ID signed events.
Reject the model if fewer than EXACTLY
R3 different true event witnesses are
recovered; this is a COMPLETE hotspot
inventory, not a tiny biased sample
from the first eight historical examples.

Rank every actual ORIGINAL source flag
by its participation degree in these
independently discovered six-distinct
signed R3 witnesses. Evaluate the
highest-degree at most four source IDs,
computing the EXACT full 51-entry
\(\Delta D_2,\Delta D_3,\Delta R_3\)
vectors for EACH original source ID.
Choose the candidate with greatest strict
true-R3 decrease, explicitly guard
D2 nonincrease, and modify its ONE
immutable original source-ID palette.

After **EACH accepted edit**, not just
the final edit, run an ENTIRE NEW
independent W34 12,704,100-triple
GF5 external radix census, check all
true original one/two/three-sums,
the full 28D physical equation witnesses,
source-disjointness IE, and the
all-N exact independent R2 overlap formula.
Verify its measured D2,D3,R3 equal
the 51-way derivative predictions
**exactly**, or FAIL CLOSED and
reject any claimed improvement.

The bounded two-round / four-hotspot
search is a reproducible finite experiment,
NOT a global optimum proof. A run may
find no improving original source ID
among the tested true-R3 hotspots even
when a different single edit or a
multi-source edit can help.

## 5. Independent mathematical test obligations

**Strong small-source independent oracle:**
for two TRUE ORIGINAL W32 source IDs,
the 51-way predicted D2,D3 and TRUE
six-distinct-original-ID R3 are compared
against 51 SEPARATE, FRESH full
45-source vector construction and full
990-two-source and 14,190-three-source
GF5 physical sum enumerations, with
NO dependence on new projection
derivative code for the expected result.

Other tests independently reconstruct
the ACTUAL #714 W34 real 425-flag
repaired source assignments and genuine
full D2/R3 baselines, check multiple
single-source changes by
fully re-enumerating all 90,100
actual original two-source sums, and
enforce fail-closed source/budget/negative
risk guards.

Hosted CI runs these reference tests
and both independent real W34
lex/reverse-line exact bounded direct-R3
source optimisation experiments on
GitHub-hosted ubuntu-24.04. Successful
full source HEAD runs are saved as
per-branch permanent JSON coefficient
certificates with all 425 exact source
palette indices, unchanged original
f,g, candidate costs, actual local
changes and independent full 12.7m
physical GF5 audit proof provenance.

## 6. Limits, blockers and next allowed mathematics

A strict finite R3 improvement is
valuable, but it does NOT by itself
create a full 425-column GF5 ASET;
for that we also require D2=0 and
R3=0 simultaneously with the
constant nonzero checksum4
cardinality barrier.

No finite W34 result proves
an ALL-h construction, a positive
asymptotic ASET exponent gain,
or refutes the accepted Branch A
large-s positive EXPECTED signed
GF5 R3 lower bound at fixed f,g.

Root issue #230 remains
`OPEN_WITH_FORMAL_BLOCKER`
until its actual universal formal
acceptance is proved. No merge
or promotion of hypotheses.
