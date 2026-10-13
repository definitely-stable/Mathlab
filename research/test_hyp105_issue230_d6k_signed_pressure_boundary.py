"""D6-K finite falsifiers independent of Dinic for exact pressure-boundary cuts."""
from itertools import combinations
from random import Random
import unittest

from hyp105_issue230_d6k_signed_pressure_boundary import (
    original_signed_pressure_boundary,
    signed_pressure_global_certificate,
    genuine_complete_W32_pressure_report,
)


def independent_signed_cut(source, accepted, K, F):
    """Direct scan of originals; no pressure, flow, or projection code reused."""
    inside=sum(w for T,w in source.items() if all(e in F for e in T))
    ports=sum(sum(e in F for e in Q) for Q in accepted)
    return 6*inside-K*ports


def independent_crossings(source, F):
    """Two independent direct original triple counts for orientation and pairs."""
    oriented=sum(w*len(set(T)&F) for T,w in source.items()
                 if 0<len(set(T)&F)<3)
    pair=sum(w for T,w in source.items()
             for a,b in combinations(T,2) if (a in F)!=(b in F))
    return oriented,pair


class SignedPressureBoundaryTests(unittest.TestCase):
    def test_every_original_incidence_subset_small_random_oracle(self):
        rng=Random(230611)
        for i in range(24):
            source={}
            while len(source)<2+i%2:
                T=tuple(sorted(rng.sample(range(13),3)))
                source[T]=1+rng.randrange(3)
            six={}
            while len(six)<1+i%3:
                Q=tuple(sorted(rng.sample(range(13),6)))
                six[Q]="synthetic-six"
            active=sorted({e for T in source for e in T})
            for K in (0,1,3):
                best=0
                for mask in range(1<<len(active)):
                    F={active[j] for j in range(len(active)) if mask>>j&1}
                    with self.subTest(i=i,K=K,mask=mask):
                        oracle=independent_signed_cut(source,six,K,F)
                        row=original_signed_pressure_boundary(source,six,K,F)
                        self.assertEqual(row["six_M_minus_K_D"],oracle)
                        self.assertEqual(
                            row["signed_vertex_pressure_sum"]-
                            2*row["original_partial_source_boundary"],oracle)
                        crossing,pairs=independent_crossings(source,F)
                        self.assertEqual(row["original_partial_source_boundary"],
                                         crossing)
                        self.assertEqual(row["original_pair_projection_cut_weight"],
                                         pairs)
                        self.assertLessEqual(pairs,2*crossing)
                        best=max(best,oracle)
                result=signed_pressure_global_certificate(source,six,K)
                self.assertEqual(
                    result["uniform_exact_scaled_Hall_deficit_Delta6"],best)
                self.assertGreaterEqual(
                    result["uniform_exception_upper_floor_Delta6_div6"],
                    result["exact_D6F_full_original_exception_mass"])

    def test_pressure_variance_tree_gate_is_nontrivial_with_positive_vertex(self):
        # One weighted original source triple, strongly connected pair graph,
        # but a *positive* p_K(e). The pointwise D6-H gate fails;
        # rigorous graph cut expansion still proves ZERO local Hall excess.
        source={(0,1,2):4}
        accepted={}
        for e,n in ((0,7),(1,9),(2,8)):
            for j in range(n):
                base=10000+1000*e+5*j
                accepted[(e,base,base+1,base+2,base+3,base+4)]="synthetic"
        case=signed_pressure_global_certificate(source,accepted,1)
        self.assertEqual(case["active_original_incidence_N"],3)
        self.assertEqual(case["global_signed_pressure_G"],0)
        self.assertEqual(case["signed_pressure_variance_numerator_v"],6)
        self.assertEqual(case["certified_maximum_spanning_tree_bottleneck_b"],4)
        self.assertTrue(case["spectral_tree_global_only_Hall_deficit_CERTIFIED"])
        self.assertTrue(case["calibrated_pair_flow_global_only_Hall_deficit_CERTIFIED"])
        self.assertEqual(case["positive_source_incidence_pressure_count"],1)
        self.assertEqual(case["negative_source_incidence_pressure_count"],1)
        self.assertEqual(case["uniform_exact_scaled_Hall_deficit_Delta6"],0)
        self.assertEqual(case["exact_D6F_full_original_exception_mass"],0)

    def test_global_positive_boundary_circularity_and_local_obstruction(self):
        # One original accepted Q has five ports not shared by any source:
        # D(I)=1, NOT 6*S. Claims D(I)=6*S require full target support.
        source={(0,1,2):3}
        accepted={(0,3,4,5,6,7):"synthetic"}
        info=signed_pressure_global_certificate(source,accepted,1)
        self.assertEqual(info["positive_target_port_degree_sum_all_original"],6)
        self.assertEqual(info["positive_port_degree_sum_on_active_source_I"],1)
        self.assertEqual(info["positive_port_memberships_outside_active_source_I"],5)
        self.assertEqual(info["global_signed_pressure_G"],17)
        self.assertEqual(info["uniform_exact_scaled_Hall_deficit_Delta6"],17)
        self.assertEqual(info["exact_D6F_full_original_exception_mass"],2)

        # Overall K*S>C but an ORIGINAL source component is unsupported.
        second={(0,1,2):3,(20,21,22):2}
        six={(0,3,4,5,6,7):"synthetic",
             (0,8,9,10,11,12):"synthetic"}
        fail=signed_pressure_global_certificate(second,six,10)
        self.assertGreater(fail["exact_local_Hall_excess_over_global_source_pressure"],0)
        self.assertFalse(fail["spectral_tree_global_only_Hall_deficit_CERTIFIED"])
        self.assertFalse(fail["calibrated_pair_flow_global_only_Hall_deficit_CERTIFIED"])
        self.assertGreater(fail["centred_pair_pressure_calibration"][
            "failed_pair_cut_witness"]["exact_positive_pair_cut_shortfall"],0)
        self.assertEqual(fail["exact_D6F_full_original_exception_mass"],2)

    def test_centred_pair_flux_independent_divergence_and_bipartite_cut(self):
        rng=Random(230612)
        for i in range(32):
            sources={}
            while len(sources)<2+i%2:
                T=tuple(sorted(rng.sample(range(14),3)))
                sources[T]=rng.randint(1,5)
            six={}
            while len(six)<1+i%3:
                Q=tuple(sorted(rng.sample(range(14),6)))
                six[Q]="synthetic"
            K=i%5
            result=signed_pressure_global_certificate(sources,six,K)
            calibration=result["centred_pair_pressure_calibration"]
            active=sorted({e for T in sources for e in T})
            n=len(active)
            loads={e:sum(w for T,w in sources.items() if e in T)
                   for e in active}
            degrees={e:sum(e in Q for Q in six) for e in active}
            pressure={e:2*loads[e]-K*degrees[e] for e in active}
            G=sum(pressure.values())
            q={e:n*pressure[e]-G for e in active}
            if calibration["feasible"]:
                divergence={e:0 for e in active}
                for u,v,g,cap in calibration["centred_signed_edge_flux"]:
                    self.assertLessEqual(abs(g),cap)
                    self.assertEqual(cap,n*sum(
                        w for T,w in sources.items() if u in T and v in T))
                    divergence[u]+=g
                    divergence[v]-=g
                self.assertEqual(divergence,q)
                self.assertEqual(
                    result["exact_local_Hall_excess_over_global_source_pressure"],0)
            else:
                w=calibration["failed_pair_cut_witness"]
                F=set(w["original_incidence_support_F"])
                count=sum(q[e] for e in F)
                pair=sum(v for T,v in sources.items()
                         for u,t in combinations(T,2)
                         if (u in F)!=(t in F))
                self.assertEqual(count,w["sum_centred_integer_pressure"])
                self.assertEqual(pair,w["original_pair_cut_weight"])
                self.assertEqual(count-n*pair,
                                 w["exact_positive_pair_cut_shortfall"])
                self.assertGreater(count-n*pair,0)

    def test_empty_sources_zero_capacity_and_strict_input_validation(self):
        self.assertEqual(signed_pressure_global_certificate(
            {},{(0,1,2,3,4,5):"synthetic"},0)[
            "uniform_exact_scaled_Hall_deficit_Delta6"],0)
        src={(0,1,2):2}
        self.assertEqual(signed_pressure_global_certificate(src,{},0)[
            "uniform_exact_scaled_Hall_deficit_Delta6"],12)
        with self.assertRaises(ValueError):
            signed_pressure_global_certificate(src,{},-1)
        with self.assertRaises(ValueError):
            original_signed_pressure_boundary(src,{},0,[7])

    def test_true_full_seven_original_W32_global_cuts_and_E_I(self):
        report=genuine_complete_W32_pressure_report()
        self.assertEqual(report["Branch_A_or_B"],"OPEN")
        self.assertEqual(report["S_s_Omega_s6"],"OPEN")
        self.assertEqual(report["W34_W38_complete_seven_positive_S"],
                         "UNKNOWN-NO-BB-SUBSTITUTION")
        expected={"lex":(942,786,156,259,4,165),
                  "reverse":(898,676,222,169,6,53),
                  "S68":(606,544,62,68,9,62),
                  "S72":(658,600,58,72,10,10)}
        self.assertEqual(len(report["genuine_complete_seven_W32_cases"]),4)
        for row in report["genuine_complete_seven_W32_cases"]:
            C,E,I,S,K,deficit=expected[row["scheme"]]
            self.assertEqual((row["C"],row["E"],row["I"],row["S_complete_seven"],
                              row["K_full"]),(C,E,I,S,K))
            prev=row["at_K_minus_one"]
            self.assertEqual(prev["active_original_incidence_N"],45)
            self.assertEqual(prev["positive_port_degree_sum_on_active_source_I"],6*S)
            self.assertEqual(prev["global_signed_pressure_G"],6*deficit)
            # Lex/reverse admit a true original pair-flow certificate.
            # S68/S72 do not, EVEN THOUGH the original 3-port Hall
            # minimum cut is globally tight: pair calibration is strict.
            expected_pair=(row["scheme"] in ("lex","reverse"))
            self.assertEqual(
                prev["calibrated_pair_flow_global_only_Hall_deficit_CERTIFIED"],
                expected_pair)
            pair_cert=prev["centred_pair_pressure_calibration"]
            if expected_pair:
                self.assertTrue(pair_cert[
                    "all_original_incidence_divergences_verified"])
                self.assertIsNone(pair_cert["failed_pair_cut_witness"])
            else:
                self.assertGreater(
                    pair_cert["failed_pair_cut_witness"][
                        "exact_positive_pair_cut_shortfall"],0)
                # Independent exact dual cuts on TRUE ORIGINAL W32, not
                # failures of the full or uniform original transport.
                pinned_pair_witness={
                    "S68":(372,28,1632,44),
                    "S72":(1215,128,6975,42),
                }
                shortage,cut,pressure,size=pinned_pair_witness[row["scheme"]]
                w=pair_cert["failed_pair_cut_witness"]
                self.assertEqual(
                    (w["exact_positive_pair_cut_shortfall"],
                     w["original_pair_cut_weight"],
                     w["sum_centred_integer_pressure"],
                     len(w["original_incidence_support_F"])),
                    (shortage,cut,pressure,size))
                self.assertEqual(pressure-45*cut,shortage)
                original=prev[
                    "failed_pair_cut_evaluated_in_original_triple_hypergraph"]
                self.assertEqual(original["k"],size)
                self.assertLessEqual(original["six_M_minus_K_D"],
                                     prev["uniform_exact_scaled_Hall_deficit_Delta6"])
                self.assertGreaterEqual(
                    2*original["original_partial_source_boundary"],
                    original["original_pair_projection_cut_weight"])
            self.assertEqual(prev["uniform_exact_scaled_Hall_deficit_Delta6"],
                             6*deficit)
            self.assertEqual(prev["exact_local_Hall_excess_over_global_source_pressure"],0)
            self.assertEqual(prev["minimum_cut_direct_pressure_boundary_witness"][
                "F_original_incidence_support"],list(range(45)))
            self.assertEqual(prev["minimum_cut_direct_pressure_boundary_witness"][
                "original_partial_source_boundary"],0)
            self.assertEqual(prev["exact_D6F_full_original_exception_mass"],deficit)
            now=row["at_K"]
            self.assertEqual(now["uniform_exact_scaled_Hall_deficit_Delta6"],0)
            self.assertEqual(now["exact_D6F_full_original_exception_mass"],0)


if __name__=="__main__":
    unittest.main()
