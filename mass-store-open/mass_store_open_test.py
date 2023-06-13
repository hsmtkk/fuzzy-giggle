import unittest

import mass_store_open


class TestSolve(unittest.TestCase):
    def test1(self):
        p = mass_store_open.Problem(1000, 1000, 50, 3, [25, 500, 80])
        self.assertEqual(1, mass_store_open.solve(p))

    def test2(self):
        p = mass_store_open.Problem(2556, 3424, 77, 3, [137, 721, 984, 999])
        self.assertEqual(1, mass_store_open.solve(p))


if __name__ == "__main__":
    unittest.main()
