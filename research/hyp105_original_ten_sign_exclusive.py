"""HYP-105 AA4-PALDIST-TEN: true original 10-sign EXCLUSIVE union theorem.

Every accepted original D6 or B/B-overlap sixset has exactly six
physical coordinate-to-column edges on EACH side (12 dual edges total).
Any nontrivial 2+2 equal-sum relation among FOUR of its six columns
would require the four column indices to be CLOSED under every one of
those dual edges: an edge crossing the chosen four/nonchosen two would
leave exactly ONE nonzero GF5 term in a physical coordinate.

For D6 both colored duals are connected C6. For B/B-overlap their
components consist of a doubled two-ID edge plus a disjoint four-ID C4
on each colored side; the two repeated-source pairs have exactly ONE
common original ID and therefore no common closed 4-column subset.
Consequently, neither family can have an internal 2+2 equality under
ANY legal nonzero coefficients. The full 425/source global pair-injected
model also makes all six source singletons physically distinct.

Two different global-sign-unordered balanced 3+3 signed equalities
on the SAME sixset, after choosing canonical signs containing local
ID 0, have positive triples intersecting in 1 or 2 source IDs.
Subtracting the two GF5 signed equations (2 invertible mod5) implies
a 2+2 equal-sum if intersection=1 or a singleton equal-sum if
intersection=2. BOTH impossible. Thus the TEN signed events of one
accepted original sixset are PAIRWISE DISJOINT: their full-51-palette
union probability equals the SUM of the ten exact signed flow counts.

Sharp previous independent AA4-SIGN10 source counts:
D6       54,162 legal six-palette assignments (EXACT).
BBo      53,526 OR 53,838 assignments (EXACT).
Therefore the exact union event probability for EVERY accepted D6/BBo
is at least q10=53,526/51^6, instead of the 5,175/51^6 previously used
for ONE arbitrary signed partition. This does NOT assume ten events
independent, and does NOT apply to arbitrary sixset classes.

Independent original sixset-ID-disjoint pack events remain independent
ACROSS sixsets, permitting exponential random-clean ASET scarcity
and palette Hamming repair lower bounds with q10.

This new all-N theorem is independent of the unaccepted universal
geometric #672/#674. An all-h implication still requires #674.
"""
from fractions import Fraction
from itertools import combinations
from collections import Counter

from hyp105_original_random_palette_distance import (
    check_disjoint_original_sixset_packing,
    exact_independent_failure_distribution,
    genuine_W32_source_disjoint_motif_report,
    FULL_PALETTE_SPACE,ORIGINAL_ROOT_230_OPEN)

MIN_UNION_SIX_SIGNED=53526
Q_TEN=Fraction(MIN_UNION_SIX_SIGNED,FULL_PALETTE_SPACE)
EXACT_TOTALS={"D6":frozenset({54162}),
              "B/B-overlap":frozenset({53526,53838})}
SOURCE_CLASSES=frozenset(EXACT_TOTALS)


def closed_four_flag_subsets(physical_original_sixset_dual_edges):
    """Independent combinatorial oracle: 15 candidate true 4/6 ID masks.

    12 edges: six physical GF5 source coordinate dual edges on left
    and six on right, each with TWO ORIGINAL column indices. If an
    original four-source support is not closed under EVERY edge, no
    nonzero signed 2v2 equation on that 4-source set is possible.
    """
    edges=tuple(tuple(e) for e in physical_original_sixset_dual_edges)
    if (len(edges)!=12 or
        any(len(e)!=2 or len(set(e))!=2 or
            any(type(id) is not int or not 0<=id<6 for id in e)
            for e in edges)):
        raise ValueError("only genuine 12 full physical coordinate dual edges")
    for side in (edges[:6],edges[6:]):
        if (len(side)!=6 or
            any(sum(id in e for e in side)!=2 for id in range(6))):
            raise ValueError("not six original columns with EXACTLY two"
                             " typed physical coordinates per original ID")
    good=[]
    for selected in combinations(range(6),4):
        S=set(selected)
        if all((u in S)==(v in S) for u,v in edges):
            good.append(selected)
    return tuple(good)


def canonical_ten_original_signs_are_mutually_exclusive(edges):
    """Mathematical all-51-palette no-R2 gate: not a statistical assertion."""
    closed=closed_four_flag_subsets(edges)
    if closed:
        raise AssertionError(
            "4-flag support closed: overlapping 3v3 signed events NOT excluded")
    return {
        "all_15_original_four_flag_subsets_checked":15,
        "source_local_original_flag_IDs":list(range(6)),
        "source_four_flag_dual_closed_subsets":[],
        "all_10_balanced_signed_GF5_events_pairwise_exclusive":True,
        "not_sign_independence_but_sign_disjointness":True,
    }


def original_ten_sign_union_counts(edges, accepted_class):
    """Two independent exact GF5 solvers, 10 canonical signed equations."""
    from hyp105_gf5_original_sixid_flow_referee import (
        SIGNS,gf5_flow_inclusion_exclusion,gf5_flow_spanning_tree)
    if accepted_class not in SOURCE_CLASSES:
        raise ValueError("only original positive D6 or B/B-overlap source class")
    structure=canonical_ten_original_signs_are_mutually_exclusive(edges)
    full=[]
    for plus in SIGNS:
        a=gf5_flow_inclusion_exclusion(edges,plus)
        b=gf5_flow_spanning_tree(edges,plus)
        if a!=b or a<5175:
            raise AssertionError("not exact full 51^6 true original GF5 sign flow")
        full.append(a)
    total=sum(full)
    if total not in EXACT_TOTALS[accepted_class]:
        raise AssertionError("not a true source-original accepted sixset topology")
    return {
        **structure,
        "accepted_original_sixset_class":accepted_class,
        "all_ten_original_signed_flow_counts":full,
        "source_ten_sign_union_favorable_palette_assignments_exact":total,
        "source_ten_sign_union_event_probability":{
            "numerator":Fraction(total,FULL_PALETTE_SPACE).numerator,
            "denominator":Fraction(total,FULL_PALETTE_SPACE).denominator},
        "six_original_source_legal_palette_universe":FULL_PALETTE_SPACE,
        "all_ten_signs_are_MUTUALLY_EXCLUSIVE_not_independent":True,
        "probability_may_be_summed_without_any_R2_or_singleton_overlap":True,
    }


def stronger_genuine_W32_original_tensign_packing(scheme):
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
    from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked
    from hyp105_gf5_original_sixid_flow_referee import original_projected_column_edges
    base=genuine_W32_source_disjoint_motif_report(scheme)
    model=pair_labeled_symplectic(1,scheme)
    pack=base["original_source_signed_sixset_witnesses"]
    check_disjoint_original_sixset_packing(len(model["incidences"]),pack)
    enhanced=[]
    for z in pack:
        ids=tuple(z["original_source_IDs"])
        family=z["accepted_class"]
        if (classify_seven_prechecked(ids,model["left_labels"],
                model["right_labels"],model["incidences"])!=family):
            raise AssertionError("true original W32 source class drift")
        edges=original_projected_column_edges(
            model["incidences"],ids,model["left_labels"],
            model["right_labels"])
        ten=original_ten_sign_union_counts(edges,family)
        if ten["all_ten_original_signed_flow_counts"][0]!=z[
              "chosen_signed_GF5_legal_assignments"]:
            raise AssertionError("not same ORIGINAL source coefficient assignment")
        enhanced.append({"original_source_IDs":list(ids),
                         "accepted_class":family,
                         "ten_sign_GF5_full_51_palette_audit":ten})
    probabilities=tuple(Fraction(
        z["ten_sign_GF5_full_51_palette_audit"][
            "source_ten_sign_union_favorable_palette_assignments_exact"],
        FULL_PALETTE_SPACE) for z in enhanced)
    exact_product=Fraction(1)
    for p in probabilities:exact_product*=1-p
    qn=Q_TEN*len(enhanced)
    return {
        "schema":"mathlab.hyp105.original-W32-exclusive-ten-sign-packing.v1",
        "scheme":scheme,
        "original_source_W32_flags":45,
        "true_original_source_globally_injected_f_g":True,
        "all_source_original_sixsets_have_six_distinct_original_flag_IDs":True,
        "all_ten_signs_mutually_EXCLUSIVE_for_each_original_motif":True,
        "original_motif_sign_sets_are_INDEPENDENT_ACROSS_disjoint_sixsets":True,
        "source_disjoint_sixset_packing_size":len(enhanced),
        "source_original_sixset_witnesses":enhanced,
        "exact_independent_NO_motif_with_ANY_of_ten_signs_probability":{
            "numerator":exact_product.numerator,
            "denominator":exact_product.denominator},
        "exact_expected_number_of_failed_selected_motifs":{
            "numerator":sum(probabilities,Fraction()).numerator,
            "denominator":sum(probabilities,Fraction()).denominator},
        "rigorous_uniform_lower_union_p":str(Q_TEN),
        "uniform_palette_full_zero_ASET_probability_UPPER_only":True,
        "allh_requires_separate_unaccepted_source_deletion_674":True,
        "root_original_230_status":ORIGINAL_ROOT_230_OPEN,
        "root_allh_accepted_here":False,
        "source_nontrivial_internal_two_plus_two_equalities_EXCLUDED":True,
        "exponential_clean_probability_rate_at_least_q10_times_t":str(qn),
        "hamming_repair_distance_threshold_q10_times_t_over_two":str(qn/2),
        "chernoff_lower_tail_exponent_q10_times_t_over_eight":str(qn/8),
    }


def conditional_allh_exclusive_signed_palettes(s,rho,*,assume_external_674=False):
    from hyp105_original_random_palette_distance import conditional_allh_hamming_distance
    c=conditional_allh_hamming_distance(
        s,rho,parent_deletion_theorem_is_an_assumption=assume_external_674)
    t=rho*s**4/6
    c.update({
        "schema":"mathlab.hyp105.original-conditional-allh-EXCLUSIVE-tensign-distance.v1",
        "all_ten_signs_are_disjoint_NOT_independent_inside_one_motif":True,
        "source_six_motif_exact_BBo_ten_sign_probability_floor":str(Q_TEN),
        "allh_full_clean_probability_upper_expression":
            "exp(-(53526/51^6)*rho*s^4/6)",
        "allh_clean_exponential_rate":str(Q_TEN*rho/6),
        "allh_repair_distance_floor":str(Q_TEN*rho/12),
        "allh_repair_lower_tail_rate":str(Q_TEN*rho/48),
        "parent_674_geometric_allh_is_NOT_acceptance":True,
        "root_allh_accepted":False,
    })
    return c


def run():
    return {
        "schema":"mathlab.hyp105.original-W32-ten-sign-exclusive-distance.v1",
        "source_original_W32_schemes":{
            s:stronger_genuine_W32_original_tensign_packing(s)
            for s in ("lex","reverse-line")},
        "signed_uniform_GF5_51_to_6_union_probability_min":{
            "numerator":Q_TEN.numerator,"denominator":Q_TEN.denominator},
        "full_original_sixset_signs_not_falsely_independent":True,
        "original_root_230_status":ORIGINAL_ROOT_230_OPEN,
        "new_root_allh_geometric_obstruction_proved":False,
        "conditional_allh_requires_674_external_scientific_acceptance":True,
    }


if __name__=="__main__":
    import json
    print("AA4_ORIGINAL_EXCLUSIVE_TENSIGN_CERTIFICATE="+json.dumps(
        run(),separators=(",",":"),sort_keys=True),flush=True)
