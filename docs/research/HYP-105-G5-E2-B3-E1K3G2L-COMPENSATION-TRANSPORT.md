# HYP-105 E1-K3-G2-L — exact signed B/A compensation and original-six-source XOR swap transport

Date: 2026-10-12. Root [issue #230](https://github.com/definitely-stable/Mathlab/issues/230). Stacked Draft child of fully green [PR #384](https://github.com/definitely-stable/Mathlab/pull/384), pinned parent HEAD `5a9044af5b3b67d89b4ac123ccd0a4879376140e`. Neither main nor parent branches are changed. No merge.

## 1. Mathematical audit: the naive compensation proposal is algebraically tautological

The K3-G2-K conditional-expectation theorem constructs SOME right injection g with B-left/A-right count `U(f,g) >= mu_f`; B1-A gave the exact uniform-injection `mu_f = (140+o(1)) s^6` for EACH fixed legal f. Neither proves positivity for EVERY adversarial correlated right g.

Set `S=S_seven(f,g)`, `R=S-U` (the other SIX strictly positive original-incidence GF5 accepted families), `D=mu_f-U` (SIGNED B/A count loss). Then for every legal source mapping and every s, exactly:

```
R - D = (S-U) - (mu_f-U) = S-mu_f.
D <= R+beta*Jcross   IFF   S+beta*Jcross >= mu_f.
```

**Theorem L0 (all-h exact equivalence).** The previously proposed compensation bound is NOT a new inequality if one merely renames D and R; it is IDENTICAL to the desired S+beta J lower bound with a particular `mu_f` threshold. A proof must use new geometry (sixth-order dependencies, incidence origins, source provenance, bounded charging), NOT rely on the equality. It is incorrect to infer universal positive alpha from the identity.

**Finite necessary beta gate.** For every true coherent original W32 labeling m with J>0, the candidate `D<=R+beta*J`, beta>=0, requires `beta >= max(0,(mu_f-S)/J)`. If any legal m has J=0 and S<mu_f, the normalized inequality fails for EVERY beta. For any finite legal corpus F the exact maximum of the rational ratios is NECESSARY for all-label beta, NOT sufficient. In particular a finite corpus without observed violation at beta=0 does NOT prove the global inequality.

This gate differs from K3-G2-J's constant-alpha envelope: the threshold here is the exact **f-dependent** B/A random-injection mean, not an arbitrarily chosen constant multiple of s^6.

## 2. Nontrivial all-h XOR swap-support theorem L1 (all globally coherent injections)

Let `w_f(R)` be the C0 original-right-sixset multiplicity (each unit is one distinct original six-incidence B/A candidate), `T` the physical 6-edge simple 2-factor target supports, and `g` a globally injective original right-source to physical pair map. Swap the WHOLE physical pair labels g(u),g(v) at two distinct ORIGINAL right vertices u and v, obtaining g'. This preserves global injectivity and the original GQ incidence host.

For any original sixset R:
- neither u nor v in R: the right-image physical SIXSET is unchanged;
- BOTH u,v in R: the right-image physical SIXSET is unchanged (the two physical images exchange positions);
- EXACTLY ONE of u,v in R: its right-image set can change.

Hence for ANY original source host, any physical target sixset class, and arbitrary nonnegative w_f, the exact signed transport identity is

```
U(f,g')-U(f,g)
 = sum_{R: |R intersection {u,v}|=1}
     w_f(R) * (1_T(g'(R))-1_T(g(R))).
```

**Proof:** Case split on membership of the two globally swapped original sources in R. If both occur, unordered sixset images are permutation-invariant; if neither, there is no changed physical label. The other cases account for all differences. No random variables, independence, physical-template automorphism division, incidence-column relabeling or asymptotic approximation.

This improves the support of a right ORIGINAL vertex swap over the K3-G2-I source-six-incidence change lemma (which touched all sixsets containing either source). It is a theorem on the B/A six-uniform original right-source hypergraph, NOT a bound on the magnitude of the signed sum. The generic `abs(delta) <= sum_{R: xor} w_f(R)` is valid but far too coarse by itself to prove `Omega(s^6)` for all f,g. For `K=V` complete bijections, any right map may be joined by label transpositions and exact signed deltas telescope; without control of cancellation and positive target compensation, telescoping gives no uniform lower bound.

## 3. Complete exact W32 7-family positive-source ledger

For each legal coherent W32 K6 model, independently compute:

1. C0 exact weighted original B-left source right-sixset hypergraph w_f from the complete eligible left-original selected source sixsets, summing multiplicities only for SIX DISTINCT original right endpoints. Memoize only by immutable complete original LEFT pair-label tuple f (never by an unrelated g).
2. Exact rational `mu_f=(sum_R w_f(R))*70*C(a,6)/C(C(a,2),6)`; for W32 K6 this is `2*sum_R w_f(R)/143`.
3. C0 independent exact accepted B/A source-weight overlap `U(f,g)` under this SAME global right physical pair-label injection.
4. Independent complete B0 enumeration of all **62,370** eligible original incidence sixsets, all SEVEN true positive GF5 family tags `S`, `U` cross-check, other six family counts, strict positive GF5 certified numerator (not full R3).
5. ALL actual original Kikuchi Jcross witnesses `J` via G2-D, with BOTH original source sides included.
6. Exact rational signed deficit `D=mu_f-U`, remainder `R=S-U`, compensated `R-D=S-mu_f`, and necessary beta floor `max(0,(mu_f-S)/J)` for J>0. J=0 and S<mu_f is an explicit no-finite-beta FAIL flag.

**Corpus:** 2 standard baseline source maps, the COMPLETE G2-H 210 single whole-label transposition shell, 7 coherent G2-I best selected correlated anchor/trajectory maps, PLUS 4 all-true-original conditional high/low K3-G2-K maps (lex and correlated left f). Exactly **223 named finite W32 source maps**. It is NOT exhaustion of all (15!)² global factor maps, nor all s. Every finite no-go must carry actual S,J,mu. The source S/GF5 positive classifier is the complete one, NOT W34 partial accepted discovery.

Full-shell regression min S=176, max Jcross=47, min(S-Jcross)=139 is checked for the exact same 210 source-map subset. G2-K high/low real B/A results are checked: lex 131/33 with S=320/101, correlated-left 120/40 with S=245/104. The note of lower mean for RIGHT injections must not be misreported as lower total S.

## 4. Scope and scientific decision gate

**Already proved all-h:** L0 algebraic necessary-equivalence and L1 signed XOR-support identity on original right source-sixsets. Neither gives a numerical all-h lower bound by itself. The exact f-conditioned sixth-order source weights and physical target 2-factor structure are required; C0's generic equal-up-to-two-marginal cube trade demonstrates why only lower-order marginals cannot settle the minimum-over-injection problem.

**The missing all-label theorem remains**
`S_s(f,g)+beta Jcross_s(f,g) >= mu_f` for ALL legal original f,g, or a valid infinite family contradicting every candidate finite beta / unconditional Omega(s6). Future K3-G2-M should seek an actual **typed/source-origin sixth-order signed transfer certificate** bounding the negative gradient part by NEW positive original motifs or bounded-multiplicity actual J sources. A naive union bound over all source swap effects yields an O(s12) per-swap bound from B1-B and is useless for an s6 target, particularly over O(s3) swaps.

## 5. Acceptance

- Independent unit tests directly reconcile C0 physical-source signed delta against full C0 weighted recount and genuine independent B0 seven accepted positive-family census for multiple whole-original right source label transpositions.
- Independent full B0 S/positive GF5, entire original Jcross, and beta-equivalence checks for lex, swapped left and right W32 maps, best G2-I coherent correlation, and four G2-K constructed maps.
- Run complete 223-map ledger **ONCE** in a dedicated GitHub-hosted 25m Contract; pin SHA256 and exact extrema only after a successful first hosted report; inherited full Research must not run the 223 cases redundantly. INDEX/Research/Contract SUCCESS at exact final PR HEAD. Keep Draft pending independent mathematical review, main unchanged, issue #230/#176/#169 OPEN.

## 6. Exact 223-map signed compensation audit — first hosted Contract

The [GitHub-hosted complete Contract #38232996122](https://github.com/definitely-stable/Mathlab/actions/runs/38232996122) **SUCCESS** at original child HEAD `f8a97ebe02716e4128b2e1dbf58332db0663b75a`. Four focused true-original tests PASS, followed by exactly **223** independently full-replayed true coherent W(3,2) global factor maps and **109 distinct fixed left f** hypergraph sources. Each includes exact C0 weighted B/A and independently full 62,370-candidate B0 accepted GF5 seven-family original-sixset count, all Jcross sources, exact rational signed deficit and six-class remainder.

**New precise finite theorem for JUST the named 223 source maps:** exactly 11 have `D=mu_f-U_B/A>0`, yet **ZERO** satisfy `S_seven<mu_f`. Hence in THIS corpus the normalized compensation inequality `D<=S_other` holds at beta=0. That is a complete result on the specified 223 maps, NOT a uniform bound for all W32 physical bijections or all h. This result cannot be turned into positive universal alpha merely from the sampled minimum; full GQ sixth-order correlation remains unknown.

The smallest observed signed compensation slack `S_seven-mu_f` occurs at the explicitly reconstructed genuine G2-I correlated path map `corr:5`:
- S=90, all Jcross=21, true B/A U=44, other six accepted families R=46;
- exact fixed-left B/A injection mean `mu_f=10638/143`;
- signed deficit `D=4346/143`;
- strictly POSITIVE net residual `R-D=2232/143` (~15.61).
- Rest-family true-original split: A-left/B-right 37, B/B-disjoint 6, B/B-overlap 1, C/A 2, C/B 0, D6 0.

At `corr:6`, same f, same U=44 and mu but S=94, Jcross=26, R=50, residual `2804/143`. For independently constructed K3-G2-K low B/A examples: lex U=33, mu=10000/143, S=101, R=68, signed D=5281/143 and net residual=4443/143; correlated-left U=40, mu=10638/143, S=104, R=64, D=4918/143 and net residual=4234/143. Every one of these figures was reproduced from the **same actual original f,g** used for B0 and C0. No simultaneous mixing of separate extremal maps.

For these finite maps the rational necessary lower beta for the candidate `S+beta Jcross>=mu_f` is zero; there were no J=0, S<mu_f cases. **This is NOT a proof that universal beta=0 works.** The report also preserves the 210 shell H-G2 extrema min S=176, max J=47, min(S-J)=139 and checks all four complete K3-G2-K high/low original oracle results.

Exact ordered full source-row SHA256, over (source-name, S, Jcross, B/A, mu, other-six, certified GF5 lower numerator):

`ebfc121f04056fe0b6215633e1f93ab135a306ced5fb92213925f665e672f1d0`.

After this success the extrema, 11 positive deficits, zero below-mean total S, exact rational worst map and digest were PINNED in the dedicated Contract. The final child HEAD must pass all Contract/INDEX/Research again. Root issue OPEN, main unchanged, all prior results remain FINITE versus ALL-h firewall.

## 7. Next K3-G2-M research fork

The data now motivate, but do NOT establish, the potentially strong proposition `S_seven(f,g)>=mu_f` for arbitrary legal ALL-h f,g, which together with B1-A's `mu_f=(140+o(1))s^6` would close Branch A. Focus on actual SOURCE SIXTH-ORDER positivity across seven GF5 families: pair/marginal-only arguments are invalidated by C0's exact 3-cube trade. A useful next step is a typed signed-transport *certificate* showing every negative B/A right swap gradient must be compensated by the gain in other original positive classes or by a globally bounded Jcross obstruction. The sign of an individual gradient is not enough, and a naive telescoping sum of absolute bounds loses the required s^6 scale. Before any universal claim, check exact adversarial correlates and per-GQ projection class source original incidences, and seek a true all-h inequality rather than extrapolating the 223 maps.
