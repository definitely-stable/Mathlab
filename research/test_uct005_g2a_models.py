"""UCT-005 G2-A. Exact honest bit-cell probes; deliberately NO cryptographic soundness."""
from itertools import product
from math import ceil
import unittest


def parity(seq):
    out = 0
    for x in seq:
        out ^= x
    return out


def lowbit(i):
    return i & -i


class Raw:
    def __init__(self, values):
        self.bits = list(values)
        self.storage = len(values)

    def flip(self, i):
        self.bits[i - 1] ^= 1
        return (1, 1, 1)  # physical read, write, changed bit

    def prefix(self, t):
        return parity(self.bits[:t]), t


class Prefix:
    def __init__(self, values):
        self.n = len(values)
        self.bits = [parity(values[:i]) for i in range(1, self.n + 1)]
        self.storage = self.n

    def flip(self, i):
        for p in range(i - 1, self.n):
            self.bits[p] ^= 1
        return (self.n - i + 1,) * 3

    def prefix(self, t):
        return (self.bits[t - 1], 1) if t else (0, 0)


class Block:
    def __init__(self, values, width):
        assert 1 <= width <= len(values)
        self.width = width
        self.bits = list(values)
        self.blocks = [parity(values[j:j + width])
                       for j in range(0, len(values), width)]
        self.storage = len(values) + ceil(len(values) / width)

    def flip(self, i):
        self.bits[i - 1] ^= 1
        self.blocks[(i - 1) // self.width] ^= 1
        return (2, 2, 2)

    def prefix(self, t):
        full, part = divmod(t, self.width)
        result = parity(self.blocks[:full])
        result ^= parity(self.bits[full * self.width:full * self.width + part])
        return result, full + part


class Fenwick:
    def __init__(self, values):
        self.n = len(values)
        self.bit = [0] * (self.n + 1)
        self.storage = self.n
        for i, value in enumerate(values, 1):
            if value:
                self._toggle(i)

    def _toggle(self, i):
        cost = 0
        while i <= self.n:
            self.bit[i] ^= 1
            cost += 1
            i += lowbit(i)
        return cost

    def flip(self, i):
        count = self._toggle(i)
        return count, count, count

    def prefix(self, t):
        answer = 0
        probes = 0
        while t:
            answer ^= self.bit[t]
            t -= lowbit(t)
            probes += 1
        return answer, probes


class Fenwick2D:
    def __init__(self, n, cells):
        self.n = n
        self.cells = list(cells)
        self.bit = [[0] * (n + 1) for _ in range(n + 1)]
        for i, v in enumerate(cells):
            if v:
                self._toggle(i // n, i % n)

    def _toggle(self, row, col):
        cost = 0
        i = row + 1
        while i <= self.n:
            j = col + 1
            while j <= self.n:
                self.bit[i][j] ^= 1
                cost += 1
                j += lowbit(j)
            i += lowbit(i)
        return cost

    def flip(self, row, col):
        self.cells[row * self.n + col] ^= 1
        k = self._toggle(row, col)
        return k, k, k

    def prefix(self, row, col):  # half-open rows [0,row), columns [0,col)
        result = count = 0
        while row:
            col2 = col
            while col2:
                result ^= self.bit[row][col2]
                col2 -= lowbit(col2)
                count += 1
            row -= lowbit(row)
        return result, count

    def rectangle(self, r0, c0, r1, c1):
        result = probes = 0
        for x, y in ((r1, c1), (r0, c1), (r1, c0), (r0, c0)):
            value, reads = self.prefix(x, y)
            result ^= value
            probes += reads
        return result, probes


class Uct005G2AHonestModels(unittest.TestCase):
    def test_exhaustive_all_states_and_single_flips_1d(self):
        for n in range(1, 7):
            for values in product((0, 1), repeat=n):
                for i in range(1, n + 1):
                    oracle = list(values)
                    oracle[i - 1] ^= 1
                    models = [Raw(values), Prefix(values), Fenwick(values)]
                    models.extend(Block(values, b) for b in range(1, n + 1))
                    for model in models:
                        ur, uw, changed = model.flip(i)
                        self.assertEqual(uw, changed)  # flip model; not all updates!
                        if isinstance(model, Raw):
                            self.assertEqual((ur, uw, changed), (1, 1, 1))
                        if isinstance(model, Prefix):
                            self.assertEqual((ur, uw, changed), (n - i + 1,) * 3)
                        if isinstance(model, Block):
                            self.assertEqual((ur, uw, changed), (2, 2, 2))
                        for t in range(n + 1):
                            got, reads = model.prefix(t)
                            self.assertEqual(got, parity(oracle[:t]))
                            if isinstance(model, Raw):
                                self.assertEqual(reads, t)
                            if isinstance(model, Prefix):
                                self.assertEqual(reads, 1 if t else 0)
                            if isinstance(model, Block):
                                self.assertEqual(reads, t // model.width + t % model.width)
                            if isinstance(model, Fenwick):
                                self.assertEqual(reads, t.bit_count())

    def test_adaptive_transcripts_1d(self):
        for n in range(1, 18):
            raw = [0] * n
            models = [Raw(raw), Prefix(raw), Fenwick(raw),
                      Block(raw, max(1, n // 3))]
            for step in range(3 * n):
                i = 1 + (step * 5 + step // 3) % n
                raw[i - 1] ^= 1
                for model in models:
                    model.flip(i)
                    for t in range(n + 1):
                        self.assertEqual(model.prefix(t)[0], parity(raw[:t]))

    def test_2d_fenwick_against_all_small_rectangles(self):
        for n in (1, 2, 3):
            states = product((0, 1), repeat=n * n)
            for original in states:
                for row, col in product(range(n), repeat=2):
                    oracle = list(original)
                    oracle[row * n + col] ^= 1
                    fw = Fenwick2D(n, original)
                    rr, ww, changed = fw.flip(row, col)
                    self.assertEqual((rr, ww, changed), (ww,) * 3)
                    self.assertLessEqual(ww, (n.bit_length()) ** 2)
                    for r0 in range(n):
                        for r1 in range(r0 + 1, n + 1):
                            for c0 in range(n):
                                for c1 in range(c0 + 1, n + 1):
                                    expected = parity(
                                        oracle[r * n + c]
                                        for r in range(r0, r1)
                                        for c in range(c0, c1))
                                    result, count = fw.rectangle(r0, c0, r1, c1)
                                    self.assertEqual(result, expected)
                                    self.assertLessEqual(
                                        count, 4 * n.bit_length() ** 2)

    def test_w_times_p_fails_for_honest_dynamic_parity(self):
        n, k = 256, 8
        fw = Fenwick([0] * n)
        max_w = max(fw.flip(i)[2] for i in (1, 2, 3, 16, 128, 256))
        max_p = max(fw.prefix(t)[1] for t in range(n + 1))
        self.assertEqual(max_w, k + 1)
        self.assertEqual(max_p, k)
        self.assertLess(max_w * max_p, n)
        self.assertFalse(hasattr(fw, "verify"))  # Not an authenticated protocol.

if __name__ == "__main__":
    unittest.main()
