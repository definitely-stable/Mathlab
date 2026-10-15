# HYP-105 / issue #230 — D6-AA4-AG: deterministic occupied two-triangle mass and original Hall barrier

Status: research-only **restricted all-h theorem**. Child of AA4-AF [PR #514](https://github.com/definitely-stable/Mathlab/pull/514), pinned parent commit 557feadcaebc26d2a376c4d510f6f6e68e3f5fe8. One genuine original W(3,2^h) incidence graph, two independent typed but each internally **globally coherent** complete injections f,g into unordered edges of a minimal physical K_a. A statement for **every f and g**, not for random draws. This document does not prove issue #230 Branch A, B or C.

## 1. New AG-1 theorem: all-map physical pre-Hall mass

Put s=2^h, h>=19, V=(s+1)(s²+1), a=min{t:binom(t,2)>=V}, K=binom(a,2), m=K-V<=a-2. For each genuine original point p and unordered pair {l0,l1} of distinct true original lines through p, use the actual original incidence IDs (p,l0),(p,l1). Consider:

1. An occupied physical four-cycle C4 inside the complement of the two physical coordinates of f(p), whose four distinct physical edges globally inverse-map to four different real original points q0..q3.
2. Two disjoint physical triangles on six opposite coordinates containing the globally fixed images g(l0),g(l1) in separate triangles. All four other physical edges are **occupied** under that very same complete injection g, and inverse-map to four different actual original lines.

Count each indexed tuple (p,{l0,l1},C4,H) once. Its existence does **not** guarantee the four required q_i-to-inverse-line incidences exist in the true original GQ. Call the total P_triangle(f,g), a physical pre-Hall mass, not a count of accepted original six-Q.

For all full globally injective typed map pairs and all s=2^h >= 2^19:

    P_triangle(f,g) >= s^14 / 256.

No randomness, no expectation, no fake full physical surjectivity if m>0, no induced physical orbit quotient and no source geometry averaging occur in the statement.

## 2. All-h proof: few exceptional actual original line-root pairs

The physical hole graph on K_a has exactly m missing edges; its degree sum is 2m. Mark physical coordinates with missing degree at least a/16; there are at most floor(32m/a)<=32 such coordinates. At most 32(a-1) physical occupied original line factor images touch a marked coordinate.

In genuine W(3,s), two different original lines intersect in AT MOST ONE original point (source graph girth eight). Thus all N=V*binom(s+1,2) actual original intersecting line pairs are distinct, and their distinct physical images form N different unordered pairs of occupied physical edges in K_a.

There are exactly a*binom(a-1,2) unordered pairs of physically adjacent edges in full K_a. At most 32(a-1)(V-1) pairs involving occupied images touching a marked coordinate are possible. Hence for every complete original g the number of *good actual original intersecting line pairs* with (i) disjoint physical images and (ii) hole-degree <a/16 at all four pinned endpoints satisfies

    N_good >= N - a*binom(a-1,2) - 32(a-1)(V-1).

For each such disjoint pinned pair uv,wx, let Y be free physical coordinates adjacent (through occupied edges) to both u and v, and Z similarly to w and x. There are at least a-4-a/8 choices for y in Y and at least a-5-a/8 choices for z in Z avoiding y. For a>=32 these are respectively at least 3a/4 and a/2. Each ordered y,z constructs one different physically **occupied** two-triangle H:

    {uv, uy, vy} union {wx, wz, xz}.

There are therefore at least a²/4 such real physical completions for every good pair. All six edges are globally occupied, not redrawn.

From AA4-AF, EVERY genuine original point p under every globally complete f has

    C4_occ(p) >= C4_floor
      = max(0, 3*binom(a-2,4) - m(a-4)(a-5)).

Since m<=a-2, algebra gives the independent strengthened bound

    C4_floor >= (a-2)(a-4)(a-5)(a-11)/8 >= a^4/128
    for a>=22.

For s>=8, the minimal alphabet inequalities 2V<=a²<=4s³ and V<=2s³ apply; N>=s^5/2. The above bad pair upper is <=132s^(9/2), and sqrt(s)>=528 whenever s is a power of two at least 2^19. Hence N_good>=N/2. All choices above are INDEXED; root and pinned flags are unique for their original line pair. Distinct C4 patterns and distinct occupied triangles give distinct indexed tuples. Therefore

    P_triangle >= (N/2) * (a^4/128) * (a²/4)
               = N*a^6/1024
               >= (s^5/2)*(8s^9)/1024
               = s^14/256.

The threshold h>=19 is a **conservative provable threshold**, not an empirical extrapolation or phase transition. The exact integer oracle also evaluates lower s without claiming this coarse threshold there.

## 3. New AG-2 exact deterministic Hall/C8 compensation identity

For every indexed tuple above, let M be the true original 4x4 point-line incidence submatrix between the four original point factors obtained from f and four actual original line factors obtained from g. The two pinned true flags already exist, and the four nonpinned flags must be selected via one true original perfect matching of M to create a real six-DISTINCT-incidence-ID Q. The physical type on the first side is B and on the opposite side is A (two disjoint physical triangles).

From prior AA4-AE, every such genuine W(3,s) matrix has permanent in {0,1,2}; permanent two occurs exactly for a chordless true original source C8. Partition indexed physical tuples as H0/H1/H2 according to their permanent. Then for the accepted original Q subset selected here, with multiplicity for distinct original matchings,

    P_triangle = H0 + H1 + H2
    T_triangle = H1 + 2 H2 = P_triangle - H0 + H2,
    0 <= T_triangle <= C_BA(f,g) <= S_s(f,g).

Here H0 counts blocked Hall instances, H1 unique original perfect matchings, H2 induced ORIGINAL C8 double completions. No mixing with artificial physical C8 or automorphism orbits, no independence assumption.

**Quantitative deterministic barrier:** If some adversarial globally coherent sequence has S_s(f_s,g_s)=o(s^6), necessarily

    (H1+H2)/P_triangle = o(s^-8).

For the bounded version S_s<=C*s^6 this fraction is <=256*C/s^8. Conversely, a new theorem saying that **all f,g** have Hall-positive density (H1+H2)/P_triangle >= c/s^8 for a fixed c>0 would suffice to prove the Branch A universal omega(s^6) floor. We do **not** prove that Hall density lower here.

This is a new **restricted sufficient condition** for A, NOT a model-equivalent reduction to the full seven-class S: other physical A 2-factors, other GF5 classes and D6 may remain positive when this triangle subclass is Hall-negative. A high Hall-failure proportion by itself is not a surprising obstruction — typical randomly injected pairs also have very sparse true original source matchings. The missing ingredient is a positive adversarial lower on Hall successes at the correct scale.

## 4. Exact finite independent checks, source and file protocol

Python module: research/hyp105_issue230_d6aa4ag_deterministic_triangle_hall.py. The all-h proof oracle uses only exact integer arithmetic, isqrt, binomial coefficients and explicit counting upper bounds; no finite fit. Independent 2-triangle oracles use (a) literal enumeration of all occupied y,z and (b) |Y||Z|-|Y intersection Z|. K6/K7 complete and deliberately incomplete K7/K8/K10 physical graphs are tested, including a pinned edge whose physical completions can all be destroyed.

Genuine original W(3,2) S68/S72/lex (both typed directions, actual original root and pair-of-distinct-flags selections) are checked via true source incidence row masks, all 24 original matching permutations in the prior independent AE oracle, exact source C8 charge and a cross-check that selected triangle counts cannot exceed the full AA4-AD 2-factor/Hall count. True original W(3,4) lex/random non-surjective physical embeddings, with m=6 holes, are checked on sampled actual root C4s with the same globally fixed f,g. No generated random fake incidence source.

Eight independent regression tests and a dedicated GitHub-hosted workflow are included in this stack child. CI passing is engineering evidence, not proof acceptance. Keep draft; require exact-head dedicated, INDEX, Proof Audit, Full Research and separate math review before RCP JSON claims and regeneration of the five derived Markdown registries. Do not merge to main or close #230 based on this restricted result.

## 5. Next mathematical milestone

Aim for a true all-h **Hall-positive lower** of order c/s^8 across this guaranteed indexed candidate mass under arbitrary correlated global f,g; or prove compensated positivity using the full seven accepted GF5 classes plus genuine D6. If such a lower fails, an infinite genuine complete-global-map counterfamily to the restricted Hall lemma is informative but by itself neither Branch B (requires full S=o(s^6)) nor a final R3/ASET upper bound.
