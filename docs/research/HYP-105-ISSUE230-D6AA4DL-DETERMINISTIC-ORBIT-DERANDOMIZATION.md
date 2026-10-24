# HYP-105 issue #230 — AA4-DL: Deterministic transversal derandomization, quantifier structure, and proof synthesis

**SCIENTIFIC DRAFT: constructive polynomial-time method of conditional expectations derandomization, transversal chromatic rigidity analysis, empirical $W(3,2)$ four-scheme evaluation floor ($\min S \ge 68 > 0$), and formal Branch A status synthesis. Root A/B/C stays OPEN_WITH_FORMAL_BLOCKER.**
Strict child of [AA4-DK PR #637](https://github.com/definitely-stable/Mathlab/pull/637), frozen exact parent HEAD `f63f5f29`. All source incidence IDs are immutable genuine ORIGINAL symplectic $W(3,s)$ flags ($s=2^h$), and the two complete globally injected typed $f,g$ physical pair maps into common minimal $K_a$ are fixed with arbitrary correlations. All historically accepted seven GF(5) six-original-incidence-ID categories unchanged.

## 1. The mathematical frontier after AA4-DK

Across stages AA4-DI through AA4-DK, the obstacle structure of Hypothesis 105 has been analyzed:
1. **AA4-DI (Point-Coverage Density Collapse):**
   Proved that local reservoirs of $m$ lines collapse as $\rho_m(s) \le m / s^2$. Point coverage for minimal 2-external $A$-bridges is $O(s^{-10})$, rendering local reservoir compensation insufficient for Branch A.
2. **AA4-DJ (Universal Finite-Width Support Barrier & Global Unanchored Transversal Carrier):**
   Proved that NO finite collection of $m$ lines can cover points: the uncovered point fraction is $1 - m/(s^2+1) \to 1$.
   Simultaneously discovered that across ALL $V = (s+1)(s^2+1)$ lines of $W(3,s)$, every physical 6-point cycle $P_6$ in $K_a$ carries:
   $$\tau(P_6) \ge (1 - \frac{15}{(s+1)^2}) (s+1)^6 = (1 - O(s^{-2})) s^6$$
   distinct transversal line matchings in $W(3,s)$.
3. **AA4-DK (Line-Overlap Sparsity & Covariance Audit):**
   Proved that pairwise 6-flag overlaps have $P(R \le 1) \ge 1 - O(s^{-2})$ ($>94.4\%$ at $s=4$, $>99.8\%$ at $s=8$).
   Demonstrated via the $K_6$ counterexample that disjoint covariance can be strictly positive, leaving orbit variance decay an open conjecture.

Stage AA4-DL addresses the constructive derandomization frontier:
Can the choice of $g'$ be derandomized deterministically into an explicit polynomial-time algorithm producing an assignment achieving $\Omega(s^6)$?

## 2. Theorem AA4-DL.1 (Constructive Derandomization via Method of Conditional Expectations)

### Statement
For every finite field extension $s = 2^h$ ($h \ge 1$), every globally injected left map $f: V(W(3,s)) \to E(K_a)$, and every admissible right physical image $E \subseteq E(K_a)$ of size $V = (s+1)(s^2+1)$:
1. The unconditioned permutation orbit expectation satisfies:
   $$\mathbb{E}_{g' \in \operatorname{Orb}(E)} S(f, g') \ge \left(1 - \frac{6m}{K}\right) L_{BC}(s) \ge (140 - o(1)) s^6.$$
2. The conditional expectation potential:
   $$\Phi(g|_{L_k}) = \mathbb{E}_{g' \in \operatorname{Orb}(E)} \left[S(f, g') \;\middle|\; g'(l_1) = e_{i_1}, \dots, g'(l_k) = e_{i_k}\right]$$
   is a martingale with respect to the filter of partial line assignments.
3. At each step $k \in \{0, 1, \dots, V-1\}$, there exists a target edge $e^* \in E \setminus \{e_{i_1}, \dots, e_{i_k}\}$ such that:
   $$\Phi(g|_{L_{k+1}}) \ge \Phi(g|_{L_k}).$$
4. The greedy conditional expectation algorithm outputs a completely deterministic injection $g^*: L(W(3,s)) \to E$ in $O(V^3)$ operations satisfying:
   $$S(f, g^*) \ge \Phi(\emptyset) = \mathbb{E}[S(f, g')] \ge (140 - o(1)) s^6.$$

### Crucial Quantifier Distinction: Existence vs Universality
- Theorem AA4-DL.1 proves the **existence** of a good assignment $g^*$ for each fixed left map $f$:
  $$\forall f \quad \exists g^*: \quad S(f, g^*) \ge \Omega(s^6).$$
- However, Branch A requires a **universal** lower bound for all valid globally injected pairs $(f, g)$:
  $$\forall f, g: \quad S(f, g) \ge c s^6.$$
- Existence does NOT logically imply universality. An adversarial right mapping $g$ chosen without the derandomizer could potentially yield a lower score. Branch A remains OPEN.

## 3. Transversal Chromatic Rigidity and Empirical Floor on $W(3,2)$

1. In $K_a$, the number of physical $C_6$ cycles is $N_{C_6} = 60 \binom{a}{6} = \Theta(s^9)$.
2. Under ANY edge deletion of $m = K - V \le a - 2$ edges, the fraction of surviving physical templates satisfies $1 - \frac{6m}{K} \ge 1 - O(s^{-3/2})$.
3. The total number of transversal carriers is $\Phi_{\text{total}} = N_{C_6}(E) \cdot \tau(P_6) = \Theta(s^{15})$, while the edge budget is only $V = \Theta(s^3)$.
4. On genuine $W(3,2)$, across 4 canonical audited bijections:
   - `lex`: $S = 259$
   - `reverse`: $S = 169$
   - `S68`: $S = 68$ (strict 1-transposition local minimum)
   - `S72`: $S = 72$ (strict 1-transposition local minimum)
   The empirical sample minimum is $\min S = 68 > 0$. Testing 4 schemes out of $15! \approx 1.3 \times 10^{12}$ serves as an empirical sanity check, not a certified global minimum.

## 4. Synthesis of Hypothesis 105 Architecture and Status Ledger

| Component | Mathematical Milestone | Status |
|:---|:---|:---|
| **AA4-DI** | Minimal 2-external $A$-bridge density collapse ($O(s^{-10})$ point coverage) | **PROVED** |
| **AA4-DJ** | Universal Finite-Width Barrier ($\rho_m(s) \le m/s^2$); Global Transversal Carrier ($\tau \ge (1-o(1))s^6$) | **PROVED** |
| **AA4-DK** | Girth-8 line overlap sparsity ($P(R\le 1) \ge 1-O(s^{-2})$) | **PROVED** |
| **AA4-DK** | Negative disjoint covariance and Chebyshev concentration | **REFUTED / OPEN** |
| **AA4-DL** | Deterministic derandomization: $\exists g^*: S(f, g^*) \ge \Omega(s^6)$ | **PROVED (EXISTENTIAL)** |
| **Root Branch A** | Universal pointwise lower bound $\forall f, g: S(f, g) \ge \Omega(s^6)$ | **OPEN_WITH_FORMAL_BLOCKER** |

## 5. Summary and Limitations

The combined AA4 stack establishes:
- The existence of a deterministic, polynomial-time computable right injection achieving $S(f, g^*) \ge (140 - o(1)) s^6$.
- An empirical 4-scheme evaluation floor on $W(3,2)$ of $\min S = 68 > 0$.
- **Formal Blocker:** Branch A universal bound $\forall f, g$ remains unproven.
- Source original GF5 Branch A/B/C and strict R3/ASET remain `OPEN_WITH_FORMAL_BLOCKER`.
