# HYP-105 — Registered Research Results

> Generated from pinned research registries; do not edit by hand.
> DOCUMENTED_IN_DRAFT is not independently reviewed/proven mathematics.
> HYP-105 issue [#230](https://github.com/definitely-stable/Mathlab/issues/230) remains unresolved by these registered results.
> GitHub PR HEAD and CI are live data; none are hardcoded here.

## Coverage and acceptance

The table indexes **7 specific results** from **5 research PRs**. It does not claim to catalog all open HYP-105 research PRs.

| Stable claim | Scope / logical mode | Mathematical status | Pinned proof |
|---|---|---|---|
| HYP105-AA4N-QUENCHED-IDENTITY | CONDITIONAL_EXPECTATION | DOCUMENTED_IN_DRAFT | [PR #470 @ 2af74df348a9](https://github.com/definitely-stable/Mathlab/blob/2af74df348a9c0921497757356199a609252f2c2/docs/research/HYP-105-ISSUE230-D6AA4N-QUENCHED-RIGHT-TRANSFER.md) |
| HYP105-AA4N-QUENCHED-LOWER | CONDITIONAL_EXPECTATION | DOCUMENTED_IN_DRAFT | [PR #470 @ 2af74df348a9](https://github.com/definitely-stable/Mathlab/blob/2af74df348a9c0921497757356199a609252f2c2/docs/research/HYP-105-ISSUE230-D6AA4N-QUENCHED-RIGHT-TRANSFER.md) |
| HYP105-AA4O-QUINTIC-IDENTITY | ALL_H_IDENTITY | DOCUMENTED_IN_DRAFT | [PR #471 @ b086566d8be1](https://github.com/definitely-stable/Mathlab/blob/b086566d8be17307b102e7bd89d28d4167af86a6/docs/research/HYP-105-ISSUE230-D6AA4O-QUINTIC-ADVERSARIAL-SWAP.md) |
| HYP105-AA4O-SWAP-IDENTITY | ALL_H_IDENTITY | DOCUMENTED_IN_DRAFT | [PR #471 @ b086566d8be1](https://github.com/definitely-stable/Mathlab/blob/b086566d8be17307b102e7bd89d28d4167af86a6/docs/research/HYP-105-ISSUE230-D6AA4O-QUINTIC-ADVERSARIAL-SWAP.md) |
| HYP105-EICE003K-DIRTY-ANCHOR | DETERMINISTIC_BOUND | DOCUMENTED_IN_DRAFT | [PR #469 @ 73cfebed8042](https://github.com/definitely-stable/Mathlab/blob/73cfebed8042f0f9b6592bd318295fb0bdf69a5b/docs/research/HYP-105-ISSUE230-EICE003K-CLEAN-ANCHOR-CONCENTRATION.md) |
| HYP105-JPKC015-D6-ENSEMBLE | ENSEMBLE_EXPECTATION | DOCUMENTED_IN_DRAFT | [PR #455 @ c02188a4d4f2](https://github.com/definitely-stable/Mathlab/blob/c02188a4d4f2e4e07440c4d7b25fc25c6dd31b3e/docs/research/HYP-105-ISSUE230-JPKC-015-ENSEMBLE-D6.md) |
| HYP105-LT-LOCAL-COUNTEREXAMPLE | LOCAL_CONSTRUCTION | DOCUMENTED_IN_DRAFT | [PR #466 @ 5d2c70e3adeb](https://github.com/definitely-stable/Mathlab/blob/5d2c70e3adeb1779904401f88161c9e71c884892/docs/research/HYP-105-ISSUE230-LOCAL-CYCLE-BARRIER.md) |

## Mathematical statements (registered subset)

### HYP105-AA4N-QUENCHED-IDENTITY — Fixed-right-map exact B/A expected internal charge identity

**Claim:** For every h>=1 and every complete original right-line global injection g, E_f[I_L^(BA,int)(f,g) | g]=p_B(s)*T_g where f is sampled ONCE uniformly from complete original point global injections, p_B(s)=K*C(a-2,4)*3*4!/(K)_5; all genuine original six-incidence sets Q share the same f,g.

**Ordered quantifiers:** forall h (integer h>=1, s=2^h) ; forall g (arbitrary fixed complete globally injected original line map) ; expectation f (one uniformly sampled complete globally injected original point map; fixed same g)

**Model IDs:** MODEL-GQ-ORIGINAL, MODEL-TYPED-GLOBAL-INJECTION, MODEL-ORIGINAL-SIXSET, MODEL-POSITIVE-GF5-SEVEN, MODEL-UNIFORM-GLOBAL-ENSEMBLE, MODEL-BA-INTERNAL-CHARGE

**Claim dependencies:** none registered

**Proof provenance:** [PR #470 @ 2af74df348a9](https://github.com/definitely-stable/Mathlab/blob/2af74df348a9c0921497757356199a609252f2c2/docs/research/HYP-105-ISSUE230-D6AA4N-QUENCHED-RIGHT-TRANSFER.md)

**Review:** NOT_REVIEWED; novelty: NOT_ASSESSED

**Does not imply:** Expectation does not imply all-f individual lower bound. Identity alone does not imply a positive T_g lower bound. No universal inf_(f,g) positive motif result.


### HYP105-AA4N-QUENCHED-LOWER — For every right map, conditional expectation Omega(s^6)

**Claim:** For s=2^h>=8, every complete globally injected right-line map g satisfies E_f[I_L^(BA,int)(f,g)|g]>=3*s^6/65536 for one uniformly drawn complete globally injected left-point map f. Therefore min_g max_f I_L^(BA,int)(f,g)>=3*s^6/65536, NOT min_(f,g).

**Ordered quantifiers:** forall h (integer h>=3, s=2^h) ; forall g (arbitrary fixed complete globally injected original line map) ; expectation f (one uniformly sampled complete globally injected original point map, with fixed g)

**Model IDs:** MODEL-GQ-ORIGINAL, MODEL-TYPED-GLOBAL-INJECTION, MODEL-ORIGINAL-SIXSET, MODEL-POSITIVE-GF5-SEVEN, MODEL-UNIFORM-GLOBAL-ENSEMBLE, MODEL-BA-INTERNAL-CHARGE

**Claim dependencies:** HYP105-AA4N-QUENCHED-IDENTITY

**Proof provenance:** [PR #470 @ 2af74df348a9](https://github.com/definitely-stable/Mathlab/blob/2af74df348a9c0921497757356199a609252f2c2/docs/research/HYP-105-ISSUE230-D6AA4N-QUENCHED-RIGHT-TRANSFER.md)

**Review:** NOT_REVIEWED; novelty: NOT_ASSESSED

**Does not imply:** Does not yield min_(f,g) I_L^(BA,int)(f,g)>0. Does not imply universal seven-class S_s(f,g)>=c*s^6. No Branch A proof nor full risk exponent.


### HYP105-AA4O-QUINTIC-IDENTITY — Exact five-original-point deterministic B/A charge polynomial

**Claim:** For s=2^h>=2 and arbitrary complete right g and left f global injections, I_L^(BA,int)(f,g)=sum_{p,A:|A|=4} w_g(p,A)*chi_B(f(p),f(A)), with w_g counting actual original six-incidence Q sharing exactly five genuine original point factor IDs, nonnegative integer coefficients and one globally coherent pair of maps.

**Ordered quantifiers:** forall h (integer h>=1, s=2^h) ; forall g (any complete original globally injected right-line map) ; forall f (any complete original globally injected left-point map)

**Model IDs:** MODEL-GQ-ORIGINAL, MODEL-TYPED-GLOBAL-INJECTION, MODEL-ORIGINAL-SIXSET, MODEL-POSITIVE-GF5-SEVEN, MODEL-BA-INTERNAL-CHARGE

**Claim dependencies:** HYP105-AA4N-QUENCHED-IDENTITY

**Proof provenance:** [PR #471 @ b086566d8be1](https://github.com/definitely-stable/Mathlab/blob/b086566d8be17307b102e7bd89d28d4167af86a6/docs/research/HYP-105-ISSUE230-D6AA4O-QUINTIC-ADVERSARIAL-SWAP.md)

**Review:** NOT_REVIEWED; novelty: NOT_ASSESSED

**Does not imply:** Nonnegative quintic representation need not have a uniform positive minimum. This is not a degree-two pair-charge lower bound. Does not settle the root Branch A/B/C.


### HYP105-AA4O-SWAP-IDENTITY — Exact transposition-local delta for globally injective B/A charge

**Claim:** For s=2^h>=2 and any fixed complete globally injected f,g and two distinct original point factors u,v, swap the global assigned physical pair labels f(u),f(v). The exact B/A charge difference equals the quintic sum over supports {p} union A intersecting {u,v}; all other terms cancel exactly.

**Ordered quantifiers:** forall h (integer h>=1, s=2^h) ; forall f,g (complete original globally injected point and line maps) ; forall u,v (two distinct original point factors of W(3,s))

**Model IDs:** MODEL-GQ-ORIGINAL, MODEL-TYPED-GLOBAL-INJECTION, MODEL-ORIGINAL-SIXSET, MODEL-POSITIVE-GF5-SEVEN, MODEL-BA-INTERNAL-CHARGE

**Claim dependencies:** HYP105-AA4O-QUINTIC-IDENTITY

**Proof provenance:** [PR #471 @ b086566d8be1](https://github.com/definitely-stable/Mathlab/blob/b086566d8be17307b102e7bd89d28d4167af86a6/docs/research/HYP-105-ISSUE230-D6AA4O-QUINTIC-ADVERSARIAL-SWAP.md)

**Review:** NOT_REVIEWED; novelty: NOT_ASSESSED

**Does not imply:** A one-transposition local optimum need not be globally optimal. Finite adversarial W32 search does not yield all-h global counterfamily. Does not establish a universal lower bound for all maps.


### HYP105-EICE003K-DIRTY-ANCHOR — Original GQ source-anchor dirty-pencil identity and uniform marginal

**Claim:** For genuine W(3,s), fixed arbitrary complete globally injected f,g: D_left=s*sum_q t_f(q) and D_right=s*sum_r t_g(r), each <=2*s*(a-2)*V. For uniformly chosen original nonincident (q,r), P(anchor end-dirty)<=min(1,4*(a-2)/(s*(s+1)))=O(s^-1/2). Probability is over original nonincident endpoint pairs, not over f,g or a conditioned physical-template law.

**Ordered quantifiers:** forall h (integer h>=1, s=2^h) ; forall f,g (complete globally injected original point and line physical-edge maps)

**Model IDs:** MODEL-GQ-ORIGINAL, MODEL-TYPED-GLOBAL-INJECTION, MODEL-TRUE-GQ-ANCHOR

**Claim dependencies:** none registered

**Proof provenance:** [PR #469 @ 73cfebed8042](https://github.com/definitely-stable/Mathlab/blob/73cfebed8042f0f9b6592bd318295fb0bdf69a5b/docs/research/HYP-105-ISSUE230-EICE003K-CLEAN-ANCHOR-CONCENTRATION.md)

**Review:** NOT_REVIEWED; novelty: NOT_ASSESSED

**Does not imply:** Does not prove conditioned four-correlated-anchor capacity C_e=o(s^4). Does not transfer clean-anchor marginal to an accepted original GF5 sixset. Does not establish Branch A or B.


### HYP105-JPKC015-D6-ENSEMBLE — All-h expected genuine D6 original sixset count

**Claim:** For s=2^h (h>=1), with V=(s+1)(s^2+1), N=C(a,2)>=V minimal, independent uniform complete global injections f,g: E[D6]=M6(s)*60*((a)_6/(N)_6)^2 and E[D6]~(16/3)*s^6 as s->infinity. This is an ensemble expectation, not a worst-case bound.

**Ordered quantifiers:** forall h (integer h>=1, s=2^h) ; expectation (f,g) (independent uniformly sampled complete original point and line global injections)

**Model IDs:** MODEL-GQ-ORIGINAL, MODEL-TYPED-GLOBAL-INJECTION, MODEL-ORIGINAL-SIXSET, MODEL-POSITIVE-GF5-SEVEN, MODEL-UNIFORM-GLOBAL-ENSEMBLE

**Claim dependencies:** none registered

**Proof provenance:** [PR #455 @ c02188a4d4f2](https://github.com/definitely-stable/Mathlab/blob/c02188a4d4f2e4e07440c4d7b25fc25c6dd31b3e/docs/research/HYP-105-ISSUE230-JPKC-015-ENSEMBLE-D6.md)

**Review:** NOT_REVIEWED; novelty: NOT_ASSESSED

**Does not imply:** The expectation does not imply inf_(f,g) D6 or S >= c*s^6. Does not close Branch A, B or C and does not derive ASET R2/R3 exponents.


### HYP105-LT-LOCAL-COUNTEREXAMPLE — All-h local obstruction to pathwise GF5 transfer

**Claim:** For every s=2^h>=8, legal complete global typed injections f,g and an induced 18-ORIGINAL-incidence subuniverse exist with five end-clean coordinate-proper 3-edge paths sharing endpoints, ten improper physical C6 and zero original six-incidence accepted seven-GF5 positive counts on that selected subuniverse. This falsifies local pathwise positivity without further global hypotheses.

**Ordered quantifiers:** forall h (integer h>=3, s=2^h) ; exists f,g,I (legal complete globally injected original typed pair label maps and an induced local 18-incidence subuniverse)

**Model IDs:** MODEL-GQ-ORIGINAL, MODEL-TYPED-GLOBAL-INJECTION, MODEL-ORIGINAL-SIXSET, MODEL-POSITIVE-GF5-SEVEN, MODEL-SELECTED-LOCAL-PATTERN

**Claim dependencies:** none registered

**Proof provenance:** [PR #466 @ 5d2c70e3adeb](https://github.com/definitely-stable/Mathlab/blob/5d2c70e3adeb1779904401f88161c9e71c884892/docs/research/HYP-105-ISSUE230-LOCAL-CYCLE-BARRIER.md)

**Review:** NOT_REVIEWED; novelty: NOT_ASSESSED

**Does not imply:** Does not estimate full-model S for the completed injections. Does not refute high-minimum-degree EICE-002 transfer or Root Branch A. Not an infinite global correlated low-S counterfamily for Branch B.


## Sources and remaining obligations

The proof is the pinned original source, not this index. Branch A/B/C requires separate uniform or counterfamily proof.

