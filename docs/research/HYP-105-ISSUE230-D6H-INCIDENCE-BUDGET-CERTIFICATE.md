# HYP-105 #230 — D6-H: all-h sufficient incidence-budget theorem

**2026-10-13. RESTRICTED_THEOREM_C; SUFFICIENT ALL-h THEOREM, NOT ROOT BRANCH A.**

Stacked over [D6-G Draft #406](https://github.com/definitely-stable/Mathlab/pull/406). The true complete accepted seven GF5-positive ORIGINAL sixset family is available only for W(3,2) in these diagnostics. W(3,4)/W(3,8) BB-only subsets never become the complete seven-family denominator.

## 1. Universal sufficient allocation theorem

Fix any finite original incidence universe, distinct-incidence source triples T, integer oriented blocked-path multiplicities w(T), accepted distinct-incidence sixsets Q in A, and integer target capacity K>=0. Define:

- C=sum_T w(T), S=|A|;
- L(e)=sum_{T containing e} w(T), including both endpoint E and internal-only I paths;
- d(e)=number of accepted ORIGINAL sixsets containing e;
- D_K=C-maxflow_K from the exact D6-D factored network, the D6-F minimum integer exception mass.

**Allocation theorem (all finite universes, hence every h and every true original global f,g):** Let a(Q,e)>=0 be rational numbers, supported only on e in Q, and satisfying sum_{e in Q} a(Q,e)<=K. Define c(e)=sum_{Q containing e} a(Q,e). Solve the fractional source->T->e->sink maxflow with incidence-to-sink capacities c(e), obtaining V. Then

    D_K <= floor(C-V).

**Proof.** Decompose the T->e fractional flow by ORIGINAL common incidences. At each e, the incoming V_e<=c(e) units can be distributed among incident recipients Q with slot capacities a(Q,e), because every source using e intersects each such Q in e. Every recipient's combined slots total at most K. Thus the full ORIGINAL D6-D network has a feasible fractional assignment of V units. That network has integer w(T), K, and an integral maximum flow, so it can route at least ceil(V) source units. Hence D_K<=C-ceil(V)=floor(C-V).

This is a sufficient bound only: reserved recipient capacity may be much less effective than the exact D6-D flow. No fixed universal K or small D_K is asserted.

### 1.1 Uniform six-incidence allocation

Choose a(Q,e)=K/6 for each of the six ORIGINAL incidences of Q. Then c(e)=K*d(e)/6. Let V_6 be the integer maxflow in the scaled-by-six T->e network: source capacities 6w(T), incidence-to-sink capacities K*d(e). Therefore

    D_K <= floor((6*C-V_6)/6).

Splitting each source path equally across its three ORIGINAL incidence ports supplies scaled load 2L(e) at e. Clipping its load at K*d(e) yields a completely local bound:

    D_K <= floor[(1/6)*sum_e max(0,2*L(e)-K*d(e))].

**Pointwise all-h sufficient criterion:**

    if 2*(L_E(e)+L_I(e)) <= K*d(e) for every original source incidence e,
    then D_K=0 and C<=K*S.

Both E and I MUST share the same incidence budget. Giving them each a full capacity K would double-spend positive recipients.

### 1.2 Integral concentrated budgets

Choose a deterministic selector pi(Q) among the six ORIGINAL incidences of each accepted Q. Assign the entire K-slot target budget to the selected incidence pi(Q). Let n_pi(e)=|{Q:pi(Q)=e}| and V_pi be integer T->e maxflow with incidence capacities K*n_pi(e). Then

    D_K <= C-V_pi.

Two independent deterministic selectors are implemented: largest joint source-incidence load L(e), ties resolved by original incidence ID; and greedy remaining load L(e)-K*n_pi(e) in sorted sixset order. Both are sufficient constructions, not purported optimum algorithms. Take the minimum exception upper bound among uniform and two integral orientations.

## 2. New analytic route and conditional consequence

D6-E–G expose exact Hall maxima over all source-closed F. D6-H gives a sufficient local certificate avoiding enumeration of all F. For the actual PR394 coherently retained H, proving for some absolute K and eta>0 that

    sum_e max(0, 2L(e)-K*d(e)) <= 6*(16-eta)*s^6 + o(s^6)

would establish D_K<=(16-eta)*s^6+o(s^6), hence

    (16-o(1))*s^6 <= (K+2)*S_s + sqrt(192*m*S_s)+D_K

and, using m=Theta(s^4), conditionally

    S_s >= (eta/(K+2)-o(1))*s^6.

The strongest target is an all-h overload o(s^6), but NO such analytic estimate currently exists. The pointwise condition itself is not shown to hold on high-h PR394 H.

## 3. Executable contract and independent validation

- [Implementation](../../research/hyp105_issue230_d6h_incidence_budget_certificate.py): scaled integral source-to-incidence maxflow, equal-source-thirds overflow, and two integral recipient orientations.
- [Tests](../../research/test_hyp105_issue230_d6h_incidence_budget_certificate.py): independent exhaustive unit-by-unit assignment on small synthetic instances; global and local Hall obstructions; unsupported incidences; K=0; endpoint/internal decomposition; four complete genuine W32 seven-positive global maps checked against D6-F exact exceptions.
- [GitHub-hosted contract](../../.github/workflows/hyp105-issue230-d6h-incidence-budget-certificate.yml): fail-closed comparison of exact D6-F exception against every D6-H certified upper and source/recipient degree identities.

Uniform 1/6 allocation can be very conservative: an integral concentrated assignment may close a case where the uniform bound is nonzero. No W32 finite congestion is extrapolated all-h. W34 and W38 full seven-positive S remain unmeasured.

## 4. Pinned genuine W32 complete-seven exact finite certificates

The first GitHub-hosted D6-H Contract [#38353460351](https://github.com/definitely-stable/Mathlab/actions/runs/38353460351) succeeded with four independent tests. Its original same-map W32 complete-seven report yielded the following, now pinned to prevent accidental changes:

| Original W32 scheme | K | D6-F exact exception | D6-H uniform 6-scaled exception upper | Simpler equal-thirds overflow upper |
| --- | ---: | ---: | ---: | ---: |
| lex | 3 | 165 | **165** | 180 |
| lex | 4 | 0 | **0** | 61 |
| reverse | 5 | 53 | **53** | 131 |
| reverse | 6 | 0 | **0** | 63 |
| S68 | 8 | 62 | **62** | 105 |
| S68 | 9 | 0 | **0** | 72 |
| S72 | 9 | 10 | **10** | 119 |
| S72 | 10 | 0 | **0** | 90 |

In each of these eight *finite* complete-seven true-original W32 cases, the uniform 1/6 fractional incidence allocation is **exactly optimal** after integrality, while the easier pointwise source-thirds overflow is not always sharp. This is not evidence of all-h equality: the actual high-h complete positive-recipient incidence degrees d(e) are analytically unconstrained.

## 5. Strict status

Proved as mathematics (pending independent review): the universally quantified sufficient incidence-allocation theorem and its local overload corollary. Finite source data and CI do not replace proof.

OPEN: all-h uniform K, all-h small incidence overload or exception mass, true PR394 high-h nonvacuous certificates, full original W34/W38 seven-positive S, Branch A/B, complete R3 and ASET exponents. Keep #230/#176/#169 OPEN, stacked PRs Draft, and main untouched.

**Next:** derive, or explicitly falsify under a coherent infinite construction, a quantitative lower bound on d(e) or an all-h positive recipient selector pi that can absorb the joint original incidence path loads L_E(e)+L_I(e). Do not assume independence or replace the seven-class family by BB-only.
