def solution(numbers):
    answer = -1
    num = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    diff = list(num - set(numbers))
    answer = sum(diff)

    return answer
