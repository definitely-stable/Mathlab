# HYP-105 / #230 — AA4-BP: simultaneous k original cherries on ONE repaired full global map

**Scientific Draft, strict child [#583](https://github.com/definitely-stable/Mathlab/pull/583), parent exact SHA 90b21425e6263887482c212e022dd560bdadfc48.** Genuine symplectic W(3,2^h) original incidence and SIX distinct ACTUAL original source flag IDs per Q. Both already completely fixed possibly correlated f,g original factor pair-edge injections, unchanged source incidence, ONE common repaired map. No main or accepted registry edits. Root #230 OPEN_WITH_FORMAL_BLOCKER.

## Prior work and novelty

[#580](https://github.com/definitely-stable/Mathlab/pull/580) already gives an exact candidate-level source assignment compatibility test and Cayley shortest path for selected original Q and targets. Immediate parent [#583](https://github.com/definitely-stable/Mathlab/pull/583) already forces compatible targets for TWO arbitrary distinct physically pin-regular original same-type cherry roots, yielding ONE globally corrected map within EIGHT transpositions, with BOTH roots accepted on it. Parallel [#581](https://github.com/definitely-stable/Mathlab/pull/581) already proves ONE-root h≥22 THREE-swap repair and [#584](https://github.com/definitely-stable/Mathlab/pull/584) its same-Q radius-THREE multiplicity. None of those scopes are claimed new.

**AA4-BP new result:** for EVERY fixed f,g, force simultaneously accepted original B/A for ANY k distinct BL-regular source POINT cherries, where k GROWS as Θ(s), on ONE single globally corrected complete original LINE map within 4k swaps while preserving the UNION of every original source root LINE pin at every step. This is not a proof about the original unchanged g.

## Exact all-h theorem

Let s=2^h,h≥5, d=s+1,V=(s+1)(s²+1), and a=min{n:binom(n,2)≥V}, m=binom(a,2)−V≤a−2. Fix ANY genuine original symplectic W(3,s) and ANY fully globally injected original POINT map f and LINE map g into their separate typed complete K_a pair-edge alphabets. The true source geometry can be adversarially correlated with both physical maps.

Call an actual original source POINT cherry root r=(p;(p,l1),(p,l2)), l1 distinct from l2, **BL-regular** if every physical coordinate endpoint of the two EXISTING right pair-edge images g(l1),g(l2) has at most floor((a−4)/8) incident missing right physical pair edges of K_a minus im(g), as established by [AA4-BL #577](https://github.com/definitely-stable/Mathlab/pull/577). More than 3/4 of all genuine original point cherries are BL-regular for every given complete g (PRIOR result).

Set

\[
\boxed{k_*(s)=\min\{\lfloor s/8\rfloor,\lfloor(a-4)/16\rfloor\}.}
\]

For any 1≤k≤k_*(s) and ANY k distinct genuine original BL-regular POINT cherry roots r1,...,rk, there exists a SINGLE complete globally injected ORIGINAL LINE physical map g' with all of the following:

1. Exactly the SAME original W(3,s) source incidence graph and full original POINT f, and EXACTLY same occupied physical right edge support im(g')=im(g).
2. Every authentic original LINE factor ID appearing in ANY root twoflag pair keeps its original current physical pair edge image throughout ALL intermediate swaps and in g'.
3. g' is reachable from this GIVEN g in at most **4k TRANSPOSITIONS OF WHOLE ORIGINAL LINE factor physical pair edge images**, always maintaining globally injected complete maps onto the same right support.
4. There are **k DISTINCT six-element sets Q1,...,Qk of SIX DIFFERENT genuine-original source incidence flag IDs** on this SAME final f,g'. Each Qi contains its exact chosen original two root flags, has true source point factor B profile, six DISTINCT original LINE factor IDs, physical point projection a double f(p_i) edge plus an occupied physical C4, and physical right projection a connected C6 on six right coordinates. All k Qi are HISTORICALLY GF5-POSITIVE B-left/A-right SIMULTANEOUSLY under ONE final g'. The genuine original LINE-root/POINT-image-swap dual gives A-left/B-right.

Formally,

\[
\boxed{\forall f,g\ \forall R\subset\mathrm{GoodCherries}(g):
1\le|R|=k\le k_*(s)\quad\exists g'_R\in B_{4k}(g):
\ \forall r\in R,\ U_{B/A,r}(f,g'_R)\ge1.}
\]

The repaired common map depends on R. No source incidence IDs are redrawn and no independent local map per Q is allowed.

## Proof: uniformly disjoint SOURCE factor assignments + physically compatible target sixcycles

For all k genuine source roots, collect the union P of their existing opposite original LINE source factor IDs pinned by their actual two source flags, |P|≤2k. Their current occupied pair images g(P) are distinct because g is injective. Process the k roots in any fixed order. After i−1 roots, keep four DIFFERENT free original LINE source factor IDs per previously selected Q, all outside P, forming F_{i−1} of size exactly 4(i−1). Keep four DIFFERENT occupied FREE right target physical pair edges per selected C6, all outside physical g(P), forming T_{i−1} of size 4(i−1). The same actual physical pin may be used in several target right C6, because it requests exactly the same unchanged actual LINE factor mapping in each target; this is not a conflict.

### 1. A genuine original source sixflag Qi exists for every root

The original physical point f(p_i) has its two endpoints saturated by the selected two actual source flags, so the remaining four actual source flags must use a physical point C4 on four physical coordinates disjoint from those endpoints, corresponding under injective f to four DISTINCT other actual original point source factors. Existence of such an occupied C4 in every full point physical support with ≤m≤a−2 missing edges was ALREADY proved in #575/#576; no fake high-h source GQ is synthesized.

At each of the four new actual original point factors choose one genuine original incidence LINE neighbor, explicitly AVOIDING all protected original source pins P, all previously used free source LINE IDs F_{i−1}, and the at most three earlier new source LINE IDs at this root. Every genuine original source point factor has d=s+1 authentic LINE neighbors, whereas at most

\[
|P|+|F_{i-1}|+3\le2k+4(k-1)+3=6k-1<d
\]

are excluded when k≤floor(s/8). Thus greedily choose four DISTINCT additional TRUE original LINE IDs for Qi, disjoint from every previous Qi free source LINE ID and all global root pins. Each Qi has six DISTINCT true original incidence flag IDs and source B on left, source A on right; distinct true original source cherry roots yield different Qi.

### 2. A physical occupied right C6 per root avoiding all OTHER source targets

Each selected source root has two existing occupied physical LINE pin images e1,e2 satisfying BL-LOCAL. Earlier [#577](https://github.com/definitely-stable/Mathlab/pull/577) proved a HALF-total count for the canonical two-pin connected physical right C6 template families on the same occupied support E:

\[
C_{\rm adj}\ge(a-3)(a-4)(a-5)/2,\quad
C_{\rm dis}\ge(a-4)(a-5)/2.
\]

Now FORBID every physical pair edge in g(P) outside this root's own two source pins, together with all previously chosen four-per-root FREE target physical pair edges T_{i−1}. The total number of forbidden OCCUPIED physical pair edges, none equal to this root's own e1,e2, is at most

\[
e_i\le(|P|-2)+4(i-1)\le2k-2+4(k-1)=6k-6.
\]

A single extra excluded occupied physical pair edge destroys at most (a−4)(a−5) cycles in the canonical ADJACENT-root-pin family, or at most (a−5) cycles in the DISJOINT-pin family (already counted in parent #583). Hence the two lower bounds for STILL available right connected physical 6cycles containing the root's old two pins are

\[
\begin{aligned}
R_{\rm adj}^{(k)}
&\ge(a-4)(a-5)((a-3)/2-(6k-6))>0,\\
R_{\rm dis}^{(k)}
&\ge(a-5)((a-4)/2-(6k-6))>0.
\end{aligned}
\]

When k≤floor((a−4)/16), the excluded count 6k−6 is strictly LESS than (a−4)/2, so both classes survive all missing physical pair edges AND every cross-root target forbiddance. Pick one surviving actual occupied right C6. Its FOUR extra right physical edges are NOT in g(P) nor any prior selected T_{i−1}. Add exactly those four to T_i. The construction also allows roots with overlapping SOURCE pins: no source factor is ever prescribed to a different edge from its already original pinned g-image.

### 3. One global source permutation, no target/source conflicts

At completion there are k six-incidence-ID Qi, with exactly 4k different actual free original LINE factor IDs outside P and exactly 4k different physically occupied free right target pair edges outside g(P). Prescribe any bijective assignment per root from its four actual free original LINE IDs to its four occupied target right pair edges. The union is an injective partial source-to-edge permutation: no source factor receives two conflicting targets, no different source factors demand the same physical edge and no protected actual original root LINE pin moves. This is a CONSTRUCTED input to the exact partial-permutation consistency/Cayley minimum algorithm ALREADY proved by parent #580.

Its nontrivial original-factor-owner arcs number at most 4k; if c nontrivial directed cycles appear, the shortest number of transpositions is arcs minus c, therefore at most 4k. Every intermediate map is a complete globally injected original LINE source image map onto the SAME occupied physical right support, protecting all authentic source root pins. The same final full g' accepts all k selected genuine Qi by the independently verified original seven GF5 B/A classifier. This finishes the theorem, including duality.

### How many k-subsets are independently repairable?

For each original given full g, total true POINT source cherry count is N=V·binom(d,2). Prior #577 deterministically bounds number of BL-regular original cherries below by G_min >3N/4. Hence EVERY k-subset of those G_min roots admits its OWN one-common-map repair, and therefore

\[
\#(\text{repairable original }k\text{-root selections})\ge\binom{G_{\min}}k,\quad
\frac{\binom{G_{\min}}k}{\binom Nk}
\ge\left(\frac{G_{\min}-k+1}{N}\right)^k.
\]

For large h these are symbolic quantities, NOT giant binomial materializations or fabricated high-order incidence geometry. No claim that the fraction is >1/2 for large k: generally it decays exponentially with k. Likewise no single g' is claimed for ALL good roots simultaneously.

## Independent falsifiers and safety of claims

An additive three-job GitHub-hosted CI validates:

- All dyadic h5..36 and 40/48/64/80 using exact integers and Fractions for k=1,2 and the full k_*(s)=Theta(s) without constructing any imaginary large symplectic GQ. Checks genuine source d and the ≤6k−1 exclusion, ≤6k−6 right forbidden pair edges, strictly positive adjacent and disjoint canonical C6 reserves, >3/4 regular source cherry roots, accurate symbolic k-subset counting and wrong-h/k rejection.
- An independent SIX physical vertex Hamiltonian cycle oracle on actual complete K8, verifying any chosen two-pin rooted physical 6cycle avoiding arbitrary occupied edge forbiddances including more than SIX exclusions is truly physically occupied connected degree2 on six vertices, and never asserting the canonical disjoint-pin C6 subfamily is complete.
- Actual authentic source symplectic W34 GF4, nononto occupied K14 lex/random complete point/LINE maps, both typed original source-root directions: select two original distinct cherry roots and check ONE SAME full corrected original map; literal REPLAY each source-factor image transposition to validate every actual source pin remains fixed and all complete global pair-edge images stay injective and preserve the occupied support; independent historical sevenGF5 source classifier checks every actual six-incidence-ID Qi on the same map. Opportunistically examine THREE actual W34 source roots without applying the h>=5 all-root theorem to finite h=2.
- Actual symplectic original W32 finite dual_zero/lex/S68 schemes source root pairs when finite one-map witnesses exist; no fabricated h=1 universal conclusion.
- Independent original genuine source sixflag Q pairwise distinctness and exact k_arcs−c_cycles minimum from parent #580; rigorous malformed source/physical input rejection.

**No closure of Branch A/B/C:** The theorem concerns an EXISTENTIALLY MODIFIED one-common global map g'_R within O(s) swaps of a given g for any selected Θ(s) locally regular source roots. It proves NEITHER a positive accepted original GF5 motif on the ORIGINAL UNMODIFIED arbitrary fixed f,g nor a universal Ω(s^6) accepted sixflag lower for all such maps. It does not guarantee one g' for the whole ~s^5 regular source-root population, an infinite actual original correlated o(s6) counterfamily, or complete R3/ASET strict upper exponent.

**Acceptance:** maintain Draft until exact FINAL HEAD specialized GitHub-hosted tests, INDEX, Proof Audit, Full Research, genuine independent mathematical referee, parent stack review and postmerge main Research SUCCESS. No registry accepted result promotion based on green dedicated CI.
