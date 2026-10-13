# HYP-105 / issue #230 — D6-M: exact ORIGINAL GQ collinearity C/A transfer

**2026-10-13. RESTRICTED_THEOREM_C (genuinely GQ/GF5 positive, RIGHT-RANDOM ONLY). Branch A/B remain OPEN.** Base: fully GitHub-hosted green [D6-L Draft #411](https://github.com/definitely-stable/Mathlab/pull/411), parent HEAD 511b851048afc16f89d01647026205cda341e829. Main unchanged. No new generic Hall flow.

## 1. The EXACT right-line distinctness combinatorics

Work in ORIGINAL W(3,s), s=2^h, with V=(s+1)(s²+1) points and lines, every point on d=s+1 distinct original lines. The original point/line incidence graph has girth eight. Fix a complete *globally injective* original point map f into unordered K_a physical pair labels, where a is the minimal symbol alphabet with K=binom(a,2)>=V. A left physical C-template is EXACTLY a triple of distinct original points p1,p2,p3 whose coordinate-pair images f(p_i) are pairwise disjoint; selecting two distinct true incidence-lines at each creates a six-incidence set whose left half has type C (physical three doubled edges of a perfect matching).

Let B=binom(d,2), A=d-1 and Z=binom(d-1,2). For each triple independently choose an unordered 2-subset of its d ORIGINAL incident lines. Let Phi_d count choices such that the six resulting ORIGINAL right factor lines are all distinct.

**Exact four-type theorem, for every s, every original triple:**

| Induced ORIGINAL point collinearity pattern | Phi_d |
| --- | --- |
| No collinear pairs | B³ |
| One collinear pair | B³-A²B |
| Two collinear pairs (a length-two path on three points, distinct ORIGINAL common lines) | B³-2A²B+A² |
| Three collinear pairs (ALL three points on ONE original line) | Z³+3AZ² |

**Proof:** Partial linearity ensures two original points share at most one line. For one collinear pair, both independently choosing their sole shared line has exactly A²B realizations. For two collinear pairs there are two excluded events; their intersection requires the middle point to choose both distinct common lines (one possibility), and each remaining endpoint to include its one shared line (A possibilities): intersection A². For three collinear pairs, the ORIGINAL GQ triangle axiom forces the three points onto one and the same true line. To avoid any repeated right line, at most one of the three point choices may include that line. There are Z³ choices with none and 3AZ² with exactly one. Nonconcurrent collinear triangles are rejected, not treated as valid GQ types.

Since d>=3, Z³+3AZ² is at most each other expression (integer arithmetic). This is a NEW exact GQ three-point lift formula. In particular, the line-availability correction is a genuine original GQ property: no fake GQ diagonal, physical-label orbit symmetry, BB-only positive subset or inferred independence appears.

## 2. Exact all-h C/A expectation for EVERY fixed left f

Let M_f be the family of unordered triples {p1,p2,p3} of ORIGINAL points with pairwise disjoint physical f(p_i). Let K=binom(a,2) and

    p_A = 6!*70*binom(a,6) / (K)_6.

The numerator counts all assignments of six DISTINCT physical unordered pairs that form one of the 70 labelled simple physical six-edge 2-factors on six physical symbols. The denominator counts ordered distinct physical-pair images of six distinct right factor lines. For a UNIFORMLY RANDOM INJECTION g of all ORIGINAL right lines into K physical pair labels, any six distinct fixed right lines map to an ordered distinct physical six-tuple uniformly, independent of which six right lines were chosen.

The **directional subclass C-left/A-right** of the accepted ORIGINAL positive GF5 class C/A is characterized by exactly this left physical C and right physical A (all six distinct right factor lines). The existing seven-class classifier aggregates BOTH orientations, C-left/A-right AND A-left/C-right, into the single tag "C/A". Our equality is for the DIRECTIONAL subclass only, hence supplies a lower bound — NOT an exact expectation — for the aggregate tag. Every directional original six-incidence set is counted EXACTLY ONCE (one original doubled left point triple and one unordered pair of distinct original lines per point). Therefore **for every s=2^h and every fixed globally injective left f**,

    E_g[U_C-left/A-right(f,g) | f]
      = p_A * sum_{T in M_f} Phi_d(T).                         (1)

This is an EXACT rational formula, not a random experiment or finite-h asymptotic extrapolation. The GF5 coefficient of each accepted C/A sixset in the seven-class R3 lower numerator is 43320 (accepted prior seven-GF5 certificate). Hence the expected **nonnegative selected seven-class GF5 lower numerator** includes at least 43320 times expression (1). No full R3 upper claim follows.

## 3. A uniform all-f expected-positive lower, strengthened by GQ pair geometry

The existing proven one-sided E1-B1A physical C template lower is

    M_f >= M_C^lower = 15*binom(a,6)-missing*(3*15*binom(a,6)/binom(a,2)),

using EXACT integer per-omitted-edge edge-transitivity and missing=K-V<a; the source library supplies the integer expression and checks divisibility. Regardless of f, from the four types above

    E_g U_C-left/A-right >= p_A * M_C^lower * Phi_min,
    Phi_min=Z³+3AZ².

A stronger ALL-f bound comes from ORIGINAL W(3,s) point collinearity. There are exactly

    P_coll = V*s*(s+1)/2

unordered collinear ORIGINAL point pairs. For any pair at most V-2 third points can complete a triple with disjoint physical f-labels, regardless of the fixed injection. The *union bound over repeated chosen ORIGINAL lines* loses at most A² B for each collinear pair within an accepted left C triple. Consequently

    sum_(T in M_f) Phi_d(T)
       >= [M_C^lower * B³ - A²*B*P_coll*(V-2)]_+.

Both bounds hold simultaneously; take their MAXIMUM. They are integer-only symbolic for all h. As s grows, a~sqrt(2)*s^(3/2), B~s²/2, p_A~560*s^-9, M_C^lower~s^9/6; their product yields

    E_g U_C-left/A-right(f,g) >= (35/3-o(1))*s^6                 (2)

UNIFORMLY IN THE FIXED LEFT f. The refined pair penalty is asymptotically O(s^12) versus the principal C-lift term Theta(s^15), a relative O(s^-3), whereas the universal Phi_min alone loses relative O(s^-2).

### Disjoint B/A + C/A transfer on the SAME random right g

Previously proved E1-B1A:

    E_g U_B-left/A-right(f,g) >= (140-o(1))*s^6.

B/A and C/A count **disjoint ORIGINAL sixsets** because a left half cannot be simultaneously physical type B and type C. They involve the very SAME g, so linearity of expectation gives the strengthened original seven-positive S lower **in the RIGHT-RANDOM model**:

    E_g[S_seven(f,g) | f] >= E_g[U_B-left/A-right+U_C-left/A-right | f]
                         >= (455/3-o(1))*s^6.         (3)

The exact finite rational lower equals the sum of the previous original B/A lower and the new exact directed C-left/A-right lower, in the executable report. This uniform-in-left-f result is NEW but **NOT** a lower bound for an arbitrary fixed adversarial right injection g. A positive expectation proves some right g have high S; it does NOT prove all right g do, and does not close universal Branch A. Nor does it establish a counterfamily for Branch B or strict full GF5 R3/R2 upper bounds.

**Critical dual-orientation audit:** The existing fixed-g W32 classifier reports the union of left-C/right-A and left-A/right-C. The independent finite falsifier counts both separately and checks that they sum to the classifier's "C/A" tag. For lex the directed C-left/A-right count is 4 and the reversed A-left/C-right count is 9 (aggregate 13); for reverse they are 0 and 1 (aggregate 1). Hence it is mathematically invalid to equate the new right-random directional expectation with the aggregate C/A expectation. The all-seven S inequality is nevertheless valid because this directed subset is contained in its accepted positive GF5 class.

## 4. Independent original finite evidence

The original genuine W(3,2) lex/reverse/S68/S72 and original W(3,4) lex/random global injective pair maps are evaluated by scanning triples of ORIGINAL factor points with pairwise disjoint physical labels, classifying their true ORIGINAL point collinearity from independently checked GQ incidence sets. In every case the four Phi types are added with integer weights to obtain the EXACT conditional expectation (1) on all uniformly random right injections without enumerating any g. At W32, an INDEPENDENT scan of every actual original left C sixset and its six distinct right line endpoints must reproduce the weighted Phi count, and a separate full seven-positive ORIGINAL same-map GF5 classifier must reproduce the observed fixed-right-g C/A count.

At W34 the code evaluates *only* the actual ORIGINAL geometric left-triple profile and its expectation over a FUTURE UNIFORM right injection. It does **NOT** claim to enumerate the unknown COMPLETE original seven-positive W34 family, does NOT reuse BB-only as full S, and does NOT interpret a random-right expectation as an observed actual S on a given W34 map. A separate enumeration of the three ORIGINAL two-line choices for 4 representative geometric orbit types on W32/W34 is required to independently validate each Phi formula, with a fake nonconcurrent triangle rejected.

### Confirmed true-original finite expectations vs FIXED right injections

[Hosted D6-M Contract #38372684216](https://github.com/definitely-stable/Mathlab/actions/runs/38372684216) SUCCESS, including independent four-orbit true GQ original-line-pair enumeration (W32 and W34), 70 physical right six-edge simple 2-factors of K6, all 405 left-C ORIGINAL W32 subsets, and actual full seven-positive GF5 W32 aggregate C/A counts.

| True original GQ and left f | Left physical C-template triples | Left-C lifts with six DISTINCT ORIGINAL right lines | EXACT E_g[C-left/A-right | f] | ACTUAL fixed-g C-left/A-right |
| --- | ---: | ---: | --- | ---: |
| W32 lex | 15 | 209 | 38/13 | **4** |
| W32 reverse | 15 | 209 | 38/13 | **0** |
| W32 S68 | 15 | 297 | 54/13 | **0** |
| W32 S72 | 15 | 297 | 54/13 | **2** |
| W34 lex | 36,270 | 32,283,840 | 1,129,934,400/110,983 | Not computed |
| W34 random | 36,624 | 32,560,144 | 1,139,605,040/110,983 | Not computed |

These are **exact conditional expectations**, not observed full seven-positive S for the six right mappings. Genuine W34 enumerates only original GQ collinearity types; it does not count a fabricated full seven-positive GF5 S.

**Actual fixed-right obstruction to promoting an expectation to a deterministic bound:** The original W32 lex and reverse models have EXACTLY the SAME globally injective left f. With this fixed f, the directional C-left/A-right expected count is 38/13 for a uniformly random right g, yet their ACTUAL right pair injections yield respectively **4** and **0** such directional accepted sixsets. Their aggregate C/A observed counts, counting both directions, are 13 and 1. The independent original W32 S68 case ALSO has zero fixed-right directed C-left/A-right, despite exact expected count 54/13; S72 has 2 against the same expectation 54/13. This is a rigorous finite falsifier of the invalid assertion that a positive conditional mean forces a positive directional C-left/A-right count for every fixed right g. It is **NOT** an infinite Branch B counterfamily and the actual full seven S of reverse remains nonzero.

## 5. Scope and next mathematical gate

- [Code](../../research/hyp105_issue230_d6m_gq_collinearity_ca_transfer.py): exact four-orbit symbolic polynomial, independently true-original GQ collinearity profiles, all-h universal template bound, p_A as Python Fraction, additive proven B/A+new C/A random-right expectation.
- [Falsifiers](../../research/test_hyp105_issue230_d6m_gq_collinearity_ca_transfer.py): direct independent original line-pair enumeration for all four GQ triple motifs at h=1,2; 5005 physical right K6 six-edge subsets proving 70 physical simple two-factors; independent 405 original W32 left C sixset scan and separate GF5 seven-class classifier; genuine W34 geometry/left-injection controls; invalid non-GQ triangle rejection.
- [GitHub-hosted workflow](../../.github/workflows/hyp105-issue230-d6m-gq-collinearity-ca-transfer.yml): exact full original W32 expected vs observed separation, exact W34 right-random-only output, hard reject all-g Branch A claim; Proof Audit, INDEX, full Research separately.

**D6-N suggested next:** examine the centered *correlation* between left C (or B) physical 2-factor tests and right A completion under arbitrary globally injective right maps, on true ORIGINAL GQ incidence tensors. A second-moment bound over random right g or a conditional sampler is NOT automatically a fixed-g theorem; the rigorous goal remains a deterministic lower bound for all correlated f,g or an infinite constructive Branch B adversary. No additional generic Hall-network formulation is needed. All research PRs Draft, no merge/main mutation, #230/#176/#169 remain OPEN.
