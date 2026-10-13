"""Independent acceptance gates for exact same-map JPKC ledger."""
import unittest

from hyp105_issue230_jpkc_joint_defect_gate import (
    _cycles_independent, _path3_and_theta, joint_record,
)
from hyp105_issue230_projection import fixture, ProjectionClosure


class JPKCGates(unittest.TestCase):
    def test_arbitrary_six_cycle_K2_identity_and_proper_classification(self):
        # No GQ-specific import used in either graph-only computation.
        a=6
        vertices=[i*a+i for i in range(6)]
        graph=[set() for _ in range(a*a)]
        for i in range(6):
            u,v=vertices[i],vertices[(i+1)%6]
            graph[u].add(v)
            graph[v].add(u)
        adj=tuple(frozenset(x) for x in graph)
        energy=_path3_and_theta(adj)
        direct=_cycles_independent(adj,a,max_cycles=1)
        self.assertEqual(energy["P3"],12)
        self.assertEqual(energy["Theta"],0)
        self.assertEqual(energy["C6_from_K2"],1)
        self.assertEqual((direct["C6_DFS"],direct["D6_proper_DFS"]),(1,1))

    def test_w32_all_four_true_original_map_coupling(self):
        path_ledger={
            "lex":(1346,0,400,942,4),
            "reverse":(1154,0,256,898,0),
            "S68":(678,0,72,606,0),
            "S72":(738,0,80,658,0),
        }
        for scheme, expected in path_ledger.items():
            with self.subTest(scheme=scheme):
                row=joint_record(fixture(1,scheme),seven=True)
                p=row["projection"]
                self.assertEqual(tuple(p[k] for k in (
                    "proper_P3","missing","incident","blocked","unblocked")),expected)
                self.assertTrue(row["seven_original"]["exact_D6_and_BBo_subclass_reconciled"])
                self.assertGreaterEqual(row["kikuchi"]["sum_P3_squared"],
                                        row["kikuchi"]["P3"])
                self.assertEqual(row["kikuchi"]["C6_DFS"],
                                 row["kikuchi"]["C6_from_K2"])
                self.assertTrue(row["joint"]["J2_exact_variance_identity_verified"])
                self.assertEqual(row["joint"]["J2_endpoint_variance_exact"],
                                 row["P3_Cauchy_Schwarz_slack_exact"])
                self.assertEqual(row["kikuchi"]["C6_DFS"],
                                 row["kikuchi"]["D6_proper_DFS"]+
                                 row["kikuchi"]["C6_improper_DFS"])
                self.assertGreaterEqual(int(row["joint"]["kikuchi_lower_bound_slack_exact"].split("/")[0]),0)
                self.assertFalse(row["universal_A_proved"])
        self.assertEqual(joint_record(fixture(1,"S68"),seven=True)["seven_original"]["S"],68)
        self.assertEqual(joint_record(fixture(1,"S72"),seven=True)["seven_original"]["S"],72)

    def test_w32_K1_independent_numerical_pins(self):
        for scheme,p3,theta,c6,d6 in [
            ("lex",3846,5476,730,15),
            ("reverse",3300,3316,485,3),
        ]:
            with self.subTest(scheme=scheme):
                row=joint_record(fixture(1,scheme),seven=True)
                k=row["kikuchi"]
                self.assertEqual((k["P3"],k["Theta"],k["C6_DFS"],
                                  k["D6_proper_DFS"]),(p3,theta,c6,d6))
                self.assertEqual(k["sum_P3_squared"],p3+theta+12*c6)

    def test_w34_full_GQ_lex_energy_and_direct_C6(self):
        row=joint_record(fixture(2,"lex"),seven=False,max_cycles=100_000)
        p,k=row["projection"],row["kikuchi"]
        self.assertEqual((p["proper_P3"],p["missing"],p["incident"],
                          p["blocked"],p["unblocked"]),
                         (83892,8860,4584,55384,15064))
        self.assertEqual((k["P3"],k["Theta"],k["C6_DFS"],k["D6_proper_DFS"]),
                         (132644,127684,37320,8481))
        self.assertEqual(k["C6_from_K2"],k["C6_DFS"])

    def test_w34_global_random_injection_no_mixed_fixtures(self):
        row=joint_record(fixture(2,"random"),seven=False,max_cycles=100_000)
        p,k=row["projection"],row["kikuchi"]
        self.assertEqual((p["proper_P3"],p["missing"],p["incident"],
                          p["blocked"],p["unblocked"]),
                         (78894,10198,4112,48542,16042))
        self.assertEqual(k["C6_from_K2"],k["C6_DFS"])
        self.assertGreaterEqual(k["C6_DFS"],k["D6_proper_DFS"])

    def test_original_symplectic_spread_W34_joint_adversarial_gate(self):
        from hyp105_issue230_jpkc_spread_adversary import spread_adversary_model
        model,cert=spread_adversary_model(2)
        self.assertEqual(cert["s"],4)
        self.assertGreaterEqual(cert["M_f_original_exact"],cert["M_f_D4_floor"])
        self.assertEqual(cert["M_f_D4_floor"],30)
        row=joint_record(model,max_cycles=1_000_000)
        self.assertEqual(row["kikuchi"]["C6_DFS"],row["kikuchi"]["C6_from_K2"])
        self.assertEqual(row["s"],4)
        self.assertTrue(row["global_injections_both_sides"])
        self.assertFalse(row["joint"]["finite_JPKC_dichotomy_proved"])

    def test_original_symplectic_spread_W38_graph_energy_stress(self):
        # W38 full projected path census may exceed its independent path
        # budget on an adversarial star; do NOT report it as a completed
        # JPKC classification or a seven-family exact census.
        from hyp105_issue230_jpkc_spread_adversary import spread_adversary_model
        from hyp105_issue230_jpkc_joint_defect_gate import _graph
        model,cert=spread_adversary_model(3)
        self.assertEqual(cert["s"],8)
        self.assertEqual(cert["M_f_D4_floor"],288)
        ctx=ProjectionClosure(model)
        graph=_graph(ctx)
        k=_path3_and_theta(graph)
        self.assertGreaterEqual(k["C6_from_K2"],0)
        self.assertEqual(k["sum_P3_squared"],
                         k["P3"]+k["Theta"]+12*k["C6_from_K2"])

    def test_fail_closed_and_no_fake_global_proof(self):
        ctx=ProjectionClosure(fixture(1,"lex"))
        with self.assertRaisesRegex(ValueError,"direct C6 budget"):
            _cycles_independent(tuple(frozenset(v for v,_ in row)
                                      for row in ctx.adj),ctx.a,max_cycles=0)
        row=joint_record(fixture(1,"S68"),seven=True)
        self.assertFalse(row["joint"]["finite_JPKC_dichotomy_proved"])
        self.assertFalse(row["counterexample_B_proved"])
        with self.assertRaisesRegex(ValueError,"W32"):
            joint_record(fixture(2,"lex"),seven=True)


if __name__=="__main__":
    unittest.main()
