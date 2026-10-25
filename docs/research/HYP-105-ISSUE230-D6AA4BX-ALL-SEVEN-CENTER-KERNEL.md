# HYP-105 / issue #230 — AA4-BX: all-seven true-original Boolean-kernel center envelope

**Research-only scientific Draft**, strict child of [AA4-BV-C/A PR #595](https://github.com/definitely-stable/Mathlab/pull/595), frozen parent exact head f2375a37398a6c4603eab23a7930867a91858343. Also reviews parallel [AA4-BW #596](https://github.com/definitely-stable/Mathlab/pull/596), which ALREADY proves a source-dependent C/B sixcube degree<=3 uniform-error bound from quartic/quintic GQ source geometry. This new result is a **seven-class ORIGINAL fixed-center weighted risk LOWER CERTIFICATE**, from exact SHARP single-Boolean-indicator high-pass operator norm and one fixed physical POINT f source incidence Q support. It is different from #596's C/B only per-coefficient triangle approach, and explicitly strengthens the generic source-Q high-degree envelope simultaneously for all seven accepted GF5 classes. General Walsh Fourier/Krawtchouk projection kernels are CLASSICAL (Ryan O'Donnell, *Analysis of Boolean Functions*, arXiv:2105.10386). We claim no new general Boolean-cube operator norm theory or GF5-positive proof.

## Root Branch A/B/C, strict quantifiers

For every actual symplectic ORIGINAL W(3,s), s=2^h h>=1, take arbitrary fully CORRELATED globally injected complete typed original physical pair maps f and g from V=(s+1)(s²+1) point factors and V LINE factors into physical pair edges of minimal K_a. Preserve original six DISTINCT incidence flag IDs Q on BOTH physical halves, the SAME global f at all cube vertices, and one whole globally injected g^x at each vertex x of a cube of six DISJOINT whole ORIGINAL LINE-factor source image swaps (fixed occupied right physical pair-edge support E). The root #230 selected GF5 necessary-R3 lower numerator is W(x)=Σ_{c in seven} w_c S_c(f,g^x), with true historical weights (5643,45600,45600,43320,49050,51750,45010). This W≥0 is NOT full R3 equality.

### BX-KERNEL: exact sharp Boolean-indicator high-pass center norms (classical Fourier tools)

Fix a cutoff r=3 and a Boolean acceptance indicator b:{0,1}^k→{0,1}, where 0≤k≤6. On uniform k-bit cube use Walsh characters χ_T(x)=(-1)^{|T∩x|}, coefficients hat b(T)=2^(-k)Σ_x b(x)χ_T(x). Define high-pass remainder R_k b(0)=Σ_|T|≥4 hat b(T). The unnormalized high-pass kernel is

\[
K_k(y)=\sum_{|T|\ge4}\chi_T(y).
\]

Therefore R_k b(0)=2^(-k)Σ_y b(y)K_k(y). For every k≤6, Σ_y K_k(y)=0, so its positive and negative masses are equal. Since b(y) is BOOLEAN 0/1,

\[
\boxed{|R_k b(0)|\le \eta_k:=\frac{1}{2^{k+1}}\sum_y|K_k(y)|.}
\]

Translation invariance proves the same bound at EVERY k-cube vertex. This is the EXACT Boolean-indicator operator norm, not merely a coarse L1 triangle or Cauchy bound. Equality among abstract Boolean indicators is attained by b(y)=1_{K_k(y)>0} (and with opposite sign by indicator K_k<0); it is NOT claimed that these extremizers represent a genuine original W3 GF5 acceptance indicator for any given f,g.

The EXACT constants at cutoff 3 are

| k genuine touched original LINE source-swap packets in one Q | eta_k | old per-coefficient triangle bound |
|---|---|---|
| 0..3 | 0 | 0 |
| 4 | 1/2 | 1/2 |
| 5 | 15/16 | 3 |
| 6 | 51/32 | 11 |

Each constant is verified independently by two explicit enumeration constructions of the Krawtchouk-like high-pass kernel plus its sign-positive extremizer for all k 0..6. Sharpness only in the GENERIC Boolean class is important.

### BX-GEOMETRIC: f-quenched all-SEVEN original source high-pass error (ALL h)

For a chosen family P of six disjoint two-ORIGINAL-LINE-factor swap packets and a given fixed COMPLETE original f, let L_f be the set of true six-DISTINCT-original-incidence-Q whose original POINT projection under f is physically selected six-coordinate 2-regular. This f-only set is defined by the historical original left physical classifier, with true original POINT/LINE incidence IDs kept unchanged; NO g dependence. Each Q has at most ONE possible accepted selected GF5 class c(Q), from its IMMUTABLE original incidence factor multiplicities and B/B original repeated source position overlap (proved in earlier #476 and #589). If no selected source class is eligible for Q, do not charge it.

Let D_Q={i: Q contains at least one TRUE ORIGINAL LINE incidence factor from either original LINE source ID in packet P_i}; k_Q=|D_Q|≤6. For every global right source map g^x, the historical accepted indicator I_Q(g^x)∈{0,1} depends ONLY on coordinates D_Q. Therefore its degree≥4 projection, at EVERY full sixcube vertex x, has absolute value ≤eta_{k_Q}. With POSITIVE historical GF5 selected weights w_c,

\[
\boxed{
\forall x\in\{0,1\}^6:\quad
|W(f,g^x)-P_{\le3}W(f,g^x)|
\le E_f(P):=\sum_{Q\in L_f:c(Q)\in seven} w_{c(Q)}\,\eta_{k_Q}.
}\tag{BX-ALL-SEVEN}
\]

This uses a single full global original f,g^x per vertex, same original Q on both physical sides, and NO independence assumptions on original physical map correlations, source-Q intersections or per-Q right redraw. Critically E_f depends ONLY on original f, true W3 source incidence, the fixed historical seven class weights and chosen original LINE source packet IDs; it is UNIFORM over EVERY possible globally injected complete right map g (including DIFFERENT original occupied physical pair-edge support E). No unconditional bounded E_f/c*s^6 is asserted; the sum can be huge for large h and adversarial original f.

The historical nonnegative necessary-R3 lower numerator at the ACTUAL ORIGINAL UNCHANGED center (f,g), x=0, therefore obeys the **computable conditional original-center lower certificate**

\[
\boxed{
W(f,g)\ge \max\{0,\ P_{\le3}W(0)-E_f(P)\}.
}\tag{BX-CENTER}
\]

This is the novel scoped purpose: transfer the known signed low-three-degree part and a TRUE original GF5 geometric f-quenched error envelope to the unchanged ORIGINAL global map, NOT claim the RHS is universally Ω(s^6). Conditional theorem: to close Branch A using this method, one would STILL have to prove (or otherwise replace) an all-h f,g-uniform positive lower for P≤3W(0)−E_f(P) for at least one choice of six packets (possibly adaptive, but chosen on authentic unchanged map; all certificates hold simultaneously). Mere high-degree bounds or positive cube averages cannot guarantee it.

### BX-IMPROVEMENT: exact strict improvement over individual-coefficient absolute triangle

The prior straightforward g-independent source count would bound |hat I_Q(T)|≤1/2 for each nonempty Fourier subset T⊆D_Q with |T|>=4, then triangle: E_f^triangle=(1/2)Σ_{eligible Q}w_c Σ_{j=4}^{k_Q} C(k_Q,j). Our exact Boolean kernel norm has eta_5=15/16<3 and eta_6=51/32<11, never worse for any Q (eta4=1/2 equality). This is a **simultaneous higher-order cancellation internal to one TRUE ORIGINAL Q**, before cancellations or correlations ACROSS distinct Q. It does not require nonnegative off-diagonal all-seven class covariance (empirically false on real W32 as AA4-BS shows).

### Finite TRUE original falsifiers

Implementation file research/hyp105_issue230_d6aa4bx_all_seven_center_kernel.py, independent tests research/test_hyp105_issue230_d6aa4bx_all_seven_center_kernel.py, hosted three-job scoped workflow. On actual symplectic W32/K6 complete physically injected typed f,g (schemes lex and S72), enumerate ALL historical 62,370 genuine original LEFT six-coordinate candidates once; compute only original source c(Q) and source LINE swap touched packet number k_Q, derive exact f-quenched E_f from 7 GF5 weights and eta_k; reassign entire original global LINE map to an independent arbitrary complete permutation while holding source geometry and f fixed and verify E_f literally unchanged. Independently evaluate historical GF5 all-seven original counts under 64 COMPLETE globally injected original right maps per scheme (6 original LINE source image swaps) via the unmodified full historical seven_census, compute all Walsh coefficients and P<=3 at every x. Check exact centered W decomposition, |R|<=E_f over ALL vertices and original center lower. Separately retag EACH Q on only its own source-relevant ORIGINAL LINE transpositions and independently compute its signed high-degree Fourier sum; must match WHOLE-GLOBAL-history high-degree center correction exactly. An independent naive direct 64×64 signed Fourier matrix validates 8 selected vertices of the fast Walsh projection. Reject invalid original source pair overlap, malformed cube degree or fake finite W34 full-history input. All-h proof is symbolic; **NO** fictitious large-h source geometry is enumerated.

### Independently verified genuine-original W32 numerical margin (the bound is vacuous here)

Two TRUE symplectic W(3,2)/K6 original complete typed physical pair-image schemes, six ACTUAL disjoint ORIGINAL LINE source factor swaps (0,1),(2,3),(4,5),(6,7),(8,9),(10,11), and 64 COMPLETE globally injected original right g^x states each, with the historical full ALL-SEVEN GF5 source-six-ID classifier:

| Original f,g scheme | f-only E_f sharp Boolean kernel | old naive individual-coefficient triangle | original W(0) selected GF5 weighted lower numerator | P≤3 W(0) | signed R>3(0) |
|---|---:|---:|---:|---:|---:|
| lex | 16325377051/32 | 879467921 | 11225795 | 90904087/8 | -1097727/8 |
| S72 | 7806024657/16 | 817837593 | 3283610 | 105103511/32 | -27991/32 |

The accepted source-possible six-Q touch-count vectors (k=0..6) are lex (0,51,3151,19349,25210,7485,351) totaling 55,597 Q and S72 (0,27,2807,20589,26490,7389,301) totaling 57,603 Q; all originate from 62,370 actual historically selected LEFT physical six-Q candidates per fixed f. The f-quenched bound E_f is LITERALLY identical after globally permuting every original complete right g label while f/source Q fixed. Exact f-only weighted E_f is a strict improvement over the old triangle upper, but remains enormously larger than P≤3 W(0); therefore **the certified original-center lower is 0 in BOTH tested schemes**. This is an explicit REAL original W3 numeric warning against mistaking a better Fourier tail bound for a successful universal original-map GF5 obstruction.

The precise signed tail R>3(0) is small relative to this worst-case source-only bound, and its computation matches two INDEPENDENT methods: full historical seven_census over all 64 original global maps and a sum of separately classified ORIGINAL-Q indicators on only their touching source LINE image swaps. Those finite values are pinned as exact Fractions in hosted regression tests, not fitted asymptotic data.

### Historical method gate

This is NOT root #230 universal Branch A S_s(f,g)>=c*s^6 or an ALL original f,g positive center margin, NOT genuine original correlated infinite all-h o(s^6) counterfamily B, NOT accepted exact model-equivalent Branch C reduction (in particular E_f and P<=3 are CONDITIONAL certificate and projection on changed full maps, not a root-strength tensor equivalence), and NOT strict full R3/ASET. Full historical GF5 necessary risk W involves all seven class weights, but no full R3 equality. Automated CI supports numeric checks and code, not independent mathematical refereeing. Stronger class-specific GQ capacity from #591-#596 can reduce E_f for selected classes but has not been asserted as automatic positive center sign. Next root-facing step is to prove a *SIGNED* positivity margin of low-degree original source/quench tensor against the f-dependent sharp E_f, or an authentic original correlated adversarial obstruction.

Prior art: O'Donnell, *Analysis of Boolean Functions*, arXiv:2105.10386; classical finite GQ source line incidence axioms (Encyclopedia of Mathematics, Quadrangle). #596 previously bounded only C/B with per-coefficient triangle; #587/#590 previous degree and covariance identities, all fully credited. Draft only; root issue remains OPEN_WITH_FORMAL_BLOCKER, no main edits or merge before exact-head dedicated/index/Proof Audit/Full Research + independent referee + ancestor acceptance.
