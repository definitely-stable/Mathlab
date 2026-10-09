# HYP-105 G5-E2-B1 — Exact disjoint additive energy and GF5 3-vs-3 meet-in-middle oracle

2026-10-09. [HYP-105 G5-E2-B #169](https://github.com/definitely-stable/Mathlab/issues/169), [G5-E root #162](https://github.com/definitely-stable/Mathlab/issues/162), [#106](https://github.com/definitely-stable/Mathlab/issues/106), [#95](https://github.com/definitely-stable/Mathlab/issues/95). Predecessor [finite signed flow motifs E1](HYP-105-G5-E1-FLOW-MOTIFS-AND-NEXT-PROOF.md), [explicit all-h geometry mapping E2-A](HYP-105-G5-E2-A-PAIR-INJECTION-MODELS.md), and [exact GF5 boundary-flow E0](HYP-105-G5-E0-BOUNDARY-FLOWS.md).

**PROVED_CLASSICAL_INCLUSION_EXCLUSION / EXACT_GF5_ENERGY_ORACLE / E2-B_B1_ONLY / NO_UNIFORM_RISK_POWER / NO_NEW_ASET_EXPONENT / NO_ORIGINALITY_CLAIM.**

## 1. Audit: what E2-B must actually solve

The symplectic W(3,2^h) all-h graphs with N=Theta(m^(8/3)) and explicit pair-coordinate injections already exist (E2-A). E1 proves for each k=2,3 that the exact GF5 weighted trade risk R_k is a finite signed graph-type sum 51^(-2k) SUM_tau M_k(tau;B) F_tau(b;5). But currently no all-h upper on the multiplicities M_k for **positive** F_tau, so E2-B's claimed improved power remains completely open.

This slice supplies a mathematically independent way to compute exactly the SAME R_k through additive sum signatures, with precise correction for overlapping sets. This can independently validate motif counts and avoid explicit N-choose-4 flow calls. The identity is elementary Möbius inclusion-exclusion, and related additive energy and Sidon/B_h counting techniques have long classical prior art. DO NOT call the identity or its algorithm a globally new mathematical theorem. Genuine original work must yield an all-h risk or extremal bound stronger than Lefmann, not a change of computation basis.

## 2. All-N exact overlap-corrected k-sum energy theorem

Let B={S_1,...,S_N} be N **distinct four-coordinate supports** in [m]. At each support i, independently select one of the 51 GF5 all-nonzero coefficient quadruples with sum 4. Denote the resulting random vector X_i in GF5^m. For a k-element set T of column IDs, define the integer histogram

    H_T(z) = number of all 51^k weight assignments to T
             that give the exact GF5 vector sum z.

There is NO approximation, hash collision, or random independence between different T assumed. Histograms are exact mathematical functions of distinct finite supports.

For any index subset U of size r<=k define the incidence-sum

    B_U(z) = SUM_{T superset U, |T|=k} H_T(z).

For the empty subset U, B_empty(z)=SUM_{|T|=k}H_T(z). Our true probability risk is

    R_k(B) =
      SUM over unordered disjoint k-subset pairs {T,T'} of
      SUM_z H_T(z) H_T'(z) / 51^(2k).

**Theorem E2-B1 (exact disjoint-energy Möbius formula; ALL m,N; classical inclusion-exclusion).** For k=2,3,

    R_k(B) = 1/(2*51^(2k)) *
             SUM_z SUM_{r=0}^k (-1)^r
                 SUM_{U subset [N], |U|=r} B_U(z)^2.

The sum is a nonnegative integer numerator divisible by 2, even though individual Möbius terms may have alternating signs. In particular,

    R_2 = [SUM_z ( B_empty(z)^2
             - SUM_i B_{i}(z)^2
             + SUM_{i<j} H_{ij}(z)^2 )] / (2*51^4),

    R_3 = [SUM_z ( B_empty(z)^2
             - SUM_i B_{i}(z)^2
             + SUM_{i<j} B_{ij}(z)^2
             - SUM_{i<j<l} H_{ijl}(z)^2 )] / (2*51^6).

**Proof.** Expand every square B_U(z)^2 into ordered pairs of k-subsets (T,T'), each weighted H_T(z)H_T'(z) and included iff U⊆T∩T'. A pair with |T∩T'|=r appears with coefficient SUM_{j=0}^r (-1)^j binom(r,j) = (1-1)^r. This equals 1 if T and T' are disjoint and equals 0 otherwise. Thus the signed squared histogram sum counts precisely all ORDERED disjoint k-subset pairs weighted by equal exact vector sums. Each unordered pair occurs in both orders, so divide by 2. Independence of the independently sampled per-column weights for DISJOINT T,T' implies the product H_T H_T' / 51^(2k) is precisely the underlying random trade probability, as desired. QED.

**Key subtlety:** if T and T' overlap, their *actual random sums* are dependent because they share sampled vectors. The proof does NOT compute their true joint probability and does NOT assume their independence: all intersecting index-set pairs are removed algebraically via Möbius inversion BEFORE evaluating risk. Simply squaring the aggregate sum histogram and claiming independence would be WRONG. This is the essential reason for the correction terms.

This theorem is valid for any finite abelian additive group and arbitrary finite independent per-column palettes, provided H_T uses the correct palette product; the GF5 denominator 51^(2k) is the special uniform 51-option case and may not be ported to nonuniform palettes without adjustment.

## 3. E2-B1-B: independent full GF5 event oracle via meet in the middle

For a SINGLE signed event with k positive columns P and k negative columns Q, the existing published prescribed-boundary flow identity gives its exact numerator F_G(b;5). Instead of enumerating all 51^(2k) joint weight assignments or a 2^(8k)-term boundary-flow inclusion-exclusion, form two finite histograms H_P,H_Q, each requiring at most 51^k combinations. Then

    F_G(b;5) = SUM_z H_P(z)*H_Q(z).

Proof: choose a coefficient assignment independently on P and on Q. Their signed GF5 vector sums cancel iff both exact unsigned k-sums equal the same z. Each contributing pair of assignments is counted exactly once in the displayed product. E0 established the bijection to nowhere-zero prescribed-boundary flow assignments, so the result equals F_G(b;5). QED.

For k=3, this evaluates two histograms with exactly 51³=132,651 weighted assignments on each side, instead of testing 51^6 assignments; it uses EXACT GF5 vectors and finite deterministic hashing of complete byte signatures, not approximate hash fingerprints. It is a bounded finite proof tool and does not improve the asymptotic exponent of R3(B) as B grows because the number of six-column events is O(N^6).

## 4. Algorithmic scope and executable independent falsification

[Proof checker](../../research/hyp105_g5e2b1_energy.py) provides:
- exact true GF5 coordinate vector addition with per-position mod5, including source validation of 4 distinct support coords and all-nonzero checksum4 palette;
- bounded local histogram H_T(z) without generating 51^(2k) configurations;
- generic Möbius disjoint-pair numerator for k=2 or k=3, matching the all-m mathematical theorem;
- exact *finite* R2 computation from ALL pair histograms H_{ij} with work scaling like O(binomial(N,2)*51²*m) to generate the local signatures, **not** O(binomial(N,4)*51^4) separate flow calculations; score aggregation and memory depend on the distinct signatures and their overlap-incidence data;
- a tiny-N k3 energy verifier with explicit total combinations budget and custom admissible subpalettes;
- the fully admissible **51-pattern** exact k3 signed-event meet-in-middle oracle with a 51^3-side budget.

[Independent regression](../../research/test_hyp105_g5e2b1_energy.py) checks:
1. Two synthetic overlapping-index distributions against a completely independent direct enumeration of all unordered disjoint k-set pairs, for k=2 and k=3, including nonuniform multiplicities and identical signatures.
2. Select a REAL W(3,2) all-one four-column signed 2-vs-2 collision via the preexisting independent physical GF5 sum oracle. Compute the *whole* true R2 on those four real supports via energy and compare exactly with the three possible pair-of-pairs events evaluated by BOTH the previously accepted Fu–Ren–Wang flow inclusion-exclusion oracle (2^16 capped) and the newly independent GF5 meet-in-middle oracle. All numbers are exact rational Fractions; the unit coefficient witness gives a strictly positive lower bound >=1/51^4.
3. Select a REAL W(3,2) six-column 3-vs-3 unit witness; compute R3 on that 6-column actual support family with a reduced TWO-pattern nonzero/checksum4 palette. Independently enumerate **every** unordered 3-vs-3 partition and **every** 2^6 coefficient assignment, and compare exact rational risks to the k3 Möbius identity.
4. For the SAME real signed 3-vs-3 W(3,2) event, use ALL 51 checksum4 nonzero coefficient patterns and compute the exact signed flow probability by 51^3-side meet-in-middle; compare sign-swapped orientation and pin positivity from the all-one assignment.
5. Malformed supports, invalid or duplicate coefficient patterns, unbalanced signs, excessive dimension and resource budget tests MUST fail.

**Safety:** the exact finite full R2 implementation is capped by TOTAL pair-local coefficient choices, initially 160,000. The full 51^3 k3 oracle is for ONE signed event. Never call a direct full R3 oracle on W(3,4) N=425: C(425,3)*51³ is too large and cannot prove any all-h exponent.

## 5. Next theorem work: E2-B2 / E2-B3

**B2 — actual all-h positive flow motif counts.** Now two independent expressions must match for every finite B:

    R_k(B) = 51^(-2k) SUM_tau M_k(tau;B) F_tau(b;5)
           = GF5 overlap-corrected exact weighted additive k-energy.

This is a powerful **audit equality**, not an all-h asymptotic power theorem. To claim one, derive a new uniform-in-s upper bound on M_k(tau;B_s) of every positive motif class for a specifically defined pair-label scheme. Alternatively upper-bound the overlap-corrected energies directly using field structure, without assuming hypothetical action of symplectic automorphisms on the coordinate pair palette. The existing lex and coordinate-flag controls do not preserve arbitrary Sp(4,s) actions on support labels.

**B3 — compare and challenge graph-only first moment.** E1 proves the averaged independent-uniform-label risk R3=Omega(m^4), so simply averaging the first-moment certificate over such labels cannot surpass m^(12/5). A better proof needs **special** deterministic correlated labelings, an actual new energy bound, or a stronger hypergraph independence theory with proved codegree assumptions. An isolated finite sample cannot defeat an averaged asymptotic obstruction.

**Sufficient GO condition:** with N=Theta(m^(8/3)), prove for all h an upper R2=O(m^b4), b4<52/15, and an upper R3=O(m^b6), b6<4, or stronger certified extraction. No such bounds are established by B1. A new exponent or a Rust crate is NOT authorized.

Sources: Fu–Ren–Wang 2025, DOI 10.1016/j.aam.2025.102901, already gives general b-compatible nowhere-zero flows; Naor–Verstraëte 2008 DOI 10.1007/s00493-008-2195-2 supplies current ASET upper; Lefmann 2005 lower. Inclusion-exclusion and additive energy have longstanding combinatorial prior art. No priority attribution to Mathlab for these classical principles. Related recent generic B_h work (O'Bryant, EJC 2025, DOI 10.37236/12977; Marques, Canadian Mathematical Bulletin 2026) addresses different models, not an automatically applicable GF5 four-sparse bound.

**Acceptance:** full proof and quantifier audit, direct physical GF5 brute checks and exact known flow agreement, resource caps, GitHub-hosted exact-PR-head Research SUCCESS. Keep #169/#162/#106/#95 OPEN until a genuinely new asymptotic theorem is proved.
