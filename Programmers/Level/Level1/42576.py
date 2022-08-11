def solution(participant, completion):
    answer = ''
    dict_p = {}
    dict_c = {}
    for p in participant:
        if p not in dict_p:
            dict_p[p] = 0
        dict_p[p] += 1
    for c in completion:
        if c not in dict_c:
            dict_c[c] = 0
        dict_c[c] += 1

    for p in dict_p:
        for _ in range(dict_p[p]):
            if p in dict_c:
                if dict_c[p] > 0:
                    dict_p[p] -= 1
                    dict_c[p] -= 1

    for p in dict_p:
        if dict_p[p] > 0:
            answer += p
            break

    return answer

# [참고]
# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
#     for i in range(len(completion)):
#         if participant[i] != completion[i]:
#             return participant[i]
#     return participant[-1]