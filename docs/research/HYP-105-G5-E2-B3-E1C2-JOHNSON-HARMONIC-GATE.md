# HYP-105 B3.2-E1-C2 — exact Johnson order-two transfer and quantified higher-order obstruction

Date: 2026-10-10. Parent [#230](https://github.com/definitely-stable/Mathlab/issues/230), #176. Stacked on [B1-C1 PR #260](https://github.com/definitely-stable/Mathlab/pull/260) and [B1-C0 PR #249](https://github.com/definitely-stable/Mathlab/pull/249).

**TYPE: RESTRICTED_THEOREM_C / exact all-h algebraic overlap decomposition applicable to the actual GQ m_f, plus W(3,2) complete independent falsifiers. A classical Johnson-scheme / Hoeffding projection of hypergraph intersections; no claim of new worldwide harmonic decomposition. No universal all-g Omega(s^6) proof, no infinite correlated counterexample, no complete R3 upper, no improved ASET exponent.**

## 1. The precise transfer that C2 can and cannot prove

For all s=2^h, h>=1, let V=(s+1)(s²+1), a minimal with K=binom(a,2)>=V. Freeze ANY left physical pair injection f and the GQ-derived original-right weighted six-uniform source m_f(R) from B1-C0/C1. Freeze ANY right physical pair injection g of all V original factor lines into the K labels E(K_a), including arbitrary correlations with f. The overlap

```text
U(f,g) = sum_{R subset L_s, |R|=6} m_f(R) 1[g(R) in T_a]
```

is EXACTLY the accepted B-left/A-right six-incidence motif count, not the seven-family S nor total full-GF5 R3. Both endpoints here are ORIGINAL typed GQ vertices; a right physical pair label is a vertex of the TARGET hypergraph T_a, not an original incidence.

Choose a fixed abstract set of K vertices and inject the V original right vertices into its first V slots. Extend m_f by ZERO to all sixsets not completely in the first V. Every physical right injection g can be extended to a permutation pi of the K abstract vertices by assigning the K-V unused physical pair labels arbitrarily to the K-V padded vertices. The padded m_f makes every such extension give the SAME overlap. Consequently the ordinary Johnson orthogonal decomposition on real functions on binom([K],6) applies **to all legal injections**, not only to bijective W32.

The target indicator t(S)=1[S in T_a] is invariant under physical coordinate renaming S_a but not arbitrary permutations of its K edge-label vertices. It is a one-design, so t has a CONSTANT W0 component and **ZERO W1 component**. This last fact is exact for all a>=6, not a stochastic approximation.

## 2. Exact W2 target projection — only adjacent versus disjoint physical labels

Let N=binom(K,6), T=70 binom(a,6), and define

```text
q_A = 7 binom(a-3,3)    # pair labels share exactly one physical coordinate
q_D = 14 binom(a-4,2)   # pair labels have disjoint physical coordinates
A   = K(a-2)            # number of adjacent unordered label pairs in E(K_a)
Q   = binom(K,2)        # number of all unordered label pairs
u   = A/Q
q_bar = 15 T / Q
lambda_2 = binom(K-4,4)
```

The B1-C0 target design identities imply q_bar = u*q_A+(1-u)*q_D, and for each physical label x the centered pair-codegrees sum to ZERO over y != x. For the inclusion operator I_2 (sixsets to pairs), the Johnson W2 row-sum-zero eigenvalue is

```text
I_2 I_2^T r = lambda_2 r,     if sum_{y != x} r(x,y) = 0 for each x.
```

Proof by elementary counting: in (I_2 I_2^T r)(x,y), the pair (x,y) itself occurs in binom(K-2,4) sixsets, pairs sharing exactly one of x,y occur in binom(K-3,3), and disjoint pairs occur in binom(K-4,2). Row-sum-zero implies the sum over pairs sharing one is -2r(x,y) and the sum over disjoint pairs is +r(x,y). Hence the eigenvalue is binom(K-2,4)-2binom(K-3,3)+binom(K-4,2)=binom(K-4,4).

Therefore the exact target W2 projection evaluated at any physical label sixset S is

```text
t_2(S) = (1/lambda_2) sum_{{x,y} subset S} (q_T(x,y)-q_bar),
where q_T(x,y) = q_A if x,y adjacent in K_a, else q_D.
```

For an original right source m_f, let M=sum_R m_f(R), and let

```text
B_g(m_f) = sum_{i<j in original right vertices}
           [sum_{R superset {i,j}}m_f(R)] * 1[g(i) cap g(j) nonempty].
```

Here **physical adjacency in g** is compared against original-source TWO-point weights; it is NOT presumed to agree with original GQ line concurrency c_GQ(i,j). Direct contraction with t_2 yields an exact fixed-g identity:

```text
U(f,g) = mu(f) + U2(f,g) + U_ge3(f,g),

mu(f) = M*T/N,               (uniform independent right expectation),
U2(f,g) = (q_A-q_D)/lambda_2 *
            (B_g(m_f) - 15*M*u).
```

The first moment is **not** asserted as an all-g lower. The third term is an exact orthogonal W>=3 contraction; it cannot be dropped and its sign is uncontrolled. The identity is a model-equivalent transfer decomposition for the B/A overlap alone, with no probability assumptions on f,g.

**Special case a=9:** q_A=q_D=140, so the entire target W2 component vanishes for EVERY source and EVERY injection g. This is an exact 2-design property already proved in C0. Note a=9 is not a minimal alphabet arising from W(3,2^h), so this is a mathematical stress test, not an admissible all-h asymptotic shortcut.

## 3. Quantify the residual — exact squared Johnson energies and a valid (possibly vacuous) sufficient condition

For any weighted source m on the zero-padded sixsets of [K], let d_i=sum_{R contains i} m(R), and d_ij=sum_{R contains i,j}m(R), where M=sum m, N=binom(K,6).

```text
m0(R) = M/N.
beta_i = (d_i - 6M/K) / binom(K-2,5).
m1(R) = sum_{i in R} beta_i,     sum_i beta_i = 0.

r_ij = d_ij - binom(K-2,4)*(M/N)
            - binom(K-3,4)*(beta_i+beta_j).
sum_{j!=i}r_ij = 0.
m2(R) = sum_{{i,j} subset R} r_ij / binom(K-4,4).
```

These W0/W1/W2 parts are orthogonal for the uniform sixsubset inner product. Exactly,

```text
||m0||² = M²/N
||m1||² = sum_i (d_i-6M/K)² / binom(K-2,5)
||m2||² = sum_{i<j} r_ij² / binom(K-4,4)
||m>=3||² = sum_R m(R)² - ||m0||²-||m1||²-||m2||² >=0.
```

For target t, t1=0 and

```text
||t0||² = T²/N
||t2||² = [A(q_A-q_bar)² + (Q-A)(q_D-q_bar)²] / lambda_2
||t>=3||² = T - T²/N - ||t2||².
```

For **all injections g**, by orthogonality, permutation invariance, and Cauchy–Schwarz,

```text
|U2(f,g)| <= sqrt(||m2||² * ||t2||²)
|U>=3(f,g)| <= sqrt(||m>=3||² * ||t>=3||²)

U(f,g) >= M*T/N
          -sqrt(||m2||² * ||t2||²)
          -sqrt(||m>=3||² * ||t>=3||²).
```

This is a rigorously correct, computable, **SUFFICIENT** positive-overlap gate for each fixed f if the right side is positive; the test harness also uses a conservative sufficient rational-only check mu²>4max(B2,B>=3), without relying on float approximations. It is NOT a necessary condition, not an equivalence to the all-seven-family #230 problem, and may be numerically vacuous. If it is vacuous on W32, that does not disprove the desired global lower bound.

At **a=6**, K=15, N=5005, T=70, lambda2=330, q_A=7, q_D=14, q_bar=10, A=60, Q-A=45. Therefore:

```text
||t2||² = [60*(7-10)²+45*(14-10)²]/330 = 42/11.
||t>=3||² = 9324/143.
```

The fraction of CENTERED target squared energy residing in W2 is exactly

```text
(42/11)/(70-70²/5005) = 13/235  (~5.5319%).
```

Thus more than **94% of centered T6 squared energy** is in W>=3. A degree-two-only bound cannot recover this component by orthogonal projection. Importantly, this does NOT imply higher correlations produce a lower bound or prevent one: it rigorously quantifies the missing part.


## 3A. Stronger exact all-a W3 transfer: five physical target orbits (additional C2 closure)

The accepted B1-C0 three-edge physical target codegree theorem can be orthogonally projected exactly, rather than left in U_ge3. Let I_3 be incidence of a triple of abstract K physical pair labels in a sixset. The harmonic W3 eigenvalue is

```text
lambda_3 = binom(K-6,3).
```

On a triple tensor r with all pair-lower sums zero (sum_{z not in {x,y}} r(x,y,z)=0 for every x≠y), the standard Johnson I_3 I_3^T eigenvalue is lambda_3. This follows from inclusion and exclusion of overlaps 3,2,1,0 and the binomial identity; it is classical Johnson-scheme algebra. The executable oracle independently checks that the projected target has zero W0/W1/W2 pair marginals.

For the physical target, enumerate the five orbit classes of three different *pair-edge labels*. Their within-triple physical-adjacent label-pair counts are respectively 3,2,3,1,0 for triangle, P4, claw, P3 plus disjoint edge, matching3. The target triple codegrees are exactly the B1-C0 proven values C(a-3,3), 2C(a-4,2), 0, 5(a-5), 8. With qbar, qA/qD and lambda2 from section 2, set for each physical label triple H:

```text
c2(H) = sum_{{i,j} subset H}(q_T(i,j)-qbar)/lambda_2
r_T3(H) = codeg_T(H) - binom(K-3,3)*T/N
           - binom(K-5,3)*c2(H)
t3(S) = sum_{H subset S, |H|=3} r_T3(H)/lambda_3.
```

Target W1=0, so there is no missing W1 subtraction. The K_a physical coordinate orbits have exact cardinalities C(a,3), 12C(a,4), 4C(a,4), 30C(a,5), 15C(a,6); each gives a constant r_T3(H). Their complete sum of squared residuals gives

```text
||t3||² = (1/lambda_3) sum_{H, |H|=3} r_T3(H)²,
||t>=4||² = T - T²/N - ||t2||² - ||t3||².
```

For a zero-padded source m, define original right three-line marginal d_ijk, W1 beta and W2 pair residual gamma_ij=r_ij/lambda2 as in section 3. The exact source W3 triple residual is

```text
r_m3(i,j,k)
  = d_ijk - binom(K-3,3)*(M/N)
          - binom(K-4,3)*(beta_i+beta_j+beta_k)
          - binom(K-5,3)*(gamma_ij+gamma_ik+gamma_jk).

||m3||² = sum_{i<j<k} r_m3(i,j,k)²/lambda_3
||m>=4||² = ||m>=3||² - ||m3||².
```

For EVERY correlated legal physical right injection g, independently of the left f, the all-h identity now refines to

```text
U(f,g) = mu(f) + U2(f,g) + U3(f,g) + U>=4(f,g),

U3(f,g) = sum_{{i,j,k} original right triple}
             d_ijk(m_f)*r_T3(g(i),g(j),g(k))/lambda_3.
```

This is precisely the missing **joint original-source third marginal × physical-target five-orbit contraction**. Its numerical value can change arbitrarily under g; the original GQ triple-concurrence 0/1/2/3 class of {i,j,k} does not determine the physical target five-orbit class of {g(i),g(j),g(k)}. The all-g estimate remains open until those couplings or higher harmonics are constrained GQ-specifically.

Exactly,

```text
|U3(f,g)| <= sqrt(||m3||²*||t3||²)
|U>=4(f,g)| <= sqrt(||m>=4||²*||t>=4||²).
```

The corresponding global sufficient positive-overlap certificate uses mu>sqrt(B2)+sqrt(B3)+sqrt(B>=4). The implementation tests the conservative rational-only sufficient condition mu²>9 max(B2,B3,B>=4), not a necessary condition.

For K6, the **complete exact numbers** are

```text
lambda_3 = 84,
||t2||² = 42/11,
||t3||² = 710/1001,
||t>=4||² = 4966/77.
```

Thus the W>=4 contribution alone is exactly **32279/34545 (~93.44%)** of target CENTERED squared energy. The full W>=3 94.47% statement above stays true; the third-order projection accounts for only ~1.03% of centered target energy. This **does not** prove that U>=4 is positive or negative for any adversarial g, nor a global all-label risk power.

Additional independent tests compute all 455 K6 physical triple marginal values from the brute 70-target enumeration, reconstruct t3 over all 5005 sixsets, confirm its 5 orbit residuals and exact 710/1001 norm, and check orthogonality to every pair indicator. The original W32 source W3 residual and W>=4 norms are independently reconstructed over all 5005 right sixsets. All 105 real right factor swaps retain the cheaper exact W0+W2+W>=3 check; four specially selected W32 permutations additionally validate the full W0+W2+W3+W>=4 identity.

**Scientific status unchanged:** RESTRICTED_THEOREM_C (exact structural transfer), #230 Branch A/B unresolved. Any claim that this proves all-h Omega(s6) is prohibited.

## 4. Why both physical and GQ structure are indispensable

C1 constrains source weights via the ORIGINAL right concurrence graph: m_f(R)<=c_GQ(R)(s+1)^4, with support restricted to sextets with concurrent original lines. C2 exactly characterizes the order-two part of their interaction with the physical target under g. However the pair-adjacency weight B_g above depends on **g**, which can arbitrarily change the physical adjacency relation among images of original factor lines. Replacing physical adjacency in B_g with c_GQ(i,j) is FALSE in general. Even controlling B_g would not control the W>=3 remainder.

The C0 three-cube trade provides an independent exact boundary: two abstract nonnegative six-uniform source weights with all order<=2 marginals identical have identical mu and U2 for a fixed g, but intersection differs by one. This is a generic hypergraph countermodel, not a genuine W(3,s) source. C1's GQ-specific spread excludes that toy as a *complete* source model for large s, but has not proved an inequality ruling out its high-order cancellation mechanisms inside a genuine GQ incidence source.

Prior art: the Johnson association scheme, Efron–Stein/Hoeffding projections of uniform fixed-size subsets, and Bollobás–Scott *Intersections of hypergraphs* (JCTB 2015, DOI 10.1016/j.jctb.2014.08.002), whose W-component framework already studies weighted hypergraph overlap. The projection, eigenvalues, and Cauchy step are **classical calculations**, not a new general discrepancy theorem. The deliverable is their precise GQ-source/physical-target interface, full exact constants, and independently falsifiable applicability restrictions.

## 5. Independent acceptance and branch status

[Reference implementation](../../research/hyp105_g5e2b3e1c2_johnson_gate.py) computes the all-a target two-orbit Johnson energies symbolically, source W0/W1/W2/W>=3 norms by sparse sixsets, actual fixed-injection U2 and U>=3 with exact rational values, and independent Cauchy checks. Original source comes from frozen B1-C0 without rewriting its m_f enumeration.

[Independent tests](../../research/test_hyp105_g5e2b3e1c2_johnson_gate.py) include two non-circular methods:
1. Independently enumerate ALL 5005 K6 six-edge sets; derive the 70 target hyperedges, their 105 physical edge-label pair codegrees, evaluate target W2 over all 5005 sixsets, and check its norm and orthogonality to W0/W1 without using the analytic target formula.
2. Independently reconstruct actual W32 source W0/W1/W2/W>=3 vectors over all 5005 original right sixsets and their squared norms, then exhaust all **105 original right-factor transpositions** of one fixed genuine GQ model. For every transposition, compare full original source target overlap via an independent K6 target enumeration against the exact U0+U2+U>=3 decomposition. Include the previously pinned swap (4,13) with exact 77->57 B/A count.
3. Check the 3-cube same-0/1/2-margin no-go (overlap 0 versus 1) and the non-surjective 15-to-36 alphabet injection at a=9; reject malformed original source weights and physical maps.

No new mathematical acceptance until **exact-head GitHub-hosted Research SUCCESS**, plus acceptance of upstream #249/#260 and postmerge main Research SUCCESS. Source, target, arbitrary g, all original incidences, and full-GF5 palette scope fences remain immutable.

**Decision:** RESTRICTED_THEOREM_C for the exact degree-two transfer, but #230 is **OPEN_WITH_FORMAL_BLOCKER** for Branch A/B. The physical target has a rigorously large order>=3 remainder; C3 must seek GQ-specific inequalities controlling this remainder or a certified infinite all-seven-family correlated labeling family. Neither "random mean positive" nor "W2 small" solves #230.
