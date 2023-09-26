import unittest

import dietrecord


class TestDietRecord(unittest.TestCase):
    def test0(self):
        weights = [55, 56, 57, 55, 56, 53, 52, 50]
        want = dietrecord.Answer(3, 2)
        got = dietrecord.solve(weights)
        self.assertEqual(want, got)
