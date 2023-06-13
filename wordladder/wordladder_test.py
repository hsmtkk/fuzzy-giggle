import unittest

import wordladder


class TestWordLadder(unittest.TestCase):
    def test1(self) -> None:
        words = ["apPle", "error", "suBway", "Zb"]
        problem = wordladder.Problem(words)
        want = wordladder.Answer(chained=False, last="r", first="s")
        got = wordladder.solve(problem)
        self.assertEqual(want, got)

    def test2(self) -> None:
        words = ["idIOh", "hiKoQA", "AbijoD", "djgeldi", "kjoial"]
        problem = wordladder.Problem(words)
        want = wordladder.Answer(chained=False, last="D", first="d")
        got = wordladder.solve(problem)
        self.assertEqual(want, got)

    def test3(self) -> None:
        words = ["adijA", "Akq", "qZR"]
        problem = wordladder.Problem(words)
        want = wordladder.Answer(chained=True)
        got = wordladder.solve(problem)
        self.assertEqual(want, got)


if __name__ == "__main__":
    unittest.main()
