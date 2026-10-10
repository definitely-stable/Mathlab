# HYP-105 B3.2-E1-C6 — all-order Johnson variance, exact shared-transposition Dirichlet, and deterministic certificate limits

Date: 2026-10-10. Parent [#230](https://github.com/definitely-stable/Mathlab/issues/230). Stacked #249 C0 (merged) → #260 C1 → #261 C2 → #266 C3 → #269 C4 → #273 C5 → C6.

**TYPE: RESTRICTED_THEOREM_C.** Exact classical Johnson permutation representation applied to actual GQ original six-incidence hypergraph and physically occupied K_a target. No original generic Johnson eigenvalue or representation theory is claimed. No theorem `inf_{f,g} S_seven(f,g)=Omega(s^6)`, no infinite counterexample B, and no GF5 full R3 bound.

## 1. The exact shared-permutation random variable (C5), including fixed occupied physical image

For every h>=1 and s=2^h, choose arbitrary original-left factor pair embedding f and arbitrary fixed occupied physical right-label image F⊆E(K_a), |F|=V=(s+1)(s²+1), with minimal K_a alphabet. The source m_f(R) is weighted on six distinct ORIGINAL right line vertices R; the target t_F(A) is one precisely when the six different **occupied physical pair labels** A produce a physical simple 2-regular six-edge factor on six physical coordinate vertices.

A single uniformly random bijection Pi:L_s→F is used for all original right lines. Define U(Pi)=sum_R m_f(R)t_F(Pi(R)). The finite product is the B-left/A-right overlap only, not the full seven GF5 class family. One fixed adversarial g is a single value of Pi and need not have U close to the mean.

C5 gives exact mean, variance by seven |R∩S| classes, and a uniform physically occupied-image random mean ≥(140−o(1))s^6. C6 adds **a second, independently falsifiable exact variance formula** that isolates contributions of each order r=0..6, including all uncontrolled fourth/fifth/sixth order terms.

## 2. Johnson harmonic squared energies from seven lower incidence moments

Let n=V≥12, X=binom([n],6), and m:X→nonnegative integers. Write m=m_0+...+m_6 for standard mutually orthogonal real isotypic projections of the multiplicity-free S_n permutation representation on six-subsets. Johnson W_r has dimension

```text
d_r = C(n,r)−C(n,r−1), 0<=r<=6, C(n,-1)=0.
```

For k=0..6 define exactly (same marginal arrays as C5)

```text
d_k(Q)=sum_{R in X, Q⊆R}m(R),             Q⊆[n], |Q|=k
A_k=sum_{Q:|Q|=k}d_k(Q)^2.
```

Classical inclusion-matrix representation theory gives eigenvalues for the positive operator I_k^*I_k (rank-k inclusion of ksets into sixsets) on W_r:

```text
B_(k,r) = C(6−r,k−r) C(n−k−r,6−k), 0<=r<=k<=6.
A_k = sum_{r=0}^k B_(k,r) * E_r(m),
E_r(m) = ||m_r||_2^2 >=0.
```

This triangular system is invertible for n≥12 because B_(r,r)=C(n−2r,6−r)>0, so

```text
E_r(m) = [A_r−Σ_{j<r} C(6−j,r−j) C(n−r−j,6−r) E_j(m)]
        / C(n−2r,6−r).
```

All calculations are **exact rational operations on seven integers A_k** already produced in C5, and Parseval checks Σ_r E_r=Σ_R m(R)^2. For 7≤n<12 (small independent toys only) the spectrum stops at r=min(6,n−6) and the same triangular formula applies. No dense C(n,6) vector or floating point diagonalization required.

## 3. Exact harmonic variance under ONE shared right permutation

For the target t_F, compute analogously E_r(t_F)=||t_{F,r}||² from its exact occupied physical sixset indicator. The W_r are pairwise nonisomorphic, irreducible real S_n representations. Schur orthogonality implies

```text
Var_Pi U = Σ_{r=1}^{min(6,n−6)} E_r(m_f)*E_r(t_F)/d_r.
```

Exactly the C5 global seven-overlap variance, now decomposed by harmonic degree with nonnegative rational contributions. The implementation checks equality of these **independent** calculations; any discrepancy is a model, spectral normalization, original-factor indexing, or implementation failure.

**Important physical occupancy caveat:** full physical T_a is a 1-design, so E_1(t_{K_a})=0. An arbitrary occupied F missing physical pair labels generally BREAKS this symmetry and can make E_1(t_F)>0. Thus C2's full-target W1=0 cannot be blindly transferred to C5's arbitrary fixed occupied F.

For W(3,2), a=6 and F=K6 full, C2's complete target energies must reappear as independent C6 exact values

```text
E_0(t)=70²/5005,
E_1(t)=0,
E_2(t)=42/11,
E_3(t)=710/1001,
E_4(t)+E_5(t)+E_6(t)=4966/77.
```

The independent source m_f from actual original W32, not a fabricated general six-uniform source, supplies all seven source E_r. Unlike C2, the residual W>=4 is resolved into three separate exact nonnegative squared energies and hence separate contributions to the C5 variance. Large target E_r alone need not imply large variance: irreducible dimension d_r divides each product.

## 4. Common-map random transposition walk — exact spectral Dirichlet identity

Fix ONE uniform Pi and, independently, sample ONE transposition tau of TWO different ORIGINAL right lines, uniformly among C(n,2) choices. Define U'=U(Pi∘tau), all sixset incidences interpreted on the same original source/physical target.

The random transposition Markov chain on sixsets has Johnson eigenvalue `1−alpha_r` on W_r, where

```text
alpha_r = r*(n+1−r)/C(n,2),    0<=r<=min(6,n−6).
```

Schur orthogonality gives the second exact identity

```text
(1/2) E_(Pi,tau)[(U'−U)²]
   = Σ_{r>=1} alpha_r * E_r(m_f)*E_r(t_F)/d_r.
```

This measures mean swap sensitivity over **ONE shared global right-map distribution**, not an independent C4 per-P map. It is NOT a bound on the value of U for every fixed right labeling.

The independent exact oracle exhausts all **8!=40320** single right bijections in a finite occupied K6 image with eight abstract original right factors, then all C(8,2)=28 swaps at EACH map: **1,128,960 ordered map/swap pairs**. It independently counts U before and after every transposition and compares the exact half squared-difference average to the spectral formula. This is a stringent normalization falsifier; no Monte Carlo fitting is accepted.

## 5. A valid deterministic all-right spectral certificate — and its scope

For ONE fixed mapping g from all original lines to the chosen occupied F, the permutation preserves the standard inner product and every W_r norm. Thus

```text
U(g) = mu + Σ_{r>=1}<m_r,g*t_r>,
mu = M(f)|T(F)|/C(V,6),
|U(g)−mu|² <= (Σ_{r>=1} E_r(m_f))*(Σ_{r>=1}E_r(t_F)).
```

Therefore the rationally checkable strict condition

```text
mu² > [Σ_{r>=1} E_r(m_f)] [Σ_{r>=1} E_r(t_F)]
```

is a sufficient universal all-g positive-overlap certificate for this one f,F. Its failure is **NOT** a counterexample. It can be sharpened using Σ_r sqrt(E_r(m_f)E_r(t_F)), retaining each order separately, but no positive universal Omega(s^6) follows unless the actual GQ model yields adequate asymptotic inequalities for EVERY legal f and F.

C6 reports both fixed-g Cauchy gate and global variance separately; never confuse the much smaller expected-squared discrepancy divided by d_r with a worst-case fixed-g discrepancy. In particular the natural attempt `sqrt(Var)<mu` is NOT a worst-case certificate — variance is an average over all n! permutations and can coexist with exceptionally bad g.

An even stronger obstruction to an inference from full global moments alone exists on the **actual GQ W(3,2)** source: reverse-line and its (4,13) right-label swap have identical source, target, all E_r, mean/variance and average Dirichlet energy, but their actual B/A overlaps differ, 77 versus 57. An auxiliary non-GQ onehot toy has identical full spectra and fixed-g 1 versus 0, showing no general spectral-only positive minimum theorem.

## 6. Prior art, QA and next decision

Johnson schemes, harmonic irreducible decompositions, eigenvalues and random-transposition walks are classical. See Rodrigo Iglesias and Mauro Natale, *Complexity of the Fourier Transform on the Johnson Graph*, 2017 (arXiv:1704.06299), and J. Ducey et al., *Integer diagonal forms for subset intersection relations*, Algebraic Combinatorics 8(1), 2025, DOI 10.5802/alco.406. The latter is a useful modern reference on inclusion/intersection matrices and Johnson Bose–Mesner algebra, not a source of a new all-correlated GQ estimate. This slice implements exact primary-model transfer, not a claim to have invented harmonic representation theory.

[Reference](../../research/hyp105_g5e2b3e1c6_johnson_variance.py) and [independent falsifiers](../../research/test_hyp105_g5e2b3e1c6_johnson_variance.py) compare 7 marginal norm squares with a separate direct marginal enumerator for n=7,8,9,12,15; test the exact 8! one-common-map variance against brute all permutations and 28 transpositions per map, verify the W32 full K6 target W2/W3/W>=4 exact accepted constants and the physically broken W1 for an occupied V=8 target, and compare genuine fixed W32 maps 77→57 with unchanged global moments.

**Acceptance:** RESTRICTED_THEOREM_C *pending exact-head* fast contract and full GitHub-hosted Research SUCCESS. Parent #230 and #176 remain OPEN. No full seven-family Omega(s6), no infinite counterfamily and no ASET exponent. C7 requires a GQ-specific *deterministic* bound on each actual correlated permutation's high-degree contractions, or an infinite legitimate all-seven-family negative family.
