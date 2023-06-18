import dataclasses
import sys


@dataclasses.dataclass
class Problem:
    members: list[int]
    turns: list[tuple[int, int, int]]


@dataclasses.dataclass
class Answer:
    beans: list[int]


def solve(problem: Problem) -> Answer:
    beans = [0 for _ in problem.members]
    for turn in problem.turns:
        for i in range(turn[0] - 1, turn[1]):
            beans[i] += turn[2]
            if problem.members[i] < beans[i]:
                beans[i] = problem.members[i]
    return Answer(beans=beans)


if __name__ == "__main__":
    lines = sys.stdin.readlines()
    count = int(lines[0])
    members = list(map(int, lines[1 : 1 + count]))
    turns = list()
    for line in lines[2 + count :]:
        line = line.strip()
        elems = list(map(int, line.split(" ")))
        turns.append((elems[0], elems[1], elems[2]))
    answer = solve(Problem(members=members, turns=turns))
    for a in answer.beans:
        print(a)
