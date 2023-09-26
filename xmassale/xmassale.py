import dataclasses
import sys


@dataclasses.dataclass
class Input:
    threshold: int
    free: int
    prices: list[int]


def solve(input: Input) -> int:
    if len(input.prices) < input.threshold:
        return sum(input.prices)
    sorted_prices = list(reversed(sorted(input.prices)))
    non_free_counts = len(input.prices) - input.free
    return sum(sorted_prices[:non_free_counts])


if __name__ == "__main__":
    lines = sys.stdin.readlines()
    elems = lines[0].split(" ")
    nums = list(map(int, elems))
    price_strs = lines[1:]
    prices = list(map(int, price_strs))
    input = Input(nums[1], nums[2], prices)
    total = solve(input)
    print(total)
