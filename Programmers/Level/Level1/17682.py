def solution(dartResult):
    answer = 0
    result = []
    flag = 0
    j = -1
    for i in dartResult:
        if i >= '0' and i <= '9':
            if flag == 1:
                result[j] = int(result[j]) * 10 + int(i)
            else:
                flag = 1
                result.append(int(i))
                j += 1
        elif i == 'S':
            flag = 0
            continue
        elif i == 'D':
            flag = 0
            result[j] **= 2
        elif i == 'T':
            flag = 0
            result[j] **= 3
        elif i == '*':
            flag = 0
            result[j] *= 2
            if j - 1 >= 0:
                result[j-1] *= 2
        elif i == '#':
            flag = 0
            result[j] *= (-1)

    return sum(result)
