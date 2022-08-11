from itertools import combinations


def solution(nums):
    answer = 0
    coms = list(combinations(nums, 3))
    for com in coms:
        sum_com = sum(list(com))
        if isPrime(sum_com):
            answer += 1

    return answer


def isPrime(n):
    cnt = 0
    for i in range(1, n + 1):
        if n % i == 0:
            cnt += 1
        if cnt > 2:
            break
    if cnt == 2:
        return True
    else:
        return False
