"""AA4-CP: exact true-original six-incidence selected all-seven join and W32 oracle.

C++ fast exact integer right-source multigraph shape enumeration A/B/C.
Python handles authentic source W(3,s) fixtures, validation and independent
HISTORICAL original W32 classifier. No per-Q physical redraw.
"""
import os
import pathlib
import subprocess
import tempfile
from functools import lru_cache

from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_projection import fixture

ROOT=pathlib.Path(__file__).resolve().parent
SRC=ROOT/"hyp105_issue230_d6aa4cp_original_full_sevenclass_right_join.cpp"
CLASS_NAMES=("D6","B-left/A-right","A-left/B-right","C/A","C/B",
             "B/B-overlap","B/B-disjoint")
WEIGHTS=(5643,45600,45600,43320,49050,51750,45010)

@lru_cache(maxsize=1)
def compile_join_engine():
    if not SRC.is_file():
        raise FileNotFoundError(SRC)
    # Only standard library C++17; available on GitHub HOSTED Linux.
    dst=pathlib.Path(tempfile.mkdtemp(prefix="aa4cp-"))/"exact_seven_join"
    p=subprocess.run(["g++","-std=c++17","-O3","-DNDEBUG","-pipe",
                      "-o",str(dst),str(SRC)],
                    capture_output=True,text=True,check=False,timeout=120)
    if p.returncode:
        raise RuntimeError("AA4-CP compile failed closed: "+p.stderr[:7000])
    return dst


def full_original_sevenclass_right_join(model, *, timeout_seconds=1200):
    s,V,a,inc,f,g,_,_=_original_source(model)
    if (s,V,a) not in ((2,15,6),(4,85,14)):
        raise ValueError("exact optimized nibble engine validated only for genuine W32/W34")
    if type(timeout_seconds) is not int or timeout_seconds<1:
        raise ValueError("positive exact join CPU budget in seconds required")
    with tempfile.TemporaryDirectory(prefix="aa4cp-gq-") as work:
        fpath=pathlib.Path(work)/"original_gq.txt"
        with fpath.open("w",encoding="ascii") as h:
            h.write(f"{s} {V} {a} {len(inc)}\n")
            for edge in f:g1=tuple(edge);h.write(f"{g1[0]} {g1[1]}\n")
            for edge in g:g1=tuple(edge);h.write(f"{g1[0]} {g1[1]}\n")
            for p,l in inc:h.write(f"{p} {l}\n")
        p=subprocess.run([str(compile_join_engine()),str(fpath)],
            capture_output=True,text=True,timeout=timeout_seconds,check=False)
    if p.returncode:
        raise RuntimeError("AA4-CP failclosed original source right join: "+p.stderr[:7000])
    out={}
    for line in p.stdout.splitlines():
        name,*value=line.split()
        if name=="SCHEMA":
            if value!=["AA4CP1"]:raise AssertionError("wrong exact join schema")
        elif len(value)==1:
            out[name]=int(value[0])
        else:raise AssertionError("unknown original sevenjoin result "+repr(line))
    if len(out)<17:
        raise AssertionError("incomplete exact original GF5 sevenjoin evidence")
    if (out["s"],out["V"],out["a"])!=(s,V,a):
        raise AssertionError("original GQ source parameters mutated")
    if out["physical_sixpalettes"]!=(1 if a==6 else 3003):
        raise AssertionError("6-coordinate right shape palette count mismatch")
    counts={c:out[c] for c in CLASS_NAMES}
    if sum(counts.values())!=out["S_unweighted"]:
        raise AssertionError("original sixflag S count does not reconcile")
    if sum(counts[c]*w for c,w in zip(CLASS_NAMES,WEIGHTS))!=out["W_weighted"]:
        raise AssertionError("original accepted seven GF5 necessary risk not exact")
    if out["all_h_lower_proved"]!=0:
        raise AssertionError("finite W32/W34 original count cannot prove all-h root A")
    return {"s":s,"V":V,"a":a,"seven_class_motif_counts":counts,
            "S_unweighted":out["S_unweighted"],
            "W_weighted":out["W_weighted"],
            "right_line_A_patterns":out["source_LINE_pattern_A"],
            "right_line_B_patterns":out["source_LINE_pattern_B"],
            "right_line_C_patterns":out["source_LINE_pattern_C"],
            "right_source_Q_candidate_completions_tested":out["source_Q_right_deg2_tested"],
            "right_to_left_degree_prunes":out["early_right_to_left_physical_degree_prunes"],
            "physical_sixpalettes":out["physical_sixpalettes"],
            "one_full_original_source_incidence_host":True,
            "one_entire_globally_injected_f_g":True,
            "root_230":"OPEN_WITH_FORMAL_BLOCKER"}


def independent_W32_sevenclass_reference(model):
    from hyp105_g5e2b3e1b0_seven_signature import seven_census
    ref=seven_census(model,independent_checks=False)
    return {"counts":ref["seven_class_motif_counts"],
            "S":ref["S_seven"],"W":ref["GF5_seven_lower_numerator"]}
