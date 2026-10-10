# HYP-105 B3.2-E1-C1 — GQ concurrence fibers, exact third-line census, B/A wedge oracle

Date: 2026-10-10. Parent [#230](https://github.com/definitely-stable/Mathlab/issues/230), #176. Stacked on B1-C0 [PR #249](https://github.com/definitely-stable/Mathlab/pull/249). Inherits the exact source m_f(R), target T_a, the full-51 GF5 risk restrictions, and the independently accepted B1-A left-mass floor.

**TYPE:** classical all-h GQ concurrence graph facts + their exact application to the B-left/A-right source; independently implemented COMPLETE W(3,2) original-incidence wedge-oracle; no global all-g intersection lower or full R3 bound. The three-line GQ classes below are NOT the five physical-target three-edge orbits in B1-C0.

## 1. GQ concurrence graph: exact third-line census for all h

Let s=2^h, h>=1, Delta=s+1, V=(s+1)(s²+1). Let Gamma_s be the graph whose vertices are the V ORIGINAL right factor lines of W(3,s), with an edge if two such lines meet at an ORIGINAL left factor point. These edges do NOT mean adjacency of two physical pair labels g(l).

The ordinary generalized quadrangle axioms imply that Gamma_s is strongly regular with

```text
v=V,  k=Delta*(Delta-1)=s(s+1),
lambda=s-1, mu=s+1.
```

* Degree: each of the Delta original points on a line is incident to Delta-1 other lines; no two lines share two original points (incidence graph has no 4-cycle).
* Adjacent pair: the only other lines meeting both members of a concurrent pair go through their unique common original point, giving lambda=Delta-2. Three pairwise meeting original lines must meet at ONE common point, since a triangle with three distinct intersection points would induce an incidence 6-cycle.
* Nonadjacent pair: the GQ unique-connector axiom supplies one connector through each of the Delta points on the first line to the second, giving mu=Delta.

Write N_j for the number of UNORDERED triples of distinct original right lines inducing exactly j edges of Gamma_s. With E=Vk/2 and H=Vk*lambda/6, the exact values are

```text
N3 = H                                       (all concurrent triples)
N2 = V*binom(k,2) - 3*H                     (induced 2-edge paths)
N1 = E*(V-2) - 2*N2 - 3*N3                 (exactly one meeting pair)
N0 = binom(V,3) - N1 - N2 - N3             (three pairwise skew lines).
```

At s=2, (N0,N1,N2,N3)=(80,180,180,15); at s=4, (43520,40800,13600,850). These are classical graph-theoretic consequences of GQ parameters, **not an originality claim**.

## 2. Exact GQ-specific m_f(R) wedge-cycle factorization

For any injective left factor map f and six DISTINCT original right lines R, let c(R) be the number of pairs {l,l'} contained in R that are adjacent in Gamma_s.

For each original left factor point p, a B-left six-incidence set has p as its UNIQUE doubled point and four singleton original left points q1,q2,q3,q4. Because f(p) is a physical edge occurring twice in the six selected original incidences, both of its physical coordinates already have degree 2. Thus the FOUR distinct physical edges f(q1),...,f(q4) must form a SIMPLE C4 on four other physical coordinates, disjoint from the endpoints of f(p). No physical K_a edge may be used by both p and any qi because f is injective.

Let Cyc_f(p) be the family of UNORDERED four-element sets of original points q whose f-images form such a C4. Let Inc(x) be the ORIGINAL right lines incident to the ORIGINAL left point x. Then the exact source identity is

```text
m_f(R) =
 sum over p in P_s
 sum over Q in Cyc_f(p)
 sum over unordered distinct {u,v} in C(Inc(p),2)
 sum over choices l_q in Inc(q) for each q in Q
    1[{u,v} union {l_q:q in Q} = R, with all six lines distinct].
```

Each B-left unordered original incidence sixset has exactly ONE such decomposition: its doubled original point p, its four singleton points Q, its two distinct original lines u,v at p, and its four singleton original lines. Thus no 6!, 4!, graph-automorphism factor or signed GF5 flow factor occurs.

A necessary condition for any summand is that the doubled original right line pair {u,v} belongs to R and is concurrent at p. The GQ no-4-cycle property determines p uniquely from that pair. Each of the remaining four right lines offers at most Delta candidate original points, independently, before the stringent f-C4 constraint. Consequently, for every s=2^h, every f and every R,

```text
0 <= m_f(R) <= c(R)*Delta^4 <= 15*Delta^4.
c(R)=0  ==>  m_f(R)=0.
```

This REFINES B1-C0's uniform cap by the actual ORIGINAL line concurrency count c(R). The universal overlap with T_a is still a separate question; c(R) only constrains source support.

Since Gamma_s has E=Vk/2 edges, at most E*binom(V-2,4) distinct original six-line subsets contain a concurrent pair, by an exact union bound over concurrent pairs. For a uniform random six-subset R of ORIGINAL lines,

```text
E[c(R)] = binom(6,2)*k/(V-1) = 15*s(s+1)/(V-1)
          = (15+o(1))/s.
Pr[c(R)>0] <= min(1, E[c(R)]).
```

Therefore support(m_f) occupies at most an O(1/s) FRACTION of the original right six-subset universe for large s. This upper support sparsity is consistent with B1-C0's uniform lower |supp(m_f)|=Omega(s^11): the ambient right six-subset universe has order s^18, while the upper bound is O(s^17). Neither bound proves a positive minimum over right injections.

## 3. GQ-source third marginal versus physical target tensor

For every triple A of ORIGINAL right lines, define

```text
mu_f^(3)(A) = sum_{R subset L_s, |R|=6, R superset A} m_f(R).
```

Grouping by c(A)=0,1,2,3 gives four computable exact source statistics M_j(f). They obey

```text
sum_{j=0}^3 M_j(f) = binom(6,3) * sum_R m_f(R).
```

The left side is source-side ORIGINAL concurrence; it must NOT be identified with physical-target T_a's five S_a-orbit codegrees (1,2,0,5,8 on K6, with their all-a factors). The correlation between these two different classifications is controlled by the unknown adversarial right map g. Neither the GQ SRG parameters nor these four aggregates alone determine the intersection m_f(g^-1(T_a)).

For a possible all-h lower proof one needs a **joint** restriction on m_f and g or a positive-coefficient inequality involving the full seven-family S_s, not an unjustified matching of source and target orbit means. The source is constrained by concurrence but an adversarial g does not preserve that graph.

## 4. Independent executable acceptance

[Reference](../../research/hyp105_g5e2b3e1c1_gq_concurrency.py) constructs Gamma_2 from all 45 ORIGINAL W(3,2) incidences, independently checks k=6 and lambda=1/mu=3 and the complete 455-triple census, then constructs the entire weighted B/A source by the **repeated-point + physical four-cycle + incident-line choices** algorithm. The source iterator does not call the B1-C0 `source_weighted_BA_hypergraph` or B1-A's `selected_left_six`.

[Independent tests](../../research/test_hyp105_g5e2b3e1c1_gq_concurrency.py) compare this wedge census **per original right sixset and with full multiplicity** against a separate original-incidence `selected_left_six` enumeration, for BOTH lex and reverse-line maps. Expected W32 totals: 10,935 B-left candidates, 5,000 qualifying six-distinct-right weighted mass, 3,076 supported right sixsets, max observed m=6. They exhaust all 5,005 right sixsets for the refined c(R) cap, compute all 455 third marginal values by signature, and independently verify `sum mu_3 = 20*5000 = 100000`.

This remains a COMPLETE FINITE W32 test, not a proof for s>2. The all-h proof above is elementary and algebraic and its integer formulas are tested at multiple powers of two. No C1 acceptance is claimed until Research CI on exact PR head is SUCCESS.

## 5. Next mathematical decision

This slice proves **structural restrictions** absent in arbitrary weighted hypergraphs. The next genuine B1-C2 decision gate is either (i) identify a model-preserving nonnegative joint GQ/physical tensor inequality that yields a fixed-g lower, or (ii) produce a certified all-h family of f,g violating the specific B/A minimum, then check the OTHER six positive families before claiming #230 Branch B. Do not promote finite s=2 or first-moment estimates to either gate.

Outcome for parent #230: **OPEN_WITH_FORMAL_BLOCKER**. No positive universal Omega(s6), no same-map strict GF5 R3 upper, no ASET exponent.
