def solution(n, lost, reserve):
    intersection = set(lost) & set(reserve)
    answer = n - len(lost) + len(intersection)
    lost = list(set(lost) - intersection)
    reserve = list(set(reserve) - intersection)

    for l in lost:
        if l in reserve:
            answer += 1
            del reserve[reserve.index(l)]
            continue
        if l - 1 in reserve:
            answer += 1
            del reserve[reserve.index(l - 1)]
        elif l + 1 in reserve:
            answer += 1
            del reserve[reserve.index(l + 1)]

    return answer
