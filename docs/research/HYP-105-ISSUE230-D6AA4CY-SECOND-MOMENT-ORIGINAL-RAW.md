# HYP-105 / issue #230 — AA4-CY: genuine ORIGINAL GQ second moment forces Ω(s^(11/2)) raw-positive nonincident paths

**SCIENTIFIC DRAFT, PARTIAL ALL-h THEOREM — NOT root Branch A/B/C.**
Strict child [AA4-CX PR #624](https://github.com/definitely-stable/Mathlab/pull/624), frozen parent HEAD `285dc6ba2815102599aa14978ec6b6c2b79c9a92`. Prerequisite all-cut raw original spoke SOURCE flag first moment [AA4-CW PR #623](https://github.com/definitely-stable/Mathlab/pull/623); previous per-anchor spectral bound/physical doubled-factor exclusions [AA4-CX #624](https://github.com/definitely-stable/Mathlab/pull/624), and positive original physical C4→true source 3×3 matching requirement [AA4-CR #618](https://github.com/definitely-stable/Mathlab/pull/618). No accepted GF(5) seven-class or main modification.

## 1. Exact target, every h and arbitrary fully correlated physical f,g

Take genuine W(3,s), s=2^h, h>=24, V=(s+1)(s²+1) original point and V line factors, original incidence matrix M∈{0,1}^{V×V}, degree d=s+1 and nontrivial singular value sqrt(2s). Fix ONCE arbitrary globally injected full typed ORIGINAL POINT mapping f and LINE mapping g into unordered coordinate pairs of the SAME minimal physical K_a, a=min{t:binom(t,2)>=V}. No independence or local re-embedding. Choose ANY two physical coordinate cuts X,Y each of cardinality k=floor(a/2).

Set P_X={p true original POINT: f(p)⊂X}, L_Y={l true original LINE: g(l)⊂Y}. Let A_f be the V×V real symmetric adjacency on ORIGINAL POINT factor IDs: `A_f[p,i]=1` iff p≠i are both in P_X and physical pair labels f(p),f(i) overlap at a physical coordinate. Similarly A_g on the V ORIGINAL LINE factors in L_Y. These are **induced line graphs of the occupied physical simple K_k pair edges**, not the original geometric GQ incidence matrix.

The AA4-CW RAW true source spoke count is EXACTLY

```
C=A_f M A_g^T,
C[p,l]=#{(i,j) GENUINE ORIGINAL INCIDENCE ID:
           i∈N_f^X(p),j∈N_g^Y(l), M[i,j]=1}.
```

Every original p∈P_X,l∈L_Y with p NOT source incident l is a unique genuine ORIGINAL THREE-INCIDENCE-ID path p--l0--q--l (from GQ projection). C[p,l]>0 does **NOT** mean a physically occupied C4, original 3×3 perfect matching, or a positive historic six-original-flag GF(5) B/B-overlap Q.

**NEW Theorem AA4-CY.1 (all h>=24, ALL true original W(3,2^h), ALL fully correlated complete typed f,g, ALL physical halfcuts X,Y):**

```
T := sum_(p∈P_X,l∈L_Y) C[p,l]
   >= k²*d*V/512.                                          (CY.1)

Q := sum_(p∈P_X,l∈L_Y) C[p,l]²
   = ||A_f M A_g^T||_F²
   <= 32*d²*k⁴ + 32*s*V*k³
   <= 64*s*V*k³.                                            (CY.2)

N_RAW_POS := #{(p,l)∈P_X×L_Y:
                p NOT original incident l, C[p,l]>0}
   >= d²*V*k/(2^24*s) - V*d
   >= s*V*k/(2^25)
   > s^(11/2)/2^26.                                        (CY.3)
```

The power **11/2** improves AA4-CX's **5** and is a true many-anchor nonincident original 3path estimate for arbitrary global correlated maps. Only RAW spoke-original flag positivity is proven; no root #230 all-seven score transfer.

## 2. Proof of the NEW upper bound on the WHOLE true-original second moment

**Original source geometry and spectral decomposition.** By true generalized quadrangle point/line incidence regularity and the classical strongly regular point graph spectrum, write exactly

```
M = (d/V) 1 1^T + E,
||E||_op = sqrt(2s).                                       (CY.4)
```

There are no physical graphs or random source IDs in M. The complete original GQ incidence set contains exactly Vd immutable flags, used unchanged in both calculations.

**Physical line-graph adjacency bounds.** A physical edge of simple K_k is adjacent to at most 2(k−2) other distinct K_k pair edges. Therefore (since A_f,A_g are symmetric, nonnegative and padded by zeros outside cuts)

```
||A_f||_op, ||A_g||_op <= 2(k−2) <= 2k,
||A_f||_F², ||A_g||_F² <= 2kV,
||A_f 1||², ||A_g 1||² <= 4k² V.                           (CY.5)
```

These deterministic facts hold for EVERY fully complete original pair embedding, including adversarially missing physical pairs. They do not require f,g independent or a distribution on embeddings.

Decompose `C=C_main+C_res` as

```
C_main=(d/V)(A_f 1)(A_g 1)^T,
C_res=A_f E A_g^T.
```

Using genuine original singular-spectrum control and mixed Frobenius/operator inequalities,

```
||C_main||_F² <= (d/V)² * (4k²V)² = 16d²k⁴;
||C_res||_F² <= ||A_f||_F² ||E||_op² ||A_g||_op²
             <= (2kV)(2s)(4k²)=16sVk³.
```

The elementary inequality `||B+D||_F²<=2||B||_F²+2||D||_F²` yields CY.2's first inequality. The elementary dyadic minimal-physical-alphabet bound `a−2 < 3s^(3/2)/2` for s>=16 implies k < s²/4 for s>=16; also d²<2s². Hence `d²k < sV` for all s>=16 (since V>s³), producing CY.2's second inequality. These are classical linear-algebra estimates applied to genuinely original GQ source M and two physical pair-overlap graph adjacencies.

**Original source RAW first moment, inherited independently.** AA4-CW proves for ALL h>=24 a lower `T>=k²*d*V/512` by charging physical missing-coordinate heavy vertices and genuine original source GQ expander mixing. It explicitly preserves one global f,g and all actual immutable source incidence IDs. CY.1 is a reused parent result, not a new independent theorem.

**Cauchy–Schwarz original support.** Since C has NONNEGATIVE INTEGER entries,

```
T² = (sum_{C[p,l]>0} C[p,l])²
    <= #{C[p,l]>0} * Q.
```

Combining CY.1 and CY.2,

```
#{C>0}>= (k⁴ d² V²/512²)/(64 s V k³)
         = d² V k/(2^24 s).
```

At most Vd original endpoint pairs are SOURCE INCIDENT and thus not eligible true P3 anchors. Discarding all of them gives the first CY.3 bound. For all h>=24, `k s >= 2^25 d` from k>0.5s^(3/2), s>=2^24; thus `Vd<= sVk/2^25` and `d²>=s²` imply the second bound. Moreover `V>s³` and k>0.5s^(3/2) produce the strict third bound.

All quantifiers are FOR ALL h>=24, for ALL adversarially correlated complete typed original f,g, for ALL X,Y. Checking h1..34 integers is a falsifier, **not** a proof by interpolation.

## 3. Exact new original SOURCE four-flag second-moment identity (independent oracle)

Define real true original source cut flags
`F_XY={(i,j) ORIGINAL incidence ID : i∈P_X,j∈L_Y}`. For each true original POINT factor i in P_X, its physical in-cut spoke-neighbor set N_f(i) is defined by ORIGINAL source factor IDs, similarly N_g(j). Reversing two sums gives a second *exact* identity

```
Q = sum_((i,j),(i',j')∈F_XY TRUE ORIGINAL flag IDs)
      |N_f(i)∩N_f(i')| |N_g(j)∩N_g(j')|.                 (CY.6)
```

This is a **PAIR-of-TWO-GENUINE-original-incidence-flags** identity; it is not the six-flag or seven-family GF(5) model reduction, and no 3×3 matching appears. It provides an independent falsifier against silently counting synthetic source incidences or undercounting strongly correlated physical overlaps.

## 4. Quantitative negative transfer, unchanged research gate

AA4-CX proved that the original nonincident P3 anchors failing either physical doubled-image disjointness condition in fixed X,Y can be as numerous as `O(s^(11/2))` by a rigorous upper bound `N_bad<=4(a−2)sV`. This has exactly the SAME power of s as CY.3 (and its worst-case coefficient exceeds our positive constant). Therefore subtracting physical bad anchors still **DOES NOT** guarantee any positive RAW surviving double-disjointness for all f,g. Even once a real double-disjoint source path survives, deleting up to four raw-spoke original source factor images on each side can remove at most 8d true original crossing incidences but could erase every cross-flag. Even a surviving SAFE original flag is not two actual occupied physical C4s plus the other two original flags needed for a perfect 3×3 SOURCE matching.

Thus we do NOT infer historical original `U_BB-overlap>0` or any positive seven-class score, root Branch A/B/C, strict R3 or ASET exponent. No false transfer to an original six-incidence-ID Q.

## 5. Source credit and independent exact PR-HEAD validation

- Classical generalized quadrangle/singular spectrum is known, e.g. [Spiro et al., *Large incidence-free sets in geometries*, Electronic Journal of Combinatorics 19(4):P24, §3.4 (2012)](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v19i4p24/pdf/), where genuine GQ eigenvalue sqrt(2s) and incidence path identity are explicitly used. Standard expander mixing and singular-value Cauchy–Schwarz are classical ([Alon–Chung style Expander Mixing Lemma, Babai notes](https://people.cs.uchicago.edu/~laci/papers/srg2.pdf)). Do not present CY.2's general spectral inequality as a globally new standalone theorem.
- AA4-CY's new **project-specific scoped** application concerns arbitrary physically injected typed original factor pair maps, complete K_a−H physical occupancy, true original source GQ source flags, and second-moment Ω(s^(11/2)) positive distinct nonincident source path anchors in EVERY two halfcuts.
- Source `research/hyp105_issue230_d6aa4cy_second_moment_original_raw.py` constructs C by actual original source incidence-flag-first counts with fixed complete f,g, then independently checks exact first moment against parent AA4-CW. New genuine source Q original TWO-flag Gram formula CY.6 has an independent implementation, not inferred from a finite-h fitted model.
- Independent `research/test_hyp105_issue230_d6aa4cy_second_moment_original_raw.py`: REAL original W32 lex/S72, three physical cut pairs each, every SOURCE cut point-line pair, independently enumerated whole ORIGINAL incidence flag list per anchor; independent original source-flag-pair Gram Q; genuine W34/W38 lex/random complete embeddings and two-source-flag Gram Q, all-h exact integer gates h1..34, source Frobenius bound and original nonincident support checks, fail-closed malformed global typed pair maps/cuts.
- Five GitHub-hosted isolated jobs in `.github/workflows/hyp105-issue230-aa4cy-second-moment-original-raw.yml`. A green CI validates implementation/falsifiers, not a qualifying independent mathematics referee. Parent scientific ancestry remains Draft; no main accepted claim registry update or merge without independent scientific acceptance.

**Best next theorem AA4-CZ**: bound the *second moment on physically doubly-disjoint true original P3 anchors* more sharply than the global raw-C second moment or control correlated bad-anchor mass by source GQ projection incidence tensor; then prove survivor safe original 3matching or a fixed-global-map ALL-SEVEN GF5 compensation. Root #230 remains `OPEN_WITH_FORMAL_BLOCKER`.
