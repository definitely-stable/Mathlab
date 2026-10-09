"""UCT-004 G2-C: exact finite nonlinear parity proof-cover oracle.

Standalone stdlib search over p-coordinate distinguishability and minimum
set cover. It tests, but does NOT prove, the general n-parameter conjecture.
"""
from functools import lru_cache
from itertools import combinations
from math import ceil, log2
import unittest


def parity(x):
    return x.bit_count() & 1


def candidate_projection_masks(n, p):
    return tuple(mask for mask in range(1, 1 << n)
                 if mask.bit_count() <= p)


def admissible_for_class(H, good, wrong, projections):
    """Actual x values H, not bit-mask coding of selected good elements."""
    return all(any(all((x & mask) != (y & mask) for x in H)
                   for mask in projections) for y in wrong)


@lru_cache(maxsize=None)
def finite_cover_oracle(n, p):
    assert 1 <= p <= n <= 5
    good = tuple(x for x in range(1 << n) if parity(x) == 0)
    wrong = tuple(x for x in range(1 << n) if parity(x) == 1)
    probes = candidate_projection_masks(n, p)
    universe = (1 << len(good)) - 1

    # For each false input and each proposed local test S, encode which
    # honest states that test CAN distinguish from that false input.
    admissible_mask_choices = []
    for y in wrong:
        candidates = []
        for S in probes:
            mask = 0
            for i, x in enumerate(good):
                if (x & S) != (y & S):
                    mask |= 1 << i
            candidates.append(mask)
        admissible_mask_choices.append(tuple(candidates))

    def is_admissible(H):
        for masks_for_y in admissible_mask_choices:
            if not any(H & candidate == H for candidate in masks_for_y):
                return False
        return True

    allowed = tuple(H for H in range(1, universe + 1)
                    if is_admissible(H))
    ordered = sorted(allowed, key=lambda x: x.bit_count(), reverse=True)
    maximal = []
    for H in ordered:
        if not any((H & M) == H for M in maximal):
            maximal.append(H)
    maximum = ordered[0].bit_count() if ordered else 0

    # Exact set cover, independently from rank, using a tight integer bound
    # and an MRV (minimum remaining values) branching order. All maximal
    # admissible sets are sufficient because admissibility is downward closed.
    by_coordinate = {
        i: tuple(M for M in maximal if M & (1 << i))
        for i in range(len(good))
    }

    def find_k_cover(uncovered, k):
        if uncovered == 0:
            return ()
        if k == 0:
            return None
        if uncovered.bit_count() > k * maximum:
            return None
        uncovered_indices = (i for i in range(len(good))
                             if uncovered & (1 << i))
        pivot = min(uncovered_indices,
                    key=lambda i: len(by_coordinate[i]))
        for M in by_coordinate[pivot]:
            next_uncovered = uncovered & ~M
            answer = find_k_cover(next_uncovered, k - 1)
            if answer is not None:
                return (M,) + answer
        return None

    selected = None
    covering_number = None
    expected_upper = 1 << (ceil(n/p) - 1)
    for k in range(1, expected_upper + 1):
        solution = find_k_cover(universe, k)
        if solution is not None:
            covering_number, selected = k, solution
            break
    assert covering_number is not None

    # Independently check existence and full coverage, without trusting
    # the searcher's running uncovered mask.
    covered = 0
    for H in selected:
        assert is_admissible(H)
        covered |= H
    assert covered == universe
    assert len(selected) == covering_number
    return {
        "n": n, "p": p,
        "good": good, "wrong": wrong,
        "all_admissible_count": len(allowed),
        "maximal_count": len(maximal),
        "max_fiber": maximum,
        "min_cover": covering_number,
        "cover": tuple(tuple(good[i] for i in range(len(good))
                             if H & (1 << i)) for H in selected),
    }


class Uct004NonlinearCoverTests(unittest.TestCase):
    EXPECTED = {
        (2, 1): (2, 1),
        (3, 1): (4, 1), (3, 2): (2, 2),
        (4, 1): (8, 1), (4, 2): (2, 4), (4, 3): (2, 6),
        (5, 1): (16, 1), (5, 2): (4, 4),
        (5, 3): (2, 8), (5, 4): (2, 12),
    }

    def test_exact_all_small_n_p_cover_numbers_and_max_fibers(self):
        for (n, p), (min_cover, max_fiber) in self.EXPECTED.items():
            with self.subTest(n=n, p=p):
                found = finite_cover_oracle(n, p)
                self.assertEqual(found["min_cover"], min_cover)
                self.assertEqual(found["max_fiber"], max_fiber)
                self.assertEqual(min_cover, 1 << (ceil(n/p)-1))
                self.assertEqual(ceil(log2(min_cover)), ceil(n/p)-1)
                self.assertEqual(len(found["cover"]), min_cover)

    def test_every_reported_cover_fiber_separates_all_wrong_inputs(self):
        for n, p in self.EXPECTED:
            result = finite_cover_oracle(n, p)
            projections = candidate_projection_masks(n, p)
            for H in result["cover"]:
                self.assertTrue(admissible_for_class(
                    H, result["good"], result["wrong"], projections))
            self.assertEqual(set(x for H in result["cover"] for x in H),
                             set(result["good"]))

    def test_both_parities_have_identical_cover_structure(self):
        # Translating by e0 preserves the p-projection relation.
        for n in range(2, 5):
            for p in range(1, n):
                result = finite_cover_oracle(n, p)
                shifted = [tuple(x ^ 1 for x in H)
                           for H in result["cover"]]
                projections = candidate_projection_masks(n, p)
                odd = tuple(x for x in range(1 << n) if parity(x))
                even = tuple(x for x in range(1 << n) if not parity(x))
                self.assertEqual(set(x for H in shifted for x in H),
                                 set(odd))
                for H in shifted:
                    self.assertTrue(admissible_for_class(
                        H, odd, even, projections))

    def test_weight_two_nonaffine_fiber_has_six_elements(self):
        n, p = 4, 3
        H = tuple(x for x in range(1 << n) if x.bit_count() == 2)
        self.assertEqual(len(H), 6)
        self.assertGreater(len(H), 1 << (n - ceil(n/p)))
        self.assertTrue(admissible_for_class(
            H, (), (1, 2, 4, 7, 8, 11, 13, 14),
            candidate_projection_masks(n, p)))

    def test_full_parity_class_not_admissible_when_p_less_than_n(self):
        for n in range(2, 6):
            even = tuple(x for x in range(1 << n) if parity(x) == 0)
            odd = tuple(x for x in range(1 << n) if parity(x) == 1)
            for p in range(1, n):
                self.assertFalse(admissible_for_class(
                    even, even, odd, candidate_projection_masks(n, p)))

    def test_full_probe_needs_no_witness(self):
        for n in range(1, 6):
            result = finite_cover_oracle(n, n)
            self.assertEqual(result["min_cover"], 1)
            self.assertEqual(result["max_fiber"], 1 << (n-1))


if __name__ == "__main__":
    unittest.main()
