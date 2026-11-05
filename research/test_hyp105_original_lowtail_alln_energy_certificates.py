r"""Permanent original W32/W34 Z-masked all-N low-tail energy proof reviewer.

Rebuild ACTUAL original symplectic incidence, physical paired graph,
each physical 3-path, GQ projection, exact original endpoint 5-state
mask, original all-3 anchor exposure, two dual masked source B books,
all four physical blocker inequalities, and every six-distinct-ID
historical positive GF5 BBo from original geometry.
"""
from fractions import Fraction
import copy
import json
from pathlib import Path
import unittest

from hyp105_original_lowtail_alln_energy import canonical_original_lowtail_allN

CERT=Path(__file__).with_name(
    "hyp105_original_lowtail_alln_energy_certificates.json")


def verify_original_fullsource_lowtail_allN(cert,*,replay=False):
    if (cert.get("schema")!="mathlab.hyp105.original-LOWTAIL-allN-energy-source.v1"
        or cert.get("root_230_status")!="OPEN_WITH_FORMAL_BLOCKER"
        or cert.get("allh_unconditional_ROOT_230_claim") is not False
        or len(cert.get("genuine_true_original_cases",()))!=4):
        raise AssertionError("lost actual original source six-ID scope or false root claim")
    expected=((2,"lex",30,1,2254,416,370,44,1,1457,1375),
              (2,"reverse-line",34,1,2504,448,362,86,0,1486,1485),
              (4,"lex",247,14,43880,18624,12114,3442,1534,28073,28355),
              (4,"reverse-line",176,15,14592,5854,3748,1180,463,20095,19505))
    for x,ref in zip(cert["genuine_true_original_cases"],expected):
        actual=(x.get("s"),x.get("scheme"),
                x.get("original_core_source_count"),
                len(x.get("deleted_original_flag_IDs",())),
                x.get("physical_full_graph_ordered_3walks"),
                x.get("physical_proper_ordered_3paths"),
                x.get("actual_original_bad_endpoint_path_mass"),
                x.get("physical_internal_original_blocked_path_union"),
                x.get("real_positive_original_BBo_sixsets"),
                x.get("original_masked_POINT_source_B",{}).get("B"),
                x.get("original_masked_LINE_dual_source_B",{}).get("B"))
        if (actual!=ref
            or x.get("schema")!="mathlab.hyp105.original-lowtail-allN-Z-masked-energy.v1"
            or x.get("root_230_status")!="OPEN_WITH_FORMAL_BLOCKER"
            or x.get("allh_positive_root_Branch_A_proved_here") is not False
            or x.get("all_N_complete_original_source_path_partition") is not True
            or x.get("all_N_symmetric_original_masked_four_blocker_bound") is not True
            or x.get("all_N_TRUE_ORIGINAL_lowtail_condition_valid_even_if_negative") is not True):
            raise AssertionError("real original full-core/Z physical source data changed")
        core=x["original_core_source_IDs"]
        deleted=x["deleted_original_flag_IDs"]
        n=x["original_source_flags"]
        if (len(core)!=x["original_core_source_count"] or
            len(set(core))!=len(core) or
            len(set(deleted))!=len(deleted) or
            set(core)&set(deleted) or
            any(type(i) is not int or not 0<=i<n for i in core+deleted) or
            x["physical_real_edge_count"]!=2*len(core)):
            raise AssertionError("not true pair-owned six-source original IDs")
        part=x["original_exact_exception_endpoint_partition"]
        a=x["physical_alphabet"]
        if (set(part)!={"missing","incident","source_end_bad",
                        "deleted_projection","admissible"}
            or sum(part.values())!=a*a*(a-1)*(a-1)
            or sum(part[k] for k in part if k!="admissible")!=
               x["original_bad_endpoint_union_size"]):
            raise AssertionError("false original GQ source-endpoint mask union")
        path=x["physical_proper_ordered_3paths"]
        bad=x["actual_original_bad_endpoint_path_mass"]
        blocked=x["physical_internal_original_blocked_path_union"]
        bbo=x["real_positive_original_BBo_sixsets"]
        if (x["physical_full_graph_ordered_3walks"]-path !=
            x["physical_improper_3walks"]
            or x["physical_improper_3walks"]>
               x["physical_improper_3walks_max_3DeltaQ"]
            or x["exact_original_admissible_endpoint_proper3_path_mass"]!=path-bad
            or path-bad-blocked!=2*bbo):
            raise AssertionError("not exact physical proper/improper/endmask/4-blocker ORIGINAL partition")
        real_six=x["real_positive_original_BBo_six_IDs"]
        if (len(real_six)!=bbo
            or len({tuple(ids) for ids in real_six})!=bbo
            or any(len(ids)!=6 or len(set(ids))!=6 or
                   set(ids)&set(deleted) or
                   any(type(i) is not int or not 0<=i<n for i in ids)
                   for ids in real_six)):
            raise AssertionError("not genuine positive six DISTINCT ORIGINAL source ID BBo")
        Delta=x["physical_original_core_max_Delta"]
        tr4=x["physical_trace_A4"]
        bx=x["original_masked_POINT_source_B"]
        by=x["original_masked_LINE_dual_source_B"]
        blocks=x["physical_four_separate_internal_original_blocker_paths"]
        if (len(blocks)!=4
            or blocks[0]**2>bx["B"]*Delta*tr4
            or blocks[1]**2>bx["B"]*Delta*tr4
            or blocks[2]**2>by["B"]*Delta*tr4
            or blocks[3]**2>by["B"]*Delta*tr4
            or sum(blocks)<blocked
            or bx["B"]**2>bx["F1"]*bx["F2"]
            or by["B"]**2>by["F1"]*by["F2"]
            or x["source_dual_four_blocker_Cauchy_integer_upper"]<
               blocked):
            raise AssertionError("four original source physical blocker inequalities false")
        norm=x["exact_original_proper3_endpoint_Frobenius_square"]
        ebad=x["original_bad_endpoint_union_size"]
        if (bad*bad>ebad*norm
            or x["bad_endpoint_Cauchy_integer_upper"]<bad):
            raise AssertionError("exact ORIGINAL source projected Z endpoint bad Cauchy false")
        if (Fraction(x["physical_three_walk_Blackley_Roy_density_fraction"])>
               x["physical_full_graph_ordered_3walks"] or
            Fraction(x["all_N_abstract_energy_good3_lower"])>2*bbo or
            Fraction(x["all_N_fully_observable_good3_lower"])>2*bbo):
            raise AssertionError("false all-N density/source BBo six-ID inequality")
    if replay:
        rebuilt=json.loads(json.dumps(canonical_original_lowtail_allN(),
                                     sort_keys=True))
        if rebuilt!=cert:
            raise AssertionError("exact TRUE original W32/W34 source data cannot be reconstructed")
    return True


class PermanentTrueOriginalLowTailAllNEnergy(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cert=json.loads(CERT.read_text(encoding="utf8"))

    def test_full_true_original_W32_W34_reconstruct_all_source_six_IDs(self):
        self.assertTrue(verify_original_fullsource_lowtail_allN(self.cert,replay=True))

    def test_tamper_deleted_original_Z_source_ID_fails_closed(self):
        bad=copy.deepcopy(self.cert)
        bad["genuine_true_original_cases"][2]["deleted_original_flag_IDs"][0]=0
        with self.assertRaises(AssertionError):
            verify_original_fullsource_lowtail_allN(bad)

    def test_tamper_physical_four_blocker_position_fails_closed(self):
        bad=copy.deepcopy(self.cert)
        z=bad["genuine_true_original_cases"][2]
        z["physical_four_separate_internal_original_blocker_paths"][0]=10**8
        with self.assertRaises(AssertionError):
            verify_original_fullsource_lowtail_allN(bad)

    def test_tamper_dual_SOURCE_GQ_line_book_fails_closed(self):
        bad=copy.deepcopy(self.cert)
        bad["genuine_true_original_cases"][2]["original_masked_LINE_dual_source_B"]["B"]+=1
        with self.assertRaises(AssertionError):
            verify_original_fullsource_lowtail_allN(bad)

    def test_tamper_original_endpoint_source_mask_fails_closed(self):
        bad=copy.deepcopy(self.cert)
        bad["genuine_true_original_cases"][3]["original_exact_exception_endpoint_partition"][
            "deleted_projection"]+=1
        with self.assertRaises(AssertionError):
            verify_original_fullsource_lowtail_allN(bad)

    def test_tamper_original_BBo_six_ID_provenance_fails_closed(self):
        bad=copy.deepcopy(self.cert)
        bad["genuine_true_original_cases"][2]["real_positive_original_BBo_six_IDs"][0][0]=999
        with self.assertRaises(AssertionError):
            verify_original_fullsource_lowtail_allN(bad)

    def test_tamper_real_physical_3walk_Cauchy_fails_closed(self):
        bad=copy.deepcopy(self.cert)
        bad["genuine_true_original_cases"][1]["physical_full_graph_ordered_3walks"]+=1
        with self.assertRaises(AssertionError):
            verify_original_fullsource_lowtail_allN(bad)

    def test_falsely_claim_complete_allh_230_proof_fails_closed(self):
        bad=copy.deepcopy(self.cert)
        bad["allh_unconditional_ROOT_230_claim"]=True
        with self.assertRaises(AssertionError):
            verify_original_fullsource_lowtail_allN(bad)


if __name__=="__main__":
    unittest.main()
