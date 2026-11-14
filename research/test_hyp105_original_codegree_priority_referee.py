"""Independent source rank/permutation and real GQ W32/W34 codegree falsifiers."""
from fractions import Fraction
from itertools import permutations, combinations
import unittest

from hyp105_original_codegree_priority_referee import (
    SCHEMA,ROOT_STATUS,CASES,_exact_original_pair_local_minimum,
    _original_three_owner_codegree_selector_envelope,canonical_report
)
from hyp105_original_full_w34_weighted_risk_referee import (
    _source,_rank_probability3
)
from hyp105_original_three_owner_joint_ports_referee import (
    _joint_original_three_owner_ports
)


def _independent_synthetic_original_J(masks):
    """Owner 0,1,2 independent; each outsider has an exact owner subset."""
    J=[set() for _ in range(3+len(masks))]
    for k,mask in enumerate(masks,3):
        if not 1<=mask<=7:
            raise ValueError("nonempty owner-neighbor mask required")
        for i in range(3):
            if mask&(1<<i):
                J[i].add(k);J[k].add(i)
    return J


def _literal_uniform_priority_permutation_event(owners,J):
    """Completely independent finite permutation oracle, no integrals."""
    active=sorted(set(owners).union(*(J[i] for i in owners)))
    good=0
    total=0
    for perm in permutations(active):
        at={v:k for k,v in enumerate(perm)}
        total+=1
        if all(all(at[i]<at[j] for j in J[i]) for i in owners):
            good+=1
    return Fraction(good,total)


class TestOriginalSourceCodegreePriority(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report=canonical_report()

    def test_root_scope_and_eight_complete_true_original_source_censuses(self):
        cert=self.report
        self.assertEqual(cert["schema"],SCHEMA)
        self.assertEqual(cert["status"],ROOT_STATUS)
        self.assertEqual(cert["issue"],230)
        for key in ("all_h_ROOT_seven_motif_obstruction_proved",
                    "all_h_strict_global_B75_all_fixed_correlated_maps_proved",
                    "ASET_exponent_claimed"):
            self.assertFalse(cert[key])
        rows=cert["eight_complete_genuine_original_source_cases"]
        self.assertEqual([(r["s"],r["scheme"],r["retained_original_CORE"])
                          for r in rows],list(CASES))
        self.assertEqual([r["counts"]["real_proper_source_threepaths"]
                          for r in rows],
                         [1346,1154,838,83892,82846,79404,9966,66418])

    def test_pair_probability_independent_brute_uniform_all_local_orders(self):
        for masks in ([1,2,4],[7],[3,5],[1,2,3],[1,2,3,4,7],
                      [7,7],[3,5,6],[1,4,6,7]):
            J=_independent_synthetic_original_J(masks)
            for i,j in combinations((0,1,2),2):
                exact=_exact_original_pair_local_minimum(i,j,J)
                independent=_literal_uniform_priority_permutation_event((i,j),J)
                self.assertEqual(exact,independent,(masks,i,j))
                self.assertEqual(exact,_exact_original_pair_local_minimum(j,i,J))

    def test_all_synthetic_triple_common_priority_events_independently(self):
        for masks in ([1,2,4],[7],[3,5],[1,2,3],[7,7],
                      [3,5,6],[1,4,6,7]):
            J=_independent_synthetic_original_J(masks)
            lo,hi,disjoint=_original_three_owner_codegree_selector_envelope((0,1,2),J)
            via_original_rank=_rank_probability3((0,1,2),J)/64
            via_independent_permutation=(
                _literal_uniform_priority_permutation_event((0,1,2),J)/64)
            self.assertEqual(via_original_rank,via_independent_permutation)
            self.assertLessEqual(lo,via_original_rank)
            self.assertLessEqual(via_original_rank,hi)
            self.assertEqual(disjoint,all(
                not J[i].intersection(J[j]) for i,j in combinations((0,1,2),2)))
            if disjoint:
                self.assertEqual(lo,hi)
                self.assertEqual(hi,via_original_rank)

    def test_shared_single_outsider_strict_improvement_not_independent(self):
        J=_independent_synthetic_original_J([7])
        self.assertEqual(_exact_original_pair_local_minimum(0,1,J),
                         Fraction(1,3))
        lo,hi,disjoint=_original_three_owner_codegree_selector_envelope(
            (0,1,2),J)
        self.assertFalse(disjoint)
        self.assertEqual(lo,Fraction(1,6*64))
        self.assertEqual(hi,Fraction(1,3*64))
        self.assertEqual(_rank_probability3((0,1,2),J)/64,Fraction(1,4*64))
        self.assertGreater(lo,Fraction(1,8*64))
        self.assertLess(hi,Fraction(1,2*64))

    def test_three_disjoint_outsider_neighborhoods_exact_product(self):
        J=_independent_synthetic_original_J([1,2,4])
        lo,hi,disjoint=_original_three_owner_codegree_selector_envelope(
            (0,1,2),J)
        self.assertTrue(disjoint)
        self.assertEqual(lo,hi)
        self.assertEqual(lo,Fraction(1,8*64))

    def test_invalid_owner_adjacent_or_identical_refused(self):
        J=_independent_synthetic_original_J([3])
        with self.assertRaises(ValueError):
            _exact_original_pair_local_minimum(0,0,J)
        J[0].add(1);J[1].add(0)
        with self.assertRaises(ValueError):
            _exact_original_pair_local_minimum(0,1,J)
        with self.assertRaises(ValueError):
            _original_three_owner_codegree_selector_envelope((0,1,2),J)

    def test_all_eight_full_genuine_source_exact_B75_and_nesting(self):
        for row in self.report["eight_complete_genuine_original_source_cases"]:
            M=Fraction(row["exact_original_M"])
            G=Fraction(row["exact_original_G"])
            B=Fraction(row["exact_original_B"])
            gold=Fraction(row["original_Harris_lower_G_old"])
            gnew=Fraction(row["original_CODEGREE_lower_G_new"])
            uold=Fraction(row["original_singleton_degree_M_upper_old"])
            unew=Fraction(row["original_CODEGREE_M_upper_new"])
            urankless=Fraction(row["original_rankless_M_upper"])
            mnewlow=Fraction(row["original_CODEGREE_M_lower_new"])
            old_cert=Fraction(row["old_common_original_B_over_M_upper"])
            new_cert=Fraction(row["new_CODEGREE_common_original_B_over_M_upper"])
            self.assertEqual(M,G+B)
            self.assertTrue(0<gold<=gnew<=G<=M<=unew<=uold<=urankless)
            self.assertTrue(0<mnewlow<=M)
            self.assertTrue(B/M<=new_cert<=old_cert<1)
            self.assertEqual(row["M_upper_STRICT_improvement_over_parent"],unew<uold)
            self.assertEqual(row["G_lower_STRICT_improvement_over_parent"],gnew>gold)
            self.assertEqual(row["codegree_certified_strict_global_B75"],4*gnew>unew)
            self.assertFalse(row["root_PROVED_A"])

    def test_true_original_three_owner_priority_bound_against_actual_path(self):
        # Independent true W32 source triples, not a synthetic pair-edge host.
        c=_source(2,"reverse","full")
        bins,_=_joint_original_three_owner_ports(c)
        cache={}
        triples=0
        for group in bins.values():
            for path,owners,w,old_lo,old_up in group:
                key=tuple(sorted(owners))
                if key not in cache:
                    cache[key]=_original_three_owner_codegree_selector_envelope(
                        key,c["J"])
                lo,hi,disjoint=cache[key]
                self.assertTrue(old_lo<=lo<=w<=hi<=old_up)
                if disjoint:
                    self.assertEqual(lo,w)
                    self.assertEqual(w,hi)
                triples+=1
        self.assertEqual(triples,1154)


if __name__=="__main__":
    unittest.main()
