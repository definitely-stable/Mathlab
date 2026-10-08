# HYP-001 / HYP-002 — two-cell theorem and three-cell capacity conjecture

Program: **LENT-001 exact additive set families**, separate from TOM.
Issues: [HYP-001 #24](https://github.com/definitely-stable/Mathlab/issues/24),
[HYP-002 #25](https://github.com/definitely-stable/Mathlab/issues/25).
Status: **PHASE A, falsification-first**.
Last mathematical review: 2026-10-08.

## Model and claim ledger

Fix an **odd prime** q and m coordinates. Distinct nonzero column
vectors a_x belong to F_q^m and have support size at most w. A family
is **ASET exact through d=2** when the sums of distinct subsets with
0, 1, or 2 columns are all different. Write its largest size as
A_q^set(m,w,2). This does *not* claim collision resistance for larger
active sets, integer (non-modular) counters, or robustness to arbitrary
repeated insertions.

| ID | Statement | Classification | Novelty status |
|---|---|---|---|
| HYP-001-A | A_q^set(m,2,2) = Theta_q(m^(3/2)) as m grows | DERIVED THEOREM (proof below) | NOT ESTABLISHED |
| HYP-001-B | Projective-plane incidence yields two-update deterministic witnesses | CONSTRUCTION / DERIVED RESULT | CLASSICAL |
| HYP-002-A | Every linear 3-uniform hypergraph yields an odd-q exact d=2 ASET family | DERIVED LEMMA | NOT ESTABLISHED |
| HYP-002-B | A_q^set(m,3,2) = Omega_q(m^2) | DERIVED RESULT | CLASSICAL CONSTRUCTION |
| HYP-002-C | A_q^set(m,3,2) = O_q(m^(5/2)) | DERIVED THEOREM (proof below) | NOT ESTABLISHED |
| HYP-002-D | A_q^set(m,3,2) = Theta_q(m^2) | **CONJECTURE** | UNVERIFIED |

The words "DERIVED THEOREM" mean a self-contained mathematical argument
is supplied, **not** that Lean has verified it or novelty is established.
Finite CI checks only concrete cases, not the quantified asymptotics.

## HYP-001-A — two-cell capacity

### Lower bound, constructive

Let p be an auxiliary prime, **unrelated to the sketch field q**.
The projective plane PG(2,p) has n=p^2+p+1 points and n lines, each
point on p+1 lines and any two points share exactly one line. Its
point-line incidence bipartite graph has 2n vertices, n(p+1) edges,
and no four-cycle.

For every edge of the incidence graph, use an F_q^(2n) column with
unit entries at its two endpoints, zeros elsewhere. Distinct
one-edge columns have support exactly two. For a pair of distinct
edges, either their endpoints are disjoint (sum support four with
all values 1) or they meet in one endpoint (sum support three with
the common value **2 != 0,1** in odd characteristic). Thus empty,
singleton and two-edge subset sums have different forms.

Two different pairs of edges cannot have identical sums. In the
shared-endpoint case, the unique value-2 position fixes the center
and two remaining endpoints fix both edges. In the disjoint case
equal sums would be two different perfect matchings on the same
four endpoints, producing a C4, which is forbidden. Therefore all
subset sums of size at most two are distinct.

Consequently

    A_q^set(2(p^2+p+1), 2, 2) >= (p+1)(p^2+p+1).

Prime orders p suffice for Theta lower growth along an unbounded
sequence. For any sufficiently large m, choose an auxiliary prime
p between constant multiples of sqrt(m) with 2(p^2+p+1)<=m;
Bertrand's postulate and monotonicity in m extend the lower bound
to Omega(m^(3/2)) for **every** sufficiently large m.

### Upper bound, reduction to C4-free bipartite graphs

First remove support-one columns: there are at most (q-1)m.
The remaining columns have support exactly two.

Randomly partition the m coordinates into two labeled parts L,R
with equal independent probability. A given support-two column is
split by the partition with probability 1/2, so **some partition**
preserves at least half the support-two columns. Partition the
preserved columns into (q-1)^2 classes indexed by their nonzero
coefficient at the L endpoint and at the R endpoint.

Each class forms a **simple C4-free bipartite graph** on L,R.
Indeed, a four-cycle at L vertices u,v and R vertices x,y
would yield the signed equality

    a_(u,x) + a_(v,y) = a_(u,y) + a_(v,x),

because the coefficients are the same at each labeled endpoint
within a class. These are four distinct columns: two-versus-two
is an illegal exact-ASET collision.

For a C4-free bipartite graph with |L|,|R|<=m, each pair of right
vertices has at most one common left neighbor, so

    sum_(u in L) binom(deg(u),2) <= binom(|R|,2).

By Cauchy-Schwarz/Jensen,
E^2/|L| - E <= |R|(|R|-1);
therefore E <= |L| + sqrt(|L|)*|R| = O(m^(3/2)).
Handle |L|=0 separately. Sum the (q-1)^2 coefficient classes,
undo the factor 1/2 from partitioning and add support-one
columns. This proves O_q(m^(3/2)) and hence HYP-001-A.

**Classification:** likely an elementary application of known
Zarankiewicz bounds with classical projective incidence. Novelty
audit is REQUIRED before claiming a new theorem. Do not publish
the exponent as an original discovery.

## HYP-002-A/B — linear triples imply a quadratic lower bound

A 3-uniform hypergraph is **linear** when two different blocks share
at most one vertex (equivalently, every vertex pair appears in at
most one block). Associate to each block its zero-one incidence
vector, over odd F_q.

We prove injectivity for empty, singleton and unordered pairs of
**distinct** blocks.

- Empty has all-zero sum. Each singleton has support three.
- Two disjoint blocks sum to six 1s. Two blocks meeting in one
  vertex sum to four 1s and a single 2 (support five).
  Hence different subset cardinalities cannot collide.
- If two pairs of blocks have the same sum and each pair overlaps,
  the unique 2-coordinate fixes their common vertex v; any other
  coordinate u fixes the *unique* block containing {v,u}.
  Thus the unordered pair of blocks is identical.
- If one pair overlaps and the other is disjoint, one sum has a
  2 and the other does not, impossible.
- If both pairs are disjoint, equality of coordinate sums means
  the same six-point union. A block in an alternative partition
  into two triples contains at least two points from one of the
  original triples. Linearity forces that block to equal the
  original triple, hence the other is equal too.

So every linear 3-uniform hypergraph is ASET exact for odd q.
This lemma does **not** apply without further proof to q=2;
a Pasch configuration is a concrete counterexample.

A Steiner Triple System STS(m) is linear and has m(m-1)/6 blocks,
for every m congruent to 1 or 3 mod 6 (Kirkman's classical
existence theorem). Therefore

    A_q^set(m,3,2) >= m(m-1)/6  when m = 1 or 3 (mod 6).

Since admissible STS orders have bounded gaps, monotonicity gives
A_q^set(m,3,2) = Omega(m^2) for arbitrary large m.

For an explicit algebraic infinite sequence use the triples of
F_3^r: three distinct x,y,z satisfy x+y+z=0 coordinatewise.
Every pair determines a unique third distinct point because
q_geometry=3 (separate from q_sketch). With m=3^r, this creates
exactly m(m-1)/6 blocks.

## HYP-002-C — general O_q(m^(5/2)) upper bound

Support-one and support-two columns together contribute at most
O_q(m^(3/2)) by HYP-001-A (the subsequence remains exact).

For all remaining support-three columns, randomly assign each
coordinate to one of THREE labeled classes X,Y,Z. A given triple
hits each class exactly once with probability 3!/3^3 = 2/9.
Thus some partition retains at least a 2/9 fraction of these
columns. Split retained columns by their three nonzero
coefficients (alpha,beta,gamma), yielding (q-1)^3 classes.

Fix such a class and x in X. The link of x is the simple bipartite
graph on Y,Z: each triple (x,y,z) corresponds to the edge y-z.
A C4 in this link, with y1,y2 and z1,z2, gives

    a_(x,y1,z1)+a_(x,y2,z2)
       =a_(x,y1,z2)+a_(x,y2,z1),

with coefficient 2*alpha at x on both sides, and matching
coefficients at the other coordinates. This is an illegal d=2
collision. Each link is therefore C4-free and contains at most
O(m^(3/2)) edges by the same elementary graph counting argument.

Sum over at most m possible x, over the fixed (q-1)^3
coefficient patterns, then undo the 2/9 partition fraction:
the total number of weight-three columns is O_q(m^(5/2)).
Adding the lower-support columns proves the claimed bound.

This is **not** an O(m^2) proof. The missing exponent 1/2 is the
specific HYP-002 research gap.

## Falsification and parameter-boundary checks

Finite construction/test harness: research/locality_transition.py,
research/test_locality_transition.py.

1. PG(2,2): m=14, V=21, w=2; PG(2,3): m=26, V=52.
2. STS(7): m=7, V=7; affine STS(9): m=9, V=12; affine STS(27):
   m=27, V=117.
3. Check exact ASET subset sums using pre-existing G1A code,
   independently cross-check small fixtures with a separate oracle.
4. A four-cycle must create a collision in weight-two codes.
5. The four linear triples (012),(034),(135),(245) form a Pasch
   configuration: a collision exists in F_2 but not in odd F_q.
6. Nonlinear blocks (012),(345),(013),(245) must collide even in odd
   fields because the two pair-sums are identical.

These are finite correctness checks, NOT proof of an asymptotic
theorem or mathematical novelty.

## Prior-art map and non-equivalences

- Classical Zarankiewicz / Kővári–Sós–Turán / Reiman C4-free
  bipartite edge counting; finite projective-plane incidence
  supplies standard sharp-order witnesses.
  https://doi.org/10.1016/j.procs.2021.11.053
  https://arxiv.org/abs/2506.23942
- Kirkman's STS existence and design-theoretic constructions:
  https://encyclopediaofmath.org/wiki/Steiner_triple_system
  https://www.math.princeton.edu/events/existence-designs-2014-04-10t203004
- Liu, Shangguan, Zhang, *Sharp bounds for uniform union-free
  hypergraphs* (2026), adjacent but **union-preservation is not
  modular multiplicity preservation**; exact implication/reduction
  must be proved before moving a theorem.
  https://arxiv.org/abs/2605.11949
- Cilleruelo, Serra, Wötzel, *Sidon set systems* (2018):
  its "sumsets A+B" are not automatically sums of incidence columns.
  https://arxiv.org/abs/1802.10511

No claim of comprehensive prior-art coverage, originality of the
HYP-001 exponent, or HYP-002 openness is authorized. A separate
source-to-definition audit is mandatory before publication.

## Decision gates and prospective primitive

HYP-001: promote proof only as a **derived classical-order baseline**.
HYP-002: retain CONJECTURE, request improved upper or superquadratic
construction and explicit collision oracle. Choose between
THEOREM_CANDIDATE / COUNTEREXAMPLE / CLASSICAL / NO_SIGNAL *after*
definition-level prior-art review.

A possible future Rust primitive would be a narrowly scoped
**bounded-cardinality additive identifier** with 2/3 coordinate
updates and deterministic recovery for at most two simultaneously
active IDs. The existence of compact coordinates does **not**
automatically imply efficient encoding, indexability, decoder
speed, deletion safety under over-capacity inputs, or competitive
product economics. No crate creation is authorized by Phase A.
