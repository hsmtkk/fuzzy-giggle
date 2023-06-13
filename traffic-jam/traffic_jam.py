import sys


def calculate(intervals: list[int], threshold: int) -> int:
    sum = 0
    for interval in intervals:
        if interval <= threshold:
            sum += interval
    return sum


def run():
    lines = sys.stdin.readlines()
    threshold = int(lines[0].split(" ")[1])
    intervals = map(lambda line: int(line), lines[1:])
    sum = calculate(intervals, threshold)
    print(sum)


if __name__ == "__main__":
    run()
