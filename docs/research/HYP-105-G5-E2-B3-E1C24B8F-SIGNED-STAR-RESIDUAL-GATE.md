# HYP-105 C24-B8-F — signed-star QAP, rational dual lower and pointwise residual gate

Root [#230](https://github.com/definitely-stable/Mathlab/issues/230), stacked on [B8-E PR #361](https://github.com/definitely-stable/Mathlab/pull/361), pinned parent HEAD `1f6e020f172011d0c4fdd1808a511ea91d8d18f3`. Classification: **RESTRICTED_THEOREM_C_FINITE_FULL_BIJECTION_SIGNED_STAR_RELAXATION**. Draft only; no main changes, no merge authorization, and no proof of Branch A, Branch B, full R3 or a new ASET exponent. Only GitHub-hosted runners.

## 1. Why B8-E requires a global pointwise gate

B8-E gives the optimal *mean-square linear pair projection* `S(f,g)=mu_f+P_2(f,g)+R(f,g)`. At genuine W32 `S(f0,g68)=68`, `mu_f=870476/5005`, `P_2=-6875243/60060`, `R=73373/8580`. The nonzero residual proves *non-affine dependence on pair adjacency indicators*, not statistical independence or information missing from the complete pair graph. Its sign at one g is NOT a lower bound on R over all g.

We now bound the minimum of the **linear component** over an entire coherent global bijection, **independently of the nonlinear component**. This is a restricted finite theorem; the W(3,s) hosts for larger s typically have `n<m`, where this full-bijection reduction does not apply without modification.

## 2. Exact physical star / quadratic assignment identity

For `a>=4` put `m=C(a,2)`, `n=m`. Let `I_ij` be ANY rational symmetric zero-diagonal matrix satisfying the exact B8-D full-bijection condition `sum_{j!=i} I_ij=0` for every i. For any complete global bijection `g:[m]->E(K_a)`, let

```
T_u(g) = {i : u is an endpoint of g(i)},   u=0,...,a-1,
W(T)    = sum_{i<j in T} I_ij,
T(g)    = sum_u W(T_u(g)).
```

All `T_u` have size `a-1`; every original right line is in **exactly two** stars; and `|T_u cap T_v|=1` for every two distinct physical vertices u,v. Since any two distinct K_a physical edges share at most one endpoint,

```
T(g)=sum_{i<j} I_ij * 1{g(i) intersects g(j)}.
```

The same incidence design gives the Johnson projection coefficient `v/lambda2=(m-3)/(m-1)` for the full host. Because `sum_{i<j} I_ij=0`, centering drops out and

```
P_2(g) = (m-3)/(m-1) * T(g).
W32: P_2(g) = 6/7 * sum_{u=0}^5 W(T_u(g)).
```

Thus the linear problem is one *quadratic assignment on a globally coherent bijection*, not 105 independent binary events. Every entire assignment is counted once with global consistency. The physical coordinate permutation group `Sym(a)` acts on the stars; it does NOT make them independent.

## 3. Exact rational lower bound using a star-subset dual

Enumerate all `C(m,a-1)` *possible individual* original-line subsets of size `a-1` (for W32 only `C(15,5)=3003`), with exact rational cost W(U). Every true g chooses exactly a such subsets, with each original label appearing precisely twice. For arbitrary rational `y_0,...,y_{m-1}` set

```
q(y) = min_{U subset [m], |U|=a-1}
       [ W(U) - sum_{i in U} y_i ],
L(y) = 2 sum_i y_i + a q(y).
```

**Certified inequality for every legal global g:**

```
T(g) = sum_u (W(T_u)-sum_{i in T_u} y_i) + 2 sum_i y_i
     >= L(y).
P_2(g) >= ((m-3)/(m-1))*L(y).
```

The finite minimum defining `q(y)` is **exhaustively checked** over all individual star subsets, not over full `m!` labelings. This relaxation drops the *pairwise one-point star-overlap* condition, so `L(y)` may be strictly below the real `min_g T(g)`. It cannot become an upper bound or exact optimizer by assertion.

To improve a rational dual without an external LP solver, update one coordinate at a time. With all other coordinates fixed let `q_in` and `q_out` be minima over stars containing or excluding i, after removing the current i-price from inside costs. Then as a function of `y_i=t`,

```
L(t) = 2t + constant + a min(q_in-t,q_out).
```

For `a>2` the exact one-coordinate maximizer is `t=q_in-q_out`. Several deterministic sweeps monotonically improve the lower certificate. **No global dual LP optimality is asserted.** The final bound is re-evaluated directly from all raw star costs and final dual prices, with no floating-point or solver status.

## 4. Residual gate: what remains to prove

Let `L_P(f)` be a proved global lower bound on P for ONE fixed f, such as `(6/7)L(y)` at W32. Then for ANY uniform-in-g *independently proved* bound `R(f,g)>=r_f`, all g satisfy

```
S(f,g) >= mu_f + L_P(f) + r_f.
```

A sufficient condition to prove a strictly positive floor for this *fixed* f is

```
r_f > -mu_f - L_P(f).
```

The module reports the **required threshold**, not an assumed residual bound. The observed `R(f0,g68)=73373/8580` is not valid for `r_f`. An L2 orthogonality statement likewise cannot be plugged into the pointwise gate. The trivial `S>=0` does not produce a useful strictly positive score conclusion from this decomposition.

A universal `Omega(s^6)` Branch-A theorem would require (i) an all-h lower bound `mu_s(f)`, (ii) a uniformly valid partial-host pair-assignment lower bound `L_{P,s}(f)` for **every f**, and (iii) a pointwise residual lower bound `r_s(f)`, with their sum `>=c s^6` uniformly across f, s. B8-F proves **none** of these three universal requirements.

## 5. Independent falsification and hosted evidence

- `research/hyp105_g5e2b3e1c24b8f_signed_star_gate.py`: exact full-host global-star identity; 3003-subset signed lower dual; monotone rational coordinate improvement; conditional residual threshold. Fails closed for nonzero rows, missing pair weights, non-bijections, nonrational input, unsupported oversized hosts.
- `research/test_hyp105_g5e2b3e1c24b8f_signed_star_gate.py`: **all 6!=720 K4 global physical-edge bijections** for a nontrivial signed zero-row matrix, with independently computed pair cost, true finite minimum vs certified lower; independent genuine K6 combinatorial incidence identities, physical-coordinate relabeling and zero-matrix controls.
- `research/hyp105_g5e2b3e1c24b8f_w32_signed_star_witness.py`: original W(3,2) f0/g68; B8-D exact 105-influence matrix; B8-E exact projected variance; independent original RIGHT-FIRST 62370-sixset score 68; algebraically independent star/Johnson pair contractions; full rational dual re-evaluation; one observed nonlinear residual and exact unproved-threshold report.
- `.github/workflows/hyp105-c24b8f-signed-star-residual-gate.yml`: isolated GitHub-hosted dedicated Contract; full inherited Research and INDEX remain unchanged. No full 15! search, 11236-cell sweep or new noisy CI workflow changes.

**Acceptance:** same exact final B8-F HEAD must have Dedicated Contract SUCCESS, all six inherited Full Research jobs plus fail-closed aggregate SUCCESS, and INDEX SUCCESS. Parent B8-E must separately be accepted at its own pinned HEAD. No results from older commits satisfy this gate. PR remains Draft and root issue #230 OPEN_WITH_FORMAL_BLOCKER.

## 6. Next research fork if dual lower is too loose

Inspect the **certified gap** `T(g68)-L(y)` from the hosted log, not assumed numerical values. If large, add progressively stronger *pairwise star overlap and two-incidence degree constraints*, e.g. an exact finite matching/packing relaxation with auditable dual. Independently, derive a signed all-g lower for the genuine **nonlinear** residual using original six-incidence fibers, not local-swap extrapolation. For n<m develop a host-slack-aware assignment model with unoccupied physical edges before extrapolating the W32 full-host algebra to all h.
