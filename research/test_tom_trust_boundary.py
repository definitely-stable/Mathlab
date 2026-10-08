"""TOM-003: all finite Boolean functions + exact trust-cost counterexamples."""
from itertools import product
import unittest

from tom_trust_boundary import (
    PromisedOldBitSummary, essential_mask,
    full_overwrite_state_bits, future_equivalence_partition,
    oracle_report, threshold_truth_table, trusted_counter_state_bits,
    untrusted_count_alias, value, write,
)


class TOM003Tests(unittest.TestCase):
    def test_all_256_three_bit_functions_moore_quotient(self):
        expected = {
            1: [2, 2],
            2: [2, 4, 10],
            3: [2, 6, 30, 218],
        }
        for n, histogram in expected.items():
            result=oracle_report(n)
            self.assertEqual(result["truth_tables_checked"],2**(2**n))
            self.assertEqual(result["essential_histogram"],histogram)
            self.assertTrue(result["all_full_overwrite_quotients_match"])

    def test_fully_essential_and_xor_threshold_need_full_input_without_old(self):
        for n in (1,2,3,4):
            and_tt=1 << ((1 << n)-1)
            xor_tt=sum(1<<x for x in range(1<<n) if x.bit_count()%2)
            for table in (and_tt,xor_tt,threshold_truth_table(n,1),
                          threshold_truth_table(n,n)):
                self.assertEqual(essential_mask(n,table),(1<<n)-1)
                self.assertEqual(full_overwrite_state_bits(n,table),n)
            # This test does not claim a new theorem or nontrivial
            # lower bound for any weaker update model.
            self.assertEqual(trusted_counter_state_bits(n),n.bit_length())

    def test_nonessential_variables_are_ignored_exactly(self):
        for n in (2,3,4):
            table=sum(1<<x for x in range(1<<n) if x&1)
            self.assertEqual(essential_mask(n,table),1)
            self.assertEqual(full_overwrite_state_bits(n,table),1)
        for n in (1,2,3):
            for table in (0,(1<<(1<<n))-1):
                self.assertEqual(essential_mask(n,table),0)
                labels,_=future_equivalence_partition(n,table)
                self.assertEqual(len(set(labels)),1)

    def test_untrusted_same_count_alias_root_divergence(self):
        alias=untrusted_count_alias()
        self.assertTrue(alias["same_initial_root"])
        self.assertEqual(alias["same_initial_count"],2)
        self.assertEqual(set(alias["post_roots"]),{0,1})
        self.assertTrue(alias["requires_external_old_bit_check"])
        # The proof does NOT rely on a hash collision.
        self.assertNotEqual(*alias["initial_states"])

    def test_trusted_delta_all_initial_values_three_updates(self):
        for n in (1,2,3,4):
            for threshold in range(1,n+1):
                for start in range(1<<n):
                    for writes in product(range(2*n),repeat=3):
                        x=start
                        summary=PromisedOldBitSummary(n,threshold,x.bit_count())
                        self.assertEqual(summary.root(),x.bit_count()>=threshold)
                        for action in writes:
                            i,new=divmod(action,2)
                            old=(x>>i)&1
                            y=write(n,x,i,new)
                            expected_changed=(x.bit_count()>=threshold)!=(y.bit_count()>=threshold)
                            summary,changed=summary.apply_assuming_verified_old(old,new)
                            self.assertEqual(changed,expected_changed)
                            self.assertEqual(summary.ones,y.bit_count())
                            self.assertEqual(summary.root(),y.bit_count()>=threshold)
                            x=y

    def test_promised_old_unchecked_is_not_a_safe_product(self):
        # Counter summary is unable to detect incorrect 'old', even
        # when numerical count stays within valid 0..n.
        n, threshold = 3,2
        actual=0b101  # count=2; old bit at index 1 is 0
        summary=PromisedOldBitSummary(n,threshold,2)
        new_summary,changed=summary.apply_assuming_verified_old(1,0)
        actual=write(n,actual,1,0)
        self.assertNotEqual(new_summary.ones,actual.bit_count())
        self.assertTrue(changed)
        self.assertTrue(actual.bit_count()>=threshold)

    def test_invalid_arguments_rejected(self):
        for n,tt in ((0,0),(3,-1),(3,1<<8),(True,0),(3,1.0)):
            with self.assertRaises(ValueError):
                essential_mask(n,tt)
        for n,x,i,b in ((3,0,3,1),(3,0,1,2),(3,8,0,1),
                         (3,0,True,1),(3,0,0,True)):
            with self.assertRaises(ValueError):
                write(n,x,i,b)
        for kw in ({"length":0,"threshold":1,"ones":0},
                   {"length":3,"threshold":4,"ones":0},
                   {"length":3,"threshold":2,"ones":4}):
            with self.assertRaises(ValueError):
                PromisedOldBitSummary(**kw)
        with self.assertRaises(ValueError):
            PromisedOldBitSummary(3,2,0).apply_assuming_verified_old(1,0)
        with self.assertRaises(ValueError):
            PromisedOldBitSummary(3,2,3).apply_assuming_verified_old(0,1)
        with self.assertRaises(ValueError):
            PromisedOldBitSummary(3,2,2).apply_assuming_verified_old(True,0)


if __name__=="__main__":
    unittest.main()
