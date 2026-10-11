"""B8-D separate GitHub-hosted W(3,2) two-line influence oracle.

One B2 compressed 105-pair census plus independent ORIGINAL six-incidence
enumeration for three selected pairs. Never imported by generic unit tests.
"""
from collections import Counter
from fractions import Fraction
import json

from hyp105_g5e2b3e1c24b_three_collision import W32_LEFT_H45
from hyp105_g5e2b3e1c24_right_c_certificate import K6_PAIRS
from hyp105_g5e2b3e1c24b6_mixed_curvature_s68 import W32_RIGHT_S68
from hyp105_g5e2b3e1c24b2_joint_seven import compile_left, full_left_score
from hyp105_g5e2b3e1c24b8a_physical_tensor import (
    physical_factor_state, source_profile,
)
from hyp105_g5e2b3e1c24b8a_w32_tensor_witness import (
    independently_enumerate_left_original_sixsets,
)
from hyp105_g5e2b3e1c24b8d_two_line_influence import (
    compiled_matrix, source_influence,
)

def report():
    f0=tuple(W32_LEFT_H45)
    source=compile_left(f0)
    result=compiled_matrix(source,6,15)
    if result["mean"]!=Fraction(870476,5005):
        raise AssertionError("B8-C exact fixed-f conditional mean not retained")
    if full_left_score(source,tuple(W32_RIGHT_S68))["S_seven"]!=68:
        raise AssertionError("actual coherent W32 right score S68 not retained")
    if source["static_eligible"]!=53907:
        raise AssertionError("original left-eligible seven-source total changed")
    if len(result["matrix"])!=105 or any(result["row_sums"].values()):
        raise AssertionError("complete W32 two-pin influence matrix invalid")

    # A genuinely independent ORIGINAL six-incidence source enumerator,
    # not B2 compiled records. For the 3 selected original right line
    # pairs, evaluate every original left-eligible sixset exactly once.
    original=independently_enumerate_left_original_sixsets(f0)
    if len(original)!=62370:
        raise AssertionError("true ORIGINAL W32 left sixset universe changed")
    f={p+1:K6_PAIRS[v] for p,v in enumerate(f0)}
    selected=((0,1),(0,7),(3,10))
    independent={pair:Fraction(0) for pair in selected}
    by_tag=Counter()
    count=0
    for six in original:
        tag=source_profile(six)
        if tag is None:
            continue
        eligible,sig=physical_factor_state(six,f,left=True)
        if not eligible or (tag=="D6" and sig is None):
            continue
        count+=1
        by_tag[tag]+=1
        right_lines=tuple(l for _,l in six)
        for pair in selected:
            independent[pair]+=source_influence(
                6,tag,right_lines,sig if tag=="D6" else None,
                *pair)["influence"]
    if count!=source["static_eligible"] or by_tag!=Counter(result["populations"]):
        raise AssertionError("independent ORIGINAL GQ source populations disagree")
    for pair in selected:
        if independent[pair]!=result["matrix"][pair]:
            raise AssertionError("independent ORIGINAL two-line covariance mismatch")

    scores=tuple(result["matrix"].values())
    positive=sum(v>0 for v in scores)
    negative=sum(v<0 for v in scores)
    zeros=sum(v==0 for v in scores)
    if positive+negative+zeros!=105:
        raise AssertionError("influence sign accounting failed")
    p=result["p_adj"]
    mu=result["mean"]
    # Weighted second-pin orbit identity for all 105 pairs, exact rationals.
    for I in scores:
        adj=mu+(1-p)*I
        dis=mu-p*I
        if p*adj+(1-p)*dis!=mu or adj<0 or dis<0:
            raise AssertionError("exact complete-right conditional mean invalid")
    return {
        "slice":"HYP-105-C24-B8-D",
        "original_W32_source_count":len(original),
        "original_left_eligible_count":count,
        "independent_original_selected_pairs_verified":[list(x) for x in selected],
        "unconditional_fixed_left_mean":str(mu),
        "coherent_right_score":68,
        "pairs":105,
        "positive":positive,"negative":negative,"zero":zeros,
        "min_influence":str(min(scores)),
        "max_influence":str(max(scores)),
        "max_absolute_influence":str(max(abs(x) for x in scores)),
        "nonzero_rows":sum(v!=0 for v in result["row_sums"].values()),
        "full_K6_edge_bijection_row_sums_zero":True,
        "no_all_h_positive_lower_no_global_minimum_no_R3_claim":True,
    }

if __name__=="__main__":
    print(json.dumps(report(),indent=2,sort_keys=True))
