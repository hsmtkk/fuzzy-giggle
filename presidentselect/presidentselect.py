import collections
import dataclasses


@dataclasses.dataclass
class Input:
    name_vote: list[tuple[str, int]]


@dataclasses.dataclass
class Output:
    presidents: tuple[str, str]


def solve(inp: Input) -> Output:
    first_counter = collections.Counter()
    second_dict = dict()
    for name, vote in inp.name_vote:
        first_counter[name] += 1
        votes = second_dict.get(name, 0)
        votes += vote
        second_dict[name] = votes
    first = first_counter.most_common(1)[0][0]
    second = inp.name_vote[0][0]
    max_vote = 0
    for name, vote in second_dict.items():
        if vote > max_vote:
            second = name
            max_vote = vote
    return Output((first, second))
