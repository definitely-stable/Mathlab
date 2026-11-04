# HYP-105 / #230 — AA4-ERASE0: exact no-new-event ORIGINAL GF5 signed-R3 conflict erasure

**Scientific Draft**, strictly stacked on frozen [#718](https://github.com/definitely-stable/Mathlab/pull/718)
exact HEAD `b0be049a0899ec653a36956d363c43eb762426a2`.
Do not merge or change main, the parent Draft PR, fixed f/g source labels or issue #230 governance. Root stays `OPEN_WITH_FORMAL_BLOCKER` until the actual universal theorem is proved.

## 1. New mathematical frontier: removing events instead of merely decreasing their number

The previous exhaustive complete W34 fixed-original-source experiments
repeatedly found **every active ORIGINAL flag** could strictly improve
true R3 while keeping true R2 nonincreasing, but reducing R3 by four
does not prevent NEW signed 3+3 events from appearing elsewhere.

The full 51-palette local risk tables from the independent
[#718 exact-source experiment](https://github.com/definitely-stable/Mathlab/actions/runs/41720801379)
reveal a stronger and useful finite property on its
BEFORE-#718 source assignments, where original R3 was 58/65:
ALL 239 lex-active and ALL 263 reverse-line-active original flags
each had a source palette that was simultaneously

1. R2-safe: no increase of global complete original R2;
2. **zero-incidence**: the exact source-local count of true
   six-DISTINCT-original-ID signed R3 events containing the
   edited original flag was ZERO.

The corresponding exact number of source palettes `t` satisfying
BOTH conditions was at least 4 (lex) / at least 3 (reverse-line)
for every active original flag, on those two specific fixed
BEFORE-#718 arrays. These are exact finite census observations,
not a theorem covering the NEW after-#718 54/61 arrays or all h.

This justifies a qualitatively different next algorithm:
force no new signed 3+3 event in each accepted source edit,
instead of merely finding a lower total R3.

## 2. Source-local zero-incidence erasure theorem (all N)

Fix N pairwise distinct ORIGINAL full physical GF5 source
columns `c_0,...,c_{N-1}`, obtained from a fixed original
point-line incidence geometry, fixed complete separately injected
point-pair and line-pair maps f,g and one globally reused
legal GF5 coefficient palette per ORIGINAL source flag.

Let E(c) be the set of all unordered signed balanced
3-positive/3-negative cancellations on SIX DISTINCT
ORIGINAL source IDs, with sign equivalence under
simultaneous reversal:

\[
 E(c)=\bigl\{\{P,T\}:|P|=|T|=3,\ P\cap T=\varnothing,\
 \sum_{p\in P}c_p=\sum_{t\in T}c_t\bigr\}.
\]

For any fixed original source ID i and legal palette
t on its four physical support coordinates, set

\[
 H_i(t)=\#\bigl\{(A,B):|A|=2,\ |B|=3,\ A\cap B=\varnothing,\
 i\notin A\cup B,\ c_i(t)+\sum_{a\in A}c_a=\sum_{b\in B}c_b\bigr\}.
\]

The signature of any signed event containing i
has a UNIQUE global orientation making i positive.
That event is in bijection with exactly one disjoint
(A,B) counted by H_i(t). All signed events avoiding
i do not depend on the coefficient of i.

**Theorem (exact event SET subtraction).** If c' is
obtained by changing ONLY c_i to a legal palette t
for which `H_i(t)=0`, then

\[
 \boxed{E(c')=E(c)\setminus\{e\in E(c):i\in e\}.}
\]

**Proof.** Partition signed events in c' according
to whether their six original IDs contain i.
Those containing i are counted exactly by H_i(t),
which by hypothesis is zero. Every signed
six-ID event avoiding i is an equality among
unchanged original source columns, and so is
an event in c' iff it already was one in c.
The displayed event-set equality follows,
with no probabilistic assumption, no
surrogate D3 and no graph-class restriction. QED.

**Strict progress.** If i participates in at
least one existing event (its exact current
witness degree `d_i>0`), this edit deletes
exactly d_i actual signed events, and creates
zero new ones. Thus the entire conflict
hypergraph monotonically decreases under
set inclusion, not merely cardinality:

\[
 E(c^{(k+1)})\subsetneq E(c^{(k)}),
 \quad R3_{k+1}=R3_k-d_i.
\]

If independently the complete original 2+2
risk `R2_{k+1}<=R2_k`, then the
integer potential `R2+R3` never increases
and strictly decreases on any move deleting
an R3 event or an R2 event. The finite
sequence must terminate in at most
`R2_start + R3_start` accepted moves,
but it may stop at nonzero R3 if
no legal zero-incidence source move exists.

**No blanket ASET convergence theorem is claimed.**
The existence of a legal t with H_i(t)=0
and R2 nonincrease for at least one
current active source i at EVERY subsequent
configuration is an additional condition,
to be tested by actual exact physical GF5
source data. If it holds, the algorithm
eventually constructs a full R3=0 source
assignment; if R2 also becomes zero,
this gives a completely genuine finite
425-original-column 0-to-3 GF5 ASET
certificate for that particular fixed
W(3,4) source map, NOT an all-h theorem.

## 3. Real W34 deterministic conditional-erasure algorithm

Start from frozen #718 actual full 425-ORIGINAL-flag
source palette arrays (not the old #717 source)
with independently checked complete physical risks

| Genuine symplectic W(3,4), fixed f/g | R2 | D3 | TRUE six-ID R3 |
|---|---:|---:|---:|
| lex | 1 | 475 | 54 |
| reverse-line | 0 | 61 | 61 |

Independently re-enumerate ALL 12,704,100
true original GF5^28 three-source signatures
using the established #713 external-disk auditor,
and request ALL original signed event witnesses.
Require the initial physical 28D source equation
for EVERY signed witness, six distinct true
original flag IDs and exact initial R2/D3/R3.

At each step choose a source ID occurring in an
actual surviving signed event. If R2>0,
first consider the ORIGINAL flags participating
in actual R2 events, including flags currently
absent from R3, to try to eliminate R2 as well.
The source-ordering heuristic does NOT purport
to prove global palette optimality.

For the chosen actual source ID i, call the
unchanged, independently verified exact
C++17 projected source-local GF5 oracle.
The oracle builds the full 24D outside and
4D physical inside coordinate representations,
indexes ALL 89,676 other ORIGINAL source
pairs, streams ALL 12,614,424 other ORIGINAL
triples, excludes overlapping source IDs,
and derives EXACTLY 51 H_i(t) true
signed six-ID incidences and 51 separate
K_i(t) source R2 incidences.

**Accept a candidate ONLY when**
`H_i(t)=0`,
`R2(new)=R2(old)+K_i(t)-K_i(old)<=R2(old)`,
and at least one of R2 or R3 decreases.
No new physical source supports,
no changes to global f,g, no unaligned
class-only proxies, no fake random columns.

The maintained canonical signed hypergraph
is updated by deleting *precisely* the
events containing i. This is justified by
the theorem, not by stale approximate
or sampled collision hashes. The algorithm
keeps an explicit sequence of original
flag IDs and legal original coefficient
changes and verifies the complete actual
90,100 source pair sums plus every
surviving 28D GF5 signed equation AFTER
EACH accepted edit.

Every eight accepted edits (or more frequently),
and unconditionally at the end, a NEW
fully independent external-disk
12,704,100-original-triple physical
GF5^28 enumeration must reproduce
BOTH the exact predicted R2/D3/R3
and the ENTIRE canonical current
signed event set — not just its
cardinality. On ANY discrepancy,
fail closed; never call partial
W34 output proof-complete.

The original full source assignment
has N=425, m=28, 51 legal all-nonzero
checksum4 physical palettes, EXACT
source IDs and real separately
pair-injective f,g factor maps.
Every accepted globally reused
source coefficient change is
saved in exact chronological order.

The finite search has a strict bounded
step budget of 72, above
R3+R2=55/61 of its two actual
fixed starting assignments.
On a stopped nonzero run
report EXACTLY what was tried
and that this proves no universal
nonexistence. Do not silently
convert an unsuccessful heuristic
into a mathematical no-go.

## 4. Independent source falsification, CI, and root governance

The source-erasure identity is tested
on actual original W(3,2)
45-source-flag GF5^12 geometry
for TWO CONSECUTIVE legal
zero-incidence coefficient edits.
A separate full 14,190-original-
triple physical source auditor
must independently verify the
EXACT set subtraction of all
true signed six-ID events for
each move, full source R2 and
the all-N D3=R3+(N-4)R2
identity. These tests must fail
if even one previously absent
original signed event appears.
Additional tests lock both
complete frozen after-#718 source
arrays and the source-ID
coverage assumptions.

Use only GitHub-hosted Ubuntu
for actual complete W34 runs.
Separate 90-minute-budget
lex/reverse-line workers independently
produce complete signed-event
erasure traces and final
source-coefficient arrays as
inspectable artifacts.
Finite acceptance is CONDITIONAL
on the independent full external
physical audit; the mere printed
command output is not proof.

### Full Research CI blocker observed on frozen #718

The [#718 Research](https://github.com/definitely-stable/Mathlab/actions/runs/41720801356)
did not finish with success:
the inherited `lent-001-foundation`
job was **cancelled at its former
20-minute timeout** during the
unfiltered whole-research
`python -m unittest discover`
step; the strict research-full-suite
guard then correctly failed.
The mathematical GF5 specialized
run remained green.

This CHILD branch raises ONLY the
`lent-001-foundation` GitHub-hosted
time budget from 20 to 40 minutes,
without removing any source test,
skipping a slow independent W34
referee, altering a hardness
manifest or changing ancestor
research governance. All four
Research shards must still
complete SUCCESS before a
full Research green claim.

## 4A. COMPLETE real original W34 GF5 0-to-3 ASET constructed on BOTH fixed f/g maps

The initial independent hosted
[scientific Actions #41785719789](https://github.com/definitely-stable/Mathlab/actions/runs/41785719789)
finished **SUCCESS on ALL THREE jobs**:
- the original W32 two consecutive exact source-erasure
  independent physical GF5 falsifier;
- the full 425-source **lex** W34 proof;
- the full 425-source **reverse-line** W34 proof.

The algorithm reached genuine zero source-risk on
BOTH real original W34 global separately pair-injective
point/line source maps:

| Fixed actual W(3,4) ORIGINAL source f/g scheme | Prior complete (R2,D3,TRUE six-ID R3) | Actual final complete (R2,D3,TRUE R3) | Genuine one-ORIGINAL-flag source recolorings | Independent FULL external 12,704,100-triple source checkpoints |
|---|---|---|---:|---:|
| **lex** | (1,475,54) | **(0,0,0)** | **27** | **6** |
| **reverse-line** | (0,61,61) | **(0,0,0)** | **29** | **6** |

The lex source also removed the original
one remaining source 2+2 signed risk
in its FIRST recoloring:
source ID **188, palette 38→1**,
R2:1→0 and true R3:54→53.
No R2 event reappeared. The subsequent
26 clean recolorings deleted the other
53 signed six-source R3 events exactly,
without introducing any new one.
For reverse-line R2 was zero at every step;
29 recolorings delete exactly 61 true
source R3 events.

The two complete exact original source
425-column final legal GF5 coefficient
assignments are permanently committed in

`research/hyp105_w34_zero_incidence_erasure_certificates.json`.

This file includes for EACH map:
- all 425 ordered ORIGINAL source
  palette indices BEFORE and AFTER;
- EVERY real source ID recolored,
  old/new true checksum4 legal palette,
  number of actual six-distinct-ID
  signed R3 events eliminated;
- exact complete original R2/D3/R3
  after EVERY source edit;
- the initial and final six independent
  physical GF5 FULL 12,704,100-triple
  external-disk rehash checkpoints,
  all requiring the **ENTIRE canonical
  signed six-source event set**
  to match the theorem's deletion-only
  prediction, not merely matching
  the total event count;
- GitHub Actions IDs and SHA256 of
  the complete full proof trace.

The complete immutable hosted traces are
available as
[lex scientific artifact #13300718437](https://github.com/definitely-stable/Mathlab/actions/runs/41785719789/artifacts/13300718437)
(28,958-byte JSON, SHA256
`250bf7f6417561047d74083d01177a50a91b2473bef01b346e447526be85102d`)
and
[reverse-line scientific artifact #13301800312](https://github.com/definitely-stable/Mathlab/actions/runs/41785719789/artifacts/13301800312)
(30,427-byte JSON, SHA256
`36d28dd294c283e00a6e46179385fa4d65ac04706f1ceaddc0d66c292c183f7e`).
The code reproduces these traces
deterministically. Recheck the fixed
source array against the permanent
certificate, not only against
downloadable short-lived Actions artifacts.

### Complete 0-to-3 ASET theorem for this finite physical source certificate

Write `S_k` for all GF5^28 sums
of k-DISTINCT original W34 source
columns, k=0,1,2,3.

**Within each cardinality:** the independently
exact current physical source referee
reports:
\[
 |S_0|=1,\quad |S_1|=425,\quad
 |S_2|=\binom{425}{2}=90,100,\quad
 |S_3|=\binom{425}{3}=12,704,100.
\]
No two different genuine original
subsets of the same size k≤3
have equal full GF(5)^28 sum.

**Between different cardinalities:** each
legally globally reused ORIGINAL source
column c_i has 4 nonzero physical
coordinates whose GF5 checksum satisfies
\(\sum_{j=0}^{27} (c_i)_j=4\pmod5\).
Consequently any k-source sum has
total physical coordinate checksum
\(4k\pmod5\). For k=0,1,2,3
these are **0,4,3,2**, which
are pairwise different in GF5.
Thus different source-subset
cardinalities in 0..3
CANNOT collide, regardless
of the actual individual indices.

**Conclusion:** for EACH of the two
complete fixed original W34
source coefficient assignments
the subset-sum map
\[
 (I,\ |I|\le3)\longmapsto
 \sum_{i\in I}c_i\in GF(5)^{28}
\]
is INJECTIVE. Its domain contains
\[
 1+425+90,100+12,704,100
 =\boxed{12,794,626}
\]
different original subsets,
all mapped to different complete
physical GF5 vectors.

This is an exact CONSTRUCTIVE
**425-column 0-to-3 GF5 ASET
on genuine symplectic W(3,4)**
for both frozen original
global source geometries,
not merely the vanishing
of a proxy 3SUM score.

### Mandatory independent final scientific peer check

A NEW verifier
`research/hyp105_w34_zero_incidence_final_certificate_verify.py`
parses both committed exact full 425-source
arrays and traces; replays all 27/29
changes against the earlier immutable
#718 physical coefficient arrays;
reconstructs both actual original
symplectic W34 f/g and original
point-line incidence flags;
checks the globally shared nonzero
checksum4 source palettes and
425 distinct 28-coordinate
original source columns; recomputes
EVERY one of 90,100 true
source two-subset sums;
and re-enumerates ALL 12,704,100
true original GF5^28 three-subset
sums for EACH map using the
separate historical #713
exact external disk-sorted
signature oracle.

It MUST confirm exact `(R2,D3,R3)=(0,0,0)`,
all 12,704,100 triple signatures distinct,
and no single/multi-cardinality
counterexamples. It does NOT call
the new erasure algorithm or
its C++ source-local 51-option
candidate evaluator to establish
that final fact. This last
mandatory independent CI is
a separate hosted job on the
FINAL committed source SHA.
Do NOT call the committed
dual finite certificates
referee-ACCEPT until this
job completes SUCCESS.

## 5. Scientific limits

If actual W34 zero R2 and R3
is constructed and independently
verified, it is a finite exact
source certificate ONLY for
the particular chosen
f,g maps and s=4. It does NOT
prove the universal positive-power
HYP-105 theorem for all h, nor
contradict any asymptotic lower
bound on the EXPECTED risk of
random original GF5 patterns.

If no erasure move is found
during a bounded source
choice, it does not prove
that no ordinary R3-decreasing
single-source edit exists
and says nothing about two-source
trades or nonmonotone paths.

Root HYP-105 issue #230 remains
`OPEN_WITH_FORMAL_BLOCKER`
unless a separately proved
full all-h theorem justifies
an issue governance change.
No merges or parent/main mutations.
