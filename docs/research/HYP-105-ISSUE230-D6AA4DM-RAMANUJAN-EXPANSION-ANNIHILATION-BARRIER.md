# HYP-105 issue #230 — AA4-DM: Ramanujan expander spectrum, simultaneous annihilation analysis, and Branch B status

**SCIENTIFIC DRAFT: super-Ramanujan bipartite incidence spectrum of $W(3,s)$, exact spectrum multiplicities, expander mixing flux analysis, simultaneous $D6/BA/AB$ annihilation conjecture, verified genuine $W(3,2)$ empirical trade-off floor ($\min(D6+BA+AB) = 65 > 0$), and status of Branch B infinite counterfamilies. Root A/B/C stays OPEN_WITH_FORMAL_BLOCKER.**
Strict child of [AA4-DL PR #638](https://github.com/definitely-stable/Mathlab/pull/638), frozen exact parent HEAD `98394306`. All source incidence IDs are immutable genuine ORIGINAL symplectic $W(3,s)$ flags ($s=2^h$), and the two complete globally injected typed $f,g$ physical pair maps into common minimal $K_a$ are fixed with arbitrary correlations. All historically accepted seven GF(5) six-original-incidence-ID categories unchanged.

## 1. The mathematical frontier after AA4-DL

AA4-DL proved:
1. The Method of Conditional Expectations provides a deterministic, polynomial-time algorithm producing an explicit right injection $g^*$ satisfying:
   $$S(f, g^*) \ge \mathbb{E}[S(f, g')] \ge (140 - o(1)) s^6.$$
2. On genuine $W(3,2)$, across 4 audited bijections, $\min S(f, g) \ge 68 > 0$.

However, the question remained:
Could an adversary construct an infinite sequence of globally injected pairs $(f_s, g_s)$ across dyadic $s = 2^h$ with $S(f_s, g_s) = o(s^6)$ (Branch B)?
As established in AA4-BH, achieving $S(f_s, g_s) = o(s^6)$ would require forcing **BOTH** $D6 \to 0$ AND the non-A/A compensated classes ($B/A, A/B, C/A, B/B$) to zero simultaneously.

Stage AA4-DM investigates whether the Ramanujan bipartite expander spectrum of $W(3,s)$ forces a trade-off preventing simultaneous annihilation.

## 2. Theorem AA4-DM.1 (Super-Ramanujan Spectrum and Multiplicities of $W(3,s)$)

For any dyadic prime power $s = 2^h$ ($h \ge 1$):
1. The bipartite incidence graph $\mathcal{G} = (V \cup L, \mathcal{I})$ of the generalized quadrangle $W(3,s)$ has:
   - Vertices: $2V = 2(s+1)(s^2+1)$ (with $|V| = |L| = (s+1)(s^2+1)$).
   - Regular degree: $d = s + 1$.
2. The adjacency spectrum of $\mathcal{G}$ and its exact multiplicities:
   - $\pm (s + 1)$ with multiplicity **1 each** (total 2);
   - $\pm \sqrt{2s}$ with multiplicity **$\frac{1}{2} s(s+1)^2$ each** (total $s(s+1)^2$);
   - $0$ with multiplicity **$s(s^2+1)$**.
   Total multiplicity sum: $2 + s(s+1)^2 + s(s^2+1) = 2(s+1)(s^2+1) = 2V$.
   
   **Numerical evaluation across field extensions:**
   - $s = 2$ ($2V = 30$ vertices): $\pm 3$ (mult 1 each), $\pm 2$ (mult 9 each), $0$ (mult 10). Sum = $2 + 18 + 10 = 30$.
   - $s = 4$ ($2V = 170$ vertices): $\pm 5$ (mult 1 each), $\pm \sqrt{8}$ (mult 50 each), $0$ (mult 68). Sum = $2 + 100 + 68 = 170$.
3. The second eigenvalue is $\lambda_2 = \sqrt{2s}$. Because $\sqrt{2} \approx 1.414 < 2$, we have:
   $$\lambda_2 = \sqrt{2s} < 2\sqrt{s} = 2\sqrt{d - 1}.$$
   Therefore, $\mathcal{G}$ is **strictly super-Ramanujan**.
4. The expander mixing ratio satisfies:
   $$\frac{\lambda_2}{d} = \frac{\sqrt{2s}}{s+1} = O(s^{-1/2}) \xrightarrow{s \to \infty} 0.$$

## 3. Conjecture AA4-DM.2 (Simultaneous Annihilation Barrier — OPEN)

### Statement
For any dyadic field extension $s = 2^h$ ($h \ge 1$) and ANY globally injected physical mapping pair $(f, g)$:
1. By the Bipartite Expander Mixing Lemma:
   $$\left|e(X, Y) - \frac{s+1}{V} |X| |Y|\right| \le \sqrt{2s} \sqrt{|X| |Y|}.$$
2. **The Open Mathematical Gap:**
   While EML controls the edge incidence count $e(X, Y)$ between sets of points and lines, it does not directly control the number of 6-tuples of incidences forming physical 6-cycles or cherries satisfying specific GF(5) sign classes.
3. Establishing that:
   $$D6(f, g) + B/A(f, g) + A/B(f, g) \ge c_0 \left(1 - \frac{\sqrt{2s}}{s+1}\right) s^6 > 0$$
   remains an **open conjecture**.
4. Consequently, the refutation of Branch B is **not yet proven**, and Branch B remains formally open.

## 4. Verified Empirical Evidence on Genuine $W(3,2)$

On genuine $W(3,2)$, across 4 canonical global injection schemes:

| Scheme | $D6$ | $B/A$ | $A/B$ | Core Sum ($D6+BA+AB$) | Total $S_{\text{seven}}$ | Mechanism |
|:---|:---:|:---:|:---:|:---:|:---:|:---|
| **lex** | 15 | 98 | 110 | **223** | 259 | Standard alignment |
| **reverse** | 3 | 77 | 74 | **154** | 169 | Reversed orientation |
| **S68** | 0 | 44 | 21 | **65** | 68 | Strict 1-swap local min: $D6=0$, $BA+AB=65$ |
| **S72** | 0 | 36 | 31 | **67** | 72 | Strict 1-swap local min: $D6=0$, $BA+AB=67$ |

- On both strict local minima where $D6 = 0$ ($S68$ and $S72$), the core sum remains $\ge 65 > 0$.
- In these 4 audited configurations, simultaneous annihilation does not occur.

## 5. Complete Proof Stack Synthesis

| Stage | Theorem / Discovery | Outcome |
|:---|:---|:---|
| **AA4-DI** | Point-coverage density barrier $O(s^{-10})$ for minimal 2-external $A$-bridges | Local reservoir route refuted |
| **AA4-DJ** | Universal Finite-Width Barrier ($\rho_m \le m/s^2$); Global Unanchored Carrier ($\tau \ge (1-o(1))s^6$) | Global transversal carrier discovered |
| **AA4-DK** | Girth-8 line-overlap sparsity ($P(R\le 1) \ge 1-O(s^{-2})$) | Sparsity proved; negative covariance refuted by $K_6$ |
| **AA4-DL** | Method of Conditional Expectations derandomization | Constructive $\Omega(s^6)$ witness $g^*$ proved; universal bound open |
| **AA4-DM** | Super-Ramanujan spectrum $\lambda_2 = \sqrt{2s} < 2\sqrt{s}$ with correct multiplicities | Multiplicities certified; compensation law is OPEN CONJECTURE |
| **Resolution** | Derandomized transversal carrier achieves $\Omega(s^6)$; Branch A universal and Branch B counterfamily | **OPEN_WITH_FORMAL_BLOCKER** |
