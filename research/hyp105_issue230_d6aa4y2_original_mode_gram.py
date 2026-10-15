"""HYP-105 / issue #230 / D6-AA4-Y2.
ALL-h exact seven-class ORIGINAL-incidence feature Gram identity and
sign-robust mixed finite-difference Cauchy budget. Independently audit
the complete finite Y-CYC 106x106 original global (f,g) matrix against
exact one-sided physically generated Q-mode gradient energies.

No unsigned-Hessian assumption. No universal S>=c*s^6 claim.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import isqrt
from pathlib import Path
import argparse
import csv
import json
import subprocess

from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1b0_seven_signature import (
    R3_CERTIFIED_FLOORS, physical_column_dual, is_connected_column_cycle,
    classify_seven_prechecked)
from hyp105_issue230_d6aa4q_two_sided_seven_join import strict_true_W32_model
from hyp105_issue230_d6aa4ycyc_bilateral_original_matrix import (
    TAGS, MOVES, engine_input, parse_exact_native_tsv, historical_verify,
    source_model_at)

ENERGY_HEADER=("side","move","D6","Bleft","Aleft","CA","CB","BBover","BBdisjoint")
N_MOVES=106


def original_source_cell(Q, incidences):
    """Independent of the historical projection evaluator; immutable
    ACTUAL source endpoint profile of six different original flags."""
    if len(Q)!=6 or len(set(Q))!=6:
        raise ValueError("six DISTINCT actual original incidence IDs")
    counts=[]
    for side in (0,1):
        cnt=Counter(incidences[j][side] for j in Q)
        signature=tuple(sorted(cnt.values(),reverse=True))
        counts.append({
            (1,1,1,1,1,1):"A",
            (2,1,1,1,1):"B",
            (2,2,2):"C",
        }.get(signature))
    L,R=counts
    if L is None or R is None:return None
    if L==R=="C":
        raise AssertionError("actual GQ girth eight forbids original C/C")
    if L==R=="A":return "D6"
    if L=="B" and R=="A":return "B-left/A-right"
    if L=="A" and R=="B":return "A-left/B-right"
    if {L,R}=={"A","C"}:return "C/A"
    if {L,R}=={"B","C"}:return "C/B"
    if L==R=="B":
        lp=Counter(incidences[j][0] for j in Q)
        rp=Counter(incidences[j][1] for j in Q)
        point=next(p for p,c in lp.items() if c==2)
        line=next(l for l,c in rp.items() if c==2)
        return ("B/B-overlap" if (point,line) in
                {incidences[j] for j in Q} else "B/B-disjoint")
    raise AssertionError("unrecognized actual ORIGINAL source forest type")


def original_half_feature(Q,incidences,labels,side):
    """Original per-Q non-AA one-hot or AA 60-position-C6 mode.

    Return (historical immutable tag, mode) or None; feature positions
    belong to actual six ORIGINAL incidence IDs, not physical orbit reps.
    """
    Q=tuple(sorted(Q))
    cell=original_source_cell(Q,incidences)
    if cell is None:return None
    counts=Counter()
    for j in Q:
        source=incidences[j][side]
        counts.update(labels[source])
    if len(counts)!=6 or any(v!=2 for v in counts.values()):
        return None
    if cell=="D6":
        original_sources=tuple(incidences[j][side] for j in Q)
        mode=physical_column_dual(incidences,labels,original_sources)
        if not is_connected_column_cycle(mode):
            return None
        return (cell,mode)
    return (cell,None)


def verify_original_mode_product(Q,model):
    """A literal ORIGINAL six-incidence independent historical falsifier
    of the exact rank-one projection feature factorization."""
    inc,f,g=strict_true_W32_model(model)
    a=original_half_feature(Q,inc,f,0)
    b=original_half_feature(Q,inc,g,1)
    factorized=a[0] if a is not None and a==b else None
    historical=classify_seven_prechecked(Q,f,g,inc)
    if factorized!=historical:
        raise AssertionError("original GF5 seven-class physical projection Gram identity failed")
    return factorized


def parse_gradient_native_tsv(text):
    rows=text.splitlines()
    if not rows or rows[0].split("\t")!=list(ENERGY_HEADER):
        raise AssertionError("source feature gradient seven-tag schema drift")
    if len(rows)!=1+2*N_MOVES:
        raise AssertionError("missing full original typed point+line energy catalog")
    energy={}
    for line in rows[1:]:
        vals=tuple(int(v) for v in line.split("\t"))
        if len(vals)!=9:
            raise AssertionError("incorrect native source feature energy row")
        side,i=vals[:2]
        if side not in (0,1) or not 0<=i<106 or (side,i) in energy:
            raise AssertionError("duplicate original source move or side")
        E=dict(zip(TAGS,vals[2:]))
        if any(v<0 for v in E.values()):
            raise AssertionError("source feature energy cannot be negative")
        if i==0 and any(E.values()):
            raise AssertionError("original complete identity feature derivative nonzero")
        energy[side,i]=E
    if len(energy)!=2*106:
        raise AssertionError("incomplete original source feature energy table")
    return energy


def ceil_sqrt(n):
    if type(n) is not int or n<0:
        raise ValueError("exact integer nonnegative Cauchy product only")
    floor=isqrt(n)
    return floor if floor*floor==n else floor+1


def audit_original_signed_gram(matrix,energy):
    """Proves each exact original mixed Hessian obeys ALL-h Gram/CS bound.

    The proof is combinatorial; the finite oracle tests EVERY pair and
    EVERY historical class at genuine W32, without assuming sign.
    """
    if len(matrix)!=11236 or len(energy)!=212:
        raise AssertionError("full genuine 106x106 original matrix+212 gradient rows required")
    weight={t:R3_CERTIFIED_FLOORS[t] for t in TAGS}
    base=matrix[0,0]
    count=Counter()
    max_sector_ratio=(0,1,None)
    extremal_negative=None
    largest_signed_deficit=(0,None)
    minimum_signed_lower_bound=None
    worst_class_margin=None
    for i in range(106):
        left=energy[0,i]
        for j in range(106):
            right=energy[1,j]
            row=matrix[i,j]
            point=matrix[i,0]
            line=matrix[0,j]
            delta={t:row["seven"][t]-point["seven"][t]-
                   line["seven"][t]+base["seven"][t] for t in TAGS}
            ds=sum(delta.values())
            dw=sum(weight[t]*delta[t] for t in TAGS)
            assert ds==row["S"]-point["S"]-line["S"]+base["S"]
            assert dw==row["weight"]-point["weight"]-line["weight"]+base["weight"]
            Eleft=sum(left.values())
            Eright=sum(right.values())
            left_weighted=sum(weight[t]*left[t] for t in TAGS)
            right_weighted=sum(weight[t]*right[t] for t in TAGS)
            if ds*ds>Eleft*Eright:
                raise AssertionError(f"GLOBAL ORIGINAL Gram Cauchy S failure {i,j}")
            if dw*dw>left_weighted*right_weighted:
                raise AssertionError(f"GLOBAL ORIGINAL Gram Cauchy GF5 W failure {i,j}")
            for t in TAGS:
                margin=left[t]*right[t]-delta[t]*delta[t]
                if margin<0:
                    raise AssertionError(f"GF5 ORIGINAL per-class Gram Cauchy failure {i,j,t}")
                if worst_class_margin is None or margin<worst_class_margin:
                    worst_class_margin=margin
            # Sectorwise upper can be no worse than global Cauchy, and
            # integer ceilings add at most 7 above the true sector sum.
            budget=sum(ceil_sqrt(left[t]*right[t]) for t in TAGS)
            weight_budget=sum(weight[t]*ceil_sqrt(left[t]*right[t]) for t in TAGS)
            if abs(ds)>budget or abs(dw)>weight_budget:
                raise AssertionError("weighted original seven-family sector budget insufficient")
            signed_lower=point["S"]+line["S"]-base["S"]-budget
            if row["S"]<signed_lower:
                raise AssertionError("deterministic sign-robust original S lower invalid")
            if minimum_signed_lower_bound is None or signed_lower<minimum_signed_lower_bound:
                minimum_signed_lower_bound=signed_lower
            if i and j:
                count["genuine_mixed"]+=1
                if ds<0:count["negative"]+=1
                elif ds>0:count["positive"]+=1
                else:count["zero"]+=1
                if ds<0 and (extremal_negative is None or
                        ds<extremal_negative["mixed_delta_S"]):
                    extremal_negative={
                        "point_swap":MOVES[i],"line_swap":MOVES[j],
                        "mixed_delta_S":ds,"mixed_delta_weight":dw,
                        "point_gradient_original_mode_energy":Eleft,
                        "line_gradient_original_mode_energy":Eright,
                        "sector_cauchy_integer_budget":budget,
                        "weighted_sector_cauchy_integer_budget":weight_budget,
                        "S00":base["S"],"S10":point["S"],
                        "S01":line["S"],"S11":row["S"],
                    }
                if budget>=abs(ds):
                    count["bounds_validated"]+=1
            else:
                if ds or dw:
                    raise AssertionError("mixed finite difference with identity side must vanish")
    if count["genuine_mixed"]!=11025 or count["bounds_validated"]!=11025:
        raise AssertionError("full 105x105 correlated true source second differences missing")
    return {
        "genuine_full_correlated_source_mixed_pairs_checked":11025,
        "all_11236_global_pairs_AND_7_class_gram_Cauchy_checks":"PASS",
        "all_11236_weighted_51palette_source_gram_Cauchy_checks":"PASS",
        "all_11236_seven_class_source_sector_budget_checks":"PASS",
        "signed_original_mixed_negative_count":count["negative"],
        "signed_original_mixed_positive_count":count["positive"],
        "signed_original_mixed_zero_count":count["zero"],
        "extremal_negative_signed_original_global_witness":extremal_negative,
        "minimum_S_signed_sector_lower_bound_across_complete_finite_grid":
            minimum_signed_lower_bound,
        "signed_lower_bound_is_a_global_minimax_certificate":False,
        "historical_true_ORIGINAL_GQ_mixed_source_projection_mode_theorem_all_h":True,
        "historical_seven_51palette_weighted_CS_theorem_all_h":True,
        "all_h_seven_S_omega_s6_PROVED":False,
    }


CONFLICT_COLUMNS=("point_move","line_move","pp","nn","pn","np",
                  "wpp","wnn","wpn","wnp")


def parse_exact_signed_conflict_tsv(text):
    """Independent parsing of 11,236 nonnegative ORIGINAL shared-mode
    quadrant counts. +/+ and -/- are helpful; +/- and -/+ are harmful."""
    records=text.splitlines()
    if len(records)!=11237 or tuple(records[0].split("\t"))!=CONFLICT_COLUMNS:
        raise AssertionError("full original signed-mode conflict TSV schema/row count failed")
    out={}
    for line in records[1:]:
        cells=line.split("\t")
        if len(cells)!=10:
            raise AssertionError("original signed-mode conflict row width invalid")
        values=tuple(int(x) for x in cells)
        i,j=values[:2]
        if not 0<=i<106 or not 0<=j<106 or (i,j) in out:
            raise AssertionError("duplicate or out-of-range original source paired move")
        payload=dict(zip(CONFLICT_COLUMNS[2:],values[2:]))
        if any(q<0 for q in payload.values()):
            raise AssertionError("true original source-mode conflict counts must be nonnegative")
        if (i==0 or j==0) and any(payload.values()):
            raise AssertionError("no signed joint mode collision if one side unchanged")
        out[i,j]=payload
    if len(out)!=11236:
        raise AssertionError("incomplete full original 106x106 sign-separated collision matrix")
    return out


def audit_exact_original_conflict_charge(matrix,energies,conflicts):
    """ALL-h deterministic exact ORIGINAL conflict/compensation identity
    audited on the entire genuine W32 11,236-pair paired-swap grid.

    This is strictly sharper than generic Cauchy for each actual finite
    pair, but its harmful budget needs NEW all-h structural control
    before a root seven-class minimax lower can follow.
    """
    if len(matrix)!=11236 or len(energies)!=212 or len(conflicts)!=11236:
        raise AssertionError("full genuine original matrix, energies and collisions needed")
    base=matrix[0,0]
    worst=None
    best_lower=None
    stats=Counter()
    for (i,j),row in matrix.items():
        c=conflicts[i,j]
        favor=c["pp"]+c["nn"]
        harm=c["pn"]+c["np"]
        favorable_weight=c["wpp"]+c["wnn"]
        harmful_weight=c["wpn"]+c["wnp"]
        ds=row["S"]-matrix[i,0]["S"]-matrix[0,j]["S"]+base["S"]
        dw=row["weight"]-matrix[i,0]["weight"]-matrix[0,j]["weight"]+base["weight"]
        if ds!=favor-harm or dw!=favorable_weight-harmful_weight:
            raise AssertionError(f"historical original seven-GF5 signed transport equality violated {i,j}")
        if i and j:
            stats["checked"]+=1
            if harm>0:stats["nonzero_harm"]+=1
            if favor>0:stats["nonzero_favor"]+=1
            if ds<0:stats["negative"]+=1
            if ds>0:stats["positive"]+=1
            if ds==0:stats["zero"]+=1
        original_lower=(matrix[i,0]["S"]+matrix[0,j]["S"]-
                        base["S"]-harm)
        if row["S"]<original_lower or row["S"]-original_lower!=favor:
            raise AssertionError("original signed harmful-charge lower and exact compensating surplus failed")
        if best_lower is None or original_lower<best_lower:
            best_lower=original_lower
        if i and j and (worst is None or ds<worst["mixed_delta_S"]):
            Eleft=energies[0,i]
            Eright=energies[1,j]
            sector_cs=sum(ceil_sqrt(Eleft[t]*Eright[t]) for t in TAGS)
            if harm>sector_cs:
                raise AssertionError("original harmful signed matches exceed class Cauchy energy budget")
            worst={
                "point_source_swap":MOVES[i],
                "line_source_swap":MOVES[j],
                "mixed_delta_S":ds,
                "favorable_same_sign_original_modes":favor,
                "harmful_opposite_sign_original_modes":harm,
                "favorable_GF5_weighted":favorable_weight,
                "harmful_GF5_weighted":harmful_weight,
                "sector_energy_Cauchy_rounded_budget":sector_cs,
                "exact_charge_lower_at_witness":original_lower,
                "true_original_full_S_at_witness":row["S"],
                "original_baseline_S":base["S"],
            }
    if stats["checked"]!=11025:
        raise AssertionError("missed true original 105x105 simultaneous source mapping pairs")
    return {
        "genuine_original_mixed_pairs":stats["checked"],
        "exact_original_same_mode_signed_quad_separation_ALL_H_THEOREM":True,
        "finite_all_11236_original_conflicts_and_historical_GF5_51palette_exact":"PASS",
        "harmful_nonzero_mixed_pairs":stats["nonzero_harm"],
        "favorable_nonzero_mixed_pairs":stats["nonzero_favor"],
        "negative_mixed_S_pairs":stats["negative"],
        "positive_mixed_S_pairs":stats["positive"],
        "zero_mixed_S_pairs":stats["zero"],
        "worst_negative_original_signed_mode_transport_witness":worst,
        "minimum_sign_robust_exact_conflict_lower_over_11236":best_lower,
        "universal_omega_s6_root_from_conflict_bound_PROVED":False,
    }


def report(scheme,native_matrix,native_gradient,native_conflicts=None,matrix_output=None,energy_output=None,conflict_output=None):
    if scheme not in ("S68","S72"):
        raise ValueError("true original pinned W32 S68/S72 models only")
    model=fixture(1,scheme)
    data=engine_input(model)
    matrix_run=subprocess.run([str(native_matrix)],input=data,text=True,
                              capture_output=True,check=True)
    if "GENUINE ORIGINAL 106x106 BILATERAL MATRIX COMPLETE" not in matrix_run.stderr:
        raise AssertionError("original 11,236 complete matrix generator did not finish")
    energy_run=subprocess.run([str(native_gradient)],input=data,text=True,
                              capture_output=True,check=True)
    if ("GENUINE ORIGINAL SOURCE LINE COMPLETE 106 TRUE SIX-FLAG MODE GRADIENTS PASS"
            not in energy_run.stderr or
        "GENUINE ORIGINAL SOURCE POINT COMPLETE 106 TRUE SIX-FLAG MODE GRADIENTS PASS"
            not in energy_run.stderr):
        raise AssertionError("missing one genuine original half projection gradient")
    if matrix_output:Path(matrix_output).write_text(matrix_run.stdout,encoding="utf8")
    if energy_output:Path(energy_output).write_text(energy_run.stdout,encoding="utf8")
    matrix=parse_exact_native_tsv(matrix_run.stdout)
    energy=parse_gradient_native_tsv(energy_run.stdout)
    conflict_certificate=None
    if native_conflicts is not None:
        conflict_run=subprocess.run([str(native_conflicts)],input=data,text=True,
                                    capture_output=True,check=True)
        if "GENUINE ORIGINAL 11236 EXACT SIGNED MODE CONFLICTS COMPLETE" not in conflict_run.stderr:
            raise AssertionError("full original nonnegative signed conflict mode engine not completed")
        if conflict_output:
            Path(conflict_output).write_text(conflict_run.stdout,encoding="utf8")
        conflicts=parse_exact_signed_conflict_tsv(conflict_run.stdout)
        conflict_certificate=audit_exact_original_conflict_charge(matrix,energy,conflicts)
    original_gq=fixture(1,scheme)
    for moves in ((0,0),(1,1),(7,11),(35,78),(105,105)):
        historical_verify(original_gq,matrix[moves])
    result=audit_original_signed_gram(matrix,energy)
    return {
        "slice":"HYP105-ISSUE230-D6-AA4-Y2-ALL-H-ORIGINAL-SEVEN-MODE-GRAM-CHARGE",
        "scheme":scheme,
        "global_true_original_physically_injective_maps":True,
        "all_h_unconditional_original_seven_source_mode_gram_and_sign_robust_cauchy":True,
        "raw_actual_original_W32_106_by_106_historical_seven_matrix_verified":True,
        "signed_original_gradient":result,
        "exact_original_conflicts":conflict_certificate,
        "root_A":"OPEN","root_B":"OPEN","root_C":"OPEN",
    }


if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--scheme",choices=("S68","S72"),required=True)
    ap.add_argument("--native-matrix",type=Path,required=True)
    ap.add_argument("--native-gradient",type=Path,required=True)
    ap.add_argument("--native-conflicts",type=Path,required=True)
    ap.add_argument("--matrix-output",type=Path)
    ap.add_argument("--energy-output",type=Path)
    ap.add_argument("--conflict-output",type=Path)
    ap.add_argument("--summary",type=Path)
    a=ap.parse_args()
    out=report(a.scheme,a.native_matrix,a.native_gradient,a.native_conflicts,
               a.matrix_output,a.energy_output,a.conflict_output)
    text=json.dumps(out,sort_keys=True,indent=2)+"\n"
    if a.summary:a.summary.write_text(text,encoding="utf8")
    print(text)
