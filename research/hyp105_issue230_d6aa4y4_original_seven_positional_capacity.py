"""HYP-105 #230 / D6-AA4-Y4.
All-h exact connected-C6 original AA positional physical capacity and
independent full W(3,2) seven-tag x four-sign-mode collision audit.

UNIVERSAL: for any genuine original W(3,2^h), h>=1, every global
injective physical edge pair map and two swapped genuine source
factors on each side, original source AA D6 modes occupy only
connected C6, not disconnected 2C3. Full K_a rooted connected
pattern numbers 24 C(a-2,4), adjacent-two 6 C(a-3,3),
disjoint-two 12 C(a-4,2). Via same ORIGINAL six-Q support,
H_D6 <= 2 min(U^point_conn, U^line_conn, U^cross_conn).
No all-h S_s=Omega(s^6) conclusion.

FINITE: independently compare EACH of 11,236 global pairs and all
seven historical GF5 tags to exact signed four-mode quadrants, the
Y-CYC true-original two-sided join, and the independent Y2 four-
quadrant original GF5 signed mode engine.
"""
from collections import Counter
from itertools import combinations
from math import comb
import argparse
import csv
import json
import subprocess
from pathlib import Path

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ycyc_bilateral_original_matrix import (
    TAGS, MOVES, engine_input, parse_exact_native_tsv, historical_verify)
from hyp105_issue230_d6aa4y2_original_mode_gram import (
    parse_exact_signed_conflict_tsv)
from hyp105_issue230_d6aa4y3_original_source_star_capacity import (
    original_parameters, original_two_factors_union_capacity)
from hyp105_issue230_d6aa4y3_original_cross_source_capacity import (
    original_two_plus_two_actual_GQ_harm_upper)
from hyp105_g5e2b3e1b0_seven_signature import R3_CERTIFIED_FLOORS


def choose(n,k):
    return comb(n,k) if n>=k>=0 else 0


def original_AA_connected_root_physical_capacity(s):
    s,d,V,a,K=original_parameters(s)
    return {
        "s":s,"d":d,"a":a,
        "all_physical_connected_C6_patterns_per_fixed_edge":
            24*choose(a-2,4),
        "all_physical_2_regular_A_patterns_per_fixed_edge":
            28*choose(a-2,4),
        "connected_C6_two_fixed_adjacent_physical_edges":
            6*choose(a-3,3),
        "connected_C6_two_fixed_disjoint_physical_edges":
            12*choose(a-4,2),
        "all_h_true_original_AA_connected_only_not_2C3":True,
    }


def original_AA_affected_two_source_capacity(s,relation):
    x=original_AA_connected_root_physical_capacity(s)
    if relation not in ("adjacent","disjoint"):
        raise ValueError("distinct physical source images adjacent or disjoint")
    d=x["d"]
    one=x["all_physical_connected_C6_patterns_per_fixed_edge"]*d**6
    both=x["connected_C6_two_fixed_adjacent_physical_edges" if
           relation=="adjacent" else
           "connected_C6_two_fixed_disjoint_physical_edges"]*d**6
    return {
        "s":s,"relation":relation,
        "connected_mode_source_star_upper":one,
        "connected_mode_two_source_both_upper":both,
        "connected_mode_two_source_union_upper":2*one-both,
        "complete_physical_A_two_source_union_upper":
            original_two_factors_union_capacity(s,relation)[
                "two_source_factor_original_sixsets_union_upper"]["A"],
        "all_h_connected_AA_one_side_source_pair_upper":True,
    }


def original_AA_crossed_point_line_capacity(s,source_incidences):
    """Source AA Q touching both two changed original point factors and
    two changed original line factors, with m<=3 true original source
    incidences among the marked 2x2 GQ factors. Count by opposite
    factor ell and its genuine point neighbors q, keeping the fixed
    actual original flag (q,ell). Connected physical cycles only.
    """
    if type(source_incidences) is not int or not 0<=source_incidences<=3:
        raise ValueError("genuine original GQ no K2,2 between two points and two lines")
    x=original_AA_connected_root_physical_capacity(s)
    d=x["d"]
    one_flag=x["all_physical_connected_C6_patterns_per_fixed_edge"]*d**5
    two_flag=max(
        x["connected_C6_two_fixed_adjacent_physical_edges"],
        x["connected_C6_two_fixed_disjoint_physical_edges"])*d**5
    return {
        "s":s,"m":source_incidences,
        "fixed_actual_original_AA_connected_flag_upper":one_flag,
        "fixed_other_original_source_flag_pair_upper":two_flag,
        "original_2point_2line_AA_source_cross_upper":
            source_incidences*one_flag+(4*d-source_incidences)*two_flag,
        "all_h_actual_source_girth_eight_and_positional_connected_C6":True,
    }


def original_AA_harmful_two_swap_upper(s,point_relation,line_relation,m):
    point=original_AA_affected_two_source_capacity(s,point_relation)
    line=original_AA_affected_two_source_capacity(s,line_relation)
    cross=original_AA_crossed_point_line_capacity(s,m)
    c=2*min(point["connected_mode_two_source_union_upper"],
            line["connected_mode_two_source_union_upper"],
            cross["original_2point_2line_AA_source_cross_upper"])
    prior=original_two_plus_two_actual_GQ_harm_upper(
        s,m,point_relation,line_relation)[
            "harmful_shared_original_seven_GF5_mode_upper"]
    if c>prior:
        raise AssertionError("AA restricted upper cannot exceed full seven GF5 capacity")
    return {
        "s":s,"point_relation":point_relation,"line_relation":line_relation,
        "actual_GQ_source_2x2_incidence_count":m,
        "D6_harmful_same_original_Q_connected_C6_mode_upper":c,
        "prior_all_seven_untagged_mode_bound":prior,
        "strict_improvement_over_untagged_bound":c<prior,
        "all_h_connected_positional_AA_GF5_harm_bound_PROVED":True,
        "all_h_seven_S_omega_s6_PROVED":False,
    }


# Source type is immutable for each genuine-original six-incidence Q.
# C/A and C/B pool both actual typed orientations.
TAG_POINT_SHAPES={
    "D6":("CONNECTED_A",),
    "B-left/A-right":("B",),
    "A-left/B-right":("A",),
    "C/A":("A","C"),
    "C/B":("B","C"),
    "B/B-overlap":("B",),
    "B/B-disjoint":("B",),
}
TAG_LINE_SHAPES={
    "D6":("CONNECTED_A",),
    "B-left/A-right":("A",),
    "A-left/B-right":("B",),
    "C/A":("A","C"),
    "C/B":("B","C"),
    "B/B-overlap":("B",),
    "B/B-disjoint":("B",),
}


def original_tag_affected_half_upper(s,relation,shapes):
    if relation not in ("adjacent","disjoint"):
        raise ValueError("only different injected physical source edges")
    generic=original_two_factors_union_capacity(s,relation)[
        "two_source_factor_original_sixsets_union_upper"]
    con=original_AA_affected_two_source_capacity(s,relation)[
        "connected_mode_two_source_union_upper"]
    available={"A":generic["A"],"B":generic["B"],
               "C":generic["C"],"CONNECTED_A":con}
    if len(set(shapes))!=len(shapes) or not set(shapes)<=set(available):
        raise ValueError("immutable source factor A/B/C/connected AA only")
    return sum(available[t] for t in shapes)


QUADRANTS=("pp","nn","pn","np")
HEADERS=("point_move","line_move") + tuple(
    tag_name+"_"+quad for tag_name in
    ("D6","Bleft","Aleft","CA","CB","BBover","BBdisjoint")
    for quad in QUADRANTS)


def parse_original_seven_quadrants(text):
    lines=text.splitlines()
    if len(lines)!=11237 or tuple(lines[0].split("\t"))!=HEADERS:
        raise AssertionError("true original full seven-tag four-sign schema drift")
    result={}
    for line in lines[1:]:
        vals=tuple(int(x) for x in line.split("\t"))
        if len(vals)!=30:
            raise AssertionError("real original seven-tag signed line width invalid")
        i,j=vals[:2]
        if not 0<=i<106 or not 0<=j<106 or (i,j) in result:
            raise AssertionError("duplicate or missing globally completable source change pair")
        if any(x<0 for x in vals[2:]):
            raise AssertionError("four quadrant counts cannot be negative")
        table={tag:dict(zip(QUADRANTS,vals[2+4*k:6+4*k]))
               for k,tag in enumerate(TAGS)}
        if (i==0 or j==0) and any(
                z for row in table.values() for z in row.values()):
            raise AssertionError("identity on one side must annihilate every mixed mode")
        result[i,j]=table
    if len(result)!=11236:
        raise AssertionError("incomplete genuine original 106x106 signed GF5 census")
    return result


def audit_all_original_tagged_correlations(model,seven,tagged,aggregate):
    """Compare two independently implemented C++ mode engines to an
    entirely separately generated two-sided historical original GF5
    11,236-row census, for all 7x11236 exact mixed per-tag deltas.
    """
    if len(tagged)!=11236 or len(aggregate)!=11236 or len(seven)!=11236:
        raise AssertionError("complete original 106x106 matrices mandatory")
    original_edges=(model["left_labels"],model["right_labels"])
    inc=set(tuple(x) for x in model["incidences"])
    base=seven[0,0]
    per_tag={t:Counter() for t in TAGS}
    max_witness={t:None for t in TAGS}
    total_peak=None
    strict_D6_cap=0
    all_checks=0
    for (i,j),table in tagged.items():
        old=aggregate[i,j]
        totals={q:sum(table[t][q] for t in TAGS) for q in QUADRANTS}
        if any(totals[q]!=old[q] for q in QUADRANTS):
            raise AssertionError("new tagged signed-position mode not equal to INDEPENDENT Y2 aggregate")
        actual=seven[i,j]
        point=seven[i,0]
        line=seven[0,j]
        ds=0;dw=0
        for tag in TAGS:
            q=table[tag]
            favor=q["pp"]+q["nn"]
            harm=q["pn"]+q["np"]
            delta=favor-harm
            expected=(actual["seven"][tag]-point["seven"][tag]
                      -line["seven"][tag]+base["seven"][tag])
            if delta!=expected:
                raise AssertionError(f"historical original seven-class source GF5 mixed Δ conflict {i,j,tag}")
            ds+=delta
            dw+=R3_CERTIFIED_FLOORS[tag]*delta
            stats=per_tag[tag]
            stats["all_pairs"]+=1
            if i and j:
                stats["genuine_mixed"]+=1
                stats["sum_harm"]+=harm
                stats["sum_favor"]+=favor
                if delta<0:stats["negative_mixed"]+=1
                elif delta>0:stats["positive_mixed"]+=1
                else:stats["zero_mixed"]+=1
                if max_witness[tag] is None or harm>max_witness[tag]["harmful_modes"]:
                    max_witness[tag]={"point_swap":MOVES[i],
                                      "line_swap":MOVES[j],
                                      "harmful_modes":harm,
                                      "favorable_modes":favor,
                                      "mixed_delta_tag":delta}
                if tag=="D6":
                    P=MOVES[i];L=MOVES[j]
                    p_relation=("adjacent" if set(original_edges[0][P[0]])&
                                set(original_edges[0][P[1]]) else "disjoint")
                    l_relation=("adjacent" if set(original_edges[1][L[0]])&
                                set(original_edges[1][L[1]]) else "disjoint")
                    m=sum((p,l) in inc for p in P for l in L)
                    cap=original_AA_harmful_two_swap_upper(
                        2,p_relation,l_relation,m)
                    if harm>cap["D6_harmful_same_original_Q_connected_C6_mode_upper"]:
                        raise AssertionError("actual ORIGINAL same-Q D6 60-positional-C6 charge capacity fail")
                    if cap["strict_improvement_over_untagged_bound"]:
                        strict_D6_cap+=1
                all_checks+=1
        if ds!=actual["S"]-point["S"]-line["S"]+base["S"]:
            raise AssertionError("original total S seven-tag coupling mismatch")
        if dw!=actual["weight"]-point["weight"]-line["weight"]+base["weight"]:
            raise AssertionError("weighted historical selected 51palette GF5 coupling mismatch")
    if all_checks!=7*11025:
        raise AssertionError("not all original seven classes for 105x105 paired swaps")
    # Recheck extrema against the different AA4-Q original six-Q source
    # hash join with independent historical seven-family classification.
    witnesses={(0,0),(1,1),(7,11),(35,78),(105,105)}
    for w in max_witness.values():
        if w is not None:
            witnesses.add((MOVES.index(w["point_swap"]),MOVES.index(w["line_swap"])))
    for key in sorted(witnesses):
        historical_verify(model,seven[key])
    return {
        "full_106_by_106_true_original_seven_tag_four_sign_certified":True,
        "seven_historical_GF5_class_and_weighted_exact_deltas_checked":all_checks,
        "all_11236_tagged_quadrants_equal_independent_Y2_aggregate":True,
        "all_original_51palette_risk_weighted_deltas_equal_native_historical_join":True,
        "strict_D6_connected_positional_capacity_improvements_among_11025":
            strict_D6_cap,
        "independent_original_historical_full_recounts":len(witnesses),
        "per_historical_seven_GF5_class":{
            tag:{**dict(per_tag[tag]),"maximum_harm_witness":max_witness[tag]}
            for tag in TAGS},
        "root_A":"OPEN","root_B":"OPEN","root_C":"OPEN",
    }


def report(scheme,engine_original,engine_tagged,engine_old,tagged_output=None,
           seven_output=None,summary_output=None):
    if scheme not in ("S68","S72"):
        raise ValueError("true-original pinned W32 source pair anchors only")
    model=fixture(1,scheme)
    source=engine_input(model)
    def native(program,terminal):
        p=subprocess.run([str(program)],input=source,text=True,
                         capture_output=True,check=True)
        if terminal not in p.stderr:
            raise AssertionError("native original source six-ID complete evidence missing")
        return p.stdout
    original_text=native(engine_original,
        "GENUINE ORIGINAL 106x106 BILATERAL MATRIX COMPLETE")
    tag_text=native(engine_tagged,
        "GENUINE ORIGINAL 11236 SEVEN-CLASS SIGNED POSITIONAL MODE QUADRANTS COMPLETE")
    old_text=native(engine_old,
        "GENUINE ORIGINAL 11236 EXACT SIGNED MODE CONFLICTS COMPLETE")
    if tagged_output:Path(tagged_output).write_text(tag_text,encoding="utf8")
    if seven_output:Path(seven_output).write_text(original_text,encoding="utf8")
    seven=parse_exact_native_tsv(original_text)
    tagged=parse_original_seven_quadrants(tag_text)
    old=parse_exact_signed_conflict_tsv(old_text)
    results=audit_all_original_tagged_correlations(model,seven,tagged,old)
    document={
        "slice":"HYP105-ISSUE230-D6-AA4-Y4-ORIGINAL-SEVEN-POSITIONAL-SAME-Q-CONFLICTS",
        "scheme":scheme,"original_global_injections_only":True,
        "genuine_original_six_incidence_IDs_not_physical_orbit_reps":True,
        "all_h_connected_AA_60_positional_mode_pattern_bound":True,
        "finite_original_full_11236_global_map_grid":True,
        "certificate":results,
    }
    if summary_output:
        Path(summary_output).write_text(
            json.dumps(document,indent=2,sort_keys=True)+"\n",encoding="utf8")
    return document


if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--scheme",choices=("S68","S72"),required=True)
    ap.add_argument("--original",type=Path,required=True)
    ap.add_argument("--tagged",type=Path,required=True)
    ap.add_argument("--aggregate",type=Path,required=True)
    ap.add_argument("--tagged-output",type=Path)
    ap.add_argument("--seven-output",type=Path)
    ap.add_argument("--summary",type=Path)
    x=ap.parse_args()
    print(json.dumps(report(x.scheme,x.original,x.tagged,x.aggregate,
                            x.tagged_output,x.seven_output,x.summary),
                     indent=2,sort_keys=True))
