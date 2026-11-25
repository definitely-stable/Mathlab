import Mathlib

/-!
# GIO-003 / G6-F7: ONE real global iid Uniform[0,1] owner priority law.

Unlike F5's conditional algebra and F6's disconnected univariate moments,
the kernel now constructs one actual finite product probability law on ALL
original owner priorities; proves coordinate independence, true joint
competitor event probabilities, real uniform tails, and target-product
Fubini over the SAME global probability law.

STRICT LIMIT: the event that ALL target owners are strict J-local minima,
with thresholds depending on the random TARGET coordinates, still requires
a formal joint-event disintegration/conditional expectation step. No
full all-graph Caro-Wei simultaneous-minima bound is asserted here.
-/

set_option autoImplicit false

namespace Mathlab.GIO003.G6F7

open MeasureTheory ProbabilityTheory Set intervalIntegral

/-! # 1. One actual continuous uniform probability measure -/

/-- Lebesgue-uniform probability law on the real unit interval (0,1]. -/
noncomputable def unitPriority : Measure ℝ :=
  volume.restrict (Set.Ioc (0 : ℝ) 1)

/-- The marginal is an ACTUAL probability measure, not an axiom. -/
instance : IsProbabilityMeasure unitPriority := by
  constructor
  simp [unitPriority, Real.volume_Ioc]

/-- One shared array for ALL original source-owner labels, with one
independent uniform coordinate per label. -/
noncomputable def globalOwnerPriorities (ι : Type*) [Fintype ι] :
    Measure (ι → ℝ) :=
  Measure.pi (fun _ : ι => unitPriority)

/-- The global array itself has TOTAL probability one, including an
empty finite original owner type. -/
theorem global_law_is_probability (ι : Type*) [Fintype ι] :
    IsProbabilityMeasure (globalOwnerPriorities ι) := by
  change IsProbabilityMeasure (Measure.pi (fun _ : ι => unitPriority))
  infer_instance

/-! # 2. True independence of COORDINATE priorities, not winner events -/

/-- Exact marginal law of every original source-owner priority in the
ONE global probability array, obtained from Mathlib's product measure. -/
theorem coordinate_is_uniform {ι : Type*} [Fintype ι] (i : ι) :
    (globalOwnerPriorities ι).map (fun ω : ι → ℝ => ω i) =
      unitPriority := by
  change (Measure.pi (fun _ : ι => unitPriority)).map
    (Function.eval i) = unitPriority
  exact (measurePreserving_eval (fun _ : ι => unitPriority) i).map_eq

/-- ALL different ORIGINAL owner PRIORITIES are mutually independent.
This never claims that source-owner local-minimum WINNER EVENTS are
independent (those share competing owner priorities). -/
theorem all_priority_coordinates_independent
    {ι : Type*} [Fintype ι] :
    iIndepFun (fun (i : ι) (ω : ι → ℝ) => ω i)
      (globalOwnerPriorities ι) := by
  change iIndepFun
      (fun (i : ι) (ω : ι → ℝ) => (id : ℝ → ℝ) (ω i))
      (Measure.pi (fun _ : ι => unitPriority))
  exact iIndepFun_pi (X := fun _ : ι => id)
    (fun _ => measurable_id.aemeasurable)

/-! # 3. Exact joint event for arbitrarily many fixed competitors -/

/-- For ANY finite set of distinct external owner ID coordinates,
the probability that each priority exceeds its given fixed threshold
factors into its REAL one-dimensional marginal probabilities.

The thresholds are FIXED here, and do not secretly depend on random
target priorities. The latter conditioning remains separate work.
-/
theorem global_competitor_fixed_threshold_probability
    {ι : Type*} [Fintype ι]
    (competitors : Finset ι) (threshold : ι → ℝ) :
    globalOwnerPriorities ι
        ((competitors : Set ι).pi (fun j => Set.Ioi (threshold j))) =
      ∏ j ∈ competitors, unitPriority (Set.Ioi (threshold j)) := by
  change (Measure.pi (fun _ : ι => unitPriority))
      ((competitors : Set ι).pi (fun j => Set.Ioi (threshold j))) =
        ∏ j ∈ competitors, unitPriority (Set.Ioi (threshold j))
  exact Measure.pi_pi_finset (fun _ : ι => unitPriority)
    (fun j => Set.Ioi (threshold j)) competitors

/-- Exact unit-interval tail law for any actual fixed threshold t∈[0,1].
There are NO atoms at the boundaries. -/
theorem uniform_one_priority_tail
    (t : ℝ) (ht0 : 0 ≤ t) (ht1 : t ≤ 1) :
    unitPriority (Set.Ioi t) = ENNReal.ofReal (1 - t) := by
  have heq : Set.Ioi t ∩ Set.Ioc (0 : ℝ) 1 = Set.Ioc t 1 := by
    ext x
    simp only [Set.mem_inter_iff, Set.mem_Ioi, Set.mem_Ioc]
    constructor
    · rintro ⟨hxt, _hx0, hx1⟩
      exact ⟨hxt, hx1⟩
    · rintro ⟨hxt, hx1⟩
      exact ⟨hxt, lt_of_le_of_lt ht0 hxt, hx1⟩
  simp [unitPriority, Measure.restrict_apply, heq, Real.volume_Ioc]

/-- Actual unconditional probability on one finite global array of
independent COMPETITOR priorities, at FIXED thresholds t_j∈[0,1]:

  Pr(∀j∈K, U_j>t_j) = product_{j∈K} (1−t_j).

This is a probability theorem (ENNReal-valued), not merely the F5
algebra of conditional factors. All K are arbitrary finite sets.
-/
theorem global_competitor_fixed_threshold_exact
    {ι : Type*} [Fintype ι]
    (competitors : Finset ι) (threshold : ι → ℝ)
    (ht0 : ∀ j ∈ competitors, 0 ≤ threshold j)
    (ht1 : ∀ j ∈ competitors, threshold j ≤ 1) :
    globalOwnerPriorities ι
        ((competitors : Set ι).pi (fun j => Set.Ioi (threshold j))) =
      ∏ j ∈ competitors, ENNReal.ofReal (1 - threshold j) := by
  rw [global_competitor_fixed_threshold_probability]
  apply Finset.prod_congr rfl
  intro j hj
  exact uniform_one_priority_tail (threshold j) (ht0 j hj) (ht1 j hj)

/-! # 4. Multivariate Fubini on this SAME real global priority law -/

/-- Exact Fubini identity for arbitrary products of coordinate
functions on the ONE GLOBAL source probability law. In particular
different owner's priorities are genuinely independent here.
The functions need not be nonnegative: this is Mathlib's REAL integral.
-/
theorem global_priorities_fubini
    {ι : Type*} [Fintype ι] (f : ι → ℝ → ℝ) :
    (∫ ω : ι → ℝ,
      ∏ i : ι, f i (ω i) ∂(globalOwnerPriorities ι)) =
      ∏ i : ι, ∫ t : ℝ, f i t ∂unitPriority := by
  change (∫ ω : ι → ℝ,
      ∏ i : ι, f i (ω i) ∂(Measure.pi (fun _ : ι => unitPriority))) =
      ∏ i : ι, ∫ t : ℝ, f i t ∂unitPriority
  exact MeasureTheory.integral_fintype_prod_eq_prod f

/-- Exact uniform marginal real integral for ANY original conflict
degree d, no bounded-graph-size assumption. -/
theorem global_one_priority_power_moment (d : ℕ) :
    (∫ t : ℝ, (1 - t) ^ d ∂unitPriority) =
      1 / ((d : ℝ) + 1) := by
  change (∫ t in Set.Ioc (0 : ℝ) 1,
      (1 - t) ^ d ∂volume) = 1 / ((d : ℝ) + 1)
  rw [← intervalIntegral.integral_of_le (show (0 : ℝ) ≤ 1 by norm_num)]
  have hreflect :
      (∫ t in (0 : ℝ)..1, (1 - t) ^ d) =
        ∫ t in (0 : ℝ)..1, t ^ d := by
    simpa using
      (intervalIntegral.integral_comp_sub_left
        (a := (0 : ℝ)) (b := (1 : ℝ))
        (f := fun t : ℝ => t ^ d) (1 : ℝ))
  rw [hreflect, integral_pow]
  simp

/--
The fundamental F6 integrals are now integrated with REAL Fubini
over an ACTUAL SINGLE COMMON GLOBAL ARRAY of independent Uniforms.
For EVERY finite original owner type and arbitrary degree function:

  E_global[ product_i (1-U_i)^(deg_i) ]
     = product_i 1/(deg_i+1).

This is NOT yet the probability of the all-J-local-minima event;
one must connect the conditional shared-competitor inequality from
F5 to this expectation by a formal conditioning/Fubini lemma.
-/
theorem global_actual_joint_target_power_expectation
    {ι : Type*} [Fintype ι] (degree : ι → ℕ) :
    (∫ ω : ι → ℝ,
       ∏ i : ι, (1 - ω i) ^ (degree i)
       ∂globalOwnerPriorities ι) =
      ∏ i : ι, (1 / ((degree i : ℝ) + 1)) := by
  calc
    (∫ ω : ι → ℝ,
       ∏ i : ι, (1 - ω i) ^ (degree i)
       ∂globalOwnerPriorities ι) =
        ∏ i : ι, ∫ t : ℝ, (1 - t) ^ (degree i) ∂unitPriority :=
      global_priorities_fubini (fun i t => (1 - t) ^ (degree i))
    _ = ∏ i : ι, (1 / ((degree i : ℝ) + 1)) := by
      apply Finset.prod_congr rfl
      intro i hi
      exact global_one_priority_power_moment (degree i)

#print axioms global_law_is_probability
#print axioms coordinate_is_uniform
#print axioms all_priority_coordinates_independent
#print axioms global_competitor_fixed_threshold_probability
#print axioms uniform_one_priority_tail
#print axioms global_competitor_fixed_threshold_exact
#print axioms global_priorities_fubini
#print axioms global_one_priority_power_moment
#print axioms global_actual_joint_target_power_expectation

end Mathlab.GIO003.G6F7
