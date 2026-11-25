import Mathlib

/-!
# GIO-003 / G6-F8: TRUE random-threshold probability disintegration

F5 proved finite conditional shared-competitor algebra. F6 proved true
uniform real moments and source competing-owner multiplicities. F7
constructed a real one-global continuous probability measure and Fubini,
but its joint competitor event used FIXED competitor thresholds.

F8 proves that thresholds are allowed to be MEASURABLE FUNCTIONS OF
THE RANDOM TARGET OWNER PRIORITY ARRAY. It constructs the ACTUAL
joint event on a product probability space and applies Mathlib's
Tonelli/product-measure disintegration to the true event. No resampling
of shared competitor owners or independence of owner WINNER EVENTS.

STRICT SCOPE: the final arbitrary J-independent S probability lower
bound requires a further graph-specialized max-neighbor argument,
a nonnegative integral comparison, and matching original J degrees.
A genuine proof of this random-threshold disintegration is a major
step but it is NOT a Lean proof of full original-six-ID T3.
-/

set_option autoImplicit false
namespace Mathlab.GIO003.G6F8

open MeasureTheory ProbabilityTheory Set

/-! ## Real probabilities on ALL original target and competitor IDs -/

/-- One honest continuous uniform priority on the real unit interval. -/
noncomputable def uniformPriority : Measure ℝ :=
  volume.restrict (Set.Ioc (0 : ℝ) 1)

instance : IsProbabilityMeasure uniformPriority := by
  constructor
  simp [uniformPriority, Real.volume_Ioc]

/-- One joint array for all target owners; all its coordinates are iid. -/
noncomputable def targetLaw (ι : Type*) [Fintype ι] :
    Measure (ι → ℝ) := Measure.pi (fun _ : ι => uniformPriority)

/-- One joint array for all distinct competitor owner IDs. The
COMPETITOR IDs are NOT resampled per target owner. -/
noncomputable def competitorLaw (κ : Type*) [Fintype κ] :
    Measure (κ → ℝ) := Measure.pi (fun _ : κ => uniformPriority)

/-- One honest global joint experiment: the pair of arrays is sampled
ONCE under the product probability measure. It is equivalent to a
single array on the disjoint union of target and competitor IDs. -/
noncomputable def splitGlobalLaw
    (ι κ : Type*) [Fintype ι] [Fintype κ] :
    Measure ((ι → ℝ) × (κ → ℝ)) :=
  (targetLaw ι).prod (competitorLaw κ)

/-- The single target-plus-competitor global measure has total mass 1. -/
theorem split_global_law_probability
    (ι κ : Type*) [Fintype ι] [Fintype κ] :
    IsProbabilityMeasure (splitGlobalLaw ι κ) := by
  change IsProbabilityMeasure
    ((Measure.pi (fun _ : ι => uniformPriority)).prod
      (Measure.pi (fun _ : κ => uniformPriority)))
  infer_instance

/-! ## Actual random target thresholds and ONE competitor array -/

/-- EVENT: every competitor j has an owner priority strictly exceeding
a possibly RANDOM threshold m_j(target priorities). The threshold
functions are evaluated on ONE shared target sample, not separately
resampled for every competing owner. -/
def randomThresholdEvent
    {ι κ : Type*} (m : (ι → ℝ) → κ → ℝ) :
    Set ((ι → ℝ) × (κ → ℝ)) :=
  {ω | ∀ j : κ, m ω.1 j < ω.2 j}

/-- If every random threshold is measurable as a function of the WHOLE
target priority tuple, then the TRUE joint event is measurable. -/
theorem random_threshold_event_measurable
    {ι κ : Type*}
    (m : (ι → ℝ) → κ → ℝ)
    (hm : ∀ j : κ, Measurable (fun t => m t j)) :
    MeasurableSet (randomThresholdEvent m) := by
  have heq :
      randomThresholdEvent m =
        ⋂ j : κ, {ω : (ι → ℝ) × (κ → ℝ) |
          m ω.1 j < ω.2 j} := by
    ext ω
    simp [randomThresholdEvent]
  rw [heq]
  apply MeasurableSet.iInter
  intro j
  exact measurableSet_lt
    ((hm j).comp measurable_fst)
    ((measurable_pi_apply j).comp measurable_snd)

/-- For a fixed realized target tuple t, the true set of competitor
priority arrays satisfying the random-threshold event is EXACTLY the
ordinary product cylinder with fixed thresholds m_j(t). -/
theorem random_threshold_fiber
    {ι κ : Type*} (m : (ι → ℝ) → κ → ℝ)
    (t : ι → ℝ) :
    (Prod.mk t ⁻¹' randomThresholdEvent m) =
      Set.univ.pi (fun j : κ => Set.Ioi (m t j)) := by
  ext u
  simp [randomThresholdEvent, Set.mem_pi, Set.mem_Ioi]

/-- True conditional COMPETITOR probability at EVERY realized target
tuple t, by applying the product-measure cylinder theorem. This is an
event probability on the same actual competitor law, not a formal
algebraic bound. -/
theorem fixed_target_competitor_probability
    {ι κ : Type*} [Fintype κ]
    (m : (ι → ℝ) → κ → ℝ) (t : ι → ℝ) :
    competitorLaw κ (Prod.mk t ⁻¹' randomThresholdEvent m) =
      ∏ j : κ, uniformPriority (Set.Ioi (m t j)) := by
  rw [random_threshold_fiber]
  change (Measure.pi (fun _ : κ => uniformPriority))
    (Set.univ.pi (fun j : κ => Set.Ioi (m t j))) =
      ∏ j : κ, uniformPriority (Set.Ioi (m t j))
  exact Measure.pi_pi (fun _ : κ => uniformPriority)
    (fun j : κ => Set.Ioi (m t j))

/-- KEY G6-F8 theorem: Tonelli / actual conditional DISINTEGRATION
for RANDOM thresholds m_j(T), with all target priorities sampled once
and all external competitor priorities sampled once.

    Pr_{(T,K)}[∀j, U_j > m_j(T)]
      = ∫⁻ t ~ P_T, ∏_j Pr_U[U>m_j(t)].

The thresholds may depend arbitrarily on the WHOLE random target tuple
subject only to measurability. In particular several competitors may
depend on the SAME target owner's random coordinate. Independence
is only across DISTINCT competitor PRIORITIES, conditional on T.

This theorem removes the fixed-threshold bottleneck of G6-F7.
-/
theorem random_threshold_joint_disintegration
    {ι κ : Type*} [Fintype ι] [Fintype κ]
    (m : (ι → ℝ) → κ → ℝ)
    (hm : ∀ j : κ, Measurable (fun t => m t j)) :
    splitGlobalLaw ι κ (randomThresholdEvent m) =
      ∫⁻ t : ι → ℝ,
        (∏ j : κ, uniformPriority (Set.Ioi (m t j)))
        ∂targetLaw ι := by
  change (targetLaw ι).prod (competitorLaw κ)
    (randomThresholdEvent m) = _
  rw [Measure.prod_apply (random_threshold_event_measurable m hm)]
  congr 1
  funext t
  exact fixed_target_competitor_probability m t

/-! ## Genuine marginal tail and variable-threshold expression -/

/-- A REAL continuous uniform competitor has survival probability
1−t whenever the possibly realized target-dependent threshold t lies
in the [0,1] interval. -/
theorem exact_uniform_competitor_tail
    (t : ℝ) (ht0 : 0 ≤ t) (ht1 : t ≤ 1) :
    uniformPriority (Set.Ioi t) = ENNReal.ofReal (1 - t) := by
  have heq : Set.Ioi t ∩ Set.Ioc (0 : ℝ) 1 = Set.Ioc t 1 := by
    ext x
    simp only [Set.mem_inter_iff, Set.mem_Ioi, Set.mem_Ioc]
    constructor
    · rintro ⟨hxt, _hx0, hx1⟩
      exact ⟨hxt, hx1⟩
    · rintro ⟨hxt, hx1⟩
      exact ⟨hxt, lt_of_le_of_lt ht0 hxt, hx1⟩
  simp [uniformPriority, Measure.restrict_apply, heq, Real.volume_Ioc]

/-- The mathematical identity at the heart of conditioning:
at ANY FIXED realization of all target priorities in the unit cube,
the genuine external competitor joint probability is exactly
the product of 1−m_j(t), even though the threshold m_j was originally
a RANDOM function and may share target coordinates across j. -/
theorem random_threshold_conditional_exact
    {ι κ : Type*} [Fintype κ]
    (m : (ι → ℝ) → κ → ℝ) (t : ι → ℝ)
    (ht0 : ∀ j : κ, 0 ≤ m t j)
    (ht1 : ∀ j : κ, m t j ≤ 1) :
    competitorLaw κ (Prod.mk t ⁻¹' randomThresholdEvent m) =
      ∏ j : κ, ENNReal.ofReal (1 - m t j) := by
  rw [fixed_target_competitor_probability]
  apply Finset.prod_congr rfl
  intro j _
  exact exact_uniform_competitor_tail (m t j) (ht0 j) (ht1 j)

/-- Generic nonnegative integral comparison for the SAME actual
target-plus-competitor event. If a measurable ENNReal lower function L
is pointwise dominated by its TRUE conditional competitor probability,
then its integral is a valid global probability LOWER bound.

A future graph-specialized theorem must instantiate L from F5's
shared-competitor inequality and compute its integrated degree product
using F6/F7. No theorem here assumes independence of winner events.
-/
theorem random_threshold_global_lower_of_pointwise
    {ι κ : Type*} [Fintype ι] [Fintype κ]
    (m : (ι → ℝ) → κ → ℝ)
    (hm : ∀ j : κ, Measurable (fun t => m t j))
    (lower : (ι → ℝ) → ℝ≥0∞)
    (hlower : ∀ t, lower t ≤
      ∏ j : κ, uniformPriority (Set.Ioi (m t j))) :
    (∫⁻ t : ι → ℝ, lower t ∂targetLaw ι) ≤
      splitGlobalLaw ι κ (randomThresholdEvent m) := by
  rw [random_threshold_joint_disintegration m hm]
  exact lintegral_mono hlower

#print axioms split_global_law_probability
#print axioms random_threshold_event_measurable
#print axioms random_threshold_fiber
#print axioms fixed_target_competitor_probability
#print axioms random_threshold_joint_disintegration
#print axioms exact_uniform_competitor_tail
#print axioms random_threshold_conditional_exact
#print axioms random_threshold_global_lower_of_pointwise

end Mathlab.GIO003.G6F8
