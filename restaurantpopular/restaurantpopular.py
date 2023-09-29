import dataclasses
import sys


@dataclasses.dataclass
class Input:
    calory_threshold: int
    rank_calories: list[tuple[int, int]]


def solve(inp: Input) -> bool | int:
    menus = list(range(1, 11))
    total_calories = 0
    cleared = 0
    for rank, calory in inp.rank_calories:
        total_calories += calory
        if total_calories >= inp.calory_threshold:
            return cleared
        cleared += 1
        if rank in menus:
            menus.remove(rank)
        if len(menus) == 0:
            break
    return True


if __name__ == "__main__":
    lines = sys.stdin.readlines()
    first_nums = list(map(int, lines[0].strip().split(" ")))
    calory_threshold = first_nums[1]
    rank_calories = []
    for line in lines[1:]:
        nums = list(map(int, line.strip().split(" ")))
        rank = nums[0]
        calory = nums[1]
        rank_calories.append((rank, calory))
    inp = Input(calory_threshold, rank_calories)
    ans = solve(inp)
    if type(ans) == type(True) and ans:
        print("Yes")
    else:
        print(ans)
