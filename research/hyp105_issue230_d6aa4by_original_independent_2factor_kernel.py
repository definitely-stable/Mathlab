"""HYP-105 / #230 AA4-BY — original six-packet 2-factor exclusion.

ALL genuine symplectic ORIGINAL W(3,2^h), h>=1, every globally
injected, arbitrarily correlated complete typed original f,g:
on six disjoint whole ORIGINAL LINE-factor image transpositions,
a historical six-DISTINCT-original-incidence-Q touching ALL six
packets uses exactly one original LINE factor in each packet.
Its accepted RIGHT six-edge physical projection is 2-regular, and
a toggle replaces ONE edge by ANOTHER globally distinct physical
edge. Thus no two adjacent cube vertices accept this SAME Q.

Unlike earlier AA4-BX (#597), which uses an arbitrary Boolean 6-cube
indicator and eta6=51/32, the true original acceptance indicators lie
in the cube-independent-set cone. Classical bipartite weighted
independent-set analysis gives eta6<=45/32, sharp for ABSTRACT
independent sets (no claim of realizability by actual W3/GF5).

Refines the f-quenched all-seven selected-GF5 lower numerator error
envelope at all 64 complete original maps by 3/16 times the total
weights of genuine f-left-eligible Q touched by ALL six packets.
This is an all-h conditional ORIGINAL center certificate, NOT the
universal Omega(s^6) root theorem.
"""
from collections import Counter
from fractions import Fraction

from hyp105_issue230_d6aa4bx_all_seven_center_kernel import (
    exact_boolean_high_pass_operator_norm,
    high_degree_boolean_kernel,
    true_original_W32_left_f_quenched_high_pass_envelope,
    true_original_W32_all_seven_center_envelope,
)
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4bs_true_original_walsh_covariance import (
    true_original_line_swap_support,unnormalized_walsh,
)
from hyp105_issue230_d6aa4br_all_seven_signed_source_flux import (
    immutable_original_sixflag_class,
)
from hyp105_issue230_d6aa4bq_all_seven_reverse_switching import (
    validate_disjoint_factor_swaps,apply_disjoint_factor_swaps,
)
from hyp105_g5e2b3e1b0_seven_signature import R3_CERTIFIED_FLOORS,classify_seven_prechecked
from hyp105_g5e2b3e1a_fixed_leading import selected_left_six

CUBE6_INDEPENDENT_HIGH_PASS=Fraction(45,32)
CUBE6_BOOLEAN_HIGH_PASS=Fraction(51,32)
CUBE6_IMPROVEMENT=Fraction(3,16)
RIGHT_ORIGINAL_LINE_A_ALLOWED=("D6","B-left/A-right","C/A")

def original_six_packet_source_line_A(Q,inc,swaps,V):
    """True-original source incidence necessary structure at SIX packets."""
    pairs=validate_disjoint_factor_swaps(V,swaps)
    if len(pairs)!=6:raise ValueError("exactly six disjoint original source LINE swaps")
    Q=tuple(Q)
    touched=true_original_line_swap_support(Q,inc,pairs,V)
    if touched!=63:return False
    source_lines=[inc[j][1] for j in Q]
    if len(set(source_lines))!=6:
        raise AssertionError("six disjoint packets cannot repeat a source LINE")
    if any(sum(inc[j][1] in (u,v) for j in Q)!=1 for u,v in pairs):
        raise AssertionError("one TRUE ORIGINAL six-flag per disjoint source packet")
    return True

def physical_right_is_six_vertex_two_regular(Q,inc,global_original_g):
    """Source-Q projected multigraph on the ACTUAL original global right map."""
    degree=Counter()
    for j in Q:
        a,b=global_original_g[inc[j][1]]
        degree[a]+=1;degree[b]+=1
    return len(degree)==6 and all(n==2 for n in degree.values())

def assert_one_edge_swap_exclusion(Q,inc,g,swaps,V):
    """Finite executable independent-set falsifier for one true original Q."""
    if not original_six_packet_source_line_A(Q,inc,swaps,V):
        raise ValueError("true original Q must touch all SIX disjoint LINE packets")
    vertices=tuple(apply_disjoint_factor_swaps(g,swaps,
        tuple(i for i in range(6) if mask>>i&1)) for mask in range(64))
    accepted=tuple(int(physical_right_is_six_vertex_two_regular(Q,inc,h))
                   for h in vertices)
    if any(accepted[mask] and accepted[mask^(1<<i)]
           for mask in range(64) for i in range(6)):
        raise AssertionError("one physical edge replacement preserved 2-regular graph")
    return accepted

def independent_sixcube_highpass_certificate():
    """Exact sharp Boolean-independent-set kernel constant; classical tool.

    For k=6, unnormalized cutoff3 highpass kernel K depends on Hamming
    weight j: K_j=(22,-10,2,2,-2,-2,10). Absolute signed max over
    ALL independent subsets of Q6 is 90: negative direction achieved
    by all weight-1 and weight-4 vertices (60+30=90). Positive
    direction at most 72 (and attained by levels 0,3,6).
    Bipartite inclusion-graph Hall matching gives the upper bounds:
    levels 4+5 max independent cardinality 15, levels 2+3 max 20.
    Sharp only in abstract cube independent subsets, NOT true W3.
    """
    K=high_degree_boolean_kernel(6)
    levels={j:tuple(K[x] for x in range(64) if x.bit_count()==j)
            for j in range(7)}
    expected=(22,-10,2,2,-2,-2,10)
    if any(set(levels[j])!={expected[j]} for j in range(7)):
        raise AssertionError("Boolean sixcube highpass radial kernel changed")
    negative_witness={x for x in range(64) if x.bit_count() in (1,4)}
    positive_witness={x for x in range(64) if x.bit_count() in (0,3,6)}
    for witness in (negative_witness,positive_witness):
        if any((x^(1<<i)) in witness for x in witness for i in range(6)):
            raise AssertionError("abstract witness not independent in Q6")
    if sum(K[x] for x in negative_witness)!=-90 or \
       sum(K[x] for x in positive_witness)!=72:
        raise AssertionError("wrong exact Q6 abstract independent norm witnesses")
    if CUBE6_INDEPENDENT_HIGH_PASS!=Fraction(90,64) or \
       CUBE6_BOOLEAN_HIGH_PASS!=exact_boolean_high_pass_operator_norm(6):
        raise AssertionError("universal Boolean vs original 2factor independent constants")
    return {"abstract_independent_sixcube_signed_highpass_min_numerator":-90,
      "abstract_independent_sixcube_signed_highpass_max_numerator":72,
      "abstract_sharp_sixcube_independent_norm":Fraction(90,64),
      "general_boolean_sixcube_norm":CUBE6_BOOLEAN_HIGH_PASS,
      "strict_improvement":CUBE6_IMPROVEMENT,
      "original_GF5_realizability_of_abstract_extremizer_NOT_CLAIMED":True,
      "original_unchanged_all_h_positive_NOT_PROVED":True}

def refined_original_W32_f_only_all_seven_kernel(model,pairs):
    """Original POINT-map f only: sharpen #597 all-seven quench certificate."""
    s,V,a,inc,f,g,_,_=_original_source(model)
    if (s,V,a)!=(2,15,6):raise ValueError("finite f-quenched oracle true W32 only")
    pairs=validate_disjoint_factor_swaps(V,pairs)
    if len(pairs)!=6:raise ValueError("exactly six source LINE packets")
    old=true_original_W32_left_f_quenched_high_pass_envelope(model,pairs)
    weighted6=0; source_counts=Counter()
    Qtotal=0
    for Q,_ in selected_left_six(model):
        Qtotal+=1
        if not original_six_packet_source_line_A(Q,inc,pairs,V):continue
        tag=immutable_original_sixflag_class(Q,inc)
        if tag not in RIGHT_ORIGINAL_LINE_A_ALLOWED:
            raise AssertionError("six actual original LINE IDs must have source RIGHT A")
        if tag not in R3_CERTIFIED_FLOORS:
            raise AssertionError("genuine original Q missing selected weighted class")
        source_counts[tag]+=1
        weighted6+=R3_CERTIFIED_FLOORS[tag]
    if Qtotal!=62370 or sum(source_counts.values())!=old["source_Q_touch_count_histogram"][6]:
        raise AssertionError("genuine Q sixth packet source f-histogram mismatch previous proof")
    oldE=old["fixed_f_all_seven_weighted_high_pass_error_upper"]
    saving=CUBE6_IMPROVEMENT*weighted6
    newer=oldE-saving
    if newer<0 or saving<=0:
        raise AssertionError("expected positive actual true-original W32 source support")
    return {
        "prior_general_boolean_f_quenched_E":oldE,
        "sharpened_true_original_2factor_independent_f_quenched_E":newer,
        "exact_source_line_A_six_packet_weighted_GF5_support":weighted6,
        "f_only_true_original_six_touch_source_Q_by_class":dict(source_counts),
        "strict_reduction_from_prior_center_error":saving,
        "general_boolean_eta6":CUBE6_BOOLEAN_HIGH_PASS,
        "true_original_six_source_eta6":CUBE6_INDEPENDENT_HIGH_PASS,
        "parent_597_f_only_source_evidence":old,
        "uniform_over_all_original_complete_right_maps_g":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }

def refined_original_W32_all64_center_certificate(model,pairs):
    """Independent all-64 COMPLETE global original right maps, f-only new E."""
    old=true_original_W32_all_seven_center_envelope(model,pairs)
    env=refined_original_W32_f_only_all_seven_kernel(model,pairs)
    E=env["sharpened_true_original_2factor_independent_f_quenched_E"]
    low=old["degree_at_most_three_weighted_values"]
    full=old["full_64_original_GF5_seven_weighted_necessary_numerators"]
    high=old["signed_higher_order_weighted_values"]
    if any(abs(x)>E for x in high):
        raise AssertionError("full actual ORIGINAL seven GF5 highpass broke sharpened E")
    if any(low[i]-E>full[i] for i in range(64)):
        raise AssertionError("new exact fixed-original-center certificate broken")
    return {
      "full_64_true_original_weighted_GF5_counts":full,
      "original_center_true_weighted_GF5":full[0],
      "original_center_low_degree_Walsh_value":low[0],
      "original_center_actual_signed_highpass":high[0],
      "new_original_center_certified_lower":max(Fraction(0),low[0]-E),
      "new_sharpened_f_only_E":E,
      "all_global_right_map_vertices_verified":64,
      "original_f_g_arbitrary_correlations_preserved":True,
      "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }

def original_six_Q_exact_poincare_identity(accepted):
    """A Boolean Q6 independent set has E_i (I-I^i)^2=2p, all i."""
    b=tuple(accepted)
    if len(b)!=64 or any(type(x) is not int or x not in (0,1) for x in b):
        raise ValueError("exact Boolean full Q6 indicator required")
    if any(b[x]*b[x^(1<<i)] for x in range(64) for i in range(6)):
        raise ValueError("actual acceptance must have no adjacent cube vertices")
    p=Fraction(sum(b),64)
    hat=unnormalized_walsh(b)
    energy=Fraction(sum(T.bit_count()*hat[T]**2 for T in range(64)),64**2)
    if energy!=3*p:
        raise AssertionError("original accepted independent Q6 spectral energy identity")
    return {"mean_acceptance":p,
      "exact_sixcube_dirichlet_energy":energy,
      "energy_equals_three_times_acceptance_density":True}
