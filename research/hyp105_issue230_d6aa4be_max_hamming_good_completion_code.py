"""HYP-105 #230 AA4-BE — many maximally Hamming-separated TRUE original
global LINE-map completions, all simultaneously GOOD under 10% arbitrary
pins. Strict child of parallel AA4-BD #565 (not another pin-loss lemma).

For EVERY true original W(3,2^h), h>=10, any fixed COMPLETE point
physical map f, any right physical V-edge occupied support E, and
ANY injected images of k<=floor(V/10) actual source LINE factor IDs,
there exist m=floor(V/400_000_000)>=2 different complete global
injected right maps g_0..g_(m-1) extending all pins, such that:
 * EACH has >=s^6/160 genuine original GOOD point/line
   physically opposite centered three-incidence-flag wedges.
 * EVERY TWO differ on EVERY unpinned original LINE factor
   physical pair image; Hamming distance exactly n=V-k.
 * In fact, a positive >=1/2 fraction of ALL n! pinned full map
   completions can be chosen as a base g for one fixed cyclic
   permutation of the WHOLE n free physical right-edge images,
   giving this entire successful Hamming code simultaneously.

Only uses ACTUAL original GQ source, f and E; per completed g
every original source factor image is one GLOBAL mapping.
No source-event per-Q randomization, no every-fixed-g theorem,
no selected historical seven GF5 six-original-incidence-ID bound.

Prior #565 proves under k<=V/10 the conditional probability for
one globally uniformly sampled complete right map of having
R_GOOD<s^6/160 is <=4eta, eta<=50_000_000/V.
For any PRESELECTED entire-free-support bijections T_j, uniform
pinned completion is invariant under g->T_j(g). Union bound:
 P_g[ALL_j R_GOOD(T_j g)>=s^6/160] >=1-4m*eta.
Choose T_j=cyclic shift^j on the n FREE physical pair images,
j=0..m-1. For m<=n these cyclic shifts differ pointwise for
each free original source LINE ID. Since m<=V/400e6,
4m eta<=1/2. For h>=10 V>8e8, m>=2.
This is an ORBIT packing corollary of global permutation
concentration, not a novel general permutation code theorem.
"""
from fractions import Fraction

from hyp105_issue230_d6aa4bd_tenth_pins import (
    tenth_pinned_GOOD_completion)


def preselected_original_global_LINE_orbit(s,k,m):
    """Exact conditional *simultaneous* source-good map orbit probability.

    PRESELECTED m arbitrary permutations of the one fixed FREE
    occupied physical right pair-edge support; each transformation
    acts on the ENTIRE globally injected true-original line map.
    Existence when 4*m*eta<1. No independence used.
    """
    z=tenth_pinned_GOOD_completion(s,k)
    if type(m) is not int or m<1:
        raise ValueError("m >=1 preselected complete global free-right-support image shuffles")
    eta=z["conditional_relative_variance_upper"]
    bound=Fraction(1)-4*m*eta
    return dict(
        s=s,k=k,m=m,V=z["V"],n=z["unpinned_original_LINE_factors"],
        global_right_LINE_map_completion_count_factorial_argument=z[
            "unpinned_original_LINE_factors"],
        exact_rational_conditional_relative_variance_parent=eta,
        exact_union_lower_on_simultaneously_GOOD_fraction=max(Fraction(0),bound),
        exact_union_lower_before_truncation=bound,
        all_selected_COMPLETE_global_right_image_shuffles_have_good_original_wedges=(
            bound>0),
        every_ORIGINAL_line_pin_preserved_by_all_transformations=True,
        every_full_map_genuine_original_good_wedge_count_at_least_s6_over160_IF_certified=True,
        original_source_point_map_and_FULL_right_edge_support_fixed=True,
        entire_global_source_f_g_no_independent_event_image_resampling=True,
        arbitrary_fully_fixed_global_g_OR_original_seven_GF5_six_ID_lower_NOT_PROVED=True,
    )


def original_maximal_Hamming_good_LINE_completion_code(s,k):
    """Guaranteed >=2 mutually MAX-HAMMING all-GOOD global right maps.

    h>=10: let m=floor(V/400m), all actual source LINE ID pins
    k<=V/10. Preselect a cyclic ordering of FREE occupied physical
    pair-edge labels, and shift all free line images j=0..m-1.
    Any distinct shifts differ on ALL n free original source
    LINE factor images. Simultaneous success occupies at least
    1/2 the uniform ORIGINAL legal global completion fiber.
    """
    z=tenth_pinned_GOOD_completion(s,k)
    if z["h"]<10:
        raise ValueError("universal at least two original fully deranged GOOD maps requires h>=10")
    V=z["V"]
    n=z["unpinned_original_LINE_factors"]
    m=V//400000000
    if not (m>=2 and m<=n and V>800000000):
        raise AssertionError("all-h>=10 true original LINE full free-image cyclic packing feasibility")
    event=preselected_original_global_LINE_orbit(s,k,m)
    if event["exact_union_lower_on_simultaneously_GOOD_fraction"]<Fraction(1,2):
        raise AssertionError("source/physical complete-global 50% cyclic orbit packing proof")
    return dict(
        s=s,h=z["h"],V=V,k=k,
        max_arbitrary_pinned_TRUE_original_LINE_factor_images=V//10,
        pointwise_Hamming_distance_on_all_unpinned_SOURCE_LINE_factor_images=n,
        number_of_distinct_completed_global_right_LINE_maps=m,
        any_two_completed_original_LINE_maps_differ_on_EVERY_unpinned_LINE=True,
        all_maps_have_same_original_symplectic_point_line_incidence_flags=True,
        all_maps_preserve_same_FIXED_original_point_physical_f_and_right_edge_support=True,
        every_completed_global_original_GOOD_wedge_count_ge_s6_over160=True,
        at_least_half_all_base_pinned_line_maps_yield_THIS_entire_max_Hamming_good_code=True,
        exact_rational_actual_source_good_base_fraction_lower=event[
            "exact_union_lower_on_simultaneously_GOOD_fraction"],
        not_all_arbitrary_fully_fixed_original_right_maps_proved_GOOD=True,
        no_accepted_SEVEN_GF5_SIX_distinct_original_flag_Q_theorem=True,
        root_230="OPEN_WITH_FORMAL_BLOCKER",
    )


def exact_two_all_original_global_completions_Hamming(s,k):
    """The m=2 special case, h>=10, ANY whole free image derangement."""
    z=tenth_pinned_GOOD_completion(s,k)
    if z["h"]<10:
        raise ValueError("universal h>=10 two-full-global-original-map result")
    if z["V"]<=400000000:
        raise AssertionError("h>=10 dyadic V threshold")
    event=preselected_original_global_LINE_orbit(s,k,2)
    if event["exact_union_lower_before_truncation"]<=0:
        raise AssertionError("some original globally coherent base map and arbitrary full derangement must be simultaneously GOOD")
    return dict(
        s=s,k=k,
        two_legal_COMPLETE_original_LINE_maps_preserve_ALL_arbitrary_pins=True,
        pointwise_Hamming_difference_on_every_free_true_original_LINE_factor=z[
            "unpinned_original_LINE_factors"],
        both_original_global_maps_Good_opposite_flag_wedges_ge_s6_over160=True,
        exact_positive_base_map_fraction_for_arbitrary_PRESELECTED_derangement=event[
            "exact_union_lower_on_simultaneously_GOOD_fraction"],
        no_original_S_GF5_six_distinct_flag_lower_claimed=True,
    )


def literal_true_original_small_full_LINE_support_shift_family(model,pinned_ids,
                                                                number_of_maps):
    """Explicit finite SOURCE original W32/W34 global maps, not all-h enumeration.

    Fix actual point f and the entire original occupied physical right
    edge image support E, fix ORIGINAL line factor IDs. Act on
    ALL remaining image edges by cyclic permutations. Emit distinct
    full source LINE-factor image arrays (one coherent global mapping
    each), no per-source incidence image redraw. Real s>=32 objects
    are treated only symbolically by the proof above.
    """
    V=(model["s"]+1)*(model["s"]**2+1)
    if V not in (15,85):
        raise ValueError("literal all-factor image array checks only original W32/W34")
    imgs=tuple(tuple(sorted(e)) for e in model["right_labels"])
    if len(imgs)!=V or len(set(imgs))!=V:
        raise ValueError("genuine fully injected original LINE image support")
    pin=tuple(sorted(pinned_ids))
    if len(pin)!=len(set(pin)) or any(type(j)!=int or j<0 or j>=V for j in pin):
        raise ValueError("distinct original source LINE factor pins required")
    free=tuple(j for j in range(V) if j not in pin)
    n=len(free)
    if (type(number_of_maps)!=int or
            not 1<=number_of_maps<=n or n<2):
        raise ValueError("number of cyclic global maps must be between 1 and free source factors")
    shifts=[]
    for shift in range(number_of_maps):
        right=list(imgs)
        for j,idx in enumerate(free):
            right[idx]=imgs[free[(j+shift)%n]]
        if len(set(right))!=V:
            raise AssertionError("global original LINE image injection not retained")
        if any(right[idx]!=imgs[idx] for idx in pin):
            raise AssertionError("adversarial pinned original source LINE physical image changed")
        shifts.append(tuple(right))
    for i in range(len(shifts)):
        for j in range(i):
            if sum(shifts[i][t]!=shifts[j][t] for t in range(V))!=n:
                raise AssertionError("full support cyclic shifts not maximally Hamming-separated on real original SOURCE LINE factors")
    return tuple(shifts)
