# HYP-105 / issue #230 — D6-Z: exact original-incidence wedge-moment transport; image-only GF5 information barrier

**2026-10-13. RESTRICTED_THEOREM_C + exact ORIGINAL W32 falsification.**
Strictly stacked on [D6-Y #425](https://github.com/definitely-stable/Mathlab/pull/425)
pinned parent HEAD \`73ddbae8e12e6444b19069d541082d8a46094a79\`
(all 4 GitHub-hosted parent CI SUCCESS). No \`main\` mutation
or merges. #230/#176/#169 and Branch A/B remain OPEN.

## 1. Fundamental distinction: image-only physical capacity versus ORIGINAL GF5 factors

The sharp D6-Y physical-image adjacency theorem is a near-complete
specialization of classical Ahlswede–Katona extremal graph theory,
DOI https://doi.org/10.1007/BF01902206. It is independently true
on each typed physical image E(f), E(g), without the ORIGINAL
point-line incidence edges of W(3,s). In particular it is invariant
under ANY independent permutation of the ORIGINAL point factors
or line factors that reassigns the SAME physical edge images.

The seven-GF5-positive factor S_s is NOT image-only: each term
comes from SIX DISTINCT ORIGINAL point-line incidences, preserving
their ORIGINAL positions, including their endpoint multiplicities
and the physical positional D6 matching/ B/B-overlap distinction.
An image-only physical adjacency bound can be used as a valid
GLOBAL constraint in a joint optimization, but CANNOT be treated
as an exact formula for S_s, or as a sufficient seven-class indicator.

## 2. Theorem Z1 — exact all-h wedge transport across six ORIGINAL incidences

Fix s=2^h,h>=1. Let V=(s+1)(s²+1), Delta=s+1,
N=V*Delta=number of DISTINCT ORIGINAL point-line incidences in
W(3,s), a=min{a:C(a,2)>=V}, and f,g arbitrary COMPLETE
independent typed injections into physical K_a pairs.

For Q an unordered SIX-DISTINCT-incidence subset, let the ordered
incidence positions be e_i=(p_i,l_i), and define

    tau_L(Q)=sum_{physical coordinates c} C(
                      #{i: c in f(p_i)},2),
    tau_R(Q)=sum_c C(#{i: c in g(l_i)},2).

Repeated ORIGINAL points/lines in the six **incidence positions**
count WITH MULTIPLICITY in the degrees and every i<j wedge.
Consequently, exactly and without probability assumptions,

    tau_L(Q)=sum_{i<j}|f(p_i) intersect f(p_j)|
    tau_R(Q)=sum_{i<j}|g(l_i) intersect g(l_j)|.

Because typed ORIGINAL point and line incidence degrees are Delta,
among all unordered incidence-position PAIRS:
- for each of V original point factors, C(Delta,2) pairs of
  original incidence positions share that ORIGINAL factor and
  contribute exactly TWO physical-coordinate incidences;
- for each pair of DISTINCT ORIGINAL factors, Delta² incidence
  position pairs contribute ONE if their injected physical K_a
  pair edges share a physical coordinate, otherwise ZERO.

Let A(f)=sum_{p<q}1[f(p) physical-intersects f(q)],
and analogously A(g) for the independent right original line map.
Every two ORIGINAL incidence positions belong to exactly
C(N-2,4) different ORIGINAL sixsets Q. Thus

    sum_{Q in C(I,6)} tau_L(Q)
      = C(N-2,4)*[ 2V C(Delta,2) + Delta² A(f) ],

    sum_Q tau_R(Q)
      = C(N-2,4)*[ 2V C(Delta,2) + Delta² A(g) ].

This is an ALL-h double-counting IDENTITY for **arbitrary correlated
globally injective f,g**. It does NOT compute S_s and by itself
imposes no positive lower bound on the number of seven-GF5 classes.
It spans ALL C(N,6) original incidence sixsets, NOT only the
physical left A/B/C candidates or the exact seven accepted classes.

## 3. Theorem Z2 — sharp all-h two-sided wedge-moment envelopes

D6-Y bounds A(E) via m=K−V missing physical edges of K_a,
0<=m<=a−2. The complement H of m missing edges satisfies

    A(E)=a C(a−1,2)−2m(a−2)+sum_c C(deg_H(c),2).

The previous exact maximum has sum missing wedges C(m,2),
achieved when all m missing edges share a physical vertex.

For the exact minimum, convexity of binom(d,2) over
nonnegative integers with sum degrees 2m implies

    sum_c C(deg_H(c),2) >= max(0,2m−a).

This LOWER bound is attainable for every 0<=m<=a−2:
if 2m<=a, H is a matching of m physical edges. If 2m>a,
take a disjoint union of a−m simple paths covering all a
physical vertices, with m edges total. Precisely 2m−a
vertices have degree 2, the remainder degree 1, and no
higher degrees arise. An explicit construction uses a−m−1
single-edge components plus one longer path.

Therefore the **global-image adjacency interval is SHARP
at BOTH ends**:

    A_min=a C(a−1,2)−2m(a−2)+max(0,2m−a),
    A_max=a C(a−1,2)−2m(a−2)+C(m,2).

Plugging those into Z1 yields the **sharp exact all-h interval**
for each total six-incidence wedge moment,
independently on the point and line typed sides:

    C(N−2,4)*[2V C(Delta,2)+Delta² A_min]
      <= sum_Q tau_X(Q)
      <= C(N−2,4)*[2V C(Delta,2)+Delta² A_max].

Extremal assignments of both typed images are constructively
attained, and the ORIGINAL GQ incidence relation is unchanged.

This is a straightforward complement degree-convexity/
double-counting fact, not a claim of new graph extremal theory.
It is a physically correct necessary global constraint
useful for future incidence-aware GF5 moment certificates.

## 4. Theorem Z3 — geometry-aware collinear pair transport

For a true ORIGINAL W(3,s) generalized quadrangle, any two
distinct original points share AT MOST ONE original line (and
likewise the dual statement for lines), so exactly

    C_src=V C(Delta,2)

unordered ORIGINAL point factor pairs are collinear, counted
ONCE. Define the incidence-aware physical adjacency statistic

    B_f=sum_{p<q, source-collinear}1[f(p) intersects f(q)].

Fix the physical IMAGE E(f), of size V, and uniformly randomly
permute its V pair labels over the V ORIGINAL point factors.
Every unordered pair of distinct ORIGINAL point factors gets
a uniformly random unordered pair of distinct physical image
edges. Hence

    E_perm[B_f | E(f)] = C_src*A(E(f))/C(V,2).

The identical formula holds for the right line map g over
source pairs of concurrent original lines. This is a true
all-h geometry-conditioned EXPECTATION identity, not a
deterministic lower bound on B_f, or a seven-GF5 count.
In particular the physical IMAGE statistic does not fix the
specific source collinearity correlations, only their mean
under this independent random reassignment.

## 5. ORIGINAL W32 seven-GF5 exact falsification of an image-only shortcut

For s=2, V=15 and a=6, K=C(6,2)=15=V. Thus EVERY
globally injective physical point or line assignment uses the
ENTIRE physical K6 edge IMAGE, with the SAME physical
adjacency A(E)=6 C(5,2)=60. No image-only function, even of
the complete two physical image graphs, can distinguish any
two complete W32 f,g label assignments.

Yet the two canonical true ORIGINAL incidence-position-aware
W32 models S68 and S72 use the same full physical K6
image on BOTH typed sides and even the SAME left point map f,
while their accepted all-seven GF5-positive counts differ:

    S_seven(f,g68)=68,    S_seven(f,g72)=72.

This is an exact finite **NON-IDENTIFIABILITY** result for
the full seven-S objective from image-only physical adjacency.
It is not an all-h counterexample to a POSITIVE lower bound.
The full selected nonnegative GF5 numerator likewise remains
position-aware; it is never confused with total exact R3 risk.

To audit a more generous 2-sided second-order physical proxy,
enumerate ALL 62,370 actual left-2-regular ORIGINAL sixsets
for each true W32 map (including physical A/B/C left classes).
Count those whose right physical coordinates also have
exactly six degree-two coordinates. Every accepted GF5 class
lies in this proxy, but the proxy includes additional
REJECTED candidate sixsets, such as misaligned physical
A/A cycles or C/C sectors. Preserve the actual six ORIGINAL
incidence IDs in all classifications. Produce and
independently recheck at least one actual positive and
one actual false-positive witness per scheme.

Therefore **even exact two-sided 2-regularity is necessary,
not sufficient, for the accepted seven-family classification**.
For a>=7, the scalar equality tau_L=tau_R=6 is weaker still:
a physical seven-vertex tree with six distinct edges and
degree sequence (3,2,2,2,1,1,1) has wedge 6 but is NOT a
six-coordinate 2-regular support.

None of these finite negative tests proves an infinite
correlated counterfamily, a global Omega(s^6) lower, or a
strict upper for full R3. They prevent a mathematically
UNSOUND transfer from the classical D6-Y graph bound directly
to the seven-positive ORIGINAL incidence GF5 objective.

## 6. Independent reproducible falsifiers and D6-AA gate

- True ORIGINAL W(3,2) / W(3,4) incidence-pair sum
  independently checks Z1 in O(N²) without extracting the
  physical image wedge by the same histogram algorithm.
- Exact original W(3,2), W(3,4), W(3,8) paired
  globally injective point/line extremizers for both
  ends of the Z2 physical image interval.
- A separate 8-incidence toy host enumerates ALL C(8,6)
  sixsets to falsify the incidence-pair transport identity
  independently, including original repeated sites.
- Actual source GQ collinear point/line counts and a
  4! toy label-image permutation oracle check Z3.
- W32 complete 62,370-candidate seven-family census for
  S68 and S72, plus independent positive and false
  2-regular proxy witness classifications.
- Fail-closed noncanonical, duplicate physical pairs,
  malformed original incidences, missing factors or
  source nonregularity, explicit computational budgets.

**D6-AA:** Do not merely add more image-only global inequalities;
W32 proves these lose necessary ORIGINAL placement information.
The next admissible proof step must combine SOURCE incidence-aware
physical wedge distributions (not just their overall sum)
with higher-order conditions distinguishing D6 matched
column cycles, B/B incidence overlaps and the other accepted
GF5-positive classes. Determine whether a source-conditioned
higher moment/dual is positive uniformly for all f,g, or give
an exact restricted no-go; no Branch A/B claim before all-h proof.
