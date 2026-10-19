"""AA4-CO: independent full-original W32 seven-GF5 root S vs twofiber covariance."""
import unittest
from fractions import Fraction

from hyp105_issue230_d6aa4co_global_allseven_W32_96map_bridge import (
    GROUPS,SEVEN,EXPECTED_LEFT_COUNT,source_original_POINT_multiplicity,
    original_W32_global_96_allseven_census,
    original_W32_global_reference_single_state,
    original_W32_S72_reversible_TWO_family_fixture,
)
from hyp105_issue230_d6aa4cl_shared_four_point_fibers_covariance import (
    ORBIT,genuine_original_two_fiber_fixture,
)
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_g5e2b3e1b0_seven_signature import R3_CERTIFIED_FLOORS

FIXTURE_LEX=None

def _get_lex():
    return genuine_original_two_fiber_fixture(1,"four_cycle_switch")[:2]


def _verify_all_96(data,model,pts):
    weight=data["full_original_hist_GF5_weighted_seven_numerator"]
    unweighted=data["full_root_UNWEIGHTED_seven_motif_S"]
    selfgroups=data["all_original_GF5_weight_by_SOURCE_group"]
    classcounts=data["all_seven_original_historical_class_counts_by_complete_f"]
    selfcounts=data["all_original_Q_counts_by_SOURCE_group"]
    assert len(weight)==len(unweighted)==96
    for i in range(96):
        assert data["physically_left_original_six_Q_each"][i]==62370
        assert weight[i]==sum(selfgroups[k][i] for k in GROUPS)
        assert unweighted[i]==sum(selfcounts[k][i] for k in GROUPS)
        assert weight[i]==sum(classcounts[i].get(tag,0)*R3_CERTIFIED_FLOORS[tag] for tag in SEVEN)
        assert unweighted[i]==sum(classcounts[i].values())
        assert unweighted[i]>0
        assert weight[i]>0
    for index in (0,1,17,47,95):
        raw=original_W32_global_reference_single_state(model,pts,ORBIT[index])
        assert (raw["weighted"],raw["unweighted"])==(weight[index],unweighted[index])
        assert raw["historical_seven_classes"]=={
            k:classcounts[index].get(k,0) for k in SEVEN}
        assert raw["original_complete_left_Q"]==EXPECTED_LEFT_COUNT
    variance=data["global_variance_ledger_components"]
    expected=(variance["Var_A"]+variance["Var_B"]+variance["Var_rest"]
        +2*(variance["Cov_A_B"]+variance["Cov_A_rest"]+variance["Cov_B_rest"]))
    assert expected==data["full_original_GF5_weighted_variance"]
    assert data["weighted_min"]<=data["weighted_max"]
    assert data["unweighted_min"]<=data["unweighted_max"]
    assert data["unweighted_min"]==min(unweighted)
    assert data["unweighted_max"]==max(unweighted)
    assert data["root_A_B_C_status"]=="OPEN_WITH_FORMAL_BLOCKER"
    return {"root_S_range":(min(unweighted),max(unweighted)),
            "GF5_range":(min(weight),max(weight)),
            "cov_AB":str(data["source_fiber_A_B_GF5_covariance"]),
            "cov_A_rest":str(variance["Cov_A_rest"]),
            "cov_B_rest":str(variance["Cov_B_rest"]),
            "weighted_full_var":str(data["full_original_GF5_weighted_variance"]),
            "root_unweighted_var":str(data["full_original_UNWEIGHTED_seven_variance"]),
            "S_SOURCE_group_minmax":data["all_original_Q_count_minmax_by_SOURCE_group"],
            "GF5_SOURCE_group_minmax":data["all_original_weight_minmax_by_SOURCE_group"],
            "S_SOURCE_group_means":{k:str(v) for k,v in data["all_original_accepted_S_mean_by_SOURCE_group"].items()}}


class AA4COGlobalOriginalSevenClassRootCountercheck(unittest.TestCase):
    def test_01_true_original_W32_lex_complete_96map_all7_S_and_GF5(self):
        model,pts=_get_lex()
        data=original_W32_global_96_allseven_census(model,pts)
        result=_verify_all_96(data,model,pts)
        self.assertEqual(data["source_fiber_A_B_GF5_covariance"],Fraction(10614483,16))
        self.assertEqual((data["unweighted_min"],data["unweighted_max"]),(127,190))
        self.assertEqual((data["weighted_min"],data["weighted_max"]),(5813330,8572049))
        self.assertEqual(data["full_original_UNWEIGHTED_seven_variance"],Fraction(39749,192))
        self.assertEqual(data["full_original_GF5_weighted_variance"],Fraction(28183991874289,72))
        self.assertEqual(data["global_variance_ledger_components"]["Cov_A_rest"],Fraction(9707398965,32))
        self.assertEqual(data["global_variance_ledger_components"]["Cov_B_rest"],Fraction(-146709849,2))
        self.assertEqual(data["a"],6)
        self.assertEqual(data["V"],15)
        self.assertTrue(data["all_96_full_original_f_and_one_g"])
        print("AA4CO_GLOBAL_W32_LEX",result,flush=True)

    def test_02_true_original_W32_S72_complete_96map_all7_S_and_GF5(self):
        model,pts=original_W32_S72_reversible_TWO_family_fixture()
        data=original_W32_global_96_allseven_census(model,pts)
        result=_verify_all_96(data,model,pts)
        self.assertEqual(data["a"],6)
        self.assertEqual((data["unweighted_min"],data["unweighted_max"]),(72,167))
        self.assertEqual((data["weighted_min"],data["weighted_max"]),(3283610,7332844))
        self.assertEqual(data["source_fiber_A_B_GF5_covariance"],Fraction(0))
        self.assertEqual(data["full_original_UNWEIGHTED_seven_variance"],Fraction(220907,576))
        self.assertEqual(data["full_original_GF5_weighted_variance"],Fraction(406820603747771,576))
        self.assertEqual(data["global_variance_ledger_components"]["Cov_A_rest"],Fraction(10874141883,16))
        self.assertEqual(data["global_variance_ledger_components"]["Cov_B_rest"],0)
        self.assertEqual(len(data["full_root_UNWEIGHTED_seven_motif_S"]),96)
        print("AA4CO_GLOBAL_W32_S72",result,flush=True)

    def test_03_actual_original_sevenclass_source_pattern_and_invalid_Q(self):
        model,pts=_get_lex()
        s,V,a,inc,f,g,_,_=_original_source(model)
        Q=tuple(range(6))
        self.assertIn(source_original_POINT_multiplicity(Q,inc),("A","B","C","OTHER"))
        for Q in ((0,0,1,2,3,4),(0,1,2,3,4,999)):
            with self.assertRaises(ValueError):
                source_original_POINT_multiplicity(Q,inc)
        with self.assertRaises(ValueError):
            original_W32_global_96_allseven_census(model,pts[:7])
        with self.assertRaises(ValueError):
            original_W32_global_96_allseven_census(model,pts[:7]+pts[:1])
        with self.assertRaises(ValueError):
            original_W32_global_96_allseven_census(dict(model,s=4),pts)

    def test_04_W34_W38_original_twofiber_scope_guard_not_global_S(self):
        # Real higher-h geometries intentionally only verify the TRUE
        # original twofiber block construction, NOT 62,370 global-Q.
        # Do NOT infer finite W32 complete-global enumeration is all-h.
        from hyp105_issue230_d6aa4cm_negative_original_named_pair_covariance import (
            true_original_negative_D6_pair_fixture,
        )
        from hyp105_issue230_d6aa4cn_joint_dual_compatibility_block_ledger import (
            original_twofiber_pairwise_D6_compensation_ledger,
        )
        for h in (2,3):
            sample=true_original_negative_D6_pair_fixture(h)
            model=sample["actual_original_model"]
            pts=sample["eight_REAL_original_POINT_source_ids"]
            with self.assertRaises(ValueError):
                original_W32_global_96_allseven_census(model,pts)
            x=original_twofiber_pairwise_D6_compensation_ledger(model,pts)
            self.assertTrue(x["full_original_GQ_S_s_NOT_COMPUTED"])
            self.assertEqual(x["s"],1<<h)
            print("AA4CO_ALLH_SCOPE_GUARD",h,"real_twofiber",x["right_original_D6_Q_active_A"],
                  x["right_original_D6_Q_active_B"],"full_global_uncomputed",True,flush=True)


if __name__=="__main__":
    unittest.main()
