# GIO-001.3 / G6-D4 — bounded positive outliers transfer, with no centered-F norm gate

**Scope and governance.** Research [#793](https://github.com/definitely-stable/Mathlab/issues/793), [G6-D1-FIX #808](https://github.com/definitely-stable/Mathlab/pull/808) exact **frozen parent** `2940b21deefaa997f78f3f9b0ec7beb8047f7334`. Original G6-C1/C2/C3 and corrected D1/D2/D3 stack is retained without changes. This is a **new conditional source theorem** plus finite exact falsifiers, NOT a theorem for arbitrary quadratic-excess sources, a new spectral graph family, proof of a better ASET exponent, external human peer review or Lean formal proof.

## 1. The question, and a strictly better algebraic idea

The G6-D2 quadratic-excess conditional transfer assumed a **global centered singular bound** `||F0||_2^2 <= kappa*r^3` on the original missing-projection matrix F. G6-D3 verified that bound for the classical affine-arc/Wenger-like source family. It remains unknown whether every ACTUAL quadratic-excess near-Moore girth-eight source automatically enjoys it.

The earlier proposed G6-D4 approach controlled exceptional collinearity eigenvalues using individually delocalized eigenvectors. **Delocalization is unnecessary.** For a minimal, complete, separately globally pair-injective fixed factor map, its vertex-by-symbol incidence matrix H has *exactly two ones per row* and at most *a−1 ones per column*. Thus for any real unit vector v:

```
  ||H^T v||_2^2 <= ||H||_2^2
                  <= ||H||_infinity ||H||_1
                  <= 2(a-1).
```

This elementary factor-incidence operator inequality permits a *small collection of arbitrarily localized source eigenvectors*. No random f/g, no correlation condition, no eigenvector infinity norm or incoherence is needed.

## 2. Fixed-parameter source theorem: G6-D4 / OUTLIER-T3

Fix integers `b>=1`, `C>=0`, `ell>=0`, `nu>=0` **before** selecting any source graph or its factor maps. Let `I ⊆ P×L` be an ACTUAL finite, simple, thick, (s,t)-biregular original point-line incidence with girth at least eight. Each point is incident with t+1 original lines; each line with s+1 original points. Put

```
  r = min(s,t),           max(s,t) <= b*r,
  V_P = |P|,              V_L = |L|,
  Delta_L = V_L-(t+1)(st+1),
  Delta_P = V_P-(s+1)(st+1),
  Delta_L <= C*r^2,
  (t+1)*Delta_P = (s+1)*Delta_L.
```

Let `A_P` be the original point-collinearity adjacency matrix: two *distinct* original points adjacent when they lie on an actual ORIGINAL line; let `A_L` be its line dual. Their degrees are `k_P=s(t+1)` and `k_L=t(s+1)`, respectively.

**Additional, source-intrinsic spectral multiplicity gate** (NOT claimed automatic from degree/girth/excess):

```
  #{ eigenvalues lambda of A_P restricted to 1_P^perp
       with lambda > ell*r }^6 <= nu^6*r^7,

  #{ eigenvalues lambda of A_L restricted to 1_L^perp
       with lambda > ell*r }^6 <= nu^6*r^7.
```

This is the **critical fractional outlier-rank gate** `m<=nu*r^(7/6)`, verified with **exact integers** as `m^6<=nu^6*r^7`. Count multiplicity exactly, including nontrivial principal-sized modes of disconnected graphs. Negative eigenvalues need no extra gate. The older `m<=nu*r` condition is a strictly stronger sufficient subcase for r>1.

Under these conditions, for **EVERY** complete minimal separately pair-injective typed fixed factor labels `f:P -> C([aP],2)`, `g:L -> C([aL],2)`, allowing arbitrary within-type ordering and **adversarial f/g correlation**, there exist uniform constants

```
  e_col^P(f), e_col^L(g) <= j0*r^4,
  J_original(f,g) <= 2*j0*r^4,
  Gram_P(f), Gram_L(g) <= G0*r^(11/2).
```

The last bound is expressed as the **integer-checkable inequality** `Gram^2<=G0^2*r^11`.

Provided the **same accepted G6-C3 original HEAVY/LOW supersaturation argument**, historical G6-C2 proper FULL/CORE three-source-ID book inverse, and the published ordinary C6 counting theorem with its existential external constants, this gives a **conditional original-source T3**: for sufficiently large r, and for any adversarial deletion of at most `rho*r^4` original named flags,

```
  D6_original(I\Z;f,g) + BBo_produced_original(I\Z;f,g)
       >= delta*r^6,
```

for `rho,delta>0` and `r0` depending **only on b,C,ell,nu** and published external graph constants. No invented projection flags; no GQ completeness assumed. In the existing argument the exact original missing endpoint budget is `4 V_P Delta_L <=4 v0 C r^5`, not an invalid o(r^5) claim. **This is a conditional extension of #793, not a settled unrestricted T3 theorem.**

## 3. New universal conflict lemma, exact proof

Write the original point label incidence `H[p,x]=1` when x is one of the two factor symbols of f(p). Pair injectivity implies `d_x=|{p:x in f(p)}|<=a_P-1`. Then `sum_x d_x=2V_P`, `sum_x d_x^2<=2V_P(a_P-1)`, and the operator norm inequality above gives `||H^T v||^2<=2(a_P-1)` for **every** normalized eigenvector v.

Every original collinear pair shares at most ONE factor symbol (otherwise its unordered factor pair would coincide). Therefore, with `A=A_P` and `V=V_P`,

```
  2 e_col(f) = sum_x 1_{S_x}^T A 1_{S_x}
             = Tr(H^T A H).
```

Since the ORIGINAL A is k-regular, split its spectral decomposition into its one *specified* all-ones mode `(k/V)J`, centered eigenvalues <=ell*r, and the exceptional centered eigenvalues >ell*r. For the all-ones mode,

```
  (k/V) ||H^T 1||^2 <= 2k(a_P-1).
```

For the nonexceptional modes, including all negative ones, the total contribution is at most `ell*r * ||H||_F^2 = 2 ell*r*V`. For exceptional orthonormal eigenvectors `v_j`, the factor-operator norm gives `||H^T v_j||^2<=2(a_P-1)`. **No assertion on individual coordinates of v_j is used.** Thus

```
  e_col(f) <= k(a_P-1)+ell*r*V
                     +(a_P-1)*sum_exceptional(lambda_j^+).     (D4-C)
```

The same proof, independently, holds for the line dual.

By corrected D1's literal original-source threewalk relation,

```
  (BB^T)(BB^T-(s+t)I)^2
      = FF^T+(V_L-2 Delta_L)J_PP.
```

For a centered eigenvalue x of `BB^T`,

```
  x(x-s-t)^2 <= Delta_L Delta_P.
```

If x>=2(s+t), then `x^3<=4 Delta_L Delta_P`; if not, x<=2(s+t). Now use `Delta_P<=(b+1)C*r^2`, `2(s+t)<=4br`, and the **fixed integer**

```
  B0 = ceil_cuberoot(4(b+1) C^2).
```

Any positive original collinearity eigenvalue `lambda=x-(t+1)` obeys

```
  lambda <= (4b+B0)*r^(4/3)           (r>=1).
```

The exact sixth-power gate implies at most `nu*r^(7/6)` positive exceptional eigenvalues, so

```
 sum_exceptional lambda_j^+ <= nu(4b+B0) r^(5/2).
```

As `V<=v0*r^3`, `a_P<=a0*r^(3/2)`, `k<=k0*r^2`, the right-hand side of (D4-C) is

```
 e_col(f) <= [k0*a0 + ell*v0 + a0*nu*(4b+B0)]*r^4
           = j0*r^4
```

because `r^(7/2)<=r^4` and the exceptional factor `r^(3/2)*r^(5/2)=r^4` **exactly**, for every r>=1. **This is a genuinely uniform all-label bound at the critical exponent 7/6.** More generally, if exceptional rank is `O(r^gamma)`, this proof yields exceptional conflict scale `O(r^(gamma+17/6))` and closes at the r⁴ threshold precisely for `gamma<=7/6`. This is a threshold **for this trace-and-cubic bound**, not an impossibility theorem for larger rank or a claim that sources attaining equality exist. The earlier O(r)-rank subcase gives the stronger `O(r^(23/6))=o(r⁴)` exceptional term.

For clarity the explicit constants match the G6-D2/source ledger envelope:

```
 v0=(b+1)(b^2+1+C); n0=(b+1)v0; a0=2v0+3;
 k0=b(b+1); theta0=b+2;
 J0=2j0;
 G0=2v0*k0+2theta0*j0+2(b+1)v0*a0.
```

The Gram formula is **the original exact** G6-C1 identity

```
 G = 2V(k-mu)+2theta*e_col+mu*sum_x d_x^2
                       -sum_x 1_Sx^T D 1_Sx.
```

The final term is **nonnegative BEFORE subtraction only for actual nonnegative symbol indicators**, because the original defect D is entrywise nonnegative; it is **not PSD on arbitrary signed vectors**. Apply `|theta|<=theta0*r`, `mu<=(b+1)r`, `e_col<=j0 r^4`, `sum d_x^2<=2V(a-1)` to get `G<=G0 r^(11/2)`. No hidden GQ identity is substituted.

## 4. Exact independent finite certificates

Implementation `research/gio_t3d4_few_outliers.py` computes the integer count of eigenvalues exceeding `ell*r` by **exact rational Sylvester congruence**, including indefinite **2×2 zero-diagonal pivots**, not NumPy floating eigenvalues or a loose Gershgorin bound. For regular A it counts positive inertia of `A-ell*r I` and removes exactly one positive principal all-ones eigenvalue when `k>ell*r`. In particular, extra principal eigenvectors of disconnected sources are **not** erased. The implementation reconstructs the actual graph through G6-C1's original-incidence source oracle and checks the actual point and line side separately.

Finite genuine fixtures include `W32`, `GQ(2,4)`, `GQ(4,2)`, actual prime-field Wenger `W2(3)`, `W2(5)`, and disjoint **real original** double sources `2*W32`, `2*GQ(2,4)`, `2*GQ(4,2)`; the source labels are lexicographic or correlated minimal label maps. Independently coded vertex-by-symbol trace checks compare `Tr(H^T A H)=2e_col` on original source adjacency. All double sources have precisely ONE extra large centered collinearity eigenmode per side at cutoff `ell=2`, whereas undoubled GQ and tested Wenger sources have zero. The previous D2 `kappa=1` norm gate is violated by the actual double's exact centered block-sign Rayleigh quotient `Delta_L Delta_P > r^3`, yet D4 `ell=2,nu=1` passes. **This is a strictly differentiating finite witness only:** doubled GQ families have `Delta=Theta(r^3)` as order varies, so these cases do NOT prove existence of any infinite quadratic-excess family outside D2.

Formal all-order fixed-parameter HEAVY/LOW ledgers are provided for `(b,C,ell,nu)=(1,3,2,1),(1,3,2,0),(2,12,2,1)`. Their graph C6 numeric inputs `C0=c0=1` are **FORMAL placeholders** not asserted as published constants. All four inherited LOW budgets are independently asserted in exact integer/rational arithmetic, including the **O(r^5)** original missing-projection endpoint term.

## 5. Prior art / research boundary / next source realizability

- The spectral theorem, source adjacency decompositions, operator norm `||H||_2^2<=||H||_1 ||H||_infinity`, and Sylvester inertia are standard linear algebra. Neither the norm argument nor spectral counting is claimed as a newly discovered worldwide theorem.
- Classical Wenger-graph spectra and their embeddings into generalized-quadrangle incidence have published prior art: Cioabă–Lazebnik–Li, [On the Spectrum of Wenger Graphs](https://arxiv.org/abs/1402.3341) (2014).
- The **research-program contribution** is the use of the elementary two-symbol factor-incidence trace to replace a **worst-eigenvalue missing-projection** gate in the *historical original six-ID D6+produced BBo transfer*, conditional on the inherited G6-C2/C3 source-level proof. Original six-flag counting itself remains the previously established machinery; this work proves a new *sufficient A1/G1 source certificate*.
- **OPEN:** construct an ACTUAL infinite, connected quadratic-excess girth8 biregular source family that obeys few-outlier gate but violates every fixed global `||F0||^2<=kappa*r^3` bound. Synthetic 0/1 regular missing matrices do not count. Also open: show few-outlier multiplicity automatically from intrinsic near-Moore girth hypotheses (or prove a counterexample).
- No automatic change to issue #793 completion, no permission to merge stacked Draft PRs implicitly, no external independent human referee or Lean certification, no new dependent-GF5 ASET improvement.

**Engineering acceptance:** require exact HEAD specialized GitHub-hosted unittest+JSON assertion, full `research`, INDEX, and independent written mathematical critique; reject if the source-derived spectral argument incorrectly counts trivial modes, if the conditional T3 is presented as unconditional, or if any finite certificate is claimed as an infinite-family witness.
