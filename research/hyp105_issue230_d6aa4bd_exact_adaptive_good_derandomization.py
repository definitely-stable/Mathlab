"""HYP-105 #230 AA4-BD: constructive conditional-expectation GOOD completion.

Parents: #561 exact genuine-original fixed-f GOOD source weights and
physical clean ordered triples, #563 exact global permutation moments,
#564 ALL f/support adversarial k<=V//1024 partial-source label existence
with R_good >= s^6/512 for h>=5.

NEW: deterministic method of conditional expectations constructs one
WHOLE globally injected original LINE map, extending ALL adversarial
initial source LINE->physical edge pins, with R_good >= its exact
conditional expectation. At EACH next step an ADVERSARY may choose
WHICH not-yet-assigned source LINE ID arrives; this solver picks the
physical edge image maximizing EXACT conditional GOOD potential.
Thus guarantees >=s^6/512 for h>=5,k<=floor(V/1024), for ANY
(adaptive) source factor ORDER, no Monte Carlo or brute-force V! search.

Only initial unlocked-source triples count as guaranteed R_free;
full real original R_good >=R_free for the final SAME global f/g.
The theorem requires access to true-original point-side source triple
weights; enumerating them is polynomial in source input size but may
be prohibitive in practice on huge W3s. No run-time performance claim.
Never claim ALL previously FIXED global g positive or six-ID GF5.
"""
from collections import Counter,defaultdict
from fractions import Fraction
from itertools import combinations

from hyp105_issue230_d6aa4az_quenched_allD_variance import (
    original_line_triple_weights,
)
from hyp105_issue230_d6aa4az_quenched_good_opposite import (
    support_bad_clean_energy,
)
from hyp105_issue230_d6aa4bc_robust_pins import (
    actual_original_pinned_completion_certificate,
    certified_robust_pins_envelope,
)


def _canonical_pair(edge,a):
    if (not isinstance(edge,(tuple,list)) or len(edge)!=2 or
        any(type(v) is not int or v<0 or v>=a for v in edge) or
        edge[0]==edge[1]):
        raise ValueError("actual occupied undirected physical pair required")
    return tuple(sorted(edge))


def _fall(n,k):
    if type(n) is not int or type(k) is not int or k<0 or n<k:
        raise ValueError("cannot sample unassigned globally distinct physical source labels")
    out=1
    for j in range(k):
        out*=n-j
    return out


def physically_clean_opposite_ordered_edge_indices(physical_support,a):
    """Independent literal physical 3-edge construction: center edge,
    left neighbor intersects at one endpoint, right at its OTHER
    endpoint; all edges in ORIGINAL FULL support's AA4-AO CLEAN graph.
    Physically mixed cross-typed vertices are distinct alphabets.
    """
    E=tuple(_canonical_pair(e,a) for e in physical_support)
    if len(set(E))!=len(E):
        raise ValueError("one injective original LINE occupied physical pair image")
    clean=set(support_bad_clean_energy(E,a)["clean_induced_occupied_edges"])
    index={e:i for i,e in enumerate(E)}
    star=[[] for _ in range(a)]
    for e in clean:
        for v in e:
            star[v].append(index[e])
    good=[]
    for e in clean:
        idx=index[e]
        u,v=e
        left=[j for j in star[u] if j!=idx and v not in E[j]]
        right=[j for j in star[v] if j!=idx and u not in E[j]]
        for x in left:
            for y in right:
                if x==y:
                    raise AssertionError("distinct physical 3-source factor pair labels")
                good.append((idx,x,y))
                good.append((idx,y,x))
    if len(set(good))!=len(good):
        raise AssertionError("duplicate ordered clean physical 3-edge witnesses")
    return tuple(good)


def _validate_state(weights,physical_support,a,pins):
    E=tuple(_canonical_pair(e,a) for e in physical_support)
    V=len(E)
    if len(set(E))!=V:
        raise ValueError("physical occupied support must be globally injective")
    if not isinstance(pins,dict):
        raise ValueError("global original source line factor pins must be a mapping")
    index={e:i for i,e in enumerate(E)}
    x={}
    for line,edge in pins.items():
        if type(line) is not int or not 0<=line<V:
            raise ValueError("source original line ID outside range")
        ce=_canonical_pair(edge,a)
        if ce not in index:
            raise ValueError("pinned physical edge outside ORIGINAL complete support")
        x[line]=index[ce]
    if len(set(x.values()))!=len(x):
        raise ValueError("all pinned source LINE physical images must be distinct")
    if not isinstance(weights,dict):
        raise ValueError("original source ordered triple weight ledger must be mapping")
    for ids,number in weights.items():
        if (not isinstance(ids,tuple) or len(ids)!=3 or
            len(set(ids))!=3 or any(type(i) is not int or
            i<0 or i>=V for i in ids) or type(number) is not int or
            number<=0):
            raise ValueError("only positive true original source 3-LINE-ID weights")
    return E,index,x


def exact_global_completion_conditional_GOOD_expectation(
        weights,physical_support,a,pins,*,physical_triples=None):
    """EXACT conditional expectation with ONE uniformly random GLOBAL
    bijection of every remaining source LINE ID to every remaining
    globally occupied physical edge. All ordered original source
    triples may overlap; no independent per-triple image redrawing.

    Sum conditional TRUE ORIGINAL source weights by prescribed
    3-position patterns; physical favorable triple counts by those
    patterns. One explicit scan of physical witnesses, 8 masks each.
    """
    E,index,assigned=_validate_state(weights,physical_support,a,pins)
    V=len(E);n=V-len(assigned)
    free=set(range(V))-set(assigned.values())
    if physical_triples is None:
        physical_triples=physically_clean_opposite_ordered_edge_indices(E,a)
    by_mask=Counter()
    for triple in physical_triples:
        if len(triple)!=3 or len(set(triple))!=3:
            raise ValueError("bad physical good triple witness")
        for mask in range(8):
            if any(triple[slot] not in free for slot in range(3)
                   if not mask&(1<<slot)):
                continue
            key=(mask,tuple(triple[slot] for slot in range(3)
                             if mask&(1<<slot)))
            by_mask[key]+=1
    grouped=Counter()
    for (l0,l1,l2),weight in weights.items():
        ids=(l0,l1,l2)
        mask=sum(1<<slot for slot in range(3)
                 if ids[slot] in assigned)
        key=(mask,tuple(assigned[ids[slot]] for slot in range(3)
                        if mask&(1<<slot)))
        grouped[key]+=weight
    expected=Fraction(0)
    for (mask,chosen),weight in grouped.items():
        remaining=3-mask.bit_count()
        if remaining>n:
            raise AssertionError("unassigned source triple exceeds remaining line labels")
        expected+=Fraction(weight*by_mask.get((mask,chosen),0),
                           _fall(n,remaining))
    return expected


def independent_literal_final_global_GOOD_charge(weights,global_original_line_edges,
                                                  original_full_support,a):
    """No expectation or conditional-table algebra: literal
    3-source LINE-IDs and their ONE FULL GLOBAL images."""
    E=tuple(_canonical_pair(e,a) for e in original_full_support)
    clean=set(support_bad_clean_energy(E,a)["clean_induced_occupied_edges"])
    g=tuple(_canonical_pair(e,a) for e in global_original_line_edges)
    if len(g)!=len(E) or set(g)!=set(E) or len(set(g))!=len(E):
        raise ValueError("not a full globally legal original line labeling")
    total=0
    for (l,k0,k1),w in weights.items():
        e,x,y=g[l],g[k0],g[k1]
        if e not in clean or x not in clean or y not in clean:
            continue
        left=set(e)&set(x);right=set(e)&set(y)
        if len(left)==len(right)==1 and left!=right:
            total+=w
    return total


def choose_one_adaptive_original_line_image(
        weights,physical_support,a,pins,source_line_id,*,physical_triples=None):
    """One turn in an adversarial SOURCE LINE arrival order.

    The user/adversary chooses the NEXT unpinned line factor ID.
    The solver picks its physical occupied edge image maximizing
    exact future conditional charge, checking all candidate images.
    Law of total expectation is certified via integer/Fraction equality:
        (1/n)sum_candidate E[R|pins, line=e] = E[R|pins].
    Therefore chosen expectation NEVER decreases. Physical right
    support and previous globally pinned source assignment unchanged.
    """
    E,index,old=_validate_state(weights,physical_support,a,pins)
    V=len(E)
    if type(source_line_id) is not int or not 0<=source_line_id<V or source_line_id in old:
        raise ValueError("next real original LINE ID must be UNASSIGNED")
    physical_triples=(physically_clean_opposite_ordered_edge_indices(E,a)
                      if physical_triples is None else physical_triples)
    prior=exact_global_completion_conditional_GOOD_expectation(
        weights,E,a,pins,physical_triples=physical_triples)
    free=tuple(i for i in range(V) if i not in set(old.values()))
    values=[]
    for candidate in free:
        trial=dict(pins);trial[source_line_id]=E[candidate]
        after=exact_global_completion_conditional_GOOD_expectation(
            weights,E,a,trial,physical_triples=physical_triples)
        values.append((candidate,after))
    if sum((v for _,v in values),Fraction())!=len(free)*prior:
        raise AssertionError("ONE GLOBAL full-permutation conditional expectation tower failed")
    chosen,maxval=min(values,key=lambda pair:(-pair[1],pair[0]))
    if maxval<prior:
        raise AssertionError("a deterministic globally legal next edge must preserve expectation")
    nextpins=dict(pins);nextpins[source_line_id]=E[chosen]
    return {
        "original_line_source_factor_ID_chosen_by_ADVERSARY":source_line_id,
        "globally_legal_new_physical_edge":E[chosen],
        "prefix_exact_conditional_expectation":prior,
        "after_exact_conditional_expectation":maxval,
        "complete_global_source_line_map_pins_after_step":nextpins,
        "candidate_expected_values":tuple((E[j],v) for j,v in values),
        "uniform_average_of_all_possible_assignments_equals_previous":True,
        "adversarial_order_allowed_but_physical_labels_chosen_by_algorithm":True,
    }


def constructive_true_original_GOOD_partial_line_completion(
        model,initial_pins,*,source_order=None,max_steps=None,
        verify_all_h_floor=True):
    """Deterministically derandomize parent's genuine ORIGINAL W3s
    pinned-completion result into one REAL complete global g.

    If max_steps is not None, returns valid preserved partial original
    pins with nondecreasing exact conditional expectation (useful for
    expensive W34 checks), NOT a completed-map claim.

    For h>=5 and k<=V//1024, the all-global theorem guarantees
    R_good(final)>=R_free(final)>=E[R_free|initial pins]>=s6/512.
    Smaller genuine W32/W34 are directly tested as computational
    falsifiers only; no blanket s>=2 s6/512 theorem asserted.
    """
    s=model["s"]
    V=(s+1)*(s*s+1)
    E=tuple(tuple(sorted(e)) for e in model["right_labels"])
    a=model["a"]
    if len(E)!=V:
        raise ValueError("original LINE global support must have V physical edges")
    _validate_state({},E,a,initial_pins)
    if not isinstance(initial_pins,dict):
        raise ValueError("initial source pins")
    original_pins=dict(initial_pins)
    if verify_all_h_floor and s>=32:
        certified_robust_pins_envelope(s,len(initial_pins))
    original_source=original_line_triple_weights(model,clean_only=True)
    weights={key:value for key,value in original_source.items()
             if not(set(key)&set(initial_pins))}
    physical=physically_clean_opposite_ordered_edge_indices(E,a)
    initial_exact=exact_global_completion_conditional_GOOD_expectation(
        weights,E,a,initial_pins,physical_triples=physical)
    if verify_all_h_floor and s>=32:
        previous=actual_original_pinned_completion_certificate(model,initial_pins)
        if initial_exact!=previous["mean_unpinned_source_good_wedges"]:
            raise AssertionError("prior independent pinned true-original exact mean discrepancy")
        if initial_exact<Fraction(s**6,512):
            raise AssertionError("all-h pinned deterministic initial floor violated")
    if source_order is None:
        source_order=tuple(i for i in range(V) if i not in original_pins)
    else:
        source_order=tuple(source_order)
        if set(source_order)!=set(range(V))-set(original_pins) or len(source_order)!=V-len(original_pins):
            raise ValueError("exactly each remaining ORIGINAL source LINE ID once")
    if max_steps is not None:
        if type(max_steps) is not int or not 0<=max_steps<=len(source_order):
            raise ValueError("nonnegative valid finite step budget")
        source_order=source_order[:max_steps]
    current=dict(original_pins)
    hist=[]
    for line_id in source_order:
        v=choose_one_adaptive_original_line_image(
            weights,E,a,current,line_id,physical_triples=physical)
        current=v["complete_global_source_line_map_pins_after_step"]
        hist.append({
            "source_original_line_ID":line_id,
            "chosen_occupied_physical_edge":v["globally_legal_new_physical_edge"],
            "before":v["prefix_exact_conditional_expectation"],
            "after":v["after_exact_conditional_expectation"],
        })
    final=exact_global_completion_conditional_GOOD_expectation(
        weights,E,a,current,physical_triples=physical)
    if final<initial_exact:
        raise AssertionError("exact original conditional expectation monotonicity")
    complete=len(current)==V
    actual=None;full_actual=None;global_line_images=None
    if complete:
        global_line_images=tuple(tuple(current[i]) for i in range(V))
        actual=independent_literal_final_global_GOOD_charge(
            weights,global_line_images,E,a)
        full_actual=independent_literal_final_global_GOOD_charge(
            original_source,global_line_images,E,a)
        if Fraction(actual)!=final or full_actual<actual:
            raise AssertionError("real original source GOOD 3flag expectation not materialized")
    return {
        "s":s,"V":V,"initial_fixed_adversarial_original_LINE_ID_to_edge":original_pins,
        "fixed_original_point_f_unchanged":True,
        "fixed_original_line_physically_occupied_E_unchanged":True,
        "deterministic_algorithm_adaptive_original_LINE_ID_arrival_order":tuple(source_order),
        "conditional_good_wedge_source_3flag_initial_mean":initial_exact,
        "conditional_good_wedge_source_3flag_final_potential":final,
        "all_real_original_source_global_line_pins_after_steps":current,
        "steps":tuple(hist),
        "is_COMPLETE_legal_global_original_LINE_map":complete,
        "completed_GLOBAL_original_line_source_factor_images":global_line_images,
        "completed_true_original_FREE_good_opposite_threeflag_charge":actual,
        "completed_true_original_ALL_good_opposite_threeflag_charge":full_actual,
        "global_unpinned_GOOD_at_least_original_conditional_mean_if_complete":
            complete and Fraction(actual)>=initial_exact,
        "s_ge32_initial_k_le_V_over1024_implies_constructed_GOOD_ge_s6_over512":
            complete and verify_all_h_floor and s>=32,
        "algorithm_may_be_expensive_polynomial_enumeration_not_scalable_promised":True,
        "arbitrary_fully_FIXED_g_positive_not_proved":True,
        "selected_seven_GF5_six_original_incidence_ID_Q_NOT_PROVED":True,
        "root230_Branch_A_B_C_OPEN":True,
    }
