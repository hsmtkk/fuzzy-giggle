import sys

from pydantic.dataclasses import dataclass


@dataclass
class CorrectOrNot:
    first: bool
    second: bool


def problems_to_be_solved(correct_or_nots: list[CorrectOrNot]) -> list[int]:
    problems: list[int] = list()
    for i, correct_or_not in enumerate(correct_or_nots):
        if not correct_or_not.first or not correct_or_not.second:
            problems.append(i + 1)
    return problems


def parse_line(line: str) -> CorrectOrNot:
    line = line.strip()
    elems = line.split(" ")
    correct_or_not = CorrectOrNot(first=True, second=True)
    if elems[0] == "n":
        correct_or_not.first = False
    if elems[1] == "n":
        correct_or_not.second = False
    return correct_or_not


def run():
    lines = sys.stdin.readlines()
    correct_or_nots = list(map(parse_line, lines[1:]))
    print(correct_or_nots)
    problems = problems_to_be_solved(correct_or_nots)
    if len(problems) == 0:
        print(0)
    else:
        print(len(problems))
        for p in problems:
            print(p)


if __name__ == "__main__":
    run()
