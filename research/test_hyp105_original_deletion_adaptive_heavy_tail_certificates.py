r"""Permanent exact ORIGINAL source-ID-deletion adaptive SS6 proof acceptance.

The full true original symplectic W32/W34 model, actual fixed global
factor pair injections, all ORIGINAL owned two-diagonal physical edges,
frozen-before-deletion heavy Q, original conflict graph, Caro-Wei,
bichromatic physical selectors, noncloned ordinary F, and positive
original six distinct GF5 D6 IDs are REGENERATED from source, not
silently accepted from a frozen unverified numerical JSON.

The 2^64 C^3 threshold is a conditional HEAVY branch, not an externally
certified numeric published C_graph and not a complete all-h Branch A.
"""
import copy
from fractions import Fraction
import json
from pathlib import Path
import unittest

from hyp105_original_deletion_adaptive_heavy_tail import (
    canonical_original_deleted_adaptive_heavy_report,
)

CERT=Path(__file__).with_name(
    "hyp105_original_deletion_adaptive_heavy_tail_certificates.json")


def verify_permanent_real_original_Z_tail(cert,*,replay=False):
    if (cert.get("schema")!=
            "mathlab.hyp105.AA4-true-original-deletion-robust-heavy-SS6.v1"
        or cert.get("root_230_status")!="OPEN_WITH_FORMAL_BLOCKER"
        or cert.get("root_allh_Branch_A_proved_here") is not False
        or cert.get("allh_ss6_external_C_c_required_NOT_numeric") is not True
        or len(cert.get("genuine_source_cases",()))!=4
        or len(cert.get("formal_constants",()))!=2):
        raise AssertionError("false all-h root proof or lost exact original source evidence")
    expected=[
        (2,"lex",1,36,88,44,54,10,20,34,0),
        (2,"reverse-line",3,35,84,42,39,11,22,34,0),
        (4,"lex",4,185,842,421,520,79,108,136,0),
        (4,"reverse-line",5,165,837,420,513,73,124,146,1),
    ]
    for x,ref in zip(cert["genuine_source_cases"],expected):
        s,scheme,z,q,E_A,L,eJ,selected,mF,vF,c6F=ref
        F=x.get("actual_uncloned_balanced_chunk",{})
        values=(x.get("s"),x.get("scheme"),
                len(x.get("deleted_original_flag_IDs",())),
                x.get("full_original_QT_vertices"),
                x.get("original_tail_edges_remaining_after_Z"),
                len(x.get("retained_heavy_original_flag_IDs",())),
                x.get("original_heavy_conflict_edges_actual"),
                x.get("original_both_typed_cuts_selected_count"),
                F.get("winner_ordinary_subgraph_edges"),
                F.get("winner_ordinary_subgraph_vertices"),
                x.get("actual_winner_uncloned_physical_C6"))
        if (values!=ref
            or x.get("schema")!="mathlab.hyp105.original-adaptive-Z-robust-balanced-SS6.v1"
            or x.get("root_230_status")!="OPEN_WITH_FORMAL_BLOCKER"
            or x.get("root_allh_Branch_A_proved_here") is not False
            or x.get("unknown_published_C_graph_c_graph_NOT_guessed") is not True
            or x.get("source_c6_injects_original_positive_D6_after_Z") is not True
            or x.get("no_cloned_vertices_or_source_IDs") is not True
            or x.get("original_both_real_diagonals_per_selected_ID") is not True):
            raise AssertionError("original W32/W34 full physical source tail certificate mismatch")
        Z=x["deleted_original_flag_IDs"]
        I=x["retained_heavy_original_flag_IDs"]
        n=x["full_original_physical_vertices"]
        if (len(set(Z))!=z or len(set(I))!=L
            or set(Z)&set(I) or any(type(i) is not int or
              not 0<=i<x["original_source_flags"] for i in Z+I)
            or x["actual_original_heavy_edges_removed_by_Z"]>2*z
            or E_A!=x["full_original_tail_edges"]-
                      x["actual_original_heavy_edges_removed_by_Z"]
            or L*2<E_A
            or 4*selected*(L+2*eJ)<L**2):
            raise AssertionError("original flag owner heavy-edge sensitivity or Caro-Wei guarantee lost")
        if not F.get("no_clone_bipartite_chunk"):
            raise AssertionError("non-simple cloned physical SS6 chunk cannot use published theorem")
        owners=x["true_original_D6_six_flag_IDs_selected"]
        if (len(owners)!=x["actual_physical_selected_C6"]
            or len({tuple(y) for y in owners})!=len(owners)
            or any(len(y)!=6 or len(set(y))!=6 or
                   set(y)&set(Z) for y in owners)):
            raise AssertionError("selected ordinary sixcycles NOT genuine positive original six-ID D6")
        if c6F>len(owners):
            raise AssertionError("winner subgraph original physical C6 count exceeds source G")
        predicted=Fraction(L*L,32*n*(L+2*eJ))
        qC3=Fraction(L**6,2**16*n**3*q*(L+2*eJ)**3)
        if (Fraction(x["exact_adaptive_guaranteed_density"])!=predicted
            or Fraction(x["exact_external_C_graph_CUBED_sufficient_data_threshold"])!=qC3
            or Fraction(F["source_chunk_e_over_v"])!=Fraction(mF,vF)
            or Fraction(mF**3,vF**4)<qC3
            or vF>2*q
            or not F["source_chunk_actual_E_to_r_pigeonhole_verified"]):
            raise AssertionError("inexact source-data adaptive SS6 ordinary cubic graph hypothesis")
        vertices={tuple(y) for y in F["winner_original_physical_vertices"]}
        physical_edges=[tuple(tuple(v) for v in e)
                        for e in F["winner_actual_physical_edges"]]
        if (len(vertices)!=vF or len(physical_edges)!=mF
            or any(len(set(e))!=2 or not set(e)<=vertices
                   for e in physical_edges)
            or len({frozenset(e) for e in physical_edges})!=mF):
            raise AssertionError("SS6 chunk has cloned physical edges/vertices")
    for x,(C,c) in zip(cert["formal_constants"],(
            (Fraction(1),Fraction(1)),(Fraction(7,3),Fraction(2,101)))):
        if (x["schema"]!="mathlab.hyp105.original-SS6-Z-resilient-allh-constants.v1"
            or Fraction(x["published_graph_C_is_only_unfixed_symbolic_trial"])!=C
            or Fraction(x["published_graph_c_is_only_unfixed_symbolic_trial"])!=c
            or Fraction(x["residual_original_tail_epsilon"])!=Fraction(1,16)
            or Fraction(x["improved_684_AND_adversarial_original_deletion_T"])!=2**64*C**3
            or Fraction(x["root_674_NEW_T_for_same_full_tail_deletion_hypothesis"])!=2**64*C**3
            or Fraction(x["root_674_old_T_for_full_tail_eighth_original_deletion_at_most_1over32"])!=2**65*C**3
            or x["actual_published_graph_constants_numerical_values_VERIFIED"] is not False
            or x["new_root_allh_geometric_Branch_A_proved"] is not False
            or x["root_230_status"]!="OPEN_WITH_FORMAL_BLOCKER"):
            raise AssertionError("invented external graph SS6 constants or incorrect symbolic heavy source cap")
    if replay:
        generated=json.loads(json.dumps(
            canonical_original_deleted_adaptive_heavy_report(),sort_keys=True))
        if generated!=cert:
            raise AssertionError("permanent true ORIGINAL W32/W34 Z-heavy selector source proof not reproducible")
    return True


class PermanentTrueOriginalZRobustSS6(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cert=json.loads(CERT.read_text(encoding="utf-8"))

    def test_entire_original_GQ_W32_W34_adversarial_deleted_source_proof_replay(self):
        self.assertTrue(verify_permanent_real_original_Z_tail(
            self.cert,replay=True))

    def test_tamper_frozen_FULL_Q_before_original_Z_fails_closed(self):
        altered=copy.deepcopy(self.cert)
        altered["genuine_source_cases"][2]["full_original_QT_vertices"]+=1
        with self.assertRaises(AssertionError):
            verify_permanent_real_original_Z_tail(altered)

    def test_corrupt_actual_original_conflict_pairs_fails_closed(self):
        altered=copy.deepcopy(self.cert)
        altered["genuine_source_cases"][0]["original_heavy_conflict_edges_actual"]+=1
        with self.assertRaises(AssertionError):
            verify_permanent_real_original_Z_tail(altered)

    def test_corrupt_genuine_source_six_ID_positive_original_D6_fails_closed(self):
        altered=copy.deepcopy(self.cert)
        altered["genuine_source_cases"][3]["true_original_D6_six_flag_IDs_selected"][0]=[0]*6
        with self.assertRaises(AssertionError):
            verify_permanent_real_original_Z_tail(altered)

    def test_corrupt_actual_data_adaptive_cubed_external_SS6_gate_fails_closed(self):
        altered=copy.deepcopy(self.cert)
        altered["genuine_source_cases"][1][
            "exact_external_C_graph_CUBED_sufficient_data_threshold"]="3"
        with self.assertRaises(AssertionError):
            verify_permanent_real_original_Z_tail(altered)

    def test_corrupt_declared_original_no_clone_physical_F_fails_closed(self):
        altered=copy.deepcopy(self.cert)
        edges=altered["genuine_source_cases"][3][
            "actual_uncloned_balanced_chunk"]["winner_actual_physical_edges"]
        edges[1]=copy.deepcopy(edges[0])
        with self.assertRaises(AssertionError):
            verify_permanent_real_original_Z_tail(altered)

    def test_false_published_actual_numeric_C_graph_equals_one_fails_closed(self):
        altered=copy.deepcopy(self.cert)
        altered["formal_constants"][0][
            "actual_published_graph_constants_numerical_values_VERIFIED"]=True
        with self.assertRaises(AssertionError):
            verify_permanent_real_original_Z_tail(altered)

    def test_false_claim_complete_root_allh_from_heavy_branch_fails_closed(self):
        altered=copy.deepcopy(self.cert)
        altered["root_allh_Branch_A_proved_here"]=True
        with self.assertRaises(AssertionError):
            verify_permanent_real_original_Z_tail(altered)


if __name__=="__main__":
    unittest.main()
