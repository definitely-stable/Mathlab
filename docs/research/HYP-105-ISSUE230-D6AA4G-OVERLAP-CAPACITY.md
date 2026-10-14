# HYP-105 #230 — D6-AA4-G: overlapping ORIGINAL triads and physical-capacity controls

**Status: RESTRICTED_THEOREM_C / OPEN_WITH_FORMAL_BLOCKER.** All-h conditional frozen-outside separator identity, independent D6-X/Y physical-capacity adversarial checks, and exhaustive ORIGINAL W(3,2) pure-four-factor source fibers. No universal seven-class positive bound, infinite Branch B witness, full R3, or ASET exponent.

Stacked Draft on AA4-F PR #444, parent HEAD 1e44610b79ca1edcda872bce38f5524167b61181 (4/4 CI SUCCESS). Do not modify or merge main; issue #230/#176/#169 remain OPEN.

## 1. Motivation

AA4-E's globally-injective unary-price dual has a rigorous three-source integrality gap 0<1. AA4-F classified all actual ORIGINAL W32 sixset candidates for selected coherent source triples and established strict pair-to-triple gaps (S68 +2/+9; S72 +5/+1). JPKC-011 found 63/68 S68 and 66/72 S72 original positive Q with no coordinate-proper physical P3. Thus a physical-path-only surrogate cannot substitute for the full accepted seven-class GF5 predicate. The next step must couple overlapping ORIGINAL source-factor clusters without pretending locally chosen sixsets can assign physical labels independently.

## 2. Exact all-h conditional two-triad separator theorem

Fix arbitrary h>=1, s=2^h, a genuine ORIGINAL W(3,s) incidence host and arbitrary full globally injective typed pair maps f,g. Freeze assignments OUTSIDE any block B of precisely four typed ORIGINAL point/line source factors; J(B) denotes ALL genuine globally typed-injective complete assignments to B, including spare physical edges for h>=2. Each distinct ORIGINAL six-incidence set Q has true source dependency T(Q) intersect B; c_Q(t) is the accepted seven-GF5 nonnegative indicator, or its nonnegative selected GF5 floor numerator, evaluated under ONE complete t.

Pick shared ORIGINAL source pair C of the four factors; A=C union {k}, D=C union {l}, where k,l are the remaining two factors. Assign EVERY Q exactly ONCE to A when its touched support is contained in A, otherwise to D if its support is contained in D, else to residual R (which includes genuine four-source Q and supports containing both k and l). Let r=sum over Q in R of min over full t in J(B) c_Q(t).

For any overlap assignment z actually realized by a full state t in J(B), define a(z)=min over complete t with t|C=z of sum over Q in A c_Q(t), and d(z)=similarly for D. Define

L_ind = sum_Q min_t c_Q(t),
L_unlinked = min_t sum_{Q in A}c_Q(t) + min_t sum_{Q in D}c_Q(t) + r,
L_sep = min_z (a(z)+d(z)) + r,
L_joint = min_t sum_Q c_Q(t).

THEOREM (for ALL h>=1 and ANY starting genuine f,g, with OUTSIDE frozen):

0 <= L_ind <= L_unlinked <= L_sep <= L_joint <= S_s(f',g')

for every genuine completed f',g' agreeing with the frozen outside assignment.

Proof: each local Q minimum is no greater than its cost in any genuine complete assignment. A group's sum of local minima is at most its common-assignment minimum. Conditioning both triad costs on the SAME separator z cannot lower their independent unconditional minima. Every complete assignment with separator z incurs at least a(z) on A, d(z) on D, and at least r on residual; taking minima over z and over all complete states proves the chain. The source factor identities and original incidence IDs, including all six ORIGINAL positions, are fixed. Cross-type physical edge reuse is allowed and injectivity is enforced IN each type only. No GF5 event is duplicated.

There are six choices of shared pair and two orientations of the remaining factors (12 covers). Taking the maximum of these valid lower bounds is still valid. At true W32 with zero unused physical labels, a pure-type four-factor block has 4!=24 globally complete permutations; for s>=4 the additional freed/unused physical pairs require larger fibers. The executable exhaustive engine intentionally only handles W32 fixed-image blocks; the all-h theorem is symbolic, NOT an all-h solver.

The new separator bound is NOT necessarily stronger than the independently globally-priced AA4-E lower on every instance. Never sum distinct bounds on the same Q events; their maximum, if separately sound on the same instance, is valid.

## 3. Required independent D6-X/Y adversarial regression

D6-X (PR #424): for s>=4 the local-star zero-accepted-GF5 pseudomarginal violates a globally valid lifted column capacity cut. For adjacent distinct physical edges e,e':

E[x_(p,e)*(1-sum_(q!=p)x_(q,e'))] = 1/K - (V-1)/(a(a-1)(a-2)) < 0.

At genuine W(3,4), (V,a,K,m)=(85,14,91,6), the exact negative slack is -5/182. This pseudomarginal is NOT feasible under that selected global column lift and is not a standard SA-integrality-gap construction.

D6-Y (PR #425): the physical-image adjacency upper, an Ahlswede–Katona near-complete special case, is

A_max = a*C(a-1,2) - 2*m*(a-2) + C(m,2),

with m=K-V<=a-2 and sharpness attained by deleting a common-center star of m physical edges. A selected locally-injective two-site pseudomarginal passing specifically selected physical-column lifts achieves expected V*(a-2) physically adjacent original factor pairs. Their difference m*(a-2)-C(m,2) is >0 whenever m>0. At s=4: A_max=963, fake expectation 1020, gap 57. These are independent regression tests of ALREADY KNOWN prior results, not new GF5 risk lower bounds, nor full Sherali-Adams/SOS feasibility claims.

## 4. Actual ORIGINAL W32 exact independent GF5 audit

For each genuine pinned S68 and S72:
1. Recover all actual W32 original incidences, reconstruct full original seven-positive Q and require the AA4-D transversal counts 53/119 across all C(30,4)=27,405 supports.
2. Choose deterministically the first genuine all-four-point and all-four-line original support transversal. Freeze remaining 26 typed ORIGINAL source factors.
3. Exhaust all 4!=24 globally injective pure-type label permutations for each chosen block. For EACH full complete map, execute the historical GF5 seven_census of ALL 62,370 actual ORIGINAL sixset candidates. Keep original six source incidence IDs, class and GF5 floor weight per Q.
4. Rebuild each original Q's exact dependency intersection with the chosen block. A Q's value must be identical on any two full global states with identical labels on its claimed true original source-factor support. Fail closed on any dependency violation.
5. Evaluate ALL 12 two-triad covers for both nonnegative unit positive-seven count and weighted selected GF5 numerator. Require recomposition across all Q to equal full original census for all 24 complete states.
6. Compare the exact joint fiber min against AA4-D's known range. This is a conditional finite BLOCK result, not an all-W32 minimum and not a universal all-h bound.

This branch does not import unmerged JPKC-012 code. Independent JPKC-012 PR #443 found genuine W32 source-line-profile independent minima 11 -> coherent 68 (S68), and 0 -> 68 (S72), further justifying original-factor common-assignment constraints.

## 5. Acceptance and scope

New research implementation and independent tests validate fully-injective typed four-source assignments, strict source dependency and complete Q-table GF5 recomposition, all 12 valid covers, random nonnegative cost falsifiers and D6-X/Y capacity formulas. Dedicated GitHub-hosted independent test plus two actual-original W32 per-scheme full matrix jobs, plus INDEX / Proof Audit / full Research workflows are required SUCCESS on the exact final HEAD. Mathematical peer review remains OPEN until separately performed.

Scientific status: OPEN_WITH_FORMAL_BLOCKER. No uniform positive c*s^6 lower and no infinite Branch B construction. Next D6-AA4-H: combine actual ORIGINAL source-cluster coherence and global physical-image capacity constraints in a tractable source-independent dual/LP; test against X/Y marginal falsifiers, JPKC-011 invisibility and JPKC-012 source-profile tensor. Do not expand finite radii without a new all-h invariant.
