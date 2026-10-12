"""HYP-105 E1-K3-G2-K: exact conditional-expectation derandomization.

Constructs whole globally injective right pair-label maps with B-left/A-right
overlap respectively >= and <= the uniform-injection expectation, for ANY
nonnegative weighted 6-uniform source hypergraph and physical 6-set target
family. All arithmetic is Fraction. The conditional formula is all-host/all-h;
the hosted concrete weighted-B/A original-incidence oracle is complete W32.

This is a classical conditional-expectations theorem applied to the specific
original-six-incidence B/A structure. It is NOT a universal ALL f,g positive
lower bound, nor a new derandomization method.
"""
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from math import comb
import json

from hyp105_g5e2a_pair_embeddings import unrank_pair
from hyp105_g5e2b3e1k1_kikuchi_c6 import gq_pair_model, labeled_model
from hyp105_g5e2b3e1b0_seven_signature import seven_census, R3_CERTIFIED_FLOORS
from hyp105_g5e2b3e1c0_weighted_overlap import (
    source_weighted_BA_hypergraph, simple_six_2factor_targets,
    exact_BA_overlap, random_injection_expectation,
)
from hyp105_g5e2b3e1k3g2h_exact_swap_shell import swapped_labeling

RANK=6


def fraction_pair(value):
    v=Fraction(value)
    return [v.numerator,v.denominator]


def _validate_weights(weights, V, K):
    if type(V) is not int or type(K) is not int or not 6<=V<=K:
        raise ValueError("require 6<=original vertices<=distinct physical pairs")
    result={}
    for R,w in weights.items():
        if type(w) is not int or w<0:
            raise ValueError("nonnegative integer six-uniform source weights")
        if type(R) not in (tuple,frozenset,set) or len(R)!=RANK or (
                any(type(v) is not int or not 0<=v<V for v in R)):
            raise ValueError("distinct six original endpoint IDs required")
        mask=sum(1<<v for v in R)
        if w:
            result[mask]=result.get(mask,0)+w
    return tuple(sorted(result.items()))


def _validate_targets(targets, K):
    masks=set()
    for T in targets:
        if type(T) not in (tuple,frozenset,set) or len(T)!=RANK or any(
                type(x) is not int or not 0<=x<K for x in T):
            raise ValueError("targets must have six distinct physical pair IDs")
        masks.add(sum(1<<v for v in T))
    return tuple(sorted(masks))


class SixSourceConditionalExpectation:
    """General weighted original-source / physical-six-target oracle.

    A partial injection maps k original endpoints to k DISTINCT physical
    pair IDs. For an original sixset R, fixed selected physical labels F
    and used labels O, its remaining unordered image is uniform among all
    C(K-k, 6-|F|) subsets of unused labels. Therefore

      P(image(R) in T | prefix) =
       #{T in targets: T & O == F} / C(K-k, 6-|F|).

    Includes labels assigned outside R as FORBIDDEN: omitting them would
    be an incorrect conditional probability.
    """
    def __init__(self, V, K, weights, targets):
        self.V=V
        self.K=K
        self.weights=_validate_weights(weights,V,K)
        self.target_masks=_validate_targets(targets,K)
        self._cover_cache={}

    def _count_eligible(self,occupied,forced):
        key=(occupied,forced)
        cached=self._cover_cache.get(key)
        if cached is not None:
            return cached
        n=sum((T&occupied)==forced for T in self.target_masks)
        self._cover_cache[key]=n
        return n

    def expectation(self,prefix):
        if not isinstance(prefix,(tuple,list)) or len(prefix)>self.V:
            raise ValueError("prefix length out of range")
        assigned=tuple(prefix)
        if any(type(x) is not int or not 0<=x<self.K for x in assigned):
            raise ValueError("physical IDs must be integer labels in range")
        if len(set(assigned))!=len(assigned):
            raise ValueError("right physical labels must be injective")
        k=len(assigned)
        occupied=sum(1<<x for x in assigned)
        source_prefix=(1<<k)-1
        physical_by_source=tuple(1<<x for x in assigned)
        buckets=[0]*7
        for R,w in self.weights:
            fixed=R&source_prefix
            t=fixed.bit_count()
            forced=0
            while fixed:
                lowest=fixed&-fixed
                fixed-=lowest
                forced|=physical_by_source[lowest.bit_length()-1]
            completions=self._count_eligible(occupied,forced)
            buckets[t]+=w*completions
        result=Fraction(0)
        for t,value in enumerate(buckets):
            if value:
                remaining=RANK-t
                if remaining>self.K-k:
                    raise AssertionError("impossible original injection completion")
                result+=Fraction(value,comb(self.K-k,remaining))
        return result

    def uniform_expectation(self):
        return self.expectation(())

    def full_overlap(self,labels):
        if len(labels)!=self.V:
            raise ValueError("complete original label assignment required")
        if len(set(labels))!=self.V:
            raise ValueError("complete map must inject physical pair labels")
        actual=self.expectation(tuple(labels))
        if actual.denominator!=1:
            raise AssertionError("complete overlap must be an integer")
        return actual.numerator

    def _branch_expectations(self,prefix):
        used=set(prefix)
        choices=[(self.expectation((*prefix,p)),p)
                 for p in range(self.K) if p not in used]
        if not choices:
            raise AssertionError("no remaining injection labels")
        parent=self.expectation(prefix)
        if sum((v for v,_ in choices),Fraction(0)) != parent*len(choices):
            raise AssertionError("exact conditional expectation tower failed")
        return parent,choices

    def construct(self,mode):
        if mode not in ("maximize","minimize"):
            raise ValueError("mode must be maximize or minimize")
        prefix=()
        start=self.uniform_expectation()
        path=[]
        for source_id in range(self.V):
            parent,options=self._branch_expectations(prefix)
            ranked=sorted(options,key=lambda x:(-x[0] if mode=="maximize"
                                                   else x[0],x[1]))
            selected,pair_id=ranked[0]
            if mode=="maximize" and selected<parent:
                raise AssertionError("conditional maximum below parent mean")
            if mode=="minimize" and selected>parent:
                raise AssertionError("conditional minimum above parent mean")
            prefix=(*prefix,pair_id)
            path.append({
                "source_id":source_id,
                "physical_pair_id":pair_id,
                "conditional_before":fraction_pair(parent),
                "conditional_after":fraction_pair(selected),
                "choices":len(options)
            })
        actual=self.full_overlap(prefix)
        if Fraction(actual)!=self.expectation(prefix):
            raise AssertionError("terminal score is not actual original overlap")
        if mode=="maximize" and actual<start:
            raise AssertionError("constructive upper expected count failed")
        if mode=="minimize" and actual>start:
            raise AssertionError("constructive lower expected count failed")
        serial=json.dumps(path,separators=(",",":"),sort_keys=True)
        return {
            "mode":mode,
            "source_vertices":self.V,
            "physical_label_capacity":self.K,
            "source_positive_sixsets":len(self.weights),
            "total_original_BA_weight":sum(w for _,w in self.weights),
            "target_sixsets":len(self.target_masks),
            "expectation":fraction_pair(start),
            "actual_overlap":actual,
            "pair_ids":list(prefix),
            "trajectory":path,
            "trajectory_sha256":sha256(serial.encode("ascii")).hexdigest(),
            "six_source_all_h_construction":True,
            "all_f_g_positive_lower_bound_proved":False
        }


def _W32_oracle(model):
    if (model["s"]!=2 or model["a"]!=6 or
            model["v_left"]!=15 or model["v_right"]!=15):
        raise ValueError("hosted full B/A original hypergraph is W32/K6 only")
    weights=source_weighted_BA_hypergraph(model)
    physical=tuple(unrank_pair(i,6) for i in range(comb(6,2)))
    reverse={pair:i for i,pair in enumerate(physical)}
    templates=simple_six_2factor_targets(6)
    targets=[frozenset(reverse[edge] for edge in template)
             for template in templates]
    return weights,physical,targets,SixSourceConditionalExpectation(
        len(model["right_labels"]),len(physical),weights,targets)


def hosted_W32_pair(*,left_variant="lex"):
    base=gq_pair_model(1,"lex")
    if left_variant=="lex":
        source=base
    elif left_variant=="correlated-left":
        source=base
        for i,j in ((0,14),(1,4),(2,13),(2,3)):
            source=swapped_labeling(source,"left",i,j)
    else:
        raise ValueError("supported original left selections: lex,correlated-left")
    weights,physical,targets,oracle=_W32_oracle(source)
    expected=oracle.uniform_expectation()
    independent=random_injection_expectation(
        weights,a=6,original_vertices=15)
    if expected!=independent:
        raise AssertionError("independent random-injection B/A mean disagrees")
    results={}
    for mode in ("maximize","minimize"):
        cert=oracle.construct(mode)
        labels=tuple(physical[i] for i in cert["pair_ids"])
        model=labeled_model(2,6,source["incidences"],
                            source["left_labels"],labels,
                            scheme=f"conditional-{left_variant}-{mode}")
        direct=exact_BA_overlap(weights,labels)
        full=seven_census(model,independent_checks=False)
        tag=full["seven_class_motif_counts"]["B-left/A-right"]
        if cert["actual_overlap"]!=direct or direct!=tag:
            raise AssertionError("independent source-weight and full B0 census mismatch")
        if full["S_seven"]<direct:
            raise AssertionError("accepted family exceeds full original S")
        cert.update({
            "complete_true_W32_B0_S":full["S_seven"],
            "actual_BA_full_B0_independent":tag,
            "seven_GF5_risk_floor_numerator":full["GF5_seven_lower_numerator"],
            "BA_GF5_risk_floor_numerator":
                tag*R3_CERTIFIED_FLOORS["B-left/A-right"],
            "physical_labels_sha256":sha256(
                repr(labels).encode("ascii")).hexdigest(),
        })
        results[mode]=cert
    if not (results["minimize"]["actual_overlap"]<=expected<=
            results["maximize"]["actual_overlap"]):
        raise AssertionError("deterministic pair does not bracket random mean")
    return {
        "slice":"HYP-105-E1-K3-G2-K",
        "left_variant":left_variant,
        "random_mean":fraction_pair(expected),
        "max_and_min_verified_all_true_W32":True,
        "all_h_construction_theorem":True,
        "universal_all_label_S_omega_proved":False,
        "all_h_S_surplus_proved":False,
        "results":results,
    }


def report():
    return {"slice":"HYP-105-E1-K3-G2-K",
            "models":{v:hosted_W32_pair(left_variant=v)
                      for v in ("lex","correlated-left")},
            "prior_art_method":"classical conditional expectation",
            "all_h_constructive_some_right_g":True,
            "all_h_universal_every_f_g":False,
            "issue_230_branch_A_B":"OPEN"}


if __name__=="__main__":
    print(json.dumps(report(),sort_keys=True,indent=2))
