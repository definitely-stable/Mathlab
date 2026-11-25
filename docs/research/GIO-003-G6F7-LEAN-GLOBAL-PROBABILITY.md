# GIO-003 / G6-F7 — одна настоящая глобальная вероятностная мера в Lean

**Research:** [#793](https://github.com/definitely-stable/Mathlab/issues/793). **Frozen parent:** [G6-F6 Draft #822](https://github.com/definitely-stable/Mathlab/pull/822), exact SHA \`f5ee0ce8fdd4a55d6561f129f5c1fb4bc26d9716\`, specialist F6 7/7 SUCCESS, inherited F4 Lean and INDEX SUCCESS. At initiation full Research #45563550802 was still executing \`lent-001-foundation\`; its final status must be verified separately. New work is a separately stacked DRAFT PR; no changes to main/ancestry or closure of #793.

## 1. Why F7 matters: existing F5/F6 do NOT prove a joint event probability

The previous formal stages established the correct finite **conditional algebra** for shared ORIGINAL owner competitors (F5) and the exact univariate real integral plus combinatorial actual competitor multiplicities (F6), but did NOT construct the joint probability measure. A proof claiming \`Pr(S⊆Min_J)\` from only these two stages would have a genuine unproven probability/Fubini bridge, even though the paper argument in G6-F3 is mathematically plausible.

The fully specified actual random experiment must assign **one** independent continuous uniform \`U_i∈[0,1]\` to each original source-flag owner i, once for the **whole** graph. Re-sampling a competitor each time it appears as a neighbor of a different desired owner is INVALID. Desired owner local-minimum winner events are correlated if they have common neighbors. Only the *priority coordinates of distinct external competitors* are independent, conditionally on the already fixed target priorities.

The exact probability measure is mathematically standard prior art, as are Caro–Wei local-minimum selection and the ordinary graph C6 supersaturation used in F1. F7's contribution is reproducible kernel formalization **for the concrete Mathlab source-flag owner semantics** and an explicit statement of the remaining bridge, NOT a new global probabilistic graph theorem.

## 2. One ACTUAL real uniform marginal and finite global array

Let \`U = volume.restrict (Ioc (0:ℝ) 1)\`. The interval has Lebesgue measure one; hence \`IsProbabilityMeasure U\` is **proved**, not declared as a custom axiom.

For any arbitrary finite ORIGINAL owner ID type \`ι\`, define the one global sample space \`Ω=ι→ℝ\` with the finite product probability law

\`\`\`
   P_ι = Measure.pi (fun _ : ι => U).
\`\`\`

This one law is shared by **ALL owners**: \`ω i\` is the unique priority of source-owner i. With Mathlib \`measurePreserving_eval\` and \`iIndepFun_pi\`, kernel-check that:
- P_ι is a probability measure, including empty ι;
- EACH owner-coordinate marginal \`(ω↦ω i)_*P_ι\` equals U exactly;
- ALL original owner-coordinate random variables are mutually independent under one joint P_ι.

The last property does NOT imply that local-minimum WINNER events, which reuse competitor coordinates, are independent.

## 3. Exact JOINT competitor event under fixed target thresholds

Fix any finite competitor owner subset K and any **deterministic** threshold \`t_j\` for each competitor. The genuine event under the ONE global law is

\`\`\`
  { ω | ∀ j∈K, ω j>t_j } = K.pi (fun j=>Ioi(t_j)).
\`\`\`

For the single genuine global measure P_ι, Mathlib's exact product cylinder set theorem yields

\`\`\`
  P_ι({∀ j∈K: ω j>t_j})
      = ∏_{j∈K} U(Ioi(t_j)).
\`\`\`

For \`0≤t_j≤1\`, the exact marginal Lebesgue calculation gives \`U(Ioi(t_j))=ENNReal.ofReal(1−t_j)\`; hence

\`\`\`
 P_ι({∀ j∈K:ω j>t_j})
     = ∏_{j∈K} ENNReal.ofReal(1−t_j).
\`\`\`

This is a **real probability identity**, not F5's purely algebraic comparison of conditional factors. Critically, a competitor owner j is represented by ONE coordinate \`ω j\` regardless of how many target owners it threatens. To obtain F5's factor \`1−max_{i∈S∩N(j)}t_i\`, the above holds with \`t_j\` chosen as that actual maximum AFTER fixing the desired target priorities \`t_i\`. The formal theorem is intentionally for fixed thresholds; constructing the joint conditional distribution when those thresholds depend on target owner coordinates is a separate substantial step.

## 4. TRUE MULTIVARIATE Fubini on the SAME global probability space

For ANY finite index type and ANY family \`f_i : ℝ→ℝ\`, Mathlib \`integral_fintype_prod_eq_prod\` on the actual P_ι proves

\`\`\`
    ∫_{ω∼P_ι} [∏_i f_i(ω i)]dω
           = ∏_i∫_{t∼U} f_i(t)dt.
\`\`\`

Here \`∫_{t∼U}(1−t)^d dt\` is mathematically the same interval integral as F6's \`∫₀¹(1−t)^d dt\`; in Lean it is explicitly converted through \`intervalIntegral.integral_of_le\` and evaluated by the verified Mathlib power integral. Thus one obtains a genuine **SINGLE-GLOBAL-ARRAY** expectation, for any degree function \`d:ι→ℕ\`:

\`\`\`
 E_{ω∼P_ι} ∏_{i∈ι}(1−ω i)^(d_i)
       = ∏_{i∈ι}1/(d_i+1).
\`\`\`

This is stronger than F6's product of *separate integrals*: it now states and proves a genuine joint expectation under a shared probability law, and Fubini plus independence of the actual PRIORITY COORDINATES are mathematically justified by Mathlib.

## 5. Exact kernel coverage and STRICT scientific boundaries

Nine Lean statements in \`formal/gio003_f4/Gio003F7.lean\`:
1. \`global_law_is_probability\` — true all-owner global probability measure.
2. \`coordinate_is_uniform\` — exact uniform coordinate marginal.
3. \`all_priority_coordinates_independent\` — real all-coordinate independence under ONE global P_ι.
4. \`global_competitor_fixed_threshold_probability\` — actual joint cylinder event probability at any fixed thresholds.
5. \`uniform_one_priority_tail\` — exact uniform tail \`1−t\` for any \`t∈[0,1]\`.
6. \`global_competitor_fixed_threshold_exact\` — joint external-competitor priority event probability as a product of exact uniform tails.
7. \`global_priorities_fubini\` — actual multivariate product integration over ONE common owner priority measure.
8. \`global_one_priority_power_moment\` — exact global marginal degree moment.
9. \`global_actual_joint_target_power_expectation\` — actual joint target degree moment for ALL finite source owner index types.

**Absolutely not yet formalized:** the FULL J-local-minimum event \`E={∀i∈S,∀j∈N(i):ω i<ω j}\` with \`S\` an ORIGINAL J-independent target owner set; its conditional probability given all target \`ω i\` using the external competitor event from §3; the F5 conditional shared-competitor pointwise lower bound combined with that true joint event via Fubini/Tonelli; and precise identification of the external finite competitor counts with \`SimpleGraph.degree\`. F7 would be **incomplete and misleading** if it claimed the final \`Pr(E)≥∏(1/(deg_J(i)+1))\` is already one formal Lean theorem.

Source girth8 quadratic Moore defect/typed Loewner PSD, original FULL/CORE physical book triple injection, original six-source-ID BBo inverse, actual D6 and unrestricted incidence T3, dependent GF5 ASET and human academic refereeing remain separate obligations. G6-F3's source-CONDITIONAL paper may use the known probability inequality, but this PR only kernel-proves new factual portions explicitly listed above.

## 6. Acceptance and next material step

Files added ONLY:
- \`formal/gio003_f4/Gio003F7.lean\`, compiled by Lean 4.34.0 with exact Mathlib SHA \`5ed2965256430c3649e86755f9576b54eca72435\`, no proof holes or added axioms;
- this strict mathematical proof/coverage note;
- \`.github/workflows/gio003-g6f7-lean-one-global-probability.yml\`, GitHub-hosted real kernel, nine \`#print axioms\`, artifact and all-error fail-closed gates.

**Acceptance:** nine real kernel statement SUCCESS on exact final HEAD; inherited F4/F6 specialist plus INDEX and full Research SUCCESS; separate COMMENT-only rigorous internal review of the precise probabilistic event and measure assumptions. Keep Draft, issue #793 OPEN, no changes/merges to main or ancestors. The next step after this acceptance is **formal conditional disintegration for actual local-minima event** (not numerical tables), finally obtaining the full one-global priority probability bound in a single Lean theorem.
