# HYP-105 / issue #230 — AA4-FULLR3: exact full ORIGINAL 3-vs-3 GF(5) census by three-source subset sums

**Scientific objective:** resolve the precise gap left by #711:
its two 45-ORIGINAL-flag deterministic certificates avoid every
3v3 signed event in the seven *leading* 6+6-coordinate sixset classes,
but that does NOT establish the complete R3. This slice independently
tests the SAME saved original palettes for ALL other coordinate
multiplicity profiles, without rescanning the C(45,6) source sixsets,
and determines the true full 0..3 ASET status.

Strict scientific Draft stacked on frozen #711 exact HEAD
`3dc61153bb2aa16dac5a26aac95db048500e4f5d`.
No merged PR, ancestor/main edits, theorem exponent promotion or
claim that a finite W32 result establishes a uniform all-h statement.

## 1. The all-h exact bijection — NEW method, unlike seven-class lookup

Let `c_i` be the entire physical GF(5)^m column of ORIGINAL source
flag ID `i`, where the two point physical coordinate labels, two line
physical coordinate labels and all four nonzero GF5 coefficients are
taken together. The SAME ORIGINAL source ID variable is reused
globally. Each `c_i` has support exactly four and checksum
`sum_k c_i[k]=4 mod5`.

For every three-DISTINCT-source-ID subset T, define

```
  s(T) = sum_{i in T} c_i  (in GF(5)^m).
```

**Theorem (complete signed R3 meet-in-the-middle).** For ANY N
distinct ORIGINAL source flags and any full fixed coefficient assignment,
the set of ALL unordered signed 3-positive/3-negative collision events
on six DISTINCT original source flag IDs is in bijection with

```
 { {T,U} : T,U subset [N], |T|=|U|=3,
             T intersect U = empty,
             T != U, s(T)=s(U) }.
```

**Proof:** a signed sixset event is a six-term equation
`sum_{i in T} c_i - sum_{j in U}c_j=0` for its
three source IDs with plus sign and three with minus. Because there
are exactly six different ORIGINAL source IDs, T and U are disjoint.
The equation holds iff the full physical GF5 vectors s(T),s(U) agree,
coordinate-by-coordinate, with NO degree-two, leafless, cycle,
coordinate-proper, original geometric or connectedness hypotheses.
Interchanging T,U is overall sign reversal and is already identified
by the historical ten sign partitions. Conversely every pair
of disjoint triples with equal sums yields one such signed event.
These maps are exact inverses, proving bijectivity for all N,m
and all genuine or non-genuine source-host geometries. QED.

**Why this is materially stronger than #711:** the seven-class
GF5 parity solver requires that every physical coordinate be
occupied by exactly TWO selected original source columns. The
three-sum bijection imposes NO such restriction: its GF5 additions
handle multiplicity 2,3,4,5,6, different coordinate alphabets,
disconnected dual graphs and any point/line source multiplicity.

## 2. Exact complexity and the full source count

For true original W(3,2), N=45 and m=12. There are

```
 C(45,3) = 14190    distinct ORIGINAL source triples
 C(45,6) = 8145060  distinct ORIGINAL source sixsets.
```

A complete FULL R3 event census requires only ONE exact GF5^12
sum per triple, a hash table grouped by the resulting twelve GF5
digits, and comparison of triples in the SAME equality bucket.
It does not enumerate 8,145,060 source sixsets times ten signs.

For every equal-sum pair of triples, the algorithm checks whether
they are disjoint. Overlapping triples can have equal sums but are
NOT falsely charged as six-original-ID signed events:
one common original flag reduces to an old two-versus-two event,
two common flags reduce to a one-versus-one equality. The code
reports their count separately. A second completely different
twelve-coordinate modular summation explicitly verifies every
reported disjoint 3v3 event; its selected original six IDs,
original point/line factors, sign assignment, full twelve-digit
GF5 sum and coordinate multiplicity profiles are recorded.

For all 45 columns, the referee ALSO enumerates exact
`C(45,1)=45` and `C(45,2)=990` sums and checks their
injectivity in the same GF5^12 field. With the common checksum4
constraint, unequal subset cardinalities 0,1,2,3 have distinct
GF5 checksums `0,4,3,2`, so **all 0..3 subset sums are unique**
iff each of these four same-size sum maps is injective.
Thus the exact FULL original weighted ASET certificate can be
checked independently, not merely the 3+3 collision subgroup.

The implementation checks all triple sums by exact coordinatewise
mod-five arithmetic (NEVER by ordinary integer addition/carry).
For a selected independent twelve-original-source-ID subset it
also exhaustively enumerates every sixset x all TEN sign choices
and compares this mathematically DIFFERENT brute-force verifier
to the hash-pair census. The direct brute scan is not reused
to construct the triple hash.

## 3. Genuine ORIGINAL geometry and unmodified seven-class control

Both true W(3,2) complete fixed typed pair assignments
(`lex` and `reverse-line`) are reconstructed from the
source's actual 45 unique ORIGINAL incidence flag IDs:
15 original point factors, 15 original line factors and
separately bijective coordinate-pair maps to K6 edges.
The complete physical GF(5)^12 column is constructed from
the ORIGINAL flag's actual f(p),g(ell) and the saved original
51-palette assignment, with the second coordinate alphabet
shifted into the other six physical coordinates.

The two 45-entry assignments are EXACTLY the permanently committed
#711 certificates in
`research/hyp105_w32_sevenclass_original_45flag_certificates.json`.
They are not reseeded or replaced to make a nicer result. The
full R3 hash outcome is directly compared with #711's separate
explicit 10-sign GF5 event census on ALL 259 / 169 leading
original sixsets. Any collision outside these accepted classes
is **not** swept into the seven-class zero floor: the report
isolates and counts all such source events and gives their
real physical coordinate multiplicity profiles and original
flag-ID witnesses.

As a positive control the all-ones source palette, which is
legal under checksum4, has at least 96 lex and 11 reverse-line
leading signed events, and the new FULL R3 oracle MUST find
all of them. As an unrelated historical independent reference,
the older 45-column original W32 GF5 checksum4 ASET witness
in `research/hyp105_g5d_w32_45_witness.json` is loaded and
its 45,990,14190 individual subset sums are independently
verified by the NEW GF5 triple hash. This earlier construction
already proved a full 45-column finite ASET result; we do
not misrepresent its existence as a discovery in this PR.

## 3A. NEW exact local ORIGINAL source repair — theorem, not a blind search

The full census exposes an important honest falsification of #711:
the frozen full source palette `lex` has **SEVEN** TRUE full-R3
3+3 events, and `reverse-line` has **FOUR**, while their respective
seven-leading-class event counts are BOTH exactly ZERO. On the
unaccounted events the physically repeated coordinate profiles
include (3,3,2,2,2), (4,3,3,2), (5,3,2,2) and (3,3,3,3).
No original sixset or GF5 signed event has been fabricated or
ignored. These are concrete counterexamples to the logically
invalid inference `seven-leading zero -> full R3 zero` for
the SAME original W32 source f,g.

**New exact single-original-flag descent lemma:** choose one
original source flag i and hold EVERY other original flag palette
fixed. Partition all triples into U, the C(N-1,3) triples NOT
containing i, and I_i, the C(N-1,2) triples containing i.
The number of unordered equal-sum pairs of triples is

```
  Q = Q(U,U) + Q(I_i,I_i) + Q(U,I_i).
```

Under ANY change of the SINGLE original palette of flag i:

- Q(U,U) is invariant because NONE of those original three-source
  subset sums contains i.
- Q(I_i,I_i) is invariant because the common c_i cancels
  when comparing two triple sums both containing i:
  c_i+c_a+c_b=c_i+c_c+c_d iff c_a+c_b=c_c+c_d.
- Therefore the ENTIRE exact global change of Q is equal to
  the change of the cross-term `Q(U,I_i)` alone.

For W32, independently hash the **13,244** true original
triple sums on the 44 other flag IDs, then precompute the
**946** pair sums on those other flag IDs. For EACH of the
51 physically legal checksum4 source palettes `omega_i`,
compute the new 946 affected triple sums and count how many
collide with the 13,244 fixed unaffected triple sums. Pick
the first strictly better palette. This minimizes the
**EXACT GLOBAL** all-3-subset collision count for that one
source ID, not a heuristic proxy or expectation.

A selected move has a guaranteed **strictly decreasing nonnegative
integer** global triple-collision objective. The implementation
checks the predicted cross-term difference against a FRESH
independent recomputation of ALL 14,190 original three-subset sums
after EVERY accepted move. Repeatedly process source IDs that
participate in actual currently equal triple sums. If no
improving one-variable move exists, STOP with the nonzero
remaining risk: a local minimum is NOT proof of nonexistence
of a global full-zero assignment. Thus the algorithm is
mathematically safe but not claimed globally complete.

**Actual successful hosted W32 repairs of the frozen #711 witnesses:**

| Fixed true W32 original f,g | Prior full 3v3 events | Source IDs edited | New full 3v3 events |
|---|---:|---|---:|
| `lex` | **7** | **29, 40, 23** | **0** |
| `reverse-line` | **4** | **17, 30** | **0** |

All other ORIGINAL flag IDs retain EXACTLY the same 51-palette
choice they had in the frozen #711 certificates. After these
three/two legal SOURCE-local changes, both completed sources
have **exactly 14,190 DISTINCT 3-subset GF5^12 sums**, **990
distinct 2-subset sums**, **45 distinct 1-subset sums** and
the unique empty-subset sum. Across different sizes checksum4
prevents equality; thus all 1+45+990+14190=**15,226**
original subset sums of sizes 0..3 are pairwise distinct.

**Permanent exact artifact:** the true fully verified
45 ORIGINAL source-flag-ID ordered palette arrays for BOTH
fixed maps are committed in
`research/hyp105_w32_full_r3_original_45flag_certificates.json`.
The new hosted test parses the STATIC file, proves that
exactly these 3/2 source IDs differ from prior #711,
and independently recomputes the entire original full 3-sum
hash, all k=1,2,3 uniqueness results, and all 259/169
historical seven-family direct physical GF5 signs.
The source maps f,g and all 45 original flag IDs remain
unchanged, with no coordinate relabeling or newly invented source.

**Novelty boundary:** #G5-D had already generated another
45-column exact GF5 ASET witness at W32; the *existence*
of a finite 45-column example is NOT newly claimed.
The new contribution is the source-preserving, exact quantified
full-R3 repair of the specific 45-ID assignments from #711,
the 14,190-triple source-complete independent verifier, its
coordinate-multiplicity counterexamples, and the 946-pair
single-variable optimization identity. Nothing here proves
a uniform positive-power all-h asymptotic result.

## 4. What the final exact certificate can and cannot establish

Two different, fully checkable conditions are reported:

1. `FULL_original_distinct_sixflag_3v3_signed_events == 0`:
   the TRUE full fixed-original-map R3 signed 3+3 collision
   count is zero, not merely the seven leading motif subcount.
2. `all_45_original_source_0_to_3_subset_sums_unique == True`:
   after also independently checking the 1-,2-,3-subset sums
   and the affine checksum barrier, the actual 45-column
   original construction is a full finite ASET through order 3.

These are never conflated with bounds on random GF5 coefficient
expectations, the all-h s→infinity Branch A obstruction,
or an improvement of the best known ASET exponent.

A bounded deterministic seed search (same exact SHA256 source
domain as #711) may additionally find another full zero witness.
It is only a reproducible finite search; if no seed succeeds,
the program reports the tested results without pretending that
a new full zero certificate exists. An independent check of the
2010s? no — the *pre-existing 2026* G5-D witness is the genuine
reference for finite full-ASET feasibility.

**Research acceptance:** this closes the exact finite-source
W32 full-R3 coverage gap from #711 if and only if the
GitHub-hosted actual full-source hash and independent checks pass.
It does not settle infinitely many dyadic W(3,s), deterministic
asymptotic zero R3, or issue #230's all-map expected lower bound.
Continue scientific draft governance; no merge to main.
