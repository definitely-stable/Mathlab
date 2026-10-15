# HYP-105 / #230 — D6-AA4-R: original-GQ validation and two-type global mixed-swap certificate

**Research-only, stacked Draft on D6-AA4-Q / PR #476, exact base a51ce5aeb7883dcd029b9275ce44eaca9a60370f.** This establishes an all-h exact *support identity*, a rigorous elementary upper certificate for the support of nonlinear point/line interactions, and genuine W(3,2) adversarial test infrastructure for the entire seven-GF5 positive count. It does **NOT** establish the universal infimum S=Omega(s^6), an infinite counterfamily, a positive GF5 R3 upper, or an ASET exponent. Main is untouched.

## 1. Audit: original GQ validation must reject girth-six impostors

The old D6-AA4-Q W(3,2) input validator checked 15+15 source factors, 45 distinct source flags, degree 3, a physical K6 full injection on each side, and no source C4 (no two points on two common lines). Those checks alone do **not** characterize an original generalized quadrangle: a regular partial linear incidence graph can contain source C6 without C4. Such a graph can have a C/C six-incidence source configuration, invalidating the crucial "C/C=0 for GQ" premise on fake test input. The AA4-Q statement for *actual* W(3,s) remains valid; the test-input gate needed strengthening.

The new strict W32 validator independently checks the full GQ unique-anchor axiom: for each original point p NOT on original line ell, exactly one original point q on ell is collinear with p. The check covers all 180 nonincident p/ell pairs. On a partial linear space this rules out a source C6. Thus the code fails closed before applying the seven-class acceptance structure.

Independent negative witness: points/lines indexed modulo 15, with line ell incident to points ell, ell+1, ell+3. This is regular degree three and avoids C4 because the six signed pairwise differences of {0,1,3} are distinct modulo 15. Nevertheless, the six incidences (0,0),(1,0),(1,1),(2,1),(2,14),(0,14) form a SOURCE six-cycle. The previous degree/no-C4 gate can admit this fake geometry; the new genuine GQ gate rejects it. This is a source-geometric counterexample to a **validator sufficiency premise**, not a counterexample to HYP-105 or any actual generalized quadrangle result.

## 2. All-h global two-type transposition locality theorem

Fix a true original W(3,s), s=2^h >=2, its actual incidence-ID set E, N=|E|=(s+1)^2(s^2+1), and two complete globally typed-injective physical pair maps f and g. Let sigma_(f,g)(Q) in {0,1} be the actual seven-GF5 acceptance indicator for an unordered SIX-element subset Q of E; zero is assigned to nonphysical or unaccepted Q. AA4-Q establishes

    S(f,g) = sum_{Q in binom(E,6)} sigma_(f,g)(Q)
           = |J|-|AA|+|D6|.

Let f^{uv} be the result of exchanging the COMPLETE physical edge labels of two distinct original source points u and v; similarly g^{wx} exchanges the full edge labels of two distinct original source lines w and x. Both operations preserve GLOBAL typed injection and reuse the same labels at every true original incidence bearing their source endpoint.

Define U={e in E: original point(e) in {u,v}}, V={e in E: original line(e) in {w,x}}.

Exact one-sided source support identities:

    S(f^{uv},g)-S(f,g)
      = sum_{Q: Q intersects U} [sigma_(f^{uv},g)(Q)-sigma_(f,g)(Q)].

    S(f,g^{wx})-S(f,g)
      = sum_{Q: Q intersects V} [sigma_(f,g^{wx})(Q)-sigma_(f,g)(Q)].

The **genuinely nonlinear coupled two-type interaction** is

    Delta_{uv;wx}S =
          S(f^{uv},g^{wx})-S(f^{uv},g)
        - S(f,g^{wx})+S(f,g)

      = sum_{Q: Q intersects U AND Q intersects V}
          [sigma_(f^{uv},g^{wx})(Q)-sigma_(f^{uv},g)(Q)
           -sigma_(f,g^{wx})(Q)+sigma_(f,g)(Q)].

Proof: for every Q avoiding U, changing f labels of u,v changes none of the physical labels occurring in the point half of Q; therefore its *full seven-class indicator* is identical. Likewise for Q avoiding V on the line half. The mixed four-term expression cancels identically if Q avoids either support. Summation is finite and exact, no probabilistic independence, no fictitious local per-Q label assignment, no asymptotic fit, no assumption of nonnegative mixed derivatives. In particular, this is an all-h identity for FULL seven-family S, not only internal B/A.

This identity also holds componentwise for each of the seven disjoint accepted historical class indicator vectors, and for the selected certified 51-palette GF5 numerator W=sum_Q w(class(Q)) sigma(Q), by linearity. Mixed coefficients can have either sign: their presence is **NOT a positive lower certificate** for the global minimum.

## 3. Rigorous all-h original incidence support ceiling

Let r=|U intersect V|: these are actual original incidences between the TWO changed points and TWO changed lines. Source GQ has no C4, so r<=3. Count original sixsets touching both U and V by a union bound over ordered (e in U,j in V):

- e=j, r possible actual common original incidence IDs: at most C(N-1,5) sixsets per e;
- e != j, |U||V|-r ordered source-incidence pairs: at most C(N-2,4) sixsets per pair.

Therefore for every true original W(3,s), both arbitrary globally injected f,g, and every two-type label transposition,

    M(U,V)=# {Q in binom(E,6):Q cap U != empty and Q cap V != empty}
        <= min{ C(N,6), r*C(N-1,5)
                        + (|U||V|-r)*C(N-2,4) },   r<=3.

Each individual mixed sixset bracket has absolute value at most 2, since its four Boolean terms alternate. Consequently

    |Delta_{uv;wx} S| <= 2 M(U,V)
    |Delta_{uv;wx} W| <= 2 w_max M(U,V),

where w_max is the largest of the seven fixed nonnegative accepted 51-palette class numerators. This is a rigorous **upper sensitivity certificate**, not a lower bound on S and not a substitute for a global source/physical expansion inequality. The finite W32 code calculates its safe numeric upper and verifies actual mixed active supports are contained therein.

## 4. True W32 full seven-class original source oracle

For fixed g, enumerate ALL 62,370 true ORIGINAL sixsets in H_L(g) independently of f using AA4-Q's right-source physical enumerator, then classify the independently computed physical point half for the SAME six ORIGINAL incidence IDs with ONE global f. This does not enumerate left half first and does not call historical seven_census in the main algorithm. Every accepted Q necessarily belongs to H_L, so the seven vector is exact.

For each two-sided swap compare four true full labelings (f,g), (f^{uv},g), (f,g^{wx}), (f^{uv},g^{wx}). Certify the full selected seven-class S, all seven signed mixed differences, the selected fixed-GF5 numerator mixed derivative, and exact cancellation on every original Q avoiding either of the TWO changed source-factor supports. Compare with independent AA4-Q left/right source-major original-sixset join; the test suite also independently compares one-sided fixed-right seven outputs to the historical original sixset 51-palette census. Fixed S68=68, S72=72, lex=259, reverse=169 are baseline regressions, NOT all-h guarantees.

Dedicated hosted test jobs are evidence, not a substitute for independent mathematical review. The parent PR #476 must be accepted on its exact final SHA. The new branch does not modify production source, main, root issue or previous research files.

### Exact genuine W32 nonadditivity witnesses (verified hosted AA4-R dedicated CI)

Perform the SAME point-factor swap (0,1) and line-factor swap (0,1) across four genuine full globally injected ORIGINAL maps; one globally fixed source coordinate pair per factor throughout each map. Distinct point and line source alphabets; original incidence topology unchanged. Independent right-first and two-sided-source-major classifiers agree.

| Original full W32 baseline | S(f,g) | S(f',g) | S(f,g') | S(f',g') | Mixed full-seven Δ²S | Mixed selected 51-GF5 numerator Δ²W |
|---|---:|---:|---:|---:|---:|---:|
| S68 | 68 | 89 | 87 | 104 | **−4** | −185680 |
| S72 | 72 | 95 | 84 | 102 | **−5** | −287757 |

The S68 seven-class signed mixed vector is (A-left/B-right +7, B-left/A-right −8, B/B-disjoint −1, B/B-overlap −1, C/A −1, C/B 0, D6 0); it sums to −4. S72 gives (0, −7, +3, −2, +1, −1, +1) in the same class order; it sums to −5. Each witness is a real full W32 global injection, not an artificial original-source local neighborhood.

**Finite genuine nonseparability theorem:** there does NOT exist a pair of functions F and G such that S(f,g)=F(f)+G(g) simultaneously for all complete globally injected point/line physical K6 label maps on this genuine W32 host. Proof by contradiction: every additive F+G has identically zero four-map mixed derivative, whereas these independently certified genuine four-map rectangles have mixed derivative −4 and −5. The same argument with nonzero mixed 51-palette numerator disproves additive separability for that selected certified weighted numerator. This theorem is for actual W32, not an asserted all-h quantitative lower. It does not preclude nonlinear, jointly geometric lower certificates.

## 5. Mathematical decision and next proof gate

**New result:** mathematically exact full seven-class global mixed support / interaction identities; 3-regular/no-C4 alone explicitly disproved as sufficient ORIGINAL GQ fixture validation. This replaces another unconstrained search over a single B/A charge by a genuine joint nonlinear coupling audit retaining all physical and original incidence identities.

**What is still missing:** a lower bound, uniform in ALL complete globally injected f,g and ALL s=2^h, for the favorable non-AA joint cells plus aligned genuine D6. The mixed difference may be negative; local one- or two-type swap stationarity never certifies global minimax. Nor does the all-h support ceiling grow at the sharp O(s^6) positive-charge scale; it must not be cited as a route to Branch A.

**Next eligible AA4-S theorem target:** form a true-original geometry-constrained joint incidence-cell tensor and prove a nonnegative source-physical expansion lower for non-AA or aligned D6, including a term that explicitly survives a worst-case nonaligned A/A reservoir. Test each proposed tensor inequality on the genuine globally injected adversarial W32 four-map examples and on the fake-C6 **negative-input** oracle before making any all-h claim. If finite falsified, report the actual full global f,g countermap and its seven 51-palette classes; if no theorem, retain OPEN_WITH_FORMAL_BLOCKER.

Acceptance conditions: exact final head hosted AA4-R dedicated tests, INDEX, Proof Audit, Research; independent proof review separate from mechanical CI. Root #230 (A/B), #176, #169 stay OPEN.
