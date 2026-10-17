# HYP-105 / #230 — AA4-BX: weighted genuine-original POINT-C sixcube cubic rigidity

**Scientific Draft.** Strict child of [AA4-BW #596](https://github.com/definitely-stable/Mathlab/pull/596) at pinned HEAD d9085a761c6d5bae379d5cc6eec44fcabe82b0e0. The root #230 is OPEN_WITH_FORMAL_BLOCKER; no main/accepted registry edits. All claims concern actual W(3,2^h), all h>=1, six DISTINCT original incidence IDs per historical sixflag, same six IDs on both physical projections, arbitrary globally injected possibly correlated original POINT f and LINE g maps.

## Exact prior art separation

Prior #587 proves degree<=6 for all seven original historical GF5 scores on disjoint original LINE-factor whole-image-swap Boolean cubes and a logically abstract zero-center no-go. #590 establishes genuine source packet Walsh support and signed Gram. #591 gives genuine sixth-order original C/A source cap 960 and complete C/B annihilation. #593 gives genuine fifth-order source C/A <=480d(d-1), C/B <=960; parallel #592 corrected fifth-order exterior original source incidence. Parent #594 proves fourth-order C/B true GQ bound B4(d)=960+96d+192(2d-1)(d-1). Parent #596 already proves C/B-only sixcube uniformly cubic modulo O(s^2). **Separate sibling #595** proved the missing fourth-order POINT-C anchor bound \(A_4(d,V)=96d^2(d-1)^2+48(V-2)\binom d2\) with correct source-anchor multiplicity for C/A. Sibling #595 is a necessary mathematical proof dependency for the present mixed two-class result, not merged or rebranded as authored here. General Walsh inversion and GQ line intersection facts are classical.

**New scoped deduction:** a single **historical GF5 R3-weighted symmetric C/A+C/B two-class** subtotal, combining C/A and C/B simultaneously, is uniformly cubic with an explicit \(O(s^5)=o(s^6)\) signed remainder over every full 64-map genuine-original six-line-swap cube. Additionally, an exact finite original-f-only two-class source support certificate and genuine W32 opposite-signed weighted fourth coefficients provide a specific all-real-source limitation on naive sign-based proofs.

## Theorem: arbitrary fully fixed original f,g, every six-packet swap cube

Let s=2^h,h>=1, d=s+1, V=(s+1)(s^2+1), a minimal with binom(a,2)>=V. Choose ANY true original W(3,s), ANY full injective and arbitrarily correlated typed point and LINE factor pair-edge maps f,g. Choose SIX disjoint pairs of ACTUAL original LINE factor IDs, and toggle whole original source LINE factor image transpositions. Each x in {0,1}^6 gives a complete globally injected right map g^x onto the SAME occupied physical pair-edge support, with f and every original incidence ID unchanged.

Let W_C(x)=43320 S_C/A(f,g^x)+49050 S_C/B(f,g^x) be the historically necessary selected GF(5) weighted subtotal of TWO symmetric classes: C/A includes BOTH original POINT C=(2,2,2)/LINE A=(1,1,1,1,1,1) AND original POINT A/LINE C; C/B includes BOTH original POINT C/LINE B=(1,1,1,1,2) AND original POINT B/LINE C. Every S counts six DISTINCT genuine-original incidence sets with BOTH physical typed six-coordinate 2-regular projections. **At Walsh orders t>=4, only source POINT C with right source LINE A or B can contribute**, because the reverse orientation has right source LINE C=(2,2,2) with only THREE distinct LINE IDs and cannot hit four disjoint source LINE swap packets. The reverse orientation nevertheless contributes to the full original score, zero mode and orders 1..3; it is NEVER discarded or replaced by an independent per-Q redraw.

Let \(\widehat W_C(T)=64^{-1}\sum_x(-1)^{\langle T,x\rangle}W_C(x)\) and \(P_{\le3}W_C(x)=\sum_{|T|\le3}\widehat W_C(T)(-1)^{\langle T,x\rangle}\) be the EXACT zero-through-third Walsh projection (including signed original source cross correlations and the actual zero mode). Define

\[
\begin{aligned}
A_4&=96d^2(d-1)^2+48(V-2)\binom d2,\quad
A_5=480d(d-1),\quad A_6=960,\\
B_4&=960+96d+192(2d-1)(d-1),\quad
B_5=960,\quad B_6=0 .
\end{aligned}
\]

**Theorem, all h, ALL valid fixed f,g and EVERY one of the 64 complete-map vertices x**:

\[
\boxed{
|W_C(x)-P_{\le3}W_C(x)|
\le E_C(s)=\frac{43320}{2}(15A_4+6A_5+A_6)
+\frac{49050}{2}(15B_4+6B_5)
=O(s^5)=o(s^6).
}
\tag{BX}
\]

**Proof:** The reverse-orientation original source POINT A/LINE C and POINT B/LINE C contributions are each functions of at most THREE disjoint LINE swap bits for any one original sixflag Q, because source LINE C has exactly THREE distinct original LINE IDs. By source packet locality (#590) their individual Walsh coefficients at ALL orders t>=4 are zero, even though they are retained without alteration in W_C(x) and the cubic projection. Thus for t>=4 only source POINT C/right A or B needs geometric source counting. A nonzero t-th Walsh coefficient of any one real six-original-ID GF5 indicator requires that same original Q intersect all t corresponding disjoint true LINE source-factor image-swap packets (#590). The physical GF5 acceptance indicator is {0,1} on the original complete-map cube, so its nonzero Walsh magnitude is <=1/2. For t=4 the real GQ POINT-C/right A source quadruple anchor proof of sibling #595 gives the A4 bound: four selected genuine packet source flags in a sixflag with source POINT C must have multiplicity (2,1,1) or (2,2), with <=6*4*(2d)^2*(d-1)^2 and <=3*16*(V-2)*binom(d,2) marked anchor completions respectively. Every actual Q hitting four packets has AT LEAST ONE such anchor; repeated anchors produce overcount and only strengthen the upper bound. For right B the sharper GQ exterior-line/transversal source bound B4 from #594 applies.

For t=5, actual true source POINT C/right A candidates are <=480d(d-1) (#593) and actual POINT C/right B candidates <=960 (#593); t=6 has at most 960 actual source POINT C/right A sixflag Q and ZERO right-source B sixflag Q (#591), since source LINE B has only five distinct source LINE factor IDs and cannot hit six disjoint packet pairs. These bounds hold for all f,g because they count genuine source Q before physical acceptance. There are 15 fourbit subsets, six fivebit subsets, one sixbit subset. Weighted linearity and exact Walsh inversion give BX immediately and uniformly for all vertices. Since V=Theta(s^3) and d=Theta(s), A4=O(s^5) dominates, proving strict o(s^6).

### Stronger mathematically defined f-only source-support certificate

For each t=4,5,6 and subset T of that size define H_t,C/A(f;T) to count REAL six-distinct-incidence Q of original **POINT C / LINE A orientation** touching each selected source LINE packet in T for which the THREE doubled original POINT images under the UNCHANGED f occupy three pairwise disjoint physical unordered pair edges. Analogously H_t,C/B(f;T) counts the **POINT C / LINE B orientation** for t=4,5 (H_6,C/B=0). These SOURCE candidate sets are independent of g and are physically necessary for left 2regularity.

Therefore the SAME original weighted source count obeys for EVERY original right labeling g and EVERY full right-map cube state:

\[
|W_C(x)-P_{\le3}W_C(x)|
\le E_{f,C}:=\frac{43320}{2}\sum_{t=4}^6\sum_{|T|=t}H_{t,C/A}(f;T)
+\frac{49050}{2}\sum_{t=4}^5\sum_{|T|=t}H_{t,C/B}(f;T)
\le E_C(s).
\]

For true W32 this PR computes ALL of these H counts exactly with an independent literal scan of 62,370 left physically eligible original sixflag IDs, filtering the original POINT C/LINE A and POINT C/LINE B profiles for high-order source support; the reverse original LINE C orientation contributes only to the low-order score and does not enter the H4/H5/H6 packet sets. Parent #596 true GQ line-intersection methods compute the C/B terms for W32/W34. The all-h f-only formula is a source-set definition; **no scalable high-h C/A enumerator** is claimed. The all-h closed-form E_C remains directly computable at arbitrary h without fabricating a high-h W3.

### Genuine-original weighted fourth-order sign obstruction — distinct fourcube and sixcube derivatives

For the SAME first four of six selected actual original source LINE-factor packets on symplectic W32 lex/S72, the **standalone fourcube with only four right images allowed to toggle** (independently tested in parallel #595/#594) has original C/A fourth coefficients lex=-1/8, S72=0, and C/B fourth coefficients lex=0, S72=+1/16. Its selected two-class weighted fourth derivatives are therefore -5415 for lex and +24525/8 for S72: opposite signs.

**Critical distinction confirmed by hosted independent tests:** the coefficient indexed by these same four bits in the SIX-DIMENSIONAL cube is a Fourier MARGINAL, namely the average of four separate fourbit signed derivatives at the four settings of the two remaining source swaps. This need NOT equal the standalone fourcube derivative with those two bits FIXED at zero. The actual full SIXCUBE original historical C/A fourth coefficient is lex=-1/8, **S72=-1/32**; the original C/B coefficient is lex=0, S72=+1/16. Therefore its actually measured weighted fourth coefficients are lex=-5415 and S72=

\[
43320(-1/32)+49050(1/16)=13695/8>0.
\]

Hence the weighted TRUE ORIGINAL sixcube fourth coefficient itself still changes sign (negative lex, positive S72), without illicitly identifying a fourcube coefficient with a sixcube marginal. This is genuine W(3,2), not an abstract surrogate, and refutes only an unconditional nonnegative signed fourth-order WEIGHTED POINT-C coefficient premise; it does not disprove other cross-order inequalities or a seven-class original-center positive floor.

**Additional historical GF(5) oracle guard, independently reproduced:** The original positive seven-GF5 C/A label is symmetric between SOURCE POINT C / LINE A and SOURCE POINT A / LINE C, and C/B similarly accepts SOURCE POINT C / LINE B and POINT B / LINE C. Both source orientations are evaluated on the SAME genuine six-incidence Q and count toward the raw 64-map historical class score. The historical non-D6 C/A and C/B classifier accepts any two-sided 2-regular six-coordinate physical projections with their source C/A or C/B multiplicity profiles; a pair of disconnected triangles is **not excluded** by a connectedness rule for these classes. The connected original sixcycle requirement applies to aligned A/A D6, not to all historic C/A. The previous intermediate independent tests incorrectly omitted reverse-source LINE-C orientation and then introduced a false C/A connectedness rule; those tests FAILED as designed and have been corrected to match the actual independent historical positive GF5 seven-class census, without weakening any high-order source-packet estimates.

## Exact falsification scope

Six independent hosted groups: (1) h1..36/40/48/64/80 BigInt/Fraction source fourth/fifth/sixth and weighted E_C; (2) all 64 original W32 lex/S72 complete global right maps and both historical GF5 class scores plus exact sixcube degree3 projections; (3) separate direct signed 64-state Walsh sums and opposite signed genuine weighted fourth coefficient; (4) independent COMPLETE 62,370 original left-eligible six-Q ×64 complete right maps, literal source point/LINE ID profiles and both physical six-coordinate degree2, no historical GF5 classifier or source packet prefilter; (5) real W34 symplectic GF4 with nononto K14 labels, original C/B f-only GQ source certificate unchanged by fully permuting g and all-h weighted s4 bound; (6) malformed genuine incidence/injections, wrong dyadic order, fewer/overlapping source LINE-factor swap pairs fail closed. One additional explicitly ABSTRACT degree1 zero-center countermodel is previously known (#587), not a true source-GQ Branch B claim. Exact finite W32 signed quantities are pinned after specialized CI.

**Strict research gate:** This is only TWO of SEVEN historical positive classes. The low-order projection P<=3 contains unrestricted signed original correlations and zero mode, so BX does NOT imply any positive original UNCHANGED f,g seven-class count, root Branch A, an infinite original correlated true W3 o(s^6) family (B), a qualifying full-seven Branch C equivalent reduction, or any complete strict R3/ASET exponent. Independent mathematical referee of #595 plus parent proof stack and exact final-HEAD hosted Dedicated/INDEX/Proof Audit/Full Research are required. Keep Draft, do not merge or change accepted registry/root #230.


## Final exact W32 weighted original seven-GF5 subsystem: authentic values and fixed-f error

The following numbers are **historically accepted positive GF5 C/A plus C/B including BOTH source orientations**, on genuine original symplectic W(3,2), with real globally injected pair-image maps f/g under six disjoint ORIGINAL LINE-factor pair-image swap packets (0,1),(2,3),(4,5),(6,7),(8,9),(10,11). Every cube state is a COMPLETE physical global right labeling, with the SAME six original source incidence IDs evaluated on both sides. The exact 51-column necessary R3 weights are 43320 and 49050.

| Genuine W32 labeling | ORIGINAL unchanged weighted center W_C(0) | Mean/zero mode over 64 complete maps | Sixcube marginal first-four-bit weighted Walsh | Max actual degree≥4 weighted residual | Original-f-only source-support E_f upper |
|---|---:|---:|---:|---:|---:|
| lex | 612210 | 5664375/16 | **−5415** | 284445/8 | 12798870 |
| S72 | 86640 | 1075035/8 | **+13695/8** | 197805/8 | 12288435 |

All five entries per labeling are pinned as exact-Fraction regression tests on the final HEAD. The SOURCE original-f-only cap is conservative at h=1, but it is independent of the original g labeling. The actual weighted high-order signed remainder is smaller, as expected.

The independent witness scan examines **all 62,370 historical original LEFT six-coordinate-eligible six-incidence-ID sets × ALL 64 complete right maps**, classifies source POINT C/LINE A OR POINT A/LINE C as C/A, and POINT C/LINE B OR POINT B/LINE C as C/B, and checks both physical typed projections degree2 on six physical coordinates. It does NOT call the production historical class method and does NOT prefilter high-order source packets. This scan agreed on every complete-map class count and on every weighted original subtotal. A spurious C/A connected-6cycle restriction would reject historically valid disjoint 2-regular physical patterns and is explicitly disallowed.

The negative lex weighted fourth coefficient and positive S72 weighted fourth coefficient are actual source-geometry signed counterexamples to the hypothesis of universal nonnegative weighted FOURTH-order source C/A+C/B response. They are NOT a negative original weighted score (both original centers are positive) and are NOT a seven-class Branch A counterexample or an infinite h family. The mathematical all-h theorem is only the uniform O(s5) control of ORDERS ≥4, leaving unbounded and potentially signed ZERO/LOWER orders and five other accepted source classes.
