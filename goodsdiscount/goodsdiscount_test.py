import unittest

import goodsdiscount


class TestGoodsDiscount(unittest.TestCase):
    def test1(self):
        p = goodsdiscount.Problem(4, 60, 100, 10)
        want = 520
        got = goodsdiscount.solve(p)
        self.assertEqual(want, got)

    def test2(self):
        p = goodsdiscount.Problem(4, 10, 8, 5)
        want = 36
        got = goodsdiscount.solve(p)
        self.assertEqual(want, got)
