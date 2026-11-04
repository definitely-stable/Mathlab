"""Independent permanent exact ORIGINAL W32/W34 selector proof replay.

Machine-check the actual source 2/3-path union-neighborhood weights,
nonindependent path Jensen moments, actual physical 4th/6th moments,
original P2/Qx/Qy, and FORCED genuine source-owned physical C6 -> D6.
The complete source geometry is rebuilt on replay; source-ID corruption,
incorrect rational or fake all-h proof flags must fail closed.
"""
import copy
from fractions import Fraction
from pathlib import Path
import json
import unittest

from hyp105_original_adaptive_selector_moments import (
    canonical_adaptive_original_source_certificate,
)

CERT=Path(__file__).with_name(
    "hyp105_original_adaptive_selector_moments_certificates.json")


def validate_permanent_original_selector(cert,*,full_replay=False):
    if (cert.get("schema")!=
            "mathlab.hyp105.AA4-ORIGINAL-path-adaptive-selector-CI-proof.v1"
        or cert.get("root_230_status")!="OPEN_WITH_FORMAL_BLOCKER"
        or cert.get("all_h_Branch_A_proved_here") is not False
        or cert.get("all_N_adaptive_priority_and_bichromatic_path_weight_proof") is not True
        or len(cert.get("exact_original_source_cases",()))!=4):
        raise AssertionError("false all-h proof or lost true original source scope")
    expected=[
      (2,"lex",45,0,4,614,1346,52674,
        "3493493/203212800","310019889/3283356876800"),
      (2,"reverse-line",30,3,3,272,292,8868,
        "22663/376320","199853/481689600"),
      (4,"lex",205,15,3,3042,9622,109480,
        "49633201/22579200","4366613639/24979046400"),
      (4,"reverse-line",164,14,4,2168,5304,85748,
        "2177401/2073600","91344707/1561190400"),
    ]
    for x,ref in zip(cert["exact_original_source_cases"],expected):
        s,scheme,N,Z,K,P2,P3,trace6,W2,W3=ref
        if ((x.get("s"),x.get("scheme"),
             x.get("retained_original_source_flags"),
             len(x.get("deleted_original_source_IDs",())),
             x.get("source_original_conflict_degree_K"),
             x.get("r2",{}).get("directed_proper_original_physical_r_paths"),
             x.get("r3",{}).get("directed_proper_original_physical_r_paths"),
             x.get("real_original_trace_A6"),
             x.get("r2",{}).get("original_adaptive_weighted_endpoint_Frobenius_square"),
             x.get("r3",{}).get("original_adaptive_weighted_endpoint_Frobenius_square"))!=ref
            or x.get("root_230_status")!="OPEN_WITH_FORMAL_BLOCKER"
            or x.get("new_root_allh_Branch_A_proved_here") is not False
            or x.get("external_graph_supersaturation_needed_for_allh") is not True
            or x.get("physical_core_edges")!=2*N
            or x.get("all_N_weighted_Jensen_original_selector_proof") is not True):
            raise AssertionError("not exact true source ORIGINAL selector W32/W34 proof data")
        ids=x["selected_original_core_IDs"]
        deleted=x["deleted_original_source_IDs"]
        if (len(ids)!=N or len(set(ids))!=N
            or set(ids)&set(deleted)
            or len(set(deleted))!=Z
            or any(type(i) is not int or not 0<=i<x["original_source_flags"]
                   for i in ids+deleted)):
            raise AssertionError("not unique actual surviving original flag IDs")
        if (x["real_original_P2_square_norm"]+
            x["real_original_B2_square_norm"]!=
            x["real_original_trace_A4"]):
            raise AssertionError("true original two-path proper/improper spectral partition false")
        for r,trace in (("r2",x["real_original_trace_A4"]),
                        ("r3",x["real_original_trace_A6"])):
            y=x[r]
            adaptive=Fraction(
                y["original_adaptive_weighted_endpoint_Frobenius_square"])
            uniform=Fraction(
                y["uniform_sigma_squared_times_exact_original_proper_endpoint_Frobenius_square"])
            if (not uniform<=adaptive<=trace or
                adaptive<=uniform or
                y["physical_original_full_core_trace_A_to_2r"]!=trace or
                not y["weighted_original_selector_Jensen_bound_verified"] or
                not y["source_proper_paths_pairwise_original_ID_nonconflict"] or
                not y["adaptive_positive_path_weight_improves_uniform_coefficient"] or
                sum(y["original_source_neighborhood_size_histogram"].values())!=
                    y["directed_proper_original_physical_r_paths"]):
                raise AssertionError("false weighted original source path Jensen moment")
        if (x["real_original_core_Qx"]<0 or
            x["real_original_core_Qy"]<0):
            raise AssertionError("true physical source returns invalid")
    witnesses=cert.get("selector_actual_original_positive_D6_witness",{})
    if set(witnesses)!={"lex","reverse-line"}:
        raise AssertionError("missing two independently selected original W32 D6 motifs")
    for scheme,ids in (
        ("lex",[0,11,18,29,35,44]),
        ("reverse-line",[1,8,17,18,40,42])):
        z=witnesses[scheme]
        if (z.get("genuine_original_W32_scheme")!=scheme
            or z.get("planted_original_six_flag_IDs")!=ids
            or z.get("selected_physical_simple_C6")!=1
            or z.get("source_original_D6_sixsets_from_physical_C6")!=1
            or z.get("actual_original_flag_IDs_D6")!=[ids]
            or z.get("selector_C6_source_injective") is not True
            or z.get("all_selected_C6_coordinate_proper") is not True
            or z.get("source_priority_and_bichromatic_both_halves_FORCED_D6")
                is not True):
            raise AssertionError("false real original source positive D6 witness")
    if full_replay:
        real=canonical_adaptive_original_source_certificate()
        real=json.loads(json.dumps(real,sort_keys=True))
        if real!=cert:
            raise AssertionError("actual W32/W34 ORIGINAL physical selector certificate cannot be independently reproduced")
    return True


class PermanentOriginalSelectorWeightedMoments(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cert=json.loads(CERT.read_text(encoding="utf-8"))

    def test_independent_true_original_W32_W34_source_full_rational_replay(self):
        self.assertTrue(validate_permanent_original_selector(
            self.cert,full_replay=True))

    def test_corrupt_original_W34_weighted_r3_moment_fails_closed(self):
        bad=copy.deepcopy(self.cert)
        bad["exact_original_source_cases"][2]["r3"][
            "original_adaptive_weighted_endpoint_Frobenius_square"]="1/7"
        with self.assertRaises(AssertionError):
            validate_permanent_original_selector(bad)

    def test_fake_dyadic_universal_geometric_root_acceptance_fails_closed(self):
        bad=copy.deepcopy(self.cert)
        bad["all_h_Branch_A_proved_here"]=True
        with self.assertRaises(AssertionError):
            validate_permanent_original_selector(bad)

    def test_wrong_source_ORIGINAL_priority_conflict_neighbors_fails_closed(self):
        bad=copy.deepcopy(self.cert)
        bad["exact_original_source_cases"][0][
            "source_original_conflict_degree_K"]+=1
        with self.assertRaises(AssertionError):
            validate_permanent_original_selector(bad)

    def test_falsify_true_D6_six_original_source_flags_fails_closed(self):
        bad=copy.deepcopy(self.cert)
        bad["selector_actual_original_positive_D6_witness"]["reverse-line"][
            "planted_original_six_flag_IDs"]=[0,0,0,0,0,0]
        with self.assertRaises(AssertionError):
            validate_permanent_original_selector(bad)

    def test_wrong_physical_original_sixth_moment_fails_closed(self):
        bad=copy.deepcopy(self.cert)
        bad["exact_original_source_cases"][3]["real_original_trace_A6"]+=10
        with self.assertRaises(AssertionError):
            validate_permanent_original_selector(bad)

    def test_reused_original_source_flag_ID_under_Z_fails_closed(self):
        bad=copy.deepcopy(self.cert)
        bad["exact_original_source_cases"][2]["selected_original_core_IDs"][0]=0
        with self.assertRaises(AssertionError):
            validate_permanent_original_selector(bad)

    def test_false_endpoint_path_neighborhood_histogram_fails_closed(self):
        bad=copy.deepcopy(self.cert)
        first=bad["exact_original_source_cases"][0]["r2"]
        key=next(iter(first["original_source_neighborhood_size_histogram"]))
        first["original_source_neighborhood_size_histogram"][key]+=1
        with self.assertRaises(AssertionError):
            validate_permanent_original_selector(bad)


if __name__=="__main__":
    unittest.main()
