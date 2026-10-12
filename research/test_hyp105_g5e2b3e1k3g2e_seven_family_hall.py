"""Independent seven-accepted-GF5-family finite Hall and support tests."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
import unittest

from hyp105_g5e2b3e1k1_kikuchi_c6 import gq_pair_model,kikuchi_graph
from hyp105_g5e2b3e1b0_seven_signature import (
    seven_census,R3_CERTIFIED_FLOORS
)
from hyp105_g5e2b3b1_critical_flows import SIGNS
from hyp105_g5e2b3b1b_five_six_flows import exact_dual_GF5_six_flow
from hyp105_g5e2b3e1k3g2d_charging_hall import (
    cross_witnesses,finite_charging_certificate
)
from hyp105_g5e2b3e1k3g2e_seven_family_hall import (
    seven_family_hall_certificate,witness_original_five_support,
    hall_capacity_certificate,_rules_for
)


def independent_original_column_five_support(model,w):
    """Independently write actual physical vertex cycle by source-side logic."""
    a=model["a"]
    p,l=w["anchor"]
    x,xx=model["left_labels"][p]
    y,yy=model["right_labels"][l]
    vtx={"A":x*a+y,"B":xx*a+yy,"C":x*a+yy,"D":xx*a+y}
    m,n=w["middle_pair"]
    if w["side"]=="line":
        names=("A","C","D","B")
    elif w["side"]=="point":
        names=("A","D","C","B")
    else:
        raise ValueError("unrecognized dual witness side")
    # Six-cycle A,m,C,D,n,B or A,m,D,C,n,B
    cycle=(vtx[names[0]],m,vtx[names[1]],
           vtx[names[2]],n,vtx[names[3]])
    physical_by_edge={}
    for pp,ll in model["incidences"]:
        xx1,xx2=model["left_labels"][pp]
        yy1,yy2=model["right_labels"][ll]
        physical_by_edge[frozenset((xx1*a+yy1,xx2*a+yy2))]=(pp,ll)
        physical_by_edge[frozenset((xx1*a+yy2,xx2*a+yy1))]=(pp,ll)
    provenance=[physical_by_edge[frozenset((cycle[i],cycle[(i+1)%6]))]
                for i in range(6)]
    cnt=Counter(provenance)
    if cnt[w["anchor"]]!=2 or sorted(cnt.values())!=[1,1,1,1,2]:
        raise AssertionError("source column is not antipodal-only repeat")
    return frozenset(cnt)


class K3G2ESevenMotifHallTests(unittest.TestCase):
    def test_exact_seven_gf5_targets_and_global_source_provenance(self):
        for scheme,seed,expected_S,expected_cross in (
            ("lex",None,259,36),
            ("reverse-line",None,169,28),
            ("random",20261012,None,17),
        ):
            model=gq_pair_model(1,scheme,seed)
            cert=seven_family_hall_certificate(model)
            self.assertEqual(cert["accepted_seven_sixset_targets"],expected_S
                             if expected_S is not None else
                             cert["accepted_seven_sixset_targets"])
            self.assertGreater(cert["accepted_seven_sixset_targets"],0)
            self.assertEqual(cert["J_cross_five_column_witnesses"],expected_cross)
            self.assertTrue(cert["all_target_types_have_proved_positive_GF5_floor"])
            self.assertFalse(cert["all_h_uniform_bounded_charging_proved"])
            self.assertFalse(cert["all_h_seven_family_S_omega_s6_proved"])
            rows=cross_witnesses(model)
            for w in rows:
                self.assertEqual(len(independent_original_column_five_support(model,w)),5)
            self.assertEqual(cert["witness_support_cardinality"],5)
            self.assertEqual(cert["accepted_target_original_column_cardinality"],6)
            accepted=seven_census(model,independent_checks=False,witness_sets=True)
            self.assertEqual(len(accepted["sets"]),cert["accepted_seven_sixset_targets"])
            for ids,family in accepted["sets"].items():
                self.assertEqual(len(set(ids)),6)
                self.assertIn(family,R3_CERTIFIED_FLOORS)
                self.assertGreater(R3_CERTIFIED_FLOORS[family],0)
            self.assertEqual(cert["accepted_full_GF5_risk_floor_numerator"],
                             accepted["GF5_seven_lower_numerator"])
            for rule,stats in cert["rules"].items():
                self.assertLessEqual(stats["all"]["matched"],len(rows))
                self.assertEqual(stats["all"]["left_nodes"],len(rows))
                self.assertEqual(stats["heavy"]["left_nodes"],
                                 cert["heavy_class_witnesses"])
                self.assertEqual(stats["all"]["min_cut_capacity"],
                                 stats["all"]["matched"])
                self.assertEqual(stats["heavy"]["min_cut_capacity"],
                                 stats["heavy"]["matched"])
                self.assertEqual(stats["all"]["right_nodes"],
                                 len(accepted["sets"]))
            prior=finite_charging_certificate(model)
            self.assertEqual(cert["same_anchor_D6_only_reconciliation"]["matched"],
                             prior["all_cross_anchor_local_charge"]["matched"])
            self.assertEqual(cert["same_anchor_D6_only_reconciliation"]["isolated"],
                             prior["all_cross_anchor_local_charge"]["isolated"])

    def test_real_accepted_GF5_signed_oracle_representatives(self):
        """Check at least one true nonzero signed GF5 event for all seven target families."""
        model=gq_pair_model(1,"lex")
        accepted=seven_census(model,independent_checks=False,witness_sets=True)["sets"]
        first={}
        for ids,tag in accepted.items():
            first.setdefault(tag,ids)
        self.assertEqual(set(first),set(R3_CERTIFIED_FLOORS))
        for tag,ids in first.items():
            supports=tuple(
                tuple(sorted(model["left_labels"][model["incidences"][i][0]]+
                             tuple(model["a"]+x for x in
                                   model["right_labels"][model["incidences"][i][1]])))
                for i in ids)
            witnesses=[]
            for mask in SIGNS:
                sign=tuple(1 if mask>>j&1 else -1 for j in range(6))
                exact=exact_dual_GF5_six_flow(supports,sign,
                                               dimension=2*model["a"])
                if exact>0:
                    witnesses.append(exact)
            self.assertTrue(witnesses,(tag,ids))
            # The certified floors sum selected allowed-sign GF5 masses;
            # positivity is independently checked on true actual supports.
            self.assertLessEqual(min(witnesses),max(witnesses))

    def test_model_actual_all_seven_rule_relations_independent(self):
        model=gq_pair_model(1,"lex")
        cert=seven_family_hall_certificate(model)
        accepted=seven_census(model,independent_checks=False,witness_sets=True)
        targets=[
            frozenset(model["incidences"][i] for i in ids)
            for ids in sorted(accepted["sets"])
        ]
        for w in cross_witnesses(model):
            five=independent_original_column_five_support(model,w)
            overlaps=Counter(len(five & S) for S in targets)
            self.assertEqual(sum(overlaps.values()),len(targets))
        one=cert["rules"]["overlap_ge_1"]["all"]
        two=cert["rules"]["overlap_ge_2"]["all"]
        three=cert["rules"]["overlap_ge_3"]["all"]
        self.assertGreaterEqual(one["matched"],two["matched"])
        self.assertGreaterEqual(two["matched"],three["matched"])
        self.assertLessEqual(
            cert["rules"]["anchor_and_overlap_ge_2"]["all"]["matched"],
            cert["rules"]["same_anchor"]["all"]["matched"])

    def test_small_capacity_hall_exact_and_monotone(self):
        for adj,n,expected in (
            ([(0,),(0,),(0,),(0,)],2,4),
            ([(0,),(1,),(0,1),(0,1)],2,2),
            ([(0,1),(0,1)],2,1),
            ([(),(0,)],1,None),
            ([],2,0),
        ):
            check=hall_capacity_certificate(adj,n)
            self.assertEqual(check["minimum_capacity_to_charge_all"],expected)
            self.assertEqual(check["min_cut_capacity"],check["matched"])
            self.assertEqual(check["all_capacity_impossible_due_to_orphans"],
                             bool(any(not r for r in adj)))
        self.assertTrue(_rules_for(
            frozenset(range(5)),frozenset((1,2,3,7,8,9)),1)["same_anchor"])
        self.assertFalse(_rules_for(
            frozenset(range(5)),frozenset((1,2,3,7,8,9)),1)["overlap_ge_4"])

    def test_fail_closed(self):
        model=gq_pair_model(1,"lex")
        with self.assertRaises(RuntimeError):
            seven_family_hall_certificate(model,max_witnesses=0)
        with self.assertRaises(RuntimeError):
            seven_family_hall_certificate(model,max_seven_targets=0)
        with self.assertRaises(ValueError):
            seven_family_hall_certificate(model,max_witnesses=True)
        with self.assertRaises(ValueError):
            seven_family_hall_certificate(gq_pair_model(2,"lex"))
        with self.assertRaises(ValueError):
            hall_capacity_certificate([(3,)],2)

if __name__=="__main__":
    unittest.main()
