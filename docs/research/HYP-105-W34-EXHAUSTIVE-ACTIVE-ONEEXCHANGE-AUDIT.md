# HYP-105 / #230 — AA4-ALL1: exhaustive true W34 active-source 51-palette one-exchange audit

**Scientific objective.** Upgrade the bounded top-four-original-source search
in frozen [#716](https://github.com/definitely-stable/Mathlab/pull/716)
to a COMPLETE audit of EVERY ORIGINAL source flag that participates in
the current full six-distinct-ORIGINAL-source signed GF(5) R3
conflict hypergraph, under the same unchanged fixed global f,g
and the hard no-increase-R2 guard. Either identify a proven
strictly better one-original-source move and independently verify
its full GF(5) physical source risk, OR if NO source improves
prove a finite **guarded 1-exchange local optimum** for that one
fixed 425-source-coefficient assignment. Do NOT confuse it with
a global optimum, an absence of multi-source moves or a uniform
all-h asymptotic theorem.

Strictly stacked on frozen #716 HEAD
`b2d848270980585904fe7c00676dc70bcf7001be`.
No main or parent changes, no merges, root #230 unchanged
`OPEN_WITH_FORMAL_BLOCKER`.

## 1. Exact all-N reduction of one-source strict improvement domain

Let the complete source original signed-event set
`E(omega)` contain ALL unordered balanced 3+3 cancellations
on SIX DISTINCT ORIGINAL incidence flag IDs for the fixed
full physical GF5^28 assignment omega.

For one ORIGINAL source flag i and legal pattern t,
define
\[
H_i(t)=\#\{(P,T):
|P|=2,\ |T|=3,\ P\cap T=\varnothing,\
i\notin P\cup T,\
c_i(t)+\sum_{j\in P}c_j=\sum_{k\in T}c_k\}.
\]

The previous rigorously proved direct-disjoint original-source
theorem identifies every current true signed 3+3 cancellation
involving i with exactly one term of H_i(current), by
choosing the unique global sign making i positive.
Hence, for any two legal source patterns u,t,

\[
\boxed{R_3(t)-R_3(u)=H_i(t)-H_i(u).}
\]

If i is ABSENT from every actual current event, then
`H_i(current)=0` and all nonnegative integer H_i(t)
are >=0. Consequently **no one-original-source edit
at an absent source flag can STRICTLY reduce TRUE R3**.
This prunes some source IDs mathematically, not heuristically.

Let
\[
A=\bigcup_{e\in E(omega)}e
\]
be the set of active actual ORIGINAL source IDs. To
verify every strict one-source improvement with R2
nonincrease, it is NECESSARY AND SUFFICIENT
to test ALL i in A and all legal 51 palettes.
An arbitrary top-4/top-12 shortlist is insufficient.

**Important finite logical result:** if for EVERY active i,
all 51 legal t obey either
`R3(t)>=R3(current)` or
`R2(t)>R2(current)`, then the current complete
425-source assignment is a GUARDED original-source
**one-exchange local minimum** for true full R3.
The logical statement quantifies over exactly
425 original IDs and 51 patterns, but NOT
any two-source edit or nonmonotone sequence.

## 2. Source-complete independent preparation

For each real fixed W34 map `lex` and `reverse-line`,
load the immutable #716 complete real 425-original-
flag palette vectors, with frozen full exact risks

| Full fixed source risk | D2 | D3 | TRUE six-ID R3 |
|---|---:|---:|---:|
| lex | 1 | 483 | 62 |
| reverse-line | 0 | 69 | 69 |

Rebuild the actual W(3,4) symplectic source and the two globally
injected point/line pair mappings f,g. The independent #713
external full original GF5^28 oracle enumerates EVERY one of
the exact `C(425,3)=12,704,100` three-original-ID subsets
and EXACTLY all current 62/69 true six-DISTINCT-ID signed
3+3 witnesses. Every signed event must have a canonical
unique global sign, six actual source IDs and a true
complete 28-coordinate GF5 physical equation.

The source active-ID degree of flag i is the EXACT
number of signed 3v3 events containing it.
The total degree must equal 6R3, i.e.
372 for lex and 414 for reverse-line. The
source-support and 425×28 full physical original
GF5 coefficient matrix, the legal global 51-palette
table and ALL active ID-degree pairs are written
to a deterministic small UTF8 scientific input,
bound to its SHA256 digest and a separate source
manifest. No fabricated source palette or random
trial is introduced.

## 3. New fast EXACT original GF5 source-palette oracle

For EACH i in A, the existing Python
source-geometry code is mathematically exact
but too costly to repeat sequentially across
the potentially hundreds of true active IDs.
This slice adds a standalone optimized C++17
source-local kernel compiled on GitHub-hosted
Ubuntu runners (never the user's PC).

Each kernel call rebuilds the complete exact
original physical projection into:

- `outside_i(c)` in GF5^(m-4), 24 digits on actual W34;
- `inside_i(c)` in GF5^4, in exactly the REAL
  two-point/two-line physical support positions of
  ORIGINAL flag i.

The source 24-digit full outside key fits
in 56 bits, encoded in exact radix-five limbs.
GF5 addition of four-digit groups is
PRECOMPUTED as a 625×625 lookup table;
unlike normal integer addition, this performs
addition modulo five with NO base-five carries.
Full outside keys are never truncated,
sampled, Bloom-filtered or replaced by
probabilistic fingerprints.

Index EACH of the 89,676 actual other-original
2-subsets P by exact outside key, preserving
both ORIGINAL source IDs and all four
inside GF5 digits. Stream EACH of the
12,614,424 other-original source triples T,
reusing pair limbs, matching complete
outside GF5 keys, and explicitly rejecting
all P sharing ANY actual original source
flag with T. The four inside digits then
force at most ONE of the 51 legal nonzero
checksum-4 original source coefficient palettes
for the equality `c_i+sum(P)=sum(T)`.

The accumulated exact H_i(t) counts every
true six-source signed 3v3 event containing i
for all 51 palettes in ONE original-triple pass,
with no R2-shadow correction or assumed
independence.

A SECOND independent exact source R2
incidence histogram counts collisions
`c_i(t)+c_j=c_a+c_b` among real
original source singleton/pair projections,
rejecting overlapping source IDs. For each
palette t compute

\[
R3_{new}=R3_{old}+H_i(t)-H_i(old),\qquad
R2_{new}=R2_{old}+K_i(t)-K_i(old)
\]
and
\[
D3_{new}=R3_{new}+(N-4)R2_{new}.
\]

The original source H_i(old) MUST equal
the independently enumerated current
true R3 witness degree of flag i, and
K_i(old) cannot exceed global current R2.
All predicted D2/D3/R3 must be nonnegative.
For each flag i the C++ kernel chooses
the exact minimum lexicographic tuple
`(new_true_R3,new_R2,new_D3,palette_index)`
among ALL 51 candidates that obey
`new_R2<=R2_old`. The unchanged
palette always supplies an available
non-worsening control.

## 4. Distributed completeness and immutable evidence

The two current fixed-source assignments
are checked in separate GitHub-hosted
parallel matrices of **8 deterministic shards
per scheme**. A flag i is assigned
to shard `i mod 8`: every original
active ID belongs to exactly one
shard, independent of iteration order.

A mandatory separate aggregator downloads
EVERY one of the 16 shard JSON artifacts
and the SHA256-bound complete input manifests;
it FAILS CLOSED if any source i in A is
absent, duplicated, belongs to another
shard, has wrong current source coefficient,
does not have EXACTLY 51 candidate costs,
or does not reproduce its independently
counted original R3 incidence degree.

For EVERY active source and EVERY of the
51 patterns, the aggregator independently
reconstructs the exact candidate D2/D3/R3,
checks the no-increase-R2 condition, and
recalculates the kernel's selected per-source
optimum. It chooses the best globally
over ALL currently active IDs. Because
all 425-|A| inactive original flags are
mathematically pruned, this decision
covers ALL one-source edits, not a
top-K heuristic.

**Acceptance alternative A (improvement):**
if one active original source has a
strict smaller true R3 under nonincrease
R2, apply ONLY this legal source palette
in the full immutable 425-index original
coefficient array (retain the same complete
f,g and all other original source
variables), and FRESHLY scan ALL
12,704,100 ORIGINAL triples with the
PREVIOUS, independent Python GF5
external physical full-risk oracle.
This must reproduce predicted
D2,D3,TRUE R3 exactly, and independently
verify 28 real physical GF5 coordinates
for all emitted signed witnesses.
Never claim success if any result differs.

**Acceptance alternative B (local minimum):**
if NONE of the true active flags
admits a strict R3 decrease with
R2 nonincrease for ANY of its
51 legal patterns, the aggregator
independently recomputes the
current entire 425-original-source
full GF5 risk and emits an exact
finite source **R2-guarded
one-exchange local-minimum
certificate**. This does NOT
prove a global optimum, nor
exclude two-source moves or
intermediate R2/R3 increases.

The 425-index source assignment,
full source-ID participation
table, all source 51×R2/R3
exact cost histograms, chosen
global best move or exact
local-minimum evidence,
independent full physical
recheck and all source hashes
are saved as complete JSON
CI artifacts. Once actual
hosted run results have been
fully verified, they are
eligible to be frozen back
to the branch as separately
tested permanent scientific
certificates.

## 5. Adversarial independent testing

The same C++17 fast kernel MUST
also run on a TRUE original
45-flag W32 model with its
own nonzero 51-pattern global
source assignment and 12
physical GF5 coordinates.

For TWO genuine original
source flag IDs, the entire
51-option source H_i and
source-R2 cost vectors must
match 102 fresh, independently
computed FULL original
45-source GF5 1/2/3-subset
sum censuses, including
the complete signed 3+3
six-DISTINCT-ID collision
count. They must independently
agree with the unrelated
previous #715 exact
ΔD3−41ΔD2 oracle.
Malformed physical source
columns or truncated source
input must fail before any
scientific result is emitted.

Every full W34 result
is independently source-rechecked
after selection. The work
runs on GitHub-hosted Linux
only; no use of the user's PC.

## 5A. ACTUAL first complete true W34 active-source exhaustive result

The initial complete GitHub-hosted
[dedicated run #41647811306](https://github.com/definitely-stable/Mathlab/actions/runs/41647811306)
achieved **SUCCESS on every one of its
16 independent active-source matrix shards,
the independent W32 all-51 test,
the two full original source
preparation models and the aggregator**.
Its true symplectic W34 preparation
independently recomputed ALL 12,704,100
original three-source GF5 physical
sums for each frozen #716 425-flag
source assignment, enumerated ALL
current genuine signed six-ID R3
events and proved these coverage
counts:

| True fixed full W34 original source | lex | reverse-line |
|---|---:|---:|
| Prior original full R2 | 1 | 0 |
| Prior original full R3 | 62 | 69 |
| Complete six-ID signed events | 62 | 69 |
| Total actual incidence degrees (6×R3) | 372 | 414 |
| Original source IDs active in at least one current signed event | **247** | **272** |
| Inactive ORIGINAL flags rigorously pruned | 178 | 153 |
| All 51 coefficient options exhaustively evaluated | **12,597** | **13,872** |
| Exact active flags with a STRICT improving R2-guarded one-source palette | **247** | **272** |
| Local-minimum certificate for this prior assignment? | **NO** | **NO** |
| Best true R3 reduction with one legal source edit | 4 | 4 |
| Chosen original source ID, old→new palette | **136: 8→10** | **270: 22→0** |
| Final independent full original R2 | 1 | 0 |
| Final independent full original R3 | **58** | **65** |
| Final independent equal-triple D3 | 479 | 65 |

These two fixed source models have
**519 currently active source IDs
in total, and 26,469 exact
legal one-source GF5 options**
that must be audited to establish
full active source coverage
(247×51 + 272×51).
All 519 active flag IDs were
indeed independently checked
by all eight disjoint shards
per fixed model, including
every one of the 51 source
coefficient patterns.

The number of active sources
with a strictly improving
R2-guarded source edit, classified
by the maximum integer decrease
in TRUE six-distinct-original-ID R3:

| Strict full TRUE R3 reduction per active original source | lex sources | reverse-line sources |
|---|---:|---:|
| −1 | 158 | 168 |
| −2 | 62 | 74 |
| −3 | 18 | 22 |
| −4 | 9 | 8 |
| All improving active source flags | **247** | **272** |

Thus in THESE two complete
specific source assignments,
**EVERY currently active source
flag has a strict R3-improving
single-ORIGINAL-palette edit**
without increasing R2. In
particular, neither prior
#716 assignment is anywhere
close to an R2-guarded
one-exchange local minimum.
This is a fixed finite,
fully audited statement:
it does NOT assert this
property for arbitrary W34
source coefficient assignments
or for all h.

The R2 guard separately
rejected **148** source/palette
candidates on lex and **182**
on reverse-line out of the
entire 26,469 candidate set.
The best actual R3 improvement
was only four, but it was
determined globally among
ALL remaining active ORIGINAL
source flags, not guessed
from a top-4 partial search.

**Independent full-GF5 acceptance:**
after choosing the best permissible
source edit, the aggregator
rebuilt the complete REAL 425-original-ID
GF5 coefficient assignment with
the SAME original f,g maps
and recomputed every one of
the 12,704,100 source triple
sums using the SEPARATE
prior Python exact 12-byte
external-disk source oracle.
Both final signed risk triples
were independently confirmed:
lex `(D2,D3,R3)=(1,479,58)`,
reverse-line `(0,65,65)`.
The independent source R2
90,100-pair checker and
the actual physical 28D
signed six-ID witness equations
were also checked.

**Permanent compact original-source
scientific certificate:**
`research/hyp105_w34_all_active_oneexchange_certificates.json`
contains the two complete
425-ID ordered pre/post palette
vectors, exact 519-source
coverage statistics, exact
improvement histograms, optimal
source edit, unchanged f,g
scope and an SHA256 binding
to the full **1,135,227-byte**
CI-generated exact source
certificate with ALL 519
source-specific 51-way
R2/R3 cost arrays. The
complete certificate remains
available as a GitHub-hosted
[Actions artifact #13236088070](https://github.com/definitely-stable/Mathlab/actions/runs/41647811306/artifacts/13236088070),
and can be regenerated by
the committed deterministic
GitHub workflow. The source
input SHA256 hashes are also
recorded to tie the whole
matrix to the actual frozen
source coefficients.

An additional strict static
test independently reconstructs
both permanently stored final
real W34 physical source vectors,
checks EXACTLY one changed
ORIGINAL flag ID on each
model, recounts all true
source R2 pairs and repeats
the complete real
12,704,100-GF5-triple
external signed-event audit.
This static acceptance
does not rely on source
degree rankings, C++ cost
tables or optimization
code to arrive at final
R3=58 and 65.

### Next mathematical frontier

The logical one-exchange audit
found positive improvements,
so an R2-guarded
local-minimum/2-exchange
escape experiment is
**NOT yet warranted**
for these current assignments.
The correct next step is to
continue the exact direct
source-local R3 descent
using fresh signed-event
hotspots after the new
136/270 edits, possibly
amortizing fixed-source
outside-index calculations.
Only if exhaustive active
source audits fail to find
a strict guarded one-step
improvement is a two-source
escape argument meaningful.

## 6. Scientific limitations and STOP

The finite results concern
exact genuine W(3,4)
ORIGINAL GF5 coefficients
for two particular fixed
globally injected f,g maps.
Even if the full active search
proves guarded one-exchange
local optimality, it does
NOT show that no full zero
425-column ASET exists:
two or more coordinated
source edits may succeed,
and a nonmonotone step may
escape the local optimum.

Even a complete finite
W34 zero would not
automatically prove a uniform
all-h ASET asymptotic exponent.
The accepted large-s lower
bound on EXPECTED signed
R3 over uniform independent
original 51-palettes is a
different mathematical quantity.

Root HYP-105 #230 stays
`OPEN_WITH_FORMAL_BLOCKER`.
No merges or parent/main changes.
