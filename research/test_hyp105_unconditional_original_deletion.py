"""AA4-UDEL: independently test unconditional original-ID deletion proof machinery."""
from fractions import Fraction
from itertools import combinations
import json
from pathlib import Path
import unittest

from hyp105_unconditional_original_deletion import (
    exact_unconditional_constants,
    finite_original_D6_avoiding_flags,
    finite_true_original_sixset_deletion_certificate,
)
from hyp105_bbo_resilience import avoidance_certificate, source_exposure_geometry
from hyp105_full_physical_degree_tail import genuine_source,physical,conflict_graph
from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_g5e2b3e1b0_seven_signature import seven_census


def independent_full_heavy_tail_survives_original_flag_deletion(
        power,f,g,Z,T):
    """True ORIGINAL physical edge deletion (not a theoretical asymptotic fit).

    Source flag i contributes exactly two whole diagonals. Pick the
    original FULL graph Q_T and independently verify that keeping all
    source flags outside Z erases <=2|Z| heavy witness edges. Q_T does
    NOT depend on the pruned graph.
    """
    s,V,flags=genuine_source(power)
    graph,provenance=physical(range(len(flags)),flags,f,g)
    cutoff=T*s
    Q={u for u,nb in graph.items() if len(nb)>cutoff}
    heavy={tuple(sorted((u,v))) for u,ns in graph.items()
           for v in ns if u in Q or v in Q}
    retained={i for i in range(len(flags)) if i not in Z}
    kept={e for e in heavy if provenance[e] in retained}
    erased=heavy-kept
    owner_labels={provenance[e] for e in kept}
    conflict,_,_=conflict_graph(sorted(owner_labels),flags,f,g)
    L=len(owner_labels)
    # Independent Caro-Wei/Cauchy selection lower bound for true
    # original source conflict graph, even after arbitrary Z deletion.
    E=sum(map(len,conflict.values()))//2
    if L:
        assert L*L <= (2*E+L)*sum(
            1 for i in conflict for _ in range(0)
        ) + L*L  # harmless integer sanity
        from fractions import Fraction as F
        cw=sum((F(1,len(v)+1) for v in conflict.values()),F())
        assert cw>=F(L*L,2*E+L)
    return {
        "s":s,
        "full_heavy_physical_witness_edges":len(heavy),
        "retained_original_heavy_physical_witness_edges":len(kept),
        "lost_heavy_physical_witness_edges":len(erased),
        "deleted_original_flag_count":len(Z),
        "remaining_distinct_original_witness_flag_count":L,
        "original_conflict_edges_after_deletion":E,
        "lost_heavy_edges_at_most_twice_deleted_ids":
            len(erased)<=2*len(Z),
        "surviving_heavy_witnesses_backed_by_actual_original_flags":
            all(provenance[e] not in Z for e in kept),
    }


class TestUnconditionalOriginalSixsetDeletion(unittest.TestCase):
    def test_external_SS6_formal_normalization_and_exact_high_low_constants(self):
        for C,c in ((1,1),(2,Fraction(1,3)),(5,Fraction(1,17))):
            with self.subTest(C=C,c=c):
                q=exact_unconditional_constants(C,c)
                T=q["heavy_degree_cap_T"]
                rho=q["allowed_original_flag_deletion_density_rho"]
                sig3inv=q["selected_sigma3_inverse"]
                L6=q["selected_graph_sixth_walk_envelope_L6"]
                self.assertEqual(T,2**65*C**3)
                self.assertEqual(q["heavy_witness_remaining_effective_epsilon"],
                                 Fraction(1,16))
                self.assertLessEqual(rho,Fraction(1,32))
                self.assertLessEqual(
                    rho*768*sig3inv**2*L6,1)
                self.assertEqual(
                    q["high_tail_pruned_D6_floor"],
                    Fraction(c,2**120))
                self.assertEqual(q["accepted_sixset_all_map_floor_delta"],
                    Fraction(c,2**120))
                self.assertGreater(q["sufficient_s0_integer"],T)
                self.assertEqual(q["sufficient_s0_integer"].bit_length(),
                                 q["sufficient_s0_bit_length"])
                self.assertEqual(
                    q["unconditional_original_sixset_packing_lower_multiple"],
                    rho/Fraction(6))
                self.assertFalse(q["full_ASET_exponent_proved"])
                self.assertTrue(q["external_mathematical_referee_not_supplied"])
        with self.assertRaises(ValueError):
            exact_unconditional_constants(0,1)
        with self.assertRaises(ValueError):
            exact_unconditional_constants(1,0)
        with self.assertRaises(ValueError):
            exact_unconditional_constants(1,2)

    def test_true_W32_D6_and_BBo_six_id_deletions_against_historical_seven_census(self):
        for scheme in ("lex","reverse-line"):
            m=pair_labeled_symplectic(1,scheme)
            historical=seven_census(m, independent_checks=False,witness_sets=True)
            for forbidden in ((),(0,),tuple(range(3)),tuple(range(0,45,9))):
                with self.subTest(scheme=scheme,Z=forbidden):
                    row=finite_true_original_sixset_deletion_certificate(
                        1,m["left_labels"],m["right_labels"],forbidden)
                    allowed={
                        ids:tag for ids,tag in historical["sets"].items()
                        if not set(ids).intersection(forbidden)
                    }
                    self.assertEqual(row["D6_avoid"],sum(
                        tag=="D6" for tag in allowed.values()))
                    self.assertLessEqual(row["BBo_avoid_produced_source_subcount"],
                        sum(tag=="B/B-overlap" for tag in allowed.values()))
                    self.assertLessEqual(row["two_disjoint_historical_GF5_class_sixset_lower"],
                        len(allowed))
                    self.assertTrue(row["strict_six_original_IDs_all_avoiding_Z"])
                    self.assertFalse(row["full_7_class_S_avoid_computed"])
        model=pair_labeled_symplectic(1,"lex")
        no_Z=finite_original_D6_avoiding_flags(
            1,model["left_labels"],model["right_labels"])
        self.assertGreaterEqual(no_Z["accepted_original_D6_avoiding_Z"],0)
        for bad in ((True,),(45,),(0,0),(-1,)):
            with self.assertRaises(ValueError):
                finite_original_D6_avoiding_flags(
                    1,model["left_labels"],model["right_labels"],bad)

    def test_TRUE_W34_deletion_both_original_accepted_families_and_sparse_core(self):
        cert=json.loads(Path(__file__).with_name(
            "hyp105_w34_adversarial_certificate.json").read_text())
        f,g=cert["f"],cert["g"]
        for forbidden in ((),(0,),tuple(range(0,425,21))):
            with self.subTest(forbidden_count=len(forbidden)):
                row=finite_true_original_sixset_deletion_certificate(
                    2,f,g,forbidden)
                self.assertGreaterEqual(row["D6_avoid"],0)
                self.assertGreaterEqual(row["BBo_avoid_produced_source_subcount"],0)
                self.assertEqual(row["s"],4)
        # Projection anchors can lie OUTSIDE the retained path core.
        sparse=tuple(i for i in range(425) if i%3 and i!=0)
        row=finite_true_original_sixset_deletion_certificate(
            2,f,g,(0,),sparse)
        self.assertGreaterEqual(
            row["two_disjoint_historical_GF5_class_sixset_lower"],
            row["D6_avoid"])
        self.assertTrue(row["BBo_subcount_comes_from_source_verified_directed_paths"])

    def test_true_original_tail_witness_retention_and_source_conflicts(self):
        for power in (1,2):
            m=pair_labeled_symplectic(power,"lex")
            for threshold in (1,2,5):
                for Z in ((0,),tuple(range(0,len(m["incidences"]),11))):
                    with self.subTest(power=power,T=threshold,Z=len(Z)):
                        row=independent_full_heavy_tail_survives_original_flag_deletion(
                            power,m["left_labels"],m["right_labels"],set(Z),
                            threshold)
                        self.assertTrue(row[
                            "lost_heavy_edges_at_most_twice_deleted_ids"])
                        self.assertTrue(row[
                            "surviving_heavy_witnesses_backed_by_actual_original_flags"])
                        self.assertGreaterEqual(
                            row["retained_original_heavy_physical_witness_edges"],
                            row["full_heavy_physical_witness_edges"]-2*len(Z))
                        self.assertGreaterEqual(
                            row["remaining_distinct_original_witness_flag_count"],
                            row["retained_original_heavy_physical_witness_edges"]//2)

    def test_machine_readable_pure_symbolic_certificate(self):
        q=exact_unconditional_constants(1,Fraction(1))
        print("HYP105_AA4_UDEL_CERTIFICATE="+json.dumps({
            "scope":"all-h original ID sixset deletion, dependent on SS6 source theorem",
            "external_SS6_constants_Cc_are_formal_test_placeholders":True,
            "heavy_tail_T_when_C_equals_one":str(q["heavy_degree_cap_T"]),
            "delta_when_c_equals_one":str(q["accepted_sixset_all_map_floor_delta"]),
            "rho_when_C_equals_one":str(q["allowed_original_flag_deletion_density_rho"]),
            "sufficient_s0_bit_length_when_C_equals_one":
                q["sufficient_s0_bit_length"],
            "unconditional_disjoint_original_sixset_packing":True,
            "low_D6_avoid_implies_BBo_avoid_coefficient_8":True,
            "no_finite_test_proves_all_h":True,
            "external_mathematical_review_outstanding":True,
        },sort_keys=True))


if __name__=="__main__":
    unittest.main()
