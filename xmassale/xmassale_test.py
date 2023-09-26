import unittest

import xmassale


class TestXmasSale(unittest.TestCase):
    def test1(self):
        prices = [500, 300, 400, 200, 100]
        input = xmassale.Input(3, 1, prices)
        want = 1400
        got = xmassale.solve(input)
        self.assertEqual(want, got)

    def test2(self):
        prices = [400, 300, 200]
        input = xmassale.Input(5, 5, prices)
        want = 900
        got = xmassale.solve(input)
        self.assertEqual(want, got)
