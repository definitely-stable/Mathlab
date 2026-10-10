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


def physical_target_two_point_design(a):
    """All-a exact 1-design and two adjacency-orbit codegrees of T_a.

    The six-edge simple 2-factors of K6 number 70. Under S6 symmetry,
    each physical K6 edge belongs to 28 factors. Every unordered pair
    of adjacent K6 edges belongs to 7 factors, every disjoint pair
    belongs to 14 factors (independently exhaustively verified by tests).

    Embed each fixed 6-symbol factor into K_a:
      |T_a|=70*C(a,6);
      deg(e)=28*C(a-2,4);
      co_deg(adjacent e,e')=7*C(a-3,3);
      co_deg(disjoint e,e')=14*C(a-4,2).
    Thus T_a is a 1-design for all a>=6. It is a 2-design
    precisely at a=9 (for a>=6), where 7*C(6,3)=14*C(5,2)=140.
    Actual HYP-105 minimal a_s is 6 at s=2, 14 at s=4 and
    grows thereafter, so the accidental a=9 2-design does NOT
    give a positive-min theorem for any actual W(3,2^h).
    """
    if not isinstance(a,int) or isinstance(a,bool) or a<6:
        raise ValueError("physical K_a must have at least six coordinates")
    n=comb(a,2)
    count=70*comb(a,6)
    d=28*comb(a-2,4)
    adj=7*comb(a-3,3)
    dis=14*comb(a-4,2)
    # C(K,2) unordered physical PAIR-EDGE pairs, two adjacency orbits:
    # adj pair of K_a edges share one physical coordinate;
    # disjoint pair of K_a edges occupy four physical coordinates.
    n_adj=a*comb(a-1,2)
    n_dis=3*comb(a,4)
    if (6*count!=n*d or
            comb(6,2)*count!=n_adj*adj+n_dis*dis or
            n_adj+n_dis!=comb(n,2)):
        raise AssertionError("two-point incidence design identities failed")
    return {
        "a":a,"physical_pair_label_vertices":n,
        "physical_six_2factor_target_size":count,
        "target_degree_each_pair_label":d,
        "pair_codegree_adjacent_physical_labels":adj,
        "pair_codegree_disjoint_physical_labels":dis,
        "target_is_one_design":True,
        "target_is_two_design":adj==dis,
        "uniform_target_component_W1_zero":True,
        "all_correlated_right_min_lower_proved":False,
    }


def physical_target_three_point_orbits(a):
    """Exact ALL-a triple-label orbit co-degrees for six-edge 2factors.

    Three distinct physical K_a pair edges have exactly five possible
    unlabeled 3-edge graph shapes (all simple):
      triangle (r=3): 1*C(a-3,3) target hyperedges;
      length-three path P4 (r=4): 2*C(a-4,2);
      claw K1,3 (r=4): 0, since physical degree would exceed 2;
      P3 + disjoint K2 (r=5): 5*C(a-5,1);
      three-edge perfect matching (r=6): 8.
    Values 1,2,0,5,8 are an exact exhaustive K6 template census,
    independently verified against all 70 K6 physical target factors.
    They embed into K_a on all C(a-r,6-r) ways to add coordinates.
    Target triplet incidence sum = C(6,3)*|T_a| exactly.
    Neither all-h GQ-specific source m_f nor a positive min follows.
    """
    if not isinstance(a,int) or isinstance(a,bool) or a<6:
        raise ValueError("K_a physical coordinate count must be >=6")
    k=lambda n,m: comb(n,m) if n>=m>=0 else 0
    target=physical_target_two_point_design(a)
    triples={
        "triangle":{"vertices":3,"source_K6_codegree":1,
                    "orbit_cardinality":k(a,3),
                    "codegree":k(a-3,3)},
        "path_P4":{"vertices":4,"source_K6_codegree":2,
                    "orbit_cardinality":12*k(a,4),
                    "codegree":2*k(a-4,2)},
        "star_K1_3":{"vertices":4,"source_K6_codegree":0,
                    "orbit_cardinality":4*k(a,4),
                    "codegree":0},
        "path_P3_plus_edge":{"vertices":5,"source_K6_codegree":5,
                    "orbit_cardinality":30*k(a,5),
                    "codegree":5*k(a-5,1)},
        "matching_3":{"vertices":6,"source_K6_codegree":8,
                    "orbit_cardinality":15*k(a,6),
                    "codegree":8},
    }
    if (sum(t["orbit_cardinality"] for t in triples.values())!=
            k(k(a,2),3)):
        raise AssertionError("all physical 3-edge graph orbits not exhausted")
    if (sum(t["orbit_cardinality"]*t["codegree"]
            for t in triples.values())!=20*target["physical_six_2factor_target_size"]):
        raise AssertionError("target third-incidence moment consistency")
    return {
        "a":a,
        "target_triple_label_orbits":triples,
        "target_third_incidence_total":
            20*target["physical_six_2factor_target_size"],
        "exact_all_a_census_proved":True,
        "actual_GQ_source_order3_distribution_computed":False,
        "all_correlated_right_min_lower_proved":False,
    }


def one_degree_source_overlap_invariant(a, constant, vertex_coefficients):
    """Exact all-right-BIJECTION value for degree<=1 source m(R).

    m(R)=constant + sum_{v in R} beta[v] on C(K,6). For a full
    bijection pi:[K]->E(K_a), <m_pi, 1_{T_a}>
      = constant*|T_a| + d(T_a)*sum_v beta[v],
    independent of pi, because T_a is 1-design.

    This does NOT apply to arbitrary incidence-generated m_f, and
    does not cover non-surjective right injections V<K where
    only a restricted physical subset of pair labels is occupied.
    """
    target=physical_target_two_point_design(a)
    coeff=tuple(vertex_coefficients)
    if (len(coeff)!=target["physical_pair_label_vertices"] or
            not isinstance(constant,int) or isinstance(constant,bool) or
            any(not isinstance(x,int) or isinstance(x,bool) for x in coeff)):
        raise ValueError("complete bijective degree-one source required")
    result=(constant*target["physical_six_2factor_target_size"]+
            sum(coeff)*target["target_degree_each_pair_label"])
    return result


def two_marginal_blind_cube_trade(scale=1):
    """Explicit 3-dimensional 6-uniform trade invisible through order two.

    Source V=K=15 abstract original right-factor vertices, mapped via
    identity to the 15 physical K6 pair labels in lex ordering.
    Common 3 vertices = (0,1,6), switch pairs (2,11),(3,12),(13,14).
    Eight 6sets split evenly by selection parity. This 3-cube trade
    has equal |R|<=2 marginals for even and odd halves, since fixing
    at most two chosen vertices leaves one independent sign toggle.
    Yet exactly ONE odd sixset, mask 7, is a K6 physical 2factor.
    Neither source models actual W(3,s) incidence weights m_f.
    """
    if not isinstance(scale,int) or isinstance(scale,bool) or scale<=0:
        raise ValueError("positive integer weight scale required")
    shared=(0,1,6)
    pairs=((2,11),(3,12),(13,14))
    lhs, rhs=Counter(),Counter()
    for mask in range(8):
        R=frozenset((*shared,*(pairs[i][(mask>>i)&1] for i in range(3))))
        (rhs if mask.bit_count()%2 else lhs)[R]=scale
    if len(lhs)!=4 or len(rhs)!=4:
        raise AssertionError("cube trade lost sixset injectivity")
    def signature(weights,order):
        if order==0:
            return {():sum(weights.values())}
        out=Counter()
        for R,m in weights.items():
            for subset in combinations(sorted(R),order):
                out[subset]+=m
        return dict(out)
    same={}
    for k in (0,1,2):
        if signature(lhs,k)!=signature(rhs,k):
            raise AssertionError("3-cube pair marginal cancellation invalid")
        same[k]=True
    palette=tuple(combinations(range(6),2))
    target=simple_six_2factor_targets(6)
    left_value=exact_BA_overlap(lhs,palette,target=target)
    right_value=exact_BA_overlap(rhs,palette,target=target)
    if (left_value,right_value)!=(0,scale):
        raise AssertionError("3-cube trade was not detected by physical T6")
    return {
        "source_abstract_original_vertices":15,
        "source_even_sixsets":tuple(sorted(tuple(sorted(x)) for x in lhs)),
        "source_odd_sixsets":tuple(sorted(tuple(sorted(x)) for x in rhs)),
        "equal_0_1_2_marginals":same,
        "equal_total_mass_each":4*scale,
        "even_overlap_T6":left_value,
        "odd_overlap_T6":right_value,
        "overlap_gap":scale,
        "extends_to_any_physical_a_at_least_six_by_embedding":True,
        "actual_W3s_incidence_source":False,
        "universal_all_correlated_S_lower_proved":False,
    }


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
        "pair_marginal_blind_3cube_trade":two_marginal_blind_cube_trade(),
        "physical_target_three_point_signature_W32":physical_target_three_point_orbits(6),
        "prior_art":"Bollobas-Scott 2015 weighted k-uniform intersections; no automatic min transfer",
        "full_R3_or_ASET_exponent":False,
    }


if __name__=="__main__":
    print(json.dumps(report(),sort_keys=True,indent=2))
