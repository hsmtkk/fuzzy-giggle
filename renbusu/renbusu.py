import fractions
import sys


def solve(xs: list[int]) -> fractions.Fraction:
    return calc_an(xs, 0)


def calc_an(xs: list[int], n: int) -> fractions.Fraction:
    if n == len(xs) - 1:
        ans = fractions.Fraction(xs[n], 1)
        return ans
    else:
        anplus1 = calc_an(xs, n + 1)
        ans = xs[n] + 1 / anplus1
        return ans


if __name__ == "__main__":
    lines = sys.stdin.readlines()
    lines = list(map(lambda s: s.strip(), lines))
    nums = list(map(lambda s: int(s), lines))
    ans = solve(nums[1:])
    print(f"{ans.numerator} {ans.denominator}")
