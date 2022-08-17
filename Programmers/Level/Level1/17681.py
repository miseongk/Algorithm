def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        str1 = binary(arr1[i], n)
        str2 = binary(arr2[i], n)

        result = ""
        for j in range(n):
            if str1[j] == 1 or str2[j] == 1:
                result += "#"
            else:
                result += ' '
        answer.append(result)

    return answer


def binary(num, n):
    str = [0] * n
    for i in range(n - 1, 0, -1):
        if num < 0:
            break
        if num % 2 == 1:
            str[i] = 1
        num //= 2
        if num < 2:
            str[i - 1] = num

    return str

# [참고]
# def solution(n, arr1, arr2):
#     answer = []
#     for i,j in zip(arr1,arr2):
#         a12 = str(bin(i|j)[2:]) -> bin() 은 이진수로 변환해주는 함수
#         a12 = a12.rjust(n,'0') -> 오른쪽으로 밀기 (n자리 숫자, 공백은 '0'으로 채우기)
#         a12 = a12.replace('1','#')
#         a12 = a12.replace('0',' ')
#         answer.append(a12)
#     return answer
