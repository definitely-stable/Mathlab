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
3. **Typed Bad Endpoint Pair Ratio:** Over genuinely nonincident source (POINT, LINE) pairs $V_{\text{noninc}} = V s^2 (s + 1)$, the fraction of pairs sharing an exterior coordinate is bounded by:
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

### Theorem 3 (Unweighted TYPED Source Bad Endpoint Bound)
For every genuinely original **POINT** $q$ and **LINE** $r$ that are nonincident,
the unique source 3-edge path is $q-l_0-p-r$. Define left-bad by
$f(q)\cap f(p)\ne\varnothing$, right-bad by
$g(l_0)\cap g(r)\ne\varnothing$. For fixed $q$,
at most $2(a-2)$ other source POINT images overlap $f(q)$.
Each collinear $p$ has exactly $s$ eligible nonincident lines $r$
whose unique original projection goes through $p$. Therefore
$|E_L|\le 2Vs(a-2)$, and by duality $|E_R|\le 2Vs(a-2)$.
A union bound, with no independence assumption, gives
$$|E_L\cup E_R|\le 4Vs(a-2),\qquad
\rho_E\le\frac{4(a-2)}{s(s+1)}=O(s^{-1/2}).$$

**Scope:** these are *unweighted original typed point/line endpoints*,
not physical 3-walks and not GF(5)-accepted six-original-incidence motifs.

---

## 3. Concrete Certified Refutation: $\mathrm{BBo} = 5261 < 5768$

In previous iterations, it was conjectured that:
$$\operatorname{BBo}(f, g) \ge 8 c_0(s) s^6.$$
For $s=4$, using $c_0(4) = 0.176$, this asserted $\operatorname{BBo} \ge \lceil 8 \cdot 0.176 \cdot 4096 \rceil = 5768$.

### Explicit Finite Witness and Reproducible Numerical Refutation:
Using simulated annealing on $W(3,4)$, an explicit global labeling $(f^*, g^*)$ was found with:
$$\operatorname{BBo}(f^*, g^*) = \mathbf{5,261 \le 5,400 < 5,768.}$$
- **Full Certificate:** [JSON physical maps](../../research/hyp105_w34_adversarial_certificate.json).
- **Independent Verification:** [independent oracle](../../research/hyp105_w34_independent_oracle.py) enumerates original GF(4) flags, physical 3-walks and unique source projections without optimizer/certificate count reuse. [Regression tests](../../research/test_hyp105_w34_adversarial_certificate.py) compare every integer census field.
- **Deficit:** 507 motifs for the explicit witness; this is NOT a proven global minimum.

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
   Cauchy–Schwarz states
   $$\sum_{E_{\mathrm{bad}}}N_3\le |E_{\mathrm{bad}}|^{1/2}(\sum N_3^2)^{1/2}.$$
   The former argument incorrectly derived an upper bound from
   $\sum N_3^2=\Omega(s^7)$. That is **invalid**: a lower moment
   bound cannot upper-bound the right-hand side. Even assuming a
   separately established $O(s^7)$ upper second moment (not proved here),
   the union bound $|E_{\mathrm{bad}}|=O(s^{11/2})$ only yields
   $O(s^{25/4})$, too weak for $o(s^6)$.
   This weighted path-multiplicity transfer is OPEN.

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


## 6. Proof-quality remediation (25 Oct 2026)

- Exact minimal-alphabet parameter arithmetic now uses `math.isqrt` for every dyadic exponent, including $h=1024$, rather than float square root.
- The witness $BBo=5261$ is independently reconstructed from the explicit $(f,g)$ physical edges and true immutable original symplectic incidence flags; it is NOT an optimization lower bound.
- Typed endpoint bad-pair bounds cannot be promoted to path-weighted risk without an independent multiplicity/correlation estimate.
- The earlier purported $O(s^{25/4})$ bound derived from an `Omega(s^7)` second-moment statement is withdrawn as invalid.
- Root issue #230 remains OPEN_WITH_FORMAL_BLOCKER; no result on all-seven GF(5) original sixflag (S_s) or R3/ASET exponents.
