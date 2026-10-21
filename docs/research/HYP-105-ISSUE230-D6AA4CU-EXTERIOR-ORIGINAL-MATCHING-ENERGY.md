# HYP-105 #230 — AA4-CU: exact original 3-matching exterior energy and the physical-compression barrier

**Scientific DRAFT.** Parent [AA4-CT PR #620](https://github.com/definitely-stable/Mathlab/pull/620), pinned `c5d859964184f60bb023494e9f509e8b62c4efca`. Prerequisites [AA4-CR #618](https://github.com/definitely-stable/Mathlab/pull/618) (exact original B/B-overlap 3path/physical C4/permanent identity) and [AA4-CS #619](https://github.com/definitely-stable/Mathlab/pull/619), [AA4-CT #620](https://github.com/definitely-stable/Mathlab/pull/620) (many source P3 and dense physical C4 completions). No change to main, original six-ID interpretation, or historically accepted seven GF(5) weights.

## 1. Selected gap: the TRUE 3x3 matching is the only remaining local gate

For original symplectic generalized quadrangle W(3,s), s=2^h for every h>=1, put V=(s+1)(s²+1). Let M be the **actual original POINT-by-LINE incidence matrix**, V×V, entries M_{p,l}=1 iff the original incidence flag (p,l) exists. Both complete typed original factor maps f,g into **unordered** physical coordinate pairs of the same minimal physical K_a may be arbitrarily adversarially correlated.

Every true nonincident point/line (p,l) determines a unique original three-incidence-ID path p--l0--q--l. In AA4-CR let C_f(p,q) be the occupied physical C4 completions of original point factor image f(p), disjoint from doubled image f(q), decoded to genuine triples P of three *other* original POINT factor IDs. Analogously C_g(l,l0) is the set of actual source LINE factor triples L from the other occupied C4. These sets use **the one immutable global original f,g**. The original 3×3 incidence matrix M[P,L] alone decides whether the other three original singleton flags exist as a true matching.

AA4-CT proves a large reservoir of such complete physical C4-pairs for h>=14. It does NOT prove they have positive original 3×3 incidence. This slice provides an exact nonnegative linear-algebraic characterization and the exact unrestricted source energy, and independently shows why the second does not settle the first.

## 2. All-h TRUE-original 3×3 determinant-squared lemma (no source relabeling)

**Lemma CU.1 (all h>=1, every triple of distinct genuine original POINT IDs P and LINE IDs L):**

```text
per(M[P,L]) ∈ {0,1};
det_Z(M[P,L]) ∈ {-1,0,+1};
per(M[P,L]) = (det_Z M[P,L])² exactly.                   (CU.1)
```

**Proof:** The source GQ incidence graph has girth eight. Two different matchings in a bipartite 3+3 vertex subgraph have an alternating symmetric-difference cycle of length 4 or 6, which is forbidden. Consequently at most one permutation contributes to the permanent, and at most one signed permutation contributes to the determinant. If one exists, determinant is ±1; if none exists, both are 0. This is an elementary special case of classical matching/determinant identities, NOT a general equality permanent=det² for arbitrary 0-1 matrices.

In particular, **all six selected actual original incidence flag IDs** (three path flags and three singleton flags from the unique matching) are immutable. No sign ambiguity affects their positive necessary GF(5) B/B-overlap class: either one true Q exists, or none.

## 3. Exact fixed-map exterior-cube energy identity

Write T=Λ³M, the exterior third compound matrix. Rows index all unordered distinct original source point triples P, columns all unordered distinct original source line triples L, with entries T_{P,L}=det_Z M[P,L], respecting one fixed increasing order. For each real nonincident source anchor (p,l), let D_f(p,q) and D_g(l,l0) be diagonal **orthogonal coordinate projections** in the corresponding exterior triple bases, selecting exactly occupied source C4 completion triples on the left and right.

**Theorem CU.2 (all dyadic h>=1, every globally complete injected original f,g, correlated without restrictions):**

```text
Phi_f,g(p,l)
 = sum_{P∈C_f(p,q)} sum_{L∈C_g(l,l0)} per(M[P,L])
 = sum_{P,L} det_Z(M[P,L])²
 = || D_f(p,q) (Λ³M) D_g(l,l0) ||_F².                  (CU.2)

U_BB-overlap(f,g) = sum_{(p,l): original nonincident} Phi_f,g(p,l). (CU.3)
```

**Proof:** CU.1 converts each genuine perfect matching into one signed determinant squared. The square is the squared entry of the corresponding projected exterior compound matrix, so the sum is exactly its Frobenius squared. AA4-CR gives a **unique** original source path anchor and unique physical C4 source triples and singleton matching for each historically accepted original B/B-overlap sixflag, proving CU.3 without double count. This is a project-specific exact *positive-semidefinite contraction* of the existing accepted original B/B-overlap class, not yet a model-equivalent reduction of the full SEVEN-class issue #230 statistic.

A uniform lower bound U_BBo>=c s^6 would prove root Branch A, but neither CU.2 nor positivity of the unprojected norm alone proves any such bound for the *adversarially varying projections* D_f,D_g.

## 4. Exactly compute the ENTIRE unrestricted original source energy, all h

The classical genuine GQ(s,s) point collinearity graph has strongly regular parameters

```text
v=V=(s+1)(s²+1);  k=s(s+1);  lambda=s-1;  mu=s+1.
```

For N=MM^T on the original POINT source factors, N=(s+1)I+A, where A is the point collinearity adjacency. From the strongly regular identity `A²=(s²-1)I-2A+(s+1)J` and `A*1=s(s+1)*1`, A has eigenvalues k (once), s-1 (multiplicity r=s(s+1)²/2) and -s-1 (other V-r-1). Thus **the squared singular values of original M are**:

```text
(s+1)²  multiplicity 1;
2s      multiplicity r=s(s+1)²/2;
0       multiplicity V-r-1.
```

This is an application of classical GQ graph spectra (not novel spectrum). Cauchy–Binet applied to all 3×3 minors, equivalently the elementary third symmetric polynomial of the nonzero eigenvalues of MM^T, and CU.1 then give the exact UNRESTRICTED source three-matching total

```text
||Λ³M||_F²
 = ∑_{|P|=|L|=3} det(M[P,L])²
 = C(r,3)*(2s)^3 + C(r,2)*(s+1)^2*(2s)^2
 = # of 3 mutually vertex-disjoint genuine original incidence flags. (CU.4)
```

**Independent elementary non-spectral count:** let d=s+1 and m=Vd genuine original incidence flags. Choose first ordered original flag (m), second disjoint original flag (m-2d+1). For each ordered disjoint pair e1=(p1,l1),e2=(p2,l2), the forbidden third flags incident with the four already selected original source factor vertices number `4d-2-cross`, with `cross=1_{p1~l2}+1_{p2~l1}`. Both crossing terms cannot occur simultaneously in the true original GQ because that would produce a source 4cycle. Summing cross over all **ordered** disjoint pairs yields exactly `2m(d-1)^2`: each crossing flag creates an ordered real threeflag two-edge extension chosen in (d-1)² ways, with the two symmetric orientations. Consequently

```text
# true original 3-matchings
 = [m(m-2d+1)(m-4d+2) + 2m(d-1)²]/6.                (CU.5)
```

Equations CU.4 and CU.5 are **equal algebraic integers for ALL s=2^h**; implemented independent exact check with arbitrary-precision integer arithmetic (h=1..26). Neither uses a random labeling or finite-h extrapolation.

Sample exact original source totals:

| true original W3 order | V source points & V source lines | true source flags m | entire unrestricted 3-matching energy |
| --- | ---: | ---: | ---: |
| s=2 | 15 | 45 | 10,560 |
| s=4 | 85 | 425 | 11,995,200 |
| s=8 | 585 | 5,265 | 24,089,495,040 |

These **DO NOT COUNT** historically physically accepted B/B-overlap Q, are not sixflags by themselves, and cannot be used as an R3 floor.

## 5. Exact finite, true-original coercivity countercontrol

At true original W(3,2), the complete lex original typed f and g maps are actually **bijective** onto physical K6 pair labels: H=0 missing edges on BOTH sides. For physical halfcoordinate cuts X={0,1,2} and Y={3,4,5}, AA4-CS/CR give exactly 8 nonincident real original source P3 anchors, of which exactly 1 passes both original source double-versus-single physical disjointness conditions.

At that unique genuine original anchor, full physical K6 yields EXACTLY TWO occupied left C4 source triples and TWO occupied right C4 source triples — **four coupled actual physical completion pairs** — yet their four TRUE original 3×3 incidence minors are ALL ZERO. The corresponding projected exterior-cube Frobenius norm is zero, despite ||Λ³M||_F²=10560 and no physical missing pair labels whatsoever.

This is a rigorously checked **finite h=1 original-model witness**: it refutes an invalid blanket assertion that occupied two-C4 completions or the unrestricted GQ spectrum alone force a positive original matching **at each anchor**. It does NOT refute a universal large-h global lower bound, does NOT construct an infinite all-label small-S family, and does NOT show the full seven-class score S can vanish (the other six accepted classes remain).

The W32 lex and S72 **entire original 180-anchor** exterior energy equals the independently established historical B/B-overlap count 8 and 1, respectively. Exact W34 original lex/random scoped 72-anchor checks and one nontrivial W38 original anchor (0,74) compare with the old independently oriented AA4-CR permanent oracle: the W38 828,100 occupied genuine C4-pairs contain exactly 23 positive 3×3 squared minors; all other coupled physical completions are *actual* source permanent-zero candidates.

## 6. Independent code, adversarial checks and scientific boundary

- `research/hyp105_issue230_d6aa4cu_exterior_matching_energy.py`: integer 3×3 original determinant, physical source C4 projectors, original source P3 anchored Frobenius-squared census, exact global source exterior energy and independent all-h flag-count formula.
- `research/test_hyp105_issue230_d6aa4cu_exterior_matching_energy.py`: genuine original W32 **all 455² distinct 3×3 minors**, independent six-permutation permanent oracle, brute 45-choose-3 original flag matchings, independent direct ordered source edge walker, separate original MM^T matrix polynomial eigen-annihilator; W34 dual complete typed maps and independent edge-walker; W32 complete original historic BBo and zero K6-C4 witness; W34/W38 original AA4-CR matching comparisons; integer all-h tests; malformed global original typed maps fail closed.
- `.github/workflows/hyp105-issue230-aa4cu-exterior-matching-energy.yml`: six GitHub-hosted isolated proof falsifier CI lanes, exact PR head checks required.

**Prior art / credit, explicitly not original general discoveries:** generalized quadrangle girth and point-graph strongly regular spectrum are classical; see Andries E. Brouwer and Willem H. Haemers, *Spectra of Graphs*, Theorem 9.6.2, author preprint https://aeb.win.tue.nl/2WF02/spectra.pdf (book Springer, 2012, https://link.springer.com/book/10.1007/978-1-4614-1939-6). Exterior powers, Cauchy–Binet and elementary symmetric polynomials of squared singular values are standard linear algebra. The contribution is the exact **true-original, physical C4-restricted, immutable six-incidence-ID GF(5) B/B-overlap energy** and the matched true-original full-source/zero-local-barrier falsifiers. Check mathematical novelty before any publication claim.

### Remaining best AA4-CV theorem

Need an **adversarial physical-projection anti-concentration / restricted exterior-energy transfer inequality**: uniformly over every arbitrary complete correlated original f,g and perhaps over sum of original p--l0--q--l anchors, force `∑||D_f Λ³M D_g||² >= c s^6`, OR prove that its failure forces the other six historical accepted GF(5) source classes to have total Ω(s^6). Both are OPEN. Raw global eigenvalues and abundant physical C4 support sizes are insufficient by CU.2 and the honest finite W32 countercontrol; neither the positivity nor an infinite adversarial no-go has been established.

**Status: scoped all-h theorem and exact original-model finite witness, scientific DRAFT, root #230 `OPEN_WITH_FORMAL_BLOCKER`.** No Branch A/B/C, no ASET exponent, no promotion from dedicated CI to independent proof acceptance. No merge ahead of scientific ancestor #620 acceptance and qualified mathematical referee.
