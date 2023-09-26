import unittest

import tricktreat


class Test1(unittest.TestCase):
    def test1(self):
        p = tricktreat.Problem(6, 3, 2, [2, 4, 5])
        want = 2
        got = tricktreat.solve(p)
        self.assertEqual(want, got)

    def test2(self):
        p = tricktreat.Problem(10, 4, 3, [1, 5, 6, 9])
        want = 6
        got = tricktreat.solve(p)
        self.assertEqual(want, got)
