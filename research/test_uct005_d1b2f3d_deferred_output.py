"""Independent exhaustive cut/count and abstract code falsifiers for F3-D."""
import itertools
import unittest

from uct005_d1b2f3d_deferred_output import (
    PhaseCut, abstract_deferred_output_upper,
)


class DeferredOutputCutTests(unittest.TestCase):
    def test_exact_integer_pigeonhole_threshold_independent_arithmetic(self):
        for N in range(1,81):
            for P in (1,2,4):
                for lam,b,w,a in ((0,0,0,0),(8,0,0,0),
                                  (0,7,0,0),(4,4,1,0),
                                  (3,6,0,5),(256,0,0,0)):
                    base=PhaseCut(N,P,lam,b,w,0,a)
                    W=8*P
                    q=max(0, -((-(N-1-lam-b-W*w-a))//W))
                    self.assertEqual(base.required_postauth_pages_if_stage_frozen,q)
                    for r in (max(0,q-1),q,q+1):
                        x=PhaseCut(N,P,lam,b,w,r,a)
                        expected=lam+b+W*(w+r)+a>=N-1
                        self.assertEqual(
                            x.exact_reconstruction_not_ruled_out_by_counting,
                            expected)
                        self.assertEqual(x.provably_insufficient_bits,
                                         max(0,N-1-(lam+b+W*(w+r)+a)))
                        if q>0 and r==q-1:
                            self.assertFalse(
                                x.exact_reconstruction_not_ruled_out_by_counting)
                        if r==q:
                            self.assertTrue(
                                x.exact_reconstruction_not_ruled_out_by_counting)

    def test_exhaustive_all_fixed_target_words_abstract_upper_witnesses(self):
        for N,P,lam,b,Q in (
            (8,1,0,7,0),
            (8,1,0,0,1),
            (16,1,2,5,1),
            (16,1,7,0,1),
            (16,1,0,7,1),
            (16,2,0,15,0),
            (16,2,2,13,0),
            (16,2,256,0,0),
        ):
            with self.subTest(N=N,P=P,lam=lam,b=b,Q=Q):
                z=abstract_deferred_output_upper(N,P,lam,b,Q)
                self.assertEqual(z["unique_transcripts"],1 << (N-1))
                self.assertEqual(z["independently_enumerated_fixed_target_inputs"],
                                 1 << (N-1))
                self.assertTrue(z["all_output_words_match_exactly"])
                self.assertTrue(z["not_an_authenticated_protocol"])
                self.assertEqual(z["root_novelty"],"OPEN_UNPROVED")

    def test_onepass_speculation_is_a_different_paid_axis(self):
        # No digest, RAM or post-auth reads can encode seven free input
        # bits, but one complete P-byte pre-auth external stage CAN carry
        # enough bits under the relaxed side-effect contract.
        no_stage=PhaseCut(8,1,0,0,0,0)
        yes_stage=PhaseCut(8,1,0,0,1,0)
        self.assertFalse(no_stage.exact_reconstruction_not_ruled_out_by_counting)
        self.assertTrue(yes_stage.exact_reconstruction_not_ruled_out_by_counting)
        self.assertEqual(no_stage.required_postauth_pages_if_stage_frozen,1)
        self.assertEqual(yes_stage.required_postauth_pages_if_stage_frozen,0)
        self.assertEqual(yes_stage.report()["W_pre"],1)

    def test_digest_and_authority_state_are_not_free(self):
        vacuous=PhaseCut(16,1,256,0,0,0)
        self.assertTrue(vacuous.exact_reconstruction_not_ruled_out_by_counting)
        self.assertEqual(vacuous.required_postauth_pages_if_stage_frozen,0)
        short=PhaseCut(80,1,8,8,0,0)
        self.assertFalse(short.exact_reconstruction_not_ruled_out_by_counting)
        self.assertEqual(short.required_postauth_pages_if_stage_frozen,8)
        self.assertTrue(short.report()["necessary_not_sufficient"])
        self.assertFalse(short.report()["full_Pareto_or_new_UCT_lower_bound"])

    def test_data_dependent_addresses_and_advice_must_be_paid(self):
        without=PhaseCut(16,2,0,0,0,0,0)
        hidden_bits=PhaseCut(16,2,0,0,0,0,15)
        self.assertFalse(without.exact_reconstruction_not_ruled_out_by_counting)
        self.assertTrue(hidden_bits.exact_reconstruction_not_ruled_out_by_counting)
        self.assertFalse(hidden_bits.report()["cryptographic_SHA_or_physical_powerloss_claim"])

    def test_abstract_witness_does_not_claim_actual_sha_encoding(self):
        with self.assertRaises(ValueError):
            abstract_deferred_output_upper(16,1,0,6,1)
        with self.assertRaises(ValueError):
            abstract_deferred_output_upper(9,1,0,8,0)
        with self.assertRaises(ValueError):
            abstract_deferred_output_upper(24,1,0,23,0)
        with self.assertRaises(ValueError):
            abstract_deferred_output_upper(8,1,0,7,2)

    def test_invalid_resource_vocabulary_fails_fast(self):
        for args in ((0,1,0,0,0,0), (8,0,0,0,0,0),
                     (8,1,-1,0,0,0), (8,1,1,-1,0,0),
                     (8,1,1,0,-1,0), (8,1,1,0,0,-1),
                     (8,1,1,0,0,0,-1), (1<<20|1,1,0,0,0,0)):
            with self.subTest(args=args),self.assertRaises(ValueError):
                PhaseCut(*args)
        with self.assertRaises(ValueError):
            PhaseCut(8,True,0,0,0,0)


if __name__=="__main__":
    unittest.main()
