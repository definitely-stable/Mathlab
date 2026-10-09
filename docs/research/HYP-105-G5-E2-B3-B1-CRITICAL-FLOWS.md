# HYP-105 E2-B3.1-A — Exact GF(5) signed flows in the six-by-six physical 2-core

Date: 2026-10-09. Parent [#176](https://github.com/definitely-stable/Mathlab/issues/176), [#169](https://github.com/definitely-stable/Mathlab/issues/169), [#162](https://github.com/definitely-stable/Mathlab/issues/162). Earlier [E2-B3.0 finite projection polynomials](HYP-105-G5-E2-B3-FOREST-PROJECTION.md), [E0 flow identity](HYP-105-G5-E0-BOUNDARY-FLOWS.md), [E2-B1 independent GF5 MITM](HYP-105-G5-E2-B1-EXACT-DISJOINT-ENERGY.md).

**PROVED FINITE EXACT COLORED-SIGNED 2-FACTOR CENSUS / EXPLICIT ALL-h MATCHING-CLASS EXPECTED R3 LOWER / CLASSICAL FINITE-GRAPH IDENTITIES / NO STRICT R3 POWER / NO INDIVIDUAL-LABEL LOWER / NO GEOMETRIC POSITIVE-MOTIF MULTIPLICITY BOUND / NO NEW ASET EXPONENT / ORIGINALITY UNVERIFIED.**

## 1. Precisely restricted branch of the six-trade problem

Fix any six pairwise disjoint factor edges of the published symplectic W(3,s) incidence graph, s=2^h, h>=1. **Factor-disjoint** means all six point endpoints and all six line endpoints are distinct. Their images under the two uniform injective pair labelings are six **distinct** coordinate pairs in each half. Restrict to outcomes where both physical projected multigraphs have precisely SIX touched coordinates and no coordinate of degree one. Since each has six simple edges, the sum of degrees is 12, so every touched physical coordinate has degree exactly TWO. The physical pair graph in each half is therefore a simple two-factor with six edges, necessarily C6 or C3 disjoint union C3.

Construct the **column-adjacency graph**: column IDs 0..5 are its vertices; each touched physical coordinate is represented by an edge between the two columns containing that coordinate. This is also a simple two-factor of type C6 or C3+C3 (line graph preserves these cycle types). A column has two incident left physical coordinates and two right ones. The two physical coordinate colors must remain distinct; the column graph is NOT the original generalized-quadrangle incidence graph, and cannot be treated as an Sp(4,s)-equivariant projection.

For six named columns there are 6!/12=60 labeled C6 graphs and binom(6,3)/2=10 two-triangle graphs, giving **70** possible two-factors for each color. An unordered 3-vs-3 GF5 event has binom(6,3)/2=10 sign partitions. Thus exactly **70²*10=49,000** labeled combinatorial cases, counted BEFORE quotienting by simultaneous S6 column relabeling and global +/- exchange. No unproved geometry multiplicities are included.

## 2. Exact GF(5) nowhere-zero flow count after degree-two contraction

Given a left two-factor L and a right two-factor R on the six column IDs, form a 12-edge, 4-regular, two-edge-colored multigraph H=L union R. Every physical coordinate corresponds to one undirected edge e={u,v}; the original coordinate cancellation equation forces z_(u,e)=-z_(v,e) where z_(i,e)=sign_i * coefficient_(i,e) in GF5*. Orient each contracted edge arbitrarily to obtain one nonzero variable x_e. Column i has demand b_i=4*sign_i in GF5. Thus the original 51-pattern checksum4 coefficient solutions correspond bijectively to nowhere-zero GF5 flows on H with prescribed boundary b.

Let A range over **subsets of the twelve distinctly colored physical edges** (parallel edges from L/R are distinct). Let c(A) denote the number of connected components of the spanning subgraph ([6],A), including isolated columns. If the prescribed boundary sums to zero in each component, the unrestricted affine GF5 flow count is 5^(|A|-6+c(A)); otherwise it is zero. Inclusion-exclusion for all edges being nonzero gives the exact integer

```text
F(L,R,b;5) =
 sum_{A subseteq E(H)} (-1)^(12-|A|)
   * [sum_{i in C} b_i = 0 (mod 5) for every component C of ([6],A)]
   * 5^(|A|-6+c(A)).
```

**Proof:** A zeroed edge is removed from the flow system. The oriented incidence matrix of each connected component of a finite multigraph has rank |V(C)|-1 over GF5; thus a solution exists exactly when its net prescribed boundary is zero and then has dimension |A|-6+c(A). Use inclusion-exclusion over forbidden zero edges. The contraction preserves every edge's nonzeroness, and sign_i is invertible mod5. QED.

This is E0/Fu–Ren–Wang's classical finite-group flow identity specialized after degree-two contraction, NOT a newly discovered universal flow theorem. Runtime bound is at most 2^12 spanning subgraphs PER color/sign isomorphism orbit; no 51^6 assignment enumeration is required. Independently verify representative results by E2-B1's **different** exact GF5 three-column-vs-three-column sum-histogram oracle (51³ assignments on each side).

## 3. Correct isomorphism quotient

Identify two signed color-preserving cases if a simultaneous permutation of the **six column vertices** transports both left/right edge sets and the balanced sign mask, possibly followed by a global sign flip. Neither arbitrary permutation of the left physical coordinates alone nor exchange of left/right colors is used as a substitute for this quotient.

Fix representative L=C6 or L=C3+C3. The stabilizer of C6 has size 12, and that of C3+C3 has size 72. Enumerate all 70 possibilities R and all 10 sign partitions and choose the lexicographically least pair (R,sign mask) among transformations by Aut(L). Each class's exact number of labeled cases equals its frequency for the representative L multiplied by 60 (respectively 10) possible left two-factors. Their total MUST equal 49,000. Graph isomorphisms and sign reversal transport solutions bijectively, so F is constant on each orbit.

The hosted report returns: number of orbits, split by left/right type, counts of positive-flow and zero-flow orbits and their exact labeled masses, extrema of nonzero GF5 flow counts, and examples. Numerical positivity is **not** inferred from passing only the E1 topology gate: it is calculated exactly. This census is COMPLETE for the stated matching+6+6 branch, NOT all 631 exponent-six E2-B3.0 abstract forest shapes or all 11,663 leafless forest shapes.

## 4. NEW explicit lower proof for the matching / 6+6 contribution

A positive type exists for every h: choose the same abstract C6 as BOTH colored column-adjacency graphs and choose alternating signs (+,-,+,-,+,-) around it. Set all four GF5 coefficients of each column equal to 1. Each physical coordinate occurs in exactly two columns of opposite sign, so cancellation holds, and each column checksum is 4 mod5. This produces at least one genuine nonzero GF5 flow for that exact signed motif; in particular no need to infer positivity from a necessary core filter.

Let V=(s+1)(s²+1) factor vertices **per side**, E=(s+1)²(s²+1) factor edges, Delta=s+1 and a=min{j:binom(j,2)>=V}, K=binom(a,2). A greedy lower count of unordered six-factor-edge matchings is

```text
M6(s) >= (1/6!) * product_{j=0}^5 (E - 2*j*Delta).
```

Indeed after j vertex-disjoint selected edges, at most 2j*Delta of all E edges meet used endpoints. At s>=2 every term is positive. To avoid double counting, divide ordered sequences by 6!.

For each matching fix **one** prescribed unordered 3-vs-3 event by an arbitrary, deterministic ordering of its six column IDs with alternating signs. Since the factor endpoints are all distinct, independently uniform injective labeling makes the six corresponding physical pair labels uniformly injective into the K unordered physical pairs on each side. The probability that one side realizes the **specified** C6 column-adjacency graph (on some six distinct coordinate symbols) is EXACT

```text
P_C6(s) = (a)_6/(K)_6.
```

To see this, assign distinct physical symbols to the six abstract adjacency edges of C6 in (a)_6 ways; this uniquely determines all six named pair labels. There is no extra 6! or 12 automorphism division: the column IDs and abstract adjacency edge slots were fixed. Left and right label injections are independent, giving probability P_C6(s)^2. Conditional on this outcome, the concrete all-one GF5 coefficient assignment occurs with probability 51^-6 and causes the selected forbidden 3-vs-3 trade.

Since each **different six-edge factor matching** yields a different six-column event in R3, positivity of every term proves the **explicit all-s** bound

```text
E_pair_labels[R3(B_s)] >=
  [ product_{j=0}^5 (E-2*j*Delta) / 720 ]
  * [(a)_6/(K)_6]^2 * (1/51^6)
  = Omega(s^6).
```

Here E=Theta(s^4), Delta=Theta(s), a=Theta(s^(3/2)), and K=Theta(s^3), so six-factor matching count scales as Theta(s^24), the two physical cycle-placement probabilities together as Theta(s^-18). The proof holds for every s=2^h (positive finite bound) and yields a uniform Omega(s^6) asymptotic constant. It is an independently specified alternative to the earlier C2-D lower route via unit-trade counts. Together with the accepted E2-B3.0 matching-independent upper E[R3]=O(s^6), the random-label expected risk is Theta(s^6).

**Critical logical scope:** this proves a lower bound on EXPECTATION for independently random injective pair labels. It says absolutely nothing about a universal per-labeling lower bound, the existence/nonexistence of a correlated good labeling, or an improved ASET exponent. The exact C6 positive-flow subfamily still has to be counted for a **fixed explicit** label construction before any such inference.

## 5. Reproducible check and next gate

- [Exact finite colored-signed census and explicit all-h matching lower](../../research/hyp105_g5e2b3b1_critical_flows.py).
- [Independent full-GF5 meet-in-middle and graph-isomorphism regression tests](../../research/test_hyp105_g5e2b3b1_critical_flows.py). Exact per-event oracle does not reuse the inclusion-exclusion flow computation.
- Reuse already pinned published Fu–Ren–Wang 2025 (DOI 10.1016/j.aam.2025.102901), and existing Lefmann 2005 / Naor–Verstraëte 2008 for extremal comparators; do not duplicate literature identities.
- All enumeration finite and proof statements explicit. Neither S6 canonicalization nor a finite census is an all-h geometric orbit counting theorem.
- **Next:** B3.1-B extends signed positive-flow classification to other E2-B3.0 exponent-six forest/projection profiles; B3.2 proves nontrivial correlated all-h pair injections preserving counts. B3.3 requires uniform upper bounds on positive motif multiplicities for the same labeling controlling R2. If using hypergraph extraction, explicitly prove degree/codegree hypotheses.
- **Acceptance:** exact PR-head hosted GitHub Research successful, independent tests plus main CI after merge; issue #176 and parents remain OPEN until strict all-h simultaneous R2/R3 bounds.
