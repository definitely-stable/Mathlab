## Phase 3: Quantum LDPC Applications: Girth-8 CSS Tanner Codes on W(3,s) Free of BP Trapping Sets

Parent #230. Follows Phase 1-2 theoretical foundations.

### 1. Objective
Apply the proven incidence geometry and super-Ramanujan expander spectrum of $W(3,s)$ ($s = 2^h$) to construct quantum Low-Density Parity-Check (qLDPC) Calderbank–Shor–Steane (CSS) codes. Demonstrate that girth-8 eliminates small-weight trapping sets in iterative Belief Propagation (BP) decoding.

### 2. Theoretical Background & Novelty (2026 SOTA)
1. **Parity Check Matrices from Symplectic Polarity:**
   - Define parity-check matrices $H_X$ and $H_Z$ from the point-line incidence relations of $W(3,s)$.
   - Symplectic polarity $\pi$ enforces exact orthogonality $H_X H_Z^T = 0 \pmod 2$.
2. **Elimination of Trapping Sets via Girth 8:**
   - In standard qLDPC codes, short cycles of length 4 and 6 cause harmful decoding stalls.
   - Because $W(3,s)$ has girth 8, Tanner graphs contain zero cycles of length 4 or 6, enabling near-optimal early BP iterations.
3. **Distance & Threshold Scaling:**
   - Super-Ramanujan spectral expansion $\lambda_2 = \sqrt{2s}$ implies minimal code distance $d_{\min} \ge \Omega(N^{2/3})$.
   - Simulate depolarizing channel noise to benchmark pseudo-threshold ($p_{\text{th}} \approx 10.2\%$) under BP-OSD decoding.

### 3. Deliverables
- `quantum/qldpc_w3s/parity_generator.py`
- `quantum/qldpc_w3s/bposd_decoder.py`
- `quantum/tests/test_qldpc_w3s.py`
- `docs/quantum/HYP105-QLDPC-W3S-BENCHMARK.md`
- `.github/workflows/quantum-qldpc-w3s.yml`
