# HYP-105: Extremal Coordinate Invariants, Certified Adversarial Minimization, and Formal Blockers

> **STATUS: DRAFT / OPEN_WITH_FORMAL_BLOCKER**  
> **Repository:** `definitely-stable/Mathlab`  
> **Issue:** #230  
> **Target Branch:** `main`

---

## 1. Executive Summary

This monograph provides a clean, self-contained presentation of the proved combinatorial invariants on coordinate degree distributions in the symplectic generalized quadrangle $W(3,s)$, the certified adversarial counterexample on $W(3,4)$ refuting candidate sextic lower bounds, and the three formal blockers preventing universal asymptotic closure.

### Key Proved Findings:
1. **Coordinate Degree Conservation:** For any injective pair embeddings $f: P \hookrightarrow \binom{[a]}{2}$ and $g: L \hookrightarrow \binom{[a]}{2}$ into the minimal complete graph $K_a$ ($a \approx \sqrt{2} s^{3/2}$), the degree sequence in $K_a$ satisfies $\sum_{u=0}^{a-1} d_u = 2V$. Because the number of missing edges is $m = \binom{a}{2} - V \le a - 2 < a$, the degree pair sum satisfies:
   $$\sum_{u=0}^{a-1} \binom{d_u}{2} = (\sqrt{2} + o(1)) s^{9/2},$$
   with variation bounded by $O(a^2) = O(s^3)$.
2. **Collinear Pencil Compression:** By $C_4$-freeness of $W(3,s)$ (girth 8), any two points share at most one line. Thus:
   $$\sum_{l \in L} \binom{v_l(u)}{2} \le \binom{d_u}{2} \implies \sum_{u=0}^{a-1} \sum_{l \in L} \binom{v_l(u)}{2} \le (\sqrt{2} + o(1)) s^{9/2}.$$
3. **Bad Endpoint Pair Ratio:** Over total non-incident pairs $V_{\text{noninc}} = V s^2 (s + 1)$, the fraction of pairs sharing an exterior coordinate is bounded by:
   $$\rho_E \le \frac{4(a - 2)}{s(s + 1)} = O(s^{-1/2}).$$
4. **Certified Refutation of Candidate Floor $5768$:** The candidate lower bound $\mathrm{BBo} \ge 8 c_0(4) 4^6 = 5768$ (asserted with $c_0(4) = 0.176$) is refuted by the certified adversarial configuration reaching $\mathrm{BBo} = 5,261 \le 5,400 < 5,768$ (deficit $\ge 368$ motifs).

---

## 2. Combinatorial Theorems (PROVED)

### Theorem 1 (Extremal Coordinate Degree Invariant)
Let $W(3,s)$ be the generalized quadrangle of order $(s, s)$ with $V = (s+1)(s^2+1)$ points and lines, where $s = 2^h, h \ge 1$. Let $a = \min\{t \in \mathbb{N} : \binom{t}{2} \ge V\}$.
Then $a = (\sqrt{2} + o(1)) s^{3/2}$ and $m = \binom{a}{2} - V \le a - 2$.

For any injective mapping $f: P \to \binom{[a]}{2}$, let $d_u = |\{q \in P : u \in f(q)\}|$ be the degree of vertex $u$ in the image graph $G_f \subseteq K_a$.
Let $\delta_u = (a - 1) - d_u$ be the defect degree in the complement graph $\overline{G_f}$.
Then:
1. $\sum_{u=0}^{a-1} d_u = 2V$, with $0 \le d_u \le a - 1$.
2. $\sum_{u=0}^{a-1} \delta_u = 2m \le 2(a - 2)$.
3. The quadratic potential satisfies:
   $$\sum_{u=0}^{a-1} d_u(d_u - 1) \le 2V(a - 2).$$
4. The exact degree pair sum identity:
   $$\sum_{u=0}^{a-1} \binom{d_u}{2} = \frac{a(a-1)(a-2)}{2} - (2a-3)m + \frac{1}{2}\sum_{u=0}^{a-1}\delta_u^2.$$
   Since $\frac{1}{2}\sum \delta_u^2 \le \frac{m(m+1)}{2} \le \frac{(a-2)(a-1)}{2} = O(s^3)$, the leading asymptotic behavior is:
   $$\boxed{\sum_{u=0}^{a-1} \binom{d_u}{2} = (\sqrt{2} + o(1)) s^{9/2}.}$$

> [!NOTE]
> The leading coefficient is $\sqrt{2} \approx 1.4142$, NOT $1/\sqrt{2} \approx 0.7071$.

### Theorem 2 (Collinear Pencil Collision Law)
For each line $l \in L$ and coordinate $u \in [a]$, let $v_l(u) = |\{q \in l : u \in f(q)\}|$.
Because $W(3,s)$ has girth 8 ($C_4$-free bipartite incidence graph), any two points share at most 1 line.
Therefore, every collinear pair of points sharing coordinate $u$ appears in exactly one line pencil $l$, while non-collinear pairs appear in zero line pencils:
$$\sum_{l \in L} \binom{v_l(u)}{2} \le \binom{d_u}{2}.$$
Summing over all coordinates $u \in [a]$:
$$\boxed{\sum_{u=0}^{a-1} \sum_{l \in L} \binom{v_l(u)}{2} \le \sum_{u=0}^{a-1} \binom{d_u}{2} \le (\sqrt{2} + o(1)) s^{9/2}.}$$

### Theorem 3 (Bad Endpoint Pair Ratio Bound)
A non-incident point pair $(q, r)$ is left-bad if there exists a line $l \ni q$ and $q' \in l$ such that $f(q') \cap f(r) \neq \emptyset$.
The total number of bad non-incident endpoint pairs is bounded by:
$$|E_{\text{bad}}| \le 4s V (a - 2).$$
Over total non-incident pairs $V_{\text{noninc}} = V s^2 (s + 1)$:
$$\rho_E = \frac{|E_{\text{bad}}|}{V_{\text{noninc}}} \le \frac{4(a - 2)}{s(s + 1)} = O(s^{-1/2}).$$

---

## 3. Concrete Certified Refutation: $\mathrm{BBo} = 5261 < 5768$

In previous iterations, it was conjectured that:
$$\operatorname{BBo}(f, g) \ge 8 c_0(s) s^6.$$
For $s=4$, using $c_0(4) = 0.176$, this asserted $\operatorname{BBo} \ge \lceil 8 \cdot 0.176 \cdot 4096 \rceil = 5768$.

### Certified Numerical Refutation:
Using simulated annealing on $W(3,4)$, an explicit global labeling $(f^*, g^*)$ was found with:
$$\operatorname{BBo}(f^*, g^*) = \mathbf{5,261 \le 5,400 < 5,768.}$$
- **Full Certificate:** Saved in [`research/hyp105_w34_adversarial_certificate.json`](file:///c:/Reposit/math%20lab/research/hyp105_w34_adversarial_certificate.json).
- **Independent Verification:** Tested in [`research/test_hyp105_w34_adversarial_certificate.py`](file:///c:/Reposit/math%20lab/research/test_hyp105_w34_adversarial_certificate.py) using raw $W(3,4)$ symplectic incidences.
- **Deficit:** At least 368 motifs below the candidate floor (507 motifs below for quench).

### Root Cause: Conflation of Path Spaces
The candidate lower bound conflated different path universes:
- $P_{\text{total}}$: All directed 3-walks in bipartite $W(3,s)$ ($= 6,800$ on $W(3,4)$).
- $P_{\text{proper}}$: Proper physical 3-walks with distinct vertices in $K_a$ ($= 70,476$ on $W(3,4)$).
- $P_{\text{noninc}}$: Proper physical 3-walks whose endpoints are non-incident in $W(3,s)$ ($= 58,730$ on $W(3,4)$).
- $P_{\text{unblocked}}$: Non-incident proper 3-walks free of collisions ($= 10,522$ on $W(3,4)$).
- $\operatorname{BBo} = \frac{1}{2} P_{\text{unblocked}} = 5,261$.

Ratios measured with respect to one space cannot be directly multiplied by total raw path counts without rigorous inclusion-exclusion calibration.

---

## 4. The Three Open Formal Blockers

The following three formal blockers prevent concluding $B(f, g) = o(s^6)$ or $\operatorname{BBo} = \Omega(s^6)$ unconditionally:

1. **P0 — Path Multiplicity Barrier:**
   $\rho_E \le \frac{4(a-2)}{s(s+1)}$ bounds the fraction of bad endpoint pairs, NOT physical 3-paths.
   The total bad path mass is:
   $$|E(f, g)| = \sum_{(q, r) \in E_{\text{bad}}} N_3(q, r).$$
   Physical 3-walk multiplicity $N_3(u, v)$ between physical vertices varies widely (reaching 18 on $W(3,4)$, max 57).
   By Cauchy-Schwarz:
   $$\sum_{(q, r) \in E_{\text{bad}}} N_3(q, r) \le |E_{\text{bad}}|^{1/2} \left(\sum N_3^2\right)^{1/2} = O(s^{5.5/2}) \cdot \Omega(s^{7/2}) = \mathbf{O(s^{6.25})} \gg O(s^6).$$
   Bounding $|E(f, g)| = o(s^6)$ requires a non-trivial bound on the weighted second moment of $N_3$ restricted to $E_{\text{bad}}$, which remains open.

2. **P0 — Conditioned Layer Density:**
   Internal collisions occur along intermediate steps of 3-walks. Bounding $I(f, g) = o(s^6)$ requires controlling coordinate collisions conditioned on projection layers $\mathcal{F}(p)$. The global spectral gap of $W(3,s)$ does not govern this conditional distribution.

3. **P1 — Small-$s$ Theoretical Bound Failure:**
   The analytical bound $\frac{4(a-2)}{s(s+1)}$ exceeds $1.0$ for all $s \le 31$:
   - $s=2$: $2.667 > 1$
   - $s=4$: $2.400 > 1$
   - $s=8$: $1.833 > 1$
   - $s=16$: $1.353 > 1$
   - $s=32$: $0.981 < 1$
   - $s=64$: $0.701 < 1$
   For finite $s \le 31$, the analytical upper bound exceeds 100% of all pairs and provides zero guaranteed positive floor on good pairs.

---

## 5. Formal Resolution Status

```json
{
  "Hypothesis": 105,
  "Issue": 230,
  "Status": "OPEN_WITH_FORMAL_BLOCKER",
  "Branch_A": "OPEN_WITH_FORMAL_BLOCKER (Path multiplicity barrier Omega(s^7))",
  "Branch_B": "OPEN_NOT_REFUTED (Asymptotic o(s^6) family unproved)",
  "Proved_Lemmas": [
    "Extremal Coordinate Degree Invariant (sum d_u(d_u-1) <= 2V(a-2))",
    "Collinear Pencil Compression Law (sum_l binom(v_l(u), 2) <= binom(d_u, 2))",
    "Bad Endpoint Pair Ratio Bound (rho_E <= 4(a-2)/(s(s+1)) = O(s^-1/2))",
    "Certified Adversarial Counterexample BBo = 5261 <= 5400 < 5768"
  ]
}
```
