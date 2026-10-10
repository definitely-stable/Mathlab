# HYP-105 B3.2-E1-C22 — one-common-global-right joint seven-family tensor and exact adversarial swap audit

Date: 2026-10-11. Root [#230](https://github.com/definitely-stable/Mathlab/issues/230); stacked on C21-D [#321](https://github.com/definitely-stable/Mathlab/pull/321) -> C21 [#317](https://github.com/definitely-stable/Mathlab/pull/317) -> C20 CI [#316](https://github.com/definitely-stable/Mathlab/pull/316) -> C20 science [#315](https://github.com/definitely-stable/Mathlab/pull/315). Main remains separate.

**Status:** two exact ALL-h combinatorial identities plus an ALL-h D6 transposition influence upper, and a complete **finite genuine W(3,2)** exact joint seven-family one-swap adversarial diagnostic. Neither a universal seven-family \(\Omega(s^6)\) lower nor infinite correlated \(o(s^6)\) family is proved. The open mathematical gate of #230 remains **OPEN_WITH_FORMAL_BLOCKER**.

## 1. The exact model — original six-incidence sets, not local block assignments

Let \(\Gamma=W(3,s)\) be the original GQ(s,s) bipartite incidence host of V=(s+1)(s²+1) original point objects P and V original line objects L, with original incidence-edge set E(\Gamma) of size N=V(s+1). Let \(f:P\to F_L\) and \(g:L\to F_R\) be ONE globally consistent injective map each into an occupied pair alphabet of a physical K_a, where a is the minimal integer with C(a,2)>=V. A six-incidence set J is an unordered set of six **different original incidence IDs**. Each source incidence \((p,\ell)\) carries physical left pair \(f(p)\), physical right pair \(g(\ell)\); repeated original endpoint objects always carry the SAME physical pair label.

Define \(\mathcal J_L(f)\) as the DISTINCT original six-incidence sets whose physical left six pairs form a loop-free 2-regular six-physical-coordinate multigraph; each occurs once. For each J, let \(\kappa_L(J)\) and \(\kappa_R(J)\) be the multiplicity partitions of its ORIGINAL left point and right line endpoints (A=(1,1,1,1,1,1), B=(2,1,1,1,1), C=(2,2,2); otherwise inadmissible). Let \(I_R(J,g)\) indicate that the physical right pairs also form a six-coordinate 2-factor. The accepted seven-category tag \(\phi_J(f,g)\) is:

* A/A: D6 **only if** the physical left column-position dual is a connected C6 and the physical RIGHT column-position dual is exactly equal on the SAME six original incidence columns. Else rejected, including unaligned A/A and disconnected 3+3 left dual.
* B/A: B-left/A-right.
* A/B: A-left/B-right.
* A/C or C/A: C/A.
* B/C or C/B: C/B.
* B/B: B/B-overlap iff doubled ORIGINAL left point and doubled ORIGINAL right line touch at one common original incidence column; otherwise B/B-disjoint. The double intersection is impossible in a simple original incidence bipartite graph.
* Other original multiplicity profiles, or right physical non-2factor: rejected.

Each admitted sixset receives EXACTLY ONE tag or none; no factor of 6! or 10 GF5 signed events is silently inserted into S. Then for every s and f,g:

    S_seven(f,g) =
        SUM_{J in J_L(f)} 1[phi_J(f,g) is one of the seven tags].

The accepted **necessary GF5 floor numerator**, NOT exact total R3, is

    Q7(f,g) =
        SUM_{J in J_L(f)} R3_CERTIFIED_FLOORS[phi_J(f,g)]

with zero for a rejected J; its fraction is Q7(f,g)/(51^6). All weights are those frozen in historical B0: D6=5643; B/A=A/B=45600; C/A=43320; C/B=49050; B/B-overlap=51750; B/B-disjoint=45010.

This is a model-equivalent expression for **the seven accepted original-incidence classes** for every legal all-h GQ instance, not a full R3 expression and not a lower bound on the minimum.

## 2. ALL-h exact six-pair parity-and-coverage lemma

Represent a physical unordered pair \(\{u,v\}\) with bit mask \(m=2^u+2^v\). For any six physical pairs, including repeats, total physical degree is exactly 12. They use EXACTLY six distinct physical coordinates, each with degree two, **if and only if**

    popcount(m_1 OR ... OR m_6) = 6
    and (m_1 XOR ... XOR m_6) = 0.

Proof: the XOR zero condition says every occupied physical coordinate has even degree, and OR popcount six says there are exactly six occupied coordinates. Every occupied degree is a positive even integer at least two; six times two is the fixed total degree twelve, hence every occupied degree is exactly two. The converse is immediate. This proof does not use s=2, physical a=6 or injectivity of the six individual edges; it applies to any a, thus to the repeated right original B/C profiles as well.

The executable exhaustive test independently checks ALL unordered six multisets over K6 physical pair palette, including repeated physical pairs, against direct integer degree counts. The only all-h claim here is the elementary identity; finite tests independently falsify its implementation.

## 3. ALL-h exact one-global-right-transposition fiber locality

Let \(\tau_{uv}\) transpose physical pair labels of TWO ORIGINAL right lines \(u,v\), without changing any other original right line's assigned pair. Let \(g'=g\circ\tau_{uv}\) mean the globally switched right assignment (not a per-sixset optimizer). For every J not containing an incidence with ORIGINAL right endpoint u or v, all its physical right pairs are unchanged, and \(\phi_J(f,g')=\phi_J(f,g)\). Thus the exact original-source identity is

    S_seven(f,g') - S_seven(f,g)
      = SUM_{J in J_L(f), J touches u or v}
          (1[phi_J(f,g')]-1[phi_J(f,g)]).

The SAME equation holds for Q7 after replacing unit weights with category weights. This is a global correlated **rearrangement identity**, not a lower for any g. In particular the right source J_L(f) is compiled ONCE from the true 45 original W32 incidences; complete right swaps update only original sixsets in the joint affected fiber. Unaffected original sixsets retain their exact previous seven tag and GF5 necessary floor.

A sharper specialized all-h UPPER bound controls how many *left simple C6* original sixsets can be touched by swapping two original right GQ lines. A fixed original line has Delta=s+1 incident points. For each original incidence (p,line), at most \(24\binom{a-2}{4}\) physical C6s include f(p), each with at most Delta^5 ways to choose incidences at the five other distinct ORIGINAL points. Thus the number touched by one original line is at most \(24\binom{a-2}{4}\Delta^6\). With two original lines, union bound:

    #affected-left-C6-original-sixsets <= 48*C(a-2,4)*(s+1)^6.

Therefore

    |D6(f,g')-D6(f,g)|
      <= min(48*C(a-2,4)*(s+1)^6,
             60*C(a,6)*(s+1)^6) = O(s^12).

This counts each original incidence J at most once in the actual source, upper-bounding overlaps via a union bound. It is independent of the particular legal f,g and missing right/left physical pair labels. **O(s^12) is vastly weaker than a positive \(\Omega(s^6)\) floor**, so this is a sensitivity lemma, NOT worst-g robustness or acceptance of issue #230 Branch A.

## 4. Finite exact common-GQ joint seven-class compiler

The hosted C22 implementation restricts enumeration to **true original W(3,2)**, with fifteen ORIGINAL points, fifteen ORIGINAL lines, exactly 45 incidences, physical K6 on each side and fixed global original left f(p)=PAIRS[p]. It enumerates exactly once the established E1-A **62,370 DISTINCT original six-incidence sets** with physical-left 2-regular six-coordinate projection: A=51,030, B=10,935, C=405.

It precomputes ORIGINAL left/right multiplicity profiles and the left column-position dual when relevant. The compressed source key is

    (static original seven-class candidate,
     six actual ORIGINAL right line IDs in original incidence-ID order,
     exact physical left column-position dual or unused sentinel).

Equal compressed keys retain a positive INTEGER multiplicity of DISTINCT original sixsets; no source counts disappear. A globally complete right g maps each original right line ID to exactly one physical pair, shared by every J. The right parity/coverage criterion and (for D6) exact dual signature determine acceptance. This compiler independently agrees with historical 62,370-original-incidence B0 seven_census and C0 weighted B/A six-uniform hypergraph overlap at multiple complete right maps; the earlier C21-D independent direct physical-left-C6 oracle independently confirms D6 counts.

The C21-D baseline uses g(line)=PAIRS[perm[line]] with

    perm=(4,13,2,9,14,3,6,0,8,1,11,5,7,12,10).

The source is unchanged for all its 105 complete right-original-line transpositions. For each of these, C22 records the actual global seven-vector, S_seven, Q7 numerator, number of touched compiled groups, number of changed group tags, number of changed ORIGINAL sixsets, exact S histogram, exact class-conditional S and Q7 minima (with their globally compatible attaining right transpositions), and the exact D6/complement covariance numerator. Histograms/minima are scoped **ONLY TO THIS 105-NEIGHBORHOOD**, NOT all 15! right permutations or all left f, and not all-h.

**Do not interpret covariance sign as all-h compensation.** A D6=0 configuration with S>0 is a true finite counterexample only to D6-alone mean-to-min; the size of its other six classes neither proves nor refutes a universal seven-family \(\Omega(s^6)\).

### Independently verified finite 105-neighborhood minima and NO-GO for naive compensation

A second independent exact GF(2) W32 incidence generator and original six-incidence enumerator confirms exactly **62,370** unique left-source sixsets (A=51,030, B=10,935, C=405), **52,309** statically eligible original sixsets and **36,272** weighted source signatures. It then computes the seven-vector under all 105 single global right transpositions from the C21-D baseline, reproduces the earlier independent D6 histogram 0:40, 1:29, 2:24, 3:6, 4:4, 5:1, 9:1, and certifies the restricted exact minima:

    min over THESE 105 complete global right transpositions S_seven = 122
    min over THESE 105 accepted GF5 necessary numerators Q7 = 5,623,340
    both witnessed by swapping ORIGINAL right line IDs 4 and 14
    global right perm at baseline = (4,13,2,9,14,3,6,0,8,1,11,5,7,12,10)
    one-swap true original seven-vector at (4,14):
      D6=0, B-left/A-right=47, A-left/B-right=57,
      C/A=2, C/B=0, B/B-overlap=11, B/B-disjoint=5.

By contrast the baseline complete g has seven-vector (0,60,66,5,0,9,6), **S=146** and Q7=6,698,010. The SAME original global left f and SAME true GQ incidence host are used. The one-swap true global g changes the six-class residual count from 146 to 122 **without adding any D6**. Therefore a proposed **monotonic-compensation premise** such as "D6=0 implies the other six-class count is at least its D6=0 baseline value 146 throughout the one-swap neighborhood" is rigorously FALSE even on genuine W32. This does NOT rule out a *different* seven-family all-h inequality or a uniform positive minimum: 122 remains strictly positive and covers only 105 right maps at s=2.

These independent finite integers are now frozen as executable regression assertions in the C22 test suite; a different result is a CI FAIL, not an opportunity to silently revise the research claim. The full original historical B0 seven_census remains a separate comparator on several complete right maps, rather than sole self-reference to the new compiled tensor.

## 5. Executable independent falsification and CI

Source: research/hyp105_g5e2b3e1c22_joint_seven_tensor.py
Tests: research/test_hyp105_g5e2b3e1c22_joint_seven_tensor.py
Dedicated GitHub-hosted Contract: .github/workflows/hyp105-c22-contract.yml

Independent tests: all K6 unordered six multisets (repeated pairs included) check mask identity vs direct degrees; all 70 physical K6 twofactors split 60 single-C6/10 disjoint-C3; original W32 full 62,370 candidates and original A/B/C counts; 105 exact full right swap vectors and D6 histogram vs independent C21-D; direct full joint recounts for selected swaps vs sparse swaps; independent complete 62,370-original-set B0 seven_census + C0 weighted-source B/A checks at multiple diverse swapped actual global right maps; physical RIGHT K6 coordinate relabel gauge; malformed input caps and incomplete right permutations fail closed.

Full Research six GitHub-hosted shards preserve all existing C21-D 121 command names/runs, add exactly TWO C22 explicit tests/report commands (123), update frozen FNV1a hash, and enforce the fail-closed seventh aggregate. No self-hosted runner. Do not promote to accepted or merge before exact HEAD dedicated Contract, full Research and INDEX success and staged base ancestry reconciliation.

## 6. Next scientific decision gate

Candidate for C23: seek a non-vacuous **joint full seven-family** global extremal lower or a rigorous infinite actual W(3,2^h) small-S family, not D6-only and not an expectation. The exact C22 local swap tensor is useful for falsifying proposed finite trade-off inequalities (and for engineering efficient true-global search), but 105 swaps cannot establish any global minimum. For every candidate inequality: quantify over all original f,g, distinguish s=2 exception from asymptotic claim, and check whether C9/C10 low-pin barriers or C18/C19 local-block sabotage invalidate it. Preserve ROOT OPEN_WITH_FORMAL_BLOCKER without all-h proof.
