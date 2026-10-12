# HYP-105 E1-K3-G2-N — exact Johnson sixset decomposition and fifth/sixth-order proof gate

2026-10-12. Root [issue #230](https://github.com/definitely-stable/Mathlab/issues/230); stacked on Draft [PR #386](https://github.com/definitely-stable/Mathlab/pull/386) exact parent HEAD `294ce9c1fc688374631d58d91b20ffa8d62ad9c2`. **Main stays unchanged; #230/#176/#169 remain OPEN**. This note concerns ORIGINAL incidence sixsets, not signed-event counts or physical automorphism orbits. The two C0 weights are recomputed on the ORIGINAL host and its genuine dual, and the complete independent seven-GF5 B0 census remains authoritative.

## 1. Why M does not close the proof

K3-G2-M established the true exact dual original-sixsource expressions for B-left/A-right (`U_BA`) and A-left/B-right (`U_AB`). Its dedicated Contract/INDEX/Research are all **SUCCESS at final HEAD**: [38235992182](https://github.com/definitely-stable/Mathlab/actions/runs/38235992182), [38235992189](https://github.com/definitely-stable/Mathlab/actions/runs/38235992189), [38235992146](https://github.com/definitely-stable/Mathlab/actions/runs/38235992146). It certified 223 original maps and 18 selected/anchor adversarial models with zero P2 violations, without enumerating all W32 bijections.

The stronger proposal `P2: U_BA(f,g)+U_AB(f,g)>=mu_f`, with `mu_f=H_f*70*C(a,6)/C(K,6)`, is still **OPEN for arbitrary legal f,g and all s=2^h**. If established for every injection, it implies `P7: S_seven>=mu_f=(140+o(1))s^6` and gives one route to Branch A. Conversely, a P2 failure need not refute P7; the five other true positive families may rescue it.

We now analytically isolate the **exact** first two Johnson harmonics of the physical sixset indicator, then identify the residual ranks 3–6 that an actual GQ-specific compensation proof must control. No assumptions of independence of f and g are made.

## 2. All-a theorem N1: target rank zero, rank one and rank two

Let `a>=6`, `K=C(a,2)` physical pair-label vertices, `M=C(K,6)`, and `T_a` the `70*C(a,6)` genuine simple six-edge 2-factors on exactly six physical coordinates. Regard `t=1_{T_a}` as a function on the Johnson slice `J(K,6)` (all unordered sixsets of physical K_a pair edges). Its inner product is the **unnormalized** sum over all `M` sixsets. Define `p=|T_a|/M`.

Its zeroth lift is the constant `t_0(S)=p`. Since every physical pair edge belongs to exactly `28*C(a-2,4)` targets, `t` is a 1-design and its first Johnson lift is **identically zero** for every `a>=6`.

For two distinct physical pair-edge labels e,e', their common-target multiplicity is
- `c_adj=7*C(a-3,3)` if e,e' share a physical coordinate;
- `c_dis=14*C(a-4,2)` if they have disjoint physical endpoints.

Let `lambda_2=C(K-4,4)` and `q=p*C(K-2,4)`. Then the *unique harmonic second-rank coefficient* is

```
h2(e,e') = (c_adj-q)/lambda_2  [adjacent];
            (c_dis-q)/lambda_2  [disjoint].
t2(S) = sum_{unordered {e,e'} subset S} h2(e,e').
```

**Proof:** After removing the rank-zero constant and identically zero rank-one lift, the pair marginal at each `{e,e'}` equals `c_type - q`. On a Johnson harmonic of rank two, the down/up-incidence operator has eigenvalue `C(K-4,4)`. Dividing obtains `h2`; the pair-orbit population identity gives `sum_{e' != e} h2(e,e')=0`. Consequently, its rank-two lift is orthogonal to ranks 0 and 1 and reproduces the rank-two marginal. This is a Johnson-scheme identity, **not** a new universal GQ lower bound.

For `A(S)=sum_v C(deg_S(v),2)` adjacent unordered pair-edge pairs among six physical edges, the **explicit all-a formula** is
```
t2(S) = A(S)*h2_adj + (15-A(S))*h2_dis.
```
Thus *only* the exact pair-coordinate adjacency statistic contributes to physical target rank two. In particular `a=9` is a 2-design and `t2=0`; the actual GQ alphabets of interest are `a=6` for W32 and `a=14` for W34, so the accidental `a=9` cancellation is not a proof opportunity.

At `a=6`, all values are exact:
```
K=15, M=5005, |T|=70, p=2/143
h2_adj=-1/110, h2_dis=2/165
t2(S)=(60-7*A(S))/330
||t0||²=140/143, ||t1||²=0, ||t2||²=42/11
||t_ge3||²=70-140/143-42/11=9324/143.
```
For every a, `||t2||²=lambda2*[a*C(a-1,2)*h2_adj² + 3*C(a,4)*h2_dis²]` and `||t_ge3||²=|T|-|T|²/M-||t2||²`. The last number is **not assumed small**.

## 3. All-host identity N2 and rigorous sixth-order obstruction test

For a fixed ORIGINAL left injection f, let `w_f(R)>=0` count DISTINCT ORIGINAL B-left six-incidence supports over each original right-sixset `R`; for any legal original right injection g, push `w_f` to physical sixsets with **zeros on unused physical pair labels**, obtaining `W_{f,g}` on `J(K,6)`. It is NOT an independent random hypergraph and cannot be simplified to an ordinary pair-design.

The exact identity, valid for any rank-six weighted source and hence the actual GQ at ALL h, is
```
U_BA(f,g) = <W_(f,g), t>
          = mu_f + C2(f,g) + C_ge3(f,g)
mu_f      = (sum_R w_f(R))*p
C2        = sum_R w_f(R) * t2(g(R))
C_ge3     = <W_(f,g), t3+t4+t5+t6>.
```
The **original dual** gives the same identity for `U_AB` with `w_g^dual` and original f in the right position, but its uniform-dual mean `mu_g^dual` is generally **not** the same as `mu_f`. Do not replace either actual count by an unrelated mean.

Write `E_W_ge3=||W||²-||W0||²-||W1||²-||W2||²` using exact one-/two-point source marginals after zero-padding. Orthogonality yields the rigorous Cauchy–Schwarz inequality
```
C_ge3² <= E_W_ge3 * E_t_ge3.
U_BA(f,g) >= mu_f + C2(f,g)
             - sqrt(E_W_ge3*E_t_ge3).
```
Thus the *sufficient, fully checkable condition* `U_AB + C2 >= sqrt(E_W_ge3*E_t_ge3)` proves P2 on any family where it holds **uniformly**; failure of this sufficient condition does not refute P2. Conversely, if a genuine original map violates P2, then necessarily `U_AB+C2 < sqrt(E_W_ge3*E_t_ge3)`. This narrows the analytical obligation to SOURCE-GQ constraints on the high-order component, and cannot be replaced by a norm bound using total mass alone.

For source moment computation `M=C(K,6)`, `lambda1=C(K-2,5)`, `lambda2=C(K-4,4)`, `m=sum_S W(S)`, `d(e)=sum_{S contains e}W(S)`, `b(e,e')=sum_{S contains both}W(S)`:
```
W0 = m/M
h1(e) = [d(e)-W0*C(K-1,5)]/lambda1
h2(e,e') = [b(e,e')-W0*C(K-2,4)
             -(h1(e)+h1(e'))*C(K-3,4)]/lambda2
E_W0=m²/M; E_W1=lambda1*sum_e h1(e)²;
E_W2=lambda2*sum_{e<e'} h2(e,e')².
```
These are exact rational **orthogonal** projections, not numerical fits, and hold with unused physical labels when V<K.

## 4. Original GQ finite falsification and strict limits

The executable rank-0..6 decomposition enumerates **ALL 5005** physical K6 sixsets, projects exactly with Fraction coefficients, verifies the level-j down-kernel, reconstruction, mutually orthogonal lifts and Parseval (total energy 70). Independently compare the computed rank-two lifted values with the **closed adjacency/disjoint orbit** formula on all 5005 sets, plus the explicit pair-orbit general-a formulas for a=6,9,14 and additional a.

Each source certificate computes original B/A weighted overlap both from C0 direct target membership and all seven target spectral levels, verifies `C0=mu_f`, `C1=0`, exact `C2`, and checks the squared high-order CS bound with **independently computed SOURCE norms**. Repeating this on the genuine original GQ dual certifies A/B without exchanging physical templates on the wrong source.

The already-known 3-cube trade from C0 consists of two **abstract** nonnegative 6-uniform source hypergraphs with identical 0/1/2 source marginals but target overlaps differing by exactly 1. N adds an exact rank certificate: their spectral correlations through levels 0/1/2 coincide, while ranks 3..6 account for precisely the unit difference. **This proves low-degree data alone cannot control the full overlap for arbitrary rank-six sources; it does not construct an actual GQ incidence counterexample.**

Dedicated hosted Contract runs the focused finite theorem/oracle tests and a two-original-map report (W32 lex, the previously published harder original correlated + left (13,14) state), not the 223-map M corpus again. The complete independent B0 seven-family and C0 dual recount is performed for each reported original map. No finite success is promoted to all-h P2/P7 or `S=Omega(s^6)`.

## 5. Follow-on proof gate K3-G2-O

The first mathematical task after hosted green N is to obtain a **GQ-specific coercivity statement on ranks 3–6**, exploiting original projection-fiber classes of G2-C and simultaneous dependence of w_f and w_g on the same incidences. A useful target is an inequality of the form
```
U_AB(f,g) + C2(f,g) + C_ge3(f,g) >= 0
```
with a genuine positive or nonnegative *geometric* lower certificate, **not** a rearranged tautology. The exact N orthogonal decomposition states what must be controlled but is NOT such a certificate. Any alternative finite adversarial result must preserve whole original labels and independently recheck B0/C0. A W32 counterexample to P2 (if found) does not automatically disprove seven-family P7.

Acceptance: exact-head Contract/INDEX/Research SUCCESS, regression on complete K6 Johnson spectrum and dual C0/B0, independent mathematical review; keep stacked PR Draft, maintain root issues OPEN, do not merge to main.
