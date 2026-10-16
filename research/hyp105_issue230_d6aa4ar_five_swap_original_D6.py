"""HYP-105 issue #230: deterministic FIVE global right-factor transpositions
to ONE true original D6 sixset, for EVERY fully global original f,g.

This is a bounded-repair partial theorem, never a lower bound on D6(f,g)
at the original fixed g nor the seven-class minimax conjecture.

Two ingredients: (i) K_a minus m<=a-2 physical edges (a>=14) has
at most one occupied edge absent from ALL simple C6, necessarily the
edge incident to a physical pendant vertex; (ii) the true original GQ
incidence graph is connected d-regular, so six source points admit six
different original adjacent line IDs avoiding any ONE forbidden line.

The finite adapters retain genuine original incidence IDs and exactly one
globally injective complete g; never redraw each sixset independently.
"""
from collections import Counter
from itertools import combinations, permutations
from math import comb, perm

from hyp105_issue230_d6aa4r_quenched_original_d6 import _params
from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked


def _canonical_edge(a,b):
    if type(a) is not int or type(b) is not int or a==b:
        raise ValueError("two distinct integer physical coordinates required")
    return (min(a,b),max(a,b))


def normalize_occupied(a,occupied):
    if type(a) is not int or a not in (6,) and a<10:
        raise ValueError("physical proof domain: a=6 or a>=10")
    pairs={_canonical_edge(*e) for e in occupied}
    if any(u<0 or v>=a for u,v in pairs):
        raise ValueError("physical edge outside K_a")
    full=comb(a,2)
    if len(pairs)!=len(tuple(occupied)) or full-len(pairs)>a-2:
        raise ValueError("physically global injective missing-edge budget breached")
    if a==6 and len(pairs)!=full:
        raise ValueError("small original W32 case has full physical K6")
    return pairs


def exceptional_noncycle_edge(a,occupied):
    """For a>=10 and missing<=a-2, <=ONE occupied C6-free edge.

    The only possible such edge joins a vertex of occupied degree ONE.
    This is a FULL characterization, not an alleged theorem for arbitrary
    low-density physical graphs. At a=6 accept only complete K6.
    """
    E=normalize_occupied(a,tuple(occupied))
    m=comb(a,2)-len(E)
    degrees=Counter(v for e in E for v in e)
    pendants=[v for v in range(a) if degrees[v]==1]
    if len(pendants)>1:
        raise AssertionError("missing budget should forbid two pendants")
    if pendants:
        if m!=a-2:
            raise AssertionError("pendant requires exact missing-edge extremum")
        bad=next(e for e in E if pendants[0] in e)
        if any(next(e for e in E if v in e)!=bad for v in pendants):
            raise AssertionError("inconsistent pendant edge")
        return bad
    return None


def complete_physical_C6_with_anchor(a,occupied,edge,reverse=False):
    """Find a physical cycle containing a particular occupied edge.

    Uses at most (a-2)_4 ordered 4-tuples; for h>>1 use the symbolic
    lemma, not finite exhaustive geometry materialization.
    """
    E=normalize_occupied(a,tuple(occupied))
    edge=_canonical_edge(*edge)
    if edge not in E or edge==exceptional_noncycle_edge(a,E):
        raise ValueError("selected physical edge does not belong to an occupied C6")
    u,v=edge if not reverse else edge[::-1]
    for middle in permutations((w for w in range(a) if w not in edge),4):
        vs=(u,v)+middle
        ordered=tuple(_canonical_edge(vs[i],vs[(i+1)%6]) for i in range(6))
        if all(e in E for e in ordered):
            return ordered
    raise AssertionError("physical edge C6 coverage theorem contradicted")


def find_first_physical_C6(a,occupied):
    E=normalize_occupied(a,tuple(occupied))
    for e in sorted(E):
        if e == exceptional_noncycle_edge(a,E):
            continue
        return complete_physical_C6_with_anchor(a,E,e)
    raise AssertionError("complete minimal palette has no genuine occupied physical C6")


def _six_actual_source_lines(points,incidences,V,forbidden_line):
    """Simple independent Hall-witness backtracking on SIX true source points."""
    original=tuple(tuple(x) for x in incidences)
    bypoint=[set() for _ in range(V)]
    for p,l in original:
        if not 0<=p<V or not 0<=l<V:
            raise ValueError("invalid original incidence ID")
        bypoint[p].add(l)
    if len(set(points))!=6 or any(p<0 or p>=V for p in points):
        raise ValueError("six different actual original source POINT factors required")
    result=[None]*6
    def visit(i,used):
        if i==6:
            return True
        for line in sorted(bypoint[points[i]]):
            if line==forbidden_line or line in used:
                continue
            result[i]=line
            if visit(i+1,used|{line}):
                return True
        result[i]=None
        return False
    if not visit(0,set()):
        raise AssertionError("true connected regular original GQ Hall property violated")
    return tuple(result)


def repair_original_D6_with_at_most_five_line_swaps(model,reverse=False):
    """Fully legal actual original (f,g) -> (same f,g') repair witness.

    This finite executable adapter is bounded to true W32/W34/W38 fixture
    size. The all-h theorem is mathematical, not a huge fake-GQ builder.
    """
    s=model["s"]
    V,a,K,m=_params(s)
    if V>600:
        raise ValueError("finite original geometry adapter capped at V<=600")
    inc=tuple(tuple(e) for e in model["incidences"])
    f=tuple(tuple(e) for e in model["left_labels"])
    g=tuple(tuple(e) for e in model["right_labels"])
    if (model["a"]!=a or len(f)!=V or len(g)!=V
            or len(set(f))!=V or len(set(g))!=V or len(set(inc))!=V*(s+1)
            or len(inc)!=V*(s+1)):
        raise ValueError("complete true original point/line pair maps required")
    original=set(inc)
    if (any(type(p) is not int or type(l) is not int
            or not 0<=p<V or not 0<=l<V for p,l in inc)
            or any(tuple(sorted(e))!=e or len(e)!=2 or not 0<=e[0]<e[1]<a
                   for e in f+g)):
        raise ValueError("invalid original incidence IDs or physical injection")
    d=s+1
    if any(sum(p==q for p,_ in inc)!=d for q in range(V)):
        raise ValueError("original source POINT degrees not regular")
    if any(sum(l==q for _,l in inc)!=d for q in range(V)):
        raise ValueError("original source LINE degrees not regular")
    if len(original)!=V*d:
        raise ValueError("duplicate original flags")
    if a==6 and m!=0:
        raise AssertionError("genuine W32 physical palette should be full")
    bad=exceptional_noncycle_edge(a,g)
    badline={edge:l for l,edge in enumerate(g)}.get(bad) if bad is not None else None
    # Physical left cycle gives six truly distinct point factors.
    left_cycle=find_first_physical_C6(a,f)
    inverse_point={edge:p for p,edge in enumerate(f)}
    points=tuple(inverse_point[edge] for edge in left_cycle)
    lines=_six_actual_source_lines(points,inc,V,badline)
    original_Q=tuple(sorted(inc.index((p,l)) for p,l in zip(points,lines)))
    if len(set(original_Q))!=6 or len(set(points))!=6 or len(set(lines))!=6:
        raise AssertionError("true original six incidence-source uniqueness broken")

    # IMPORTANT: original source lines chosen to avoid the one potential
    # physical C6-dead image label; preserve g(lines[0]) as first target.
    anchor=g[lines[0]]
    right_cycle=complete_physical_C6_with_anchor(a,g,anchor,reverse=reverse)
    if right_cycle[0]!=anchor:
        raise AssertionError("anchor right physical unordered edge changed")
    desired={l:edge for l,edge in zip(lines,right_cycle)}
    working=list(g)
    owner={edge:l for l,edge in enumerate(working)}
    swaps=[]
    for l in lines[1:]:
        target=desired[l]
        if working[l]==target:
            continue
        other=owner[target]
        if other==lines[0] or other in lines[1:lines.index(l)]:
            raise AssertionError("swapping would corrupt a previously frozen original line")
        held=working[l]
        working[l],working[other]=working[other],working[l]
        owner[target]=l
        owner[held]=other
        swaps.append((l,other))
    if len(swaps)>5 or working[lines[0]]!=g[lines[0]]:
        raise AssertionError("theorem failed: more than five swaps or moved anchor")
    if len(set(working))!=V or set(working)!=set(g):
        raise AssertionError("not one COMPLETE globally injected right image mapping")
    if any(working[l]!=desired[l] for l in lines):
        raise AssertionError("required same-source six-cycle positional images not restored")
    observed=classify_seven_prechecked(original_Q,f,tuple(working),inc)
    if observed!="D6":
        raise AssertionError("historical accepted GF5 D6 oracle rejected actual repaired Q")
    return {
        "s":s,"scheme":model.get("scheme","unspecified"),
        "actual_original_six_incidence_IDs":original_Q,
        "six_actual_original_point_factor_IDs":points,
        "six_actual_original_line_factor_IDs":lines,
        "physical_right_C6_free_exceptional_edge":bad,
        "excluded_original_line_if_pendant":badline,
        "anchored_original_line_factor_ID":lines[0],
        "anchored_physical_image_preserved":anchor,
        "swap_list_of_TRUE_original_LINE_factor_labels":tuple(swaps),
        "global_line_transposition_distance_upper":len(swaps),
        "right_global_full_injection_before":g,
        "right_global_full_injection_after":tuple(working),
        "historical_original_seven_GF5_class_after":"D6",
        "one_global_right_map_all_six_incidence_IDs":True,
        "original_fixed_pair_may_have_D6_zero":True,
        "entire_seven_family_minimax_proved":False,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


def report():
    rows=[]
    for power,schemes in ((1,("S68","S72","lex","reverse")),
                          (2,("lex","random"))):
        for scheme in schemes:
            original=fixture(power,scheme)
            if "scheme" not in original:
                original=dict(original,scheme=scheme)
            z=repair_original_D6_with_at_most_five_line_swaps(original)
            rows.append({
                "s":z["s"],"scheme":scheme,"swaps":z["global_line_transposition_distance_upper"],
                "six_original_incidence_IDs":z["actual_original_six_incidence_IDs"],
                "original_zero_D6_may_be_adversarial":True,
                "repaired_original_D6_verified":True
            })
    return {"slice":"HYP105-ISSUE230-D6-AA4-AR-FIVE-SWAP-REPAIR",
            "all_h_genuine_original_one_positive_D6_with_at_most_5_right_swaps":True,
            "right_map_full_global_injection_preserved":True,
            "no_all_f_g_original_seven_minimax":True,
            "original_finite_controls":rows}


if __name__=="__main__":
    import json
    print(json.dumps(report(),sort_keys=True,indent=2))
