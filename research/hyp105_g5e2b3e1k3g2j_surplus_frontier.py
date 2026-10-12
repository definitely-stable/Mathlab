"""HYP-105 E1-K3-G2-J: exact rational NECESSARY all-h surplus constants.

For any true legal coherent labeling of W(3,s) the desired
    S_s >= alpha*s**6 - beta*Jcross, alpha>0, beta>=0
forces alpha <= (S_s + beta*Jcross) / s**6.
This module computes the exact LOWER ENVELOPE of those upper bounds from
finite legally reconstructed W32 labelings, using integer/Fraction math.

An observed upper envelope is NOT a universal lower bound. Every reported
coefficient candidate beyond it has a concrete finite counterexample.
"""
from fractions import Fraction
from itertools import combinations
from hashlib import sha256
import json

from hyp105_g5e2b3e1k1_kikuchi_c6 import gq_pair_model
from hyp105_g5e2b3e1b0_seven_signature import seven_census
from hyp105_g5e2b3e1k3g2d_charging_hall import cross_witnesses
from hyp105_g5e2b3e1k3g2h_exact_swap_shell import swapped_labeling

BEST_CORRELATED_ANCHOR=(
    ("left",0,14),("right",0,14),
)
BEST_CORRELATED_PATH=(
    ("left",1,4),("right",2,4),("left",2,13),
    ("right",3,13),("left",2,3),("right",1,14),
)
BEST_PATH_EXPECTED=(
    (168,29),(132,18),(117,15),
    (101,17),(90,21),(94,26),
)


def _frac_pair(value):
    q=Fraction(value)
    return [q.numerator,q.denominator]


def _from_pair(value):
    if not (isinstance(value,(tuple,list)) and len(value)==2
            and type(value[0]) is int and type(value[1]) is int
            and value[1]>0):
        raise ValueError("exact rational [integer numerator, positive denominator]")
    return Fraction(value[0],value[1])


def exact_point(model, source):
    """Count complete genuine positive seven-S and all original Jcross."""
    if model["s"]!=2 or model["a"]!=6:
        raise ValueError("full exact B0 coefficient oracle supports only W32/K6")
    census=seven_census(model,independent_checks=False,witness_sets=False)
    if census["left_6coordinate_candidates"]!=62370:
        raise AssertionError("incomplete source-sixset enumeration")
    S=census["S_seven"]
    J=len(cross_witnesses(model))
    if S<0 or J<0 or (
            census["GF5_seven_lower_numerator"]<0):
        raise AssertionError("negative true original GF5-positive multiplicity")
    return {"name":source,"S":S,"J":J,"s":model["s"],
            "GF5_numerator":census["GF5_seven_lower_numerator"]}


def finite_models(*,shell_limit=105,include_correlated=True):
    """Legal coherent W32 maps, NOT all permutations or an all-h sample."""
    if type(shell_limit) is not int or not 0<=shell_limit<=105:
        raise ValueError("shell_limit must be integer 0..105")
    if type(include_correlated) is not bool:
        raise ValueError("include_correlated must be a boolean")
    base=gq_pair_model(1,"lex")
    output=[exact_point(base,"lex"),exact_point(
        gq_pair_model(1,"reverse-line"),"reverse-line")]
    pairs=tuple(combinations(range(15),2))
    shell=[]
    for side in ("left","right"):
        for i,j in pairs[:shell_limit]:
            point=exact_point(swapped_labeling(base,side,i,j),
                              f"lex:{side}:{i}:{j}")
            shell.append(point)
    output.extend(shell)
    if shell_limit==105:
        if (len(shell)!=210 or
                min(row["S"] for row in shell)!=176 or
                max(row["J"] for row in shell)!=47 or
                min(row["S"]-row["J"] for row in shell)!=139):
            raise AssertionError("complete G2-H shell finite extrema changed")
    correlated=[]
    if include_correlated:
        model=base
        for side,i,j in BEST_CORRELATED_ANCHOR:
            model=swapped_labeling(model,side,i,j)
        correlated.append(exact_point(model,"corr:anchor"))
        for step,((side,i,j),(S,J)) in enumerate(zip(
                BEST_CORRELATED_PATH,BEST_PATH_EXPECTED),1):
            model=swapped_labeling(model,side,i,j)
            candidate=exact_point(model,f"corr:{step}")
            if (candidate["S"],candidate["J"])!=(S,J):
                raise AssertionError("reconstructed correlated source map mismatch")
            correlated.append(candidate)
        output.extend(correlated)
    if (output[0]["S"],output[0]["J"])!=(259,36) or (
            output[1]["S"],output[1]["J"])!=(169,28):
        raise AssertionError("baseline full W32 accepted-S/J counters changed")
    return output


def _canonical_lines(points):
    """One true-source witness per identical (J,S), keep deterministic IDs."""
    if not points:
        raise ValueError("nonempty finite original coherent labeling certificates")
    indexed={}
    for row in points:
        if type(row.get("S")) is not int or type(row.get("J")) is not int or (
                row["S"]<0 or row["J"]<0 or row.get("s")!=2 or
                not isinstance(row.get("name"),str) or not row["name"]):
            raise ValueError("finite point must carry valid W32 S,J and name")
        key=(row["J"],row["S"])
        if key not in indexed or row["name"]<indexed[key]["name"]:
            indexed[key]=row
    # Drop physically dominated lines with same slope and larger intercept.
    best={}
    for (J,S),row in indexed.items():
        if J not in best or (S,row["name"])<(
                best[J]["S"],best[J]["name"]):
            best[J]=row
    return list(best.values())


def lower_line_envelope(points):
    """Piecewise exact min_{finite legal maps} (S+beta*J)/64, beta>=0.

    Construct each switch via exact rational intersections.  Verify every
    piece at BOTH endpoints against every input line (affine certificate).
    On the final ray verify the slope as well.
    """
    lines=_canonical_lines(points)
    active=min(lines,key=lambda p:(p["S"],p["J"],p["name"]))
    left=Fraction(0)
    pieces=[]
    for _ in range(len(lines)+1):
        candidates=[]
        for alt in lines:
            if alt["J"]>=active["J"]:
                continue
            cross=Fraction(alt["S"]-active["S"],active["J"]-alt["J"])
            if cross>left:
                candidates.append(cross)
        right=min(candidates) if candidates else None
        for row in lines:
            for x in (left,) if right is None else (left,right):
                if (active["S"]+x*active["J"] >
                        row["S"]+x*row["J"]):
                    raise AssertionError("unverified rational support line")
            if right is None and active["J"]>row["J"]:
                raise AssertionError("terminal ray has nonminimal slope")
        pieces.append({"beta_from":_frac_pair(left),
                       "beta_to":_frac_pair(right) if right is not None else None,
                       "active_source":active["name"],
                       "S":active["S"],"J":active["J"],
                       "alpha_intercept":_frac_pair(Fraction(active["S"],64)),
                       "alpha_slope":_frac_pair(Fraction(active["J"],64))})
        if right is None:
            break
        best_value=min(p["S"]+right*p["J"] for p in lines)
        later=[p for p in lines if p["S"]+right*p["J"]==best_value]
        next_active=min(later,key=lambda p:(p["J"],p["S"],p["name"]))
        if next_active["J"]>=active["J"]:
            raise AssertionError("envelope fails strict decreasing slopes")
        active=next_active
        left=right
    else:
        raise AssertionError("nonterminating finite line envelope")
    return pieces


def independent_intersection_oracle(points,pieces):
    """Different oracle: evaluate ALL pair intersections and rational midpoints.

    The proof certificate itself is endpoint and ray-slope verification
    above. This independent falsifier catches omitted switches.
    """
    lines=_canonical_lines(points)
    cut={Fraction(0)}
    for a,b in combinations(lines,2):
        if a["J"]!=b["J"]:
            cross=Fraction(b["S"]-a["S"],a["J"]-b["J"])
            if cross>=0:
                cut.add(cross)
    cuts=sorted(cut)
    probes=set(cuts)
    probes.update((a+b)/2 for a,b in zip(cuts,cuts[1:]))
    probes.add(cuts[-1]+1)
    probes.add(cuts[-1]+100)
    for beta in sorted(probes):
        minimum=min(p["S"]+beta*p["J"] for p in lines)
        eligible=[p for p in pieces if (
            _from_pair(p["beta_from"])<=beta and (
                p["beta_to"] is None or beta<=_from_pair(p["beta_to"])))]
        if not eligible or min(
                p["S"]+beta*p["J"] for p in eligible)!=minimum:
            raise AssertionError("independent pair-intersection oracle failed")
    return len(probes)


def necessary_counterexample(points,alpha,beta):
    """Exact finite falsifier of any proposed ALL-h (alpha,beta).

    alpha,beta are exact Fraction-coercible integers/strings; no floats.
    """
    if isinstance(alpha,float) or isinstance(beta,float):
        raise ValueError("no floating-point theorem constants")
    A=Fraction(alpha);B=Fraction(beta)
    if A<=0 or B<0:
        raise ValueError("require alpha>0 and beta>=0")
    violated=[p for p in points
              if Fraction(p["S"])+B*p["J"]<A*(p["s"]**6)]
    if not violated:
        return {"refuted":False,"witness":None}
    row=min(violated,key=lambda p:(
        Fraction(p["S"])+B*p["J"]-A*(p["s"]**6),p["name"]))
    return {"refuted":True,"witness":row["name"],
            "S":row["S"],"J":row["J"],"s":row["s"],
            "actual_S_plus_beta_J":_frac_pair(
                row["S"]+B*row["J"]),
            "claimed_alpha_s6":_frac_pair(A*row["s"]**6)}


def report(*,shell_limit=105,include_correlated=True):
    points=finite_models(shell_limit=shell_limit,
                         include_correlated=include_correlated)
    pieces=lower_line_envelope(points)
    probes=independent_intersection_oracle(points,pieces)
    finite_lower_K=max(
        (Fraction(p["J"],p["S"]) for p in points if p["S"]>0),
        default=Fraction(0))
    if any(p["S"]==0 and p["J"]>0 for p in points):
        K=None
    else:
        K=_frac_pair(finite_lower_K)
    best_zero=min(points,key=lambda p:(p["S"],p["name"]))
    recorded=[(p["name"],p["S"],p["J"],p["GF5_numerator"])
              for p in points]
    digest=sha256(json.dumps(recorded,separators=(",",":"),
                              ensure_ascii=True).encode("ascii")).hexdigest()
    return {
        "slice":"HYP-105-E1-K3-G2-J",
        "status":"FINITE_RATIONAL_NECESSARY_SURPLUS_FRONTIER",
        "quantified_all_h_gate":"alpha <= inf_(s=2^h,all_legal_f_g) (S+beta*Jcross)/s^6",
        "true_all_h_positive_alpha_beta_proved":False,
        "all_h_Jcross_leq_K_S_proved":False,
        "branch_A_or_B_proved":False,
        "entire_W32_label_space_enumerated":False,
        "complete_single_swap_shell":shell_limit==105,
        "correlated_best_path_replayed":include_correlated,
        "finite_exact_model_count":len(points),
        "finite_distinct_S_J_pairs":len({(p["S"],p["J"]) for p in points}),
        "minimum_observed_S_at_beta_zero":{
            "name":best_zero["name"],"S":best_zero["S"],
            "J":best_zero["J"],"alpha_upper":_frac_pair(
                Fraction(best_zero["S"],64))},
        "finite_K_necessary_lower":K,
        "envelope_rational_pieces":pieces,
        "independent_pair_intersection_probes":probes,
        "example_refuted_alpha_2_beta_0":
            necessary_counterexample(points,2,0),
        "observations_sha256":digest,
        "no_W34_partial_target_as_negative_evidence":True,
    }


if __name__=="__main__":
    print(json.dumps(report(),sort_keys=True,indent=2))
