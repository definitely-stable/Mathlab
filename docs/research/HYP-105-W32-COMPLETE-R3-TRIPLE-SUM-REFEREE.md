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
