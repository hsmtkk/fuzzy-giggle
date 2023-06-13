import dataclasses
import sys


@dataclasses.dataclass
class Problem:
    words: list[str]


@dataclasses.dataclass
class Answer:
    chained: bool
    last: str | None = None
    first: str | None = None


def solve(problem: Problem) -> Answer:
    for i in range(len(problem.words) - 1):
        word = problem.words[i]
        next_word = problem.words[i + 1]
        last = last_char(word)
        first = first_char(next_word)
        if last != first:
            return Answer(chained=False, last=last, first=first)
    return Answer(chained=True)


def last_char(word: str) -> str:
    return word[len(word) - 1]


def first_char(word: str) -> str:
    return word[0]


if __name__ == "__main__":
    lines = sys.stdin.readlines()
    words = list(map(lambda s: s.strip(), lines[1:]))
    answer = solve(Problem(words))
    if answer.chained:
        print("Yes")
    else:
        print(f"{answer.last} {answer.first}")
