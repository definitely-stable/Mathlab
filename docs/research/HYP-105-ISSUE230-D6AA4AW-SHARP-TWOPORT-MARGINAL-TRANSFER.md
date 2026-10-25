# HYP-105 / #230 — AA4-AW: SHARP true-original GOOD two-port marginal transfer

**Research-only restricted all-h theorem; original #230 Branch A/B/C still OPEN.** Strict Draft child of [AA4-AV #554](https://github.com/definitely-stable/Mathlab/pull/554), frozen parent SHA c877702263d7dc1d94f4a374495a86ec49685445. All quantifiers refer to the ONE genuine original symplectic W(3,s), s=2^h≥2, and the SAME arbitrary fully globally injected correlated physical source-factor point map f and line map g on all true original incidence flags. No source redrawing, statistical independence, or false fully selected seven-GF5 lower.

## 1. What is already known

Prior [AA4-AR #543](https://github.com/definitely-stable/Mathlab/pull/543) established the exact original GOOD D graph physical point/line four-bin color counts x00,x01,x10,x11 and opposite-typed centered 3-flag wedge count R=x00·x11+x01·x10, including the equivalent four-port polarized quadratic identity. **Those facts and their underlying combinatorics are NOT claimed new here.** Prior [AA4-AV #554](https://github.com/definitely-stable/Mathlab/pull/554) proved a genuine original GOOD source A/A 3-flag wedge reservoir W_AA≥s⁶/10 for all arbitrary complete original global f,g when h≥16, and exact original source-incidence corrected physical FᵀBG 2×2 port transport. It did **NOT** prove a positive universal count of opposite physical ports. Prior [#546](https://github.com/definitely-stable/Mathlab/pull/546), [#551](https://github.com/definitely-stable/Mathlab/pull/551) and [#552](https://github.com/definitely-stable/Mathlab/pull/552) already define the additional residual three-source-flag physical T/P and true original 3×3 Hall conditions, still required after any opposite-typed wedge.

**New AA4-AW contribution:** determine the exact SHARP integer lower on R_i when only the true-original GOOD point-port TWO MARGINAL counts and line-port TWO MARGINAL counts are fixed, prove a sharp uniform half-minority-product transfer, give a local activation IF AND ONLY IF, and freeze which marginal condition must be proved in the source geometry to move toward #230.

## 2. Exact sharp integer fixed-marginal opposite-port theorem

For a genuine original source incidence center flag i=(p,l), globally assigned point physical pair f(p) has two ports and line physical pair g(l) has two ports. Let x00,x01,x10,x11 be counts of real true original GOOD D neighboring flags by their unique shared physical point/line coordinate ports with i. Each is a nonnegative integer. Define physical point marginals r0=x00+x01 and r1=x10+x11; physical line marginals c0=x00+x10 and c1=x01+x11; common degree D=r0+r1=c0+c1.

Given **only** the four marginal numbers, EVERY feasible 2×2 integer table has one integer degree of freedom t=x00, in the sharp interval
\[
L=\max(0,r_0+c_0-D)\le t\le U=\min(r_0,c_0),
\]
and entries (t,r0−t,c0−t,D−r0−c0+t). Hence true same-center opposite typed physical GOOD wedge count is the exact integer quadratic
\[
R_i(t)=2t^2+(D-2r_0-2c_0)t+r_0c_0.
\]

**AA4-AW1 NEW sharp all-h local marginal lower:**
\[
\boxed{
R_i\ge\mathfrak F(r_0,r_1;c_0,c_1)
:=\min_{t\in\mathbb Z\cap[L,U]}R_i(t).
}
\]
The real quadratic vertex is \(t_*=(2r_0+2c_0-D)/4\); the integer optimum is attained at either clipped floor(t*) or clipped ceil(t*), or a boundary L/U. At most FOUR integer candidate calculations give an EXACT minimum, for arbitrarily large genuine original source degree D. Every extremal formal table is explicitly constructible from its chosen t, so the bound is SHARP among all local integer tables with those margins. **This is NOT an assertion that every formal local extremal table can appear as a globally coherent true-original f,g assignment.**

## 3. Sharp half-minority-product lower and activation iff

Let a=min(r0,r1), b=min(c0,c1), with point and line port orientations freely exchanged. Arrange r0=a,c0=b and D≥2max(a,b). Then for t≥0,
\[
R_i(t)=ab+2t^2+(D-2a-2b)t
 \ge ab+2t^2-2mt
 = ab-\frac{m^2}{2}+2(t-\frac m2)^2
 \ge\frac{ab}{2},
\]
where m=min(a,b). Since R_i is an integer,
\[
\boxed{R_i\ge\mathfrak F_i\ge
 \left\lceil\frac{\min(r_0,r_1)\min(c_0,c_1)}2\right\rceil.}
\]
**The coefficient 1/2 is BEST POSSIBLE:** take all four bins equal to any integer t>0. Then marginals are 2t/2t on each type and the actual opposite count is 2t², exactly the displayed half-minority product.

A genuinely useful strictly SOURCE/physical statement is the new all-h local zero **iff**:
\[
\boxed{
R_i>0\ \Longleftrightarrow\
\min(r_0,r_1)>0\ \text{AND}\
\min(c_0,c_1)>0.
}
\]
If one typed port marginal is monochromatic, the real original source GOOD neighbors occupy only one physical point row or line column, and R_i=0. Conversely both typed margins positive force a positive integer R_i≥1. Every such opposite-typed true original GOOD 3-flag wedge automatically has THREE DIFFERENT true original source point factors and THREE different original source line factors; it does not automatically extend to a positive true-original six-incidence-ID GF5 class.

## 4. Deterministic all-global source W(3,s) pre-Hall transfer

Sum over ALL actual original incidence flag ID centers i in the SAME globally injected W(3,s) model with fixed physically correlated global maps f,g:
\[
\boxed{
R_{\rm GOOD}(f,g)
\ge\sum_i\mathfrak F_i
\ge\sum_i\left\lceil\frac{m_i^P m_i^L}{2}\right\rceil
\ge\frac12\sum_i m_i^P m_i^L,
}
\]
where \(m_i^P=\min(r_{i0},r_{i1})\), \(m_i^L=\min(c_{i0},c_{i1})\) are the two **separately physical-port-minority** counts at that genuine source center. In particular the count of source incidence centers with BOTH point ports and BOTH line ports populated by GOOD D neighbors is a lower bound on R_GOOD; centers lacking activity on at least one typed side have R_i=0. This is a deterministic exact all-h transfer, not a conditional expectation or source-forest incidence upper.

**Precisely open frontier:** if one subsequently proves \(\sum_i m_i^P m_i^L\ge\delta s^6\) for EVERY fixed genuine original globally injected correlated f,g, the new inequality immediately yields \(R_{\rm GOOD}\ge(\delta/2)s^6\). AA4-AV's guaranteed SOURCE AA GOOD wedge \(s^6/10\) does NOT currently imply such a port-minority-product lower: source factor distinctness alone allows a physical port concentration on one row/column. Even a positive R_GOOD remains a THREE-flag pre-Hall object; no deterministic lower on accepted original GF5 six-Q follows without the additional three-flag T/P physical residual, genuine original 3×3 Hall Boolean and final GF5 alignment gates. Root #230 universal seven-class lower and counterfamily branches remain OPEN.

The already known AA4-AR polarized quadratic can be recast for independent verification as \(8R_i=D_i^2+C_i^2-A_i^2-B_i^2\), A_i=r0−r1, B_i=c0−c1, C_i=x00+x11−x01−x10. This is an **equivalent prior identity**, NOT another new theorem.

### Frozen actual-original W(3,2) and W(3,4) pre-Hall source/physical frontier

One source-GQ 3flag literal neighbor-pair oracle (without marginal convex minimization) independently counted actual opposite typed GOOD wedges and source A/A GOOD wedges on seven SAME, globally complete typed f,g schemes, and the exact marginal solver certified its lower from the locally separately measured original GOOD D point and line physical endpoint counts. No per-Q physical map redraw, and W34 typed physical supports contain six globally missing K14 edges each.

| Genuine ORIGINAL fixed typed f,g | GOOD real D edges | Source A/A GOOD centered 3flag wedges | Actual two-typed physical OPPOSITE GOOD 3flags | **SHARP marginal-only lower** | Half-minority sum lower | Source centers with BOTH physical port types active |
|---|---:|---:|---:|---:|---:|---:|
| W32 dual-zero | 277 | 2,675 | **870** | **821** | 652 | 45 / 45 |
| W32 lex | 307 | 3,259 | **1,105** | **1,000** | 794 | 45 / 45 |
| W32 reverse | 300 | 3,141 | **1,013** | **968** | 784 | 45 / 45 |
| W32 S68 | 257 | 2,268 | **697** | **683** | 509 | 45 / 45 |
| W32 S72 | 261 | 2,346 | **750** | **714** | 545 | 45 / 45 |
| W34 lex | 2,072 | 20,650 | **3,544** | **3,174** | 2,183 | 118 / 425 |
| W34 random | 147 | 158 | **10** | **8** | 6 | 6 / 425 |

These finite results are source-backed **exact integers**, not an asymptotic fit. The first five true W32 physical maps all have 45 physically two-port-active source flag centers, while only 118 of 425 true W34 lex and SIX of 425 true W34 random centers are two-port active. Thus the W34 random original **AA-to-opposite physical-port lift** is 10/158, with marginal-only forcing 8/10 of those surviving opposite 3flag wedges. The large loss 158→10 occurs before the independent actual original 3×3 forest Hall and historical positive sevenclass GF5 acceptance gates. Finite W34 random loss cannot be asserted as a universal high-h correlated counterfamily.

The source AA reservoir alone therefore provides **no positive universal two-typed port-minority product bound** at the current research frontier. Sharp marginal forcing can be nearly tight (S68 683/697, S72 714/750) while a small minority-product mass still blocks global sixmotif lower. An actual all-h result controlling this sum from source incidence spectral geometry rather than sampled finite schemes is the next significant unresolved transition.

## 5. Independent falsifiers, exact scopes and scientific gates

Four additive files: mathematical executor, independent 8-test suite, this proof/source-prior-art Markdown and GitHub-hosted dedicated workflow.

- **Exhaustive all integer 2×2 margins D=0,…,18:** enumerate independently EVERY feasible nonnegative table for each pair of point/line two-port margins. Verify O(1) clipped-convex exact integer minimum, the feasible minimizing table, sharp half-minority bound, local activity iff and typed-port row/column interchange symmetries. Several thousand distinct marginal cases, plus explicit coefficient-1/2 tightness witnesses.
- **Genuine true-original full W32 K6** typed global maps dual-zero, lex, reverse, S68, S72: calculate ALL source GOOD D four physical port bins at every actual source incidence center; independently enumerate literal TRUE original triple wedges and check physical opposite source point/line distinctness, prior AA4-AV exact source AA/BA/AB wedge counts, and true original ALL-D source-incidence corrected FᵀBG tensor upper. Freeze actual opposite counts, exact sharp marginal-only lower, half-minority floor and center activity from CI, not fabricated prior to execution.
- **Genuine original W34 GF4**, lex/random physically nononto K14 with six physical missing edges per typed global source map: count all 425 actual source incidence centers, verify same-global physical margins, literal independent 3-flag opposite and all true-original GOOD wedges, no pretend complete W34 selected seven-Q census.
- Genuine original source symplectic automorphism and independent point versus line physical coordinate permutations preserve the exact center-wide marginal forcing energy and global actual opposite GOOD source wedges.
- Exactly rational all-h AA4-AV source A/A GOOD s6/10 theorem h≥16 already proved upstream, compared here with a clearly marked **CONDITIONAL assumed** port-minority mass. We do not fabricate high-order symplectic finite source fixtures.
- Fake incomplete original source incidence, noninjective full physical source factor images, inconsistent typed marginal totals, negative/non-integer entries fail closed. Abstract one-row-only local tables show that high source A/A wedge mass need not force physical opposite-typed port pairs absent additional true global restrictions; no fake infinite original counterfamily claimed.

**Acceptance:** strict research-only Draft child of #554 at exact pinned parent SHA. Need exact final-head dedicated/INDEX/Proof Audit/Full Research green **and separate independent mathematics referee** before scientific acceptance, SHA-pinned canonical RCP JSON or generation of five derived Markdown registries. Main unchanged, root issue #230 OPEN. **Next AA4-AX** must prove a uniform bound on the original GQ mixed point-line typed-port minority product for every correlated globally complete f,g, or find a genuine infinite obstruction, then pass the independent true-original residual T/P Hall seven-GF5 selection gates.
