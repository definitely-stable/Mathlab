"""HYP-105 #230 AA4-K32ZERO: genuine W34 zero-fresh-extension falsifier.

Exactly the SAME original 12 selected source incidence IDs, the SAME
complete f point-pair labeling (ALL 85 points), and the SAME g line-pair
labels on ALL 12 selected source lines induce the EXACT SAME selected
coherent physical graph with TWO saturated source-backed K3,2 parents.

Yet TWO different, full separately injected line-pair completions g:
   POS: original #664 protected construction
   ZERO: an explicitly frozen permutation of the OTHER 79 line labels
produce positive (4) vs zero (0) FULL H fresh hub-pair common neighbors.
The original source is TRUE symplectic W(3,4), all 425 real incidence
flags exist in both full maps. This is a finite counterexample to any
claimed universal positive per-saturated-block extension based ONLY
on the selected graph/coherent source IDs or even the entire f map.
It is NOT an infinite o(s^6) HYP-105 seven-GF5 counterfamily.

The frozen permutation is an explicit finite mathematical certificate,
not probabilistic evidence. Independent source-factor incidence-rectangle
and physical full H neighbor oracles MUST both agree.
"""
from itertools import combinations

from hyp105_full_physical_degree_tail import physical, genuine_source
from hyp105_physical_degree_energy import (
    minimal_alphabet, _verify_typed_injections,
)
from hyp105_k32_saturated_unit_multiplicity import (
    real_W34_two_disjoint_saturated_blocks,
    genuine_source_saturated_unit_transfer,
    saturated_bipartite_k32_list,
)

# Frozen bijection on the 79 unused full K14 line-pair labels,
# order of unselected ORIGINAL source line IDs is increasing.
ZERO_OTHER_LINE_PAIR_PERMUTATION = (
    75,64,68,70,3,26,71,36,25,43,58,47,57,42,4,20,67,34,14,29,
    27,33,45,59,74,54,56,9,66,63,31,48,0,49,44,62,78,39,72,15,
    32,24,21,77,5,23,65,40,18,73,10,12,17,55,60,69,41,53,1,76,
    16,6,52,22,35,46,28,7,37,51,2,8,11,19,61,50,13,38,30,
)


def source_incidence_rectangle_counts(hubs, frees, flags, f, g):
    """Independently count FULL H fresh pair hub neighbors by TRUE W flags.

    Does NOT query the physical graph: identify unique ORIGINAL point
    and line labels from typed K_a edges, and require BOTH actual
    point-line incidence relations in the original symplectic GQ.
    """
    a=minimal_alphabet((len(f)))
    occupied_x={v[0] for v in hubs+frees}
    occupied_y={v[1] for v in hubs+frees}
    by_point_label={tuple(sorted(pair)):i for i,pair in enumerate(f)}
    by_line_label={tuple(sorted(pair)):i for i,pair in enumerate(g)}
    if len(by_point_label)!=len(f) or len(by_line_label)!=len(g):
        raise ValueError("separate global pair-label injections required")
    original_incidence=set(flags)
    out={}
    for i,j in combinations(range(len(hubs)),2):
        h1=hubs[i]
        h2=hubs[j]
        accepted=[]
        for x in range(a):
            if x in occupied_x:
                continue
            p1=by_point_label.get(tuple(sorted((h1[0],x))))
            p2=by_point_label.get(tuple(sorted((h2[0],x))))
            if p1 is None or p2 is None:
                continue
            for y in range(a):
                if y in occupied_y:
                    continue
                l1=by_line_label.get(tuple(sorted((h1[1],y))))
                l2=by_line_label.get(tuple(sorted((h2[1],y))))
                if l1 is None or l2 is None:
                    continue
                if ((p1,l1) in original_incidence and
                        (p2,l2) in original_incidence):
                    accepted.append((x,y))
        out[i,j]=tuple(sorted(accepted))
    return out


def true_W34_same_selected_zero_vs_positive_fresh_mass():
    """Two source-valid complete maps, identical f and selected subgraph."""
    positive,f,g_positive,flags,ids=(
        real_W34_two_disjoint_saturated_blocks(return_inputs=True))
    s,V,real_flags=genuine_source(2)
    if (s,V,len(real_flags))!=(4,85,425) or tuple(flags)!=real_flags:
        raise AssertionError("underlying W34 not genuine")
    if len(ids)!=12 or len(set(ids))!=12:
        raise AssertionError("not twelve different ORIGINAL source incidences")
    original_selected_lines={flags[i][1] for i in ids}
    original_selected_points={flags[i][0] for i in ids}
    if len(original_selected_lines)!=len(ids) or (
            len(original_selected_points)!=len(ids)):
        raise AssertionError("selected original flags not source-factor disjoint")
    a=minimal_alphabet(V)
    frozen_pairs={tuple(g_positive[l]) for l in original_selected_lines}
    free_pairs=tuple(pair for pair in combinations(range(a),2)
                     if pair not in frozen_pairs)
    other_lines=tuple(l for l in range(V)
                      if l not in original_selected_lines)
    if not (len(free_pairs)==len(ZERO_OTHER_LINE_PAIR_PERMUTATION)==79
            and len(other_lines)==73):
        raise AssertionError("expected exactly 79 unused K14 pair labels")
    if set(ZERO_OTHER_LINE_PAIR_PERMUTATION)!=set(range(len(free_pairs))):
        raise AssertionError("frozen zero permutation not a bijection")
    g_zero=list(g_positive)
    for l,j in zip(other_lines,ZERO_OTHER_LINE_PAIR_PERMUTATION):
        g_zero[l]=free_pairs[j]
    g_zero=tuple(g_zero)
    _verify_typed_injections(a,V,f,g_positive)
    _verify_typed_injections(a,V,f,g_zero)
    if any(g_positive[l]!=g_zero[l] for l in original_selected_lines):
        raise AssertionError("selected ORIGINAL line labels changed")
    if not any(g_positive[l]!=g_zero[l] for l in other_lines):
        raise AssertionError("two completions accidentally identical")
    selected_pos,prov_pos=physical(ids,flags,f,g_positive)
    selected_zero,prov_zero=physical(ids,flags,f,g_zero)
    if selected_pos!=selected_zero or prov_pos!=prov_zero:
        raise AssertionError("selected SOURCE physical graph not fixed")
    sats=saturated_bipartite_k32_list(selected_pos)
    if len(sats)!=2:
        raise AssertionError("selected graph does not contain two saturated blocks")
    cold=genuine_source_saturated_unit_transfer(2,f,g_zero,ids)
    if (positive["saturated_source_sixsets"]!=
            cold["saturated_source_sixsets"] or
            positive["true_source_selected_incidence_ids"]!=
            cold["true_source_selected_incidence_ids"]):
        raise AssertionError("source selected saturated block families differ")
    if positive["full_H_fresh_common_neighbor_mass"]!=4 or (
            cold["full_H_fresh_common_neighbor_mass"]!=0):
        raise AssertionError("frozen original W34 extension contrast not 4 vs 0")
    if positive["two_swap_D6_extension_memberships"]!=8 or (
            cold["two_swap_D6_extension_memberships"]!=0):
        raise AssertionError("accepted ORIGINAL D6 extension contrast not 8 vs 0")

    cert={}
    for name,g,report in (("positive",g_positive,positive),
                          ("zero",g_zero,cold)):
        full,source_edge_map=physical(range(len(flags)),flags,f,g)
        direct={}
        by_source={}
        for hubs,frees in sats:
            old=tuple(sorted(
                source_edge_map[tuple(sorted((h,z)))
                ] for h in hubs for z in frees))
            if old in direct:
                raise AssertionError("two saturated blocks share original sixset")
            inferred=source_incidence_rectangle_counts(
                hubs,frees,flags,f,g)
            geometric={
                ij:tuple(sorted(
                    w for w in full.get(hubs[ij[0]],set()) &
                    full.get(hubs[ij[1]],set())
                    if w[0] not in {v[0] for v in hubs+frees}
                    and w[1] not in {v[1] for v in hubs+frees}
                ))
                for ij in combinations(range(3),2)
            }
            if inferred!=geometric:
                raise AssertionError("source incidence and FULL physical neighbor count disagree")
            direct[old]=inferred
            by_source[old]=geometric
        count=sum(len(w) for groups in direct.values() for w in groups.values())
        if count!=report["full_H_fresh_common_neighbor_mass"]:
            raise AssertionError("source-only direct count disagrees with GF5 classified extension")
        cert[name]={
            "per_source_block_per_hub_pair_fresh":tuple(
                sorted((old,tuple(sorted(q.items()))) for old,q in direct.items())
            ),
            "independent_original_source_rectangle_count":count,
            "selected_true_original_GF5_D6":report["selected_original_GF5_D6"],
            "full_map_original_D6_radius_two_extensions":
                report["two_swap_D6_extension_memberships"],
        }
    if cert["zero"]["independent_original_source_rectangle_count"]!=0:
        raise AssertionError("full original source zero extension example invalid")
    return {
        "s":s,"V":V,"original_source_incidence_flags":len(flags),
        "globally_injected_point_pair_labels_identical":True,
        "all_selected_original_line_pairs_identical":True,
        "same_selected_physical_adjacency_and_source_provenance":True,
        "selected_source_ID_count":len(ids),
        "selected_source_incidence_IDs":tuple(ids),
        "same_saturated_selected_K32_blocks":len(sats),
        "selected_ordinary_C6_both":positive["selected_ordinary_C6"],
        "positive":cert["positive"],
        "zero":cert["zero"],
        "full_maps_both_source_GQ_and_complete":True,
        "finite_W34_selected_structure_cannot_force_fresh_mass":True,
        "infinite_asymptotic_HYP105_counterexample":False,
    }
