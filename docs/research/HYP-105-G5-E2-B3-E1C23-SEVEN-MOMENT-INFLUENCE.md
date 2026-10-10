# HYP-105 B3.2-E1-C23 — exact all-seven mean for ONE globally uniform right bijection and all-h swap sensitivity

Date: 2026-10-11. Parent [#230](https://github.com/definitely-stable/Mathlab/issues/230). Child of [C22 PR #327](https://github.com/definitely-stable/Mathlab/pull/327) -> C21-D #321 -> C21 #317 -> C20 CI #316 -> C20 #315. This is an **ALL-h exact FIRST-MOMENT identity and ALL-h upper bound on worst-case transposition influence**, with exact genuine W(3,2) finite sources. It is NOT a lower on every global right map, not full GF5 R3 or ASET exponent.

## 1. Original GQ factor-label quantifiers

For s=2^h>=2, V=(s+1)(s²+1), Delta=s+1, a minimal integer with binom(a,2)>=V. Let F_L,F_R be occupied size-V subsets of K_a physical pair edges; let f map ALL V ORIGINAL GQ points bijectively to F_L and g map ALL V ORIGINAL GQ lines bijectively to F_R, globally coherently across all original incidences.

Let J be one DISTINCT ORIGINAL six-incidence set with physical left six-coordinate degree2 projection. Its original right endpoint multiplicity profile r(J) can be A=(1^6), B=(2,1^4), C=(2^3), or inadmissible; its original left endpoint multiplicity profile and physical left column-position dual determine which of the seven accepted classes it *could* enter, using the frozen B0 classifier. D6 additionally requires strictly matched connected left/right column-position dual cycles; unaligned A/A is rejected. For any original right multiplicity class r, under **one** uniform random complete global right map g, the images of the distinct ORIGINAL right lines appearing in J form a uniformly random ordered injection into F_R. No other random right mapping is sampled for any other original J.

## 2. Exact physical six-coordinate multigraph decomposition — ALL-a

Every physical six-edge multigraph of unordered pairs (with repeats allowed) spanning exactly six physical coordinates of degree two is a disjoint union of cycles whose lengths are at least two, with a two-cycle represented by a doubled physical pair edge. The only possible length partitions of six are:

- A physical simple 6-cycle (60 physical patterns per 6-set) or two disjoint triangles (10), giving **T_A(full K_a)=70 binom(a,6)** distinct simple six-edge factors;
- one doubled physical edge plus a disjoint physical C4 (15 choices of doubled pair times 3 C4 choices), giving **T_B(full K_a)=45 binom(a,6)** distinct physical six-edge *multisets*;
- three doubled disjoint pair edges (15 perfect matchings), giving **T_C(full K_a)=15 binom(a,6)** distinct physical six-edge multisets.

Therefore there are exactly **130 binom(a,6)** physical 2-factor multisets over the full K_a, each counted once, and at most this many when some physical pair labels are missing.

For an arbitrary occupied F_R subset of K_a of size V, let T_A(F_R),T_B(F_R),T_C(F_R) denote the numbers of physical six-coordinate factors of these types for which every used pair label belongs to F_R. Let C6(F_R) be the number of simple physical six-cycles in F_R. Each count is a nonnegative integer independent of any original GQ-label injection, and the finite target oracle enumerates these exactly for a<=14 (K6 and missing-edge K14 genuine examples). The all-h identities below do not require that enumeration.

## 3. Exact ALL-h expected seven-class formula for ONE shared uniform global g

Fix one original six-incidence J with k distinct ORIGINAL right lines and one admissible source profile. Let (V)_k denote the ordered falling factorial. Physical successful injections of those k named original line objects into occupied F_R are exactly:

- profile A (six distinct): 6! T_A(F_R) ordered right assignments among (V)_6;
- profile B (one named right line repeated in two original incidence columns, four other named right lines distinct): 4! T_B(F_R) ordered assignments among (V)_5. The doubled physical edge is fixed by its ORIGINAL source identity; no bogus factor 5! or 6!;
- profile C (three named right lines each repeated twice): 3! T_C(F_R) ordered assignments among (V)_3;
- strict D6 (original right A, connected column-dual physically aligned to left): 12 C6(F_R) ordered assignments among (V)_6. Dihedral automorphisms of the left connected sixcycle number 12, and unaligned A/A is rejected.

Thus define exact probabilities P_A=6! T_A(F_R)/(V)_6, P_B=4! T_B(F_R)/(V)_5, P_C=3! T_C(F_R)/(V)_3, and P_D6=12 C6(F_R)/(V)_6.

For a FIXED complete original global left f, define H_{tag,r}(f) to count DISTINCT ORIGINAL six-incidence sets satisfying the LEFT physical degree2 projection, the static ORIGINAL left/right multiplicity profile conditions for the named accepted tag, and (D6 only) a connected left column-position dual. Distinct original right source lines may be repeated in B/C profiles, but each ORIGINAL incidence ID is counted once and all repeated original objects have the same actual physical labels. These static counts depend only on the ORIGINAL true GQ and f, not on g.

For the seven tags, the exact all-h identity is

    E_{ONE uniform complete global g} S_seven(f,g)
      = sum_{tag,r} H_{tag,r}(f) *
              (P_D6 if tag=D6 else P_r).

Likewise for the accepted **NECESSARY** GF5 seven-family risk numerator:

    E_g Q7(f,g)
      = sum_{tag,r} R3_CERTIFIED_FLOORS[tag] * H_{tag,r}(f) *
              (P_D6 if tag=D6 else P_r).

Q7/51^6 is a certified lower contribution to R3, **not the full R3**. These are **EXACT expectations** for every s=2^h and every legally occupied physical F_R, not independent motif-by-motif random experiments. There may be strong correlation between motifs sharing original right lines: none is discarded because only linearity of expectation is used.

For full K6, V=15, the four exact probabilities are:

    P_A  = 70/5005,
    P_B  = 3/1001,
    P_C  = 3/91,
    P_D6 = 1/5005.

The finite W32 original source contains exactly 62,370 distinct left sixsets, of which 52,309 satisfy one of the static seven-family source schemas before choosing g, compressed to 36,272 positive integer weighted original right source records (as independently certified in C22). Exact rational arithmetic in the C23 source evaluates the entire expected seven-vector for this original GQ f, and requires that it dominate the previously accepted C21 C5+B/A + D6 restricted lower. The result is not a fixed-g minimum.

## 4. Exact ALL-h global-right two-line transposition sensitivity

The key new count concerns the exact physical 130 template family. Fix one physical pair e on a six-coordinate set. Among all 130 factors:

    e occurs ONCE in 40 patterns = 28 simple A + 12 square-edge B;
    e occurs TWICE in 6 patterns = 3 doubled-edge B + 3 doubled matching C.

These values are per fixed physical edge of K_a **and per six-coordinate set containing its endpoints**; there are binom(a-2,4) such six-coordinate sets. Thus for one fixed ORIGINAL GQ incidence edge (p,line) with left physical pair e=f(p), each candidate J containing it is of one of two types:

- e used once. At most 40 binom(a-2,4) physical multigraph templates include e once, with at most Delta^5 choices of ORIGINAL right incidences for the other five source column slots;
- e used twice. At most 6 binom(a-2,4) physical patterns use e twice. The second incidence at ORIGINAL point p must differ from (p,line), so there are at most Delta-1 possibilities, with <=Delta^4 ways to fill the other four original incidence columns (including C repeated-point choices).

Therefore one fixed ORIGINAL incidence edge belongs to at most

    binom(a-2,4) [40 Delta^5 + 6(Delta-1)Delta^4]

distinct ORIGINAL left physical 2factor sixsets. One ORIGINAL right GQ line has exactly Delta distinct point incidences. Transposing the physical right labels of two ORIGINAL GQ lines under ONE globally compatible full g cannot change any accepted tag on a sixset avoiding those two lines. Union bound over all touched original incidences gives for every full legal f,g and every transposition:

    |S_seven(f,g') - S_seven(f,g)|
       <= 2 binom(a-2,4) (46 Delta^6 - 6 Delta^5)
       = O(s^12).

This can also be capped by the exact all-h complete physical left source upper

    U_left=binom(a,6)[70 Delta^6
                     +45 binom(Delta,2) Delta^4
                     +15 binom(Delta,2)^3].

For s=2, a=6, Delta=3, **U_left=62,370**, agreeing with the exact ORIGINAL W32 left source. The upper bound on |Q7(f,g')-Q7(f,g)| is the same affected original sixset bound multiplied by max(R3_CERTIFIED_FLOORS)=51,750, because each old and new class contribution is between 0 and that maximum. This bounds change in a necessary R3 **numerator** and does NOT imply a corresponding bound on total GF5 R3.

This O(s^12) influence upper is too large to transfer a positive mean Omega(s^6) into an all-g positive Omega(s^6): traversing arbitrary permutations by many swaps is uncontrolled. It is a rigorous upper sensitivity result, not an adversarial positive minimum.

## 5. Code, falsifiers, and CI

- research/hyp105_g5e2b3e1c23_seven_moment_influence.py
- research/test_hyp105_g5e2b3e1c23_seven_moment_influence.py
- .github/workflows/hyp105-c23-contract.yml

Independent oracles exhaust ALL physical 6-edge K6 multisets with repeated physical pair labels (not just 70 simple graphs), verify 70/45/15 counts and 40/6 incidence values from different generation strategies; test the all-h sensitivity formula over s=2,4,8,...,128 with invalid cases fail-closed; verify exact full/partly missing physical K6 target pattern counts; independently enumerate all ordered injections of 3 named ORIGINAL right line IDs into 15 physical pairs for P_C=3/91; verify complete real W32 original source static H_{tag,r} counts and exact rational entire seven class mean + GF5 numerator, plus the previously verified C21 lower. Full Research CI preserves every command from 123-command C22 six-hosted-shard suite and adds two explicit C23 checks; dedicated Contract, Research, INDEX required on final exact HEAD.

**Research gate #230 remains OPEN_WITH_FORMAL_BLOCKER.** No universal adversarial min or infinite all-h small-S correlated construction is claimed. Next C24 should combine more than first moments and bounded one-line influence, or rigorously falsify such proposed upgrades using complete global f,g.
