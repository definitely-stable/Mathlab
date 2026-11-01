"""AA4-SIGN10: sharp full-ten-sign GF(5) root risk floor on ORIGINAL six IDs.

Independent signed-partition aggregation on top of #687's two SEPARATE
full-GF5 oracles; no generic finite-h fitting and no changes to f or g.
The new theorem concerns the *signed-event expectation* R3, not the
probability of a UNION of overlapping signed events.
"""
from collections import Counter
from fractions import Fraction

from hyp105_gf5_original_sixid_flow_referee import (
    SIGNS, c4_edge_sets, coincident_c6_template, bb_overlap_templates,
    gf5_flow_inclusion_exclusion, gf5_flow_spanning_tree,
    original_projected_column_edges, planted_original_bb_overlap,
    planted_original_d6, _fill_f_g, _minimal_alphabet,
)

PALETTE_DENOMINATOR=51**6
HISTORICAL_D6_COEFFICIENT=5643
HISTORICAL_BBO_COEFFICIENT=51750
SHARP_D6_COEFFICIENT=54162
SHARP_BBO_COEFFICIENT=53526


def signed_flow_vector(edges, *, independent_tree=False):
    """Ten DISTINCT global-sign-unordered 3+3 signed events on six named IDs."""
    if len(SIGNS)!=10 or len(set(SIGNS))!=10:
        raise AssertionError("incorrect 3+3 global-sign quotient")
    values=tuple(gf5_flow_inclusion_exclusion(edges,mask) for mask in SIGNS)
    if independent_tree:
        independent=tuple(gf5_flow_spanning_tree(edges,mask) for mask in SIGNS)
        if values != independent:
            raise AssertionError("independent GF5 chord solver contradicts IE on signs")
    if any(v<=0 for v in values):
        raise AssertionError("nonpositive GF5 event in claimed positive leading class")
    return values


def coincident_d6_full_signed_certificate(*, independent_tree=False):
    counts=signed_flow_vector(coincident_c6_template(),
                              independent_tree=independent_tree)
    multiplicities=Counter(counts)
    if multiplicities != Counter({5265:3,5454:6,5643:1}):
        raise AssertionError("unexpected full ten-sign D6 distribution")
    if sum(counts)!=SHARP_D6_COEFFICIENT:
        raise AssertionError("exact D6 signed mass not 54162")
    return {"ten_signed_counts":counts,"histogram":dict(sorted(multiplicities.items())),
            "all_ten_signed_events":10,"exact_total":sum(counts),
            "old_one_event_lower":HISTORICAL_D6_COEFFICIENT,
            "improvement":Fraction(sum(counts),HISTORICAL_D6_COEFFICIENT)}


def bb_overlap_full_signed_certificate(*, independent_tree=False):
    vectors=tuple(signed_flow_vector(e,independent_tree=independent_tree)
                  for e in bb_overlap_templates())
    if len(vectors)!=9:
        raise AssertionError("nine physical C4/C4 pairs required")
    totals=tuple(map(sum,vectors))
    distribution=Counter(totals)
    if distribution!=Counter({53526:6,53838:3}):
        raise AssertionError("incorrect exact B/B-overlap total-sign mass")
    if sum(totals)!=482670 or min(totals)!=SHARP_BBO_COEFFICIENT:
        raise AssertionError("incorrect all-template signed BBo total")
    return {"nine_template_totals":totals,"histogram":dict(sorted(distribution.items())),
            "min_exact_ten_signs_per_original_sixset":min(totals),
            "max_exact_ten_signs_per_original_sixset":max(totals),
            "sum_all_nine":sum(totals),
            "old_ten_times_min_lower":HISTORICAL_BBO_COEFFICIENT,
            "improvement":Fraction(min(totals),HISTORICAL_BBO_COEFFICIENT)}


def _physical_c4_factor_labels(named_column_ids, adjacency_edges):
    """Column graph's EDGE = one physical coordinate, label every source
    factor/column with its two distinct incident coordinate symbols.
    """
    labels={}
    for col in named_column_ids:
        coords=tuple(i for i,e in enumerate(adjacency_edges) if col in e)
        if len(coords)!=2:
            raise AssertionError("physical C4 coordinate degree !=2")
        labels[col]=coords
    if len(set(labels.values()))!=4:
        raise AssertionError("physical C4 labels not globally injective")
    return labels


def true_original_nine_bbo_lifts(power, *, independent_tree=False):
    """For SAME true original six flags, construct NINE fully legal f,g.

    Full original q--ell--p--r plus three disjoint genuine flag IDs.
    Only the fixed typed physical pair maps vary, not the source flags.
    Every C4/C4 named incidence pattern is realized, including a
    literal sharp-minimum signed total 53526 on a true W(3,s).
    """
    witness=planted_original_bb_overlap(power)
    flags=witness["flags"]
    ids=witness["ids"]
    six=tuple(flags[i] for i in ids)
    V=witness["V"]
    a=_minimal_alphabet(V)
    counts_point=Counter(p for p,_ in six)
    counts_line=Counter(r for _,r in six)
    repeated_point=next(p for p,n in counts_point.items() if n==2)
    repeated_line=next(r for r,n in counts_line.items() if n==2)
    singles_point=tuple(j for j,(p,_) in enumerate(six) if p!=repeated_point)
    singles_line=tuple(j for j,(_,r) in enumerate(six) if r!=repeated_line)
    if not (len(singles_point)==len(singles_line)==4 and
            len(set(ids))==6 and repeated_point!=None and repeated_line!=None):
        raise AssertionError("not a genuine B/B-overlap original source sixset")
    if len({j for j,(p,ell) in enumerate(six)
            if p==repeated_point and ell==repeated_line})!=1:
        raise AssertionError("source repeated factors do not overlap in one flag")
    output=[]
    for edges_left in c4_edge_sets(singles_point):
        for edges_right in c4_edge_sets(singles_line):
            f_labels=_physical_c4_factor_labels(singles_point,edges_left)
            g_labels=_physical_c4_factor_labels(singles_line,edges_right)
            planted_f={repeated_point:(4,5)}
            planted_g={repeated_line:(4,5)}
            for j in singles_point:
                planted_f[six[j][0]]=f_labels[j]
            for j in singles_line:
                planted_g[six[j][1]]=g_labels[j]
            f,g=_fill_f_g(V,a,planted_f,planted_g)
            if len(set(f))!=V or len(set(g))!=V:
                raise AssertionError("not a complete separately injected pair assignment")
            edges=original_projected_column_edges(flags,ids,f,g)
            vector=signed_flow_vector(edges,independent_tree=independent_tree)
            output.append({"s":witness["s"],"six_source_ids":ids,
                           "signed_mass":sum(vector),
                           "signed_vector":vector,
                           "point_factor_count":len(counts_point),
                           "line_factor_count":len(counts_line)})
    if Counter(x["signed_mass"] for x in output)!=Counter({53526:6,53838:3}):
        raise AssertionError("sharp original BBo floor not attainable with true GQ maps")
    return tuple(output)


def true_original_d6_full_signed_lift(power, *, independent_tree=False):
    """Same-source six matching flags in actual W32/W34, all ten signs."""
    witness=planted_original_d6(power)
    six=tuple(witness["flags"][i] for i in witness["ids"])
    if len(set(p for p,_ in six))!=6 or len(set(r for _,r in six))!=6:
        raise AssertionError("genuine D6 source flags not point/line matching")
    edges=original_projected_column_edges(
        witness["flags"],witness["ids"],witness["f"],witness["g"])
    values=signed_flow_vector(edges,independent_tree=independent_tree)
    if sum(values)!=SHARP_D6_COEFFICIENT:
        raise AssertionError("true ORIGINAL D6 does not attain sharp signed coefficient")
    return {"s":witness["s"],"six_source_ids":witness["ids"],
            "signed_vector":values,"signed_mass":sum(values)}


def stronger_root_r3_floor(D6,BBo, *, geom_delta=None):
    """Exact lower risk for two DISJOINT ORIGINAL sixset classes.

    The optional geometric result is a separately accepted premise:
    D6+BBo>=delta*s^6 is NOT proved by this function.
    """
    if (type(D6) is not int or type(BBo) is not int or D6<0 or BBo<0):
        raise ValueError("nonnegative integer ORIGINAL sixset multiplicities required")
    numerator=SHARP_D6_COEFFICIENT*D6+SHARP_BBO_COEFFICIENT*BBo
    older=HISTORICAL_D6_COEFFICIENT*D6+HISTORICAL_BBO_COEFFICIENT*BBo
    if numerator<older:
        raise AssertionError("sharpened fixed-map R3 floor got worse")
    return {"exact_risk_floor":Fraction(numerator,PALETTE_DENOMINATOR),
            "numerator":numerator,
            "old_numerator":older,
            "uniform_min_coefficient":min(SHARP_D6_COEFFICIENT,SHARP_BBO_COEFFICIENT),
            "root_asymptotic_coefficient_conditional":SHARP_BBO_COEFFICIENT}
