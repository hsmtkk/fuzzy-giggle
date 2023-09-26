import sys


def sort(cards: list[int]) -> list[list[int]]:
    cards = sorted(cards)
    result: list[list[int]] = []
    inner: list[int] = [cards[0]]
    for i in range(1, len(cards)):
        n = cards[i]
        if inner[-1] + 1 == n:
            inner.append(n)
        else:
            result.append(inner)
            inner = [n]
    result.append(inner)
    return result


def count(cards: list[list[int]]) -> int:
    sum = 0
    for ns in cards:
        sum += ns[-1]
    return sum


if __name__ == "__main__":
    lines = sys.stdin.readlines()
    elems = lines[1].strip().split(" ")
    nums = list(map(lambda s: int(s), elems))
    print(count(sort(nums)))
