def solution(targets):
    answer = 1
    targets.sort()
    s = targets[0][0]
    e = targets[0][1]
    for i in range(1, len(targets)):
        current = targets[i]
        # 포함되는 경우
        if s <= current[0] < e and current[1] <= e:
            e = current[1]
            s = current[0]
        # 걸치는 경우
        elif s <= current[0] < e and current[1] > e:
            s = current[0]
        # 넘어가는 경우
        elif current[0] >= e:
            answer += 1
            s = current[0]
            e = current[1]

    return answer
