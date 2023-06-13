import sys


def solve(begin: int, end: int) -> int:
    count = 0
    for n in range(begin, end + 1):
        if rotated_same(n):
            count += 1
    return count


def rotated_same(n: int) -> bool:
    ns: list[int] = [int(x) for x in str(n)]
    ns.reverse()
    if not convertible(ns):
        return False
    ss: list[str] = list(map(convert, ns))
    m: int = int("".join(ss))
    return m == n


def convertible(ns: list[int]) -> bool:
    if 2 in ns or 3 in ns or 4 in ns or 5 in ns or 7 in ns:
        return False
    return True


convert_dict = {
    0: "0",
    1: "1",
    6: "9",
    8: "8",
    9: "6",
}


def convert(n: int) -> str:
    return convert_dict[n]


def run():
    lines = sys.stdin.readlines()
    first_line = lines[0].strip()
    begin, end = map(lambda s: int(s), first_line.split(" "))
    count = solve(begin, end)
    print(count)


if __name__ == "__main__":
    run()
