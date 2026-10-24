## Phase 4: Formal Verification: Machine-Checked W(3,q) Ramanujan Geometry in Lean 4 / Mathlib4

Parent #230. Follows complete Python/Research validation.

### 1. Objective
Achieve computer-verified formalization of the core mathematical foundations of generalized quadrangle $W(3,s)$ geometry, its super-Ramanujan incidence spectrum, and the simultaneous annihilation barrier using Lean 4 and Mathlib4.

### 2. Formalization Scope
1. **Geometric Definitions in Lean 4:**
   - Formal definition of Symplectic Generalized Quadrangle $W(3, q)$ over $\mathbb{F}_q$.
   - Definition of points, lines, and symplectic bilinear form $\langle u, v \rangle = u_0 v_3 + u_1 v_2 + u_2 v_1 + u_3 v_0$.
   - Theorem proving girth is exactly 8 (no triangles, no quadrilaterals).
2. **Spectral Graph Theory in Mathlib4:**
   - Adjacency operator of the bipartite point-line incidence graph.
   - Machine-checked proof that $\lambda_2 = \sqrt{2s} < 2\sqrt{s}$ (super-Ramanujan bound).
3. **Formalization of the Annihilation Barrier:**
   - Formal statement and proof that the fiber of non-zero motif witnesses is non-empty for all valid injective factor embeddings.

### 3. Deliverables
- `lean/Hyp105/Basic.lean`
- `lean/Hyp105/SymplecticGQ.lean`
- `lean/Hyp105/RamanujanSpectrum.lean`
- `lean/Hyp105/AnnihilationBarrier.lean`
- `lakefile.lean` with CI verification (`lake build`).
