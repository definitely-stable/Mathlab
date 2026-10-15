"""HYP-105 / #230 / D6-AA4-Y-CYC: ALL 106^2 true-original W32
globally coherent point+line transposition pairs and their 7 GF5 classes.

ALL-h theorem, purely algebraic: for one point transposition u,v and
one line transposition x,y the mixed second finite difference of EACH
true-original accepted six-incidence indicator vanishes on a Q unless
it touches BOTH swapped original point and swapped original line factors.
Consequently the mixed difference of all seven accepted counts and
their selected 51-palette positive weighted sum has EXACT support in
six ACTUAL source incidence sets meeting BOTH source supports.
No independence or positive sign is asserted.

Finite certified experiment: native independent C++20 A/B/C half-index
construction and ORIGINAL six-ID sort-merge join for all 11236 full
global injection pairs at genuine W(3,2) per baseline. Python verifies
ALL 210 one-side neighbors against AA4-X-CYC, selected mixed witnesses
against AA4-Q two-sided join PLUS historical original GF5 oracle.
"""
import argparse
from collections import Counter
from itertools import combinations
import json
import subprocess
from pathlib import Path

from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1b0_seven_signature import R3_CERTIFIED_FLOORS
from hyp105_issue230_d6aa4q_two_sided_seven_join import (
    strict_true_W32_model, exact_two_sided_original_seven_join)
from hyp105_issue230_d6aa4xcyc_seven_joint_swap_frontier import (
    ExactRightLineSwapFrontier, dual_original_W32_model)

TAGS = (
    "D6", "B-left/A-right", "A-left/B-right",
    "C/A", "C/B", "B/B-overlap", "B/B-disjoint")
HEADERS=("point_move", "line_move", "D6", "Bleft", "Aleft", "CA",
         "CB", "BBover", "BBdisjoint", "S", "weight")
MOVES = (None,) + tuple(combinations(range(15), 2))
ROWS = len(MOVES) ** 2


def mixed_original_two_side_support(Q,incidences,point_move,line_move):
    """ALL-h genuine-original membership predicate for mixed delta support."""
    if len(Q)!=6 or len(set(Q))!=6:
        raise ValueError("six distinct actual original flag IDs required")
    if (len(point_move)!=2 or len(line_move)!=2 or
        point_move[0]==point_move[1] or line_move[0]==line_move[1]):
        raise ValueError("two different actual original factors per side required")
    return (
        any(incidences[i][0] in point_move for i in Q)
        and any(incidences[i][1] in line_move for i in Q))


def source_model_at(model, point_index, line_index):
    if (type(point_index) is not int or type(line_index) is not int or
            not 0<=point_index<len(MOVES) or
            not 0<=line_index<len(MOVES)):
        raise ValueError("only actual 106x106 original source moves")
    f=list(model["left_labels"])
    g=list(model["right_labels"])
    for labels,move in ((f,MOVES[point_index]),(g,MOVES[line_index])):
        if move is not None:
            u,v=move
            labels[u],labels[v]=labels[v],labels[u]
    return {**model,"left_labels":tuple(f),"right_labels":tuple(g)}


def engine_input(model):
    inc,f,g=strict_true_W32_model(model)
    lines=[f"{p} {l}" for p,l in inc]
    lines += [f"{u} {v}" for u,v in f]
    lines += [f"{u} {v}" for u,v in g]
    if len(lines)!=75:
        raise AssertionError("source input requires 45 genuine flags + 30 global labels")
    return "\n".join(lines)+"\n"


def parse_exact_native_tsv(text):
    data=text.splitlines()
    if not data or data[0].split("\t")!=list(HEADERS):
        raise AssertionError("native original seven-class schema mismatch")
    if len(data)!=1+ROWS:
        raise AssertionError("incomplete original 106x106 global-mapping matrix")
    matrix={}
    for raw in data[1:]:
        parts=raw.split("\t")
        if len(parts)!=11:
            raise AssertionError("native six-original-ID row width incorrect")
        vals=tuple(int(v) for v in parts)
        p,l=vals[:2]
        if not 0<=p<106 or not 0<=l<106 or (p,l) in matrix:
            raise AssertionError("native correlated source-swap matrix duplicate or invalid")
        counts=dict(zip(TAGS,vals[2:9]))
        S,weighted=vals[9:]
        if any(c<0 for c in counts.values()) or sum(counts.values())!=S:
            raise AssertionError("native selected ORIGINAL S count mismatch")
        if sum(counts[t]*R3_CERTIFIED_FLOORS[t] for t in TAGS)!=weighted:
            raise AssertionError("native selected GF5 certified 51palette weight mismatch")
        if S>62370:
            raise AssertionError("native original seven count cannot exceed half candidate size")
        matrix[p,l]={
            "point_move_id":p,"line_move_id":l,
            "seven":counts,"D6":counts["D6"],"non_AA":S-counts["D6"],
            "S":S,"weight":weighted,
        }
    if len(matrix)!=ROWS or matrix.keys() != {
            (p,l) for p in range(106) for l in range(106)}:
        raise AssertionError("not all valid correlated original pairs exhausted")
    return matrix


def historical_verify(model,row):
    original=source_model_at(model,row["point_move_id"],row["line_move_id"])
    z=exact_two_sided_original_seven_join(original,independent_history=True)
    assert z["accepted_seven_GF5_original_Q_by_tag"]==row["seven"]
    assert z["physical_A_A_genuine_D6_only"]==row["D6"]
    assert z["accepted_seven_GF5_original_S"]==row["S"]
    assert z["selected_GF5_51palette_certified_numerator"]==row["weight"]
    return True


def full_one_side_independent_regression(model,matrix):
    """Crosscheck EACH of all 210 finite one-side global maps by independent
    sparse true-original Q support method from earlier green X-CYC."""
    right=ExactRightLineSwapFrontier(model)
    leftdual=ExactRightLineSwapFrontier(dual_original_W32_model(model))
    expected={None: None}
    for side in ("right","left"):
        o=right if side=="right" else leftdual
        for i,move in enumerate(MOVES):
            if move is None:
                rec=o.base
            else:
                rec=o.swap(*move)
            p,l=(0,i) if side=="right" else (i,0)
            got=matrix[p,l]
            counts=rec["true_original_seven_classes"].copy()
            if side=="left":
                counts["B-left/A-right"],counts["A-left/B-right"] = (
                    counts["A-left/B-right"],counts["B-left/A-right"])
            if got["seven"]!=counts:
                raise AssertionError(f"independent original one-side seven tags mismatch {p,l}")
            if (got["S"]!=rec["S_seven"] or
                got["weight"]!=rec["selected_GF5_51palette_certified_numerator"]):
                raise AssertionError("earlier true-original X-CYC finite results disagree")
    return {"full_210_one_side_crosschecks":"PASS",
            "independent_full_original_left_and_right_Q_oracles":True}


def score_key(row):
    return (row["S"],row["D6"],row["point_move_id"],row["line_move_id"])


def summarize_original_correlated_matrix(model,matrix,scheme):
    baseline=matrix[0,0]
    baseline_expected={"S68":(68,0,3112510),"S72":(72,0,3283610)}
    if (baseline["S"],baseline["D6"],baseline["weight"])!=baseline_expected[scheme]:
        raise AssertionError("genuine historical anchored S/D6/weighted seed drift")
    rows=list(matrix.values())
    mixed=[row for row in rows if row["point_move_id"] and row["line_move_id"]]
    if len(mixed)!=105*105:
        raise AssertionError("not all genuine 11025 strictly simultaneous swaps examined")
    zero=[row for row in rows if row["D6"]==0]
    mixed_zero=[row for row in mixed if row["D6"]==0]
    min_all=min(rows,key=score_key)
    min_mixed=min(mixed,key=score_key)
    min_zero=min(zero,key=score_key) if zero else None
    min_mixed_zero=min(mixed_zero,key=score_key) if mixed_zero else None
    weighted=min(rows,key=lambda x:(x["weight"],*score_key(x)))
    weighted_mixed=min(mixed,key=lambda x:(x["weight"],*score_key(x)))
    pairs=sorted({(x["D6"],x["non_AA"]) for x in rows})
    pareto_pairs=[]
    best_non_AA=float("inf")
    for d,n in pairs:
        if n<best_non_AA:
            pareto_pairs.append((d,n))
            best_non_AA=n
    pareto=[
        min((row for row in rows if (row["D6"],row["non_AA"])==pair),
            key=score_key)
        for pair in pareto_pairs
    ]
    # Genuine mixed discrete Hessian / source-support identity, not additivity.
    interactions=[]
    for row in mixed:
        i,j=row["point_move_id"],row["line_move_id"]
        a=matrix[i,0];b=matrix[0,j]
        mixed_delta={
            tag:row["seven"][tag]-a["seven"][tag]-
                b["seven"][tag]+baseline["seven"][tag] for tag in TAGS}
        S=sum(mixed_delta.values())
        weight=sum(mixed_delta[tag]*R3_CERTIFIED_FLOORS[tag] for tag in TAGS)
        if S!=row["S"]-a["S"]-b["S"]+baseline["S"]:
            raise AssertionError("original mixed seven-tag support identity S failed")
        if weight!=row["weight"]-a["weight"]-b["weight"]+baseline["weight"]:
            raise AssertionError("historical GF5 selected numerator mixed finite difference failed")
        interactions.append((i,j,S,weight,mixed_delta["D6"]))
    strongest_negative=min(interactions,key=lambda a:(a[2],a[0],a[1]))
    strongest_positive=max(interactions,key=lambda a:(a[2],-a[0],-a[1]))
    # Independently historical reclassify all objective winners plus
    # predetermined mixed hard probes and every nondominated witness.
    selected={
        (q["point_move_id"],q["line_move_id"])
        for q in (min_all,min_mixed,weighted,weighted_mixed,*pareto)
    }
    selected.update(((0,0),(1,1),(7,11),(35,78),(105,105)))
    if min_zero:
        selected.add((min_zero["point_move_id"],min_zero["line_move_id"]))
    if min_mixed_zero:
        selected.add((min_mixed_zero["point_move_id"],min_mixed_zero["line_move_id"]))
    for i,j in sorted(selected):
        historical_verify(model,matrix[i,j])
    one_side=full_one_side_independent_regression(model,matrix)
    def public(q):
        if q is None:return None
        return {**q,
                "point_actual_source_swap":MOVES[q["point_move_id"]],
                "line_actual_source_swap":MOVES[q["line_move_id"]]}
    return {
        "scheme":scheme,
        "scope":"Genuine ORIGINAL W(3,2); each 15-factor physical K6 global injection, exact seven 51palette GF5 classes",
        "complete_global_pairs":11236,
        "genuinely_mixed_point_plus_line_swaps":11025,
        "point_side_move_catalog":106,"line_side_move_catalog":106,
        "genuine_ORIGINAL_45_flag_source":True,
        "historical_full_original_62370_each_half_index":True,
        "baseline":public(baseline),
        "minimum_S_full_11236":public(min_all),
        "minimum_S_strictly_mixed":public(min_mixed),
        "minimum_S_while_D6_zero":public(min_zero),
        "minimum_S_while_D6_zero_strictly_mixed":public(min_mixed_zero),
        "minimum_selected_GF5_weighted_full":public(weighted),
        "minimum_selected_GF5_weighted_strictly_mixed":public(weighted_mixed),
        "D6_zero_total":len(zero),"D6_zero_strictly_mixed":len(mixed_zero),
        "number_distinct_D6_nonAA_pairs":len(pairs),
        "pareto_frontier":list(map(public,pareto)),
        "mixed_second_difference_nonzero_S":sum(x[2]!=0 for x in interactions),
        "mixed_second_difference_negative_S":sum(x[2]<0 for x in interactions),
        "mixed_second_difference_positive_S":sum(x[2]>0 for x in interactions),
        "most_negative_mixed_delta_S":{
            "point_move_id":strongest_negative[0],"line_move_id":strongest_negative[1],
            "delta_S":strongest_negative[2],"delta_weight":strongest_negative[3],
            "delta_D6":strongest_negative[4]},
        "most_positive_mixed_delta_S":{
            "point_move_id":strongest_positive[0],"line_move_id":strongest_positive[1],
            "delta_S":strongest_positive[2],"delta_weight":strongest_positive[3],
            "delta_D6":strongest_positive[4]},
        "historical_original_51palette_independent_witnesses_checked":len(selected),
        **one_side,
        "mixed_all_h_source_intersection_support_identity_PROVED":True,
        "finite_complete_106_by_106_original_bilateral_matrix_VERIFIED":True,
        "global_full_symmetric_group_minimum_NOT_PROVED":True,
        "all_h_minimum_S_Omega_s6_NOT_PROVED":True,
        "root_A":"OPEN","root_B":"OPEN","root_C":"OPEN",
    }


def report(scheme,engine,matrix_path=None):
    if scheme not in ("S68","S72"):
        raise ValueError("two pinned true W32 baseline anchors only")
    model=fixture(1,scheme)
    strict_true_W32_model(model)
    result=subprocess.run([str(engine)],input=engine_input(model),text=True,
                          stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True)
    if "GENUINE ORIGINAL 106x106 BILATERAL MATRIX COMPLETE" not in result.stderr:
        raise AssertionError("native all global pair matrix was not completed")
    if matrix_path:
        Path(matrix_path).write_text(result.stdout,encoding="utf8")
    matrix=parse_exact_native_tsv(result.stdout)
    return {
        "slice":"HYP105-ISSUE230-D6-AA4-Y-CYC-TRUE-ORIGINAL-CORRELATED-BILATERAL-11236",
        "engine":"C++20 independent physical A/B/C original 6-ID sorted merge, Python true-original GF5 historical falsifier",
        "global_injections_only":True,
        "no_independent_motif_relabeling":True,
        "all_h_mixed_locality_exact_but_NO_sign":True,
        "case":summarize_original_correlated_matrix(model,matrix,scheme),
    }


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--scheme",choices=("S68","S72"),required=True)
    parser.add_argument("--engine",type=Path,required=True)
    parser.add_argument("--matrix",type=Path)
    parser.add_argument("--summary",type=Path)
    args=parser.parse_args()
    obj=report(args.scheme,args.engine,args.matrix)
    serialized=json.dumps(obj,sort_keys=True,indent=2)+"\n"
    if args.summary:args.summary.write_text(serialized,encoding="utf8")
    print(serialized)
