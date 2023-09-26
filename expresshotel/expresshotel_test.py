import unittest

import expresshotel


class TestExpressHotel(unittest.TestCase):
    def test1(self):
        days = [
            expresshotel.Internship(1, 3),
            expresshotel.Internship(4, 6),
            expresshotel.Internship(8, 10),
        ]
        p = expresshotel.Problem(200, 300, days)
        want = 1100
        got = expresshotel.solve(p)
        self.assertEqual(want, got)
