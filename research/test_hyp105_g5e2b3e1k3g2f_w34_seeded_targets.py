"""Independent generic accepted-seven classifier and W34 positive target search."""
from collections import Counter
from itertools import combinations
import unittest

from hyp105_g5e2b3e1k1_kikuchi_c6 import gq_pair_model,kikuchi_graph
from hyp105_g5e2b3e1b0_seven_signature import (
    seven_census,classify_seven_prechecked,R3_CERTIFIED_FLOORS
)
from hyp105_g5e2b3e1a_fixed_leading import selected_left_six
from hyp105_g5e2b3e1k3g2f_w34_seeded_targets import (
    generic_seven_family,seed_pair_completion,targeted_seven_hall_probe
)


class K3G2FW34TargetTests(unittest.TestCase):
    def test_generic_all_s_classifier_entire_w32_left_finite_census(self):
        # The new all-a structural predicate must agree for ALL 62,370
        # original source sixsets in B0's independent W32 enumerator.
        for scheme in ("lex","reverse-line"):
            model=gq_pair_model(1,scheme)
            expected=seven_census(model,independent_checks=False,
                                  witness_sets=True)["sets"]
            hist=Counter()
            total=0
            for ids,left_type in selected_left_six(model):
                generic=generic_seven_family(model,ids)
                old=classify_seven_prechecked(
                    ids,model["left_labels"],
                    model["right_labels"],model["incidences"])
                self.assertEqual(generic,old)
                self.assertEqual(generic,expected.get(ids))
                if generic:
                    hist[generic]+=1
                total+=1
            self.assertEqual(total,62370)
            self.assertEqual(sum(hist.values()),len(expected))

    def test_w32_seeded_completion_is_exact_where_untruncated(self):
        for scheme in ("lex","reverse-line"):
            model=gq_pair_model(1,scheme)
            accepted=seven_census(model,independent_checks=False,
                                  witness_sets=True)["sets"]
            witnesses={}
            for cols,kind in accepted.items():
                witnesses.setdefault(kind,cols)
            self.assertEqual(set(witnesses),set(R3_CERTIFIED_FLOORS))
            for kind,six in witnesses.items():
                i,j=sorted(six)[:2]
                attempt=seed_pair_completion(
                    model,i,j,max_nodes=250000,max_targets=1000)
                self.assertTrue(attempt["complete"],(scheme,kind,attempt["reason"]))
                self.assertEqual(attempt["reason"],"exhaustive")
                expected={ids:tag for ids,tag in accepted.items()
                          if i in ids and j in ids}
                self.assertEqual(dict(attempt["targets"]),expected)
                self.assertIn((six,kind),attempt["targets"])

    def test_w34_finite_positive_only_and_exact_gf5_family_validation(self):
        for scheme,seed in (("lex",None),("random",20261012)):
            m=gq_pair_model(2,scheme,seed)
            result=targeted_seven_hall_probe(
                m,witness_limit=4,seed_pairs_per_witness=2,
                max_nodes_per_seed=20000,max_targets_per_seed=12)
            self.assertEqual(result["s"],4)
            self.assertEqual(result["tested_witnesses"],4)
            self.assertLessEqual(result["tested_witnesses"],
                                 result["all_Jcross_witnesses"])
            self.assertEqual(result["source_seed_pair_attempts"],8)
            self.assertEqual(result["unit_capacity_maximum_injection"]+
                             result["unmatched_selected_witnesses"],4)
            self.assertEqual(len(result["constructive_assignment_sha256"]),64)
            self.assertTrue(all(
                generic_seven_family(m,cols)==tag and
                R3_CERTIFIED_FLOORS[tag]>0
                for cols,tag in result["positive_targets_sample"]))
            self.assertFalse(result["failure_of_universal_overlap_rule_proved"])
            self.assertFalse(result["all_h_S_omega_s6_proved"])
            self.assertLessEqual(result["unit_capacity_maximum_injection"],
                                 result["discovered_true_positive_sixsets"])
            if result["truncated_seed_searches"]:
                self.assertFalse(result["search_complete_for_all_seed_pairs_tested"])
            self.assertFalse(result["search_complete_for_all_possible_seed_pairs"])

    def test_genuine_w34_targets_have_strict_positive_exact_GF5_signed_mass(self):
        # Independently pin true W(3,4) accepted targets, discovered by
        # the first exact-head hosted seeded search, WITHOUT reusing its
        # search output or its positive class score.
        from hyp105_g5e2b3b1_critical_flows import SIGNS
        from hyp105_g5e2b3b1b_five_six_flows import exact_dual_GF5_six_flow
        cases=(
            ("lex",None,(0,41,68,139,189,206),"B-left/A-right"),
            ("random",20261012,(0,140,141,197,209,420),"A-left/B-right"),
            ("random",20261012,(2,3,284,334,341,379),"B/B-disjoint"),
        )
        for scheme,seed,ids,expected in cases:
            model=gq_pair_model(2,scheme,seed)
            tag=generic_seven_family(model,ids)
            self.assertEqual(tag,expected)
            a=model["a"]
            supports=[]
            for col in ids:
                p,l=model["incidences"][col]
                support=tuple(sorted(model["left_labels"][p]+tuple(
                    a+x for x in model["right_labels"][l])))
                self.assertEqual(len(set(support)),4)
                supports.append(support)
            weights=[]
            for mask in SIGNS:
                sign=tuple(1 if mask>>j&1 else -1 for j in range(6))
                weights.append(exact_dual_GF5_six_flow(
                    supports,sign,dimension=2*a))
            self.assertEqual(len(weights),10)
            self.assertGreater(min(weights),0)
            self.assertGreaterEqual(sum(weights),R3_CERTIFIED_FLOORS[tag])

    def test_large_model_canonical_physical_gauges(self):
        model=gq_pair_model(2,"lex")
        a=model["a"]
        px=list(reversed(range(a)))
        py=[(i+3)%a for i in range(a)]
        renamed=dict(model)
        renamed["left_labels"]=tuple(
            tuple(sorted((px[x],px[y]))) for x,y in model["left_labels"])
        renamed["right_labels"]=tuple(
            tuple(sorted((py[x],py[y]))) for x,y in model["right_labels"])
        for six in (
            tuple(range(6)),
            tuple(range(0,12,2)),
            tuple(range(10,16)),
            (1,24,78,120,221,400),
        ):
            self.assertEqual(generic_seven_family(model,six),
                             generic_seven_family(renamed,six))

    def test_budgets_and_truncation_do_not_prove_negative(self):
        model=gq_pair_model(1,"lex")
        p=seed_pair_completion(model,0,1,max_nodes=0)
        self.assertFalse(p["complete"])
        self.assertEqual(p["reason"],"node_budget")
        self.assertEqual(p["targets"],())
        with self.assertRaises(ValueError):
            seed_pair_completion(model,0,0)
        with self.assertRaises(ValueError):
            seed_pair_completion(model,0,1,max_nodes=True)
        with self.assertRaises(ValueError):
            seed_pair_completion(model,0,1,max_targets=0)
        with self.assertRaises(ValueError):
            generic_seven_family(model,(0,0,1,2,3,4))
        with self.assertRaises(ValueError):
            targeted_seven_hall_probe(model,witness_limit=0)
        with self.assertRaises(ValueError):
            targeted_seven_hall_probe(model,seed_pairs_per_witness=11)

if __name__=="__main__":
    unittest.main()
