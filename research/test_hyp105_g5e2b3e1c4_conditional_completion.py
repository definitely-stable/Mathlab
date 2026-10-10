"""HYP-105 C4 independent original-incidence, target, and permutation falsifiers."""
from collections import Counter
from fractions import Fraction
from itertools import combinations,permutations,product
from math import comb
import unittest

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_g5e2b3e1a_fixed_leading import (
    _two_factors_K6, validated_small_model,
)
from hyp105_g5e2b3e1c0_weighted_overlap import (
    simple_six_2factor_targets, source_weighted_BA_hypergraph,
    exact_BA_overlap,
)
from hyp105_g5e2b3e1c4_conditional_completion import (
    occupied_target_residuals, original_W32_conditional_source,
    pair_frozen_moment_certificate,evaluate_conditional_tensor,
    occupied_disjoint_triangle_completion_lower,all_h_pairwise_random_benchmark_lower,
)


def independently_brute_target(a,occupied,pair):
    """No call to C4 templated target generator: all physical 6-edge sets."""
    anchor=frozenset(pair)
    target=set()
    for S in combinations(occupied,6):
        degrees=Counter(v for edge in S for v in edge)
        if len(degrees)==6 and all(d==2 for d in degrees.values()):
            S=frozenset(S)
            if anchor<=S:
                target.add(S-anchor)
    return frozenset(target)


def independently_brute_original_point_cycle_source(model):
    """C4-independent complete original incidence by doubled ORIGINAL point.

    Uses C4s on the four OTHER physical coordinates and incidence neighbor
    products, not the C4 actual selected_left_six production enumerator.
    """
    physical,_,edges,_=validated_small_model(model)
    point_by_physical={edge:i for i,edge in enumerate(physical)}
    incidence=[set() for _ in physical]
    for p,l in edges:
        incidence[p].add(l)
    tensor={}
    count=0
    for p,edge in enumerate(physical):
        remaining=tuple(x for x in range(6) if x not in edge)
        for square in combinations(tuple(combinations(remaining,2)),4):
            if any(sum(x in e for e in square)!=2 for x in remaining):
                continue
            singles=[point_by_physical[e] for e in square]
            for uv in combinations(sorted(incidence[p]),2):
                for rest in product(*(sorted(incidence[q]) for q in singles)):
                    count+=1
                    if len(set(uv+rest))!=6:
                        continue
                    P=frozenset(uv)
                    H=frozenset(rest)
                    tensor.setdefault(P,Counter())[H]+=1
    if count!=10935:
        raise AssertionError("independent B-source candidate count changed")
    return tensor


def independent_incidence_full_BA_count(tensor,labels,a):
    total=0
    for P,rows in tensor.items():
        for H,w in rows.items():
            six=tuple(labels[i] for i in P|H)
            degrees=Counter(c for e in six for c in e)
            if len(degrees)==6 and set(degrees.values())=={2}:
                total+=w
    return total


class ConditionalFourLineTests(unittest.TestCase):
    def test_physical_completion_oracle_K6_all_105_anchor_pairs(self):
        physical=tuple(combinations(range(6),2))
        counts=Counter()
        for pair in combinations(physical,2):
            actual,q=occupied_target_residuals(6,physical,pair)
            expected=independently_brute_target(6,physical,pair)
            self.assertEqual(actual,expected)
            shape="adjacent" if set(pair[0])&set(pair[1]) else "disjoint"
            self.assertEqual(len(actual),7 if shape=="adjacent" else 14)
            self.assertEqual(q,len(actual))
            counts[shape]+=1
        self.assertEqual(counts,{"adjacent":60,"disjoint":45})
        self.assertEqual(
            sum(len(independently_brute_target(6,physical,p))
                for p in combinations(physical,2)),
            70*15)

    def test_occupied_vs_full_target_and_missing_star_limit(self):
        all_pairs=tuple(combinations(range(6),2))
        target=tuple(_two_factors_K6())[0]
        base=next((p,q) for p,q in combinations(target,2)
                  if not set(p)&set(q))
        F=tuple(base)+tuple(x for x in target if x not in base)
        F+=tuple(e for e in all_pairs if e not in F)[:2]
        self.assertEqual(len(F),8)
        for p in combinations(F,2):
            got,q=occupied_target_residuals(6,F,p)
            self.assertEqual(got,independently_brute_target(6,F,p))
            self.assertLessEqual(len(got),q)
        # The C3 relaxed full-K_a completion can FAIL entirely within
        # the occupied pair-label image: an endpoint has physical degree 1.
        a=7
        occupied=tuple(e for e in combinations(range(a),2)
                       if 0 not in e or e==(0,1))
        isolated_anchor=((0,1),(2,3))
        got,q=occupied_target_residuals(a,occupied,isolated_anchor)
        self.assertEqual(q,14*comb(a-4,2))
        self.assertEqual(len(got),0)
        self.assertEqual(got,independently_brute_target(a,occupied,isolated_anchor))
        self.assertEqual(comb(a,2)-len(occupied),a-2)

    def test_constructive_occupied_two_triangle_subfamily_all_K6_disjoint(self):
        physical=tuple(combinations(range(6),2))
        for pair in combinations(physical,2):
            if set(pair[0])&set(pair[1]):
                continue
            cert=occupied_disjoint_triangle_completion_lower(6,physical,pair)
            q,_=occupied_target_residuals(6,physical,pair)
            self.assertEqual(cert["two_triangle_occupied_completion_count"],2)
            self.assertEqual(cert["uniform_missing_budget_lower"],2)
            self.assertLessEqual(cert["two_triangle_occupied_completion_count"],len(q))
        # Adversarial occupancy from the independent full brute target:
        a=7
        all_edges=tuple(combinations(range(a),2))
        pair=((0,1),(2,3))
        for removed in (
            (),((0,4),),((0,4),(0,5),(0,6)),
            tuple((0,j) for j in range(2,a)),
        ):
            F=tuple(e for e in all_edges if e not in removed)
            got=occupied_disjoint_triangle_completion_lower(a,F,pair)
            Q,_=occupied_target_residuals(a,F,pair)
            self.assertLessEqual(got["uniform_missing_budget_lower"],len(Q))
            self.assertLessEqual(got["two_triangle_occupied_completion_count"],len(Q))
            if len(removed)==a-2:
                self.assertEqual(len(Q),0)
                self.assertEqual(got["two_triangle_occupied_completion_count"],0)

    def test_all_h_pairwise_benchmark_strictly_not_global_overlap(self):
        for s in (2,4,8,16,32,64,128,256,512,1024):
            c=all_h_pairwise_random_benchmark_lower(s)
            L=max(0,c["a"]-4-c["physical_missing_t"])
            self.assertEqual(c["all_disjoint_anchors_occupied_completion_lower"],
                             L*(L-1) if L>=2 else 0)
            self.assertEqual(c["pairwise_frozen_bijection_benchmark_lower"],
                Fraction(
                    c["all_correlated_disjoint_original_witness_mass_lower"]
                    *c["all_disjoint_anchors_occupied_completion_lower"],
                    comb(c["V"]-2,4)))
            self.assertFalse(c["bound_is_global_deterministic_BA_overlap"])
            if s>=16 and L>=2:
                self.assertGreater(c["pairwise_frozen_bijection_benchmark_lower"],0)
        for bad in (1,3,True):
            with self.assertRaises(ValueError):
                all_h_pairwise_random_benchmark_lower(bad)

    def test_exact_genuine_W32_original_conditional_tensor_and_105_swaps(self):
        for scheme in ("lex","reverse-line"):
            model=pair_labeled_symplectic(1,scheme)
            actual=original_W32_conditional_source(model)
            alternate=independently_brute_original_point_cycle_source(model)
            self.assertEqual(actual,alternate)
            self.assertEqual(sum(map(sum,(r.values() for r in actual.values()))),5000)
            self.assertEqual(len(actual),45)
            labels=tuple(model["right_labels"])
            original_source=source_weighted_BA_hypergraph(model)
            variants=((None,)+tuple(combinations(range(15),2))
                      if scheme=="reverse-line" else (None,))
            positive_zero=0
            for swap in variants:
                physical=list(labels)
                if swap is not None:
                    i,j=swap
                    physical[i],physical[j]=physical[j],physical[i]
                cert=evaluate_conditional_tensor(actual,physical,a=6)
                direct=independent_incidence_full_BA_count(actual,physical,6)
                self.assertEqual(
                    cert["actual_complete_six_edge_BA_overlap"],direct)
                self.assertEqual(direct,exact_BA_overlap(original_source,physical))
                self.assertEqual(cert["source_mass"],5000)
                self.assertEqual(cert["original_distinguished_pairs"],45)
                self.assertEqual(
                    cert["pairwise_conditioned_benchmarks_sum"]
                    +cert["pairwise_conditioned_discrepancy_sum"],direct)
                self.assertEqual(cert["relaxed_occupied_two_label_completion_weight"],
                    sum(v["mass"]*v["occupied_target_two_label_codegree"]
                        for v in cert["pairs"].values()))
                positive_zero+=bool(cert["pairs_with_available_completion_but_zero_actual"])
                if swap is None and scheme=="reverse-line":
                    self.assertEqual(direct,77)
                if swap==(4,13):
                    self.assertEqual(direct,57)
            self.assertGreater(positive_zero,0)

    def test_frozen_pair_random_bijection_first_second_moments_by_720_perms(self):
        # Genuine physical K6 2factor plus two extra occupied pair labels,
        # eight ORIGINAL vertices, pair P={0,1}, six remaining permutation.
        all_pairs=tuple(combinations(range(6),2))
        T=_two_factors_K6()[0]
        base=next((p,q) for p,q in combinations(T,2) if not set(p)&set(q))
        labels=list(base)+[e for e in T if e not in base]
        labels.extend([e for e in all_pairs if e not in T][:2])
        self.assertEqual(len(labels),8)
        completions,full=occupied_target_residuals(6,labels,base)
        self.assertGreaterEqual(len(completions),1)
        rows=Counter({
            frozenset((2,3,4,5)):2,
            frozenset((2,3,4,6)):3,
            frozenset((2,4,6,7)):1,
            frozenset((3,4,5,7)):2,
        })
        cert=pair_frozen_moment_certificate(
            rows,8,completions,retain_overlap_counts=True)
        vals=[]
        for perm in permutations(labels[2:]):
            image={i:perm[i-2] for i in range(2,8)}
            values=sum(w for H,w in rows.items()
                       if frozenset(image[i] for i in H) in completions)
            vals.append(values)
        self.assertEqual(len(vals),720)
        self.assertEqual(Fraction(sum(vals),len(vals)),
                         cert["conditional_random_mean"])
        self.assertEqual(Fraction(sum(x*x for x in vals),len(vals)),
                         cert["conditional_random_second_moment"])
        self.assertEqual(Fraction(sum((Fraction(x)-cert["conditional_random_mean"])**2
                                      for x in vals),len(vals)),
                         cert["conditional_random_variance"])
        self.assertEqual(sum(cert["ordered_source_pair_overlap_mass"]),
                         sum(rows.values())**2)
        self.assertEqual(sum(cert["ordered_target_completion_pair_overlap_count"]),
                         len(completions)**2)

    def test_Cauchy_certificate_is_exact_and_not_a_fake_lower(self):
        model=pair_labeled_symplectic(1,"reverse-line")
        x=evaluate_conditional_tensor(
            original_W32_conditional_source(model),model["right_labels"],
            a=6,include_random_second_moments=True)
        for entry in x["pairs"].values():
            err=entry["exact_conditional_discrepancy"]
            self.assertLessEqual(err*err,
                entry["deterministic_error_squared_upper"])
            if entry["deterministic_positive_overlap_sufficient"]:
                self.assertGreater(entry["actual_six_edge_completions"],0)
        self.assertFalse(x["universal_s6_lower_proved"])
        self.assertTrue(x["not_a_joint_randomization"])

    def test_invalid_occupied_sets_and_tensor_fail_closed(self):
        labels=tuple(combinations(range(6),2))
        p=(labels[0],labels[1])
        for wrong in ((labels[0],labels[0]),(labels[0],(0,6))):
            with self.assertRaises(ValueError):
                occupied_target_residuals(6,labels,wrong)
        with self.assertRaises(ValueError):
            occupied_target_residuals(6,labels+(labels[0],),p)
        with self.assertRaises(ValueError):
            evaluate_conditional_tensor({frozenset((0,1)):Counter({frozenset((0,2,3,4)):1})},labels)
        with self.assertRaises(ValueError):
            pair_frozen_moment_certificate({},5,())


if __name__=="__main__":
    unittest.main()
