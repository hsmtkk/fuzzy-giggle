import unittest

import jet_lag


class TestJetLag(unittest.TestCase):
    def test1(self) -> None:
        records: list[jet_lag.Record] = [
            jet_lag.Record(7, 5, 12),
            jet_lag.Record(10, 6, 20),
            jet_lag.Record(12, 3, 8),
        ]
        want = jet_lag.Answer(20, 31)
        got = jet_lag.solve(records)
        self.assertEqual(want, got)

    def test2(self) -> None:
        records: list[jet_lag.Record] = [
            jet_lag.Record(1, 1, 23),
            jet_lag.Record(23, 1, 1),
        ]
        want = jet_lag.Answer(3, 47)
        got = jet_lag.solve(records)
        self.assertEqual(want, got)

    def test3(self) -> None:
        records: list[jet_lag.Record] = [
            jet_lag.Record(5, 4, 20),
        ]
        want = jet_lag.Answer(13, 13)
        got = jet_lag.solve(records)
        self.assertEqual(want, got)


if __name__ == "__main__":
    unittest.main()
