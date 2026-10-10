"""HYP-105 B3.2-E1-C0: exact weighted 6-hypergraph overlap reduction.

For W(3,2), physical K6 pair labels form 15 target vertices.
The six-edge K6 2-factors (one C6 or two C3) form a 70-edge
6-uniform target hypergraph on 15 vertices. The source m_f(R)
counts ORIGINAL six-incidence B-left / six-distinct-right-factor
selections grouped by their UNORDERED six right factor endpoints.

For all h the same equality holds as a finite incidence identity,
even though executable full original-incidence enumeration is capped
at W(3,2). No universal min over correlated permutations follows.

Bollobas-Scott (JCTB 110 (2015), DOI 10.1016/j.jctb.2014.08.002)
studied weighted hypergraph overlap/discrepancy. Their two-sided
discrepancy conclusions do not imply positive minimum overlap.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb
import json

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_g5e2b3e1a_fixed_leading import selected_left_six,validated_small_model
from hyp105_g5e2b3e1b0_seven_signature import seven_census


def simple_six_2factor_targets(a=6):
    """All 6-edge simple 2-regular graphs on exactly 6 vertices of K_a."""
    if not isinstance(a,int) or isinstance(a,bool) or not 6<=a<=14:
        raise ValueError("finite physical target alphabet must be 6..14")
    from hyp105_g5e2b3e1a_fixed_leading import _two_factors_K6
    templates=tuple(_two_factors_K6())
    if len(templates)!=70:
        raise AssertionError("physical K6 reference template count changed")
    output=set()
    for verts in combinations(range(a),6):
        for edges6 in templates:
            output.add(frozenset(
                (verts[u],verts[v]) for u,v in edges6))
    expected=70*comb(a,6)
    if len(output)!=expected:
        raise AssertionError("expected K6 2factor count 70 per six symbols")
    return frozenset(output)


def source_weighted_BA_hypergraph(model):
    """Exact finite W32 weighted right six-uniform original-line hypergraph.

    Every multiplicity unit is ONE unordered original SIX-incidence set.
    Original right endpoints must all be distinct; left factor profile
    B and exactly 6 leafless left physical coordinates are generated
    independently by the accepted A/B/C source enumeration.
    """
    _,_,edges,_=validated_small_model(model)
    counts=Counter()
    generated=0
    for ids,kind in selected_left_six(model):
        if kind!="B":
            continue
        generated+=1
        right_tuple=tuple(edges[i][1] for i in ids)
        if len(set(right_tuple))!=6:
            continue
        counts[frozenset(right_tuple)]+=1
    if generated!=10935 or sum(counts.values())>generated:
        raise AssertionError("W32 B-left incidence census changed")
    if any(len(r)!=6 or m<=0 for r,m in counts.items()):
        raise AssertionError("invalid weighted six-uniform original source")
    return counts


def exact_BA_overlap(weights, right_labels, *, target=None):
    """Weighted hypergraph overlap under an arbitrary injective right map.

    target is the set of unordered SIX physical pair-edge subsets.
    Unordered source R multiplicities are counted once, no 6! factor.
    """
    labels=tuple(tuple(pair) for pair in right_labels)
    if len(set(labels))!=len(labels) or any(len(e)!=2 or e[0]>=e[1]
          for e in labels):
        raise ValueError("right physical pair labels must be injective")
    if target is None:
        target=simple_six_2factor_targets(6)
    total=0
    for R,mult in weights.items():
        if len(R)!=6 or not isinstance(mult,int) or mult<0:
            raise ValueError("six-uniform nonnegative integer weights only")
        if any(not isinstance(j,int) or j<0 or j>=len(labels) for j in R):
            raise ValueError("invalid original right factor endpoint")
        if frozenset(labels[j] for j in R) in target:
            total+=mult
    return total


def random_injection_expectation(weights, *, a, original_vertices):
    """Exact rational E_g overlap for UNIFORM right edge-label injections.

    Each fixed 6-subset of original right vertices maps uniformly
    to any of C(K,6) subsets of K physical pair edges, hence all-h
    E_U_BA=(sum_R m_f(R))*70*C(a,6)/C(C(a,2),6).
    """
    if not isinstance(a,int) or a<6 or not isinstance(original_vertices,int):
        raise ValueError("invalid finite hypergraph source/target sizes")
    K=comb(a,2)
    if original_vertices>K or original_vertices<6:
        raise ValueError("injection not possible")
    if any(len(R)!=6 or any(j<0 or j>=original_vertices for j in R)
           for R in weights):
        raise ValueError("source line hyperedge out of range")
    return Fraction(sum(weights.values())*70*comb(a,6),comb(K,6))


def finite_W32_overlap_report():
    model=pair_labeled_symplectic(1,"reverse-line")
    source=source_weighted_BA_hypergraph(model)
    target=simple_six_2factor_targets(6)
    actual=exact_BA_overlap(source,model["right_labels"],target=target)
    independent=seven_census(model,independent_checks=False)
    expected=independent["seven_class_motif_counts"]["B-left/A-right"]
    if actual!=expected:
        raise AssertionError("weighted right-6 hypergraph overlap != independent B/A census")
    source_mass=sum(source.values())
    return {
        "source_host":"W(3,2) factor lines",
        "source_original_B_sixsets_with_six_distinct_right_factors":source_mass,
        "source_distinct_right_sixsets":len(source),
        "max_source_weight":max(source.values()),
        "target_K6_six_edge_2factor_sets":len(target),
        "target_K6_sixset_universe":comb(15,6),
        "actual_BA_overlap":actual,
        "independently_checked_accepted_BA":expected,
        "uniform_random_right_expected_BA":str(
            random_injection_expectation(source,a=6,original_vertices=15)),
        "all_h_hypergraph_reduction_identity":True,
        "all_right_permutations_minimum_computed":False,
        "all_h_universal_BA_minimum_lower_proved":False,
        "all_h_seven_family_Omega_s6_proved":False,
        "total_GF5_R3_computed":False,
    }


def generic_mass_only_countermodel(weight=1):
    """Positive mean but ZERO min under some bijection, for ANY weight>0.

    One weighted original six-edge source R of size 6 on 15 abstract
    vertices; target contains exactly the 70 K6 2factors.
    A physical 6-star-plus-chord image is not 2-regular, so weighted
    overlap 0 under a valid right-pair bijection. This demonstrates
    general mass-only inference is FALSE (not a W32 incidence source).
    """
    if not isinstance(weight,int) or isinstance(weight,bool) or weight<=0:
        raise ValueError("positive integer source mass required")
    src={frozenset(range(6)):weight}
    pair_labels=list(combinations(range(6),2))
    # Select 5 edges in star at physical coordinate 0, plus (1,2).
    bad=[(0,j) for j in range(1,6)]+[(1,2)]
    rest=[e for e in pair_labels if e not in bad]
    labels=bad+rest
    target=simple_six_2factor_targets(6)
    if frozenset(bad) in target:
        raise AssertionError("explicit bad sixset unexpectedly physical 2factor")
    actual=exact_BA_overlap(src,labels,target=target)
    mean=random_injection_expectation(src,a=6,original_vertices=15)
    if actual!=0 or mean!=Fraction(weight*2,143):
        raise AssertionError("generic mass-only countermodel invalid")
    return {
        "source_mass":weight,
        "min_attained_overlap":0,
        "positive_random_mean":str(mean),
        "physical_image":tuple(bad),
        "does_NOT_model_actual_GQ_source":True,
        "invalidates_generic_mass_only_minimum_transfer":True,
    }


def report():
    return {
        "exact_W32":finite_W32_overlap_report(),
        "generic_mass_only_countermodel":generic_mass_only_countermodel(),
        "prior_art":"Bollobas-Scott 2015 weighted k-uniform intersections; no automatic min transfer",
        "full_R3_or_ASET_exponent":False,
    }


if __name__=="__main__":
    print(json.dumps(report(),sort_keys=True,indent=2))
