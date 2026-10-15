# HYP-105 / issue #230 — D6-AA4-O: exact quintic ORIGINAL source-point adversarial energy and full-map swap frontier

**Scope:** NEW all-h exact nonnegative degree-five source factor polynomial for the real B-left/A-right internal original-line GF(5) charge, and an EXACT transposition-local gradient. Genuine global W32 complete typed-injection adversarial searches with independent full 62,370-candidate ORIGINAL sixset classifiers. This is NOT a proof of the all-h adversarial minimum or Branch A/B. Rigorous global all-map positive lower is OPEN.

Stack strictly on [D6-AA4-N / Draft PR #470](https://github.com/definitely-stable/Mathlab/pull/470) at pinned fully 4/4 CI-green HEAD \`2af74df348a9c0921497757356199a609252f2c2\`. No merges or edits of main, root issue #230 remains OPEN.

## 1. Why the preceding all-h fixed-g theorem is not enough

AA4-N established that for EVERY complete globally injected original source-line map g on REAL W(3,s), s=2^h>=8, a SINGLE uniformly chosen complete source-point map f satisfies \`E_f I_L^{BA,internal}(f,g)>=3s⁶/65536\`. This is an actual all-h quantifier advance: even after arbitrary g, SOME globally admissible f has high true original B/A seven-GF5 source-line charge. It does not imply that ALL globally admissible f have high charge. Our next mathematically meaningful step is to expose the *exact deterministic polynomial* minimized over f and test global injection–preserving adversarial moves, with the original source geometry preserved.

Parallel EICE-003-I / PR #465 and local-transfer PR #466 cannot be substituted as all-h GF5 positivity witnesses. JPKC-011 showed many actual accepted Q lack proper physical P3. This stage counts accepted B/A using genuine positional factor multiplicities and full physical C4/A projection; it never filters physical paths.

## 2. ALL-h exact true-original five-factor polynomial: no independence or surrogate original Q

Fix any true ORIGINAL W(3,s), s=2^h>=2, and any full typed-injective fixed source LINE physical map g. Write \`F_g\` for all true ORIGINAL SIX-distinct-incidence sets Q with (a) one ORIGINAL point p appears exactly twice, in two distinct source-original lines l0,l1 sharing p; (b) the other four original incidences each have a fresh distinct source point qi !=p and all six source lines are distinct; (c) the SIX g-assigned line physical edges form an actual six-coordinate degree-two **A projection**, i.e. a physical six-cycle or two disjoint triangles; (d) the two root source lines l0,l1 have physically DISJOINT g images.

All original line images used in such Q come from ONE globally coherent fixed g. For any such Q, its left physical B projection is accepted by the historical full seven-GF5 positional classifier precisely when its repeated source point p has an edge f(p) physically disjoint from the four physical coordinate symbols of the four other source points, while f(q1),...,f(q4) are four DISTINCT edges making a physical C4. (Global f-injectivity forces the four edges distinct.) This is an *exact if and only if* condition for left B projected onto SIX physical coordinates with every coordinate degree two. No extra same-Q independent right choices, and no physically proper-P3 acceptance gate.

Define the nonnegative integer genuine-original source coefficient
\[
w_g(p,\{q_1,q_2,q_3,q_4\})=
\#\{Q\in F_g:\hbox{repeated ORIGINAL point}=p,\ 
\hbox{other original points}=\{q_1,q_2,q_3,q_4\}\}.
\]
The root point is unique, its two original root lines are unique within Q, so **each actual original six-incidence Q contributes once** to exactly one coefficient. Let \(\chi_B(e_0;e_1,e_2,e_3,e_4)\) be 1 iff e1,...,e4 form a simple C4 over four physical coordinates and e0 is a disjoint physical edge; otherwise 0.

Then the complete globally consistent original seven-GF5 internal B/A charge has the exact ALL-h deterministic identity
\[
\boxed{I_L^{BA,\mathrm{int}}(f,g)
=\sum_{p,A,\ |A|=4}w_g(p,A)\,
\chi_B(f(p);(f(q))_{q\in A}).}
\]
This is a nonnegative FIVE-original-factor polynomial in the one-hot original-point-to-physical-edge assignment variables \(x_{p,e}\), subject to the global typed assignment equations \(\sum_e x_{p,e}=1\), \(\sum_p x_{p,e}\le1\). It is **not** a degree-two source-pair energy, and its quintic dependence explains why the previous first/second Gram identities or pair-spectral constraints do not immediately force a deterministic positive minimum.

The predecessor N's conditional expectation is recovered immediately by averaging this *same* single global map f over all injections:
\[
\mathbb E_f I_L^{BA,\mathrm{int}}(f,g)=p_B\sum_{p,A}w_g(p,A)=p_B T_g.
\]
The exact constant \(p_B=K\binom{a-2}{4}3\cdot4!/(K)_5\) is valid because each term involves five different actual source point factors and a uniform complete injection induces a uniform ordered injective five-edge marginal. This **exact** averaged identity says nothing about whether the assignment-constrained quintic polynomial has an exceptional low-energy point.

## 3. ALL-h exact 2-swap locality / conditional descent identity

For any two different original point factors u and v, let \(f^{u\leftrightarrow v}\) exchange ONLY their two assigned physical pair labels. This preserves the complete typed injection and the globally shared map (all other source point labels and ALL original line labels remain unchanged). The exact total B/A change is

\[
\boxed{
\Delta_{u,v}I=\!
\sum_{(p,A):\{u,v\}\cap(\{p\}\cup A)\ne\varnothing}
w_g(p,A)\bigl[\chi_B(f^{u\leftrightarrow v}|_{\{p\}\cup A})
-\chi_B(f|_{\{p\}\cup A})\bigr].}
\]

All coefficients with no source-point support on u or v cancel exactly. This is an all-h exact locality theorem for the **full globally coherent original B/A quintic polynomial**, not an assumption of independent local terms, and is suitable for finite exact exhaustive swap checks.

A complete assignment that has \(\Delta_{u,v}I\ge0\) for every pair u,v is only a **one-transposition local optimum**. It is NOT a globally minimum-energy assignment (nor a certificate of any all-h lower bound). The optimization routine explicitly reports this scope and only accepts strictly reducing moves; no stochastic simulated annealing is promoted to a proof.

## 4. Genuine W32 frozen-g exact weighted tensor and adversarial search

For each pinned TRUE W(3,2) source scheme lex/reverse/S68/S72, reconstruct all 45 source point-line incidence IDs and the full 15-edge K6 globally injected original line mapping g. Enumerate ALL 70 actual right A physical two-factors (simple six-edge degree-two K6 edge sets). For every true original point pencil p and its two distinct actual original incident source lines l0,l1 with DISJOINT g-physical labels, enumerate every A physical six-edge line factor set containing both, and every valid assignment of the four other original line factors to four NEW DISTINCT actual ORIGINAL source point-line incidences q_i !=p. Group each true six-incidence candidate Q into exactly one quintic support key (p,sorted(q1,q2,q3,q4)) and count its nonnegative integer weight \(w_g\).

Independently verify that \(\sum_{p,A}w_g(p,A)=T_g\) exactly equals AA4-N's separately implemented same-g true source pencil oracle for each scheme. For any TRUE full globally injected source-point map f (K6 point labels are a permutation of all 15 physical edges), evaluate each support's left-B physical condition by independently checking the four edge-label endpoints form C4 with four physical coordinates and f(p) is disjoint.

**Critical independent GF5 check:** on the baseline and every optimized COMPLETE f, re-enumerate all historical 62,370 true original six-incidence candidates with the existing \`seven_census\`, count ALL real accepted seven-GF5 B-left/A-right Q whose two ORIGINAL source lines through the repeated actual source point have physically disjoint right labels, and require EXACT equality with the new quintic polynomial. This is not testing only the new implementation against itself.

**Exact swap gradients:** enumerate ALL C(15,2)=105 admissible whole-label point transpositions; for each verify the delta computed using only source support keys touching the swapped points equals a *separately recomputed full quintic energy difference*, including multiple independently randomly permuted full source maps. Perform steepest valid swap descent from the pinned true S68/S72 baseline and additional deterministic pseudorandom full globally injected starting maps. Require all 105 final gradients nonnegative, strictly decreasing energy sequence, true global injection of final f, and independent full historical original GF5 classifier after each run.

The scan is finite original W32, not exhaustive over the 15! point label bijections, and an observed one-swap minimum is not a global minimum. A zero-charge example, if found, is a rigorous all-seven-GF5 internal B/A zero-charge W32 **single-real-map** witness after full independent census, but does not refute all-h root seven-family S_s nor a uniform asymptotic s>=4 bound.

## 5. What the exact quintic energy suggests for the next proof

The g-dependent tensor \(w_g\) retains ACTUAL original six-incidence positional coupling and all physical A-2factors, so it is a better gateway than a separate pair-degree/moment-only model. The remaining universal theorem would require something like an all-h positive lower bound for the nonnegative weighted quintic C4/disjoint-edge polynomial over **every** assignment-injective physical map f, uniformly in the coefficients realizable by ANY actual original GQ line map g.

The new tensor exposes exactly where counterexamples to **over-relaxed** local source/pair constraints may arise: arbitrary formal nonnegative \(w_g\) tensors admit zero-energy assignments despite positive mean, so the true ORIGINAL GQ/right-physical-image realizability constraints on \(w_g\) are essential. An LP/SA relaxation of the source tensors alone without globally common f/g physical images cannot certify the original GF5 root.

Acceptance: exact hosted final-HEAD dedicated independent tensor/test job, two genuine W32 S68/S72 search jobs, INDEX, Proof Audit, full Research CI and independent mathematical peer review. Four new files in stacked research Draft, main unchanged, root Branch A/B, full R3/ASET power OPEN. The next D6-AA4-P step should seek a source-physical *cycle expansion lower for every complete f* or construct a real adversarial globally injected all-h low-charge family, using this exact tensor and JPKC-012/014 plus EICE-003 local barriers, not another ungrounded finite radius.
