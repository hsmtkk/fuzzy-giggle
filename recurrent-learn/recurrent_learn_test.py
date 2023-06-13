import unittest

import recurrent_learn


class TestRecurrentLearn(unittest.TestCase):
    def test1(self):
        correct_or_nots = [
            recurrent_learn.CorrectOrNot(first=True, second=False),
            recurrent_learn.CorrectOrNot(first=False, second=True),
            recurrent_learn.CorrectOrNot(first=False, second=False),
            recurrent_learn.CorrectOrNot(first=True, second=True),
        ]
        want = [1, 2, 3]
        got = recurrent_learn.problems_to_be_solved(correct_or_nots)
        self.assertEqual(want, got)

    def test2(self):
        correct_or_nots = [recurrent_learn.CorrectOrNot(first=True, second=True)]
        want = []
        got = recurrent_learn.problems_to_be_solved(correct_or_nots)
        self.assertEqual(want, got)


if __name__ == "__main__":
    unittest.main()
