import dataclasses
import sys


@dataclasses.dataclass
class Answer:
    diet: int
    no_diet: int


def solve(weights: list[int]) -> Answer:
    diet = 0
    no_diet = 0
    up = 0
    down = 0
    for i in range(len(weights) - 1):
        this = weights[i]
        next = weights[i + 1]
        if this < next:
            up += 1
            if down > diet:
                diet = down
            down = 0
        else:
            down += 1
            if up > no_diet:
                no_diet = up
            up = 0
    if down > diet:
        diet = down
    if up > no_diet:
        no_diet = up
    return Answer(diet, no_diet)


if __name__ == "__main__":
    lines = sys.stdin.readlines()
    weights = list(map(int, lines[1:]))
    ans = solve(weights)
    print(ans.diet, ans.no_diet)
