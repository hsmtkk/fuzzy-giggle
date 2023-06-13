import sys

from pydantic import PositiveInt
from pydantic.dataclasses import dataclass


@dataclass
class Record:
    departure: PositiveInt
    flight: PositiveInt
    arrival: PositiveInt


@dataclass
class Answer:
    min: PositiveInt
    max: PositiveInt


def solve(records: list[Record]) -> Answer:
    hours = []
    for record in records:
        hours.append(record.departure + record.flight + (24 - record.arrival))
    return Answer(min=min(hours), max=max(hours))


def parse_lines(lines: list[str]) -> list[Record]:
    records: list[Record] = list()
    for line in lines:
        line = line.strip()
        digits: list[int] = list(map(int, line.split(" ")))
        records.append(Record(digits[0], digits[1], digits[2]))
    return records


if __name__ == "__main__":
    lines = sys.stdin.readlines()
    records: list[Record] = parse_lines(lines[1:])
    answer = solve(records)
    print(answer.min)
    print(answer.max)
