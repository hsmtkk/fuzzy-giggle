import dataclasses
import re
import sys


@dataclasses.dataclass
class Problem:
    words: list[str]


@dataclasses.dataclass
class Answer:
    words: list[str]


def solve(p: Problem) -> Answer:
    ans = list(sorted(p.words, key=sorter))
    return Answer(words=ans)


PATTERN = re.compile(r"[a-z]+([0-9]+)")


def sorter(s: str) -> int:
    matched = PATTERN.match(s)
    if matched is None:
        raise
    key = matched.group(1)
    return int(key)


if __name__ == "__main__":
    lines = sys.stdin.readlines()
    words = list(map(lambda s: s.strip(), lines[1:]))
    problem = Problem(words=words)
    answer = solve(problem)
    for w in answer.words:
        print(w)
