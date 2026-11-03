# HYP-105 / issue #230 — AA4-DETG5: deterministic ORIGINAL GF(5) extraction from a selected sixset family

**Scientific scope:** a genuinely new deterministic theorem about any SELECTED
finite collection of ORIGINAL source six-ID configurations on the SAME
fixed true symplectic W(3,2^h) geometry and the SAME complete separately
globally pair-injective, possibly correlated, maps f,g. It does not
change the fixed maps, manufacture original flags, independently resample
overlapping sixsets or pretend that Branch A's lower bound in EXPECTATION
is a lower bound for every deterministic GF5 assignment.

The present finite implementation independently tests true ORIGINAL
W(3,2)/W(3,4) source factor geometry. The mathematical theorem below
is valid for every dyadic order h and every selected subfamily, and is
not extrapolated from these two finite computations.

Strict Draft child of frozen parent #709 at
7b584ba44386cd20837bfcbed4ec163b5b0c3ca8.
No ancestor/main modifications, merge or issue closure.

## 1. The correct new question

A legal original source flag i=(p,ell) receives one of the 51 patterns

  omega_i=(a0,a1,b0,b1) in {1,2,3,4}^4,
  a0+a1+b0+b1 = 4 (mod 5),

with slots corresponding EXACTLY to the two sorted physical f(p)
coordinates and two sorted physical g(ell) coordinates.

The original R3 is an expectation over independently uniform omega_i.
The sharp six-ID flow sum is 54162 on each genuine original D6 and
53838 on each B/B-overlap sixset PRODUCED by the good unblocked
ORIGINAL three-path bridge; #708 proves the distinction between
the three aligned and six unaligned BBo profiles.

A large expectation for the sum of signed events on all legal source
sixsets does **NOT** force a large signed-event count on every
deterministic assignment. Even the statement that a single sixset
has a positive expected number of signed events never forces that
sixset to collide on every GF5 palette assignment.

This slice addresses the other direction rigorously: find one
deterministic source-flag palette assignment avoiding a SPECIFIED
selected family of the two proved motif classes.

## 2. New all-h uniform finite-family zero-risk theorem

Let M be ANY finite set of DISTINCT ORIGINAL six-flag subsets,
each either an accepted genuine aligned D6, or the image of an
unblocked good coordinate-proper physical path giving a genuine
aligned ORIGINAL B/B-overlap class. Each sixset's six ORIGINAL
source flag IDs are immutable; different sixsets may SHARE ANY
NUMBER of original IDs. A single palette variable omega_i is reused
wherever that ORIGINAL ID reappears.

For each Q in M and each of its ten unordered balanced 3-versus-3
sign partitions sigma, let X_(Q,sigma)(omega) be the INDICATOR
that all 12 physical-coordinate signed cancellation conditions hold.
Set

  Z_M(omega) = sum_(Q in M) sum_(sigma) X_(Q,sigma)(omega),

an integer >=0, not a union probability.

For fixed legal f,g, by the previously independently checked GF5
signed masses and LINEARITY ALONE,

  E[Z_M] =
      (54162 * |M_D6| + 53838 * |M_BBo-produced|) / 51^6. (E1)

This identity is true despite arbitrary overlaps of M, because each
individual Q has six distinct ORIGINAL flags and hence its six
palettes have the required independent uniform 51-valued law.
The sixset indicators as a FAMILY need not be independent and
can have positive or negative covariance.

Since Z_M is a nonnegative integer, E[Z_M]<1 implies the existence
of a deterministic assignment omega with Z_M=0. A worst-case
class-independent sufficient bound is

  |M| <= floor((51^6 - 1)/54162) = 324882. (E2)

For a pure aligned BBo-produced family the bound improves to

  |M| <= floor((51^6 - 1)/53838) = 326837. (E3)

For arbitrary mixtures, the SHARP weighted criterion is the exact
integer inequality

  54162 * |M_D6| + 53838 * |M_BBo-produced| < 51^6. (E4)

These are all-h mathematical existence results that require NO
assumption on independent motif events, NO geometric restriction
on overlaps beyond genuine original sixsets, and NO randomization
of the physical maps f,g.

**Important:** 51^6 = 17,596,287,801. This threshold counts ONLY
the selected sixsets M, not all possible ORIGINAL sixsets in W(3,s).
It does NOT establish a full-source deterministic ASET construction.

## 3. NEW exact conditional GF5 completion oracle

To construct omega rather than merely prove existence, fix any
already assigned subset A of ORIGINAL flags. The exact conditional
probability of X_(Q,sigma) is

  Count(Q,sigma,omega_A) / 51^(6 - |Q intersect A|),

where Count is the integer number of 51-valued palettes that can
complete the sixset while satisfying its signed conditions.

The new implementation computes Count WITHOUT enumerating
51^(6-|A|) palettes.

Take the physical column-dual multigraph of Q: six named ORIGINAL
column IDs, twelve genuine physical coordinate edges, two typed
f(p) slots and two typed g(ell) slots per original column.
Give every coordinate edge an orientation from its smaller named
column index to the larger. For a chosen sign partition sigma,
the signed palette constraints are exactly the nowhere-zero
incidence-current equation

  B_H x = b mod 5,    b_i=4*sigma_i,    x_e in {1,2,3,4}.

If a column palette is fixed, all four incident currents are forced
(and each fixed-fixed edge is checked for consistency).
Let U denote the remaining unfixed original columns and
E_free the ORIGINAL physical coordinate edges joining two
unfixed columns. The boundary currents give the residual demand
b'_v at each unfixed vertex v.

For each subset A of E_free, set all other free edges to zero
and permit arbitrary GF5 currents on A. If every component C of
the graph (U,A) has sum_(v in C) b'_v=0 mod 5, it has EXACTLY

  5^(|A| - |U| + components(U,A))

solutions, else zero. Möbius inversion therefore gives the exact
NONZERO-current completion count:

  Count = sum_(A subset E_free) (-1)^(|E_free|-|A|)
           1[each component has balanced residual]
           * 5^(|A|-|U|+components(U,A)). (E5)

All sums are INTEGER, with <=4096 edge subsets and in fact only
<=256 after one fixed column (every column has 4 incident edges).
The input contains full typed source coordinate slots; no
synthetic physical edge or column copy enters this calculation.
The first all-free step is independently reconciled against the
historical full palette 54162/53838 coefficients, and the
almost-complete states are separately verified by brute force
over the remaining 51 palette values.

This is a conditional AFFINE GF5 original-coordinate algorithm,
not the old unconditioned fixed-six-column Fourier-only oracle.

## 4. Derandomization by exact averaging, with overlap handled correctly

Let F(A) be the conditional expected signed-event count over the
remaining independently uniform ORIGINAL flag palettes. It is
the sum of the exact rational completion probabilities in (E5).
For any unassigned ORIGINAL flag i and all 51 legal palettes t,

  F(A) = (1/51) * sum_(t in PALETTES) F(A union {omega_i=t}).

Therefore choose a palette t that minimizes the next conditional
expectation, in deterministic lexicographic tie-breaking order:

  F(A union {omega_i=t}) <= F(A).

Repeat until every ORIGINAL ID occurring anywhere in selected M
has exactly one palette. All other source flag IDs may be given any
legal palette because they affect none of these selected sixset
events. After all chosen variables are fixed,

  F(full assignment)=Z_M(full assignment) in nonnegative integers
                       <= E[Z_M]. (E6)

In particular if (E4) holds then the greedy assignment necessarily
has ZERO events in M. No claim of computational tractability for
huge M is made: the current independent referee explicitly limits
the number of selected motifs per exact-CI run to avoid exponential
repeated subset enumeration. The all-h mathematical theorem itself
does not rely on this implementation cap.

The new code checks (E6) by a SECOND and simpler physical algorithm:
directly evaluate the 12 signed coordinate constraints on every
specified ORIGINAL sixset for ALL ten sign partitions. That direct
check does not call the affine IE completion count.

## 5. Actual original-source finite falsification

Hosted exact tests cover genuine full-source W32 and W34, not
six invented synthetic flag IDs:

- A planted TRUE nonincident original q--ell--p--r and its three
  real source owner flags yield the aligned produced BBo class,
  which has EXACTLY the expected weight 53838.
- A distinct genuine ORIGINAL six-point/six-line matching realizes
  D6 with EXACT signed mass 54162.
- A protected genuine W34 K4,4 source-owned CORE yields MULTIPLE
  overlapping produced ORIGINAL BBo sixsets under the SAME fixed
  maps f,g; palette variables are shared for repeated original IDs.
- Each selected family has its exact initial Fraction expected risk
  and a direct final signed-constraint census, which must agree with
  the conditional expected final integer.
- All 51 legal checksum palettes, malformed source labels, duplicate
  original Q, incomplete factor maps, unsupported source orders,
  exact worst-case threshold and selected almost-full conditional
  completion cases are independently tested.

The emitted JSON fixture contains a CONCRETE original flag ID ->
4-entry GF5 palette map with zero signed conflicts in a selected
genuine W32 BBo sixset.

## 6. Scientific conclusion and actual next frontier

The step is constructive and explores the logically distinct
DETERMINISTIC side of the problem. It proves that a very large
selected family (up to 324882 worst-case original sixsets) can
always be made collision-free, EVEN WITH arbitrary source-ID overlap.
This complements the Branch A expectation obstruction but DOES
NOT contradict it: the latter is about EXPECTATION over the
uniform 51-palette ensemble, whereas the new result is about
the EXISTENCE of a carefully chosen deterministic assignment
on a SELECTED finite motif family.

**Remaining actual research blocker:** to say something about
deterministic full-source ASET one must characterize the ENTIRE
ORIGINAL signed-event conflict hypergraph under one fixed map f,g,
including the other five accepted leading six-coordinate classes
and possible higher-order events. Only then can a global sparsity,
local lemma, algebraic unsatisfiability, or extraction claim
be rigorously attempted. Do not generalize (E2) to all sixsets,
do not claim the universal HYP-105 conjecture proved in all
possible models, and do not merge this scientific Draft.
