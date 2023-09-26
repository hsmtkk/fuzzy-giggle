import dataclasses
import sys


@dataclasses.dataclass
class Problem:
    n: int
    m: int
    k: int
    boys: list


def solve(p: Problem) -> int:
    surprised = 0
    treat = 0
    for i in range(1, p.n + 1):
        if i in p.boys:
            surprised += 1
            if surprised >= p.k:
                break
        else:
            surprised = 0
            treat += 1
    return treat


if __name__ == "__main__":
    lines = sys.stdin.readlines()
    boys = []
    for line in lines[1:]:
        s = line.strip()
        boys.append(int(s))
    first_line = lines[0].strip()
    nums = list(map(int, first_line.split(" ")))
    p = Problem(nums[0], nums[1], nums[2], boys)
    answer = solve(p)
    print(answer)
