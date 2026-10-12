"""Independent exact-delta locality and fail-closed correlated search tests."""
import unittest

from hyp105_g5e2b3e1k1_kikuchi_c6 import gq_pair_model
from hyp105_g5e2b3e1b0_seven_signature import seven_census
from hyp105_g5e2b3e1k3g2h_exact_swap_shell import full_target_hall
from hyp105_g5e2b3e1k3g2i_correlated_delta import (
    ExactSevenDelta, independent_full_replay, correlated_search, _labels_digest,
)


class K3G2ICorrelatedExactDeltaTests(unittest.TestCase):
    def test_left_and_right_original_support_locality(self):
        base=gq_pair_model(1,"lex")
        state=ExactSevenDelta(base)
        self.assertEqual(state.S,259)
        self.assertEqual(state.GF5_numerator,11225795)
        original=state.eligible
        for side,i,j in (("right",2,11),("left",1,14),
                         ("right",0,14),("left",3,9)):
            before=state
            state,delta=state.transition(side,i,j)
            self.assertEqual(delta["original_columns_touched"],6)
            self.assertEqual(delta["S_before"],before.S)
            self.assertEqual(delta["S_after"],state.S)
            self.assertGreater(delta["old_candidates_affected"],0)
            self.assertLessEqual(delta["new_candidates_affected"],62370)
            if side=="right":
                self.assertIs(state.eligible,before.eligible)
            else:
                self.assertEqual(len(state.eligible),62370)
            exact=seven_census(state.model,witness_sets=True,
                               independent_checks=False)
            self.assertEqual(state.tags,exact["sets"])
            self.assertEqual(state.GF5_numerator,
                             exact["GF5_seven_lower_numerator"])
            hall=independent_full_replay(state)
            self.assertEqual(hall["S_seven_exact"],len(state.tags))
            self.assertEqual(hall["matched"]+hall["hall_deficiency"],
                             hall["Jcross"])
        self.assertEqual(len(original),62370)

    def test_composed_transpositions_preserve_valid_global_pair_bijections(self):
        base=gq_pair_model(1,"lex")
        state=ExactSevenDelta(base)
        for side,i,j in (("left",1,14),("right",2,11),
                         ("left",3,9),("right",1,8)):
            state,_=state.transition(side,i,j)
            for s in ("left","right"):
                self.assertEqual(set(state.model[s+"_labels"]),
                                 set(base[s+"_labels"]))
                self.assertEqual(len(set(state.model[s+"_labels"])),15)
            self.assertEqual(base["incidences"],state.model["incidences"])
        self.assertNotEqual(_labels_digest(base),_labels_digest(state.model))
        self.assertEqual(independent_full_replay(state)["S_seven_exact"],state.S)

    def test_small_correlated_adversary_deterministic_full_oracle(self):
        kw=dict(steps=2,proposals_per_step=3,seed=20261012,
                anchor_limit=1)
        a=correlated_search(**kw)
        b=correlated_search(**kw)
        self.assertEqual(a,b)
        self.assertEqual(a["anchors_tested"],1)
        self.assertEqual(a["candidate_transitions_exactly_scored"],6)
        self.assertEqual(a["committed_states_independently_full_replayed"],3)
        self.assertEqual(a["results"][0]["committed_moves"],2)
        self.assertEqual(len(a["selected_path_certificate_sha256"]),64)
        self.assertFalse(a["full_W32_labeling_space_exhausted"])
        self.assertFalse(a["all_h_universal_Hall_proved"])
        self.assertFalse(a["all_h_S_omega_proved"])
        for row in a["results"][0]["path"]:
            self.assertEqual(row["GF5_floor_numerator"]>0,True)
            self.assertEqual(len(row["labels_sha256"]),64)
            self.assertGreaterEqual(row["S_seven_exact"],0)
            if row["Hall_deficiency"]:
                self.assertFalse(row["full_Hall_unit"])
                self.assertGreater(
                    row["Hall_cut_witness_subset"],
                    row["Hall_cut_neighbor_size"])
            else:
                self.assertTrue(row["full_Hall_unit"])

    def test_invalid_budgets_and_model_fail_closed(self):
        for args in (
            {"steps":0},{"steps":11},{"steps":True},
            {"proposals_per_step":0},{"proposals_per_step":106},
            {"proposals_per_step":True},{"seed":True},
            {"anchor_limit":0},{"anchor_limit":4},
            {"anchor_limit":True}
        ):
            with self.subTest(args=args),self.assertRaises(ValueError):
                correlated_search(**args)
        base=ExactSevenDelta(gq_pair_model(1,"lex"))
        for side,i,j in (
            ("invalid",0,1),("left",0,0),("right",-1,0),
            ("left",14,15),("right",True,9)):
            with self.subTest(side=side,i=i,j=j),self.assertRaises(ValueError):
                base.transition(side,i,j)


if __name__=="__main__":
    unittest.main()
