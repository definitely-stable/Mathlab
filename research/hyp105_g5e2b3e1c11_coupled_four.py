"""HYP-105 C11: EXACT conditional second moment for ONE shared right map.

For a fixed partial original-right bijection p, all remaining four-line
completions use the SAME permutation. This is an exact Johnson-like
conditional orbit count, not independent C4 anchor-frozen random maps.
No all-GQ, all-f,g, seven-family lower is inferred.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial
import json

from hyp105_g5e2b3e1c5_common_bijection import (
    validate_weighted_sixsets, fixed_map_overlap, physical_occupied_target,
)


def _validated(source, target, V, pinned):
    src=validate_weighted_sixsets(source,V)
    if not isinstance(target,(tuple,list,set,frozenset)):
        raise ValueError("target must be explicit sixsets")
    seq=tuple(target)
    dst=validate_weighted_sixsets({frozenset(t):1 for t in seq},V)
    if len(seq)!=len(dst):
        raise ValueError("duplicate or zero-size target sixset")
    if not hasattr(pinned,"items"):
        raise ValueError("pinned must be an original->physical mapping")
    p=dict(pinned)
    if (any(type(i) is not int or not 0<=i<V
            or type(j) is not int or not 0<=j<V
            for i,j in p.items())
        or len(set(p.values()))!=len(p)):
        raise ValueError("partial map must be injective and in range")
    return src,dst,p


def _orbit_buckets(weights, V, pin_index, remaining_index, permitted_patterns=None):
    """Group sixsets by pinned membership and residual bitmask.

    Only original pinned-membership classes PRESENT in physical target
    need be considered: every excluded source sixset contributes ZERO
    for EVERY one-common-map completion of this prefix.
    """
    groups=Counter()
    for R,w in weights.items():
        a=sum(1<<pin_index[x] for x in R if x in pin_index)
        if permitted_patterns is not None and a not in permitted_patterns:
            continue
        u=sum(1<<remaining_index[x] for x in R if x in remaining_index)
        if u.bit_count()+a.bit_count()!=6:
            raise AssertionError("sixset partition lost an original line")
        groups[(a,u)]+=w
    return tuple((a,u,w) for (a,u),w in groups.items() if w)


def _ordered_pair_orbits(bucket):
    counts=Counter()
    for a,u,w in bucket:
        for b,v,z in bucket:
            counts[(a,b,(u&v).bit_count())]+=w*z
    return counts


def _ceil_fraction(x):
    return -(-x.numerator//x.denominator)


def _lower_from_full_population_variance(mu, variance, size):
    """Exact finite-population min >= ceil(mu-sqrt((size-1)*Var)).

    Avoid sqrt floats. If x is one deviation among size centered values,
    their sum is zero; by Cauchy the remaining squares >=x*x/(size-1).
    Hence x*x <= (size-1)*Var for ANY individual full permutation.
    """
    if size<1 or variance<0:
        raise ValueError("invalid finite population")
    if size==1 or variance==0:
        if mu.denominator!=1:
            raise AssertionError("constant integer population needs integral mean")
        return int(mu)
    cap=(size-1)*variance
    lo,hi=0,_ceil_fraction(mu)
    while lo<hi:
        mid=(lo+hi)//2
        if Fraction(mid)>=mu or (mu-mid)**2<=cap:
            hi=mid
        else:
            lo=mid+1
    return lo


def common_prefix_joint_moments(source, target, V, pinned,
                                *, max_relevant_source_cells=10000):
    """All-h exact conditional moments of ONE global common completion.

    D is the pinned ORIGINAL right subset, I=p(D) its occupied physical
    image; n=V-|D| remaining lines. For ordered original (R,S), let
    A=R∩D, B=S∩D, r=|R\\D|, t=|S\\D|, j=|(R∩S)\\D|.
    Their images under ONE uniformly chosen completion are uniform
    among ordered physical target candidates with the SAME pinned
    patterns and residual intersection j. The orbit size is exactly
      comb(n,r)*comb(r,j)*comb(n-r,t-j).
    Therefore E U² = Σ_(A,B,j) S_(A,B,j) Q_(pA,pB,j)/orbit_size.
    The cross terms are global (one Pi), not independent by P.
    """
    src,tgt,p=_validated(source,target,V,pinned)
    D=tuple(sorted(p))
    physical_pins=tuple(p[i] for i in D)
    pin_source={x:i for i,x in enumerate(D)}
    pin_target={x:i for i,x in enumerate(physical_pins)}
    rem_source={x:i for i,x in enumerate(range(V)) if x not in pin_source}
    rem_target={x:i for i,x in enumerate(range(V)) if x not in pin_target}
    n=V-len(D)
    T=_orbit_buckets(tgt,V,pin_target,rem_target)
    allowed={a for a,_,_ in T}
    S=_orbit_buckets(src,V,pin_source,rem_source,allowed)
    if type(max_relevant_source_cells) is not int or max_relevant_source_cells<1:
        raise ValueError("invalid relevant-cell cap")
    if len(S)>max_relevant_source_cells:
        raise ValueError("relevant source cells exceed explicit computation cap")
    sm=Counter()
    tm=Counter()
    for a,u,w in S:sm[a]+=w
    for a,u,w in T:tm[a]+=w
    mean=Fraction(0)
    for a,mass in sm.items():
        r=6-a.bit_count()
        denom=comb(n,r)
        if denom==0:
            raise AssertionError("impossible source pinned fiber")
        mean+=Fraction(mass*tm[a],denom)
    spectrum_s=_ordered_pair_orbits(S)
    spectrum_t=_ordered_pair_orbits(T)
    second=Fraction(0)
    for (a,b,j),mass in spectrum_s.items():
        physical=spectrum_t.get((a,b,j),0)
        if not physical:
            continue
        r=6-a.bit_count()
        t=6-b.bit_count()
        if not (0<=j<=min(r,t) and 0<=t-j<=n-r):
            raise AssertionError("impossible shared residual intersection orbit")
        orbit=comb(n,r)*comb(r,j)*comb(n-r,t-j)
        if orbit<=0:
            raise AssertionError("empty shared conditional permutation orbit")
        second+=Fraction(mass*physical,orbit)
    variance=second-mean*mean
    if variance<0:
        raise AssertionError("negative shared conditional variance")
    N=factorial(n)
    lower=_lower_from_full_population_variance(mean,variance,N)
    upper=mean.numerator//mean.denominator
    if lower>upper:
        raise AssertionError("conditional mean/variance gave inverted minimum interval")
    return {
        "V":V,"pinned_original_right_lines":D,
        "pinned_target_labels":physical_pins,
        "remaining_original_right_lines":n,
        "common_full_map_completions":N,
        "mean_one_shared_completion":mean,
        "second_moment_one_shared_completion":second,
        "variance_one_shared_completion":variance,
        "worst_completion_lower_from_second_moment":lower,
        "existential_completion_upper_from_mean":upper,
        "min_exact_if_bounds_meet":lower if lower==upper else None,
        "relevant_source_cells":len(S),
        "target_cells":len(T),
        "original_pair_orbit_count":len(spectrum_s),
        "occupied_target_pair_orbit_count":len(spectrum_t),
        "all_completions_use_one_map":True,
        "no_all_g_GQ_seven_family_lower":True,
    }


def _tensor_coupled_recount(tensor, target, pi):
    """Independent ORIGINAL doubled-pair + FOUR remaining lines recount.

    A single pi assigns ALL four H lines, shared across all original
    anchor pairs P. Physical residual foursets are checked exactly,
    with no separately chosen per-P permutation.
    """
    residual=defaultdict(set)
    for R in target:
        for z in combinations(R,2):
            residual[frozenset(z)].add(frozenset(R)-frozenset(z))
    result=0
    for P,rows in tensor.items():
        z=frozenset(pi[i] for i in P)
        allowed=residual.get(z,set())
        for H,w in rows.items():
            if frozenset(pi[i] for i in H) in allowed:
                result+=w
    return result


def genuine_W32_coupled_four_report():
    """EXHAUST ALL 4! completions of ONE fixed prefix, not all 15! maps."""
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
    from hyp105_g5e2b3e1c0_weighted_overlap import source_weighted_BA_hypergraph
    from hyp105_g5e2b3e1c4_conditional_completion import original_W32_conditional_source

    V=15
    original=pair_labeled_symplectic(1,"reverse-line")
    source=source_weighted_BA_hypergraph(original)
    tensor=original_W32_conditional_source(original)
    palette=tuple(combinations(range(6),2))
    target=physical_occupied_target(6,palette)
    lookup={e:i for i,e in enumerate(palette)}
    historical=tuple(lookup[e] for e in original["right_labels"])
    p={i:historical[i] for i in range(11)}
    moments=common_prefix_joint_moments(source,target,V,p)
    available=tuple(x for x in range(V) if x not in p.values())
    vals=[]
    argmin=None
    for tail in permutations(available):
        pi=historical[:11]+tail
        actual=fixed_map_overlap(source,target,pi)
        independent=_tensor_coupled_recount(tensor,target,pi)
        if independent!=actual:
            raise AssertionError("original C4 coupled four-line tensor disagrees")
        vals.append(actual)
        if argmin is None or actual<argmin[0]:
            argmin=(actual,pi)
    n=len(vals)
    mu=Fraction(sum(vals),n)
    second=Fraction(sum(x*x for x in vals),n)
    if (n!=24 or mu!=moments["mean_one_shared_completion"]
            or second!=moments["second_moment_one_shared_completion"]):
        raise AssertionError("independent 4! enumeration violates shared-orbit moments")
    if not (moments["worst_completion_lower_from_second_moment"]<=min(vals)
            <=moments["existential_completion_upper_from_mean"]):
        raise AssertionError("conditional interval misses true restricted minimum")

    # An improvement in ONE B/A term is NOT automatically an improvement in
    # all seven ORIGINAL incidence motif families. Recount both maps on the
    # SAME genuine original W32 left incidence model, before any claim.
    from hyp105_g5e2b3e1b0_seven_signature import seven_census
    candidate=dict(original)
    candidate["right_labels"]=tuple(palette[i] for i in argmin[1])
    before=seven_census(original,independent_checks=False)
    after=seven_census(candidate,independent_checks=False)
    if (before["seven_class_motif_counts"]["B-left/A-right"]!=77
            or after["seven_class_motif_counts"]["B-left/A-right"]!=argmin[0]):
        raise AssertionError("exact seven-family source B/A census not consistent")
    before_counts=before["seven_class_motif_counts"]
    after_counts=after["seven_class_motif_counts"]
    class_deltas={key:after_counts[key]-before_counts[key]
                  for key in sorted(before_counts)}
    if sum(class_deltas.values())!=after["S_seven"]-before["S_seven"]:
        raise AssertionError("all seven original motif counts not reconciled")
    return {
        "seven_family_original_S":before["S_seven"],
        "seven_family_candidate_S":after["S_seven"],
        "seven_family_total_delta":after["S_seven"]-before["S_seven"],
        "seven_family_class_count_delta":class_deltas,
        "GF5_seven_necessary_floor_original_numerator":
            before["GF5_seven_lower_numerator"],
        "GF5_seven_necessary_floor_candidate_numerator":
            after["GF5_seven_lower_numerator"],
        "full_GF5_R3_or_all_h_obstruction_proved":False,
        "model":"GENUINE_ORIGINAL_GQ_W32_BA_ONLY",
        "fixed_left":"reverse-line",
        "original_right_prefix_fixed":11,
        "four_original_right_lines_jointly_permuted":(11,12,13,14),
        "all_common_tail_maps_checked":n,
        "historical_BA":fixed_map_overlap(source,target,historical),
        "restricted_four_line_exact_minimum":min(vals),
        "restricted_four_line_exact_maximum":max(vals),
        "minimizing_full_right_permutation":argmin[1],
        "conditional_mean":str(mu),
        "conditional_variance":str(second-mu*mu),
        "moment_based_lower":moments["worst_completion_lower_from_second_moment"],
        "conditional_mean_existential_upper":moments["existential_completion_upper_from_mean"],
        "independent_original_C4_tensor_all_24_agree":True,
        "f_and_F_unrestricted_15_factorial_minimum_proved":False,
        "seven_GF5_classes_evaluated":False,
    }


if __name__=="__main__":
    print(json.dumps(genuine_W32_coupled_four_report(),
                     indent=2,sort_keys=True))
