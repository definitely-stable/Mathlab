# HYP-105 / #230 — AA4-DISJOINT5: direct all-51 signed R3 by six-distinct ORIGINAL-source 2+3 GF(5) incidences

**Research slice:** an entirely different exact FULL R3
one-original-source-variable oracle, without the D3−(N−4)D2
inclusion-exclusion identity, plus a new genuine W34 bounded
continuation from the frozen complete #715 425-ORIGINAL-source
GF(5) certificates. Scientific Draft stacked strictly on
[#715](https://github.com/definitely-stable/Mathlab/pull/715),
frozen parent SHA `d40428a720c3269774c02fa207448d9d08ee983e`.
No parent, main or PR root modification or merge.

## 1. Mathematical problem: direct TRUE original signed R3

Each true ORIGINAL incident source flag ID i of symplectic
W(3,s) has a globally reused, fixed physical GF(5)^m
column c_i. Its physical support S_i consists of
exactly four source coordinates:
two separately injected point-pair coordinates f(p),
two separately injected line-pair coordinates g(ell).
Every legal palette is one of 51 all-nonzero,
checksum-4 GF(5)^4 patterns, reused for the same
ORIGINAL flag everywhere in the full configuration.

Fix a source flag ID i, all other source palettes,
both source factor maps f,g, and all true ORIGINAL
point-line incidences.

Define the integer H_i(t) to be the number of pairs
(P,T) such that P is a set of TWO other distinct
ORIGINAL flag IDs, T is a set of THREE other
distinct ORIGINAL IDs, **P and T are DISJOINT**,
and

\[
  c_i(t) + \sum_{j\in P} c_j
       = \sum_{k\in T}c_k
       \qquad\text{in the complete physical }GF(5)^m.
\]

## 2. NEW all-N exact signed-source incidence theorem

**Theorem.** Let R3(t) denote the number of
all balanced signed 3-positive/3-negative events on
SIX DISTICT ORIGINAL source IDs under fixed
global coefficient assignment except at source
flag i with legal palette t. Then for any two legal
palettes t,u,

\[
\boxed{R_3(t)-R_3(u)=H_i(t)-H_i(u).}
\]

**Proof:** Partition ALL true six-DISTINCT-original-ID
balanced signed 3+3 events into those whose six source
IDs do not contain i and those whose six IDs contain i.
The first subset is unaffected when changing the column
c_i. For any event containing i, the balanced sign
partition is identified up to global sign reversal.
There is a UNIQUE choice of its overall sign so that i
is positive; the other two positive ORIGINAL IDs
define the two-source subset P, and the three negative
ORIGINAL IDs define the three-source subset T.
All six sources are distinct precisely because
P and T are disjoint and each avoids i.
The signed six-column cancellation equation is
exactly c_i+sum(P)=sum(T). This construction is
bijective with H_i's pairs. Hence H_i(t) counts
precisely all true R3 events containing the
flag i; the other events remain invariant.
Subtracting proves the formula for ALL N,
all real or abstract fixed source incidence geometries
and all m; there is NO reference to D2,
D3, expectation, graph topology, source
degree-two classes or any heuristic independence. QED.

**Additional necessary-condition theorem:** if a
real ORIGINAL source flag i participates in
ZERO currently existing true R3 events,
then H_i(current)=0 and H_i(t)≥0 for
EVERY legal t. Thus modifying this one
source flag cannot STRICTLY DECREASE
the full R3. Hence the union of the
source IDs in ALL actual current true
R3 witnesses contains EVERY source
that could make a strictly-improving
one-source-coefficient move. This
pruning is rigorous; ranking only
the highest-degree 4 flags out of
that union is STILL a bounded heuristic
and must not be called a global
single-source local-optimality proof.

## 3. NEW direct 51-way GF(5) projected six-source algorithm

Since c_i(t) is supported only in
its fixed four physical source
coordinates S_i, it vanishes
in the other m-4 physical coordinates.
For actual W(3,4), m=28, and
this gives a complete exact split
into 24 outside coordinates
and four inside coordinates.

The six-DISTINCT-source signed
equation above can hold only when

\[
outside_i(\sum_{P} c_j)
   =outside_i(\sum_{T}c_j).
\]

In that case the four inside GF5
coordinates uniquely force

\[
 t=inside_i(\sum_{T}c_j)
    -inside_i(\sum_{P}c_j)
    \pmod5.
\]

Enumerate ALL `C(N-1,2)` actual
other-ORIGINAL-source two-subsets
P, group them by their COMPLETE
GF5^(m-4) outside projection, and
retain the **ACTUAL TWO SOURCE IDs**
for each P. This is the crucial
difference from the old raw D3
algorithm that stored only
sum multiplicities.

For EVERY actual
`C(N-1,3)` original source
three-subset T, calculate its
complete outside projection
and look up ALL equal-outside
source pairs P. **Discard every
P with P∩T≠∅ before computing
the source palette or charging
an event.** These intersection
cases are the R2-generated
shadow events that had confused
the old D3-only optimisation.
For disjoint P,T only, calculate
the legal source palette t
forced by the four original
inside GF5 digits and increment
the corresponding entry in a
51-element TRUE R3 incidence
histogram. A forced tuple outside
the real 51 all-nonzero checksum4
patterns is rejected.

Thus one full 12,614,424-triple
pass and 89,676 pair index for
W34 gives the ENTIRE 51-entry
**direct H_i(t) true R3
collision incidence** without
ever computing D2/D3. It is
physically GF5-exact, source-disjoint,
fully source-preserving and
has NO probabilistic hashes,
sampling or inferred independence.

Use #715's independently tested
51-entry source-local R2 derivative
ONLY as a guardrail, not to
derive the direct R3 change:
require R2(t)≤current R2.
For every candidate t, the
predicted full true R3 is
`current_R3 + H_i(t)-H_i(current)`,
and predicted source R2
is its independently calculated
source-local R2 value.
Pick the best candidate
subject to strict true R3
decrease and R2 nonincrease.

## 4. Independent mathematical falsification

For two actual W32 original
source IDs under the original
frozen global source palettes,
the new 51-entry source-disjoint
histogram must match **51 FRESH**
complete exact source 45-flag
full six-distinct-ID 3+3 GF5
collisions, for EACH source ID.
The independent small-source
referee uses the earlier
complete 14,190 original
triple-sum hash to compute
all true signed events for every
candidate. Further, every one
of those 102 new true source
candidate deltas must agree
with #715's mathematically
DIFFERENT GF5
`ΔD3-41ΔD2` oracle.
Thus this is a genuinely
independent two-way
verification of the new
direct signed-event method,
not merely an algebraic
self-consistency test.

A second W32 test proves the
source-local pruning rule on
an actual original source ID
that is absent from all
currently occurring true
3+3 signed events; no
single new palette can
make an absent current
collision disappear.

For W34 the starting
complete 425-source arrays
are the exact frozen #715
certificates:
`lex:(D2,D3,R3)=(1,497,76)`;
`reverse-line:(0,83,83)`.
Every source palette preserves
the same four-coordinate physical
support, source ID and original
point/line incidence factors.

## 5. A bounded next finite W34 experiment

At EACH round, first run
the independent earlier
external disk-based exact
12,704,100-triple full
original GF5 source referee,
requesting at least 256
actual six-original-ID
witnesses and proving that
the returned witnesses are
ALL R3 signed events.
Rank original source IDs
by real participation counts
in current true R3 witnesses.
Evaluate up to FOUR highest-degree
real source IDs using the new
direct source-disjoint
51-palette algorithm and
an independent exact R2
guardrail. Pick the strict
best legal true-R3 decrease,
making at most THREE
one-ORIGINAL-source coefficient
edits.

After EACH accepted edit,
run the ENTIRE independent
original 12,704,100-triple
GF5^28 external referee again.
Its measured exact true
signed R3, exact R2 and
all-D3 count MUST equal
the values predicted by
the new direct-disjoint
R3 derivative and
independent all-N R2/R3
identity. On any discrepancy,
FAIL CLOSED rather than
claim improvement.

The output logs and
permanent source certificate
contain all 425 original
source-ID ordered palette
indices, the exact 51
direct signed-event deltas
for every accepted edit,
the true original source
IDs changed, source rank
data and the external
full-source evidence.
The finite case may
make no further improvement;
that does NOT prove global
no-zero existence.

## 6. Limits

This is a verified mathematical
algorithm for finite original
signed R3 under fixed global
source f,g. Even finite W34
zero signed risk would not
imply a uniform all-h
positive ASET exponent,
nor refute the accepted
large-s expectation lower
bound in root #230.
Root issue remains
`OPEN_WITH_FORMAL_BLOCKER`;
no PR merges.
