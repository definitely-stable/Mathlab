# HYP-105 / issue #230 — D6-S: exact ordered three-cycle commutator and full W32 three-factor-support gate

**2026-10-13. RESTRICTED_THEOREM_C / root Branch A,B OPEN.** New Draft child of four-hosted-green D6-R [PR #417](https://github.com/definitely-stable/Mathlab/pull/417), parent pinned HEAD `fa81256cb105b1af8c16fe43297eb65ced15d0c6`. Keep `main` unchanged and root #230/#176/#169 OPEN. Do not interpret finite checks or CI as external mathematical peer review.

## 1. Why noncommuting original-right permutations are genuinely different

D6-P recorded the ALL-SEVEN GF5-positive original six-incidence classes as a sum of position-aware cylinders and proved an exact fixed-g right single-transposition boundary. D6-R proved an intersection-of-cylinder-shadows Hessian for TWO **DISJOINT** original right-line transpositions (four distinct moved lines). In real W(3,2) this revealed S68/S72 strict one-swap minima and negative two-swap interactions without escaping them in an explicitly restricted top-12 pairing sample.

Two transpositions sharing ONE original line factor instead compose into a **3-cycle**. They do NOT commute. Extending D6-R's doubly touched intersection formula to these compositions is mathematically false. D6-S isolates the correct signed order defect and evaluates *all* 3-factor-supported right label permutations of two real W(3,2) configurations, with explicit finite scope.

## 2. ALL-h arbitrary right-permutation cylinder boundary theorem

Fix true ORIGINAL W(3,s), s=2^h, h>=1, its distinct ORIGINAL factor incidence sixsets, arbitrary complete globally injective physical-pair maps f,g of its ORIGINAL point and right-line factors, and the D6-P cylinders c with exact original incidence multiplicities m_f(c), right ORIGINAL line sets R(c) (repetitions retained in the actual signature) and all-seven positive GF5 classifier chi_c(g).

For any **permutation pi of original right factor identities supported on T**, let g^pi mean the complete right injection obtained by PERMUTING the existing physical pair labels assigned to those original lines, leaving all other original line labels untouched. Each cylinder c with R(c) disjoint from T reads the same right physical pair images before and after pi, and hence its positive class remains identical. Therefore, without probabilistic assumptions,

    Δ_pi S_seven(f,g)
      = Σ_{c:R(c)∩T≠∅} m_f(c)
           (1[chi_c(g^pi) accepted]−1[chi_c(g) accepted]).

The same holds separately for each of the seven accepted GF5 sectors, and for the **previously certified selected necessary GF5 R3 lower numerator** with class coefficients 5643, 45600 twice, 43320, 49050, 51750, 45010. This is a precise model-equivalent identity, NOT an all-g lower bound.

For the special directed left-B/right-A and left-C/right-A classes with SIX DISTINCT original right lines, if *all* moved original right line identities are already among the six chosen, their g-images are merely permuted and the unordered six physical right edges are unchanged. The right A indicator is invariant. This sharpening is NOT valid for aligned D6, where moving original right physical edges between immutable incidence positions can alter the six-column-dual C6 matching.

## 3. NEW exact order-sensitive curvature, commutator and overlap-tail theorem

Take three different ORIGINAL right factor IDs u<v<w and name two overlapping transpositions

    sigma=(u,v), tau=(v,w).

**Order convention:**

- `g^(sigma then tau)`: swap physical labels at u,v, THEN swap the current labels at v,w. The resulting simultaneous 3-cycle is `g_plus`: u takes old g(v), v takes old g(w), w takes old g(u).
- `g^(tau then sigma)`: swap v,w, THEN swap u,v. The resulting inverse 3-cycle is `g_minus`: u takes old g(w), v takes old g(u), w takes old g(v).

The two assignments are different. Both are legal complete globally injective original right maps and preserve the fixed occupied PHYSICAL right image set E.

Define two **ordered mixed discrete second differences**:

    H_{sigma->tau}(g)
       = S(g_plus)−S(g^sigma)−S(g^tau)+S(g),
    H_{tau->sigma}(g)
       = S(g_minus)−S(g^tau)−S(g^sigma)+S(g).

Let I_sigma and I_tau denote the original-cylinder sets that touch at least one original line ID moved by the named transposition. For a cylinder c DISJOINT from I_tau, the second (last) tau move cannot change any of its ORIGINAL right factor images between g^sigma and g_plus; also g^tau and g agree there. Hence its contribution to H_{sigma->tau} vanishes. There is **no analogous requirement that c belong to I_sigma**: sigma may move the physical label that tau subsequently transfers into a third original factor, even when c did not use sigma's original factor identities at the baseline. Thus the correct support and decomposition are

    H_{sigma->tau}
      = Σ_{c∈I_tau∩I_sigma} m_f(c) h_c^plus
        + Σ_{c∈I_tau\I_sigma} m_f(c)
              [a_c(g_plus)−a_c(g^tau)].

The second sum is the **noncommuting order-overlap tail** absent in the disjoint-swap case. Reversing the move order gives the symmetric identity with support I_sigma and the tail I_sigma\I_tau. Both formulas hold **for each seven-class indicator separately** and for the selected GF5 numerator.

Subtracting the two ordered Hessians exactly cancels the two singleton terms:

    H_{sigma->tau}−H_{tau->sigma}
       = S(g_plus)−S(g_minus) =: C_{sigma,tau}(g).

The order commutator defect C is supported on the ORIGINAL cylinder union I_sigma∪I_tau, equivalently those c with R(c) intersecting T={u,v,w}. Since both a_c(g_plus) and a_c(g_minus) lie in {0,1},

    |C_{sigma,tau} S(g)| ≤ M_T(f),

where M_T(f) is the integer number of genuinely distinct ORIGINAL six-incidence candidates (counted by cylinder multiplicity) meeting T. For the certified **selected** positive GF5 necessary R3 numerator,

    |C_{sigma,tau} Y(g)| ≤ 51750 M_T(f).

These are exact deterministic all-finite-h **support bounds** and a new order-aware model obstruction. They do not imply that S(g)≥c s^6 for every g.

**Explicit independent synthetic falsifier against overgeneralization:** construct a single B-left/A-right incidence cylinder using original right factors 2,3,4,5,6,7. Let sigma=(0,1) and tau=(1,2); this cylinder misses *both* original IDs touched by sigma, so `I_sigma∩I_tau` is EMPTY. Choose a fully injective physical right map on eight original lines so that the six right physical edges form an A-C6 only when the label at original right factor 2 is replaced with old g(0), and not when it receives old g(1). Then H_{sigma->tau}=+1 despite the empty double-shadow, and its GF5 floor Hessian is +45600. This is an exact proof-scope counterexample to importing D6-R's disjoint formula. It is **not** claimed to be a full true GQ W32 original incidence host or a root Branch B counterexample.

## 4. FULL finite W32 three-factor-supported permutation gate (not just sampled swaps)

W(3,2) has exactly 15 ORIGINAL right line factors, labelled by globally injective physical pair edges of K6. The number of **different 3-factor support sets** is `binom(15,3)=455`. Each supports exactly two nonidentity oriented 3-cycles. Thus **910 exact three-cycles per fixed map** and 1820 across the two previously accepted true-original W32 one-swap strict minima S68 and S72.

The algorithm compiles the exact D6-P original-position cylinders ONCE per frozen map, verifies all seven baseline GF5 counts against the existing **independent original-incidence full seven_census**, precomputes their baseline class tags, and evaluates each of the two oriented complete-global-right-injection three-cycles **only on the union of original-cylinder supports meeting the three moved factor IDs**. The two orientations are deliberately evaluated separately because S need not be conjugate-symmetric under a fixed correlated f,g.

Every nonidentity permutation supported on **AT MOST three** ORIGINAL right line factors is EITHER one of the 105 original-right transpositions (covered and rigorously pinned in D6-P) OR one of the 910 oriented 3-cycles (exhaustively evaluated in this slice). Therefore, combining D6-P singleton data with these 910 oriented 3-cycle deltas gives a logically complete finite certificate for local stability **against ALL right label permutations supported on at most three ORIGINAL line factors** for a specific fixed f,g. It is NOT a global right-label optimum over S15, since arbitrary right permutations may move four or more original factor identities, and f itself is held fixed. It proves nothing asymptotic for all h by itself.

The finite scan reports, for S68 and S72 separately, how many 3-cycles decrease, preserve, or increase the seven-GF5-positive count S, how many reduce the certified selected GF5 floor numerator, how many original triple supports have a NONZERO commutator between the two orientations, and the best/worst exact oriented 3-cycle and its all-seven class vector. All numerical results must come from actual GitHub-hosted execution before being pinned in tests; no guessed search outcomes.

The dedicated CI uses **parallel GitHub-hosted jobs** for the two frozen maps after a once-per-PR independent full-original seven-census test job. Each finite exhaustive job evaluates exactly one map's 910 cycles, with a hard runtime limit. This respects the constraint of GitHub-hosted only; it avoids duplicating the entire two-map enumeration inside the unit-test phase.

## 4a. Exact hosted original W32 exhaustive result: S72 escapes; S68 resists ALL <=3-factor right permutations

Initial specialized hosted [run #38395675172](https://github.com/definitely-stable/Mathlab/actions/runs/38395675172) returned SUCCESS on implementation HEAD `4d61bbccb825a2d354984c770a6a07be7f3a6211`. Its six independent ORIGINAL seven-GF5 classifier tests all passed. Separately on two GitHub-hosted matrix jobs, ALL 455 ORIGINAL right factor triples and BOTH orientations were checked per map (910 complete globally injective three-cycles per map, 1820 total), with the D6-P 105 exact right transpositions independently rechecked in the same job. The following exact data are now frozen as fail-closed regression assertions on the later PR HEAD.

| Exact result (true original W32) | S68 | S72 |
| --- | ---: | ---: |
| Baseline positive seven-S | 68 | 72 |
| Strictly worsening singleton transpositions | 105 of 105 | 105 of 105 |
| Oriented three-cycles tested | 910 of 910 | 910 of 910 |
| Decreasing S three-cycles | **0** | **1** |
| Equal-S three-cycles | 0 | 0 |
| Increasing S three-cycles | 910 | 909 |
| Three-cycles decreasing selected necessary GF5 numerator | **0** | **1** |
| Three-original-line supports with a NONZERO order commutator | 445 of 455 | 449 of 455 |
| Minimum observed oriented three-cycle ΔS | **+8** | **−4** |
| Maximum observed oriented three-cycle ΔS | +108 | +101 |
| Best oriented original right triple | (3,11,12), forward | **(1,7,9), reverse** |
| Exact Δ GF5 necessary floor numerator at best ΔS | +317513 | **−179530** |
| Order commutator ΔS between orientations at best triple | −32 | +46 |

**New genuine ORIGINAL finite falsifier.** For the frozen S72 scheme, rotate physical right pair labels on ORIGINAL line identities (1,7,9) in the **reverse orientation**: u receives old g(w), v receives old g(u), w receives old g(v). This preserves the entire same original symplectic GQ, the SAME fixed left map f, right global injectivity, and exactly the same physical right IMAGE. The count changes **S:72→68**. Full source ORIGINAL `seven_census` independently confirms the following **all-seven class count deltas** (new minus original):

    D6                       0
    B-left/A-right          +7
    A-left/B-right          -9
    C/A                     -1
    C/B                      0
    B/B-overlap              0
    B/B-disjoint            -1
    TOTAL S                 -4
    certified GF5 lower numerator delta = -179530

The one-swap strict local minimum S72 is therefore **NOT** a strict minimum once 3-factor-supported moves are admitted. D6-R's top-12-selected disjoint double-swap search did not include these overlapping 3-cycles, so there is no contradiction. This is a valid finite h=1 short witness; it does NOT construct an infinite Branch B family, and reaching the same count 68 does not establish equality of the resulting right map to the frozen S68 map.

**New stronger finite positive certificate for S68.** All 105 single swaps and all 910 oriented three-cycles strictly increase S68, and also do not decrease the selected certified GF5 necessary lower numerator. Every nonidentity permutation on a support of at most three ORIGINAL right factor lines is either a transposition or a 3-cycle. Therefore **S68 is a strict right-permutation local minimum against EVERY move supported on at most three original right factors** for its fixed original W32 left map. It is NOT proved a global minimum against permutations of FOUR or more right factors, not an optimal value over changing f, and absolutely not an all-h positive lower bound.

**Order matters empirically.** S68's two 3-cycle orientations have different S in 445/455 triple supports; for S72 this happens in 449/455 triple supports. This is direct finite evidence that oriented permutations cannot be collapsed to unordered three-factor supports or treated with D6-R's commuting Hessian. The synthetic noncommuting transfer-tail counterexample and independent source recount are retained as permanent regression controls.

## 5. Mathematical branch gate, limitations, acceptance

The D6-P strict one-swap local minima, D6-R targeted double-swap non-escapes, and D6-S exhaustive <=3-factor right permutation certificate are all **finite W32 facts**, not all-h uniform lower bounds. Even a strict W32 minimum against all three-line-supported right permutations is not necessarily globally optimal for 15 right lines. The substantive root alternative remains:

- Branch A: for ALL powers of two s, ALL complete globally injective correlated original maps f,g, establish `S_s(f,g)≥c s^6` for a universal positive c;
- Branch B: exhibit coherent explicit complete infinite original GQ labelings f_s,g_s with `S_s=o(s^6)`;
- or a carefully scoped Branch C conditional theorem whose missing global anti-avoidance gate and finite falsifiers are explicit.

Future work after D6-S should NOT continue mistaking small-support local optimality or positive right-orbit expectation for Branch A. A meaningful D6-T candidate would be a globally valid **primal-dual constraint/infeasibility certificate** for the original seven-cylinder system, or proof that no such local-only certificate can extend to all f,g. Such a certificate must account for all original incidence positions, all seven GF5 tags and both globally coherent factor maps, not just physical edge usage or one-/two-swap derivatives.

Require dedicated D6-S Contract, INDEX, Proof Audit, full Research GitHub-hosted checks on the EXACT FINAL PR HEAD, all SUCCESS, plus independent human mathematical review before any merger. Keep Draft, `main` unchanged, #230/#176/#169 OPEN; no new ASET exponent, no total GF5 R3 upper, no proved Branch A or B.
