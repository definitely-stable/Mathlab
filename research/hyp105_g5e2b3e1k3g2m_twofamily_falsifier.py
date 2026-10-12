"""HYP-105 E1-K3-G2-M: dual original B/A-A/B exact transfer and falsifier.

Exact all-h identity (M1): A-left/B-right of the original model is
B-left/A-right on its transposed ORIGINAL incidence host, with the
original physical pair-label injections swapped whole. Every multiplicity
is an ORIGINAL distinct six-incidence source support.

The candidate U_BA(f,g)+U_AB(f,g)>=mu_BA(f) is a proper mathematical
strengthening of S_seven>=mu_BA(f), not a previously proved theorem.
Every negative W32 certificate here is checked by COMPLETE independent
62370 B0 enumeration AND two independent C0 original-sixsource weights.
Search is nonexhaustive and all-h positive claims are forbidden.
"""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
import json
import random

from hyp105_g5e2b3e1k1_kikuchi_c6 import gq_pair_model,labeled_model
from hyp105_g5e2b3e1b0_seven_signature import seven_census
from hyp105_g5e2b3e1c0_weighted_overlap import (
    source_weighted_BA_hypergraph,exact_BA_overlap,
    random_injection_expectation,simple_six_2factor_targets,
)
from hyp105_g5e2b3e1k3g2h_exact_swap_shell import swapped_labeling
from hyp105_g5e2b3e1k3g2i_correlated_delta import ExactSevenDelta
from hyp105_g5e2b3e1k3g2d_charging_hall import cross_witnesses
from hyp105_g5e2b3e1k3g2j_surplus_frontier import (
    BEST_CORRELATED_ANCHOR,BEST_CORRELATED_PATH,
)
from hyp105_g5e2b3e1k3g2l_compensation_transport import (
    _iterate_legal_W32_maps,as_pair,
)
from hyp105_g5e2b3e1k3g2k_conditional_injection import _W32_oracle

BA="B-left/A-right"
AB="A-left/B-right"


def dual_model(model):
    """Reverse actual ORIGINAL GQ factor incidences; keep full pair maps."""
    result=labeled_model(
        model["s"],model["a"],
        ((l,p) for p,l in model["incidences"]),
        model["right_labels"],model["left_labels"],
        scheme="original-dual:"+model["scheme"])
    if result["N"]!=model["N"]:
        raise AssertionError("original dual lost incidences")
    return result


def _support_digest(model):
    return sha256(repr((model["incidences"],model["left_labels"],
                        model["right_labels"])).encode("ascii")).hexdigest()


def _weights(cache,model):
    key=model["left_labels"]
    if key not in cache:
        cache[key]=source_weighted_BA_hypergraph(model)
    return cache[key]


def exact_two_family_point(model,*,left_cache=None,right_cache=None):
    """Three INDEPENDENT full original oracles, same coherent f,g."""
    if model["s"]!=2 or model["a"]!=6 or len(model["left_labels"])!=15:
        raise ValueError("complete true finite source-gate supports W32/K6 only")
    left_cache={} if left_cache is None else left_cache
    right_cache={} if right_cache is None else right_cache
    left=_weights(left_cache,model)
    dual=dual_model(model)
    right=_weights(right_cache,dual)
    targets=simple_six_2factor_targets(6)
    BA_value=exact_BA_overlap(left,model["right_labels"],target=targets)
    AB_value=exact_BA_overlap(right,dual["right_labels"],target=targets)
    mu=random_injection_expectation(left,a=6,original_vertices=15)
    census=seven_census(model,independent_checks=False)
    tags=census["seven_class_motif_counts"]
    dual_census=seven_census(dual,independent_checks=False)
    dual_tags=dual_census["seven_class_motif_counts"]
    if (tags[BA]!=BA_value or tags[AB]!=AB_value or
            dual_tags[BA]!=AB_value or dual_tags[AB]!=BA_value or
            sum(tags.values())!=census["S_seven"] or
            dual_census["S_seven"]!=census["S_seven"]):
        raise AssertionError("dual independent exact C0 and complete B0 disagree")
    pair=BA_value+AB_value
    S=census["S_seven"]
    return {
        "U_BA":BA_value,"U_AB":AB_value,
        "two_family":pair,
        "five_other_family":S-pair,
        "S_seven":S,
        "mu_BA":as_pair(mu),
        "two_family_minus_mu":as_pair(pair-mu),
        "all_seven_minus_mu":as_pair(S-mu),
        "finite_two_family_counterexample":pair<mu,
        "finite_all_seven_mu_counterexample":S<mu,
        "distinct_original_left_6candidates":
            census["left_6coordinate_candidates"],
        "distinct_original_dual_left_6candidates":
            dual_census["left_6coordinate_candidates"],
        "dual_seven_S_invariant":True,
        "accepted_class_counts":tags,
        "strict_positive_GF5_lower_numerator":
            census["GF5_seven_lower_numerator"],
        "physical_global_labels_sha256":_support_digest(model),
        "no_all_h_positive_claim":True,
    }


def _cheap_objective(state,mu_cache):
    """EXACT total two-positive-family score from maintained original tags.

    Candidate evaluations use precise G2-I delta tags; committed cases
    MUST undergo independent complete B0/C0/dual recount before reporting.
    """
    if state.model["left_labels"] not in mu_cache:
        w=source_weighted_BA_hypergraph(state.model)
        mu_cache[state.model["left_labels"]]=random_injection_expectation(
            w,a=6,original_vertices=15)
    counts=Counter(state.tags.values())
    return Fraction(counts[BA]+counts[AB])-mu_cache[
        state.model["left_labels"]]


def source_corpus(*,shell_limit=105,include_constructed=True):
    """Exact finite 223-model two-family theorem/falsifier, NOT all labelings."""
    left_cache={}
    right_cache={}
    cases=[]
    digest=sha256()
    for name,model in _iterate_legal_W32_maps(
            shell_limit,include_constructed):
        row=exact_two_family_point(
            model,left_cache=left_cache,right_cache=right_cache)
        cases.append((name,row))
        digest.update(json.dumps(
            (name,row["U_BA"],row["U_AB"],row["S_seven"],row["mu_BA"],
             row["strict_positive_GF5_lower_numerator"]),
            separators=(",",":"),sort_keys=True).encode("ascii")+b"\n")
    count=2+2*shell_limit+7+(4 if include_constructed else 0)
    if len(cases)!=count:
        raise AssertionError("finite original coherent corpus coverage changed")
    failures=[(n,r) for n,r in cases if r[
        "finite_two_family_counterexample"]]
    sevenfail=[(n,r) for n,r in cases if r[
        "finite_all_seven_mu_counterexample"]]
    low=min(cases,key=lambda x:(
        Fraction(*x[1]["two_family_minus_mu"]),x[0]))
    selected_names={"lex","corr:5","corr:6",
                    "CE:lex:minimize","CE:correlated-left:minimize"}
    return {
        "slice":"HYP-105-E1-K3-G2-M",
        "named_exact_original_source_maps":len(cases),
        "complete_single_swap_shell":shell_limit==105,
        "constructed_high_low_four":include_constructed,
        "distinct_original_left_f":len(left_cache),
        "distinct_original_right_g":len(right_cache),
        "two_family_failures":len(failures),
        "full_seven_mu_failures":len(sevenfail),
        "finite_two_family_counterexample_cases":[
            {"name":n,**r} for n,r in failures[:6]
        ],
        "finite_full_seven_mu_counterexample_cases":[
            {"name":n,**r} for n,r in sevenfail[:6]
        ],
        "smallest_two_family_signed_margin":{
            "name":low[0],
            "value":low[1]["two_family_minus_mu"],
            "S":low[1]["S_seven"],
            "U_BA":low[1]["U_BA"],
            "U_AB":low[1]["U_AB"],
            "five_other_family":low[1]["five_other_family"],
            "mu":low[1]["mu_BA"],
            "physical_global_labels_sha256":
                low[1]["physical_global_labels_sha256"],
        },
        "selected_full_true_source_ledger":{
            name:r for name,r in cases if name in selected_names},
        "full_source_corpus_sha256":digest.hexdigest(),
        "universal_all_h_two_family_claim":False,
        "universal_all_h_full_S_claim":False,
        "entire_W32_pair_map_space_exhausted":False,
    }


def _anchors():
    base=gq_pair_model(1,"lex")
    correlated=base
    for side,i,j in BEST_CORRELATED_ANCHOR:
        correlated=swapped_labeling(correlated,side,i,j)
    for side,i,j in BEST_CORRELATED_PATH[:5]:
        correlated=swapped_labeling(correlated,side,i,j)
    weights,physical,targets,oracle=_W32_oracle(base)
    low=oracle.construct("minimize")
    low_right=tuple(physical[i] for i in low["pair_ids"])
    low_model=labeled_model(2,6,base["incidences"],base["left_labels"],
                            low_right,scheme="K3-K-lex-low")
    return (("correlated-5",correlated),("K3-K-lex-low",low_model),
            ("lex",base))


def correlated_twofamily_probe(*,steps=5,proposals_per_step=8,
                               anchor_limit=3,seed=20261012):
    """Deterministic GREEDY finite falsifier; every chosen map independently full."""
    if any(type(v) is not int for v in
           (steps,proposals_per_step,anchor_limit,seed)) or (
            not 1<=steps<=8 or
            not 1<=proposals_per_step<=105 or
            not 1<=anchor_limit<=3):
        raise ValueError("exact legal steps 1..8, proposals 1..105, anchors 1..3")
    pair_ids=list(combinations(range(15),2))
    result=[]
    digest=sha256()
    left_cache={}
    right_cache={}
    mu_cache={}
    scored=0
    full=0
    for n,(name,model) in enumerate(_anchors()[:anchor_limit]):
        rng=random.Random(seed+n*10103)
        state=ExactSevenDelta(model)
        incumbent=exact_two_family_point(
            state.model,left_cache=left_cache,right_cache=right_cache)
        if _cheap_objective(state,mu_cache)!=Fraction(*incumbent[
                "two_family_minus_mu"]):
            raise AssertionError("selected anchor G2-I delta mismatch")
        full+=1
        path=[]
        if incumbent["finite_two_family_counterexample"]:
            stop="initial_full_certificate"
        else:
            stop="completed_nonexhaustive_path"
            for step in range(steps):
                # Alternate LEFT/RIGHT to expose genuine correlated changes
                side="left" if step%2==0 else "right"
                proposals=rng.sample(pair_ids,proposals_per_step)
                options=[]
                for i,j in proposals:
                    child,_=state.transition(side,i,j)
                    score=_cheap_objective(child,mu_cache)
                    options.append((score,child,i,j))
                    scored+=1
                _,state,i,j=min(options,key=lambda x:(x[0],x[2],x[3]))
                exact=exact_two_family_point(
                    state.model,left_cache=left_cache,right_cache=right_cache)
                full+=1
                margin=Fraction(*exact["two_family_minus_mu"])
                if margin!=_cheap_objective(state,mu_cache):
                    raise AssertionError("full independent original source replay differed")
                entry={
                    "step":step+1,"side":side,"i":i,"j":j,
                    "U_BA":exact["U_BA"],"U_AB":exact["U_AB"],
                    "S_seven":exact["S_seven"],
                    "five_other_family":exact["five_other_family"],
                    "mu_BA":exact["mu_BA"],
                    "two_family_minus_mu":exact["two_family_minus_mu"],
                    "full_S_minus_mu":exact["all_seven_minus_mu"],
                    "Jcross":len(cross_witnesses(state.model)),
                    "finite_two_family_counterexample":
                        exact["finite_two_family_counterexample"],
                    "finite_all_seven_mu_counterexample":
                        exact["finite_all_seven_mu_counterexample"],
                    "physical_global_labels_sha256":
                        exact["physical_global_labels_sha256"],
                }
                path.append(entry)
                digest.update(json.dumps(
                    (name,entry),sort_keys=True,separators=(",",":")).encode(
                        "ascii")+b"\n")
                if entry["finite_two_family_counterexample"]:
                    stop="found_complete_true_source_counterexample"
                    break
        result.append({
            "anchor":name,
            "initial":incumbent,
            "selected_path":path,
            "terminal_status":stop,
        })
    scored_expectation=sum(len(r["selected_path"])*proposals_per_step
                            for r in result)
    if scored!=scored_expectation or full!=anchor_limit+sum(
            len(r["selected_path"]) for r in result):
        raise AssertionError("candidate/full-source coverage mismatch")
    fail=[(r["anchor"],p) for r in result for p in r["selected_path"]
          if p["finite_two_family_counterexample"]]
    for r in result:
        if r["initial"]["finite_two_family_counterexample"]:
            fail.append((r["anchor"],r["initial"]))
    all_rows=[p for r in result for p in [r["initial"]]+r["selected_path"]]
    minrow=min(all_rows,key=lambda p:Fraction(*p["two_family_minus_mu"]))
    return {
        "slice":"HYP-105-E1-K3-G2-M",
        "seed":seed,
        "anchors_tested":anchor_limit,
        "candidate_moves_precisely_delta_scored":scored,
        "complete_original_B0_C0_dual_replays":full,
        "strict_full_source_two_family_counterexamples":len(fail),
        "finite_counterexample_first":(
            {"anchor":fail[0][0],"value":fail[0][1]} if fail else None),
        "minimum_found_two_family_minus_mu":
            minrow["two_family_minus_mu"],
        "selected_path_sha256":digest.hexdigest(),
        "result":result,
        "all_h_branch_A_B_proved":False,
        "whole_W32_map_space_exhausted":False,
    }


def report():
    return {"slice":"HYP-105-E1-K3-G2-M",
            "complete_corpus":source_corpus(),
            "correlated_adversarial":correlated_twofamily_probe(),
            "all_h_two_family_inequality_proved":False,
            "all_h_seven_family_inequality_proved":False,
            "branch_A_B":"OPEN"}


if __name__=="__main__":
    print(json.dumps(report(),sort_keys=True,indent=2))
