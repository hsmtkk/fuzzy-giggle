import unittest

import restaurantpopular


class TestRestaurantPopular(unittest.TestCase):
    def test1(self):
        rank_calories = [
            (11, 100),
            (1, 120),
            (2, 200),
            (3, 200),
            (4, 500),
            (5, 800),
            (6, 10),
            (7, 123),
            (8, 900),
            (9, 3000),
            (10, 2),
            (12, 7000),
        ]
        inp = restaurantpopular.Input(9000, rank_calories)
        want = True
        got = restaurantpopular.solve(inp)
        self.assertEqual(want, got)

    def test2(self):
        rank_calories = [
            (1, 1500),
            (2, 300),
            (4, 100),
            (12, 500),
            (10, 10),
            (9, 10),
            (8, 10),
            (7, 5),
            (6, 10),
            (5, 20),
            (11, 10000),
            (3, 100),
        ]
        inp = restaurantpopular.Input(2000, rank_calories)
        want = 3
        got = restaurantpopular.solve(inp)
        self.assertEqual(want, got)
