def solution(N, stages):
    answer = []
    dic = {}
    for stage in range(1, N+1):
        if (dic.get(stage, -1) == -1):
            cur = stages.count(stage)
            n = len(list(filter(lambda x: x>= stage, stages)))
            if n == 0:
                dic[stage] = 0
            else:
                dic[stage] = cur / n
        else:
            continue

    sort_dict = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))
    answer = list(sort_dict.keys())
    return answer

# [참고]
# def solution(N, stages):
#     answer = []
#     dic = {}
#     stage_len = len(stages)
#     for stage in range(1, N + 1):
#         if stage_len != 0:
#             if dic.get(stage, -1) == -1:
#                 cur = stages.count(stage)
#                 dic[stage] = cur / stage_len
#                 stage_len -= cur
#         else:
#             dic[stage] = 0
#
#     sort_dict = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))
#     answer = list(sort_dict.keys())
#     return answer
