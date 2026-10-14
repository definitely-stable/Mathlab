# HYP-105 / issue #230 — JPKC-016: true ORIGINAL two-D6 overlap

**2026-10-14 research-only Draft.** Strict child of JPKC-015 [PR #455](https://github.com/definitely-stable/Mathlab/pull/455), parent HEAD `c02188a4d4f2e4e07440c4d7b25fc25c6dd31b3e`; no main mutation/merge. Root A/B OPEN.

## 1. Methodological blocker after the all-h D6 first moment

JPKC-015 proves the exact mean of the positive seven-family D6 subset in the ensemble of two INDEPENDENT UNIFORM WHOLE ORIGINAL point/line GLOBAL injections into unordered physical K_a pair labels, with a minimal such that C(a,2)>=V=(s+1)(s²+1):

`E[D6]=M6(s)*p(a)~(16/3)s^6`, where `p(a)=60*((a)_6/(N)_6)^2`, `N=C(a,2)`, `M6(s)` counts true ORIGINAL six-edge point-line **matchings**.

The next rigorous question is the second moment `E[D6²]`, a sum over **ordered pairs** (Q,Q') of ORIGINAL source matchings. Events are NOT independently sampled per sixset: all share the same GLOBAL physical pair injection. Even disjoint original incidence-ID sets may share original point or line factors. Conversely, even when they share NO ORIGINAL factors on EITHER source side, the physical pair labels are sampled WITHOUT REPLACEMENT and correlate them.

This slice gives an exact all-h physical second-moment kernel for the source-factor-disjoint sector, exact original source-overlap rows for a genuine W32 anchor, and a rigorous partial lower contribution. **It does NOT compute a full E[D6²], variance or universal low-tail bound.** Do not silently replace mixed source overlaps by products p².

## 2. J54 — sixcycle-avoidance polynomial for one prior physical D6

Condition on a first six-edge true source matching Q being physical D6. Its left and right physical unordered pair images each comprise the six distinct physical K_a edges of a connected coordinate 6-cycle. For any second original matching Q' with source point and line factor sets both disjoint from Q, its six images on EACH side must avoid those six occupied K_a physical edge labels because the original factor maps are globally injective.

Let H_a be the number of unoriented connected Hamiltonian six-cycles in K_a (on any six vertices) whose *edge set* is disjoint from a fixed prescribed physical coordinate C6. H_a depends only on a.

**Exact inclusion-exclusion of the six forbidden physical K_a edges:**

`H_a = Σ_{F⊆E(C6)} (-1)^|F| h_a(F)`.

If F is empty, `h_a(∅)=60*C(a,6)`. If F=E(C6) completely, `h_a(F)=1`. For any nonempty proper subset F of k<6 edges consisting of p path components occupying t=k+p physical coordinate vertices,

`h_a(F)=C(a-t,6-t) * 2^(p-1)*(5-k)!`.

This is an EXACT finite positive integer for a≥6; no distributional or all-h Root-A hypothesis. The complement sixcycle count is independently checked by brute graph enumeration of Hamiltonian 6cycles for a=6,7,8,9, not by reusing the same inclusion-exclusion routine.

## 3. J55 — exact all-h global-injection joint kernel for completely original-factor-disjoint Q,Q'

Each Q has 6 ORIGINAL point factors and 6 ORIGINAL line factors. Let Q' share NONE of those point factors AND NONE of the line factors (not merely edge-disjoint). Let `p=60*((a)_6/(N)_6)^2` be JPKC-015's first-event D6 probability.

Conditioned on first-event D6, on either half Q' receives a uniformly random ordered six-tuple of pair labels drawn injectively from the N-6 remaining physical pairs. There are 60 possible named ORIGINAL Q' column duals. Each physical sixcycle avoiding first-event physical occupied edges contributes 6! ordered assignments of six Q' incidence columns to its six edges. Those 6! assignments are equidistributed across the 60 named duals; hence for a *fixed* named dual there are 6!/60*H_a=12H_a possibilities on each side.

Both source original factor maps remain independent conditional on the matching physical Q dual; the two first-event physical C6 graphs are isomorphic (not literally the same coordinate labels) and therefore both sides have the same H_a. As a result, EXACTLY,

`P(D6(Q') | D6(Q)) = 60*(12*H_a/(N-6)_6)^2`,

`P(D6(Q) and D6(Q')) = p * 60*(12*H_a/(N-6)_6)^2`.

This formula enforces the full original GLOBAL injections without replacement; it is not a local independence approximation. At a=6, direct H_6=3 gives

`p=12/5,010,005`, `P(second|first)=1/47,040`,
`P(both)=1/19,639,219,600`,

so the source-factor-disjoint two-event ratio over the naive product is approximately **8.875434**, i.e. strictly POSITIVE covariance even with ZERO source overlap. The correlation tends to zero RELATIVELY in the a→∞ limit, since H_a~(a)_6/12 and (N-6)_6~N^6, but the finite effect invalidates any source-disjoint independence assumption.

## 4. J56 — true W32 ORIGINAL source overlap fingerprint (anchored row)

A NEW exact original incidence bipartite source DP, independent of physical f,g and historical seven_census, chooses one fixed genuine original six-edge matching Q0 by original incidence IDs. For every other true W32 six-edge ORIGINAL matching Q', compute the exact histogram over

`(i,j,k) = (|points(Q')∩points(Q0)|, |lines(Q')∩lines(Q0)|, |original_incidence_IDs(Q')∩original_incidence_IDs(Q0)|)`.

The DP state is `(used original right-line 15-bit mask, already-shared original point count, already-shared original incidence-edge count)`; right-factor overlap j comes from final mask intersection. It processes all 15 true original point factors and derives exact integer multiplicities for all possible anchored overlap signatures, verified to total the independently established **M6(W32)=1,566,360**. The unique diagonal original matching produces signature (6,6,6) with count one.

Independently reverse the two ORIGINAL bipartition directions; signature i,j are normalized back into source point/line order, and each exact histogram cell must match. This is an **exact row relative to Q0**, NOT the complete 1,566,360×1,566,360 pair tensor and NOT a claim that (i,j,k) alone determines all mixed-overlap D6 joint probabilities. Full gluing type may depend on more than those three integers.

The number of source-factor-disjoint Q' from the anchored Q0 is exactly the (0,0,0) cell, and each of these true Q' has the exact J55 joint physical kernel.

## 5. J57 — all-h rigorous lower sector of the D6 second moment

Write `I_Q=1{D6(Q)}`, `D6=Σ_Q I_Q`. Exactly

`E[D6²]=Σ_(ordered Q,Q') P(I_Q=I_Q'=1)`.

The diagonal sector contributes `M6*p`. The source-factor-disjoint ordered sector contributes **exactly** `N00*p_joint`, where N00 is the number of ordered pairs of source six-matchings sharing no ORIGINAL point and no ORIGINAL line. Mixed types are NONNEGATIVE but UNCOMPUTED.

For any fixed true original six-matching Q, it occupies six original points and six original lines, forbidding at most 12d original incidences in d=s+1 regular W(3,s). After choosing j≤5 further source-disjoint matching edges, at most 2jd further original edges are forbidden. For V>22 (all s=2^h≥4),

`#Q' completely source-factor-disjoint from Q >= Π_(j=0)^5( M-(12+2j)d )/720=:D_min(s)>0`.

Consequently for all such s,

`E[D6²] >= M6(s)*[p(a)+D_min(s)*p_joint(a)]`,

and with the JPKC-015 lower M6 floor one obtains an entirely explicit all-h second-moment **lower bound**. At W32 s=2 the coarse greedy bound D_min is zero, yet an independent exact pinned anchored overlap DP can witness a positive (0,0,0) cell and contribute two strictly positive offdiagonal terms to a W32 second-moment lower bound.

An exact second-moment LOWER bound does not supply an upper variance/concentration bound or a worst-case positive minimum. The sharp asymptotic mass from disjoint pairs is consistent with first-moment squared (as s→∞), but mixed SOURCE factor overlap types and physical embedding constraints remain uncontrolled in this slice.

## 6. Acceptance and next blocker

Five+ hosted fail-closed tests, physical independent graph C6 oracles, exact Fraction pair probabilities, genuine true original W32 anchor histogram and swapped-bipartition verification, all-h analytic disjoint-source matching floors, dedicated matrix and INDEX/Proof Audit/Research workflows MUST be SUCCESS on exact HEAD. No merges or main edits, independent mathematical review required.

Next JPKC-017 should classify two-matching **union bipartite incidence gluing graphs** beyond the crude (i,j,k) summary, derive physical pair-embedding kernels for shared original factor supports with guaranteed original global injection, then combine exact source overlap multiplicities. A full E[D6²], lower-tail concentration and Root A/B remain OPEN.
