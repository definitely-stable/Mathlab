# HYP-105 / issue #230 — D6-AA4-Y2: universal original seven-mode Gram and sign-robust charge

Scientific status: rigorous ALL-h deterministic factorization and mixed-change estimate. NOT a proof of the root universal Omega(s^6) obstruction. Strict research-only child of Y-CYC PR #497 at d6991ac288add1cb64ac55952b35d6d712430259; main untouched, issue #230 OPEN.

## 1. Quantifiers and ORIGINAL mode space

For EVERY genuine symplectic original generalized quadrangle W(3,s), s=2^h>=2, and arbitrary complete globally injective typed source point/line physical unordered-edge maps f,g into the minimal physical K_a alphabet, index the same actual sets Q of six distinct ORIGINAL point-line incidence IDs on both sides. Immutable source endpoint profiles A=(1^6), B=(2,1^4), C=(2^3) determine the feasible source forest cell, with source C/C forbidden by GQ girth eight.

For each of the six accepted NON-AA historical positive GF5 source forest classes, attach ONE scalar feature mode to a Q of that immutable source class. For each original AA Q, attach 60 alternative connected positional C6 modes H, each a 6-edge 2-factor on the SAME sorted six ORIGINAL Q incidence positions; the 10 disconnected two-triangle modes have NO D6 feature. Source-ineligible Q have none.

Define L_(Q,t,m)(f), R_(Q,t,m)(g) as 0/1 physical half-projection indicators: six physical coordinates of degree exactly 2, and for AA connected dual exactly m. Each half occupies at most one mode per Q. Both typed maps are SINGLE globally coherent injections, not per-Q relabelings.

Historical AA4-Q original six-incidence classification implies EXACTLY, for all h and all f,g:

    C_t(f,g) = sum_(Q,m : tag=t) L_(Q,t,m)(f) * R_(Q,t,m)(g)
    S(f,g) = <L(f),R(g)> = N_nonAA(f,g) + D6(f,g).

For the historical selected positive 51-palette GF5 lower numerator W(f,g) = sum_t w_t C_t(f,g), weights are D6 5643; B-left/A-right 45600; A-left/B-right 45600; C/A 43320; C/B 49050; B/B-overlap 51750; B/B-disjoint 45010. Hence W=<sqrt(w)L,sqrt(w)R>. W is a selected seven-family lower numerator only, NOT full R3.

## 2. NEW ALL-h signed-gradient theorem

Choose ANY four admissible full global maps f0,f1 and g0,g1, not necessarily source swaps. Define mode differences dL=L(f1)-L(f0), dR=R(g1)-R(g0), and integer per-tag energies E_P,t=sum_(mode tag t) dL^2, E_L,t=sum_(mode tag t) dR^2. Every component belongs to {-1,0,+1}; energy is exactly the symmetric difference cardinality of the two original half-mode index sets. AA switching between two different connected C6 modes costs TWO energy units, while switching to disconnected/ineligible costs ONE.

Define four-corner mixed differences Delta C_t=C_t(f1,g1)-C_t(f1,g0)-C_t(f0,g1)+C_t(f0,g0), similarly Delta S and Delta W. Then

    Delta C_t = <dL_t,dR_t>.
    (Delta C_t)^2 <= E_P,t * E_L,t.
    |Delta S| <= sum_t sqrt(E_P,t * E_L,t) <= sqrt(sum_t E_P,t * sum_t E_L,t).
    |Delta W| <= sum_t w_t sqrt(E_P,t * E_L,t)
              <= sqrt(sum_t w_t E_P,t * sum_t w_t E_L,t).

Therefore, for ALL admissible f0,f1,g0,g1,

    S(f1,g1) >= S(f1,g0)+S(f0,g1)-S(f0,g0)
                - sum_t sqrt(E_P,t * E_L,t).

An analogous lower for W holds with w_t times each charge. PROOF: expand the exact original seven-mode Gram identity at four corners; the mixed difference is precisely the inner product of the two signed gradients. Apply Cauchy-Schwarz on each disjoint tag-mode family and then on their direct sum. This handles arbitrary negative, zero, and positive mixed interactions and does not assume statistical independence. It also strictly generalizes the preceding Y-CYC original swap-locality lemma: if physical images change only for swapped original source factors, dL*dR has support only on Q touching both original source supports.

These are exact unconditional ALL-h inequalities but can be quantitatively WEAK: they do not furnish a positive c*s^6 without an additional all-h lower for base intersections and control of original gradient charges. Do not mark root #230 Branch A/B/C solved.

## 3. Independent original W32 finite falsifiers

Native C++20 engine reuses the previously successful true ORIGINAL 62,370-per-half six-ID enumerator, constructs one-hot non-AA and connected C6 ORIGINAL position modes independently for each side and each 106 global source swap variants, and computes EXACT seven-tag integer symmetric difference energies against the full complete baseline typed map. Its output is a 212-row TSV: point/line side, move ID, seven integer energies. No synthetic source Q or physical-label orbits.

The separate Y-CYC C++ original 106x106 global pair enumerator regenerates all 11,236 historical accepted original seven-GF5 motif counts per pinned S68/S72. Python audits EVERY one of 11,236 four-corner per-class signed differences using integer squares against each seven-class exact Cauchy energy product; the aggregate S and historical weighted W bounds are also checked. Sectorwise sqrt bounds are conservatively rounded UP using integer isqrt. A separate Python ORIGINAL per-Q mode builder compares its product exactly with the independent historical seven-GF5 classifier under one and jointly swapped complete global f,g. Extremal genuine negative interactions from Y-CYC are preserved and must satisfy the charge inequality.

Reproduce on GitHub-hosted ubuntu-latest with Python 3.12 and C++20:

    python -m unittest discover -s research -p test_hyp105_issue230_d6aa4y2_original_mode_gram.py -v
    g++ -std=c++20 -O3 -Wall -Wextra -pedantic -o /tmp/y research/hyp105_issue230_d6aa4ycyc_bilateral_original_join.cpp
    g++ -std=c++20 -O3 -Wall -Wextra -pedantic -o /tmp/y2 research/hyp105_issue230_d6aa4y2_original_mode_gradient.cpp
    python research/hyp105_issue230_d6aa4y2_original_mode_gram.py --scheme S68 --native-matrix /tmp/y --native-gradient /tmp/y2 --summary /tmp/S68-gram.json
    python research/hyp105_issue230_d6aa4y2_original_mode_gram.py --scheme S72 --native-matrix /tmp/y --native-gradient /tmp/y2 --summary /tmp/S72-gram.json

## 4. Decision and limitations

The theorem is a universal sign-robust quantitative transfer identity, not a Branch A obstruction or model-equivalent Branch C reduction. Next research gate: establish strong all-h controls on true-original source forest baseline mass and C6 alignment versus negative gradient energy; first assess numerical tightness in the complete W32 local grids. A finite tightness observation does NOT imply a general bound. Retain research Draft; require exact-head Dedicated, INDEX, Proof Audit, Full Research SUCCESS and independent mathematical review before integration. Keep issue #230 OPEN.

## 5. Stronger NEW exact harmful-versus-favorable signed transport

The generic Cauchy estimate is analytically valid but numerically loose: the genuine original S68 worst negative mixed delta is -70 against a conservatively rounded seven-sector Gram upper 53,105; S72 is -76 against 52,099. These are TRUE original independent hosted initial-check outputs, not all-h lower bounds. A more informative sign-robust charge must retain signed mode coincidences rather than lose cancellation in the energy norm.

For each ORIGINAL feature k=(Q,tag,mode), its true signed point-side change dL_k and line-side change dR_k belong to {-1,0,+1}. Define FOUR **nonnegative integer** counts per historical original seven-mode feature space:

    F_pp = #{k : dL_k=+1, dR_k=+1},
    F_nn = #{k : dL_k=-1, dR_k=-1},
    H_pn = #{k : dL_k=+1, dR_k=-1},
    H_np = #{k : dL_k=-1, dR_k=+1}.

These are shared mode intersections on the SAME original six-incidence Q and same connected AA positional C6 pattern, not loosely overlapping physical label sets. EXACT universal all-h equality:

    Delta S = (F_pp+F_nn) - (H_pn+H_np).
    Delta W = sum_k w_tag * (+1 for pp/nn, -1 for pn/np).

Consequently the **exact sign-robust harmful-charge transfer** is

    S11 >= S10 + S01 - S00 - (H_pn+H_np),
    S11 - [S10+S01-S00-(H_pn+H_np)] = F_pp+F_nn >= 0.

Similarly W11 >= W10+W01-W00 - (weighted H_pn+weighted H_np) with exact nonnegative weighted favorable surplus. This is strictly sharper than an arbitrary Cauchy upper for the sampled cases, though still NOT a positive all-h root obstruction unless harmful conflicts are bounded relative to baseline source-forest mass. The equality is universally valid for arbitrary four globally complete maps, not merely transpositions.

**Proof:** for one mode k, the integer product (dL_k)(dR_k) is 0 if either difference vanishes; otherwise it is +1 when the signs agree and -1 when they disagree. Partition the finite original shared mode set into the four possible nonzero sign classes and sum. Historical tag weights are nonnegative integers and constant across map corners for immutable source Q profiles. No independence assumptions or sign-of-Hessian restrictions. For point/line source swaps, Y-CYC's true original support theorem applies to each intersection.

Native independent C++20 signed-conflict engine reconstructs 106 complete point half-mode sets and 106 complete line half-mode sets per anchored W32 true original mapping, forms signed half-mode symmetric differences, then counts ALL four quadrants on EVERY 106x106 paired corner. It emits a FULL 11,236-row TSV including pp/nn/pn/np AND their exact selected historical 51palette positive GF5 weighted sums. Python verifies the exact literal original seven GF5 Delta S and Delta W from the SEPARATELY computed full Y-CYC two-sided original 62,370/62,370 incidence-index joined matrix. Each sampled true-original Q is independently checked with historical GF5 classification. The full certificate is retained as hosted workflow artifact.

Do not infer a lower bound S_s>=c*s^6 from this exact decomposition. It converts the root science blocker into a precise task: prove genuine all-h harmful mode intersections cannot overwhelm unavoidable original forest/AA positive structure. Quantitative strength and finite gap must be assessed from last exact-head GREEN CI.

## 6. Independent exact W32 signed-mode charge results

Verified source-run https://github.com/definitely-stable/Mathlab/actions/runs/38711231772 : specialized three-job workflow SUCCESS, including two separate original all-11,236-pair matrix and seven-mode C++ signed-quadrant reconstruction passes. The following measured counts derive from the hosted executed ORIGINAL full global-map certificates, not from simulations or inferred asymptotic scaling:

| Exact true-original W32 quantity | S68 anchor | S72 anchor |
|---|---:|---:|
| Number full globally coherent paired source maps | 11,236 | 11,236 |
| Strictly mixed maps | 11,025 | 11,025 |
| Mixed Delta S negative/positive/zero | 8,286 / 2,396 / 343 | 8,642 / 2,096 / 287 |
| Worst negative Delta S | -70 | -76 |
| Harmful original same-mode conflicts H at worst Delta S | 103 | 106 |
| Favorable same-mode coincidences F at worst Delta S | 33 | 30 |
| Earlier seven-sector Gram rounded CS upper on abs(Delta S) at this witness | 53,105 | 52,099 |
| Exactly charged lower S11 at worst Delta S witness | 63 | 77 |
| Actual S11 at this witness | 96 | 107 |
| Smallest sharp signed-conflict lower S11 over all 11,236 | **6** | **2** |
| Actual minimum selected S over all 11,236 from original independent Y-CYC | 68 | 72 |

Exact four-corner witness S68: swap actual original POINT source factors (4,14) and LINE source factors (4,11), with (S00,S10,S01,S11)=(68,107,127,96), Delta S=-70, F=33,H=103. GF5 weighted signed interactions: favorable 1,510,360 and harmful 4,693,160, giving exact mixed Delta W=-3,182,800.

Exact four-corner witness S72: swap actual original POINT source factors (2,5) and LINE source factors (6,11), (72,126,129,107), Delta S=-76, F=30,H=106. Weighted favorable 1,379,120 and harmful 4,762,669, Delta W=-3,383,549.

**NEW finite positive certificate from a general ALL-h-valid transfer principle:** For EVERY member of the explicitly enumerated 106×106 global original source point/line swap box around S68, independent sign-segregated original feature sets certify S>=6; around S72, S>=2. This proof does NOT use the full two-sided pair count S11 as an input to the lower bound; it uses S00,S10,S01 and independent original source mode harmful intersection H per joint pair. The separate complete two-sided Y-CYC original GF5 classification checks these lower bounds and records the stronger actual finite minima.

The new finite charge certificate is genuinely nonvacuous (positive), unlike the earlier minimum Cauchy-charge lower values -58,880 and -59,113. It remains far weaker than actual S minima and DOES NOT prove a uniform lower in arbitrary s=2^h or arbitrary full global f,g outside these finite boxes. Its value is demonstrating a sound, sign-robust transfer primitive and identifying the specific harmful original source-mode intersections that require quantitative all-h control.
