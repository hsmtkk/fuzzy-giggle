import unittest

import jobactivity


class TestJobActivity(unittest.TestCase):
    def test1(self):
        days = [1, 2, 4, 5, 6, 9, 10, 11, 13]
        want = (4, 6)
        got = jobactivity.solve(days)
        self.assertEqual(want, got)

    def test2(self):
        days = [2, 4, 6]
        want = (2, 2)
        got = jobactivity.solve(days)
        self.assertEqual(want, got)
