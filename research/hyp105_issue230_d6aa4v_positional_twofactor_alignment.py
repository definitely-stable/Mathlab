"""HYP-105 #230 AA4-V: TRUE ORIGINAL six-ID AA positional 2-factor alignment.

ALL-h deterministic: in the same ORIGINAL six-incidence Q whose physical
point and line source-half projections are both type A, each physical
coordinate-column dual is a simple 2-factor on the same six Q positions
(C6 or C3+C3). The 70 possible positional 2-factors and their entire
overlap graph are classified exactly. Distinct connected C6 duals share
at most FOUR of the six coordinate-column adjacencies; five shared
adjacencies force identical connected H and positive D6.

For every complete globally typed-injective f,g:
    S(f,g) = N_nonAA(f,g) + D6(f,g)
    D6 >= max(0, ceil((E_CC - 4*M_CC)/2))
where M_CC counts same-Q A/A original Q with BOTH connected physical
positional C6, and E_CC their total common positional C6 edges.
This is a conditional deterministic certificate; no all-h positive
unconditional lower and no Branch-A inference are claimed.
"""
from collections import Counter
from itertools import combinations
from math import comb

from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1b0_seven_signature import R3_CERTIFIED_FLOORS, seven_census
from hyp105_issue230_d6aa4q_two_sided_seven_join import (
    _column_physical_dual, _is_single_6cycle_on_incidence_positions,
    exact_ONE_side_original_projection_index, exact_two_sided_original_seven_join,
)
from hyp105_issue230_d6aa4r_original_joint_swap_certificate import (
    strict_true_W32_gq_model,
)

EXPECTED_ROW_COUNTS={
    "C/C":{0:3,1:12,2:15,3:20,4:9,6:1},
    "C/T":{0:1,2:6,4:3},
    "T/C":{0:6,2:36,4:18},  # column-oriented TOTAL / disconnected-row correction below
    "T/T":{2:9,6:1},
}
# The asymmetric 10-vs-60 population explains why a fixed T row
# sees 6 connected H with overlap 0, 36 with 2, 18 with 4.
EXPECTED_ROW_COUNTS["T/C"]={0:6,2:36,4:18}

ALL_TYPES=("C/C","C/T","T/C","T/T")
PHYSICAL_K6_EDGES=tuple(combinations(range(6),2))


def physical_twofactor_kind(dual):
    """Return C for connected C6, T for two C3 triangles, fail closed."""
    if len(dual)!=6 or len({tuple(sorted(q)) for q in dual})!=6:
        raise AssertionError("six distinct simple 2factor edges required")
    g=[set() for _ in range(6)]
    for edge in dual:
        if len(edge)!=2:
            raise AssertionError("simple original-column dual edge required")
        u,v=edge
        if not (type(u) is int and type(v) is int and
                0<=u<6 and 0<=v<6 and u!=v):
            raise AssertionError("six valid original incidence positions required")
        g[u].add(v)
        g[v].add(u)
    if any(len(q)!=2 for q in g):
        raise AssertionError("a physical two-factor must have original-position degree two")
    reached={0}
    stack=[0]
    while stack:
        for q in g[stack.pop()]:
            if q not in reached:
                reached.add(q)
                stack.append(q)
    return "C" if len(reached)==6 else "T"


def independent_all_70_positional_twofactors():
    """Independent of physical half source enumerators and both global maps."""
    found=[]
    for edges in combinations(PHYSICAL_K6_EDGES,6):
        ds=Counter(u for uv in edges for u in uv)
        if len(ds)!=6 or set(ds.values())!={2}:
            continue
        dual=frozenset(edges)
        found.append((dual,physical_twofactor_kind(tuple(dual))))
    if len(found)!=70 or Counter(kind for _,kind in found)!={"C":60,"T":10}:
        raise AssertionError("physical K6 2factor 60 C6 + 10 C3C3 enumeration failed")
    return found


def all_h_positional_twofactor_overlap_theorem(s):
    """All-h valid finite column template: six positions in EVERY order.

    The enumeration is of 6-position graph combinatorics, independent
    of s, original GQ size, f/g images, and finite-W32 experiments.
    """
    if type(s) is not int or s<2 or s&(s-1):
        raise ValueError("only true original W(3,2^h), h>=1")
    Fs=independent_all_70_positional_twofactors()
    rowdistributions={}
    paircounts={}
    for t in ALL_TYPES:
        left,right=t.split("/")
        representatives=[(F,k) for F,k in Fs if k==left]
        rowseq=[]
        aggregated=Counter()
        for F,_ in representatives:
            counts=Counter(len(F&G) for G,k in Fs if k==right)
            rowseq.append(dict(counts))
            aggregated.update(counts)
        if any(row!=rowseq[0] for row in rowseq):
            raise AssertionError("S6 action should preserve physical factor overlap rows")
        if dict(rowseq[0])!=EXPECTED_ROW_COUNTS[t]:
            raise AssertionError("independent 70x70 overlap row distribution changed")
        rowdistributions[t]={str(k):v for k,v in sorted(rowseq[0].items())}
        paircounts[t]={str(k):v for k,v in sorted(aggregated.items())}
    if sum(sum(m.values()) for m in paircounts.values())!=70*70:
        raise AssertionError("some physical positional pair cells missing")
    # Two distinct connected cycles cannot share 5 / 6 of their edges
    # unless the entire 2-regular simple factor is equal; the shortest
    # alternating-switch difference is a 4-cycle, changing two edges.
    return {
        "s":s,
        "num_connected_C6_positional_factors":60,
        "num_disconnected_2C3_positional_factors":10,
        "full_70_by_70_ordered_positional_factor_pairs":4900,
        "row_distribution_by_first_type":rowdistributions,
        "ordered_pair_overlap_counts":paircounts,
        "distinct_connected_C6_common_original_position_adjacencies_max":4,
        "no_five_edge_connected_cycle_mismatch_ALL_H":True,
        "equal_disconnected_2C3_must_NOT_count_as_D6":True,
        "all_h_conditional_deterministic_certificate_PROVED":True,
        "uniform_positive_minimum_s6_PROVED":False,
    }


def genuine_W32_same_original_Q_positional_alignment(model, *,
                                                        check_history=True):
    """All real W32 same-six-original-ID A/A, exact TWO typed global injections.

    AA Q must be six different ORIGINAL point IDs, six different ORIGINAL
    line IDs, hence six source actual flags form a true original matching.
    A/A physical candidate never gets its H from an independently sampled
    local relabel: both global point and line maps are reused for all Q.
    """
    inc,f,g=strict_true_W32_gq_model(model)
    P=exact_ONE_side_original_projection_index(model,0)["candidate_sixset_map"]
    L=exact_ONE_side_original_projection_index(model,1)["candidate_sixset_map"]
    common=P.keys()&L.keys()
    hist=Counter()
    connected_overlap=Counter()
    e_CC=m_CC=d6=nonAA=0
    for Q in common:
        pl,rl=P[Q],L[Q]
        if (pl,rl)!=("A","A"):
            nonAA+=1
            continue
        if (len({inc[j][0] for j in Q})!=6 or
            len({inc[j][1] for j in Q})!=6):
            raise AssertionError("A/A must use six DISTINCT original factors of each type")
        hP=_column_physical_dual(Q,inc,f,0)
        hL=_column_physical_dual(Q,inc,g,1)
        a,b=physical_twofactor_kind(hP),physical_twofactor_kind(hL)
        r=len(set(hP)&set(hL))
        hist[f"{a}/{b}:r{r}"]+=1
        if a==b=="C":
            m_CC+=1
            e_CC+=r
            connected_overlap[r]+=1
            if r==6:
                if hP!=hL or not _is_single_6cycle_on_incidence_positions(hP):
                    raise AssertionError("six shared C6 edges MUST be same connected dual")
                d6+=1
            elif r>4:
                raise AssertionError("distinct original-position C6 cannot share 5 edges")
        if r==6 and a!=b:
            raise AssertionError("identical physical six-position dual must have same cycle kind")
    aa=sum(hist.values())
    if aa+nonAA!=len(common):
        raise AssertionError("all ORIGINAL two-sided joint Q must partition exact")
    # E - 4 M = 2 D6 - sum_nonD6(4-overlap)
    positional_deficit=sum((4-r)*v for r,v in connected_overlap.items() if r!=6)
    if 2*d6!=e_CC-4*m_CC+positional_deficit:
        raise AssertionError("exact all-h connected-overlap deficit identity failed")
    certificate=max(0,(e_CC-4*m_CC+1)//2)
    if certificate>d6:
        raise AssertionError("positional AA-alignment lower cannot exceed D6")
    ref=exact_two_sided_original_seven_join(
        model,independent_history=check_history,collect=check_history)
    if (ref["physical_A_A_joint_candidates"]!=aa or
        ref["physical_A_A_genuine_D6_only"]!=d6 or
        ref["accepted_seven_GF5_original_S"]!=nonAA+d6 or
        ref["exact_source_original_Q_double_projection_intersection"]!=len(common)):
        raise AssertionError("genuine seven-GF5 source six-ID oracle disagrees")
    weighted_nonAA=sum(R3_CERTIFIED_FLOORS[tag]*n for tag,n in
                       ref["accepted_seven_GF5_original_Q_by_tag"].items()
                       if tag!="D6")
    weighted_exact=weighted_nonAA+R3_CERTIFIED_FLOORS["D6"]*d6
    if weighted_exact!=ref["selected_GF5_51palette_certified_numerator"]:
        raise AssertionError("selected 51-palette weighted ORIGINAL charge changed")
    if check_history:
        z=seven_census(model,independent_checks=False,witness_sets=True)
        if z["S_seven"]!=nonAA+d6 or z["GF5_seven_lower_numerator"]!=weighted_exact:
            raise AssertionError("independent ORIGINAL historical GF5 oracle mismatch")
        selected={Q for Q,tag in z["sets"].items() if tag=="D6"}
        independently_found={
            Q for Q in common if (P[Q],L[Q])==("A","A") and
            _column_physical_dual(Q,inc,f,0)==_column_physical_dual(Q,inc,g,1) and
            physical_twofactor_kind(_column_physical_dual(Q,inc,f,0))=="C"
        }
        if independently_found!=selected:
            raise AssertionError("independent original six-Q positional D6 source sets changed")
    return {
        "scope":"Genuine ORIGINAL W32 same six immutable true source incidence IDs; ONE complete global f and g",
        "same_original_Q_two_sided_joint":len(common),
        "actual_nonaligned_A_A_plus_non_A_A_decomposition":True,
        "actual_A_A_original_sixset_count":aa,
        "actual_non_A_A_accepted_seven":nonAA,
        "actual_A_A_two_connected_C6_count":m_CC,
        "actual_A_A_two_connected_C6_common_adjacency_sum":e_CC,
        "actual_A_A_genuine_connected_D6":d6,
        "actual_A_A_rejected":aa-d6,
        "AA_physical_dual_type_and_positional_overlap_histogram":
            dict(sorted(hist.items())),
        "CC_overlap_histogram":{str(r):connected_overlap[r]
                                 for r in (0,1,2,3,4,6)},
        "exact_overlap_surplus_correction":positional_deficit,
        "exact_D6_from_E_minus_4M_plus_surplus_numerator":
            e_CC-4*m_CC+positional_deficit,
        "deterministic_all_h_D6_lower_by_CC_adjacency_threshold":certificate,
        "deterministic_all_h_S_lower_using_exact_nonAA_and_CC_threshold":
            nonAA+certificate,
        "real_full_selected_original_seven_S":nonAA+d6,
        "original_51palette_weighted_nonAA":weighted_nonAA,
        "original_51palette_weighted_selected_seven":
            ref["selected_GF5_51palette_certified_numerator"],
        "original_51palette_weighted_conditional_lower":
            weighted_nonAA+R3_CERTIFIED_FLOORS["D6"]*certificate,
        "certifies_uniform_all_h_root_omega_s6":False,
        "no_false_D6_from_equal_two_triangles":True,
        "strict_true_original_GQ_and_global_injections":True,
        "independent_full_seven_history":"PASS" if check_history else "NOT_RUN",
    }


def report(schemes=("S68","S72","lex","reverse")):
    return {
        "slice":"HYP105-ISSUE230-D6-AA4-V-ORIGINAL-POSITIONAL-2FACTOR",
        "all_h_s2_template":all_h_positional_twofactor_overlap_theorem(2),
        "cases":{s:genuine_W32_same_original_Q_positional_alignment(fixture(1,s))
                 for s in schemes},
        "root_A":"OPEN","root_B":"OPEN","ASET":False,
    }


if __name__=="__main__":
    import argparse,json
    cli=argparse.ArgumentParser()
    cli.add_argument("--scheme",choices=("S68","S72","lex","reverse"))
    args=cli.parse_args()
    obj=(genuine_W32_same_original_Q_positional_alignment(fixture(1,args.scheme))
         if args.scheme else report())
    print(json.dumps(obj,sort_keys=True,indent=2))
