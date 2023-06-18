import unittest

import setubunrobot


class TestSetubunRobot(unittest.TestCase):
    def test1(self):
        problem = setubunrobot.Problem(
            members=[10, 20, 30, 40, 50], turns=[(2, 4, 10), (1, 3, 15)]
        )
        want = setubunrobot.Answer(beans=[10, 20, 25, 10, 0])
        got = setubunrobot.solve(problem)
        self.assertEqual(want, got)

    def test2(self):
        problem = setubunrobot.Problem(members=[3, 1, 4], turns=[(1, 1, 2)])
        want = setubunrobot.Answer(beans=[2, 0, 0])
        got = setubunrobot.solve(problem)
        self.assertEqual(want, got)


if __name__ == "__main__":
    unittest.main()
