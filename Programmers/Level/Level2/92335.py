def solution(n, k):
    answer = 0
    if k != 10:
        convert_k = convert(n, k)
    else:
        convert_k = str(n)

    arr = convert_k.split('0')
    for n in arr:
        if n == '' or n == '1':
            continue
        if is_prime(int(n)):
            answer += 1

    return answer


# 10진수 -> k진수 변환 함수
def convert(n, k):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)

    return rev_base[::-1]


def is_prime(n):
    # n의 제곱근 까지만 판별한다 -> 제곱근을 기준으로 약수는 짝을 이루기 때문 (시간초과 방지)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
