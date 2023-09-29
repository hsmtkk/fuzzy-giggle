import dataclasses
import sys


@dataclasses.dataclass
class Problem:
    row: int
    column: int
    thunder_counts: list[list[int]]


@dataclasses.dataclass
class Answer:
    average_counts: list[list[int]]


def calc_average(
    thunder_counts: list[list[int]], block_row: int, block_column: int
) -> int:
    sum = 0
    for r in range(3 * block_row, 3 * block_row + 3):
        for c in range(3 * block_column, 3 * block_column + 3):
            sum += thunder_counts[r][c]
    return sum // 9


def solve(p: Problem) -> Answer:
    block_row = p.row // 3
    block_column = p.column // 3
    average_counts = []
    for br in range(block_row):
        line: list[int] = []
        for bc in range(block_column):
            ave = calc_average(p.thunder_counts, br, bc)
            line.append(ave)
        average_counts.append(line)
    return Answer(average_counts)


def main():
    lines = sys.stdin.readlines()
    nums = list(map(int, lines[0].strip().split(" ")))
    row = nums[0]
    column = nums[1]
    thunder_counts = []
    for line in lines[1:]:
        nums = list(map(int, line.strip().split(" ")))
        thunder_counts.append(nums)
    p = Problem(row, column, thunder_counts)
    ans = solve(p)
    for row in ans.average_counts:
        ss = list(map(str, row))
        print(" ".join(ss))


if __name__ == "__main__":
    main()
