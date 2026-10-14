# HYP-105 / issue #230 — EICE-003-H: true GQ spectral double-star source fibres and heavy-middle criterion

**Acceptance:** \`RESTRICTED_THEOREM_H / OPEN_WITH_FORMAL_BLOCKER\`. Strict research-only child of [Draft PR #463](https://github.com/definitely-stable/Mathlab/pull/463), parent fixed at \`73edb2e4da20d7d9ec69b52b134f63a770f70e14\`. No merge, no main change. No Branch A/B, no all-h GF5 accepted-seven classifier extension, no ASET exponent. **The key new bridge is a genuine source-fibre constraint, NOT an o(s^8) global abundance theorem.**

## H1 — exact source GQ incidence spectral polynomial

For genuine W(3,s), s=2^h, let \`V=(s+1)(s²+1)\` and let \`B\` denote its ORIGINAL V×V point–line 0/1 incidence matrix, with regular degree \`d=s+1\`. By generalized-quadrangle source geometry, for the ORIGINAL point-point collinearity graph A one has

    B B^T = d I + A.

The point-collinearity graph is strongly regular with parameters

    (V, k, λ, μ) = ( (s+1)(s²+1), s(s+1), s-1, s+1 ),

where its eigenvalues are \`k=s(s+1), r=s-1, t=-(s+1)\`. Hence the ORIGINAL true-source incidence singular values are \`s+1\`, \`sqrt(2s)\`, and \`0\`. Equivalently, with C=B B^T and J the all-ones V×V matrix,

    C^2 - 2s C = (s+1) J.                          (H1)

This identity has **integer entries** and is independently verified over ALL V² entries in the real W32/W34 fixtures, without numerical eigenvalue fitting. The GQ spectral theorem is standard mathematics; only its exact use as an ORIGINAL five-source physical-overlap capacity certificate is the new research direction here.

For ANY sets P of true original points and L of true original lines with \`x=|P|, y=|L|\`, the expander-mixing lemma and nontrivial singular value \`sqrt(2s)\` imply

    | e_GQ(P,L) - dxy/V |
       <= sqrt(2s) * sqrt( x(1-x/V) * y(1-y/V) ).

After multiplying by V and squaring, the exact, finite-integer falsifier becomes

    ( V e_GQ(P,L) - dxy )²
         <= 2s x(V-x)y(V-y).                      (H1-MIX)

No probabilistic or random-label independence assumption is used.

## H2 — NEW all-h true-original double-physical-star source-fibre theorem

Fix ANY true original middle incidence \`e=(p2,ell2)\`. Its two globally injective ORIGINAL physical pair labels are \`f(p2)={x0,x1}\`, \`g(ell2)={y0,y1}\`. Define

    P_e = { p TRUE original point : f(p) intersects f(p2) },
    L_e = { ell TRUE original line : g(ell) intersects g(ell2) },
    F_e = { e'=(p,ell) TRUE original incidence : p∈P_e, ell∈L_e }.

Because f,g are injective into *simple* K_a pairs, a given pair intersects at most \`2a-3\` selected source labels, including itself. Hence \`x_e=|P_e|<=2a-3\`, \`y_e=|L_e|<=2a-3\`.

Each original incidence source e'=(p,ell) contributes EXACTLY TWO disjoint physical Kikuchi diagonals; their combined four physical endpoints are the Cartesian set f(p)×g(ell). Therefore **an exact, bidirectional identity** holds:

    F_e = { e' : [ f(p')×g(ell') ] intersects
                    [ f(p2)×g(ell2) ] nontrivially }.    (H2-PHYSICAL)

This formula retains the TWO original-source diagonals, not only one edge. It means that F_e is the complete *true ORIGINAL source ID bandwidth* whose physical endpoints can touch any of the four physical corners associated with the middle original source e.

If a genuine source-coherent 2×2 NB3 plaquette has TRUE ORIGINAL middle incidence ID e and four external original source IDs e1,e2,e3,e4, then every physical outer arm touches a physical vertex of its central middle edge and therefore **ALL FIVE true original IDs lie in F_e**:

    {e,e1,e2,e3,e4} subset F_e.                 (H2-LOCALIZE)

This remains true for every globally injected original labeling and ANY genuinely coherent paired G*. It is independent of the actual GQ anchor status / positivity and does not pretend that adjacent physical path edges share ORIGINAL source factors.

Applying H1-MIX to P_e,L_e yields the TRUE uniform source-fibre upper

    |F_e| <= d x_e y_e / V
           + sqrt(2s) sqrt[x_e(1-x_e/V)y_e(1-y_e/V)].

In particular,

    |F_e| <= d(2a-3)^2/V + sqrt(2s)*(2a-3)
           = O(s²)    for minimal a=O(s^(3/2)).             (H2-O2)

This is all-h, deterministic, and survives arbitrarily correlated labels f,g. The implementation uses an exact integer upper certificate (no square-root rounding optimism), enumerates every true physical-pair overlap set, and independently sums the true original line-point pencils.

The source bipartite subgraph induced by ANY five such genuine incidences is a **forest**, since the ORIGINAL GQ incidence girth is 8 and five edges cannot contain a cycle. The finite oracle explicitly reconstructs point/line degree sequences, connected components, and the exact forest identity \`#edges=#vertices-#components\`. This forest property is a standard GQ consequence, not a positive original GF5 motif proof.

## H3 — rigorously isolated HEAVY-MIDDLE condition for Branch A

EICE-003-F F5/F6 and EICE-003-G G4 proved, on a fixed EICE-002 source-coherent **stationary high-degree** G* with the SAME globally injective f,g, and \`δ=10^-6\`, for \`s=2^h>=2^22\`:

    # distinct actual all-four-blocked five-ORIGINAL-incidence source sets
       >= δ^4*s^8/(25,600,000) *
          q(s,theta),

    q(s,theta) = max{0,4theta-3,theta^4-2/(δs-1)},

where theta denotes the TRUE stationary internal end-clean blocked path probability on that SAME valid G*, and the at-most-20 oriented squares per ORIGINAL five-source ID set multiplicity has been proved.

There are exactly \`N=(s+1)^2(s²+1)=Theta(s^4)\` possible genuine original source middle incidence IDs. Every five-source blocked set has at least ONE genuine realized middle incidence; fix one deterministically for counting (not an arbitrary abstract transport coordinate). By pigeonhole there exists a TRUE middle source e supporting at least

    H_e >= [δ^4*s^8/(25,600,000*N)]*q(s,theta).  (H3-HEAVY)

If \`theta>=epsilon>0\`, the RHS is \`Omega_epsilon(s^4)\`. This is a real quantitative NECESSARY condition on any high-blocked hypothetical counterexample, and stronger than simply saying 'some fibre is large'.

**Critical unresolved gap:** H2 says F_e contains only \`O(s²)\` possible genuine arm incidence IDs, but this leaves up to \`binom(O(s²),4)=O(s^8)\` four-arm subsets per middle source e; it does NOT imply \`H_e=o(s^4)\`. Similarly, EICE-002 physical degree coherence only gives a crude local \`O(s^6)\` oriented square-slot capacity per middle incidence e, which is above the required \`Omega(s^4)\` load. Therefore **H2/H3 do NOT close Branch A**.

One very concrete sufficient (NOT PROVED) future source-capacity theorem would be

    max_e H_e = o(s^4) uniformly over ALL global f,g and
                    their valid EICE-002 coherent G*.         (OPEN H4)

Combining that with H3 would force \`theta_I=o(1)\` for these G* and could close the internal-blocking side of the Opus route, IF the separate path/endpoint E-H reduction and the remaining positive-sixset transfers were also formally accepted. The theorem is powerful but presently unsupported. No spectral estimate in this PR proves it.

## H4 — exact finite W32/W34 global source-fibre pressure census

The executable implementation extends the prior fully sourced W34 exhaustive five-incidence search via an OPTIONAL \`export_true_five_source_families\` result. Export is off by default, preserving all prior F/G behavior and deterministic CI. When enabled every counted family carries its sorted five ORIGINAL incidence IDs, every ACTUALLY REALIZED true middle original source ID, exact oriented square multiplicity, and true original blocker-mask channels.

For the real W32 lex/reverse/S68/S72 and W34 lex/random global fixtures it computes:
- H1 exact integer polynomial over ALL V² source point pairs;
- H2 exact true source double physical-star incidence fibre for EVERY one of the N original incidence IDs;
- independent line-point-pencil census for every true fibre and squared integer expander mixing;
- full G2 true five-source blocked families from the COMPLETE source graph, **not merely empty canonical small G***;
- true original forest degree sequences and components for each distinct five-source set;
- count/size of true middle-source fibres carrying these families; signed source role participation and top-heavy middle source ID lists;
- no all-h entropy, spectral o(s^4) source count, global seven-GF5 compensation or Branch A claim.

**Special note on the frozen accepted seven-GF5 classifier:** the existing W32/K6 exact class machinery does not apply to W34; therefore no motif positivity conclusions are inferred from the W34 five-source analysis.

## Next proof gate — EICE-003-I

Target a *geometric* restriction on the number of distinct **simultaneously blocked and end-clean** original five-source forests inside each real true GQ double-star fibre F_e. Quantitatively, seek a \`o(s^4)\` upper (or an explicit constant lower than H3 at fixed positive theta) on that number uniformly over all-h, using BOTH original GQ anchor projections and physical paired-diagonal coherence; mere H1 expander mixing or the H2 source fibre size O(s²) is insufficient. Alternatively implement an all-h certified accepted original seven-GF5 family oracle and construct a bounded-multiplicity transfer. Keep issue #230 OPEN; do not merge research PR pending independent proof audit.

## Artifacts

- \`research/hyp105_issue230_spectral_source_fibres.py\`
- \`research/test_hyp105_issue230_spectral_source_fibres.py\`
- \`docs/research/HYP-105-ISSUE230-EICE003H-SPECTRAL-SOURCE-FIBRES.md\`
- \`.github/workflows/hyp105-issue230-eice003h.yml\`
- Optional source family export extension in \`research/hyp105_issue230_five_source_blocked_search.py\`.

Research-only Draft. All mathematical upper bounds are explicitly scoped; finite tests do not substitute for all-h proof.
