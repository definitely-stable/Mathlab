"""HYP-105 #230 / D6-AA4-Q — exact two-sided ORIGINAL GF5 seven join.

NEW all-h factor-index identity, plus true ORIGINAL W32 exact joint
A/B/C source-column sixset join. Build left and right physical
2-regular sixset sets INDEPENDENTLY from their own complete global
source-factor images. Intersect on the exact SIX original incidence IDs.
Reclassify original full seven positive GF5 classes, including A/A
connected matching-column dual (true D6) and B/B overlap source flags.

All-h structural impossibility: a true generalized quadrangle has NO
C/C pair of degree-two projection source multiplicities, because
three ORIGINAL points and three ORIGINAL lines each repeated twice
would form a forbidden original incidence 6-cycle (GQ girth 8).

The per-side W32 source A/B/C candidate marginals 51030/10935/405
are CONSTANT for EVERY complete K6 globally injected image labeling,
while their two-sided intersection and original seven GF5 S change.
So unilateral independent half marginal *sizes* alone do not certify
positive joint couplings or the universal all-h root S>=c s^6.
"""
from collections import Counter
from itertools import combinations,product
from math import comb,factorial
from fractions import Fraction
import random

from hyp105_g5e2b3e1b0_seven_signature import R3_CERTIFIED_FLOORS
from hyp105_issue230_projection import fixture

KINDS=("A","B","C")
TAG_NAMES=tuple(R3_CERTIFIED_FLOORS)
EDGE_K6=tuple(combinations(range(6),2))


def _perfect_matching(xs):
    xs=tuple(xs)
    if len(xs)==0:
        yield ()
    else:
        first=xs[0]
        for j in range(1,len(xs)):
            for remainder in _perfect_matching(xs[1:j]+xs[j+1:]):
                yield ((first,xs[j]),)+remainder


def _physical_C4(four):
    four=tuple(sorted(four))
    if len(four)!=4 or len(set(four))!=4:
        raise ValueError("four different physical coordinate symbols required")
    all_edges=set(combinations(four,2))
    a,b,c,d=four
    for paired in (((a,b),(c,d)),((a,c),(b,d)),((a,d),(b,c))):
        yield tuple(sorted(all_edges-set(paired)))


def _K6_2factors():
    # Independent physical-edge-major construction: all K6 six-edge
    # subsets, not historical selected_left_six(source) enumerator.
    result=[]
    for six in combinations(EDGE_K6,6):
        degree=Counter(c for e in six for c in e)
        if len(degree)==6 and all(degree[x]==2 for x in range(6)):
            result.append(six)
    if len(result)!=70:
        raise AssertionError("K6 six-physical-edge 2-factors must be 70")
    return tuple(result)


def strict_true_W32_model(model):
    """Require real original 45-incidence 15+15 GQ, full K6 typed injections."""
    if model.get("s")!=2 or model.get("a")!=6:
        raise ValueError("true original W(3,2) with physical K6 only")
    inc=tuple(tuple(e) for e in model["incidences"])
    if len(inc)!=45 or len(set(inc))!=45:
        raise ValueError("need 45 DISTINCT true ORIGINAL source incidences")
    out=[]
    for key in ("left_labels","right_labels"):
        labels=tuple(tuple(x) for x in model[key])
        if len(labels)!=15 or set(labels)!=set(EDGE_K6):
            raise ValueError("two separately full globally injected K6 source maps required")
        out.append(labels)
    for p,l in inc:
        if (type(p) is not int or type(l) is not int or
                not 0<=p<15 or not 0<=l<15):
            raise ValueError("original W32 endpoint factor ID invalid")
    bypoint=[set() for _ in range(15)]
    byline=[set() for _ in range(15)]
    for p,l in inc:bypoint[p].add(l);byline[l].add(p)
    if any(len(q)!=3 for q in (*bypoint,*byline)):
        raise ValueError("not regular genuine W32 original source incidence")
    # Absence of original 6 cycles in a generalized quadrangle:
    for p in range(15):
        for q in range(p+1,15):
            if len(bypoint[p]&bypoint[q])>1:
                raise ValueError("not a source GQ partial linear space")
    return inc,tuple(out[0]),tuple(out[1])


def exact_ONE_side_original_projection_index(model,side):
    """Independent right/left source-major sixset generation, EXACT W32.

    Side index is 0=original point, 1=original line. Number of
    Q for each type A/B/C is EXACT 51030,10935,405 for every globally
    complete injection, regardless of actual original source geometry.
    """
    inc,left,right=strict_true_W32_model(model)
    if side not in (0,1) or type(side) is not int:
        raise ValueError("true ORIGINAL source type side index 0 or 1 only")
    labels=(left,right)[side]
    bysource=[[] for _ in range(15)]
    for col,edge in enumerate(inc):bysource[edge[side]].append(col)
    if any(len(row)!=3 for row in bysource):
        raise AssertionError("true original source incidence degree not three")
    inverse={edge:i for i,edge in enumerate(labels)}
    accepted={}
    counts=Counter()
    def add(indices,kind):
        ids=tuple(sorted(indices))
        if len(ids)!=6 or len(set(ids))!=6:
            raise AssertionError("source six-incidence ID multiplicities invalid")
        if ids in accepted:
            raise AssertionError("physical half enumerator repeated original incidence Q")
        accepted[ids]=kind
        counts[kind]+=1
    # Type A: 6 distinct source factors forming a 6-edge physical two-factor.
    for sixedges in _K6_2factors():
        six_ids=tuple(inverse[e] for e in sixedges)
        for selection in product(*(bysource[x] for x in six_ids)):
            add(selection,"A")
    # Type B: one twice-used ORIGINAL factor with doubled physical edge,
    # and four distinct other factors making physical C4 on other coords.
    for root_edge in EDGE_K6:
        source=inverse[root_edge]
        othercoords=tuple(x for x in range(6) if x not in root_edge)
        for cycle in _physical_C4(othercoords):
            others=tuple(inverse[e] for e in cycle)
            for same_source_twice in combinations(bysource[source],2):
                for rest in product(*(bysource[q] for q in others)):
                    add(same_source_twice+rest,"B")
    # Type C: three different original factors each used TWICE, physical
    # perfect matching (all six physical symbols, degree two each).
    for matching in _perfect_matching(tuple(range(6))):
        sources=tuple(inverse[e] for e in matching)
        for choices in product(*(tuple(combinations(bysource[p],2)) for p in sources)):
            add(tuple(j for pair in choices for j in pair),"C")
    expected={"A":51030,"B":10935,"C":405}
    if dict(counts)!=expected or len(accepted)!=62370:
        raise AssertionError("true W32 source half A/B/C index count changed")
    return {
        "side":side,"genuine_original_source_kind":"P" if side==0 else "L",
        "candidate_class_marginals":dict(counts),
        "candidate_sixset_map":accepted,
        "original_sixset_count":len(accepted),
        "total_original_45_incidence_ids":len(inc),
        "full_global_K6_bijection_confirmed":True,
    }


def _column_physical_dual(Q,inc,labels,side):
    """Independent *six original incidence positions* physical coordinate dual."""
    incidences=tuple(inc[i][side] for i in Q)
    coords={}
    for local,source in enumerate(incidences):
        for c in labels[source]:
            coords.setdefault(c,[]).append(local)
    if len(coords)!=6 or any(len(q)!=2 for q in coords.values()):
        raise AssertionError("not six physical symbols each touching two original incidence IDs")
    return tuple(sorted(tuple(v) for v in coords.values()))


def _is_single_6cycle_on_incidence_positions(dual):
    if len(dual)!=6 or len(set(dual))!=6:
        return False
    graph=[set() for _ in range(6)]
    for u,v in dual:
        if u==v:return False
        graph[u].add(v);graph[v].add(u)
    if any(len(q)!=2 for q in graph):
        return False
    seen={0}
    stack=[0]
    while stack:
        for v in graph[stack.pop()]:
            if v not in seen:
                seen.add(v);stack.append(v)
    return len(seen)==6


def independent_joint_classify(Q,lk,rk,inc,left,right):
    """Exact seven ORIGINAL accepted classes, independent of history oracle."""
    if (lk,rk)==("A","A"):
        dualL=_column_physical_dual(Q,inc,left,0)
        dualR=_column_physical_dual(Q,inc,right,1)
        if dualL==dualR and _is_single_6cycle_on_incidence_positions(dualL):
            return "D6"
        return None
    if (lk,rk)==("B","A"):return "B-left/A-right"
    if (lk,rk)==("A","B"):return "A-left/B-right"
    if {lk,rk}=={"C","A"}:return "C/A"
    if {lk,rk}=={"C","B"}:return "C/B"
    if (lk,rk)==("B","B"):
        lp=Counter(inc[j][0] for j in Q)
        rp=Counter(inc[j][1] for j in Q)
        sourceP=next((p for p,n in lp.items() if n==2),None)
        sourceL=next((l for l,n in rp.items() if n==2),None)
        if sourceP is None or sourceL is None:
            raise AssertionError("true original B/B repeated source factor missing")
        posP={i for i,j in enumerate(Q) if inc[j][0]==sourceP}
        posL={i for i,j in enumerate(Q) if inc[j][1]==sourceL}
        shared=len(posP&posL)
        if shared not in (0,1):
            raise AssertionError("simple original incidence means repeated P/L position intersection at most one")
        return "B/B-overlap" if shared else "B/B-disjoint"
    if (lk,rk)==("C","C"):
        raise AssertionError("GQ girth-eight theorem violated: original C/C induces forbidden 6-cycle")
    return None


def exact_two_sided_original_seven_join(model,*,independent_history=True,collect=False):
    """Real W32 same-map physical 2factor ORIG-incidence-index set INTERSECTION."""
    inc,left,right=strict_true_W32_model(model)
    P=exact_ONE_side_original_projection_index(model,0)
    L=exact_ONE_side_original_projection_index(model,1)
    leftsets=P["candidate_sixset_map"]
    rightsets=L["candidate_sixset_map"]
    common=leftsets.keys()&rightsets.keys()
    cross=Counter()
    seven=Counter()
    selected={} if collect else None
    numerator=0
    aa_total=aa_positive=0
    for Q in common:
        lk,rk=leftsets[Q],rightsets[Q]
        cross[lk+"/"+rk]+=1
        tag=independent_joint_classify(Q,lk,rk,inc,left,right)
        if lk==rk=="A":
            aa_total+=1
            aa_positive+=tag=="D6"
        if tag is not None:
            seven[tag]+=1
            numerator+=R3_CERTIFIED_FLOORS[tag]
            if selected is not None:selected[Q]=tag
    S=sum(seven.values())
    if aa_positive!=seven["D6"] or aa_positive>aa_total or cross["C/C"]!=0:
        raise AssertionError("7 family original AA and prohibited CC structural check failed")
    if sum(cross.values())!=len(common):
        raise AssertionError("true original full two-sided 3x3 projection intersection lost Q")
    for tag in R3_CERTIFIED_FLOORS:
        seven.setdefault(tag,0)
    if independent_history:
        from hyp105_g5e2b3e1b0_seven_signature import seven_census
        historical=seven_census(model,independent_checks=False,witness_sets=True)
        if (historical["S_seven"]!=S or
                historical["GF5_seven_lower_numerator"]!=numerator or
                historical["seven_class_motif_counts"]!=dict(seven)):
            raise AssertionError("independent TRUE full original seven-GF5 62370-sixset census disagrees")
        if set(historical["sets"])!={Q for Q in common if
              independent_joint_classify(Q,leftsets[Q],rightsets[Q],inc,left,right) is not None}:
            raise AssertionError("historical GF5 selected original sixsets differ from TWO-sided index join")
        if collect and selected!=historical["sets"]:
            raise AssertionError("selected true original GF5 Q tags disagree")
    return {
        "scope":"TRUE ORIGINAL W32 same globally injected complete f and g",
        "exact_independent_half_marginal_counts":{"P":P["candidate_class_marginals"],
                                                   "L":L["candidate_class_marginals"]},
        "candidate_P_total":len(leftsets),
        "candidate_L_total":len(rightsets),
        "exact_source_original_Q_double_projection_intersection":len(common),
        "physical_projection_source_3x3_joint_matrix":{
            f"{p}/{l}":cross[f"{p}/{l}"] for p in KINDS for l in KINDS},
        "physical_A_A_joint_candidates":aa_total,
        "physical_A_A_genuine_D6_only":aa_positive,
        "physical_A_A_nonD6_rejected":aa_total-aa_positive,
        "forbidden_original_GQ_C_C_sixsets":cross["C/C"],
        "accepted_seven_GF5_original_Q_by_tag":dict(seven),
        "accepted_seven_GF5_original_S":S,
        "selected_GF5_51palette_certified_numerator":numerator,
        "independent_historical_62370_original_Q_oracle":"PASS" if independent_history else "NOT_RUN",
        "retains_true_six_ORIGINAL_incidence_IDs":True,
        "all_h_no_C_C_original_GQ_incidence_girth_six_PROVED":True,
        "same_global_complete_f_g_both_side_join":True,
        "S_full_root_all_h_omega_s6_PROVED":False,
        "selected_ORIGINAL_Q_tags":selected,
    }


def all_h_source_girth_and_side_count_identity(s,a,occupied2factor,occupied_B,occupied_matching):
    """Symbolic all-h EXACT same-side candidate counts for true GQ incidence host.

    Source degree is d=s+1. Physical pattern counts are the numbers of
    ACTUALLY OCCUPIED source physical six-edge 2factors, doubled-edge +
    four-edge C4 patterns, and 3-edge perfect matchings. Each physical
    pattern picks distinct source factors, then each source factor has
    precisely d distinct original incidence choices. Thus the exact
    half-sixset counts are A=occ2*d^6, B=occB*C(d,2)*d^4,
    C=occMatching*C(d,2)^3. No two-half INTERSECTION lower is implied.
    """
    if type(s) is not int or s<2 or s&(s-1) or type(a) is not int or a<6:
        raise ValueError("true original s=2^h >=2 and physical a>=6")
    V=(s+1)*(s*s+1)
    if comb(a,2)<V:
        raise ValueError("physical K_a cannot inject V original source factors")
    patterns=(occupied2factor,occupied_B,occupied_matching)
    if any(type(x) is not int or x<0 for x in patterns):
        raise ValueError("nonnegative physically occupied pattern counts required")
    d=s+1
    return {
        "s":s,"V":V,"a":a,
        "A_original_sixset_candidates":occupied2factor*d**6,
        "B_original_sixset_candidates":occupied_B*comb(d,2)*d**4,
        "C_original_sixset_candidates":occupied_matching*comb(d,2)**3,
        "C_C_source_congruence_impossible_for_true_GQ":True,
        "any_all_h_joint_positive_lower_derived_from_half_marginals":False,
    }


def report(schemes=("lex","reverse","S68","S72")):
    cases={scheme:exact_two_sided_original_seven_join(fixture(1,scheme))
           for scheme in schemes}
    return {
        "slice":"HYP105-ISSUE230-D6-AA4-Q-TWO-SIDED-ORIGINAL-SEVEN-JOIN",
        "all_h_exact_half_A_B_C_candidate_count_formula":True,
        "all_h_original_GQ_C_C_forbidden_by_incidence_girth_eight":True,
        "global_full_injection_same_ORIGINAL_six_id_two_sided_intersection":True,
        "full_original_W32_one_side_A_B_C_marginals_constant_for_all_full_K6_maps":True,
        "full_original_W32_joint_seven_classes_NOT_constant":True,
        "root_A":"OPEN","root_B":"OPEN","full_GF5_R3":False,
        "cases":cases,
    }


if __name__=="__main__":
    import argparse,json
    p=argparse.ArgumentParser()
    p.add_argument("--scheme",choices=("lex","reverse","S68","S72"))
    x=p.parse_args()
    # compact report, no per-Q keys in JSON
    if x.scheme:
        r=exact_two_sided_original_seven_join(fixture(1,x.scheme))
    else:
        r=report()
    print(json.dumps(r,sort_keys=True,indent=2))
