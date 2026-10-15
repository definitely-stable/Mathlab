"""HYP-105 #230 / AA4-U: true ORIGINAL six-incidence FOREST cell coupling.

All-h exact source topology lemma:
If six distinct actual incidences have source endpoint multiplicities
A=(1^6), B=(2,1^4), or C=(2^3) on both sides, then the genuine
GQ incidence subgraph is a disjoint union of paths (girth>=8).
The nine feasible source forests (B/B split) completely determine
the possible joint SOURCE multiplicity cell. Original source C/C is
forbidden. This does not imply joint physical acceptance.

The deterministic Fréchet transportation relaxation within EACH actual
source forest cell is sharp for arbitrary ABSTRACT subsets, but may
fail to correspond to global point/line physical injections. We test
this gap on genuine W(3,2) using all 8,145,060 actual six-flag sets.
"""
from collections import Counter
from itertools import combinations
from math import comb

from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1b0_seven_signature import R3_CERTIFIED_FLOORS, seven_census
from hyp105_issue230_d6aa4q_two_sided_seven_join import (
    exact_ONE_side_original_projection_index,
    exact_two_sided_original_seven_join,
)
from hyp105_issue230_d6aa4r_original_joint_swap_certificate import (
    strict_true_W32_gq_model,
)

A=(1,1,1,1,1,1)
B=(2,1,1,1,1)
C=(2,2,2)
TYPE={A:"A",B:"B",C:"C"}
SOURCE_SHAPES={
    "A/A":(1,1,1,1,1,1),
    "A/B":(2,1,1,1,1),
    "B/A":(2,1,1,1,1),
    "A/C":(2,2,2),
    "C/A":(2,2,2),
    "B/C":(4,2),
    "C/B":(4,2),
    "B/B-overlap":(3,1,1,1),
    "B/B-disjoint":(2,2,1,1),
}
CELL_TO_GF5={
    "A/B":"A-left/B-right",
    "B/A":"B-left/A-right",
    "A/C":"C/A",
    "C/A":"C/A",
    "B/C":"C/B",
    "C/B":"C/B",
    "B/B-overlap":"B/B-overlap",
    "B/B-disjoint":"B/B-disjoint",
}
CELL_NAMES=tuple(SOURCE_SHAPES)


def _multiplicities(Q,inc,side):
    return Counter(inc[j][side] for j in Q)


def original_sixset_source_cell(Q,inc):
    """Key one ACTUAL source six-ID set by its FULL GQ forest profile.

    No physical coordinates required. Values based on BOTH true original
    source endpoint multiplicities, including B/B overlap by actual
    original incidence membership.
    """
    if len(Q)!=6 or len(set(Q))!=6:
        raise ValueError("six DIFFERENT original incidence IDs required")
    p=_multiplicities(Q,inc,0)
    l=_multiplicities(Q,inc,1)
    pk=TYPE.get(tuple(sorted(p.values(),reverse=True)))
    lk=TYPE.get(tuple(sorted(l.values(),reverse=True)))
    if pk is None or lk is None:
        return None
    if pk==lk=="C":
        raise AssertionError("genuine ORIGINAL GQ girth-eight forbids source C/C")
    if pk==lk=="B":
        repeated_p=next(p0 for p0,n in p.items() if n==2)
        repeated_l=next(l0 for l0,n in l.items() if n==2)
        overlaps=sum(inc[j]==(repeated_p,repeated_l) for j in Q)
        if overlaps not in (0,1):
            raise AssertionError("true source incidence simplicity violated")
        return "B/B-overlap" if overlaps else "B/B-disjoint"
    key=pk+"/"+lk
    if key not in SOURCE_SHAPES:
        raise AssertionError("unknown ORIGINAL source forest type")
    return key


def independent_true_source_component_lengths(Q,inc):
    """Separate six-edge connected-component oracle (not source-cell logic).

    Because original host is a GQ, the six source flags form no cycle.
    For a joint A/B/C source profile they also have max degree<=2.
    Component sizes are therefore original source path lengths.
    """
    Q=tuple(Q)
    pending=set(range(6))
    lengths=[]
    while pending:
        start=pending.pop()
        comp={start}
        fringe=[start]
        while fringe:
            i=fringe.pop()
            p,l=inc[Q[i]]
            joins=[j for j in tuple(pending)
                   if p==inc[Q[j]][0] or l==inc[Q[j]][1]]
            for j in joins:
                pending.remove(j)
                fringe.append(j)
                comp.add(j)
        lengths.append(len(comp))
    return tuple(sorted(lengths,reverse=True))


def all_h_original_gq_six_forest_theorem(s):
    if type(s) is not int or s<2 or s&(s-1):
        raise ValueError("true GQ W(3,2^h), h>=1")
    V=(s+1)*(s*s+1)
    N=V*(s+1)
    if N<6:
        raise ValueError("at least six actual original flags needed")
    return {
        "s":s,"original_points":V,"original_lines":V,
        "actual_original_incidence_ids":N,
        "gq_incidence_girth":8,
        "any_six_distinct_gq_incidence_ids_induce_acyclic_source_forest":True,
        "max_source_degree_two_with_types_A_B_C_implies_disjoint_paths":True,
        "source_C_C_impossible":True,
        "nine_actual_source_forest_cells":{key:list(shape)
                                           for key,shape in SOURCE_SHAPES.items()},
        "full_seven_GF5_minimum_PROVED":False,
    }


def exact_W32_source_six_forest_universe(model):
    """Exhaustive TRUE 45 choose 6 source-only, independent of f and g.

    Count ALL 8,145,060 six-original-flag sets, including those with
    endpoint multiplicity profiles outside A/B/C; do not derive the
    source universes from the selected physical 62,370 half-candidates.
    """
    inc,_,_=strict_true_W32_gq_model(model)
    n=0
    cells=Counter()
    leftsource=Counter()
    rightsource=Counter()
    for Q in combinations(range(len(inc)),6):
        n+=1
        pk=TYPE.get(tuple(sorted(Counter(inc[j][0] for j in Q).values(),
                                 reverse=True)))
        lk=TYPE.get(tuple(sorted(Counter(inc[j][1] for j in Q).values(),
                                 reverse=True)))
        if pk is not None:leftsource[pk]+=1
        if lk is not None:rightsource[lk]+=1
        if pk is None or lk is None:
            continue
        # Avoid twice reclassifying source profiles for every 8m Q.
        if pk==lk=="C":
            raise AssertionError("actual W32 cannot contain source 6-cycle")
        if pk==lk=="B":
            pcount=Counter(inc[j][0] for j in Q)
            lcount=Counter(inc[j][1] for j in Q)
            rp=next(p for p,x in pcount.items() if x==2)
            rl=next(l for l,x in lcount.items() if x==2)
            cell=("B/B-overlap" if (rp,rl) in (inc[j] for j in Q)
                  else "B/B-disjoint")
        else:
            cell=pk+"/"+lk
        cells[cell]+=1
    if n!=comb(45,6):
        raise AssertionError("missing genuine original six-incidence subsets")
    expected={"A":comb(15,6)*3**6,
              "B":15*comb(14,4)*comb(3,2)*3**4,
              "C":comb(15,3)*comb(3,2)**3}
    if dict(leftsource)!=expected or dict(rightsource)!=expected:
        raise AssertionError("original unweighted SOURCE multiplicity census wrong")
    if set(cells)!=set(CELL_NAMES):
        raise AssertionError("genuine W32 must have all nine source forest cells")
    return {
        "total_original_45_choose_6":n,
        "left_source_A_B_C_universe":dict(leftsource),
        "right_source_A_B_C_universe":dict(rightsource),
        "original_source_forest_universe":{key:cells[key] for key in CELL_NAMES},
        "independent_of_physical_f_g":True,
    }


def exact_W32_forest_stratified_frechet(model,*,source_universe=None,
                                       independent_historical=True,
                                       component_crosscheck=False):
    """Genuine globally injected P/L physical half maps, exact per-forest LP.

    For each original SOURCE forest cell F:
      N_F = all actual six-Q with that source graph type (not physical)
      left_F = same Q with physical point-half 2regular projection,
      right_F = same Q with physical line-half 2regular projection.
      lower_F=max(0,left_F+right_F-N_F).
    This is SHARP over arbitrary abstract subsets for each F,
    NOT guaranteed globally realizable via pair-edge injections.
    """
    inc,f,g=strict_true_W32_gq_model(model)
    if source_universe is None:
        source_universe=exact_W32_source_six_forest_universe(model)
    universes=source_universe["original_source_forest_universe"]
    P=exact_ONE_side_original_projection_index(model,0)["candidate_sixset_map"]
    L=exact_ONE_side_original_projection_index(model,1)["candidate_sixset_map"]
    pc=Counter()
    lc=Counter()
    both=Counter()
    arbitrary_check_count=0
    for index,(Q,kind) in enumerate(P.items()):
        cell=original_sixset_source_cell(Q,inc)
        if cell is None or cell.split("/")[0]!=kind:
            raise AssertionError("point physical half SOURCE type disagree")
        pc[cell]+=1
        if component_crosscheck and (index%401==0):
            if independent_true_source_component_lengths(Q,inc)!=SOURCE_SHAPES[cell]:
                raise AssertionError("original forest paths disagree with source type")
            arbitrary_check_count+=1
    for index,(Q,kind) in enumerate(L.items()):
        cell=original_sixset_source_cell(Q,inc)
        if cell is None or cell.split("/")[0]=="IMPOSSIBLE":
            raise AssertionError("line half source type impossible")
        if cell.startswith("B/B"):
            if kind!="B":raise AssertionError("B/B source line type disagrees")
        elif cell.split("/")[1]!=kind:
            raise AssertionError("line half source type disagrees")
        lc[cell]+=1
        if Q in P:
            if original_sixset_source_cell(Q,inc)!=cell:
                raise AssertionError("same six actual original IDs not shared")
            both[cell]+=1
        if component_crosscheck and index%401==0:
            if independent_true_source_component_lengths(Q,inc)!=SOURCE_SHAPES[cell]:
                raise AssertionError("independent true GQ component oracle disagree")
            arbitrary_check_count+=1
    table={}
    sum_nonAA=0
    for cell in CELL_NAMES:
        N=universes[cell]
        x=pc[cell];y=lc[cell];z=both[cell]
        if not (0<=z<=min(x,y)<=N and x+y-z<=N):
            raise AssertionError("true ORIGINAL two-sided physical source population impossible")
        lower=max(0,x+y-N)
        if not lower<=z:
            raise AssertionError("exact cell-conditioned Frechet lower violated")
        if cell!="A/A":sum_nonAA+=z
        table[cell]={
            "true_original_source_universe":N,
            "point_physical_half_in_source_cell":x,
            "line_physical_half_in_source_cell":y,
            "actual_global_two_side_join":z,
            "sharp_abstract_subset_Frechet_lower":lower,
            "unconstrained_abstract_subset_lower_is_realisable":True,
            "physical_global_injection_realisability_NOT_ASSERTED":True,
            "forest_component_lengths":list(SOURCE_SHAPES[cell]),
        }
    original=exact_two_sided_original_seven_join(model,independent_history=False)
    D6=original["physical_A_A_genuine_D6_only"]
    S=original["accepted_seven_GF5_original_S"]
    if S!=sum_nonAA+D6:
        raise AssertionError("full sevenGF5 ORIGINAL joint source forest decomposition failed")
    if sum(both.values())!=original["exact_source_original_Q_double_projection_intersection"]:
        raise AssertionError("source forest cells do not partition exact six-ID joint")
    if sum(pc.values())!=62370 or sum(lc.values())!=62370:
        raise AssertionError("physical source side population leaked")
    if independent_historical:
        ref=seven_census(model,independent_checks=False,witness_sets=True)
        if S!=ref["S_seven"]:
            raise AssertionError("historical original full GF5 S mismatch")
        weighted=ref["GF5_seven_lower_numerator"]
        classes=Counter()
        for key,cell in table.items():
            if key=="A/A":continue
            classes[CELL_TO_GF5[key]]+=cell["actual_global_two_side_join"]
        classes["D6"]=D6
        if dict(classes)!=ref["seven_class_motif_counts"]:
            raise AssertionError("historic all-seven original source classes mismatch")
        estimated=sum(R3_CERTIFIED_FLOORS[tag]*count
                      for tag,count in classes.items())
        if estimated!=weighted:
            raise AssertionError("historic selected 51-palette numerator mismatch")
    else:
        weighted=original["selected_GF5_51palette_certified_numerator"]
    strict_floor=sum(table[k]["sharp_abstract_subset_Frechet_lower"]
                     for k in CELL_NAMES if k!="A/A")
    return {
        "scope":"true ORIGINAL W32 all 45 choose 6 original IDs; one actual full f and g",
        "forest_cells":table,
        "source_population_from_all_45_choose_6":source_universe["total_original_45_choose_6"],
        "true_source_universe_used_separately_from_physical_half_indexes":True,
        "source_path_component_crosschecks":arbitrary_check_count,
        "actual_nonaligned_A_A_joint":both["A/A"]-D6,
        "actual_genuine_D6":D6,
        "actual_accepted_non_A_A_seven":sum_nonAA,
        "actual_full_seven_GF5_S":S,
        "selected_GF5_51palette_certified_numerator":weighted,
        "forest_stratified_abstract_nonaligned_seven_lower":strict_floor,
        "forest_conditioned_frechet_proves_all_h_S_omega_s6":False,
        "all_h_geometric_forest_partition_PROVED":True,
        "true_GLOBAL_injection_realising_relaxed_empty_intersection_PROVED":False,
    }


def report(schemes=("S68","S72","lex","reverse")):
    source=exact_W32_source_six_forest_universe(fixture(1,"lex"))
    cases={}
    for scheme in schemes:
        cases[scheme]=exact_W32_forest_stratified_frechet(
            fixture(1,scheme),source_universe=source)
    return {
        "slice":"HYP105-ISSUE230-D6-AA4-U-FOREST-TRANSPORTATION",
        "all_h_proof":all_h_original_gq_six_forest_theorem(2),
        "source_universe":source,
        "cases":cases,
        "branch_A":"OPEN","branch_B":"OPEN","full_R3_or_ASET":False,
    }


if __name__=="__main__":
    import argparse,json
    cli=argparse.ArgumentParser()
    cli.add_argument("--scheme",choices=("S68","S72","lex","reverse"),
                     default="S68")
    cli.add_argument("--all-source",action="store_true")
    args=cli.parse_args()
    model=fixture(1,args.scheme)
    if args.all_source:
        out=report()
    else:
        out=exact_W32_forest_stratified_frechet(model,component_crosscheck=True)
    print(json.dumps(out,sort_keys=True,indent=2))
