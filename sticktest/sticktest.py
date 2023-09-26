import dataclasses
import sys


@dataclasses.dataclass
class Problem:
    span: int
    hit_or_miss: list[bool]


def solve(p: Problem) -> bool:
    for i in range(len(p.hit_or_miss) - p.span + 1):
        sticks = p.hit_or_miss[i : i + p.span]
        if not any(sticks):
            return False
    return True


def int_to_bool(n: int) -> bool:
    if n == 0:
        return False
    else:
        return True


if __name__ == "__main__":
    lines = sys.stdin.readlines()
    first_nums = list(map(int, lines[0].strip().split(" ")))
    second_nums = list(map(int, lines[1].strip().split(" ")))
    sticks = list(map(int_to_bool, second_nums))
    p = Problem(first_nums[1], sticks)
    ans = solve(p)
    if ans:
        print("OK")
    else:
        print("NG")
