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
