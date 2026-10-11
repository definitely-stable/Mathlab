# HYP-105 C24-B8-C — exact conditional right mean and two-edge orbit discrepancy gate

Root: [issue #230](https://github.com/definitely-stable/Mathlab/issues/230). Scientific stacked parent: [C24-B8-B PR #358](https://github.com/definitely-stable/Mathlab/pull/358), HEAD `d79fddff6c046daff1f6eaacec3fbf79779f6355`. No merge, main changes, self-hosted runners, or reuse of old-head CI as acceptance.

## 1. The main analytic defect in the prior program

B8-B provides EXACT overall mean under TWO uniform independent complete global point/line injections; yet HYP-105 Branch A quantifies over **ALL f,g**, so that annealed mean is insufficient. A needed intermediate is the exact CONDITIONAL uniform-right mean for EVERY FIXED left f, together with worst-case conditional discrepancy:

    mu_s(f) = E_{g uniform COMPLETE injection} S_s(f,g);
    D_s(f) = max_g [mu_s(f)-S_s(f,g)] = mu_s(f)-min_g S_s(f,g).

The second equality is a tautology, NOT progress by itself. This slice isolates what can be proved and calculated exactly without falsely solving the discrepancy bound.

## 2. Theorem C24-B8-C1: exact conditional mean given arbitrary full fixed LEFT f

Let s=2^h>=2, V=(s+1)(s²+1), a=min{a:C(a,2)>=V}, M=C(a,2). f is ANY complete global original-point-to-physical-edge injection. g is uniformly drawn from the FULL set of complete global original-line-to-physical-edge injections, independently of this fixed f. Sixsets J are ORIGINAL distinct incidences; each J uses one common map f,g.

Define p_A(a),p_B(a),p_C(a),p_sigma(a) exactly as in B8-B3, with the physical six-coordinate 2-factor template counts 70/45/15 and ONE fixed D6 connected cycle dual signature probability p_sigma=C(a,6)*6!/(M)_6.

Let T_ordinary(f) be the original distinct J with one of six ordinary tags, with physical LEFT factor eligible L_J(f)=1. Let T_D6(f) be original A/A J with a CONNECTED left physical six-cycle dual signature. Then

    mu_s(f) =
        sum_{J in T_ordinary(f)} p_(right original endpoint profile of J)(a)
      + |T_D6(f)| * p_sigma(a).

PROOF: Ordinary acceptance is L_J(f)*R_J(g); the right marginal physical degree-two event probability depends only on the number of distinct original lines and their multiplicities, because g restricted to any k original lines is an injective uniformly random k-tuple of distinct K_a physical edges. For D6 the left signature is FIXED; right acceptance requires ONE specific six-incidence-position connected dual cycle. Its right marginal probability is p_sigma rather than 60 p_sigma² or p_A. Apply linearity across ORIGINAL sixsets, without any source-independence assumption. QED.

This exact formula can be evaluated using B2's *compressed but ORIGINAL-multiplicity-preserving* left source fibers without drawing a single g. Independent full 62,370 ORIGINAL W32 left source enumeration tests it against the compressed result at s=2. The full GQ all-h typed eligible source count still requires geometric estimates if one wants a uniform lower of order s^6.

## 3. Theorem C24-B8-C2: zero first-pin information, exactly two second-pin orbits

Fix arbitrary distinct original right lines i != j and ANY physical edge e of K_a. Conditional on g(i)=e, the remaining complete injection is uniform over all injective assignments avoiding e.

The score S(f,g) is invariant under a physical coordinate permutation acting on g ALONE (hold f fixed): original right 2-factor eligibility depends on six-coordinate vertex degrees, and the D6 right dual cycle signature on the SIX ORIGINAL INCIDENCE POSITIONS is unchanged by coordinate renaming. Thus the full symmetric coordinate group Sym(a) acts transitively on the M physical edges and maps conditioning g(i)=e to any g(i)=e'. Consequently

    E[S_s(f,g) | g(i)=e] = mu_s(f)   for EVERY i,e.

In particular the first revealed right physical edge has identically zero Doob martingale increment, even after f is arbitrarily optimized.

Fix g(i)=(0,1). The stabilizer of this physical edge has EXACTLY TWO orbits on the M-1 available physical edges for g(j):
- adjacent: 2(a-2) edges sharing exactly one physical vertex with (0,1);
- disjoint: C(a-2,2) edges sharing none.

Write mu_adj(f;i,j) and mu_dis(f;i,j) for the conditional right means in these two second-pin orbits, which are well defined independently of the chosen edge representatives. Then

    2(a-2) * mu_adj + C(a-2,2) * mu_dis = (M-1) * mu_s(f).

This is an EXACT signed two-orbit centered projection on ALL original source populations and ALL globally complete physical injections. It does not require independence across sources or assume that a physical edge assigned to g(j) can be selected separately for different J. The right conditional means can be evaluated sourcewise via the finitely many injective completions of at most six distinct source lines, preserving all previously pinned occupied physical edges.

**No conclusion for min_g S follows from the two-orbit identity alone.** In particular nonnegative weighted average cannot be read as a worst-case positive lower. The second-pin conditional score might decrease in one class while increasing in the other. The first Doob increment is zero but later increments may be large.

## 4. Theorem C24-B8-C3: exact right-C adjacent-pair hard-zero

Let an ORIGINAL J have RIGHT endpoint-multiplicity pattern C=(2,2,2), so exactly three different original right lines occur twice each. To be physical-right eligible, their three distinct physical edges must form a perfect matching of six physical coordinates (three pairwise disjoint edges, each appearing twice in the six-incidence multiset). If any TWO of those three distinct original lines are globally assigned physical edges sharing a vertex, J is CERTAINLY rejected for every legal completion of all other right assignments.

Thus for any such original source J and two of its three right lines i,j,

    E_g[X_J(f,g) | g(i),g(j) intersect] = 0

for ALL s,h,f and all legal complete global right assignments conditioned as stated. With e_i,e_j disjoint, the third right-line physical edge must avoid four occupied physical vertices; if the left is ordinary eligible (e.g. C/A or C/B), its exact conditional probability is

    C(a-4,2) / (M-2)

and for the marginal

    p_C = 15*C(a,6)*3!/(M)_3.

For a=6: p_C=3/91, adjacent conditional=0, disjoint conditional=1/13, and the orbit-weighted mean gives 8*0 + 6*(1/13) = 14*(3/91).

This is a sharp all-h conditional exclusion, NOT a global seven-score lower: many other source types can be accepted and the global right injection can correlate the three-edge matching statuses across sources.

## 5. Independent executable falsification and bounded CI

- `research/hyp105_g5e2b3e1c24b8c_conditional_discrepancy.py`: exact symbolic probability for fixed-f original tagged sources, a mathematically exact compressed left-source conditional mean, a separate per-ORIGINAL-sixset mean, and a budgeted exact conditional source completion enumerator (global pins are shared, no per-J optimized mappings).
- `research/test_hyp105_g5e2b3e1c24b8c_conditional_discrepancy.py`: five fast tests. Independent three-double-edge original C profile forces adjacent hard-zero and disjoint 1/13. Original B profile repeated edge similarly forces some adjacency hard-zeros. D6 matching connected C6 signature tested on both second-pin coordinate orbits, including an explicit conjugate pair. A REAL original W32 3,003-sixset subuniverse compares independent uncompressed-source conditional mean against an independently built compressed sixset fiber. Guarded invalid and oversized exact enumeration cases fail closed.
- `research/hyp105_g5e2b3e1c24b8c_w32_conditional_witness.py`: isolated dedicated-contract execution. For the true W32 global LEFT f0 from C24-B1, independently enumerate ALL 62,370 f0-eligible original sixsets (not only one baseline right-accepted set), then compare exact conditional-right mean by ORIGINAL tag against the separate C24-B2 51k compressed left fibers. Score the baseline ONE complete right g68=68, additionally verify original RIGHT-FIRST census and invariance of the full seven-vector under three distinct physical coordinate transpositions of g alone, and find a genuine ORIGINAL W32 right-C source with a certified zero adjacent-pin conditional probability. No 15! enumeration and no 11,236 B7 map repeat.
- Dedicated GitHub-hosted C24-B8-C Contract runs fast 5 tests and one W32 conditional mean report separately from old Research. Existing 141 named Research commands, six shards + fail-closed seventh aggregate, and INDEX are unchanged. Research foundation auto-discovers ONLY the quick tests; no heavy original full sixset census hidden in generic unittest.

The witness's exact W32 conditional mean is **NOT guessed**. Accept its rational numerical value only from the hosted HEAD-specific independent original enumerations. Freeze numerical regression only in a separately budgeted follow-up if it provides scientific benefit, since updating HEAD causes all CI to run again.

## 6. Next theoretical decision (C24-B8-D or STOP)

The mathematically relevant unproved objective is uniform ALL-f control of the conditional LEFT physical source-weight profile and worst-case RIGHT signed discrepancy. An explicit SUFFICIENT Branch-A criterion is:

    for all s=2^h>=s0 and every allowed f:
      mu_s(f)>=c0*s^6;
      sup_g[mu_s(f)-S_s(f,g)]<=c1*s^6;
      c1<c0.

C24-B8-C1 determines the exact mu_s(f) algebraically; C2 isolates the first nontrivial coordinate-orbit dependence at TWO fixed right assignments; C3 provides a physically forced zero class. NONE of them establishes c0>c1 or even positive c0, and no Chernoff/independent-sixset concentration claim is valid.

Further work should attempt either (a) all-h count or signed incidence-tensor discrepancy exploiting GQ six-edge structure under full injection; (b) a rigorous infinite correlated f_s,g_s family with o(s^6) full seven score. High-cost finite local minima search, an unconditional first moment, a one-pin symmetry statement, and generic pairwise spectral estimates do not by themselves settle #230.

**Verdict:** RESTRICTED_THEOREM_C_CONDITIONAL_MEAN_ORBIT, pending latest-head Contract + complete Research + INDEX. Root #230 remains OPEN_WITH_FORMAL_BLOCKER. No PROVED_A, COUNTEREXAMPLE_B, full GF5 R3 upper or ASET exponent. No main merge.
