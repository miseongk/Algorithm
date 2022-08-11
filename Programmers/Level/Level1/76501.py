def solution(absolutes, signs):
    answer = 0
    for pair in zip(absolutes, signs):
        if pair[1] == False:
            answer += -pair[0]
            # answer -= pair[0]
        else:
            answer += pair[0]
    return answer
