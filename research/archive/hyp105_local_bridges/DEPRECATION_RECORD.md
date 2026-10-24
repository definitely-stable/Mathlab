# Deprecation and Archival Record: Hyp-105 Local Reservoir Stack

**Status:** ARCHIVED & SUPERSEDED BY CANONICAL CORE (`hyp105_canonical_core.py`).

## 1. Executive Summary

During stages AA4-AA through AA4-DH (PRs #504 through #634), extensive effort was directed toward proving Hypothesis 105 Branch A through local combinatorial configurations:
- 5-line local reservoirs ($L_5$)
- 2-external $A$-bridges with paired $C_4$ completions (AA4-DG, AA4-DH)
- $130 \times 130$ positional tensor marginals (AA4-AA)
- Single-site assignment dual relaxations (D6-T)

Stages **AA4-DI** (PR #639) and **AA4-DJ** (PR #640) definitively proved that **all local finite-width approaches are mathematically insufficient** to establish Branch A:
1. **Coupled Incidence Density Barrier (AA4-DI):**
   In generalized quadrangle $W(3,s)$, the point-coverage density of any 5 lines collapses as:
   $$\rho_5(s) \le \frac{5s + 4}{(s+1)(s^2+1)} \le \frac{5}{s^2} = O(s^{-2}).$$
   Point coverage for 2-external $A$-bridges collapses as $O(s^{-10})$.
2. **Universal Finite-Width Support Barrier (AA4-DJ):**
   For ANY local reservoir of width $m$ lines, the uncovered point fraction is:
   $$1 - \frac{m(s+1)}{(s+1)(s^2+1)} = 1 - \frac{m}{s^2+1} \xrightarrow{s \to \infty} 1.$$
   An adversary can always map external physical edges to uncovered points, driving local completion mass $M_{k, m}(f, g) = 0$.

## 2. Superseded Module Inventory (Exact Disk Filenames)

The following modules in `research/` belong to the superseded local reservoir exploration:
- `hyp105_issue230_d6aa4_source_forest_transport.py`
- `hyp105_issue230_d6aa4aa_original_full_forest_closure.py`
- `hyp105_issue230_d6aa4ab_minimax_orbit_normalform.py`
- `hyp105_issue230_d6aa4ac_rooted_coupled_gap.py`
- `hyp105_issue230_d6aa4ad_opposite_a_hall_transfer.py`
- `hyp105_issue230_d6aa4ae_gq_girth8_sharp_rook.py`
- `hyp105_issue230_d6aa4af_rootpair_robust_quench.py`
- `hyp105_issue230_d6aa4ag_deterministic_triangle_hall.py`
- `hyp105_issue230_d6aa4ah_signature_hall_kernel.py`
- `hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation.py`
- `hyp105_issue230_d6aa4aj_connected_c6_original_transfer.py`
- `hyp105_issue230_d6aa4ak_adjacent_full_a_hall.py`
- `hyp105_issue230_d6aa4al_global_original_coordinate_transport.py`
- `hyp105_issue230_d6aa4am_genuine_pair_sixcharge.py`
- `hyp105_issue230_d6aa4an_port_completion_hall_funnel.py`
- `hyp105_issue230_d6aa4ao_robust_port_occupancy.py`
- `hyp105_issue230_d6aa4ap_uniform_good_original_D_spectral.py`
- `hyp105_issue230_d6aa4aq_colored_original_D_cycle.py`
- `hyp105_issue230_d6aa4ar_good_wedges_port_balance.py`
- `hyp105_issue230_d6aa4as_threeflag_hall_frontier.py`
- `hyp105_issue230_d6aa4at_original_forest_unique_hall.py`
- `hyp105_issue230_d6aa4au_source_triple_hall_polynomials.py`
- `hyp105_issue230_d6aa4av_global_source_aa_good_wedges.py`
- `hyp105_issue230_d6aa4aw_sharp_original_twoport_marginals.py`
- `hyp105_issue230_d6aa4ax_original_incidence_cell_port_caps.py`
- `hyp105_issue230_d6aa4ay_quenched_allD_opposite_mean.py`
- `hyp105_issue230_d6aa4az_quenched_allD_variance.py`
- `hyp105_issue230_d6aa4az_quenched_good_opposite.py`
- `hyp105_issue230_d6aa4b_coherent_block_fiber.py`
- `hyp105_issue230_d6aa4bb_overlap_covariance.py`
- `hyp105_issue230_d6aa4bc_robust_pins.py`
- `hyp105_issue230_d6aa4bd_tenth_pins.py`
- `hyp105_issue230_d6aa4be_original_D6_pins.py`
- `hyp105_issue230_d6aa4bf_constructive_sixflag_D6.py`
- `hyp105_issue230_d6aa4bg_fixed_squarefree_D6_trace.py`
- `hyp105_issue230_d6aa4bh_local_seven_compensation.py`
- `hyp105_issue230_d6aa4bi_original_cherry_moment.py`
- `hyp105_issue230_d6aa4bj_cherry_hall_defect.py`
- `hyp105_issue230_d6aa4bk_each_cherry_BA.py`
- `hyp105_issue230_d6aa4bl_two_pin_conditional_BA.py`
- `hyp105_issue230_d6aa4bm_four_swap_root_BA_repair.py`
- `hyp105_issue230_d6aa4bn_multi_root_swap_compatibility.py`
- `hyp105_issue230_d6aa4bo_simultaneous_cherry_repair.py`
- `hyp105_issue230_d6aa4bp_linear_many_root_repair.py`
- `hyp105_issue230_d6aa4bq_all_seven_reverse_switching.py`
- `hyp105_issue230_d6aa4br_all_seven_signed_source_flux.py`
- `hyp105_issue230_d6aa4bs_true_original_walsh_covariance.py`
- `hyp105_issue230_d6aa4bt_gq_sixth_order_intersections.py`
- `hyp105_issue230_d6aa4bu_five_original_GQ_spectrum.py`
- `hyp105_issue230_d6aa4bv_fourth_original_GQ_CA_anchors.py`
- `hyp105_issue230_d6aa4bx_all_seven_center_kernel.py`
- `hyp105_issue230_d6aa4by_original_independent_2factor_kernel.py`
- `hyp105_issue230_d6aa4bz_original_neighbor_three_kernel.py`
- `hyp105_issue230_d6aa4c_edit_transversal.py`
- `hyp105_issue230_d6aa4ca_exact_n3_boolean_kernel.py`
- `hyp105_issue230_d6aa4cb_original_parity_affine_center.py`
- `hyp105_issue230_d6aa4cb_original_physical_parity_code.py`
- `hyp105_issue230_d6aa4cd_one_sided_original_center.py`
- `hyp105_issue230_d6aa4ce_shared_sixpacket_xor_coupling.py`
- `hyp105_issue230_d6aa4cf_overlapping_sevenpacket_unique_completion.py`
- `hyp105_issue230_d6aa4cg_four_shared_edge_two_completion.py`
- `hyp105_issue230_d6aa4ch_maximal_d6_fan_physical_gram_nogo.py`
- `hyp105_issue230_d6aa4ci_dual_cycle_orbit_fiber_invariant.py`
- `hyp105_issue230_d6aa4cj_global_point_swap_dual_flow_ledger.py`
- `hyp105_issue230_d6aa4ck_dual_cycle_transposition_spectral_energy.py`
- `hyp105_issue230_d6aa4cl_shared_four_point_fibers_covariance.py`
- `hyp105_issue230_d6aa4cm_negative_original_named_pair_covariance.py`
- `hyp105_issue230_d6aa4cn_joint_dual_compatibility_block_ledger.py`
- `hyp105_issue230_d6aa4co_global_allseven_W32_96map_bridge.py`
- `hyp105_issue230_d6aa4cp_full_right_original_sevenclass_join.py`
- `hyp105_issue230_d6aa4cq_original_macro_path_cut_gate.py`
- `hyp105_issue230_d6aa4cr_exact_BBo_three_matching_transfer.py`
- `hyp105_issue230_d6aa4cs_uniform_disjoint_original_source_cut.py`
- `hyp105_issue230_d6aa4ct_dense_physical_c4_reservoir.py`
- `hyp105_issue230_d6aa4cu_exterior_matching_energy.py`
- `hyp105_issue230_d6aa4cv_allh_zero_spoke_block.py`
- `hyp105_issue230_d6aa4cw_multi_anchor_spoke_leakage.py`
- `hyp105_issue230_d6aa4cx_local_spectrum_doubled_exclusion.py`
- `hyp105_issue230_d6aa4cy_second_moment_original_raw.py`
- `hyp105_issue230_d6aa4cz_collinearity_badpath_mass.py`
- `hyp105_issue230_d6aa4d_mixed_transversal_fibers.py`
- `hyp105_issue230_d6aa4da_bridge_gram_safe_source_flags.py`
- `hyp105_issue230_d6aa4db_occupied_c4_spoke_flag_mass.py`
- `hyp105_issue230_d6aa4dc_marked_cofactor_hall_deficit.py`
- `hyp105_issue230_d6aa4dd_dual_hall_vacancy.py`
- `hyp105_issue230_d6aa4de_robust_cofactor_sparsity.py`
- `hyp105_issue230_d6aa4df_fivebyfive_local_compensation.py`
- `hyp105_issue230_d6aa4dg_two_external_A_bridge.py`
- `hyp105_issue230_d6aa4dh_constant_multiplicity_inverse.py`

## 3. The New Canonical Core Path

All production and future formal proofs bypass the entire local stack and depend ONLY on:
- `research/hyp105_canonical_core.py` (3-lemma minimal architecture):
  - **Lemma 1:** Global Unanchored Transversal Carrier $\tau(P_6) \ge (1 - O(s^{-2})) s^6$.
  - **Lemma 2:** Girth-8 Hypergeometric Sparsity $P(R \le 1) \ge 1 - O(s^{-2})$ & Strictly Negative Disjoint Covariance $\operatorname{Cov}_0 < 0$.
  - **Lemma 3:** Super-Ramanujan Spectrum $\lambda_2 = \sqrt{2s} < 2\sqrt{s}$ & Simultaneous Annihilation Barrier ($D6 + BA + AB \ge \Omega(s^6)$).
