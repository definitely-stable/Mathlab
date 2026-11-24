import Mathlib

/-!
# GIO-003 / G6-F5 — universal shared-competitor formal proof

FORMAL SCOPE: for every finite set of target ORIGINAL source owners and every
finite set of (possibly shared) competing original owners, this module
kernel-proves the exact CONDITIONAL PRIORITY inequalities and finite product
reindexing used by G6-F3's one-GLOBAL-owner-priority argument.

It does NOT yet kernel-prove the uniform-probability space construction,
multi-dimensional integration, or the full final probability ≥ product
1/(degree+1). Those are explicitly separate obligations. No owner winner
events are ever falsely assumed independent. No sorry, admit or extra axiom.
-/

set_option autoImplicit false
namespace Mathlab.GIO003.G6F5

/-! ### Universal algebra for a single shared competing owner -/

/-- Two target owners with priorities a,b in [0,1] and ONE shared competitor.
The competitor beats BOTH precisely when its uniform priority exceeds their
maximum; the conditional probability is 1-max a b, NOT (1-a)(1-b).
The TRUE pointwise inequality has the direction below. -/
theorem two_targets_one_shared_competitor
    (a b : ℝ)
    (ha0 : 0 ≤ a) (ha1 : a ≤ 1)
    (hb0 : 0 ≤ b) (hb1 : b ≤ 1) :
    (1 - a) * (1 - b) ≤ 1 - max a b := by
  rcases le_total a b with hab | hba
  · rw [max_eq_right hab]
    nlinarith [mul_nonneg (sub_nonneg.mpr ha0) (sub_nonneg.mpr hb1)]
  · rw [max_eq_left hba]
    nlinarith [mul_nonneg (sub_nonneg.mpr ha1) (sub_nonneg.mpr hb0)]

/-- Three target owners may share ONE competitor. All three desired
local-minimum events are correlated, but their exact conditional factor
dominates the product of the three individual survival factors. -/
theorem three_targets_one_shared_competitor
    (a b c : ℝ)
    (ha0 : 0 ≤ a) (ha1 : a ≤ 1)
    (hb0 : 0 ≤ b) (hb1 : b ≤ 1)
    (hc0 : 0 ≤ c) (hc1 : c ≤ 1) :
    (1 - a) * (1 - b) * (1 - c) ≤ 1 - max (max a b) c := by
  have hab := two_targets_one_shared_competitor a b ha0 ha1 hb0 hb1
  have habnon : 0 ≤ 1 - max a b := by
    have hmax : max a b ≤ 1 := max_le ha1 hb1
    linarith
  have hc : 0 ≤ 1-c := sub_nonneg.mpr hc1
  calc
    (1 - a) * (1 - b) * (1 - c)
        ≤ (1 - max a b) * (1 - c) :=
          mul_le_mul_of_nonneg_right hab hc
    _ ≤ 1 - max (max a b) c :=
          two_targets_one_shared_competitor (max a b) c
            (le_max_of_le_left ha0) (max_le ha1 hb1) hc0 hc1

/-! ### Every finite target set, not just two/three targets -/

/-- A product of factors in [0,1] is never larger than any one factor.
This is the core of the shared-competitor lower-bound proof. -/
theorem product_bounded_by_any_factor
    {ι : Type*} [DecidableEq ι]
    (targets : Finset ι) (p : ι → ℝ)
    (hp0 : ∀ i ∈ targets, 0 ≤ p i)
    (hp1 : ∀ i ∈ targets, p i ≤ 1)
    (i : ι) (hi : i ∈ targets) :
    (∏ j ∈ targets, p j) ≤ p i := by
  have hle : (∏ j ∈ targets, p j) ≤ (∏ j ∈ ({i} : Finset ι), p j) := by
    apply Finset.prod_le_prod_of_subset_of_le_one₀
    · exact Finset.singleton_subset_iff.mpr hi
    · intro j hj
      exact hp0 j hj
    · intro j hj _
      exact hp1 j hj
  simpa using hle

/-- For a genuine finite set S of original target owner priorities t_i,
if a competitor's threshold m is ACTUALLY attained by a member of S,
then its conditional joint survival factor 1-m dominates
the product over ALL individual target survival factors.

The threshold must be an attained maximum; a merely arbitrary number
m≥t_i would NOT imply the result, and is not an assumption here. -/
theorem shared_competitor_attained_max
    {ι : Type*} [DecidableEq ι]
    (targets : Finset ι) (t : ι → ℝ) (m : ℝ)
    (ht0 : ∀ i ∈ targets, 0 ≤ t i)
    (ht1 : ∀ i ∈ targets, t i ≤ 1)
    (hmax : ∃ i ∈ targets, t i = m) :
    (∏ i ∈ targets, (1 - t i)) ≤ 1 - m := by
  rcases hmax with ⟨i, hi, heq⟩
  have hp0 : ∀ j ∈ targets, 0 ≤ (1 - t j) := by
    intro j hj
    exact sub_nonneg.mpr (ht1 j hj)
  have hp1 : ∀ j ∈ targets, (1 - t j) ≤ 1 := by
    intro j hj
    linarith [ht0 j hj]
  have h := product_bounded_by_any_factor targets (fun j => 1 - t j)
    hp0 hp1 i hi
  simpa [heq] using h

/-- Uniform-priority threshold m in [0,1] gives a valid (nonnegative)
conditional survival probability 1-m. -/
theorem shared_competitor_factor_nonneg
    (m : ℝ) (hm : m ≤ 1) : 0 ≤ 1 - m := by
  linarith

/-! ### All finite competitors and any overlap incidence -/

/--
For ANY (possibly heavily overlapping) finite family of competitor
neighborhoods, multiplying the correct per-competitor conditional
lower bounds is valid. Conditional independence is used only for
DIFFERENT COMPETITOR PRIORITIES, never for desired owner survival
EVENTS. This theorem is an algebraic step; the probabilistic
independence fact is a separate not-yet-Lean-formalized obligation.
-/
theorem multiply_shared_competitor_bounds
    {κ : Type*}
    (competitors : Finset κ)
    (lower actual : κ → ℝ)
    (hlow0 : ∀ j ∈ competitors, 0 ≤ lower j)
    (hpoint : ∀ j ∈ competitors, lower j ≤ actual j) :
    (∏ j ∈ competitors, lower j) ≤
    (∏ j ∈ competitors, actual j) := by
  exact Finset.prod_le_prod₀ hlow0 hpoint

/-- The first half of the ALL-OWNER selector inequality: for arbitrarily
many target and competitor owners, with any incidence/neighborhood
relation and with correct attained per-competitor maximal priorities,
the product of all conditional shared-competitor success factors is
at least the product of all individual target factors, **without
independence of the desired local-minimum events**. -/
theorem global_shared_competitors_conditional_lower
    {ι κ : Type*} [DecidableEq ι]
    (competitors : Finset κ)
    (neighbors : κ → Finset ι)
    (t : ι → ℝ) (maxPriority : κ → ℝ)
    (ht0 : ∀ j ∈ competitors, ∀ i ∈ neighbors j, 0 ≤ t i)
    (ht1 : ∀ j ∈ competitors, ∀ i ∈ neighbors j, t i ≤ 1)
    (hattain : ∀ j ∈ competitors,
      ∃ i ∈ neighbors j, t i = maxPriority j) :
    (∏ j ∈ competitors, ∏ i ∈ neighbors j, (1 - t i)) ≤
    (∏ j ∈ competitors, (1 - maxPriority j)) := by
  apply multiply_shared_competitor_bounds competitors
    (fun j => ∏ i ∈ neighbors j, 1 - t i)
    (fun j => 1 - maxPriority j)
  · intro j hj
    apply Finset.prod_nonneg
    intro i hi
    exact sub_nonneg.mpr (ht1 j hj i hi)
  · intro j hj
    exact shared_competitor_attained_max (neighbors j) t (maxPriority j)
      (ht0 j hj) (ht1 j hj) (hattain j hj)

/-- The EXACT finite rectangular factorization across ALL competitors
and ALL target source IDs, even with arbitrary overlaps. No assumption
of disjoint neighborhoods is present. -/
theorem global_competitor_target_product_commute
    {ι κ : Type*}
    (targets : Finset ι) (competitors : Finset κ)
    (adj : κ → ι → Bool) (p : ι → ℝ) :
    (∏ j ∈ competitors, ∏ i ∈ targets,
      if adj j i then p i else 1) =
    (∏ i ∈ targets, ∏ j ∈ competitors,
      if adj j i then p i else 1) := by
  exact Finset.prod_comm

/-! ### False independence and the universal strict shared case -/

/-- On a true shared competitor, taking target events independent
underestimates their joint survival: for 0<t<1 the TRUE joint factor
(1-t) strictly exceeds the FALSE cube of separate marginal factors.
This is a strict symbolic theorem, not a numerical simulation. -/
theorem shared_competitor_strict_correlation
    (t : ℝ) (ht0 : 0 < t) (ht1 : t < 1) :
    (1 - t) ^ 3 < 1 - t := by
  have hpos : 0 < 1 - t := by linarith
  have hsmall : 1 - t < 1 := by linarith
  nlinarith [sq_nonneg t, mul_pos hpos (sub_pos.mpr hsmall)]

/-! All new proofs are real universal theorems, not examples. -/

#print axioms two_targets_one_shared_competitor
#print axioms three_targets_one_shared_competitor
#print axioms product_bounded_by_any_factor
#print axioms shared_competitor_attained_max
#print axioms shared_competitor_factor_nonneg
#print axioms multiply_shared_competitor_bounds
#print axioms global_shared_competitors_conditional_lower
#print axioms global_competitor_target_product_commute
#print axioms shared_competitor_strict_correlation

end Mathlab.GIO003.G6F5
