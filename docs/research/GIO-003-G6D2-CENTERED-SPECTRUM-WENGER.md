# GIO-003 / G6-D2 — centered missing-projection spectrum, quadratic-excess T3 and a *real infinite* Wenger family

**Primary issue:** [#793](https://github.com/definitely-stable/Mathlab/issues/793). **Stacked prerequisite:** [G6-D1 #805](https://github.com/definitely-stable/Mathlab/pull/805), exact reviewed HEAD `0f0d4b5f76373a00513d9085ee5d3cfa011d5c0f`; its G6-C3/C2/C1 proofs are imported with quantifiers intact. No source flag completion, GQ source axiom, field assumption or GQ edit witness is made in the **general** new theorem.

**Status design:** There are TWO separate sufficient routes, not interchangeable:
(A) a directly certified centered operator norm `||F0||² <= kappa r³` (the **main** quadratic-excess theorem, applies to the infinite Wenger W₂(q) family);
(B) a stronger sixth-moment certificate `S6(F) <= M r⁹` (elementary and source-verifiable, **does NOT hold uniformly** for the Wenger family). Never report (B) as automatic from degree or as necessary for the theorem.

## 1. Original source setup and the centered cubic identity

Let `I⊆P×L` be ANY ACTUAL finite simple thick (s,t)-biregular incidence source of girth≥8 (no C4/C6), with original point-line biadjacency B. Every original nonincident (p,ell) has at most one 3flag source path. Set `F[p,ell]=1` if and only if the original nonincident pair has **none**; else F[p,ell]=0. No GQ source projection completeness is presumed.

Write `V_P=|P|`, `V_L=|L|`,
`Delta_L=|L|-(t+1)(st+1)`,
`Delta_P=|P|-(s+1)(st+1)`,
`(t+1)Delta_P=(s+1)Delta_L`.
G6-D1 independently proved the literal point-line cubic

```
   BB^T B - (s+t)B = J_PL - F,                 (1)
   T(T-(s+t)I)^2 = FF^T + (|L|-2Delta_P)J_PP, T=BB^T. (2)
```

and the exact dual for `U=B^TB`. F is original rectangular, 0/1, regular by rows and columns, and row(F)=Delta_L, col(F)=Delta_P. The full operator norm `||F||²=Delta_L Delta_P` includes the trivial all-ones singular vectors; **we do not use this full norm in G6-D2**.

Let `alpha=Delta_L/V_L=Delta_P/V_P` and let

```
F0 = F - alpha*J_PL,
K  = FF^T,
H  = K - (Delta_L*Delta_P/V_P)*J_PP = F0 F0^T.
```

The equalities are entrywise exact (use F J identities from its row/column sums). H is symmetric **positive semidefinite**, satisfies `H*1=0`, and its nonzero eigenvalues are precisely the SQUARED nontrivial singular values of F. Note the distinction from the old G6-C1 defect D, which is entrywise nonnegative but can be indefinite; no PSD property of D is inherited.

For any centered eigenvalue x≥0 of T (whether source connected or not), (2) gives

```
x(x-s-t)^2 ≤ ||F0||².
```

**Direct quadratic spectral condition.** If `||F0||²<=kappa*r³` with fixed `kappa>=0`, then for x≥2(s+t), x³/4<=kappa*r³, and for smaller x the other branch is immediate. Therefore

`0<=x<= [2(s+t)+ceil_cuberoot(4kappa)*r]`.

Since original point/line collinearity adjacency is `T-(t+1)I` / `U-(s+1)I`, for fixed balanced max(s,t)≤b*r both original typed nontrivial collinearity spectra are bounded by

`Lambda0*r` with `Lambda0=5b+1+ceil_cuberoot(4kappa)`.

This is an **additional structural condition** on F, not a consequence of girth plus `Delta_L=O(r²)` in the present work.

## 2. All-source conditional quadratic-excess T3 (direct centered spectrum)

Fix three integers b≥1, C≥0, kappa≥0 **BEFORE** choosing a source, factor maps, deletion mask or family. Let `r=min(s,t)`, `max(s,t)≤br`, and assume

```
          0<=Delta_L<=C*r²,
          ||F0||²<=kappa*r³.                    (3)
```

The fixed-C quadratic excess still gives `V_P,V_L=O_(b,C)(r³)`, `N=O_(b,C)(r⁴)`, minimal factor-alphabet sizes `aP,aL=O_(b,C)(r^(3/2))`, and original missing-projection endpoints exactly `4V_P Delta_L=O_(b,C)(r⁵)`. The fixed-kappa centered spectral bound above and the already **exact original-source symbol-fibre expander-mixing argument** from G6-C1 now give

```
 e_col,P(f),e_col,L(g), e(original owner J) = O_(b,C,kappa)(r⁴),
 G_f,G_g=O_(b,C,kappa)(r^(11/2))
```

for **every** pair of arbitrary, complete, separately globally pair-injective MINIMAL typed physical factor maps `f:P->binom([aP],2)`, `g:L->binom([aL],2)`. They may be adversarially correlated with each other and the source. The Gram uses the exact negative correction `-Σu_x^T D u_x`, dropped only for actual NONNEGATIVE indicator u_x; it does not assume D PSD.

**Every part of the accepted original-source HEAVY/LOW argument in G6-C3** (same single global original owner priority / global x,y cuts, actual physical HEAVY ordinary C6 supersaturation, FULL surviving A and CORE C mixed book, strict original triple-to-book blocker injection, partial original projection inverse) uses only these source bounds, original 3st projection load, and original missing endpoint count. The G6-D2 ledger recomputes the exact b,C,kappa-dependent integer envelopes and fixes `rho,delta,r0` LAST. Its new finite endpoint mask includes **`4V_P Delta_L ≤4v0 C*r⁵`**, not an unproven o(r⁵). The four LOW errors remain separately bounded by eps*r⁶:

```
improper:         3 T Q0*r⁵,
clean endpoints:  E*r^(11/2),
deleted anchors:  q3 sqrt(12 b² rho L6)*r⁶,
four inner masks: D*r^(47/8).
```

The actual proper 3walk selector has W3>w*r⁶ and the four errors total≤w*r⁶/2, so the original **actually produced** aligned historical six-ID BBo sixsets number>w*r⁶/4. HEAVY yields historical original six-ID D6 ≥c0 r⁶/R⁶ through the **published ordinary graph** C6 supersaturation theorem. One gets the following theorem:

**Theorem T3-Q(`b,C,kappa`).** With the fixed b,C,kappa structural gates (3), for any sufficiently large ACTUAL girth≥8 biregular source I, every legal minimal complete f,g and every adversarial original source flag deletion `Z` with `|Z|<=rho r⁴`,

```
    D6_(I\Z)(f,g) + BBo_produced,(I\Z)(f,g) >= delta*r⁶,
    rho= rho_(b,C,kappa)>0, delta=delta_(b,C,kappa)>0.
```

The constants also depend on the published ordinary-graph C6 supersaturation theorem's existential positive constants. We DO NOT fabricate their numeric values: all sample exact rational ledgers `C0=c0=1`, etc. remain **FORMAL_ONLY**. No new unrestricted ASET exponent or dependent-GF5 coefficient result is claimed.

The *main* spectral gate can be checked without eigensolvers or numerical tolerance: given ACTUAL F, compute integer common-missing-projection codegrees `K[p,p']=#{ell: F[p,ell]=F[p',ell]=1}`; form the exact rational symmetric centered Gram `H=K-(Delta_L Delta_P/|P|)J`. Then `||F0||²<=kappa r³` is EXACTLY equivalent to the rational PSD inequality

```
    kappa*r³*I - H >= 0.
```

A rational Schur-complement elimination certifies this with strict zero-pivot checks; separately `max_p Σ_{p'} |H[p,p']| <= kappa r³` is a sufficient (often weaker) purely combinatorial L1 codegree criterion by the symmetric row-norm bound. Neither of these requires a complete GQ source projection table. Finite exact PSD checks **never substitute for the universal algebraic proof**; they only verify specific sources.

## 3. A natural but STRICTER sixth-moment certificate, and its optimal bulk scaling

The original typed missing-projection bipartite graph `F` has

```
tr((FF^T)^3) = sum_(p,q,u in P) K[p,q] K[q,u] K[u,p],
```

the exact number of closed length-six walks in the missing-projection graph rooted at a point. The dual line-rooted count agrees by rectangular matrix algebra. The principal all-ones mode of `FF^T` has eigenvalue `Delta_L Delta_P` and is removed exactly once. Define **the nonnegative integer**

```
 S6(F)= tr((FF^T)^3) - (Delta_L Delta_P)^3
      = sum_(j>=2) sigma_j(F)^6.
```

Thus

```
  ||F0||^6 <= S6(F).
```

For fixed M≥0, `S6(F)<=M*r^9` is a **SUFFICIENT** condition for the direct gate with `kappa=ceil_cuberoot(M)`. This yields a second conditional quadratic-excess T3 with `b,C,M` fixed before the family. The code independently checks both typed rooted sixwalk counts and exact rational PSD certificates. The sixth moment is **NOT automatically bounded** just because F has regular rows/columns and `Delta_L=O(r²)`.

The moment scale r⁹ is near the minimum permitted by the bulk singular values: the exact sum of SQUARED nontrivial singular values equals

```
 S2(F)=tr(FF^T)-Delta_L Delta_P
      =|P| Delta_L-Delta_L Delta_P
      =Delta_L(|P|-Delta_P).
```

With at most `|P|-1` such eigenvalues, power-mean/Hölder gives the exact lower bound

```
    S6(F) >= S2(F)^3/(|P|-1)^2,
```

and its point-line dual. When `Delta_L~r²` and `|P|~r³`, this lower bound has order r⁹; hence the sufficient S6 scale is a **bulk-optimal lower-order threshold**, albeit a much stronger requirement than the direct operator cap.

**Critical limitation discovered below:** known natural Wenger graphs do **not** satisfy any fixed-M bound `S6(F)=O(r⁹)` although they DO satisfy the required `||F0||²=O(r³)`. Therefore the sixth-moment route is *not* the default recommended gate for full quadratic-excess classification.

## 4. The main scientific improvement: real infinite non-GQ Wenger W₂(q)

**Published prior art, explicitly credited:**
- **S. M. Cioabă, F. Lazebnik, W. Li**, *On the Spectrum of Wenger Graphs* (2014), [published preprint PDF](https://bpb-us-w2.wpmucdn.com/sites.udel.edu/dist/3/7714/files/2022/03/WengerSpectrumJCTBp.pdf), [arXiv 1402.3341](https://arxiv.org/abs/1402.3341). Their **Theorem 2.1** supplies the COMPLETE original Wenger graph spectrum and eigen multiplicities.
- The Wenger construction, its girth, connectivity, its monomial model `W'_2(q)`, and its embedding as an induced subgraph in the classical `Q(4,q)` GQ are **KNOWN mathematics**. None is presented as Mathlab's original discovery.
- Also relevant: **Camino Balbuena**, *Small regular bipartite graphs of girth 8* (DMTCS), [full paper](https://dmtcs.episciences.org/articles/461/download), provides another infinite near-cage construction. We use the readily reproducible **Wenger** model and its exact published spectrum here.

Let q≥3 be a prime power. The published Wenger graph `W_2(q)` has point and line parts both `F_q^3`, q edges at every point and line, connected original incidence graph of girth eight, and no hidden source GQ **axiom**. It *is* a known induced subgraph of the incidence graph of Q(4,q), so claims that it lacks a geometric embedding would be FALSE. Our general theorem DOES NOT REQUIRE or USE that embedding, but the existence and spectrum of this family use published work.

For `s=t=q-1`, `r=q-1`, `|P|=|L|=q³`, its original missing-projection excess is

```
 Delta_L=Delta_P=q³-q((q-1)²+1)
                =2q(q-1)=2r(r+1),
 0<Delta_L<=3r² for all q>=3.
```

So **b=1,C=3** are fixed, the excess is genuinely asymptotically `Theta(r²)`, and this is a TRUE infinite non-GQ positive-excess family **OUTSIDE** the old fixed-`Cr^(3/2)` domain for arbitrarily large q. Prime powers q→∞ provide an infinite sequence of ACTUAL sources.

The published eigenvalues of the full bipartite graph `W_2(q)` are `±q, ±sqrt(2q), ±sqrt(q), 0`. Thus the point matrix T=BBᵀ has principal eigen `q²` and centered eigenvalues `0,q,2q`. G6-D1's **original cubic source identity** on centered eigenspaces gives exact nontrivial F squared singular levels

```
       x*(x-2(q-1))² =
        0                 when x=0,
        q*(q-2)²          when x=q,
        8q                when x=2q.
```

Both positive levels actually occur for every prime power q≥3. Consequently

```
   ||F0||² = max(q(q-2)²,8q) <=3(q-1)³.
```

The two **all-integer checks** are

```
 (q-1)³-q(q-2)² = (q-1)²+(q-1)-1 >0,
 3(q-1)³-8q = (q-3)*(3(q-1)²+6(q-1)+4)>=0.
```

Thus **kappa=3 is an actual fixed global operator certificate** for the entire known Wenger family. No S6 bound is needed. We now have a concrete **nonvacuous infinite** corollary to the quadratic theorem, rather than merely a theorem about a possibly empty nonGQ class:

**Corollary WENGER-T3.** For every sufficiently large prime power q, put r=q−1 and take the ACTUAL original `W_2(q)` flags with ANY complete minimal separately pair-injective f/g (no random labels), and adversarial original Z with |Z|≤rho*r⁴. With b=1,C=3,kappa=3 fixed, and positive constants rho,delta determined by the external existential ordinary-graph C6 theorem, the historical original six-named-ID obstruction satisfies

```
         D6_(W_2(q)\Z)(f,g)
       + BBo_produced,(W_2(q)\Z)(f,g)
                 >= delta*(q-1)^6.
```

The source is **not itself a GQ**, although it has a known larger-GQ embedding; our proof is intrinsic to its actual named flags, and never imports any nonexisting projection anchor from its ambient Q(4,q).

### 4.1 Why sixth moment alone would miss Wenger

Using the PUBLISHED m=2 eigen multiplicities, T has multiplicity `m1=2q(q-1)` at x=q, and `m2=q(q-1)²/2` at x=2q. Hence the EXACT original centered-missing sixth moment is

```
S6(W₂(q)) = 2q(q-1)*[q(q-2)²]^3
           + (q(q-1)²/2)*(8q)^3.
```

The first term has leading order `2q^11`, so `S6(W₂(q))=Theta(q^11)`, whereas `r⁹=Theta(q⁹)`. The ratio grows like `Theta(q²)` and no fixed M can satisfy `S6<=M*r⁹` along this family, despite the **uniform exact** bound `||F0||²<=3r³`. This is a concrete proof that the moment hypothesis is **too strong to be the primary route**.

The general quadratic spectral theorem and the real Wenger application are therefore the primary G6-D2 result. The sixth moment becomes a secondary sufficient certificate for other specially balanced missing-projection structures.

## 5. Exact finite oracles and external-source separation

- `research/gio_t3d2_centered_sixth.py`: exact original point+line missing F matrices and centered S6 via independent closed-walk traces; centered rational Gram H, exact rational Schur-complement PSD (zero pivot with nonzero cross FAILS), exact smallest *integer* kappa for actual finite sources, and a separate L1 common-missing-codegree certificate. It does not run a floating eigensolver and does not fabricate a GQ projection.
- The same file contains **fully separate** fixed-b,C,M sixth-moment and fixed-b,C,kappa direct-spectral all-error HEAVY/LOW ledgers with explicit original `4|P|Delta_L` error of order r⁵ and actual projection load 3st. rho,delta,r0 are chosen only after all source and selected-moment constants. All sample numeric external C6 theorem inputs are tagged FORMAL_ONLY.
- A prime-field **actual W'_2(q)** source builder uses the published monomial representation: points (a,b,c), lines [u,v,w], incidence `v+b=u a` and `w+c=u a²`. The paper proves the W'_2(q) model is isomorphic to W₂(q). We implement the field modulo q **ONLY for prime q**; do not treat integer mod 4 or mod 9 as a field. The all-prime-power theorem follows from the published finite-field family and spectral theorem, NOT from illegally using Z/4.
- Literal independent line-first polynomial incidence, actual original degree/girth/projection builder and exact published point polynomial `T(T-qI)(T-2qI)=q(q-1)(q-2)J` are tested on **true q=3 and q=5 Wenger sources**. Their exact ORIGINAL missing-F sixth and second moments agree with the published spectral multiplicities; q=3's exact `kappa=3` is checked independently with rational PSD.
- GQ W32/W33 and unequal GQ(2,4) + dual, disconnected doubleW32 and connected switched-doubleW32, lex/correlated minimal f/g maps, exact original historical collinearity conflict and corrected Gram bounds, zero/nonzero missing projection, synthetic **non-incidence** 0/1 block-biregular F adversarial countermodels, all present. The synthetic block mask proves mere regularity of F does not force the centered norm: its balanced block-sign mode has `||F0||²>=q⁴`, violating any uniform `O(q³)` gate, but **we explicitly DO NOT claim** this synthetic F arises from a valid near-Moore girth8 incidence source.
- `research/test_gio_t3d2_centered_sixth.py`: independent incidence-first F and closed 6walk censuses, PSD and previous integer kappa−1 failure, independent published Wenger line-first oracle, fixed symbolic b,C,kappa spectral gate and all four LOW errors, exact Jensen lower bound, Wenger sixth-moment failure, no false full unrestricted T3 claim.
- `.github/workflows/gio003-g6d2-centered-sixth.yml`: GitHub-hosted specialist test + JSON artifact, ordinary PR Research + INDEX are separately required exact HEAD.

**Scientific STOP:** No theorem for ALL quadratic-excess sources without additional centered spectral condition, no `O(r²)` extension to arbitrary biregular girth≥8 graphs, no automatic centered singular gap from degrees alone, no newly discovered Wenger graph/field construction/eigenvalues, no claim that the known Wenger induced GQ embedding does not exist. No independent external human referee, formal Lean, numerical published ordinary-graph C6 constants, dependent-GF5 theorem or unrestricted ASET exponent. Keep [#793](https://github.com/definitely-stable/Mathlab/issues/793) OPEN, stack Draft until all exact-head CI green and internal critical review; do not merge unrelated PRs.

**Next frontier G6-D3:** find intrinsic incidence-graph conditions (not simply a relabeled spectral gate) forcing `||F0||²=O(r³)` for a broader actual quadratic-excess source class; investigate known near-cage constructions (including Balbuena and Wenger) with rigorous cited spectral/combinatorial estimates, and whether the generally unrestricted T3 can be approached by replacing a worst-eigenvalue conflict bound with aggregate fibre-energy or a low-rank exceptional-mode decomposition.
