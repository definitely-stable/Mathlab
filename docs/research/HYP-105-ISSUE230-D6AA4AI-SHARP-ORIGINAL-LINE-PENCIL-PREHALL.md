# HYP-105 / issue #230 — AA4-AI: sharp ORIGINAL GQ pencil accounting lowers AG deterministic pre-Hall threshold from 2¹⁹ to 16

**Research-only, strict all-h deterministic physical PRE-HALL theorem.** Stack on [AA4-AH PR #517](https://github.com/definitely-stable/Mathlab/pull/517), parent exact pinned SHA \`09114a7be997207537c5bf75d318dc4fe61e362d\`. No issue #230 Branch A/B/C closure, no accepted genuine GF(5) positive lower, no main edits. The scope is exactly the **original source-root-indexed physically occupied point-B C4 × opposite disjoint physical two-triangle A completion** of the existing [AA4-AG #516](https://github.com/definitely-stable/Mathlab/pull/516), **before** the true ORIGINAL 4×4 source-incidence Hall gate and AA4-AH six-channel transfer. This slice is a genuine improvement of the earlier bound's range, not a new assertion that global original-point and line labels are independently reselected per Q.

## 1. WHY AG's 2^19 threshold was avoidable: one true-original line intersects only d(d−1) others

For genuine original W(3,s), s=2^h>=2, let

\[
V=(s+1)(s^2+1),\quad d=s+1,\quad
a=\min\{t:\binom t2\ge V\},\quad K=\binom a2,\quad
m=K-V\le a-2.
\]

Fix **any TWO complete globally injected** physically unordered-edge typed maps \(f:P\hookrightarrow E(K_a)\) and \(g:L\hookrightarrow E(K_a)\), reused on the SAME every true original incidence-Q. There are **exactly**

\[
N=V\binom d2
\]

distinct indexed triples \((p,\{\ell_0,\ell_1\})\) with a true ORIGINAL point p and TWO distinct ACTUAL ORIGINAL lines \(\ell_0,\ell_1\) through p. Different source lines intersect in **AT MOST ONE** original point because W(3,s) incidence girth is eight; thus each original rootpair is uniquely indexed by its two actual original line factors.

The physical complement of e=f(p) supports at least, by AA4-AF,

\[
C_{4,\min}
=\max\left(0,3\binom{a-2}{4}-m(a-4)(a-5)\right)
\]

occupied first-side B 4-cycles (four distinct globally f-inverse-mapped actual original point factors) for **every p and f**. The second side g may leave exactly m physical K_a pairs unoccupied.

For each physical coordinate x, define \(D(x)\) = number of missing physical edges incident with x (relative to the SINGLE global im(g)). Define its **hot** status \(16D(x)\ge a\). Because \(\sum_x D(x)=2m\), the number H of hot physical coordinate vertices satisfies

\[
H\le \left\lfloor\frac{32m}{a}\right\rfloor\le32.
\]

The older AG formula bounded pairs of original lines whose physical images touch these hot coordinates by \(H(a-1)(V-1)\). Although valid as a coarse count, this ignores the actual ORIGINAL GQ fact:

> **ORIGINAL point-line pencil lemma.** One actual original source line ℓ contains precisely d original points. At each of these points it meets exactly d−1 different other original lines. These sets of other lines are disjoint by source girth eight (no two real original lines meet twice). Therefore each original line meets EXACTLY d(d−1) other original lines — **not V−1**.

A chosen physical coordinate x belongs to at most a−1 physical edges of the COMPLETE K_a. Because g is globally injected, x can appear in physical pair images of at most a−1 distinct actual original source lines. Therefore the number of TRUE ORIGINAL rooted intersecting source line pairs whose **either** globally assigned physical pair contains x is at most

\[
(a-1)\,d(d-1).
\]

The key **NEW** bad-rootpair counting bound, simultaneously for every full global g, is thus

\[
\boxed{
B_{\rm hot}(g)\le
\left\lfloor\frac{32m}{a}\right\rfloor
(a-1)d(d-1).
}
\]

This is much smaller than \(H(a-1)(V-1)\) at large s: the true GQ line-neighborhood degree is \(d(d-1)\sim s^2\), whereas V−1~s³. It does not assume independence of different original rootpairs; it uses a direct double count on ONE common complete opposite typed g.

## 2. NEW AI-1 — improved deterministic safe true original rooted pair count

Two distinct globally injected physical source LINE edges e₀=g(ℓ₀),e₁=g(ℓ₁) are physically adjacent if they share one physical coordinate, or physically disjoint otherwise. There are exactly \(a\binom{a-1}2\) unordered physically adjacent edge pairs in full K_a. Because any TWO different original lines meet at at most one original point, the number of actual original rootpairs whose opposite physical edges are adjacent is at most that absolute number.

Define an original rootpair \((p,\{\ell_0,\ell_1\})\) **SAFE** when e₀,e₁ have **four distinct physical coordinates** and NONE of those four coordinates is hot. Union bounding only *actual original rootpairs* gives for any physical full f,g, with no probability:

\[
\boxed{
N_{\rm safe}(g)\ge
N-a\binom{a-1}2
-\left\lfloor\frac{32m}{a}\right\rfloor
(a-1)d(d-1).
}
\]

If the right side is negative, use zero. The source-point injection f does NOT appear in this safe-count expression, and its physical complement-C4 bound is valid for all f. Unlike counting generic pairs of original line labels, the reduced hot term is rigorously valid because the source line-intersection graph of W(3,s) has valency d(d−1).

## 3. NEW AI-2 — retained exact pre-Hall lower with explicit s≥16 threshold

For a SAFE opposite physical edge pair e₀={u,v},e₁={w,x}, all four endpoint coordinates have missing-edge degree \(<a/16\). Exclude all four pinned physical coordinates from the eligible additional physical vertices. The common physical-neighbor sets

\[
Y=\{y\notin\{u,v,w,x\}:\{u,y\},\{v,y\}\in \operatorname{im}(g)\},\\
Z=\{z\notin\{u,v,w,x\}:\{w,z\},\{x,z\}\in \operatorname{im}(g)\}
\]

satisfy

\[
|Y|,|Z|\ge(a-4)-2a/16=7a/8-4.
\]

For a≥32, this is at least 3a/4. Because y=z would collapse six distinct physical vertices into five, the number of *occupied, disjoint physical TWO-TRIANGLE A patterns* containing both pinned opposite edges is EXACTLY \(|Y||Z|-|Y\cap Z|\), and hence at least

\[
|Y||Z|-|Y\cap Z|
\ge\frac{9a^2}{16}-a\ge\frac{a^2}{4}.
\]

Since it is integer, it is ≥\(\lceil a^2/4\rceil\). Every SAFE true original rootpair and every occupied original point physical complementary C4 yield this many complete opposite physical two-triangle patterns, counted as INDEXED candidates. **NO source Hall positive condition is imposed**: many or all 4×4 actual GQ incidence matrices can still have permanent 0.

Hence the deterministic full global two-map bound, for a≥32:

\[
\boxed{
P_\triangle(f,g)\ge
\left[N-a\binom{a-1}{2}
-\left\lfloor\frac{32m}{a}\right\rfloor(a-1)d(d-1)\right]_+
C_{4,\min}\left\lceil\frac{a^2}{4}\right\rceil.
}
\]

All original roots, pinned flag pairs, opposite global pairs, occupied first physical C4 and occupied opposite two-triangle patterns are counted with their correct **INDEXED multiplicity**, not source automorphism quotient or physical orbit count. This is the EXACT SAME pre-Hall indexed quantity P_triangle as AG; thus it directly strengthens AG rather than inventing a different physical model.

### Explicit \(s^{14}/256\) for every s=2^h≥16

1. From a's minimality, \(m\le a-2\). For a≥22, the occupied physical C4 complement bound satisfies
\[
C_{4,\min}\ge\frac{(a-2)(a-4)(a-5)(a-11)}8\ge\frac{a^4}{128}
\]
(the last inequality uses each factor ≥a/2).

2. For s≥16, \(a\le(3/2)s^{3/2}\). Elementary integer-free construction: minimality gives \(a\le\sqrt{2V}+2\); for all s≥16, \(2V\le(3s^{3/2}/2-2)^2\). Indeed the difference is \(\frac14s^3-2s^2-2s-6s^{3/2}+2\ge0\): since s≥16, \(\frac14s^3-2s^2\ge2s^2\), while \(2s+6s^{3/2}\le(s^2/8)+(3s^2/2)<2s^2\).

3. For s≥128, the true GQ pencil-aware bad-pair bound relative to \(N=Vds/2\ge s^5/2\) is
\[
\frac{B_{\rm total}}N
\le \frac{27}{8\sqrt s}+\frac{96}{s^{3/2}}
< \frac12.
\]
The last inequality follows immediately from \(\sqrt s>11\) and \(s^{3/2}>1408\) at s≥128. Therefore \(N_{\rm safe}\ge N/2\) at all powers h≥7.

4. For the ONLY smaller powers in the claimed range, **s=16,32,64**, the formulas above are exact bounded-size integer certificates, not a trend extrapolation:

| Genuine original s | Minimal a | Missing m | Hot upper H | True rooted N | Adjacent upper | NEW hot-touch upper | SAFE rootpair lower |
|---|---:|---:|---:|---:|---:|---:|---:|
| 16 | 94 | 2 | 0 | 594,184 | 402,132 | 0 | **192,052** |
| 32 | 261 | 105 | 12 | 17,859,600 | 8,787,870 | 3,294,720 | **5,777,010** |
| 64 | 731 | 510 | 22 | 553,914,400 | 194,508,135 | 66,809,600 | **292,596,665** |

Direct exact integer multiplication verifies \(256\,N_\mathrm{safe} C_{4,\min}\lceil a^2/4\rceil\ge s^{14}\) separately for all three rows; the source of each number is an explicit closed formula, not a stochastic estimate. For s≥128 the analytic bound \(N_\mathrm{safe}\ge N/2\), \(N\ge s^5/2\), \(a^2\ge2V\ge2s^3\), \(C_{4,\min}\ge a^4/128\) gives

\[
P_\triangle(f,g)\ge\frac N2\frac{a^4}{128}\frac{a^2}{4}
\ge \frac{s^5}{4}\frac{8s^9}{512}
=\boxed{\frac{s^{14}}{256}}.
\]

**NEW ALL-h universal theorem:** for every genuine W(3,s), s=2^h≥16, EVERY complete global point f and EVERY complete global line g,

\[
\boxed{P_\triangle(f,g)\ge s^{14}/256.}
\]

This strengthens the range of the preexisting AG-1 theorem from \(s\ge2^{19}\) to \(s\ge16\), while maintaining the **same constant and identical physically indexed pre-Hall quantity**. For s=2,4,8 the new coarse SAFE lower may be 0, and this theorem intentionally makes NO universal s14/256 claim there.

## 4. Exact independent finite TRUE source falsifiers

The analytic all-h proof does **not** depend on brute finite W3s runs. To guard the model and improve auditability, the code also literally scans **real original root+two-flag IDs** on original W(3,2), W(3,4), W(3,8), using the same fully global physical images f,g on every source Q. For each typed orientation point-B/line-A and line-B/point-A, it independently computes:
- all actual true ORIGINAL rootpair indices, actual pinned globally injected physical-edge overlap, physical endpoint missing-edge degrees, actual hot vertex set, and actual SAFE original rootpair count;
- independently checks actual physically adjacent-pair count ≤ full K_a adjacency capacity, actual HOT-touch count ≤ NEW true original-line-pencil cap, actual #hot coordinates ≤ floor(32m/a), and actual SAFE count ≥ analytic floor;
- for bounded sampled SAFE rootpairs, independently enumerates literal occupied disjoint physical two-triangle completions using all y≠z vs the **separate** \(|Y||Z|-|Y\cap Z|\) count; for a≥32, each actual SAFE pair must support ≥ceil(a²/4) physical two-triangle completions;
- independently checks one ORIGINAL B-side physical complement-C4 count using the prior genuine source-factor inverse-physical image oracle, including W34/W38 physical unused-pair holes.

The TRUE ORIGINAL W(3,4) (a=14,K=91,V=85) finite fixtures lex and random each have 850 actual source root flag pairs per typed orientation; W(3,8) (a=35,K=595,V=585) each have exactly 21,060. **Neither s=4 nor s=8 falls in the NEW 16+ theorem's scope**, so we never require a positive universal pre-Hall s14/256 in these finite source fixtures. They are model falsifiers only. Original symplectic automorphisms (one common ORIGINAL point/line transport) and independent physical point/line coordinate permutations preserve full global indexed class totals, HOT counts, SAFE source rooted counts and physical occupancy counts up to relabeling. Negative controls reject noninjective physical source maps, incorrect actual original incidence graph and invalid input s.


### Exact independent hosted authentic GQ finite safety ledger

Actual true-original symplectic incidence flags, rootpair IDs, globally fixed f/g physical edge labels and missing physical edges were independently enumerated for the following fixed complete global schemes. On each source typed side all real source root+pinned two-flag pairs were counted **once**, then disjoint non-HOT physical images tested. Counts are neither abstract complete K_a pair counts nor all-h estimates.

| Genuine source order | Full source labels | Repeated original B-root type | ALL indexed true source rootpairs | Physically adjacent opposite pinned pairs | Touching hot physical coordinates | Exact SAFE rootpairs |
|---|---|---|---:|---:|---:|---:|
| W(3,4) | lex | point | 850 | 305 | 599 | **140** |
| W(3,4) | lex | line | 850 | 235 | 605 | **148** |
| W(3,4) | random | point | 850 | 237 | 822 | **11** |
| W(3,4) | random | line | 850 | 226 | 838 | **6** |
| W(3,8) | lex | point | 21,060 | 3,682 | 9,324 | **9,302** |
| W(3,8) | lex | line | 21,060 | 2,360 | 9,422 | **10,104** |
| W(3,8) | random | point | 21,060 | 2,341 | 0 | **18,719** |
| W(3,8) | random | line | 21,060 | 2,298 | 0 | **18,762** |

Physical adjacency and touching-HOT sets OVERLAP, so their sizes must NOT simply be added to obtain the number of bad rootpairs. The exact verified identity is SAFE = TOTAL − |adjacent union HOT|. The random global map has no high-hole-degree physical vertices in W(3,8), hence its hot-touch count vanishes. W(3,4) physical a=14 is below the a≥32 uniform two-triangle capacity proof; W(3,8) also lies below the all-s≥16 mass theorem, so their many actual SAFE rootpairs are finite validation rather than the universal proof.

On W(3,4), the independently measured occupied physical B-complement C4 populations at the selected first SAFE original source root were:
- lex point root 6: 1,050 C4;
- lex line root 2: 1,050 C4;
- random point root 1: 1,144 C4;
- random line root 18: 1,151 C4.

These source-root-specific counts are all ≥the all-h W34 C4 floor 945. **They are deliberately not identified with the AA4-AF root-0 values** (which have a different source root and may therefore differ). The code now returns the selected actual original root ID and independently verifies its C4 using a separate oriented adjacency-walk/8 oracle.

The final theorem does NOT need any of these finite measurements. It follows algebraically from the original line-pencil incidence bound plus exact exceptional orders 16,32,64 and the uniform analytic inequality at all s≥128.

## 5. Relation to genuine original Hall / six-channel acceptance

The parallel and stacked AA4-AH theorem exactly computes the ACCEPTED two-triangle source GF5 subset as six nonnegative 2-by-2 original rook channels, whereas AG/AI physical mass P_triangle counts candidate physical e/f/g patterns **before** checking any actual source-neighborhood Hall constraints. If every accepted original six-incidence-Q is counted once, its true source four-rook permanent lies in {0,1,2} by AA4-AE, but an indexed physical pattern may have permanent ZERO.

The deterministic all-map theorem therefore gives only a **necessary obstruction density**: if a sequence of real full globally injected pairs had \(S_s(f_s,g_s)=o(s^6)\), then its Hall-positive physical two-triangle density among the AI indexed P_triangle candidates would necessarily be \(o(s^{-8})\). Conversely a uniform lower density c/s^8 of genuinely Hall-positive original two-triangle patterns in all global maps would suffice for a real original selected positive \(S_s=\Omega(s^6)\) bound. Neither such density lower nor an infinite real counterfamily is proved.

The essential next genuinely mathematical gate is to use a common opposite globally injected g, true GQ JPKC/EICE structural correlation, and all six source Hall channel tensors to exclude global near-perfect anti-alignment of the occupied physical two-triangle candidates. The original source 8-cycle positive excess from AA4-AE remains trackable but cannot substitute for a Hall density lower. Root Branch A/B/C, full R3, and ASET remain OPEN.

**Integration protocol:** strict research-only Draft child of [AH #517](https://github.com/definitely-stable/Mathlab/pull/517), separate four additive source/test/math MD/hosted CI artifacts, exact pinned parent SHA. Require dedicated, INDEX, Proof Audit, Full Research all SUCCESS on exact final head and an independent mathematical referee before any RCP canonical JSON scientific claim registration. Register accepted proof plus symbols/quantifiers/uncertainties/source SHA and regenerate five derived research Markdown registries **from JSON only**; do not hand edit generated register documents, do not merge research chain to main or close issue #230 in this slice.
