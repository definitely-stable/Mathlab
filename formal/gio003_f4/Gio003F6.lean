import Mathlib

/-!
# GIO-003 / G6-F6 — exact global-target priority INTEGRATION arithmetic

The targets are the ORIGINAL source owner IDs, with arbitrary finite
competitor sets and overlapping neighborhoods. This module proves
genuine all-natural-degree Lebesgue/interval integration and EXACT
finite competitor incidence-to-degree factorization in the Lean kernel.

STRICT SCOPE: The actual joint event in one GLOBAL iid Uniform(0,1)
priority probability space, its conditional competitor independence and
the Fubini identification of that joint probability with the product
of target integrals remain NOT YET formalized. No full-source T3 or
whole J-local-minima probability theorem is asserted in Lean here.
-/

set_option autoImplicit false

namespace Mathlab.GIO003.G6F6

open MeasureTheory intervalIntegral

/-! ### 1. The exact Lebesgue integral of a uniform target priority -/

/--
For every natural degree d, with no finite maximum degree imposed,
the exact moment of a continuous uniform target priority on [0,1]:

    ∫₀¹ (1-t)^d dt = 1/(d+1).

Uses a genuine Mathlib integral and a rigorously proved reflection,
not sampled priorities or an assumed constant.
-/
theorem uniform_target_power_integral (d : ℕ) :
    (∫ t in (0 : ℝ)..1, (1 - t) ^ d) =
      1 / ((d : ℝ) + 1) := by
  have hreflect :
      (∫ t in (0 : ℝ)..1, (1 - t) ^ d) =
        ∫ t in (0 : ℝ)..1, t ^ d := by
    simpa using
      (intervalIntegral.integral_comp_sub_left
        (a := (0 : ℝ)) (b := (1 : ℝ))
        (f := fun t : ℝ => t ^ d) (1 : ℝ))
  rw [hreflect, intervalIntegral.integral_pow]
  simp

/--
For any finite collection of original source target owners with ANY
natural degrees, the product of their exact one-dimensional uniform
moments equals the desired product of 1/(deg+1).

This proves the deterministic RHS. It does not prove independent
probability integration over the global array by itself.
-/
theorem all_target_priority_moments
    {ι : Type*}
    (targets : Finset ι) (degree : ι → ℕ) :
    (∏ i ∈ targets,
       (∫ t in (0 : ℝ)..1, (1 - t) ^ (degree i))) =
      ∏ i ∈ targets, (1 / ((degree i : ℝ) + 1)) := by
  apply Finset.prod_congr rfl
  intro i hi
  exact uniform_target_power_integral (degree i)

/-- The exact target uniform moment is strictly positive even at d=0. -/
theorem uniform_target_moment_positive (d : ℕ) :
    0 < (∫ t in (0 : ℝ)..1, (1 - t) ^ d) := by
  rw [uniform_target_power_integral]
  positivity

/-- The arbitrary finite target moment product is strictly positive. -/
theorem all_target_moments_positive
    {ι : Type*}
    (targets : Finset ι) (degree : ι → ℕ) :
    0 < ∏ i ∈ targets,
       (∫ t in (0 : ℝ)..1, (1 - t) ^ (degree i)) := by
  apply Finset.prod_pos
  intro i hi
  exact uniform_target_moment_positive (degree i)

/-! ### 2. Every actual external competitor, including shared ones -/

/-- An exact finite-product identity: a true competitor either is or
is not adjacent to fixed original target i. There is exactly one
factor (1-t_i) for each adjacent competing OWNER ID. -/
theorem product_if_eq_pow_filter
    {ι κ : Type*} [DecidableEq κ]
    (competitors : Finset κ)
    (adj : κ → ι → Prop) [∀ j i, Decidable (adj j i)]
    (i : ι) (x : ℝ) :
    (∏ j ∈ competitors, if adj j i then x else 1) =
      x ^ ((competitors.filter (fun j => adj j i)).card) := by
  induction competitors using Finset.induction_on with
  | empty => simp
  | @insert j s hj ih =>
    by_cases h : adj j i
    · simp [hj, h, ih, pow_succ, mul_comm]
    · simp [hj, h, ih]

/--
The exact competing-owner × target-owner product reordering for an
arbitrary true finite incidence relation, even when several desired
targets share the SAME original external competitor. The exponent
is the number of actual competing flags adjacent to the target.
-/
theorem global_competitor_product_eq_neighbor_degree
    {ι κ : Type*} [DecidableEq κ]
    (targets : Finset ι) (competitors : Finset κ)
    (adj : κ → ι → Prop) [∀ j i, Decidable (adj j i)]
    (priority : ι → ℝ) :
    (∏ j ∈ competitors, ∏ i ∈ targets,
       if adj j i then 1 - priority i else 1) =
      (∏ i ∈ targets,
         (1 - priority i) ^
           ((competitors.filter (fun j => adj j i)).card)) := by
  rw [Finset.prod_comm]
  apply Finset.prod_congr rfl
  intro i hi
  exact product_if_eq_pow_filter competitors adj i (1 - priority i)

/--
Combines the actual competitor-incidence degree counts with the
kernel-proved exact uniform integral for EVERY target in the finite
family, giving the final deterministic RHS of the global-priority
probability argument.

The missing connection is a *measure-theoretic* theorem that the
full joint event's probability is bounded below by these target
integrals. Neither this theorem nor F5 silently assumes that
correlated local-minimum events are independent.
-/
theorem integrated_original_competitor_degrees
    {ι κ : Type*} [DecidableEq κ]
    (targets : Finset ι) (competitors : Finset κ)
    (adj : κ → ι → Prop) [∀ j i, Decidable (adj j i)] :
    (∏ i ∈ targets,
       (∫ t in (0 : ℝ)..1, (1 - t) ^
         ((competitors.filter (fun j => adj j i)).card))) =
      (∏ i ∈ targets,
        1 / (((competitors.filter (fun j => adj j i)).card : ℝ) + 1)) := by
  exact all_target_priority_moments targets
    (fun i => (competitors.filter (fun j => adj j i)).card)

#print axioms uniform_target_power_integral
#print axioms all_target_priority_moments
#print axioms uniform_target_moment_positive
#print axioms all_target_moments_positive
#print axioms product_if_eq_pow_filter
#print axioms global_competitor_product_eq_neighbor_degree
#print axioms integrated_original_competitor_degrees

end Mathlab.GIO003.G6F6
