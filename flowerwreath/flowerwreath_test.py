import unittest

import flowerwreath


class TestFlowerWreath(unittest.TestCase):
    def test1(self):
        problem = flowerwreath.Problem("baaab", "aabba")
        self.assertTrue(flowerwreath.solve(problem))

    def test2(self):
        problem = flowerwreath.Problem("baaab", "abaab")
        self.assertFalse(flowerwreath.solve(problem))


class TestRotate(unittest.TestCase):
    def test1(self):
        got = flowerwreath.rotate("baaab")
        want = {"baaab", "aaabb", "aabba", "abbaa", "bbaaa"}
        self.assertEqual(want, got)


if __name__ == "__main__":
    unittest.main()
