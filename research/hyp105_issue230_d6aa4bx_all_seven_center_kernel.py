"""HYP-105 #230 AA4-BX — TRUE-ORIGINAL all-seven signed center envelope.

For every genuine symplectic W(3,2^h), every arbitrary correlated
globally injected fixed pair maps f,g, and six disjoint ORIGINAL LINE
factor image swaps, one common cube of 64 complete original right maps
is defined. On that cube the HISTORICAL selected seven-GF5 floor
numerator W=Σ_c w_c S_c satisfies exactly W=P_<=3 W+R_>3.

Each genuine same-six-original-incidence-ID indicator I_Q depends on
k<=6 source LINE swap packets. Its high-order Fourier projection has
a SHARP universal Boolean-indicator sup norm eta(k), where for k=4,5,6
the values are 1/2,15/16,51/32 (eta(k)=0 for k<=3).
Thus |R_>3(x)|<=E_f=Σ_{true original Q left physical 6-eligible,
source selected seven-GF5 class c(Q)} w_c(Q)*eta(k_Q), for ALL
64 global right maps simultaneously. E_f is independent of original
g and even of the occupied right pair-edge image set E. Exact signed
R is computed via the true-original history on one coherent cube.

Unlike preceding #596 class-C/B triangle bounds, this works for ALL
SEVEN historical source classes and uses the exact Boolean kernel
operator norm instead of separate crude Fourier triangle caps.

It is an all-h CONDITIONAL CENTER certificate W(f,g)>=P_<=3 W(0)-E_f,
NOT a proof that the RHS is >=c*s^6 for all original f,g. Boolean
Walsh Fourier projection/Krawtchouk kernels are classical prior art.
"""
from collections import Counter
from fractions import Fraction

from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4bq_all_seven_reverse_switching import (
    validate_disjoint_factor_swaps, apply_disjoint_factor_swaps,
)
from hyp105_issue230_d6aa4bs_true_original_walsh_covariance import (
    true_original_line_swap_support, unnormalized_walsh,
)
from hyp105_issue230_d6aa4br_all_seven_signed_source_flux import (
    immutable_original_sixflag_class,
)
from hyp105_g5e2b3e1b0_seven_signature import (
    R3_CERTIFIED_FLOORS, classify_seven_prechecked, seven_census,
)
from hyp105_g5e2b3e1a_fixed_leading import selected_left_six


def high_degree_boolean_kernel(k, cutoff=3):
    """Exact Walsh high-pass kernel on k bits, evaluated at center zero.

    K(y)=Σ_{|T|>cutoff}(-1)^popcount(T∩y), zero mean. Its positive-mass
    L1/2 equals the EXACT operator norm for Boolean functions I∈{0,1}.
    No reliance on an FFT, binomial normal approximation or independent Q.
    """
    if type(k) is not int or not 0<=k<=6:
        raise ValueError("true ORIGINAL sixflag has <=6 sensitive swap packets")
    if type(cutoff) is not int or not 0<=cutoff<=6:
        raise ValueError("a valid exact Boolean spectral cutoff is needed")
    n=1<<k
    result=tuple(sum(
        (-1 if ((T & y).bit_count() & 1) else 1)
        for T in range(n) if T.bit_count()>cutoff
    ) for y in range(n))
    if sum(result)!=0:
        raise AssertionError("zero-mean high-degree Boolean Fourier kernel violated")
    return result


def exact_boolean_high_pass_operator_norm(k, cutoff=3):
    """Sharp sup over all BOOLEAN original-indicator patterns, not W3 sharp."""
    kernel=high_degree_boolean_kernel(k,cutoff)
    n=len(kernel)
    return Fraction(sum(abs(z) for z in kernel),2*n)


def all_h_boolean_six_source_kernel_certificate():
    """Exact cutoff=3 constants, valid for all h and ALL source f,g."""
    eta=tuple(exact_boolean_high_pass_operator_norm(k) for k in range(7))
    if eta!=(
        Fraction(0),Fraction(0),Fraction(0),Fraction(0),
        Fraction(1,2),Fraction(15,16),Fraction(51,32)):
        raise AssertionError("exact sharp Boolean high-pass norms changed")
    return {
        "maximum_genuine_original_sixflag_swaps":6,
        "all_seven_GF5_classes_one_original_Q_immutable":True,
        "uniform_boolean_per_Q_high_pass_exact_operator_norms":eta,
        "exact_for_arbitrary_correlated_original_complete_f_g":True,
        "same_one_global_original_right_map_at_every_cube_vertex":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


def true_original_W32_left_f_quenched_high_pass_envelope(model, pairs):
    """Finite W32 concrete E_f, independent of ANY complete right map g.

    Uses ALL 62,370 actually selected LEFT physical sixflags Q ONCE.
    The original POINT source factor map f and source incidence system
    alone determine k_Q and immutable possible historical GF5 tag c(Q).
    """
    s,V,a,inc,f,g,_,_=_original_source(model)
    if (s,V,a)!=(2,15,6):
        raise ValueError("source f-quenched finite proof oracle only true W32")
    pairs=validate_disjoint_factor_swaps(V,pairs)
    if len(pairs)!=6:
        raise ValueError("six pairwise disjoint WHOLE original LINE source swaps")
    stats=Counter()
    weights=R3_CERTIFIED_FLOORS
    bound=Fraction(0)
    candidates=0
    considered=0
    side={}
    for Q,_ in selected_left_six(model):
        candidates+=1
        tag=immutable_original_sixflag_class(Q,inc)
        if tag is None:
            continue
        k=true_original_line_swap_support(Q,inc,pairs,V).bit_count()
        if k>6:raise AssertionError("true Q touches >6 disjoint original swaps")
        considered+=1
        stats[(tag,k)]+=1
        eta=exact_boolean_high_pass_operator_norm(k)
        if eta:bound+=eta*weights[tag]
    if candidates!=62370:
        raise AssertionError("all genuine original W32 LEFT six-coordinate census changed")
    if considered!=sum(stats.values()):
        raise AssertionError("source GF5 type histogram missing original Q")
    byk={k:sum(n for (tag,j),n in stats.items() if j==k)
         for k in range(7)}
    perclass={c:sum(n for (tag,j),n in stats.items() if tag==c)
              for c in weights}
    naive=Fraction(sum(
      n*weights[c]*sum(
        1 for T in range(1<<k) if T.bit_count()>3
      ) for (c,k),n in stats.items()),2)
    if bound>naive:
        raise AssertionError("sharp Boolean operator norm is worse than termwise triangle")
    return {
      "s":s,"source_POINT_complete_original_map_f":f,
      "actual_LINE_original_swap_pairs":pairs,
      "n_original_left_sixflag_candidates":candidates,
      "n_original_Q_with_possible_selected_GF5_class":considered,
      "original_source_GF5_possible_class_counts":perclass,
      "source_Q_touch_count_histogram":byk,
      "source_selected_class_by_touch_count":dict(stats),
      "fixed_f_all_seven_weighted_high_pass_error_upper":bound,
      "older_naive_22_termwise_triangle_error_upper":naive,
      "new_bound_never_exceeds_naive":bound<=naive,
      "independent_of_original_global_right_map_g":True,
      "original_unchanged_f_g_positive_NOT_PROVED":True,
    }


def true_original_W32_all_seven_center_envelope(model,pairs, *, local_oracle=False):
    """Exact historical all-seven Walsh degree<=3 at every original cube map.

    64 COMPLETE globally coherent right-map values independently
    classified by the existing full seven_census; no source-Q-local
    reassignments. Optionally compare an independent per-original-Q
    LOCAL Walsh Fourier tail against the whole-W_Fourier transform.
    """
    s,V,a,inc,f,g,_,_=_original_source(model)
    env=true_original_W32_left_f_quenched_high_pass_envelope(model,pairs)
    pairs=env["actual_LINE_original_swap_pairs"]
    n=1<<6
    maps=tuple(apply_disjoint_factor_swaps(g,pairs,
       tuple(i for i in range(6) if mask & (1<<i)))
       for mask in range(n))
    if not all(set(assignment)==set(g) for assignment in maps):
        raise AssertionError("whole-line source swaps changed original occupied support")
    counts=tuple(seven_census(dict(model,right_labels=assignment),
                             independent_checks=False)["seven_class_motif_counts"]
                  for assignment in maps)
    wc=R3_CERTIFIED_FLOORS
    all7=tuple(sum(row.values()) for row in counts)
    W=tuple(sum(wc[c]*row[c] for c in wc) for row in counts)
    coefficients=unnormalized_walsh(W)
    low=tuple(Fraction(sum(coefficients[T]*
                         (-1 if (T & x).bit_count() & 1 else 1)
                         for T in range(n) if T.bit_count()<=3),n)
              for x in range(n))
    high=tuple(Fraction(W[x])-low[x] for x in range(n))
    bound=env["fixed_f_all_seven_weighted_high_pass_error_upper"]
    if any(abs(value)>bound for value in high):
        raise AssertionError("true original all-seven g-uniform sharp E_f falsified")
    if any(low[x]-bound>W[x] for x in range(n)):
        raise AssertionError("certified original unchanged-map lower bound false")
    source_local_total=None
    if local_oracle:
        source_local_total=Fraction(0)
        for Q,_ in selected_left_six(model):
            tag=immutable_original_sixflag_class(Q,inc)
            if tag is None:continue
            mask=true_original_line_swap_support(Q,inc,pairs,V)
            relevant=tuple(i for i in range(6) if mask&(1<<i))
            k=len(relevant)
            if k<=3:continue
            local_vals=[]
            for y in range(1<<k):
                toggled=tuple(relevant[j] for j in range(k) if y&(1<<j))
                changed=apply_disjoint_factor_swaps(g,pairs,toggled)
                actual=classify_seven_prechecked(Q,f,changed,inc)
                if actual is not None and actual!=tag:
                    raise AssertionError("one original Q switched positive GF5 classes")
                local_vals.append(int(actual is not None))
            qhat=unnormalized_walsh(local_vals)
            source_local_total+=Fraction(
                wc[tag]*sum(qhat[T] for T in range(1<<k)
                            if T.bit_count()>3),1<<k)
        if source_local_total!=high[0]:
            raise AssertionError("independent original-Q local Walsh tail != full historical census")
    return {
      "n_full_global_original_right_maps":n,
      "full_64_original_GF5_seven_weighted_necessary_numerators":W,
      "full_64_unweighted_seven_class_scores":all7,
      "full_64_true_original_historical_seven_class_counts":counts,
      "unnormalized_all_seven_historical_weighted_Walsh":coefficients,
      "degree_at_most_three_weighted_values":low,
      "signed_higher_order_weighted_values":high,
      "exact_source_Q_local_signed_higher_order_at_original_center":
          source_local_total,
      "original_center_actual_weighted_necessary_GF5_numerator":W[0],
      "original_center_degree_at_most_three_part":low[0],
      "original_center_signed_high_order_correction":high[0],
      "original_center_certified_lower":
          max(Fraction(0),low[0]-bound),
      "pointwise_uniform_all_64_full_global_maps":True,
      "complete_original_map_occupied_right_support_preserved":True,
      "quenched_geometric_source_envelope":env,
      "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }
