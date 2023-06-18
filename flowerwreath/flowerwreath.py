import dataclasses
import sys


@dataclasses.dataclass
class Problem:
    first: str
    second: str


def solve(problem: Problem) -> bool:
    patterns = rotate(problem.first)
    return problem.second in patterns


def rotate(orig: str) -> set[str]:
    result = set()
    s = orig
    for i in range(len(orig)):
        result.add(s)
        s = s[1:] + s[0]
    return result


if __name__ == "__main__":
    lines = sys.stdin.readlines()
    lines = list(map(lambda s: s.strip(), lines))
    problem = Problem(lines[1], lines[2])
    answer = solve(problem)
    if answer:
        print("Yes")
    else:
        print("No")
