import fractions
import unittest

import renbusu


class TestRenbusu(unittest.TestCase):
    def test1(self):
        want = fractions.Fraction(30, 13)
        got = renbusu.solve([2, 3, 4])
        self.assertEqual(want, got)

    def test2(self):
        want = fractions.Fraction(29, 12)
        got = renbusu.solve([2, 2, 2, 2])
        self.assertEqual(want, got)

    def test3(self):
        want = fractions.Fraction(11223788, 1100889)
        got = renbusu.solve([10, 5, 8, 7, 8, 9, 7, 7])
        self.assertEqual(want, got)
