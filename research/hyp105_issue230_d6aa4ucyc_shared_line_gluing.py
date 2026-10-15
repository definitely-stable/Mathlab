"""HYP-105 #230 / D6-AA4-U-CYC: exact shared-line C6 gluing kernel.

Fix ONE arbitrary true ORIGINAL W(3,s) complete globally injected POINT
map f. Each original six-incidence D6-eligible Q has six distinct
original point/line factors and a physical left COLUMN connected C6,
which induces a 6-cycle on the SIX ACTUAL ORIGINAL LINE factor IDs.

For any TWO such Q0,Q1 with r=0..6 shared original line factors,
their joint D6 probability under ONE uniformly random complete global
line injection g into K_a is an exact normalized integer-valued
falling-factorial polynomial, depending on the RELATIVE cyclic gluing
of shared line IDs, not merely r:

  P_g[D6(Q0) & D6(Q1) | f]
    = (a)_6 / (K)_(12-r) * sum_{k=0}^6 c_{tau,k} (a-6)_k.

Here tau is the canonical two-C6 vertex-gluing diagram. The integer
c_{tau,k} counts assignments of the SIX right physical COORDINATE
symbols of the second cycle that use exactly k new symbols beyond
six already used by the first, with canonical new-symbol order,
shared original LINE factor physical pair labels identical and all
12-r source-line physical pair labels globally distinct.

Unlike previous AA4-T-CYC, r>=1 is fully supported. Genuine ORIGINAL
W32 anchors, independent brute enumeration, and actual globally
completed two-Q historical GF5 D6 witnesses accompany the formula.

A whole 21,186-Q anchored row may be aggregated EXACTLY, but NOT
confused with the 21,186^2 full pair histogram, all-h global
conditional variance, or min_(f,g) S_s Omega(s^6).
"""
from collections import Counter, defaultdict
from functools import lru_cache
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, perm

from hyp105_issue230_d6aa4r_quenched_original_d6 import _params
from hyp105_issue230_d6aa4tcyc_fixed_f_d6_pair import (
    genuine_W32_fixed_f_original_connected_left_Q,
    exact_one_sided_fixed_f_disjoint_LINE_D6_kernel,
)


def _orientations(cycle):
    cycle=tuple(cycle)
    if len(cycle)!=6 or len(set(cycle))!=6:
        raise ValueError("six different ACTUAL original source LINE IDs required")
    return tuple(tuple(cycle[(base+direction*i)%6] for i in range(6))
                 for base in range(6) for direction in (1,-1))


def canonical_two_source_C6_gluing(first_cycle,second_cycle):
    """Exact isomorphism under independent D6 rotations/reflections and
    canonical renumbering of Q1 source lines not found in the first.
    The two true Q stay ORDERED, only cyclic representation changes.
    """
    first=tuple(first_cycle);second=tuple(second_cycle)
    if len(first)!=6 or len(second)!=6 or len(set(first))!=6 or len(set(second))!=6:
        raise ValueError("two genuine six-DISTINCT-original-line cycles required")
    best=None
    for first_orientation in _orientations(first):
        inverse={v:i for i,v in enumerate(first_orientation)}
        for second_orientation in _orientations(second):
            extra={}
            result=[]
            for line in second_orientation:
                if line in inverse:
                    result.append(inverse[line])
                else:
                    if line not in extra:
                        extra[line]=6+len(extra)
                    result.append(extra[line])
            candidate=tuple(result)
            if best is None or candidate<best:
                best=candidate
    if best is None or len(set(best))!=6:
        raise AssertionError("actual original two-C6 gluing canonicalization failed")
    if len(set(first)&set(second))!=sum(v<6 for v in best):
        raise AssertionError("actual original shared-line count not preserved by canon")
    return best


@lru_cache(maxsize=None)
def exact_second_cycle_coordinate_color_coefficients(gluing):
    """Independent-of-a canonical coefficient enumerator.

    FIRST original line cycle vertices = (0,1,2,3,4,5).
    Its physical right coordinate colors on cyclic EDGES are fixed
    exactly at (0,1,2,3,4,5). The physical image of vertex i is
    unordered pair (color[i-1],color[i]).
    Second cycle physical coordinate colors are INJECTIVE within Q1.
    A color can be one of old 0..5, or a fresh 6,7,... (always
    distinct; assigned in increasing second-cycle position order).
    Each canonical fresh assignment of k second colors has exactly
    (a-6)_k realizations in the physical alphabet, preserving
    uniqueness of all complete globally injected right maps g.
    """
    gluing=tuple(gluing)
    if len(gluing)!=6 or len(set(gluing))!=6:
        raise ValueError("true C6 gluing has six DISTINCT second original lines")
    if any(type(v) is not int or not 0<=v<12 for v in gluing):
        raise ValueError("gluing original source line indices out of 0..11")
    # New original line factors must use consecutive 6..6+t-1.
    extras=tuple(v for v in gluing if v>=6)
    if set(extras)!=set(range(6,6+len(extras))):
        raise ValueError("gluing must be canonical and source-line-new IDs consecutive")
    first={i:tuple(sorted(((i-1)%6,i))) for i in range(6)}
    coefficients=[0]*7
    colors=[0]*6
    source_second={}
    visited=0

    def accept(k):
        nonlocal visited
        visited+=1
        for pos,line in enumerate(gluing):
            source_second[line]=tuple(sorted((colors[(pos-1)%6],colors[pos])))
        if any(source_second[line]!=first[line] for line in range(6) if line in source_second):
            return
        if len(set(source_second.values())|set(first.values()))!=12-sum(x<6 for x in gluing):
            return
        coefficients[k]+=1

    def search(pos,old_used,new_count):
        if pos==6:
            accept(new_count)
            return
        for old in range(6):
            if not (old_used>>old)&1:
                colors[pos]=old
                search(pos+1,old_used|(1<<old),new_count)
        # Use the NEXT fresh symbol only: this is a canonical orbit
        # representative, not all its (a-6)_k concrete assignments.
        colors[pos]=6+new_count
        search(pos+1,old_used,new_count+1)

    search(0,0,0)
    if visited!=13327:
        raise AssertionError("all 13,327 injective old/fresh second color patterns not examined")
    if not 0<=sum(coefficients)<=visited:
        raise AssertionError("invalid count of physically consistent C6 gluing")
    return tuple(coefficients)


def exact_two_D6_gluing_kernel(s,first_cycle,second_cycle):
    """ALL-h exact true-original conditional second probability for
    ONE fixed globally injected f, ANY shared source-L cyclic pattern.
    """
    V,a,K,m=_params(s)
    gluing=canonical_two_source_C6_gluing(first_cycle,second_cycle)
    r=sum(v<6 for v in gluing)
    coefficients=exact_second_cycle_coordinate_color_coefficients(gluing)
    ordered_remaining=sum(value*perm(a-6,k)
                          for k,value in enumerate(coefficients)
                          if a-6>=k)
    complete=(perm(a,6)*ordered_remaining)
    denom=perm(K,12-r)
    joint=Fraction(complete,denom)
    p=Fraction(perm(a,6),perm(K,6))
    if joint<0 or joint>p:
        raise AssertionError("true two D6 joint probability outside marginal range")
    if r==0:
        previous=exact_one_sided_fixed_f_disjoint_LINE_D6_kernel(s)
        if joint!=Fraction(previous[
            "exact_two_Q_D6_joint_probability_disjoint_original_LINE_factors"]):
            raise AssertionError("shared-line general gluing kernel != independent AA4-T-CYC r0")
    if r==6 and gluing==tuple(range(6)) and joint!=p:
        raise AssertionError("same six source lines and same C6 must represent identical D6 event")
    return {
        "s":s,"a":a,"K":K,
        "source_line_shared_count":r,
        "canonical_ORIGINAL_line_C6_gluing":gluing,
        "integer_falling_factorial_color_coefficients_k0_to_k6":coefficients,
        "number_second_injection_right_color_tuples_given_first":ordered_remaining,
        "joint_probability_one_complete_GLOBAL_g":str(joint),
        "one_event_true_original_D6_probability":str(p),
        "conditional_second_probability_after_first_D6":str(joint/p),
        "point_source_factor_overlap_unrestricted":True,
        "line_source_factor_gluing_positions_required":True,
        "same_one_global_source_line_label_map":True,
        "fully_computable_for_any_true_GQ_order_and_gluing":True,
        "full_conditional_second_moment_PROVED":False,
        "all_maps_global_seven_GF5_lower_PROVED":False,
    }


def brute_given_first_SIX_physical_right_color_assignments(gluing):
    """INDEPENDENT 6! concrete physical-color brute at a=6; no
    old/fresh canonical enumeration and no coefficient reuse.
    """
    first=tuple(range(6))
    second=tuple(gluing)
    if len(second)!=6 or len(set(second))!=6:
        raise ValueError("bad source line gluing")
    old={line:tuple(sorted(((i-1)%6,i))) for i,line in enumerate(first)}
    count=0
    for palette in permutations(range(6)):
        secondedges={line:tuple(sorted((palette[(i-1)%6],palette[i])))
                     for i,line in enumerate(second)}
        if any(secondedges[x]!=old[x] for x in set(first)&set(second)):
            continue
        if len(set(old.values())|set(secondedges.values()))!=len(set(first)|set(second)):
            continue
        count+=1
    return count


def _actual_original_Q_line_cycle(model,Q):
    """Genuine left physical 6-column coordinate dual graph on the SIX
    source original line IDs. Not a graph of physical source paths.
    """
    inc=tuple(tuple(x) for x in model["incidences"])
    f=tuple(tuple(x) for x in model["left_labels"])
    if len(Q)!=6 or len(set(Q))!=6:
        raise ValueError("six real distinct original incidence IDs required")
    ends=tuple(inc[j] for j in Q)
    lines=tuple(l for p,l in ends)
    if len(set(lines))!=6 or len({p for p,l in ends})!=6:
        raise ValueError("true ORIGINAL AA distinct point and line factors required")
    graph={line:set() for line in lines}
    for physical_coordinate in range(model["a"]):
        positions=[i for i,(p,l) in enumerate(ends) if physical_coordinate in f[p]]
        if not positions:
            continue
        if len(positions)!=2:
            raise ValueError("not a physical six-coordinate left 2factor")
        u,v=(lines[j] for j in positions)
        if u==v or v in graph[u]:
            raise ValueError("not a simple source-line C6")
        graph[u].add(v);graph[v].add(u)
    if any(len(n)!=2 for n in graph):
        raise ValueError("not a genuine left dual C6")
    start=min(graph)
    direction=min(graph[start])
    cycle=(start,direction)
    while len(cycle)<6:
        options=graph[cycle[-1]]-{cycle[-2]}
        if len(options)!=1:raise ValueError("broken true line cycle")
        next_source=next(iter(options))
        if next_source in cycle:raise ValueError("premature short source-line cycle")
        cycle+=(next_source,)
    if start not in graph[cycle[-1]]:
        raise ValueError("not connected actual original six-column C6")
    return cycle


def genuine_W32_anchored_FULL_shared_line_D6_kernel(scheme):
    """EXACT ONE true W32 anchored 21,186-element joint D6 probability
    row across ALL source L-overlap sectors r=0..6, using shared g.
    It is NOT the full 21,186² original source pair histogram.
    """
    model,rows=genuine_W32_fixed_f_original_connected_left_Q(scheme)
    anchor=next(iter(rows))
    first=_actual_original_Q_line_cycle(model,anchor)
    matrix=Counter()
    by_overlap=Counter()
    representative={}
    anchored_sum=Fraction(0)
    n_positive=n_zero=0
    for Q in rows:
        second=_actual_original_Q_line_cycle(model,Q)
        signature=canonical_two_source_C6_gluing(first,second)
        matrix[signature]+=1
        r=sum(v<6 for v in signature)
        by_overlap[r]+=1
        if signature not in representative:
            representative[signature]=Q
    all_certificates={}
    for signature, count in sorted(matrix.items()):
        kernel=exact_two_D6_gluing_kernel(2,tuple(range(6)),signature)
        probability=Fraction(kernel["joint_probability_one_complete_GLOBAL_g"])
        anchored_sum+=count*probability
        all_certificates[signature]=kernel
        if probability>0:n_positive+=count
        else:n_zero+=count
    if n_positive+n_zero!=21186 or sum(by_overlap.values())!=21186:
        raise AssertionError("missed genuine W32 all 21,186 anchored source D6 joint events")
    if by_overlap[0]!=305:
        raise AssertionError("AA4-T-CYC genuine ORIGINAL W32 anchored disjoint-line count drift")
    if by_overlap[6]<1:
        raise AssertionError("missing diagonal genuine ORIGINAL D6 Q")
    if Fraction(all_certificates[
        canonical_two_source_C6_gluing(first,first)][
        "joint_probability_one_complete_GLOBAL_g"])!=Fraction(1,5005):
        raise AssertionError("true original anchored D6 diagonal conditional joint mismatch")
    return {
        "scheme":scheme,
        "actual_anchor_six_ORIGINAL_incidence_IDs":anchor,
        "actual_anchor_canonical_six_original_LINE_factor_cycle":first,
        "source_Q_in_true_original_anchored_row":21186,
        "source_right_LINE_overlap_counts":dict(sorted(by_overlap.items())),
        "distinct_two_C6_gluing_isomorphism_types":len(matrix),
        "exact_original_gluing_type_counts":{
            ",".join(map(str,k)):v for k,v in sorted(matrix.items())},
        "exact_all_21186_genuine_Q_anchored_joint_D6_probability_sum":str(anchored_sum),
        "number_positive_joint_probability_pairs_from_this_anchor":n_positive,
        "number_zero_joint_probability_pairs_from_this_anchor":n_zero,
        "literal_true_original_gluing_representatives":{
            ",".join(map(str,k)):list(Q) for k,Q in representative.items()},
        "partial_anchored_row_NOT_full_conditional_second_moment":True,
        "original_source_point_overlap_unrestricted":True,
        "same_one_FULL_global_right_g_probability_model":True,
        "root_A":"OPEN","root_B":"OPEN",
    }


def independent_W32_TWO_real_D6_global_right_completion(scheme,*,shared_count=2,require_positive=True):
    """Find genuine Q0, Q1 with specified overlapping original LINE IDs
    and canonical gluing of requested sign. For a=6 a positive kernel
    constructs ONE COMPLETE right map g accepting BOTH actual GF5 D6.
    Negative kernel is a strict positional NO-GO for this actual pair.
    """
    from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked
    model,rows=genuine_W32_fixed_f_original_connected_left_Q(scheme)
    Q0=next(iter(rows))
    cycle0=_actual_original_Q_line_cycle(model,Q0)
    target=None
    looked_at=0
    for Q1 in rows:
        cycle1=_actual_original_Q_line_cycle(model,Q1)
        sig=canonical_two_source_C6_gluing(cycle0,cycle1)
        if sum(v<6 for v in sig)!=shared_count:
            continue
        if (brute_given_first_SIX_physical_right_color_assignments(sig)>0)!=require_positive:
            continue
        target=(Q1,cycle1,sig)
        break
    if target is None:
        raise AssertionError("no actual genuine W32 source-line gluing with requested sign")
    Q1,cycle1,sig=target
    coeff=exact_second_cycle_coordinate_color_coefficients(sig)
    brute=brute_given_first_SIX_physical_right_color_assignments(sig)
    if brute!=coeff[0]:
        raise AssertionError("independent literal physical 6-color brute differs from canonical coefficient")
    result={
        "scheme":scheme,
        "Q0_original_six_incidence_IDs":Q0,
        "Q1_original_six_incidence_IDs":Q1,
        "original_line_C6_gluing_signature":sig,
        "shared_original_LINE_source_factors":shared_count,
        "exact_independent_SIX_physical_color_bruteforce_count":brute,
        "all_h_gluing_color_coefficients":coeff,
        "positive_genuine_joint_D6":require_positive,
        "one_complete_g_construction":None,
    }
    if not require_positive:
        if exact_two_D6_gluing_kernel(2,cycle0,cycle1)[
            "joint_probability_one_complete_GLOBAL_g"]!="0":
            raise AssertionError("claimed actual zero gluing not zero at K6")
        return result
    # First physical-coordinate labels on original line-cycle EDGES are
    # color i (0..5), hence original line cycle vertex i has edge (i-1,i).
    source0={l:tuple(sorted(((i-1)%6,i))) for i,l in enumerate(cycle0)}
    fixed_six_first_colors=tuple(range(6))
    source1=None
    for palette in permutations(range(6)):
        images={l:tuple(sorted((palette[(i-1)%6],palette[i])))
                for i,l in enumerate(cycle1)}
        if any(source0[l]!=images[l] for l in set(source0)&set(images)):
            continue
        if len(set(source0.values())|set(images.values()))!=len(set(source0)|set(images)):
            continue
        source1=images;break
    if source1 is None:
        raise AssertionError("positive coefficient but no actual full-global-right completion")
    g=[None]*15
    for l,image in tuple(source0.items())+tuple(source1.items()):
        if g[l] is not None and g[l]!=image:
            raise AssertionError("original shared LINE factor got inconsistent physical label")
        g[l]=image
    palette=tuple(combinations(range(6),2))
    missing=iter(e for e in palette if e not in set(e for e in g if e is not None))
    for l in range(15):
        if g[l] is None:g[l]=next(missing)
    g=tuple(g)
    if set(g)!=set(palette) or len(set(g))!=15:
        raise AssertionError("right global source-line physical injection broken")
    inc=model["incidences"];f=model["left_labels"]
    tags=(classify_seven_prechecked(Q0,f,g,inc),
          classify_seven_prechecked(Q1,f,g,inc))
    if tags!=("D6","D6"):
        raise AssertionError("historical ORIGINAL full GF5 classifier rejects actual two simultaneous D6")
    result["one_complete_g_construction"]=g
    result["historical_original_Q_two_GF5_tags"]=tags
    return result


def report(scheme=None):
    val={
        "slice":"HYP105-ISSUE230-D6-AA4-U-CYC-SHARED-LINE-GLUING",
        "all_h_two_C6_original_SHARED_SOURCE_LINE_gluing_polynomial_exact":True,
        "one_GLOBAL_complete_right_g_and_one_FIXED_source_point_f":True,
        "shared_line_C6_cyclic_positions_required_NOT_just_cardinality":True,
        "all_h_exact_gluing_k0_to_k6_falling_factorial_form":True,
        "disjoint_original_lines_reduces_to_earlier_AA4_T_CYC":True,
        "real_physical_SIX_color_brute_crosschecks":{
          "r0":brute_given_first_SIX_physical_right_color_assignments((6,7,8,9,10,11)),
          "r2_possible":brute_given_first_SIX_physical_right_color_assignments((0,6,3,7,8,9)),
          "r2_impossible":brute_given_first_SIX_physical_right_color_assignments((0,2,6,7,8,9)),
          "r6_identical":brute_given_first_SIX_physical_right_color_assignments((0,1,2,3,4,5)),
          "r6_incompatible":brute_given_first_SIX_physical_right_color_assignments((0,1,2,3,5,4)),
        },
        "all_h_minimax_original_S_Omega_s6_PROVED":False,
        "full_fixed_f_conditional_second_moment_PROVED":False,
        "root_A":"OPEN","root_B":"OPEN",
    }
    if scheme is not None:
        val["true_original_W32_anchor"]=genuine_W32_anchored_FULL_shared_line_D6_kernel(scheme)
        val["true_original_W32_joint_r2_positive"] = independent_W32_TWO_real_D6_global_right_completion(
            scheme,shared_count=2,require_positive=True)
        val["true_original_W32_joint_r2_zero"] = independent_W32_TWO_real_D6_global_right_completion(
            scheme,shared_count=2,require_positive=False)
    return val


if __name__=="__main__":
    import argparse,json
    p=argparse.ArgumentParser()
    p.add_argument("--scheme",choices=("S68","S72"))
    args=p.parse_args()
    print(json.dumps(report(args.scheme),indent=2,sort_keys=True))
