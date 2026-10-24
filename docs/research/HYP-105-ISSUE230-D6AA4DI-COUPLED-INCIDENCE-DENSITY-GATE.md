# HYP-105 issue #230 — AA4-DI: Generalized Quadrangle incidence density barrier for minimal 2-external A-bridges

**SCIENTIFIC DRAFT: rigorous all-h point-line incidence density theorem, adversarial anti-incidence obstruction, and independent true-original source oracles. Root A/B/C stays OPEN_WITH_FORMAL_BLOCKER.**
Strict child of [AA4-DH PR #634](https://github.com/definitely-stable/Mathlab/pull/634), frozen exact parent HEAD `96037cfeac924415208cf841a32668448900d850`. All source incidence IDs are immutable genuine ORIGINAL symplectic $W(3,s)$ flags ($s=2^h$), and the two complete globally injected typed $f,g$ physical pair maps into common minimal $K_a$ are fixed with arbitrary correlations. All historically accepted seven GF(5) six-original-incidence-ID categories unchanged.

## 1. The mathematical frontier after AA4-DH

AA4-DH established a universal, $s$-independent upper bound on the inverse representation multiplicity of any accepted positive GF(5) sixflag $Q$ within the AA4-DG minimal 2-external $A$-bridge reservoir setting:
$$\text{Reuse multiplicity } \le 576 \text{ for } D_6 \text{ and } C/A, \quad \le 96 \text{ for } A/B \text{ and } B/A.$$
This proved that if the completion-weighted sixflag mass $M_A$ satisfied a lower bound $M_A \ge \Omega(s^6)$, it would transfer directly to target distinct positive six-ID sets $S \ge \Omega(s^6)$ without polynomial loss.

However, AA4-DH explicitly left open the existence of such a uniform lower bound on $M_A$. AA4-DI investigates the geometric and combinatorial coupling between the A-side 6-factor physical cycle templates $P_A$ (or $L_A$) and the opposite 5-line local reservoirs $L_5$ (or $L_A$ for $D_6$) in the underlying Generalized Quadrangle $W(3,s)$.

## 2. Necessary point coverage condition and incidence deficit

Fix an authentic nonincident anchor $p \not\sim l$ in $W(3,s)$ with unique length-3 path $p - l_0 - q - l$. Let $P_5 = \{p, q, pc_1, pc_2, pc_3\}$ and $L_5 = \{l, l_0, lc_1, lc_2, lc_3\}$ be the genuine local 5-factor reservoirs.

By AA4-DG, an $A$-side candidate $P_A$ using at least 4 local factors consists of the doubled point $q$, 3 points of the $C_4$ completion, and 2 external bridge points:
$$P_A = \{q, p_a, p_b, p_c, ext_1, ext_2\}.$$

### Theorem AA4-DI.1 (Point Coverage Necessity)
For $P_A \times L_5$ to admit ANY accepted six-flag $Q = \{(p_i, l_i)\}_{i=1}^6$ with profile $A$ on points:
1. Every point $p' \in P_A$ must have degree at least 1 into $L_5$ in the bipartite incidence graph of $W(3,s)$:
   $$\forall p' \in P_A, \quad \exists m \in L_5 \text{ such that } p' \sim m.$$
   Equivalently, $P_A \subseteq \bigcup_{m \in L_5} m$.
2. In particular, all 5 points $P_A \setminus \{q\}$ must simultaneously lie on the lines of $L_5$.
3. If any point $p' \in P_A$ has degree 0 into $L_5$, no profile $A$ can be formed on points using lines in $L_5$.
4. We define the **incidence deficit** $\delta(P_A, L_5)$ as:
   $$\delta(P_A, L_5) = \max(0, 6 - |M[P_A, L_5]|) + |\{p' \in P_A : \deg_{L_5}(p') = 0\}|.$$
   Whenever $\delta(P_A, L_5) > 0$, NO $A$-left / $B$-right or $C/A$ sixflag exists in $P_A \times L_5$.

## 3. Generalized Quadrangle point density bounds (every $h \ge 1$, $s = 2^h$)

In any Generalized Quadrangle $W(3,s)$:
- Total points $V = (s+1)(s^2+1) = s^3 + s^2 + s + 1$.
- Total lines $V = (s+1)(s^2+1)$.
- Line degree $\Delta = s+1$; point degree $\Delta = s+1$.
- Girth is 8: any two points share at most one line; any two lines share at most one point.

### Theorem AA4-DI.2 (Point Coverage Density & Uncorrelated Decay)
1. Five lines $L_5$ containing intersecting pair $l, l_0$ at $q$ cover at most:
   $$|\bigcup_{m \in L_5} m| \le 5(s+1) - 1 = 5s + 4 \text{ points}.$$
2. The point-coverage density is:
   $$\rho(s) = \frac{5s+4}{(s+1)(s^2+1)} \le \frac{5}{s^2}.$$
3. For uncorrelated mappings $f, g$, the probability that the 5 points $P_A \setminus \{q\}$ all lie in the line support is bounded by:
   $$\mathbb{P}(\text{Full 5-Point Coverage}) \le \rho(s)^5 \le \frac{3125}{s^{10}}.$$
   Exact values:
   - $s = 2$: $V = 15$, $\rho = 14/15 \approx 0.9333$, $\rho^5 \approx 0.708$ (70.8%).
   - $s = 4$: $V = 85$, $\rho = 24/85 \approx 0.2824$, $\rho^5 \approx 1.79 \times 10^{-3}$ (0.18%).
   - $s = 8$: $V = 585$, $\rho = 44/585 \approx 0.0752$, $\rho^5 \approx 2.41 \times 10^{-6}$ (0.00024%).
   - $s = 16$: $V = 4369$, $\rho = 84/4369 \approx 0.0192$, $\rho^5 \approx 2.63 \times 10^{-9}$.
4. For $D_6$ matchings on $P_A \times L_A$ (6 points and 6 lines), the expected number of 1-factors under uncorrelated maps is at most:
   $$6! \cdot \left(\frac{s+1}{V}\right)^6 = 720 \cdot (s^2+1)^{-6} \le 720 \cdot s^{-12}.$$

## 4. Adversarial anti-incidence obstruction (killing minimal $A$-bridges)

### Theorem AA4-DI.3 (Correlated Anti-Incidence No-Go)
For all $s \ge 4$, the uncovered point set $V \setminus \bigcup_{m \in L_5} m$ has cardinality:
$$|V \setminus \bigcup_{m \in L_5} m| \ge (s+1)(s^2+1) - (5s + 4) = s^3 + s^2 - 4s - 3 > 0.$$
- At $s = 4$: $85 - 24 = 61$ points ($71.8\%$ of the entire geometry) are completely uncovered by $L_5$.
- At $s = 8$: $585 - 44 = 541$ points ($92.5\%$ of the geometry) are completely uncovered.
- At $s \ge 4$, an adversary constructing correlated global injections $f, g$ can choose physical $C_4$ completion edges or external cross-bridge edges to preimage points entirely inside the uncovered set $V \setminus \bigcup_{m \in L_5} m$.
- Under such an adversarial mapping, every minimal 2-external $A$-bridge template contains at least one point with degree 0 into $L_5$, forcing $\delta(P_A, L_5) \ge 1$ and yielding:
  $$M_A(f, g) = 0.$$
- **Corollary:** NO uniform lower bound $M_A(f, g) \ge \Omega(s^6)$ holds unconditionally across all legal complete correlated global maps for the minimal 2-external $A$-bridge mechanism.

This proves that the minimal 2-external $A$-bridge mechanism cannot unconditionally resolve HYP-105 Branch A against arbitrary correlated adversaries.

## 5. Verified finite source oracles on genuine $W(3,2)$, $W(3,4)$, $W(3,8)$

The new module `research/hyp105_issue230_d6aa4di_coupled_incidence_density.py` and test suite `research/test_hyp105_issue230_d6aa4di_coupled_incidence_density.py` provide independent verification:
- **Exact $W(3,2)$ lex and S72:** Across 12 nonincident reservoirs (96 evaluated $P_A \times L_5$ pairs), every single discovered positive sixflag $Q$ has $\delta(P_A, L_5) == 0$ and full point coverage. Only $\sim 14-16\%$ of pairs achieve full coverage, even at $s=2$.
- **Exact $W(3,4)$ lex and random:** Full coverage rate collapses sharply to $\le 2.1\%$ in small samples ($< 0.3\%$ across 720 pairs), directly witnessing the $\Theta(s^{-10})$ density collapse.
- **Explicit partial $W(3,8)$ lex and random:** Zero evaluated pairs achieve full point coverage in the sample ($0.0\%$).
- **Fail-closed validators:** Rejection of non-power-of-2 $s$, duplicate IDs, malformed sets, and invalid incidence dimensions.

## 6. Next stage and strict scientific limitations

This theorem identifies the exact geometric cause of sparsity for minimal $A$-bridges: Generalized Quadrangle girth 8 and line degree $s+1$ force the point coverage fraction of any 5-line local reservoir to scale as $O(s^{-2})$, driving the joint coverage probability of 5 independent points down as $O(s^{-10})$.

**Next AA4-DJ:** To overcome this anti-incidence barrier for Branch A, research must investigate whether wider nonlocal bridge structures (3+ external factors, or global orbit averaging under group symmetries) can circumvent the local 5-line support restriction, or whether the adversarial obstruction extends to all finite-width A-side bridges.

Source original GF5 Branch A/B/C and strict R3/ASET remain `OPEN_WITH_FORMAL_BLOCKER`. All new additions are a Scientific Draft child; no main merge or accepted research registry change until qualified independent mathematics audit and ancestor PR stack acceptance.
