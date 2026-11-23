# GIO-001.3 / G6-D7 — local PSD row-top source transfer for all two-symbol factor maps

**Research:** [#793](https://github.com/definitely-stable/Mathlab/issues/793), [#790](https://github.com/definitely-stable/Mathlab/issues/790). Frozen parent [G6-D6 #811](https://github.com/definitely-stable/Mathlab/pull/811) at `e4491693df03c263401f3cd8baa8d81278ec68c4`: specialist 18/18, INDEX, full Research SUCCESS on exact parent HEAD. This G6-D7 is a stacked **Draft**, not a merge or main change. All G6-C2/C3 FULL/CORE and HEAVY/LOW transfers remain EXPLICITLY imported and conditional. This is not unrestricted T3, a new graph family, a new ASET exponent, external academic peer review or Lean.

## 1. New, genuinely factor-adapted source gate

Earlier G6-D2 demanded a worst centered missing-projection eigenvalue; G6-D4 bounded the NUMBER of positive collinearity outliers; G6-D5 bounded the first positive spectral tail; G6-D6 bounded the second positive spectral tail. Each is a **global** spectral restriction, potentially overly conservative when permissible factor-incidence matrices can touch only a sparse subset of the positive spectral coupling.

For an ACTUAL simple thick (s,t)-biregular point–line incidence `I⊆P×L` of girth at least eight, set `r=min(s,t)`, `max(s,t)<=b*r`, original line Moore excess `Delta_L<=C*r²`, for FIXED integers `b>=1,C>=0`. Original point-collinearity adjacency A_P has degree `k_P=s(t+1)` and original line dual A_L has degree `k_L=t(s+1)`. Their original vertex counts V_P,V_L obey the known `v0*r³` bound. Define

```
  a(V) = min{a>=2: binom(a,2)>=V},
  P=I-(J/V),   D=P(A-ell*r*I)P.
```

For each source side independently, assume there EXISTS a **real symmetric** `W` satisfying `W>=0` and `W-D>=0` in Loewner order, with the following **local sparse pair budget**. Fix `ell,M>=0` BEFORE choosing source; for each row i, let `Top_{h}(W;i)` be the sum of the **h largest strictly positive** offdiagonal entries `W_{ij}` (i≠j), or all positive entries if fewer, where

```
  h = min(V-1,2(a(V)-2)).

  LOCAL_a(W) = 2*Tr(W) + sum_i Top_h(W;i).
```

**G6-D7 gate (on BOTH original types):**

```
  W_P>=0, W_P>=P_P(A_P-ell*r I)P_P,
  LOCAL_{a(V_P)}(W_P)<=M*r⁴;

  W_L>=0, W_L>=P_L(A_L-ell*r I)P_L,
  LOCAL_{a(V_L)}(W_L)<=M*r⁴.
```

This is an **existential matrix source certificate** with a fixed M, not a norm bound on F0 or on the total positive spectrum. The verifier checks any supplied rational W **exactly**; existence of an arbitrary real W is a mathematical sufficient condition but the rational finite verifier is not asserted to discover it. Note that a(V) is determined by ORIGINAL source vertex count, not by f or g, and all constants `b,C,ell,M` are fixed before the source family.

## 2. Exact row-capacity lemma for EVERY admissible factor map

For any complete MINIMAL globally unordered-pair-injective fixed `f:[V]->binom([a],2)`, its vertex-by-symbol incidence H has exactly two ones per row. For two distinct i≠j, the overlap `X_ij=(HH^T)_ij=|f(i)∩f(j)|` is in {0,1}; diagonal `X_ii=2`. Each symbol x occurs at most a−1 times, so for each i

```
  #{j != i: X_ij=1}
     <=(d_{f(i)_1}-1)+(d_{f(i)_2}-1)
     <=2(a-2).
```

Crucially, this is true even for maximally adversarial f/g and contains no randomness, correlation, eigenvector-delocalization or source-specific GQ assumptions.

For ANY symmetric W (the Loewner witness requires additionally PSD), the exact trace decomposes into

```
 Tr(W HH^T)
      = 2*sum_i W_ii + sum_i sum_{j!=i} W_ij X_ij
      <=2*Tr(W)+sum_i Top_{2(a-2)}(W;i)
      =LOCAL_a(W).                                    (D7-ROW)
```

The last inequality follows independently for each i from an exact maximum-weight subset of size at most `2(a−2)` and simply discards negative offdiagonal terms. Row-top is a VALID UPPER BOUND; no claim that some global valid unordered-pair-injective map simultaneously attains all independent row maxima is made. This is the key distinction from a fabricated worst-case label family. Both source types are handled independently.

## 3. All-order original conflicts and inherited Gram

For original regular A of valency k let `P=I-J/V` and `D=P(A-ell*r I)P`. The identity

```
 A=(k/V)J + ell*r P + D
```

is literal. Since W-D is PSD, and X=HH^T is PSD, `Tr(DX)<=Tr(WX)`. The exact original source collinearity conflict identity is

```
 2 e_col(f)=Tr(H^T A H).
```

The one-ones term is bounded by `(k/V)sum_x d_x²<=2k(a−1)`; the centered `ell*r` term is at most `2ell*rV`; and (D7-ROW) bounds the W term. Consequently, for **EVERY** allowed f,

```
 e_col(f) <= k(a−1)+ell*rV+ (1/2)*LOCAL_a(W).
```

From the accepted source envelopes `V<=v0*r³`, `a-1<=a0*r^(3/2)`, `k<=k0*r²`, define uniform FIXED integers

```
 v0=(b+1)(b²+1+C); a0=2v0+3; k0=b(b+1);
 j0=k0*a0+ell*v0+ceil(M/2);
 J0=2*j0; theta0=b+2;
 G0=2*v0*k0+2theta0*j0+2(b+1)v0*a0.
```

Then for ALL fixed factor maps `f,g`, including arbitrary adversarial correlation,

```
  e_col^P(f),e_col^L(g) <=j0*r⁴,
  J_original(f,g)<=J0*r⁴,
  Gram_P²,Gram_L²<=G0²*r^11.
```

Gram follows from the previously verified ORIGINAL G6-C1 exact pencil identity, whose missing-defect correction is ENTRYWISE nonnegative when tested on original nonnegative symbol-indicator vectors; no false PSD assertion about its action on arbitrary signed vectors.

The historical G6-C2 proper ORIGINAL 3-source-ID FULL/CORE BBo inversion, G6-C3 HEAVY/LOW single global owner/bit selector, literal `3st` source projection loads and true missing-original-projection budget `4V_P Delta_L<=4v0 C*r⁵` are **imported**, not independently reproved. With the external ordinary C6 theorem and its existential constants, the earlier conditional all-order conclusion follows for sufficiently large r and up to `rho*r⁴` removed ORIGINAL named flags:

```
  D6_original(I\Z;f,g)+BBo_produced_original(I\Z;f,g)
      >=delta*r⁶,    rho,delta>0.
```

All-order formal ledgers specify `rho,delta,r0` after fixed b,C,ell,M; numeric external `C0=c0=1` are **FORMAL_ONLY** illustrative constants, not independently verified numerical graph-theorem values. This does not prove unrestricted abstract T3 or a new ASET exponent.

## 4. Exact finite verifier / stronger source-specific certificate

The implementation `research/gio_t3d7_local_psd_rowtop.py` builds A using the ACTUAL original source point/line collinearity adjacency, validates regularity and symmetry, constructs the CENTERED cutoff D literally, and checks BOTH

```
      W PSD                  (exact rational Sylvester inertia),
      W-D PSD                (exact rational Sylvester inertia).
```

The exact minimal alphabet is computed from integer `binom(a,2)>=V`, no float square root. The verifier sorts rational positive offdiagonal entries row-by-row, uses the correct **2(a−2)** row capacity, includes diagonal contribution exactly **2Tr W**, and checks `LOCAL_a(W)<=M*r⁴` without numerical eigendecompositions. The original factor map f/g is not used to choose W; it is used only in separately calculated independent original conflict, Gram and trace checks.

The tests include independently brute-forced `Tr(W HH^T)<=LOCAL_a(W)` with nontrivial signed offdiagonals on actual prime-field Wenger W₂(3), W₂(5) and ORIGINAL doubled asymmetric GQ source flags; correlated vs lex minimal maps; all 360 ordered 4-pair maps on a separately labelled small pure-matrix algebraic test (NOT a claimed graph source); original source 4-cycle corruption that fails closed; rational PSD under-budget and wrong-dimension counterexamples. Each actual non-GQ finite source originates in source_graph, not a synthetic missing-projection matrix.

## 5. Entire true prime-power Wenger W₂(q): simple diagonal witness and fixed-cutoff no-go for old moments

The TRUE already-published original Wenger W₂(q) source family (every prime power q>=3) has

```
 n_P=n_L=q³, r=q−1,
 original Δ_L=Δ_P=2qr<=3r²,
 original centered collinearity spectrum {-q,0,+q}.
```

At **fixed** parameters `b=1,C=3,ell=0,M=11`, choose the particularly simple **diagonal** witness

```
   W_P=W_L=q*I_n.
```

It is real, rational, PSD, and dominates centered D=P A P since every centered eigenvalue of A is <=q (known published spectrum; exact finite matrices checked for prime q=3,5). All offdiagonal entries of W are ZERO, so the factor-adapted local gate is exact and independent of a:

```
  LOCAL_a(qI)=2*Tr(qI)=2*q⁴.
```

Because r>=2 implies `q=r+1<=3r/2`,

```
 LOCAL_a(qI) =2q⁴ <= (81/8) r⁴ < 11r⁴.
```

Thus **all actual Wenger prime-power orders** pass G6-D7 with fixed `ell=0,M=11`, on BOTH original types. No q³-matrix is fabricated for large symbolic q; only prime q=3,5 are explicitly instantiated in finite original geometry.

Meanwhile G6-D6 with the **same fixed ell=0,M=11** has

```
 E2_0(A)=m2*q² =q³r²/2,
```

and requires `q³<=22 r^(3/2)`, which FAILS for all integers r>=8 (and hence infinitely many real prime powers q=9,11,16,17,19,...). The earlier G6-D5 first-tail with ell=0,nu=11 and G6-D4 rank criterion also fail asymptotically. This is a **rigorously sourced, fixed-cutoff infinite-family separation of sufficient mathematical GATES**, not just one finite example.

**NOVELTY BOUNDARY:** the Wenger family and its entire spectrum are prior art. It was **already admitted by G6-D2 under its different optimized centered-F0 condition**, as well as G6-D5 with a more favorable cutoff `ell=2`. Therefore **this does NOT establish a new source family beyond the optimized union of old theorems**, nor a worldwide first graph construction. The project's mathematical contribution is the **factor-sparsity-adapted row-top positive-PSD source certificate** and its exact all-label original six-source-ID transfer.

## 6. Prior art and next mathematically material question

PSD Loewner dominance, spectral decomposition, row-wise maximal weight/capacity and exact Sylvester inertia are standard algebraic ingredients. This document does **not** claim that the row-top optimization, a priori, is unstudied. Wenger source spectra are published by Cioabă–Lazebnik–Li, [*On the spectrum of Wenger graphs* (2014)](https://arxiv.org/abs/1402.3341). The potential Mathlab contribution is application of a **uniform** sparse-label energy certificate to its historical original six-flag obstruction theory.

The next **high-value** research problem is existence or structural impossibility of a *connected, genuine, quadratic-Moore-excess* infinite original girth8 incidence source meeting a fixed `LOCAL_a(W)=O(r⁴)` gate on BOTH types, but not any of the optimized G6-D2–D6 sufficient conditions. Such sources cannot be replaced with arbitrary 0/1 regular missing F masks or a post-hoc choice of constants for a single finite graph. Alternatively, exploit exact local source codegrees to construct sparse W and bound its row tops independent of full spectral moments.

**Engineering STOP:** require exact PR-head GitHub-hosted specialist, full Research, INDEX, independent mathematical review, inspect exact original-source witness logs, do not automatically merge the stacked Draft chain, and keep #793 OPEN.
