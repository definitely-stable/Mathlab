# HYP-105 issue #230 — EICE-003-K: exact TRUE ORIGINAL GQ dirty-anchor pencil identity and physical-template concentration

**Acceptance:** \`RESTRICTED_THEOREM_K / OPEN_WITH_FORMAL_BLOCKER\`. Strict research-only child of fully green [EICE-003-J Draft PR #467](https://github.com/definitely-stable/Mathlab/pull/467) pinned at \`834e1e753746fa044f09313ea79cec1683d1531b\`. Never change \`main\`. No accepted positive GF(5) six-incidence compensator, no Branch A/B proof, no ASET exponent. The previously proposed bound \`max_e C_e=o(s^4)\` remains **OPEN**; this slice prevents an invalid proof based on declaring original anchor cleanness globally rare.

## 1. K1 — exact all-h dirty-anchor source-pencil identity

Let \(\mathcal Q=W(3,s)\) be the genuine ORIGINAL generalized quadrangle, \(s=2^h\), \(V=(s+1)(s^2+1)\), \(a=\min\{b:\binom b2\ge V\}\). The globally injective ORIGINAL point labels \(f(q)\) and line labels \(g(r)\) are distinct edges of \(K_a\).

For every ORIGINAL nonincident source point/line pair \((q,r)\), let its unique ORIGINAL GQ anchor be the genuine source path

    q -- ell -- p -- r

in the ORIGINAL incidence graph (three actual source incidences). Define its two END-DIRTY events

    D_f(q,r) = 1[ f(q) intersects f(p) ],
    D_g(q,r) = 1[ g(r) intersects g(ell) ].

The source endpoint is end-clean iff both events are zero. These events concern the anchor's own **ORIGINAL endpoint labels**, NOT overlap of its central source labels f(p2),g(ell2); the latter are EICE-I/J *internal blocking* and are a different predicate.

Fix a TRUE original point q. Each other TRUE original point p collinear with q has exactly ONE ORIGINAL source line ell through q,p; among the s+1 genuine lines through p, exactly s are different from ell, and every such r is NONINCIDENT with q and has UNIQUE GQ anchor q--ell--p--r. Consequently the number of left-end-dirty pairs \((q,r)\) with fixed q equals

    s * t_f(q), where
    t_f(q) = #{p≠q : p is ORIGINAL GQ collinear with q,
                  f(p) intersects f(q)}.

Likewise, for any true original line r, the right-dirty pairs \((q,r)\) with r fixed are \`s*t_g(r)\`, where \`t_g(r)\` counts other ORIGINAL GQ-intersecting lines ell with \`g(ell) intersects g(r)\`.

**K1 all-h exact identity:**

    D_left  = s * sum_q t_f(q)
            = 2s * #{unordered collinear ORIGINAL q,p with f(q)∩f(p)≠∅},
    D_right = s * sum_r t_g(r)
            = 2s * #{unordered intersecting ORIGINAL r,ell with g(r)∩g(ell)≠∅}.       (K1)

Each original physical pair f(q)={x,x'} intersects at most \`2(a-2)\` OTHER possible edges of simple \(K_a\). Global f-injectivity implies \`t_f(q)<=2(a-2)\`, and likewise for g. Thus

    D_left  <= 2s(a-2)V,
    D_right <= 2s(a-2)V,
    D_union <= D_left+D_right <=4s(a-2)V.                               (K1-UB)

There are exactly \`V*(V-(s+1))=V*s²*(s+1)\` TRUE ORIGINAL nonincident (q,r) pairs. Divide by this genuine source-domain total:

    Pr_{UNIFORM TRUE ORIGINAL nonincident(q,r)}[anchor end dirty]
          <= min(1, 4(a-2)/(s(s+1))) = O(s^(-1/2)),                    (K1-UNIFORM)

since minimal a=Theta(s^(3/2)). Hence the ORIGINAL end-clean fraction is AT LEAST \`1-4(a-2)/(s(s+1))\`, and **tends to one for EVERY globally injective f,g**. The union estimate may be vacuous for small s; cap it at one. The exact finite census separately counts dirty LEFT-only, RIGHT-only, BOTH and their intersection; K1 union bound itself is not generally sharp.

**Logical NO-GO:** a proposed all-h proof of \`C_e=o(s^4)\` cannot be justified by claiming a uniformly chosen ORIGINAL q,r nonincident anchor is unlikely to be clean. The all-h theorem proves the OPPOSITE marginal fact: original end-clean is asymptotically typical. The 4-anchor scarcity seen on W34 Lex/Random must be caused by the strong nonuniform and correlated **I1 physical source-template** endpoint law, if it persists under adversarial globally injected maps. K1 does **NOT disprove** that 4-anchor capacity upper itself; it only invalidates this naive one-anchor-marginal argument.

As another mathematically valid but NOT applicable-to-physical-templates illustration, any hypothetical joint sample of four (possibly dependent) ORIGINAL nonincident endpoint pairs in which EACH of four individual marginals is uniform over all ORIGINAL nonincident pairs satisfies by union bound

    Pr[all 4 anchors end clean]>=max(0,1-16(a-2)/(s(s+1))).

The actual four physical I1 endpoint pairs have NO such marginal uniformity assumption. Do not apply this inequality to J's \`C_e/N_e\`.

## 2. K2 — explicit source-law mismatch on genuine W32/W34

Two exact and distinct probability spaces are measured:

1. **GLOBAL UNIFORM ORIGINAL q,r law:** sample uniformly a genuine original NONINCIDENT pair; take the unique ORIGINAL GQ anchor and its f/g end-dirty indicators. K1 applies.
2. **QUENCHED SOURCE-CORRELATED 5-ID physical-template law:** sample an actual I1-valid ORIGINAL five-incidence source set with all FOUR q/r endpoints nonincident, conditioned on a frozen real original global f,g source assignment. Demand that **ALL FOUR** true GQ anchors be end-clean, as counted by EICE-003-J \`N_e,C_e\`.

The second law has a conditioning to a true physical five-source quadrant matching AND a simultaneous 2x2 four-corner joint requirement, so it is not implied by the first law. The implementation reports both EXACT rational fractions side-by-side, without inventing independence or transferring them to GF5-positive sixsets.

The earlier GitHub-hosted J census has, on genuine W34 Lex/Random, \`sum_e N_e=127831/94876\`, \`sum_e C_e=6421/7968\`, so the second all-FOUR-end-clean fractions are exactly \`6421/127831\` and \`7968/94876\`. The new independent K source-marginal audit computes the first law for the same actual globally injected label maps, providing a falsifiable direct comparison. These W34 values do not constitute an all-h clean-anchor scarcity theorem for the source-correlated physical template law.

## 3. K3 — exact ORIGINAL dirty-anchor endpoint pullback and obstruction

Fix a TRUE middle ORIGINAL source incidence e=(p2,ell2). Let \(\mathcal T_e^{NI}\) be the exact finite set of genuine I1 physical five-incidence templates with ALL FOUR actual source q/r endpoint pairs NONINCIDENT. Write \`N_e=|T_e^{NI}|\` and \`C_e\` for the subset with ALL FOUR true ORIGINAL anchors END-CLEAN.

For every genuine ORIGINAL end-dirty nonincident q,r define \`M_e(q,r)\` as the number of corner OCCURRENCES of that dirty original pair over ALL templates in \(\mathcal T_e^{NI}\). If one template has multiple dirty source endpoints, it contributes multiple occurrences; no independence or uniformity is assumed. Then the exact multiset identity and deterministic four-corner union inequality are

    sum_{original dirty (q,r)} M_e(q,r)
        = sum_{T∈T_e^{NI}} #{dirty true original GQ anchors of T},
    N_e-C_e <= sum_{original dirty (q,r)} M_e(q,r)
           <= 4(N_e-C_e).                                            (K3)

This is not an upper on C_e. Rather, it precisely captures the possible **concentration/amplification** of dirty ORIGINAL endpoint pairs in the physically source-selected sample, despite their global O(s^(-1/2)) upper density. A future mathematical attempt to control C_e via ORIGINAL marginal information must additionally bound the actual highly nonuniform transport multiplicities M_e(q,r).

\`exact_middle_dirty_pullback\` independently constructs all true physical five-source quadrant matching templates for a user-selected actual e; decodes its FOUR ORIGINAL q/r pairs using a SECOND independent GQ anchor-status algorithm (not J's row-pair codegree); retains all four only when nonincident; computes the true distinct dirty original pair support, all LEFT/RIGHT/BOTH dirty-anchor masks, dirty-corner-per-template histogram, and verifies the exact inequality (K3). It is crosschecked against the separately computed J count at selected W32/W34 middle source IDs. Budgets fail closed; finite experiments cannot prove an all-h transport multiplicity bound.

## 4. Research conclusion and next proof gate

- **PROVED all h, algebraically:** exact K1 point/line GQ pencil identity and O(s^-1/2) global ORIGINAL nonincident anchor dirtiness; exact K3 source-template dirty pullback count/union identity.
- **VERIFIED finitely:** original W32 Lex/Reverse/S68/S72, W34 Lex/Random; six deterministic additional genuine globally injected W32 f/g label permutations; independent source q/r census, true line/point pencil identities, strict source-lifting selected e against J.
- **NOT proved:** original four-anchor end-clean capacity \`max_e C_e=o(s^4)\`, joint original anchor correlation bound, original seven GF5 positive sixset transfer, all-h root Branch A/B, ASET exponent.
- **WARNING against mistaken route:** global uniform original anchor dirtiness tends to ZERO, so original four-anchor cleanliness cannot be made scarce by a one-point marginal pigeonhole or unconditioned mixing argument. The actual source-conditioned 2x2 endpoint law is the central mathematical obstruction.

**Next EICE-003-L:** obtain a quantified ORIGINAL endpoint-pair TRANSPORT bound \`M_e(q,r)\` or a GQ source-fibre condition preserving four-corner correlations. A useful alternative is to find actual adversarial globally injected f/g mappings giving high per-middle C_e, which could falsify the tentative \`o(s^4)\` target; either outcome advances the mathematics. Do not count positive original GF5 sixsets without all-h accepted-seven proof.

## Implementation

- \`research/hyp105_issue230_clean_anchor_concentration.py\`: all-h integer bound, exact original q/r dirty/source GQ pencil census, true five-source-vs-uniform diagnostic, independently anchored per-middle original endpoint dirty transport.
- \`research/test_hyp105_issue230_clean_anchor_concentration.py\`: 7 focused independent tests, true source point/line pencil checks, six adversarial deterministic W32 globally injected maps, W34 parent-J stage and K3 independent direct endpoint-pullback verification, invalid/budget fail closed.
- \`docs/research/HYP-105-ISSUE230-EICE003K-CLEAN-ANCHOR-CONCENTRATION.md\`: this proof and limitations.
- \`.github/workflows/hyp105-issue230-eice003k.yml\`: GitHub-hosted ubuntu, no user PC or self-hosted runner, tests and exact finite W32/W34 report and J regression.

No main edits, no merge; Draft until exact HEAD CI green and independent math review.
