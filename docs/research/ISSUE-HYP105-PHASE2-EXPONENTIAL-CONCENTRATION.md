## Phase 2: Mathematical Hardening: Negative Association Concentration & Cheeger Isoperimetric Infimum

Parent #230. Follows Phase 1 consolidation.

### 1. Objective
Strengthen the probabilistic and spectral bounds of Hypothesis 105 from polynomial Чебышёв concentration to exponential tails via Negative Cylinder Dependence (Dubhashi–Ranjan), and derive an exact closed-form analytical lower bound for the universal infimum $\inf_{f, g} S(f, g)$ via the bipartite Cheeger isoperimetric constant $h(\mathcal{G})$.

### 2. Key Mathematical Targets
1. **Negative Association Concentration Engine:**
   - Establish that the family of 6-flag indicators $\{\mathbf{1}_Q\}$ under uniform permutation orbit $\operatorname{Orb}(E)$ satisfies negative cylinder dependence.
   - Prove the subexponential Chernoff-type concentration bound:
     $$\mathbb{P}_{g'} \left(S(f, g') < (1 - \epsilon)\mathbb{E}[S]\right) \le \exp\left( -\Omega(\epsilon^2 s^6) \right).$$
2. **Analytical Cheeger Infimum Formula:**
   - Compute the exact bipartite Cheeger constant $h(\mathcal{G}) = \frac{d - \lambda_2}{2d} = \frac{s + 1 - \sqrt{2s}}{2(s + 1)}$.
   - Prove that for all globally injected pairs $(f, g)$, without orbital averaging:
     $$S(f, g) \ge \left( \frac{455}{3} \cdot h(\mathcal{G})^2 - o(1) \right) s^6 \approx \left( 37.91 - O(s^{-1/2}) \right) s^6.$$
3. **Finite Verification on $W(3,2)$ and $W(3,4)$:**
   - Validate the Cheeger floor against empirical minima (68 on $W(3,2)$).

### 3. Deliverables
- `research/hyp105_exponential_concentration.py`
- `research/test_hyp105_exponential_concentration.py`
- `docs/research/HYP-105-EXPONENTIAL-CONCENTRATION-CHEEGER.md`
- `.github/workflows/hyp105-exponential-concentration.yml`
