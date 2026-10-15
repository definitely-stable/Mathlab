# HYP-105 / issue #230 — AA4-AM: all-map true-original triple transport and degree-three non-lift

**Status: research-only restricted ALL-h theorem, not Branch A/B/C.** Child of [AA4-AL coordinate transport PR #529](https://github.com/definitely-stable/Mathlab/pull/529), pinned EXACT parent SHA \`8e5763dea0f95ad9959a3050be47f8aa078c2334\`. Every statement concerns the **actual symplectic W(3,s)** source incidence for s=2^h≥2 and two separately TYPED, complete GLOBAL original-factor injective physical pair maps f:P→E(K_a), g:L→E(K_a), reused unmodified for EVERY original incidence. \(V=(s+1)(s²+1)\), \(d=s+1\), \(a=\min\{t:\binom t2\ge V\}\). No random maps, no independence of original flags, no source relabel by artificial model.

## 1. Prior art and what is new

- Parent [AA4-AL #529](https://github.com/definitely-stable/Mathlab/pull/529) **already** defines the exact physical coordinate two-type transport \(M=F^\top B G\), \(M_{xy}=\#\{(p,\ell)\in I(W(3,s)):x\in f(p),y\in g(\ell)\}\) and proves every-global-map \(\Omega(s^5)\) **two**-flag physical bicoincidence. Its classical Cauchy/ANOVA, original regular incidence spectrum, source-degenerate two-flag corrections and actual W32/W34 finite oracles are not new here.
- Earlier [AA4-AK #524](https://github.com/definitely-stable/Mathlab/pull/524), [#525](https://github.com/definitely-stable/Mathlab/pull/525), [AA4-AL #527](https://github.com/definitely-stable/Mathlab/pull/527) already decompose real ORIGINAL selected GF5 B/A and A/B full physical A cases and give **upper** per anchored B/C4 accepted six-Q, with source Hall-girth8 constraints. A physical bicoincidence does not automatically pass the 2-regular accepted GF5 degree gate.

**New mathematical object:** third *FACTORIAL* moment of the single common two-global-map transport \(M\), with exact removal of triples concentrated at one original point or one original line. **New quantified restricted theorem:** at least \(4V(s+1)^3\ge4s^6\) ORDERED triples of distinct ACTUAL original incidence flag IDs, with at least two different actual original point IDs and two different actual original line IDs, that simultaneously share a physical coordinate in each typed projection. All h and EVERY f,g, rather than just finite true W32 evidence. **New explicit non-lift:** every such mixed triple already has physical coordinate multiplicity at least three in BOTH typed projections, and therefore cannot be contained in a six-flag pattern whose projection is physically 2-regular. This is NOT a seven-GF5 selected six-incidence \(\Omega(s^6)\) proof.

## 2. Exact original-source triple-coincidence definition

Let \(\mathcal I=\{(p,\ell):p\in\ell\}\) be the **ACTUAL** original \(Vd\) incident flag IDs (each \(p,\ell\) pair unique). Every true source flag \(e=(p,\ell)\) belongs to exactly FOUR physical coordinate cells \((x,y)\in f(p)\times g(\ell)\), and the same globally injected labels occur everywhere. The parent genuine transport is

\[
M_{xy}=\#\{(p,\ell)\in\mathcal I:\ x\in f(p),\ y\in g(\ell)\},
\qquad
\sum_{x,y} M_{xy}=4Vd.
\]

For an integer t≥0 define \((t)_3=t(t-1)(t-2)\) (zero for t=0,1,2). Then the exact third factorial transport

\[
T_3(f,g):=\sum_{x,y}(M_{xy})_3
\]

counts ordered triples \((e_1,e_2,e_3)\) of **THREE DISTINCT genuine original incidence FLAG IDs** together with a common physical point-coordinate x and common physical line-coordinate y. No source incidence selection is redrawn or independently replicated.

If all three actual flags share one original point p, their original line factors are automatically distinct. For each y define \(r_{p,y}=\#\{\ell\in N(p):y\in g(\ell)\}\). Such a triple shares both physical types precisely when these three line labels share y; the common original point label f(p) contributes TWO choices of x. Thus its EXACT multiplicity in \(T_3\) is

\[
A_P=2\sum_{p}\sum_y(r_{p,y})_3.
\]

Dually, for each real original source line ℓ let \(r_{\ell,x}=\#\{p\in N(\ell):x\in f(p)\}\) and

\[
A_L=2\sum_{\ell}\sum_x(r_{\ell,x})_3.
\]

All-same-p and all-same-ℓ are DISJOINT among triples of DIFFERENT original flags (three flags cannot have both the same p and ℓ). Their exact removal leaves

\[
\boxed{\mathcal T_{\ge2,\ge2}(f,g)=T_3(f,g)-A_P-A_L.}
\]

This is an exact integer identity, not a probabilistic approximation. The retained triples involve at least TWO different original point source IDs and at least TWO different original line source IDs. Because any two different original points have two different globally assigned physical unordered pair edges whose intersection has size ≤1, and likewise for two different original lines, every retained triple has ONE UNIQUE physical coordinate pair (x,y). Hence this counts ORDERED actual original flag triples **once**, not coordinate-cell or source automorphism orbits. The unordered count is \(\mathcal T_{\ge2,\ge2}/6\).

**Important quantifier distinction:** at least 2 original point IDs and at least 2 original line IDs among the 3 flags does **NOT** mean all three source point IDs are pairwise distinct, nor all three line IDs pairwise distinct. The stronger \((3,3)\) subset is measured in finite tests but is NOT claimed positive uniformly in this theorem.

## 3. New AA4-AM-1: exact nonnegative Jensen third factorial transport

Let \(\mu:=4Vd/a²\), the exact physical coordinate-cell mean. For \(f(t)=t(t-1)(t-2)\), its exact tangent-remainder identity at \(\mu\), for every integer entry \(n\ge0\), is

\[
f(n)-f(\mu)-f'(\mu)(n-\mu)
=(n-\mu)^2(n+2\mu-3).
\]

Because \(\sum(M_{xy}-\mu)=0\), summing gives the EXACT nonnegative energy identity

\[
\boxed{
T_3=
a²\mu(\mu-1)(\mu-2)
+\sum_{x,y}(M_{xy}-\mu)^2(M_{xy}+2\mu-3).
}
\]

For every allowable order s=2^h≥2, \(\mu\ge5\) by the minimal physical alphabet lemma below; thus the remainder is nonnegative **for all integer entries including zero**, and no false Jensen application to nonconvex small-t domain is needed. Therefore, with no independence assumptions,

\[
\boxed{T_3\ge a²\mu(\mu-1)(\mu-2).}
\]

This is a physically two-typed ORIGINAL incidence transport theorem. Jensen is elementary prior art; the novel restricted content here is its exact globally coherent true-GQ and source degeneracy application, not claiming a novel general probabilistic inequality.

## 4. New AA4-AM-2: all-h global physical alphabet inequality

For every s=2^h≥2 with minimal a, we prove

\[
\boxed{5a²\le12V.}
\]

- At s=2, \((V,a)=(15,6)\), equality: 5·36=12·15.
- At s=4, \((V,a)=(85,14)\): 5·196=980≤1020.
- For s≥8, V≥585, a≥35. Minimality gives \(V>\binom{a-1}2\). Since \(a²-18a+12\ge0\) for a≥18, \(a²\le\frac65(a-1)(a-2)<\frac{12}5 V\).

Consequently \(\mu=4Vd/a²\ge(5/3)d\ge5\).

No fictitious full K_a surjectivity is used: the actual global label images have precisely \(\binom a2-V\) missing physical unordered pairs, and the proof needs only global completeness and alphabet minimality.

## 5. New AA4-AM-3: genuine original source repetition costs and the uniform \(\Omega(s^6)\) triple bound

Fix ONE genuine original point p. Its d genuine original line neighbors \(\ell\in N(p)\) are d **different** original factors, hence g assigns them d **different** physical unordered edges. For ANY ordered triple of three different such original lines, the intersection of their three g-images has at most ONE physical coordinate: two globally assigned different edges cannot share two coordinates. Therefore

\[
\sum_y(r_{p,y})_3\le(d)_3.
\]

The repeated original point contributes two possible physical x coordinates, so

\[
A_P\le2V(d)_3.
\]

By genuine ORIGINAL point/line degree regularity and the same global edge injection, also \(A_L\le2V(d)_3\). Thus

\[
\boxed{\mathcal T_{\ge2,\ge2}\ge a²\mu(\mu-1)(\mu-2)-4V(d)_3.}
\]

Since \(\mu\ge5d/3\) and \(\mu(\mu-1)(\mu-2)=\mu(\mu-1)(\mu-2)\) with \(\mu\ge5\), substitution \(\mu a²=4Vd\) yields

\[
\begin{aligned}
\mathcal T_{\ge2,\ge2}
&\ge4Vd\left[
\left(\frac{5d}{3}-1\right)\left(\frac{5d}{3}-2\right)
-(d-1)(d-2)
\right]\\
&=V\left(\frac{64}{9}d³-8d²\right)\\
&\ge\boxed{4Vd³}
\ge\boxed{4s^6}.
\end{aligned}
\]

The penultimate inequality holds for EVERY integer d≥3 because \(\frac{28}{9}d-8\ge\frac43>0\). Final \(V\ge s³,d\ge s\) holds for genuine W(3,s). The ordered count is divisible by six; the corresponding unordered mixed genuine original triples are at least \(\frac23s^6\), up to integer rounding.

**Scope exactly:** a positive universal count of three distinct original flag IDs with ≥2 point IDs and ≥2 line IDs, shared physical coordinate on BOTH sides. NO selected GF5 six-incidence Q count is claimed.

## 6. New AA4-AM-4: formal non-lift to physically degree-two GF5 gateway

For every counted mixed triple, all THREE selected actual original flags have a common point-side physical coordinate x and all THREE have a common line-side physical coordinate y. Their physical multigraphs (counting each incident flag's pair image with multiplicity) already have \(\deg(x)\ge3\) and \(\deg(y)\ge3\).

Adding three more original flags to form six cannot REDUCE a physical coordinate degree. Therefore **no six-flag extension containing this mixed triple can have a degree-two physical multigraph on EITHER typed side**. In particular, such a triple is not directly chargeable to any B/A or A/B physical 2-regular six-coordinate selected positive GF5 six-ID Q, including the D6 physical 2-regular patterns addressed by the prior source/physical-twofactor protocol. We do **NOT** assert every possible positive GF5 class has this shape without a separate exhaustive classification; the non-lift theorem applies precisely to the actual physical degree-two gateway.

This is the central **formal blocker**: reaching an auxiliary original-coordinate triple count of order s^6 does NOT prove the issue #230 all-seven positive six-motif lower of order s^6. The physical degree obstruction invalidates the naive "choose three more actual flags and count them as accepted" transfer. Any genuine Branch A proof must instead find a different source/physical charging or compensation argument not contradicting this structural impossibility.

## 7. Independent genuine original finite validation and negative controls

- All exact dyadic powers h=1..60: minimal true a, \(\frac{5a²}{12V}\), exact Fraction \(\mu\), third factorial Jensen and nonnegative remainder, original all-same-point/line triple subtraction, all-h \(4Vd³\) and \(4s^6\) inequalities; never construct fake enormous GQ finite sources.
- REAL W(3,2) full original 45 actual flag IDs, five globally complete independently typed K6 schemes (dual-zero, lex, reverse, S68, S72): **three INDEPENDENT** computations of \(\mathcal T_{\ge2,\ge2}\): (1) transport M 3rd factorial minus real-original-source triple repetitions; (2) literal source-flag ID combinations of size3 INSIDE each physically compatible cell without M; (3) source-first exhaustive all \(\binom{45}3=14\,190\) distinct actual original flag triples, directly testing both physical coordinate intersections without M nor any cell grouping. Historical two-flag original transport oracle compared separately.
- TRUE original W(3,4), lex/random physically nononto K14 (V85,K91,m6), two independent factorial/source correction and actual-cell triple enumeration algorithms. TRUE original W(3,8), lex/random physically nononto K35 (V585,K595,m10), bounded independent actual-source-flag triple enumeration from physical cells (NOT \(\binom{5265}{3}\) global brute).
- Real source symplectic automorphism shared by original point+line types and independent typed physical alphabet permutations preserve full third factorial, exact true original same-point/same-line corrections and mixed genuine three-flag counts.
- Negative controls: fake truncated original incidence flag set, repeated/invalid globally injected physical labels and non-dyadic s rejected. Direct degree-two finite K6 two C3, one C6 and repeated-root edge + four-cycle patterns have NO three physical edges sharing one coordinate, confirming the explicitly restricted no-lift scope.
- The finite-only stronger **three different point IDs AND three different line IDs** count is measured and explicitly stored as exploratory evidence; NO universal positive theorem about it follows from the present source degeneracy subtraction.


### Exact TRUE original finite data — pinned reproducible source witnesses

The following **UNORDERED** triple counts are independently counted via **one globally fixed** original source point map f and line map g, re-used for every one of the genuine original incidence flags. The mixed class means at least **TWO different original point IDs AND TWO different original line IDs** within each three-flag subset, with a common physical coordinate on BOTH typed sides. The parenthesized stronger class (all THREE actual source points and all THREE actual source lines pairwise distinct) is **FINITE-ONLY exploratory data, NOT an all-h theorem**.

| Genuine ORIGINAL symplectic GQ | Complete global typed map scheme | Unordered MIXED original triples (new theorem class) | Finite-only THREE-distinct points AND lines | Guaranteed MIXED lower from \(4Vd³/6\) |
|---|---|---:|---:|---:|
| W(3,2) | dual-zero | **466** | 152 | 270 |
| W(3,2) | lex | **605** | 202 | 270 |
| W(3,2) | reverse | **486** | 199 | 270 |
| W(3,2) | S68 | **409** | 118 | 270 |
| W(3,2) | S72 | **439** | 124 | 270 |
| W(3,4) | lex | **23,534** | 14,590 | ≥7,084 |
| W(3,4) | random | **20,048** | 13,219 | ≥7,084 |
| W(3,8) | lex | **1,165,246** | 939,764 | 284,310 |
| W(3,8) | random | **1,006,839** | 858,278 | 284,310 |

At s=4, \(4Vd³/6=42500/6\), so the integer unordered lower is its CEILING 7,084. At s=2 the ordered floor 1,620 is divisible by six, and at s=8 the ordered floor 1,705,860 is divisible by six. Actual numbers above are NOT assertions of the minimum over all f,g at fixed s.

For every W(3,2) row the values were simultaneously checked by:
1. factorial third transport with both actual original source degeneracies explicitly subtracted;
2. independent direct cell-based three-actual-flag-ID combinations, without M or those degeneracy formulas;
3. independent source-FIRST enumeration of all 14,190 unordered triples among the 45 TRUE original incidence flag IDs, testing global point and line physical coordinate intersections directly, without any coordinate-cell data structure.

For W(3,4) and W(3,8) the first two independent methods agree exactly on every row including genuine non-surjective K14 (six pair holes per type) and K35 (ten pair holes per type). The W(3,8) tests enumerate only compatible source-flag triples within physically occupied cells and do NOT attempt \(\binom{5265}{3}\) brute triples. Literal common ORIGINAL symplectic-source automorphism plus separate physical typed coordinate permutations preserves all exact transport and degeneracy counts; malformed globally injected source label maps and fake source incidences are rejected.

The finite stronger three-points/three-lines positivity is encouraging but logically **not established for arbitrary global f,g or every order** by this third-moment proof. Equally importantly, even three all-distinct original factors can still share a physical point-coordinate on all three point labels and a physical line-coordinate on all three line labels, so **the degree-three obstruction to direct physically 2-regular GF5 lifting remains**.

## 8. Decision and next allowed mathematical gate

**PROVED as restricted all-h genuine-original all-global-map statement subject to independent proof review:** new third factorial actual FᵀBG identity, exact globally consistent original-source p/l triple subtraction, \(\mathcal T_{\ge2,\ge2}(f,g)\ge4V(s+1)^3\ge4s^6\), dual-typed physical center uniqueness for mixed triple, and impossibility of direct containment into any 6-original-flag degree-two physical factor class.

**NOT PROVED:** all selected seven GF5 \(S_s(f,g)=\Omega(s^6)\), three pairwise distinct original points/lines among triples for every f/g, infinite globally complete original counterfamily S=o(s^6), full R3/ASET exponent, Branch A/B/C closure. This is an honest restriction showing why a naive global-transport 3rd moment argument cannot be substituted for a Hall-positive source six-Q theorem.

**Genuine next step:** seek a global source **degree-two-compatible** statistic, e.g. balanced six-flag physical pair-spectrum / row-col six-coordinate 2-regular tensor, whose nonzero support is bounded from below for arbitrary globally correlated f/g; compare to other five original GF5 modes incl D6, or provide explicit all-h correlated original pair-label failure. Repeatedly raising powers of globally coincident coordinate moments without the physical 2-regularity gate is insufficient.

**Integration protocol:** four additive versioned code/tests/mathematical Markdown/GitHub-hosted CI research artifacts in strict Draft child of #529. Full exact-final-HEAD dedicated, INDEX, Proof Audit, Full Research success and a separate independent mathematical referee before accepted RCP JSON scientific claim registration, regenerating five derived Markdown registries, or merging. Do not edit generated registry docs by hand. Root issue #230 stays OPEN.
