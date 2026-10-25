"""Independent all-original-incidence F enumeration for D6-L directed 3-port cuts."""
import unittest
from random import Random
from itertools import combinations

from hyp105_issue230_d6l_directed_triple_calibration import (
    directed_original_triple_calibration,
    compare_original_pair_and_directed,
    finite_genuine_W32_directed_report,
)


def independent_raw_directed_deficit(sources,targets,K):
    """Brute EVERY ORIGINAL source-incidence F; no reused maxflow."""
    incidences=sorted({e for t in sources for e in t})
    N=len(incidences)
    if not N:
        return 0, []
    L={e:sum(w for t,w in sources.items() if e in t)
       for e in incidences}
    d={e:sum(e in q for q in targets) for e in incidences}
    pressure={e:2*L[e]-K*d[e] for e in incidences}
    G=sum(pressure.values())
    q={e:N*pressure[e]-G for e in incidences}
    best=0
    supports=[]
    for mask in range(1<<N):
        F={incidences[i] for i in range(N) if mask>>i&1}
        boundary=sum(len(F.intersection(t))*w
                     for t,w in sources.items()
                     if 0<len(F.intersection(t))<3)
        value=sum(q[e] for e in F)-2*N*boundary
        if value>best:
            best=value
            supports=[F]
        elif value==best:
            supports.append(F)
    return best,supports


class DirectedOriginalThreePortTests(unittest.TestCase):
    def test_independent_every_F_dual_random_and_local_upper(self):
        rng=Random(2306122)
        for i in range(48):
            sources={}
            while len(sources)<2+i%2:
                t=tuple(sorted(rng.sample(range(15),3)))
                sources[t]=rng.randint(1,4)
            targets={}
            while len(targets)<1+i%3:
                q=tuple(sorted(rng.sample(range(15),6)))
                targets[q]="synthetic"
            for K in (0,1,2,4):
                with self.subTest(case=i,K=K):
                    expect,_=independent_raw_directed_deficit(
                        sources,targets,K)
                    row=compare_original_pair_and_directed(
                        sources,targets,K)
                    directed=row["original_directed"]
                    self.assertEqual(
                        directed["directed_calibration_deficit_E"],expect)
                    self.assertLessEqual(
                        expect,row["original_pair"][
                            "centred_pair_deficit_E"])
                    self.assertLessEqual(
                        row["true_original_exact_uniform_local_excess"],
                        expect//directed["N"])
                    self.assertGreaterEqual(
                        directed["routed_q"],0)
                    self.assertEqual(
                        directed["routed_q"]+expect,
                        directed["integer_q_supply"])
                    self.check_original_triple_primal(sources,row)

    def check_original_triple_primal(self,sources,row):
        pr=row["original_directed"]
        if pr["directed_calibration_deficit_E"]!=0:
            self.assertEqual(pr["triple_primal_all_integer_ports"],[])
            return
        N=pr["N"]
        K=pr["K"]
        # Verify exact triple-level conservation and capped input flow
        # independently from the flow implementation.
        across={}
        inside={}
        for record in pr["triple_primal_all_integer_ports"]:
            t=tuple(record["source_original_triple"])
            self.assertIn(t,sources)
            x=sum(w for _,w in record["incoming_original_ports"])
            y=sum(w for _,w in record["outgoing_original_ports"])
            self.assertEqual(x,y)
            self.assertEqual(x,record["total_flow"])
            for e,w in record["incoming_original_ports"]:
                self.assertIn(e,t)
                self.assertLessEqual(w,2*N*sources[t])
                across[e]=across.get(e,0)+w
            for e,w in record["outgoing_original_ports"]:
                self.assertIn(e,t)
                inside[e]=inside.get(e,0)+w
        self.assertEqual(sum(across.values()),sum(inside.values()))

    def test_nontrivial_directional_success_when_pair_fails(self):
        # 1 original triple T weight4: L(e)=4 for e=0,1,2;
        # K=1, positive recipient degrees (0,0,17), so
        # p=(8,8,-9), N=3, G=7, q=(17,17,-34).
        # For F={0,1}, pair=2w=8 so N*pair=24<q(F)=34,
        # but directed triple cost=2*N*2*w=48 >=34.
        source={(0,1,2):4}
        targets={}
        for j in range(17):
            u=100+5*j
            targets[(2,u,u+1,u+2,u+3,u+4)]="synthetic"
        row=compare_original_pair_and_directed(source,targets,1)
        self.assertGreater(row["original_pair"]["centred_pair_deficit_E"],0)
        self.assertEqual(row["original_directed"][
            "directed_calibration_deficit_E"],0)
        self.assertEqual(row["true_original_exact_uniform_local_excess"],0)
        self.check_original_triple_primal(source,row)

    def test_directed_obstruction_and_strict_upper(self):
        # Source with one unsupported ORIGINAL triple component.
        sources={(0,1,2):3,(7,8,9):2}
        targets={(0,3,4,5,6,10):"synthetic"}
        # At K=30, global G=6*C-K*D(I)=0; the unsupported
        # disconnected source triple gives a STRICT local obstruction.
        # K=5 would instead have global G=25 and local excess zero.
        r=compare_original_pair_and_directed(sources,targets,30)
        self.assertGreater(r["original_directed"][
            "directed_calibration_deficit_E"],0)
        self.assertGreater(r["true_original_exact_uniform_local_excess"],0)
        self.assertEqual(r["original_directed"]["G"],0)
        self.assertEqual(
            r["original_directed"]["directed_calibration_deficit_E"],
            r["original_directed"]["N"]*
            r["true_original_exact_uniform_Delta6"])
        # Balanced pressure G=0 makes directed calibration EXACTLY
        # equivalent to original restricted uniform Hall, not merely
        # a one-sided sufficient bound.
        self.assertGreaterEqual(r["original_pair"]["centred_pair_deficit_E"],
                                r["original_directed"][
                                    "directed_calibration_deficit_E"])
        F=set(r["original_directed"]["dual_original_incidence_support_F"])
        self.assertTrue(F)
        self.assertEqual(
            r["original_directed"]["directed_calibration_deficit_E"],
            independent_raw_directed_deficit(sources,targets,30)[0])

    def test_zero_capacity_empty_source_validation(self):
        target={(0,1,2,3,4,5):"synthetic"}
        empty=directed_original_triple_calibration({},target,0)
        self.assertEqual(empty["directed_calibration_deficit_E"],0)
        self.assertEqual(empty["N"],0)
        one=compare_original_pair_and_directed({(0,1,2):5},{},0)
        self.assertEqual(one["true_original_exact_uniform_Delta6"],30)
        self.assertEqual(one["true_original_exact_uniform_local_excess"],0)
        with self.assertRaises(ValueError):
            directed_original_triple_calibration(
                {(0,1,2):2},target,-1)

    def test_genuine_same_map_W32_full_seven_not_BB_only(self):
        report=finite_genuine_W32_directed_report()
        self.assertEqual(report["all_h_uniform_K"],"OPEN")
        self.assertEqual(report["root_Branch_A_B"],"OPEN")
        self.assertEqual(report["W34_W38_complete_seven_S"],
                         "UNKNOWN-NO-BB-SUBSTITUTION")
        expected={
            "lex":(942,786,156,259,4,165),
            "reverse":(898,676,222,169,6,53),
            "S68":(606,544,62,68,9,62),
            "S72":(658,600,58,72,10,10),
        }
        self.assertEqual(len(report["genuine_complete_original_W32_cases"]),4)
        for x in report["genuine_complete_original_W32_cases"]:
            C,E,I,S,K,ex=expected[x["scheme"]]
            self.assertEqual(
                (x["C"],x["E"],x["I"],
                 x["S_complete_TRUE_GQ_seven_GF5_positive"],x["full_original_K"]),
                (C,E,I,S,K))
            row=x["K_minus_one"]
            self.assertEqual(row["true_original_exact_uniform_Delta6"],6*ex)
            self.assertEqual(row["true_original_exact_uniform_local_excess"],0)
            self.assertEqual(row["true_original_D6F_integer_exception"],ex)
            self.assertEqual(x["K_at_minimum"][
                "true_original_exact_uniform_Delta6"],0)
            self.assertLessEqual(row["original_directed"][
                "directed_calibration_deficit_E"],
                row["original_pair"]["centred_pair_deficit_E"])
            # Genuine GF5-positive complete-seven W32: directed ORIGINAL
            # triple calibration succeeds even where PAIR fails.
            empirical_pair={"lex":0,"reverse":0,"S68":372,"S72":1215}
            active_triples={"lex":148,"reverse":179,"S68":123,"S72":180}
            self.assertEqual(
                row["original_pair"]["centred_pair_deficit_E"],
                empirical_pair[x["scheme"]])
            self.assertEqual(
                row["original_directed"]["directed_calibration_deficit_E"],0)
            self.assertTrue(row["original_directed"][
                "certified_zero_directed_calibration_deficit"])
            self.assertEqual(
                row["original_directed"]["triple_primal_nonzero_count"],
                active_triples[x["scheme"]])


if __name__=="__main__":
    unittest.main()
