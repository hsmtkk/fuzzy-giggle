import unittest

import thunderarea


class TestThunderArea(unittest.TestCase):
    def test1(self):
        thunder_counts = [
            [3, 4, 6, 2, 4, 6],
            [3, 5, 1, 3, 5, 3],
            [5, 1, 3, 6, 6, 4],
            [7, 8, 3, 2, 2, 2],
            [5, 9, 3, 2, 2, 2],
            [7, 2, 4, 2, 2, 2],
        ]
        p = thunderarea.Problem(6, 6, thunder_counts)
        got = thunderarea.solve(p)
        want = thunderarea.Answer([[3, 4], [5, 2]])
        self.assertEqual(want, got)

    def test2(self):
        thunder_counts = [
            [55, 66, 3],
            [1, 35, 36],
            [55, 3, 2],
            [3, 53, 77],
            [46, 46, 14],
            [31, 3, 5],
        ]
        p = thunderarea.Problem(6, 3, thunder_counts)
        got = thunderarea.solve(p)
        want = thunderarea.Answer([[28], [30]])
        self.assertEqual(want, got)
