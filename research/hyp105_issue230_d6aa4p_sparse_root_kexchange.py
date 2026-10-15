"""HYP-105 #230 D6-AA4-P: exact physical-root dual of TRUE ORIGINAL GF5 quintic.

An exact all-h sparse support identity:
  I_BA,int(f,g) = sum_p sum_{U 4-subset disjoint f(p)}
                  sum_{C4 of K(U) occupied by image f}
                  w_g(p, source_f(C4)).
Only <= 3*V*C(a-2,4) physically active quintic support keys per
complete globally injected f; for actual W32 bijection f: all K6 edges
are present and exactly 15*3=45 compatible source support keys.

Full derangement neighborhood at distance <=4 in S_15 has
  105 distance-2, 910 distance-3, and 12285 distance-4 maps,
  TOTAL 13300 including all k=2,3,4. Every map remains FULL original
source factor-to-physical-edge injection; no local per-Q relabeling.
Result is exact finite exchange-neighborhood certificate, not the
global minimum over 15! full maps nor any all-h HYP-105 result.
"""
from itertools import combinations,permutations
from math import comb, factorial
from collections import Counter
from functools import lru_cache

from hyp105_issue230_d6aa4o_quintic_adversarial_swap import (
    true_original_W32_fixed_g_weighted_tensor,
    exact_original_BA_energy,
)


@lru_cache(None)
def _C4_edges_for_four_coordinates(coords):
    coords=tuple(coords)
    if (len(coords)!=4 or tuple(sorted(set(coords)))!=coords or
            any(type(x) is not int or x<0 for x in coords)):
        raise ValueError("four distinct sorted physical coordinate symbols required")
    a,b,c,d=coords
    K4=set(combinations(coords,2))
    matchings=(((a,b),(c,d)),((a,c),(b,d)),((a,d),(b,c)))
    graphs=tuple(tuple(sorted(K4-set(m))) for m in matchings)
    if len(graphs)!=3 or len(set(graphs))!=3 or any(len(x)!=4 for x in graphs):
        raise AssertionError("physical K4 C4 set exact 3-cycle enumeration failed")
    for C4 in graphs:
        if any(sum(v in edge for edge in C4)!=2 for v in coords):
            raise AssertionError("true physical C4 degree not 2")
    return graphs


def exact_physically_active_source_B_supports(labels,a=6):
    """ALL-h root/physical 4-coordinates enumerator, no tensor input.

    Globally one-to-one assigned physical edges, but physical image may
    miss K_a edges for a>6. Only actual complete f labels are allowed.
    All sets here satisfy left-B six-coordinate degree 2 exactly.
    """
    labels=tuple(tuple(x) for x in labels)
    if type(a) is not int or a<6:
        raise ValueError("physical coordinate alphabet a>=6 required")
    if len(labels)>comb(a,2) or len(set(labels))!=len(labels):
        raise ValueError("source point image is not globally edge-injective")
    if any(len(e)!=2 or any(type(x) is not int for x in e)
           or not 0<=e[0]<e[1]<a for e in labels):
        raise ValueError("noncanonical source physical pair edge")
    reverse={edge:p for p,edge in enumerate(labels)}
    support=[]
    for p,edge in enumerate(labels):
        complement=tuple(c for c in range(a) if c not in edge)
        for four_coords in combinations(complement,4):
            for C4 in _C4_edges_for_four_coordinates(four_coords):
                if all(e in reverse for e in C4):
                    ids=(p,)+tuple(sorted(reverse[e] for e in C4))
                    if len(set(ids))!=5:
                        raise AssertionError("actual B left physical source factors not distinct")
                    support.append(ids)
    if len(set(support))!=len(support):
        raise AssertionError("physical left-B support counted twice")
    upper=len(labels)*3*comb(a-2,4)
    if len(support)>upper:
        raise AssertionError("sparse all-h B supports exceed physical alphabet cap")
    if a==6 and len(labels)==15:
        # All K6 physical edges occupied exactly once. Root's physical
        # complement is ONE 4-symbol set, with EXACTLY three C4s.
        if len(support)!=45 or len({p for p,*A in support})!=15:
            raise AssertionError("true complete W32 sparse 45 left-B supports false")
        roots=Counter(p for p,*A in support)
        if any(roots[p]!=3 for p in range(15)):
            raise AssertionError("true K6 complete left-B exactly 3 per original source point false")
    return tuple(support)


def exact_sparse_original_BA_energy(tensor,labels,a=6,*,return_supports=False):
    """Exact globally injected GF5 true-original energy in O(V*a^4)."""
    support=exact_physically_active_source_B_supports(labels,a)
    weights=dict(tensor["terms"])
    value=sum(weights.get(ids,0) for ids in support)
    if return_supports:
        return {"energy":value,"compatible_physical_B_supports":len(support),
                "positive_weight_B_supports":sum(weights.get(ids,0)>0 for ids in support),
                "sparse_active_source_factor_keys":support}
    return value


def all_coordinate_orbit_images(labels,a=6):
    """All a! point-physical-coordinate relabelings, with fixed right g.

    This symmetry applies to the BA INTERNAL quintic because the left-B
    predicate depends only on physical C4/disjointness on LEFT.
    DO NOT claim it preserves the full seven-GF5 ROOT S or arbitrary
    mixed physical point/line coordinate alignment.
    """
    if type(a) is not int or a<6 or a>7:
        raise ValueError("finite verified orbit enumeration a=6 or 7 only")
    f=tuple(tuple(x) for x in labels)
    if len(set(f))!=len(f):
        raise ValueError("point injection broken")
    orbit=[]
    for perm in permutations(range(a)):
        relabeled=tuple(tuple(sorted((perm[x],perm[y]))) for x,y in f)
        orbit.append(relabeled)
    if a==6 and len(f)==15 and len(set(orbit))!=factorial(a):
        raise AssertionError("full K6 map physical coordinate S6 action not free")
    return orbit


def exact_distance_k_derangement_frontier(tensor,labels,k):
    """Exact finite ALL globally admissible assignments at Hamming distance k.

    Enumerate every k-source subset and each derangement of its k
    physical edge images. This is a complete neighborhood certificate
    at EXACT distance k, and NOT a certificate over all 15! maps.
    """
    if type(k) is not int or k not in (2,3,4):
        raise ValueError("only exact 2-, 3-, or 4-source exchange supported")
    f=tuple(tuple(x) for x in labels)
    if len(f)!=15 or len(set(f))!=15:
        raise ValueError("must start from complete true ORIGINAL W32 K6 edge bijection")
    old=exact_sparse_original_BA_energy(tensor,f)
    best=(old,(),f)
    examined=0
    min_delta=0
    histogram=Counter()
    for source in combinations(range(15),k):
        images=tuple(f[p] for p in source)
        for choice in permutations(images):
            if any(choice[j]==images[j] for j in range(k)):
                continue
            new=list(f)
            for p,e in zip(source,choice):new[p]=e
            val=exact_sparse_original_BA_energy(tensor,new)
            examined+=1
            delta=val-old
            histogram["lower" if delta<0 else "equal" if delta==0 else "higher"]+=1
            if (val,source,tuple(new))<(best[0],best[1],best[2]):
                best=(val,source,tuple(new))
            min_delta=min(min_delta,delta)
    expected={2:105,3:910,4:12285}[k]
    if examined!=expected or sum(histogram.values())!=examined:
        raise AssertionError("missing exact complete permutation-neighborhood assignments")
    if old+min_delta!=best[0]:
        raise AssertionError("exact min delta not equal best actual global f score")
    if len(set(best[2]))!=15 or exact_sparse_original_BA_energy(tensor,best[2])!=best[0]:
        raise AssertionError("all candidate source maps must be full globally injected")
    return {
        "exact_support_changed_source_points":k,
        "number_of_complete_globally_injective_point_maps_checked":examined,
        "original_BA_internal_charge":old,
        "best_neighborhood_BA_internal_charge":best[0],
        "exact_min_delta":min_delta,
        "strictly_improving_full_maps":histogram["lower"],
        "equal_cost_full_maps":histogram["equal"],
        "worse_full_maps":histogram["higher"],
        "best_changed_original_source_point_IDs":best[1],
        "best_global_point_labels":best[2],
        "full_exact_k_permutation_neighborhood_checked":True,
        "global_original_all_15_factor_assignment_minimum_NOT_proved":True,
    }


def exact_W32_original_kexchange_report(scheme):
    """Independent full ORIGINAL seven GF5 proof oracle for exact k=2,3,4."""
    from hyp105_issue230_projection import fixture
    from hyp105_g5e2b3e1b0_seven_signature import seven_census
    model=fixture(1,scheme)
    tensor=true_original_W32_fixed_g_weighted_tensor(model)
    original_f=tuple(tuple(x) for x in model["left_labels"])
    right=tuple(tuple(x) for x in model["right_labels"])
    sparse=exact_sparse_original_BA_energy(tensor,original_f,return_supports=True)
    full=exact_original_BA_energy(tensor,original_f)
    if sparse["energy"]!=full:
        raise AssertionError("new physical-root sparse 45-support identity differs from AA4-O quintic tensor")
    historical=seven_census(model,independent_checks=False,witness_sets=True)
    from collections import Counter
    def historical_BA_internal(source_labels):
        x={**model,"left_labels":tuple(tuple(e) for e in source_labels)}
        census=seven_census(x,independent_checks=False,witness_sets=True)
        charged=0
        for Q,tag in census["sets"].items():
            if tag!="B-left/A-right":
                continue
            points=Counter(model["incidences"][j][0] for j in Q)
            root=next(p for p,n in points.items() if n==2)
            lines=[model["incidences"][j][1] for j in Q
                   if model["incidences"][j][0]==root]
            if len(lines)!=2:
                raise AssertionError("not two genuine ORIGINAL root line factors")
            charged+=not(set(right[lines[0]])&set(right[lines[1]]))
        return charged,census["S_seven"]
    actual,S0=historical_BA_internal(original_f)
    if (actual,S0)!=(full,{"S68":68,"S72":72}[scheme]):
        raise AssertionError("baseline true original seven-GF5 historical census changed")
    orbit=all_coordinate_orbit_images(original_f)
    if len(orbit)!=720 or any(
        exact_sparse_original_BA_energy(tensor,new)!=full for new in orbit):
        raise AssertionError("source-point physical S6 action not exact internal BA charge symmetry")
    frontiers=[exact_distance_k_derangement_frontier(tensor,original_f,k)
               for k in (2,3,4)]
    enriched=[]
    for result in frontiers:
        bestlabels=result["best_global_point_labels"]
        from_quintic=exact_original_BA_energy(tensor,bestlabels)
        verified,seven=historical_BA_internal(bestlabels)
        if from_quintic!=verified or verified!=result["best_neighborhood_BA_internal_charge"]:
            raise AssertionError("sparse k-exchange minimum not genuine ORIGINAL historical GF5")
        enriched.append({
            **result,
            "full_dense_5_source_quintic_oracle":"PASS",
            "full_original_62370_sixset_GF5_oracle":"PASS",
            "historical_full_original_seven_GF5_positive_Q_at_k_frontier":seven,
        })
    min_k=next((row["exact_support_changed_source_points"] for row in enriched
                if row["best_neighborhood_BA_internal_charge"]<full),None)
    return {
        "scheme":scheme,
        "original_right_g_UNCHANGED_across_all_complete_point_maps":True,
        "original_incidence_ids":45,
        "baseline_internal_BA_charge":full,
        "baseline_full_original_positive_GF5_seven_S":S0,
        "physical_B_supports_per_complete_K6_point_map":45,
        "source_root_C4_candidates_per_actual_original_point":3,
        "all_source_coordinate_S6_orbit_size":len(orbit),
        "source_coordinate_action_exact_BA_charge_invariance":"PASS",
        "exact_distances_2_3_4_full_injection_neighborhood":enriched,
        "minimum_improving_source_exchange_support_size_within_2_3_4":min_k,
        "all_13300_nonidentity_k_le_4_full_injections_checked":True,
        "parent_AA4O_one_swap_global_certificate_NO_GO":True,
        "all_15_source_global_minimum_certified":False,
        "root_A":"OPEN","root_B":"OPEN",
    }


def report(scheme=None):
    if scheme is None:
        return {
            "slice":"HYP105-ISSUE230-D6-AA4-P-SPARSE-ROOT-KEXCHANGE",
            "all_h_exact_root_C4_source_support_duality":True,
            "all_h_sparse_physical_B_support_limit":"3*V*binom(a-2,4)",
            "complete_original_W32_K6_exact_45_active_five_factor_supports":True,
            "full_original_W32_hamming_exchange_counts":{"k2":105,"k3":910,"k4":12285,"all":13300},
            "root_A":"OPEN","root_B":"OPEN",
            "global_assignment_minimum_PROVED":False,
        }
    if scheme not in ("S68","S72"):
        raise ValueError("only pinned genuine true ORIGINAL W32 schemes")
    return exact_W32_original_kexchange_report(scheme)


if __name__=="__main__":
    import argparse,json
    p=argparse.ArgumentParser()
    p.add_argument("--scheme",choices=("S68","S72"))
    x=p.parse_args()
    print(json.dumps(report(x.scheme),sort_keys=True,indent=2))
