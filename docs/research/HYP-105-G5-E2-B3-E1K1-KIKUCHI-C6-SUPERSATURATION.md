# HYP-105 B3.2-E1-K1 — Kikuchi graph: D6 equals proper six-cycles, and a Cauchy–Schwarz/Moore conditional floor

Date: 2026-10-11. Parent [#230](https://github.com/definitely-stable/Mathlab/issues/230), [#176](https://github.com/definitely-stable/Mathlab/issues/176). Base: `main` (E1-A, B0, B1-A, B1-B and C0 merged). This slice is independent of the unmerged stack C1…C24-B8-I ([#260](https://github.com/definitely-stable/Mathlab/pull/260) … [#365](https://github.com/definitely-stable/Mathlab/pull/365)); §7 records how the two programs relate.

**STATUS: RESTRICTED_THEOREM_C (exact all-h identities K1–K3 and a conditional all-h D6 floor) / OPEN_WITH_FORMAL_BLOCKER (one explicit coincidence-mass functional).** No universal Ω(s^6), no infinite low-S family, no full GF5 R3 bound and no ASET exponent are claimed.

## 0. Why a new route

The #230 program so far has used four families of tools, and each has a proved or finite-certified ceiling:

1. **Moments and averaging** (B1-A, C5, C6, C21, C23, B8-B/C). These give `E_g S ≥ (436/3−o(1))s^6`, but on W32 the same global moments are compatible with fixed-map values 77 and 57, and B8-B proves the swap-orbit mean of mixed curvature is zero.
2. **Pinning and local relaxations** (C7–C10, C14–C19). These have all-h zero barriers for ≤3 pins, for pure local signatures, and for shared-left blocks of support ≤B(s)=Θ(s^{3/2}).
3. **Local search on W32** (C22, C24-B2…B7). This yields the descent 177→129→111→72→68, a strict radius-two right minimum, and an 11,236-cell typed rectangle.
4. **Pair projections** (B8-D…G). These yield separated pair/residual certificates that provably cannot close (gaps 9817/2860 and 598987/17160). B8-H/B8-I replace them by pinned-cylinder source floors.

The missing ingredient is structural: D6, the smallest accepted family, is literally a **six-cycle count in an auxiliary graph whose density sits at the Turán/Moore threshold for C6**. Methods of order one or two (means, variances, pair projections, local swaps) cannot see a sixth-order supersaturation phenomenon. In addition, **s=2 is below that threshold** (§4). All prior finite evidence, including the W32 maps with D6=0, therefore lives in a regime that cannot separate Branch A from Branch B.

## 1. The Kikuchi graph and the exact encoding (K1)

Fix s=2^h, W(3,s) with V points, V lines and N=(s+1)V incidences, a=min{a: C(a,2)≥V}, and injective f: points→E(K_a) and g: lines→E(K_a).

**Definition.** The level-(1,1) Kikuchi graph Ĝ=Ĝ(f,g) has vertex set [a]×[a]. Each incidence (p,l) with f(p)={x,x'} and g(l)={y,y'} contributes the two edges

```text
(x,y) — (x',y')      and      (x,y') — (x',y).
```

**Lemma K1.1 (simple, 2N edges).** An edge {(x,y),(x',y')} determines {x,x'} and {y,y'}, hence by injectivity the point and the line, hence the incidence. The two edges of one incidence are distinct. So Ĝ is simple with exactly 2N edges and average degree d̄=4N/a² over all a² vertices.

**Lemma K1.2 (D6 = proper six-cycles).** Call a cycle of Ĝ *proper* if its first coordinates are pairwise distinct and its second coordinates are pairwise distinct. Then the accepted D6 family (A/A with identical connected column-dual C6, see the [B0 note](HYP-105-G5-E2-B3-E1B0-SEVEN-MOTIF-TENSOR.md)) is in bijection with the proper six-cycles of Ĝ.

*Proof.* Take a proper six-cycle (x_i,y_i), i∈Z_6. Its i-th edge is produced by the incidence c_i with f(p_i)={x_i,x_{i+1}} and g(l_i)={y_i,y_{i+1}}. The six left pairs form the simple C6 x_0…x_5, the six right pairs form the simple C6 y_0…y_5, and consecutive incidences share x_{i+1} on the left and y_{i+1} on the right. So both column-dual graphs are the same connected C6 on the six incidence positions, which is exactly the D6 condition.

Conversely, for a D6 set, order the incidences along their common column-dual C6. Put x_{i+1} equal to the left coordinate shared by c_i and c_{i+1}, and y_{i+1} equal to the right one. This gives a proper six-cycle. The choice is forced, because the shared coordinate of two adjacent edges of a simple cycle is unique. Rotation and reflection of the walk give the same subgraph. ∎

The same argument shows that the **accepted Q4 family equals the number of proper four-cycles of Ĝ**.

*Executable check.* At s=2, Ĝ gives D6=15/3 and Q4=50/32 for lex/reverse-line. These match the accepted `seven_census` values and the B0 table. Twelve further seeded W32 bijections agree with `seven_census`. At s=4, lex and seeded-random maps agree with the independent left-C6 DFS + right join `exact_coincident_c6` and with `exact_coincident_c4`.

## 2. An exact Cauchy–Schwarz identity (K2)

For u≠v let P3(u,v) be the number of simple paths u–b–c–v, and let P3=Σ P3(u,v).

**Lemma K2.** For every simple graph,

```text
Σ_{u,v} P3(u,v)^2 = P3 + 12·C6 + Θ,
Θ = 4·Σ_{Q∈C4} Σ_{w∈Q} (deg w − 2 − [w ~ opp_Q(w)])
    + 2·Σ_{ab∈E} c_ab(c_ab − 1) + 16·#bowties,
```

Here c_ab is the number of common neighbours of an edge ab (triangles on ab), and a bowtie is a pair of triangles sharing exactly one vertex.

*Proof.* The left side counts ordered pairs (P,P') of simple 3-paths with the same ordered endpoints.
- **Equal paths.** The diagonal P=P' contributes P3.
- **Internally disjoint pairs.** If P=u b c v and P'=u b' c' v have {b,c}∩{b',c'}=∅, they close a six-cycle. Each six-cycle arises from its three antipodal pairs, times two orientations, times two orders of (P,P'), which gives 12.
- **Pairs sharing internal vertices.** The remaining pairs fall into five cases:
  - b=b', c≠c' gives a four-cycle b c v c' with the pendant edge u b;
  - c=c', b≠b' is the symmetric case;
  - b=c', c=b' gives two triangles on the edge bc (a diamond);
  - b=c' only gives a bowtie centred at b;
  - c=b' only gives a bowtie centred at c.
- **Counting.** Counting each case once per configuration gives the three terms of Θ:
  - for a four-cycle Q, a vertex w and a pendant neighbour outside Q: two orders of the Q-neighbours of w, times two symmetric cases;
  - for a diamond: two ordered pairs per ordered endpoint pair;
  - for a bowtie: 2 cases × 2 endpoint choices × 2 endpoint choices × 2 orders. ∎

All three terms depend only on codegrees. With c_uv the number of common neighbours,

```text
Σ_Q Σ_{w∈Q} φ(w, opp(w)) = Σ_{u<v} C(c_uv, 2) · [φ(u,v) + φ(v,u)],
#bowties(center) = C(t, 2) − Σ_{u ~ center} C(c_{center,u}, 2),
```

where t is the number of triangles through the centre. The reference computes Θ this way. The tests recompute Θ **from the definition** (explicit pairs of 3-paths sharing an internal vertex) on 40 dense random graphs, including complete graphs, and on true Kikuchi graphs at s=2 and s=4.

## 3. A non-backtracking floor (K3)

Let NB3 be the number of non-backtracking walks with three edges. NB3 = P3 + 6·C3, because the only non-path NB 3-walks are closed triangles.

**Lemma K3.1.** If every degree is ≥2 and the average degree is d̄, then NB3 ≥ 2m(d̄−1)².

*Proof.* An NB 3-walk is fixed by its middle directed edge and one continuation at each end, so NB3 = 2Σ_{uv∈E}(d_u−1)(d_v−1).
- By Jensen for exp, this is ≥ 2m·exp((1/m)Σ_{uv}[log(d_u−1)+log(d_v−1)]) = 2m·exp((1/m)Σ_u d_u log(d_u−1)).
- The map x↦x·log(x−1) is convex on [2,∞), since its second derivative is (x−2)/(x−1)² ≥ 0.
- Hence Σ_u d_u log(d_u−1) ≥ n·d̄·log(d̄−1) = 2m·log(d̄−1). ∎

This is the k=3 case of the Alon–Hoory–Linial counting lemma; see also the entropy proof of Babu–Radhakrishnan.

**Lemma K3.2 (peeling).** Let F(m,n)=2m(2m/n−1)². If 2m/n≥3, then deleting an isolated vertex or a vertex of degree 1 does not decrease F, and the average degree stays ≥3. Hence the 2-core satisfies F(core) ≥ F(G).

*Proof.* Put x=2m/n. Deleting an isolated vertex raises x and keeps m, so F rises. For a leaf, x'=(2m−2)/(n−1) satisfies x'−x=(x−2)/(n−1)≥0. The claim F(m−1,n−1)≥F(m,n) follows from (1−1/m)(1+ε)²≥1 with ε=(x−2)/((n−1)(x−1)). That in turn reduces to n(x²−3x+1)≥x−3, which holds for x≥3 because (x²−3x+1)−(x−3)=(x−2)². ∎

For Ĝ we have m=2N, n=a² (isolated vertices included) and d̄=4N/a²≥5 for every s≥2. Hence

```text
P3(Ĝ) ≥ P3₀ := 4N(4N/a² − 1)² − 6·C3(Ĝ).
```

## 4. Conditional all-h theorem

**Theorem K (RESTRICTED_THEOREM_C).** For every s=2^h and all legal f,g, with L(x)=x(x/a⁴−1) and C6_imp the number of improper six-cycles of Ĝ:

```text
12·D6(f,g) ≥ L(P3) − Θ(f,g) − 12·C6_imp(f,g)
          ≥ L(max(P3₀, a⁴/2)) − Θ(f,g) − 12·C6_imp(f,g).
```

*Proof.* By Cauchy–Schwarz over the a⁴ ordered pairs, Σ P3(u,v)² ≥ P3²/a⁴. Combine this with K2, D6=C6−C6_imp (K1.2), and K3, using that L is increasing on [a⁴/2,∞). ∎

Asymptotically μ₀=P3₀/a⁴→4 and L(P3₀)/12 → 4s⁶·(1+o(1)), so **Branch A follows from a single coincidence-mass lemma:**

```text
(CM)   Θ(f,g) + 12·C6_imp(f,g) ≤ (48 − ε)·s⁶   for all legal f,g and s ≥ s₀.
```

Then D6 ≥ (ε/12−o(1))s⁶, and S ≥ D6, which is PROVED_A. In the uniformly random model Θ=O(s⁵) and C6_imp=O(s⁶/a)=O(s^{4.5}), so (CM) holds on average with room. **(CM) is not proved here for adversarial labelings.**

**Exact a-priori table** (`a_priori_table()`):

| s | V | a | K−V | d̄ | 2N/(a²)^{4/3} | μ₀ | L(P3₀)/(12 s⁶) |
|--:|--:|--:|--:|--:|--:|--:|--:|
| 2 | 15 | 6 | 0 | 5.00 | 0.757 | 2.22 | 4.58 |
| 4 | 85 | 14 | 6 | 8.67 | 0.747 | 2.61 | 3.27 |
| 8 | 585 | 35 | 10 | 17.19 | 0.803 | 3.68 | 4.70 |
| 16 | 4369 | 94 | 2 | 33.62 | 0.813 | 4.05 | 4.79 |
| 32 | 33825 | 261 | 105 | 65.54 | 0.802 | 4.01 | 4.34 |
| 64 | 266305 | 731 | 510 | 129.57 | 0.798 | 4.01 | 4.18 |

**Turán position.** Ĝ has about 0.79·n̂^{4/3} edges with n̂=a². That is above every known upper bound for C6-free graphs: Füredi–Naor–Verstraëte (<0.6272·n^{4/3}) and Das–Islam–Mohapatra–Sen 2026 (<0.6144·n^{4/3}). So Ĝ always contains six-cycles, but Turán numbers alone give only Θ(s⁴) of them. The s⁶ scale needs the counting argument above.

**Why s=2 is uninformative.** At s=2 the a-priori value is L(P3₀)=a⁴·μ₀(μ₀−1)=1296·(20/9)(11/9)≈3520. That is far below Θ+12·C6_imp: 5476+12·715 for lex and 3316+12·482 for reverse-line. With a=6 almost every six-cycle repeats a coordinate. The proper fraction of six-cycles behaves like e^{−18/a}: about 0.05 at s=2, 0.28 at s=4, 0.6 at s=8 and 0.83 at s=16. **s=8 is the first size where the conditional floor can be non-vacuous** for random-like maps.

## 5. Finite evidence (exact counts, report-pinned)

All counts come from `research/hyp105_g5e2b3e1k1_kikuchi_c6.py`. The K2 identity and the floor of Theorem K are asserted inside the report for every model with a cycle census.

| model | P3 | μ=P3/a⁴ | C3 | C4 | Q4 = proper C4 | Θ | C6 | D6 = proper C6 | D6/s⁶ |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| s=2 lex | 3,846 | 2.97 | 20 | 69 | 50 | 5,476 | 730 | 15 | 0.23 |
| s=2 reverse-line | 3,300 | 2.55 | 25 | 49 | 32 | 3,316 | 485 | 3 | 0.05 |
| s=4 lex | 132,644 | 3.45 | 112 | 873 | 573 | 127,684 | 37,320 | 8,481 | 2.07 |
| s=4 random(20261011) | 119,854 | 3.12 | 106 | 629 | 460 | 85,992 | 28,712 | 6,805 | 1.66 |
| s=8 lex | 6,596,358 | 4.40 | 904 | 20,347 | 12,566 | 5,948,664 | (opt-in) | (opt-in) | — |

At s=8 lex, Theorem K already gives a lower bound on *all* six-cycles: 12·C6 ≥ L(P3)−Θ ≈ 1.65·10⁷, that is C6 ≳ 1.37·10⁶ ≈ 5.2 s⁶. The proper part is computed only behind the `--s8-cycles` flag (about 10⁶ cycles). It is not pinned until a completed run is recorded.

**Exploratory adversary (local, not CI-pinned).**
- *Run.* A deterministic greedy descent on the exact D6 at s=4, starting from a seeded random map. It made 2,778 swaps or moves to unused K_a edges in ten minutes.
- *Result.* D6 fell from 6,987 to 3,327 (0.81·s⁶) and plateaued. It did not reach zero.
- *Not through Θ.* The adversary did **not** inflate the coincidence mass: Θ fell from 81,724 to 58,376, M2=Σdeg² from 15,916 to 15,220, and the maximum degree from 15 to 12.
- *Through two levers.* It (i) regularised Ĝ, so that μ fell from 3.08 to 2.78, towards the K3 floor μ₀=2.61; and (ii) shifted cycles to improper ones, with the proper fraction falling from 0.25 to 0.16.
- *Reading.* Lever (i) is bounded by K3. Lever (ii) is exactly the C6_imp part of (CM), which is cheap only because a=14 is small. `greedy_d6_adversary` reproduces the method under a small move budget.

## 6. The formal blocker and the proof program

(CM) is the only missing step for Branch A along this route. The planned decomposition is:

- **(D1)** Theorem K itself.
- **(D2) Edge-sharing four-cycles force six-cycles.** Two four-cycles sharing exactly one edge form a six-cycle with an antipodal chord. Hence 3·C6 ≥ Σ_e C(c4(e),2) − (pairs sharing a 2-path) − (chorded degeneracies), with Σ_e C(c4(e),2) ≥ 8·C4²/|E|. A failure of (D1) needs Θ_□≈16·d̄·C4, so roughly C4 ≳ 1.5·s⁵. That in turn yields ≈(4λ²/3)s⁶ six-cycles unless the four-cycles concentrate in **books** K_{2,t} with t≫1.
- **(D3) Books via GQ geometry.** codeg_Ĝ((x,y),(x'',y'')) ≤ min(n(x,y), n(x'',y'')), where n(x,y) counts incidences between the point star X_x={p: x∈f(p)} and the line star Y_y. Girth 8 gives n(x,y)=O(s²). Packing bounds for pencils inside stars, and for lines inside stars, are expected to give an s^{−1/2} saving. The target is Σ codeg³ = o(s⁶) for every labelling.
- **(D4) Improper six-cycles.** A repeat x_i=x_{i+2} means two concurrent lines with physically adjacent images: a "cherry" 𝒞={(p;l,l'): g(l)∩g(l')≠∅}, |𝒞|≤C(a,2)(a−2). A repeat x_i=x_{i+3} is a left bowtie. The y-repeats are symmetric. Each type has at most 11 free physical coordinates.

**Threat model / Branch-B candidate.** Large books need point stars and line stars with many mutual incidences. For even h, Baer subquadrangles W(3,√s) have (√s+1)(s+1)≈s^{3/2} points, about 70% of a star (a−1≈√2·s^{3/2}), and ≈s² internal incidences ≫ d̄. Star families aligned with Baer subquadrangles are therefore both the natural counterexample candidate and the configuration that (D3) must exclude. At s=4 a star has 13 points, while W(3,2) has 15.

## 7. Relation to the unmerged C1…C24-B8-I stack

- **C9, C10, C18, C19.** These prove zero floors for *pinned/local relaxations*. Theorem K is unpinned and global in f and g, so those barriers do not apply to it.
- **B8-H ([#364](https://github.com/definitely-stable/Mathlab/pull/364)) and B8-I ([#365](https://github.com/definitely-stable/Mathlab/pull/365)).** These certify pointwise floors on a pinned right cylinder. On W32 with ten pins: supportwise 16, coupled 29, exact cylinder minimum 68 (hosted). Their own next gate asks for "a symbolic original GQ incidence inequality allowing nontrivial floors with K empty". Theorem K is such an inequality for the D6 component, with explicit residual terms.
- **Division of labour.** The two routes are complementary. Proof trees settle small s, where Theorem K is vacuous. Theorem K plus (CM) addresses the asymptotic regime. A hybrid is natural: on a cylinder, the Ĝ-edges of pinned lines are frozen, so P3, Θ and C6_imp split into pinned and free parts.
- **Citation status.** This note cites those PRs as unmerged drafts. Their numbers are not used in any test here.

## 8. Prior art and transfer firewall

- **Alon, Hoory, Linial.** *The Moore bound for irregular graphs.* Graphs Combin. 18 (2002) 53–57, DOI [10.1007/s003730200002](https://doi.org/10.1007/s003730200002).
- **Babu, Radhakrishnan.** *An entropy based proof of the Moore bound for irregular graphs.* [arXiv:1011.1058](https://arxiv.org/abs/1011.1058).
- **Füredi, Naor, Verstraëte.** *On the Turán number for the hexagon.* Adv. Math. 203 (2006) 476–496 ([ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0001870805001349)).
- **Das, Islam, Mohapatra, Sen.** *An improved upper bound for the Turán number of the hexagon.* [arXiv:2609.10003](https://arxiv.org/abs/2609.10003) (2026).
- **Morris, Saxton.** *The number of C_{2ℓ}-free graphs.* Adv. Math. 298 (2016) 534–580 ([ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0001870816305382)). This gives supersaturation only above an unspecified large constant times n^{1+1/ℓ}, so it does **not** apply at density 0.79.
- **Guruswami, Kothari, Manohar.** *Algorithms and certificates for Boolean CSP refutation: "Smoothed is no harder than Random".* [arXiv:2109.04415](https://arxiv.org/abs/2109.04415). This proves Feige's even-cover conjecture via Kikuchi graphs.
- **Hsieh, Kothari, Mohanty.** *A simple and sharper proof of the hypergraph Moore bound.* SODA 2023, DOI [10.1137/1.9781611977554.ch89](https://doi.org/10.1137/1.9781611977554.ch89).

The Kikuchi construction and the use of non-backtracking walks to force even covers are classical in that literature. What is specific here is:
- the exact identification of the accepted D6/Q4 families with proper cycles of the level-(1,1) graph;
- the explicit coincidence mass Θ;
- the observation that the GQ pair-label regime sits at μ→4, about 0.79·n^{4/3}, i.e. constant-factor above the Moore threshold.

No novelty is claimed for K2 or K3 as graph theory. No new LIT IDs are allocated here.

## 9. Acceptance

The dedicated `hyp105-k1-contract` workflow, the full Research workflow (two named steps in `research-hyp105-foundation`) and INDEX must all succeed on the exact PR head. A post-merge main Research run is also required. #230, #176 and #169 stay open. Theorem K is conditional on (CM). The next slices are (D2)–(D4), the Baer-subquadrangle test at s=4, and exact proper counts at s=8.
