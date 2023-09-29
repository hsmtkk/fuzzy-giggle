import sys


def solve(days: list[int]) -> tuple[int, int]:
    begin = 0
    end = 0
    max_span = 0
    for d in days:
        span = 1
        while d + span in days:
            span += 1
        if span > max_span:
            max_span = span
            begin = d
            end = d + span - 1
    return (begin, end)


if __name__ == "__main__":
    lines = sys.stdin.readlines()
    days = list()
    for line in lines[1:]:
        line = line.strip()
        num = int(line)
        days.append(num)
    ans = solve(days)
    print(f"{ans[0]} {ans[1]}")
