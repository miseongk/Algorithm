def solution(lottos, win_nums):
    answer = [0] * 2
    cnt_0 = lottos.count(0)
    lottos = set(lottos)
    win_nums = set(win_nums)
    diff = 6 - len(win_nums - lottos)
    answer[0] = rank(diff + cnt_0)
    answer[1] = rank(diff)

    return answer


def rank(n):
    if n == 6:
        return 1
    elif n == 5:
        return 2
    elif n == 4:
        return 3
    elif n == 3:
        return 4
    elif n == 2:
        return 5
    else:
        return 6

# 조건문 대신 rank = [6, 6, 5, 4, 3, 2, 1] 로 간단하게 할 수 있음
