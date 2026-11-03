# HYP-105 / issue #230 — AA4-W34LOCAL: exact 51-palette ORIGINAL source-local repair of full GF(5) triple sums

Scientific Draft, STRICTLY stacked on frozen W34 exact full-R3 #713
at `c3b62d35da40ac3101330a2f9d918c1c710c1ce6`.
No ancestor/main mutations, no merges, no closure of #230.
All source flags, original point/line factors, and separately globally
pair-injective physical f,g maps remain immutable.

## 1. Actual research question

The prior FULL genuine symplectic W(3,4) original-source audit
covered ALL C(425,3)=12,704,100 three-source subsets under two fixed
legal pair maps f,g, with a single globally reused 51-valued GF5
checksum4 source palette per each of the 425 actual ORIGINAL incidence
flag IDs. It gave for the fixed seed0 global palette assignments:

| EXACT prior seeded source assignment | lex | reverse-line |
|---|---:|---:|
| D2 equal full 2-sum source pairs | 3 | 1 |
| D3 equal full 3-sum source pairs | 1,349 | 517 |
| Actual R3det with six distinct ORIGINAL IDs | 86 | 96 |

The independently proved all-N identity for distinct fixed physical
source vectors is D3 = R3det + (N-4)*D2. For N=425,
`1349=86+421*3` and `517=96+421*1`.
The goal here is to change as FEW SOURCE palettes as possible
without changing f or g, strictly reducing the exact full D3
and independently verifying the resulting full D2 / R3.
This is an honest constructive FINITE test, not an
all-h asymptotic proof or a result that every W34 assignment
has zero collisions.

## 2. New exact all-N one-variable GF5 cross-collision lemma

Fix a genuine ORIGINAL source flag i with physical 4-coordinate
support S_i. All other source palettes and all actual pair maps
are held fixed.

Let U denote original 3-subsets NOT containing i and A_i denote
3-subsets CONTAINING i. Decompose equal-three-sum pair count:

`D3(omega) = Q(U,U) + Q(A_i,A_i) + Q(U,A_i)`.

Both Q(U,U) and Q(A_i,A_i) are INVARIANT under a change of the
one actual original palette omega_i:
- sums of U triples do not include the source column c_i;
- any equality of two A_i triple sums includes the same c_i
  on both sides and cancels it exactly.

Therefore for any two choices t,u from the same legal 51-palette,

`D3(omega_i=t)-D3(omega_i=u)
     = Q(U,A_i;t)-Q(U,A_i;u).            (LOCAL)`

This is an EXACT global-objective identity, not a local heuristic,
random score, or a proxy for R3. In particular choosing a palette
with a strictly smaller true cross-collision count strictly
decreases the FULL count D3 of equal three-source subset sums.

**Mathematical limitation:** minimizing D3 is a legitimate
sufficient direction for full 0..3 ASET; if D3 becomes zero,
the all-N identity and N>4 imply D2=R3det=0.
For D3>0, R3det can increase when D2 decreases since
R3det=D3-(N-4)*D2; NEVER claim every D3 decrease
also strictly decreases R3. The code reports both
full R2 and full R3 separately and accepts only the
rigorously verified D3 monotonicity.

## 3. New exact projection algorithm: ALL 51 possibilities in ONE full pass

Write an ORIGINAL physical GF5^m vector as
`(outside_i(v), inside_i(v))`, where inside_i
contains the FOUR actual support coordinates of the ORIGINAL
source flag i (two f(p) and two g(ell) coordinates), and
outside_i contains all other m-4 physical coordinates.

For W34, m=28 so the outside projection is GF5^24 and
inside is GF5^4. It is losslessly encoded with exact
radix-five digits. Crucially, c_i has ZERO entries
in the outside projection.

For every two-subset P={j,k} of the other N-1 source IDs
and every three-subset T={a,b,c} of those same other
IDs (they MAY OVERLAP: this calculation counts D3
not R3), an equality

`c_i + sum_{j in P} c_j = sum_{a in T} c_a`

is possible for SOME choice of source palette iff their
OUTSIDE sums are exactly equal; in that case it forces
the ENTIRE four-coordinate source palette to be

`omega_i = inside_i(s(T)) - inside_i(s(P)) (mod 5)`.

The forced four-coordinate GF5 tuple may contain zeros
or violate checksum4, in which case it is NOT a legal
source coefficient assignment; otherwise it belongs
to EXACTLY ONE of the 51 available ORIGINAL palettes.
Thus scanning every matching outside pair/triple tuple
increments the corresponding exact 51-entry histogram
once. It directly counts cross-collisions for ALL
51 choices, without 51 full triple rescans.

The algorithm:
1. builds an exact lookup for all `C(N-1,2)` other
   ORIGINAL pair sums, indexed by their complete
   GF5 outside projection and storing inside4
   sum multiplicities;
2. streams EACH of the `C(N-1,3)` other ORIGINAL
   triple sums once, reconstructing the outside
   projection and looking up ALL matching actual pair sums;
3. computes the forced four GF5 coefficients and looks
   up the EXACT palette ID in a new 625x625 GF5
   difference table, never a truncated hash;
4. selects the lexicographically first minimizer
   of the 51 fully computed exact counts, accepting
   an edit ONLY for strict FULL-D3 improvement.

For N=425 this is a full source 89,676-pair index
and an EXACT 12,614,424-other-triple streaming scan
for each chosen original ID; all operations are
genuine source GF5 vector additions, and every
checked projection equality is exact over 24 physical
GF5 coordinates. For W32, N=45, the corresponding
numbers are 946 original pairs and 13,244 triples.

This FULL one-pass per source-paletted variable algorithm
uses memory proportional to the 89,676-indexed pair
sums plus fixed four-GF5-digit tables, NOT a
12.7-million Python-object full triple hash.

## 4. Independent exhaustive reference and source safeguards

On true complete symplectic W32, the new algorithm's entire
51-valued cross histogram is INDEPENDENTLY verified for
multiple ACTUAL source IDs against a fresh full census of
ALL 14,190 source 3-subset GF5^12 sums for EACH individual
one-original-ID palette change. This tests all 51,
not only the chosen minimizer or self-consistency.
The true W34 implementation's 24-coordinate projections
are checked against direct 28-coordinate sums on real
genuine source triples, as are the 625x625 GF5
difference table and fixed physical support slots.
Bad input/source IDs, unsupported source budgets and
illegal palette indices fail closed.

For W34, source IDs to evaluate are first selected
from ACTUAL nonzero R2 original two-subset equality
witnesses (3 lex, 1 reverse-line at seed0).
This is justified mathematically as a high-leverage
first repair direction, because each disjoint 2+2
collision accounts for EXACTLY 421 overlap-one
three-subset collisions in D3, as independently
proved in #713. This is a finite source-variable
HEURISTIC ORDER; it does NOT pretend to maximize
the number of six-distinct-source R3 events removed,
nor guarantee finite full-zero convergence.

After EVERY accepted source change, the exact
R2 is recomputed by a fresh original 90,100-pair
full GF5 sum census. The D3 value is updated
using the independently checked exact LOCAL
cross-difference identity, with strictly
decreasing integer objective.

**Final independent acceptance gate:** after the
finite source changes, the program reruns the
ENTIRE prior external 12,704,100-triple
original GF5^28 audit from #713, including
lossless source signatures, source intersection
IE, independent all-N R2-to-R3 identity,
all selected true signed witnesses, and
full source scope checks.
The measured full D3, D2, R3 MUST match the
predicted values exactly. No partial
census or unverified local-risk value
is ever promoted to final proof.

## 4A. Actual hosted complete W34 R2-first source repair outcomes

Hosted dedicated [first repair CI #41606244186](https://github.com/definitely-stable/Mathlab/actions/runs/41606244186)
completed ALL THREE GitHub-hosted jobs SUCCESS: independent
51-by-51 exhaustive real W32 source projection test,
full true W34 lex source repair, full true W34 reverse-line
source repair. Each repaired global source assignment was
rechecked against an ENTIRE fresh 12,704,100-original-triple
GF5^28 external disk census, including true source
intersection correction and independent full R2.

| Fixed REAL original W34 scheme | D2 before → after | D3 before → after | TRUE full R3det before → after | edited ORIGINAL flag IDs |
|---|---:|---:|---:|---|
| lex | **3 → 1** | **1,349 → 507** | **86 → 86** | **45, 143** |
| reverse-line | **1 → 0** | **517 → 96** | **96 → 96** | **184** |

Every edited original flag retains exactly the
same four physical coordinates, original
point/line factor ownership and global
source ID. Only its source-wide legal GF5
checksum-4 coefficient palette is changed;
all other source IDs retain the original
domain-separated SHA256 seed0 assignment.

For lex, the exact original source changes
were ID 45: palette **38→3**, then
ID 143: palette **35→2**, each
removing one actual original 2+2 event.
For reverse-line, ID 184: palette **18→8**,
removing its sole original 2+2 event.

**Important independent mathematical observation:**
each eliminated true R2 event removes exactly
`N-4=421` overlapping equal-triple pairs,
and NO six-distinct-original-ID 3+3 event
in these particular experiments.
Indeed the exact all-N identity gives

\[
(1349-507)=421(3-1)+86-86=842,
\]

\[
(517-96)=421(1-0)+96-96=421.
\]

This is a CONCRETE counterexample to the
tempting inference that a substantial
decrease in D3 is itself progress
on the actual six-distinct-ID R3.
The algorithm correctly claims
only the quantity it optimizes.

The **complete reproducible exact scientific evidence**
was emitted by the hosted full source workers
and permanently committed to
`research/hyp105_w34_r2first_repaired_source_certificates.json`:
both 425-source-ID ordered legal GF5 palette arrays,
all actually edited ORIGINAL source IDs,
the entire 51-candidate projected cross score
on each edit, full D2/D3/R3 before/after,
and true 28-coordinate physical GF5
signed witnesses. Independent tests parse
the committed STATIC artifact, reconstruct
both true source maps and original 425 flags,
check that ONLY the stated 2/1 original
source ID coefficient variables changed,
recompute the exact R2 from all 90,100
actual two-flag sums, enforce both 421
overlap-correction equalities, and directly
verify each final real W34 six-original-flag
28D signed collision witness.

**The correct NEXT mathematical target is a
direct R3 objective**, not blind D3 descent.
The same exact two-point support projection
method can also obtain, for EACH of the
51 palettes, the change `ΔD2(t)`
from comparing affected source pairs
`{i,j}` against unaffected pairs
`{k,l}`. There are only 424
affected one-other-original-source
choices and 89,676 unaffected pairs,
so its exact computation is smaller
than the 12.6m-triple D3 projection.

Then by the independently established
all-N identity, for EVERY palette t

\[
\boxed{
ΔR3_{det}(t)=ΔD3(t)-421\,ΔD2(t).
}
\]

Thus future source repair can CHOOSE A
PALETTE TO MINIMIZE ACTUAL FULL R3,
and impose D2=0 or nonincrease as a
separate hard guardrail. This can be
tested for every source candidate using
the all-51 exact projection histogram
rather than 51 full external risk scans.
No such direct-R3 repair is silently
claimed as implemented in this slice.

## 5. What counts as success, and scientific STOP

A certified D3 decrease for either real W34 source scheme
is a valid algorithmic advance. If R2 is driven to zero,
that is a separately verified improvement over the
seed0 baseline. If residual genuine full R3>0,
then a full finite ASET has NOT yet been built
in this slice; do not conflate lower D3,
zero R2, zero seven-class risk or a
single 425-source-assignment with all-h ASET.

The exact final 425-entry source-ID ordered palette
arrays, source changes, original and final R2/D3/R3,
and full hosted-recheck status are intended as
the permanent reproducible outputs of the
GitHub-hosted lex/reverse-line experiments,
with no altered original geometry.

The accepted all-h large-s Branch A theorem is about
EXPECTED signed risk over independent uniform
51-palette original source variables at fixed f,g.
Even a finite W34 zero risk (were it achieved)
would neither disprove that expected lower bound
nor prove a new asymptotic exponent.

Root #230 remains `OPEN_WITH_FORMAL_BLOCKER`;
all results should be peer-reviewable as source and
hosted CI evidence, all PRs Draft and unmerged.
