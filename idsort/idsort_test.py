import unittest

import idsort


class TestIDSort(unittest.TestCase):
    def test1(self):
        problem = idsort.Problem(
            words=["paiza1", "kirishima813", "pizza99", "sushi100", "beef1001"]
        )
        want = idsort.Answer(
            words=["paiza1", "pizza99", "sushi100", "kirishima813", "beef1001"]
        )
        got = idsort.solve(problem)
        self.assertEqual(want, got)

    def test2(self):
        problem = idsort.Problem(words=["tanaka1192", "tanaka123", "tanaka95"])
        want = idsort.Answer(words=["tanaka95", "tanaka123", "tanaka1192"])
        got = idsort.solve(problem)
        self.assertEqual(want, got)


if __name__ == "__main__":
    unittest.main()
