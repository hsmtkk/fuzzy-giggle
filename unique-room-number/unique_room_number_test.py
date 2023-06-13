import unittest

import unique_room_number


class TestUniqueRoomNumber(unittest.TestCase):
    def test1(self):
        want = 2
        got = unique_room_number.solve(1, 9)
        self.assertEqual(want, got)

    def test2(self):
        want = 32
        got = unique_room_number.solve(100, 10000)
        self.assertEqual(want, got)


if __name__ == "__main__":
    unittest.main()
