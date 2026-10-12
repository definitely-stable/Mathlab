# HYP-105 E1-K3-G2-K — exact conditional-injection derandomization of B-left/A-right

Date 2026-10-12. Root [#230](https://github.com/definitely-stable/Mathlab/issues/230); stacked Draft child of fully GitHub-hosted-green [PR #383](https://github.com/definitely-stable/Mathlab/pull/383), pinned parent HEAD `62fc61376d1190d243968e0e7ca901a120b67570`. Do not change or merge main, root #230/#176/#169 stay OPEN.

## 1. Scientific choice: constructive all-h positive direction, not fabricated all-label theorem

The previous stages G2-H/I proved finite Hall charge for 210 single-swap W32 maps and 21 correlated W32 maps. G2-J computed an EXACT rational necessary constant envelope over 219 W32 maps; **no universal positive alpha** was proved. Another finite sampled search or a necessary rational constraint does not close issue #230. A direct all-label `S_s >= alpha*s^6-beta*Jcross` transfer remains the main proof gap.

Here we exploit the already PROVED one-sided B1-A exact expectation and C0's exact weighted original-source right-sixset overlap for ONE globally coherent f,g to construct actual global right injections, not merely assert an average. This is a restricted constructive theorem for SOME g for EVERY fixed legal f. This DOES NOT prove positive S for every correlated pair f,g, a worst-case right-transfer, all-h `Jcross<=K*S`, or Branch A/B.

The method of conditional expectations is classical (and already formalized in the Archive of Formal Proofs: Karayel, *Derandomization with Conditional Expectations*, 2024/2025). The new work is the exact original-6-incidence weighted six-uniform **sampling-without-replacement conditional formula** and an independently verified globally injective construction in this HYP-105 B/A problem. Do not claim original discovery of the general derandomization technique.

## 2. General exact all-h theorem K-CE (arbitrary source hypergraph)

Let V original right source vertices, K physical pair labels (K>=V>=6), a nonnegative integer weighted original **6-uniform** hypergraph w_R (weights count distinct original incidence sixsets, not arbitrary repeated physical source copies), and a finite family T of physical **6-uniform** target subsets of [K]. For an injection g:[V]->[K] let

```
U(g)= sum_(R subset [V], |R|=6) w_R * 1{g(R) in T}.
```

Under UNIFORM random injection, every original R maps to a uniformly random physical 6-subset:

```
mu=E_g U(g) = (sum_R w_R) * |T| / C(K,6).
```

Fix a partial legal injection `g(0),...,g(k-1)` and let O be its USED physical label set. For an original 6-set R, let F_R be the labels already assigned to original vertices in R, t_R=|F_R|. The remaining images of R are a uniform unordered `(6-t_R)` subset of the `(K-k)` unused physical pair labels. Therefore the **exact** conditional success probability is

```
P(g(R) in T | prefix) =
  |{A in T: A intersect O = F_R}| / C(K-k,6-t_R).
```

This counts BOTH required already assigned physical edges (F_R) and forbids occupied labels assigned to original vertices **OUTSIDE** R. Omitting the second part makes the conditional probability wrong. The denominator is nonzero for a legal injective partial assignment with k<=V. Sum these fractions weighted by original sixset multiplicities to obtain an exact Fraction conditional expectation `Phi(prefix)`.

**Theorem K-CE:** Evaluate `Phi(prefix + p)` for every unused physical label `p`. The law of total expectation gives

```
Phi(prefix) = (1/(K-k)) * sum_(unused p) Phi(prefix+p).
```

Take a maximum (respectively minimum) with deterministic smallest-label tie-break. Thus for a complete legal coherent right injection `g_max`, `U(g_max)>=mu`; for a complete legal coherent `g_min`, `U(g_min)<=mu`. The inequalities hold for EVERY weighted 6-uniform source hypergraph and target family; no independence of distinct R-events is assumed. This is a finite constructive proof and the method requires only finite exact combinatorial sums (for fixed rank six, straightforward exhaustive counts have polynomial input-size bounds, but may have high exponent/memory). No source incidence columns are independently relabeled.

## 3. Specialization to original GQ B-left/A-right

Fix ANY physically injective LEFT original-source mapping `f` for W(3,s), s=2^h. For each six **distinct original right line** source set R, define `w_f(R)` to be the number of **distinct original six-incidence source supports** whose LEFT original profile is B (one original factor cherry and four singles), whose LEFT physical degree-two profile has six coordinates, and whose RIGHT original endpoints equal R (all distinct). This nonnegative original weighted hypergraph is EXACT, and depends only on original GQ and f.

Let the target T consist of all physical pair-edge sixsets inducing a simple 2-regular six-coordinate graph in K_a, i.e., one 6-cycle or two triangles. The number of targets is EXACTLY `70*C(a,6)`, with K=`C(a,2)` physical pair edges. A source sixset contributes to `U_B/A(f,g)` iff its right-image set belongs to T. Thus:

```
mu(f) = (sum_R w_f(R))*70*C(a,6)/C(C(a,2),6),
U_B/A(f,g_max) >= mu(f) >= U_B/A(f,g_min).
```

B1-A's previously proved uniform asymptotics establish `mu(f)=(140+o(1))*s^6` independently of f, subject to its precise existing theorem scope. Therefore for every h and every legal f there is a **deterministically constructible** coherent original right global injection g such that

```
S_seven(f,g) >= U_B/A(f,g) >= mu(f) = (140+o(1))*s^6.
```

This is an **existence-for-each-f** construction, not a universal **for-all-g** conclusion. The same conditional formula produces another explicit global right injection with U_B/A <= mu, explaining why first-moment arguments alone cannot establish an all-label min. It DOES NOT necessarily construct U_B/A=0, and a below-average positive g is not an infinite counterexample to any universal positive lower bound.

## 4. Independent finite actual-original validation

Hosted W32 K6 models: (1) lex left original mapping and (2) a legal multiple-transposition left mapping derived from G2-I's exact correlated path. For each fixed f, construct TWO entirely globally injective right maps (maximize/minimize). For each of the four original W32 maps:
- Compare exact weighted `U_B/A` under the selected real global g against (i) a distinct direct C0 physical-target overlap oracle and (ii) the complete original B0 enumeration of 62,370 eligible left source sixsets / all seven certified positive GF5 classes.
- Verify `S_seven>=U_B/A` and `51^6 R3>= S_class_floor` for true original supports.
- Verify the initial exact rational conditional mean against independent `random_injection_expectation` and the bound `min<=mu<=max`, and verify every prefix tower identity exactly.
- Independently brute-force all remaining full injections for small 7-source/7-physical-label synthetic weighted six-hypergraphs and compare conditional expectations, including the case where a physical label used OUTSIDE R invalidates a target.

No invented random probabilities, no truncation-as-negative, no floating-point. Report exact original sixset counts, all selected pair-label maps and SHA256, class floors, rational mean, and local greedy path transcripts. Never assert any improvement to ASET exponent.

## 5. Novelty and subsequent all-label proof gate

The broad derandomization principle is **classical prior art**, not a new central theorem. The contribution here is a concrete all-h explicit right-injection witness for the known B/A positive mean, with exact original-source combinatorial weight and independent finite oracle. It makes the existential side constructive and isolates the crucial failure of the method for arbitrary adversarial g.

The next genuine all-label task K3-G2-L should analyze the **distance / signed trade / six-coordinate rearrangement** between an arbitrary right injection and these constructed above-mean maps, with exact charge to actual positive original S or Jcross, rather than presuming a Lipschitz telescoping bound: B1-B's per-transposition influence is O(s^12), much too large over O(V) swaps to derive an s^6 min. The C0 3-cube equal-two-marginal trade also rules out a naive marginals-only proof. Alternatively produce a legitimate infinite coherent f,g falsifier. Only a uniform all-h lower proof closes Branch A.

## 6. First genuine W32 deterministic output (GitHub-hosted 2026-10-12)

[Focused Contract #38227910260](https://github.com/definitely-stable/Mathlab/actions/runs/38227910260) **SUCCESS** on original child HEAD `5da127fe9588ba079ec6f787dd1e77e242431f82`. The first hosted oracle was run for TWO legal globally coherent original W(3,2)/K6 left maps. Exactly 70 physical target six-edge 2-factors were used, and all right maps are whole-original-source vertex injections onto the 15 physical edges of K6:

| Fixed original left f | Original source right-sixset weight sum | Exact uniform right mean E[U_B/A] | Constructive max U_B/A | Full true S at max | Constructive min U_B/A | Full true S at min |
|---|---:|---:|---:|---:|---:|---:|
| lex | 5000 | 10000/143 | **131** | **320** | **33** | **101** |
| correlated-left | 5319 | 10638/143 | **120** | **245** | **40** | **104** |

For lex fixed f, `33 < 10000/143 < 131`. For correlated-left, `40 < 10638/143 < 120`. Every one of the four `U_B/A` values was independently recomputed with C0's weighted ORIGINAL-right-sixset physical target oracle and B0's COMPLETE original 62,370-left-candidate seven-family census. Thus they are not artificial template counts and the positive GF5 class floors are strictly additive on true original six-incidence supports.

Full seven-family certified 51^6 GF5 R3 **lower numerators** (not full R3) in max/min order:
- lex: `13,589,291` / `4,629,430`.
- correlated-left: `10,917,154` / `4,681,086`.

Deterministic complete right physical-label SHA256 in max/min order:
- lex: `f06c5203f316494b559d3a5e4ff64a5c381681bca9a82272c40d8831f296972f` / `e9f3bb5e6753513c3eb09803f8566206ccd5fbe8a47c63f9a94d576533c86742`.
- correlated-left: `9e676e01195a181effd96aa554378e527a072710268124fcf0314f2b1456b23b` / `c0c1cd1803903c34dca2b8e31dedee27125756856fe7d55e75cb4b3db78dd226`.

**Interpretation:** The high right injections construct B/A counts above the uniform right mean and hence strictly positive true seven-family S for each of these f. The low right injections demonstrate a real range within globally legal coherent pair maps, but still yield positive B/A counts. Neither map is a general all-h counterexample. This method itself is classical derandomization; its scientific role is a constructive benchmark for the harder arbitrary-right all-label transport theorem. Exact-value regression was added after the first success; final child HEAD CI verification is required.
