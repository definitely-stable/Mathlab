"""AA4-ERASE0 falsify true ORIGINAL W32 no-new-R3-event theorem.

This suite does NOT need any W34 source-local heuristic to prove the
mathematical invariant. On independently enumerated genuine W32
original GF5 physical 12D signed events, it checks that a safe
H_i(t)=0 new palette DELETES exactly the events incident to original
flag i and introduces NONE. Two consecutive actual original edits
are tested with fresh independent 14,190-three-source external scans.
The complete W34 proof lives in dedicated hosted checkpoint jobs.
"""
import unittest
from collections import Counter

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_w32_complete_r3_triple_sum_referee import committed_sevenclass_indices
from hyp105_w34_external_triple_r3_referee import exact_full_original_external_r3
from hyp105_w34_disjoint_fiveflag_r3_referee import (
    all_51_direct_disjoint_original_R3_costs,
)
from hyp105_w34_direct_r3_palette_derivative_referee import (
    all_51_exact_original_source_D2_cross_cost,
)
from hyp105_w34_zero_incidence_erasure_referee import (
    frozen_current_original_W34,canonical_event,_candidate_source_priority,
)


class TrueOriginalZeroNewR3Erasure(unittest.TestCase):
    def test_all_N_proof_two_consecutive_real_W32_signed_erasing_edits(self):
        model=pair_labeled_symplectic(1,"lex")
        indices=list(committed_sevenclass_indices()["lex"])
        full=exact_full_original_external_r3(
            model,tuple(indices),max_triples=14190,max_witnesses=40)
        events=list(full["verified_independent_true_source_witnesses"])
        r2=full["R2_signed_2v2_events_exact"]
        self.assertEqual(len(events),7)
        for round_id in range(2):
            if not events:break
            degree=Counter(j for w in events
                           for j in w["six_distinct_ORIGINAL_flag_IDs"])
            tested=0
            choice=None
            for source_id in sorted(degree,key=lambda i:(-degree[i],i)):
                tested+=1
                h=all_51_direct_disjoint_original_R3_costs(
                    model,tuple(indices),source_id,max_other_triples=13244)
                d2=all_51_exact_original_source_D2_cross_cost(
                    model,tuple(indices),source_id)
                prior=indices[source_id]
                self.assertEqual(h["current_source_TRUE_R3_incidence"],
                                 degree[source_id])
                self.assertEqual(d2["current_original_palette"],prior)
                safe=tuple(t for t in range(51)
                    if h["all_51_exact_TRUE_R3_incidence_counts"][t]==0 and
                    r2+d2["all_51_legal_source_D2_cross_counts"][t]-
                    d2["current_exact_D2_cross_count"]<=r2)
                if safe:
                    choice=(source_id,min(safe),h,d2)
                    break
            self.assertIsNotNone(choice)
            i,t,h,d2=choice
            old_events={canonical_event(w) for w in events}
            reduced={canonical_event(w) for w in events
                     if i not in w["six_distinct_ORIGINAL_flag_IDs"]}
            new_r2=(r2+d2["all_51_legal_source_D2_cross_counts"][t]
                    -d2["current_exact_D2_cross_count"])
            self.assertGreater(len(old_events),len(reduced))
            self.assertLessEqual(new_r2,r2)
            indices[i]=t
            independent=exact_full_original_external_r3(
                model,tuple(indices),max_triples=14190,max_witnesses=40)
            new_events=tuple(independent[
                "verified_independent_true_source_witnesses"])
            self.assertEqual({canonical_event(w) for w in new_events},reduced)
            self.assertEqual(len(new_events),len(reduced))
            self.assertEqual(independent[
                "FULL_six_distinct_original_ID_3v3_signed_event_count"],
                len(reduced))
            self.assertEqual(independent["R2_signed_2v2_events_exact"],new_r2)
            self.assertEqual(independent[
                "equal_sum_pairs_of_distinct_ORIGINAL_triples"],
                len(reduced)+41*new_r2)
            events=list(new_events)
            r2=new_r2

    def test_frozen_verified_both_real_W34_after_718_sources(self):
        for scheme,expected,original in (
            ("lex",(1,475,54),276),
            ("reverse-line",(0,61,61),285),
        ):
            with self.subTest(scheme=scheme):
                flags,risk=frozen_current_original_W34(scheme)
                self.assertEqual(risk,expected)
                self.assertEqual(len(flags),425)
                self.assertTrue(all(isinstance(x,int) and 0<=x<51
                                    for x in flags))
                self.assertEqual(flags[original],0 if scheme=="lex" else 3)

    def test_source_priority_handles_true_two_plus_two_source_endpoints(self):
        empty=[]
        r2=(((1,2),(3,4)),)
        ranks,degrees=_candidate_source_priority(empty,r2)
        self.assertEqual(set(ranks),{1,2,3,4})
        self.assertEqual(sum(degrees.values()),0)
        self.assertEqual(len(ranks),4)
        self.assertEqual(_candidate_source_priority([],())[0],())


if __name__=="__main__":
    unittest.main()
