# HYP-105 / issue #230 — AA4-BQ: exact all-seven inverse-switching flux and seventh-difference no-go

**Scientific Draft, strict child of AA4-BP [PR #585](https://github.com/definitely-stable/Mathlab/pull/585), frozen corrected parent HEAD `49ab7cf43497261f07eafd6e18b693184ad7be5b`. Independent parallel [PR #586](https://github.com/definitely-stable/Mathlab/pull/586) proves linear-in-s many-root repair via a different budget and does not contain a reverse-transport theorem. Earlier D6-AA4-O [PR #471](https://github.com/definitely-stable/Mathlab/pull/471) ALREADY proves the ORIGINAL B/A **quintic point-side** single-pair-swap source-supported gradient and a true W32 counterexample to using one-swap local stationarity as a global optimization certificate. Do not claim the degree-6 seven-class LINE-side theorem is its rediscovery. #574 has fixed-pair all-seven factorial source collision moments; #580 exact constrained Cayley swap metric; #585 all-h k-root moved-map positive original GF5 guarantee. Root #230 remains OPEN_WITH_FORMAL_BLOCKER, no accepted claim promotion or main edits.

## Why inverse switching is the next actual obstacle

AA4-BP proves that for every original full correlated fixed pair (f,g), for every k-subset of its >75% regular true original point cherry roots, one nearby **CHANGED** opposite map h has at least k accepted B/A source-Q. The root Branch A is about **S_seven(f,g)** at the UNCHANGED g. Radius accessibility is not a pointwise positivity theorem. A correct reverse-switching argument needs to account for predecessor multiplicity and exact support locality, **before** any attempt to transfer a lower bound to the origin.

## Theorem BQ-SEVEN: six-local genuine ORIGINAL seven-GF5 switching and 7th difference zero

For any genuine original symplectic W(3,2^h) (h>=1), any two complete globally injected typed factor-to-physical-edge maps f,g, fix f and the entire occupied LINE physical support E=im(g). For any m disjoint pairs of DISTINCT actual ORIGINAL LINE source factor IDs \((u_i,v_i)\), i=1..m, let \(\tau_i\) swap the WHOLE currently assigned two-coordinate physical pair edge images between those factors. These swaps commute, preserve complete injection and E, and form a genuine Boolean cube of 2^m different full line maps \(g^A\), A subset [m]. Define the **full historically positive seven-GF5 original-sixflag** count

\[
S(g^A)=D6+U_{B/A}+U_{A/B}+U_{C/A}+U_{C/B}
       +U_{B/B,overlap}+U_{B/B,disjoint}
\]

on the **same** fixed f and genuine original incidence identifiers, ALL correlations retained. For every A subset[m], define the finite-difference/Möbius coefficient

\[
D_A S(g)=\sum_{B\subseteq A}(-1)^{|A|-|B|}S(g^B).
\]

**Exact all-h theorem**: whenever \(|A|\ge7\), \(D_A S(g)=0\). In fact the same holds separately for EVERY individual true-original six-flag Q accepted-indicator \(1_{Q\text{ historically GF5 positive}}(f,g)\), even when Q changes GF5 class across cube vertices: a Q has six DISTINCT original incidence IDs and hence involves **at most six DISTINCT original LINE factor images**. Of seven source-ID-disjoint swap pairs at least one misses all factors in Q, and the Q-indicator is independent of that bit. Its alternating sum cancels exactly. Summing over ALL genuine original Q retains zero. Thus for any dimension m the restriction of the **full seven-class function** to that original LINE transposition cube is a Boolean multilinear polynomial of degree at most SIX:

\[
\boxed{S(g^A)=\sum_{T\subseteq A,\ |T|\le6}D_T S(g).}\tag{BQ-DEG6}
\]

For independent Bernoulli(p) toggles of these **commuting** source-factor pairs (ONE resulting global complete map, not independent resampling per six-Q), an **exact** rational generating identity follows:

\[
\boxed{\mathbb{E}_{A\sim Bern(p)} S(g^A)
=\sum_{T\subseteq[m], |T|\le6}p^{|T|}D_T S(g).}\tag{BQ-CUBE}
\]

Every identity applies with the historical SEVEN original GF5 tags, not merely B/A, all h, any physical holes, arbitrary fixed f,g. Overlapping transpositions are explicitly EXCLUDED; their toggles do not commute and the cube proof is not applicable. This is a structural exactness theorem, NOT a uniform sign on any derivative or a positive pointwise all-h lower.

**Class-specific tighter possible degree:** an individual six-Q source LINE factor profile may have only 3,5 or 6 distinct actual source LINE IDs. This theorem states the safe all-seven common cutoff SIX and does not assume all seven classes use six distinct factor IDs. Any higher order mixed derivatives vanish on disjoint swap directions.

## Theorem BQ-INVERSE: exact reversed many-root switching incidence inequality

Keep same genuine original f,g,E, with V original opposite factors, and the set \(\mathcal G\) of G true original BL-regular source point-cherry roots of g provided by #577 (>3/4 of N=V*binom(s+1,2)). For any \(2\le k\le\lfloor(s+1)/6\rfloor\), put r=4k and let \(B_r(g)\) be the FULL Cayley ball of whole original LINE image transpositions of radius at most r, with the same E. For each full globally injected h in that ball define \(R_{\mathcal G}(h)\) as the number of **distinct original good cherry roots in \(\mathcal G\)** for which h already admits at least one genuine six-DISTINCT-original-incidence historical GF5 B/A sixflag through the exact rooted two flags.

AA4-BP provides, for EVERY k-subset A of \(\mathcal G\), at least ONE h_A in B_r(g) with A subset the set of roots witnessed by h_A. Hence without ANY assumption of independence or unique root->map assignments,

\[
\boxed{\binom{G}{k}
\le\sum_{h\in B_r(g)}\binom{R_{\mathcal G}(h)}{k}
\le\sum_{h\in B_r(g)}\binom{S_{BA}(f,h)}{k}.}\tag{BQ-HALL}
\]

The second inequality uses a TRUE originality fact: each B/A-positive original six-Q has a UNIQUE twice-used original POINT factor and EXACT two rooted incidence flags, hence determines exactly ONE genuine original point-cherry root; therefore \(R_{\mathcal G}(h)\le S_{BA}(f,h)\) with no fake multiple root credit. The first inequality is a straightforward *reverse incidence* double count; no assumed injective choice A->h_A. It is valid all dyadic h>=5, independently of the central original g's accepted count.

The number of complete occupied-support line maps in the ball depends ONLY on V and r, not f,g,E, and is exactly

\[
\boxed{|B_r(g)|=\sum_{j=0}^{\min(r,V-1)}
\left[{V\atop V-j}\right],}\tag{BQ-BALL}
\]

where the bracket is an UNSIGNED Stirling number of the first kind (classical formula for Cayley transposition distance V minus cycle count). This is a genuine all-h mathematical identity; the reproducibility helper caps huge V for feasibility and **does not** enumerate astronomical high-h permutation sets. The mean bound obtained by division by this often enormous ball cardinal is a bound on neighborhood averages, NOT on its center. The strictly valid extremal corollary is that SOME repaired h in the ball supports at least k roots. #585 already proves this constructively; #BQ is an exact inverse-count accounting of all potential h, not a stronger center lower bound.

## Theorem BQ-NOGO: quantitative and logical blocker for center extraction

**An abstract full-permutation countermodel shows that even much STRONGER local repairability + degree-six cube locality do not logically imply a positive center**: let n>=2 and E consist of n distinct (abstract) physical pair-edge labels; assign them bijectively to n original source factor IDs. Give G artificial 'root' labels an accepted predicate \(1\{g(0)=e_0\}\) simultaneously. For EVERY input full bijection g, swapping source factor 0 with the current owner of edge e0 (0 or 1 transposition) makes all G artificial roots simultaneously accepted. Yet for any initial g with g(0)!=e0, the center accepts ZERO. This artificial acceptance predicate depends on one source factor image, so has Boolean cube degree at most ONE for every collection of disjoint source transpositions. Thus **radius-1 universal simultaneous k-root accessibility, reversible Cayley connectivity and degree<=6 all FAIL as abstract implications to strictly positive original center**.

It is deliberately NOT a genuine symplectic W3 or true-original GF5 counterfamily and does NOT disprove root Branch A. Rather, it proves precisely that those three classes of assumptions in isolation are insufficient; a valid proof must exploit *additional source-specific signed/correlated flux or physical/GQ structure*, e.g. control of negative six-Q boundary events on **the original map**.

**Magnitude-only swap-gradient limitation:** if a proposed unchanged-map transfer uses only \(|S(g\tau)-S(g)|\le L\) and #585's guarantee S(h)>=k at radius <=4k, then triangle inequality gives S(g)>=k−4kL. Since historical motif counts are integers, any nonconstant S has global swap-Lipschitz constant L>=1 and the bound is nonpositive for k>=1. Even this is not a counterexample to pointwise positivity itself: it blocks this *particular* naive uniform absolute-gradient argument. Signed and instance-dependent boundary inequalities remain open.

## Independent reproducibility and prior-art guard

Versioned Python original GF5 cube/partial-oracle implementation and six-group independent tests:
- Genuine ORIGINAL W32 symplectic `S72` full K6 complete f,g. Enumerate 62,370 original six-incidence left projection candidates ONCE using historically accepted original source construction; evaluate 8 separate full globally injected right maps from THREE pairwise disjoint actual original LINE factor-image transpositions; independently reclassify ALL seven GF5 classes and verify exact 3-dimensional Möbius reconstruction and Bernoulli(p) mean for several exact rational p. Baseline cross-check against original `seven_census` literal ORIGINAL accepted Q set.
- Genuine ORIGINAL W32 `lex`, SEVEN pairwise disjoint original LINE factor image swaps on 14 of 15 source factors. Verify independently for EVERY one of 62,370 actual left-sixset Q that it meets at most SIX of the seven source swap pairs, and evaluate sampled REAL genuine-original Q in all 2^7 complete globally injected maps with the independent full historical GF5 classifier: exact 7th derivative zero.
- Exhaustively enumerate full symmetric groups n=2..7 and compare EVERY Cayley ball size to independent cycle-count distance and the unsigned Stirling recurrence. No fake W3.
- Finite exact reverse Hall covering enumeration, detect missing prescribed original root subsets, different full maps sharing same accepted roots, no injectivity assumption; explicit arbitrary good set subset count.
- Independent exhaustive S5 countermodel: EVERY complete permutation center is within one factor-image swap of a map accepting ALL G artificial roots, while EXACTLY 96/120 input centers have zero artificial accepted roots. This is labeled a proof-method countermodel, NOT an original GQ six-motif construction.
- Invalid original six-incidence IDs, repeated source factor swap indices, incomplete injected maps, malformed cube and GF5 classification guards.

The Cayley metric and unsigned Stirling counts are classical (e.g., Diaconis, Petersen, and standard combinatorics references); finite cube Möbius inversion and degree-of-dependence locality are likewise elementary. The **new scoped** artifact is the explicit true-original *all-SEVEN* GF5 source-sixflag disjoint original-factor switching cutoff together with an exact *many-root* inverse incidence/ball accounting and a formally separated method limitation. No claim of global research novelty without an external literature audit, peer review or original root Branch A/B/C.

**Next honest root-facing step:** derive **signed**, original GQ-restricted lower bounds on the full seven-class switching flux or on the sixth-order source-factor interaction tensor that survive adversarially correlated typed global image maps. Simply repeating local repair abundance, low Boolean degree, averaged counts, or magnitude-only global Lipschitz estimates will not solve the unchanged-map root #230.

Keep Draft, require exact-final-head specialized/INDEX/Proof Audit/full Research and independent mathematical referee and acceptance of #585 ancestor chain. #230 remains OPEN_WITH_FORMAL_BLOCKER.
