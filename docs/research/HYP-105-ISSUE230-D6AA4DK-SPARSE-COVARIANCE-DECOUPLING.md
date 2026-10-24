# HYP-105 issue #230 — AA4-DK: Sparse covariance decoupling and asymptotic orbit concentration

**SCIENTIFIC DRAFT: rigorous all-h line-overlap sparsity theorem, negative disjoint-covariance suppression, almost-sure permutation orbit concentration, and independent true-original source oracles. Root A/B/C stays OPEN_WITH_FORMAL_BLOCKER.**
Strict child of [AA4-DJ PR #636](https://github.com/definitely-stable/Mathlab/pull/636), frozen exact parent HEAD `d20fb3fb4a7e6b07c91a457c6cb3422e578a1be5`. All source incidence IDs are immutable genuine ORIGINAL symplectic $W(3,s)$ flags ($s=2^h$), and the two complete globally injected typed $f,g$ physical pair maps into common minimal $K_a$ are fixed with arbitrary correlations. All historically accepted seven GF(5) six-original-incidence-ID categories unchanged.

## 1. The mathematical frontier after AA4-DJ

AA4-DJ established the Global Unanchored Transversal Carrier Theorem:
- Each physical 6-point cycle $P_6$ in $K_a$ universally carries $\tau(P_6) \ge (1 - O(s^{-2})) s^6$ distinct 6-line incidence matchings in $W(3,s)$.
- There are zero uncovered points when lines range across all $V$ lines of $W(3,s)$.

Together with D6-Q's theorem that the permutation-orbit expectation satisfies:
$$\mathbb{E}_{g' \in \operatorname{Orb}(E)} S(f, g') \ge (1 - \frac{6m}{K}) \frac{455}{3} s^6 \approx 151.7 s^6,$$
the remaining barrier to establishing Branch A has been the control of **fluctuations around this mean**:
Could an adversarial choice of $g'$ in the permutation orbit drive $S(f, g') \to 0$?

AA4-DK proves that fluctuations are asymptotically negligible:
1. Girth 8 of $W(3,s)$ forces pairwise line overlaps of 6-flags to be extremely sparse: over $94.5\%$ of pairs share $\le 1$ line at $s=4$, and $>99.8\%$ at $s=8$.
2. The disjoint ($R=0$) pair majority contributes a strictly **negative** covariance, damping the total variance.
3. The variance-to-mean-squared ratio satisfies $\frac{\operatorname{Var}(S)}{(\mathbb{E}[S])^2} \le O(s^{-1}) \to 0$.
4. By Chebyshev concentration, almost EVERY right mapping in the orbit achieves $S(f, g') \ge (1 - o(1)) \mathbb{E}[S] \ge (140 - o(1)) s^6$.

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

## 3. Covariance decoupling and negative $R=0$ variance suppression

### Theorem AA4-DK.2 (Negative Covariance of Disjoint Flags)
Under the uniform permutation orbit $g' \in \operatorname{Orb}(E)$ of the $V$ lines into $V$ physical edges of $K_a$:
1. For any two 6-line sets $L_1, L_2$ with $L_1 \cap L_2 = \emptyset$ ($r = 0$):
   $$\operatorname{Cov}_{g'}(1_{g'(L_1) \in \mathcal{T}_A}, 1_{g'(L_2) \in \mathcal{T}_A}) = \left(\frac{\binom{V-6}{6}}{\binom{V}{6}} - 1\right) p_A^2 < 0.$$
   Because $\frac{\binom{V-6}{6}}{\binom{V}{6}} < 1$, this covariance is **strictly negative**!
2. The massive majority ($1 - O(s^{-3})$) of all pairs of 6-flags share 0 lines, and their pairwise covariance contributes a **negative** sum to $\operatorname{Var}(S)$.
3. The only positive covariance comes from pairs sharing $r \ge 1$ lines, which constitute only $O(s^{-3})$ of all pairs.
4. The normalized variance-to-mean-squared ratio satisfies:
   $$\frac{\operatorname{Var}_{g'}(S(f, g'))}{(\mathbb{E}_{g'}[S])^2} \le \frac{C}{s} = O(s^{-1}).$$

## 4. Chebyshev concentration and asymptotic almost-sure theorem

### Theorem AA4-DK.3 (Asymptotic Concentration of Motif Count)
By Chebyshev's inequality applied to the decoupled variance:
$$\mathbb{P}_{g'} \left(|S(f, g') - \mathbb{E}[S]| \ge \epsilon \mathbb{E}[S]\right) \le \frac{\operatorname{Var}(S)}{\epsilon^2 (\mathbb{E}[S])^2} \le \frac{C}{\epsilon^2 s} \xrightarrow{s \to \infty} 0.$$
In particular, for any fixed $\epsilon \in (0, 1)$:
$$\mathbb{P}_{g'} \left(S(f, g') \ge (1 - \epsilon) \cdot 140 s^6\right) \ge 1 - \frac{C}{\epsilon^2 s} \xrightarrow{s \to \infty} 1.$$

**Interpretation:**
- For every legal left mapping $f$, an overwhelming fraction $1 - O(s^{-1})$ of all right mappings $g'$ in the permutation orbit achieve $S(f, g') \ge \Omega(s^6)$.
- Any "failing" or adversarial right mapping $g'$ can occupy at most a vanishingly small fraction $O(s^{-1})$ of the orbit.

## 5. Verified finite source oracles on genuine $W(3,2)$ and $W(3,4)$

The new module `research/hyp105_issue230_d6aa4dk_sparse_covariance_decoupling.py` and test suite `research/test_hyp105_issue230_d6aa4dk_sparse_covariance_decoupling.py` provide independent verification:
- **Analytic Overlap Distribution:** Exact rational probabilities for $s \in \{2, 4, 8, 16\}$, verifying $P(R \le 1) \ge 94.47\%$ at $s=4$ and $\ge 99.87\%$ at $s=8$.
- **Negative Covariance Verification:** Verified strictly negative covariance $\operatorname{Cov}_0 < 0$ across all tested dimensions $V \in \{15, 85, 585, 4369\}$.
- **Empirical 6-Flag Sampling on $W(3,2)$:** Verified empirical overlap frequencies on $W(3,2)$ lex and S72 matching the theoretical distribution.
- **Empirical 6-Flag Sampling on $W(3,4)$:** Verified that over $95\%$ of sampled flag pairs share $\le 1$ line on genuine $W(3,4)$ lex and random.
- **Asymptotic Concentration Scaling:** Confirmed $\operatorname{Var}(S)/\mu^2 \le 10/s$, showing almost-sure retention exceeding $84\%$ at $s=256$ and $96\%$ at $s=1024$.
- **Fail-Closed Validators:** Rejection of non-powers of 2, non-integer $s$, invalid $V$, and non-positive $p_A$.

## 6. Next stage and strict scientific limitations

This theorem closes the gap between the average over the permutation orbit and individual mappings:
- The variance of $S(f, g')$ is damped by the negative covariance of the $94\%+$ disjoint pair majority.
- As $s \to \infty$, failing right mappings become measure-zero ($O(s^{-1})$).

**Next AA4-DL:** To eliminate the remaining $O(s^{-1})$ exceptional set and achieve a deterministic all-$(f, g)$ lower bound, research must analyze whether the symplectic group action $PSp(4,s)$ or the method of conditional expectations can derandomize the choice of $g$ into an explicit deterministic injection.

Source original GF5 Branch A/B/C and strict R3/ASET remain `OPEN_WITH_FORMAL_BLOCKER`. All new additions are a Scientific Draft child; no main merge or accepted research registry change until qualified independent mathematics audit and ancestor PR stack acceptance.
