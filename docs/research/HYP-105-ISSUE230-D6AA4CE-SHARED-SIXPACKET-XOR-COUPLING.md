# HYP-105 / #230 — AA4-CE: TRUE-original sixpacket shared physical XOR coupling and pairwise Gram certificate

**Scientific Draft**, strict child of [AA4-CD #604](https://github.com/definitely-stable/Mathlab/pull/604) pinned observed parent head `baee0cefbca7a605e397cb13b4251756d2393bcb`. Inherits historical #602 affine GF(2) parity and #603 rank-two uniform bound, and #604 signed one-sided per-Q physical error. NO accepted-register or `main` edits; issue #230 is `OPEN_WITH_FORMAL_BLOCKER`.

## Decision and scientific frontier

The root issue [#230](https://github.com/definitely-stable/Mathlab/issues/230) requires **every** legal ORIGINAL global pair f,g on TRUE symplectic W(3,2^h) to have `S_s(f,g)>=c s^6` (A), or an explicit infinite original correlated `o(s^6)` family (B), or a qualifying equivalent reduction (C). Positive ensemble mean, finite h=1 center, local kernel and individual repair do NOT suffice. Recent parallel work:
- #597–601 proved per-six-source-Q all-seven selected-GF5 highpass conditional error and abstract cube bounds.
- #602 first proved original physical right-GF2 affine parity and exact original-map-conditioned screening.
- #603 proved rank-one impossible, and uniform all-h sixth-sensitive Walsh norm <=27/32; PR git ancestry was later retargeted, and #604 carries #602 pinned dependent sources explicitly.
- #604 *already* gives sharper per-Q negative-tail true-original seven-GF5 original-center certificates; in W32 lex and S72 both are strictly positive, but not universal.
- **GAP:** existing per-Q calculations do not exhibit the algebraic correlations forced when MANY original Q share exactly the same six source-LINE swap packets. Treating each source Q as an independent right physical draw is forbidden.

Candidate new routes were multi-packet coding joint ranks, global cherry Hall-defect/physical-mask transport, two-sided D6 squarefree trace and fully correlated all-h original counterfamily search. We select a **shared sixpacket right-mask coupling**: elementary but exact, model-faithful, and strong enough to exhibit nontrivial cross-Q pair exclusions without an unproved global positivity assumption.

## All-h AA4-CE-SHARED theorem (every actual correlated original f,g)

For EVERY dyadic `s=2^h`, `h>=1`, let `W(3,s)` be the authentic original symplectic generalized quadrangle. Fix ANY complete globally injective original physical pair images f (POINT) and g (LINE), with arbitrary correlation, same occupied physical support preserved under whole-source swaps, and SIX PAIRWISE DISJOINT packets of TWO true original LINE-factor IDs each:

`P_i=(u_i,v_i), i=0,...,5`.

Fix any SIX DISTINCT TRUE ORIGINAL incidence IDs `Q` whose original source LINE endpoints use exactly ONE of `{u_i,v_i}` in each packet. Its six original LINE endpoints are DISTINCT. The entire original six-incidence set Q remains unchanged across all 64 globally injected complete right maps `g^x` (one whole-factor-image permutation per bit).

Let `e_i^0=g(u_i)`, `e_i^1=g(v_i)`. All twelve actual physical unordered pair edges are **pairwise distinct** because original g is globally injected. Define the right six-edge graph predicate, once for the entire packet family,

```text
R_g(z)=1  iff  {e_0^{z0},...,e_5^{z5}} is a physical
                2-regular six-edge graph on exactly 6 coordinates.
```

Define the **original source orientation** t_Q independently of g by `(t_Q)_i=0` if the original LINE factor used by Q in packet i is u_i, 1 if v_i. The TRUE right physical 2-factor indicator of Q at every **complete global map** g^x satisfies the exact, literal identity

```text
R_Q(x) = R_g(x XOR t_Q).                (CE-SHARED)
```

**Proof:** in g^x the original factor u_i owns the original e_i^{x_i}, and v_i owns e_i^{1 XOR x_i}. The unique original Q factor chosen from that packet thus owns e_i^{x_i XOR (t_Q)_i}. Since all six chosen ORIGINAL incidence IDs and their six source LINE endpoints are fixed, the complete six-edge graph is exactly the one defining R_g(x XOR t_Q). No source IDs are reassigned. All Q use the SAME globally injected map g^x. No independence, averaging or asymptotic assumptions.

This identity is stronger than merely knowing all Q satisfy an affine parity constraint. All physically admissible original Q are XOR TRANSLATES of ONE right mask, even when parity alone would permit additional physically illegal states. The historically positive seven-GF5 indicator I_Q(x) remains only a **subset** of R_Q(x), NOT equivalent to it; original POINT projection, source-GQ patterns and GF5 palette remain essential.

## AA4-CE-PAIR — exact cross-Q two-event physical Gram and exclusion

For any two original sixth-sensitive source-incidence sets Q,Q' on these same packet IDs, put `delta=t_Q XOR t_Q'` and define the single right-mask autocorrelation

```text
A_g(delta) = sum_{z in {0,1}^6} R_g(z) R_g(z XOR delta).
```

At one uniformly sampled complete global swap state x — NOT sampling each Q separately — exact joint physical eligibility is

```text
Pr_x[R_Q(x)=R_Q'(x)=1] = A_g(delta)/64.
Pr_x[R_Q(x)=1] = |R_g|/64.
Cov_x(R_Q,R_Q') = A_g(delta)/64 - (|R_g|/64)^2.
```

For the actual `D_i=∂e_i^0 XOR ∂e_i^1` introduced in prior #602, physical R support lies in the one affine parity coset `D z=beta`. Consequently

```text
D(t_Q XOR t_Q') != 0  IMPLIES A_g(delta)=0.
```

**Hence two original source Q with distinct orientation syndromes cannot BOTH be right-physically admissible at the SAME globally injected g^x**, and therefore cannot both be historical GF5 positive there. For equality of syndromes the exact actual *physical* joint obstruction is still A_g(delta), which can be zero even though parity allows both. This is a genuine deterministic cross-Q restriction absent in individual per-Q highpass estimates.

**Exact quantitative forbidden-pair charge, with NO distributional hypothesis.** Write `H_f(t)` for the positive historical f-eligible source weights defined below and `G(σ)=sum_{t:D t=σ}H_f(t)`; let `H=sum_t H_f(t)`. Then the **sum of products of historical weights over UNORDERED pairs of DISTINCT original Q in DIFFERENT source orientation parity-syndrome classes** equals

```text
F_syndrome = (H² - sum_σ G(σ)²)/2.
```

Every such distinct-Q pair is physically **mutually excluded at every unchanged complete g^x**. The sharper exact physical forbidden cross-orientation charge is

```text
F_physical = sum_{t<u, A_g(t XOR u)=0} H_f(t)H_f(u)
           >= F_syndrome.
```

This sum ranges over DIFFERENT orientation bins, so no diagonal/same-Q products enter. Both are integer identities about a possible original f-eligible source candidate population; **they are not a positive lower for historically accepted motifs**. When R_g is identically zero the physical needed class is empty even within an orientation bin, so this two-bin restriction understates that stronger obstruction.

The nonnegative autocorrelation array A_g is positive definite; its exact unnormalized XOR Walsh transform equals the coordinatewise square of the transform of R_g. This is the classical finite abelian group autocorrelation/Parseval identity. We do NOT claim discovery of general harmonic analysis.

## AA4-CE-MASS — one shared source×physical convolution, all-h

For a fixed original **point** map f and true original source incidence system, select each original physical-left-eligible SIX-DISTINCT-ID Q with exactly one LINE endpoint per packet and an immutable possible one of the HISTORICAL seven positive GF5 source types (the same eligibility/weight rule as #597/#599). Assign its exact historical positive 51-column integer weight w_Q and define

```text
H_f(t) = sum_{Q selected : t_Q=t} w_Q,    t in {0,1}^6.
```

This is a source-side, **f-only** nonnegative 64-bin orientation histogram, with historical `H6(f)=sum_t H_f(t)`. At each original complete g^x the actual weighted historical GF5 selected necessary numerator from sixth-sensitive source Q alone, `W_6(f,g^x)`, satisfies

```text
0 <= W_6(f,g^x)
   <= B_{f,g}(x) := sum_t H_f(t) R_g(x XOR t)
   = (H_f *_XOR R_g)(x).                  (CE-MASS)
```

The RHS uses EXACTLY one fixed global original g and one shared R_g; not one independent image redraw per Q. Its complete 64-map Fourier transform factorizes. For unnormalized `Ftilde(T)=sum_x (-1)^{T·x}F(x)`,

```text
Btilde(T) = Htilde(T) * Rtilde(T),  T subset [6].
```

The exact first two uniform-global-map moments of this **physical necessary upper surrogate** are

```text
mean_x B(x) = H6(f) |R_g| / 64,

mean_x B(x)^2
  = (1/64) sum_{t,u} H_f(t) H_f(u) A_g(t XOR u)
  = (1/64) sum_x B(x)^2.
```

No analogous equality for W_6 is asserted; historic positive GF5 indicators can be strictly below R_Q. In particular this is NOT an independence-based second-moment lower for actual S_s.

For `sigma_Q=beta XOR D t_Q`, the exact historical right-parity necessary class for Q is `D x=sigma_Q`. Thus at fixed x, **only source orientations in one syndrome bucket** can possibly contribute:

```text
B(x) <= sum_{t: D t = beta XOR D x} H_f(t).
```

The number of distinct potentially active classes is at most `2^rank(D)`, not 64 independent source Q draws. If beta is NOT in im(D), the physical mask R_g is identically zero and so is B, for all 64 complete g^x — again only for this particular sixth-sensitive source sector, not for all seven classes / total S.

This structured, exact source×physical convolution and Gram decomposition is a possible input to future GLOBAL cross-packet inequalities, not yet a coercive positive lower on `S_s(f,g)`.

## Prior art, independence and scientific novelty scope

The XOR Walsh convolution theorem, Boolean cube Fourier, physical graph cycle spaces and autocorrelation PSD are classical. Prior original #602 established the affine right parity screen; #603 the rank bound; #604 the per-Q one-sided support bound. This work does NOT rebrand any of those as novel.

The new scoped original-W3 statement is the **COMMON** right physical mask and exact source-orientation convolution/cross-Q Gram for all the true six-incidence Q sharing the same six whole-original-LINE-factor swap packets, while their genuine historical positive GF5 tags are only necessary subsets. This makes the correlation between distinct Q **explicit**, rather than merely preserving their arbitrary dependence as a hypothesis.

## Two separate independent falsification paths

1. **Finite raw physical graph oracle:** 12 distinct physical edges of K6 form six actual pair-image packets, one full physical g; enumerate all 64 graph states independently, all translated orientations, and direct pairwise intersections. Check auto-correlation by both brute force 64² and unnormalized Walsh squares; verify parity-inequivalent orientations have exactly ZERO simultaneous acceptance.
2. **Genuine original symplectic W32:** lex/S72 complete point f and LINE g; enumerate original left-eligible 351/301 source Q (historical source-tag classifier) and their exact original six-incidence IDs; ALL 64 complete original right maps; independently evaluate literal per-Q 2factor physical degree and historical seven-GF5 tags and check the original shared physical mask `R_g(x XOR t_Q)` for EVERY Q and x. The weighted source H histogram is unchanged when the complete original g is adversarially reversed; direct per-Q physical upper B is exactly independently computed 64-bin XOR Walsh convolution. Signed joint autocorrelation has an independent direct sum and numerical rank/syndrome tests. Reject overlapping source packets, invalid edge injections and malformed Q.

No synthetic high-h symplectic geometry is used. W32 is a finite falsifier only; the all-h theorem follows from the explicit source packet relabeling identity. Exact 64-bit code arithmetic and all-GitHub-hosted three-job CI, no external optimizer.

## Scientific acceptance / nonimplications

This is a precise **PARTIAL** all-h true-original proof, NOT root Branch A/B/C. We do **not** prove that positive right physical eligibility leads to positive GF5 acceptance, nor that a one-sided U reservoir cannot be completely erased by source/global-map correlations. `B` is an upper surrogate, so it provides **no universal lower bound** on unchanged (W(f,g)), no infinite correlated original o(s^6) counterfamily, no full R3/ASET exponent, and no accepted model-equivalent Branch C reduction. Every all-h statement is for genuine complete globally injected f,g and SIX distinct actual original incidence IDs. Root #230 remains OPEN_WITH_FORMAL_BLOCKER. Keep Draft pending exact head specialized/INDEX/Proof Audit/Full Research, independent mathematical review and actual ancestor branch Git ancestry repair.
