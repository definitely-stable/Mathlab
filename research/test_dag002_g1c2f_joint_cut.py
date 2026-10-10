"""Independent tests for source-prefix, transcript and Hamming-ball cut."""
import itertools
import unittest
from math import comb
from dag002_g1c2f_joint_cut import (
    Cut, Witness, ChargedOldSource, ball_volume, hamming_ball, joint_cut,
    construct_matching_witness, independent_ancestor_dfs, verify_witness,
)


def brute_ball(n, w):
    return {v for v in range(1 << n) if v.bit_count() <= w}


def old_parent_graph(m, bitmask):
    return tuple(() for _ in range(m)) + (
        tuple(i for i in range(m) if bitmask & (1 << i)),)


class JointCutTests(unittest.TestCase):
    def test_independent_exact_ball_counts_and_no_duplicate_codes(self):
        for n in range(7):
            for w in range(n + 2):
                direct = brute_ball(n, w)
                self.assertEqual(set(hamming_ball(n, w)), direct)
                self.assertEqual(ball_volume(n, w), len(direct))
                self.assertEqual(ball_volume(n, w),
                                 sum(comb(n, j) for j in range(min(n,w) + 1)))

    def test_exact_all_history_vectors_are_complete_hypercube(self):
        for m in range(6):
            outputs = set()
            for old_mask in range(1 << m):
                graph = old_parent_graph(m, old_mask) + ((m,),)
                observed = sum(1 << i for i in range(m + 1)
                               if independent_ancestor_dfs(graph, i, m + 1))
                self.assertEqual(observed, (1 << m) | old_mask)
                outputs.add(observed)
            self.assertEqual(len(outputs), 1 << m)

    def test_two_necessary_cuts_are_independent_obstructions(self):
        # Enough new-record patterns, but the update transcript lacks a bit.
        a = joint_cut(4, 1, 2, 5, 2)
        self.assertEqual(a.target_vectors, 16)
        self.assertEqual(a.read_transcript_cap, 8)
        self.assertGreaterEqual(a.new_record_cap, 16)
        self.assertFalse(a.allowed_by_cuts)
        # Enough old-source probes; too few changed fresh-record patterns.
        b = joint_cut(4, 0, 4, 3, 1)
        self.assertEqual(b.read_transcript_cap, 16)
        self.assertEqual(b.new_record_cap, 4)
        self.assertFalse(b.allowed_by_cuts)
        self.assertIsNone(construct_matching_witness(4,0,4,3,1))

    def test_matching_promise_family_for_all_small_resource_parameters(self):
        for m in range(6):
            for h in range(m + 1):
                r=m-h
                for n in range(6):
                    for w in range(n + 1):
                        cut=joint_cut(m,h,r,n,w)
                        cert=construct_matching_witness(m,h,r,n,w)
                        self.assertEqual(cert is not None, cut.allowed_by_cuts)
                        if cert is not None:
                            self.assertTrue(verify_witness(cert,r))
                            self.assertLessEqual(max(v.bit_count()
                                for v in cert.codewords),w)

    def test_extra_read_budget_does_not_create_a_free_program_channel(self):
        for m,h,n,w in ((3,1,3,1),(4,2,2,2),(2,0,2,2)):
            need=m-h
            cert=construct_matching_witness(m,h,need+3,n,w)
            self.assertIsNotNone(cert)
            self.assertEqual(cert.update_probes,need)
            self.assertTrue(verify_witness(cert,need+3))
            self.assertFalse(verify_witness(cert,need-1))

    def test_charged_prehistory_local_bits_and_fresh_target_semantics(self):
        cert=construct_matching_witness(3,1,2,3,1)
        self.assertTrue(verify_witness(cert,2))
        retained = cert.retained_state_from_prior_append(0b101)
        source = ChargedOldSource(0b101, 3, 2)
        local, word = cert.update_charged(retained, source.read_bit)
        self.assertEqual(local, 1)
        self.assertEqual(source.reads, 2)
        self.assertEqual(source.addresses, (1, 2))
        self.assertEqual(cert.query_vector(local, word), 0b1101)
        with self.assertRaises(ValueError):
            cert.retained_state_from_prior_append(1 << 3)
        with self.assertRaises(ValueError):
            cert.query_vector(1,7)

    def test_updater_cannot_bypass_charged_old_source_channel(self):
        cert = construct_matching_witness(3, 1, 2, 3, 1)
        seen = []
        def one_bit_only(address):
            self.assertIn(address, (1, 2))
            seen.append(address)
            return (0b110 >> address) & 1
        local, remote = cert.update_charged(0, one_bit_only)
        self.assertEqual(seen, [1, 2])
        self.assertEqual(cert.query_vector(local, remote), 0b1110)

        insufficient = ChargedOldSource(0b110, 3, 1)
        with self.assertRaises(ValueError):
            cert.update_charged(0, insufficient.read_bit)
        self.assertEqual(insufficient.reads, 1)
        self.assertEqual(insufficient.addresses, (1,))

        corrupted = ChargedOldSource(0b110, 3, 2)
        with self.assertRaises(ValueError):
            corrupted.read_bit(4)
        self.assertEqual(corrupted.reads, 0)
        with self.assertRaises(ValueError):
            cert.update_charged(2, corrupted.read_bit)

    def test_corrupt_or_overpriced_certificate_rejected(self):
        cert=construct_matching_witness(3,1,2,3,1)
        self.assertIsNotNone(cert)
        tampered=Witness(3,1,2,3,1,(0,1,1,4))
        self.assertFalse(verify_witness(tampered,2))
        overweight=Witness(3,1,2,3,1,(0,1,2,3))
        self.assertFalse(verify_witness(overweight,2))
        self.assertFalse(verify_witness(cert,1))
        self.assertFalse(verify_witness(None,3))

    def test_necessary_cut_does_not_claim_general_query_lower_bound(self):
        # An older adjacency record is one additional query-side source:
        # from old 0->1 and same next command (1), reach(0,2) differs.
        first=((),())
        second=((),(0,))
        for old, outcome in ((first,False),(second,True)):
            graph=old+((1,),)
            self.assertEqual(independent_ancestor_dfs(graph,0,2),outcome)
        self.assertNotEqual(first,second)

    def test_invalid_dimensions_and_out_of_scope_enumerator(self):
        for args in ((-1,0,0,0,0),(2,3,0,0,0),
                     (2,0,-1,0,0),(2,0,0,0,True),
                     (0,0,0,10001,1)):
            with self.assertRaises(ValueError):
                joint_cut(*args)
        with self.assertRaises(ValueError):
            hamming_ball(13,1)
        with self.assertRaises(ValueError):
            ball_volume(2,-1)


if __name__=="__main__":
    unittest.main()
