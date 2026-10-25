# HYP-105 / issue #230 — AA4-DE: universal LARGE genuine-original 3×3 cofactor deficit; a quantitative NO-GO for “make D small”

**Scientific Draft, all-h rigorously scoped source-theorem + proof-method no-go; NOT Branch A/B/C.** Strict child of [AA4-DD #630](https://github.com/definitely-stable/Mathlab/pull/630), frozen head `10c6ca0cb7faed1aab9cd07291d9dd75174c0b1e`. All actual original SOURCE symplectic W(3,s), s=2^h, complete globally injected typed ORIGINAL POINT/LINE physical pair images f,g into the SAME minimal K_a, arbitrary f/g correlation and ALL original immutable incidence IDs. The seven registered GF(5) positive classes and main are unchanged.

## 1. Scientific decision: switch from attempted upper bound on D to an actual unconditional LOWER bound

The last chain AA4-CZ→DA→DB proved for EVERY h>=96 and EVERY fully complete globally correlated original typed f,g and ANY physical halfcuts X,Y (|X|=|Y|=k=floor(a/2)):

```
V=(s+1)(s²+1), d=s+1, a=min{t:binom(t,2)>=V},
T_SAFE(X,Y)
 = Σ_(real original nonincident and double-disjoint P3 anchors p--l0--q--l)
    # {TRUE ORIGINAL point i and line j crossing incidence flag (i,j):
        f(i) touches f(p), g(j) touches g(l), source spoke
        f(i) avoids f(q), g(j) avoids g(l0), f(i)⊂X, g(j)⊂Y}
 >= s^7 / 2^14.                                          (DE.0)
```

These are ANCHOR-INDEXED, immutably ORIGINAL SOURCE flags, not synthetic edges and not necessarily accepted historical GF(5) sixflags.

AA4-DC/DD exact historical accepted B/B-overlap cofactor bookkeeping on the ACTUAL two completed physical C4 original factor triples gives `T=D+E`, where for every true-original marked spoke-to-spoke source flag in the 3×3 original incidence matrix, E marks whether its complementary true-original 2×2 source incidence has a perfect matching; D records nonextendible true-original marks. We previously sought an **upper bound** on D in order to make U_BBo positive.

**New result AA4-DE:** such a method is quantitatively impossible: **for every fixed legal global original f,g and every pair of physical halfcuts, D is unconditionally at least Ω(s^10) as a C4-PAIR-MULTIPLICITY-WEIGHTED true ORIGINAL marked-source cofactor-deficit**. This does NOT imply that original U_BBo or the other accepted six GF(5) classes are small. The extra exponent from s^7 to s^10 comes from counting many REAL, globally occupied physical C4 completion pairs for EACH true original source SAFE crossing flag.

## 2. Precise all-h theorem AA4-DE.1

Fix ANY dyadic h>=96, s=2^h, the true original symplectic W(3,s), V=(s+1)(s²+1), d=s+1. Fix ANY complete globally injected typed original POINT map f and original LINE map g into unordered physical edges of the SAME MINIMAL K_a, with no independence assumptions. Fix ANY two physical halfcoordinate subsets X,Y of size k=floor(a/2).

On each typed physical map f (respectively g), define the physical missing-edge degree `δ_f(u)` (respectively `δ_g(u)`) to be the number of UNoccupied unordered physical K_a pairs containing u. By minimality, the total number of physical missing edges per typed map `H=binom(a,2)−V<=a−2` and `Σ_u δ(u)=2H`.

Call u **HEAVY** if `4 δ(u) >= a−5`; otherwise LIGHT. Call a genuine ORIGINAL typed factor **light** if BOTH coordinates of its actual physical edge image are light for its own typed map. Keep only the TRUE ORIGINAL SAFE crossing flags (p,l;i,j) counted in DE.0 for which all FOUR original SOURCE typed factor images f(p),f(i),g(l),g(j) are light. Denote their number `F_light(X,Y)`. Let m=floor((a−5)/2)+1.

Let `T_light` be the total ACTUAL original SOURCE spoke-to-spoke marked incidence weight obtained by expanding each such light crossing `(p,l;i,j)` over ALL ACTUALLY OCCUPIED ORIGINAL POINT physical C4 completion triples of f(p) containing actual original source point i, avoiding doubled factor f(q), times ALL ACTUALLY OCCUPIED ORIGINAL LINE physical C4 completion triples of g(l) containing actual original source line j, avoiding doubled g(l0). Each paired C4 contributes ONE marked original SOURCE edge (i,j). No source original incidence is invented from the physical pair overlap. Let `E_light` be the subset of these original marked positions for which the complementary TRUE original SOURCE 2×2 incidence permanent is one, and `D_light=T_light−E_light` the rest.

**Theorem (EVERY h>=96, every actual W(3,s), ALL fixed complete arbitrary-correlated f,g, ALL physical halfcuts X,Y):**

```
F_light >= s^7 / 2^15;                              (DE.1)
T_light >= m² F_light >= s^10 / 2^17;               (DE.2)
E_light <= (2d/m)*T_light <= T_light/2;             (DE.3)
D_BBo(full;X,Y) >= D_light >=s^10 / 2^18;          (DE.4)
max_{four original typed dual Hall vacancy classes} D_type
                         >=s^10 / 2^20.           (DE.5)
```

Here the left side of DE.4 is EXACT the FULL original AA4-DC/DD Hall cofactor deficit D over ALL actual paired two-sided C4 completion triples, with ORIGINAL nonincident anchors in cuts X,Y (completion edges not artificially limited to cuts), counted WITH actual completion-pair multiplicity. It is NOT a count of DISTINCT original six-incidence-ID accepted GF5 Q sets. DE.5 uses AA4-DD's exact nonnegative four-class fractional partition of the same D (point other-spoke, point center, line other-spoke, line center).

In particular **a universal theorem asserting `D_BBo=o(s^10)` or `D_BBo=o(T_light)` for all maps contradicts DE.3–DE.4.** This is a NO-GO for the former “bound the original cofactor deficit away by smallness” proof strategy in this full counted-completion model. It is NOT a no-go for Branch A or seven-class compensation.

## 3. Proof part I: few genuinely ORIGINAL source factor images touch heavy physical coordinates

Each typed map omits only H<=a−2 physical K_a pairs. Since `Σ_u δ(u)=2H`, number of coordinates satisfying `δ(u)>=(a−5)/4` is at most

```
#HEAVY <= 8H/(a−5) <=16, for a>=8.           (DE.6)
```

Each physical coordinate belongs to at most (a−1) image edges because the original typed map is injective into physical unordered pairs. Thus each map has at most `16(a−1)` ACTUAL ORIGINAL typed SOURCE factor IDs with some heavy coordinate.

Charge original SOURCE SAFE crossing flags with ANY heavy image among the four actual factor roles (original point anchor p, point spoke i, original line anchor l, line spoke j). For any single fixed genuine original SOURCE typed factor r, the total **RAW** original SPOKE cross-incidence-flag mass in which r appears as an anchor or as a spoke is at most `4k²d` for EACH of these distinct roles: any occupied image edge in one typed physical K_k overlaps at most 2k other occupied pair images, each ORIGINAL point/line factor has exactly d genuine original incident factors in W(3,s), and the opposite typed physical K_k physical-overlap graph has at most 2k neighbors per such incident factor. This does NOT assume random placement of original source factor IDs.

There are at most 16(a−1) heavy source factors in EACH typed map, TWO roles per typed source. Therefore

```
#deleted original SAFE source flags <=
4 * 16(a−1) * 4k²d = 256(a−1)k²d.           (DE.7)
```

For all h>=96, exact minimal-K_a integer bounds imply `32768*256(a−1)k²d<=s^7`. Combining DE.7 with DE.0 gives DE.1:

```
F_light >= s^7/2^14 − s^7/2^15 =s^7/2^15.
```

This is fully deterministic for ANY fixed correlated complete original f,g.

## 4. Proof part II: every light genuine original SAFE spoke has many ACTUAL occupied C4 completions

Consider a retained REAL source POINT SAFE spoke f(i)={u,z}, base f(p)={u,v}, and doubled original factor f(q)={x,y} with all five coordinates distinct (source SAFE conditions). Its REAL occupied physical C4 source-factor completions containing f(i) have the exact form

```
f(i)={u,z},  f(center)={z,w},  f(other-spoke)={w,v},
w∈[a] \ {u,v,x,y,z}.
```

There are a−5 candidate w. At most `δ(z)+δ(v)` candidates fail because one or both required true source-factor physical images are MISSING. Because original point anchor p and actual original point spoke i are both LIGHT, the physical coordinate z and opposite base coordinate v have `4δ(z)<a−5` and `4δ(v)<a−5`. Hence

```
#TRUE ORIGINAL point typed physical C4 triples containing i
 >=a−5−δ(z)−δ(v) >(a−5)/2,
 >=m=floor((a−5)/2)+1.                       (DE.8)
```

Same for TRUE ORIGINAL LINE typed physical C4 triples containing the original line spoke j. Every selected source SAFE crossing (p,l;i,j) thus generates at least m² **genuine** paired physical C4 source-factor triples, all original IDs drawn from the same globally fixed f/g. As different source crossing flags/cut anchors define different marked positions in the full AA4-DC historical C4 energy, summing gives DE.2. No synthetic ORIGINAL incidence flags are added by this physical count.

For s>=2^96, `4m²>=s³` (analytically from minimal a), yielding `T_light >= s^7 m²/2^15>=s^10/2^17`.

## 5. Proof part III: per marked ORIGINAL source flag, very few C4 pairs can be matched

Fix ONE retained genuine original source SAFE marked CROSSING incidence (i,j) attached to original nonincident three-flag anchor (p,l). Freeze any ONE actual occupied POINT physical C4 triple containing the genuine original source point spoke i. The other two ACTUAL ORIGINAL SOURCE POINT factors (call them other-spoke `i_other` and center `i_center`) are fixed.

Now vary the occupied LINE physical C4 triples containing the fixed genuine ORIGINAL source line spoke j. Each such triple has one other LINE physical spoke `j_other`, whose image contains the physical endpoint of g(l) OPPOSITE its intersection with g(j), and an additional physical coordinate w. DISTINCT line C4 completion choices have DISTINCT physical w and hence DISTINCT globally injected ORIGINAL line factor `j_other`. This injection holds in the SAME g and does not rely on any distribution over original source factor IDs.

If the marked actual source incidence (i,j) is extended to a REAL ORIGINAL 3×3 matching, the other ORIGINAL LINE SPOKE factor `j_other` must be truly source incident to EITHER actual original source POINT factor `i_other` OR `i_center`, since there are only TWO remaining source point factors to match with the two remaining source line factors. Each genuine original point in W(3,s) has d=s+1 original incident LINE factors. Thus there are at most **2d** possible `j_other` candidates and hence at most **2d** physically distinct LINE C4 completion triples whose complementary source cofactor could equal one, FOR THIS FIXED POINT C4 triple.

Therefore over the `m_P>=m` actual point C4s and `m_L>=m` actual line C4s containing the SAME retained marked genuine source flag,

```
E_mark <= (2d)*m_P,
T_mark = m_P*m_L,
E_mark / T_mark <=2d/m_L <=2d/m.             (DE.9)
```

Sum DE.9 over ALL retained original source marked flags. The estimates hold pointwise for each source flag, so they remain valid under arbitrary correlations of f,g and original source incidence placements. This yields the first DE.3 bound. Exact all-h minimal a gives `m>=4d` for h>=96, hence `E_light<=T_light/2`, and `D_light>=T_light/2`. DE.4 and DE.5 then follow since `D_BBo(full)>=D_light` and the four AA4-DD Hall source vacancy classes partition full D.

## 6. What this ACTUALLY means scientifically

- **Proved:** An unconditional ALL-map/all-h lower bound `D_BBo(full;X,Y)=Ω(s^10)`, not merely the old disjunction `U_BBo large OR D large`. The exponent 10 is on a **multiplicity-weighted cofactor-failure count of true source C4 pairs**, whereas root #230 needs `S_s(f,g)=Ω(s^6)` for **DISTINCT accepted original six-incidence-ID GF5 Q sets**. Exponents are not interchangeable.
- **Proved:** Dense near-complete physical pair embeddings structurally PRODUCE many unmatchable completed source C4 pairs, rather than making all source 3×3 matchings likely. The per-flag success fraction of the robust light subset is at most `2d/m=O(s^(−1/2))` under each fixed source map.
- **NOT proved:** that `D_BBo(full)` is `Θ(T_full)` for all legal maps (we control only the canonical large light sub-ensemble); that U_BBo is small; that a large typed Hall vacancy induces one of the other six accepted original GF5-positive classes; that a specific original sixflag Q uses only the six source factors of a no-match C4 pair; or that the whole root Branch A/B/C or strict R3/ASET exponent is closed.
- **Research decision:** The proposed next step “upper-bound D by a vanishing fraction of the large physical C4 mark mass” is not viable for the robust sub-ensemble. Future AA4-DF must seek **genuine other-class positive GF5 compensation on the same complete correlated f/g**, or a different original matching mechanism that does NOT require the universal smallness of these physical-C4-weighted cofactor deficits.

## 7. Three independently implemented genuine-original falsifiers

The additive Python module `research/hyp105_issue230_d6aa4de_robust_cofactor_sparsity.py` verifies exact dyadic h=1..110 analytic gates, computes actual physical missing degrees for the two globally fixed typed original SOURCE maps, extracts TRUE original nonincident P3 unique paths and actual 3×3 source incidence cofactor failures on all canonical occupied C4 completion pairs containing marked ORIGINAL source flag i,j. It checks the pointwise TRUE original `# LINE C4 source-3match completions <=2d` for fixed POINT completion, and the required `m>=floor((a−5)/2)+1` for each light flag when NOT explicitly capped.

A **separate source-flag-independent loop** in `research/test_hyp105_issue230_d6aa4de_robust_cofactor_sparsity.py` enumerates every CANONICAL AA4-CR occupied two-C4 pair FIRST, then every actual original marked point-spoke→line-spoke incidence within the two source triples, and counts ORIGINAL complementary 2×2 perfect matchings with an independent two-permutation direct oracle. It is distinct from the source module's MARKED-FLAG-FIRST completion pairing loop. Genuine W32 lex/S72 and W34 lex/random selected true-original anchors use all original C4 completions (NO triple cap) and compare both orientations, source pointwise 2d bound and AA4-DC full real-original Hall-defect bound. Genuine W38 lex/random sample explicitly 4 true source anchors×first 8 C4 triples per side (PARTIAL); no universal W38 claim from that run. All physical coordinate hole degrees are recomputed independently. Fail-closed malformed genuine source injected images, cuts, anchor IDs and illegal cap. **Five hosted isolated jobs** must be inspected at current exact-head before claiming CI success; proof and scientific acceptance are NOT guaranteed by green CI.

## 8. Prior art and threshold

The underlying degree d=s+1, original GQ girth8 and point-line incidence graph properties are classical; see the Electronic Journal of Combinatorics 15 (2008), survey *Cages* §2.2.2, and Peter J. Cameron's 2026 review *Hall's marriage theorem*, JLMS 113(1):e70378, for standard matching terminology. Elementary missing-edge charging and the 2d union bound are not new as standalone tools. The **project-specific quantified AA4-DE theorem** involves the simultaneous arbitrary original SOURCE GQ→physical pair embeddings, actual original source nonincident projection P3, all completed typed original physical C4 marks and true source cofactors with constrained global correlation. Its scientific novelty and journal quality still require independent mathematical proof review and thorough prior-art comparison.

Large h>=96 is deliberately conservative, analytically certified for ALL dyadic h>=96. Exact integer h1..110 diagnostics are falsifiers, not finite-size curve fitting.

**Root #230: `OPEN_WITH_FORMAL_BLOCKER`; #176/#169 untouched; no accepted seven-class GF5 theorem; scientific Draft pending qualified independent referee and complete exact-head Research + all ancestor integration checks.**
