from itertools import combinations


def solution(numbers):
    answer = []
    coms = list(combinations(numbers, 2))
    result = set()

    for com in coms:
        result.add(com[0] + com[1])
    answer = list(result)
    answer.sort()

    return answer
