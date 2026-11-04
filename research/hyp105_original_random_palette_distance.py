"""HYP-105 AA4-PALDIST: exact ORIGINAL six-ID packing / random GF5 palette distance.

NEW ALL-N CONDITIONAL-ON-GIVEN-PACKING THEOREM, no geometric Branch A:
Fix any genuine physical-original source columns with independent
uniform legal 51-pattern checksum4 GF5 coefficients, and t pairwise
ORIGINAL-ID-disjoint accepted D6/B/B-overlap signed-sixsets. Each chosen
balanced signed equality has probability >= 5175/51**6, by independent
exact 51-pattern per-sign flow enumeration in AA4-SIGN10.

The chosen events are independent because their SIX original flag-ID
sets are disjoint. Their failures Y lower bound the Hamming distance
from the random source palettes to ANY full 0-to-3 source ASET, even
when the final source palettes may change globally/nonmonotonically.
Thus P(random source is zero 0..3 ASET) <= (1-q)^t <= exp(-q*t),
P(dist_to_any_clean_source < q*t/2) <= exp(-q*t/8).
The complete 0..3 source assignment need not exist; distance=+inf
then satisfies the inequality.

CONDITIONAL ALL-h COROLLARY ONLY: if the externally unaccepted
source-deletion theorem in Draft #674 is established, t > rho*s**4/6
uniformly for all complete arbitrarily correlated maps f,g, giving
an exp(-Omega(s**4)) palette-zero rarity and Omega(s**4) typical
minimal recolor distance. This is not a proof of Root #230 Branch A,
and not an R3 upper bound or an ASET exponent improvement.

Finite W32 genuine original six-incidence packings are checked against
BOTH independent GF5 coefficient solvers, with all ten original signs
available. Never substitute a synthetic source for the genuine GQ.
"""
from collections import Counter
from fractions import Fraction
from functools import reduce
from itertools import combinations
import json
from math import comb
from operator import mul

LEGAL_PALETTES=51
SOURCE_FLAG_SIZE=6
FULL_PALETTE_SPACE=LEGAL_PALETTES**SOURCE_FLAG_SIZE
UNIFORM_MIN_SIGNED_COUNT=5175  # exact B/B-overlap min per sign, AA4-SIGN10
Q=Fraction(UNIFORM_MIN_SIGNED_COUNT,FULL_PALETTE_SPACE)
ALLOWED_CLASSES=frozenset(("D6","B/B-overlap"))
ORIGINAL_ROOT_230_OPEN="OPEN_WITH_FORMAL_BLOCKER"


def check_disjoint_original_sixset_packing(n_original_flags,pack):
    """Verify literal ORIGINAL flag IDs, without physical-coordinate dedup."""
    if type(n_original_flags) is not int or n_original_flags<6:
        raise ValueError("invalid number of original source flags")
    selected=set()
    result=[]
    for z in pack:
        ids=tuple(z["original_source_IDs"])
        family=z["accepted_class"]
        if (family not in ALLOWED_CLASSES or len(ids)!=6 or
            len(set(ids))!=6 or
            any(type(x) is not int or not 0<=x<n_original_flags for x in ids) or
            tuple(sorted(ids))!=ids or
            not selected.isdisjoint(ids)):
            raise ValueError("invalid source-ID-disjoint ORIGINAL accepted sixset")
        selected.update(ids)
        result.append((ids,family))
    return tuple(result)


def source_palette_signed_probability(signed_count):
    if (type(signed_count) is not int or
        not UNIFORM_MIN_SIGNED_COUNT<=signed_count<=FULL_PALETTE_SPACE):
        raise ValueError("original chosen balanced sign must meet exact GF5 lower")
    return Fraction(signed_count,FULL_PALETTE_SPACE)


def exact_independent_failure_distribution(signed_counts):
    """Finite exact Poisson-binomial law, never treats 10 signs as independent."""
    signed_counts=tuple(signed_counts)
    if len(signed_counts)>32:
        raise ValueError("exact distribution reserved for finite control <=32 sixsets")
    pmf=[Fraction(1)]
    for n in signed_counts:
        p=source_palette_signed_probability(n)
        new=[Fraction(0)]*(len(pmf)+1)
        for k,old in enumerate(pmf):
            new[k]+=old*(1-p)
            new[k+1]+=old*p
        pmf=new
    if sum(pmf)!=1 or any(p<0 for p in pmf):
        raise AssertionError("not a normalized independent TRUE ORIGINAL palette law")
    return tuple(pmf)


def exact_finite_packing_report(n_original_flags,pack,*,require_source_signs=True):
    parsed=check_disjoint_original_sixset_packing(n_original_flags,pack)
    if require_source_signs:
        counts=tuple(z["chosen_signed_GF5_legal_assignments"] for z in pack)
        probs=tuple(source_palette_signed_probability(v) for v in counts)
    else:
        counts=tuple([UNIFORM_MIN_SIGNED_COUNT]*len(parsed))
        probs=tuple([Q]*len(parsed))
    law=exact_independent_failure_distribution(counts)
    if len(law)!=len(parsed)+1:
        raise AssertionError("finite six-source independent event distribution lost")
    mu=sum(probs,Fraction())
    qpack=Q*len(parsed)
    # Uniform symbolic Chernoff:
    # P(Y <= E Y/2) <= exp(- E Y /8) <= exp(-q*t/8).
    return {
        "schema":"mathlab.hyp105.original-palettes-source-disjoint-packing.v1",
        "actual_original_flag_count":n_original_flags,
        "six_source_distinct_packing_size":len(parsed),
        "accepted_original_classes":dict(Counter(ty for _,ty in parsed)),
        "exact_signed_GF5_legal_pattern_counts":list(counts),
        "chosen_signed_GF5_legal_probabilities":[
            {"numerator":v.numerator,"denominator":v.denominator} for v in probs],
        "exact_probability_NO_chosen_3v3_source_event":{
            "numerator":law[0].numerator,"denominator":law[0].denominator},
        "exact_expected_chosen_signed_failures":{
            "numerator":mu.numerator,"denominator":mu.denominator},
        "exact_probability_at_least_one_chosen_3v3_event":{
            "numerator":(1-law[0]).numerator,
            "denominator":(1-law[0]).denominator},
        "full_independent_exact_Bernoulli_pmf_size":len(law),
        "all_51_source_coefficients_uniform_and_independent":True,
        "does_NOT_equate_chosen_event_zero_with_full_ASET_zero":True,
        "universal_signed_single_motif_q_numerator":Q.numerator,
        "universal_signed_single_motif_q_denominator":Q.denominator,
        "exponential_upper_failfree_rate_q_times_t":{
            "numerator":qpack.numerator,"denominator":qpack.denominator},
        "high_probability_minimum_recolor_distance_floor_qt_over_2":{
            "numerator":(qpack/2).numerator,"denominator":(qpack/2).denominator},
        "chernoff_deviation_exponent_qt_over_8":{
            "numerator":(qpack/8).numerator,"denominator":(qpack/8).denominator},
        "root_230_status":ORIGINAL_ROOT_230_OPEN,
        "root_all_h_branch_A_proved_here":False,
    }


def conditional_allh_hamming_distance(s,rho,*,parent_deletion_theorem_is_an_assumption):
    """Pure rational all-h implication; rho is NOT an accepted numeric constant.

    If externally unaccepted Draft #674 is proved for this rho and s>=s0,
    EVERY valid complete f,g has t>rho*s^4/6 original-disjoint
    accepted source sixsets. No call can certify the antecedent.
    """
    if type(s) is not int or s<2 or s&(s-1):
        raise ValueError("s must be 2^h, h>=1")
    if not isinstance(rho,Fraction) or not 0<rho<=1:
        raise ValueError("rho must be a positive exact rational assumption")
    if parent_deletion_theorem_is_an_assumption is not True:
        raise ValueError("cannot silently promote unaccepted #674 theorem")
    required_t=(rho*s**4/6).numerator//(rho*s**4/6).denominator+1
    r=Q*rho/6
    return {
        "schema":"mathlab.hyp105.original-allh-CONDITIONAL-palette-distance.v1",
        "s":s,
        "requires_external_acceptance_of_parent_674_allh_deletion":True,
        "requires_s_at_least_unknown_external_parent_s0":True,
        "formal_assumed_rho":{"numerator":rho.numerator,
                               "denominator":rho.denominator},
        "packing_original_sixsets_count_strictly_greater_than_rho_s4_over_6":True,
        "minimum_integer_source_sixset_packing_if_parent_holds":required_t,
        "signed_GF5_probability_min_q":str(Q),
        "palette_clean_probability_upper_bound":"exp(-q*rho*s^4/6)",
        "palette_clean_exponential_rate":{
            "numerator":r.numerator,"denominator":r.denominator},
        "probability_recolor_distance_less_than_qrho_s4_over_12":
            "at most exp(-q*rho*s^4/48)",
        "hamming_distance_rigorous_lower_coefficient":{
            "numerator":(r/2).numerator,"denominator":(r/2).denominator},
        "distance_chernoff_exponential_rate":{
            "numerator":(r/8).numerator,"denominator":(r/8).denominator},
        "root_original_230_A_B_C_status":ORIGINAL_ROOT_230_OPEN,
        "root_allh_accepted":False,
    }


def genuine_W32_source_disjoint_motif_report(scheme):
    """Actual W(3,2) flags and complete globally injected typed maps."""
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
    from hyp105_g5e2b3e1b0_seven_signature import seven_census
    from hyp105_gf5_original_sixid_flow_referee import (
        original_projected_column_edges, gf5_flow_inclusion_exclusion,
        gf5_flow_spanning_tree,SIGNS)
    if scheme not in ("lex","reverse-line"):
        raise ValueError("source map not one of genuine pinned W32 controls")
    model=pair_labeled_symplectic(1,scheme)
    census=seven_census(model,independent_checks=True,witness_sets=True)
    flags=model["incidences"]
    all_six=[(tuple(ids),tag) for ids,tag in census["sets"].items()
             if tag in ALLOWED_CLASSES]
    all_six.sort(key=lambda x:(x[1]!="D6",x[0]))
    used=set()
    chosen=[]
    for ids,tag in all_six:
        if set(ids)&used:continue
        edges=original_projected_column_edges(
            flags,ids,model["left_labels"],model["right_labels"])
        # Choose ONE canonical balanced original sign; the ten signs
        # MUST NOT be misinterpreted as independent Bernoulli events.
        plus=SIGNS[0]
        a=gf5_flow_inclusion_exclusion(edges,plus)
        b=gf5_flow_spanning_tree(edges,plus)
        if a!=b or a<UNIFORM_MIN_SIGNED_COUNT:
            raise AssertionError("two independent FULL GF5 source signed oracles disagree")
        used.update(ids)
        chosen.append({"original_source_IDs":list(ids),
                       "accepted_class":tag,
                       "chosen_positive_original_local_indices":sorted(plus),
                       "chosen_signed_GF5_legal_assignments":a})
    if not chosen or any(not (set(ids)&used) for ids,tag in all_six):
        raise AssertionError("not maximal genuine W32 six-original-ID motif packing")
    r=exact_finite_packing_report(len(flags),chosen)
    r.update({
        "scheme":scheme,
        "full_true_original_W32_incidence_flags":len(flags),
        "full_true_original_W32_accepted_D6":census[
            "seven_class_motif_counts"]["D6"],
        "full_true_original_W32_accepted_BB_overlap":census[
            "seven_class_motif_counts"]["B/B-overlap"],
        "original_source_signed_sixset_witnesses":chosen,
        "greedy_packing_maximal_NOT_claimed_maximum":True,
        "derived_from_original_W32_point_line_f_g_NOT_synthetic":True,
        "bound_on_probability_full_0_to_3_ASET_ONLY_upper":True,
    })
    return r


def run():
    return {
        "schema":"mathlab.hyp105.original-W32-signed-packing-distance-proof.v1",
        "scope":"finite true original W32 two frozen fully injected maps",
        "schemes":{scheme:genuine_W32_source_disjoint_motif_report(scheme)
                   for scheme in ("lex","reverse-line")},
        "allh_corollary_depends_on_674_EXTERNAL_ACCEPTANCE":True,
        "allh_geometric_obstruction_proved_here":False,
        "root_230_status":ORIGINAL_ROOT_230_OPEN,
    }


if __name__=="__main__":
    print("AA4_ORIGINAL_PALETTE_DISTANCE_CERTIFICATE="+json.dumps(
        run(),sort_keys=True,separators=(",",":")),flush=True)
