def solution(n):
    answer = 0
    result = 0
    while n > 0:
        result = result * 10 + n % 3
        n //= 3

    i = 0
    while result > 0:
        answer += (result % 10) * (3 ** i)
        result //= 10
        i += 1

    return answer

# [참고]
# def solution(n):
#     tmp = ''
#     while n:
#         tmp += str(n % 3)
#         n = n // 3

#     answer = int(tmp, 3) --> 문자열 tmp를 3진법으로 바꿔줌
#     return answer
