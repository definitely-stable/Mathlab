"""Independent exhaustive oracles for TOM-006's frozen toy COPY/ADD model.

The oracle generates *actual* instruction sequences with exact source offsets;
it does not derive solutions from the q-window lower-bound inequalities.
"""
import itertools
import unittest

from tom006_floor import absent_windows, optimistic_floor


def all_parses(base, target, position=0):
    """Yield all instruction parses, including noncanonical split ADDs."""
    if position == len(target):
        yield ()
        return
    remaining = len(target) - position
    for length in range(1, remaining + 1):
        for tail in all_parses(base, target, position + length):
            yield (("ADD", target[position:position + length]),) + tail
    for offset in range(len(base)):
        for length in range(1, min(remaining, len(base) - offset) + 1):
            if target[position:position + length] != base[offset:offset + length]:
                continue
            for tail in all_parses(base, target, position + length):
                yield (("COPY", offset, length),) + tail


def inspect_parse(base, target, parse):
    """Return actual flat price, L, C, A, J, and literal byte positions."""
    output = bytearray()
    literal_positions = set()
    copy_boundaries = set()
    last_command = None
    literal_bytes = 0
    copies = 0
    price = 0
    for command in parse:
        kind = command[0]
        if kind == "ADD":
            payload = command[1]
            assert payload
            literal_positions.update(range(len(output), len(output) + len(payload)))
            output.extend(payload)
            literal_bytes += len(payload)
            price += 1 + len(payload)
        else:
            _, offset, length = command
            assert length > 0 and 0 <= offset and offset + length <= len(base)
            if last_command == "COPY":
                copy_boundaries.add(len(output))
            output.extend(base[offset:offset + length])
            price += 2
            copies += 1
        last_command = kind
    assert bytes(output) == target
    regions = sum(i == 0 or i - 1 not in literal_positions
                  for i in literal_positions)
    return price, literal_bytes, copies, regions, len(copy_boundaries), literal_positions


def missing_positions(base, target, q):
    if len(target) < q:
        return []
    return [i for i in range(len(target) - q + 1)
            if all(target[i:i + q] != base[j:j + q]
                   for j in range(max(len(base) - q + 1, 0)))]


def packing_number(starts, q):
    best = 0
    for flags in itertools.product((False, True), repeat=len(starts)):
        chosen = [i for i, on in zip(starts, flags) if on]
        if all(y >= x + q for x, y in zip(chosen, chosen[1:])):
            best = max(best, len(chosen))
    return best


def exact_dp(base, target):
    """Independent shortest-path oracle, enumerating source offsets."""
    n = len(target)
    dp = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        answers = [1 + length + dp[i + length]
                   for length in range(1, n - i + 1)]
        for offset in range(len(base)):
            for length in range(1, min(n - i, len(base) - offset) + 1):
                if target[i:i + length] == base[offset:offset + length]:
                    answers.append(2 + dp[i + length])
        dp[i] = min(answers)
    return dp[0]


class Tom006ShortKillGate(unittest.TestCase):
    def check_pair(self, base, target):
        parsed = list(all_parses(base, target))
        self.assertTrue(parsed)
        true_optimum = min(inspect_parse(base, target, p)[0] for p in parsed)
        self.assertEqual(exact_dp(base, target), true_optimum)
        for q in range(1, len(target) + 2):
            starts = missing_positions(base, target, q)
            self.assertEqual(absent_windows(base, target, q), len(starts))
            disjoint = packing_number(starts, q)
            for parse in parsed:
                _, literals, copies, regions, joins, _ = inspect_parse(
                    base, target, parse)
                self.assertLessEqual(
                    len(starts), q * literals + (q - 1) * max(copies - 1, 0))
                self.assertLessEqual(
                    len(starts), literals + (q - 1) * (regions + joins))
                self.assertLessEqual(disjoint, literals + joins)
        for qmax in range(1, min(len(target) + 1, 4) + 1):
            floor = optimistic_floor(base, target, qmax)
            self.assertLessEqual(floor, true_optimum)
            for known_best in range(true_optimum + 3):
                if floor >= known_best:
                    self.assertGreaterEqual(true_optimum, known_best)

    def test_all_small_binary(self):
        words = [bytes(items)
                 for size in range(5)
                 for items in itertools.product((0, 1), repeat=size)]
        for base in words:
            for target in words:
                with self.subTest(base=base, target=target):
                    self.check_pair(base, target)

    def test_all_small_ternary(self):
        words = [bytes(items)
                 for size in range(4)
                 for items in itertools.product((0, 1, 2), repeat=size)]
        for base in words:
            for target in words:
                with self.subTest(base=base, target=target):
                    self.check_pair(base, target)

    def test_unbounded_fixed_short_q_weakness(self):
        for width in (2, 3, 4, 8, 16, 32):
            base = b"a" * width + b"bb" + b"a" * width
            target = b"ab" * width
            self.assertEqual(absent_windows(base, target, 1), 0)
            self.assertEqual(absent_windows(base, target, 2), 0)
            self.assertEqual(optimistic_floor(base, target, 2), 2)
            self.assertEqual(exact_dp(base, target), 2 * width)

    def test_fail_closed_invalid_inputs(self):
        with self.assertRaises(ValueError):
            absent_windows(b"b", b"b", 0)
        with self.assertRaises(TypeError):
            absent_windows("a", b"a", 1)
        for kwargs in ({"max_q": 0}, {"add_charge": 0},
                       {"copy_charge": -1}):
            with self.assertRaises(ValueError):
                optimistic_floor(b"ab", b"ab", **kwargs)


if __name__ == "__main__":
    unittest.main()
