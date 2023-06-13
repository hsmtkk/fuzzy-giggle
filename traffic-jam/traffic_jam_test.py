import unittest

import pydantic
import traffic_jam


@pydantic.dataclasses.dataclass
class TestCase:
    intervals: list[int]
    threshold: int
    want: int


class TestTrafficJam(unittest.TestCase):
    def test_calculate(self):
        test_cases = [
            TestCase(intervals=[5, 6, 25, 4], threshold=10, want=15),
            TestCase(intervals=[30, 10, 40], threshold=30, want=40),
        ]
        for test_case in test_cases:
            got = traffic_jam.calculate(test_case.intervals, test_case.threshold)
            self.assertEqual(test_case.want, got)


if __name__ == "__main__":
    unittest.main()
