def solution(left, right):
    answer = 0
    for n in range(left, right + 1):
        cnt = divisiorCnt(n)
        if cnt % 2 == 0:
            answer += n
        else:
            answer -= n

    return answer


def divisiorCnt(n):
    cnt = 0
    for i in range(1, n + 1):
        if n % i == 0:
            cnt += 1

    return cnt

# [참고] - 제곱수의 약수는 홀수개...👍
# def solution(left, right):
#     answer = 0
#     for i in range(left,right+1):
#         if int(i**0.5)==i**0.5:
#             answer -= i
#         else:
#             answer += i
#     return answer
