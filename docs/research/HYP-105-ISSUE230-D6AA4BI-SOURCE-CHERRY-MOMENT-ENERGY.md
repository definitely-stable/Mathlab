# HYP-105 / #230 — AA4-BI: source-cherry differential moments and positive seven-GF(5) bounds for every fixed original f,g

**Research Draft, not an accepted solution of Branch A/B/C.** Strict child of [AA4-BH PR #573](https://github.com/definitely-stable/Mathlab/pull/573), frozen parent HEAD c65ae0c49b9b4387638b8d4ffcf5b908bdf71846. This result must be read against the true-original original-incidence root [issue #230](https://github.com/definitely-stable/Mathlab/issues/230), not as a new universal 7class positive lower.

## 1. Exact frontier and prior mathematics

Existing work already establishes:
- [#534](https://github.com/definitely-stable/Mathlab/pull/534), the genuine-original two-sided six-incidence join, with scalar seven-class positivity identity S=J−AA+D6 and forbidden original C/C GQ source sixcycle.
- [#539](https://github.com/definitely-stable/Mathlab/pull/539), the D6⇔true-original bicolored-rainbow C6 equivalence.
- [#572](https://github.com/definitely-stable/Mathlab/pull/572), the squarefree matrix trace Tr(A_D^6)=12D6 for every completely fixed original f,g.
- [#573](https://github.com/definitely-stable/Mathlab/pull/573), the coefficientwise physical (P,L) local version S[P,L]=J[P,L]−AA[P,L]+D6[P,L]. The present work does NOT assert that these earlier identities are novel.
- [#530](https://github.com/definitely-stable/Mathlab/pull/530), an alternative TRUE original source D-anchor E+unanchored U equivalent-positivity reformulation; a different but legitimate prior reduction.
- [#554](https://github.com/definitely-stable/Mathlab/pull/554), positive original A/A GOOD THREEflag wedge counts for large h, without automatically implying original accepted six-GF5 S.

**NEW narrow objective:** replace potentially large subtraction J−AA with an EXPLICIT POSITIVE FIRST SOURCE-CHERRY COLLISION MOMENT on the SAME genuine-original source sixflag sets and the SAME completely fixed original f,g. Prove a nonlinear second-moment lower that can be stronger than the worst-case constant, reconstruct actual seven-class GF5 certified risk from at most four collision strata plus ONE original B/B overlap bit, and give a concrete all-h true-original differential-operator extraction. This is a quantitative certificate/proof-method target, NOT a new root uniform bound.

## 2. Quantifiers and real original source

Fix EVERY dyadic s=2^h, h>=1, the true symplectic generalized quadrangle W(3,s) with genuine bipartite point–LINE original incidence set I and original factor valency d=s+1. Fix ANY two COMPLETE globally injected physical unordered pair-edge original factor maps f and g (including arbitrary adversarial correlation with each other and the GQ incidence), with minimal physical typed coordinate-palette size a, binom(a,2)>=V=(s+1)(s²+1). Fix ANY two SIX-element physical coordinate sets P for original point projections and L for original LINE projections; the palettes are independent typed symbols.

Let J[P,L] be the family of SIX DISTINCT actual original source incidence flag IDs Q such that BOTH projections have exactly six physical coordinates of degree exactly TWO on the chosen physical sets P,L, respectively. This is exactly the fixed original two-sided selected 2regular six-Q *join*, not the historically seven-positive family until the A/A condition is resolved.

For a six-Q in J[P,L], define the **TRUE ORIGINAL source-cherry charge**:

\[
\boxed{
c(Q)=\sum_{p\in\mathrm{POINT}(W)}{\binom{n_p(Q)}2}
+\sum_{\ell\in\mathrm{LINE}(W)}{\binom{n_\ell(Q)}2}.
}
\tag{BI-C}
\]

Here n_p(Q), n_l(Q) are the numbers of actual ORIGINAL incidence flags among the selected Q sharing a given original point or LINE factor. A pair-edge factor's two physical coordinates can each have degree at most two in the projection, so n_p,n_l<=2 on ANY Q in J[P,L]. All original physical source multiplicity types must be A=(1^6), B=(2,1^4), or C=(2,2,2) on each side, giving individual source cherry charges 0,1,3 respectively. Two source type C simultaneously would induce a forbidden source original sixcycle in the true W(3,s) girth-eight bipartite incidence graph. Therefore, **for all h and every fully fixed f,g,**

\[
\boxed{c(Q)\in\{0,1,2,3,4\}.}
\tag{BI-CAP}
\]

- c=0 iff original A/A (six distinct source point and six source LINE factors), which is seven-GF5 positive only when the historical D6 two-typed sixcycle alignment is fulfilled.
- c=1 iff B/A or A/B (two distinct accepted historical classes).
- c=2 iff B/B (overlap or disjoint source repeated-factor incident flag subsets).
- c=3 iff C/A (either orientation).
- c=4 iff C/B (either orientation).
- Original C/C c=6 is strictly impossible. There is no c=5 true-original joined six-Q.

Thus **every Q with c>0 is one of the SIX accepted non-D6 original GF5 classes.** c=0 can include either rejected unaligned A/A or positive D6, handled separately by prior #572 squarefree typed physical trace.

## 3. AA4-BI1 — four exact positive-original source-cherry factorial moments

For a fixed physical coordinate fiber P,L, let

\[
M_k(P,L)=\sum_{Q\in J[P,L]}\binom{c(Q)}k,
\quad k=1,2,3,4;
\qquad
Q_2(P,L)=\sum_{Q\in J[P,L]}c(Q)^2
=M_1+2M_2.
\]

Write N[P,L] for the ACTUAL seven-GF5-positive non-A/A count, which prior #573 already identified as J[P,L]−AA[P,L]. Because c only takes values 0..4, the exact elementary binomial identity sum_(k=1)^4 (-1)^(k+1) binom(c,k)=1[c>0] yields a NEW physical-fiber integer formula with no A/A subtraction:

\[
\boxed{
N[P,L]=M_1(P,L)-M_2(P,L)+M_3(P,L)-M_4(P,L).
}
\tag{BI-EXACT}
\]

Combining with prior exact true-original sixflag squarefree two-color trace T[P,L]=12 D6[P,L]:

\[
\boxed{
S_{\mathrm{seven}}[P,L]
=M_1-M_2+M_3-M_4+T[P,L]/12.
}
\tag{BI-SEVEN}
\]

This remains exact for EVERY already fully fixed original physical f,g at ALL dyadic h. No favorable original LINE permutation and NO independence of source Q events is introduced. The positive-source factor charge c records only ORIGINAL repeated factor IDs; it is not an artificial physical point-coordinate collision.

## 4. AA4-BI2 — nonlinear variance-sensitive positive lower certificate

Write C=M1 and Q2=M1+2M2 for one physical sixcoordinate fiber. By Cauchy–Schwarz over the finite joined original Q:

\[
C^2=\left(\sum_{c(Q)>0}c(Q)\right)^2
\le\#\{Q:c(Q)>0\}\sum_{Q:c(Q)>0}c(Q)^2
=N Q_2.
\]

Consequently, for Q2>0,

\[
\boxed{
S_{\mathrm{seven}}[P,L]\ge
D6[P,L]+\frac{M_1(P,L)^2}{M_1(P,L)+2M_2(P,L)}
\ge D6[P,L]+\frac{M_1(P,L)}4 .
}
\tag{BI-LOWER}
\]

When Q2=0, interpret the rational lower as 0. The nonlinear first/second source-collision-moment bound is AT LEAST as strong as the flat 1/4 first-moment bound, and strictly stronger whenever the actual joined nonzero source-cherry distribution has values below four. The direct upper follows from every nonzero c>=1:

\[
\boxed{
D6[P,L]+\tfrac14M_1[P,L]\le
S_{\mathrm{seven}}[P,L]\le
D6[P,L]+M_1[P,L].
}
\tag{BI-SANDWICH}
\]

Unlike J−AA, this lower asks for an explicit POSITIVE cherry energy M1 and its second moment, which may be more amenable to true GQ neighbor-expansion or two-type physical source-incidence cell techniques. **NO positive uniform all-h M1 or D6 lower is proved**. If both vanish in one fiber, that fiber has no selected original GF5 six-Q.

Summing over all P,L preserves these bounds. Thus, with globally summed M1 and D6:

\[
\tfrac14(M_1^{tot}+D6^{tot})\le S_s(f,g)\le M_1^{tot}+D6^{tot}.
\]

This gives the precise *constant-factor equivalence* of any eventual original Branch A \(\Omega(s^6)\) lower, or original Branch B \(o(s^6)\) upper, with corresponding claims about **M1^{tot}+D6^{tot}** on the SAME full source f,g. It is a candidate proof target; a simple exact restatement or reduction does NOT pass the root Branch C acceptance gate without a nontrivial new bound or explicit hardness barrier.

## 5. AA4-BI3 — sharp original 51-column GF5 lower-risk sandwich

Let W[P,L] be the original certified strictly POSITIVE seven-class GF5 numerator appearing in root #230:

- D6 source class weight: 5643.
- B/A and A/B weight: 45600 each.
- C/A: 43320.
- C/B: 49050.
- B/B overlap: 51750.
- B/B disjoint: 45010.

For joined Q with c>0, its certified numerical weight divided by c is 45600 for c=1, either 51750/2 or 45010/2 for c=2, 43320/3 for c=3, and 49050/4 for c=4. Therefore the two universal extreme classwise constants are

\[
\boxed{
\frac{49050}{4}\,M_1[P,L]+5643D6[P,L]
\le W[P,L]
\le 45600\,M_1[P,L]+5643D6[P,L].
}
\tag{BI-GF5}
\]

The two constants are SHARP **on the abstract list of permitted source classes**: the lower is attained by pure C/B charge-four and the upper by pure B/A charge-one. No claim that these extremizers are available as whole globally labeled W(3,s) families for every h, or even each local physical P,L, is made. The actual class-resolved risk can be recovered EXACTLY from the collision histogram H_j=#Q with c=j, j=1..4 and the extra original B/B incidence overlap count O_BB:

\[
W=5643D6+45600H_1+
51750O_{BB}+45010(H_2-O_{BB})
+43320H_3+49050H_4.
\]

This is an exact original R3 **necessary selected-seven-GF5 floor numerator**, NOT all of R3 and NOT an ASET exponent. It remains for every full fixed original f,g and preserves the same six actual original incidence flag IDs on both typed physical projections.

## 6. AA4-BI4 — one genuine-original incidence generating product differential operator

Set physical X_{f(p)}=x_u x_v for point image {u,v}, and Y_{g(l)}=y_e y_t for LINE image {e,t}. Introduce ORDINARY commuting source tags z_p and w_l, one for each real original point and LINE source factor ID, and use the genuine-original incidence generating product

\[
H(t,\mathbf x,\mathbf y,\mathbf z,\mathbf w)
=\prod_{(p,l)\in I}
(1+t\, z_p w_l X_{f(p)}Y_{g(l)}).
\]

The source tags here remain ORDINARY until the differential operator is evaluated (do NOT impose z_p²=w_l²=0 before calculating cherries, or the very repetitions under study would disappear). Denote source Euler operators E_p=z_p d/dz_p and F_l=w_l d/dw_l. Define the integral-valued quadratic differential operator

\[
\boxed{\mathscr C =
\sum_p\frac{E_p(E_p-1)}2+
\sum_l\frac{F_l(F_l-1)}2.}
\]

On the monomial encoding each genuine selected original sixflag Q, \(\mathscr C\) acts by scalar multiplication by exactly c(Q). For each j=1..4, define the operator-valued binomial polynomial \(\binom{\mathscr C}{j}\) and apply it BEFORE setting source tags to 1; evaluating source tags afterward is an ordinary polynomial evaluation, not an invalid homomorphism from a square-zero ring. The all-h exact physical source coefficient formula is

\[
\boxed{
M_j[P,L]=
[t^6\,x_P^2 y_L^2]\;
\left.\binom{\mathscr C}{j}H
\right|_{z_p=w_l=1\ \forall p,l}.
}
\tag{BI-DIFF}
\]

Thus the original incident tensor and both complete physical maps enter one single product, and the new positive collision moment has an EXPLICIT differential-operator extraction rather than a need to subtract an almost equally large A/A coefficient. This identity is a finite polynomial identity valid for every source W(3,s) all h and every original physical coordinate P,L; evaluating high-h coefficients efficiently remains open.

## 7. Reproducible ORIGINAL W32/W34 falsifiers

The new source enumerator does NOT take selected historical seven-GF5 tags or the previous AA4-BH classification as input. For a specified fixed six-coordinate POINT set P, it independently builds real occupied physical six-edge 2regular source multigraph patterns, inverses complete fixed f to REAL original point factors, chooses real original distinct incidence flag IDs using actual source W(3,s) neighborhoods (1 flag if physical pair edge occurs once, 2 different flags if twice), then screens the SAME full original g for a six-coordinate degree-two LINE projection. It groups surviving joined real source six-Q by actual physical L and computes source cherry c independently from literal source point/line counts, four moments, Cauchy lower, B/B overlap and classwise GF5 necessary risk.

Independent tests:
1. Real original W32 full typed f,g for dual_zero, lex, reverse, S68, S72: separately construct two original A/B/C half-Q maps and intersect their ACTUAL six-incidence-ID sets; independently compute each Q's source cherry to verify histogram and B/B overlap. Compare total joined J, A/A, and complete seven GF5 count/weighted numerator against previous two-sided join and independently historical selected original seven_census; D6 independently from parent #572 trace. The second-moment bound is required to be strict beyond C/4 on at least one actual original W32.
2. Genuine W32 S68/S72 D6=0 but source cherry C>0 and positive Cauchy sevenclass lower for the SAME already fixed original global pair f,g; this shows an actual sevenclass compensation source, not a fake graph.
3. Real original W34 symplectic s=4, nononto K14, complete globally injected typed physical lex/random original f,g; fix P=(0,1,2,3,4,5) and compare every populated physical L coefficient J, A/A, non-AA sevenGF5 count and exact class-resolved 51-column risk against the INDEPENDENT prior #573 sevenGF5 physical-local compiler, but this BI enumerator NEVER consults selected GF5 tags during its computation.
4. All five allowed positive original source collision strata 1,2 overlap/disjoint,3,4 tested as separate exact small **classwise numerical** cases for exact 51-palette risk and the lower/upper ratio constants. They are not fake high-order source GQ fixtures.
5. All dyadic h=1..35 plus 40,48,64,80 verify integer parameter and exact formal all-h domain, with explicit failure markers for absent universal lower or root-C acceptance.
6. Original incidence factor degree/physical global injection corruption, bad typed six-coordinate masks, repeated original source flags and source IDs fail closed.

## 8. Limits and next scientific gate

This step DOES NOT derive a uniform lower M1^{tot}>=c s^6 when D6=0. Nor does it prove one of the sevenGF5 six-incidence classes must carry Omega(s^6) for every already fixed full f,g; no infinite original correlated all-seven counterfamily; no valid root A/B/C closure; no R3/ASET exponent. The classical binomial inversion, Cauchy and Euler derivative principles are credited as classical; the only scoped project-specific content is the true original W3 source-cherry weight c<=4, same-global-f/g exact differential physical-fiber certificate, numerical exact GF5 classwise risk and finite independent source checks.

**Next root-facing problem:** prove or refute a genuine-original, ALL-FIXED global source-cherry mass vs bicolored D6 compensation inequality

\[
\boxed{
M_1^{tot}(f,g)+\tfrac1{12}\Lambda Tr(A_D(f,g)^6)
\stackrel{?}{\ge}c\,s^6
}
\]

for one universal c>0 and all h sufficiently large. A proof would close root Branch A through BI-SANDWICH; a rigorous infinite genuine original f,g family giving little-o of BOTH terms would close root Branch B. Simple finite W32 checks or this exact local identity do neither. Investigate true GQ incidence expansion / physical two-type 3x3 Hall coupling rather than increasing random-map pinned continuation fractions.

**Acceptance:** keep Draft, no main/accepted registry edits. Need exact final-HEAD hosted specialized, INDEX, Proof Audit, Full Research SUCCESS; independent mathematical referee and parent stack gate prior to merge or scientific acceptance. Historical #573 Full Research was CANCELLED on earlier HEAD; do not promote merely because this specific math CI passes.
