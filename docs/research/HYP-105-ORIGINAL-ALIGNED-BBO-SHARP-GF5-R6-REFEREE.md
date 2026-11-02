# HYP-105 / issue #230 — AA4-R6ALIGN: independently proved sharp GF(5) signed weight for ORIGINAL produced B/B-overlap

**Scope:** mathematical all-h ORIGINAL six-source-ID theorem and independent
exact finite GF(5) certificates. Strict child Draft of PR #707 at frozen
`1653964635731839fbdab783b58644b514c99a5c`. NO main change,
no merge/closure, no theorem-exponent promotion. This reviewer is the AI
performing the technical proof analysis itself, not a claim of another referee.

## 1. Why the previous R6 coefficient was unnecessarily weak

Historical independently checked ten-sign tables (#687/#688) give EVERY
ORIGINAL B/B-overlap source sixset a total GF(5) signed-event mass in

```
  {53526, 53838}  (six versus three out of nine canonical C4/C4 types).
```

Because the Branch A dense proof does NOT generate arbitrary B/B sixsets:
it generates ONLY the image of unblocked coordinate-proper ORIGINAL
three-edge physical paths, it is possible that its **image** lies entirely
inside one of these two classes. No earlier global `53526` uniform
floor investigated this restriction.

The mathematical result below is that ALL produced ORIGINAL BBo sixsets
are in the THREE `53838` templates; the other SIX `53526` types can
still exist as valid positive GF(5) sixsets, but are not produced via this
specific aligned physical three-path bridge. Therefore the strengthened
bound is **scope-specific and sharp**, not a false universal improvement
for all BBo sixsets.

## 2. Original source model and exact canonical six IDs

Fix every dyadic `s=2^h>=2`, actual symplectic `W(3,s)`, and complete
separately globally pair-injective, arbitrarily correlated fixed
`f: P -> binom([a],2)` and `g: L -> binom([a],2)`. A retained CORE
is any subset `I` of actual original source incidence flag IDs.
Every ORIGINAL flag contributes BOTH opposite-corner physical diagonals.

Take a genuine ORIGINAL B/B-overlap sixset Q produced by a good,
unblocked, coordinate-proper, directed physical 3-path. Its true GQ
projection is `q--ell--p--r`; the UNIQUE original three anchors are

```
  column 0 = (p,ell), column 1 = (p,r), column 2 = (q,ell).
```

The other **three original flags** are columns 3,4,5. These labels are
named ORIGINAL incidence IDs, not geometric placeholders. Their actual
original point and line factors are pairwise distinct and outside the
repeated factors, as proved by the proper path and no-blocker hypotheses.

On the LEFT, the doubled pair is `(0,1)` (the same original point p);
the remaining four named columns are `(2,3,4,5)) forming a coordinate
C4 in the original six-column dual. On the RIGHT, the doubled pair is
`(0,2)` (the same original line ell); the other four columns
`(1,3,4,5)` form a coordinate C4. The physical doubled-factor coordinate
symbols lie OUTSIDE each C4's coordinate symbols, by the accepted
six-coordinate degree-two condition.

## 3. NEW all-h center-alignment iff source physical 3-path is produced

**Lemma A (unique middle owner):** In any simple C4 on four distinct
named ORIGINAL columns, removing the distinguished anchor column (2 on
left or 1 on right) leaves a UNIQUE source-factor chain on the three
nonanchor columns 3,4,5. The middle original column is exactly the
vertex OPPOSITE the anchor column in the original named-column C4.
The other two original columns become its endpoints.

Proof: the named-column graph itself is the coordinate-sharing C4.
Removing one anchor vertex leaves a three-vertex simple path; the
unique degree-two remaining vertex is opposite the removed anchor.
Its physical path-edge owner must be the second of the three
ORIGINAL source-flag owners.

**Lemma B (iff):** The two typed coordinate P4 owner sequences give the
SAME physical three-edge path, up to simultaneous reversal, **iff**
their middle ORIGINAL ID is the SAME. Indeed, for three distinct named
owners, specifying the middle fixes their undirected 3-owner chain,
and fixes the source owner order up to reversal on BOTH typed factors.
The physical vertices are the coordinate intersections of consecutive
typed source-pairs, with the endpoints uniquely supplied by the first
and last typed factor labels. Each underlying ORIGINAL flag retains
BOTH diagonal physical edges, so independently choosing the two typed
factor orientations yields a genuine physical edge, not an
unjustified synthetic edge. No randomness of f,g is invoked.

Consequently a produced original Q always has matching left/right
opposite centers. Conversely an original BBo sixset with center
alignment and THREE path owner IDs in CORE produces EXACTLY two
directed reverse genuine physical three-paths; no projection anchor
needs to be retained in CORE. If centers differ, no such good/unblocked
path exists, even when the FULL source has all six flags.

**Count:** each four-element named-column set has exactly THREE C4
structures, one for each possible opposite center among {3,4,5}.
There are 3*3=9 combined left/right templates. Exactly THREE have
equal centers, SIX unequal. This is a symbolic all-h theorem because
there are only nine local column-dual patterns and the original geometry
does not alter their classification.

## 4. NEW third independent GF(5) exact counting method

A six-original-flag signed event consists of a balanced 3+3 sign pattern
`sigma_i`, with `sigma_0=+` as representative modulo global negation.
Every source column has four nonzero GF5 coefficients totaling 4 modulo 5;
there are exactly 51 palettes. For the twelve named physical coordinate
incidences, form the 12-edge two-color multigraph `H` on the same
six ORIGINAL columns, with each column degree 2 on each color.

After choosing orientations, the coordinate cancellation and checksum
equations are equivalent to an incidence equation

```
  B_H x = b (mod 5),  x_e in {1,2,3,4},  b_i=4 sigma_i.
```

**Our referee adds an exact THIRD oracle**, mathematically separate from
the two historical #687 algorithms (edge-deletion inclusion/exclusion
and nonzero-chord spanning-tree enumeration).

Let `omega` be a formal primitive fifth root of unity; choose potential
`phi_0=0` on one named ORIGINAL column. Character orthogonality
and `sum_{t=1}^4 omega^{t(u-v)}=4` if u=v, otherwise `-1`, give

```
 count(H,b) = 5^(-5) SUM_{phi_1,...,phi_5 in GF5}
                omega^(-b.phi)
                PROD_{(i,j) in E(H)}
                   (4 if phi_i==phi_j else -1).
```

The exponent sums of all demands vanish, allowing us to fix `phi_0`
and remove exactly one global potential factor 5. Group the product
weights by exponent `0..4`, giving exact integer buckets `C_k`.
Scaling all potentials by `t in GF5^*` permutes the four nonzero
exponents, so `C_1=C_2=C_3=C_4`. Using
`1+omega+omega²+omega³+omega⁴=0` yields the **INTEGER-ONLY** formula

```
       count(H,b) = (C0-C1) / 3125.
```

The implementation enumerates precisely `5^5=3125` potentials per
signed event, and verifies the nonzero bucket equality and exact
integer divisibility; no complex roots, floating-point rounding,
inclusion/exclusion subsets, or spanning-tree current solver is
used in the new oracle.

For ALL nine canonical two-colored BBo templates and all TEN
global-sign-unordered balanced masks (90 events), the exact result is:

| Original six-column BBo type | Number of templates | GF5 ten-sign mass | Proper source path fiber |
|---|---:|---:|---:|
| Matching left/right middle source ID | 3 | **53838** | Exactly 2 reverse directed paths |
| Different middle source IDs | 6 | 53526 | No produced path |

The third Fourier method also compares to BOTH older independent exact
algorithms in the tests; all three agree. As a finite algebra identity,
this table applies for EVERY genuine original W(3,s) and legal f,g,
because any sixset belongs to one of the nine named-column templates.

## 5. New sharp source-specific R3 risk floor

Let `D6(f,g)` count true six-original-ID aligned D6 motifs;
let `U_prod(f,g;I)` count DISTINCT produced ORIGINAL BBo sixsets whose
three nonanchor source flag owners are in CORE I; and let
`U_other` count OTHER (not produced) original BBo sixsets disjoint
from those first two classes. Each original sixset contributes
its own ten signed events in expectation over the independently
uniform 51-valued GF5 coefficient palettes. The signed-event risk
`R3` is a SUM of 3+3 event probabilities, **not** a union probability.

The exact source-specific accepted lower contribution is

```
51^6 R3(f,g) >= 54162 D6(f,g)
                +53838 U_prod(f,g;I)
                +53526 U_other(f,g).
```

Other accepted GF5 classes give additional NONNEGATIVE terms and are
not silently counted in any of these three disjoint source families.
The coefficient `53838` for produced BBo is ATTAINED by all three
aligned physical templates; it cannot be raised uniformly in that
specific aligned image class. The factor `312` improvement over the
historical 53526 is exact per produced true ORIGINAL sixset.

Combining this slice with the **separately proved original source dense
branch** `U_prod>=s^6/8` and heavy branch `D6>=delta s^6`,
both required as explicit inputs from the previous Branch A proof,
strengthens its conditional conclusion to

```
 R3(f,g) >= [min(54162*delta,53838/8)/51^6] s^6,
```

for all sufficiently large dyadic orders and all fixed admissible
correlated f,g. This does NOT improve the universal ASET exponent,
does NOT bound risks for any deterministic fixed GF5 column coefficient
assignment, and does NOT assert a numerical h0 without actual
published graph-supersaturation constants.

## 6. Real-original finite falsifiers and code scope

A source-first algorithm independently constructs a genuine original
nonincident q,r and its UNIQUE original q--ell--p--r anchor, plus three
genuine independent original incidence flags, for W32 and W34.
It separately globally injects COMPLETE original point and line label
maps in the MINIMAL physical alphabet to realize ALL NINE named BBo
C4/C4 structures with the SAME six source flag IDs. For each of those
18 true-original model instances:

- rederive ORIGINAL double point/line source factors and named six
  coordinate-incidence duals from the actual six flag IDs;
- verify exactly 0/2 PHYSICAL three-paths when the FULL projection
  anchors are omitted from the retained three-owner CORE;
- check the new center criterion and independent 10-sign Fourier vector;
- reindex the six ORIGINAL flags in reverse order, then reconstruct
  the SAME canonical source names and invariant classification;
- cross-check all 90 template events against the old independent
  exact inclusion/exclusion oracle and selected events against the
  separate tree-current oracle;
- fail closed on invalid original or physical source profiles.

Finite runs are falsifiers of source indexing and exact integer
arithmetic. The all-h original source/image and GF5 algebra statements
are supplied by Sections 2–5, not inferred from W32/W34.

**Next mathematical priority:** independently audit the remaining
global assembly (R2 graph-C6 heavy-tail into R6 GF5), including
quantifiers and whether the chosen core image count really supplies
the independently counted original-sixsets; then explore deterministic
GF5 assignments/extraction rather than further coefficient polishing.
