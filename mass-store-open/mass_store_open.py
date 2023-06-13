import dataclasses


@dataclasses.dataclass
class Problem:
    construct_fee: int
    human_fee: int
    profit: int
    month: int
    amounts: list[int]


def solve(problem: Problem) -> int:
    sum = 0
    for amount in problem.amounts:
        profit = (
            problem.profit * amount
            - problem.construct_fee
            - problem.human_fee * problem.month
        )
        if profit < 0:
            sum += 1
    return sum
