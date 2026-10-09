# HYP-105 G5-E2-B3.0 — Six-edge factor forests and exact leafless pair-projection polynomials

Date: 2026-10-09. Parent [issue #176](https://github.com/definitely-stable/Mathlab/issues/176), [#169](https://github.com/definitely-stable/Mathlab/issues/169), [#162](https://github.com/definitely-stable/Mathlab/issues/162). Builds on [E2-B2](HYP-105-G5-E2-B2-RANDOM-R2-BOUND.md), [E1 signed-flow topology](HYP-105-G5-E1-FLOW-MOTIFS-AND-NEXT-PROOF.md), and [E0 GF5 prescribed-boundary flows](HYP-105-G5-E0-BOUNDARY-FLOWS.md).

**SCOPE: PROVED CLASSICAL-STRUCTURAL / EXACT FINITE PROJECTION FORMULA / ALL-h EXPECTED R3 UPPER O(s^6) / NO STRICT R3 POWER / NO GF5 SIX-FLOW CLASSIFICATION / NO CORRELATED LABELING / NO IMPROVED ASET EXPONENT / PRIORITY UNVERIFIED.**

## 1. Exactly what is counted

Take the published classical symplectic generalized quadrangle `W(3,s)` for `s=2^h, h>=1`, as already verified in B1. Its bipartite point/line incidence graph has girth eight, `V=(s+1)(s^2+1)` vertices **per side**, degree `Delta=s+1`, and `N=(s+1)^2(s^2+1)` distinct incidence edges. Let `a=min{r:binom(r,2)>=V}`, `m=2a=Theta(s^(3/2))`.

Independently uniformly inject each factor-side vertex set into the unordered edges of `K_a`. A selected incidence edge induces a distinct support of two physical coordinates in each of two disjoint blocks. The actual GF(5) checksum-4 coefficient palette still has **51** valid nonzero patterns per column; this new lemma does *not* enumerate those patterns or equate the factor graph and coordinate projections.

For any six **distinct** factor edges the factor subgraph is a **forest**: a cycle of length at most six contradicts factor girth eight. Write `r_L,r_R` for its distinct factor endpoints, and `c=r_L+r_R-6>=1` for its number of forest components. Each fixed abstract six-edge forest has at most `O(V^c Delta^6)=O(s^(3c+6))` injective embeddings into the factor graph: choose the image of one root per component (at most `V` choices in its prescribed part), then grow the six tree edges (at most `Delta` choices each). This is an upper bound, not an exact geometrical orbit count.

## 2. Exact projection polynomial for *every* partition of six

At one factor side, let `lambda=(lambda_1,...,lambda_r)` be the positive multiplicities of the `r` distinct abstract factor endpoints over six selected incidence edges. Thus `sum lambda_i=6`. Each endpoint is assigned a **different** unordered physical coordinate pair (a simple edge of `K_a`). Its assigned pair is repeated `lambda_i` times in the coordinate multigraph.

Define `c_lambda(v)` by the following *finite* combinatorial count. On an auxiliary **labeled** set of `v` physical vertices, count injective ordered assignments of `r` distinct unordered pair-edges to the `r` named factor endpoints such that the weighted degrees are all at least two and every auxiliary vertex is touched; divide by `v!`. Here each pair-edge has multiplicity `lambda_i`. Since total weighted degree is 12, the necessary minimum-degree-two condition forces `v<=6`. Therefore, for every `a>=4`, the **exact** probability of no degree-one physical coordinate is

```text
p_a(lambda) = [ sum_{v=2}^6 c_lambda(v) (a)_v ] / (binom(a,2))_r,
(x)_j = x (x-1)...(x-j+1).
```

**Proof:** Every injective ordered pair-label assignment satisfying the degree condition has a unique touched physical vertex set of size `v<=6`. Choose/order these `v` distinct physical symbols in `(a)_v` ways; each actual assignment is represented `v!` times by reordering that auxiliary set. The remaining finite `c_lambda(v)` count is independent of `a`. Divide by the total `(binom(a,2))_r` injective ordered pair labels. Nonnegative summands preclude cancellation. QED.

All 11 integer partition profiles of six are:

| `lambda` | Nonzero `c_lambda(v)`, shown as `v:coefficient` | Projection loss power in `s` |
| --- | --- | --- |
| 6 | 2:1/2 | 0 |
| 5+1 | NONE | impossible |
| 4+2 | 3:1, 4:1/4 | 0 |
| 4+1+1 | 3:1 | 9/2 |
| 3+3 | 3:1, 4:1/4 | 0 |
| 3+2+1 | 3:1, 4:1 | 3 |
| 3+1+1+1 | 4:6, 5:1/2 | 9/2 |
| 2+2+2 | 3:1, 4:4, 5:3/2, 6:1/8 | 0 |
| 2+2+1+1 | 4:9, 5:3 | 9/2 |
| 2+1+1+1+1 | 4:30, 5:36, 6:3/2 | 6 |
| 1+1+1+1+1+1 | 4:30, 5:510, 6:70 | 9 |

When a profile has positive coefficients with maximum support size `v_max`, `p_a(lambda)=Theta(a^(v_max-2r))=Theta(s^[-(3/2)(2r-v_max)])` as `s->infinity`. For the impossible `(5,1)` profile, the exact probability is zero. These constants follow by enumerating only **simple** auxiliary pair-edge sets on up to six vertices, with explicit repeated-weight factors for individually named endpoints. They do not count GF5 flows.

## 3. All-h expected signed three-vs-three risk upper

There are `Bell(6)=203` set partitions of six named factor edges on each side. For every ordered pair of these partitions, the checker separately rejects repeated factor incidences, factor cycles, and either side with identically-zero leafless probability. This leaves **11,663 admissible abstract factor-forest shapes** among the `203^2=41,209` ordered pairs. Grouping the upper exponent

```text
e = 3c+6 - (3/2)(2r_L-v_max,L) - (3/2)(2r_R-v_max,R)
```

gives the following independent finite certificate:

| `e` | Number of forest shapes |
| --- | ---: |
| 6 | 631 |
| 9/2 | 2,740 |
| 3 | 4,630 |
| 3/2 | 3,180 |
| 0 | 482 |

The maximum is **6**. The counting bound for each abstract factor forest is uniform in `h`, the two independently uniformly injective pair-label distributions factorize, and at most `binom(6,3)/2=10` unordered 3-vs-3 GF5 events exist per six distinct columns. Each such event has conditional coefficient-collision probability at most 1; the event is impossible if *either* projection has a degree-one physical coordinate. Summing finitely many shapes proves the genuine, but only model-specific,

```text
E_pair_labels[R3(B_s)] = O(s^6) = O(m^4),   s=2^h.
```

Together with the *earlier independently proved* `E_pair_labels[R3]=Omega(s^6)` in C2-D/E1, this establishes **Theta(s^6)** for the independent-uniform-pair-label expectation. Importantly this is NOT a universal lower bound over all individual labelings and does not refute exceptional/correlated constructions. The finite shape count is **a certificate for the elementary upper**, not a proof that any of the 631 exponent-six shapes has a nonzero GF5 nowhere-zero flow or is realized in Theta of its forest-embedding upper. In particular, it is invalid to call 6 a universal method impossibility bound.

## 4. Scope and next proof gate

The strict ASET route still needs the **same** all-h labeling family with `R2(B_s)=O(s^(26/5-epsilon_2))` and `R3(B_s)=O(s^(6-epsilon_3))`, both epsilons positive. This new theorem sharpens the random-label **baseline** only. It does not prove the second strict inequality.

**B3.1:** classify the finite signed six-column motifs and their actual `F_tau(b;5)>0` by E0/E2-B1 independent GF5 flow count; count *events*, not flow witnesses. **B3.2:** define and prove injectivity of genuinely correlated all-h point/line pair-label maps. **B3.3:** prove uniform multiplicity bounds for the **positive** motifs using genuine geometry of those maps; cannot transfer symmetry of `Sp(4,s)` to a non-equivariant map. **B3.4:** if blocked, verify actual degree/codegree for an alternative extraction theorem before invoking LLL. Retain issue #176 and parent roots OPEN.

## 5. Reproduction and audit

- [Projection and forest reference checker](../../research/hyp105_g5e2b3_forests.py) uses Python standard library, finite simple-graph enumeration and symbolic fractions. Never performs a `binom(425,6)` factor-event enumeration.
- [Independent finite tests](../../research/test_hyp105_g5e2b3_forests.py) directly enumerate actual injective pair labels for K4/K5; test every one of the 41,209 paired factor endpoint partitions with separately implemented DFS; check randomly chosen true GF2/GF4 symplectic six-edge samples; assert correct asymptotic **scope**.
- Prior-art boundary: classical forest embeddings and degree/cycle enumeration are elementary; the 2025 Fu–Ren–Wang prescribed-boundary flow method remains prior art for the *next* positivity classifier. Existing Lefmann 2005 and Naor–Verstraëte 2008 comparator references remain unchanged. No new literature entry is needed for these finite elementary counting steps.
- **CI requirement:** hosted exact PR-head full `research` workflow SUCCESS before merge; never merge on local evidence alone.
