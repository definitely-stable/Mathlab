# HYP-105 C24-B8-G — all-h minimal-host slack, exact physical adjacency counts and rational pair lower

Research root [#230](https://github.com/definitely-stable/Mathlab/issues/230); stacked on [B8-F PR #362](https://github.com/definitely-stable/Mathlab/pull/362) at exact parent HEAD `3489d26affa80bdb73abc131b19317a05ed2b98c`. **RESTRICTED_THEOREM_C_ALL_h_PAIR_CAPACITY_LINF**: true for every h at the physical pair-projection level and every fixed original left f, but NOT an Omega(s^6) seven-motif lower, coherent infinite low-S family, full GF(5) R3 or ASET exponent. Draft only; no main edit, no merge, hosted CI only.

## 1. Correct n<m setup

For the original GQ W(3,s), s=2^h, h>=1, let `n=(s+1)(s^2+1)` original right lines, `a=min{k:C(k,2)>=n}`, `m=C(a,2)`, `q=m-n`. Minimality means `0<=q<=a-2`. Put `d=2(a-2)`. Under ONE whole injective right map `g:[n]->E(K_a)`, define physical adjacency indicators `Z_ij=1{g(i) intersects g(j)}`, with `p=4/(a+1)`.

B8-E supplies the EXACT Johnson-covariance pseudoinverse coefficients `gamma_ij` for the fixed-left true seven-score: `P_2(f,g)=sum_{i<j}gamma_ij(Z_ij-p)`. These are coefficients of one deterministic linear function on full injections, **not independent Bernoulli probabilities**. Unlike the W32 full-bijection case, for `n<m` neither the rows of gamma nor `sum gamma` are forced to vanish.

## 2. All-h sharp host-degree and adjacency cardinality identities

Write `H=L(K_a)`, the physical line graph. It has m vertices, is d-regular and has `m(a-2)` edges. The image of the injection induces `H[occupied]`; the complement consists of q **unused physical host edges** D.

Every occupied host edge loses at most q of its d neighbors. Its occupied degree `k_i(g)=sum_{j!=i}Z_ij` therefore obeys

```
ell = max(0,d-q) <= k_i(g) <= min(d,n-1)=u.
```

Writing `A(g)=sum_{i<j} Z_ij` and `c(D)=sum_{u=0}^{a-1} C(deg_D(u),2)` (adjacent pairs inside the graph formed by the unused K_a edges), deletion gives an exact identity:

```
A(g) = m(a-2)-d*q+c(D).
```

For the MINIMAL-host range `0<=q<=a-2`, the **sharp attainable extrema** are

```
max(0,2q-a) <= c(D) <= C(q,2).
A_min = m(a-2)-2(a-2)q + max(0,2q-a)
A_max = m(a-2)-2(a-2)q + C(q,2).
```

*Proof of lower*: c(D)>=0. Also `C(r,2)>=r-1` for r>=1; summing degrees over at most a nonisolated physical vertices gives `c(D)>=2q-a`. For `2q<=a`, select a q-edge physical matching to attain zero. For `2q>a`, partition a physical vertices into `a-q` disjoint paths of at least two vertices each; possible because `q<=a-2` and `2(a-q)<=a`. There are exactly q physical edges and `2q-a` internal path vertices, each contributing one adjacent pair, attaining the lower bound. The upper bound c(D)<=C(q,2) is trivial; a star on q edges (possible since q<=a-2) attains it. Therefore the A_min/A_max extrema are genuinely reachable by some whole injections, not just relaxation artifacts. QED.

These cardinality extrema alone do NOT characterize which original pair-pattern matrices Z are simultaneously realizable.

## 3. Rational row-capacity certificate for arbitrary gamma

For each original line i, sort its n-1 rational coefficients `gamma_ij` in increasing order; let `F_i(k)` be the sum of the smallest k (with F_i(0)=0). Since each realized degree k_i lies in [ell,u],

```
sum_{j!=i}(gamma_ij-t) Z_ij >=
   min_{ell<=k<=u} [F_i(k)-t*k]
```

for ANY rational `t`: shifting by a common t preserves sorting. Since each physical pair is counted by exactly two rows and `sum_{i<j} Z_ij=A(g)`, a globally valid all-h lower is

```
L(t) = 1/2 sum_i min_{ell<=k<=u}[F_i(k)-t*k]
     + { t*A_min if t>=0 else t*A_max }
     - p*sum_{i<j}gamma_ij.

             P_2(f,g) >= L(t)    FOR EVERY LEGAL g.
```

This is a pointwise **linear pair-projection** theorem for any rational gamma. In particular inserting the exact B8-E gamma yields a valid true-seven-score projected-component bound. It does NOT require a distribution over g or pair independence. The trivial `t=0` is always permitted.

### Exact one-dimensional relaxation dual

The function L(t) is concave piecewise linear: a minimum of finitely many affine functions per row, plus the appropriate piecewise cardinality term. The only possible finite maximizing breakpoints are 0 and rational intersections

```
t=(F_i(k)-F_i(l))/(k-l),  ell<=k<l<=u.
```

As t approaches the right/left infinities, the slopes are respectively `A_min-n*u/2<=0` and `A_max-n*ell/2>=0`. Therefore the maximum of **THIS** one-dimensional relaxation is attained at a listed breakpoint or 0. Enumerating all of these is exact finite rational optimization of the **relaxation only**, NOT exact quadratic assignment or the original S minimum.

The number of candidate intersections is at most `n*C(u-ell+1,2)+1`; for large hosts the implementation explicitly caps exhaustive candidate enumeration, returns a smaller-but-still-valid certificate from 0 and extreme coefficients, and marks it **nonoptimal in the one-dimensional relaxation**. The size cap affects sharpness, never mathematical validity. Producing gamma itself may be expensive for very large h; this result does not assert a practical all-h GQ source-census runtime.

## 4. True W32 and independent n<m falsification

- **Real W32:** compile original left f0 and all seven GQ six-motif families with multiplicities and D6 positional signatures; independently recompute right-first original score `S(f0,g68)=68`. Obtain exact B8-D influence tensor and exact B8-E gamma, verify `P_2(g68)=-6875243/60060` by two implementations. Compare the new row bound to true g68 and separately to B8-F's star lower `-558274/3003`; the row bound is permitted to be weaker. The finite observed `R(g68)=73373/8580` is **not** an all-g floor.
- **Physical n<m host s=4 parameters:** `n=85`, minimal `a=14`, `m=91`, `q=6`, `d=24`, degrees 18..24 and *sharp* occupied total adjacency count 948..963. Test an EXACT synthetic centered `Z_01-4/15` score: B8-E covariance/pseudoinverse must reconstruct coefficient gamma_01=1 and every other gamma=0; then the row lower equals the true minimum `-4/15`. This is NOT a real W(3,4) original seven-family count, and its success proves no lower on that genuine S.
- **Independent brute physical falsifiers:** enumerate every `6P4=360`, `6P5=720`, `6P6=720` K4 whole injection and compare true pair scores to the rational certificate for nontrivial signed coefficients; enumerate **all deleted-edge subsets** q=0..a-2 for K4,K5,K6 and independently reconstruct exact physical adjacency minima/maxima; constant +1 and -1 weighted pair scores recover the exact total-adjacency extrema. Invalid schema and capped-candidate cases must fail or label limitations correctly.

## 5. Root-issue proof obligations left open

Even if `L_P(f)` were optimized exactly, the equation `S(f,g)=mu_f+P_2(f,g)+R(f,g)` cannot supply positive S without an **all-g pointwise** residual lower or a direct JOINT pair-plus-residual lower. A single observed R68 and L2 orthogonality cannot bound the global residual infimum. The B8-F separated-gate impossibility test remains explicit: with its current star bound an all-g floor would need to exceed 25706/2145, but the observed true valid R68 is only 73373/8580. Do not mistake this obstruction to one relaxation for a counterexample to universal `S>=c*s^6`.

Next useful research directions: (i) actually obtain the full original `gamma` and `mu` for general h (not provided here); (ii) tighten global physical star-overlap constraints beyond degree/cardinality relaxations, preferably with auditable dual witnesses; (iii) prove a signed JOINT all-g bound on `P_2+R` through original six-incidence fibers. No 15! search or extrapolation of the W32 minimum is justified.

**Acceptance:** all three workflows — B8-G Dedicated Contract, full inherited Research (six hosted shards and fail-closed aggregator), INDEX — SUCCESS on the same final B8-G HEAD. Parent B8-F's own final-head acceptance must be separately established. Keep Draft; leave [#230](https://github.com/definitely-stable/Mathlab/issues/230) `OPEN_WITH_FORMAL_BLOCKER`.
