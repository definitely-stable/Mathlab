"""Independent original GQ physical owner-ports versus prior adjacency census."""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
import unittest

from hyp105_original_three_owner_joint_ports_referee import (
    SCHEMA,ROOT_STATUS,CASES,_real_source_directed_port_books,
    _genuine_middle_diagonal_orientations,_joint_original_three_owner_ports,
    _true_original_joint_middle_moment,canonical_report
)
from hyp105_original_full_w34_weighted_risk_referee import (
    _source,_true_original_proper_P3,_rank_probability3
)
from hyp105_original_symbol_secondmoments_referee import (
    _full_exact_symbol_moments_one_bin
)


class TestOriginalJointThreeOwnerSource(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report=canonical_report()

    def test_scope_and_complete_fixed_source_census(self):
        z=self.report
        self.assertEqual(z["schema"],SCHEMA)
        self.assertEqual(z["issue"],230)
        self.assertEqual(z["status"],ROOT_STATUS)
        self.assertFalse(z["all_h_ROOT_seven_motif_sixset_theorem_proved"])
        self.assertFalse(z["ASET_exponent_claimed"])
        rows=z["actual_genuine_W32_W34_cases"]
        self.assertEqual([(r["s"],r["scheme"],r["CORE"]) for r in rows],list(CASES))
        self.assertEqual([r["real_original_directed_proper_P3s"] for r in rows],
                         [1346,1154,838,83892,82846,79404,9966,66418])

    def test_all_eight_source_exact_envelopes_and_risk_conservation(self):
        for row in self.report["actual_genuine_W32_W34_cases"]:
            M=Fraction(row["exact_original_M"])
            G=Fraction(row["exact_original_G"])
            B=Fraction(row["exact_original_B"])
            LH=Fraction(row["original_Harris_lower_M"])
            MU=Fraction(row["original_priority_degree_upper_M"])
            MN=Fraction(row["original_rankless_P3_count_square_upper_M"])
            GL=Fraction(row["original_Harris_lower_positive_compatible_G"])
            self.assertEqual(M,G+B)
            self.assertTrue(0<GL<=G<=M)
            self.assertTrue(0<LH<=M<=MU<=MN)
            self.assertLessEqual(B/M,1-GL/MU)
            self.assertTrue(row["all_h_exact_SOURCE_three_owner_joint_port_contraction"])
            self.assertTrue(row["all_h_Harris_product_lower_and_degree_minimum_upper"])
            self.assertFalse(row["root_PROVED_A"])

    def test_shared_external_original_neighbor_exact_probability_not_product(self):
        # Three J-independent ORIGINAL owners 0,1,2 share outsider 3.
        J=[{3},{3},{3},{0,1,2}]
        pi=_rank_probability3((0,1,2),J)
        self.assertEqual(pi,Fraction(1,4))
        self.assertNotEqual(pi,Fraction(1,2)**3)
        self.assertTrue(Fraction(1,8)<=pi<=Fraction(1,2))
        # Three distinct outside neighbors: independent priority tests here.
        J2=[{3},{4},{5},{0},{1},{2}]
        self.assertEqual(_rank_probability3((0,1,2),J2),Fraction(1,8))

    def test_complete_original_port_edges_are_owned_no_clones(self):
        for s,scheme,core in CASES:
            c=_source(s,scheme,core)
            inc,out=_real_source_directed_port_books(c)
            self.assertEqual(sum(map(len,inc.values())),4*len(c["ids"]))
            self.assertEqual(sum(map(len,out.values())),4*len(c["ids"]))
            for i in c["ids"]:
                self.assertEqual(len(tuple(_genuine_middle_diagonal_orientations(c,i))),4)
            for vertex,ports in inc.items():
                for other,owner in ports:
                    edge=(other,vertex) if other<vertex else (vertex,other)
                    self.assertEqual(c["owner"][edge],owner)

    def test_new_original_middle_join_vs_inherited_independent_physical_walker(self):
        # All paths and all three real source owners, not just a path count.
        for case in (CASES[0],CASES[1],CASES[2],CASES[3]):
            c=_source(*case)
            bins,_=_joint_original_three_owner_ports(c)
            new={(path,owners) for group in bins.values()
                 for path,owners,*_ in group}
            ref=set(_true_original_proper_P3(c))
            self.assertEqual(new,ref)
            self.assertEqual(sum(map(len,bins.values())),len(ref))
            self.assertEqual(len(new),len(ref))

    def test_independent_prior_symbol_moments_exact_fraction_crosscheck(self):
        # Independent inherited source moment implementation versus new one.
        for case in (CASES[0],CASES[1],CASES[2],CASES[3]):
            c=_source(*case)
            bins,_=_joint_original_three_owner_ports(c)
            for ends in sorted(bins)[:30]:
                group=bins[ends]
                new=_true_original_joint_middle_moment(group,c,2)
                old=_full_exact_symbol_moments_one_bin(
                    [(path,owners,w) for path,owners,w,*_ in group],c)
                for name in ("M","G","B","D","G00","G11_tail","G11_head"):
                    self.assertEqual(new[name],old[name],(case,ends,name))

    def test_actual_original_priority_weights_independent_owner_oracle(self):
        for case in (CASES[0],CASES[2],CASES[3]):
            c=_source(*case)
            bins,_=_joint_original_three_owner_ports(c)
            for group in list(bins.values())[:40]:
                for path,owners,w,lower,upper in group:
                    self.assertEqual(w,_rank_probability3(owners,c["J"])/64)
                    self.assertTrue(0<lower<=w<=upper<=Fraction(1,64))
                    self.assertEqual(len({z[0] for z in path}),4)
                    self.assertEqual(len({z[1] for z in path}),4)
                    self.assertTrue(all(
                        j not in c["J"][i] for i,j in combinations(owners,2)))


if __name__=="__main__":
    unittest.main()
