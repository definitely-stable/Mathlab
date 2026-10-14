"""HYP-105 JPKC-014 J50: exact conditional injective choice-star assignment bound.

Given genuine one-movable-factor ORIGINAL Q disjoint stars, their per-line
physical-image ORIGINAL positive-Q counts are additive, while images must
be injective. The true all-h conditional lower bound is the minimum-cost
INJECTIVE assignment on the finite source block, not sum of row minima.
The solver is independently combinatorial (no seven_census reuse).
"""
from functools import lru_cache


def exact_injective_choice_star_lower(cost_by_anchor, images, *,
                                      max_block=12):
    """Solve min sum_r q[r,g(r)] across distinct source images exactly.

    Missing anchor lines are absent from cost_by_anchor and contribute 0.
    Any injection on selected lines extends to a full moving block if
    the original physical pair image set has >= the full block size.
    Caller must prove ORIGINAL Q support-disjointness and existence
    of positive source cylinder witnesses for each real q entry.
    """
    if not isinstance(cost_by_anchor,dict) or not isinstance(images,(tuple,list)):
        raise ValueError("original source line cost table and image set required")
    if type(max_block)!=int or not 1<=max_block<=12:
        raise ValueError("positive exact factor assignment block budget required")
    labels=tuple(tuple(e) for e in images)
    if (not labels or len(labels)>max_block or len(set(labels))!=len(labels)
            or any(len(e)!=2 or any(type(c)!=int or c<0 for c in e)
                   or e[0]>=e[1] for e in labels)):
        raise ValueError("distinct canonical original physical pair images required")
    anchors=tuple(sorted(cost_by_anchor))
    if len(anchors)>len(labels) or any(type(r)!=int or r<0 for r in anchors):
        raise ValueError("distinct original source line anchors fit injective images")
    full=set(labels)
    rows=[]
    for r in anchors:
        costs=cost_by_anchor[r]
        if not isinstance(costs,dict) or set(costs)!=full:
            raise ValueError("complete exact ORIGINAL source line image cost row required")
        row=[]
        for e in labels:
            value=costs[e]
            if type(value)!=int or value<1:
                raise ValueError("positive integer ORIGINAL Q witness count required")
            row.append(value)
        rows.append(tuple(row))

    @lru_cache(maxsize=None)
    def solve(i,occupied):
        if i==len(anchors):
            return (0,())
        best=None
        for j,e in enumerate(labels):
            bit=1<<j
            if occupied&bit:
                continue
            suffix,tail=solve(i+1,occupied|bit)
            candidate=(rows[i][j]+suffix,(j,)+tail)
            if best is None or candidate<best:
                best=candidate
        if best is None:
            raise AssertionError("one-to-one ORIGINAL source image assignment impossible")
        return best

    optimum,selected=solve(0,0)
    if len(selected)!=len(anchors) or len(set(selected))!=len(selected):
        raise AssertionError("injective star solution reused a physical image")
    independent=sum(min(row) for row in rows)
    if optimum<independent:
        raise AssertionError("real globally injective min below row-wise minimum")
    return {
        "exact_injective_min_original_Q_lower":optimum,
        "sum_of_independent_original_source_star_row_minima":independent,
        "strict_injection_assignment_gain":optimum-independent,
        "selected_original_line_to_physical_image":
            tuple((r,labels[j]) for r,j in zip(anchors,selected)),
        "all_selected_original_source_images_distinct":True,
        "exact_assignment_dynamic_states":solve.cache_info().misses,
        "J50_all_h_conditional_injection_assignment_lemma":True,
        "unconditional_all_h_star_existence_proved":False,
    }
