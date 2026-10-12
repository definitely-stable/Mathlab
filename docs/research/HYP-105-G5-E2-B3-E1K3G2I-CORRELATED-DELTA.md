# HYP-105 E1-K3-G2-I — exact six-incidence swap locality and correlated W32 Hall adversary

Date 2026-10-12. Root [issue #230](https://github.com/definitely-stable/Mathlab/issues/230). Stacked **Draft** child of [PR #381](https://github.com/definitely-stable/Mathlab/pull/381), accepted parent HEAD `4ad9303d065910bdec38ccd6d33e58f5a3bce6db` (Contract/INDEX/Research SUCCESS). Main untouched, no merge. Original universal seven-family bound `S_s=Omega(s^6)`, all-h charge `Jcross<=K*S_s`, and full R3/ASET exponent all remain OPEN.

## 1. Motivation

K3-G2-H established complete original-two-column Hall injections across ALL 210 single whole-pair physical-label transpositions of the fixed W(3,2)/K6 lex map (105 left and 105 right), but not correlated transposition sequences. Its proven finite extremal values were `min S=176`, `max Jcross=47`, `min(S-Jcross)=139`, and minimum witness degree 3, all for potentially different labelings. Those values **must not** be combined into a fictitious single source map.

K3-G2-I attacks a correlated original GQ source-label configuration with BOTH `f` and `g` modified by two or more complete source-vertex label transpositions. A single mutation changes all occurrences of that original source vertex in the global labeling; no independently selected incidence-column labels are allowed.

## 2. Exact arbitrary-host swap-locality lemma

Fix ANY original finite incidence host `H=(P,L,E)`, an injective unordered-pair labeling `f:P->E(K_a)`, `g:L->E(K_a)`, and two distinct original vertices `u,v` of one color. Let `f'` or `g'` be obtained by exchanging the ENTIRE two original pair labels at `u,v`, with the other half and E fixed. For every original set `I subset E` with six distinct incidences, denote by `tag_{f,g}(I)` the exact accepted seven-GF5 motif tag or `None` when ineligible. Then:

```
If no incidence of I is incident on u or v in the changed factor,
tag_{f,g}(I) = tag_{f',g}(I)    (or tag_{f,g'}(I)).
```

**Proof:** For each of the six original incidences in I, both its original endpoints are unchanged and none is swapped on the changed half. Thus its two unordered physical pair labels, each physical half 2-regular degree profile, original endpoint multiplicity partition, full physical six-column dual, D6 alignment/connectedness and B/B original-overlap class are identical. The exact accepted tag therefore cannot change. No stochastic or asymptotic assumption enters.

**Exact delta algorithm in W32:** B0 independently identifies the complete **62,370** original six-incidence candidates with eligible LEFT physical degree-two profiles. A right swap leaves this eligible candidate universe unchanged; only candidates containing a column incident on u or v on the right can change accepted membership/tag. A left swap can change eligibility itself: enumerate BOTH old and new 62,370-element universes and rescore the full union of candidates touching u or v; retain unmodified tags outside the touched region. Every tag/class GF5 weight is recomputed exactly for touched supports, never estimated. Verify that the old/new untouched eligible universe agrees (the lemma) and the full class-weighted GF5 numerator is conserved by exact tagged-set updates. The W32 engine performs a complete fresh B0 seven_census with full original-sixset witness set after every SELECTED greedy move.

This is a mathematically exact finite-state maintenance method for the model and an arbitrary-host support lemma; it does **not** confer a computational complexity improvement theorem independent of the host, a universal all-h enumeration algorithm, or an all-h lower bound on S.

## 3. Finite correlated two-sided adversarial probe (not exhaustive)

Start at W(3,2)/K6 lex. Three deterministic, explicitly allowed two-sided seeds exchange LEFT and RIGHT source whole-pair labels:
- left (1,14), right (2,11);
- left (3,9), right (1,8);
- left (0,14), right (0,14).

For each seed, run SIX alternating side-move decisions (LEFT, RIGHT, LEFT, RIGHT, LEFT, RIGHT) with EIGHT sampled distinct whole-label transpositions each. The seed `20261012` governs the deterministic proposal stream, not a probabilistic guarantee. Compare all **144** candidate transitions by exact incremental `S_seven-Jcross` score, with stable tie breaking, then independently replay each of the 18 selected states plus 3 initial two-sided anchors by FULL complete B0 enumeration and full G2-H exact accepted S Hall. Every reported matching uses all true positive targets and independent maxflow/mincut plus augmenting paths. For every selected source map, `51^6 R3 >= sum_{seven distinct original sixsets} accepted positive GF5 class floors` is a strict model-specific lower numerator, NOT full R3.

The greedy method may miss adverse states, cut obstructions with S>J, or other useful witnesses. Unselected proposals are scored exactly by the delta locality lemma but are NOT asserted to have passed any Hall check. A selected Hall failure may be called a **finite counterexample to capacity-one two-original-column overlap charging** only after full independent B0 plus Hall deficit `|X|-|N(X)|=Jcross-maxflow>0`. A successful selected map is finite positive evidence only.

Report pins actual initial and selected paths, true S and Jcross, complete Hall deficits, min source degree, accepted positive GF5 lower numerator, physical-label SHA256 and ordered trajectory digest. No claim that all 210 single swaps, all 11025 left/right paired choices, or all (15!)² source-label pairs were exhausted in this new probe.

## 4. Acceptance

- New independent differential unit tests for four left/right swaps, exact affected-original-support lemma, full accepted B0 target equality and GF5 numerator equality, complete-target Hall agreement and global pair bijection invariants.
- Re-run a two-step three-proposal fixed-seed correlated smoke probe twice and check deterministic identical records.
- A dedicated GitHub-hosted 25m Contract runs the deterministic default adversarial probe **once**, with fail-closed result coverage and math status flags; full Research must not rerun 144-case experiment.
- All three checks (dedicated Contract, INDEX, complete Research) must be SUCCESS on the **exact child PR HEAD**; maintain Draft until independent mathematical review. Do not touch main or close #230/#176/#169.

## 5. Next K3-G2-J proof fork

If a complete independent selected state produces a deficient Hall subset X, publish exact original source incidence supports, matchable-target neighborhoods and cut deficit, and investigate permissible alternative capacity or charging relation (without claiming all-h Branch A false). If this finite search finds no obstruction, prioritize a structural symbolic `S_s >= alpha*s^6-beta*Jcross` positive-seven-family surplus inequality or a formal all-h counterexample to it; a richer finite search alone cannot establish either. A companion attempt at `Jcross<=K*S_s` needs all-h bounded preimage multiplicity and positive accepted target existence for every legal globally coherent f,g. Only BOTH all-h inequalities would yield `S_s >= alpha/(1+beta*K) * s^6`.
