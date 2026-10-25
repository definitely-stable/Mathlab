## Phase 1: Proof Consolidation & Canonical Core Refactoring

Parent #230. Follows completed research stages AA4-DI through AA4-DM.

### 1. Objective
Consolidate the full formal proof of Hypothesis 105 (Issue #230) into a single canonical, minimal, self-contained architecture. Eliminate historical technical debt and dead abstractions accumulated during earlier explorations of local reservoirs.

### 2. Detailed Deliverables
1. **PR Governance & Merge Preparation:**
   - Submit and verify PR chain for branches:
     - `research/hyp105-issue230-aa4di-coupled-incidence-density-gate`
     - `research/hyp105-issue230-aa4dj-universal-width-barrier`
     - `research/hyp105-issue230-aa4dk-sparse-covariance-decoupling`
     - `research/hyp105-issue230-aa4dl-deterministic-orbit-derandomization`
     - `research/hyp105-issue230-aa4dm-ramanujan-expansion-annihilation-barrier`
2. **Dead Abstraction Elimination (Ponytail Refactoring):**
   - Archive obsolete local-reservoir modules (AA4-AA through AA4-DH) into `research/archive/hyp105_local_bridges/`.
   - Preserve scientific record while unburdening the active critical path.
3. **Canonical 3-Lemma Architecture (`research/hyp105_canonical_core.py`):**
   - **Lemma 1 (Global Transversal Carrier):** For every physical $C_6$ in $K_a$, $\tau(P_6) \ge (1 - O(s^{-2})) s^6$.
   - **Lemma 2 (Girth-8 Sparsity & Negative Disjoint Covariance):** $P(R \le 1) \ge 1 - O(s^{-2})$ and $\operatorname{Cov}_0 < 0$, damping variance to $\operatorname{Var}(S)/\mu^2 \le O(s^{-1})$.
   - **Lemma 3 (Super-Ramanujan Spectrum & Simultaneous Annihilation Barrier):** $\lambda_2 = \sqrt{2s} < 2\sqrt{s}$ forbids simultaneous vanishing of cycles and cherries: $D6 + BA + AB \ge \Omega(s^6)$.
4. **Fast Unit Test Suite (`research/test_hyp105_canonical_core.py`):**
   - Independent verification running in $< 0.1\text{s}$.
5. **Comprehensive Documentation & CI:**
   - `docs/research/HYP-105-CANONICAL-CORE-PROOF.md`
   - `.github/workflows/hyp105-canonical-core.yml`

### 3. Review & Quality Gates
- Every step reviewed and audited by dedicated research subagents.
- 100% test pass rate with fail-closed validation.
