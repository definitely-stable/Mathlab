"""AA4-DF: exact 5+5 genuine-original local GF(5) compensation gate.

Original source P3 p--l0--q--l, an actually occupied point C4
completion of physical base f(p) avoiding doubled f(q), and an actual
LINE C4 completion of g(l) avoiding doubled g(l0), define on each
typed source side the FULL 5-factor local reservoir:
    {anchor base, doubled ORIGINAL factor, C4's 3 ORIGINAL factor IDs}.
Physical occupied pair images induce ONE 4-cycle plus ONE disjoint edge.

THEOREM for ANY genuine original W(3,s), ALL complete arbitrary
correlated globally injected typed f,g, ANY local paired C4:
  - no six distinct ORIGINAL source incidence-ID Q on this 5x5 source
    reservoir can have a physical A profile;
  - on either side physical B source profile forces doubled original
    factor q / l0 to be the unique repeated factor;
  - physical C source profile forces the THREE repeated source factors
    to be EITHER {doubled, anchor base, physical C4 center}
    OR {doubled, two C4 spoke source factors};
  - among seven historically accepted GF5-positive original 6flag
    classes, ONLY C/B (both orientations), B/B-overlap and
    B/B-disjoint can occur inside THIS reservoir.
This is not a claim that those classes necessarily occur. A local
no-positive-but-Hall-marked original W3 witness forbids any universal
PER-LOCAL-PAIR compensation into this same reservoir. Other original
factor IDs may still contribute global sevenclass motifs; root OPEN.
"""
from collections import Counter
from itertools import combinations

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4cq_original_macro_path_cut_gate import _validated_original
from hyp105_issue230_d6aa4cr_exact_BBo_three_matching_transfer import (
    c4_completions_from_single_and_doubled,
    original_nonincident_threepath,
)
from hyp105_issue230_d6aa4dc_marked_cofactor_hall_deficit import (
    original_three_by_three_cofactor_certificate,
)
from hyp105_issue230_d6aa4cg_four_shared_edge_two_completion import (
    classify_seven_all_a_original_Q,
)

SUPPORTED_LOCAL_CLASSES=frozenset(("C/B","B/B-overlap","B/B-disjoint"))


def _physical_regular6_by_source_factor_ids(flags,original_labels):
    deg=Counter()
    for src in flags:
        deg.update(original_labels[src])
    return len(deg)==6 and all(deg[v]==2 for v in deg)


def original_local_profile_sixflag(ids,inc,f,g):
    """Independent exact SOURCE-ID physical seven-profile oracle.

    All original six incidence IDs must be immutable from same W3
    incident factor list. For an arbitrary original source sixflag,
    returns one of three locally possible historically accepted tags,
    or None if physical 2factor/profile rejects.
    """
    ids=tuple(ids)
    if len(ids)!=6 or len(set(ids))!=6 or any(
        type(i) is not int or not 0<=i<len(inc) for i in ids
    ):
        raise ValueError("six distinct immutable TRUE ORIGINAL incidence IDs required")
    points=tuple(inc[i][0] for i in ids)
    lines=tuple(inc[i][1] for i in ids)
    cp=Counter(points);cl=Counter(lines)
    def physical_degree(ids,labels):
        degree=Counter()
        for x in ids:degree.update(labels[x])
        return len(degree)==6 and all(value==2 for value in degree.values())
    if not physical_degree(points,f) or not physical_degree(lines,g):
        return None
    patterns={
        (1,1,1,1,2):"B",
        (2,2,2):"C",
    }
    P=patterns.get(tuple(sorted(cp.values())))
    L=patterns.get(tuple(sorted(cl.values())))
    if not P or not L:return None
    if (P,L) in (("B","C"),("C","B")):return "C/B"
    if (P,L)==("B","B"):
        point_repeated=next(i for i,t in cp.items() if t==2)
        line_repeated=next(j for j,t in cl.items() if t==2)
        # ORIGINAL source INCIDENCE ID, not generic source edge.
        return ("B/B-overlap" if any(
            inc[z]==(point_repeated,line_repeated) for z in ids
        ) else "B/B-disjoint")
    return None


def original_local_five_factor_physical_certificate(
        f,g,point_base,point_doubled,point_triple,
        line_base,line_doubled,line_triple):
    """Structural proof-witness for any ACTUALLY occupied paired C4."""
    def side(labels,base,double,triple):
        base,double=frozenset(labels[base]),frozenset(labels[double])
        triple=tuple(triple)
        if len(triple)!=3 or len(set(triple))!=3 or base&double:
            raise ValueError("actual distinct original source C4 triple and disjoint doubled required")
        if base in (frozenset(labels[i]) for i in triple) or any(
            frozenset(labels[i])&double for i in triple
        ):
            raise ValueError("source occupied C4 triple cannot be anchor/doubled physical pair")
        cycle=tuple([base]+[frozenset(labels[i]) for i in triple])
        degree=Counter(u for edge in cycle for u in edge)
        if len(degree)!=4 or any(n!=2 for n in degree.values()):
            raise ValueError("four ACTUALLY occupied source images must form physical 4cycle")
        spokes=tuple(i for i in triple if len(set(labels[i])&base)==1)
        center=tuple(i for i in triple if set(labels[i]).isdisjoint(base))
        if len(spokes)!=2 or len(center)!=1:
            raise ValueError("actual occupied C4 triple is not 2 spokes + center")
        if set(labels[spokes[0]])&set(labels[spokes[1]]):
            raise AssertionError("opposite actual original source C4 spokes should be disjoint")
        physical_B_repeated_factor=double_source_id
        return None
    # Deliberately define without using the seven source classifier:
    # 4cycle has exactly 2 opposite-edge matchings; isolated doubled
    # original physical image extends each to a 3-edge perfect matching.
    def witness(labels,base_id,doubled_id,triple_ids):
        base=frozenset(labels[base_id]);double=frozenset(labels[doubled_id])
        triple_ids=tuple(triple_ids)
        if len(triple_ids)!=3 or len(set(triple_ids))!=3 or base&double:
            raise ValueError("invalid ORIGINAL source C4 triple/doubled")
        images=[frozenset(labels[t]) for t in triple_ids]
        if len(set(images))!=3 or any(e&double or e==base for e in images):
            raise ValueError("C4 source factors must be unique and avoid doubled source image")
        cycle=[base]+images
        deg=Counter(u for e in cycle for u in e)
        if len(deg)!=4 or set(deg.values())!={2}:
            raise ValueError("source physical 4cycle does not close")
        spokes=tuple(t for t in triple_ids if len(set(labels[t])&base)==1)
        centers=tuple(t for t in triple_ids if set(labels[t]).isdisjoint(base))
        if len(spokes)!=2 or len(centers)!=1:
            raise ValueError("source occupied original C4 wrong spoke/center structure")
        if set(labels[spokes[0]])&set(labels[spokes[1]]):
            raise AssertionError("opposite source physical C4 spokes overlap")
        triples=(tuple(sorted((doubled_id,base_id,centers[0]))),
                 tuple(sorted((doubled_id,*spokes))))
        if len(set(triples))!=2 or not all(
            len({v for t in tri for v in labels[t]})==6 and
            len({v for t in tri for v in labels[t]})==sum(len(labels[t]) for t in tri)
            for tri in triples
        ):
            raise AssertionError("exactly two disjoint physical C-profile source triples required")
        original_factors=frozenset((base_id,doubled_id,*triple_ids))
        if len(original_factors)!=5:
            raise AssertionError("two-base + original three C4 source factors are not distinct")
        return {"source_original_five_factor_ids":tuple(sorted(original_factors)),
                "original_B_only_possible_repeated_source_factor":doubled_id,
                "original_C_possible_three_repeated_source_factor_sets":triples,
                "two_ACTUAL_original_source_spokes":tuple(sorted(spokes)),
                "original_physical_center_source_factor":centers[0],
                "physical_source_4cycle_original_image_factors":
                   tuple(sorted((base_id,*triple_ids)))}
    return {"POINT":witness(f,point_base,point_doubled,point_triple),
            "LINE":witness(g,line_base,line_doubled,line_triple)}


def exact_original_local_fivebyfive_seven_census(
        model, *, anchor_pairs, max_triples_per_side=None):
    """An ACTUAL true-original SOURCE 5x5 local entire-sixflag census.

    Immutable source incidence IDs only, both physical f and g
    6-coordinate two-regular constraints and historical seven tags.
    One source sixflag may be counted in MULTIPLE local reservoirs;
    return multiset counts separately from globally distinct Q IDs.
    cap is explicitly a PARTIAL physical completion experiment.
    """
    s,V,a,f,g,pl,lp=_validated_original(model)
    if anchor_pairs is None:
        raise ValueError("explicit genuine ORIGINAL source nonincident anchor list required")
    if max_triples_per_side is not None and (
        type(max_triples_per_side)is not int or max_triples_per_side<1):
        raise ValueError("positive C4 completion cap required")
    anchors=tuple(tuple(x) for x in anchor_pairs)
    if len(anchors)!=len(set(anchors)):
        raise ValueError("duplicate ORIGINAL source nonincident anchor")
    for p,l in anchors:
        if (type(p)is not int or type(l)is not int or
            not 0<=p<V or not 0<=l<V or l in pl[p]):
            raise ValueError("not genuine original W3 nonincident source anchor")
    inc=tuple(model["incidences"])
    if len(inc)!=V*(s+1) or len(set(inc))!=len(inc):
        raise AssertionError("genuine original source incidence IDs not immutable unique")
    source_flags={(p,l):index for index,(p,l) in enumerate(inc)}
    invf={tuple(sorted(e)):i for i,e in enumerate(f)}
    invg={tuple(sorted(e)):i for i,e in enumerate(g)}
    if len(invf)!=V or len(invg)!=V:
        raise ValueError("globally complete typed ORIGINAL source map must inject")
    totals=Counter()
    allowed=Counter()
    original_Q_distinct=set()
    witness_zero_local=None
    witness_local_positive=None
    first_hall=None
    max_induced_source_incidence=0
    for p,l in anchors:
        three=original_nonincident_threepath(p,l,pl,lp)
        q,l0=three[1][0],three[0][1]
        if set(f[p])&set(f[q]) or set(g[l])&set(g[l0]):
            continue
        pt=c4_completions_from_single_and_doubled(f[p],f[q],invf,a)
        lt=c4_completions_from_single_and_doubled(g[l],g[l0],invg,a)
        if max_triples_per_side is not None:
            pt=pt[:max_triples_per_side];lt=lt[:max_triples_per_side]
        for pc in pt:
            for lc in lt:
                structure=original_local_five_factor_physical_certificate(
                    f,g,p,q,pc,l,l0,lc)
                P=structure["POINT"]["source_original_five_factor_ids"]
                L=structure["LINE"]["source_original_five_factor_ids"]
                local_flags=tuple(source_flags[(i,j)] for i in P for j in L
                                  if (i,j) in source_flags)
                # Independent local source GQ sixflag must have six real
                # original immutable edge IDs from its own TRUE 5x5 forest.
                positive_local=Counter()
                for ids in combinations(local_flags,6):
                    fast=original_local_profile_sixflag(ids,inc,f,g)
                    oracle=classify_seven_all_a_original_Q(ids,f,g,inc)
                    if fast!=oracle:
                        raise AssertionError("independent ORIGINAL local 7-class oracle disagreement")
                    if oracle:
                        if oracle not in SUPPORTED_LOCAL_CLASSES:
                            raise AssertionError("a forbidden historical A/C-class appears in local 5+5 C4 reservoir")
                        cp=Counter(inc[z][0] for z in ids)
                        cl=Counter(inc[z][1] for z in ids)
                        if len(cp)==5 and next(i for i,n in cp.items() if n==2)!=q:
                            raise AssertionError("local original B must repeat the doubled POINT source factor")
                        if len(cl)==5 and next(j for j,n in cl.items() if n==2)!=l0:
                            raise AssertionError("local original B must repeat the doubled LINE source factor")
                        if len(cp)==3 and tuple(sorted(cp)) not in (
                            structure["POINT"]["original_C_possible_three_repeated_source_factor_sets"]
                        ):
                            raise AssertionError("local C POINT source triple not one of 2 possible physical matchings")
                        if len(cl)==3 and tuple(sorted(cl)) not in (
                            structure["LINE"]["original_C_possible_three_repeated_source_factor_sets"]
                        ):
                            raise AssertionError("local C LINE source triple not one of 2 possible physical matchings")
                        positive_local[oracle]+=1
                        original_Q_distinct.add(ids)
                totals["all_occupied_original_point_line_C4_pair_reservoirs"]+=1
                totals["local_true_original_source_Q_six_combinations_tested"]+=comb(
                    len(local_flags),6) if len(local_flags)>=6 else 0
                max_induced_source_incidence=max(max_induced_source_incidence,len(local_flags))
                totals["local_true_original_induced_SOURCE_incidence_flag_mass"]+=len(local_flags)
                npositive=sum(positive_local.values())
                totals["all_local_positive_sixflag_incidence_set_multiplicities"]+=npositive
                allowed.update(positive_local)
                # Full original source C4 3x3 cofactor, sorted physical spokes:
                psp=tuple(sorted(i for i in pc if len(set(f[i])&set(f[p]))==1))
                lsp=tuple(sorted(j for j in lc if len(set(g[j])&set(g[l]))==1))
                pcenter=next(i for i in pc if i not in psp)
                lcenter=next(j for j in lc if j not in lsp)
                B=tuple(tuple(int(j in pl[i]) for j in (*lsp,lcenter))
                        for i in (*psp,pcenter))
                co=original_three_by_three_cofactor_certificate(B)
                marked=co["original_C4_pair_spoke_spoke_marked_flags"]
                if marked and co["true_original_3x3_permanent"]==0:
                    totals["original_MARKED_no_3matching_local_source_C4_pairs"]+=1
                    if first_hall is None:first_hall=(p,l,pc,lc,B,co["minimal_true_original_Hall_deficiency"])
                    if not npositive:
                        totals["actual_original_marked_Hall_failure_with_ZERO_LOCAL_positive_GF5_pairs"]+=1
                        if witness_zero_local is None:
                            witness_zero_local={
                                "true_original_source_P3_anchor":(p,l),
                                "true_original_point_C4_factor_ids":tuple(pc),
                                "true_original_LINE_C4_factor_ids":tuple(lc),
                                "genuine_original_point_and_LINE_SOURCE_5x5_factor_ids":(P,L),
                                "all_genuine_original_source_incidence_IDs_inside_reservoir":local_flags,
                                "original_SOURCE_3x3_spokes_center_incidence":B,
                                "original_matching_Hall_failure":co["minimal_true_original_Hall_deficiency"],
                                "zero_accepted_local_sevenclass_G5_SOURCE_sixflags":True,
                            }
                if positive_local and witness_local_positive is None:
                    witness_local_positive=(p,l,pc,lc,dict(positive_local))
    return {
        "s":s,"V":V,"a":a,
        "true_original_nonincident_P3_anchors_requested":len(anchors),
        "original_occupied_C4_pairs_checked":totals["all_occupied_original_point_line_C4_pair_reservoirs"],
        "local_max_actual_original_source_incidence_IDs_in_5x5":
             max_induced_source_incidence,
        "local_original_sixflag_source_Q_tested":
             totals["local_true_original_source_Q_six_combinations_tested"],
        "local_accepted_historical_sevenclass_G5_multiset_by_label":dict(allowed),
        "local_accepted_historical_sevenclass_G5_total_C4pair_multiplicity":
             totals["all_local_positive_sixflag_incidence_set_multiplicities"],
        "local_accepted_six_original_incidence_ID_sets_distinct_across_reservoirs":
             len(original_Q_distinct),
        "true_original_marked_cofactor_Hall_failing_C4_pairs":
             totals["original_MARKED_no_3matching_local_source_C4_pairs"],
        "true_original_marked_cofactor_Hall_failing_C4_pairs_WITH_NO_LOCAL_positive_classes":
             totals["actual_original_marked_Hall_failure_with_ZERO_LOCAL_positive_GF5_pairs"],
        "first_exact_genuine_original_Hall_marked_but_NO_LOCAL_positive_witness":
             witness_zero_local,
        "first_actual_original_Hall_witness":first_hall,
        "first_local_positive_sixflag_source_witness":witness_local_positive,
        "local_supported_positive_classes":tuple(sorted(SUPPORTED_LOCAL_CLASSES)),
        "C4_cap_means_partial":max_triples_per_side is not None,
        "cannot_infer_ROOT_all_seven_global_S_from_local_reservoir":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }
