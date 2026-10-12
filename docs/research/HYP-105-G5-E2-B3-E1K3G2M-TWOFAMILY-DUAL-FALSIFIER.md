# HYP-105 E1-K3-G2-M — exact dual original-sixsource transfer and two-family adversarial gate

Date 2026-10-12. Root [issue #230](https://github.com/definitely-stable/Mathlab/issues/230). Parent **Draft** [PR #385](https://github.com/definitely-stable/Mathlab/pull/385), pinned accepted exact HEAD `adf466f7093da91d10ea968ed2a45168d6d82739` (all dedicated Contract and INDEX green; verify Research independently). Do not merge or alter main. Maintain #230/#176/#169 OPEN.

## 1. Three competing routes from K3-G2-L, and selected gate

L's exact 223-legal-map W32 ledger found 11 genuine B-left/A-right (B/A) count deficits relative to the fixed-left random-injection mean `mu_f`, but the other six positive GF5 accepted original-six-incidence families always compensated. The smallest genuine observed total-S minus mean was `2232/143` at correlated `corr:5`, S=90, Jcross=21, B/A=44, A-left/B-right (A/B)=37. This suggested two-family compensation:
```
P2:  U_B/A(f,g) + U_A/B(f,g) >= mu_f     (ALL h, ALL legal f,g).
P7:  S_seven(f,g) >= mu_f                 (ALL h, ALL legal f,g).
```
P2 implies P7 because all other five accepted class counts are nonnegative. But P2 is STRONGER and can be false while P7 remains true, and neither was established by the 223 cases. A genuine P2 counterexample would only refute the two-class proof STRATEGY, not P7, all-h S=Omega(s^6), Branch A/B or any ASET exponent.

Alternative routes considered and explicitly NOT silently accepted:
1. The K3-G2-L rest-minus-deficit identity `(S-U)-(mu-U)=S-mu` is a TAUTOLOGY. No geometric inequality follows just by grouping.
2. B1-B's single original-right swap `|ΔS|=O(s^12)` cannot be naively telescoped over `Theta(s^3)` source-label transpositions to obtain an `Omega(s^6)` all-label lower bound.
3. The C0 rank-six source weighting has identical <=2 marginals under a cube trade with changing six-target overlap. Design 1/2 marginals cannot by themselves settle all-label P2/P7.

Chosen K3-G2-M: prove original-GQ dual weighted sixth-order identity, then perform COMPLETE W32 P2/P7 falsifiers on the existing complete true-source corpus plus a new genuine correlated search explicitly minimizing the SIGNED two-family margin. Do not claim exhaustive minimization or use partial W34 target discovery to prove absence.

## 2. New all-h dual-original-sixsource theorem M1 (EXACT)

Fix a legal *balanced* original GQ W(3,s) incidence host E subset P x L, globally injective unordered physical-pair label f for P and g for L (on the SAME original E). Define the original incidence transpose `E^op={(l,p):(p,l) in E}` and dual source model `m^op=(L,P,E^op,g,f)`. This is a genuine original GQ dual, not a right/left physical template-only swap.

Let `w_f^right(R)` be the original C0 weighted B-left source-sixset multiplicity at a SIXSET R of original right line sources (counting six DISTINCT original incidence supports). Let `w_g^left(Q)` denote the corresponding B-left weighted source hypergraph on the DUAL original incidence host, now with g as dual LEFT labels and six original points Q as dual right vertices.

The exact equalities for ALL h (with potentially unused physical pair edges K>V) are:
```
U_B/A(f,g)  = sum_{R subset L, |R|=6} w_f^right(R) * 1_T(g(R)).
U_A/B(f,g)  = sum_{Q subset P, |Q|=6} w_g^left(Q) * 1_T(f(Q)).
S_seven(m^op) = S_seven(m) [the seven-class union is dual-symmetric].
```
Here T consists of six DISTINCT physical unordered pair edges forming six-coordinate degree-two simple two-factors (one 6-cycle or two triangles). The first identity is the previously proved C0 weighted B/A reduction. The second follows by transposing each ORIGINAL incidence (p,l)->(l,p) within the same six-distinct-incidence source support and exchanging f,g. This gives an involution and a bijection between original A/B and dual B/A supports, without any 6! normalization or inconsistent physical labels. The seven-class invariant follows from dual symmetry of the accepted original A/B, B/A, C/A (dual), C/B (dual), B/B, and aligned D6 classes. Each event is a true positive GF5 certified original family. These identities do NOT imply a nonzero MINIMUM of their two-family sum.

## 3. Exact full B0 + 2 independent C0 source oracles (negative-proof integrity)

For every tested W32 K6 true coherent source map:
- Independently build original weighted RIGHT six-source B/A hypergraph with source f and the DUAL weighted LEFT six-source B/A hypergraph with source g. Memoize only by the exact immutable original f and g physical maps respectively, never substitute one for the other.
- Evaluate both physical six-target overlaps `U_B/A` and `U_A/B` with original C0 exact weighted overlap engine (on original and transposed actual original host).
- Independently enumerate **ALL 62,370** B0 eligible original six-incidence candidates and classify **ALL seven** positive GF5 accepted classes, and independently enumerate dual B0 original supports. Both sides must match BOTH weighted C0 overlaps and entire seven-S exactly; otherwise FAIL.
- Compare exact rational `mu_f=(sum_R w_f(R))*70*C(a,6)/C(C(a,2),6)` against `U_B/A+U_A/B` and full `S_seven`.
- A NEGATIVE P2 certificate requires strict `U_B/A+U_A/B < mu_f` on a real legal globally coherent (f,g), with complete original C0/B0/dual recount and exact `S_seven - (U_B/A+U_A/B)` other-five family counts. A strictly negative P7 certificate additionally requires `S_seven<mu_f`. Report P2 and P7 separately.
- Positive finite scores cannot prove all-label P2 or P7.

Two finite corpora: (1) all 223 prior named legal W32 maps (2 baselines + entire 210 single original whole-pair swap shell + 7 correlated original states + 4 real deterministic K3-G2-K high/low maps); (2) a seeded **NONEXHAUSTIVE** adversarial two-sided sequence of WHOLE source-vertex pair-label transpositions, using K3-G2-I's exact original-sixset delta tags to score proposals. A selected move is accepted as negative evidence ONLY after COMPLETE B0/C0 dual recount. The candidate score is the TRUE `U_B/A+U_A/B-mu_f` in exact rational arithmetic; it is not an approximation. Selected path's Jcross is counted only for interpretation; all verified positive class family supports and physical maps are exact. Stop upon a fully certified P2 failure.

## 4. Acceptance and proof scope

- Independently test true dual transposition involution (incidences and full physical source labels), true 62370 original and dual candidates, true full S invariant and exact individual class swap; standalone complete small corpus; deterministic independently replayed short correlated two-sided search; invalid-input fail closed.
- Dedicated 25-minute GitHub-hosted Contract runs the full 223 original-dual source corpus and the sampled finite adversary ONCE. Pin exact finite minima, violation witnesses and SHA256 only after hosted initial success; inherited Research job must NOT redundantly repeat full corpus.
- INDEX and Research SUCCESS at exact final PR HEAD; keep Draft pending independent mathematical review. Root issue OPEN, main unchanged.

## 5. Branching criterion for next K3-G2-N

If true finite P2 counterexample exists, document exact original f,g whole source pair maps, the two physical B/A original sixsource masses, rational mu, all seven actual accepted family counts and the necessary five-class compensation; P2 is refuted as a universal proof method, P7 remains open unless S<mu also occurs. Follow with an all-h source-origin class-specific theorem for at least the positive five residual classes.

If all tested finite maps pass P2, study SOURCE-ORIGINAL sixth-order signed compensation on arbitrary f,g; neither 223 finite samples nor correlated greedy success establishes all-h P2. Challenge any candidate bounds with original GQ projection-fiber class G2-C and C0's equal-small-marginal adversaries. The objective is an actual all-h inequality or an infinite legitimate coherent counterexample, not an asymptotic claim from small exact cases.

## 6. Hosted exact finite result, 2026-10-12

[Specialized GitHub-hosted Contract #38235039675](https://github.com/definitely-stable/Mathlab/actions/runs/38235039675) **SUCCESS** on original child HEAD `6d0351dd76d2368cedd96c42c0bac8a15f73ae08`. All focused original GQ involution, C0 weighted and complete B0 dual-source tests passed, followed by the **entire 223-source original+dual** W32 full enumeration and the **deterministic 3-anchor correlated adversary**.

**Complete 223 TRUE coherent-source labels:** 109 distinct complete original left f, 114 distinct complete original right g, independently verified both original and dual complete 62,370-original-incidence left-candidate seven-positive-GF5 B0 enumerations per mapping, independent original and dual C0 source-sixset physical-target overlaps, and exact random-right `mu_f`. Among these 223 named maps:
- **0** violations of the STRONGER two-family proposed bound `U_B/A+U_A/B>=mu_f`;
- **0** violations of the full `S_seven>=mu_f`;
- minimum TRUE two-family margin in the named corpus is `945/143`, for previously verified correlated original `corr:5` with `S=90, U_B/A=44, U_A/B=37, other five classes=9, mu_f=10638/143`.

**Independent sampled adversary:** three globally coherent anchor maps, five alternating left/right whole-original-source vertex transposition selections each, eight deterministic distinct proposed swaps each = **120 exactly delta-scored candidates**. All **18** initial+selected maps were INDEPENDENTLY full B0 ORIGINAL and DUAL plus both C0 ORIGINAL weighted-source recounts, with zero two-family violations and zero full S violations. The smallest found two-family margin was **`757/143`** on the first actual full-replayed move from `corr:5`: swap WHOLE physical original **left** labels of sources **(13,14)**; then
```
S_seven = 86
Jcross = 22
U_B/A = 36
U_A/B = 39
remaining five = 11
mu_fixed_left = 9968/143
two-family margin = 757/143 > 0
full-S margin = 2330/143 > 0
```
All figures refer to the SAME legal W(3,2) original f,g source map (not mixing minima of independent labelings). This is **STRICT finite positive evidence**, not an all-W32 or all-h proof of the two-family inequality. In particular none of the 120 unselected/selected candidate proposals may be called independently full-certified except the 15 SELECTED moves; 120 proposals were precisely delta-scored, not exhaustively searched over all possible permutations.

SHA256 certificates:
- Ordered exact 223 original-source corpus `cdabb909755ea9f1cc5f83874b73c880937cb50039ea5843329e460d87b0f40a`.
- Ordered 15 selected-path source snapshots `5db98923e6769b8398cf97d400e7f87520275e333bab9538732d031313d22835`.
- Hardest newly observed globally coherent whole-labeling hash `e5c3f92068d6221f44cbb77fbae5dc95000144a0c495d216a48cdf3b047bfd4a`.

The initial hosted success was followed by an update to the **dedicated Contract** pinning all 3 hashes and exact numerical extrema. The final child HEAD must independently pass dedicated Contract/INDEX/full Research before accepting, and remain Draft pending separate mathematical review.

## 7. Next all-h mathematical target

The two-family bound `U_B/A+U_A/B>=mu_f` would imply `S_seven>=mu_f=(140+o(1))s^6` and hence close Branch A if it could be proved for ALL actual coherent original f,g. No such proof is available; exact W32 full and correlated finite witnesses cannot establish positivity for arbitrary s.

The ORIGINAL/DUAL weighted rank-six hypergraphs are not independent because the right source weights of the dual depend on the SAME adversarial g that indexes the physical B/A overlap. Any true all-h proof must bound their coupled sixth-order signed behavior, potentially using the seven GQ projection-fiber classes in K3-G2-C rather than one-/two-marginal identities. C0's 3-cube equal-two-marginal trade is a strong warning against lower-order transport or naive averaged bounds. Focus next on a non-tautological all-h source-origin coupling inequality or an infinite admissible f,g counterexample; avoid more evidence-only searches without a new symbolic certificate.
