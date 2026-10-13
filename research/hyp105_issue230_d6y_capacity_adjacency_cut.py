"""HYP-105 #230 D6-Y: exact global physical-image adjacency capacity cut.

ALL-h, ALL correlated ORIGINAL typed globally injective physical-pair maps:
s=2^h,h>=1; V=(s+1)(s²+1), K=C(a,2)>=V minimal; m=K-V<=a-2.
The V occupied edges E of the physical K_a graph obey
 A(E)=sum_c C(deg_E(c),2)
   <= a*C(a-1,2) - 2*m*(a-2) + C(m,2) = A_max.
The bound is sharp: remove m distinct edges incident to coordinate 0.
Equivalently, for any global injective original point label assignment,
sum_{p<q} 1[f(p) shares a physical coordinate with f(q)] <= A_max.
Same theorem independently holds for ORIGINAL line assignments.

A symmetrized two-original-factor physical-edge pair distribution can
saturate EVERY explicitly enumerated single physical-column capacity
lift of the form E[x_(p,e)(1-sum_{q != p}x_(q,e'))]>=0, preserve local
injectivity and uniform site marginals, yet (for m>0) VIOLATE the valid
global quadratic image adjacency inequality by exactly
m*(a-2)-C(m,2)>0. Thus the SPECIFIED selected lifted column cuts
are insufficient to characterize global realisability, even at the
2-site marginal level. This is NOT a standard SA/SOS integrality gap
or proof of universal positive seven-GF5 risk.

No full original sixset truth tables or Branch A/B proof claimed.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb
import json

from hyp105_issue230_proof_audit import parameters


def edge_adjacent(e, other):
    """Two DISTINCT canonical physical pairs sharing exactly one coordinate."""
    return e != other and bool(set(e).intersection(other))


def graph_adjacency_count(occupied_edges, a):
    """Independent exact O(K) degree census for a physical simple-edge IMAGE."""
    if type(a) is not int or a<4:
        raise ValueError("physical complete-graph alphabet a>=4 required")
    if not isinstance(occupied_edges,(tuple,list,set,frozenset)):
        raise ValueError("physical edge collection required")
    pairs=tuple(occupied_edges)
    if (any(not isinstance(e,(tuple,list)) or len(e)!=2
            or any(type(v) is not int for v in e)
            or not 0<=e[0]<e[1]<a for e in pairs)
            or len(set(map(tuple,pairs)))!=len(pairs)):
        raise ValueError("distinct canonical physical pair edges required")
    degrees=Counter(v for e in pairs for v in e)
    return sum(comb(degrees[v],2) for v in range(a))


def sharp_adjacency_image_bound(s):
    """Proved exact all-h global-injection bound and its sharpness gap."""
    z=parameters(s)
    a,V,K=z["a"],z["V"],z["K"]
    m=K-V
    if not 0<=m<=a-2:
        raise AssertionError("minimal K_a must leave at most a-2 unused edges")
    full=a*comb(a-1,2)
    bound=full-2*m*(a-2)+comb(m,2)
    t=2*(a-2) # physical adjacent edges available to a fixed edge
    d=comb(a-2,2) # physical disjoint edges available to a fixed edge
    if t+d!=K-1:
        raise AssertionError("physical pair edge adjacency partition false")
    lifted=Fraction(t,V-1)
    global_bound=Fraction(2*bound,V*(V-1))
    gap=Fraction(m*(a-2)-comb(m,2))
    if lifted-global_bound!=2*gap/(V*(V-1)):
        raise AssertionError("lifted versus true global gap algebra false")
    if (m and gap<=0) or (not m and gap):
        raise AssertionError("sharp missing-edge gap sign false")
    return {
        **z,"missing_physical_edges":m,
        "complete_Ka_adjacent_unordered_edge_pairs":full,
        "sharp_max_occupied_adjacent_unordered_pairs":bound,
        "pairwise_lifted_capacity_upper":str(lifted),
        "true_global_random_original_pair_adjacent_upper":str(global_bound),
        "sharp_integrality_gap_adjacent_pair_count":str(gap),
        "sharp_integrality_gap_random_pair_probability":
            str(lifted-global_bound),
        "sharp_image_achievable_by_missing_star":True,
        "not_GF5_positive_sixset_lower":True,
    }


def constructive_sharp_original_injection(s, *, max_labels=100000):
    """Produce globally injected ORIGINAL point and line maps attaining A_max.

    Geometry independent, but uses correct ORIGINAL W(3,s) point/line
    cardinality and BOTH separately typed physical alphabets.
    """
    z=sharp_adjacency_image_bound(s)
    a,V,m=z["a"],z["V"],z["missing_physical_edges"]
    if V>max_labels:
        raise ValueError("exact physical assignment output exceeds explicit budget")
    removed={(0,i) for i in range(1,m+1)}
    full=tuple(combinations(range(a),2))
    left=tuple(e for e in full if e not in removed)
    right=tuple(reversed(left))
    if len(left)!=V or len(right)!=V or len(set(left))!=V:
        raise AssertionError("original physical assignment incomplete")
    degree=graph_adjacency_count(left,a)
    if degree!=z["sharp_max_occupied_adjacent_unordered_pairs"]:
        raise AssertionError("deleted physical star not actually extremal")
    return {"s":s,"a":a,"V":V,"removed_physical_star_edges":
            tuple(sorted(removed)),"left_original_labels":left,
            "right_original_labels":right,
            "exact_adjacent_left_unordered_original_point_pairs":degree,
            "exact_adjacent_right_unordered_original_line_pairs":
                graph_adjacency_count(right,a),
            "two_globally_injective_typed_maps":True}


def pairwise_capacity_saturated_distribution(s):
    """A complete exact two-ORIGINAL-point marginal in exchangeable orbit form.

    x_pe one-site probability 1/K.
    For DISTINCT physical edges e,e':
      joint adjacent  = 1/[K*(V-1)]
      joint disjoint  = [V-1-2(a-2)]/[K*(V-1)*C(a-2,2)].
    For equal physical edges joint 0. The conditional distributions
    sum to one, both original-site marginals 1/K, all typed original
    point pairs are locally injective, and the selected lifted physical
    column-capacity inequalities hold for each e,e' (including e=e').
    No extension to THREE or V ORIGINAL site marginals is claimed.
    """
    z=sharp_adjacency_image_bound(s)
    a,V,K=z["a"],z["V"],z["K"]
    t=2*(a-2)
    d=comb(a-2,2)
    if V-1<t or d<=0:
        raise AssertionError("s>=2 minimal-alphabet capacity infeasible")
    qadj=Fraction(1,K*(V-1))
    qdis=Fraction(V-1-t,K*(V-1)*d)
    if t*qadj+d*qdis!=Fraction(1,K):
        raise AssertionError("conditional normalization false")
    if qdis<0 or qdis>Fraction(1,K*(V-1)):
        raise AssertionError("physical disjoint-edge lifted capacity false")
    expected_adjacent=Fraction(comb(V,2)*K*t)*qadj
    true_max=Fraction(z["sharp_max_occupied_adjacent_unordered_pairs"])
    gap=expected_adjacent-true_max
    if gap!=Fraction(z["sharp_integrality_gap_adjacent_pair_count"]):
        raise AssertionError("exact quadratic global cut falsifier false")
    return {
        "s":s,"a":a,"V":V,"K":K,"adjacent_edges_per_fixed_edge":t,
        "disjoint_edges_per_fixed_edge":d,
        "uniform_original_site_edge_marginal":str(Fraction(1,K)),
        "distinct_original_point_joint_adjacent":str(qadj),
        "distinct_original_point_joint_disjoint":str(qdis),
        "joint_same_physical_edge":0,
        "joint_marginals_exactly_normalized_and_exchangeable":True,
        "selected_rank_two_physical_column_lifts_feasible":True,
        "physical_row_injectivity_two_sites":True,
        "expected_total_adjacent_original_point_pairs":str(expected_adjacent),
        "maximum_for_any_global_point_injection":str(true_max),
        "global_image_quadratic_capacity_cut_slack":str(-gap),
        "global_image_quadratic_cut_violated":bool(gap>0),
        "pairwise_marginals_not_claimed_extendible":True,
        "standard_SA_feasibility_not_claimed":True,
    }


def independent_full_pair_oracle(s, *, max_k=100):
    """Enumerate EVERY ordered physical edge pair and check all lifts."""
    z=pairwise_capacity_saturated_distribution(s)
    a,V,K=z["a"],z["V"],z["K"]
    if K>max_k:
        raise ValueError("full two-site physical pair oracle exceeds budget")
    edges=tuple(combinations(range(a),2))
    qa=Fraction(z["distinct_original_point_joint_adjacent"])
    qd=Fraction(z["distinct_original_point_joint_disjoint"])
    marginal=Fraction(1,K)
    expected=Fraction()
    adjacent_count=0
    for e in edges:
        total=Fraction()
        for eprime in edges:
            shared=edge_adjacent(e,eprime)
            joint=Fraction(0) if e==eprime else (qa if shared else qd)
            total+=joint
            if (V-1)*joint>marginal:
                raise AssertionError("selected physical column lift violated")
            # At any original point p receiving physical edge e, an
            # alternate original q cannot receive the SAME physical edge.
            if e==eprime and joint:
                raise AssertionError("two-site global injection condition violated")
            if shared:
                adjacent_count+=1
                expected+=Fraction(comb(V,2))*joint
        if total!=marginal:
            raise AssertionError("pair law fails original one-site marginal")
    if adjacent_count!=K*2*(a-2):
        raise AssertionError("physical adjacency orbit counting failed")
    if expected!=Fraction(z["expected_total_adjacent_original_point_pairs"]):
        raise AssertionError("pairwise full orbit exact expected count drift")
    return {
        "s":s,"K":K,"ordered_distinct_physical_pair_cases":K*(K-1),
        "all_physical_column_lifts_for_any_first_original_point_label":"PASS",
        "every_original_pair_marginal_normalizes_to_uniform":"PASS",
        "symmetric_pair_orbit_uses_only_adjacent_or_disjoint":True,
        "independent_expected_total_adjacent_original_pairs":str(expected),
    }


def independent_missing_edge_brute(a,m, *, max_subsets=30000):
    """Enumerate all missing-edge sets H; verify exact physical extremum."""
    if (type(a) is not int or a<4 or type(m) is not int
            or not 0<=m<=a-2):
        raise ValueError("physical a>=4, 0<=m<=a-2 required")
    full=tuple(combinations(range(a),2))
    possible=comb(len(full),m)
    if possible>max_subsets:
        raise ValueError("physical missing-edge family enumeration over budget")
    target=a*comb(a-1,2)-2*m*(a-2)+comb(m,2)
    seen=0
    maximum=-1
    saturating=0
    for rem in combinations(full,m):
        remaining=tuple(e for e in full if e not in set(rem))
        count=graph_adjacency_count(remaining,a)
        if count>target:
            raise AssertionError("sharp missing-star adjacency theorem false")
        maximum=max(maximum,count)
        if count==target:
            saturating+=1
        seen+=1
    if seen!=possible or maximum!=target or not saturating:
        raise AssertionError("finite exact extremum not attained")
    return {
        "a":a,"m":m,"all_missing_image_subsets_checked":seen,
        "exact_max_occupied_adjacent_pairs":maximum,
        "sharp_missing_star_extremum_attained":True,
        "number_tied_extremizers":saturating,
    }


def report():
    rows=[sharp_adjacency_image_bound(2**h) for h in range(1,9)]
    pseudo=[pairwise_capacity_saturated_distribution(2**h)
            for h in range(1,9)]
    return {
        "slice":"HYP105-ISSUE230-D6Y-SHARP-GLOBAL-IMAGE-ADJACENCY-CUT",
        "theorem":"ALL-H-SHARP-GLOBAL-TYPED-PHYSICAL-IMAGE-ADJACENCY",
        "global_injection_both_typed_sides":"EXACT-ALL-H",
        "pairwise_capacity_selected_lifts":"FEASIBLE-BUT-NOT-GLOBALLY-EXTENDIBLE-WHEN-m-POSITIVE",
        "stronger_quadratic_global_image_cut":"NECESSARY-AND-SHARP",
        "not_full_GF5_seven_lower":True,
        "general_Sherali_Adams_gap_PROVED":False,
        "original_global_S_PROVED_A":False,
        "infinite_correlated_counterexample_PROVED_B":False,
        "Branch_A":"OPEN","Branch_B":"OPEN",
        "all_h_parameters":rows,"pairwise_pseudo_orbit":pseudo,
        "finite_full_pair_oracle":[independent_full_pair_oracle(2),
                                   independent_full_pair_oracle(4)],
        "independent_full_missing_edge_oracle":[
            independent_missing_edge_brute(5,3),
            independent_missing_edge_brute(6,4),
            independent_missing_edge_brute(7,5),
        ],
    }


if __name__=="__main__":
    print(json.dumps(report(),sort_keys=True))
