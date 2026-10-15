# HYP-105 issue #230 — EICE-003-J: TRUE ORIGINAL four-GQ-anchor filtered codegrees

**Research-only acceptance: RESTRICTED_THEOREM_J / OPEN_WITH_FORMAL_BLOCKER.** Strict child of fully GitHub-hosted-green [EICE-003-I PR #465](https://github.com/definitely-stable/Mathlab/pull/465), pinned parent HEAD \`15277df2ce222d96020d360be10fbbf97034c25a\`. No main change/merge, no Branch A/B, no ASET exponent and no seven-GF5 positive original sixset transfer.

## J1 — new exact source-anchored pair-codegree identity

Work with globally injective TRUE W(3,s) physical pair maps f,g and exactly the previous I1 genuine original middle source e=(p2,l2) physical-quadrant model. The four external ORIGINAL incidence IDs of a valid five-source 2×2 template split 2+2 between one of the opposite quadrant pairs Q00/Q11 or Q01/Q10, with distinct outside physical x and y partner coordinates among all four.

For one directed physical middle diagonal with opposite exterior source classes A,B, and a fixed unordered two-arm row pair (a,a')∈A satisfying x(a)≠x(a') and y(a)≠y(a'), define TRUE original path status on each candidate row–column cell (a,b) by directly decoding f^-1({outer_x(a),outer_x(b)}), g^-1({outer_y(a),outer_y(b)}). The five mutually exclusive original source statuses are from EICE-003-E:

    status 0: at least one original endpoint point/line label absent;
    status 1: both endpoints exist and are ORIGINAL GQ incident;
    status 2: genuine nonincident endpoint pair, unique ORIGINAL GQ anchor end-dirty;
    status 3: unique ORIGINAL nonincident end-clean GQ anchor internally blocked by source e;
    status 4: unique ORIGINAL nonincident end-clean GQ anchor internally unblocked.

For a selected predicate Z on ORIGINAL statuses, let B_Z(a,a') be the TRUE original source-column arm IDs b∈B such that the four outside-coordinate uniqueness constraints hold against BOTH selected rows, and BOTH status(a,b) and status(a',b) belong to Z. For these original arms, count how many share each outside x coordinate and each outside y coordinate; write degrees d_x, d_y. The exact number of simultaneously accepted 2×2 TRUE source templates with this fixed row pair is

    T_Z(a,a') = C(|B_Z(a,a')|,2)
               - Σ_x C(d_x,2) - Σ_y C(d_y,2).           (J1)

The subtraction is exact: two DIFFERENT original source incidence arms from the SAME physical quadrant cannot have both the same outer x and outer y, because this would imply identical globally injected f(p),g(l) and hence the same original source incidence ID. No double-counted collision correction is necessary.

Sum J1 over all possible row pairs and BOTH opposite quadrant pairs:

    H_e(Z) = Σ_{opposite quadrant pair} Σ_{row pairs} T_Z(a,a'). (J1-EXACT)

This is an all-h exact identity for *real* ORIGINAL source incidence five-sets with the actual physical four-corner paths. It is not a simple weighted mean or pseudomarginal, and does not assume statistical independence of the four original GQ anchors.

## J2 — exact four-ORIGINAL-anchor filter cascade

Apply J1 to the nested acceptance predicates

    Z0={0,1,2,3,4} (all physical I1 source templates),
    Z1={1,2,3,4} (all FOUR original endpoints decodable),
    Z2={2,3,4}   (all FOUR true endpoint pairs nonincident),
    Z3={3,4}     (all FOUR true GQ anchors end-clean),
    Z4={3}       (all FOUR true GQ anchors internally blocked).

This gives an exact monotone cumulative chain for EVERY original e:

    A_e=H_e(Z0)>=H_e(Z1)>=H_e(Z2)>=H_e(Z3)>=H_e(Z4)=H_e.

The differences H_e(Zk)-H_e(Zk+1) are the exact number of original five-source physical templates whose FIRST failed simultaneous-four-corner property is, respectively, endpoint decode, nonincidence, end-clean unique source projection, and internal blocking. They are **not probabilities** unless divided by a specified positive denominator and not a positive-GF5 count. In particular H_e(Z3)-H_e(Z4) counts source templates for which all four ORIGINAL anchors are end-clean but at least one is not internally blocked.

J1 for Z0 is independently required to equal I2's full exact physical source-quadrant template count A_e; J1 for Z4 is independently required to equal the EICE-003-G **complete physical graph** count of actual coherent all-four-blocked original five-source families with UNIQUE middle e. By EICE-003-I's EXACT TWO oriented physical representations, the COMPLETE G source-physical count must be precisely 2 Σ_e H_e. Both equalities are executable hard assertions.

## J3 — independent real TRUE ORIGINAL GQ anchor oracle and masking

The source code uses \`status_of_cell\` (earlier EICE-003-E) only as the main status evaluator. A **SECOND INDEPENDENT checker** computes ORIGINAL q,r directly from globally injected physical pairs, checks r∈point_lines[q], fetches the unique genuine original anchor q–ell–p–r and independently checks the end-dirty/internal source overlap conditions against ORIGINAL f,g and the original middle incidence e. The two evaluations must match for EVERY evaluated cell.

A third oracle directly enumerates true original four-arm source combinations, recomputes the four source-cell statuses (without using J1 codegrees), and compares exact original 5-stage counts for ALL W32 middle source IDs and sampled W34 middle IDs.

For every genuine all-four-blocked TRUE original source five-set, independently retain:
- All four actual original endpoint point/line IDs (different original points and lines due to EICE-003-E);
- Their true unique original GQ projections and HYP-105 internal source blocker masks L/R/B, with the adjacent-same-side versus exact two-checkerboard F2 dichotomy;
- All TRUE cross point–line ORIGINAL incidences in the 4×4 source submatrix, which satisfy the genuine W(3,s) girth-eight <=8 count;
- EXACT five original source incidence IDs, no fabricated adjacent SOURCE factors and NO inferred positive GF5 sixset.

All evaluations are on TRUE original globally injected f,g, not random independent labels or abstract physical K_2,2 alone.

## J4 — what the all-h equation DOES and DOES NOT prove

With EICE-002 high-degree same-source G*, EICE-F5/F6/J1 and the I3 exactly-two oriented-source multiplicity imply

    Σ_e H_e >= δ⁴ s⁸ / 2,560,000
              * q_s(theta_I),   δ=10^-6,
    q_s(theta)=max(0,4theta-3,theta⁴-2/(δs-1)).

(The left-hand side counts source-middle-indexed allblocked five-source templates from the COMPLETE true original GQ physical source. Any template of actual G* contributes a unique source five-set, and restricting it to those sources preserves its true masks. It can have extra full-source physical candidate paths but its five-source template is unique by I3.)

Therefore, if a uniform all-h **upper** theorem showed

    Σ_e H_e = o(s⁸),

then theta_I=o(1) would follow on every valid EICE-002 same-map high-degree G*, potentially closing the INTERNAL branch of the separately unfinished Opus theorem R reduction. A stronger sufficient bound is max_e H_e=o(s⁴) because N=(s+1)^2(s²+1)=Θ(s⁴). **Neither bound is established here.** The source row-pair formula is a new exact parameterization, not itself a nontrivial upper on four simultaneous GQ source anchor collisions.

In particular, the I2 physical template count A_e can be much larger than its filtered H_e. Observing H_e/A_e small for W34 Lex/Random cannot be extrapolated to adversarial correlated f,g at arbitrary s. The accepted seven GF(5) original positive-sixset classification for W34 is not available from frozen K6-specific oracle; J does NOT classify or produce a single such new positive motif.

### J4-C — a simpler candidate proof gate: FOUR original end-clean anchors

Since H_e <= C_e, the stronger (but OPEN) all-h theorem

    max_e C_e = o(s⁴)   uniformly for all actual global injections f,g

would force the needed \`max_e H_e=o(s⁴)\`, without even analyzing the final interior-blocking predicate. Here C_e is the exact count of five-incidence original source templates with ALL FOUR genuine nonincident end-clean anchors (original status in {3,4} at all four corners). An alternate sufficient global upper is \`sum_e C_e=o(s⁸)\`. Neither candidate is established. The finite cascade merely identifies this as a promising place to focus true source geometry.

## J5 — exact finite source cascade, independently verified

Every original source incidence e is exhausted for the four globally injected W32 schemes and W34 Lex/Random. The TRUE original source 2×2 five-incidence capacity and four-anchor cascade is:

| TRUE source map | Physical templates A | Four endpoints decoded D | Four nonincident N | Four end-clean anchors C | Four internally blocked H |
|---|---:|---:|---:|---:|---:|
| W32 Lex | 44 | 44 | 6 | 0 | 0 |
| W32 Reverse | 24 | 24 | 12 | 0 | 0 |
| W32 S68 | 2 | 2 | 1 | 0 | 0 |
| W32 S72 | 6 | 6 | 6 | 0 | 0 |
| W34 Lex | **251 962** | **164 602** | **127 831** | **6 421** | **467** |
| W34 Random | **212 905** | **120 908** | **94 876** | **7 968** | **575** |

The maximum same-middle original source counts in W34 Lex are respectively \`3526,2634,2021,129,18\`; W34 Random \`1689,1132,1021,133,13\`. In Lex only 6421/127831≈5.02% of fully nonincident physical templates have all FOUR true anchors end-clean, then only 467/6421≈7.27% of those are all-four internally blocked. In Random the corresponding fractions are 7968/94876≈8.40% and 575/7968≈7.22%.

These are finite true original globally injected source observations, NOT uniform all-h estimates. The independent complete ORIGINAL physical-NB3 G oracle yields 934 and 1150 ORIENTED allblocked squares, exactly twice the 467 and 575 original five-sets. Both mask channels agree exactly. The independent direct original four-arm enumeration checks the pair-codegree identity for every W32 middle source e and selected W34 e, and all true source-status evaluations are checked against a separately implemented original GQ anchor oracle.

## J5 — reproducible exact finite W32/W34 pipeline

- \`research/hyp105_issue230_anchor_filtered_codegrees.py\`: exact source quadrant four-corner GQ anchor codegree identity, monotone cascade with clear failure stages, complete finite W32/W34 globally injected original map counts, actual original GQ girth, L/R/B typed masks and separate physical G oracle equality.
- \`research/test_hyp105_issue230_anchor_filtered_codegrees.py\`: independent direct four-source original cell grid oracle and exact codegree equality on ALL 45 W32 source middles and sampled W34 source middles, independent full W34 global physical G oracle comparison for 467/575 real five-source blockings, independent true-source-status validation, fail-closed budgeting/invalid labels, no false ASET/GF5 claims.
- \`docs/research/HYP-105-ISSUE230-EICE003J-ANCHOR-FILTERED-CODEGREES.md\`: this proof/limitations.
- \`.github/workflows/hyp105-issue230-eice003j.yml\`: single focused GitHub-hosted \`ubuntu-latest\` job, no self-hosted runner, with J test, W32/W34 full report, parent I exact regressions.

**Next EICE-003-K research gate:** interpret the exact filtered original source matrix J1 using GQ spectral and source-anchor geometry to prove a UNIFORM \`H_e=o(s⁴)\` (or \`Σ_e H_e=o(s⁸)\`), rather than confusing the known physical template count A_e with true source allblocked H_e. An alternative is an all-h original seven-GF5 sixset compensation with a rigorously bounded preimage count. Keep PR Draft, root issue OPEN.
