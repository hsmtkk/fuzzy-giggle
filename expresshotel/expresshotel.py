import dataclasses
import sys


@dataclasses.dataclass
class Internship:
    begin: int
    end: int


@dataclasses.dataclass
class Problem:
    express_fee: int
    hotel_fee: int
    internship_days: list[Internship]


def solve(problem: Problem) -> int:
    total = 0
    for i in range(len(problem.internship_days) - 1):
        end = problem.internship_days[i].end
        begin = problem.internship_days[i + 1].begin
        duration = begin - end
        express_fee = 2 * problem.express_fee
        hotel_fee = duration * problem.hotel_fee
        total += min(express_fee, hotel_fee)
    return total + 2 * problem.express_fee


if __name__ == "__main__":
    lines = sys.stdin.readlines()
    first = lines[0].strip()
    elems = first.split(" ")
    express_fee = int(elems[0])
    hotel_fee = int(elems[1])
    internship_days = []
    for line in lines[1:]:
        line = line.strip()
        elems = line.split(" ")
        begin = int(elems[0])
        end = int(elems[1])
        internship_days.append(Internship(begin, end))
    problem = Problem(express_fee, hotel_fee, internship_days)
    answer = solve(problem)
    print(answer)
