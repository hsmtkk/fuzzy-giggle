import unittest

import presidentselect


class TestPresidentSelect(unittest.TestCase):
    def test1(self):
        inp = presidentselect.Input(
            [("john", 1), ("john", 5), ("alex", 40), ("john", 4)]
        )
        want = presidentselect.Output(("john", "alex"))
        got = presidentselect.solve(inp)
        self.assertEqual(want, got)

    def test2(self):
        inp = presidentselect.Input([("smith", 675), ("smith", 694)])
        want = presidentselect.Output(("smith", "smith"))
        got = presidentselect.solve(inp)
        self.assertEqual(want, got)
