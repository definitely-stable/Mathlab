"""HYP-105 E1-K3-G2-L: exact compensation accounting + XOR swap transport.

ALL-H statements:
  (L1) For B/A original six-source weighted hypergraph w_f and a legal
       whole-source right label transposition of u,v, only right sixsets
       containing EXACTLY ONE of u,v affect U_B/A. This holds for K>=V,
       any nonnegative source weights and any six-target predicate.
  (L2) D_BA=mu-U_BA, Rest=S_seven-U_BA gives
       Rest-D_BA=S_seven-mu, an IDENTICAL expression.
       It is NOT an all-h positive surplus theorem.
  (L3) For each legal model any proposed D_BA<=Rest+beta*J has the
       necessary condition beta*J >= mu-S. Thus J=0, mu>S refutes
       ALL beta>=0 for this coefficient-normalized condition.
All finite negative certificates use COMPLETE W32 original B0, never
partial W34 target discovery. All finite positives are SAMPLE ONLY.
"""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
import json

from hyp105_g5e2b3e1k1_kikuchi_c6 import gq_pair_model,labeled_model
from hyp105_g5e2b3e1b0_seven_signature import seven_census
from hyp105_g5e2b3e1c0_weighted_overlap import (
    source_weighted_BA_hypergraph, exact_BA_overlap,
    random_injection_expectation, simple_six_2factor_targets,
)
from hyp105_g5e2b3e1k3g2h_exact_swap_shell import swapped_labeling
from hyp105_g5e2b3e1k3g2d_charging_hall import cross_witnesses
from hyp105_g5e2b3e1k3g2j_surplus_frontier import (
    BEST_CORRELATED_ANCHOR, BEST_CORRELATED_PATH, BEST_PATH_EXPECTED,
)
from hyp105_g5e2b3e1k3g2k_conditional_injection import _W32_oracle

EXPECTED_SINGLE_SHELL=(176,47,139)


def as_pair(q):
    x=Fraction(q)
    return [x.numerator,x.denominator]


def exact_original_right_swap_delta(weights, model, i, j, target=None):
    """The full rank-six XOR-support transport identity.

    Sixset R including BOTH swapped right source origins maps to the
    SAME unordered physical six-edge set; R including NEITHER is
    unchanged. Only |R intersection {i,j}|=1 has a signed contribution.
    An original incidence point is never independently relabeled.
    """
    if model["s"]!=2 or model["a"]!=6:
        raise ValueError("hosted complete B/A swap oracle is W32/K6 only")
    if type(i) is not int or type(j) is not int or not 0<=i<j<15:
        raise ValueError("right source swap needs distinct integer original IDs")
    if target is None:
        target=simple_six_2factor_targets(6)
    before=model["right_labels"]
    after=swapped_labeling(model,"right",i,j)["right_labels"]
    signed=0
    affected_sources=0
    weight_affected=0
    for R,weight in weights.items():
        if (i in R)==(j in R):
            continue
        affected_sources+=1
        weight_affected+=weight
        old=frozenset(before[x] for x in R)
        new=frozenset(after[x] for x in R)
        signed+=weight*(int(new in target)-int(old in target))
    pre=exact_BA_overlap(weights,before,target=target)
    post=exact_BA_overlap(weights,after,target=target)
    if post-pre!=signed:
        raise AssertionError("XOR original six-source transport formula failed")
    return {
        "original_right_swap":[i,j],
        "affected_exactly_one_source_sixsets":affected_sources,
        "weight_affected_exactly_one":weight_affected,
        "BA_before":pre,"BA_after":post,
        "signed_delta":signed,
        "full_original_recount_agrees":True,
    }


def compensation_point(model, weights=None):
    """FULL W32 B0 original positive GF5 seven-family census and ledger."""
    if model["s"]!=2 or model["a"]!=6:
        raise ValueError("complete W32 six-class census only")
    if weights is None:
        weights=source_weighted_BA_hypergraph(model)
    mu=random_injection_expectation(
        weights,a=6,original_vertices=len(model["right_labels"]))
    target=simple_six_2factor_targets(6)
    U=exact_BA_overlap(weights,model["right_labels"],target=target)
    census=seven_census(model,independent_checks=False)
    types=census["seven_class_motif_counts"]
    if types["B-left/A-right"]!=U or sum(types.values())!=census["S_seven"]:
        raise AssertionError("true original B/A not equal independent complete B0")
    S=census["S_seven"]
    J=len(cross_witnesses(model))
    rest=S-U
    D=mu-U
    # Separate B/A from the other SIX strictly accepted positive original
    # GF5 classes; the signed deficit need not be positive.
    assert rest==sum(n for tag,n in types.items()
                     if tag!="B-left/A-right")
    if Fraction(rest)-D!=Fraction(S)-mu:
        raise AssertionError("compensation tautology arithmetic failed")
    required=(mu-S)/J if J else None
    if required is not None:
        required=max(Fraction(0),required)
    return {
        "S":S,"Jcross":J,
        "U_BA":U,"S_other_six":rest,
        "mu_BA":as_pair(mu),
        "signed_deficit_D_mu_minus_BA":as_pair(D),
        "signed_other_minus_deficit":as_pair(rest-D),
        "signed_total_surplus_S_minus_mu":as_pair(S-mu),
        "positive_deficit":as_pair(max(D,Fraction(0))),
        "other_six_family_counts":{k:v for k,v in sorted(types.items())
                                  if k!="B-left/A-right"},
        "full_positive_GF5_seven_numerator":
            census["GF5_seven_lower_numerator"],
        "negative_residual_without_J":S<mu,
        "impossible_any_beta_if_J_zero_and_S_below_mu":J==0 and S<mu,
        "necessary_beta_nonnegative_if_J_positive":
            as_pair(required) if required is not None else None,
        "all_h_surplus_proved":False,
    }


def _iterate_legal_W32_maps(shell_limit,include_constructed):
    if type(shell_limit) is not int or not 0<=shell_limit<=105:
        raise ValueError("0<=shell_limit<=105 required")
    if type(include_constructed) is not bool:
        raise ValueError("include_constructed boolean required")
    base=gq_pair_model(1,"lex")
    yield "lex",base
    yield "reverse-line",gq_pair_model(1,"reverse-line")
    pairs=tuple(combinations(range(15),2))
    for side in ("left","right"):
        for i,j in pairs[:shell_limit]:
            yield f"lex:{side}:{i}:{j}",swapped_labeling(base,side,i,j)
    state=base
    for side,i,j in BEST_CORRELATED_ANCHOR:
        state=swapped_labeling(state,side,i,j)
    yield "corr:anchor",state
    for step,((side,i,j),(s,jj)) in enumerate(zip(
            BEST_CORRELATED_PATH,BEST_PATH_EXPECTED),1):
        state=swapped_labeling(state,side,i,j)
        yield f"corr:{step}",state
    if include_constructed:
        for label,original_left in (
            ("lex",base),
            ("correlated-left",_replay_left_correlated(base))):
            weights,physical,targets,oracle=_W32_oracle(original_left)
            for direction in ("maximize","minimize"):
                cert=oracle.construct(direction)
                right=tuple(physical[k] for k in cert["pair_ids"])
                model=labeled_model(2,6,original_left["incidences"],
                                    original_left["left_labels"],right,
                                    scheme=f"CE:{label}:{direction}")
                yield f"CE:{label}:{direction}",model


def _replay_left_correlated(base):
    state=base
    for i,j in ((0,14),(1,4),(2,13),(2,3)):
        state=swapped_labeling(state,"left",i,j)
    return state


def report(*,shell_limit=105,include_constructed=True):
    rows=[]
    left_masses={}
    snapshots={}
    digest=sha256()
    for name,model in _iterate_legal_W32_maps(
            shell_limit,include_constructed):
        left=model["left_labels"]
        if left not in left_masses:
            left_masses[left]=source_weighted_BA_hypergraph(model)
        row=compensation_point(model,left_masses[left])
        rows.append((name,row))
        if name in ("lex","corr:5","corr:6",
                    "CE:lex:maximize","CE:lex:minimize",
                    "CE:correlated-left:maximize",
                    "CE:correlated-left:minimize"):
            snapshots[name]=row
        digest.update(json.dumps(
            (name,row["S"],row["Jcross"],row["U_BA"],
             row["mu_BA"],row["S_other_six"],
             row["full_positive_GF5_seven_numerator"]),
            separators=(",",":"),ensure_ascii=True).encode("ascii")+b"\n")
    if shell_limit==105:
        shell=[p for name,p in rows if name.startswith("lex:left:") or
               name.startswith("lex:right:")]
        if (len(shell)!=210 or
            (min(p["S"] for p in shell),
             max(p["Jcross"] for p in shell),
             min(p["S"]-p["Jcross"] for p in shell))!=EXPECTED_SINGLE_SHELL):
            raise AssertionError("G2-H one-swap exact complete-shell regression")
    if include_constructed:
        anchors={
            "CE:lex:maximize":(131,320),
            "CE:lex:minimize":(33,101),
            "CE:correlated-left:maximize":(120,245),
            "CE:correlated-left:minimize":(40,104),
        }
        for name,expected in anchors.items():
            r=snapshots[name]
            if (r["U_BA"],r["S"])!=expected:
                raise AssertionError("K3-G2-K full B/A derandomization regression")
    min_slack=min(rows,key=lambda x:(
        Fraction(*x[1]["signed_total_surplus_S_minus_mu"]),x[0]))
    positive_deficit=[(name,p) for name,p in rows if
                      Fraction(*p["signed_deficit_D_mu_minus_BA"])>0]
    under=[(name,p) for name,p in rows if p["negative_residual_without_J"]]
    impossible=[name for name,p in rows if p[
        "impossible_any_beta_if_J_zero_and_S_below_mu"]]
    required=[(Fraction(*p["necessary_beta_nonnegative_if_J_positive"]),name)
              for name,p in rows if
              p["necessary_beta_nonnegative_if_J_positive"] is not None]
    beta,beta_witness=max(required,default=(Fraction(0),None))
    # An admissible zero-J source map with S<mu would make the requested
    # EXACT finite μ-normalized β repair impossible at any finite beta.
    if impossible:
        beta_possible=False
    else:
        beta_possible=True
    return {
        "slice":"HYP-105-E1-K3-G2-L",
        "model_count":len(rows),
        "complete_210_single_swap_shell":shell_limit==105,
        "four_constructed_K_maps":include_constructed,
        "unique_fixed_left_source_maps":len(left_masses),
        "right_six_target_count":70,
        "positive_deficit_D_maps":len(positive_deficit),
        "tested_S_below_fixed_left_mu_maps":len(under),
        "tested_zero_J_S_below_mu_impossible_maps":impossible[:10],
        "finite_beta_possible_for_all_tested_maps":beta_possible,
        "necessary_beta_floor_from_tested_J_positive":as_pair(beta),
        "finite_beta_floor_witness":beta_witness,
        "minimum_observed_signed_S_minus_mu":{
            "name":min_slack[0],"value":
                min_slack[1]["signed_total_surplus_S_minus_mu"],
            "S":min_slack[1]["S"],
            "mu":min_slack[1]["mu_BA"],
            "Jcross":min_slack[1]["Jcross"]},
        "witnesses":snapshots,
        "entire_W32_label_space_enumerated":False,
        "all_h_true_compensation_inequality_proved":False,
        "all_h_K_charge_proved":False,
        "branch_A_B":"OPEN",
        "ordered_full_original_ledger_sha256":digest.hexdigest(),
        "proof_scope":"all_h_XOR_swap_identity_and_algebraic_equivalence;finite_W32_full_source_audit",
    }


def report_small():
    return report(shell_limit=1,include_constructed=False)


if __name__=="__main__":
    print(json.dumps(report(),sort_keys=True,indent=2))
