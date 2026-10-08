# HYP-002-B — Sharp quadratic three-cell capacity

**Status: DERIVED THEOREM; novelty NOT ESTABLISHED; Lean NOT STARTED.**
This correction supersedes the non-sharp O_q(m^(5/2)) upper and the
HYP-002-D CONJECTURE classification in HYP-001-002-LOCALITY-TRANSITION.md.
The former document remains an historical Phase-A record.

**Source-novelty checkpoint (THEOREM-GAP-004, 2026-10-08):** [Lefmann (2005)](https://doi.org/10.1017/S0963548304006625) has \`N_q(m,4,r)=Theta(m^(ceil(4r/3)/2))\` for odd characteristic, hence at r=3 already gives a **stronger four-wise-independent** weight≤3 family of order Theta(m²). Four-wise independence implies ASET d=2, but ASET does not imply it. Therefore the *lower-bound/construction exponent is prior art*; this document's separate ASET **upper** proof remains a valid derived result, but publication-level novelty of the exact finite upper and constants has NOT been established. See [four-stage audit](THEOREM-GAP-004-FOUR-STAGE-AUDIT.md).

## Exact finite theorem

Let F_q be any finite field (q>=2) and let A_q^set(m,w,2) denote the
maximum family of distinct, nonzero vectors in F_q^m with at most w
nonzero coordinates such that all subset sums of 0,1,2 distinct
vectors are pairwise different.

Write r=q-1 and C(n,k) for the binomial coefficient. For every m>=1,

    A_q^set(m,3,2)
       <= r*m + r*r*C(m,2)
            + min(r*r*r*C(m,3), r*r*C(m,2)+C(r*m,2)).

Consequently, for any **fixed odd prime power q**,

    A_q^set(m,3,2) = Theta_q(m^2).

This is an explicit finite upper bound and matching-order lower bound,
not an originality claim.

## Proof: prefix-pair C4 exclusion

A vector of support exactly three has a unique canonical encoding

    ((i,a),(j,b),(k,c)),  i<j<k,  a,b,c nonzero.

Represent it as a bipartite edge between prefix L=((i,a),(j,b))
and suffix R=(k,c). There are at most r² C(m,2) possible prefixes
and r*m possible suffixes. Every support-three vector produces one
distinct edge.

A four-cycle with prefixes L1,L2 and suffixes R1,R2 would produce
four distinct columns v11,v12,v21,v22 satisfying

    v11 + v22 = v12 + v21.

This holds coordinatewise, even if the prefixes overlap. The two
sides consist of two distinct columns each, so such a cycle is
incompatible with exact ASET d=2.

For each used prefix L, write d_L for its degree. Each unordered
pair of suffixes can occur in at most one prefix neighborhood;
otherwise there is a four-cycle. Hence

    sum_L C(d_L,2) <= C(r*m,2).

Every integer d>=1 satisfies d<=1+C(d,2). Therefore

    number of support-three columns
      = sum_L d_L
      <= number of used prefixes + sum_L C(d_L,2)
      <= r² C(m,2) + C(r*m,2).

This count is also bounded by the number of all weight-three
columns r³ C(m,3). The support-one/two columns number at most
r*m + r² C(m,2). Add these contributions to obtain the stated
finite bound. QED.

Unlike the former three-partition/link-graph approach yielding
O_q(m^(5/2)), this single prefix-fiber graph immediately gives
O_q(m²). No probabilistic partition, solver cutoff, or asymptotic
heuristic is needed.

## Matching lower bound for odd characteristic

A linear 3-uniform hypergraph (any two distinct triples intersect
in at most one coordinate) supplies a pair-sum-exact family by
encoding every triple as a 0/1 incidence column.

Proof details: for two distinct triples, their sum either has
six ones (disjoint triples) or four ones plus one nonzero two
(intersecting triples). These are distinct from singleton and
empty states. In the intersecting case the coordinate with value
two and any other coordinate determines one of the two triples
uniquely by linearity. In the disjoint case, any alternative triple
on the same six-coordinate union would share at least two points
with one original triple, hence is the same triple, fixing the pair.
Therefore pair-sums are injective for odd fields. This implication
is false in characteristic two in general (Pasch counterexample).

Classical Steiner triple systems STS(n) exist for every admissible
n congruent to 1 or 3 modulo 6, and have n(n-1)/6 triples.
For any sufficiently large m choose such n<=m with m-n<=3;
zero-pad the coordinate vectors to dimension m. Then

    A_q^set(m,3,2) >= n(n-1)/6 = m²/6 - O(m).

Together with the preceding upper bound this proves
A_q^set(m,3,2)=Theta_q(m²) for fixed odd q. QED.

## Independent model checks / not sufficient for decoding

Code: research/hyp002_quadratic.py and
research/test_hyp002_quadratic.py.
The original independent ASET oracle is research/lent_exhaustive.py.

- Rectangular triples (013),(014),(023),(024) collide, since
  (013)+(024)=(014)+(023), for any characteristic.
- Nonzero weighted prefix/suffix rectangles collide likewise.
- Nonlinear triples (012),(345),(013),(245) collide but contain
  **no prefix-fiber C4**: absence of C4 is necessary, NOT sufficient
  for exact ASET or decoding.
- Affine Steiner lower witnesses must remain exact in the independent
  subset-sum oracle and meet the explicit finite bound.
- In characteristic two the upper bound holds, but the Steiner lower
  proof needs odd characteristic.

CI verifies finite instances, not the quantified proof or originality.

## Definition-level prior-art review

The exponent is strongly adjacent to classical results.
The claim is a DERIVED THEOREM, not a new mathematical discovery.

1. C4-free bipartite graphs / Zarankiewicz: the prefix graph
   must be C4-free; this is only a necessary reduction. A C4-free
   prefix graph is not necessarily an ASET exact family.
2. **2-separable codes length 3:** in a fixed 3-partite,
   unit-coefficient submodel over odd characteristic,
   descendant equality for codeword subsets of size <=2 is
   equivalent to equality of their three coordinate-count
   multisets, hence to a collision of the unit-incidence vectors.
   Published upper bounds are O(s²) in alphabet size s.
   General weighted/non-tripartite ASET vectors require the
   separate prefix-fiber proof, not an unqualified import.
3. **B2 codes:** pairwise real sums of symbol vectors, related
   but not automatically identical to modular field additions
   and varying-support vector families.
4. **2-union-free hypergraphs:** union uniqueness implies
   incidence multiplicity uniqueness in odd fields, but the
   converse does not generally hold. Its upper bounds cannot
   automatically bound the larger ASET family.
5. Steiner triple systems are a classical quadratic construction,
   not an originality argument.

Source entry points (publication primary records):
- Simon R. Blackburn, Probabilistic existence results for separable
  codes (2015), https://arxiv.org/abs/1505.02597
  (quotes Gao-Ge's O(s²) length-3 2-separable code bounds).
- M. Cheng et al., Bounds and Constructions for
  3-Separable Codes with Length 3 (2015),
  https://arxiv.org/abs/1507.00954 .
- M. Liu, C. Shangguan, C. Zhang, Sharp bounds for uniform
  union-free hypergraphs (2026),
  https://arxiv.org/abs/2605.11949 .

The theorem is self-contained at the elementary proof level,
but its scientific novelty remains unverified and is **unlikely
in the broad exponent form**. STOP treating the exponent as
an open/new theorem target. Further novelty claims would require
a much narrower model and a theorem-specific primary-source audit.

## Engineering / successor research

This capacity bound for sets of at most two active IDs is a
theoretical limit, NOT a working indexed data structure:
auxiliary encoding tables, dense vector cost, decoding complexity,
over-capacity detection, and adversarial updates all remain open.

Possible follow-up research: weighted-code leading constants,
near-extremal structure, compact explicit encoders/decoders with
formal runtime and memory accounting, or w>=4 locality scaling
after a fresh literature gate. G2B-B under issue #14 remains
independent and open. No new Rust crate is authorized.
