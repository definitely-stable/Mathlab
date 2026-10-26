"""HYP-105 #230 AA4-LCR: exact LOCAL coordinate return structure of C6 defects.

For every genuine W(3,2^h) and arbitrary complete globally injected
and correlated typed pair maps, any simple six-cycle of physical H is
either coordinate-rainbow/D6, or has a 2-step and/or 3-step coordinate
return. The exact canonical classification is:
  D6 + backtrack-defect + pure-triangle-return-defect = simple_C6(H).

A repeated two-step x-coordinate iff two neighboring physical edges
have the SAME original point-factor ID; similarly y/line factors.
A repeated three-step coordinate gives a triangle of three distinct
source factor labels in that physical half.
No same-position return may occur in BOTH axes in a simple physical C6.

No defective physical C6 can itself be accepted as any of the seven
historical GF5 original six-coordinate classes (it occupies <=5
coordinate symbols on at least one side). This says nothing about
compensation by OTHER original six-incidence sets on the same labels.

Executable exact finite symplectic oracle restricted to h=1/2.
"""
from collections import Counter

from hyp105_b1_symplectic import symplectic_gq
from hyp105_physical_degree_energy import minimal_alphabet
from hyp105_physical_rainbow_c6 import (
    build_original_physical_graph, exact_rainbow_c6_finite,
)


def canonical_return_signature(corners):
    """Return actual number of 2- and opposite-3-step returns on both axes.

    Counts all 6 unordered index-pairs of circular distance two and all
    3 opposite index-pairs of circular distance three. NOT probabilities.
    Caller must present a SIMPLE length-6 physical cycle with 2-coordinate
    corners; edges are validated separately by the source oracle.
    """
    if len(corners) != 6 or len(set(corners)) != 6:
        raise ValueError("six distinct actual physical corners required")
    for i in range(6):
        if (corners[i][0] == corners[(i+1)%6][0] or
                corners[i][1] == corners[(i+1)%6][1]):
            raise ValueError("both coordinate components must change per edge")
    x = [p[0] for p in corners]
    y = [p[1] for p in corners]
    bx = tuple(i for i in range(6) if x[i] == x[(i+2)%6])
    by = tuple(i for i in range(6) if y[i] == y[(i+2)%6])
    tx = tuple(i for i in range(3) if x[i] == x[i+3])
    ty = tuple(i for i in range(3) if y[i] == y[i+3])
    if any(i in by for i in bx) or any(i in ty for i in tx):
        raise AssertionError("both-axis return at same index repeats a physical corner")
    return len(bx),len(tx),len(by),len(ty)


def original_coordinate_return_census(power, f, g, *,
                                      check_independent=True):
    """Independent walk-by-walk local-return and ORIGINAL flag collision ledger.

    Recovers each real source flag ID, point ID and line ID, with a
    separate C6 enumeration implementation from the AA4-RC6 oracle.
    """
    if type(power) is not int or power not in (1,2):
        raise ValueError("finite symplectic census supports h=1,2")
    s=1<<power
    _, points, lines, flags = symplectic_gq(power)
    V=(s+1)*(s*s+1)
    if len(points)!=V or len(lines)!=V:
        raise AssertionError("original true symplectic GQ mismatch")
    adj, source_by_arc=build_original_physical_graph(s,f,g,flags)
    a=minimal_alphabet(V)
    frequency=Counter()
    totals=Counter()
    seen_sets=set()
    corner_path=[]
    occupied=set()

    def emit():
        corners=tuple(corner_path)
        bx,tx,by,ty=canonical_return_signature(corners)
        source_ids=tuple(source_by_arc[
            corners[i],corners[(i+1)%6]] for i in range(6))
        pts=tuple(flags[k][0] for k in source_ids)
        lns=tuple(flags[k][1] for k in source_ids)
        # The inverse source label of any physical x/y edge is
        # well defined, hence a backtrack is EXACTLY a consecutive
        # original point/line factor repetition.
        for i in range(6):
            if (pts[i]==pts[(i+1)%6]) != (corners[i][0]==corners[(i+2)%6][0]):
                raise AssertionError("source-point physical two-return equivalence failed")
            if (lns[i]==lns[(i+1)%6]) != (corners[i][1]==corners[(i+2)%6][1]):
                raise AssertionError("source-line physical two-return equivalence failed")
        for i in range(3):
            if corners[i][0]==corners[i+3][0]:
                if len({pts[i],pts[(i+1)%6],pts[(i+2)%6]})!=3:
                    raise AssertionError("three-step return must be physical point-factor triangle")
            if corners[i][1]==corners[i+3][1]:
                if len({lns[i],lns[(i+1)%6],lns[(i+2)%6]})!=3:
                    raise AssertionError("three-step return must be physical line-factor triangle")
        totals["simple_C6"]+=1
        frequency[bx,tx,by,ty]+=1
        totals["two_step_return_witnesses"] += bx+by
        totals["three_step_return_witnesses"] += tx+ty
        if bx+by>6 or tx+ty>3:
            raise AssertionError("both axes cannot return at the same index")
        defect=bool(bx or tx or by or ty)
        if not defect:
            totals["D6_rainbow"]+=1
            if len(set(source_ids))!=6 or len(set(pts))!=6 or len(set(lns))!=6:
                raise AssertionError("rainbow C6 needs six different original factor IDs")
            unordered=tuple(sorted(source_ids))
            if unordered in seen_sets:
                raise AssertionError("D6 original sixset repeated")
            seen_sets.add(unordered)
            return
        totals["defect_C6"]+=1
        if bx or by:
            totals["two_step_return_defect"]+=1
        else:
            totals["pure_three_step_return_defect"]+=1
        totals["x_two_step_defect"]+=bool(bx)
        totals["y_two_step_defect"]+=bool(by)
        totals["x_three_step_defect"]+=bool(tx)
        totals["y_three_step_defect"]+=bool(ty)
        distinct_source=len(set(source_ids))==6
        totals["six_distinct_source_flags_defect"]+=distinct_source
        totals["repeated_source_flag_defect"]+=not distinct_source
        # No six ORIGINAL IDs accepted by the historical seven
        # GF5 classes can be salvaged from this SAME defective
        # physical cycle: each such class has exactly six occupied
        # physical coordinates on BOTH point and line sides.
        xs={p[0] for p in corners}
        ys={p[1] for p in corners}
        if len(xs)==6 and len(ys)==6:
            raise AssertionError("coordinate defect not actually defective")
        if distinct_source:
            x_support=set(z for p in pts for z in f[p])
            y_support=set(z for l in lns for z in g[l])
            if len(x_support)>5 and len(y_support)>5:
                raise AssertionError("defect with six original flags accepted as full six-coordinate motif")
            if len(x_support)>6 or len(y_support)>6:
                raise AssertionError("physical source edges contain unknown coordinates")
            # The independent accepted seven-class GF5 ORIGINAL sixset
            # classifier must reject this very same defective set.
            from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked
            if classify_seven_prechecked(
                tuple(sorted(source_ids)), f, g, flags
            ) is not None:
                raise AssertionError("coordinate-defective physical C6 classified as accepted seven-class original motif")

    def visit(start, cur):
        if len(corner_path)==6:
            if start in adj[cur] and corner_path[1]<cur:
                emit()
            return
        for nxt in adj[cur]:
            if nxt<=start or nxt in occupied:
                continue
            occupied.add(nxt)
            corner_path.append(nxt)
            visit(start,nxt)
            corner_path.pop()
            occupied.remove(nxt)

    for v in sorted(adj):
        occupied.add(v)
        corner_path.append(v)
        visit(v,v)
        corner_path.pop()
        occupied.remove(v)
    n=totals["simple_C6"]
    if (n != totals["D6_rainbow"]+totals["defect_C6"] or
            totals["defect_C6"] !=
            totals["two_step_return_defect"]+
            totals["pure_three_step_return_defect"] or
            totals["defect_C6"] !=
            totals["six_distinct_source_flags_defect"]+
            totals["repeated_source_flag_defect"] or
            n!=sum(frequency.values()) or
            totals["two_step_return_witnesses"]+
            totals["three_step_return_witnesses"] < totals["defect_C6"] or
            totals["two_step_return_witnesses"]+
            totals["three_step_return_witnesses"] > 9*totals["defect_C6"]):
        raise AssertionError("finite local return classification or nine-fold witness bound failed")
    if check_independent:
        prior=exact_rainbow_c6_finite(power,f,g,verify_GF5=True)
        if ((n,totals["D6_rainbow"],totals["defect_C6"]) !=
                (prior["physical_simple_C6"],
                 prior["D6_original_sixsets"],
                 prior["nonrainbow_coordinate_defect"])):
            raise AssertionError("independent earlier original GF5 physical C6 audit disagrees")
        if (totals["x_two_step_defect"]>prior["nonrainbow_coordinate_defect"] or
                totals["y_two_step_defect"]>prior["nonrainbow_coordinate_defect"]):
            raise AssertionError("invalid local return class population")
    return {
        "s":s,"V":V,"a":a,
        **{key:totals[key] for key in (
            "simple_C6","D6_rainbow","defect_C6",
            "two_step_return_defect","pure_three_step_return_defect",
            "two_step_return_witnesses","three_step_return_witnesses",
            "x_two_step_defect","y_two_step_defect",
            "x_three_step_defect","y_three_step_defect",
            "six_distinct_source_flags_defect",
            "repeated_source_flag_defect")},
        "return_signature_counts":{
            ",".join(map(str,k)):v for k,v in sorted(frequency.items())
        },
        "all_h_defect_upper_O_s6_proved":False,
        "same_fixed_map_GF5_compensation_proved":False,
        "root_all_seven_lower_proved":False,
    }
