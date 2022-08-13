def solution(d, budget):
    answer = 0
    d.sort()
    i = 0
    sum = 0
    while i < len(d):
        sum += d[i]
        if sum > budget:
            break
        elif sum == budget:
            answer += 1
            break
        answer += 1
        i += 1

    return answer
