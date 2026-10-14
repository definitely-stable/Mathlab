# HYP-105 / issue #230 — D6-AA4-K: exact six-coordinate projection-aware ORIGINAL pair-charge amplification

**Scope:** ALL-h exact combinatorial improvement over D6-AA4-J: source-pair Q charge capacity per accepted six-ORIGINAL-incidence GF5 motif is **9** per type, not 15. A/B/C exact caps are **9/6/3**. Class-weighted two-type GF5 numerical lower is exact conditional on having a nonzero source-pair charge. Original globally injected W32 S68/S72 exhaustive 24-state finite calibration. No universal positive `S_s=Omega(s^6)` lower; Branch A/B remain OPEN.

Stack strictly on [D6-AA4-J Draft #457](https://github.com/definitely-stable/Mathlab/pull/457) parent `169d06a5a4dd3860aa01e12f9547e2cb4fdeffe1`, with dedicated, INDEX, proof-audit SUCCESS on that head; full Research is separately tracked. No main write/merge or premature issue closure. This is a class-sensitive original-Q charging identity, not an implementation of the full original-GQ root hypothesis.

## 1. Why improve source PAIR → positive ORIGINAL GF5 sixset capacity?

AA4-I proved, for both source point and line types of ANY genuine W(3,2^h), complete separately typed-injective physical pair maps force D_t=Omega(s^5) ORIGINAL collinear/concurrent pairs with DISJOINT physical labels (explicit D_t>=s^5/4 for h>=2). AA4-J defined the total positive-seven-Q charge I_t=sum_(pair∈F_t) C_t(pair). The TRUE source-pair-to-Q double count only gave I_t<=15*S, by noting Q has at most six distinct original point/line factors. Its naive stronger "every pair has at least one positive original Q" assumption was independently FALSIFIED: on real W32 S72, true original concurrent lines #5 and #10 have physical labels (1,3) and (0,4) disjoint yet ZERO positive seven-GF5 Q contains both. Thus the mathematically legitimate next gate is the TOTAL charge and its actual per-Q capacity, with ZERO per-pair membership allowed.

Every admitted ORIGINAL Q is SIX DIFFERENT original point-line incidence IDs with **exactly SIX touched physical coordinates of degree two** on BOTH sides, since all seven accepted classes have structural projection type A/B/C. This forces stronger A/B/C capacity than the loose choose-six upper.

## 2. ALL-h exact physical projection lemma — 9, 6, 3

Fix arbitrary physical alphabet K_a, a>=6, and ONE genuine global separately injective physical pair map for source factors of either type. Let Q contain six distinct ORIGINAL incidences whose physical projection on that type uses exactly six distinct coordinate symbols with degree two each. (This is necessary for being among the seven accepted positive GF5 classes.) The projected original factor count multiplicity is one of:

- **A** = (1,1,1,1,1,1): six distinct original source factors and six distinct physical pair edges, a simple 2-regular graph on 6 coordinate vertices. Such a graph is C6 or two C3, has exactly six adjacent pairs of distinct edges and exactly 15-6 = **9 physically disjoint original source-factor pairs**.
- **B** = (2,1,1,1,1): the original source factor repeated twice maps to one physical edge used twice, consuming two coordinates' entire degree. Four remaining distinct physical source-factor edges necessarily form a C4 on the other four coordinates. There are 4 disjoint cross-2-cycle/C4 pairs and 2 opposite C4-edge pairs: exactly **6 physically disjoint distinct original source-factor pairs**.
- **C** = (2,2,2): three original source factor edges each used twice, so the physical projection is three pairwise disjoint double edges. Its three distinct edges have exactly **3 pairwise-disjoint original source-factor pairs**.

These identities hold for ANY s=2^h, h>=1, conditional only on the actual ORIGINAL six-Q being in the true seven-class GF5 six-coordinate degree-two family and both type maps being injective. They are NOT graph-theory novelty claims. The same SOURCE pair may or may not be collinear in genuine W(3,s); adding that ORIGINAL geometry condition can only DECREASE the count. No physical-P3 route surrogate is assumed.

For each true seven-GF5 positive Q and type t∈{P,L}, define k_t(Q)∈{A,B,C}, and c_t(Q) the count of eligible ORIGINAL source-collinear physically-disjoint pairs from AA4-I whose two ORIGINAL factors both occur in Q. Then

[
0\le c_t(Q)\le d(k_t(Q)),\quad d(A)=9,\ d(B)=6,\ d(C)=3.
]

Together with the elementary AA4-J exact double count:

[
I_t=\sum_{Q>0} c_t(Q)
\le\sum_{Q>0}d(k_t(Q))
\le 9S_s(f,g)
]

and, counting BOTH source types separately but each sixset Q once,

[
I_P+I_L\le\sum_{Q>0}[d(k_P(Q))+d(k_L(Q))]\le18 S_s(f,g).
]

Hence independently valid, stronger ALL-h conditional-on-total-charge bounds:
[
S_s(f,g)\ge\max\{\lceil I_P/9\rceil,\lceil I_L/9\rceil,
\lceil(I_P+I_L)/18\rceil\}.
]

**Class-sensitive sharpening:** D6=A/A has joint capacity 18; B-left/A-right and A-left/B-right capacities 15; C/A capacity 12 (orientation may be reversed and MUST be recomputed), C/B capacity 9; B/B-overlap and B/B-disjoint capacities 12. On a single type, use the actual per-Q A/B/C orientation to charge capacity 9/6/3 rather than a single 9 multiplier. For C/A and C/B the historical tags are UNORIENTED, so the code independently reclassifies both original halves from their physical coordinates and refuses a mismatch; it never assumes C is on the point side.

**Conditional asymptotic transfer in the correct averaged form:** let `D_t=|F_t|`, and average genuine positive-Q cooccurrence multiplicity `mbar_t=I_t/D_t`. Since D_t>=s^5/4 for s>=4, a *separate all-h theorem* establishing `mbar_t>=c*s` for every complete genuine f,g (allowing SOME C_t(pair)=0) would give
[
S_s\ge\lceil I_t/9\rceil\ge c s^6/36.
]
The average hypothesis is NOT PROVED in this PR; no ASET exponent.

## 3. Class-sensitive selected 51-palette GF5 numerator

For the seven true accepted GF5 original sixset tags, let `w(Q)` be the ALREADY CERTIFIED nonnegative per-Q selected numerator floor stored in `R3_CERTIFIED_FLOORS`. The true selected six-motif numerator is `W=sum_(Q>0) w(Q)`. The exact tag-specific cap `d(k_P)+d(k_L)` is at most 18 for D6, 15 for B/A, 12 for C/A or B/B, and 9 for C/B. All seven known certified weights satisfy

[
w(Q)\ge\frac{5643}{18}\,[d(k_P(Q))+d(k_L(Q))].
]

D6 is the extremal class for that ratio; `5643/18=627/2`. Therefore by exact nonnegative accounting

[
\boxed{ W\ge\left\lceil\frac{627}{2}(I_P+I_L)\right\rceil.}
]

This is a selected GF5 **numerator** lower in terms of the actual total charge; it is NOT an all-h lower on charge, NOT the full R3, and the correct denominator/palette is maintained by the historical accepted classifier. In particular it does not establish W=Omega(s^6) on its own. For W32 the exact historical `seven_census` recomputes W independently in each true full global map. For general s it is a combinatorial inequality for ANY true original sixset with the same accepted seven class and certified weights, not an extrapolation from 24 finite states.

## 4. Genuine ORIGINAL W32 independent finite falsification

For each pinned genuine S68 and S72 ORIGINAL W32:
1. Independently recover original GQ geometry, 45 original incidence IDs, AA4-C/D's exact 53/119 critical source-four transversals, select first all-POINT size-four transversal and freeze all other original factor physical pair labels.
2. Exhaust EXACTLY ALL 24 globally point-injective full physical K6 label completions, with fixed complete globally right-injective line map. Independently reclassify all **62,370** actual ORIGINAL six-incidence candidates per full map using the historical selected seven-GF5 classifier, preserving all true original six incidence positions and the complete selected 51-palette numerator.
3. Per real accepted Q and BOTH types independently validate its actual 6-coordinate degree-two physical projection, source-factor multiplicity A/B/C, exact physically disjoint source-pair count 9/6/3, and its true 7-class GF5 tag/orientation. This is a NEW structural audit **separate from** the accepted original class label.
4. Compute c_P(Q),c_L(Q) from actual ORIGINAL collinearity/concurrency pair membership with physically disjoint assigned labels; independently verify EACH total against AA4-J's separate pair-major oracle. Enforce class-sensitive numerator, all P/L and joint charge bounds, one Q once across all seven motifs, and no physical P3 filtering.
5. Report exact min/max across 24 complete maps of total positive S, both raw pair-Q charges, class-sensitive A/B/C capacities, source-pair-charge-lower S, selected GF5 charge-lower W, and **positive Q with zero eligible source-pair charge** (explicit evidence this observable does not cover entire positive seven-Q mass).

Tests independently enumerate the THREE possible abstract six-coordinate projections, injectivity and invalid negative shapes; validate exact symbolic averaged conditional asymptotic arithmetic; verify true W32 four pinned maps and several random full typed injection maps; ensure unsuitable fake class tags and malformed original Q fail closed.

## 5. What this DOES NOT prove; next step

A tighter 15→9 worst-case capacity is a genuine all-h combinatorial strengthening even if the numerical W32 lower is modest. The open theorem is **lower bounding actual TOTAL charges uniformly over arbitrary original f,g and s>=4**. Existing S72 ZERO-charge eligible pair shows no uniform per-pair positive multiplicity can hold for ALL h. Physical proper-P3 invisibility (JPKC-011) and EICE-003 true-original path covariance prevent replacing actual full-seven counts by simple coordinate paths. Structural cost tags and guaranteed source-disjoint pairs by themselves are not enough to show total charge >=c s^6.

Follow-up D6-AA4-L should investigate whether a direct two-type SOURCE support/physical projection **energy lower bound** can force I_P+I_L=Omega(s^6), or rigorously show a matching pseudo/actual counterfamily. Audit against actual JPKC-012 original sixset tensor, JPKC-014 source-factor stars, and EICE-003-C original middle-path Gram transport before claiming ROOT A/B. No PR merges, no main edits, no root issue closure. Require exact final HEAD dedicated/INDEX/Proof Audit/full Research GitHub-hosted SUCCESS plus independent mathematical review.
