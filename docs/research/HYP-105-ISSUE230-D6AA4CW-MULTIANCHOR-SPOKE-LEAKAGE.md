# HYP-105 / #230 — AA4-CW: universal multi-anchor ORIGINAL spoke-incidence leakage in every halfcut

**Scientific DRAFT, genuinely original all-h (h>=24) scoped partial theorem — NOT root A/B/C.**

Strict child of [AA4-CV/#622](https://github.com/definitely-stable/Mathlab/pull/622) at exact parent SHA `5ab462f5a09a8a00906e4b676767f441cd15b14e`; earlier complete-original threepath/true-original permanent facts [AA4-CQ/#617](https://github.com/definitely-stable/Mathlab/pull/617), [AA4-CR/#618](https://github.com/definitely-stable/Mathlab/pull/618), [AA4-CT/#620](https://github.com/definitely-stable/Mathlab/pull/620), [AA4-CU/#621](https://github.com/definitely-stable/Mathlab/pull/621). Preserve immutable six original incidence IDs, true W(3,2^h), both globally injected typed pair maps f,g, no independence or redrawing, the original seven GF(5) class definitions and all correlations.

## 1. Select one unresolved mathematical implication, not a duplicate of AA4-CV

AA4-CV constructs for each given genuine source nonincident 3path p--l0--q--l a fully legal pair of complete original mappings whose two original-C4 completion families are maximally occupied but *all* selected 3x3 incidence permanents are zero. Its quantifier order is

```text
forall (p,l) genuine nonincident, EXISTS complete original f,g : local_phi(p,l;f,g)=0.
```

It does NOT show one pair f,g erases many source paths simultaneously. The next desirable positive statement for root Branch A would be `forall f,g sum_{p,l} phi(p,l)>=c s^6`. We cannot prove it.

**Instead we prove a rigorous many-anchor necessary leakage inequality** that rules out simultaneous incidence-free *RAW PHYSICAL SPOKE* rectangles for almost every genuine source P3 in an arbitrary halfcoordinate cut. This is weaker than the needed true original matching lower; it is a genuine joint-global-map fact not available from the separate AA4-CV per-anchor construction.

## 2. Exact model and THEOREM (all dyadic h>=24)

Let s=2^h, h>=24, original symplectic W(3,s), V=(s+1)(s²+1) original POINT and V original LINE factors, d=s+1, M the unchanged TRUE original V×V point-line incidence matrix. Let a be the **minimal** integer with binom(a,2)>=V. The *two* fully complete globally injected, potentially arbitrarily correlated typed mappings f,g place all V original point/line factors into different physical pair labels in the **same** K_a alphabet, omitting H=binom(a,2)−V<=a−2 labels on each side.

For EVERY subsets X,Y of physical coordinate labels with |X|=|Y|=k=floor(a/2), set

```text
P_X={p ORIGINAL POINT : f(p)⊂X}, L_Y={l ORIGINAL LINE : g(l)⊂Y}.
N_f^X(p)={i ORIGINAL POINT in P_X : i!=p, f(i)∩f(p)!=∅},
N_g^Y(l)={j ORIGINAL LINE in L_Y : j!=l, g(j)∩g(l)!=∅}.
C_XY(p,l)=#{(i,j) TRUE ORIGINAL INCIDENCE ID :
              i in N_f^X(p), j in N_g^Y(l), M_ij=1}.
```

These are **RAW SPOKE** neighborhoods under ONE COMPLETE global f,g. They are NOT the AA4-CR C4 source-triple completion lists: raw spokes may hit f(q) or g(l0) of the unique original nonincident path, may lack a physical C4 center, and a single original cross-flag cannot force a perfect matching for the full 3×3 incidence matrix.

**NEW scoped theorem AA4-CW.1 (quantifiers as stated):**

```text
For EVERY h>=24, for EVERY genuine W(3,2^h),
for EVERY global complete injected correlated f,g,
for EVERY two physical k-coordinate cuts X,Y,

#{(p,l)∈P_X×L_Y: p NOT source incident l, C_XY(p,l)>=1}
   >= V*k/2048 > s^(9/2)/4096.                      (CW.1)
```

The exponent 9/2 is for **NONINCIDENT genuine original POINT–LINE anchor pairs**. Each such pair corresponds to a UNIQUE genuine original 3-incidence-ID path. No real six-ID motif is asserted.

## 3. Proof from complete physical images and genuine original GQ singular spectrum

**(i) Exact physical holes, heavy vertices and good source image factors.** Every typed map covers V of K_a's physical unordered pairs and omits H<=a−2. For one cut X, call a coordinate u∈X heavy when it belongs to >=k/4 missing physical pair labels (including missing labels outside X, a conservative overcount). Since the sum of missing degrees over every coordinate is 2H, there are at most 8H/k heavy vertices. At most (k−1) occupied source pair-images in X touch any given coordinate; therefore **at most 8H** original point factors p∈P_X have f(p) touching a heavy physical coordinate. Define I⊂P_X after removing these; similarly J⊂L_Y for g.

For an original source point factor i∈I with physical edge f(i)={u,v}⊂X, each of its two endpoints is incident with <k/4 physical missing pair labels. Among all source images in X, the number of **other** image edges sharing a coordinate with f(i) is at least

```text
2(k−2)−h(u)−h(v) > (3/2)k−4 >=k                (k>=8).
```

So |N_f^X(i)|>=k for every i∈I, and |N_g^Y(j)|>=k for every j∈J. No regularity is assumed for individual physical images outside I,J.

From the elementary minimal-alphabet occupancy inequality
`binom(k,2)>=binom(a,2)/4−a`,
`|P_X|,|L_Y|>=binom(k,2)−H>=V/4−7a/4>=V/8`
when V>=14a. For h>=24, the standard minimal-alphabet bound `a−2<3s^(3/2)/2`, V>=s³, and a>=4 imply `V>=128(a−2)>=14a`. Thus `|I|,|J|>=V/8−8H>=V/16`.

**(ii) Genuine original incidence expansion.** The true original W(3,s) point-line incidence matrix M has largest singular value d=s+1 and largest *nontrivial* singular value sqrt(2s), by the standard genuine GQ strongly regular point-collinearity spectrum (this identity is already established/checked independently in AA4-CU). Its expander-mixing inequality on arbitrary ORIGINAL source factor sets I,J reads

```text
E_GQ(I,J) >= d*|I||J|/V - sqrt(2s)*sqrt(|I||J|).
```

Because sqrt(|I||J|)>=V/16 and `d²>=2048s` for all s>=2^24, we have `d>=32sqrt(2s)` and hence

```text
E_GQ(I,J) >= (d/2V)*|I||J| >= dV/512.          (CW.2)
```

These are TRUE source incidence IDs. Source geometry is not reconstructed from the physical K_a pair intersections.

**(iii) Exact global anchored first moment, no independence.** Define `T=sum_{p in P_X,l in L_Y} C_XY(p,l)`. Reverse the order of the **finite integer sum** over actual original source incidence IDs:

```text
T = Σ_(i,j TRUE original incidence, i∈P_X,j∈L_Y)
       |N_f^X(i)|*|N_g^Y(j)|.
```

Since at least E_GQ(I,J) original flags have endpoints in I×J and each carries weight >=k²,

```text
T >= k² E_GQ(I,J) >= k²*d*V/512.               (CW.3)
```

This is a genuine simultaneous multianchor obstruction to making ALL raw spoke rectangles empty for ONE frozen pair f,g; it does not claim positive *local* permanent, and the original flag (i,j) can contribute to many anchors (allowed because we count distinct anchors separately at the end).

**(iv) Control concentration on one anchor; exclude incident endpoint pairs.** Each original p has at most 2(k−2) other source factor images in P_X overlapping f(p). Each such i is incident with exactly d TRUE original LINE factors, so

```text
0<=C_XY(p,l)<=2(k−2)d   for EVERY p,l.
```

Therefore at least `T/[2(k−2)d] >= Vk/1024` ordered cut endpoint pairs have nonzero raw spoke source incidence (because k²>=k(k−2)). At most Vd such endpoint pairs (p,l) are **originally incident**. Hence the nonincident positive count is

```text
 >= Vk/1024−Vd >= Vk/2048                   (k>=2048d).
```

**(v) Explicit dyadic threshold, not a fitted finite h range.** Let s>=2^24. Minimality gives `a(a−1)>=2V>=2s³`. Consequently `a>=sqrt(2)s^(3/2)>(7/5)s^(3/2)`, whence `k=floor(a/2)>=(a−1)/2 > (7/10)s^(3/2)−1/2>=2048(s+1)`. The last inequality follows from sqrt(s)>=4096 and s>=16. Also V>s³ and `k> s^(3/2)/2`, giving the last strict bound in CW.1. All inequalities are exact mathematical statements for every dyadic h>=24, independently of the finite h1..30 integer test.

## 4. Independent source and physical falsifiers

Added independent module `research/hyp105_issue230_d6aa4cw_multi_anchor_spoke_leakage.py` with **two differently oriented full ORIGINAL source incidence counts**: anchor-first C(p,l) by reading real original POINT i→LINE j flags inside physical spoke-neighborhood images, and independent original-flag-first sum `Σ_(i,j genuine flag)|N_f(i)| |N_g(j)|`. Test module `research/test_hyp105_issue230_d6aa4cw_multi_anchor_spoke_leakage.py` independently re-enumerates original immutable incidence IDs and physical pair overlaps with a third direct W32 brute oracle, and verifies every cut anchor, not just aggregate moments.

- Authentic original W32 lex/S72 complete maps, four half-coordinate cuts each, **every** original cut pair checked with a direct immutable-flag oracle, including source incident endpoint separation and every unique true-original nonincident P3 path.
- Original W34 lex/random, W38 lex/random complete global maps, four cuts each; anchored source-first count agrees exactly with separately implemented original immutable-flag-first mass.
- Original dyadic exact integers h1..30, special checks h14,20,23,24,30 against analytic gates and exponent 9/2. Finite arithmetic does NOT constitute the infinite-h proof.
- Fail-closed invalid cuts, malformed h, and incomplete or duplicate original global pair embeddings. No independent random f,g redraw at any substep.
- GitHub-hosted path-scoped research workflow is required for exact PR SHA before asserting PASS. CI passing is not independent qualified mathematical review.

## 5. Explicit limitations and next missing genuine theorem

This positive multianchor result **does not** show a positive contribution to the accepted historical B/B-overlap count. A raw spoke incidence (i,j) can use a physical edge intersecting a path's doubled image f(q) or g(l0), and even a valid spoke×spoke true original flag does not automatically extend to a matching of THREE distinct original flags between two physically completed C4 source triples. In the genuine W(3,s) source, the other matching flags are strongly dependent. Thus none of CW.1–CW.3 implies `U_BBo>0`, a universal `Omega(s^6)` bound, all-seven fixed-map S positivity, an infinite Branch B `S=o(s^6)` counterfamily, a qualifying whole-root C reduction, or any R3/ASET exponent.

CW.1 rules out ONLY the possibility that all but o(s^(9/2)) nonincident cut anchors have ZERO original incidence in their **raw** spoke rectangle by the SAME global complete f,g. It does **not** show an Ω(s⁶) fraction positive among AA4-CT's physically disjoint genuine P3 and does not settle whether they can simultaneously have zero **completed** 3×3 matchings. Next AA4-CX should (a) control physical doubled-image exclusions for many anchors and (b) produce a true three-flag matching lower **or** prove fixed-map crossclass compensation.

**Prior art carefully separated:** classical generalized quadrangle spectra, expander mixing, and incidence-free-set methods are not novel here. See *Large incidence-free sets in geometries*, Electronic Journal of Combinatorics 19(4), P24 (2012), https://www.combinatorics.org/ojs/index.php/eljc/article/view/v19i4p24, and *Incidence-free sets and edge domination in incidence graphs*, Journal of Combinatorial Designs (2024), https://doi.org/10.1002/jcd.21925. The scoped contribution is their rigorous *project-specific* application to two arbitrary globally injected correlated original factor-to-physical pair images, heavy-hole control, many nonincident SOURCE GQ anchors across every physical halfcut, with independent source-ID falsifiers.

**Root #230: OPEN_WITH_FORMAL_BLOCKER.** Scientific Draft; no main modifications, no acceptance, no merge before parent #622 exact ancestry, complete exact-HEAD checks and qualified independent mathematical referee.
