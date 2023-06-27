import unittest

import factorycheck


class TestFactoryCheck(unittest.TestCase):
    def test1(self):
        expected = [1, 2, 1, 2, 3]
        input = [2, 1, 3, 2, 1]
        got = factorycheck.solve(expected, input)
        self.assertTrue(got)

    def test2(self):
        expected = [3, 1, 4]
        input = [1, 5, 2]
        got = factorycheck.solve(expected, input)
        self.assertFalse(got)


if __name__ == "__main__":
    unittest.main()
