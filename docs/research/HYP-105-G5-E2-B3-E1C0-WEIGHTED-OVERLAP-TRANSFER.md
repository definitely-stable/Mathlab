# HYP-105 B3.2-E1-C0 — weighted six-hypergraph intersection / prior-art transfer firewall

Date: 2026-10-10. Parent [#230](https://github.com/definitely-stable/Mathlab/issues/230), [#176](https://github.com/definitely-stable/Mathlab/issues/176). Prior implementations: [#233](https://github.com/definitely-stable/Mathlab/pull/233) merged B0, [#238](https://github.com/definitely-stable/Mathlab/pull/238) B1-A, [#242](https://github.com/definitely-stable/Mathlab/pull/242) B1-B.

**TYPE: exact model reduction for arbitrary s=2^h; executable COMPLETE source original-incidence census for s=2 only; generic mass-only counterexample. No all-h universal positive min, no infinite correlated counterexample, no R3 bound and no ASET exponent.**

## 1. Exact weighted six-uniform hypergraph transfer (all h, no complexity claim)

Freeze a valid left physical pair injection f from the V=(s+1)(s²+1) point vertices of W(3,s) into the K=binom(a,2) physical K_a edges, a minimal with K>=V. Let the RIGHT original line-factor vertex set be `L_s`, |L_s|=V.

For any six-element subset R⊆L_s, set

```text
m_f(R) = number of UNORDERED sets E of SIX DISTINCT ORIGINAL
incidences of W(3,s) satisfying:
 (1) original RIGHT endpoint set of E equals R, each once;
 (2) original LEFT factor multiplicity is B=(2,1,1,1,1);
 (3) LEFT physical K_a projection is leafless on exactly
     six coordinate symbols, each with physical degree TWO.
```

Each original-incidence sixset E contributes exactly one unit to exactly one m_f(R). This is a nonnegative **integer-weighted 6-uniform hypergraph** H_f on V original right factor vertices, not on physical coordinate symbols.

Define physical target `T_a` on the K=binom(a,2) vertices that are themselves unordered K_a physical pair-edge labels. A six-element subset of those pair-edge labels belongs to T_a iff it forms a simple six-edge 2-regular graph on exactly SIX distinct physical coordinate symbols; admissible components are C6 or C3⊔C3. Exactly

```text
|T_a| = 70*binom(a,6).
```

For EVERY admissible injective right label assignment g:L_s→E(K_a), exactly and pointwise,

```text
U_B-left/A-right(f,g)
  = sum_{R in C(L_s,6)} m_f(R) * 1_{g(R) in T_a}.
```

This is **not** an approximate first-moment theorem: the B/A accepted motif condition is exactly that its six original right endpoints are all distinct and their physical images form a simple 2-factor. The original six-incidence sets producing the same unordered R have multiplicity m_f(R), and each contributes once. No extra factor 6!, no GF5 signed cancellation. This is a model-specific application of the classical weighted hypergraph intersection functional, not a new mathematical operator.

For independently UNIFORMLY random right injection g, a fixed R maps uniformly to a size-six subset of the K physical pair labels. Hence

```text
E_g U_B-left/A-right(f,g)
   = (sum_R m_f(R))*|T_a|/binom(K,6)
   = (sum_R m_f(R))*70*binom(a,6)/binom(K,6).
```

This equals the accepted B1-A six-ordered-right-endpoint completion factor 6!*70*C(a,6)/(K)_6, since (K)_6=6!C(K,6). The right map has to be independent of f for the expectation; no independence is required by the exact fixed-map hypergraph overlap identity. For each fixed f, the independent expectation is (140+O(s^-1))s^6, from B1-A, but the desired `min_g U_B/A` is not thereby bounded below.

**IMPORTANT: even min_g U_B/A=0 at all h would not settle the seven-family S lower** because the other six classes may contribute; minimizing one fixed positive family is a subproblem.

## 2. Independent exact finite certification

At s=2, V=K=15, the 15 original right line vertices map bijectively to the 15 physical K6 pair labels. We build m_f from each and every accepted physical-left-B original six-incidence selection among the complete **10,935** candidates inside the **62,370** full-left-qualified collection; each selected original sixset is counted once. Only those with all six original right endpoints distinct contribute.

The target T6 is the family of **70** physical simple six-edge 2-factors, verified in a completely independent oracle by enumerating all C(15,6)=5,005 six-edge subsets of K6 and checking physical degree exactly two. The production generator uses the accepted 70 K6 templates embedded into a physical K_a coordinate subset, without the 5,005 brute loop.

Both pinned concrete fixed W32 injections are independently checked: `lex` gives U_B/A=98, `reverse-line` gives U_B/A=77. Furthermore, after the genuine original right factor pair-label swap (line IDs 4 and 13) already accepted in B1-B, H_f DOES NOT CHANGE because only the right physical mapping changes, but the weighted overlap becomes 57. The exact random-injection expectation remains unchanged. No multi-h or all-injection minimum is computed.

## 2A. Exact all-a target-design theorem: one-point uniformity and two adjacency orbits

A further **elementary all-a structural theorem** follows from the fact that each physical target hyperedge consists of six pair labels forming a 2-regular graph on six of the a physical coordinate vertices. The 70 possible K6 2-factors are vertex-transitive; they contain each K6 edge in exactly 28 factors. Their pairs of distinct physical edges fall into two S6-orbits: adjacent (sharing a physical coordinate) and disjoint. Within the 70 K6 2-factors, each fixed adjacent physical-edge pair occurs **7** times and each fixed disjoint pair occurs **14** times. Independently verify these constants by exhaustively scanning 5,005 possible six-edge subsets of K6, checking exact degree two.

After embedding each six-coordinate K6 factor into a physical K_a, the target T_a has EXACT incidence design parameters:

```text
K = binom(a,2),   |T_a| = 70 binom(a,6).

For any fixed physical pair label e in E(K_a):
  deg_T(e) = 28 binom(a-2,4).

For two DISTINCT physical pair labels e != f:
  co_deg_T(e,f) = 7 binom(a-3,3)  if |e ∩ f|=1,
                = 14 binom(a-4,2) if |e ∩ f|=0.
```

These follow by choosing the six-element physical coordinate set containing the fixed one/two pair edges and using the exact 28/7/14 embedded-template incidences. The identities `K deg_T(e) = 6|T_a|` and `sum_{e<f}co_deg_T(e,f)=binom(6,2)|T_a|` are exact integer falsification checks. Thus **T_a is a 1-design for every a>=6**, because all K physical pair-edge labels have identical degree. It is a **2-design exactly when a=9**: the adjacent and disjoint co-degrees are equal if and only if `(a-3)/6=1`. In the genuine W(3,2^h) minimal physical alphabet, a=6 at s=2, a=14 at s=4, and a grows thereafter. The exceptional a=9 2-design is NOT a GQ instance and proves nothing about the all-h risk bound.

**Exact bijection-only linear-source corollary.** If original right factor vertices and physical pair labels have exactly the SAME cardinality K (a full bijection g, as at s=2) and an abstract source weighting on six-factor subsets has only constant and degree-one components, namely `m(R)=c+sum_{v in R}beta_v`, then for EVERY bijection g:

```text
sum_{|R|=6} m(R) * 1_{g(R) in T_a}
  = c |T_a| + deg_T(e) * sum_v beta_v.
```

Proof: each target T_a edge is counted once by constant c and each physical vertex label appears in exactly `deg_T(e)` target hyperedges. This is the elementary fixed-degree counterpart of the W1 harmonic-orthogonality picture in Bollobás–Scott, **not a new generic discrepancy theorem**. Under a non-surjective injection V<K, a restricted image of T_a need NOT be 1-design. Nor is the true GQ m_f known to be constant-plus-degree-one; thus this does not imply a universal all-g lower for HYP-105.

The independent CI falsifier checks all physical pair-of-label codegrees by enumerating every target hyperedge of K6 and K9 (including the accidental K9 2-design) and verifies the linear-source overlap identity against several explicit non-gauge permutations of all 15 K6 edge-label vertices. At a=14 the exact unequal adjacency codegrees are 1155 and 630. These complete target signatures are useful invariants for the next B1-C step: computing the corresponding second-order source distribution of m_f and testing whether it can generate a universal MIN-over-g lower.

## 2B. Stronger exact no-go: a 3-cube trade defeats every degree ≤2 source marginal

This is a **rigorous finite structural countermodel** against an overstrong B1-C inference from target two-point orbits alone. It is again NOT a genuine W(3,s) source. Take a=6, K=15, and number the physical pair labels of K6 lexicographically 0..14. Let the three common source vertices be C={0,1,6}; let three switch pairs be P_0=(2,11), P_1=(3,12), P_2=(13,14). Every mask b∈{0,1}³ gives one distinct six-element hyperedge

```text
R_b = C ∪ {P_0[b_0],P_1[b_1],P_2[b_2]}.
```

Define two NONNEGATIVE, integer-weighted six-hypergraphs m_even and m_odd, each with unit weight on the four distinct R_b having even versus odd parity, zero elsewhere. For every subset A of source vertices with |A|≤2,

```text
Σ_{R ⊇ A} m_even(R) = Σ_{R ⊇ A} m_odd(R).
```

**Proof:** the signed difference of the two hypergraphs is the product of the three independent binary sign toggles. Requiring a specific set A of at most two vertices can fix at most two of those switches, leaving at least one free switch whose ± terms cancel. If A requires both endpoints of any switch, neither side contains A; cancellation is then trivial. Thus their 0th, 1st and **every** 2nd-order source marginal agrees exactly.

Yet under the SAME identity labeling into physical K6 pair edges, the exact 70-element target T6 contains exactly ONE of the eight sixsets: R_(1,1,1)={0,1,6,11,12,14}. It is a physical simple C6, with pair labels (0,1),(0,2),(1,3),(2,5),(3,4),(4,5). Therefore

```text
overlap(m_even,T6)=0,    overlap(m_odd,T6)=1.
```

Scaling all weights by any positive integer M preserves every equality of source 0th/1st/2nd marginals and gives overlap gap M. The same local counterexample embeds in the K6 coordinate subset of any physical K_a (a≥6); an injection of the remaining source vertices, if needed, completes it. Because the image sixsets only use K6 edges, no additional physical coordinates can alter membership.

**Consequence:** neither the first nor the complete second marginal of a GENERAL weighted six-hypergraph determines its intersection with T_a under a fixed permutation/injection; higher-order components matter. Combined with the target's distinct adjacent/disjoint pair codegrees, this means an all-g positive lower theorem for the actual GQ source m_f cannot be obtained just by treating its first two marginals as a sufficient statistic. The GQ incidence-derived family might still possess special structure that rules out these arbitrary signed 3-cube trades; proving that exclusion is a legitimate B1-C next step. There is no contradiction with the accepted 140 s^6 independent-right expectation because m_even and m_odd have the same total mass and thus the same random mean.

[Code](../../research/hyp105_g5e2b3e1c0_weighted_overlap.py) freezes all eight sixsets. Independent tests rederive the corners rather than using the production generator, compute all ≤2 incidence marginals by direct weighted summation, enumerate the entire 5,005 K6 six-edge universe to obtain the 70 targets, and independently compute overlaps 0 and M for M=1,17,10^6. No FPT/probabilistic claim, no actual GQ counterexample and no all-h ASET power is inferred.

## 2C. Exact all-a third-order target tensor, five edge orbits

Because the eight-corner trade above is invisible to every source marginal of order ≤2, the next target signature to compute is its **third-order incidence tensor**. For any THREE distinct physical pair labels e₁,e₂,e₃ of K_a, define `codeg_T(e₁,e₂,e₃)` as the number of target sixsets containing all three. Under coordinate permutations S_a, the three chosen physical edges have exactly FIVE isomorphism types:

| Unlabeled three-edge physical graph | Used physical vertices r | Number of such triple-label sets in K_a | Target sixset co-degree |
| --- | ---: | ---: | ---: |
| Triangle C3 | 3 | C(a,3) | C(a−3,3) |
| Simple path P4 of length 3 | 4 | 12 C(a,4) | 2 C(a−4,2) |
| Three-leaf claw K1,3 | 4 | 4 C(a,4) | **0** |
| Two-edge path P3 plus isolated edge | 5 | 30 C(a,5) | 5(a−5) |
| Three disjoint edges (perfect matching) | 6 | 15 C(a,6) | **8** |

**Proof:** for the six physical coordinates used by each target sixset, all 70 simple degree-two six-edge K6 factors are exhaustively classifiable. For a fixed three-edge graph of each type within that K6, the exact number of completions is respectively **1,2,0,5,8**. Zero for a claw follows from its degree-three central vertex, which no 2-regular target can contain. To pass from K6 to K_a, add any `6−r` new physical vertices to the specified `r` existing ones, and multiply by C(a−r,6−r). This proves the formulas for **all a≥6**, without sampling. They satisfy the global third-incidence identity

```text
Σ_{3 distinct physical pair labels} codeg_T(e₁,e₂,e₃)
    = binom(6,3)|T_a| = 20*70*C(a,6).
```

A separate oracle exhaustively enumerates every 3-edge subset of physical K6 (455 cases) and K9 (C(36,3)=7,140 cases) and checks its orbit classification and exact target co-degree against all 70*C(a,6) target hyperedges. At a=14 the code checks the symbolic counting identities without enumerating ~2.1 million target sixsets. This is an exact TARGET-side theorem. It does not compute the corresponding 3-marginal of the actual GQ source m_f for all h and it does not force a positive worst-case intersection.

**Next B1-C1 proof question:** identify what third-order source marginals the W(3,s) incidence structure permits, distinguish them from freely assignable three-cube trades, and determine whether a model-specific inequality lower-bounds all-correlated `Σ_R m_f(R)1_{g(R)∈T_a}`. In view of the seven-class scope, proving B/A-specific positivity may be strictly stronger than the ultimate needed S-seven obstruction.

## 3. Corrected prior art and disallowed transfers

The underlying weighted hypergraph intersection/discrepancy formulation is **classical**, and any originality or universal minimum theorem must be compared with:

- **Béla Bollobás, Alex Scott**, *Intersections of hypergraphs*, *Journal of Combinatorial Theory, Series B* **110** (2015), 180–208, DOI [10.1016/j.jctb.2014.08.002](https://doi.org/10.1016/j.jctb.2014.08.002), [author manuscript](https://people.maths.ox.ac.uk/~scott/Papers/hyperint.pdf), [arXiv:1408.6348](https://arxiv.org/abs/1408.6348). Its **Theorem 3** bounds the product of positive and negative *discrepancy* components in terms of the W-vectors, not the absolute `min_permutation overlap` from below; its **Theorem 16** gives orthogonal weight-component pairs with zero discrepancy. Their Section 4 treats effects of transpositions on weighted hypergraph overlap. None of these facts alone implies a positive minimum for our particular source-target pair.
- **Béla Bollobás, Alex Scott**, *Intersections of random hypergraphs and tournaments*, *European Journal of Combinatorics* **44A** (2015), 125–139, DOI [10.1016/j.ejc.2014.08.023](https://doi.org/10.1016/j.ejc.2014.08.023), [publisher](https://www.sciencedirect.com/science/article/pii/S0195669814001358). This concerns RANDOM hypergraphs and random tournaments, not a fixed weighted source generated by W(3,s) and a deterministic highly structured physical target T_a.
- **Béla Bollobás, Alex Scott**, *Intersections of graphs*, *Journal of Graph Theory* **66** (2011), 261–282, DOI [10.1002/jgt.20489](https://doi.org/10.1002/jgt.20489). Related k=2 ancestor; our k=6 model does not inherit a quantitative minimum bound automatically.
- **Béla Bollobás, Svante Janson, Alex Scott**, *Packing random graphs and hypergraphs*, *Random Structures & Algorithms* **51** (2017), 3–13, DOI [10.1002/rsa.20673](https://doi.org/10.1002/rsa.20673), [arXiv:1408.6354](https://arxiv.org/abs/1408.6354). The random-model packing thresholds do not provide a deterministic GQ source packing into T_a.

**Explicit disproof of a general mass-only inference.** On 15 abstract source vertices take m(R)=M>0 on ONE six-set R and zero elsewhere. Let T6 be the positive 70-edge six-2factor target on physical K6 pair labels. Assign those six right source vertices to a five-edge star centered at physical coordinate 0 plus physical edge (1,2). This is a valid partial bijection to SIX DISTINCT physical pair-edge labels, extendable to the other nine labels. The image is not 2-regular and hence the intersection is **exactly zero** under that assignment, although its random-permutation expectation is 2M/143>0 and its total source weight M is arbitrary. Thus source total mass alone cannot force positive minimum overlap. This **does not model W(3,s)** and therefore does NOT refute the desired GQ-specific minimum.

This identifies an essential gap: to prove `min_g U_B/A >=c*s^6` one must use structural constraints on **how the multiplicity weights m_f(R) are distributed on original six-line subsets**, not only their total `Σm_f≈(1/4)s^15`. Even then, a B/A-only lower is stronger than needed for the accepted seven-family S lower and may be false independently.

### Bibliography transaction boundary

Catalog import for HYP-105 must use unique canonical LIT IDs, title/DOI dedup, and regenerate `docs/research/catalog/LITERATURE.md` and its reverse index with the repository's generator. [IMPORT-012 PR #246](https://github.com/definitely-stable/Mathlab/pull/246) has been merged and reserves LIT-366–387 in the canonical catalog. This independent research PR pins the four DOI identities and source-transfer review in the proof note **without inventing LIT IDs or rewriting the generated catalog indexes**. A separate deduplicated import transaction should inspect the post-#246 catalog, allocate only unused canonical IDs and regenerate both derived indexes with `research/literature.py --write` on GitHub-hosted CI.

## 4. Next falsifiable research gate

Before attempting a new all-label HYP-105 asymptotic theorem, compute or bound distributional signatures of m_f beyond total mass: weighted vertex degree, weighted pair-codegree, intersection signature and W-vector components relative to T_a; prove an inequality for **MIN** over injections or build an infinite correlated avoidance construction. Classical discrepancy can be positive while min overlap is zero; don't confuse `max |deviation|`, random mean, and deterministic minimum.

CI acceptance: full exact PR-HEAD GitHub-hosted Research SUCCESS, independent original incidence W32 oracle and physical target brute, fail-closed typed inputs, research indices; do not close #230 or claim full GF5 R3 or ASET power.
