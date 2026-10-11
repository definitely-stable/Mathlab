# HYP-105 B3.2-E1-C24-B6 — exact all-h joint-touch curvature bound and original W32 radius-two audit from S68

Date: 2026-10-11. Scientific child of [C24-B5 PR #352](https://github.com/definitely-stable/Mathlab/pull/352) -> [B4 PR #348](https://github.com/definitely-stable/Mathlab/pull/348) -> [B3 #347](https://github.com/definitely-stable/Mathlab/pull/347). Root [issue #230](https://github.com/definitely-stable/Mathlab/issues/230). **Research-only stacked branch, no `main` modifications or merge.**

## Why this slice

C24-B4 exhibited a genuine original globally coherent W(3,2) seven-score **S=72** complete right labeling that was strictly one-global-right-transposition stationary. C24-B5 then exhaustively evaluated all 5,005 distinct states at exact transposition distance two from that S72 map and established **S=68** by commuting original right-line swaps (4,14) and (3,12), with a temporary barrier +10 and signed mixed discrete curvature -31. Two globally coherent two-swap endpoints improved S72. The exact W32 numerical result is finite; a single negative mixed curvature does not prove an all-h obstruction or a total GF5 R3 bound.

**B6 must start from the actual S68 map**, not confuse “the best state in the distance-two sphere centered on S72” with “locally optimal around S68.” The frozen complete right map is

    g68=(12,9,11,4,1,6,0,13,5,14,3,7,2,10,8)

with true original fixed left f=(13,4,2,14,0,11,1,7,10,6,9,5,12,3,8), seven vector (0,44,21,0,0,2,1), necessary GF5 Q7=3,112,510, original accepted right-C=0. One globally common original right map is used for all sources.

## 1. All-h joint-support theorem — exact count and valid but nonsharp absolute bound

For any order `s=2^h>=2` genuine original GQ host, any legal complete globally coherent f,g, any fixed accepted seven static candidate family of DISTINCT ORIGINAL six-incidence sets J (with original line support H(J)), and any disjoint pair of global original-right transpositions A=(i,j), B=(k,l), define indicator `X_J(g)` in {0,1} for the accepted original sixset J under right map g.

The exact mixed individual source contribution is

    kappa_J(A,B;g) =
      X_J(gAB) - X_J(gA) - X_J(gB) + X_J(g).

If H(J) fails to touch A, swapping A does not change any of the two paired conditions; similarly for B. Hence the exact SUPPORT CANCELLATION lemma is

    kappa_J=0 unless H(J) intersects both A and B.

For every original J, its four indicators are Boolean, so `|kappa_J|<=2`, and therefore, with original multiplicities w_J when compressing,

    |kappa_AB| <= 2 M_AB,
    M_AB = sum_{J: H(J) touches A AND B} w_J.

This does NOT presume the different original sixsets are statistically independent, does not mix their static tags, and does not apply symmetric curvature to overlapping transpositions (noncommutative 3-cycles).

For n original right lines and a given H of r lines, let K(n,r) be the number of **unordered PAIRS** {A,B} of *disjoint* transpositions for which H touches both. Exact elementary inclusion-exclusion yields

    2 K(n,r) =
       C(n,2)*C(n-2,2)
       - 2*C(n-r,2)*C(n-2,2)
       + C(n-r,2)*C(n-r-2,2),

where C(u,2)=0 when u<2. This is a counting identity for all integer 0<=r<=n, n>=4, and does not depend on the assigned physical right labels. In particular K(n,0)=K(n,1)=0; K(n,n)=3*C(n,4). An independent small-n exhaustive disjoint pair oracle checks n=4..6 and every 0<=r<=n.

Summing triangle inequality over *all disjoint swap pairs* gives the exact deterministic all-h joint-exposure CAP:

    sum_{ {A,B} disjoint } |kappa_AB|
        <= 2 * sum_J w_J K(n,|H(J)|).

This is a **structural absolute upper** on possible interaction, not a useful positive lower on `S_seven` by itself. In particular it does NOT show a negative curvature must exist, that the sum of signed curvatures has a particular sign, or that a small S map always admits any local move. Establishing one of those implications would require original GQ incidence-specific signed correlation inequalities and quantification over **every f,g,h**.

For the original finite W32 source, the executable checks source multiplicity 53,907 statically eligible distinct sixsets, original support histogram, all 4,095 disjoint double transpositions, computed sum of absolute curvatures <= exact exposure cap, and independent source-level mixed curvature for the most negative observed pair. **Stronger full finite falsifier:** independently compress original candidate sixsets by their actual line-support bitmask, for EACH of the 4,095 disjoint swap pairs compute the exact original jointly touched count M_AB, verify EVERY individual |kappa_AB| <= 2 M_AB, and verify that the sum of these 4,095 directly enumerated M_AB agrees EXACTLY with the analytic sum over the source K(n,|H(J)|). No probabilistic extrapolation or independent map-per-J choice.

## 2. Exactly the genuine finite W32 radius-two neighborhood around S68

The accepted C24-B5 right physical K6 edge-pair template inverse-image oracle is retained. For the frozen true original S68 globally complete right map, the code evaluates all:

- **105** distinct one-transposition globally complete right maps;
- **910** directed 3-cycle right maps (each with exactly three ordered decompositions);
- **4095** disjoint double-transposition right maps (each with exactly two ordered decompositions);

for **5005 unique exact distance-two maps**, **10920 ordered two-swap paths**, and an inclusive radius-two ball of **5111** global right maps.

Every candidate's full seven-vector, original right-C projection, exact integer necessary GF5 numerator Q7, and S are computed by 130 right physical K6 2-factor template pullbacks from the original 53,907 statically eligible sixsets. Compare *the best one-swap* AND *the best exact-two-swap* with S68: either may dominate. **Do not assume S68 is stationary.**

For the best two-swap endpoint and representative 3-cycle/disjoint/max-score endpoints, separately verify full original LEFT 51,506 compressed row scoring and an independently implemented **RIGHT-FIRST 62,370 DISTINCT original six-incidence set** enumerator. Also fully verify the best one-step source score in both orientations.

For **all 4095 disjoint pairs**, calculate exact signed curvature from the four total scores. Count negative curvatures and strict improvements separately. For the most negative pair, recompute kappa from *jointly-touched ORIGINAL sixsets*, test the all-h pointwise 2*M_AB cap, and assert equality with the four-score expression. If the best two-step endpoint is disjoint, independently recount its source-level mixed kappa too; if 3-cycle, do NOT call it a symmetric Hessian.

**No output minimum is pre-asserted before the first actual GitHub-hosted computation.** Any numeric finding should then be pinned by exact regressions with an independent provenance note. A finite escape is a counterexample to a *finite local-optimality implication* only; it is neither Branch B (which demands an infinite sub-sixth-power correlated family) nor a proof of the universal Branch A. No all-15! right-map minimum is claimed, no all-f left optimizations, no total GF5 R3 or ASET exponent.

## 3. Runtime and correctness gates

A dedicated GitHub-hosted B6 Contract must separately run fast unit tests of small-n K(n,r), original weighted support histogram, frozen true original S68, true source-level mixed indicator recounts; then perform one full finite 5005-state report. The full six-shard Research suite and seventh fail-closed aggregate retain every predecessor named command, append exactly two B6 named commands, freeze the new independent FNV1a64 hash, and keep large 5005-state scans **out of broad Unit tests**. Require latest exact PR HEAD C24-B6 Contract/Research/INDEX SUCCESS before accepting. No self-hosted runners, and do not merge stacked PRs automatically.

Outcome at code creation: ALL-h_EXACT_DISJOINT_JOINT_SUPPORT_EXPOSURE_IDENTITY_AND_ABS_CURVATURE_CAP / FINITE_TRUE_ORIGINAL_W32_COMPLETE_S68_RADIUS_TWO_IMPLEMENTED_CI_PENDING / HYP105_ROOT_OPEN_WITH_FORMAL_BLOCKER.
