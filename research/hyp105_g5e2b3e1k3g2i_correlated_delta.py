"""HYP-105 E1-K3-G2-I: exact W32 delta locality and correlated two-sided search.

All source moves swap WHOLE unordered physical pair labels of original
vertices. The exact local update theorem is deterministic, not a stochastic
approximation: only original six-incidence subsets touching one of the
swapped original endpoints on that side may change seven-family membership.
Each committed search state is independently replayed by complete B0
enumeration and complete-target Hall, never a budgeted-target negative claim.

The deterministic adversarial search is NOT exhaustive over all maps,
sequences, or even all candidate transitions at any given state.
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations
import json
import random

from hyp105_g5e2b3e1k1_kikuchi_c6 import gq_pair_model
from hyp105_g5e2b3e1a_fixed_leading import selected_left_six
from hyp105_g5e2b3e1b0_seven_signature import (
    R3_CERTIFIED_FLOORS, classify_seven_prechecked, seven_census,
)
from hyp105_g5e2b3e1k3g2d_charging_hall import cross_witnesses
from hyp105_g5e2b3e1k3g2h_exact_swap_shell import (
    swapped_labeling, full_target_hall,
)

ANCHORS=(
    (("left",1,14),("right",2,11)),
    (("left",3,9),("right",1,8)),
    (("left",0,14),("right",0,14)),
)


def _eligible_left(model):
    """The COMPLETE 62,370 distinct original sixsets left-eligible in B0."""
    found=frozenset(ids for ids,_ in selected_left_six(model))
    if len(found)!=62370:
        raise AssertionError("original left-six enumeration lost completeness")
    return found


def _labels_digest(model):
    return sha256(repr((
        model["incidences"],model["left_labels"],model["right_labels"]
    )).encode("ascii")).hexdigest()


class ExactSevenDelta:
    """Exact accepted seven-family original-sixset state at one coherent f,g."""

    def __init__(self, model, eligible=None, tags=None):
        if model["s"]!=2 or model["a"]!=6 or (
                len(model["left_labels"])!=15 or
                len(model["right_labels"])!=15):
            raise ValueError("G2-I exhaustive original-sixset oracle is W32/K6 only")
        self.model=model
        self.eligible=_eligible_left(model) if eligible is None else eligible
        if len(self.eligible)!=62370:
            raise AssertionError("incomplete left-six eligible universe")
        if tags is None:
            left=model["left_labels"];right=model["right_labels"]
            edges=model["incidences"]
            tags={}
            for ids in self.eligible:
                tag=classify_seven_prechecked(ids,left,right,edges)
                if tag is not None:
                    tags[ids]=tag
        self.tags=tags
        if not set(tags)<=self.eligible or any(
                tag not in R3_CERTIFIED_FLOORS for tag in tags.values()):
            raise AssertionError("invalid accepted seven-family source support")

    @property
    def S(self):
        return len(self.tags)

    @property
    def GF5_numerator(self):
        return sum(R3_CERTIFIED_FLOORS[v] for v in self.tags.values())

    def transition(self,side,i,j):
        """Incremental exact update using ORIGINAL factor endpoint support.

        Lemma: Any fixed original sixset omitting BOTH changed original
        source endpoints has unchanged physical labels on all its six
        incidences, hence identical accepted-family classification.
        When LEFT labels change, the complete left eligibility universe
        can change: use its old/new UNION on the impacted subfamily.
        """
        after=swapped_labeling(self.model,side,i,j)
        edges=self.model["incidences"]
        coordinate=0 if side=="left" else 1
        touched=frozenset(k for k,e in enumerate(edges)
                           if e[coordinate]==i or e[coordinate]==j)
        if len(touched)!=6:
            raise AssertionError("W(3,2) source endpoints have 3 incidences")
        next_eligible=_eligible_left(after) if side=="left" else self.eligible
        impacted_old={ids for ids in self.eligible
                      if any(column in touched for column in ids)}
        impacted_new={ids for ids in next_eligible
                      if any(column in touched for column in ids)}
        if side=="left":
            if (self.eligible-impacted_old)!=(
                    next_eligible-impacted_new):
                raise AssertionError("untouched original-six eligibility mutated")
        # Precisely preserve the unmodified accepted original sixsets,
        # including their family type; recompute every potentially changed
        # old/new eligible original sixset without any target/work cutoff.
        new_tags={ids:tag for ids,tag in self.tags.items()
                  if ids not in impacted_old}
        for ids in impacted_new:
            tag=classify_seven_prechecked(
                ids,after["left_labels"],after["right_labels"],edges)
            if tag is not None:
                new_tags[ids]=tag
        result=ExactSevenDelta(after,next_eligible,new_tags)
        changed=sum(self.tags.get(ids)!=new_tags.get(ids)
                    for ids in impacted_old|impacted_new)
        return result,{
            "side":side,"i":i,"j":j,
            "original_columns_touched":len(touched),
            "old_candidates_affected":len(impacted_old),
            "new_candidates_affected":len(impacted_new),
            "affected_union_size":len(impacted_old|impacted_new),
            "membership_or_class_changes":changed,
            "S_before":self.S,"S_after":result.S,
            "GF5_floor_delta":result.GF5_numerator-self.GF5_numerator,
        }


def independent_full_replay(state):
    """Always use independent COMPLETE B0 and entire genuine Hall universe."""
    model=state.model
    census=seven_census(model,witness_sets=True,independent_checks=False)
    if (census["sets"]!=state.tags or
            census["S_seven"]!=state.S or
            census["GF5_seven_lower_numerator"]!=state.GF5_numerator):
        raise AssertionError("incremental delta diverged from independent B0")
    hall=full_target_hall(model)
    if (hall["S_seven_exact"]!=state.S or
            hall["GF5_seven_numerator_exact_class_floor"]!=state.GF5_numerator):
        raise AssertionError("true positive S and GF5 lower bound disagree")
    if hall["Jcross"]!=len(cross_witnesses(model)):
        raise AssertionError("source witness provenance count disagrees")
    if hall["matched"]+hall["hall_deficiency"]!=hall["Jcross"]:
        raise AssertionError("inconsistent Hall mincut accounting")
    return hall


def _validated_search_limits(steps,proposals_per_step):
    if (type(steps) is not int or not 1<=steps<=10 or
            type(proposals_per_step) is not int or
            not 1<=proposals_per_step<=105):
        raise ValueError("steps in 1..10 and proposals_per_step in 1..105")


def correlated_search(*,steps=6,proposals_per_step=8,
                      seed=20261012,anchor_limit=3):
    """Adversarial selected states: exact delta proposals, fully replayed winners.

    Unlike G2-H's complete radius-1 shell, this is a seeded NONEXHAUSTIVE
    multi-step trajectory probe.  The search makes no claims about unseen
    W32 pair permutations; it can refute unit Hall if any fully replayed
    complete-target state has a rigorously certified deficient cut.
    """
    _validated_search_limits(steps,proposals_per_step)
    if (type(seed) is not int or
            type(anchor_limit) is not int or
            not 1<=anchor_limit<=len(ANCHORS)):
        raise ValueError("integer seed and 1..3 anchors required")
    base=gq_pair_model(1,"lex")
    pairs=tuple(combinations(range(15),2))
    results=[]
    digest=sha256()
    checked_candidates=0
    for anchor_number in range(anchor_limit):
        rng=random.Random(seed+anchor_number*1000003)
        state=ExactSevenDelta(base)
        transcript=[]
        for side,i,j in ANCHORS[anchor_number]:
            state,change=state.transition(side,i,j)
            transcript.append(change)
        initial_hall=independent_full_replay(state)
        initial={"S":state.S,"Jcross":initial_hall["Jcross"],
                 "S_minus_J":state.S-initial_hall["Jcross"],
                 "Hall_deficiency":initial_hall["hall_deficiency"]}
        path=[]
        # Both sides were already perturbed by different complete-label
        # transpositions before evaluating any adaptive proposals.
        for step in range(steps):
            side="left" if step%2==0 else "right"
            proposals=rng.sample(pairs,proposals_per_step)
            options=[]
            for i,j in proposals:
                child,local=state.transition(side,i,j)
                J=len(cross_witnesses(child.model))
                options.append((
                    (child.S-J,child.S,-J,i,j),
                    child,local,J,
                ))
                checked_candidates+=1
            # Stable deterministic tie-breaking; this is a greedy
            # sampled-objective move, not a global local minimum theorem.
            _,state,change,jcross=min(options,key=lambda x:x[0])
            transcript.append(change)
            hall=independent_full_replay(state)
            if hall["Jcross"]!=jcross:
                raise AssertionError("proposal Jcross source provenance mismatch")
            record={
                "step":step+1,"side":side,
                "i":change["i"],"j":change["j"],
                "S_seven_exact":state.S,
                "Jcross":jcross,
                "S_minus_J":state.S-jcross,
                "GF5_floor_numerator":state.GF5_numerator,
                "full_Hall_unit":hall["hall_unit_capacity"],
                "Hall_deficiency":hall["hall_deficiency"],
                "Hall_cut_witness_subset":hall["hall_cut_witness_subset"],
                "Hall_cut_neighbor_size":hall["hall_cut_neighbor_size"],
                "min_witness_target_degree":hall["min_target_degree"],
                "labels_sha256":_labels_digest(state.model),
                "original_columns_touched":change["original_columns_touched"],
                "membership_or_class_changes":change["membership_or_class_changes"],
            }
            path.append(record)
            digest.update(json.dumps((anchor_number,record),
                                     sort_keys=True).encode("ascii")+b"\n")
            # A true finite counterexample is only claimed after full
            # independent B0+Hall replay, never on preview alone.
            if hall["hall_deficiency"]>0:
                break
        results.append({
            "anchor_number":anchor_number,
            "initial_two_sided_anchor":list(ANCHORS[anchor_number]),
            "initial_exact":initial,
            "committed_moves":len(path),
            "path":path,
            "full_oracle_replays":len(path)+1,
            "finite_two_overlap_unit_Hall_counterexample":
                any(not row["full_Hall_unit"] for row in path) or
                initial_hall["hall_deficiency"]>0,
            "final_labels_digest":_labels_digest(state.model),
        })
    all_states=[
        {**r["initial_exact"],"anchor":r["anchor_number"],"step":0}
        for r in results
    ]+[
        {**v,"anchor":r["anchor_number"]}
        for r in results for v in r["path"]
    ]
    def risk_sort(row):
        return (row["S_minus_J"],row["S"],-row["Jcross"],
                row["anchor"],row.get("step",0))
    minimum=min(all_states,key=risk_sort)
    failures=[r for r in results if r[
        "finite_two_overlap_unit_Hall_counterexample"]]
    return {
        "slice":"HYP-105-E1-K3-G2-I",
        "method":"W32_exact_single-source-swap_delta_and_correlated_greedy",
        "status":"FINITE_CORRELATED_ADVERSARIAL_EXACT_ORACLE",
        "seed":seed,"anchors_tested":anchor_limit,
        "steps_requested_per_anchor":steps,
        "proposals_requested_per_step":proposals_per_step,
        "candidate_transitions_exactly_scored":checked_candidates,
        "committed_states_independently_full_replayed":
            sum(r["full_oracle_replays"] for r in results),
        "all_h_universal_Hall_proved":False,
        "all_h_S_omega_proved":False,
        "full_W32_labeling_space_exhausted":False,
        "finite_unit_two_overlap_Hall_counterexamples":
            sum(r["finite_two_overlap_unit_Hall_counterexample"]
                for r in results),
        "minimum_observed_S_minus_J":{
            k:minimum[k] for k in
            ("S_minus_J","S","Jcross","anchor","step")
        },
        "results":results,
        "selected_path_certificate_sha256":digest.hexdigest(),
        "Branch_A_B":"OPEN",
    }


def report():
    return correlated_search()


if __name__=="__main__":
    print(json.dumps(report(),sort_keys=True,indent=2))
