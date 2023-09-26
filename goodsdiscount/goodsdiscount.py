import dataclasses
import sys


@dataclasses.dataclass
class Problem:
    discount_number: int
    discount_rate: int
    price: int
    number: int


def solve(p: Problem) -> int:
    non_discounted_number = p.number % p.discount_number
    discounted_number = p.number - non_discounted_number
    discounted_price = p.price * (100 - p.discount_rate) // 100
    return discounted_number * discounted_price + non_discounted_number * p.price


def main():
    lines = sys.stdin.readlines()
    firsts = list(map(int, lines[0].strip().split(" ")))
    seconds = list(map(int, lines[1].strip().split(" ")))
    p = Problem(firsts[0], firsts[1], seconds[0], seconds[1])
    ans = solve(p)
    print(ans)


if __name__ == "__main__":
    main()
