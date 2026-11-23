# GIO-001.3 / G6-D6 — squared positive spectral tail and original two-symbol Frobenius transfer

**Tracking:** [#793](https://github.com/definitely-stable/Mathlab/issues/793), parent [G6-D5 #810](https://github.com/definitely-stable/Mathlab/pull/810) frozen at `39ef3c1643a3be06e068b69730545e8095223229` (parent specialist 17/17, INDEX and full Research accepted on the same parent HEAD). This research is **stacked as Draft**, does NOT merge the parent chain or modify main, and does NOT claim unrestricted T3, a new graph family, external referee/Lean, or improved GF5/ASET exponents.

## 1. Why this step instead of another G6-D5 finite example

G6-D5 assumes the *first* centered positive spectral excess at the fixed threshold `ell*r`:

```
   E1_ell(A)=sum_{lambda in Spec(A|1^perp)}(lambda-ell*r)_+
              <=nu*r^(5/2).
```

It gives `e_col(f)=O(r^4)` by `||H H^T||_operator<=2(a-1)`. But for `m=Theta(r^3)` distinct centered modes whose excess beyond the cutoff is `1`, the first tail is `Theta(r^3)` and **cannot pass a fixed nu**. The G6-D5 analysis found precisely this failure in the known all-order Wenger W2(q) family at `ell=1,nu=2` for all prime powers q>=16.

The next meaningful quantity is the *second* positive spectral excess, measured **separately on both ORIGINAL point and line collinearity graphs**:

```
  E2_ell(A)=sum_{lambda in Spec(A|1^perp)}
                   max(lambda-ell*r,0)^2.        (D6-E2)

  E2_ell(A_P),E2_ell(A_L) <= M*r^(7/2).         (D6-GATE)
```

All eigenvalues are counted with algebraic multiplicity; exactly one all-ones mode is excluded, so disconnected sources still charge additional principal-sized centered modes. Fixed `b>=1,C>=0,ell>=0,M>=0` are selected **BEFORE** an arbitrary original incidence source or any factor labeling. The source is an ACTUAL simple thick (s,t)-biregular original incidence of girth at least eight, `r=min(s,t)`, `max(s,t)<=b*r`, with **quadratic** original line Moore excess `Delta_L<=C*r^2`. The line and point constructions must pass the gate independently. GQ completeness, a synthesized missing matrix, source/label independence, or eigenvector delocalization is never assumed.

## 2. New exact factor Frobenius identity

For ANY complete minimal, globally unordered-pair-injective point label map `f:P -> C([a],2)`, form the **ORIGINAL** 0/1 point-by-symbol incidence H. Each row contains exactly two ones. Write the symbol fiber `S_x={p:x in f(p)}` and `d_x=|S_x|`; then

```
 sum_x d_x = 2V,             d_x <= a-1,
 sum_x d_x^2 <= 2V(a-1),
 ||H||_F^2=2V.
```

For two **distinct** points `p!=q`, `(H H^T)_{pq}=|f(p) intersect f(q)|` is either zero or one (two shared symbols would mean the same unordered factor pair and contradict injectivity). On the diagonal, `(H H^T)_{pp}=2`. Therefore there is the **exact combinatorial identity**:

```
  ||H H^T||_F^2
      = 4V + 2 sum_x binomial(d_x,2)
      = 2V + sum_x d_x^2
      <= 2Va.                                     (D6-FROB)
```

The same identity holds independently on original line vertices for *any* admissible g. No probability and no f/g decorrelation is used. This is a checkable source-factor identity, not just an abstract norm bound.

## 3. Source-only all-label conflict and Gram theorem

Let `A=A_P` be the actual original point-collinearity adjacency, regular of degree `k=s(t+1)`. With `P_0=I-J/V` set

```
  D=P_0(A-ell*r I)P_0,
  D_+=(D+|D|)/2,   Tr(D_+^2)=E2_ell(A).
```

Since `A=(k/V)J+ell*r P_0+D` and `D<=D_+`, taking the factor-incidence trace yields

```
  2 e_col(f)=Tr(H^T A H)
       <= (k/V)sum_x d_x^2
          + ell*r*Tr(H^T P_0 H)
          + Tr(D_+ H H^T)
       <= 2k(a-1) +2ell*r V
          + sqrt(Tr(D_+^2)*Tr((H H^T)^2)).
```

The last line is **Schatten-2 / Hilbert-Schmidt Cauchy–Schwarz**, not a new independent spectral graph theorem. Combining (D6-FROB) and (D6-GATE),

```
 e_col(f) <=k(a-1)+ell*rV+ (1/2)*sqrt(2Va*M*r^(7/2)).  (D6-CONFLICT)
```

Use the already proved all-order G6-C1/G6-D2 source envelopes

```
  V <= v0*r^3,   a <= a0*r^(3/2),    k<=k0*r^2,
  v0=(b+1)(b^2+1+C), a0=2v0+3, k0=b(b+1).
```

Then the exact third term scales as `r^(9/4+7/4)=r^4`. Set the safe **fixed integer**:

```
  u0=ceil_sqrt(2*v0*a0*M),
  j0=k0*a0+ell*v0+u0.
```

This deliberately rounds up the square-root term, making `e_col(f)<=j0*r^4` for every r>=1, every admissible fixed f. Repeat on the **original line dual** for every fixed g. Hence

```
  J_original(f,g) <= 2*j0*r^4.
```

The G6-C1 **exact source** pencil-gram identity uses an entrywise nonnegative defect and nonnegative indicator vectors; the negative defect correction may be dropped **only on these indicators**, never claiming the defect matrix is positive semidefinite. With `theta0=b+2`, `mu<=(b+1)r`, the same fixed

```
  G0=2*v0*k0 +2*theta0*j0 +2*(b+1)*v0*a0
```

proves `Gram_P^2,Gram_L^2<=G0^2*r^11` for every f,g (source `Gram=O(r^(11/2))`).

**Conditional T3 conclusion, carefully scoped.** Apply the previously accepted G6-C2 proper FULL/CORE inverse and G6-C3 original HEAVY/LOW single-global-owner/bit selector, external ordinary-graph C6 counting theorem, and original source threeflag projection load `3st`. The original missing-projection endpoint count remains `4V_P Delta_L<=4v0*C*r^5`, exactly at the **critical fifth-power** scale. The G6-D6 all-order formal ledger fixes the four LOW error budgets first, then a positive `rho,delta,r0` for each fixed b,C,ell,M. Subject to these explicitly imported inputs and sufficiently large r,

```
  D6_original(I\Z;f,g)+BBo_produced_original(I\Z;f,g)
          >= delta*r^6  for every original deletion |Z|<=rho*r^4.
```

The numeric graph C6 placeholders `C0=c0=1` in tests are **FORMAL_ONLY**, NOT verified published numerical constants. No unconditional abstract T3, better GF5 ASET exponent, or independent full formalization follows.

## 4. Exact PSD/squared-energy certificate — no floating eigenvalues

On the original centered subspace define `D=P_0(A-ell*rI)P_0`. Supply a rational symmetric W satisfying

```
     W >= 0,          W-D >=0            (both Loewner PSD),
     [Tr(W^2)]^2 <= M^2*r^7.            (D6-PSD)
```

Since `W>=D`, the Courant–Fischer/Weyl variational eigenvalue inequality gives `lambda_i(W)>=lambda_i(D)` in nonincreasing order. As `W>=0`, each `lambda_i(W)^2 >= max(lambda_i(D),0)^2`. Thus **E2_ell(A)<=Tr(W^2)**. The exact implementation checks PSD through rational Sylvester congruences (including indefinite two-by-two temporary pivots), computes `Tr(W^2)=sum_{i,j}W_ij^2` with exact fractions, and checks the equivalent integer/rational seventh-power inequality. This is a **sufficient** computable witness, not an assumption that every source with the gate has an efficiently obtainable rational W. Taking the true spectral positive part W=D_+ is valid over reals; finite rational certificates exploit known original-source projectors.

The independent tests construct H directly from original source pair labels and check **entrywise both ways** that `||H H^T||_F^2=2V+sum_x d_x^2`, and verify the exact rational Cauchy–Schwarz inequality
`Tr(W H H^T)^2 <= Tr(W^2)*Tr((H H^T)^2)`, on true source and dual original point/line graphs. This prevents a synthetic source/matrix numerical check from masquerading as a source result.

## 5. Real INFINITE Wenger family: strict same-threshold separation from G6-D5

The **existing, prior-art** Wenger W2(q) original incidence family exists for *every prime power q>=3*. Published exact source collinearity spectra: `A_P` and `A_L` have one principal mode `k=q(q-1)`, and centered levels `-q,0,+q`; multiplicity of `+q` is `m2=q(q-1)^2/2`. Here the ORIGINAL flags number `q^4`, `r=q-1`, and `Delta_L=Delta_P=2q(q-1)<=3r^2` for r>=2. Hence **fixed family constants** `b=1,C=3,ell=1,M=1` apply for all prime powers q>=3.

At this fixed cutoff `ell*r=r`, the positive excess of the `+q` source mode is **exactly one**. Consequently

```
  E2_ell(A)=m2=q*r^2/2;
  [E2_ell(A)]^2<=r^7
    <=> (r+1)^2<=4r^3,       TRUE for every integer r>=2.
```

Both typed sides satisfy the same gate, for the **entire existing infinite family**. The original D5 **fixed** `ell=1,nu=2` first-tail criterion would instead require

```
  [E1_ell(A)]^2<=4r^5
   <=> (r+1)^2<=16r,
```

which **fails for all integer r>=14**, and therefore for infinitely many real prime powers q>=16 (q=16,17,19,32,64,...). The original D4 rank criterion at the same cutoff similarly fails asymptotically. This is a **strict all-order / infinite-family separation of two FIXED-CUTOFF SUFFICIENT GATES**, unlike the merely finite W2(5) witness in G6-D5.

**Critical novelty limitation:** this is **NOT a newly discovered graph family or a new obstruction theorem on a previously inaccessible infinite family**. Wenger graphs, their spectral multiplicities and an alternative G6-D2 centered-F0 norm gate on this SAME family were already known/accepted. In particular choosing `ell=2` makes the earlier D5 first positive tail vanish on Wenger, and the old D2 centered missing-F0 bound also works. What is genuinely added to this Mathlab research programme is an independent **quadratic positive-tail condition and a sharper two-symbol factor-Frobenius transfer**, not a new worldwide graph construction.

Finite actual-source rational PSD witnesses are independently checked for prime W2(3) (27 vertices/side) and W2(5) (125 vertices/side). For any published prime power q>=3, the same polynomial centered +q original adjacency projector

```
 Q_plus=A(A+qI)/(2q^2)-k(k+q)J/(2q^2 q^3)
```

gives the rational W=Q_plus (since the excess is 1). It is PSD, majorizes the centered cutoff D, and has `Tr(W^2)=m2` for every q. Symbolic arithmetic covers published q=3,4,5,7,8,11,13,16,17,19,23,31,32,64,101 without fabricating huge q³ finite incidence graphs.

## 6. Prior art, acceptance and next frontier

The matrix Frobenius Cauchy–Schwarz and generalized Schatten Hölder inequalities are standard: [CWI Lecture Notes, Norms and Distance Measures](https://homepages.cwi.nl/~fehr/QIT2021/Chap7.pdf). The Wenger original incidence family and its entire spectrum are published: [Cioabă, Lazebnik, Li, *On the spectrum of Wenger graphs*, JCTB (2014)](https://arxiv.org/abs/1402.3341). The novel-in-project statement is the *specific conditional transfer* of a second positive spectral moment through **all** original, minimally pair-injective factor maps into the existing original six-source-ID obstruction.

**Acceptance:** all exact HEAD GitHub-hosted specialist tests + JSON certificate, INDEX, full Research; independent written mathematical critique including the squared-moment PSD witness, dual side, all-order fifth-power endpoint and correct infinite-family limitation. This does **not** replace external academic review.

**Next genuine mathematical obstacle:** construct an ACTUAL connected quadratic-excess infinite source family that obeys D6's squared positive tail but fails the *optimized* D2 centered-F0, D4 count and D5 first-tail assumptions even after choice of each theorem's fixed parameters; or establish a fiber-specific/sparse-label transfer beyond every global Schatten moment. **Do not** claim this from a synthetic missing mask or known Wenger family alone. #793 remains OPEN, Draft PRs remain unmerged.
