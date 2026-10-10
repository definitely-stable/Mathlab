"""Independent finite falsifiers for classical PIN-history observation entropy."""
import itertools
from math import comb
import unittest

from uct005_d1c0_observation_entropy import (
    ball_volume, checked_epochs, distinguishable_tuples,
    exact_minimum_fixed_bits, rank_observations, unrank_observations,
    finite_canonical_paths, independent_observation_oracle,
    independent_labeled_receipt_oracle, labeled_SET_transcript_count,
)


class MultiEpochObservationalEntropyTests(unittest.TestCase):
    def test_all_subsets_all_short_binary_update_paths(self):
        # Indep transition oracle enumerates legal flip/no-op SET outcomes.
        # This is stronger than the two-reader fixed snapshot of actual F1;
        # no output-bound transfer to physical pages is claimed.
        for n in range(1,6):
            for H in range(4):
                for mask in range(1,1<<(H+1)):
                    times=tuple(i for i in range(H+1) if mask&(1<<i))
                    with self.subTest(n=n,H=H,times=times):
                        z=independent_observation_oracle(n,H,times)
                        expect=(1<<n)
                        for a,b in zip(times,times[1:]):
                            expect*=sum(comb(n,j) for j in range(min(n,b-a)+1))
                        self.assertEqual(z["distinct_answer_tuples"],expect)
                        self.assertEqual(z["exact_minimum_fixed_code_bits"],
                                         (expect-1).bit_length())
                        self.assertTrue(z["rank_unrank_bijection"])
                        self.assertTrue(z["counting_only_not_physical_F1_storage_or_verified_cost"])
                        self.assertEqual(z["root_novelty"],"OPEN_UNPROVED")

    def test_d1_two_pins_latest_and_all_epoch_false_independent_entropy(self):
        n,H=5,3
        both=independent_observation_oracle(n,H,(0,2,3))
        allv=independent_observation_oracle(n,H,(0,1,2,3))
        self.assertEqual(both["distinct_answer_tuples"],3072)
        self.assertEqual(both["exact_minimum_fixed_code_bits"],12)
        self.assertEqual(both["independent_snapshot_bits_upper_naive"],15)
        self.assertEqual(allv["distinct_answer_tuples"],6912)
        self.assertEqual(allv["exact_minimum_fixed_code_bits"],13)
        self.assertEqual(allv["independent_snapshot_bits_upper_naive"],20)
        # A proposed universal k*n independent bits of storage for k pins
        # cannot follow from observable answer entropy of sparse SET paths.
        self.assertLess(both["exact_minimum_fixed_code_bits"],15)
        self.assertLess(allv["exact_minimum_fixed_code_bits"],20)

    def test_fixed_known_noop_epoch_is_different_public_contract(self):
        for n in range(1,6):
            observed=set()
            for path in finite_canonical_paths(n,3):
                if path[1]==path[2]:  # known no-op SET at epoch 2
                    observed.add((path[0],path[2],path[3]))
            self.assertEqual(len(observed),(1<<n)*(n+1)**2)
            self.assertLessEqual(len(observed),distinguishable_tuples(n,(0,2,3)))

    def test_distinct_author_SET_receipts_not_free_and_not_bitmap_entropy(self):
        # Different labeled no-op SETs yield the SAME bitmap but DIFFERENT
        # author's operation records. Cryptographic proofs remain unpriced.
        for n in range(1,5):
            for H in range(4):
                with self.subTest(n=n,H=H):
                    z=independent_labeled_receipt_oracle(n,H)
                    self.assertEqual(
                        z["distinct_initial_plus_labeled_SET_transcripts"],
                        (1<<n)*(2*n)**H)
                    self.assertEqual(z["distinct_bitmap_answer_paths_only"],
                                     (1<<n)*(n+1)**H)
                    self.assertTrue(z["update_labels_must_be_accounted_not_treated_as_free"])
                    self.assertFalse(z["authenticated_receipt_and_wire_bytes_priced"])
                    self.assertEqual(z["root_novelty"],"OPEN_UNPROVED")
        self.assertEqual(labeled_SET_transcript_count(5,3),32*10**3)
        with self.assertRaises(ValueError):
            labeled_SET_transcript_count(0,1)
        with self.assertRaises(ValueError):
            independent_labeled_receipt_oracle(5,3)

    def test_singleton_range_parity_fully_distinguishes_bitmaps(self):
        for n in range(1,6):
            for x in range(1<<n):
                bits=tuple((x>>i)&1 for i in range(n))
                def range_parity(lo,hi):
                    return sum(bits[lo:hi])&1
                recovered=sum(range_parity(i,i+1)<<i for i in range(n))
                self.assertEqual(recovered,x)
                for lo in range(n):
                    for hi in range(lo+1,n+1):
                        self.assertEqual(range_parity(lo,hi),
                                         (recovered>>lo & ((1<<(hi-lo))-1)).bit_count()&1)

    def test_closed_form_full_history_all_n_H_and_encoding_ceiling(self):
        for n in (1,2,3,5,12,64):
            for H in (0,1,2,3,8):
                times=tuple(range(H+1))
                cnt=distinguishable_tuples(n,times)
                self.assertEqual(cnt,(1<<n)*(n+1)**H)
                self.assertEqual(exact_minimum_fixed_bits(cnt),(cnt-1).bit_length())
                self.assertEqual(ball_volume(n,0),1)
                self.assertEqual(ball_volume(n,1),n+1)
                self.assertEqual(ball_volume(n,n),1<<n)

    def test_rank_unrank_sparse_observation_high_gap(self):
        n=5
        times=(1,3,5)
        count=distinguishable_tuples(n,times)
        for rank in range(count):
            snapshots=unrank_observations(n,times,rank)
            self.assertEqual(rank_observations(n,times,snapshots),rank)
        self.assertEqual(count,(1<<n)*ball_volume(n,2)**2)

    def test_reject_invalid_epoch_and_unreachable_snapshot(self):
        for times in ((),(-1,0),(0,0),(2,1),[0,1],(0,True)):
            with self.subTest(times=times),self.assertRaises(ValueError):
                checked_epochs(times)
        with self.assertRaises(ValueError):
            ball_volume(0,1)
        with self.assertRaises(ValueError):
            ball_volume(4,-1)
        with self.assertRaises(ValueError):
            distinguishable_tuples(0,(0,))
        with self.assertRaises(ValueError):
            rank_observations(4,(0,1),(0,15))
        with self.assertRaises(ValueError):
            rank_observations(4,(0,1),(0,))
        with self.assertRaises(ValueError):
            rank_observations(4,(0,1),(0,True))
        with self.assertRaises(ValueError):
            unrank_observations(4,(0,1),-1)
        with self.assertRaises(ValueError):
            unrank_observations(4,(0,1),distinguishable_tuples(4,(0,1)))
        with self.assertRaises(ValueError):
            independent_observation_oracle(3,2,(0,3))
        with self.assertRaises(ValueError):
            finite_canonical_paths(8,1).__next__()
        with self.assertRaises(ValueError):
            exact_minimum_fixed_bits(0)


if __name__=="__main__":
    unittest.main()
