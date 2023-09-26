import unittest

import sticktest


class TestStick(unittest.TestCase):
    def test1(self):
        p = sticktest.Problem(3, [True, False, True, True, True])
        want = True
        got = sticktest.solve(p)
        self.assertEqual(want, got)

    def test2(self):
        p = sticktest.Problem(3, [True, False, False, False, False, True])
        want = False
        got = sticktest.solve(p)
        self.assertEqual(want, got)
