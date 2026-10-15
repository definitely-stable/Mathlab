"""HYP-105 #230 / D6-AA4-V-CYC — COMPLETE TRUE ORIGINAL W32 D6 second moment.

The all-h exact original-source C6 gluing kernel was proved by D6-AA4-U-CYC.
THIS slice computes its ENTIRE finite 21,186^2 genuine original QxQ
kernel sum for a fixed complete source-point mapping f on W(3,2).

Key exact reduction: two genuine six-incidence candidates Q with the
SAME original LINE-source C6 graph have IDENTICAL D6(g) indicator under
any one complete globally injected source-line mapping g. Compress to
multiplicities w_f(C) of undirected ORIGINAL line-C6 graphs. Then

 D6(f,g) = sum_(original line C6) w_f(C) * 1{g dual = C}
 E_g D6^2 = sum_(C,C') w_f(C)w_f(C') P_g(C,C' both accepted).

The 13,327 relative ORIGINAL cyclic source-LINE gluing diagrams have
r=0..6 and exact rational pair probability from D6-AA4-U-CYC.
For true W32 a=6, every probability has SAME integer denominator
(15)_12. A small optimized independently inspectable C++ histogram
does the complete weighted ORIGINAL pair accumulation. No sampled pairs
replace full 448,846,596 original pairs; grouped event multiplicities
account for them EXACTLY.

This gives a FINITE fixed-f true W32 conditional variance and strict
Paley-Zygmund stochastic positive-probability lower. Does NOT prove an
all-h variance or the universal for-every-f,g HYP-105 S_s=Omega(s^6).
"""
from collections import Counter,defaultdict
from fractions import Fraction
from itertools import combinations,permutations
from math import comb,perm
from pathlib import Path
from subprocess import run,PIPE
import argparse,json,random

from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1b0_seven_signature import seven_census
from hyp105_issue230_d6aa4tcyc_fixed_f_d6_pair import (
    genuine_W32_fixed_f_original_connected_left_Q)
from hyp105_issue230_d6aa4ucyc_shared_line_gluing import (
    _actual_original_Q_line_cycle,
    canonical_two_source_C6_gluing,
    exact_second_cycle_coordinate_color_coefficients,
    exact_two_D6_gluing_kernel,
    genuine_W32_anchored_FULL_shared_line_D6_kernel,
)

TRUE_ORIGINAL_Q=21186
FULL_ORIGINAL_ORDERED_PAIRS=TRUE_ORIGINAL_Q**2
PHYSICAL_K6_DENOMINATOR=perm(15,12)
RELATIVE_GLUE_DIAGRAMS=sum(comb(6,r)*perm(6,r) for r in range(7))
CODE_SIZE=7**6


def normalize_original_LINE_C6(cycle):
    """Choose dihedral-normalized 6 ORIGINAL line IDs; no physical f/g
    renaming is performed and all lines remain source-factor IDs.
    """
    cycle=tuple(cycle)
    if len(cycle)!=6 or len(set(cycle))!=6:
        raise ValueError("need six different ORIGINAL source LINE factors")
    start=cycle.index(min(cycle))
    forward=tuple(cycle[(start+i)%6] for i in range(6))
    reverse=tuple(cycle[(start-i)%6] for i in range(6))
    return min(forward,reverse)


def actual_original_line_C6_multiplicities(scheme):
    """Original real W32 single fixed f: exhaustive 21186 actual Q
    => exact weighted SOURCE-LINE C6 event classes (not Q subsets).
    """
    m,rows=genuine_W32_fixed_f_original_connected_left_Q(scheme)
    counts=Counter()
    anchor=next(iter(rows))
    anchor_cycle=None
    for Q in rows:
        C=normalize_original_LINE_C6(_actual_original_Q_line_cycle(m,Q))
        counts[C]+=1
        if Q==anchor:
            anchor_cycle=C
    if sum(counts.values())!=TRUE_ORIGINAL_Q or anchor_cycle not in counts:
        raise AssertionError("lost TRUE ORIGINAL six-ID source Q")
    return m,rows,counts,anchor,anchor_cycle


def _encode_partial_source_LINE_gluing(position):
    result=0
    for d in position:
        if not 0<=d<=6:
            raise ValueError("original-source partial gluing position outside 0..6")
        result=result*7+d
    return result


def exact_13327_relative_original_LINE_gluing_weight_table():
    """ALL 13327 diagrams as 7^6 sparse array, exact probability
    numerators over common denominator (15)_12, with unused entries -1.

    A given six-position partial matching maps r chosen second original
    LINE factors injectively onto r positions 0..5 of first source C6.
    All other second factors are NEW actual source line IDs 6,7,...
    Only the relative source C6 gluing, not the actual GQ label names,
    determines exact conditional two-D6 probability for fixed f.
    """
    lookup=[-1]*CODE_SIZE
    by_r=Counter()
    iso=Counter()
    for r in range(7):
        for shared_positions in combinations(range(6),r):
            for shared_labels in permutations(range(6),r):
                digits=[6]*6
                for i,l in zip(shared_positions,shared_labels):
                    digits[i]=l
                key=_encode_partial_source_LINE_gluing(digits)
                if lookup[key]!=-1:
                    raise AssertionError("relative original-source gluing diagram counted twice")
                gluing=[]
                unseen=6
                for d in digits:
                    if d==6:
                        gluing.append(unseen);unseen+=1
                    else:gluing.append(d)
                tau=canonical_two_source_C6_gluing(tuple(range(6)),tuple(gluing))
                iso[tau]+=1
                c=exact_second_cycle_coordinate_color_coefficients(tau)[0]
                factor=PHYSICAL_K6_DENOMINATOR//perm(15,12-r)
                if factor*perm(15,12-r)!=PHYSICAL_K6_DENOMINATOR:
                    raise AssertionError("exact original source pair common denominator not divisible")
                numerator=perm(6,6)*c*factor
                if not 0<=numerator<=PHYSICAL_K6_DENOMINATOR:
                    raise AssertionError("conditional two-D6 original probability out of [0,1]")
                lookup[key]=numerator
                by_r[r]+=1
    if sum(by_r.values())!=RELATIVE_GLUE_DIAGRAMS or RELATIVE_GLUE_DIAGRAMS!=13327:
        raise AssertionError("source line gluing partial bijection count not exactly 13327")
    if len(iso)!=112:
        raise AssertionError("expected 112 nonisomorphic C6 pair gluing diagrams across all r")
    if sum(x>=0 for x in lookup)!=13327:
        raise AssertionError("sparse source-line gluing lookup uninitialized")
    # Known independent exact predecessor kernels for r0, r6.
    z0=lookup[_encode_partial_source_LINE_gluing((6,)*6)]
    z6=lookup[_encode_partial_source_LINE_gluing((0,1,2,3,4,5))]
    if Fraction(z0,PHYSICAL_K6_DENOMINATOR)!=Fraction(1,8408400):
        raise AssertionError("r0 gluing weight not previous exact AA4-T-CYC joint")
    if Fraction(z6,PHYSICAL_K6_DENOMINATOR)!=Fraction(1,5005):
        raise AssertionError("identical r6 SOURCE LINE cycle gluing is not same D6 event")
    return lookup,{
        "number_valid_original_LINE_relative_partial_gluing_diagrams":sum(by_r.values()),
        "relative_partial_source_LINE_gluings_by_shared_factor_count":dict(sorted(by_r.items())),
        "nonisomorphic_original_LINE_C6_pair_gluing_types":len(iso),
        "exact_uniform_g_gluing_probability_common_denominator":PHYSICAL_K6_DENOMINATOR,
        "r0_parent_D6_joint":"1/8408400",
        "r6_same_cycle_joint":"1/5005",
    }


def _engine_payload(counts,anchor,lookup):
    ordered=sorted(counts)
    if len(ordered)>TRUE_ORIGINAL_Q:
        raise AssertionError("more source LINE cycles than real ORIGINAL six-incidence source Q")
    if anchor not in counts:
        raise AssertionError("real original source Q anchor's cycle event absent")
    anchor_idx=ordered.index(anchor)
    rows=[f"{len(ordered)} {anchor_idx}"]
    rows.extend(" ".join(map(str,(counts[c],)+c)) for c in ordered)
    rows.extend(str(v) for v in lookup)
    return "\n".join(rows)+"\n"


def direct_grouped_true_original_D6_for_one_complete_g(counts,source_line_labels):
    """Independent event-per-source-C6 direct physical right-edge dual test,
    NOT the previous pair kernel, and NOT the historic sixset census.
    """
    g=tuple(tuple(e) for e in source_line_labels)
    if len(g)!=15 or set(g)!=set(combinations(range(6),2)):
        raise ValueError("same complete globally injected true ORIGINAL g required")
    D6=0
    for cycle,multiplicity in counts.items():
        physical=defaultdict(list)
        for line in cycle:
            for color in g[line]:
                physical[color].append(line)
        if len(physical)!=6 or any(len(x)!=2 for x in physical.values()):
            continue
        edges={tuple(sorted(lines)) for lines in physical.values()}
        expected={tuple(sorted((cycle[i],cycle[(i+1)%6]))) for i in range(6)}
        if edges==expected:
            D6+=multiplicity
    return D6


def genuine_W32_full_fixed_f_conditional_second_moment(scheme,engine,*,crosscheck_history=True):
    """True ORIGINAL W32 all 448846596 ordered Q-pairs, with compressed
    source-line C6 multiplicities; zero pair sampling in final moment.
    """
    model,rows,counts,anchor,anchor_cycle=actual_original_line_C6_multiplicities(scheme)
    table,tablemeta=exact_13327_relative_original_LINE_gluing_weight_table()
    engine=Path(engine)
    if not engine.is_file():
        raise ValueError("compiled native exact-source-line-group histogram engine missing")
    payload=_engine_payload(counts,anchor_cycle,table)
    proc=run([str(engine.resolve())],input=payload,text=True,stdout=PIPE,stderr=PIPE,timeout=600)
    if proc.returncode!=0:
        raise AssertionError("original SOURCE second-moment exact native accumulator failed: "+proc.stderr[-3500:])
    raw=json.loads(proc.stdout)
    if raw["full_original_Q_count"]!=TRUE_ORIGINAL_Q:
        raise AssertionError("real original true Q count changed")
    if raw["full_original_ordered_Q_pairs"]!=FULL_ORIGINAL_ORDERED_PAIRS:
        raise AssertionError("ALL genuine 21186^2 ordered original sixsets not counted")
    if raw["exact_common_denominator"]!=PHYSICAL_K6_DENOMINATOR:
        raise AssertionError("original full second-moment common denominator changed")

    mean=Fraction(TRUE_ORIGINAL_Q,5005)
    second=Fraction(raw["full_conditional_D6_second_moment_numerator"],PHYSICAL_K6_DENOMINATOR)
    variance=second-mean*mean
    if not second>=mean>=0 or variance<0:
        raise AssertionError("legitimate true original random D6 second moment/variance contradiction")
    anchored=Fraction(raw["original_Q_anchored_joint_row_numerator"],PHYSICAL_K6_DENOMINATOR)
    historical_anchor=Fraction(19457,10810800)
    if anchored!=historical_anchor:
        raise AssertionError("FULL compressed original cycle C6 W32 row != predecessor 21186 original six-ID Q exact kernel")
    buckets={r:raw["source_line_overlap_ordered_pair_counts"][r] for r in range(7)}
    if sum(buckets.values())!=FULL_ORIGINAL_ORDERED_PAIRS:
        raise AssertionError("full source-LINE overlap sector counts missing original Q pairs")
    # A full two-event sum is automatically nonnegative; pz upper tail
    # probability is a genuine finite exact stochastic lower, NOT an
    # every-complete-right-injection statement.
    positive_probability_lower=mean**2/second
    if not 0<positive_probability_lower<=1:
        raise AssertionError("Paley-Zygmund true original D6 positivity bound invalid")

    historical_checks=[]
    if crosscheck_history:
        samples=[("S68",fixture(1,"S68")["right_labels"]),
                 ("S72",fixture(1,"S72")["right_labels"])]
        random_generator=random.Random(2300487)
        image=list(combinations(range(6),2))
        for j in range(3):
            random_generator.shuffle(image)
            samples.append((f"complete-global-g-{j}",tuple(image)))
        for name,g in samples:
            actual=direct_grouped_true_original_D6_for_one_complete_g(counts,g)
            hist=seven_census({**model,"right_labels":tuple(g)},
                              independent_checks=False)
            oracle=hist["seven_class_motif_counts"]["D6"]
            if actual!=oracle:
                raise AssertionError("historical ORIGINAL seven-GF5 D6 != direct line-cycle weighted SOURCE event")
            historical_checks.append({"case":name,"actual_global_g_D6":actual,
                                       "independent_original_GF5_historical_D6":oracle,
                                       "exact_match":True})
    return {
        "slice":"HYP105-ISSUE230-D6-AA4-V-CYC-FULL-W32-CONDITIONAL-SECOND-MOMENT",
        "scheme":scheme,
        "source_geometry":"TRUE ORIGINAL W(3,2) six-distinct-source-incidence 45-ID",
        "all_source_point_labels_globally_injective":True,
        "all_source_line_labels_globally_injective_under_random_g":True,
        "original_TRUE_left_C6_six_incidence_Q_count":TRUE_ORIGINAL_Q,
        "distinct_source_line_C6_event_groups":len(counts),
        "compressed_original_sixset_C6_total_multiplicity":sum(counts.values()),
        "complete_g_all_TRUE_original_Q_ordered_pairs":FULL_ORIGINAL_ORDERED_PAIRS,
        "pair_kernel_precomputed":tablemeta,
        "actual_original_source_LINE_gluing_full_weighted_counts":raw,
        "exact_conditional_E_g_D6":str(mean),
        "exact_conditional_E_g_D6_squared":str(second),
        "exact_conditional_Var_g_D6":str(variance),
        "exact_P_g_D6_positive_by_Cauchy_Paley_Zygmund_lower":str(positive_probability_lower),
        "predecessor_one_actual_original_Q_anchored_joint_row":str(anchored),
        "independent_historical_five_complete_global_g_GF5_D6_oracles":historical_checks,
        "complete_true_original_W32_conditional_second_moment_PROVED":True,
        "all_h_uniform_variance_bound_PROVED":False,
        "universal_every_complete_f_g_S_omega_s6_PROVED":False,
        "root_A":"OPEN","root_B":"OPEN",
    }


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--scheme",choices=("S68","S72"),required=True)
    p.add_argument("--engine",required=True)
    p.add_argument("--no-history",action="store_true")
    args=p.parse_args()
    result=genuine_W32_full_fixed_f_conditional_second_moment(
        args.scheme,args.engine,crosscheck_history=not args.no_history)
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__=="__main__":
    main()
