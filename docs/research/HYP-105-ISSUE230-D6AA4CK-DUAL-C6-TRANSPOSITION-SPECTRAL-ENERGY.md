# HYP-105 / #230 — AA4-CK: exact 60-dual-cycle transposition spectrum and true-original seven-GF5 local energy

**Scientific Draft**; strict child of [AA4-CJ / #610](https://github.com/definitely-stable/Mathlab/pull/610), pinned parent `91c8a3ac199979fb2a538607cc9c6d69488a151b`. Research-only additive files. No main, accepted GF5 weights/registry, or root verdict edits.

## Mathematical frontier and scope

Root issue #230 asks an all-h **fixed-original-map** universal lower `S_s(f,g)=Omega(s^6)` for EVERY arbitrary correlated globally injected typed map pair f,g, OR a genuine original infinite `S=o(s^6)` counterfamily, OR an exact root-qualified reduction. Root remains `OPEN_WITH_FORMAL_BLOCKER`.

AA4-BR/#589 ALREADY has classwise signed birth/death bookkeeping for global LINE transpositions; AA4-CJ/#610 has exact globally coupled all-seven POINT swap source-sector flux (sign indefinite; W32 witnesses both signs); AA4-CI/#609 has exact 720-legal-complete-POINT-map historical seven-GF5 score for ONE fixed TRUE original six-POINT-factor source-A fiber. The new unresolved **quantitative** local question: does a NONCONSTANT right original six-incidence-column dual histogram FORCE a positive amount of squared historical GF5 signed POINT-swap fluctuation, independently of arbitrary cross-map correlations?

Here the answer is YES with exact sharp **abstract spectral** bounds `4/3`, `16/5` and contraction `3/5`. The original-W3 application is proven for every h>=1, but concerns one actual source POINT-A fiber, not full S_s. Basic Schreier graphs, S6/D6, representation theory and spectral Poincaré inequalities are classical and NOT claimed as new general mathematics. The project's incremental result is the exact integer-certified 60-state spectrum and transfer to the HISTORICALLY ACCEPTED same-six-distinct-original-incidence GF5 weighted numerator under truly GLOBAL source image swaps, without independent Q redraw.

## 1. Original all-h genuine W3 source-fiber model

For EVERY dyadic s=2^h, h>=1, genuine symplectic `W(3,s)`, ANY complete globally injected POINT f / LINE g (arbitrarily correlated), and SIX distinct TRUE ORIGINAL POINT-factor IDs `P=(p0,...,p5)` whose six occupied physical f images form one connected SIX-coordinate C6, let `F_P` consist of ALL `(s+1)^6` TRUE original six-DISTINCT-incidence-ID Q choosing exactly one actual incidence from each p in P. The original incidence Q is identical on left/right; original g and ALL other source f maps remain complete and unchanged.

AA4-CI established EXACTLY the historical accepted all-seven weighted numerator on this POINT source A fiber, for each of the 720 globally injected complete f-image permutations:
```text
T(C)=B+5643 H(C), B=45600*N_B+43320*N_C.
```
Here H(C) counts actual same-six-incidence-ID right-source-A original Q whose six physical right LINE edges form a connected C6 with right **original incidence-position** dual equal to C; C is one of exactly 60 **undirected labeled Hamiltonian 6-cycles** on the source position labels 0..5. B is a real fixed-g constant from historical positive source-right B/C classes; it is not an upper physical surrogate. The other four historical classes cannot occur on original POINT-source A. Every labeled C arises on exactly 12 of 720 globally legal POINT physical image permutations.

Now select ONE of 15 pairs `0<=i<j<6` of original POINT factors and swap their WHOLE physical edge images in the fully completed actual original f. On the source dual, this is exactly the single label transposition `tau_{ij}` of C. Thus every `C -> tau C` counted below corresponds to an ACTUAL, complete, globally injected original POINT map transition at unchanged original LINE g (and unchanged source incidence Q). The 60×15 distribution is an exact uniform count of 900 directed cycle/tau states, equivalent to 720×15 with each of 60 cycles repeated 12 times. There is no assumption of independently varying original point sixsets.

## 2. Exact integer spectral theorem for the classical 60-state Schreier graph

Let `A_{C,D}=#{unordered transpositions tau in S6: tau C=D}`. Then:

- A is a real symmetric **60×60 integer matrix**, zero diagonal, each row sum exactly15.
- Every cycle has **12 distinct** neighboring labeled cycles: 9 adjacency entries 1 and 3 entries 2 (9+2·3=15).
- Of all 900 directed (C,tau), 720 transformed cycles share exactly FOUR labeled source-position edges with their former cycle; 180 share exactly TWO.
- The EXACT **integer matrix annihilator** is `(A−15I)(A−5I)A(A+3I)(A+9I)=0`.
- The five independently computed integer power traces `tr(A^k)`, k=0,..,4, are **(60,0,1260,1440,96300)**. Since A is symmetric and the annihilating polynomial has five distinct real integer roots, A has no other eigenvalues. The five Vandermonde trace equations uniquely force eigenvalue multiplicities:

| Adjacency eigenvalue A | Multiplicity | Laplacian `L=15I−A` eigenvalue |
|---:|---:|---:|
| 15 | 1 | 0 |
| 5 | 18 | 10 |
| 0 | 16 | 15 |
| −3 | 20 | 18 |
| −9 | 5 | 24 |

The certificate and multiplicity derivation are implemented with exact Python `int` matrix arithmetic and `Fraction` elimination only: **no numerical floating-point eigenvalue approximation and no unverified appeal to general prior literature**. Graph connected because the nullspace of L has dimension1; the nonconstant Laplacian spectrum lies EXACTLY in [10,24]. The row-averaged swap operator `P=A/15` has largest nonconstant absolute eigenvalue `9/15=3/5`; spectral gap is `10/15=2/3`.

## 3. NEW all-h true-original historical GF5 squared POINT-swap flux inequality

For the actual fixed original six-source-POINT fiber define mean, variance and the **mean squared one-global-whole-factor POINT-image-swap GF5 change**:
```text
F(C)=B+5643 H(C)
Fbar=(1/60)*sum_C F(C)
Var(F)=(1/60)*sum_C (F(C)-Fbar)^2

D(F)=(1/(60*15))*sum_C sum_{tau one source POINT swap}
                         (F(tau C)-F(C))^2.
```
Then `D(F)=2/(60*15) * <F,(15I-A)F>` and the exact integer Laplacian spectrum gives:

```text
                 4/3 * Var(F) <= D(F) <= 16/5 * Var(F).
```

Moreover the **conditional single-swap averaging operator** obeys:
```text
Var(PF) <= (3/5)^2 * Var(F) = 9/25 * Var(F).
```

Both constants `4/3` and `16/5` (also `3/5` contraction) are SHARP for unrestricted real functions on the 60 labeled-dual-cycle graph because the exact corresponding nonconstant eigenspaces have multiplicities 18,5,5. **No claim that arbitrary sharp eigenfunctions are realizable as TRUE ORIGINAL nonnegative W3 original-Q dual histograms**; the universal inequalities nonetheless apply to EVERY such genuine-original histogram H because they hold for all real functions.

The consequence `H` nonconstant ⇒ `D(F)>0` is a genuine quantified **conditional global-orbit variability** theorem: positive and negative historical signed changes exist somewhere among these whole-source-POINT map transitions because every swap edge has its inverse in the same 60×15 ensemble. It does NOT assert a beneficial swap at an arbitrary fixed original f; nor does it measure or bound signed flux of OTHER intersecting genuine POINT-source fibers or the entire original root `S_s(f,g)`.

## 4. Sharp all-h named original AA4-CH D6 fan control

For the AA4-CH genuine all-h original fan of `m=s+1` different TRUE source-Q D6-positive sixflags sharing four real incidence IDs, all `m` right dual cycles are one fixed original C0. Restricting to exactly those m original Q, NOT the whole POINT source fiber:
```text
H(C0)=m, H(C)=0 for C != C0, B=0.
Var(T_named)=5643^2 * m^2 * 59 / 3600.
D(T_named)=5643^2 * m^2 / 30.
D/Var=120/59.
```
Exactly 15 directed swaps from C0 LOSE all m named D6s, exactly 15 directed swaps into C0 GAIN them, and the other 870 of 900 directed dual graph edges leave the named score unchanged. Actual W34 and W38 true-original original incidence flag Q and full 720 legal f maps independently verify the named fan multiplicity. This explicit ratio lies strictly between 4/3 and 16/5; it does NOT demonstrate spectral endpoint sharpness in the original-source model.

## 5. Independent hosted exact original W32/W34/W38 proof falsifiers

1. The full integer 60×60 adjacency is constructed from **60 independently enumerated six-position cyclic graphs** and every one of the 15 literal label transpositions. Check symmetric, 15-regular weighted, 12 distinct neighbors with weights9×1,3×2, no self-loops, 720/180 overlap counts. Compute P(A)=ZERO **entry by entry**, all five integer traces, exact rational eigen multiplicities; reject malformed transpositions, invalid cycle histograms and negative weights.
2. Authentic original W32 (h=1) `lex` and `S72`: choose six real POINT source factor IDs whose complete globally injected f physical images are C6. Independently enumerate actual `3^6=729` true source sixflag Q, build the whole original right-A/B/C dual histogram, then for each of 60 cycle representatives and 15 transpositions (900 actual legal globally injected complete-original POINT factor map transitions) evaluate **the historical sevenclass classifier on the actual original Q**. Direct original historical scores are compared with independent spectral F(C) and `D(F)`.
3. Authentic original W34 (h=2,V85) and W38 (h=3,V585) use AA4-CI's mixed right-source B/C/D6 fully globally injected complete original fixture. W34 has B/C invariant historical baseline403560 and right A/C6 histogram supported at one dual; W38 has baseline1087560, 32 true original right A/C6 Q across 13 labeled dual cycles. For EACH of 60 dual representatives ×15 WHOLE-original-POINT transpositions, recompute the 7GF5 historical Q classifier independently, compare direct squared delta sum (900 maps) to exact spectral matrix evaluation.
4. AA4-CH real original W34/W38 named fan with m=5 or9 true six-incidence IDs independently checks all-h symbolic variance `5643² m²·59/3600`, squared drift `5643² m²/30` and ratio120/59.

These are finite ORIGINAL source-Q falsifiers; they do not replace the algebraic all-h proof. All claims refer to exactly one chosen source POINT-A fiber or a named fan; all globally different complete f^π operate on the SAME source original Q and unchanged full g. No ambiguous independence or MCMC extrapolation.

## 6. What this does NOT prove; next frontier

**Not root Branch A/B/C**. Even though `D(F)>0` iff the dual histogram is nonuniform, this is an orbit-averaged **squared** difference, not a guaranteed nonnegative signed improvement from a given fixed f, nor a lower bound for the **entire** original selected all-seven `S_s(f,g)`. Generic signed flux identity already prior AA4-BR/#589; true original global POINT-sector signed ledger already AA4-CJ/#610. The new exact spectral energy theorem does **not** supersede or contradict either prior result. Abstract S6/D6 Schreier spectrum is classical group-theoretic material, project novelty is its exact integer certificate and application to real original GF5 selected seven-positive source Q.

**Mathematically useful next gate**: couple energy/mixing across MULTIPLE intersecting actual original POINT-source-A six-POINT fibers under ONE global f transposition, or bound the unequal-source sector contribution of AA4-CJ, proving a genuine fixed-map forced gain/lower bound or constructing all-h true-original correlated counterfamilies. The local 60-state spectral gap alone cannot justify treating distinct source-point families as independent or assert global `Omega(s^6)`.

Retain scientific Draft pending final exact HEAD CI, independent qualified mathematical reviewer and acceptance/ancestry gate. No changes to main or accepted registry.
