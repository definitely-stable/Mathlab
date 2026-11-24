import Mathlib

/-!
# GIO-003 / G6-F4: kernel-checked partial arithmetic core of G6-F3

NOT a proof of the full T3 theorem. Source geometry, FULL/CORE
inverse, global priority and graph six-walk counting are separate,
currently unformalized premises. This file proves universal
algebraic/finite-set transformations only. No sorry/admit/axioms.
-/

set_option autoImplicit false
namespace Mathlab.GIO003.G6F4

/-- Young step: trace-six coefficient 72, once the sixth-walk
and Cauchy estimates are provided by an independent graph proof. -/
theorem sixth_walk_young
    (u c d m e : ℝ)
    (hwalk : u ^ 2 ≤ 12 * c + 6 * d * u * m)
    (hm : m ^ 2 = 2 * e) :
    u ^ 2 ≤ 24 * c + 72 * e * d ^ 2 := by
  have hsquare : 0 ≤ (u - 6 * d * m) ^ 2 := sq_nonneg _
  have hbound : u ^ 2 ≤ 24 * c + 36 * d ^ 2 * m ^ 2 := by
    nlinarith [hsquare]
  calc
    u ^ 2 ≤ 24 * c + 36 * d ^ 2 * m ^ 2 := hbound
    _ = 24 * c + 72 * e * d ^ 2 := by rw [hm]; ring

/-- Universal exact HEAVY premise implication. Source existence and
the ordinary-graph C6 theorem are separate mathematical premises. -/
theorem heavy_density_from_source
    (v e r R C0 : ℝ)
    (hv : 0 ≤ v) (hr : 0 ≤ r) (hR : 0 < R)
    (hvertices : v * (R * C0) ^ 3 ≤ r ^ 3)
    (hedges : v * r ≤ e * R) :
    C0 ^ 3 * v ^ 4 ≤ e ^ 3 := by
  have hnon : 0 ≤ v * r := mul_nonneg hv hr
  have hcubed : (v * r) ^ 3 ≤ (e * R) ^ 3 := by
    exact pow_le_pow_left₀ hnon hedges 3
  have hscaled : (v ^ 4 * C0 ^ 3) * R ^ 3 ≤ e ^ 3 * R ^ 3 := by
    calc
      (v ^ 4 * C0 ^ 3) * R ^ 3 = v ^ 3 * (v * (R * C0) ^ 3) := by ring
      _ ≤ v ^ 3 * r ^ 3 :=
          mul_le_mul_of_nonneg_left hvertices (pow_nonneg hv _)
      _ = (v * r) ^ 3 := by ring
      _ ≤ (e * R) ^ 3 := hcubed
      _ = e ^ 3 * R ^ 3 := by ring
  have hpositive : 0 < R ^ 3 := pow_pos hR 3
  have hcancel : v ^ 4 * C0 ^ 3 ≤ e ^ 3 :=
    (mul_le_mul_iff_of_pos_right hpositive).mp hscaled
  nlinarith [hcancel]

/-- Four source-LOW errors bounded by the same eps*r6. -/
theorem four_low_losses
    (improper endpoints anchors blockers eps r6 : ℝ)
    (h₁ : improper ≤ eps * r6)
    (h₂ : endpoints ≤ eps * r6)
    (h₃ : anchors ≤ eps * r6)
    (h₄ : blockers ≤ eps * r6) :
    improper + endpoints + anchors + blockers ≤ (4 * eps) * r6 := by
  linarith

/-- With eps=w/8, aggregate loss is at most (w/2)*r6. -/
theorem four_low_losses_half
    (improper endpoints anchors blockers w r6 : ℝ)
    (h₁ : improper ≤ (w / 8) * r6)
    (h₂ : endpoints ≤ (w / 8) * r6)
    (h₃ : anchors ≤ (w / 8) * r6)
    (h₄ : blockers ≤ (w / 8) * r6) :
    improper + endpoints + anchors + blockers ≤ (w / 2) * r6 := by
  have h := four_low_losses improper endpoints anchors blockers (w / 8) r6
      h₁ h₂ h₃ h₄
  nlinarith [h]

/-- Positive source-obstruction density, provided all inputs positive. -/
theorem source_delta_pos
    (c0 R w : ℝ) (hc : 0 < c0) (hR : 0 < R) (hw : 0 < w) :
    0 < min (c0 / R ^ 6) (w / 4) := by
  apply lt_min
  · exact div_pos hc (pow_pos hR 6)
  · positivity

/-- Heavy/low case combination under explicit source-combinatorial hypotheses. -/
theorem heavy_or_low_obstruction
    (D6 BBo delta r6 : ℝ)
    (hD : 0 ≤ D6) (hB : 0 ≤ BBo)
    (hcases : D6 ≥ delta * r6 ∨ BBo ≥ delta * r6) :
    delta * r6 ≤ D6 + BBo := by
  rcases hcases with h | h
  · linarith
  · linarith

/-- For ALL J0>=0, fixed original J bound gives retained LOW fraction >1/2. -/
theorem low_core_fraction
    (J0 : ℝ) (hJ0 : 0 ≤ J0) :
    (1 : ℝ) - 1 / 8 - 1 / 32 - (2 * J0) / (16 * J0 + 2) > 1 / 2 := by
  have hden : (0 : ℝ) < 16 * J0 + 2 := by nlinarith
  have hquot : (2 * J0) / (16 * J0 + 2) ≤ 1 / 8 := by
    apply (div_le_iff₀ hden).mpr
    nlinarith
  linarith

/-- Exactly six distinct named ORIGINAL IDs, if the three genuine FULL
anchors and three genuine CORE residual owners are disjoint. The actual
source mapping producing those flags is NOT proved in Lean here. -/
theorem six_original_flag_ids
    (fullAnchors coreOwners : Finset ℕ)
    (hA : fullAnchors.card = 3)
    (hC : coreOwners.card = 3)
    (hdisjoint : Disjoint fullAnchors coreOwners) :
    (fullAnchors ∪ coreOwners).card = 6 := by
  simp [Finset.card_union_of_disjoint hdisjoint, hA, hC]

/-- Fixed p=2^20 gate arithmetic for the already proved F1 regularization.
This does NOT formalize the full regularization induction. -/
theorem c6_regularization_fixed_integer_gates :
    (9 : ℕ) ^ 6 ≤ 2 ^ 20 ∧
    (9 : ℕ) ^ 4 ≤ 4 * 2 ^ 20 ∧
    (192 : ℕ) * 2 ^ 20 ≤ (2 ^ 20 : ℕ) ^ 2 := by
  norm_num

#print axioms sixth_walk_young
#print axioms heavy_density_from_source
#print axioms four_low_losses
#print axioms four_low_losses_half
#print axioms source_delta_pos
#print axioms heavy_or_low_obstruction
#print axioms low_core_fraction
#print axioms six_original_flag_ids
#print axioms c6_regularization_fixed_integer_gates

end Mathlab.GIO003.G6F4
