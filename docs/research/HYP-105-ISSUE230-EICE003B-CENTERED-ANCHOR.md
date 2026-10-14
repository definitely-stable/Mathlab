# HYP-105 / issue #230 — EICE-003-B: centered original-anchor covariance and conditional energy

**Status: RESTRICTED_THEOREM_C / OPEN_WITH_FORMAL_BLOCKER.** Strict research-only child of [PR #451](https://github.com/definitely-stable/Mathlab/pull/451) pinned at `4cf76d7b84378c01654185d88e7e6e180a5f98c7`. No root Branch A/B, no ASET exponent, no numerical extrapolation.

## 1. Precise original-GQ scope

Retain the true typed original W(3,s), s=2^h, original globally injective f:P→E(K_a) and g:L→E(K_a), their original incidence IDs, unique GQ projection q--ell--p--r for every nonincident original (q,r), and an arbitrary **normalized reversal-invariant** probability measure mu over physical nonbacktracking length-three paths. Select only coordinate-proper paths with both original endpoint factors present, original (q,r) nonincident, and end-clean anchor f(p)∩f(q)=∅ and g(ell)∩g(r)=∅. The total eligible **subprobability** is P≤1; no independence between f,g and no assumption about normality of endpoint labels.

Define pi_f(q,r,x1), pi_g(q,r,y1) and common endpoint marginal t(q,r) as in EICE-003-A, with zero mass outside the true eligible path support. Let C be the number of true nonincident *end-clean* original (q,r), and n=a-2≥4. Since proper endpoint coordinates are f(q)={x0,x3} and g(r)={y0,y3}, **x1 never belongs to f(q)** and **y1 never belongs to g(r)**. Therefore the conditional first-inner left coordinate lives on exactly the n allowed labels U_q=[a]\\f(q), right on V_r=[a]\\g(r). The true anchor coordinate pairs f(p)⊂U_q and g(ell)⊂V_r are each of cardinality 2 because the original anchor is end-clean.

## 2. B0 — exact reduced-support Parseval, improves A3

For each eligible original (q,r), let t=t(q,r), and define

    Rf_perp = sum_(q,r) sum_(x in U_q) (pi_f(q,r,x)-t(q,r)/n)^2,
    Rg_perp = sum_(q,r) sum_(y in V_r) (pi_g(q,r,y)-t(q,r)/n)^2,
    T2 = sum_(q,r) t(q,r)^2.

Then **exactly**, for every f,g and mu,

    A_f+A_g = (2/n)*T2 + Rf_perp+Rg_perp,       (B0)
    Rf_perp,Rg_perp≥0.

Proof: on each n-element set U_q, ∑_x pi_f=t, and expansion of the centered square cancels both cross terms; identical for g. The full-a residuals from A3 are larger by 2T2*(1/n-1/a); the artificial variance from prohibited endpoint coordinates is now removed. Nothing is estimated probabilistically.

## 3. B1 — centered original-anchor compensation inequality

For each original eligible endpoint fiber i=(q,r), define the signed **centered anchor coordinate vector**

    b_f(i,x)=1[x∈f(p(i))]-2/n, x∈U_q,
    b_g(i,y)=1[y∈g(ell(i))]-2/n, y∈V_r.

Its sum on each fiber is 0 and its exact squared Euclidean norm is 2-4/n. Define

    Γ_f = sum_i sum_(x∈f(p(i))) pi_f(i,x),
    Γ_g = sum_i sum_(y∈g(ell(i))) pi_g(i,y),
    Δ_f = Γ_f - 2P/n,   Δ_g = Γ_g - 2P/n.

**Exact covariance identity** (unlike the earlier loose scalar energy):

    Δ_f = < pi_f-t/n, b_f >,
    Δ_g = < pi_g-t/n, b_g >.

By the original-anchor D1 internal-only definition and reversal-invariance,

    theta_I <= 2(Γ_f+Γ_g)
            = 8P/n + 2(Δ_f+Δ_g).                    (B1-direct)

Cauchy–Schwarz across both typed sides yields

    (Δ_f+Δ_g)^2 <= 2*C*(2-4/n)*(Rf_perp+Rg_perp).

Hence the **new exact all-h necessary bound**

    theta_I <= 8P/n
             + 4*sqrt[C*(1-2/n)*(Rf_perp+Rg_perp)]. (B1)

If C=0, every eligible path and theta_I vanishes. For all n≥4, the formula is valid. This **eliminates T2 entirely**: the EICE-003-A suggestion to prove both C*T2≤K and C*(R_f+R_g)≤1/32 is not logically required. T2 may be arbitrarily large within a chosen reversible measure and need not enter this proof route.

For comparison the old full-a centered bound (still exact, but a weaker center) is

    theta_I <= 8P/a + 4*sqrt[C*(1-2/a)*(R_f+R_g)].

These full-a and reduced-support estimates are NOT guaranteed to be pointwise ordered as numerical upper bounds, because both the baseline and residual change. Use their minimum if desired.

## 4. B2 — weighted conditional chi-square alternative

For t(i)>0 let k_f(i,x)=pi_f(i,x)/t(i) be the true conditional first-inner-coordinate distribution on U_q, and analogously k_g on V_r. Define

    Q_f = sum_i t(i) * sum_(x in U_q) [k_f(i,x)-1/n]^2,
    Q_g = sum_i t(i) * sum_(y in V_r) [k_g(i,y)-1/n]^2.

These are nonnegative, and can be calculated without zero divisions from

    Q_f = sum_(i:t(i)>0) [sum_x pi_f(i,x)^2/t(i)] - P/n,
    Q_g = sum_(i:t(i)>0) [sum_y pi_g(i,y)^2/t(i)] - P/n.

Weighted Cauchy–Schwarz on t(i) gives

    theta_I <= 8P/n
             + 4*sqrt[P*(1-2/n)*(Q_f+Q_g)].        (B2)

Unlike B1, B2 carries no explicit C factor. It measures average per-anchor deviation rather than squared endpoint masses. **There is no assumption that B2 is always tighter than B1.**

## 5. B3 — exact positive original middle-incidence correction

The preceding B1-direct estimate remains an upper bound because it used a union bound. There is an EXACT, more informative equality on the SAME true ORIGINAL source, without any spectral estimates.

For an eligible oriented proper physical 3-path define `L1={x1 in f(p)}`, `L2={x2 in f(p)}`, `R1={y1 in g(ell)}`, `R2={y2 in g(ell)}`. Let `L=L1 union L2` and `R=R1 union R2`. These refer to the TRUE unique ORIGINAL GQ anchor q--ell--p--r, not invented source incidence adjacency.

Set

    Jf = Pr_mu[eligible AND L1 AND L2],
    Jg = Pr_mu[eligible AND R1 AND R2],
    JLR = Pr_mu[eligible AND L AND R].

All three are nonnegative. By exact inclusion-exclusion and reversal-invariance

    theta_I = 2*Gamma_f + 2*Gamma_g - Jf - Jg - JLR
            = 8P/n + 2*(Delta_f+Delta_g) - D,       (B3)
    D=Jf+Jg+JLR >= 0.

These are EQUALITIES, not upper estimates. Original source provenance supplies additional structure: in the event L1 AND L2, properness ensures x1 != x2 and the anchor f(p) has EXACTLY two physical coordinates. Therefore the physical middle edge of the 3-path has left pair {x1,x2}=f(p); by global injectivity its **actual ORIGINAL middle source point equals p**. Dually R1 AND R2 forces its actual ORIGINAL middle source line to equal ell. If both occur, the middle edge carries precisely the ORIGINAL incidence (p,ell). No illicit additional GQ 6-cycle, wrong physical-to-original vertex identification or extra GF5-positive motif is claimed.

**Proof significance:** the exact correction D can compensate an otherwise large positive centered covariance. B1 and B2 discard D and so can fail even when the actual internal blocking mass is small. A future structural proof can either bound the *signed* covariance or show that the positive correction D is necessarily large whenever covariance concentration occurs, using true middle-incidence provenance and the seven approved GF5 source profiles.

## 6. New strict sufficient targets (still OPEN)

By EICE-002, there exists a coherent paired-diagonal G* of positive s^4 density and Ω(s) active min degree for all large s, and by the conditional Opus R/projection closure if S=o(s^6) its eligible end-clean mass would have to carry theta_I=1-o(1).

Thus a possible completion route is to prove: for every globally injected f,g and all sufficiently large s, **there exists one admissible paired G*** (with the required *fixed* density/min degree) such that for some η>0

    C*(Rf_perp+Rg_perp) <= (1-η)^2/16,             (TARGET-B1)

or the alternative independent sufficient target

    Q_f+Q_g <= (1-η)^2/16.                         (TARGET-B2)

Since P≤1, n→∞ and the prefactor (1-2/n)≤1, either would force theta_I≤1-η+o(1), and conditional on a separately validated uniform R theorem would yield root Branch A. A direct stronger target is

    Δ_f+Δ_g <= 1/2-η,                             (TARGET-COV)

because B1-direct then forces theta_I≤1-2η+o(1). All three targets are **OPEN**; especially TARGET-COV is a signed contraction whose cancellations may be more accessible than any positive-semidefinite energy bound.

A path law concentrated on one eligible path and its reverse can make t highly concentrated even though the original endpoint pair and GQ source are legitimate; thus reversal invariance **alone** never bounds the old C*T2 quantity. This does not falsify the stationary law on high-degree G* or the root conjecture.

## 7. Executable evidence and acceptance

- Reuse exact true ORIGINAL W32 lex/reverse/S68/S72 / W34 original symplectic incidence fixtures, and whole-incidence paired G* source selections.
- The EICE-003 exact original path tensor now verifies B0, B1 direct covariance, B1 squared rational bound, B2 weighted chi-square, B3 exact inclusion-exclusion with ORIGINAL middle-source IDs, and original full-a A4 using no floating-point operations. Low s can have conditioned-on-survival NB law; strict stationary requirement is independently fail-closed.
- The new independent regression recomputes B3 original middle-incidence double-anchor corrections, source-anchor covariance and coordinate-centered residual by enumerating all a-2 legal internal coordinates on each original eligible endpoint fiber and checks exact equality, rather than trusting the implemented aggregated tensor formulas.
- No finite W32/W34 result is advertised as proof for every h. CI tests establish implementation regressions, while B0-B2 have separate algebraic all-h proofs.

**Next proof gate EICE-003-C:** investigate the **signed centered anchor covariance-minus-correction kernel** 2*(Δ_f+Δ_g)-D using the real GQ incidence spectrum, the globally injective endpoint maps and physical coordinate-block matching constraints, with dedicated adversarial symplectic-spread/Baer original fixtures. If spectral cancellation cannot be proved, seek a true globally coherent counterfamily to TARGET-COV (not just a single finite W32 map). No merge of research Draft PRs without independent proof review.
