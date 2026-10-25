# HYP-105 Phase 2: Analytical Cheeger Infimum & Negative Association Feasibility Study

**SCIENTIFIC MONOGRAPH: Critical evaluation of Negative Cylinder Dependence under structured graph constraints, audit of the Cheeger isoperimetric constant $h(\mathcal{G})$, and calibration against the $K_6$ positive-covariance counterexample.**

---

## 1. Executive Summary

Phase 2 explores potential routes to upgrade the orbit average lower bounds of Hypothesis 105 to exponential concentration and a pointwise universal infimum.
This study establishes:
1. **Negative Association Barrier:** The classical Dubhashi–Ranjan (1998) negative association for permutation coordinates does **not** transfer to indicator variables of composite graph subgraphs (such as 2-regular subgraphs or 6-cycles). The $V=15, K_6$ counterexample exhibits strictly positive covariance $\operatorname{Cov} \approx +0.000518 > 0$, refuting negative association for 2-factor indicators.
2. **Cheeger Infimum as Open Conjecture:** The Cheeger isoperimetric constant $h(\mathcal{G}) \ge \frac{d - \lambda_2}{2d} = \frac{1}{2} - O(s^{-1/2})$ provides a compelling heuristic for boundary retention, but converting edge flux into signed 6-cycle motif retention without averaging over permutations remains an open mathematical conjecture.

---

## 2. Mathematical Audit: Negative Association & The $K_6$ Obstruction

### Classical Negative Association vs Composite Graph Indicators
A family of random variables is negatively associated (NA) only if $\operatorname{Cov}(f, g) \le 0$ for all coordinatewise non-decreasing functions of disjoint sets of variables.
While single-coordinate bin indicators under a uniform permutation are negatively associated, the indicator $I_Q = 1_{\{g(L(Q)) \in \mathcal{T}_A\}}$ of a 6-line set forming a physical 2-factor is a non-monotone composite function of 6 coordinates.

### The $K_6$ Counterexample ($V=15$)
In $K_6$, for two disjoint 6-line sets $L_1, L_2$ ($L_1 \cap L_2 = \emptyset$):
$$P(A) = \frac{70}{5005} = \frac{2}{143}, \qquad P(A_1 \cap A_2) = \frac{300}{420\,420} = \frac{5}{7007}.$$
$$\operatorname{Cov}(I_{L_1}, I_{L_2}) = \frac{5}{7007} - \left(\frac{2}{143}\right)^2 = \frac{519}{1\,002\,001} \approx \mathbf{+0.000518 > 0}.$$

Because $\operatorname{Cov} > 0$, negative association is violated. Therefore, simple Chernoff lower tail bounds based on negative association cannot be directly applied without controlling the positive graph-regularity covariance terms.

---

## 3. The Analytical Cheeger Infimum Conjecture

### Bipartite Cheeger Constant
Let $\mathcal{G} = (V \cup L, \mathcal{I})$ be the $(s+1)$-regular bipartite incidence graph of $W(3,s)$ with second eigenvalue $\lambda_2 = \sqrt{2s}$.
The Cheeger isoperimetric constant satisfies:
$$h(\mathcal{G}) \ge \frac{d - \lambda_2}{2d} = \frac{s + 1 - \sqrt{2s}}{2(s + 1)} \xrightarrow{s \to \infty} \frac{1}{2}.$$

### Conjecture (Cheeger Motif Retention — OPEN)
It is conjectured that the boundary expansion guaranteed by $h(\mathcal{G})$ prevents an adversary from isolating lines without triggering incident vertex collisions:
$$\inf_{f, g} S(f, g) \ge \left( \frac{455}{3} \cdot h(\mathcal{G})^2 - o(1) \right) s^6.$$
If proven, this would imply an asymptotic pointwise floor of $\approx 37.91 s^6$ for all valid pairs $(f, g)$.
However, a rigorous reduction from isoperimetric edge cuts to multi-edge signed cycle configurations remains an open research frontier.

---

## 4. Status Summary

- Exponential Chernoff via Negative Association: **BLOCKED BY POSITIVE COVARIANCE COUNTEREXAMPLE**.
- Pointwise Cheeger Infimum: **OPEN CONJECTURE**.
- HYP-105 status: **OPEN_WITH_FORMAL_BLOCKER**.
