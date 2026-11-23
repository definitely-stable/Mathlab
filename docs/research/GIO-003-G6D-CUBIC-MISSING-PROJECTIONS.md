# GIO-001.3 / G6-D1 — cubic missing-projection operator; extend intrinsic T3 from linear to 3/2 excess

**Research issue:** [#793](https://github.com/definitely-stable/Mathlab/issues/793), meta [#790](https://github.com/definitely-stable/Mathlab/issues/790). **Stacked prerequisite:** [G6-C3 PR #804](https://github.com/definitely-stable/Mathlab/pull/804), exact head `cc256e6147a3f267c9b11c35771de1ac9609e7ad`, and its G6-C1/C2 ancestors. All new results here concern original source incidence and *fixed minimal typed factor alphabets*. This document does NOT assert an infinite genuinely non-GQ positive-excess family, an unrestricted T3 theorem or a new ASET exponent.

## 1. The real obstacle and the research decision

G6-C3's conditional non-template theorem T3-L currently requires linear line Moore excess `Delta_L<=C*r`, where `r=min(s,t)`, `max(s,t)<=b*r`, and b,C are fixed before the source family. The G6-C1 symmetric defect matrix `D_P` has row sum `(s+1)Delta_L`, so the crude operator-norm estimate yields source collinearity spectral bound `O(r+sqrt(r*Delta_L))`; substituting `Delta_L=O(r²)` gives O(r^1.5), too large for the old `O(r⁴)` source-conflict budget. This is an **insufficiency of that bound**, not a proof that the original theorem fails for larger excess.

The more natural object is the ***rectangular original source missing-projection matrix*** F, not the `P×P` defect matrix D. The exact threewalk operator gives a **cubic** polynomial constraint and improves the permitted excess threshold to `Delta_L=O(r^(3/2))`, while retaining `O(r)` source collinearity spectrum and `O(r⁴)` conflict count.

## 2. Lemma CUBIC-I — exact rectangular source threewalk identity, no geometry axiom

Let I⊆P×L be **any finite simple (s,t)-biregular source incidence graph with girth>=8**, thick integral s,t>=2; every source line has s+1 points, every source point t+1 lines. Let `B` be its actual P×L {0,1} biadjacency matrix, `J_PL` the all-ones rectangle, and define

```
V_P0=(s+1)(st+1), V_L0=(t+1)(st+1),
Delta_P=|P|-V_P0, Delta_L=|L|-V_L0,
(t+1)Delta_P=(s+1)Delta_L.
```

A nonincident original source pair (p,ell) has **at most one** original p–line–point–ell three-flag path by girth>=8. Define `F[p,ell]=1` exactly when p is nonincident to ell and has **no** such original three-flag path; otherwise 0.

Every actual incident (p,ell) has precisely `s+t+1` original three-edge walks from p to ell: either the first line is ell, contributing s+1 point choices, or the middle point is p, contributing t+1 first-line choices, minus their one overlap. An additional walk with both different would create a forbidden source 4-cycle. Every nonincident pair has either exactly one threewalk or none, by the source 6-cycle prohibition.

Thus *entrywise* the exact identity is

```
       BB^T B - (s+t)B = J_PL - F.                       (CUBIC-I)
```

The missing matrix F has **constant row sum** Delta_L and **constant column sum** Delta_P, from the G6-C1 exact Moore projection census, not from GQ completeness. F=0 if and only if every original nonincident pair is projected, i.e. the source is a GQ at these regular parameters. For a non-GQ source the missing entries stay missing.

## 3. Lemma CUBIC-II — dual operator polynomial and singular spectral constraint

Put `T=BB^T`, `U=B^TB`, `h=s+t`. Multiply (CUBIC-I) by its transpose. Since

`(J_PL-F)(J_PL-F)^T=FF^T+(|L|-2Delta_L)J_PP`,

the following matrix identity holds **on all entries**, not merely on centered vectors:

```
 T (T-hI)^2 = FF^T + (|L|-2Delta_L)*J_PP.             (CUBIC-II-P)
 U (U-hI)^2 = F^TF + (|P|-2Delta_P)*J_LL.             (CUBIC-II-L)
```

The second equation follows independently by transposing the original incidence. Both F and B may be rectangular, and s need not equal t.
**Asymmetric full-matrix correction (G6-D1-FIX, 23 November 2026).** The original stacked #805 text interchanged `Delta_L` and `Delta_P` in the rank-one coefficients above. `F` has **row sum `Delta_L`** and **column sum `Delta_P`**; hence `JF^T=FJ^T=Delta_L J_PP` and `F^TJ=JF=Delta_P J_LL` with the appropriate rectangular all-ones matrices. This changes the full-entry equations for asymmetric positive-excess sources. It does **not** alter their centered restrictions on `1^perp`, nor the resulting `x(x-h)^2 <= Delta_L Delta_P` bound, because every rank-one `J` term vanishes there. An independent exact genuine non-GQ disconnected doubled `GQ(2,4)` (and its dual) fails the old formula and satisfies the corrected one on all entries; see `test_19_asymmetric_nonGQ_full_rank_one_coefficients` and the [correction audit](GIO-003-G6D1-RECTANGULAR-CUBIC-CORRECTION.md). Historical immutable PR-head prose is superseded by this repair; #793 unrestricted T3 stays OPEN.


Because F has nonnegative entries, constant row sum Delta_L and constant column sum Delta_P, its exact operator norm is `||F||₂=sqrt(Delta_L*Delta_P)`: the all-ones left/right singular vectors realize this value, while the induced norm inequality `||F||₂²<=||F||_∞||F||₁=Delta_L*Delta_P` gives the matching upper bound. When both defects vanish, F=0. The symmetric nonnegative matrices `FF^T,F^TF` ARE positive semidefinite; this **does not** imply the old G6-C1 square defect `D_P` is positive semidefinite (it is not, as its negative -45 eigencase shows).

On `1_P^⊥`, every eigenvector of symmetric T with eigenvalue x≥0 satisfies, by (CUBIC-II-P),

```
             x (x-h)^2 <= Delta_L*Delta_P.             (CUBIC-S)
```

The right-hand inequality holds for every such eigenvalue, regardless of connectedness. For the dual U the same inequality holds on `1_L^⊥`. Indeed, if x≥2h, then x-h≥x/2, hence x³/4≤Delta_LDelta_P. Otherwise x<2h. Thus, with `L=ceil_cuberoot(4Delta_LDelta_P)`,

```
0 <= x <= 2h+L.
```

The original point-collinearity adjacency is `A_P=T-(t+1)I`, and the dual line-collinearity adjacency is `A_L=U-(s+1)I`. Their nontrivial/centered eigenvalues therefore satisfy the **safe integer bounds**

```
|lambda_P| <= 2(s+t)+(t+1)+L,
|lambda_L| <= 2(s+t)+(s+1)+L.
```

These bounds are deliberately conservative and avoid any floating-point eigensolver or missing GQ SRG spectrum.

## 4. Theorem S(3/2) — **uniform** source conflict and corrected Gram scaling

Fix integers b≥1 and C≥0 **before an arbitrary asymptotic family and before factor labels**. Put r=min(s,t), assume max(s,t)≤br and instead of the old linear hypothesis impose the strictly **weaker** half-integer scale

```
         0<=Delta_L<=C*r^(3/2).
```

For exact arithmetic the implementation checks the equivalent integer inequality `Delta_L²<=C²*r³`, without ever computing a floating square root.

Balance implies `Delta_P=(s+1)/(t+1)*Delta_L <=(b+1)*C*r^(3/2)`; hence

```
Delta_L*Delta_P <= (b+1)*C²*r³,
ceil_cuberoot(4Delta_LDelta_P)
  <= ceil_cuberoot(4(b+1)C²)*r.
```

Consequently both centered collinearity spectra are bounded by `Lambda0*r` with

```
h0=ceil_cuberoot(4(b+1)C²), Lambda0=5b+1+h0.
```

For separately complete minimal and globally pair-injective `f:P→binom([aP],2)` and `g:L→binom([aL],2)`, possibly adversarial and mutually correlated, set the all-order conservative constants

```
v0=(b+1)(b²+1+C), n0=(b+1)v0,
a0=2v0+3, A0=a0², k0=b(b+1), theta0=b+2,
j0=k0*a0+Lambda0*v0, J0=2*j0,
G0=2*v0*k0+2*theta0*j0+2(b+1)*v0*a0.
```

Because `Delta_P=O_(b,C)(r^1.5)=o(r³)`, the original source sizes still obey `V_P,V_L<=v0*r³`, `N<=n0*r⁴`, and each minimal typed alphabet `aP,aL<=a0*r^1.5`. The **same exact** minimal symbol-fibre expander-mixing argument as G6-C1, but with CUBIC-S instead of its D-based spectral cap, gives for **every** f,g:

```
e_col,P<=j0*r⁴, e_col,L<=j0*r⁴,
e(original owner conflict J)<=J0*r⁴.
```

For the point/line pencil Gram, use the **exact old G6-C1 defect identity** `G=2V(k-mu)+2theta e_col+mu Σn_x²-Σu_x^T D u_x`. On true nonnegative symbol-indicator u_x, the negative D correction may be dropped, although D is indefinite on arbitrary signed vectors. With `theta=O_b(r)`, these conflict estimates give `G_f,G_g<=G0*r^(11/2)` **uniformly** under the broader half-integer source excess.

The key improvement over G6-C1 is **not** a new source GQ axiom: it is an independent cubic spectral gate recovered from the rectangular original missing-projection matrix F. For Delta_L=O(r²), this elementary cube-root bound gives `Lambda=O(r^(4/3))` and source conflicts at most `O(r^(13/3))`, not the required O(r⁴). No arbitrary O(r²) excess theorem is claimed.

## 5. Theorem T3-(3/2) — quantifier-closed HEAVY/LOW consequence

The exact original HEAVY/LOW and same-global-selector argument has already been explicitly assembled in [G6-C3](https://github.com/definitely-stable/Mathlab/pull/804), with its original source three-corner book, three original surviving FULL anchor inverse and shared correlated owner-priority proof. **Those combinatorial steps depend on the source only through** (a) source cardinalities N,V_P,V_L and minimal alphabets; (b) e(J)=O(r⁴); (c) G_f/G_g=O(r^(11/2)); (d) every original flag occurs in exactly 3st source projections; and (e) an upper bound on original unprojected nonincident endpoint pairs.

Items (a)-(d) remain unchanged in scale by Theorem S(3/2). The only changed endpoint loss (e) is

```
            4 V_P Delta_L <=4v0*C*r^(9/2)
                            <=4v0*C*r⁵    (r>=1).
```

Thus the original G6-C3 error ledger remains valid with the **new** v0,n0,j0,J0,G0 and the same conservative `E0=4(2a0v0+a0²)+4n0+4v0 C+8bJ0`. In particular choose the external **existential** ordinary graph C6 supersaturation constants as rationals `C0>=max(1,C_graph)`, `0<c0<=min(1,c_graph)`. These numeric values are *not supplied* by the current research; sample finite ledgers `C0=1,c0=1` are **FORMAL_ONLY** and must never be presented as published constants.

Freeze b,C, then v0,…G0, then admissible external C0,c0, then `K=16J0+1,R=512A0(1+64J0),T=ceil(8n0R³C0³),w=8/A0²`, `q2=16(K+1)²,q3=64(K+1)³`, moments `Q0=8n0+4J0,L6=1+ceil(36n0T²),L4=q2²ceil(sqrt(n0L6))+Q0T`, and `BK=ceil(sqrt(16(b+1)n0G0(K+1)T))`, `D=4ceil(sqrt(BKTL4))`, `E=q3ceil(sqrt(E0 L6))`. **Only then** choose

```
eps=w/8,
rho=min(1/32,eps²/(12b²q3² L6)) >0,
delta=min(c0/R^6,w/4)>0,
r0=max(2^32,ceil(3TQ0/eps),ceil((E/eps)²),ceil((D/eps)^8)).
```

The exact certificate checks all four LOW errors at r>=r0: improper ≤eps r⁶, clean endpoints ≤eps r⁶, deleted true original anchors ≤eps r⁶, four FULL/CORE inner blockers ≤eps r⁶. In HEAVY original historical D6≥c0 r⁶/R⁶, and in LOW actual produced BBo>w r⁶/4. Therefore:

**Conditional intrinsic Theorem T3-(3/2).** For any actual finite thick simple (s,t)-biregular girth>=8 original incidence I with fixed b,C and Delta_L<=C*r^(3/2), every adversarial complete minimal separately pair-injective typed f/g, and every original source flag deletion |Z|<=rho_(b,C) r⁴, for all r>=r0_(b,C),

```
     D6(I\Z;f,g) + BBo_produced(I\Z;f,g)
                       >= delta_(b,C) r⁶.
```

Only genuinely existing original projections are eligible to produce BBo; **no hidden old GQ witness, field or completion** enters. Source-disjoint original six-ID packing and iid GF(5) trade-sign collision Chernoff consequences follow on the same explicitly restricted family, by the accepted #230/#799 argument. Nothing here proves dependent coefficients or unrestricted ASET bounds.

**Nonvacuity:** the class includes real GQ sources (Delta=0). The existence of an infinite genuinely non-GQ family with **positive** Delta_L<=C*r^(3/2) has NOT been established. The exact finite doubled-W32 source tests validate polynomial identities and geometry-free requirements but have Delta_L~Theta(r³) when extended to higher order: they cannot be extrapolated to the target asymptotic regime.

## 6. Extra exact rigidity: symmetric per-part excess ONE is impossible

Fix equal order s=t=q≥2. Suppose a biregular girth>=8 source existed with `Delta_L=Delta_P=1`. The original rectangular missing projection F is now a **square permutation matrix**, because each of its |P| rows and |L| columns has exactly one 1 and both part sizes equal `V=(q+1)(q²+1)+1`. Therefore `FF^T=I`.

With `T=BB^T`, the exact centered cubic identity reads

```
                T(T-2qI)^2=I  on 1^perp.
```

The symmetric integer matrix T preserves the rational zero-sum subspace. Its characteristic polynomial there has roots of the monic cubic

`p_q(x)=x(x-2q)^2-1=x³-4q x²+4q²x-1.`

For integral q≥2 the only potential rational roots (rational-root theorem) are ±1; `p_q(1)=4q(q−1)>0` and `p_q(-1)=−(2q+1)²−1<0`. Thus this cubic is **irreducible over Q**. Its three conjugate eigenvalues must occur with *equal* multiplicities `(V−1)/3`. Their sum is 4q, so the centered trace must equal `4q(V−1)/3`.

But T has every diagonal entry q+1, and its all-ones eigenvalue is `(q+1)^2`, so its actual centered trace is `V(q+1)−(q+1)^2`. Equality would force

`3[V(q+1)−(q+1)²]=4q(V−1)`.

The exact difference is `(3−q)V−3(q+1)²+4q`, which equals −3 when q=2 and is **strictly negative for every q≥3**. Contradiction. Hence there is **no** thick equal-order original biregular girth-eight source with per-side Moore excess exactly 1.

This self-contained restriction is consistent with the classical nonexistence of even-girth excess-2 regular graphs (e.g. Biggs–Ito and follow-up literature; see [survey on cages](https://www.combinatorics.org/files/Surveys/ds16/ds16v3-2013.pdf) and [On a conjecture on the order of cages with a given girth pair](https://www.sciencedirect.com/science/article/pii/S0166218X15001699)). **Do not claim originality** of the general small-excess nonexistence; the actual contribution here is a short internally checked derivation using the same missing-projection matrix as the new T3 spectral gate.

An additional exact source degree divisibility gate always holds:

`(t+1)Delta_P=(s+1)Delta_L ⇒ Delta_L is divisible by (t+1)/gcd(s+1,t+1).`

For unequal parameters this excludes some positive excess values; it does **not** show that all small positive excess values are impossible.

**Connectivity from excess alone.** Every nonempty connected component of an actual biregular girth-eight incidence graph retains the SAME degrees and girth and must therefore contain at least `V_P0=(s+1)(st+1)` source points and `V_L0=(t+1)(st+1)` lines. Hence the number of connected components is at most
`min(floor(V_P/V_P0),floor(V_L/V_L0))`. In particular if `Delta_L<V_L0` (equivalently `Delta_P<V_P0`), connectedness is **forced** without any hidden GQ assumption. This applies automatically to every sufficiently large actual source with the fixed `Delta_L<=C*r^(3/2)` hypothesis, because `V_L0=Theta(r³)`. It does **not** by itself establish existence of any such source.

**Additional small-excess diameter gate.** If `Delta_L<=t` then ANY two original source points are at graph distance at most four: otherwise let p,q be an unconnected or distance≥6 pair of points. Any line through q reachable in three edges from p would append its incidence q and give a length-four p-to-q walk, contradiction. Thus all t+1 lines through q must be missing original projections from p, forcing `Delta_L>=t+1`, contradiction. Dually `Delta_P<=s` forces any two original lines to have distance at most four. Under BOTH conditions the original graph is connected and every point-to-line pair is at distance at most five (take any q on the target line ell, reach q within four edges, append q–ell); therefore its whole incidence graph has diameter at most five. This is only a **sufficient** bound, not an equivalence, and does not assert existence of positive excess.

The certificate implements these as **necessary integer parameter filters**, and separately verifies real connected/disconnected source components and distances using an **independently written literal incidence BFS**. It explicitly distinguishes a size bound from an actual graph-construction certificate. The doubled W32 source has two components and is not incorrectly declared connected; the cross-switched W32 double is connected but has an admissible component upper bound two, which is not mistakenly upgraded to a mandatory two components.

## 7. Evidence, previous work and strict STOP

- `research/gio_t3d_cubic_missing.py`: literal original B, independent F reconstructed via actual integer threewalk matrix, exact entire point+dual cubic matrix verification, centered integer Rayleigh `||F||²` checks; original source-owner conflict vs cubic spectral envelope under arbitrary lex/correlated typed f/g; fixed b,C exact square-root-free threshold gates and complete **FORMAL_ONLY** HEAVY/LOW closure; exact all-integer irreducible-cubic and trace nonexistence for Delta_L=Delta_P=1 in equal order.
- `research/test_gio_t3d_cubic_missing.py`: independent original triple nested 3path oracle, independent direct threewalk enumeration and centered quadratic forms, dual unequal s/t, positive-Moore-hole genuine connected non-GQ switched-double-W32, strict girth fail-closed switch, all-order spectral and moment constants, sharp `Delta_L²<=C²*r³` boundary, no-go in many q including arbitrarily large q.
- `.github/workflows/gio003-g6d-cubic-missing.yml`: GitHub-hosted specialist; exact certificate schema `mathlab.gio003.g6d1.cubic-missing-projection.v1`; standard stacked full Research and INDEX gates on **final HEAD**.

**Prior-art boundaries:** The degree/girth Moore bounds, bipartite cage/small-excess integrality and nonexistence, generalized quadrangles, and ordinary graph C6 supersaturation are not new. Relevant sources: [On biregular bipartite graphs of small excess](https://www.sciencedirect.com/science/article/pii/S0012365X19301232), [On bipartite cages of excess 4](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v24i1p40), [The size of bipartite graphs with girth eight](https://arxiv.org/abs/math/0102210), [Cage Problem survey](https://www.combinatorics.org/files/Surveys/ds16/ds16v3-2013.pdf), and [spectral Moore graph bounds](https://www.numdam.org/articles/10.5802/alco.71/). Exact cubic singular-polynomial relations also resemble classical excess-graph spectral polynomial techniques; novelty must not be asserted without a targeted broader literature comparison.

**STOP:** `Delta_L=O(r²)` remains OPEN; the new generic cubic estimate only gives a centered source collinearity spectral scale `O(r^(4/3))` and source conflict `O(r^(13/3))` there. Positive-excess non-GQ infinite realizability remains OPEN. Nothing here proves an arbitrary unbalanced source, arbitrary nonminimal factor alphabets, deterministic correlated GF(5) coefficients, complete unrestricted T3, or a new ASET exponent. No external independent referee or formal proof assistant certification. Keep #793 OPEN.

**Acceptance:** final HEAD specialist, INDEX and **all** full Research jobs SUCCESS; independent critical mathematical referee verifying the cubic matrix identity, exact centered norm argument, and the valid inherited HEAVY/LOW constant substitution; keep stacked Draft until these are true, and do not merge unrelated #800/#801 automatically.
