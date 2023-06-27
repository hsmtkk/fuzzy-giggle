import sys


def solve(expected: list[int], input: list[int]) -> bool:
    counter: dict[int, int] = dict()
    for n in input:
        count = counter.get(n, 0)
        counter[n] = count + 1
    for n in expected:
        count = counter.get(n, 0)
        if count == 0:
            return False
        counter[n] = count - 1
    return True


if __name__ == "__main__":
    lines = sys.stdin.readlines()
    stripped_lines = map(lambda s: s.strip(), lines[1:])
    nums = list(map(lambda s: int(s), stripped_lines))
    expected = nums[: len(nums) // 2]
    input = nums[len(nums) // 2 :]
    answer = solve(expected, input)
    if answer:
        print("Yes")
    else:
        print("No")
