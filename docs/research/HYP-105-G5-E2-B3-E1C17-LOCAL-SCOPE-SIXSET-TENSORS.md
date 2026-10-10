# HYP-105 B3.2-E1-C17 — original sixset-local two-sided tensor

2026-10-11. Parent issue #230, stacked upon scientific C16 PR #305. Parallel CI-only PR #306 is not a scientific dependency.

**TYPE: ALL-FINITE SUPPORT-LOCALITY LEMMA + RESTRICTED EXACT W(3,2) EXECUTABLE.** No universal positive all-h Omega(s^6), full GF5 R3, all-W32 15!^2 minimum or ASET exponent.

## Scope theorem valid on ANY finite original incidence host

Let H=(P,L,I) be a finite bipartite original incidence graph with injective original-factor-point/line to distinct occupied physical pair-edge maps f,g. Fix genuine partial injections f0,g0. For each DISTINCT original six-incidence set J subset of I, define a_J(f,g) as its accepted seven-class indicator, zero when the physical-left 2-factor requirement fails; likewise b_J(f,g) as its nonnegative accepted GF5 necessary numerator, zero when ineligible.

**Support locality.** Both scores depend ONLY on f restricted to original P(J) and g restricted to original L(J). Neither physical labels at any other ORIGINAL factors nor any arbitrary canonical filler can change a_J,b_J. The accepted physical projections use exactly the six ORIGINAL incidence edges and their endpoint labels.

Let U_J be P(J) minus the pinned-left domain, and V_J be L(J) minus the pinned-right domain. Partition the ORIGINAL sixsets into disjoint W_uv with (U_J,V_J)=(u,v). For LOCAL original-to-unused-physical injections alpha and beta define T_uv(alpha,beta) as the sum of a_J on W_uv, using partial f0+alpha,g0+beta and any full filler. Support locality makes T unambiguous. Every valid local injection extends to at least one full original-to-physical injection because unused source and physical edge sets have equal sizes.

For EVERY one legal common complete descendant (f,g):

    L_poly = sum_(u,v) min_(local alpha,beta) T_uv(alpha,beta)
           <= S_seven(f,g).

The same nonnegative proof gives an independent L_poly_GF5 necessary numerator. The separately minimized local clusters are NOT asserted simultaneously attainable full f,g witnesses.

**Complexity gate:** for a fixed six-incidence motif size, a direct general implementation enumerates at most binom(|I|,6) original sixsets and at most (V_left)_6*(V_right)_6 local assignment options per signature. Thus O(|I|^6 * V_left^6 * V_right^6) elementary classification work (up to bookkeeping), polynomial but prohibitively high degree. This is an algorithmic support reduction, NOT a positive all-h lower bound. The CURRENT executable is only W(3,2) with <=3 unpinned on either side and still enumerates <=6 full LEFT templates to obtain its finite source union.

## Relation to C15 and C16

Let T_empty,v denote groups whose every original left point is pinned. Preserve their ONE COMMON right full completion:

    L_frozen = min_(full g) sum_v T_empty,v(g restricted to v).
    L_shared = L_frozen + sum_(u nonempty,v) min_(alpha,beta) T_uv.

Then for S, and independently for accepted GF5 necessary numerator,

    0 <= L_poly <= L_shared
       == L_C16_two_sided_signature
       <= L_C16_one_left_group
       <= L_C16_one_shared_left
       <= L_C16_full_joint_exact
       <= real S_seven(f,g).

Equality of L_shared and C16 signature follows since every local assignment extends to a full (f,g), while the class of one J depends only on its touched original vertices. Importantly, L_shared may require factorial work to calculate its L_frozen shared-right term. ONLY L_poly has the straightforward polynomial-time bound above. This logical separation is mandatory.

## True W32 implementation and falsification

Executable: research/hyp105_g5e2b3e1c17_local_scope_tensors.py.
Independent tests: research/test_hyp105_g5e2b3e1c17_local_scope_tensors.py.
Dedicated hosted workflow: .github/workflows/hyp105-c17-contract.yml.

1. Enumerate exactly 62,370 original left-2factor sixsets for EACH genuine residual left map, deduplicate by SIX ORIGINAL incidence IDs. The source union is NOT the arbitrary filler source.
2. Group by named original touched unpinned LEFT points and RIGHT lines; tabulate local injective assignments into unused physical edge pairs for those touched vertices ONLY. Classification zeros represent absent left sources, never fabricated candidates.
3. Independently calculate one-common-right frozen-left baseline; return both pure-local polynomial-style lower and right-coupled C17 lower for seven and GF5 separately. No F x G joint score matrix is allocated.
4. Compare exact C17 right-coupled signature against C16 for the real reverse-line W32 3!^2=36 joint map box and an independently chosen non-prefix 2!^2=4 box; test off-support invariance, fully pinned seven census equality, duplicate-source elimination and budget failures.
5. Fail closed above 3 missing LEFT / 3 missing RIGHT, above 6 complete-left source templates, above 400,000 source instances, or above 10,000,000 local classifications.

Historical C15 root lower S=12 and accepted GF5 necessary numerator=513393 are fixed anchors. Do NOT report unverified C17 pure-local numeric values or performance improvements before exact-head hosted SUCCESS. This does not establish the universal positive lower in issue #230.

## Next theorem gate

A meaningful C18 must establish a positive all-h lower for the tractable L_poly under GQ incidence and physical two-factor constraints, OR a rigorously quantified zero-floor obstruction showing the relaxation cannot deliver Omega(s^6). Do not substitute bounded-W32 exhaustive success for such a theorem. No integration or branch status promotion without exact-head Research and dedicated checks.
