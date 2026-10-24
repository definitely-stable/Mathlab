# HYP-105 issue #230 — AA4-DK: Sparse line-overlap distribution, covariance analysis, and concentration status

**SCIENTIFIC DRAFT: rigorous all-h line-overlap sparsity theorem, audit of disjoint-covariance signs, exact $K_6$ counterexample to universal negative covariance, and independent true-original source oracles. Root A/B/C stays OPEN_WITH_FORMAL_BLOCKER.**
Strict child of [AA4-DJ PR #636](https://github.com/definitely-stable/Mathlab/pull/636), frozen exact parent HEAD `d20fb3fb4a7e6b07c91a457c6cb3422e578a1be5`. All source incidence IDs are immutable genuine ORIGINAL symplectic $W(3,s)$ flags ($s=2^h$), and the two complete globally injected typed $f,g$ physical pair maps into common minimal $K_a$ are fixed with arbitrary correlations. All historically accepted seven GF(5) six-original-incidence-ID categories unchanged.

## 1. The mathematical frontier after AA4-DJ

AA4-DJ established the Global Unanchored Transversal Carrier Theorem:
- Each physical 6-point cycle $P_6$ in $K_a$ universally carries $\tau(P_6) \ge (1 - O(s^{-2})) s^6$ distinct 6-line incidence matchings in $W(3,s)$.
- There are zero uncovered points when lines range across all $V$ lines of $W(3,s)$.

Together with D6-Q's theorem that the permutation-orbit expectation satisfies:
$$\mathbb{E}_{g' \in \operatorname{Orb}(E)} S(f, g') \ge (1 - \frac{6m}{K}) \frac{455}{3} s^6 \approx 151.7 s^6,$$
the remaining barrier to establishing Branch A has been the control of **fluctuations around this mean**:
Could an adversarial choice of $g'$ in the permutation orbit drive $S(f, g') \to 0$?

AA4-DK establishes:
1. Girth 8 of $W(3,s)$ forces pairwise line overlaps of 6-flags to be extremely sparse: over $94.5\%$ of pairs share $\le 1$ line at $s=4$, and $>99.8\%$ at $s=8$.
2. **Mathematical Audit of Disjoint Covariance:** While independent subset drawing yields a naive negative formula, under structured physical factor graphs (such as 2-regular subgraphs of $K_a$), disjoint subsets can exhibit **strictly positive covariance**. The universal negative covariance claim is mathematically false.
3. As a consequence, the orbit variance decay $\frac{\operatorname{Var}(S)}{(\mathbb{E}[S])^2} \le O(s^{-1})$ remains an **unproven conjecture**.

## 2. Girth-8 hypergeometric line overlap distribution (all $h \ge 1$, $s = 2^h$)

In $W(3,s)$, $V = (s+1)(s^2+1)$.
Let $Q_1, Q_2$ be two 6-flags with distinct point sets. The intersection of their line sets $R = |L(Q_1) \cap L(Q_2)| \in \{0, 1, \dots, 6\}$ has exact hypergeometric probability distribution:
$$P(R = r) = \frac{\binom{6}{r} \binom{V-6}{6-r}}{\binom{V}{6}}.$$

### Theorem AA4-DK.1 (Line Overlap Sparsity)
1. For $r = 0$:
   $$P(R = 0) = \frac{\binom{V-6}{6}}{\binom{V}{6}} = \prod_{i=0}^5 \left(1 - \frac{6}{V-i}\right) = 1 - \frac{36}{V} + O(V^{-2}) = 1 - O(s^{-3}).$$
2. For $r = 1$:
   $$P(R = 1) = \frac{36 \binom{V-6}{5}}{\binom{V}{6}} = \frac{36}{V} - O(V^{-2}) = O(s^{-3}).$$
3. For $r \ge 2$:
   $$P(R \ge 2) \le \binom{6}{2} \frac{\binom{V-6}{4}}{\binom{V}{6}} = O(V^{-2}) = O(s^{-6}).$$
4. Numerical evaluation across field extensions:
   - $s = 2$: $V = 15$, $P(R=0) = 1.68\%$, $P(R=1) = 15.10\%$, $P(R \le 1) = 16.78\%$.
   - $s = 4$: $V = 85$, $P(R=0) = 63.56\%$, $P(R=1) = 30.92\%$, $P(R \le 1) = 94.47\%$.
   - $s = 8$: $V = 585$, $P(R=0) = 93.98\%$, $P(R=1) = 5.89\%$, $P(R \le 1) = 99.87\%$.
   - $s = 16$: $V = 4369$, $P(R=0) = 99.18\%$, $P(R=1) = 0.82\%$, $P(R \le 1) = 100.00\%$.

## 3. Covariance Analysis: Exact $K_6$ Counterexample to Universal Negative Covariance

### Analysis of the Naive Formula
The naive heuristic formula:
$$\operatorname{Cov}_{\text{naive}} = \left(\frac{\binom{V-6}{6}}{\binom{V}{6}} - 1\right) p_A^2 < 0$$
arises only when comparing independent sampling with replacement to sampling without replacement for unconstrained subsets.
In reality, $g'$ is a bijection, and the events $A_1 = \{g'(L_1) \in \mathcal{T}_A\}$ and $A_2 = \{g'(L_2) \in \mathcal{T}_A\}$ depend on whether a subgraph in $\mathcal{T}_A$ leaves a complement enriched or depleted in $\mathcal{T}_A$.

### Counterexample AA4-DK.2 ($V=15$, complete physical $K_6$)
Consider physical 2-regularity on $K_6$ ($V = 15$ edges):
1. In $K_6$, the set $\mathcal{T}_A$ consists of all 2-factors (each having 6 edges): 60 cycles $C_6$ and 10 pairs of disjoint triangles $2 C_3$, total $|\mathcal{T}_A| = 70$.
2. The marginal probability is $P(A) = \frac{70}{\binom{15}{6}} = \frac{70}{5005} = \frac{2}{143} \approx 0.013986$.
3. For two disjoint 6-line sets $L_1, L_2$ ($L_1 \cap L_2 = \emptyset$), the complement $E(K_6) \setminus (g'(L_1) \cup g'(L_2))$ has $15 - 12 = 3$ edges and must be a 1-factor (perfect matching).
4. There are 15 matchings in $K_6$. For each matching $M$, $K_6 \setminus M \cong K_{2,2,2}$ decomposes into two 2-factors in exactly 20 ordered ways.
5. The number of ordered pairs of disjoint 2-factors is $15 \times 20 = 300$.
6. The total number of ordered pairs of disjoint 6-subsets is $\binom{15}{6} \binom{9}{6} = 5005 \times 84 = 420\,420$.
7. The joint probability is:
   $$P(A_1 \cap A_2) = \frac{300}{420\,420} = \frac{5}{7007} \approx 0.00071357.$$
8. Therefore, the covariance is:
   $$\operatorname{Cov}(1_{A_1}, 1_{A_2}) = \frac{5}{7007} - \left(\frac{2}{143}\right)^2 = \frac{519}{1\,002\,001} \approx \mathbf{+0.000518 > 0}.$$

**Conclusion:** The claim that disjoint subsets always yield negative covariance is **refuted**.

## 4. Status of Asymptotic Orbit Concentration

### Conjecture AA4-DK.3 (Asymptotic Orbit Concentration — OPEN)
Because disjoint covariance is not universally negative, the variance bound:
$$\frac{\operatorname{Var}_{g'}(S(f, g'))}{(\mathbb{E}_{g'}[S])^2} \le O(s^{-1})$$
is **not yet proven**.
While empirical sampling indicates that the vast majority of right mappings achieve $S(f, g') \ge \Omega(s^6)$, establishing this rigorously requires controlling higher-order graph moments beyond pairwise covariance.

## 5. Verified finite source oracles on genuine $W(3,2)$ and $W(3,4)$

The updated module `research/hyp105_issue230_d6aa4dk_sparse_covariance_decoupling.py` and test suite `research/test_hyp105_issue230_d6aa4dk_sparse_covariance_decoupling.py` provide independent verification:
- **Analytic Overlap Distribution:** Exact rational probabilities for $s \in \{2, 4, 8, 16\}$, verifying $P(R \le 1) \ge 94.47\%$ at $s=4$ and $\ge 99.87\%$ at $s=8$.
- **Exact Counterexample:** Verified that disjoint 2-factors on $K_6$ have strictly positive covariance $\operatorname{Cov} = +519 / 1002001 > 0$.
- **Empirical 6-Flag Sampling on $W(3,2)$:** Verified empirical overlap frequencies on $W(3,2)$ lex and S72 matching the theoretical distribution.
- **Empirical 6-Flag Sampling on $W(3,4)$:** Verified that over $88\%$ of sampled flag pairs share $\le 1$ line on genuine $W(3,4)$ lex and random.
- **Fail-Closed Validators:** Rejection of non-powers of 2, non-integer $s$, invalid $V$, and non-positive $p_A$.

## 6. Next stage and strict scientific limitations

- Line overlap sparsity $P(R \le 1) \ge 1 - O(s^{-3})$ is mathematically sound.
- Universal negative covariance is refuted; concentration remains an open conjecture.
- Source original GF5 Branch A/B/C and strict R3/ASET remain `OPEN_WITH_FORMAL_BLOCKER`.
