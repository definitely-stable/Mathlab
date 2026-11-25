# GIO-003 G6-F6 — точный интеграл приоритета и степени конкурентов в Lean

**Исследовательский контекст:** [#793](https://github.com/definitely-stable/Mathlab/issues/793), parent [G6-F5 Draft #821](https://github.com/definitely-stable/Mathlab/pull/821) at frozen SHA \`24525676366ad701cec11df4d78ce65a946f83db\`. Parent F5: nine REAL kernel proofs, inherited F4 kernel, INDEX and full Research **ALL SUCCESS**. F6 is a NEW STACKED DRAFT; no change to ancestors or main, issue stays OPEN.

## 1. Critical mathematical missing link and prior art

G6-F5 kernel-proved the conditional shared-competitor algebra (for any arbitrarily many target original source-flag owners and any overlaps):
\`\`\`
  product_j [1−max_{i∈S∩N(j)}t_i]
  ≥ product_j product_{i∈S∩N(j)}(1−t_i).
\`\`\`
It correctly avoids independence of target winner events. But obtaining the actual joint probability lower bound also requires a real probability space on the *single shared global array* \`(U_v)_{v∈V(J)}\`, conditional independence of **distinct competitor priorities** after fixing the targets, rearranging products into degree powers, and integrating independent target priorities. The result follows from standard uniform-product probability and a basic one-dimensional calculus identity, but neither a Mathlib named theorem nor informal prose proves that all probabilistic identifications have been checked in Lean.

**F6 focuses on the two deterministic universal bridges whose verification is independently useful:** the real Lebesgue/interval integral for EVERY natural degree and the exact original-competitor incidence count powering the per-target factors. The objective is meaningful extra kernel coverage, while maintaining a formally honest remaining probability-model requirement. Caro–Wei estimates and classical local-minimum random priority methods are previous mathematical art, NOT a newly discovered probability theorem.

## 2. All-degree real uniform integral — ACTUAL Lean calculus

For every natural integer \`d≥0\`, the proof of

\`\`\`
          ∫₀¹ (1−t)^d dt = 1/(d+1)
\`\`\`

is in \`formal/gio003_f4/Gio003F6.lean\`, theorem \`uniform_target_power_integral\`. It uses only Mathlib theorems \`intervalIntegral.integral_comp_sub_left\` (measure-preserving reflection \`t↦1−t\`) and \`intervalIntegral.integral_pow\` (exact Lebesgue/interval integral of \`t^d\`). It neither samples finite values nor assumes the desired integral as an axiom. \`d=0\` works and returns 1. Every degree is universally quantified: no finite maximum graph degree is fixed.

\`all_target_priority_moments\` extends this identity under **finite multiplication** to an arbitrary Finset of original owner targets with an arbitrary source-degree function:
\`\`\`
  product_{i∈S} [ ∫₀¹ (1−t)^(d_i) dt ]
       = product_{i∈S} 1/(d_i+1).
\`\`\`
\`uniform_target_moment_positive\` and \`all_target_moments_positive\` separately kernel-prove strict positivity, including the empty target set. These are exact ordinary real integrals, not an informal integration step.

**What these identities do NOT state:** equality between product of univariate integrals and the probability of the *actual* shared-source event. That requires an actual measure/independence/Fubini theorem, not just algebra on real numbers. The product is the correct deterministic RHS after a future probabilistic identification.

## 3. True shared competitor incidence → per-target degree

Let S be an arbitrary finite target original-owner set, K an arbitrary finite set of other owner IDs and Adj(j,i) any decidable original J adjacency. A fixed competitor contributes factor \`(1−t_i)\` iff it actually conflicts with owner i, and factor 1 otherwise. Then the universal identity

\`\`\`
 product_{j∈K} (if Adj(j,i) then 1−t_i else 1)
     = (1−t_i)^(#{j∈K:Adj(j,i)})
\`\`\`

is proved by **finite induction** (\`product_if_eq_pow_filter\`). It does not require any neighbor sets to be disjoint or any independences of the desired owner events.

Combining with the exact finite product commutation proved in F5 gives
\`\`\`
 product_{j∈K} product_{i∈S}
       (if Adj(j,i) then 1−t_i else 1)
   = product_{i∈S} (1−t_i)^(#{j∈K:Adj(j,i)}).
\`\`\`
This is \`global_competitor_product_eq_neighbor_degree\`, UNIVERSAL in all finite target and competitor sets and their overlap pattern. In the original J-independent S source application, the count of adjacent outside competitors is exactly deg_J(i). This identification must be connected to the precise \`SimpleGraph.degree\` API in a subsequent Lean theorem; no hidden input source geometry is assumed.

\`integrated_original_competitor_degrees\` combines the integrals and the exact integer counts to yield
\`\`\`
   product_{i∈S} ∫₀¹(1−t)^(#{j∈K:Adj(j,i)}) dt
      = product_{i∈S}1/(#{j∈K:Adj(j,i)}+1).
\`\`\`

## 4. Seven formal proof obligations, verification and remaining blocker

Seven declared Lean theorems in this module:
1. \`uniform_target_power_integral\` — all natural degrees, exact real integration.
2. \`all_target_priority_moments\` — arbitrary finite target product of integrals.
3. \`uniform_target_moment_positive\` — positivity of every exact moment.
4. \`all_target_moments_positive\` — positivity of finite product.
5. \`product_if_eq_pow_filter\` — real incumbent original competitor incidence multiplicities.
6. \`global_competitor_product_eq_neighbor_degree\` — double-product commutation and exact count.
7. \`integrated_original_competitor_degrees\` — source competitor count plus exact integrated RHS.

Standalone GitHub-hosted pinned Lean 4.34.0 + Mathlib SHA \`5ed2965256430c3649e86755f9576b54eca72435\`; no local PC, no proof holes or source-defined axioms. The real Lean Actions workflow checks exactly the seven names and uploads their actual kernel axiom reports. The original F5/F4 specialist suites and INDEX/Research run separately on the same commit. Only GREEN exact final SHA may be labeled engineer-accepted. A separate internal mathematical review must verify the precise distinction between actual event probability and RHS integral.

### STILL OPEN (do not label full joint-minima probability as Lean-proven)

The true desired source selector theorem:
\`\`\`
  for every finite simple original conflict graph J,
  every J-independent target original-flag subset S,
  ONE global iid Uniform(0,1) priority array U,
  Pr(all i∈S are strict J-local-minima in this ONE order)
     ≥ product_{i∈S}1/(deg_J(i)+1).
\`\`\`
The **remaining formal work** is a Lean probability measure on one joint priority product space, proving conditional independence of *different competitors* given the target U_i, and the correct finite-dimensional Fubini integral. Crucially, independence of **winner events** is FALSE and must never be introduced, even though competitor PRIORITY COORDINATES are independently sampled. Subsequent original FULL/CORE three-corner source-book injection and D6↔six original source-flag-ID inverse are additionally unformalized. Existing G6-F3 paper is a mathematical proof of the conditional source T3 transfer; G6-F6 is ONLY a subformalization of its probability chain, NOT end-to-end Lean T3, unrestricted abstract T3 or dependent GF5 ASET.

**STOP:** separate Draft stacked PR, no merges, issue #793 OPEN. Future G6-F7 can use actual Mathlib ProbabilityTheory productMeasure/Measure.pi and Fubini to finish the single-global-order probability theorem, then the original source geometry. An external academic referee remains distinct from this internal review.
