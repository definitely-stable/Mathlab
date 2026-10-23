"""AA4-DG: exactly TWO external genuine ORIGINAL factors needed for local A.

Physical 5-factor original point/line reservoir: occupied 4cycle plus
a disjoint doubled original image. Six DISTINCT physical source
factors forming a 6-vertex 2factor and using >=4 of these 5 MUST
use EXACTLY four reservoir factors: doubled+three of the C4 cycle.
Its TWO extra physically occupied ORIGINAL pair-images bridge both
terminals of the resulting 3-edge path to the two doubled endpoints,
in one of exactly 4*2=8 possible physical ways.

Thus historical accepted D6 (A/A) needs >=2 outside original
factors on EACH typed source side; A/B and C/A need >=2 on their
A side. ANY original source Q using at most ONE outside source factor
on each side cannot be D6, A/B or C/A.

No source ORIGINAL incidence inferred from physical bridge occupancy.
All accepted 6flag checks use immutable original W(3,s) source IDs.
Not Branch A/B/C, no global lower motif count.
"""
from collections import Counter
from itertools import combinations
from math import comb

from hyp105_issue230_d6aa4cq_original_macro_path_cut_gate import _validated_original
from hyp105_issue230_d6aa4cr_exact_BBo_three_matching_transfer import (
    c4_completions_from_single_and_doubled,
    original_nonincident_threepath,
)
from hyp105_issue230_d6aa4cg_four_shared_edge_two_completion import (
    classify_seven_all_a_original_Q,
)
from hyp105_issue230_d6aa4df_fivebyfive_local_compensation import (
    original_local_five_factor_physical_certificate,
)

A_SIDE_POSITIVE_CLASSES=frozenset((
    "D6","A-left/B-right","B-left/A-right","C/A"
))


def _physical_original_A_six_edges(labels,ids):
    """Independent 6-source-factor ORIGINAL physical 2factor predicate."""
    if len(ids)!=6 or len(set(ids))!=6:
        return False
    deg=Counter(v for r in ids for v in labels[r])
    return len(deg)==6 and len(ids)==6 and set(deg.values())=={2}


def original_two_external_A_completion_catalogue(labels,base,doubled,
                                                  physical_C4_source_triple):
    """Exactly the eight 4+2 physical templates, return OCCUPIED source 6-tuples.

    Original source labels must be globally injected typed K_a edges;
    C4 is an ACTUAL occupied triple, doubled edge disjoint from all C4.
    Every returned tuple has exactly 4 LOCAL source IDs and exactly 2
    ORIGINAL external source IDs, all true original factors.
    """
    labels=tuple(tuple(e) for e in labels)
    if len(set(labels))!=len(labels):
        raise ValueError("complete injected ORIGINAL typed source physical factor labels")
    if any(len(e)!=2 or len(set(e))!=2 or any(
        type(x) is not int or x<0 for x in e) for e in labels):
        raise ValueError("canonical simple physical source pair labels required")
    if any(tuple(sorted(e))!=e for e in labels):
        raise ValueError("canonical source original physical pair labels required")
    if type(base)is not int or type(doubled)is not int or not(
        0<=base<len(labels) and 0<=doubled<len(labels)):
        raise ValueError("actual ORIGINAL factor ID required")
    triple=tuple(physical_C4_source_triple)
    if len(triple)!=3 or len(set(triple))!=3 or any(
        type(t) is not int or not 0<=t<len(labels) for t in triple):
        raise ValueError("three different ORIGINAL C4 source factor IDs required")
    # Independent full original-source physical C4 input validator;
    # same five-factor statement as earlier AA4-DF, no source-incidence
    # data needed and no original incidence can be conjured here.
    original_local_five_factor_physical_certificate(
        labels,labels,base,doubled,triple,base,doubled,triple)
    physical_inverse={e:i for i,e in enumerate(labels)}
    cycle=(base,*triple)
    local=frozenset((base,doubled,*triple))
    doubled_uv=labels[doubled]
    results=[]
    for omitted in cycle:
        path=tuple(x for x in cycle if x!=omitted)
        deg=Counter(v for src in path for v in labels[src])
        terminals=tuple(sorted(v for v,n in deg.items() if n==1))
        if len(terminals)!=2 or len(deg)!=4 or sorted(deg.values())!=[1,1,2,2]:
            raise AssertionError("real original 4cycle minus one edge not a simple three-edge path")
        x,y=doubled_uv
        for U,V in (((terminals[0],x),(terminals[1],y)),
                    ((terminals[0],y),(terminals[1],x))):
            ext=tuple(physical_inverse.get(tuple(sorted(e))) for e in (U,V))
            if any(i is None or i in local for i in ext) or len(set(ext))!=2:
                continue
            six=tuple(sorted((doubled,*path,*ext)))
            if not _physical_original_A_six_edges(labels,six):
                raise AssertionError("actual original 6-factor physical source A not 2regular")
            if len(local.intersection(six))!=4:
                raise AssertionError("exact two SOURCE external factor theorem violated")
            results.append(six)
    if len(results)!=len(set(results)) or len(results)>8:
        raise AssertionError("more than exactly eight physical bridge A templates")
    return tuple(results)


def original_two_external_A_anchor_certificate(model,*,anchor_pairs,
                                                max_triples_per_side=None,
                                                max_C4_pairs=None):
    """ACTUAL W3 nonlocal A-side GF5 witness oracle for selected P3 anchors.

    For each actual paired occupied physical C4, enumerate only six-ID
    true-original incidence sets on at most 2 ORIGINAL source factors
    external to EACH five-factor reservoir. If a side has A, the exact
    8-template catalogue is COMPLETE under this two-external cap.
    Other side uses 5 local factors (for B or C), or its A 8-template
    catalog. No fabricated source flags. Counts are per-physical-C4
    reservoir WITH multiplicity; also records distinct original Q sets.

    A C4 cap or C4-pair cap makes run PARTIAL, never all-geometry S.
    """
    s,V,a,f,g,pl,lp=_validated_original(model)
    if anchor_pairs is None:
        raise ValueError("explicit ORIGINAL nonincident source anchor set mandatory")
    if max_triples_per_side is not None and (
        type(max_triples_per_side)is not int or max_triples_per_side<1):
        raise ValueError("positive partial physical source C4 triple cap")
    if max_C4_pairs is not None and (
        type(max_C4_pairs)is not int or max_C4_pairs<1):
        raise ValueError("positive partial paired source C4 cap")
    anchors=tuple(tuple(x) for x in anchor_pairs)
    if len(set(anchors))!=len(anchors):raise ValueError("duplicate original source P3 anchor")
    for p,l in anchors:
        if type(p)is not int or type(l)is not int or not 0<=p<V or not 0<=l<V or l in pl[p]:
            raise ValueError("genuine original W3 nonincident anchor needed")
    invp={e:i for i,e in enumerate(f)}
    invl={e:i for i,e in enumerate(g)}
    inc=tuple(model["incidences"])
    original_flag_id={(p,l):z for z,(p,l) in enumerate(inc)}
    counts=Counter()
    distinct_source_Q=set()
    witness_by_class={}
    first_empty_A_pair=None
    per_anchor=[]
    stop=False
    for p,l in anchors:
        path=original_nonincident_threepath(p,l,pl,lp)
        q,l0=path[1][0],path[0][1]
        if set(f[p])&set(f[q]) or set(g[l])&set(g[l0]):continue
        pts=c4_completions_from_single_and_doubled(f[p],f[q],invp,a)
        lns=c4_completions_from_single_and_doubled(g[l],g[l0],invl,a)
        if max_triples_per_side is not None:
            pts=pts[:max_triples_per_side];lns=lns[:max_triples_per_side]
        for pt in pts:
            for lt in lns:
                if max_C4_pairs is not None and counts["physical_pair_reservoirs_checked"]>=max_C4_pairs:
                    stop=True;break
                sp=original_local_five_factor_physical_certificate(
                    f,g,p,q,pt,l,l0,lt)
                P5=sp["POINT"]["source_original_five_factor_ids"]
                L5=sp["LINE"]["source_original_five_factor_ids"]
                PA=original_two_external_A_completion_catalogue(f,p,q,pt)
                LA=original_two_external_A_completion_catalogue(g,l,l0,lt)
                counts["physical_pair_reservoirs_checked"]+=1
                counts["occupied_POINT_twoexternal_A_templates"]+=len(PA)
                counts["occupied_LINE_twoexternal_A_templates"]+=len(LA)
                if (not PA or not LA) and first_empty_A_pair is None:
                    first_empty_A_pair=(p,l,pt,lt,len(PA),len(LA))
                # Three mutually exclusive historical A-side families.
                # The other side can use full L5 or P5, whose ORIGINAL
                # sixflag endpoint profile B or C is tested by oracle.
                cases=(
                    ("POINT_A_LINE_local",tuple((x,L5) for x in PA)),
                    ("LINE_A_POINT_local",tuple((P5,y) for y in LA)),
                    ("POINT_A_LINE_A",tuple((x,y) for x in PA for y in LA)),
                )
                seen_in_reservoir=set()
                for case,pairs in cases:
                    for P,L in pairs:
                        flaglist=tuple(original_flag_id[i,j]
                                       for i in P for j in L if (i,j) in original_flag_id)
                        if len(flaglist)<6:continue
                        for Q in combinations(flaglist,6):
                            Q=tuple(sorted(Q))
                            if Q in seen_in_reservoir:continue
                            kind=classify_seven_all_a_original_Q(Q,f,g,inc)
                            if kind not in A_SIDE_POSITIVE_CLASSES:
                                continue
                            cp=Counter(inc[z][0] for z in Q)
                            cl=Counter(inc[z][1] for z in Q)
                            if "A" not in (
                                "A" if len(cp)==6 else "",
                                "A" if len(cl)==6 else ""):
                                raise AssertionError("historical A-side tag without actual 6 distinct ORIGINAL factors")
                            if len(cp)==6 and not any(
                                set(cp)==set(t) for t in PA):
                                raise AssertionError("ORIGINAL POINT A source extension not from 8-template catalogue")
                            if len(cl)==6 and not any(
                                set(cl)==set(t) for t in LA):
                                raise AssertionError("ORIGINAL LINE A source extension not from 8-template catalogue")
                            if len(cp)<6 and not set(cp)<=set(P5):
                                raise AssertionError("non-A source point factor escaped tested local reservoir")
                            if len(cl)<6 and not set(cl)<=set(L5):
                                raise AssertionError("non-A source line factor escaped tested local reservoir")
                            counts["original_historical_A_side_positive_C4pair_multiplicity"]+=1
                            counts[f"historical_{kind}"]+=1
                            if kind not in witness_by_class:
                                witness_by_class[kind]=(p,l,tuple(pt),tuple(lt),Q)
                            seen_in_reservoir.add(Q)
                            distinct_source_Q.add(Q)
                if counts["physical_pair_reservoirs_checked"]<=5:
                    per_anchor.append({"anchor":(p,l),"point_A":len(PA),
                                       "line_A":len(LA)})
            if stop:break
        if stop:break
    return {
        "s":s,"V":V,"a":a,
        "physical_original_C4_pair_reservoirs_checked":
            counts["physical_pair_reservoirs_checked"],
        "physical_occupied_POINT_two_external_A_templates":
            counts["occupied_POINT_twoexternal_A_templates"],
        "physical_occupied_LINE_two_external_A_templates":
            counts["occupied_LINE_twoexternal_A_templates"],
        "historical_A_side_original_sixflag_C4_pair_multiplicities":
            {kind:counts[f"historical_{kind}"] for kind in sorted(A_SIDE_POSITIVE_CLASSES)},
        "historical_A_side_original_sixflag_C4_pair_multiplicity_total":
            counts["original_historical_A_side_positive_C4pair_multiplicity"],
        "historical_A_side_original_sixflag_distinct_Q_count":
            len(distinct_source_Q),
        "first_original_historical_A_side_witness_by_class":witness_by_class,
        "first_original_physical_C4_pair_missing_any_A_bridge":first_empty_A_pair,
        "first_real_original_A_template_source_anchor_samples":per_anchor,
        "explicitly_PARTIAL_if_C4_capped":
            max_triples_per_side is not None or max_C4_pairs is not None,
        "all_hist_GF5_positive_original_sevenclass_S_not_proven":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }
