# HYP-105 / #230 — AA4-CL: exact cross-fiber dual-aware GF5 covariance on ONE 96-map genuine-original orbit

**Scientific Draft.** Strict child of [AA4-CK #611](https://github.com/definitely-stable/Mathlab/pull/611) pinned parent `c8f77a93d07b4f52869fabab552413ff8f2ac95a`. Four additive proof/module/oracle/workflow files only. No main, accepted source GF5 class taxonomy, positive 51-column weights, or root #230 verdict changes.

## 1. Why this is the missing overlap test, and prior work

Root #230 Branch A needs a POSITIVE universal fixed-map `S_s(f,g)>=c*s^6` for ANY completely globally injected arbitrary correlated original typed f,g on TRUE symplectic `W(3,2^h)`, h>=1, with all seven historical accepted GF5 classes, or B an original infinite genuine correlated o(s6) family or C a root-equivalent reduction. Previous work #589 gave generic classwise birth/death, #609 exact 720-permutation SINGLE original POINT source-A fiber dual histograms, #610 full-seven original source-factor signed POINT transposition sectors, and #611 exact 60-cycle spectral source-FIBER squared-GF5 swap energy. None can simply add independent 720-fiber orbit estimates: distinct original six-POINT source sets often share original POINT IDs and their complete f images MUST agree.

A stronger obstacle was established by #606: two distinct physical six-edge 2factors sharing FIVE edge images cannot both be physical-eligible at one complete original f. #607 fully classified FOUR common physical edges into an alternating C4 two-edge switch or replacement of one physical cherry-center vertex. Thus the FIRST nonvacuous simultaneous six-POINT source-A-fiber test with distinct factor sets uses EIGHT distinct actual original POINT sources `p0,..,p7`, families A=(p0,p1,p2,p3,p4,p5) and B=(p0,p1,p2,p3,p6,p7), both six-edge physical C6 on the SAME complete physical original f.

Group-theoretic S4 transposition graphs, exact finite covariance under product groups, Cauchy–Schwarz and spectral Poincare are classical; do NOT claim a new general covariance or Schreier theorem. The scientific issue-specific contribution is a true-original HYP-105 same-six-distinct-incidence GF5 double-fiber quantitative covariance bound and its original full-map covariance proof, with independent symplectic W32/W34/W38 falsifiers and a careful nonclaim on universal full S.

## 2. ALL-h original W3 exact two-fiber 96-map same-f action

Fix ANY h>=1, s=2^h, authentic original W(3,s), ANY complete globally injected correlated typed f,g, and EIGHT actual different original POINT IDs `p0,...,p7` whose physical f images satisfy:

- The six actual occupied edges f(p0..p5) form one CONNECTED physical six-coordinate 2factor (C6) for A.
- The six actual occupied edges f(p0..p3,p6,p7) independently form a CONNECTED physical C6 for B.
- The two families share the SAME four complete physical edge labels assigned to actual common original POINT factor IDs p0..p3, NOT copies; all eight original images are distinct by global injection. By #607 their physical completion is either alternating C4 or fifth-vertex cherry replacement, never the #606 forbidden five-edge configuration.

For each fiber F_A and F_B, enumerate the ENTIRE genuine original `(s+1)^6` six-DISTINCT-incidence-ID Q choosing exactly one TRUE incidence on each of its six original POINT source factors. These are two disjoint collections of SIX-source-point-factor sets (a Q cannot belong to both, since each uses exactly six source POINT IDs but A != B). Both use ONE unchanged complete original LINE map g and the SAME true original Q IDs on both sides, not synthetic physical Q.

Let shared `sigma in S4`, exclusive swaps `alpha,beta in S2`. Apply ONE complete original POINT map f^{sigma,alpha,beta}: permute the four WHOLE real original POINT images f(p0..p3) consistently by sigma, independently swap the TWO WHOLE actual original POINT physical image pairs in A-only (p4,p5) iff alpha=1 and in B-only (p6,p7) iff beta=1, never modify any other source image. These 24*2*2=96 full original f maps are distinct and preserve BOTH families' physical C6 occupied six-edge multisets for ALL 96 states. All eight original factor images remain globally injective and occupied pair support identical, original g unchanged and no per-Q redraw.

For family A the score depends on sigma,alpha but **not beta**; for B on sigma,beta but **not alpha**. Their exact positive HISTORICAL all-seven GF5 weighted original source-POINT-A sixflag numerators are (#609)

```text
FA(sigma,alpha)=BA + 5643 HA(CA(sigma,alpha)),
FB(sigma,beta) =BB + 5643 HB(CB(sigma,beta)),

BA =45600 N_B,A +43320 N_C,A;
BB =45600 N_B,B +43320 N_C,B.
```

Each actual hist H is computed from genuine original LINE source multiplicities and true right original physical C6 duals on six ORIGINAL incidence-column positions under the single complete fixed original g, not physical right-only 2factor envelopes. The other four historical positive classes require non-A original source POINT multiplicity and cannot enter either fiber's full historical accepted sevenclass score.

**Exact real-original covariance identity with all quantifiers**. Uniform averaging below is over a FINITE explicitly constructed set of 96 jointly legal complete original maps, not a hypothesized probabilistic independence of real original source-Q geometry:

```text
u(sigma)=(FA(sigma,0)+FA(sigma,1))/2;
v(sigma)=(FB(sigma,0)+FB(sigma,1))/2;

Cov_(sigma,alpha,beta) [FA,FB]
      = Cov_(sigma in S4)[u(sigma),v(sigma)].
```

The identity follows by Fubini expansion of the literal FINITE Cartesian 24*2*2 product. Original incidence structures and complete original f,g remain correlated and fixed, and the two families share four source POINT factors; no false independence of their source-Q events is asserted.

For one of the SIX transpositions tau of the FOUR shared original POINT factors, define real paired historical signed original source-fiber changes `dFA=FA(tau sigma,alpha)-FA(sigma,alpha)`, similarly B. Then

```text
E_(sigma,alpha,beta,tau shared) [dFA*dFB]
    = E_(sigma,tau shared)[du(sigma,tau)*dv(sigma,tau)].
```

Exclusive-only swaps affect one family's score and leave the other IDENTICAL; therefore their mixed original score gradient is ZERO. A uniform eight-generator f walk with six shared and two exclusive swaps has mixed gradient exactly 6/8 of the shared-only expression above, NOT an arbitrary sum of two independent 720-state gradient ensembles.

## 3. NEW exact 24-state shared S4 spectral covariance inequality

Let `A_4` be the 24x24 INTEGER adjacency on ALL permutations sigma of the four original COMMON POINT image positions, where `A_4(sigma,sigma')` counts one of the six legal shared whole-source-factor image transpositions. It is simple symmetric, 6regular and zero diagonal. An independent fully exact INTEGER polynomial certificate verifies

```text
(A4-6I)(A4-2I)A4(A4+2I)(A4+6I) = 0.
tr(A4^0..A4^4) = (24,0,144,0,2880).
spectrum(A4) = { 6^1, 2^9, 0^4, (-2)^9, (-6)^1 }.
spectrum(L4=6I-A4)={ 0^1,4^9,6^4,8^9,12^1 }.
```

All traces, the polynomial ZERO on EVERY entry, and the five rational Vandermonde multiplicity equations are verified with arbitrary-size integers and Fraction, not floating point. The zero of L4 has multiplicity1: graph connected.

Define `D4(u)=(1/(24*6))*sum_sigma,sum_tau (u(tau sigma)-u(sigma))²`, similarly v. Exact Laplacian gap4 proves `D4(u)>=4/3 Var_S4(u)`. Combining TWO separate Poincare inequalities with Cauchy–Schwarz gives the genuinely quantitative **same-global-map two-fiber historical GF5 cross-covariance**:

```text
|Cov_G(FA,FB)|²
   <= Var_S4(u)*Var_S4(v)
   <= (3/4 D4(u))*(3/4 D4(v))
   = 9/16 * D4(u)*D4(v).
```

The coefficient 9/16 is SHARP for ARBITRARY REAL S4 functions u,v (choose matching eigenvectors at eigenvalue2 of A4/L4=4) but need NOT be reachable by nonnegative true-original W3 right-GF5 histograms. The theorem gives an upper bound on magnitude, **NO FIXED SIGN** and NO unconditional lower bound on the sum FA+FB, still less the full global all-seven original S.

**Crucial contrast to #611:** The 24-state S4 transposition graph is BIPARTITE: permutation parity is eigenvector of A4 with eigenvalue −6. Hence ONE random nonlazy transposition P=A4/6 has centered L2 norm EXACTLY 1; any claim of a one-step 3/5-type strict contraction like #611 is FALSE. Its lazy version (I+P)/2 has centered norm 2/3 by spectrum. The actual project test independently constructs the true 24-element sign character to falsify false nonlazy mixing, and an integer eigenvector at A4=2 to prove abstract sharpness of the 9/16 covariance coefficient. Neither eigenfunction is asserted to be a realizable original W3 right GF5 histogram.

The exact block covariance is not necessarily nonnegative merely because each separate 60-cycle physical Gram is nonnegative; ordinary entrywise nonnegative scores can have either sign after centering. Do not substitute physical eligibility for historical GF5.

## 4. True original finite countercontrol geometry and falsifier plan

**Finite genuine original W32/K6**, s=2, V=15 true original POINT and LINE factors and 45 actual incidence IDs, choose 8 DISTINCT original POINT source IDs and map their physical f pair images onto the eight different K6 edges in the **four-cycle two-edge-switch** case:
```text
shared f(p0..p3)=01,12,34,45;
A exclusive p4,p5=05,23;
B exclusive p6,p7=03,25.
```
Both actual left source six-POINT factors are genuine physical connected C6. Use a deterministic actual original LINE source-star Hall/augmenting matching to select eight DIFFERENT ORIGINAL LINE factors, one incident to each p0..p7; globally assign their g physical images to the same eight physical edges, fill every other physical g image injectively in actual K6. Thus ONE complete globally injected original correlated f,g has REAL original Q_A/Q_B with SIX DISTINCT source incidence IDs sharing four actual original IDs and both historically D6 accepted at identity. This is not a fabricated original bipartite geometry.

**True original W34 and W38**: same construction, but physical cherry-center replacement uses shared edges 01,12,23,34; A exclusive 45,05; B exclusive 46,06. Actual physical K_a has coordinate6 for s>=4; original POINT/LINE source factor counts 85/585, incidence counts 425/5265. Eight original distinct LINE neighbors from eight source POINT stars exist by Hall: each star has s+1>=5 original LINE factors, any TWO source POINT stars overlap in at most one LINE, and for k<=8 a set of k original POINT stars has at least k(s+1)-C(k,2)>=k distinct LINE neighbors (since s>=4). Complete both f/g injections in original K_a. All-h h>=2 explicit simultaneous TRUE original two-fiber D6 coacceptance follows by the same Hall argument; W32 case verified separately via actual finite original GQ fixture.

For ALL three TRUE original GQs:
1. Enumerate EACH actual fiber's `(s+1)^6` SIX-DISTINCT original incidence Q once from the actual GQ, calculate real historical GF5 right-A dual hist and right-B/C fixed positive weights using source Q (not per-Q redraw).
2. On ALL **96 complete original global f-map states**, compute TWO independent full ORIGINAL historical seven-GF5 class counts by directly retagging EVERY right-eligible ORIGINAL Q for both fibers. Check that each score agrees EXACTLY with its fixed-right dual histogram formula and that one family's exclusive swap leaves the other's score unchanged.
3. Independently calculate actual 96-state covariance, the two 24-state conditional shared means, the six shared transposition cross-squared-gradients and mixed gradients, including exact rational cancellations. Verify `Cov_96=Cov_24(u,v)`, the E_shared products equality and the `9/16` spectral squared bound, with exact `Fraction`.
4. Fail closed for duplicate source POINT IDs, malformed globally injected maps, incorrect group states and physically incompatible family-geometry. Pin numerical results on final exact HEAD, and inspect for positive or negative TRUE original covariance rather than inferring its sign from abstract spectral existence.

The 96-state action is a consciously chosen SUBGROUP of globally legal whole-original f image permutations preserving both sixedge physical C6 supports. It does NOT exhaust all 8!=40320 possible f assignments nor full original GQ all-seven sixflag S. The covariance bound is all-h conditional, but does not close root issue #230 Branch A/B/C or prove any universal positive R3/ASET exponent.

## 5. Scientific acceptance

Only add this Draft after successful exact-head hosted CI, direct raw original sevenclass tests, independently qualified mathematical review and acceptance of parent PR stack; do not merge into main or claim root solved. Strongest NEXT research question after this exact overlap theorem is whether positive or negative covariance can be compelled/blocked by TRUE original W3 GQ incidence constraints across **all** overlapping source POINT fibers under a SAME arbitrary fixed global f,g. A positive 96-orbit average does not force positive original-center all-seven S_s.
