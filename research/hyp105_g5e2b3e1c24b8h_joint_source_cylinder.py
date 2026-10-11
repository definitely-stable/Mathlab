"""HYP-105 C24-B8-H: joint original-source cylinder lower certificates.

Finite/ALL-h combinatorial lemma, not a universal positive all-f,g S bound.
For any fixed partial GLOBAL right injection and a disjoint partition of
nonnegative ORIGINAL source contributions into buckets, the sum of per-bucket
minimum over locally injective completions is a POINTWISE LOWER on the true
joint score for every entire globally consistent completion.

This does not bound P2 and R separately: on each genuine completion it bounds
P2+R = S-mu. For a small remaining alphabet we can ALSO compute exact min on
that constrained cylinder. Large instances fail CLOSED under explicit budgets.
"""
from collections import defaultdict
from itertools import permutations
from math import factorial


def falling(n,k):
    if type(n) is not int or type(k) is not int or n<0 or not 0<=k<=n:
        raise ValueError("nonnegative valid falling factorial arguments needed")
    answer=1
    for i in range(k):
        answer*=n-i
    return answer


def validate_problem(records, pinned, n, m):
    if (type(n) is not int or type(m) is not int or not 2<=n<=m
            or not isinstance(pinned,dict)
            or any(type(i) is not int or not 0<=i<n or type(e) is not int
                   or not 0<=e<m for i,e in pinned.items())
            or len(set(pinned.values()))!=len(pinned)):
        raise ValueError("one legal partial global original-right injection needed")
    if (not isinstance(records,(list,tuple)) or
            any(not isinstance(row,tuple) or len(row)!=3 for row in records)):
        raise ValueError("records must be (support,positive_weight,payload) triples")
    for support,weight,_ in records:
        if (not isinstance(support,tuple) or
                tuple(sorted(set(support)))!=support or
                not support or
                any(type(i) is not int or not 0<=i<n for i in support)
                or type(weight) is not int or weight<=0):
            raise ValueError("original support must be canonical and weight positive")
    free=tuple(i for i in range(n) if i not in pinned)
    unused=tuple(e for e in range(m) if e not in pinned.values())
    return free,unused


def _partition(records, free):
    remain=set(free)
    fibers=defaultdict(list)
    for support,weight,payload in records:
        residual=tuple(i for i in support if i in remain)
        fibers[residual].append((weight,payload))
    return tuple((key,tuple(values)) for key,values in sorted(fibers.items()))


def _merge_fibers(fibers,max_union_support):
    """Merge entire nonoverlapping source buckets; never split a source weight."""
    groups=[(key,items) for key,items in fibers]
    while True:
        options=[]
        for i in range(len(groups)):
            for j in range(i+1,len(groups)):
                union=tuple(sorted(set(groups[i][0])|set(groups[j][0])))
                if len(union)<=max_union_support:
                    # Prefer overlapping supports, then smaller union.
                    overlap=len(set(groups[i][0])&set(groups[j][0]))
                    options.append((len(union),-overlap,i,j,union))
        if not options:
            break
        _,_,i,j,union=min(options)
        combined=(union,groups[i][1]+groups[j][1])
        groups=[group for index,group in enumerate(groups) if index not in (i,j)]
        groups.append(combined)
        groups.sort(key=lambda r:r[0])
    return tuple(groups)


def _group_minimum(group,pinned,unused,evaluate,counter,max_record_evaluations):
    support,items=group
    best=None
    for images in permutations(unused,len(support)):
        assign={**pinned,**dict(zip(support,images))}
        cost=0
        for weight,payload in items:
            counter[0]+=1
            if counter[0]>max_record_evaluations:
                raise ValueError("source evaluation budget exceeded (fail closed)")
            accepted=evaluate(payload,assign)
            if type(accepted) not in (bool,int) or accepted not in (0,1):
                raise ValueError("source evaluator must return Boolean acceptance")
            cost+=weight*accepted
        if best is None or cost<best:
            best=cost
    if best is None:
        raise ValueError("no local legal injections for a source group")
    return best


def joint_cylinder_certificate(records,pinned,n,m,evaluate,*,
                               max_union_support=3,
                               include_exact=True,
                               max_group_states=10000,
                               max_record_evaluations=25000000):
    """Certify support-wise, coupled bucket and optional exact cylinder minima.

    The support of each record MUST list all original-right labels read by
    evaluate(payload,assignment); the caller's adapter must validate this.
    Source functions are Boolean and nonnegative with ORIGINAL multiplicity.
    Local states remain injections into the SAME currently unused host edges,
    relaxing consistency only BETWEEN distinct buckets.
    """
    free,unused=validate_problem(records,pinned,n,m)
    if (type(max_union_support) is not int or
            not 0<=max_union_support<=len(free) or
            type(max_group_states) is not int or max_group_states<1 or
            type(max_record_evaluations) is not int or max_record_evaluations<1
            or type(include_exact) is not bool):
        raise ValueError("explicit nonnegative integer bounded-state controls required")
    if not callable(evaluate):
        raise ValueError("source acceptance evaluator required")
    fibers=_partition(records,free)
    merged=_merge_fibers(fibers,max_union_support)
    stages=[fibers,merged]
    if include_exact:
        # All records in one group, using the WHOLE residual right alphabet.
        stages.append(((free,tuple((w,p) for _,w,p in records)),))
    budgets=[sum(falling(len(unused),len(support)) for support,_ in groups)
             for groups in stages]
    if any(x>max_group_states for x in budgets):
        raise ValueError("completion-state budget exceeded (fail closed)")
    counter=[0]
    values=[]
    for stage in stages:
        minima=tuple(_group_minimum(group,pinned,unused,evaluate,counter,
                                    max_record_evaluations) for group in stage)
        values.append(sum(minima))
    if values[0]>values[1] or (include_exact and values[1]>values[2]):
        raise AssertionError("joint relaxation monotonicity violated")
    result={
        "pinned_original_lines":len(pinned),
        "unassigned_original_lines":len(free),
        "remaining_physical_edges":len(unused),
        "original_source_records":len(records),
        "original_source_multiplicity":sum(w for _,w,_ in records),
        "independent_exact_support_groups":len(fibers),
        "coupled_support_groups":len(merged),
        "max_coupled_group_support":max((len(u) for u,_ in merged),default=0),
        "supportwise_pointwise_seven_lower":values[0],
        "coupled_pointwise_seven_lower":values[1],
        "exact_cylinder_minimum":values[2] if include_exact else None,
        "independent_completion_states_evaluated":budgets[0],
        "coupled_completion_states_evaluated":budgets[1],
        "whole_completion_states_evaluated":budgets[2] if include_exact else None,
        "weighted_source_acceptance_evaluations":counter[0],
        "all_completions_share_one_global_right_injection":True,
        "not_a_global_all_g_unpinned_lower":bool(pinned),
        "not_proof_all_h_omega_s6":True,
    }
    return result
