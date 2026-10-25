"""Tests for W(3,4) adversarial minimization and evaluator correctness."""
import unittest

from hyp105_issue230_projection import fixture, ProjectionClosure
from hyp105_issue230_d5_retained_energy import true_spread_global_model
from hyp105_w34_adversarial_search import (
    FastW34Evaluator,
    run_greedy_swap_descent,
    run_simulated_annealing,
)


class TestW34AdversarialSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.evaluator = FastW34Evaluator()

    def test_01_baseline_exact_agreement_with_projection_closure(self):
        """Verify FastW34Evaluator exactly matches ProjectionClosure.census() on lex and spread."""
        m_lex = fixture(2, 'lex')
        c_lex = ProjectionClosure(m_lex).census()
        fast_lex = self.evaluator.full_census(m_lex['left_labels'], m_lex['right_labels'])

        self.assertEqual(fast_lex['synchronized_BBo'], c_lex['synchronized_BBo'])
        self.assertEqual(fast_lex['proper_P3'], c_lex['proper_P3'])
        self.assertEqual(fast_lex['missing'], c_lex['missing'])
        self.assertEqual(fast_lex['incident'], c_lex['incident'])
        self.assertEqual(fast_lex['blocked'], c_lex['blocked'])
        self.assertEqual(fast_lex['unblocked'], c_lex['unblocked'])
        self.assertEqual(fast_lex['synchronized_BBo'], 7532)

        m_spread, _, _, _ = true_spread_global_model(2, 'balanced')
        c_spread = ProjectionClosure(m_spread).census()
        fast_spread = self.evaluator.full_census(m_spread['left_labels'], m_spread['right_labels'])

        self.assertEqual(fast_spread['synchronized_BBo'], c_spread['synchronized_BBo'])
        self.assertEqual(fast_spread['unblocked'], c_spread['unblocked'])
        self.assertEqual(fast_spread['synchronized_BBo'], 7649)

    def test_02_random_seed_exact_agreement(self):
        """Verify FastW34Evaluator matches ProjectionClosure on fixture(2, 'random')."""
        m_rand = fixture(2, 'random')
        c_rand = ProjectionClosure(m_rand).census()
        fast_rand = self.evaluator.full_census(m_rand['left_labels'], m_rand['right_labels'])
        self.assertEqual(fast_rand['synchronized_BBo'], c_rand['synchronized_BBo'])
        self.assertEqual(fast_rand['synchronized_BBo'], 8021)

    def test_03_short_greedy_descent_strictly_decreases_bbo(self):
        """Verify that greedy descent achieves strict reduction from lex."""
        m_lex = fixture(2, 'lex')
        res = run_greedy_swap_descent(self.evaluator, m_lex['left_labels'], m_lex['right_labels'],
                                      max_steps=50, patience=50, rng_seed=42)
        self.assertLess(res['final_bbo'], res['initial_bbo'])
        self.assertGreater(res['accepted_swaps'], 0)
        # BBo must stay strictly positive
        self.assertGreater(res['final_bbo'], 0)

    def test_04_universal_positive_floor(self):
        """Verify BBo remains bounded away from 0 in all tested descent paths."""
        m_lex = fixture(2, 'lex')
        res = run_greedy_swap_descent(self.evaluator, m_lex['left_labels'], m_lex['right_labels'],
                                      max_steps=100, patience=100, rng_seed=99)
        # Even after 100 descent steps, BBo should be substantially above 0 (>= 1.0 s^6 = 4096)
        self.assertGreater(res['final_bbo'], 4096)


if __name__ == '__main__':
    unittest.main()
