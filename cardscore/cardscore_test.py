import unittest

import cardscore


class TestSort(unittest.TestCase):
    def test1(self):
        cards = [5, 10, 11, 12, 24, 25]
        want = [[5], [10, 11, 12], [24, 25]]
        got = cardscore.sort(cards)
        self.assertEqual(want, got)

    def test2(self):
        cards = [5, 1, 9, 10, 2]
        want = [[1, 2], [5], [9, 10]]
        got = cardscore.sort(cards)
        self.assertEqual(want, got)


class TestCount(unittest.TestCase):
    def test1(self):
        sorted = [[5], [10, 11, 12], [24, 25]]
        want = 42
        got = cardscore.count(sorted)
        self.assertEqual(want, got)

    def test2(self):
        sorted = [[1, 2], [5], [9, 10]]
        want = 17
        got = cardscore.count(sorted)
        self.assertEqual(want, got)
